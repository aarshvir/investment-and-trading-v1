"""da2_common.py - shared helpers for auditor DA2 (as-filed fundamentals audit of D3).

Read-only use of other agents' files. Raw downloads cached in C:\\Users\\user\\eqv4\\cache\\da2 (not synced).
SEC etiquette: declared User-Agent, <= ~2.5 req/s from this agent (task limit <= 3 req/s), backoff on 403/429/5xx.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import os
import re
import threading
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

PROJECT = Path(r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments")
V4 = PROJECT / "v4"
DATA = V4 / "data"
OUT = V4 / "outputs"
AUDIT = V4 / "audit"
CACHE = Path(r"C:\Users\user\eqv4\cache\da2")
D3CACHE = Path(r"C:\Users\user\eqv4\cache\d3")
DOCS = CACHE / "edgar"
for _p in (CACHE, DOCS):
    _p.mkdir(parents=True, exist_ok=True)

SEC_UA = "PersonalEquityResearch research-admin@personal-research.org"
SEED = 20260926


class RateLimiter:
    def __init__(self, min_interval: float):
        self.min_interval = min_interval
        self._lock = threading.Lock()
        self._last = 0.0

    def wait(self):
        with self._lock:
            now = time.monotonic()
            d = now - self._last
            if d < self.min_interval:
                time.sleep(self.min_interval - d)
            self._last = time.monotonic()


_LIM = RateLimiter(0.40)
_S = requests.Session()
_S.headers.update({"User-Agent": SEC_UA, "Accept-Encoding": "gzip, deflate"})
LOG = CACHE / "sec_fetch_log.csv"


def _cache_path(url: str) -> Path:
    h = hashlib.sha1(url.encode()).hexdigest()[:16]
    tail = re.sub(r"[^A-Za-z0-9._-]", "_", url.rsplit("/", 1)[-1])[-80:]
    return DOCS / f"{h}_{tail}.gz"


def sec_get(url: str, max_tries: int = 6, timeout: int = 90) -> bytes | None:
    """Cached GET. Returns bytes (None on 404)."""
    p = _cache_path(url)
    if p.exists():
        with gzip.open(p, "rb") as f:
            b = f.read()
        return None if b == b"__404__" else b
    last = None
    for a in range(max_tries):
        _LIM.wait()
        try:
            r = _S.get(url, timeout=timeout)
            if r.status_code == 200:
                with gzip.open(p, "wb", compresslevel=6) as f:
                    f.write(r.content)
                with open(LOG, "a", encoding="utf-8") as lf:
                    lf.write(f"{pd.Timestamp.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')},200,{len(r.content)},{url}\n")
                return r.content
            if r.status_code == 404:
                with gzip.open(p, "wb") as f:
                    f.write(b"__404__")
                return None
            last = f"HTTP {r.status_code}"
            if r.status_code in (403, 429):
                time.sleep(min(300, 20 * (a + 1)))
                continue
        except requests.RequestException as e:
            last = repr(e)
        time.sleep(min(60, 2 ** a))
    raise RuntimeError(f"sec_get failed {url}: {last}")


def cik10(c) -> str:
    return f"{int(c):010d}"


def read_gz_json(p: Path):
    with gzip.open(p, "rb") as f:
        return json.loads(f.read())


def load_submissions(cik: int) -> dict:
    """D3's cached submissions JSON (read-only) + any older 'files' pages (fetched & cached by DA2)."""
    p = D3CACHE / "submissions" / f"CIK{cik10(cik)}.json.gz"
    if p.exists():
        j = read_gz_json(p)
    else:
        j = json.loads(sec_get(f"https://data.sec.gov/submissions/CIK{cik10(cik)}.json"))
    return j


def filings_table(cik: int, include_older: bool = True) -> pd.DataFrame:
    j = load_submissions(cik)
    parts = [pd.DataFrame(j["filings"]["recent"])]
    if include_older:
        for fx in j["filings"].get("files", []):
            b = sec_get("https://data.sec.gov/submissions/" + fx["name"])
            if b:
                parts.append(pd.DataFrame(json.loads(b)))
    df = pd.concat(parts, ignore_index=True)
    keep = [c for c in ["accessionNumber", "filingDate", "reportDate", "acceptanceDateTime", "form", "primaryDocument",
                        "primaryDocDescription", "isXBRL", "isInlineXBRL", "items"] if c in df.columns]
    df = df[keep].copy()
    df["cik"] = int(cik)
    return df


def filing_base(cik: int, accn: str) -> str:
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn.replace('-', '')}/"


def write_meta(data_path: Path, meta: dict):
    p = Path(str(data_path).rsplit(".", 1)[0] + ".meta.json")
    meta = dict(meta)
    meta.setdefault("agent", "da2")
    meta.setdefault("written_utc", pd.Timestamp.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
    with open(p, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, default=str)
    return p


def wilson(k: int, n: int, z: float = 1.96):
    """Wilson 95% CI for a pass rate k/n."""
    if n == 0:
        return (np.nan, np.nan, np.nan)
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (p, max(0.0, c - h), min(1.0, c + h))
