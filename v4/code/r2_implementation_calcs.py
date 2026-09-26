"""r2_implementation_calcs.py  --  agent R2 (implementation / cross-border tax facts)

Illustrative arithmetic ONLY (not tax or investment advice) for a UAE-resident,
non-US-citizen, non-US-domiciled individual (US "nonresident alien", NRA).

Inputs are hard-coded from primary sources cited in
v4/outputs/r2_implementation_facts.md (retrieved 2026-09-26 UTC):
  * IRC s.2001(c) rate schedule; IRC s.2102(b)(1) credit USD 13,000;
    Form 706-NA filing threshold USD 60,000 (Instr. Form 706-NA, Rev. 09/2025).
  * S&P 500 index dividend yield 1.11% (State Street SPY5 factsheet, data 31-Aug-2026);
    sensitivity 1.05% (multpl.com estimate 24-Sep-2026) and 1.31% (VOO 2025 distributions
    USD 7.068 / 31-Dec-2024 close USD 538.81, Yahoo Finance).
  * Fund costs from issuer factsheets (VOO 0.03%; CSPX 0.07%; VUAA 0.07%; SPY5 0.03%;
    SPXS 0.05% ongoing charge + 0.07% swap fee embedded in swap return).
  * Withholding: 30% on US-source dividends to a UAE resident (no US-UAE treaty);
    15% at fund level for Irish physical UCITS (US-Ireland treaty, IRS Tax Treaty Table 1);
    ~0% for the swap-based UCITS under the s.871(m) qualified-index exception
    (Treas. Reg. s.1.871-15(l)) -- regulatory, can change.

Outputs (written next to the report):
  v4/outputs/r2_estate_tax_scenarios.csv (+ .meta.json)
  v4/outputs/r2_tax_drag.csv (+ .meta.json)
Prints markdown tables to stdout.
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

V4 = Path(__file__).resolve().parents[1]
OUT = V4 / "outputs"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- US estate tax
# IRC s.2001(c): (lower bound, base tax at lower bound, marginal rate)
SCHEDULE = [
    (0, 0, 0.18),
    (10_000, 1_800, 0.20),
    (20_000, 3_800, 0.22),
    (40_000, 8_200, 0.24),
    (60_000, 13_000, 0.26),
    (80_000, 18_200, 0.28),
    (100_000, 23_800, 0.30),
    (150_000, 38_800, 0.32),
    (250_000, 70_800, 0.34),
    (500_000, 155_800, 0.37),
    (750_000, 248_300, 0.39),
    (1_000_000, 345_800, 0.40),
]
NRA_CREDIT = 13_000          # IRC s.2102(b)(1)
FILING_THRESHOLD = 60_000    # Instructions for Form 706-NA (Rev. 09/2025)


def tentative_tax(x: float) -> float:
    lo, base, rate = max((b for b in SCHEDULE if x >= b[0]), key=lambda b: b[0])
    return base + rate * (x - lo)


def nra_estate_tax(us_situs_taxable: float) -> float:
    """Illustrative: no deductions, no prior taxable gifts, no treaty (UAE has none)."""
    return max(0.0, tentative_tax(us_situs_taxable) - NRA_CREDIT)


# sanity checks of schedule continuity (each bracket base must equal previous bracket's top)
for (lo1, b1, r1), (lo2, b2, _) in zip(SCHEDULE, SCHEDULE[1:]):
    assert abs(b1 + r1 * (lo2 - lo1) - b2) < 1e-6, (lo1, lo2)
assert tentative_tax(60_000) == 13_000 and nra_estate_tax(60_000) == 0
assert nra_estate_tax(80_000) == 5_200 and nra_estate_tax(100_000) == 10_800

# ---------------------------------------------------------------- vehicles
YIELD_BASE = 0.0111
YIELDS = {"1.05% (multpl est. 24-Sep-2026)": 0.0105,
          "1.11% (SSGA factsheet 31-Aug-2026)": 0.0111,
          "1.31% (VOO 2025 distributions / start price)": 0.0131}
VEHICLES = [
    # name, domicile, annual fund cost (TER + embedded swap fee), US dividend WHT borne, US-situs?
    ("VOO (US ETF) held directly by UAE resident", "US", 0.0003, 0.30, True),
    ("CSPX (iShares, Irish, physical, Acc)", "IE", 0.0007, 0.15, False),
    ("VUAA (Vanguard, Irish, physical, Acc)", "IE", 0.0007, 0.15, False),
    ("SPY5 (SPDR, Irish, physical, Dist)", "IE", 0.0003, 0.15, False),
    ("SPXS (Invesco, Irish, synthetic, Acc)", "IE", 0.0005 + 0.0007, 0.00, False),
]


def main() -> None:
    lines: list[str] = []
    p = lines.append

    # 1) estate-tax ladder
    p("### Estate-tax ladder (US-situs value at death; no deductions/gifts)\n")
    p("| US-situs value | Tentative tax s.2001(c) | Less credit | US estate tax | Effective rate on total | Form 706-NA required? |")
    p("|---:|---:|---:|---:|---:|:--|")
    for v in [50_000, 60_000, 70_000, 80_000, 90_000, 100_000, 150_000, 200_000]:
        tt = tentative_tax(v)
        tax = nra_estate_tax(v)
        p(f"| ${v:,.0f} | ${tt:,.0f} | ${min(tt, NRA_CREDIT):,.0f} | ${tax:,.0f} | {tax / v:.1%} | {'Yes' if v > FILING_THRESHOLD else 'No (<= $60k)'} |")
    p("")

    # 2) scenario grid
    rows = []
    for total in (50_000, 100_000):
        for stock_share in (0.0, 0.25, 0.5, 0.75, 1.0):
            for index_vehicle in ("US ETF (e.g., VOO)", "Irish UCITS physical (e.g., CSPX/VUAA)"):
                if stock_share == 1.0 and index_vehicle.startswith("Irish"):
                    continue  # identical to US-ETF row (no index sleeve)
                stocks = total * stock_share
                index = total - stocks
                us_index = index_vehicle.startswith("US")
                us_situs = stocks + (index if us_index else 0.0)
                tax = nra_estate_tax(us_situs)
                wht_index = 0.30 if us_index else 0.15
                ter_index = 0.0003 if us_index else 0.0007
                # stock sleeve yield: placeholder = index yield (replace with actual holdings' yields)
                wht_cost = stocks * YIELD_BASE * 0.30 + index * YIELD_BASE * wht_index
                fund_cost = index * ter_index
                rows.append({
                    "total_portfolio_usd": total,
                    "stock_sleeve_pct": stock_share,
                    "stock_sleeve_usd": stocks,
                    "index_sleeve_usd": index,
                    "index_vehicle": index_vehicle if index > 0 else "n/a (no index sleeve)",
                    "us_situs_usd": us_situs,
                    "form_706na_required": us_situs > FILING_THRESHOLD,
                    "illustrative_us_estate_tax_usd": round(tax, 2),
                    "estate_tax_pct_of_portfolio": round(tax / total, 4),
                    "annual_dividend_wht_usd_at_1.11pct": round(wht_cost, 2),
                    "annual_index_fund_cost_usd": round(fund_cost, 2),
                })
    grid = pd.DataFrame(rows)
    grid.to_csv(OUT / "r2_estate_tax_scenarios.csv", index=False)

    p("### Scenario grid (illustrative; stock-sleeve yield assumed = index yield 1.11%)\n")
    p("| Total | Stocks % | Index vehicle | US-situs | 706-NA? | Illustr. US estate tax | as % of total | Annual US-dividend WHT (1.11% yld) | Index fund cost/yr |")
    p("|---:|---:|:--|---:|:--:|---:|---:|---:|---:|")
    for r in rows:
        p(f"| ${r['total_portfolio_usd']:,.0f} | {r['stock_sleeve_pct']:.0%} | {r['index_vehicle']} | ${r['us_situs_usd']:,.0f} | "
          f"{'Yes' if r['form_706na_required'] else 'No'} | ${r['illustrative_us_estate_tax_usd']:,.0f} | {r['estate_tax_pct_of_portfolio']:.1%} | "
          f"${r['annual_dividend_wht_usd_at_1.11pct']:,.0f} | ${r['annual_index_fund_cost_usd']:,.0f} |")
    p("")

    # 3) tax drag table
    drag_rows = []
    for vname, dom, cost, wht, us in VEHICLES:
        for ylab, y in YIELDS.items():
            drag = y * wht
            drag_rows.append({"vehicle": vname, "domicile": dom, "us_situs_for_estate_tax": us,
                              "dividend_yield_assumption": ylab, "yield": y,
                              "wht_rate_effective": wht, "wht_drag_pct": drag,
                              "fund_cost_pct": cost, "all_in_pct": drag + cost,
                              "all_in_usd_per_50k": (drag + cost) * 50_000,
                              "all_in_usd_per_80k": (drag + cost) * 80_000,
                              "all_in_usd_per_100k": (drag + cost) * 100_000})
    drag_df = pd.DataFrame(drag_rows)
    drag_df.to_csv(OUT / "r2_tax_drag.csv", index=False)

    p("### Annual drag vs. gross S&P 500 total return (yield 1.11%)\n")
    p("| Vehicle | Dividend WHT borne | WHT drag | Fund cost | All-in drag | $/yr on $50k | $/yr on $80k | $/yr on $100k | US-situs? |")
    p("|:--|---:|---:|---:|---:|---:|---:|---:|:--:|")
    for r in drag_rows:
        if r["yield"] != YIELD_BASE:
            continue
        p(f"| {r['vehicle']} | {r['wht_rate_effective']:.0%} | {r['wht_drag_pct']:.3%} | {r['fund_cost_pct']:.2%} | {r['all_in_pct']:.3%} | "
          f"${r['all_in_usd_per_50k']:,.0f} | ${r['all_in_usd_per_80k']:,.0f} | ${r['all_in_usd_per_100k']:,.0f} | {'Yes' if r['us_situs_for_estate_tax'] else 'No'} |")
    p("")
    p("Sensitivity of VOO-vs-CSPX all-in gap to the yield assumption:")
    for ylab, y in YIELDS.items():
        gap = (y * 0.30 + 0.0003) - (y * 0.15 + 0.0007)
        p(f"- {ylab}: gap {gap:.3%}/yr = ${gap * 80_000:,.0f}/yr on $80k")
    p("")

    # 4) one-off costs
    p("### One-off trading-cost examples (list prices; excludes spreads, exchange/regulatory fees)\n")
    for amt in (50_000, 80_000, 100_000):
        ibkr_us_fixed = 1.00  # USD 0.005/share -> < USD 1 for orders <= USD 100k if VOO price > USD 500 -> USD 1.00 minimum
        lse_fixed = max(4.0, 0.0005 * amt)
        lse_tiered = min(39.0, max(1.70, 0.0005 * amt))
        vested_basic = min(35.0, 0.0025 * amt)
        fx_ideal = max(2.0, 0.00002 * amt)
        fx_auto = 0.0003 * amt
        p(f"- ${amt:,.0f}: IBKR Pro Fixed US ETF ~${ibkr_us_fixed:.2f} (min); IBKR LSE USD line Fixed ${lse_fixed:,.2f} / Tiered ${lse_tiered:,.2f} (+venue fees); "
          f"Vested Basic ${vested_basic:,.2f}; IBKR FX (IdealPro) ${fx_ideal:,.2f} vs auto-conversion ~${fx_auto:,.2f}")
    p("")

    # 5) time for USD 50k to cross USD 60k
    p("### Years for a USD 50,000 US-situs holding to exceed USD 60,000 (constant growth)\n")
    for g in (0.05, 0.07, 0.10):
        p(f"- {g:.0%}/yr: {math.log(1.2) / math.log(1 + g):.1f} years")
    p("")

    md = "\n".join(lines)
    print(md)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    common_sources = [
        "https://www.law.cornell.edu/uscode/text/26/2001",
        "https://www.law.cornell.edu/uscode/text/26/2102",
        "https://www.irs.gov/instructions/i706na",
        "https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-spy5-gy.pdf",
        "https://www.multpl.com/s-p-500-dividend-yield",
        "https://www.irs.gov/pub/irs-lbi/tax-treaty-table-1.pdf",
    ]
    meta_grid = {
        "name": "r2_estate_tax_scenarios", "producer": "code/r2_implementation_calcs.py",
        "retrieved_utc": now, "rows": int(len(grid)), "columns": list(grid.columns),
        "sources": common_sources,
        "caveats": [
            "Illustrative arithmetic only; not tax advice.",
            "Assumes no deductions (s.2106), no prior taxable gifts, no marital/charitable deduction, no treaty.",
            "Stock-sleeve dividend yield set equal to index yield 1.11% as a placeholder.",
            "Assumes all individual stocks are US-incorporated (US-situs); foreign-incorporated US listings differ.",
            "Values are at date of death; USD 60k threshold is not inflation-indexed.",
        ],
    }
    meta_drag = {
        "name": "r2_tax_drag", "producer": "code/r2_implementation_calcs.py",
        "retrieved_utc": now, "rows": int(len(drag_df)), "columns": list(drag_df.columns),
        "sources": common_sources + [
            "https://fund-docs.vanguard.com/F0968.pdf",
            "https://www.ishares.com/uk/individual/en/literature/fact-sheet/cspx-ishares-core-s-p-500-ucits-etf-fund-fact-sheet-en-gb.pdf",
            "https://fund-docs.vanguard.com/SandP_500_UCITS_ETF_USD_Accumulating_9694_INT_OFF_ETF_EN.pdf",
            "https://www.invesco.com/content/dam/invesco/emea/en/product-documents/etf/share-class/factsheet/IE00B3YCGJ38_factsheet_en.pdf",
            "https://www.law.cornell.edu/cfr/text/26/1.871-15",
        ],
        "caveats": [
            "Drag = dividend yield x withholding rate borne + fund cost; excludes trading spreads, securities lending income, tracking error.",
            "SPXS cost includes the 0.07% swap fee that Invesco says is embedded in the swap return (not charged separately).",
            "Synthetic 0% WHT depends on the s.871(m) qualified-index exception (Treas. Reg. 1.871-15(l)); regulatory change risk.",
        ],
    }
    (OUT / "r2_estate_tax_scenarios.meta.json").write_text(json.dumps(meta_grid, indent=2), encoding="utf-8")
    (OUT / "r2_tax_drag.meta.json").write_text(json.dumps(meta_drag, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
