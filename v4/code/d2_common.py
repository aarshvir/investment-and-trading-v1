"""d2_common.py - shared paths/helpers for agent D2 (price history & returns).

Run any d2 script with:
  $env:PYTHONPATH='C:\\Users\\user\\eqv4\\pylib'; python d2_xxx.py
"""
import os
import json
import re
import time
import datetime as dt

PROJECT = r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments"
V4 = os.path.join(PROJECT, "v4")
CODE = os.path.join(V4, "code")
DATA = os.path.join(V4, "data")
OUT = os.path.join(V4, "outputs")
CACHE = r"C:\Users\user\eqv4\cache\d2"
RAW = os.path.join(CACHE, "raw")
BATCH_DIR = os.path.join(CACHE, "batches")
SINGLE_DIR = os.path.join(CACHE, "singles")
META_DIR = os.path.join(CACHE, "meta")
VAL_DIR = os.path.join(CACHE, "validation")
for _d in (CACHE, RAW, BATCH_DIR, SINGLE_DIR, META_DIR, VAL_DIR, DATA, OUT, CODE):
    os.makedirs(_d, exist_ok=True)

# Descriptive UA per CONVENTIONS (no personal data).
UA = {"User-Agent": "PersonalEquityResearch/1.0 (equity research data pipeline; "
                    "contact research-admin@personal-research.org)"}

START = "1995-01-01"
END_EXCL = "2026-09-26"     # yfinance end is exclusive -> last bar 2026-09-25
CUTOFF = "2026-09-25"       # market-data cutoff (US close Fri 2026-09-25)

URLS = {
    "wiki_current": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
    # The 'Selected changes' table was moved off the list page to this article (checked 2026-09-25 UTC).
    "wiki_changes": "https://en.wikipedia.org/wiki/Historical_components_of_the_S%26P_500",
    "fja05680": ("https://raw.githubusercontent.com/fja05680/sp500/master/"
                 "S%26P%20500%20Historical%20Components%20%26%20Changes%20%28Updated%29.csv"),
    "stooq": "https://stooq.com/q/d/l/?s={sym}&i=d",
    "cnbc_bars": "https://ts-api.cnbc.com/harmony/app/bars/{sym}/1D/{start}000000/{end}000000/adjusted/EST5EDT.json",
    "cnbc_quote": ("https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?"
                   "symbols={syms}&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json&events=1"),
    "fred_csv": "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}",
    "cboe_vix": "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",
}

BENCHMARKS = {
    # ticker: asset_class
    "SPY": "etf", "IVV": "etf", "VOO": "etf", "RSP": "etf",
    "^GSPC": "index", "^SP500TR": "index", "^IRX": "rate", "^TNX": "rate", "^VIX": "index",
    "QQQ": "etf", "IWD": "etf", "IWF": "etf", "MTUM": "etf", "QUAL": "etf", "VLUE": "etf",
    "USMV": "etf", "SPHQ": "etf", "BIL": "etf", "SHV": "etf", "SGOV": "etf",
    "XLK": "etf", "XLF": "etf", "XLV": "etf", "XLY": "etf", "XLP": "etf", "XLE": "etf",
    "XLI": "etf", "XLB": "etf", "XLU": "etf", "XLRE": "etf", "XLC": "etf",
    "CSPX.L": "ucits_etf", "VUAA.L": "ucits_etf", "IUSA.L": "ucits_etf",
    "SPXS.L": "ucits_etf", "SPY5.L": "ucits_etf",
}

SUFFIX_RE = re.compile(r"-(19|20)\d{4}$")   # e.g. XYZ-199912 (delisted-ticker disambiguation suffix)


def to_yahoo(sym: str):
    """Return (yahoo_ticker, suffix_stripped_flag)."""
    s = str(sym).strip().upper()
    stripped = False
    if SUFFIX_RE.search(s):
        s = SUFFIX_RE.sub("", s)
        stripped = True
    if s.endswith(".L") or s.startswith("^"):
        return s, stripped
    return s.replace(".", "-"), stripped


def utcnow():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_meta(path_no_ext_or_file, meta: dict):
    """Write <name>.meta.json next to a dataset file."""
    base = path_no_ext_or_file
    for ext in (".parquet", ".csv", ".json", ".md"):
        if base.endswith(ext):
            base = base[: -len(ext)]
            break
    meta = dict(meta)
    meta.setdefault("agent", "d2")
    meta.setdefault("written_utc", utcnow())
    with open(base + ".meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, default=str)


def polite_get(session, url, min_interval=0.55, _last=[0.0], **kw):
    """GET with <=~2 req/s pacing (Wikipedia/GitHub/Stooq/CNBC/FRED etiquette)."""
    wait = min_interval - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    kw.setdefault("timeout", 30)
    kw.setdefault("headers", UA)
    r = session.get(url, **kw)
    _last[0] = time.time()
    return r
