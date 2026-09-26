"""d1_common.py - shared paths/helpers for agent D1 (index membership, identifiers & sectors).

Conventions: see v4/CONVENTIONS.md. SEC requests are throttled to <= 4 req/s with retry/backoff.
"""
from __future__ import annotations

import gzip
import io
import json
import os
import time
import threading
import datetime as dt
from pathlib import Path

import requests

PROJECT = Path(r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments")
V4 = PROJECT / "v4"
CODE = V4 / "code"
DATA = V4 / "data"
OUT = V4 / "outputs"
CACHE = Path(r"C:\Users\user\eqv4\cache\d1")
SUBM_CACHE = CACHE / "submissions"
for p in (DATA, OUT, CACHE, SUBM_CACHE):
    p.mkdir(parents=True, exist_ok=True)

SEC_UA = "PersonalEquityResearch research-admin@personal-research.org"
GEN_UA = "PersonalEquityResearch/1.0 (research script; contact research-admin@personal-research.org)"

FJA_BASE = "https://raw.githubusercontent.com/fja05680/sp500/master/"
FJA_FILES = {
    "README.md": "README.md",
    "S&P 500 Historical Components & Changes (Updated).csv": "S%26P%20500%20Historical%20Components%20%26%20Changes%20%28Updated%29.csv",
    "S&P 500 Historical Components & Changes.csv": "S%26P%20500%20Historical%20Components%20%26%20Changes.csv",
    "sp500_ticker_start_end.csv": "sp500_ticker_start_end.csv",
    "sp500_changes_since_2019.csv": "sp500_changes_since_2019.csv",
    "sp500.csv": "sp500.csv",
}
WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
# As of Sep-2026 the "Selected changes" table was moved to this separate article:
WIKI_HIST_URL = "https://en.wikipedia.org/wiki/Historical_components_of_the_S%26P_500"
SEC_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_TICKERS_EXCH_URL = "https://www.sec.gov/files/company_tickers_exchange.json"
SEC_CIK_LOOKUP_URL = "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt"
SEC_SUBM_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"


def utcnow_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class RateLimiter:
    """Simple thread-safe min-interval limiter."""

    def __init__(self, per_second: float):
        self.min_interval = 1.0 / per_second
        self.lock = threading.Lock()
        self.last = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            delta = now - self.last
            if delta < self.min_interval:
                time.sleep(self.min_interval - delta)
            self.last = time.monotonic()


SEC_LIMITER = RateLimiter(3.5)   # stay under the 4 req/s budget
GEN_LIMITER = RateLimiter(1.5)   # Wikipedia / GitHub politeness


def _session(ua: str) -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": ua, "Accept-Encoding": "gzip, deflate"})
    return s


SEC_SESSION = _session(SEC_UA)
GEN_SESSION = _session(GEN_UA)
_TLS = threading.local()


def _thread_session(sec: bool) -> requests.Session:
    """one Session per thread (requests.Session is not guaranteed thread-safe)"""
    attr = "sec" if sec else "gen"
    s = getattr(_TLS, attr, None)
    if s is None:
        s = _session(SEC_UA if sec else GEN_UA)
        setattr(_TLS, attr, s)
    return s


def http_get(url: str, sec: bool = False, max_tries: int = 6, timeout: int = 120, stream: bool = False) -> requests.Response:
    sess = _thread_session(sec)
    limiter = SEC_LIMITER if sec else GEN_LIMITER
    backoff = 2.0
    last_exc = None
    for attempt in range(max_tries):
        limiter.wait()
        try:
            r = sess.get(url, timeout=timeout, stream=stream)
            if r.status_code == 200:
                return r
            if r.status_code == 404:
                return r
            if r.status_code in (429, 500, 502, 503, 504, 403):
                last_exc = RuntimeError(f"HTTP {r.status_code} for {url}")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)
                continue
            return r
        except requests.RequestException as e:  # network error
            last_exc = e
            time.sleep(backoff)
            backoff = min(backoff * 2, 60)
    raise RuntimeError(f"GET failed after {max_tries} tries: {url}: {last_exc}")


def fetch_to_cache(url: str, dest: Path, sec: bool = False, refresh: bool = False) -> Path:
    if dest.exists() and dest.stat().st_size > 0 and not refresh:
        return dest
    r = http_get(url, sec=sec)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code} for {url}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    tmp.write_bytes(r.content)
    tmp.replace(dest)
    return dest


def get_submissions(cik: int, refresh: bool = False) -> dict | None:
    """Return SEC submissions JSON (cached). None if 404."""
    dest = SUBM_CACHE / f"CIK{int(cik):010d}.json"
    if dest.exists() and not refresh:
        txt = dest.read_text(encoding="utf-8")
        if txt.strip() == "404":
            return None
        return json.loads(txt)
    r = http_get(SEC_SUBM_URL.format(cik=int(cik)), sec=True)
    if r.status_code == 404:
        dest.write_text("404", encoding="utf-8")
        return None
    if r.status_code != 200:
        raise RuntimeError(f"submissions HTTP {r.status_code} for CIK {cik}")
    d = r.json()
    _atomic_write(dest, json.dumps(d))
    return d


def _atomic_write(dest: Path, text: str):
    tmp = dest.with_name(dest.name + f".{threading.get_ident()}.part")
    tmp.write_text(text, encoding="utf-8")
    for attempt in range(8):  # Windows: AV scanners can briefly lock fresh files
        try:
            tmp.replace(dest)
            return
        except PermissionError:
            time.sleep(0.25 * (attempt + 1))
    dest.write_text(text, encoding="utf-8")
    try:
        tmp.unlink()
    except OSError:
        pass


def get_submissions_page(filename: str, refresh: bool = False) -> dict | None:
    """Older-filings pages listed in submissions['filings']['files'] (e.g. CIK0000320193-submissions-001.json)."""
    dest = SUBM_CACHE / filename
    if dest.exists() and not refresh:
        txt = dest.read_text(encoding="utf-8")
        if txt.strip() == "404":
            return None
        return json.loads(txt)
    r = http_get("https://data.sec.gov/submissions/" + filename, sec=True)
    if r.status_code == 404:
        dest.write_text("404", encoding="utf-8")
        return None
    if r.status_code != 200:
        raise RuntimeError(f"submissions page HTTP {r.status_code} for {filename}")
    d = r.json()
    _atomic_write(dest, json.dumps(d))
    return d


def yahoo(t: str) -> str:
    """Yahoo-style ticker: uppercase, '.'->'-', stripped."""
    if t is None:
        return t
    return str(t).strip().upper().replace(".", "-").replace("/", "-")


def write_meta(path: Path, meta: dict):
    """Write sidecar <name>.meta.json (name = file name without extension), per CONVENTIONS.md."""
    meta = dict(meta)
    meta.setdefault("generated_utc", utcnow_iso())
    meta.setdefault("agent", "d1")
    mp = path.with_name(path.stem + ".meta.json")
    mp.write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
    return mp


# ---------------------------------------------------------------------------------------------------------------
# NYSE month-end trading days (rule-based). Only holidays that can fall on the last weekday of a month matter:
# Good Friday (Mar/Apr) and Memorial Day (last Monday of May). No other NYSE full-day closure 1996-2026 fell on a
# month's last weekday (Sandy 2012-10-29/30: Oct 31 open; 9/11 closures mid-month; Jan-1-on-Saturday: NYSE open
# on Dec 31). Cross-check against actual price calendars is left to the prices agent (D2).
def _easter(y: int) -> dt.date:
    a = y % 19
    b, c = divmod(y, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l_ = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l_) // 451
    month = (h + l_ - 7 * m + 114) // 31
    day = ((h + l_ - 7 * m + 114) % 31) + 1
    return dt.date(y, month, day)


def _is_month_end_holiday(d: dt.date) -> bool:
    if d == _easter(d.year) - dt.timedelta(days=2):          # Good Friday
        return True
    if d.month == 5 and d.weekday() == 0 and (d + dt.timedelta(days=7)).month == 6:  # Memorial Day
        return True
    return False


def nyse_month_end(year: int, month: int) -> dt.date:
    nxt = dt.date(year + (month == 12), (month % 12) + 1, 1)
    d = nxt - dt.timedelta(days=1)
    while d.weekday() >= 5 or _is_month_end_holiday(d):
        d -= dt.timedelta(days=1)
    return d


def month_end_grid(start="1996-01", end="2026-09", last_data_date="2026-09-25") -> list[dt.date]:
    """last NYSE trading day of each month; the final month is truncated at the data cutoff."""
    out = []
    for p in pd_period_range(start, end):
        d = nyse_month_end(p[0], p[1])
        ld = dt.date.fromisoformat(last_data_date)
        out.append(min(d, ld))
    return out


def pd_period_range(start: str, end: str):
    y, m = map(int, start.split("-"))
    ye, me = map(int, end.split("-"))
    while (y, m) <= (ye, me):
        yield (y, m)
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
