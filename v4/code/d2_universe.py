"""d2_universe.py - build the D2 download universe (every S&P 500 member since 2000 + benchmarks/ETFs).

Sources (fetched live, raw copies cached in C:\\Users\\user\\eqv4\\cache\\d2\\raw):
  1. Wikipedia 'List of S&P 500 companies' table 1 (current constituents).
  2. Wikipedia 'Historical components of the S&P 500' changes table (Added / Removed tickers).
     (The 'Selected changes' table formerly on the list page now lives there.)
  3. GitHub fja05680/sp500 'S&P 500 Historical Components & Changes (Updated).csv'.
Outputs:
  v4/data/d2_universe.csv          one row per Yahoo ticker with provenance
  v4/data/d2_universe_spells.csv   D2's derived membership spells (helper for coverage stats; D1 is authoritative)
"""
import io
import os
import re
import json
import requests
import pandas as pd

from d2_common import (DATA, RAW, URLS, BENCHMARKS, CUTOFF, to_yahoo, utcnow, write_meta, polite_get)

REFRESH = False  # set True to re-download sources


def fetch(name, url, fname):
    path = os.path.join(RAW, fname)
    log_path = os.path.join(RAW, "retrieval_log.json")
    log = json.load(open(log_path)) if os.path.exists(log_path) else {}
    if REFRESH or not os.path.exists(path):
        s = requests.Session()
        r = polite_get(s, url, timeout=60)
        r.raise_for_status()
        open(path, "wb").write(r.content)
        log[name] = {"url": url, "retrieved_utc": utcnow(), "bytes": len(r.content)}
        json.dump(log, open(log_path, "w"), indent=2)
    elif name not in log:
        log[name] = {"url": url, "retrieved_utc": "cached (see file mtime)", "bytes": os.path.getsize(path)}
        json.dump(log, open(log_path, "w"), indent=2)
    return open(path, "rb").read().decode("utf-8"), log[name]


def clean_tickers(cell):
    if cell is None or (isinstance(cell, float) and pd.isna(cell)):
        return []
    return re.findall(r"[A-Z][A-Z0-9]*(?:\.[A-Z])?", str(cell).upper())


def main():
    # ---------- 1. Wikipedia current constituents ----------
    html_cur, log_cur = fetch("wiki_current", URLS["wiki_current"], "wiki_sp500.html")
    cur = pd.read_html(io.StringIO(html_cur), attrs={"id": "constituents"})[0]
    cur = cur.rename(columns={"Symbol": "ticker_orig", "Security": "name", "GICS Sector": "gics_sector",
                              "GICS Sub-Industry": "gics_sub_industry", "Date added": "date_added", "CIK": "cik"})
    assert len(cur) >= 490, len(cur)

    # ---------- 2. Wikipedia changes table ----------
    html_ch, log_ch = fetch("wiki_changes", URLS["wiki_changes"], "wiki_sp500_historical.html")
    ch = pd.read_html(io.StringIO(html_ch))[0]
    ch.columns = ["date", "add_t", "add_n", "rem_t", "rem_n", "reason", "refs"]
    ch["date"] = pd.to_datetime(ch["date"], format="mixed", errors="coerce")
    assert ch["date"].notna().all()
    ch_rows = []
    for _, r in ch.iterrows():
        for t in clean_tickers(r["add_t"]):
            ch_rows.append(dict(ticker_orig=t, date=r["date"], action="added", name=r["add_n"], reason=r["reason"]))
        for t in clean_tickers(r["rem_t"]):
            ch_rows.append(dict(ticker_orig=t, date=r["date"], action="removed", name=r["rem_n"], reason=r["reason"]))
    chl = pd.DataFrame(ch_rows)

    # ---------- 3. fja05680 historical components ----------
    csv_fja, log_fja = fetch("fja05680", URLS["fja05680"], "fja05680_hist.csv")
    h = pd.read_csv(io.StringIO(csv_fja))
    h["date"] = pd.to_datetime(h["date"])
    h = h.sort_values("date").reset_index(drop=True)
    sets = [set(t.strip() for t in str(s).split(",") if t.strip()) for s in h["tickers"]]
    fja_last_date = h["date"].iloc[-1]

    # membership spells from fja: row i effective [date_i, date_{i+1})
    events = []  # (date, ticker, +1/-1)
    prev = set()
    for d, s in zip(h["date"], sets):
        for t in s - prev:
            events.append((d, t, "start"))
        for t in prev - s:
            events.append((d, t, "end"))
        prev = s
    # tail: apply Wikipedia changes effective after the fja file's last date
    tail = chl[chl["date"] > fja_last_date].sort_values("date")
    tail_log = []
    cur_set = set(prev)
    for _, r in tail.iterrows():
        t = r["ticker_orig"]
        if r["action"] == "added" and t not in cur_set:
            events.append((r["date"], t, "start")); cur_set.add(t); tail_log.append(f"+{t}@{r['date'].date()}")
        elif r["action"] == "removed" and t in cur_set:
            events.append((r["date"], t, "end")); cur_set.discard(t); tail_log.append(f"-{t}@{r['date'].date()}")
    ev = pd.DataFrame(events, columns=["date", "ticker_orig", "kind"]).sort_values(["ticker_orig", "date"])
    spells = []
    for t, g in ev.groupby("ticker_orig"):
        start = None
        for _, r in g.iterrows():
            if r["kind"] == "start":
                start = r["date"]
            elif start is not None:
                spells.append((t, start, r["date"])); start = None
        if start is not None:
            spells.append((t, start, pd.NaT))  # open spell (still a member at cutoff)
    sp = pd.DataFrame(spells, columns=["ticker_orig", "start", "end_excl"])
    # keep spells touching >= 2000-01-01
    sp = sp[(sp["end_excl"].isna()) | (sp["end_excl"] > pd.Timestamp("2000-01-01"))].copy()
    sp["ticker"] = sp["ticker_orig"].map(lambda x: to_yahoo(x)[0])
    sp["source"] = "fja05680 (+Wikipedia changes after %s)" % fja_last_date.date()

    # consistency: reconstructed final set vs Wikipedia current list
    wiki_cur_set = set(cur["ticker_orig"].astype(str))
    recon_final = set(sp.loc[sp["end_excl"].isna(), "ticker_orig"])
    only_recon = sorted(recon_final - wiki_cur_set)
    only_wiki = sorted(wiki_cur_set - recon_final)

    # ---------- union ----------
    rows = {}

    def add(orig, src, **extra):
        y, stripped = to_yahoo(orig)
        r = rows.setdefault(y, dict(ticker=y, ticker_orig=set(), sources=set(), suffix_stripped=False))
        r["ticker_orig"].add(str(orig))
        r["sources"].add(src)
        r["suffix_stripped"] |= stripped
        for k, v in extra.items():
            if v is not None and not (isinstance(v, float) and pd.isna(v)):
                r.setdefault(k, v)

    for _, r in cur.iterrows():
        add(r["ticker_orig"], "wiki_current", current_name=r["name"], gics_sector=r["gics_sector"],
            gics_sub_industry=r["gics_sub_industry"], wiki_date_added=str(r["date_added"]), cik=r["cik"])
    for _, r in chl.iterrows():
        add(r["ticker_orig"], "wiki_changes_" + r["action"])
    fja_since2000 = set()
    for d, s in zip(h["date"], sets):
        if d >= pd.Timestamp("2000-01-01"):
            fja_since2000 |= s
    # rows before 2000 whose set persists into 2000 are captured via spells (effective until next row >= 2000)
    fja_since2000 |= set(sp["ticker_orig"])
    fja_since2000 &= set().union(*sets)  # only tickers that are actually in fja
    for t in sorted(fja_since2000):
        add(t, "fja05680")
    for t, ac in BENCHMARKS.items():
        add(t, "benchmark_list")

    u = pd.DataFrame(rows.values())
    u["ticker_orig"] = u["ticker_orig"].map(lambda s: ";".join(sorted(s)))
    u["sources"] = u["sources"].map(lambda s: ";".join(sorted(s)))
    u["in_current"] = u["sources"].str.contains("wiki_current")
    u["in_fja_since2000"] = u["sources"].str.contains("fja05680")
    u["asset_class"] = u["ticker"].map(lambda t: BENCHMARKS.get(t, "equity"))
    # Wikipedia change dates / names per yahoo ticker
    chl["ticker"] = chl["ticker_orig"].map(lambda x: to_yahoo(x)[0])
    agg = chl.groupby("ticker").agg(
        wiki_added_dates=("date", lambda s: ";".join(sorted(d.strftime("%Y-%m-%d") for d, a in zip(s, chl.loc[s.index, "action"]) if a == "added"))),
        wiki_removed_dates=("date", lambda s: ";".join(sorted(d.strftime("%Y-%m-%d") for d, a in zip(s, chl.loc[s.index, "action"]) if a == "removed"))),
        wiki_names=("name", lambda s: ";".join(sorted(set(str(x) for x in s if isinstance(x, str))))),
        wiki_removal_reasons=("reason", lambda s: " || ".join(sorted(set(str(x) for x, a in zip(s, chl.loc[s.index, "action"]) if a == "removed" and isinstance(x, str))))),
    )
    u = u.merge(agg, left_on="ticker", right_index=True, how="left")
    spa = sp.groupby("ticker").agg(member_first=("start", "min"),
                                   member_last_excl=("end_excl", lambda s: pd.NaT if s.isna().any() else s.max()),
                                   n_spells=("start", "size"))
    u = u.merge(spa, left_on="ticker", right_index=True, how="left")
    # tickers that appear only in the Wikipedia changes table with all change dates before 2000
    def pre2000_only(r):
        if r["in_current"] or r["in_fja_since2000"] or r["asset_class"] != "equity":
            return False
        ds = [x for x in (str(r.get("wiki_added_dates") or "") + ";" + str(r.get("wiki_removed_dates") or "")).split(";") if x and x != "nan"]
        return bool(ds) and max(ds) < "2000-01-01"
    u["wiki_pre2000_only"] = u.apply(pre2000_only, axis=1)
    u = u.sort_values(["asset_class", "ticker"]).reset_index(drop=True)
    cols = ["ticker", "ticker_orig", "asset_class", "sources", "in_current", "in_fja_since2000", "wiki_pre2000_only",
            "suffix_stripped", "current_name", "gics_sector", "gics_sub_industry", "wiki_date_added", "cik",
            "member_first", "member_last_excl", "n_spells", "wiki_added_dates", "wiki_removed_dates", "wiki_names",
            "wiki_removal_reasons"]
    u = u[cols]
    upath = os.path.join(DATA, "d2_universe.csv")
    u.to_csv(upath, index=False)
    sp_out = sp[["ticker", "ticker_orig", "start", "end_excl", "source"]].sort_values(["ticker", "start"])
    sppath = os.path.join(DATA, "d2_universe_spells.csv")
    sp_out.to_csv(sppath, index=False)

    # multiple originals mapping to the same yahoo ticker
    multi = u[u["ticker_orig"].str.contains(";")][["ticker", "ticker_orig"]]
    summary = {
        "n_total": int(len(u)),
        "n_equity": int((u["asset_class"] == "equity").sum()),
        "n_current": int(u["in_current"].sum()),
        "n_fja_since2000": int(u["in_fja_since2000"].sum()),
        "n_wiki_changes_only": int(((u["asset_class"] == "equity") & ~u["in_current"] & ~u["in_fja_since2000"]).sum()),
        "n_wiki_pre2000_only": int(u["wiki_pre2000_only"].sum()),
        "n_benchmarks": int((u["asset_class"] != "equity").sum()),
        "n_suffix_stripped": int(u["suffix_stripped"].sum()),
        "fja_last_row_date": str(fja_last_date.date()),
        "wiki_changes_applied_after_fja": tail_log,
        "recon_vs_wiki_current_only_recon": only_recon,
        "recon_vs_wiki_current_only_wiki": only_wiki,
        "multi_orig_mappings": multi.to_dict("records"),
    }
    json.dump(summary, open(os.path.join(DATA, "..", "outputs", "d2_universe_summary.json"), "w"), indent=2, default=str)
    write_meta(upath, {
        "description": "D2 download universe: union of current S&P 500 (Wikipedia), Wikipedia changes-table tickers, "
                       "fja05680 historical components on any date >= 2000-01-01, and benchmark/ETF list. "
                       "Yahoo-normalised tickers ('.'->'-'); '-YYYYMM' suffixes stripped (none present in this vintage).",
        "sources": {"wiki_current": log_cur, "wiki_changes": log_ch, "fja05680": log_fja},
        "rows": int(len(u)), "columns": cols, "summary": {k: v for k, v in summary.items() if k != "multi_orig_mappings"},
        "caveats": ["Tickers are symbols, not permanent IDs: a historical symbol may now belong to a different company "
                    "(ticker reuse). See d2_coverage.csv flags.",
                    "Wikipedia changes table is 'selected' changes, not exhaustive; fja05680 is a community file.",
                    "D1 builds the authoritative point-in-time membership; d2 spells are only for coverage statistics."],
    })
    write_meta(sppath, {
        "description": "D2-derived membership spells (start inclusive, end exclusive; NaT = still member) from fja05680 "
                       "row-to-row set differences, with Wikipedia changes applied after the fja last row date. "
                       "Helper for coverage statistics only; D1 owns authoritative membership.",
        "sources": {"fja05680": log_fja, "wiki_changes": log_ch}, "rows": int(len(sp_out)),
        "consistency_vs_wiki_current": {"only_in_reconstruction": only_recon, "only_in_wiki_current": only_wiki},
    })
    print(json.dumps({k: v for k, v in summary.items() if k != "multi_orig_mappings"}, indent=1, default=str))
    print("multi-orig:", multi.to_string())


if __name__ == "__main__":
    main()
