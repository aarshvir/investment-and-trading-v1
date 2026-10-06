"""Reconcile dated public prices and reprice the immutable v012 scenarios.

This is a prospective input snapshot, not a trading system. It never edits parents.
"""
from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PARENT = ROOT / "versions/v012_2026-09-27_codex/reports/review/ready/decision_model.json"
DATE = "2026-09-30"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def irr(price, terminal, dividends, withholding=.30, cost=.0025):
    flows = [-price * (1 + cost)]
    flows.extend(x * (1 - withholding) for x in dividends)
    flows[-1] += terminal * (1 - cost)
    lo, hi = -.99, 5.0
    def npv(r):
        return sum(flow / (1 + r) ** i for i, flow in enumerate(flows))
    if npv(lo) * npv(hi) > 0:
        return None
    for _ in range(120):
        mid = (lo + hi) / 2
        if npv(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def ceiling(terminal, dividends, hurdle=.12, withholding=.30, cost=.0025):
    pv = sum(div * (1 - withholding) / (1 + hurdle) ** year
             for year, div in enumerate(dividends, 1))
    pv += terminal * (1 - cost) / (1 + hurdle) ** len(dividends)
    return pv / (1 + cost)


def main():
    yahoo = read_json(OUT / "market_yahoo_2026-09-30.json")
    cboe = read_json(OUT / "market_quotes_2026-09-30.json")
    model = read_json(PARENT)
    assert yahoo["scope"] == 90 and yahoo["session_matched"] == 90
    assert cboe["scope"] == 90 and cboe["session_matched"] == 32
    y = {r["ticker"]: r for r in yahoo["records"]}
    c = {r["ticker"]: r for r in cboe["records"] if r.get("session_match")}
    rows = []
    for ticker in sorted(y):
        q = y[ticker]
        assert sha256(OUT / "raw_market" / f"yahoo_{ticker}.json") == q["raw_sha256"]
        dated = [r for r in q["rows"] if r["date_et"] == DATE]
        assert len(dated) == 1 and q["currency"] == "USD" and q["symbol"] == ticker
        yh = dated[0]
        assert yh["low"] <= yh["close"] <= yh["high"]
        cb = c.get(ticker)
        if cb:
            assert sha256(OUT / "raw_market" / f"{ticker}.json") == cb["raw_sha256"]
        diff = abs(yh["close"] / cb["close"] - 1) if cb else None
        rows.append({
            "ticker": ticker, "date_et": DATE, "currency": q["currency"],
            "yahoo_regular_close": round(yh["close"], 4),
            "yahoo_adjusted_close": round(yh["adjclose"], 4) if yh.get("adjclose") is not None else None,
            "yahoo_low": round(yh["low"], 4), "yahoo_high": round(yh["high"], 4),
            "yahoo_volume": yh["volume"], "yahoo_retrieved_utc": q["retrieved_utc"],
            "yahoo_url": q["url"], "yahoo_raw_sha256": q["raw_sha256"],
            "cboe_close": cb["close"] if cb else None,
            "cboe_last_trade_time": cb["last_trade_time"] if cb else None,
            "cboe_retrieved_utc": cb["retrieved_utc"] if cb else None,
            "cboe_url": cb["url"] if cb else None,
            "cboe_raw_sha256": cb["raw_sha256"] if cb else None,
            "relative_close_gap_pct": round(100 * diff, 5) if diff is not None else None,
            "quote_status": "two_public_feeds_agree_within_0.1pct" if diff is not None and diff <= .001 else ("single_public_feed_cboe_rate_limited" if cb is None else "conflict"),
        })
    assert len(rows) == 90 and len(c) == 32
    assert max(r["relative_close_gap_pct"] for r in rows if r["relative_close_gap_pct"] is not None) < .1
    with (OUT / "MARKET_RECONCILIATION.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

    old_stocks = {s["ticker"]: s for s in model["stocks"]}
    results = []
    for ticker, s in old_stocks.items():
        quote = next(x for x in rows if x["ticker"] == ticker)
        price = quote["yahoo_regular_close"]
        case_rows = []
        for case in s["scenarios"]:
            newirr = irr(price, case["terminal_price"], case["dividends"])
            check = irr(s["reference_price"], case["terminal_price"], case["dividends"])
            assert abs(check - case["irr_reference_after_30pct_withholding_25bp_costs"]) < 1e-10
            case_rows.append({
                "case": case["name"], "terminal_eps": case["terminal_eps"],
                "exit_pe": case["terminal_pe"], "terminal_price": case["terminal_price"],
                "annual_dividends": case["dividends"],
                "irr_after_30pct_withholding_25bp_entry_exit_at_sep30": newirr,
                "12pct_hurdle_ceiling_same_assumptions": ceiling(case["terminal_price"], case["dividends"]),
            })
        results.append({
            "ticker": ticker, "prior_action": s["decision"],
            "prior_limit": s["limit_price"], "prior_close": s["reference_price"],
            "close_sep30": price, "quote_status": quote["quote_status"],
            "price_passes_prior_limit": price <= s["limit_price"],
            "base_12pct_ceiling_same_assumptions": next(x["12pct_hurdle_ceiling_same_assumptions"] for x in case_rows if x["case"] == "base"),
            "cases": case_rows, "scenario_vintage": "v012 parent unchanged; earnings, growth, exit P/E and dividends NOT refreshed",
        })
    (OUT / "SCENARIO_REPRICE.json").write_text(json.dumps({
        "prepared_utc": datetime.now(timezone.utc).isoformat(),
        "source_model": str(PARENT.relative_to(ROOT)).replace("\\", "/"),
        "source_model_sha256": sha256(PARENT), "quote_date_et": DATE,
        "method": "Four annual cash-flow dates; 30% dividend withholding; 25bp entry and 25bp exit; 12% hurdle; personal capital-gains tax, FX and fixed fees excluded.",
        "results": results,
    }, indent=2), encoding="utf-8")
    print(json.dumps({"quotes": len(rows), "dual_source": len(c), "model_stocks": len(results), "max_diff_pct": max(r["relative_close_gap_pct"] for r in rows if r["relative_close_gap_pct"] is not None)}))


if __name__ == "__main__":
    main()
