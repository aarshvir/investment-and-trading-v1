"""Predeclared simple defensive-name substitutions; six-crisis sensitivity only.

Not a selection optimizer and not a valuation or thesis approval. Reuses the
same quarterly-rebalanced Yahoo adjusted-close replay as stress_test.py.
"""

import datetime as dt
import hashlib
import json
import math
import pathlib
import time

import requests

OUT = pathlib.Path(__file__).resolve().parent
RAW = OUT / "raw_yahoo"
baseline = json.loads((OUT / "stress_diagnostics.json").read_text(encoding="utf-8"))
base = baseline["proposed_concentration"]["stock_weight_pct"]
new_names = ["PEP", "PG", "PEG", "SO", "PM"]
manifest = {}

for ticker in new_names:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    params = {"period1": int(dt.datetime(2005, 1, 1, tzinfo=dt.timezone.utc).timestamp()),
              "period2": int(dt.datetime(2026, 10, 1, tzinfo=dt.timezone.utc).timestamp()),
              "interval": "1d", "events": "div,splits", "includeAdjustedClose": "true"}
    result = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"}, timeout=35)
    result.raise_for_status()
    raw = result.content
    data = result.json()["chart"]["result"][0]
    meta = data["meta"]
    assert meta["symbol"] == ticker and meta["currency"] == "USD"
    (RAW / f"{ticker}.json").write_bytes(raw)
    manifest[ticker] = {"url": result.url, "sha256": hashlib.sha256(raw).hexdigest(),
                        "currency": meta["currency"], "symbol": meta["symbol"],
                        "points": len(data["timestamp"])}
    print(ticker, manifest[ticker]["points"], flush=True)
    time.sleep(.3)


def prices_for(ticker):
    data = json.loads((RAW / f"{ticker}.json").read_text(encoding="utf-8"))["chart"]["result"][0]
    return {dt.datetime.fromtimestamp(stamp, dt.timezone.utc).date().isoformat(): value
            for stamp, value in zip(data["timestamp"], data["indicators"]["adjclose"][0]["adjclose"])
            if value is not None and math.isfinite(value) and value > 0}


prices = {ticker: prices_for(ticker) for ticker in set(base) | set(new_names) | {"SPY"}}


def replay(weights, start, end, missing_to_spy=False):
    source = weights.copy()
    missing = {t: w for t, w in source.items() if start not in prices[t] or end not in prices[t]}
    for t in missing:
        del source[t]
    if missing_to_spy:
        source["SPY"] = source.get("SPY", 0) + sum(missing.values())
    total = sum(source.values())
    norm = {t: w / total for t, w in source.items()}
    days = sorted(set.intersection(*(set(prices[t]) for t in source)))
    days = [d for d in days if start <= d <= end]
    assert days[0] == start and days[-1] == end
    shares = {t: norm[t] / prices[t][start] for t in norm}
    max_value = 1
    worst = 0
    prev_q = (int(start[:4]), (int(start[5:7]) - 1) // 3)
    for d in days:
        value = sum(shares[t] * prices[t][d] for t in shares)
        max_value = max(max_value, value)
        worst = min(worst, value / max_value - 1)
        q = (int(d[:4]), (int(d[5:7]) - 1) // 3)
        if q != prev_q:
            shares = {t: value * norm[t] / prices[t][d] for t in norm}
            prev_q = q
    value = sum(shares[t] * prices[t][end] for t in shares)
    return {"return": value - 1, "max_drawdown": worst,
            "missing": missing, "coverage_weight_pct": total}


def swap(changes):
    result = base.copy()
    for old, new in changes:
        result[new] = result.get(new, 0) + result.pop(old)
    assert sum(result.values()) == 100
    return result


variants = {"baseline": base,
            "HIG_to_PG": swap([("HIG", "PG")]),
            "HIG_to_PEP": swap([("HIG", "PEP")]),
            "HIG_to_SO": swap([("HIG", "SO")]),
            "HIG_to_PEG": swap([("HIG", "PEG")]),
            "HIG_to_PM": swap([("HIG", "PM")]),
            "AMP_to_PG": swap([("AMP", "PG")]),
            "AMP_to_PEP": swap([("AMP", "PEP")]),
            "USB_to_PEG": swap([("USB", "PEG")]),
            "HIG_AMP_to_PG_PEP": swap([("HIG", "PG"), ("AMP", "PEP")]),
            "HIG_USB_to_PG_PEG": swap([("HIG", "PG"), ("USB", "PEG")]),
            "HIG_AMP_USB_to_PG_PEP_PEG": swap([("HIG", "PG"), ("AMP", "PEP"), ("USB", "PEG")])}

result = {"method": "Quarterly rebalance at target weights, Yahoo adjusted daily closes; missing original names omitted with remaining weights renormalized. SPY-missing proxy separately shown for GFC/2011, diagnostic only.",
          "manifest": manifest, "variants": {}}
for label, weights in variants.items():
    episodes = {}
    for e in baseline["episodes"]:
        ep = replay(weights, e["start"], e["end"])
        if e["episode"] in ("Global financial crisis", "US downgrade / euro crisis"):
            ep["missing_as_spy_sensitivity"] = replay(weights, e["start"], e["end"], missing_to_spy=True)
        episodes[e["episode"]] = ep
    result["variants"][label] = {"weights": weights, "episodes": episodes}
(OUT / "defensive_swap_diagnostics.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
for label, item in result["variants"].items():
    print(label, [(key, round(ep["return"] * 100, 2)) for key, ep in item["episodes"].items()])
