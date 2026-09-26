"""d4_common.py - shared paths/helpers for agent D4 (live snapshot + validation).

All D4 scripts import this module. Paths follow v4/CONVENTIONS.md.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import time
from pathlib import Path

PROJECT = Path(r"C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments")
V4 = PROJECT / "v4"
CODE = V4 / "code"
DATA = V4 / "data"
OUT = V4 / "outputs"
LEGACY = PROJECT / "equity_project"
CACHE = Path(r"C:\Users\user\eqv4\cache\d4")
for _p in (DATA, OUT, CACHE):
    _p.mkdir(parents=True, exist_ok=True)

ASOF = dt.date(2026, 9, 25)          # market-data cutoff (US close Friday 2026-09-25)
ASOF_STR = ASOF.isoformat()

# Descriptive UA for Wikipedia / Cboe / CNBC (no personal data)
UA_WEB = "PersonalEquityResearch/1.0 (research; contact research-admin@personal-research.org)"
# SEC-mandated UA per CONVENTIONS.md
UA_SEC = "PersonalEquityResearch research-admin@personal-research.org"

V3_PORTFOLIO = ["NVDA", "CPAY", "AMP", "RL", "AME", "SNA", "ABNB", "NTAP", "PAYX", "MSFT", "IBKR", "HIG", "ALLE", "AIZ"]


def utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_meta(path: Path, meta: dict) -> None:
    """Write sidecar <name>.meta.json next to a dataset."""
    p = Path(path)
    meta_path = p.with_name(p.stem + ".meta.json") if p.suffix else Path(str(p) + ".meta.json")
    meta = {"dataset": p.name, "agent": "d4", "written_utc": utc_now_iso(), **meta}
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, default=str)


class RateLimiter:
    """Simple thread-safe min-interval limiter (requests per second)."""

    def __init__(self, per_second: float):
        import threading
        self.min_interval = 1.0 / per_second
        self.lock = threading.Lock()
        self.last = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            delta = self.last + self.min_interval - now
            if delta > 0:
                time.sleep(delta)
            self.last = time.monotonic()


def yahoo_ticker(sym: str) -> str:
    return sym.strip().upper().replace(".", "-")
