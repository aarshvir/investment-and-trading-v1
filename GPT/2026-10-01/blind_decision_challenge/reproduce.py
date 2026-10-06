"""Independent arithmetic challenge to the immutable v012 AMP/PAYX cash flows.

This script intentionally consumes only v012 published model, the dated GPT market
reconciliation, and local arithmetic. Forecast assumptions are never represented
as observed facts. It does not alter either input.
"""

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MODEL = ROOT / "versions/v012_2026-09-27_codex/reports/review/ready/decision_model.json"
MARKET = ROOT / "GPT/2026-10-01/MARKET_RECONCILIATION.csv"
OUT = Path(__file__).with_name("calculations.json")


def irr(price, terminal, dividends, tax=0.30, entry_cost=0.0025, exit_cost=0.0025):
    cash = [d * (1 - tax) for d in dividends]
    cash[-1] += terminal * (1 - exit_cost)
    lo, hi = -0.99, 10.0
    for _ in range(150):
        r = (lo + hi) / 2
        pv = sum(c / (1 + r) ** (i + 1) for i, c in enumerate(cash))
        if pv > price * (1 + entry_cost):
            lo = r
        else:
            hi = r
    return (lo + hi) / 2


def ceiling(terminal, dividends, hurdle=0.12, tax=0.30, entry_cost=0.0025, exit_cost=0.0025):
    cash = [d * (1 - tax) for d in dividends]
    cash[-1] += terminal * (1 - exit_cost)
    return sum(c / (1 + hurdle) ** (i + 1) for i, c in enumerate(cash)) / (1 + entry_cost)


model = json.loads(MODEL.read_text(encoding="utf-8"))
market = {r["ticker"]: r for r in csv.DictReader(MARKET.open(encoding="utf-8", newline=""))}
results = []
for stock in model["stocks"]:
    ticker = stock["ticker"]
    if ticker not in {"AMP", "PAYX", "MSFT", "NVDA"}:
        continue
    price = float(market[ticker]["yahoo_regular_close"])
    base = next(s for s in stock["scenarios"] if s["name"] == "base")
    bear = next(s for s in stock["scenarios"] if s["name"] == "bear")
    dividends = base["dividends"]
    if ticker == "AMP":
        start_eps = 44.0
    elif ticker == "PAYX":
        start_eps = 5.85
    elif ticker == "MSFT":
        start_eps = stock["baseline"]["annual_normalized_eps"] if "annual_normalized_eps" in stock["baseline"] else None
    else:
        start_eps = None
    entry_pe = price / start_eps if start_eps else None
    terminal = base["terminal_eps"] * base["terminal_pe"]
    row = {
        "ticker": ticker,
        "price_sep30_usd": price,
        "prior_limit_usd": stock["limit_price"],
        "prior_hurdle": stock["hurdle"],
        "base_hurdle_ceiling_usd": ceiling(terminal, dividends, hurdle=stock["hurdle"]),
        "base_irr_at_price": irr(price, terminal, dividends),
        "base_irr_at_prior_limit": irr(stock["limit_price"], terminal, dividends),
        "bear_irr_at_price": irr(price, bear["terminal_price"], bear["dividends"]),
        "base_irr_5pct_terminal_eps_miss": irr(price, terminal * 0.95, dividends),
        "base_irr_one_pe_turn_lower": irr(price, base["terminal_eps"] * (base["terminal_pe"] - 1), dividends),
        "one_pe_turn_lower_hurdle_ceiling_usd": ceiling(base["terminal_eps"] * (base["terminal_pe"] - 1), dividends, hurdle=stock["hurdle"]),
        "five_pct_terminal_eps_miss_hurdle_ceiling_usd": ceiling(terminal * 0.95, dividends, hurdle=stock["hurdle"]),
        "joint_one_turn_and_five_pct_eps_miss_hurdle_ceiling_usd": ceiling(base["terminal_eps"] * 0.95 * (base["terminal_pe"] - 1), dividends, hurdle=stock["hurdle"]),
        "base_exit_pe": base["terminal_pe"],
        "sep30_start_pe": entry_pe,
        "base_exit_pe_change_pct": base["terminal_pe"] / entry_pe - 1 if entry_pe else None,
        "modeled_ceiling_buffer_at_sep30_pct": ceiling(terminal, dividends, hurdle=stock["hurdle"]) / price - 1,
        "parent_scenario_vintage": "v012 2026-09-27, unchanged operating forecasts",
    }
    if entry_pe:
        fixed_sep30_pe_terminal = base["terminal_eps"] * entry_pe
        row["fixed_sep30_pe_irr_at_sep30"] = irr(price, fixed_sep30_pe_terminal, dividends)
        row["fixed_sep30_pe_hurdle_ceiling_usd"] = ceiling(fixed_sep30_pe_terminal, dividends, hurdle=stock["hurdle"])
    results.append(row)

OUT.write_text(json.dumps({
    "model_sha256": hashlib.sha256(MODEL.read_bytes()).hexdigest(),
    "market_reconciliation_sha256": hashlib.sha256(MARKET.read_bytes()).hexdigest(),
    "method": "Three annual dividend cash flows, 30% withholding, 25bp entry and exit costs; Sep30 observed price, unchanged v012 forecast. Fixed-Sep30-P/E scenario is not a no-rerating scenario at any future lower entry price.",
    "results": results,
}, indent=2) + "\n", encoding="utf-8")
print(OUT)
