"""Freeze an explicit judgment on every v011 proposed holding as a research slate."""
import csv
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
with zipfile.ZipFile(ROOT / "versions/v011_2026-09-27_claude/package.zip") as z:
    model = json.loads(z.read("v4/outputs/lead_portfolio_build.json"))
q = {r["ticker"]: r for r in csv.DictReader((HERE / "MARKET_RECONCILIATION.csv").open(newline="", encoding="utf-8"))}
c = {x["t"]: x for x in model["candidates"]}
issues = {
    "WEC": ("CUT_LARGE_SHADOW_WEIGHT", "8.32% all-stock weight lacks validated distributable-cash bridge; issuer annual dividend run-rate is $3.81 rather than archived $3.53; exit P/E sensitivity is large."),
    "LVS": ("CUT_RERATING_DEPENDENCE", "Archived 37.47% base annual case becomes about 9.81% gross with current P/E held at exit; Macau/Singapore capex bridge and exit multiple unresolved."),
    "ADP": ("REBUILD_CASH_VALUATION", "Archived free-cash-flow proxy omits $468.5m FY2026 intangible investment cash outflow; September 30 peer flat-P/E case only 10.51% after assumed tax/cost."),
    "LH": ("REBUILD_CASH_AND_REIMBURSEMENT", "H1 $384.4m FCF versus FY2026 $1.24-1.36bn guide demands strong H2; adjusted/GAAP gap and reimbursement risk remain."),
    "RSG": ("REBUILD_REVERSE_DCF", "Archived reverse DCF mixes equity FCF with enterprise WACC; September 30 flat-P/E thought experiment 8.65% under assumed growth."),
    "TJX": ("REBUILD_REVERSE_DCF", "Cost of equity minus earnings yield is not a valid implied growth rate without payout and reinvestment; lease-adjusted leverage definition needs consistency."),
    "PGR": ("DISCARD_BAD_ESTIMATE", "Malformed inherited FY1 EPS $1,012 cannot feed valuation; underwrite premiums, combined ratio, reserves and capital from filings."),
}
rows = []
for ticker in sorted(model["selected"], key=lambda t: -model["weights"][t]):
    row = c[ticker]
    status, reason = issues.get(ticker, ("RETAIN_RESEARCH_ONLY", "Archived dossier is a candidate record, but no newly validated comparable after-cost, no-rerating purchase case authorizes new capital."))
    rows.append({
        "ticker": ticker, "name": row["n"], "sector": row["s"],
        "v011_all_stock_weight_pct": round(100 * model["weights"][ticker], 3),
        "sep30_reference_close_usd": q[ticker]["yahoo_regular_close"],
        "quote_status": q[ticker]["quote_status"],
        "v011_base_scenario_unadjusted": row["base"],
        "shadow_research_action": status,
        "whole_portfolio_action": "DO_NOT_IMPLEMENT_V011_100PCT_EQUITY_UNDER_EXISTING_MANDATE",
        "new_money_weight_pct": 0,
        "reason": reason,
        "personal_hold_sell_action": "UNKNOWN_ACTUAL_HOLDINGS_AND_TAX_LOTS",
    })
with (HERE / "V011_SHADOW_REVIEW.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
assert len(rows) == 20
print(json.dumps({"reviewed": len(rows), "priority_repairs": sum(r["shadow_research_action"] != "RETAIN_RESEARCH_ONLY" for r in rows)}))
