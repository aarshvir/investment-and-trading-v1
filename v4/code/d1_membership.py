"""d1_membership.py - build entity-level PIT membership outputs.

Inputs (cache): fja_spells.parquet (d1_fja), id_segments.parquet / id_evidence.pkl / id_candidates.pkl /
id_link_month.parquet (d1_identity), wiki_current.parquet, wiki_changes.parquet, company_tickers_exchange.json.
Outputs (v4/data): d1_membership_intervals.csv, d1_membership_monthly.parquet, d1_additions_since_2015.csv
                   (+ .meta.json), cache/entity_rows.parquet (for cik map / sectors / checks).

Entity rules (documented in d1_report.md):
 R1 ticker reuse across keys: the same CIK assigned to two different keys at the same time, where Wikipedia's CIK
    column shows a different CIK for the earlier key after the later key's start -> the earlier key's segment is
    cut at the later key's start and the remainder takes the Wikipedia CIK (e.g. IR: Ingersoll-Rand plc -> TT on
    2020-03-03; the IR symbol continues as Ingersoll Rand Inc., CIK 1699150).
 R2 a within-spell CIK change within +-10 days of a Wikipedia change row that adds and removes the SAME ticker is
    a new company (e.g. FOXA/FOX 2019-03-19: 21st Century Fox -> Fox Corp) -> separate entities, boundary = row date.
 R3 other within-spell CIK changes are holding-company reorganisations/redomiciles/successor registrants
    (Google->Alphabet, Medtronic->Medtronic plc, Disney 2019, Cigna 2018 ...) -> same entity; cik column changes.
 Company = union of segments linked by R3 or by identical CIK; entity_id = 'CIK' + 10-digit CIK of the company's
 latest segment. Several index lines of one company at the same time (GOOGL/GOOG, FOXA/FOX, NWSA/NWS, UAA/UA,
 DISCA/DISCK, CMCSA/CMCSK, Sprint FON/PCS ...) -> the earliest line keeps entity_id, others get '<entity_id>.<TICKER>'.
 No CIK -> entity_id = 'NG:<Norgate/fja key>'.
Membership semantics: start_date = first trading day in the index (effective date); end_date = removal effective
date = first day NOT in the index (exclusive); blank = still a member on 2026-09-25.
"""
from __future__ import annotations

import json
from collections import defaultdict

import pandas as pd

from d1_common import CACHE, DATA, WIKI_URL, WIKI_HIST_URL, FJA_BASE, month_end_grid, write_meta, yahoo
from d1_snaplink import tkey, SUFFIX_RE, month_end

LAST = "2026-09-25"
OPEN = "9999-12-31"


def _ok(x) -> bool:
    return isinstance(x, str) and bool(x.strip())


def add_days(d: str, n: int) -> str:
    return (pd.Timestamp(d) + pd.Timedelta(days=n)).strftime("%Y-%m-%d")


def load():
    sp = pd.read_parquet(CACHE / "fja_spells.parquet")
    sp["end"] = pd.Series([x if _ok(x) else None for x in sp["end"]], dtype=object)
    sp["spell_id"] = sp["key"] + "#" + sp["spell_no"].astype(int).astype(str)
    S = pd.read_parquet(CACHE / "id_segments.parquet")
    S["to"] = pd.Series([x if _ok(x) else None for x in S["to"]], dtype=object)
    S["cik"] = S["cik"].astype("Int64")
    ev = pd.read_pickle(CACHE / "id_evidence.pkl")
    cands = pd.read_pickle(CACHE / "id_candidates.pkl")
    L = pd.read_parquet(CACHE / "id_link_month.parquet")
    cur = pd.read_parquet(CACHE / "wiki_current.parquet")
    ch = pd.read_parquet(CACHE / "wiki_changes.parquet")
    d = json.loads((CACHE / "company_tickers_exchange.json").read_text())
    ct = pd.DataFrame(d["data"], columns=d["fields"])
    return sp, S, ev, cands, L, cur, ch, ct


def overlap(a0, a1, b0, b1) -> int:
    a1 = a1 if _ok(a1) else OPEN
    b1 = b1 if _ok(b1) else OPEN
    lo, hi = max(a0, b0), min(a1, b1)
    if lo >= hi:
        return 0
    return (pd.Timestamp(min(hi, LAST)) - pd.Timestamp(lo)).days


def apply_R1(S, sp, ev, cands, log):
    """ticker reuse across keys (same CIK on two keys simultaneously, wiki shows another CIK for the older key)"""
    key_of = dict(zip(sp.spell_id, sp.key))
    start_of = dict(zip(sp.spell_id, sp.start))
    rows = S.to_dict("records")
    changed = True
    guard = 0
    while changed and guard < 5:
        changed = False
        guard += 1
        by_cik = defaultdict(list)
        for i, r in enumerate(rows):
            if pd.notna(r["cik"]):
                by_cik[int(r["cik"])].append(i)
        for cik, idx in by_cik.items():
            for i in idx:
                for j in idx:
                    a, b = rows[i], rows[j]
                    if i == j or key_of[a["spell_id"]] == key_of[b["spell_id"]]:
                        continue
                    if not (a["from"] < b["from"] and overlap(a["from"], a["to"], b["from"], b["to"]) > 5):
                        continue
                    # does Wikipedia show a different CIK for a's key after b starts?
                    wm = ev[a["spell_id"]]["wiki_ciks_months"]
                    later = {c: [m for m in ms if m >= b["from"][:7]] for c, ms in wm.items() if c != cik}
                    later = {c: ms for c, ms in later.items() if len(ms) >= 3}
                    if not later:
                        continue
                    # the switch must be visible right after b starts (<=3 months); otherwise b is a new share
                    # class of the same company (GOOG 2014, FOX 2015) and the later CIK change is a reorganisation
                    b_m = pd.Period(b["from"][:7], freq="M")
                    if not any(pd.Period(min(ms), freq="M") <= b_m + 3 for ms in later.values()):
                        continue
                    newc = max(later, key=lambda c: len(later[c]))
                    cand = cands[a["spell_id"]].get(newc, {})
                    new = dict(a)
                    new.update({"seg": a["seg"] + 0.5, "from": b["from"], "cik": newc,
                                "confidence": cand.get("confidence", "medium"),
                                "method": "+".join(sorted(cand.get("src", {"wiki_snapshot_cik"}))) + "+R1_ticker_reuse_split",
                                "sec_name": cand.get("sec_name"), "name_sim": cand.get("name_sim"),
                                "reports_in": cand.get("reports_in"), "boundary": "R1_ticker_reuse"})
                    log.append({"rule": "R1", "spell_id": a["spell_id"], "old_cik": cik, "new_cik": newc,
                                "split_date": b["from"], "evidence": f"CIK {cik} continues as {b['spell_id']}; "
                                f"Wikipedia CIK column shows {newc} for {key_of[a['spell_id']]} in {len(later[newc])} months"})
                    a["to"] = b["from"]
                    rows.append(new)
                    changed = True
                    break
                if changed:
                    break
            if changed:
                break
    out = pd.DataFrame(rows)
    return out.sort_values(["spell_id", "from"]).reset_index(drop=True)


def classify_boundaries(S, ch, log):
    """R2 vs R3 for within-spell CIK boundaries"""
    ch = ch.copy()
    ch["dt"] = pd.to_datetime(ch["date"])
    same_t = ch[ch["add_ticker"].notna() & (ch["add_ticker"] == ch["rem_ticker"])]
    S = S.copy()
    if "boundary" not in S.columns:
        S["boundary"] = None
    S["boundary"] = S["boundary"].where(S["boundary"].notna(), None)
    for sid, g in S.groupby("spell_id"):
        g = g.sort_values("from")
        idx = list(g.index)
        for p, n in zip(idx[:-1], idx[1:]):
            if S.at[n, "boundary"] == "R1_ticker_reuse":
                continue
            b = pd.Timestamp(S.at[n, "from"])
            key = sid.split("#")[0]
            hit = same_t[(same_t["add_ticker"].map(tkey) == tkey(SUFFIX_RE.sub("", key))) &
                         (abs(same_t["dt"] - b) <= pd.Timedelta(days=10))]
            if len(hit):
                d = hit["date"].iloc[0]
                S.at[p, "to"] = d
                S.at[n, "from"] = d
                S.at[n, "boundary"] = "R2_new_company"
                log.append({"rule": "R2", "spell_id": sid, "old_cik": S.at[p, "cik"], "new_cik": S.at[n, "cik"],
                            "split_date": d, "evidence": f"Wikipedia change row {d}: {hit['add_ticker'].iloc[0]} added and "
                            f"removed ({hit['reason'].iloc[0]})"})
            else:
                S.at[n, "boundary"] = "R3_reorganisation"
                log.append({"rule": "R3", "spell_id": sid, "old_cik": S.at[p, "cik"], "new_cik": S.at[n, "cik"],
                            "split_date": S.at[n, "from"], "evidence": "within-spell CIK change without index event "
                            "(holding-company reorganisation / redomicile / successor registrant); boundary = successor's "
                            "first 10-K/10-Q filing date"})
    return S


class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def build_entities(S, sp):
    S = S.copy().reset_index(drop=True)
    S["node"] = S.index
    key_of = dict(zip(sp.spell_id, sp.key))
    S["key"] = S["spell_id"].map(key_of)
    uf = UF()
    for n in S["node"]:
        uf.find(n)
    # R3 within-spell links
    for sid, g in S.sort_values("from").groupby("spell_id"):
        idx = list(g["node"])
        for p, n in zip(idx[:-1], idx[1:]):
            if S.at[n, "boundary"] == "R3_reorganisation":
                uf.union(p, n)
    # same CIK
    for cik, g in S[S["cik"].notna()].groupby("cik"):
        idx = list(g["node"])
        for n in idx[1:]:
            uf.union(idx[0], n)
    # same Norgate key, no CIK anywhere -> one entity per key
    S["comp"] = S["node"].map(uf.find)
    ent = {}
    for comp, g in S.groupby("comp"):
        if g["cik"].notna().any():
            gg = g[g["cik"].notna()].copy()
            gg["to_s"] = gg["to"].fillna(OPEN)
            last = gg.sort_values(["to_s", "from"]).iloc[-1]
            ent[comp] = f"CIK{int(last['cik']):010d}"
        else:
            ent[comp] = "NG:" + g["key"].iloc[0]
    S["company_id"] = S["comp"].map(ent)
    # keys without CIK but sharing a company? (no-CIK comps are per node; merge per key)
    nokey = S["company_id"].str.startswith("NG:")
    S.loc[nokey, "company_id"] = "NG:" + S.loc[nokey, "key"]
    # lines within a company: keys that overlap in time are distinct lines
    S["line"] = 0
    for comp, g in S.groupby("company_id"):
        keys = []
        for k, gk in g.groupby("key"):
            keys.append((gk["from"].min(), not str(k).endswith("A"), k, list(gk.index)))
        keys.sort()
        lines = []  # list of lists of (from,to)
        for f0, _notA, k, idx in keys:
            ivs = [(S.at[i, "from"], S.at[i, "to"]) for i in idx]
            placed = False
            for li, livs in enumerate(lines):
                if all(overlap(a0, a1, b0, b1) <= 5 for a0, a1 in ivs for b0, b1 in livs):
                    livs.extend(ivs)
                    S.loc[idx, "line"] = li
                    placed = True
                    break
            if not placed:
                lines.append(list(ivs))
                S.loc[idx, "line"] = len(lines) - 1
    return S


def ticker_runs(L, spell_id, frm, to, key):
    """observed at-the-time tickers (Wikipedia month-end lists, fja keys after 2019-01) inside [frm, to)"""
    g = L[(L["spell_id"] == spell_id) & L["wiki_ticker"].notna()]
    obs = []
    for m, t in sorted(zip(g["month"], g["wiki_ticker"])):
        me = month_end(m)
        if frm <= me < (to or OPEN):
            obs.append((m, str(t)))
    base = SUFFIX_RE.sub("", key)
    if frm >= "2019-01-11" or (to or OPEN) > "2019-01-11":
        # fja keys are at-the-time tickers after 2019-01-11: add months not covered by Wikipedia
        seen = {m for m, _ in obs}
        for p in pd.period_range(max(frm, "2019-01-11")[:7], min((to or LAST), LAST)[:7], freq="M"):
            me = month_end(str(p))
            if str(p) not in seen and max(frm, "2019-01-11") <= me < (to or OPEN):
                obs.append((str(p), base))
        obs.sort()
    runs = []
    for m, t in obs:
        t = t.replace(" ", "")
        if runs and runs[-1][0] == t:
            runs[-1][2] = m
        else:
            runs.append([t, m, m])
    return runs


def main():
    sp, S, ev, cands, L, cur, ch, ct = load()
    log = []
    S["boundary"] = None
    S = apply_R1(S, sp, ev, cands, log)
    S = classify_boundaries(S, ch, log)
    S = build_entities(S, sp)
    S["to"] = pd.Series([x if _ok(x) else None for x in S["to"]], index=S.index, dtype=object)
    spell = sp.set_index("spell_id")
    # ---------------------------------------------------------------- entity ids with line suffix
    S["line_ticker"] = None
    ct["tn"] = ct["ticker"].map(yahoo)
    ct_by_cik = ct.groupby("cik")["tn"].apply(list).to_dict()
    cur_by_t = {yahoo(t): r for t, r in zip(cur["symbol"], cur.itertuples())}
    cur_by_cik = cur.groupby("cik")["ticker_yahoo"].apply(list).to_dict()
    # ---------------------------------------------------------------- output rows (merge contiguous same entity/cik)
    rows = []
    for (cid, line), g in S.sort_values("from").groupby(["company_id", "line"]):
        recs = g.sort_values("from").to_dict("records")
        merged = []
        for r in recs:
            if merged and _ok(merged[-1]["to"]) and merged[-1]["to"] == r["from"] and (
                    (pd.isna(merged[-1]["cik"]) and pd.isna(r["cik"])) or
                    (pd.notna(merged[-1]["cik"]) and pd.notna(r["cik"]) and int(merged[-1]["cik"]) == int(r["cik"]))):
                merged[-1]["to"] = r["to"]
                merged[-1]["parts"].append(r)
            else:
                r = dict(r)
                r["parts"] = [dict(r)]
                merged.append(r)
        for m in merged:
            m["company_id"], m["line"] = cid, line
            rows.append(m)
    out = []
    ch2 = ch.copy()
    ch2["dt"] = pd.to_datetime(ch2["date"])
    for r in rows:
        parts = r["parts"]
        runs = []
        for p in parts:
            runs += ticker_runs(L, p["spell_id"], p["from"], p["to"], p["key"])
        # merge identical consecutive runs across parts
        mr = []
        for t, a, b in runs:
            if mr and mr[-1][0] == t:
                mr[-1][2] = b
            else:
                mr.append([t, a, b])
        first_part = parts[0]
        last_part = parts[-1]
        key0 = first_part["key"]
        base0 = SUFFIX_RE.sub("", key0)
        if mr and mr[0][1][:7] <= (first_part["from"][:7] if first_part["from"] >= "2007-03" else "2007-03") and \
                (first_part["from"] >= "2007-03-01" or True):
            tick_at = mr[0][0]
            basis = "wikipedia_snapshot" if first_part["from"] >= "2007-03-01" or mr[0][1] == "2007-03" else "wikipedia_snapshot(backfilled)"
        elif first_part["from"] >= "2019-01-11":
            tick_at, basis = base0, "fja_key"
        else:
            tick_at, basis = base0, "norgate_symbol(last_or_2019_ticker)"
        if mr and first_part["from"] < "2007-03-01":
            basis = "wikipedia_first_observed(2007+),backfilled"
        # names
        names = []
        for p in parts:
            e = ev[p["spell_id"]]
            names += [n for n, _ in sorted(e["wiki_names"].items(), key=lambda kv: -kv[1])]
        g = L[L["spell_id"].isin([p["spell_id"] for p in parts]) & L["wiki_name"].notna()].sort_values("month")
        g = g[[(r["from"] <= month_end(m) < (r["to"] or OPEN)) for m in g["month"]]] if len(g) else g
        name = g["wiki_name"].iloc[-1] if len(g) else None
        if not name and pd.notna(r["cik"]):
            c = cands[last_part["spell_id"]].get(int(r["cik"]), {})
            name = c.get("sec_name")
        # removal reason: Wikipedia change row near end removing this line's last ticker (or name)
        reason = None
        end = r["to"]
        if end and end <= LAST:
            last_t = mr[-1][0] if mr else SUFFIX_RE.sub("", last_part["key"])
            cand = ch2[abs(ch2["dt"] - pd.Timestamp(end)) <= pd.Timedelta(days=7)]
            hit = cand[cand["rem_ticker"].map(lambda x: tkey(x) if _ok(x) else "") == tkey(last_t)]
            if not len(hit) and _ok(name):
                from d1_sec_ref import token_sim
                hit = cand[cand["rem_name"].map(lambda x: token_sim(x, name) >= 0.5 if _ok(x) else False)]
            if len(hit):
                reason = hit["reason"].iloc[0]
        srcs = sorted({spell.at[p["spell_id"], "src"] for p in parts if p["from"] == spell.at[p["spell_id"], "start"]})
        out.append({
            "company_id": r["company_id"], "line": r["line"], "cik": r["cik"],
            "ticker_at_time": tick_at, "ticker_at_time_basis": basis,
            "ticker_history": ";".join(f"{t}:{a}..{b}" for t, a, b in mr),
            "name": name, "start_date": r["from"], "end_date": r["to"],
            "norgate_keys": ",".join(dict.fromkeys(p["key"] for p in parts)),
            "spell_ids": ",".join(dict.fromkeys(p["spell_id"] for p in parts)),
            "start_boundary": first_part.get("boundary") if first_part["from"] != spell.at[first_part["spell_id"], "start"] else "index_add",
            "end_boundary": ("current" if not end else ("index_remove" if end == spell.at[last_part["spell_id"], "end"] else "cik_change")),
            "removal_reason": reason, "cik_confidence": r.get("confidence"), "cik_method": r.get("method"),
            "cik_first_report": (cands[last_part["spell_id"]].get(int(r["cik"]), {}).get("first_report")
                                 if pd.notna(r["cik"]) else None),
            "cik_last_report": (cands[last_part["spell_id"]].get(int(r["cik"]), {}).get("last_report")
                                if pd.notna(r["cik"]) else None),
            "source": "+".join(dict.fromkeys([spell.at[p["spell_id"], "src"] for p in parts] +
                                             [spell.at[p["spell_id"], "end_src"] for p in parts if _ok(spell.at[p["spell_id"], "end_src"])])),
        })
    O = pd.DataFrame(out)
    # entity_id with line suffix for secondary simultaneous lines
    O["line_rank"] = O.groupby("company_id")["line"].rank(method="dense").astype(int)
    O["entity_id"] = O["company_id"]
    sec_line = O["line_rank"] > 1
    # line ticker = current Yahoo ticker if trading else last at-time ticker
    def last_ticker(row):
        h = row["ticker_history"]
        return h.split(";")[-1].split(":")[0] if _ok(h) else row["ticker_at_time"]
    O["line_last_ticker"] = O.apply(last_ticker, axis=1).map(yahoo)
    line_tick = O.groupby(["company_id", "line"])["line_last_ticker"].last().to_dict()
    O.loc[sec_line, "entity_id"] = [f"{c}.{line_tick[(c, l)]}" for c, l in zip(O.loc[sec_line, "company_id"], O.loc[sec_line, "line"])]
    # ticker_current_yahoo: entity still listed (SEC company_tickers by CIK of the company) - pick the line's class
    ent_last = O.sort_values("start_date").groupby("entity_id").tail(1).set_index("entity_id")
    tcur = {}
    for eid, r in ent_last.iterrows():
        cik = int(r["company_id"][3:]) if r["company_id"].startswith("CIK") else None
        lt = r["line_last_ticker"]
        cand_t = []
        if cik is not None:
            cand_t = list(cur_by_cik.get(cik, [])) + list(ct_by_cik.get(cik, []))
        if (pd.isna(r["end_date"]) or not _ok(r["end_date"])) and lt in cur_by_t:
            tcur[eid] = lt      # current member: Wikipedia's current symbol for this line
            continue
        if not cand_t:
            tcur[eid] = None
            continue
        if lt in cand_t:
            tcur[eid] = lt
        elif pd.isna(r["end_date"]) or not _ok(r["end_date"]):
            tcur[eid] = cand_t[0]
        else:
            # removed from index: take the SEC primary ticker unless another line of the company owns it
            others = set(O.loc[(O.company_id == r["company_id"]) & (O.entity_id != eid), "line_last_ticker"])
            tt = [t for t in cand_t if t not in others]
            tcur[eid] = tt[0] if tt else None
    O["ticker_current_yahoo"] = O["entity_id"].map(tcur)
    O["is_current_member"] = O["end_date"].isna()
    O = O.sort_values(["entity_id", "start_date"]).reset_index(drop=True)
    O.to_parquet(CACHE / "entity_rows.parquet", index=False)
    pd.DataFrame(log).to_csv(CACHE / "entity_rules_log.csv", index=False)

    # ---------------------------------------------------------------- d1_membership_intervals.csv
    cols = ["entity_id", "cik", "ticker_at_time", "ticker_current_yahoo", "name", "start_date", "end_date",
            "removal_reason", "source", "ticker_history", "ticker_at_time_basis", "norgate_keys", "start_boundary",
            "end_boundary", "cik_confidence", "cik_method", "cik_first_report", "cik_last_report"]
    I = O[cols].copy()
    I["cik"] = I["cik"].astype("Int64")
    p = DATA / "d1_membership_intervals.csv"
    I.to_csv(p, index=False)

    # ---------------------------------------------------------------- monthly parquet
    grid = [d.isoformat() for d in month_end_grid("1996-01", "2026-09", LAST)]
    ents = sorted(I["entity_id"].unique())
    M = pd.DataFrame(False, index=pd.DatetimeIndex(pd.to_datetime(grid), name="date"), columns=ents)
    for r in I.itertuples():
        e = r.end_date if _ok(r.end_date) else OPEN
        mask = [(r.start_date <= d < e) for d in grid]
        M.loc[mask, r.entity_id] = True
    M = M.loc[:, M.any(axis=0)]
    pm = DATA / "d1_membership_monthly.parquet"
    M.to_parquet(pm)
    counts = M.sum(axis=1)

    # ---------------------------------------------------------------- additions since 2015
    A = O[(O["start_boundary"] == "index_add") & (O["start_date"] >= "2015-01-01")].copy()
    # previous membership of the same entity (re-additions)
    prev_end = []
    for r in A.itertuples():
        pr = O[(O.entity_id == r.entity_id) & (O.start_date < r.start_date)]
        prev_end.append(pr["end_date"].dropna().max() if len(pr) else None)
    A["previous_membership_end"] = prev_end
    A["add_type"] = ["re-addition" if _ok(x) else "first addition (since 1996)" for x in A["previous_membership_end"]]
    cur_eids = set(O.loc[O.is_current_member, "entity_id"])
    A["still_member_2026_09_25"] = A["entity_id"].isin(cur_eids)
    # removal date of the membership that started at add date (follow contiguous rows)
    rem = []
    for r in A.itertuples():
        rr = O[(O.entity_id == r.entity_id) & (O.start_date >= r.start_date)].sort_values("start_date")
        end = None
        prev = None
        for x in rr.itertuples():
            if prev is not None and x.start_date != prev:
                break
            end = x.end_date if _ok(x.end_date) else None
            prev = x.end_date
            if end is None:
                break
        rem.append(end)
    A["removal_date"] = rem
    A = A.rename(columns={"start_date": "add_date", "ticker_at_time": "ticker_at_add"})
    acols = ["entity_id", "cik", "ticker_at_add", "ticker_current_yahoo", "name", "add_date", "removal_date",
             "still_member_2026_09_25", "add_type", "previous_membership_end", "source", "cik_confidence"]
    A = A[acols].sort_values(["add_date", "entity_id"]).reset_index(drop=True)
    A["cik"] = A["cik"].astype("Int64")
    pa = DATA / "d1_additions_since_2015.csv"
    A.to_csv(pa, index=False)

    # ---------------------------------------------------------------- metas
    fetch = json.loads((CACHE / "fetch_log.json").read_text())
    common_src = [FJA_BASE + "S%26P%20500%20Historical%20Components%20%26%20Changes.csv",
                  FJA_BASE + "S%26P%20500%20Historical%20Components%20%26%20Changes%20%28Updated%29.csv",
                  WIKI_HIST_URL, WIKI_URL,
                  "https://en.wikipedia.org/w/api.php (List_of_S%26P_500_companies page history, monthly revisions 2007-2026)",
                  "https://www.sec.gov/files/company_tickers_exchange.json",
                  "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt",
                  "https://data.sec.gov/submissions/CIK##########.json"]
    conf = I.groupby("cik_confidence", dropna=False).size().to_dict()
    write_meta(p, {"dataset": "S&P 500 point-in-time membership intervals 1996-01-02..2026-09-25 (entity level)",
                   "source_urls": common_src, "retrieved_utc": {k: v.get("retrieved_utc") for k, v in fetch.items()},
                   "rows": int(len(I)), "columns": list(I.columns), "n_entities": int(I.entity_id.nunique()),
                   "cik_confidence_rows": {str(k): int(v) for k, v in conf.items()},
                   "semantics": "start_date inclusive (effective date, first day in index); end_date exclusive "
                                "(removal effective date, first day NOT in index); blank end_date = member on 2026-09-25. "
                                "A new row starts when the registrant CIK changes (reorganisation) - see start_boundary.",
                   "caveats": ["1996-2019-01-11 from fja05680 original file (Norgate symbols), 2019-01-12..2026-08-18 from "
                               "fja Updated file, 2026-09-21 change from Wikipedia.",
                               "ticker_at_time before 2007-03 is the first Wikipedia-observed ticker back-filled, else the "
                               "Norgate symbol (last traded ticker for delisted names) - see ticker_at_time_basis.",
                               "1996-2000 lists hold 499-501 names; fja notes possible missing names in the first years."]})
    write_meta(pm, {"dataset": "S&P 500 monthly membership matrix (bool), index = last NYSE trading day of each month "
                               "1996-01..2026-09 (Sep-2026 = 2026-09-25 cutoff); columns = entity_id",
                    "source_urls": common_src, "rows": int(M.shape[0]), "columns_n": int(M.shape[1]),
                    "count_min": int(counts.min()), "count_max": int(counts.max()),
                    "count_min_since_2000": int(counts[counts.index >= "2000-01-01"].min()),
                    "calendar": "rule-based NYSE month-end: last weekday excluding Good Friday and Memorial Day",
                    "caveats": ["Member at month-end t iff start_date <= t < end_date.",
                                "Secondary share-class lines have entity_id '<CIK...>.<TICKER>' (e.g. CIK0001652044.GOOG)."]})
    write_meta(pa, {"dataset": "Entities added to the S&P 500 on/after 2015-01-01 (index additions, incl. re-additions; "
                               "excludes pure ticker/CIK changes)", "source_urls": common_src, "rows": int(len(A)),
                    "columns": list(A.columns),
                    "still_member_2026_09_25": int(A.still_member_2026_09_25.sum())})
    print("intervals", len(I), "entities", I.entity_id.nunique(), "monthly", M.shape, "count range", counts.min(), counts.max())
    print("additions since 2015:", len(A), "still members:", int(A.still_member_2026_09_25.sum()))
    print(pd.DataFrame(log).rule.value_counts().to_dict() if log else {})


if __name__ == "__main__":
    main()
