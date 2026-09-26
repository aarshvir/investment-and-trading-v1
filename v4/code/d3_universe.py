"""d3_universe.py - build the D3 company universe (CIK list) and a monthly membership table for coverage checks.

Sources
  1. Wikipedia "List of S&P 500 companies" table 1 (current constituents, includes CIK)
     https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
  2. fja05680/sp500 "S&P 500 Historical Components & Changes (Updated).csv" (daily snapshots of tickers)
     https://raw.githubusercontent.com/fja05680/sp500/master/S%26P%20500%20Historical%20Components%20%26%20Changes%20%28Updated%29.csv
  3. SEC https://www.sec.gov/files/company_tickers.json (CURRENT ticker -> CIK only)

Outputs
  v4/data/d3_universe.csv                  one row per CIK processed by D3
  v4/data/d3_ticker_cik_map.csv            fja/wiki ticker -> CIK mapping used by D3 (with method + check flags)
  CACHE/membership_monthly.parquet         month_end x constituent ticker (fja snapshot; Wikipedia for 2026-09)
"""
from __future__ import annotations

import io
import json
import urllib.parse

import pandas as pd

from d3_common import (CACHE, DATA, http_get, month_ends, utcnow_iso, write_meta)

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
FJA_NAME = "S&P 500 Historical Components & Changes (Updated).csv"
FJA_URL = "https://raw.githubusercontent.com/fja05680/sp500/master/" + urllib.parse.quote(FJA_NAME)
SEC_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"


def norm_ticker(t: str) -> str:
    return str(t).strip().upper().replace(".", "-")


def fetch(url, path, sec):
    r = http_get(url, sec=sec)
    r.raise_for_status()
    path.write_bytes(r.content)
    return r.content


def main(refresh: bool = False):
    retrieved = {}
    wiki_p, fja_p, sec_p = CACHE / "wiki_sp500.html", CACHE / "fja_components_updated.csv", CACHE / "company_tickers.json"
    for url, p, sec in [(WIKI_URL, wiki_p, False), (FJA_URL, fja_p, False), (SEC_TICKERS_URL, sec_p, True)]:
        if refresh or not p.exists():
            fetch(url, p, sec)
        retrieved[url] = utcnow_iso() if refresh else pd.Timestamp(p.stat().st_mtime, unit="s", tz="UTC").strftime("%Y-%m-%dT%H:%M:%SZ")

    # ---------------- current constituents (Wikipedia) ----------------
    wiki = pd.read_html(io.StringIO(wiki_p.read_text(encoding="utf-8")))[0]
    wiki = wiki.rename(columns={"Symbol": "ticker_orig", "Security": "name_wiki", "GICS Sector": "gics_sector",
                                "GICS Sub-Industry": "gics_sub_industry", "Date added": "date_added", "CIK": "cik"})
    wiki["ticker"] = wiki["ticker_orig"].map(norm_ticker)
    wiki["cik"] = wiki["cik"].astype(int)
    wiki_t2c = dict(zip(wiki["ticker"], wiki["cik"]))

    # ---------------- SEC current ticker map ----------------
    ct = json.loads(sec_p.read_text(encoding="utf-8"))
    sec_rows = pd.DataFrame(list(ct.values()))
    sec_rows["ticker"] = sec_rows["ticker"].map(norm_ticker)
    sec_t2c = {}
    for t, c in zip(sec_rows["ticker"], sec_rows["cik_str"]):
        sec_t2c.setdefault(t, int(c))
    sec_c2title = dict(zip(sec_rows["cik_str"].astype(int), sec_rows["title"]))

    # ---------------- fja historical snapshots ----------------
    fja = pd.read_csv(fja_p)
    fja["date"] = pd.to_datetime(fja["date"])
    fja = fja.sort_values("date").reset_index(drop=True)
    d0 = fja.loc[fja["date"] <= pd.Timestamp("2009-01-01"), "date"].max()   # snapshot in force on 2009-01-01
    fja09 = fja[fja["date"] >= d0].copy()
    fja09["tset"] = fja09["tickers"].map(lambda s: {norm_ticker(x) for x in s.split(",") if x.strip()})
    first, last = {}, {}
    for d, ts in zip(fja09["date"], fja09["tset"]):
        for t in ts:
            first.setdefault(t, d)
            last[t] = d
    fja_last_date = fja09["date"].max()

    # ---------------- ticker -> CIK map ----------------
    rows = []
    all_tickers = sorted(set(first) | set(wiki["ticker"]))
    for t in all_tickers:
        if t in wiki_t2c:
            cik, method = wiki_t2c[t], "wikipedia_current_cik"
        elif t in sec_t2c:
            cik, method = sec_t2c[t], "sec_company_tickers_current"
        else:
            cik, method = None, "unmapped"
        rows.append({"ticker": t, "cik": cik, "method": method,
                     "in_wiki_current": t in wiki_t2c, "in_fja_since2009": t in first,
                     "fja_first": first.get(t), "fja_last": last.get(t),
                     "fja_still_member_at_last_snapshot": (last.get(t) == fja_last_date) if t in last else False})
    tmap = pd.DataFrame(rows)
    tmap["cik"] = tmap["cik"].astype("Int64")

    # ---------------- universe (one row per CIK) ----------------
    u = tmap.dropna(subset=["cik"]).copy()
    g = []
    for cik, grp in u.groupby("cik"):
        wrow = wiki[wiki["cik"] == cik]
        if len(wrow):
            primary = wrow["ticker"].iloc[0]  # first listed (e.g. GOOGL before GOOG)
        else:
            primary = grp.sort_values("fja_last")["ticker"].iloc[-1]
        g.append({
            "cik": int(cik), "ticker": primary, "tickers_all": ";".join(sorted(grp["ticker"])),
            "name": (wrow["name_wiki"].iloc[0] if len(wrow) else sec_c2title.get(int(cik))),
            "sec_title": sec_c2title.get(int(cik)),
            "in_wiki_current": bool(grp["in_wiki_current"].any()),
            "in_fja_since2009": bool(grp["in_fja_since2009"].any()),
            "fja_first": grp["fja_first"].min(), "fja_last": grp["fja_last"].max(),
            "gics_sector": (wrow["gics_sector"].iloc[0] if len(wrow) else None),
            "gics_sub_industry": (wrow["gics_sub_industry"].iloc[0] if len(wrow) else None),
            "source": "wiki_current" if grp["in_wiki_current"].any() else "fja_hist_via_sec_current_tickers",
        })
    univ = pd.DataFrame(g).sort_values(["source", "ticker"]).reset_index(drop=True)

    # ---------------- monthly membership (for coverage) ----------------
    mes = month_ends()
    mem = []
    for t_me in mes:
        if t_me > fja_last_date and t_me >= pd.Timestamp("2026-09-01"):
            ts, src = set(wiki["ticker"]), "wikipedia_current"
        else:
            snap = fja09[fja09["date"] <= t_me].iloc[-1]
            ts, src = snap["tset"], f"fja_{snap['date'].date()}"
        for t in sorted(ts):
            mem.append((t_me, t, src))
    mem = pd.DataFrame(mem, columns=["month_end", "ticker", "snapshot"])
    mem.to_parquet(CACHE / "membership_monthly.parquet", index=False)

    univ.to_csv(DATA / "d3_universe.csv", index=False)
    tmap.to_csv(DATA / "d3_ticker_cik_map.csv", index=False)
    common = {"sources": [WIKI_URL, FJA_URL, SEC_TICKERS_URL], "retrieval_utc": retrieved}
    write_meta(DATA / "d3_universe.csv", {**common, "rows": len(univ), "columns": list(univ.columns),
               "n_current": int(univ["in_wiki_current"].sum()), "n_hist_only": int((~univ["in_wiki_current"]).sum()),
               "caveats": ["Historical tickers mapped with the SEC CURRENT ticker file only: renamed/delisted/acquired "
                           "companies are unmapped (see d3_ticker_cik_map.csv method=unmapped) and ticker re-use can "
                           "mis-map (checked later in d3_pull via facts-during-membership test).",
                           "Dual-class companies appear once (primary ticker = first Wikipedia symbol)."]})
    write_meta(DATA / "d3_ticker_cik_map.csv", {**common, "rows": len(tmap), "columns": list(tmap.columns),
               "n_unmapped": int((tmap["method"] == "unmapped").sum())})
    print(f"universe CIKs={len(univ)} (current={univ['in_wiki_current'].sum()}, hist-only={(~univ['in_wiki_current']).sum()})")
    print(f"tickers since 2009 (fja)={len(first)}, mapped={tmap[tmap.in_fja_since2009 & tmap.cik.notna()].shape[0]}, "
          f"unmapped={(tmap['method'] == 'unmapped').sum()}")
    print(f"membership rows={len(mem)} months={mem.month_end.nunique()}")
    return univ, tmap


if __name__ == "__main__":
    import sys
    main(refresh="--refresh" in sys.argv)
