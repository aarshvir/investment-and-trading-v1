"""d4_fetch_yahoo.py - pull the live Yahoo Finance snapshot (via yfinance 1.7) for every S&P 500 constituent.

Per ticker (one pickle per ticker in CACHE/yahoo/<TICKER>.pkl, resumable):
  info; earnings_estimate; revenue_estimate; eps_trend; eps_revisions (+ raw earningsTrend list incl. endDate
  per period - the authoritative fiscal-period end for 0q/+1q/0y/+1y); earnings_history; get_earnings_dates(16);
  analyst_price_targets; recommendations_summary; upgrades_downgrades; calendar (+ raw calendarEvents epoch
  timestamps, because yfinance's calendar converts epochs with the *local* machine timezone); income_stmt (annual);
  news (latest news + press releases titles).
  Retrieval UTC start/end recorded per ticker.

Etiquette: <=5 worker threads (conventions allow 6), global limiter ~8 req/s, exponential backoff on
rate-limit/transient errors.

Usage: python d4_fetch_yahoo.py [--only T1,T2] [--refresh]
"""
from __future__ import annotations

import argparse
import pickle
import random
import sys
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from d4_common import CACHE, DATA, RateLimiter, utc_now_iso  # noqa: E402

import yfinance as yf  # noqa: E402
from yfinance.config import YfConfig  # noqa: E402

YfConfig.debug.hide_exceptions = False   # we want to see and retry errors
YCACHE = CACHE / "yahoo"
YCACHE.mkdir(parents=True, exist_ok=True)
LIMIT = RateLimiter(8.0)
LOG_LOCK = threading.Lock()
LOG = CACHE / "fetch_yahoo.log"

NO_DATA_MARKERS = ("No upgrade/downgrade history", "No earnings dates found", "symbol may be delisted",
                   "No data found", "YFEarningsDateMissing")
RATE_MARKERS = ("429", "Too Many Requests", "RateLimit", "rate limit", "Rate limited")


def log(msg: str):
    with LOG_LOCK:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{utc_now_iso()} {msg}\n")


def call(rec: dict, name: str, fn, tries: int = 5):
    for i in range(tries):
        LIMIT.wait()
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            msg = f"{type(e).__name__}: {e}"[:600]
            if any(m in msg for m in NO_DATA_MARKERS):
                rec["errors"][name] = "NO_DATA: " + msg
                return None
            if i < tries - 1:
                if any(m in msg for m in RATE_MARKERS):
                    sl = min(120, 10 * 2 ** i) + random.random() * 3
                else:
                    sl = 1.5 * 2 ** i + random.random()
                log(f"retry {rec['ticker']} {name} in {sl:.1f}s: {msg[:200]}")
                time.sleep(sl)
                continue
            rec["errors"][name] = msg
            log(f"FAIL {rec['ticker']} {name}: {msg[:300]}")
            return None


def slim_news(items):
    out = []
    for x in items or []:
        c = x.get("content", x) if isinstance(x, dict) else {}
        out.append({
            "title": c.get("title"),
            "pubDate": c.get("pubDate") or c.get("displayTime"),
            "provider": (c.get("provider") or {}).get("displayName") if isinstance(c.get("provider"), dict) else c.get("provider"),
            "url": ((c.get("canonicalUrl") or {}).get("url") if isinstance(c.get("canonicalUrl"), dict) else None),
            "contentType": c.get("contentType"),
        })
    return out


def fetch_one(tk: str, refresh: bool = False):
    path = YCACHE / f"{tk}.pkl"
    if path.exists() and not refresh:
        try:
            with open(path, "rb") as f:
                old = pickle.load(f)
            if old.get("complete"):
                return tk, "cached", old.get("errors", {})
        except Exception:  # noqa: BLE001
            pass
    rec = {"ticker": tk, "t_start_utc": utc_now_iso(), "errors": {}, "yfinance_version": yf.__version__}
    t = yf.Ticker(tk)
    info = call(rec, "info", lambda: dict(t.info))
    rec["info"] = info
    rec["earnings_estimate"] = call(rec, "earnings_estimate", lambda: t.earnings_estimate)
    # raw trend list (same HTTP response as earnings_estimate; contains endDate per period)
    try:
        rec["earnings_trend_raw"] = list(t._analysis._earnings_trend or [])
    except Exception as e:  # noqa: BLE001
        rec["earnings_trend_raw"] = None
        rec["errors"]["earnings_trend_raw"] = str(e)[:300]
    rec["revenue_estimate"] = call(rec, "revenue_estimate", lambda: t.revenue_estimate)
    rec["eps_trend"] = call(rec, "eps_trend", lambda: t.eps_trend)
    rec["eps_revisions"] = call(rec, "eps_revisions", lambda: t.eps_revisions)
    rec["earnings_history"] = call(rec, "earnings_history", lambda: t.earnings_history)
    rec["earnings_dates"] = call(rec, "earnings_dates", lambda: t.get_earnings_dates(limit=16))
    rec["analyst_price_targets"] = call(rec, "analyst_price_targets", lambda: dict(t.analyst_price_targets))
    rec["recommendations_summary"] = call(rec, "recommendations_summary", lambda: t.recommendations_summary)
    rec["upgrades_downgrades"] = call(rec, "upgrades_downgrades", lambda: t.upgrades_downgrades)
    rec["calendar"] = call(rec, "calendar", lambda: dict(t.calendar))
    rec["calendar_raw"] = call(rec, "calendar_raw", lambda: t._quote._fetch(modules=["calendarEvents"]))
    rec["income_stmt"] = call(rec, "income_stmt", lambda: t.income_stmt)
    rec["news"] = call(rec, "news", lambda: slim_news(t.get_news(count=30, tab="news")))
    t._news = []  # yfinance caches news on the object; reset before second tab
    rec["press_releases"] = call(rec, "press_releases", lambda: slim_news(t.get_news(count=30, tab="press releases")))
    rec["t_end_utc"] = utc_now_iso()
    rec["complete"] = bool(info) and len(info) > 20
    with open(path, "wb") as f:
        pickle.dump(rec, f)
    return tk, ("ok" if rec["complete"] else "incomplete"), rec["errors"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--workers", type=int, default=5)
    a = ap.parse_args()
    u = pd.read_csv(DATA / "d4_universe.csv")
    tickers = [x for x in a.only.split(",") if x] or u["ticker"].tolist()
    log(f"START n={len(tickers)} workers={a.workers}")
    t0 = time.time()
    stats = {}
    with ThreadPoolExecutor(max_workers=min(a.workers, 6)) as ex:
        futs = {ex.submit(fetch_one, tk, a.refresh): tk for tk in tickers}
        for i, fu in enumerate(as_completed(futs), 1):
            tk = futs[fu]
            try:
                _, status, errs = fu.result()
            except Exception:  # noqa: BLE001
                status, errs = "crash", {"crash": traceback.format_exc()[-400:]}
                log(f"CRASH {tk} {errs}")
            stats[status] = stats.get(status, 0) + 1
            hard = {k: v for k, v in (errs or {}).items() if not str(v).startswith("NO_DATA")}
            if i % 25 == 0 or hard:
                print(f"[{i}/{len(tickers)}] {tk} {status} {list(hard)[:5]} elapsed={time.time()-t0:.0f}s", flush=True)
    log(f"END stats={stats} elapsed={time.time()-t0:.0f}s")
    print("DONE", stats, f"{time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
