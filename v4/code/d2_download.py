"""d2_download.py - Yahoo daily history download for the D2 universe, with caching/resume.

Phases (python d2_download.py <phase>):
  batch   : yf.download(... start=1995-01-01, end=2026-09-26, auto_adjust=False, actions=True, group_by='ticker',
            threads=6) in batches of 60 (threads capped at 6 per CONVENTIONS); each batch cached as long parquet.
  retry   : tickers with no rows are retried one-by-one via Ticker.history with exponential backoff.
  meta    : light monthly-interval chart call per ticker to capture Yahoo chart metadata
            (longName, instrumentType, exchange, currency, firstTradeDate).
  refresh : re-download the last ~3 weeks for tickers active at the cutoff (the 2026-09-25 bar was still
            intraday-live during the first pass); patches are applied in d2_build.py. If the Adj/Close factor
            changed (new ex-dividend), the full history for that ticker is re-downloaded.
  all     : batch + retry + meta
"""
import os
import sys
import json
import time
import glob
import logging
import random
import pandas as pd
import numpy as np
import yfinance as yf

from d2_common import (DATA, BATCH_DIR, SINGLE_DIR, META_DIR, CACHE, START, END_EXCL, CUTOFF, utcnow)

BATCH_SIZE = 60
THREADS = 6
PRICE_COLS = ["Open", "High", "Low", "Close", "Adj Close", "Volume", "Dividends", "Stock Splits", "Capital Gains"]
RATE_WORDS = ("rate", "too many", "429", "timed out", "timeout", "connection", "curl", "ssl", "502", "503", "500")


class ListHandler(logging.Handler):
    def __init__(self):
        super().__init__(level=logging.ERROR)
        self.records = []

    def emit(self, record):
        try:
            self.records.append(record.getMessage())
        except Exception:
            pass


YF_LOG = ListHandler()
logging.getLogger("yfinance").addHandler(YF_LOG)


def universe_order():
    u = pd.read_csv(os.path.join(DATA, "d2_universe.csv"))
    bench = u[u["asset_class"] != "equity"]["ticker"].tolist()
    cur = u[(u["asset_class"] == "equity") & (u["in_current"])]["ticker"].tolist()
    hist = u[(u["asset_class"] == "equity") & (~u["in_current"])]["ticker"].tolist()
    return bench + sorted(cur) + sorted(hist)


def to_long(df):
    out = []
    if df is None or df.empty:
        return pd.DataFrame(columns=["date", "ticker"] + PRICE_COLS)
    if isinstance(df.columns, pd.MultiIndex):
        for t in df.columns.get_level_values(0).unique():
            sub = df[t].dropna(how="all")
            if sub.empty:
                continue
            sub = sub.copy()
            sub.index.name = "date"
            sub = sub.reset_index()
            sub.insert(1, "ticker", t)
            out.append(sub)
    else:
        raise ValueError("expected MultiIndex columns")
    if not out:
        return pd.DataFrame(columns=["date", "ticker"] + PRICE_COLS)
    res = pd.concat(out, ignore_index=True)
    for c in PRICE_COLS:
        if c not in res.columns:
            res[c] = np.nan
    res = res[["date", "ticker"] + PRICE_COLS]
    res["date"] = pd.to_datetime(res["date"]).dt.tz_localize(None) if getattr(res["date"].dt, "tz", None) else pd.to_datetime(res["date"])
    return res


def cached_tickers():
    done = {}
    for f in glob.glob(os.path.join(BATCH_DIR, "*.json")) + glob.glob(os.path.join(SINGLE_DIR, "*.json")):
        j = json.load(open(f))
        for t in j.get("with_data", []):
            done[t] = f
    return done


def attempted_tickers():
    att = set()
    for f in glob.glob(os.path.join(BATCH_DIR, "*.json")):
        att |= set(json.load(open(f)).get("tickers", []))
    return att


def is_rate_error(msgs):
    txt = " ".join(msgs).lower()
    return any(w in txt for w in RATE_WORDS)


def phase_batch():
    order = universe_order()
    att = attempted_tickers()
    todo = [t for t in order if t not in att]
    print(f"[batch] universe={len(order)} already_attempted={len(att)} todo={len(todo)}", flush=True)
    existing = sorted(glob.glob(os.path.join(BATCH_DIR, "b*.parquet")))
    k0 = len(existing)
    for i in range(0, len(todo), BATCH_SIZE):
        batch = todo[i:i + BATCH_SIZE]
        k = k0 + i // BATCH_SIZE
        for attempt in range(4):
            YF_LOG.records.clear()
            t0 = time.time()
            try:
                df = yf.download(batch, start=START, end=END_EXCL, auto_adjust=False, actions=True,
                                 group_by="ticker", threads=THREADS, progress=False, timeout=30)
                err = list(YF_LOG.records)
            except Exception as e:
                df, err = None, [repr(e)]
            lg = to_long(df)
            with_data = sorted(lg["ticker"].unique().tolist()) if len(lg) else []
            empty = sorted(set(batch) - set(with_data))
            rate = is_rate_error(err)
            print(f"[batch {k:03d}] n={len(batch)} with_data={len(with_data)} empty={len(empty)} rows={len(lg)} "
                  f"secs={time.time()-t0:.1f} rate_err={rate}", flush=True)
            if rate and attempt < 3 and len(empty) > 0:
                wait = 20 * (3 ** attempt)
                print(f"   rate-limit/transient errors -> sleeping {wait}s and retrying batch", flush=True)
                time.sleep(wait)
                continue
            break
        lg.to_parquet(os.path.join(BATCH_DIR, f"b{k:03d}.parquet"), index=False)
        json.dump({"batch": k, "tickers": batch, "with_data": with_data, "empty": empty, "errors": err,
                   "retrieved_utc": utcnow(), "call": dict(start=START, end=END_EXCL, auto_adjust=False, actions=True,
                                                            group_by="ticker", threads=THREADS)},
                  open(os.path.join(BATCH_DIR, f"b{k:03d}.json"), "w"), indent=1)
        time.sleep(2.0)


def history_single(t, start=START, end=END_EXCL, interval="1d"):
    tk = yf.Ticker(t)
    h = tk.history(start=start, end=end, interval=interval, auto_adjust=False, actions=True, timeout=30)
    err = tk._price_history._last_error if tk._price_history is not None else None
    try:
        md = tk.history_metadata or {}
    except Exception:
        md = {}
    return h, err, md


def phase_retry():
    done = cached_tickers()
    att = attempted_tickers()
    todo = sorted(att - set(done))
    print(f"[retry] attempted={len(att)} with_data={len(done)} retry={len(todo)}", flush=True)
    results = {}
    rpath = os.path.join(SINGLE_DIR, "retry_log.json")
    if os.path.exists(rpath):
        results = json.load(open(rpath))
    for n, t in enumerate(todo):
        if t in results and results[t].get("final") in ("no_data", "ok"):
            continue
        hist = []
        final = "no_data"
        for attempt in range(4):
            try:
                h, err, md = history_single(t)
            except Exception as e:
                h, err, md = None, repr(e), {}
            hist.append(str(err))
            if h is not None and not h.empty:
                h = h.copy()
                h.index = pd.to_datetime(h.index).tz_localize(None)
                h.index.name = "date"
                lg = h.reset_index()
                lg.insert(1, "ticker", t)
                for c in PRICE_COLS:
                    if c not in lg.columns:
                        lg[c] = np.nan
                lg = lg[["date", "ticker"] + PRICE_COLS]
                safe = t.replace("^", "IDX_")
                lg.to_parquet(os.path.join(SINGLE_DIR, f"s_{safe}.parquet"), index=False)
                json.dump({"tickers": [t], "with_data": [t], "retrieved_utc": utcnow(), "errors": hist},
                          open(os.path.join(SINGLE_DIR, f"s_{safe}.json"), "w"))
                final = "ok"
                break
            if err and is_rate_error([str(err)]):
                time.sleep(5 * (3 ** attempt))
                continue
            if attempt >= 1:   # two clean 'no data' answers -> accept
                break
            time.sleep(2)
        results[t] = {"final": final, "errors": hist, "utc": utcnow()}
        if n % 25 == 0:
            print(f"[retry] {n}/{len(todo)} {t} -> {final}", flush=True)
            json.dump(results, open(rpath, "w"), indent=1)
        time.sleep(0.4)
    json.dump(results, open(rpath, "w"), indent=1)
    ok = sum(1 for v in results.values() if v["final"] == "ok")
    print(f"[retry] recovered={ok} no_data={len(results)-ok}", flush=True)


def phase_meta():
    from concurrent.futures import ThreadPoolExecutor, as_completed
    order = universe_order()
    mpath = os.path.join(META_DIR, "yahoo_meta.json")
    meta = json.load(open(mpath)) if os.path.exists(mpath) else {}
    done = cached_tickers()
    todo = [t for t in order if t in done and t not in meta]
    print(f"[meta] todo={len(todo)}", flush=True)
    keys = ["symbol", "longName", "shortName", "instrumentType", "exchangeName", "fullExchangeName", "currency",
            "firstTradeDate", "regularMarketTime", "exchangeTimezoneName", "regularMarketPrice"]

    def one(t):
        for attempt in range(4):
            try:
                h, err, md = history_single(t, interval="1mo")
                rec = {k: (str(md.get(k)) if md.get(k) is not None else None) for k in keys}
                rec["error"] = err
                if (not md) and err and is_rate_error([str(err)]):
                    raise RuntimeError(err)
                return t, rec
            except Exception as e:
                time.sleep(5 * (3 ** attempt))
                last = repr(e)
        return t, {"error": last}

    with ThreadPoolExecutor(max_workers=THREADS) as ex:
        futs = [ex.submit(one, t) for t in todo]
        for n, f in enumerate(as_completed(futs)):
            t, rec = f.result()
            meta[t] = rec
            if n % 100 == 0:
                print(f"[meta] {n}/{len(todo)}", flush=True)
                json.dump(meta, open(mpath, "w"), indent=1)
    json.dump(meta, open(mpath, "w"), indent=1)
    print(f"[meta] total={len(meta)}", flush=True)


def phase_refresh(start="2026-09-01"):
    """Re-download recent bars for tickers whose cached last date >= 2026-09-01."""
    frames = [pd.read_parquet(f, columns=["date", "ticker"]) for f in
              glob.glob(os.path.join(BATCH_DIR, "b*.parquet")) + glob.glob(os.path.join(SINGLE_DIR, "s_*.parquet"))]
    allp = pd.concat(frames, ignore_index=True)
    last = allp.groupby("ticker")["date"].max()
    act = sorted(last[last >= pd.Timestamp(start)].index.tolist())
    print(f"[refresh] active tickers={len(act)}", flush=True)
    outdir = os.path.join(CACHE, "refresh")
    os.makedirs(outdir, exist_ok=True)
    stamp = utcnow().replace(":", "").replace("-", "")
    parts, errs = [], []
    for i in range(0, len(act), BATCH_SIZE):
        batch = act[i:i + BATCH_SIZE]
        for attempt in range(4):
            YF_LOG.records.clear()
            try:
                df = yf.download(batch, start=start, end=END_EXCL, auto_adjust=False, actions=True,
                                 group_by="ticker", threads=THREADS, progress=False, timeout=30)
                err = list(YF_LOG.records)
            except Exception as e:
                df, err = None, [repr(e)]
            lg = to_long(df)
            miss = set(batch) - set(lg["ticker"].unique()) if len(lg) else set(batch)
            if miss and is_rate_error(err) and attempt < 3:
                time.sleep(20 * (3 ** attempt))
                continue
            break
        parts.append(lg)
        errs += err
        print(f"[refresh] {i//BATCH_SIZE}: rows={len(lg)} missing={sorted(miss)[:10]}", flush=True)
        time.sleep(2)
    ref = pd.concat(parts, ignore_index=True)
    ref.to_parquet(os.path.join(outdir, f"refresh_{stamp}.parquet"), index=False)
    json.dump({"retrieved_utc": utcnow(), "start": start, "n_tickers": len(act), "errors": errs},
              open(os.path.join(outdir, f"refresh_{stamp}.json"), "w"), indent=1)
    print(f"[refresh] saved refresh_{stamp}.parquet rows={len(ref)}", flush=True)


def phase_full_redownload(tickers):
    """Re-download full history for specific tickers (e.g. adj factor changed on refresh)."""
    outdir = os.path.join(CACHE, "redownload")
    os.makedirs(outdir, exist_ok=True)
    for t in tickers:
        for attempt in range(4):
            try:
                h, err, md = history_single(t)
                if h is not None and not h.empty:
                    h = h.copy()
                    h.index = pd.to_datetime(h.index).tz_localize(None)
                    h.index.name = "date"
                    lg = h.reset_index()
                    lg.insert(1, "ticker", t)
                    for c in PRICE_COLS:
                        if c not in lg.columns:
                            lg[c] = np.nan
                    lg[["date", "ticker"] + PRICE_COLS].to_parquet(
                        os.path.join(outdir, f"r_{t.replace('^', 'IDX_')}.parquet"), index=False)
                    json.dump({"ticker": t, "retrieved_utc": utcnow()},
                              open(os.path.join(outdir, f"r_{t.replace('^', 'IDX_')}.json"), "w"))
                    break
            except Exception as e:
                time.sleep(5 * (3 ** attempt))
        time.sleep(0.5)


if __name__ == "__main__":
    ph = sys.argv[1] if len(sys.argv) > 1 else "all"
    if ph in ("batch", "all"):
        phase_batch()
    if ph in ("retry", "all"):
        phase_retry()
    if ph in ("meta", "all"):
        phase_meta()
    if ph == "refresh":
        phase_refresh()
    if ph == "redownload":
        phase_full_redownload(sys.argv[2].split(","))
