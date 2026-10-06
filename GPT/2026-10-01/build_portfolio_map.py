"""Transparent allocation scenarios; scenario outputs are not expected returns."""
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
repriced = json.loads((HERE / "SCENARIO_REPRICE.json").read_text(encoding="utf-8"))
stocks = {r["ticker"]: r for r in repriced["results"]}

def stock_endpoint(ticker, case, no_rerating=False):
    stock = stocks[ticker]
    c = next(x for x in stock["cases"] if x["case"] == case)
    terminal = c["terminal_price"]
    if no_rerating:
        assert case == "base" and ticker in ("AMP", "PAYX")
        anchor = {"AMP": 44, "PAYX": 5.85}[ticker]
        terminal = c["terminal_eps"] * stock["close_sep30"] / anchor
    return (terminal * .9975 + sum(c["annual_dividends"]) * .70) / (stock["close_sep30"] * 1.0025)

allocations = {
    "reserve_only": {"index": 0, "direct": {}, "reserve": 1},
    "fifteen_index_no_direct_reference": {"index": .15, "direct": {}, "reserve": .85},
    "prior_starter_if_all_gates_pass": {"index": .15, "direct": {"AMP": .02, "PAYX": .02}, "reserve": .81},
    "index_only_same_19pct_equity": {"index": .19, "direct": {}, "reserve": .81},
    "full_equity_budget_all_index": {"index": .25, "direct": {}, "reserve": .75},
    "prior_full_direct_hypothetical_at_sep30": {"index": .15, "direct": {"AMP": .02, "PAYX": .02, "MSFT": .02, "NVDA": .015, "ALLE": .015, "HIG": .01}, "reserve": .75},
}
index_annual = {"bear": -.08, "base": .06, "bull": .12}
reserve_annual = {"bear": .025, "base": .035, "bull": .045}
output = []
for name, a in allocations.items():
    equity = a["index"] + sum(a["direct"].values())
    assert abs(equity + a["reserve"] - 1) < 1e-12
    cases = {}
    for case in ("bear", "base", "bull"):
        gross = a["index"] * (1 + index_annual[case]) ** 3
        gross += a["reserve"] * (1 + reserve_annual[case]) ** 3
        gross += sum(weight * stock_endpoint(ticker, case) for ticker, weight in a["direct"].items())
        cases[case] = {"ending_wealth_per_dollar": gross, "3yr_cagr": gross ** (1 / 3) - 1}
    if name == "prior_starter_if_all_gates_pass":
        gross = a["index"] * (1 + index_annual["base"]) ** 3
        gross += a["reserve"] * (1 + reserve_annual["base"]) ** 3
        gross += sum(weight * stock_endpoint(ticker, "base", True) for ticker, weight in a["direct"].items())
        cases["base_no_stock_rerating"] = {"ending_wealth_per_dollar": gross, "3yr_cagr": gross ** (1 / 3) - 1}
    # Deliberately correlated shocks, not a fitted distribution or maximum-loss bound.
    stress = {
        "equity_selloff_pct": -100 * (a["index"] * .30 + sum(a["direct"].values()) * .40),
        "severe_correlated_pct": -100 * (a["index"] * .50 + sum(a["direct"].values()) * .60 + a["reserve"] * .01),
        "tail_constructed_pct": -100 * (a["index"] * .60 + sum(a["direct"].values()) * .75 + a["reserve"] * .02),
    }
    output.append({"name": name, "weights": a, "total_equity": equity, "cases": cases, "stress": stress,
                   "status": "funded only if conditions pass" if name == "prior_starter_if_all_gates_pass" else ("non_executable_shadow" if "hypothetical" in name else "allocation_reference")})
(HERE / "PORTFOLIO_MAP.json").write_text(json.dumps({
    "prepared_utc": datetime.now(timezone.utc).isoformat(),
    "quote_cutoff": "2026-09-30 US regular session",
    "basis": "v012 company scenarios unchanged, repriced to Yahoo September 30 public closes; 30% dividend withholding and 25bp stock entry/exit; dividends held as cash; index and reserve annual assumptions from v012; fund fees, FX, capital-gains tax and fixed fees excluded.",
    "warning": "Illustrative assumptions, not calibrated probabilities, account-return forecast or a loss bound. Several conditional positions exceed entry limits at the September 30 close.",
    "recommended_allocation_id": "full_equity_budget_all_index",
    "allocations": output}, indent=2), encoding="utf-8")
print(json.dumps({r["name"]: {"base_pct": round(r["cases"]["base"]["3yr_cagr"]*100,2), "severe_stress_pct":round(r["stress"]["severe_correlated_pct"],2)} for r in output}, indent=2))
