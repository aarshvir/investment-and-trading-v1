"""Transparent, hindsight-biased historical stress diagnostic for proposed stock weights.

Reads the immutable v011 portfolio as comparator; downloads Yahoo adjusted daily
prices as a distinct historical market-data source. This is not an investable
backtest: it applies 2026 survivors and weights to prior crises, omits names
without pre-event prices, and excludes tax, withholding, slippage and fees.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import pathlib
import time
import zipfile

import requests


ROOT = pathlib.Path(__file__).resolve().parents[4]
OUT = pathlib.Path(__file__).resolve().parent
RAW = OUT / "raw_yahoo"
RAW.mkdir(parents=True, exist_ok=True)
ARCHIVE = ROOT / "versions/v011_2026-09-27_claude/package.zip"

SLATE = {
    "MSFT": 8, "AMP": 6, "NVDA": 4, "ADP": 6, "TJX": 6,
    "RSG": 5, "MA": 5, "MCK": 6, "STE": 5, "BALL": 4,
    "DOV": 5, "BR": 4, "AXP": 5, "USB": 4, "CRH": 5,
    "PTC": 4, "VEEV": 4, "GDDY": 4, "ALLE": 5, "HIG": 5,
}
assert sum(SLATE.values()) == 100

with zipfile.ZipFile(ARCHIVE) as zf:
    prior = json.loads(zf.read("v4/outputs/lead_portfolio.json"))
    prior_risk = json.loads(zf.read("v4/outputs/lead_risk_results.json"))
V011 = {row["t"]: row["w"] * 100 for row in prior["rows"]}
EPISODES = []
for x in prior_risk["stress"]:
    start, end = [s.strip() for s in x["dates"].split("→")]
    EPISODES.append((x["episode"], start, end, x))


def get_series(ticker: str):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    params = {
        "period1": int(dt.datetime(2005, 1, 1, tzinfo=dt.timezone.utc).timestamp()),
        "period2": int(dt.datetime(2026, 10, 1, tzinfo=dt.timezone.utc).timestamp()),
        "interval": "1d", "events": "div,splits", "includeAdjustedClose": "true",
    }
    last_error = None
    for attempt in range(4):
        try:
            response = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"}, timeout=35)
            if response.status_code in (429, 502, 503):
                last_error = f"HTTP {response.status_code}"
                time.sleep(2 * (attempt + 1))
                continue
            response.raise_for_status()
            raw = response.content
            data = response.json()["chart"]["result"][0]
            meta = data["meta"]
            if meta.get("symbol") != ticker or meta.get("currency") != "USD":
                raise ValueError(f"identity mismatch: {meta.get('symbol')} {meta.get('currency')}")
            stamps = data["timestamp"]
            adj = data["indicators"]["adjclose"][0]["adjclose"]
            series = {}
            for stamp, value in zip(stamps, adj):
                if value is not None and math.isfinite(value) and value > 0:
                    date = dt.datetime.fromtimestamp(stamp, dt.timezone.utc).date().isoformat()
                    series[date] = value
            (RAW / f"{ticker}.json").write_bytes(raw)
            return series, {"url": response.url, "sha256": hashlib.sha256(raw).hexdigest(),
                            "dates": len(series), "first": min(series), "last": max(series),
                            "identity": {k: meta.get(k) for k in ("symbol", "currency", "exchangeName", "instrumentType")}}
        except (requests.RequestException, KeyError, IndexError, ValueError) as exc:
            last_error = repr(exc)
            time.sleep(2 * (attempt + 1))
    return {}, {"error": last_error}


all_tickers = sorted(set(SLATE) | set(V011) | {"SPY"})
prices = {}
manifest = {}
for ticker in all_tickers:
    prices[ticker], manifest[ticker] = get_series(ticker)
    print(ticker, len(prices[ticker]), manifest[ticker].get("error", "ok"), flush=True)
    time.sleep(0.25)


def replay(weights: dict[str, float], start: str, end: str):
    # A name qualifies only if it has a quote at *both* endpoint sessions.
    available = {t: w for t, w in weights.items() if start in prices[t] and end in prices[t]}
    unavailable = {t: w for t, w in weights.items() if t not in available}
    total_weight = sum(available.values())
    if not available:
        return {"error": "no names priced"}
    session_dates = sorted(set.intersection(*(set(prices[t]) for t in available)))
    session_dates = [d for d in session_dates if start <= d <= end]
    if session_dates[0] != start or session_dates[-1] != end:
        raise ValueError(f"missing exact endpoints: {start} {end}")
    # Quarterly rebalance to target weights; no outside capital after inception.
    norm = {t: w / total_weight for t, w in available.items()}
    shares = {t: norm[t] / prices[t][start] for t in available}
    value0 = sum(shares[t] * prices[t][start] for t in available)
    high = value0
    worst = 0.0
    worst_date = start
    prev_quarter = (int(start[:4]), (int(start[5:7]) - 1) // 3)
    for date in session_dates:
        quarter = (int(date[:4]), (int(date[5:7]) - 1) // 3)
        value = sum(shares[t] * prices[t][date] for t in available)
        if quarter != prev_quarter:
            shares = {t: value * norm[t] / prices[t][date] for t in available}
            prev_quarter = quarter
        high = max(high, value)
        dd = value / high - 1
        if dd < worst:
            worst, worst_date = dd, date
    endpoint = sum(shares[t] * prices[t][end] for t in available)
    return {"episode_return": endpoint / value0 - 1, "worst_drawdown": worst,
            "worst_date": worst_date, "available_names": len(available),
            "missing_names_and_original_weight_pct": unavailable,
            "coverage_original_weight_pct": total_weight,
            "session_count": len(session_dates), "method": "quarterly target-weight rebalance; Yahoo adjusted close; missing names excluded/remaining weights renormalized"}


comparisons = []
for label, start, end, archived in EPISODES:
    comparisons.append({"episode": label, "start": start, "end": end,
                        "proposed": replay(SLATE, start, end),
                        "v011_replay_same_yahoo": replay(V011, start, end),
                        "v011_archived_sleeve_return": archived["sleeve"],
                        "v011_archived_spy_return": archived["spy"],
                        "spy_same_yahoo": replay({"SPY": 100}, start, end)})

sector_by_ticker = {r["t"]: r["s"] for r in prior["rows"]}
sector_by_ticker.update({"MSFT": "Information Technology", "AMP": "Financials",
                         "NVDA": "Information Technology", "ALLE": "Industrials",
                         "HIG": "Financials"})


def concentration(weights):
    by_sector = {}
    for ticker, weight in weights.items():
        by_sector[sector_by_ticker[ticker]] = by_sector.get(sector_by_ticker[ticker], 0) + weight
    hhi = sum((w / 100) ** 2 for w in weights.values())
    sector_hhi = sum((w / 100) ** 2 for w in by_sector.values())
    return {"names": len(weights), "total_weight_pct": sum(weights.values()),
            "max_name_pct": max(weights.values()), "top_five_pct": sum(sorted(weights.values(), reverse=True)[:5]),
            "effective_name_count": 1 / hhi, "sectors_pct": by_sector,
            "sector_effective_count": 1 / sector_hhi,
            "financials_pct": by_sector.get("Financials", 0),
            "technology_pct": by_sector.get("Information Technology", 0),
            "stock_weight_pct": weights}


result = {"data_cutoff": "2026-09-30 completed US session; historical adjusted prices from Yahoo public chart API fetched after that close",
          "proposed_concentration": concentration(SLATE),
          "v011_concentration": concentration(V011),
          "episodes": comparisons,
          "raw_manifest": manifest,
          "immutable_parent_sha256": hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
          "caveat": "Today-selected survivor replay; not a tradeable backtest or prospective risk bound. Yahoo adjusted close is gross total-return proxy; no withholding, FX, fees, taxes or corporate history validation."}
(OUT / "stress_diagnostics.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print("WROTE", OUT / "stress_diagnostics.json")
