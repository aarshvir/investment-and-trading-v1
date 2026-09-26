"""d1_out_current.py - write v4/data/d1_current_constituents.csv (+ .meta.json) from the Wikipedia current table."""
import json

import pandas as pd

from d1_common import CACHE, DATA, WIKI_URL, write_meta


def main():
    cur = pd.read_parquet(CACHE / "wiki_current.parquet")
    log = json.loads((CACHE / "fetch_log.json").read_text())
    out = pd.DataFrame({
        "ticker_yahoo": cur["ticker_yahoo"],
        "ticker_orig": cur["symbol"],
        "name": cur["security"],
        "gics_sector": cur["gics_sector"],
        "gics_sub_industry": cur["gics_sub_industry"],
        "cik": cur["cik"].astype("Int64"),
        "date_added": cur["date_added"],
        "hq": cur["hq"],
        "founded": cur["founded"],
    }).sort_values("ticker_yahoo").reset_index(drop=True)
    p = DATA / "d1_current_constituents.csv"
    out.to_csv(p, index=False)
    write_meta(p, {
        "dataset": "S&P 500 current constituents as of US close 2026-09-25",
        "source_urls": [WIKI_URL],
        "retrieved_utc": log.get("wiki_sp500.html", {}).get("retrieved_utc"),
        "rows": int(len(out)), "columns": list(out.columns),
        "coverage": {"cik_missing": int(out.cik.isna().sum()), "n_companies": int(out.cik.nunique()),
                     "sectors": out.gics_sector.value_counts().to_dict()},
        "caveats": ["503 lines = 500 companies; dual classes GOOGL/GOOG, FOXA/FOX, NWSA/NWS share a CIK.",
                    "ticker_yahoo = Wikipedia symbol with '.'->'-' (BRK-B, BF-B).",
                    "date_added is Wikipedia's 'Date added' (first addition; some firms have re-entry history).",
                    "Latest index change reflected: 2026-09-21 quarterly rebalance (BE, P, ILMN in; TAP, TTD, BLDR out)."],
    })
    print(p, len(out))


if __name__ == "__main__":
    main()
