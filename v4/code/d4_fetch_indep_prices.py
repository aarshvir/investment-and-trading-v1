"""d4_fetch_indep_prices.py - independent (non-Yahoo) closing prices for 2026-09-25, for price validation.

Sources (public, unauthenticated, no CAPTCHA/bot challenge solved or circumvented):
  1. Cboe delayed-quotes JSON  https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/<SYM>.json   (field 'close',
     plus 'prev_day_close', 'last_trade_time', response 'timestamp')                     - one request per symbol
  2. CNBC quote web service    https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=A|B|..
     (fields 'last', 'last_time', 'previous_day_closing', 'sharesout', 'eps', 'feps', 'fpe', 'mktcapView')  - batched
  3. Stooq CSV (the source requested in the brief)  https://stooq.com/q/d/l/?s=<sym>.us&i=d
     -> As of 2026-09-25 Stooq answers with a JavaScript proof-of-work "verify your browser" page. That is a bot
        challenge; we record the response once as evidence and DO NOT attempt to solve/circumvent it.

Rate: <=2 requests/second per host. Raw responses cached in CACHE/indep_prices/.
Output: v4/data/d4_indep_prices.csv (+ .meta.json)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).parent))
from d4_common import CACHE, DATA, UA_WEB, RateLimiter, utc_now_iso, write_meta  # noqa: E402

PC = CACHE / "indep_prices"
PC.mkdir(parents=True, exist_ok=True)
S = requests.Session()
S.headers.update({"User-Agent": UA_WEB, "Accept": "application/json,text/csv,*/*"})
LIM = RateLimiter(2.0)


def dot(t: str) -> str:
    return t.replace("-", ".")


def get(url, tries=4, timeout=25):
    for i in range(tries):
        LIM.wait()
        try:
            r = S.get(url, timeout=timeout)
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(2 ** i * 2)
                continue
            return r
        except requests.RequestException:
            time.sleep(2 ** i)
    return None


def stooq_probe():
    url = "https://stooq.com/q/d/l/?s=nvda.us&i=d&d1=20260918&d2=20260926"
    r = get(url)
    txt = r.text if r is not None else ""
    (PC / "stooq_probe_nvda.txt").write_text(txt[:5000], encoding="utf-8")
    challenged = ("verify your browser" in txt.lower()) or ("__verify" in txt)
    is_csv = txt.startswith("Date,") or txt.startswith("Data,")
    return {"url": url, "http_status": None if r is None else r.status_code, "is_csv": is_csv,
            "bot_challenge": challenged, "retrieved_utc": utc_now_iso()}


CBOE_LIM = RateLimiter(0.4)   # Cboe's Cloudflare returned error 1015 (rate limited) at 2 req/s -> 1 request / 2.5 s
CBOE_STATE = {"consecutive_429": 0, "aborted": False}


def cboe_get(url):
    """Polite Cboe fetch: on HTTP 429 (Cloudflare 1015) cool down 90 s; abort Cboe after 3 consecutive 429s."""
    for _ in range(3):
        if CBOE_STATE["aborted"]:
            return None
        CBOE_LIM.wait()
        try:
            r = S.get(url, timeout=25)
        except requests.RequestException:
            time.sleep(5)
            continue
        if r.status_code == 429:
            CBOE_STATE["consecutive_429"] += 1
            if CBOE_STATE["consecutive_429"] >= 3:
                CBOE_STATE["aborted"] = True
                print("Cboe: repeated 429 (rate limited) -> stopping Cboe pulls", flush=True)
                return r
            time.sleep(90)
            continue
        CBOE_STATE["consecutive_429"] = 0
        return r
    return None


def cboe_all(tickers):
    rows = []
    for tk in tickers:
        fp = PC / f"cboe_{tk}.json"
        d = json.loads(fp.read_text(encoding="utf-8")) if fp.exists() else None
        if d is None or (d.get("_http") != 200 and not CBOE_STATE["aborted"]):
            url = f"https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/{dot(tk)}.json"
            r = cboe_get(url)
            d = {"_http": None if r is None else r.status_code, "_url": url, "_retrieved_utc": utc_now_iso()}
            if r is not None and r.status_code == 200:
                try:
                    d.update(r.json())
                except ValueError:
                    d["_text"] = r.text[:300]
            elif r is not None:
                d["_text"] = r.text[:300]
            fp.write_text(json.dumps(d), encoding="utf-8")
        q = d.get("data") or {}
        rows.append({"ticker": tk, "cboe_close": q.get("close"), "cboe_prev_close": q.get("prev_day_close"),
                     "cboe_last_trade_time": q.get("last_trade_time"), "cboe_timestamp": d.get("timestamp"),
                     "cboe_http": d.get("_http"), "cboe_retrieved_utc": d.get("_retrieved_utc")})
    return pd.DataFrame(rows)


def cnbc_all(tickers, batch=20):
    rows = []
    for i in range(0, len(tickers), batch):
        chunk = tickers[i:i + batch]
        fp = PC / f"cnbc_{i:04d}.json"
        if fp.exists():
            d = json.loads(fp.read_text(encoding="utf-8"))
        else:
            syms = "%7C".join(dot(t) for t in chunk)
            url = ("https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=" + syms +
                   "&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=0&output=json&events=0")
            r = get(url)
            d = {"_http": None if r is None else r.status_code, "_retrieved_utc": utc_now_iso(), "_chunk": chunk}
            if r is not None and r.status_code == 200:
                try:
                    d.update(r.json())
                except ValueError:
                    d["_text"] = r.text[:300]
            fp.write_text(json.dumps(d), encoding="utf-8")
        quotes = ((d.get("FormattedQuoteResult") or {}).get("FormattedQuote")) or []
        for q in quotes:
            sym = (q.get("symbol") or "").replace(".", "-")
            rows.append({"ticker": sym, "cnbc_last": q.get("last"), "cnbc_last_time": q.get("last_time"),
                         "cnbc_prev_close": q.get("previous_day_closing"), "cnbc_exchange": q.get("exchange"),
                         "cnbc_sharesout": q.get("sharesout"), "cnbc_mktcap": q.get("mktcapView"),
                         "cnbc_eps_ttm": q.get("eps"), "cnbc_pe": q.get("pe"), "cnbc_feps": q.get("feps"),
                         "cnbc_fpe": q.get("fpe"), "cnbc_code": q.get("code"),
                         "cnbc_retrieved_utc": d.get("_retrieved_utc")})
    return pd.DataFrame(rows)


def num(s):
    if s is None:
        return None
    try:
        return float(str(s).replace(",", "").replace("$", ""))
    except ValueError:
        return None


def main():
    u = pd.read_csv(DATA / "d4_universe.csv")
    tickers = u["ticker"].tolist()
    t0 = utc_now_iso()
    probe = stooq_probe()
    print("stooq probe:", probe)
    cn = cnbc_all(tickers)
    print("cnbc rows", len(cn))
    cb = cboe_all(tickers)
    print("cboe rows", len(cb), "with close", cb["cboe_close"].notna().sum())
    df = u[["ticker"]].merge(cb, on="ticker", how="left").merge(cn, on="ticker", how="left")
    for c in ["cnbc_last", "cnbc_prev_close", "cnbc_eps_ttm", "cnbc_pe", "cnbc_feps", "cnbc_fpe"]:
        df[c] = df[c].map(num)
    out = DATA / "d4_indep_prices.csv"
    df.to_csv(out, index=False)
    write_meta(out, {
        "source_urls": ["https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/<SYM>.json",
                        "https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=<A|B|...>",
                        "https://stooq.com/q/d/l/?s=<sym>.us&i=d (blocked by JS bot challenge; not used)"],
        "retrieval_utc_start": t0, "retrieval_utc_end": utc_now_iso(),
        "rows": int(len(df)), "columns": list(df.columns),
        "coverage": {"cboe_close": int(df["cboe_close"].notna().sum()), "cnbc_last": int(df["cnbc_last"].notna().sum())},
        "stooq_probe": probe,
        "caveats": ["Cboe/CNBC are delayed-quote vendor feeds, not exchange-certified official closes.",
                    "CNBC feps/fpe horizon is undocumented (vendor: LSEG); used only as a descriptive comparator.",
                    "Retrieved minutes after the 2026-09-25 close; 'close' fields checked against 16:00 ET timestamps."],
    })
    print("written", out, len(df))


if __name__ == "__main__":
    main()
