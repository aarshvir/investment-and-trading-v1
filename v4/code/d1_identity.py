"""d1_identity.py - resolve fja membership spells to companies (CIK), names and at-the-time tickers.

Pipeline
 A. Evidence per spell: Wikipedia month-end snapshot rows linked by ticker (d1_snaplink), the current Wikipedia
    table (current spells), SEC company_tickers (current ticker -> CIK; plain Norgate keys are 2019 tickers),
    Wikipedia change-table rows at the spell's start/end (same ticker +-20d, or same date +-5d).
 B. CIK candidates (Wikipedia CIK column 2014+, current table, SEC ticker, exact normalised-name matches in SEC
    cik-lookup-data) verified with SEC submissions: >=1 10-K/10-Q/20-F/40-F filed inside the spell window
    ([start-120d, end+200d]); name similarity vs all SEC names (current + former).
 C. Direct ticker links whose Wikipedia name contradicts every known name of the spell are unlinked (e.g. 2007-08
    'WM' = Washington Mutual, not Waste Management whose Norgate symbol is its 2019 ticker WM).
 D. Gated co-occurrence pairing of unmatched months (a spell may pair with several Wikipedia tickers in disjoint
    periods, e.g. SPGI <- MHP then MHFI). Gate: name similarity >= 0.34, or change-table evidence (the Wikipedia
    ticker was removed/added on the spell's end/start date +-5d), or ticker similarity with Jaccard >= 0.8.
 E. Evidence and candidates are recomputed with paired months; CIK segments are assigned per spell (primary CIK
    covering the spell end; predecessor CIKs when the primary's filings start after the spell start).
 F. Segment boundaries where a CIK changes are classified as holding-company reorganisation/redomicile (same
    entity) or ticker reuse (different company) - see classify_boundary().
Outputs (cache): id_evidence.pkl, id_candidates.pkl, id_pairs.csv, id_link_month.parquet, id_segments.parquet
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from d1_common import CACHE
from d1_sec_ref import (company_tickers, name_candidates, fuzzy_candidates, norm1, submissions_summary, token_sim)
from d1_snaplink import tkey, SUFFIX_RE, month_end

LAST = "2026-09-25"
EDGAR_START = "1996-06-01"


# ------------------------------------------------------------------------------------------------ helpers
def _ok(x) -> bool:
    return isinstance(x, str) and bool(x.strip())


def _cik_ok(x) -> bool:
    try:
        return x is not None and not pd.isna(x)
    except (TypeError, ValueError):
        return True


def spell_months(start: str, end) -> list[str]:
    e = end if _ok(end) else "9999-12-31"
    out = []
    for p in pd.period_range(max(start[:7], "2007-03"), "2026-09", freq="M"):
        me = month_end(str(p))
        if start <= me < e:
            out.append(str(p))
    return out


def best_name_sim(names_a, names_b) -> float:
    best = 0.0
    for a in names_a:
        if not _ok(a):
            continue
        na = norm1(a)
        for b in names_b:
            if not _ok(b):
                continue
            nb = norm1(b)
            if not na or not nb:
                continue
            if na == nb or na.replace(" ", "") == nb.replace(" ", ""):
                return 1.0
            s = token_sim(a, b)
            if nb.startswith(na + " ") or na.startswith(nb + " "):
                s = max(s, 0.8)
            # squashed containment for short brand names ("CBRE" vs "CB RICHARD ELLIS" does not qualify)
            best = max(best, s)
    return best


def ticker_sim(key_ticker: str, wiki_ticker: str) -> bool:
    a, b = tkey(key_ticker), tkey(wiki_ticker)
    a2 = re.sub(r"Q+$", "", a) if len(a) >= 4 else a
    for x in {a, a2}:
        if len(x) >= 2 and len(b) >= 2 and (x.startswith(b) or b.startswith(x)):
            return True
        cp = 0
        for c1, c2 in zip(x, b):
            if c1 != c2:
                break
            cp += 1
        if cp >= 3:
            return True
    return False


def add_days(d: str, n: int) -> str:
    return (pd.Timestamp(d) + pd.Timedelta(days=n)).strftime("%Y-%m-%d")


class Sec:
    """cached SEC submissions summaries (parallel prefetch, global <=3.5 req/s limiter in d1_common)"""

    def __init__(self):
        self.summ = {}

    def get(self, cik: int, need_from: str | None = None) -> dict | None:
        cik = int(cik)
        key = (cik, need_from[:4] if need_from else None)
        if key not in self.summ:
            try:
                self.summ[key] = submissions_summary(cik, need_from=need_from)
            except Exception as e:  # network or parse error -> treat as unavailable, logged
                print("SEC error", cik, e)
                self.summ[key] = None
        return self.summ[key]

    def prefetch(self, reqs: list[tuple[int, str | None]], workers: int = 4):
        todo = [(int(c), n) for c, n in set(reqs) if (int(c), n[:4] if n else None) not in self.summ]
        if not todo:
            return
        print(f"SEC prefetch {len(todo)} summaries", flush=True)
        with ThreadPoolExecutor(max_workers=workers) as ex:
            res = list(ex.map(lambda a: (a, self._fetch(*a)), todo))
        for (c, n), s in res:
            self.summ[(c, n[:4] if n else None)] = s

    @staticmethod
    def _fetch(c, n):
        try:
            return submissions_summary(c, need_from=n)
        except Exception as e:
            print("SEC error", c, e)
            return None

    def names(self, cik) -> list[str]:
        s = self.get(cik)
        if not s:
            return []
        return [x for x in [s["name"]] + [f.get("name") for f in s.get("formerNames", [])] if _ok(x)]


# ------------------------------------------------------------------------------------------------ inputs
def load_inputs():
    sp = pd.read_parquet(CACHE / "fja_spells.parquet")
    sp["end"] = pd.Series([x if _ok(x) else None for x in sp["end"]], dtype=object)
    sp["spell_id"] = sp["key"] + "#" + sp["spell_no"].astype(int).astype(str)
    L = pd.read_parquet(CACHE / "snaplink_month.parquet")
    W = pd.read_parquet(CACHE / "snaplink_wiki_unmatched.parquet")
    cur = pd.read_parquet(CACHE / "wiki_current.parquet")
    ch = pd.read_parquet(CACHE / "wiki_changes.parquet")
    ch["add_tk"] = [tkey(x) if _ok(x) else None for x in ch["add_ticker"]]
    ch["rem_tk"] = [tkey(x) if _ok(x) else None for x in ch["rem_ticker"]]
    ch["dt"] = pd.to_datetime(ch["date"])
    # attach spell ids to month links
    lookup = defaultdict(list)
    for r in sp.itertuples():
        lookup[r.key].append((r.start, r.end or "9999-12-31", r.spell_id))

    def sid_for(key, m):
        me = month_end(m)
        for s, e, sid in lookup[key]:
            if s <= me < e:
                return sid
        return None

    L["spell_id"] = [sid_for(k, m) for k, m in zip(L.key, L.month)]
    return sp, L, W, cur, ch


# ------------------------------------------------------------------------------------------------ A. evidence
def build_evidence(sp, L, cur, ch):
    ct = company_tickers()
    ct_by_t = ct.groupby(ct["ticker"].map(tkey))["cik"].apply(lambda s: sorted(set(int(x) for x in s))).to_dict()
    cur_by_t = {tkey(r.symbol): r for r in cur.itertuples()}
    Lm = L[L.link.isin(["ticker", "paired"])]
    lk = {k: g for k, g in Lm.groupby("spell_id")}
    ev = {}
    for r in sp.itertuples():
        g = lk.get(r.spell_id)
        rows = g if g is not None else Lm.iloc[0:0]
        names = Counter(x for x in rows.wiki_name if _ok(x))
        ciks_m = defaultdict(list)
        for m, c in zip(rows.month, rows.wiki_cik):
            if _cik_ok(c):
                ciks_m[int(c)].append(m)
        tickers_m = defaultdict(list)
        for m, t in zip(rows.month, rows.wiki_ticker):
            if _ok(t):
                tickers_m[t].append(m)
        tk = tkey(r.ticker)
        cur_row = cur_by_t.get(tk) if r.end is None else None
        s0 = pd.Timestamp(r.start)
        near_start = ch[abs(ch.dt - s0) <= pd.Timedelta(days=5)]
        add_same_t = ch[(ch.add_tk == tk) & (abs(ch.dt - s0) <= pd.Timedelta(days=20))]
        if r.end:
            e0 = pd.Timestamp(r.end)
            near_end = ch[abs(ch.dt - e0) <= pd.Timedelta(days=5)]
            rem_same_t = ch[(ch.rem_tk == tk) & (abs(ch.dt - e0) <= pd.Timedelta(days=20))]
        else:
            near_end = rem_same_t = ch.iloc[0:0]
        sec_t = ct_by_t.get(tk, []) if (not SUFFIX_RE.search(r.key)) or r.end is None else []
        ev[r.spell_id] = {
            "spell_id": r.spell_id, "key": r.key, "start": r.start, "end": r.end, "ticker": r.ticker,
            "suffixed": bool(SUFFIX_RE.search(r.key)),
            "wiki_names": dict(names), "wiki_ciks_months": {c: sorted(v) for c, v in ciks_m.items()},
            "wiki_tickers_months": {t: sorted(v) for t, v in tickers_m.items()},
            "cur_cik": int(cur_row.cik) if cur_row is not None and _cik_ok(cur_row.cik) else None,
            "cur_name": cur_row.security if cur_row is not None else None,
            "sec_ticker_ciks": sec_t,
            "chg_add_same_t": [(d, n) for d, n in zip(add_same_t.date, add_same_t.add_name)],
            "chg_rem_same_t": [(d, n, rs) for d, n, rs in zip(rem_same_t.date, rem_same_t.rem_name, rem_same_t.reason)],
            "chg_add_tk_near_start": sorted(set(x for x in near_start.add_tk if _ok(x))),
            "chg_rem_tk_near_end": sorted(set(x for x in near_end.rem_tk if _ok(x))),
            "chg_rem_names_near_end": {t: n for t, n in zip(near_end.rem_tk, near_end.rem_name) if _ok(t)},
            "chg_add_names_near_start": {t: n for t, n in zip(near_start.add_tk, near_start.add_name) if _ok(t)},
        }
    return ev


def evidence_names(e) -> list[str]:
    nm = [n for n, _ in sorted(e["wiki_names"].items(), key=lambda kv: -kv[1])]
    if _ok(e["cur_name"]):
        nm.append(e["cur_name"])
    nm += [n for _, n in e["chg_add_same_t"] if _ok(n)]
    nm += [n for _, n, _ in e["chg_rem_same_t"] if _ok(n)]
    return list(dict.fromkeys(x for x in nm if _ok(x)))


# ------------------------------------------------------------------------------------------------ B. candidates
def window(e) -> tuple[str, str]:
    s = max(e["start"], EDGAR_START)
    en = e["end"] or LAST
    return add_days(s, -120), add_days(en, 200)


def hyp_name(e):
    from d1_manual import NAME_HYPOTHESES
    return NAME_HYPOTHESES.get(e["key"])


def delist_date(e):
    m = SUFFIX_RE.search(e["key"])
    return f"{m.group(1)[:4]}-{m.group(1)[4:]}-15" if m else None


def gen_candidates(e, use_names: bool, same_key_ciks: set, sec: "Sec") -> dict:
    c = defaultdict(lambda: {"src": set()})
    for k in e["wiki_ciks_months"]:
        c[k]["src"].add("wiki_snapshot_cik")
    if e["cur_cik"]:
        c[e["cur_cik"]]["src"].add("wiki_current_cik")
    for k in e["sec_ticker_ciks"]:
        c[k]["src"].add("sec_ticker")
    for k in same_key_ciks:
        c[k]["src"].add("same_norgate_key")
    if use_names:
        search = [(n, "name") for n in evidence_names(e)[:6]]
        for k in e["sec_ticker_ciks"]:
            search += [(n, "name_of_ticker_holder") for n in sec.names(k)[:3]]
        h = hyp_name(e)
        if h:
            search.append((h, "analyst_hypothesis"))
        for nm, why in search:
            for ck, sim, secnm in fuzzy_candidates(nm, top=8, min_sim=0.75):
                c[ck]["src"].add(why)
    return c


def evaluate(e, cands: dict, sec: Sec) -> dict:
    ws, we = window(e)
    names = evidence_names(e)
    h = hyp_name(e)
    dl = delist_date(e)
    out = {}
    for k, info in cands.items():
        s = sec.get(k, need_from=ws)
        if s is None:
            out[k] = {**info, "exists": False, "reports_in": 0, "name_sim": 0.0, "hyp_sim": 0.0, "verified": False}
            continue
        reps = [x for x in s["report_dates"] if ws <= x <= we]
        sec_names = [s["name"]] + [f.get("name") for f in s.get("formerNames", [])]
        ns = best_name_sim(names, sec_names) if names else 0.0
        hs = best_name_sim([h], sec_names) if h else 0.0
        tick_in = tkey(e["ticker"]) in {tkey(t) for t in (s.get("tickers") or [])}
        stop_ok = None
        if dl and s["last_report"]:
            stop_ok = add_days(dl, -550) <= s["last_report"] <= add_days(dl, 460)
        out[k] = {**info, "exists": True, "plain_key": not e["suffixed"], "sec_name": s["name"], "reports_in": len(reps),
                  "first_report": s["first_report"], "last_report": s["last_report"],
                  "oldest_loaded": s["oldest_loaded"], "name_sim": round(ns, 3), "hyp_sim": round(hs, 3),
                  "ticker_in_sec": tick_in, "stop_near_delist": stop_ok, "verified": len(reps) >= 1}
    return out


def score(info: dict, e) -> float:
    src = info["src"]
    sc = 0.0
    sc += 3.0 if "wiki_current_cik" in src else 0
    if "wiki_snapshot_cik" in src:
        n = len(e["wiki_ciks_months"].get(info.get("cik"), [])) if info.get("cik") else 0
        tot = sum(len(v) for v in e["wiki_ciks_months"].values()) or 1
        sc += 1.0 + 2.0 * n / tot
    sc += 1.5 if "sec_ticker" in src else 0
    sc += 1.0 if "same_norgate_key" in src else 0
    sc += 1.0 if ("name" in src or "name_of_ticker_holder" in src) else 0
    sc += 2.0 * info.get("name_sim", 0) + 1.5 * info.get("hyp_sim", 0)
    sc += 0.5 if info.get("ticker_in_sec") else 0
    if info.get("stop_near_delist") is not None:
        sc += 1.0 if info["stop_near_delist"] else -1.0
    sc += 1.0 + 0.1 * min(info.get("reports_in", 0), 10) if info.get("verified") else -3.0
    return round(sc, 3)


def confidence(v: dict) -> str:
    """high / medium / low for a chosen CIK (see report for definitions)"""
    src = v["src"]
    ver = v.get("verified")
    strong = src & {"wiki_current_cik", "wiki_snapshot_cik", "sec_ticker", "same_norgate_key"}
    ns, hs = v.get("name_sim", 0), v.get("hyp_sim", 0)
    if ver and strong and ns >= 0.5:
        return "high"
    if ver and len(strong) >= 2 and ({"wiki_current_cik", "wiki_snapshot_cik"} & strong):
        return "high"     # independent sources agree (Wikipedia CIK column + SEC ticker table) + filings verified
    if ver and "name" in src and ns >= 0.8:
        return "high"     # Wikipedia-name exact/fuzzy match + filings in window
    if ver and (ns >= 0.3 or (strong and ns >= 0.2)):
        return "medium"
    if ver and hs >= 0.8:
        return "medium"   # analyst hypothesis confirmed by SEC name + 10-K/10-Q inside the membership window
    if ver and v.get("plain_key") and "sec_ticker" in strong:
        return "medium"   # Norgate 2019 symbol = current SEC ticker holder, filings cover the window
    if (not ver) and strong and ns >= 0.8:
        return "medium"   # e.g. banks reporting to FDIC/Fed: CIK exists, name agrees, no 10-K/10-Q on EDGAR
    return "low"


def candidates_all(ev: dict, sec: Sec) -> dict:
    # CIKs seen for other spells of the same Norgate key (same security) from wiki/current sources
    key_ciks = defaultdict(set)
    for sid, e in ev.items():
        key_ciks[e["key"]] |= set(e["wiki_ciks_months"]) | ({e["cur_cik"]} if e["cur_cik"] else set())
    same = {sid: key_ciks[e["key"]] - set(e["wiki_ciks_months"]) - ({e["cur_cik"]} if e["cur_cik"] else set())
            for sid, e in ev.items()}
    base = {sid: gen_candidates(e, False, same[sid], sec) for sid, e in ev.items()}
    sec.prefetch([(k, window(ev[sid])[0]) for sid, c in base.items() for k in c])
    res, need_names = {}, []
    for sid, e in ev.items():
        r = evaluate(e, base[sid], sec)
        res[sid] = r
        good = [k for k, v in r.items() if v["verified"] and v["name_sim"] >= 0.5]
        if not good:
            need_names.append(sid)
    # sec.names() of ticker holders need their submissions -> already prefetched in round 1
    extra = {sid: gen_candidates(ev[sid], True, same[sid], sec) for sid in need_names}
    sec.prefetch([(k, window(ev[sid])[0]) for sid, c in extra.items() for k in c])
    for sid in need_names:
        res[sid] = evaluate(ev[sid], extra[sid], sec)
    for sid, r in res.items():
        for k, v in r.items():
            v["cik"] = k
            v["score"] = score(v, ev[sid])
            v["confidence"] = confidence(v)
    return res


# ------------------------------------------------------------------------------------------------ C. conflicts
def known_names(e, cands: dict, sec: Sec) -> list[str]:
    nm = evidence_names(e)
    if hyp_name(e):
        nm.append(hyp_name(e))
    for k, v in cands.items():
        if v.get("confidence") in ("high", "medium"):
            nm += sec.names(k)
    return list(dict.fromkeys(nm))


def unlink_conflicts(L, ev, cands, sec: Sec):
    """a direct ticker link whose Wikipedia name matches none of the spell's other evidence is a ticker-reuse
    artefact of Norgate's 2019 symbols -> unlink (month becomes unmatched on both sides)."""
    L = L.copy()
    unlinked = []
    for sid, g in L[L.link == "ticker"].groupby("spell_id"):
        e = ev[sid]
        # reference names: SEC names of verified high-scoring candidates + current name
        ref = []
        top = sorted(cands[sid].values(), key=lambda v: -v["score"])[:2]
        for v in top:
            if v.get("verified"):
                ref += sec.names(v["cik"])
        if _ok(e["cur_name"]):
            ref.append(e["cur_name"])
        if not ref:
            continue
        wn = Counter(x for x in g.wiki_name if _ok(x))
        for name, cnt in wn.items():
            sim = best_name_sim([name], ref)
            if sim < 0.2:
                # keep if the same name is also the dominant name overall (renamed company w/o SEC former name)
                share = cnt / max(1, sum(wn.values()))
                if share >= 0.5:
                    continue
                idx = g.index[g.wiki_name == name]
                unlinked.append({"spell_id": sid, "wiki_name": name, "months": len(idx),
                                 "first": g.loc[idx, "month"].min(), "last": g.loc[idx, "month"].max(),
                                 "ref_names": "; ".join(ref[:3])})
                L.loc[idx, "link"] = "conflict"
    return L, pd.DataFrame(unlinked)


# ------------------------------------------------------------------------------------------------ D. pairing
def pair_unmatched(sp, L, W, ev, cands, sec: Sec):
    L = L.copy()
    # wiki rows available for pairing: originally unmatched + rows unlinked as conflicts
    conf = L[L.link == "conflict"]
    Wc = pd.DataFrame({"month": conf.month, "wiki_ticker": conf.wiki_ticker, "tk": conf.wiki_ticker.map(tkey),
                       "wiki_name": conf.wiki_name, "wiki_cik": conf.wiki_cik, "wiki_sector": conf.wiki_sector})
    L.loc[conf.index, ["wiki_ticker", "wiki_name", "wiki_cik", "wiki_sector"]] = [None, None, pd.NA, None]
    L.loc[conf.index, "link"] = "unmatched"
    W2 = pd.concat([W[["month", "wiki_ticker", "tk", "wiki_name", "wiki_cik", "wiki_sector"]], Wc], ignore_index=True)
    un = L[L.link == "unmatched"]
    A = un.groupby("spell_id")["month"].apply(set).to_dict()
    B = W2.groupby("tk")["month"].apply(set).to_dict()
    Wnames = W2.groupby("tk")["wiki_name"].apply(lambda s: list(dict.fromkeys(x for x in s if _ok(x)))).to_dict()
    Wciks = W2.groupby("tk")["wiki_cik"].apply(lambda s: sorted(set(int(x) for x in s if _cik_ok(x)))).to_dict()
    Wtick = W2.groupby("tk")["wiki_ticker"].first().to_dict()
    rows = []
    for sid, ma in A.items():
        e = ev[sid]
        kn = None
        for t, mb in B.items():
            inter = ma & mb
            if len(inter) < 2:
                continue
            # overlap relative to either side (a wiki ticker may span several fja spells and vice versa)
            cont = max(len(inter) / len(mb), len(inter) / len(ma))
            jac = len(inter) / len(ma | mb)
            if cont < 0.8:
                continue
            if kn is None:
                kn = known_names(e, cands[sid], sec)
            wn = Wnames.get(t, []) + [n for c in Wciks.get(t, []) for n in sec.names(c)]
            ns = best_name_sim(kn, wn)
            ts = ticker_sim(e["ticker"], Wtick[t])
            chg = (t in e["chg_rem_tk_near_end"]) or (t in e["chg_add_tk_near_start"])
            ok = ns >= 0.34 or chg or (ts and jac >= 0.8)
            rows.append({"spell_id": sid, "wiki_tk": t, "wiki_ticker": Wtick[t], "common": len(inter),
                         "containment": round(cont, 3), "jaccard": round(jac, 3), "name_sim": round(ns, 3),
                         "ticker_sim": ts, "chg_evidence": chg, "accepted": ok,
                         "key_names": "; ".join(kn[:4]), "wiki_names": "; ".join(Wnames.get(t, [])[:3]),
                         "months": sorted(inter)})
    C = pd.DataFrame(rows)
    if len(C) == 0:
        return C, L
    C["score"] = C.jaccard + C.name_sim + 0.5 * C.chg_evidence + 0.3 * C.ticker_sim + 0.002 * C.common
    C = C.sort_values("score", ascending=False).reset_index(drop=True)
    taken_s = defaultdict(set)   # spell -> months already paired
    taken_t = defaultdict(set)   # wiki tk -> months already paired
    chosen = []
    for i, r in C[C.accepted].iterrows():
        ms = set(r.months)
        if ms & taken_s[r.spell_id] or ms & taken_t[r.wiki_tk]:
            continue
        taken_s[r.spell_id] |= ms
        taken_t[r.wiki_tk] |= ms
        chosen.append(i)
    C["chosen"] = C.index.isin(chosen)
    Wi = {(m, t): row for m, t, row in zip(W2.month, W2.tk, W2.itertuples())}
    assign = {}
    for r in C[C.chosen].itertuples():
        for m in r.months:
            assign[(r.spell_id, m)] = r.wiki_tk
    for i, r in L[L.link == "unmatched"].iterrows():
        t = assign.get((r.spell_id, r.month))
        if t and (r.month, t) in Wi:
            w = Wi[(r.month, t)]
            L.loc[i, ["wiki_ticker", "wiki_name", "wiki_cik", "wiki_sector", "link"]] = \
                [w.wiki_ticker, w.wiki_name, w.wiki_cik, w.wiki_sector, "paired"]
    # wiki rows left unmatched
    used = set((m, t) for (sid, m), t in assign.items())
    W2["paired"] = [(m, t) in used for m, t in zip(W2.month, W2.tk)]
    return C.drop(columns=["months"]), L, W2


# ------------------------------------------------------------------------------------------------ E/F. segments
def first_filing_date(sec: Sec, cik: int, forms=("8-K12B", "8-K12G3", "10-12B", "10-12G")) -> str | None:
    from d1_common import get_submissions
    d = get_submissions(cik)
    if not d:
        return None
    rec = d.get("filings", {}).get("recent", {})
    dates = [dd for f, dd in zip(rec.get("form", []), rec.get("filingDate", [])) if f in forms]
    return min(dates) if dates else None


def assign_segments(sp, ev, cands, sec: Sec):
    segs = []
    for r in sp.itertuples():
        sid = r.spell_id
        e = ev[sid]
        c = cands.get(sid, {})
        rank = {"high": 2, "medium": 1, "low": 0}
        ver = {k: v for k, v in c.items() if v.get("verified") or v.get("confidence") in ("high", "medium")}
        if not ver:
            best = max(c.values(), key=lambda v: v["score"]) if c else None
            segs.append({"spell_id": sid, "seg": 1, "from": r.start, "to": r.end, "cik": None,
                         "cik_unverified_best": best["cik"] if best else None, "confidence": "none",
                         "method": "none", "score": best["score"] if best else None})
            continue
        # primary = best-confidence candidate covering the end of the spell, then best score
        end = r.end or LAST
        wstart = max(r.start, EDGAR_START)

        def covers_end(v):
            return (not v.get("last_report")) or v["last_report"] >= add_days(end, -550)

        def covers_start(v):
            return bool(v.get("first_report")) and v["first_report"] <= add_days(wstart, 400)

        def chainable(v):
            strong = v["src"] & {"wiki_current_cik", "wiki_snapshot_cik", "sec_ticker", "same_norgate_key"}
            return bool(strong) or v.get("name_sim", 0) >= 0.8 or v.get("hyp_sim", 0) >= 0.999

        prim_pool = [v for v in ver.values() if covers_end(v)] or list(ver.values())
        prim = max(prim_pool, key=lambda v: (rank[v["confidence"]], covers_start(v), v["score"]))
        chain = [prim]
        # predecessor search (holding-company reorganisations / redomiciles / successor registrants) while the
        # head's filings start after the spell start; only 'chainable' candidates (strong source or strong name)
        head = prim
        guard = 0
        while guard < 3 and chainable(head):
            guard += 1
            fr = head.get("first_report")
            if not fr or covers_start(head) or head.get("oldest_loaded", "9999") > fr:
                break
            pool = [v for v in ver.values() if v["cik"] not in {x["cik"] for x in chain}
                    and v.get("confidence") in ("high", "medium") and chainable(v)
                    and v.get("last_report") and v["last_report"] >= add_days(fr, -550)
                    and v.get("first_report") and v["first_report"] < fr]
            if not pool:
                break
            pred = max(pool, key=lambda v: (rank[v["confidence"]], v["score"]))
            chain.append(pred)
            head = pred
        chain = list(reversed(chain))   # oldest first
        # boundary = successor's first periodic report (10-K/10-Q/20-F/40-F) filing date, clamped to the spell
        bounds = [r.start]
        for prev, nxt in zip(chain[:-1], chain[1:]):
            b = nxt.get("first_report")
            if not b:
                wm = e["wiki_ciks_months"]
                b = (min(wm[nxt["cik"]]) + "-01") if nxt["cik"] in wm else r.start
            b = max(b, r.start)
            if r.end:
                b = min(b, r.end)
            bounds.append(b)
        # drop zero-length segments (e.g. successor appears only when the spell ends)
        keep = [i for i in range(len(chain)) if (bounds[i + 1] if i + 1 < len(chain) else (r.end or "9999")) > bounds[i]]
        chain = [chain[i] for i in keep]
        bounds = [bounds[i] for i in keep]
        if bounds:
            bounds[0] = r.start
        for i, v in enumerate(chain):
            to = bounds[i + 1] if i + 1 < len(chain) else r.end
            segs.append({"spell_id": sid, "seg": i + 1, "from": bounds[i], "to": to, "cik": v["cik"],
                         "cik_unverified_best": None, "confidence": v["confidence"],
                         "method": "+".join(sorted(v["src"])), "score": v["score"],
                         "name_sim": v.get("name_sim"), "hyp_sim": v.get("hyp_sim"),
                         "reports_in": v.get("reports_in"), "stop_near_delist": v.get("stop_near_delist"),
                         "sec_name": v.get("sec_name")})
    return pd.DataFrame(segs)


def main():
    sp, L, W, cur, ch = load_inputs()
    sec = Sec()
    ev = build_evidence(sp, L, cur, ch)
    cands = candidates_all(ev, sec)
    L1, conflicts = unlink_conflicts(L, ev, cands, sec)
    C, L2, W2 = pair_unmatched(sp, L1, W, ev, cands, sec)
    ev2 = build_evidence(sp, L2, cur, ch)
    cands2 = candidates_all(ev2, sec)
    segs = assign_segments(sp, ev2, cands2, sec)
    C.to_csv(CACHE / "id_pairs.csv", index=False)
    conflicts.to_csv(CACHE / "id_conflicts.csv", index=False)
    L2.to_parquet(CACHE / "id_link_month.parquet", index=False)
    W2.to_parquet(CACHE / "id_wiki_rows_unlinked.parquet", index=False)
    pd.to_pickle(ev2, CACHE / "id_evidence.pkl")
    pd.to_pickle(cands2, CACHE / "id_candidates.pkl")
    segs.to_parquet(CACHE / "id_segments.parquet", index=False)
    print("links:", L2.link.value_counts().to_dict())
    print("conflicts unlinked:", len(conflicts))
    print("pairs chosen:", int(C.chosen.sum()) if len(C) else 0)
    print("segments:", len(segs), "spells w/o CIK:", int(segs.cik.isna().sum()),
          "multi-seg spells:", int((segs.groupby("spell_id").size() > 1).sum()))


if __name__ == "__main__":
    main()
