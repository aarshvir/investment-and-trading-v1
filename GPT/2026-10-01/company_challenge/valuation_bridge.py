"""Reproduce prior scenarios and quantify their dependence on exit multiples.

All prices are September 30 completed regular-session observations supplied by
the parallel market audit; this script does not fetch or independently certify
prices. The scenario forecasts are inherited assumptions, not forecasts proven
by the SEC filings archived alongside this script.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[2]
MODEL = json.loads((WORKSPACE / "review/ready/decision_model.json").read_text(encoding="utf-8"))
PRICES = {"AMP": 492.35, "PAYX": 98.50, "MSFT": 512.90, "NVDA": 228.38}
NORMALIZED_EPS = {"AMP": 44.0, "PAYX": 5.85, "MSFT": 16.66303501945525, "NVDA": 2.1782672431542105 * 4}
SBC_NOTE = {"AMP": "Buyback effect is embedded in per-share EPS growth, no separate yield.",
            "PAYX": "Company-adjusted EPS is not economic EPS; $5.85 anchor includes a $0.10 integration cost allowance.",
            "MSFT": "GAAP operating-income anchor retains SBC; investment gains removed.",
            "NVDA": "Quarter core EPS annualized fourfold only to label entry P/E; fiscal-year forecast differs."}


def irr(price: float, terminal: float, dividends: list[float], tax: float = .30, cost: float = .0025) -> float:
    # 25 bp entry and exit proportional trading cost, dividends at year ends.
    cashflows = [-price * (1 + cost)] + [d * (1 - tax) for d in dividends]
    cashflows[-1] += terminal * (1 - cost)
    lo, hi = -0.99, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        pv = sum(c / (1 + mid) ** t for t, c in enumerate(cashflows))
        if pv > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def ceiling(terminal: float, dividends: list[float], hurdle: float, tax=.30, cost=.0025) -> float:
    pv = sum(d * (1 - tax) / ((1 + hurdle) ** t) for t, d in enumerate(dividends, 1))
    pv += terminal * (1 - cost) / (1 + hurdle) ** 3
    return pv / (1 + cost)


results = []
for row in MODEL["stocks"]:
    symbol = row["ticker"]
    if symbol not in PRICES:
        continue
    price = PRICES[symbol]
    eps0 = NORMALIZED_EPS[symbol]
    base = next(s for s in row["scenarios"] if s["name"] == "base")
    bear = next(s for s in row["scenarios"] if s["name"] == "bear")
    initial_multiple = price / eps0
    no_rerating_terminal = base["terminal_eps"] * initial_multiple
    chosen_terminal = base["terminal_price"]
    hurdle = row["hurdle"]
    pv_dividends = sum(d * .70 / ((1 + hurdle) ** t) for t, d in enumerate(base["dividends"], 1))
    required_terminal = (price * 1.0025 - pv_dividends) * (1 + hurdle) ** 3 / .9975
    results.append({
        "ticker": symbol,
        "sep30_price_usd": price,
        "normalized_eps_baseline_usd": eps0,
        "entry_normalized_pe": initial_multiple,
        "base_exit_pe": base["terminal_pe"],
        "multiple_change_pct": base["terminal_pe"] / initial_multiple - 1,
        "base_terminal_eps": base["terminal_eps"],
        "base_terminal_price_usd": chosen_terminal,
        "base_after_tax_cost_irr": irr(price, chosen_terminal, base["dividends"]),
        "no_rerating_terminal_price_usd": no_rerating_terminal,
        "no_rerating_after_tax_cost_irr": irr(price, no_rerating_terminal, base["dividends"]),
        "no_rerating_hurdle_ceiling_usd": ceiling(no_rerating_terminal, base["dividends"], hurdle),
        "required_exit_pe_to_clear_hurdle": required_terminal / base["terminal_eps"],
        "five_pct_terminal_eps_miss_irr": irr(price, chosen_terminal * .95, base["dividends"]),
        "one_turn_lower_exit_pe_irr": irr(price, base["terminal_eps"] * (base["terminal_pe"] - 1), base["dividends"]),
        "bear_after_tax_cost_irr": irr(price, bear["terminal_price"], bear["dividends"]),
        "hurdle": hurdle,
        "assumption_note": SBC_NOTE[symbol],
    })

(ROOT / "valuation_bridge.json").write_text(json.dumps({"data_cutoff": "2026-09-30 US regular close", "method": "Annual dividend cash flows; 30% dividend withholding; 25bp cost on entry and exit. No-rerating uses Sep30 price divided by normalized starting EPS as fixed exit P/E.", "rows": results}, indent=2), encoding="utf-8")
for r in results:
    print(r["ticker"], "entryPE", round(r["entry_normalized_pe"], 2), "exitPE", r["base_exit_pe"], "base", round(100*r["base_after_tax_cost_irr"],2), "flatPE", round(100*r["no_rerating_after_tax_cost_irr"],2), "bear", round(100*r["bear_after_tax_cost_irr"],2), "flatPEceiling", round(r["no_rerating_hurdle_ceiling_usd"],2))
