"""Comparable flat-multiple diagnostics for four Claude v011 candidates.

Growth assumptions are deliberately transparent thought experiments, not
independent forecasts or management promises. Excluding incremental buyback
yield prevents double counting expected per-share growth.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def irr(price: float, terminal: float, dividends: list[float], tax=.30, cost=.0025) -> float:
    cashflows = [-price * (1 + cost)] + [d * (1 - tax) for d in dividends]
    cashflows[-1] += terminal * (1 - cost)
    lo, hi = -.99, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        pv = sum(c / (1 + mid) ** t for t, c in enumerate(cashflows))
        if pv > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def ceiling(terminal: float, dividends: list[float], hurdle: float, tax=.30, cost=.0025) -> float:
    pv = sum(d * (1 - tax) / (1 + hurdle) ** t for t, d in enumerate(dividends, 1))
    pv += terminal * (1 - cost) / (1 + hurdle) ** 3
    return pv / (1 + cost)
CASES = [
    # price = dual-source US 2026-09-30 regular close from parallel market audit
    {"ticker": "ADP", "price": 258.06, "eps0": 10.94, "eps_definition": "FY2026 consolidated GAAP diluted EPS, year ended 2026-06-30", "g": .09, "div": 6.80, "eps_source": "https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm", "div_source": "https://investors.adp.com/news/news-details/2026/ADP-Declares-Regular-Quarterly-Dividend-a7157c3eb/default.aspx", "limitation": "9% EPS growth is analyst assumption, near lower end of management FY2027 adjusted EPS guidance; GAAP and adjusted definitions differ. Client-funds interest is rate sensitive."},
    {"ticker": "TJX", "price": 132.31, "eps0": 5.175, "eps_definition": "midpoint of FY2027 company adjusted EPS guidance excluding one-time tariff benefit", "g": .09, "div": 1.92, "eps_source": "https://www.sec.gov/Archives/edgar/data/109198/000010919826000045/tjxq2fy27earningspressrele.htm", "div_source": "https://investor.tjx.com/node/21541/html", "limitation": "9% adjusted EPS growth is analyst assumption; guidance excludes tariff benefit and forecast should be reduced if tariffs or Marmaxx comps worsen."},
    {"ticker": "RSG", "price": 209.87, "eps0": 7.255, "eps_definition": "midpoint of FY2026 company adjusted diluted EPS guidance", "g": .08, "div": 2.68, "eps_source": "https://www.sec.gov/Archives/edgar/data/1060391/000106039126000273/exhibit991q22026.htm", "div_source": "https://investor.republicservices.com/stock-information-and-dividends", "limitation": "8% adjusted EPS growth is analyst assumption; recurring acquisition spending, debt and capital intensity require a consistent equity FCF bridge."},
    {"ticker": "LH", "price": 308.11, "eps0": 18.325, "eps_definition": "midpoint of FY2026 company adjusted EPS guidance, reaffirmed 2026-09-10", "g": .10, "div": 2.88, "eps_source": "https://www.sec.gov/Archives/edgar/data/920148/000092014826000201/formpr091026ex991investord.htm", "div_source": "https://ir.labcorp.com/news-releases/news-release-details/labcorp-declares-quarterly-dividend-15", "limitation": "10% is midpoint of management 8.5–11.5% adjusted EPS growth outlook through FY2029, includes projected allocation; recurring acquisition amortization and low H1 FCF remain concerns."},
]
out = []
for x in CASES:
    eps3 = x["eps0"] * (1 + x["g"]) ** 3
    pe0 = x["price"] / x["eps0"]
    terminal = pe0 * eps3
    dividends = [x["div"]] * 3
    out.append({**x, "sep30_entry_pe": pe0, "fy2029_equivalent_eps": eps3,
                "flat_pe_terminal_price": terminal,
                "after_30pct_withholding_and_25bp_costs_flat_pe_irr": irr(x["price"], terminal, dividends),
                "illustrative_12pct_hurdle_ceiling_at_fixed_sep30_pe": ceiling(terminal, dividends, .12)})
(ROOT / "candidate_bridge.json").write_text(json.dumps({"basis": "Illustrative no-rerating diagnostics; 3 annual cash dividends, 30% dividend withholding and 25bp entry/exit costs; fiscal periods differ and no formal portfolio selection is inferred.", "rows": out}, indent=2), encoding="utf-8")
for x in out:
    print(x["ticker"], "entryPE", round(x["sep30_entry_pe"],2), "growth", str(round(x["g"]*100,1))+'%', "IRR", round(x["after_30pct_withholding_and_25bp_costs_flat_pe_irr"]*100,2), "ceiling",round(x["illustrative_12pct_hurdle_ceiling_at_fixed_sep30_pe"],2))
