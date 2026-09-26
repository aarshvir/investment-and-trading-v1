"""d1_wiki.py - parse Wikipedia current constituents + 'Historical components of the S&P 500' change table.

Outputs (cache): wiki_current.parquet, wiki_changes.parquet
"""
import io
import re

import pandas as pd

from d1_common import CACHE, yahoo


def clean_ticker(x):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return None
    s = str(x).replace("\xa0", " ").strip()
    s = s.replace("|", " ").strip()
    if ":" in s:  # e.g. 'NYSE: CLF'
        s = s.split(":")[-1].strip()
    s = s.split()[0] if s else s
    s = re.sub(r"\[.*?\]", "", s).strip()
    return s.upper() if s and s.lower() != "nan" else None


def clean_text(x):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return None
    s = re.sub(r"\[\d+\]", "", str(x).replace("\xa0", " ")).replace("|", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s if s and s.lower() != "nan" else None


def parse_current() -> pd.DataFrame:
    html = (CACHE / "wiki_sp500.html").read_text(encoding="utf-8")
    t = pd.read_html(io.StringIO(html), flavor="lxml")[0]
    t.columns = ["symbol", "security", "gics_sector", "gics_sub_industry", "hq", "date_added", "cik", "founded"]
    t["symbol"] = t["symbol"].map(clean_ticker)
    t["ticker_yahoo"] = t["symbol"].map(yahoo)
    for c in ["security", "gics_sector", "gics_sub_industry", "hq", "founded"]:
        t[c] = t[c].map(clean_text)
    t["date_added"] = pd.to_datetime(t["date_added"].map(clean_text), errors="coerce").dt.strftime("%Y-%m-%d")
    t["cik"] = pd.to_numeric(t["cik"], errors="coerce").astype("Int64")
    return t


def parse_changes() -> pd.DataFrame:
    html = (CACHE / "wiki_sp500_historical.html").read_text(encoding="utf-8")
    t = pd.read_html(io.StringIO(html), flavor="lxml")[0]
    t.columns = ["date_raw", "add_ticker", "add_name", "rem_ticker", "rem_name", "reason", "refs"]
    t["date"] = pd.to_datetime(t["date_raw"].map(clean_text), format="mixed", errors="coerce").dt.strftime("%Y-%m-%d")
    for c in ["add_ticker", "rem_ticker"]:
        t[c] = t[c].map(clean_ticker)
    for c in ["add_name", "rem_name", "reason"]:
        t[c] = t[c].map(clean_text)
    t["row_id"] = range(len(t))
    return t[["row_id", "date", "date_raw", "add_ticker", "add_name", "rem_ticker", "rem_name", "reason"]]


def main():
    cur = parse_current()
    ch = parse_changes()
    for df in (cur, ch):
        for c in df.columns:
            if df[c].dtype == object:
                df[c] = df[c].astype("string")
    cur.to_parquet(CACHE / "wiki_current.parquet", index=False)
    ch.to_parquet(CACHE / "wiki_changes.parquet", index=False)
    print("current:", cur.shape, "cik missing:", int(cur.cik.isna().sum()), "dup tickers:", int(cur.symbol.duplicated().sum()))
    print("sectors:", cur.gics_sector.value_counts().to_dict())
    print("changes:", ch.shape, ch.date.min(), ch.date.max(), "bad dates:", int(ch.date.isna().sum()))
    print(cur[cur.symbol.str.contains(r"\.", regex=True)][["symbol", "ticker_yahoo", "security"]].to_string())


if __name__ == "__main__":
    main()
