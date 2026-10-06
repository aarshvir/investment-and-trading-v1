"""Bounded, reproducible valuation sensitivities for the stock-only challenge.

These are conditional cash-flow IRRs, not return forecasts or odds.
"""
from __future__ import annotations

import json
from pathlib import Path


def irr(entry: float, terminal: float, annual_dividend: float, years: int = 3) -> float:
    """Annual IRR with annual dividends, 30% withholding and 25 bp each-side costs."""
    cash_in = entry * 1.0025
    div = annual_dividend * 0.70

    def npv(rate: float) -> float:
        return -cash_in + sum(div / ((1 + rate) ** t) for t in range(1, years + 1)) + terminal * 0.9975 / ((1 + rate) ** years)

    low, high = -0.99, 10.0
    for _ in range(160):
        mid = (low + high) / 2
        if npv(mid) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def main() -> None:
    rows = []
    # WEC: FY2026 EPS guidance midpoint $5.56; 7.5% annual EPS growth is a
    # management-target midpoint assumption, not a freely distributable FCF path.
    wec_eps_2029 = 5.56 * 1.075 ** 3
    for multiple in (18.25, 15.0, 13.0):
        rows.append({
            "ticker": "WEC", "entry_sep30": 100.78, "eps_anchor_period": "FY2026 guidance midpoint",
            "eps_anchor": 5.56, "annual_eps_growth_assumption": 0.075,
            "annual_dividend_constant": 3.81, "exit_multiple": multiple,
            "terminal_eps": wec_eps_2029,
            "terminal_price": wec_eps_2029 * multiple,
            "after_withholding_cost_irr": irr(100.78, wec_eps_2029 * multiple, 3.81),
        })
    # USB: bank-specific P/TBV sensitivity. The future tangible book growth
    # assumption must be checked after credit provisions and repurchases.
    usb_tbv_2029 = 30.04 * 1.06 ** 3
    for multiple in (1.92, 1.60, 1.30):
        rows.append({
            "ticker": "USB", "entry_sep30": 57.76, "book_anchor_period": "2026-06-30 tangible book value per share",
            "book_anchor": 30.04, "annual_tbv_growth_assumption": 0.06,
            "annual_dividend_constant": 2.16, "exit_price_to_tangible_book": multiple,
            "terminal_tangible_book": usb_tbv_2029,
            "terminal_price": usb_tbv_2029 * multiple,
            "after_withholding_cost_irr": irr(57.76, usb_tbv_2029 * multiple, 2.16),
        })
    # Defensive replacements: growth is an analyst extension past the first
    # guided year, and PG/PEP/PEG anchors are non-comparable non-GAAP bases.
    defensives = (
        ("PG", 145.28, 6.89, "FY2026 core EPS (FY2027 0-3% guide)", 0.02, 4.2589, 18.0),
        ("PEP", 126.72, 8.14 * 1.06, "FY2026 core EPS proxy: FY2025 core $8.14 x 1.06 midpoint guidance", 0.05, 5.92, 13.0),
        ("PEG", 67.34, 4.34, "FY2026 non-GAAP operating EPS guidance midpoint", 0.07, 2.68, 13.0),
    )
    for ticker, price, eps0, basis, growth, dividend, contract_pe in defensives:
        entry_pe = price / eps0
        terminal_eps = eps0 * (1 + growth) ** 3
        for multiple in (entry_pe, contract_pe):
            rows.append({
                "ticker": ticker, "entry_sep30": price,
                "eps_anchor_period": basis, "eps_anchor": eps0,
                "annual_eps_growth_assumption": growth,
                "annual_dividend_constant": dividend,
                "exit_multiple": multiple,
                "terminal_eps": terminal_eps,
                "terminal_price": terminal_eps * multiple,
                "after_withholding_cost_irr": irr(price, terminal_eps * multiple, dividend),
            })
    out = Path(__file__).with_name("forensic_sensitivities.json")
    out.write_text(json.dumps({
        "data_cutoff": "2026-09-30 completed US session",
        "method": "three annual dividends; 30% withholding; 25bp entry and exit costs; no capital gains tax, fees or FX",
        "purpose": "conditional multiple and tangible-book sensitivities, not calibrated forecasts",
        "rows": rows,
    }, indent=2) + "\n", encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
