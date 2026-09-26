"""d4_universe.py - current S&P 500 constituents from Wikipedia (table 1) + 'selected changes' table (table 2).

Outputs:
  v4/data/d4_universe.csv            one row per constituent (Yahoo-style ticker)
  v4/data/d4_index_changes.csv       Wikipedia 'Selected changes' table (used for corporate-event context)
Raw HTML cached to CACHE/wiki_sp500.html
"""
from __future__ import annotations

import sys
from io import StringIO

import pandas as pd
import requests

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from d4_common import CACHE, DATA, UA_WEB, utc_now_iso, write_meta, yahoo_ticker  # noqa: E402

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


def main():
    raw = CACHE / "wiki_sp500.html"
    retrieved = utc_now_iso()
    r = requests.get(URL, headers={"User-Agent": UA_WEB}, timeout=60)
    r.raise_for_status()
    raw.write_text(r.text, encoding="utf-8")
    tables = pd.read_html(StringIO(r.text), attrs={"id": "constituents"})
    t = tables[0]
    t.columns = [str(c).strip() for c in t.columns]
    cols = {"Symbol": "ticker_orig", "Security": "name", "GICS Sector": "gics_sector",
            "GICS Sub-Industry": "gics_sub_industry", "Headquarters Location": "hq", "Date added": "date_added",
            "CIK": "cik", "Founded": "founded"}
    t = t.rename(columns=cols)
    t["ticker"] = t["ticker_orig"].map(yahoo_ticker)
    t["cik"] = pd.to_numeric(t["cik"], errors="coerce").astype("Int64")
    t = t[["ticker", "ticker_orig", "name", "gics_sector", "gics_sub_industry", "cik", "date_added", "hq", "founded"]]
    out = DATA / "d4_universe.csv"
    t.to_csv(out, index=False)
    write_meta(out, {
        "source_urls": [URL], "retrieval_utc": retrieved,
        "rows": int(len(t)), "columns": list(t.columns),
        "unique_tickers": int(t["ticker"].nunique()), "unique_cik": int(t["cik"].nunique()),
        "caveats": ["Wikipedia is a secondary source; D1 agent owns authoritative membership/IDs.",
                    "Tickers converted to Yahoo style ('.'->'-'); original kept in ticker_orig."],
    })
    print("constituents", len(t), "unique cik", t["cik"].nunique())

    # Selected changes table (id="changes"). As of the 2026-09-25 retrieval the page no longer carries this table
    # (only the constituents table + a navbox), so this block is best-effort and skipped when absent.
    if 'id="changes"' not in r.text:
        print("changes table not present on page (skipped)")
        return
    ch = pd.read_html(StringIO(r.text), attrs={"id": "changes"}, flavor="lxml")[0]
    ch.columns = ["_".join([str(x) for x in c if "Unnamed" not in str(x)]).strip("_") if isinstance(c, tuple) else str(c)
                  for c in ch.columns]
    ren = {}
    for c in ch.columns:
        lc = c.lower()
        if lc.startswith("effective date") or lc == "date":
            ren[c] = "date"
        elif "added" in lc and "ticker" in lc:
            ren[c] = "added_ticker"
        elif "added" in lc and "security" in lc:
            ren[c] = "added_name"
        elif "removed" in lc and "ticker" in lc:
            ren[c] = "removed_ticker"
        elif "removed" in lc and "security" in lc:
            ren[c] = "removed_name"
        elif "reason" in lc:
            ren[c] = "reason"
    ch = ch.rename(columns=ren)
    ch["date_parsed"] = pd.to_datetime(ch["date"], errors="coerce", format="mixed")
    out2 = DATA / "d4_index_changes.csv"
    ch.to_csv(out2, index=False)
    write_meta(out2, {"source_urls": [URL + "#Selected_changes_to_the_list_of_S&P_500_components"],
                      "retrieval_utc": retrieved, "rows": int(len(ch)), "columns": list(ch.columns),
                      "caveats": ["Wikipedia 'selected changes' table; not exhaustive; reasons are free text."]})
    print("changes", len(ch), ch["date_parsed"].max())


if __name__ == "__main__":
    main()
