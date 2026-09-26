"""
b2_run.py -- Agent B2 reference runs. Executes the "Runs to do now" in
v4/prompts/B2_risk_engine.md using v4/code/b2_risk.py and writes
v4/outputs/b2_reference_results.json. Run with:

  PYTHONPATH='C:\\Users\\user\\eqv4\\pylib' python b2_run.py
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import b2_risk as b2

V4 = Path(__file__).resolve().parents[1]
PROJECT = V4.parent
OUT_JSON = V4 / "outputs" / "b2_reference_results.json"

# ---------------------------------------------------------------------------
# Inputs: R1 scenarios (v4/data/r1_scenarios.csv) and the v3 conviction portfolio
# ---------------------------------------------------------------------------
SCENARIOS = {  # geometric (compound) nominal annual target; arithmetic_equiv = g + sigma^2/2, from R1
    "Bear": {"geo": 0.02, "arith": 0.0328},
    "Base": {"geo": 0.06, "arith": 0.0728},
    "Bull": {"geo": 0.09, "arith": 0.1028},
}
CASH_ANNUAL = 0.04
VOL_ASSUMPTION_1Y, VOL_ASSUMPTION_STRESS = 0.16, 0.195  # R1: 16% base, 19-20% stress

with open(PROJECT / "equity_project" / "conv_port.json") as f:
    conv = json.load(f)
V3_WEIGHTS_RAW = conv["w"]
wsum = sum(V3_WEIGHTS_RAW.values())
V3_WEIGHTS = {k: v / wsum for k, v in V3_WEIGHTS_RAW.items()}  # renormalise 4dp rounding to exactly 1.0
BLEND_5050 = {"SPY": 0.5, **{k: 0.5 * v for k, v in V3_WEIGHTS.items()}}
PROXIES_ABNB = {"ABNB": "BKNG"}

print(f"v3 weight sum before renorm: {wsum:.6f}; tickers: {list(V3_WEIGHTS)}")

prices = b2.load_prices()
sector_map = b2.load_sector_map()
spy_ret_full = prices["SPY"].pct_change().dropna()
N = 20000
SEED = 42

RESULTS = {
    "generated_utc": pd.Timestamp.utcnow().isoformat(),
    "data_cutoff": str(prices.index[-1].date()),
    "scenarios_source": "v4/data/r1_scenarios.csv (R1 complete)",
    "scenarios": SCENARIOS,
    "cash_annual": CASH_ANNUAL,
    "vol_assumption": {"base_1y": VOL_ASSUMPTION_1Y, "stress": VOL_ASSUMPTION_STRESS},
    "v3_weights_used": V3_WEIGHTS,
    "blend_50_50_weights": BLEND_5050,
    "flagged_ticks_disclosure": b2.flagged_ticks_for(list(V3_WEIGHTS) + ["SPY", "RSP", "BKNG"]),
}

PORTFOLIOS = {
    "SPY": (dict(SPY=1.0), {}),
    "RSP": (dict(RSP=1.0), {}),
    "v3_exclude": (V3_WEIGHTS, dict(missing="exclude")),
    "v3_proxy_BKNG": (V3_WEIGHTS, dict(missing="proxy", proxies=PROXIES_ABNB)),
    "blend_50_50": (BLEND_5050, dict(missing="exclude")),
}

# ---------------------------------------------------------------------------
# 1. risk_summary
# ---------------------------------------------------------------------------
t0 = time.time()
RESULTS["risk_summary"] = {}
for name, (w, _) in PORTFOLIOS.items():
    if name == "v3_proxy_BKNG":
        continue  # identical to v3_exclude: 3y/5y trailing window has real ABNB data either way
    RESULTS["risk_summary"][name] = b2.risk_summary(w, prices=prices, sector_map=sector_map)
print(f"[1/7] risk_summary done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
# 2. stress_tests
# ---------------------------------------------------------------------------
t0 = time.time()
RESULTS["stress_tests"] = {}
for name, (w, kw) in PORTFOLIOS.items():
    RESULTS["stress_tests"][name] = b2.stress_tests(w, prices=prices, **kw)
print(f"[2/7] stress_tests done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
# 3. COVID zero-fill / proxy / exclude reconciliation vs lead_v3_audit.md
# ---------------------------------------------------------------------------
t0 = time.time()
covid = ("2020-02-19", "2020-03-23")
recon = {}
for label, kw in [
    ("zero_fill_replication_of_lead", dict(missing="cash", cash_annual=0.0)),
    ("proxy_BKNG", dict(missing="proxy", proxies=PROXIES_ABNB)),
    ("exclude_renormalise", dict(missing="exclude")),
]:
    path = b2.portfolio_daily_path(V3_WEIGHTS, covid[0], covid[1], rebalance="M", prices=prices, **kw)
    recon[label] = path.summary()
recon["spy_return"] = float(prices["SPY"].loc[covid[1]] / prices["SPY"].loc[covid[0]] - 1)
recon["lead_reported"] = {"zero_fill": -0.362, "bkng_proxy": -0.401}
recon["external_review_reported"] = {"method_unstated_likely_zero_fill": -0.3615}
RESULTS["covid_reconciliation"] = recon
print(f"[3/7] COVID reconciliation done in {time.time()-t0:.1f}s: "
      f"exclude={recon['exclude_renormalise']['total_return']:.4f} "
      f"zero_fill={recon['zero_fill_replication_of_lead']['total_return']:.4f} "
      f"proxy={recon['proxy_BKNG']['total_return']:.4f}")

# ---------------------------------------------------------------------------
# 4. simulate_outcomes: Bear/Base/Bull for each portfolio, jointly bootstrapped vs SPY
# ---------------------------------------------------------------------------
t0 = time.time()
RESULTS["simulate_outcomes"] = {}
for name, (w, kw) in PORTFOLIOS.items():
    RESULTS["simulate_outcomes"][name] = {}
    sim_kw = {k: v for k, v in kw.items() if k in ("missing", "proxies")}
    for scen, vals in SCENARIOS.items():
        if name == "SPY":
            out = b2.simulate_outcomes(w, vals["geo"], n=N, seed=SEED, prices=prices, **sim_kw)
        else:
            out = b2.simulate_outcomes(w, vals["geo"], n=N, seed=SEED, prices=prices,
                                        benchmark_returns=spy_ret_full,
                                        benchmark_drift_annual=vals["geo"], **sim_kw)
        RESULTS["simulate_outcomes"][name][scen] = out
    print(f"    simulate_outcomes[{name}] done ({time.time()-t0:.1f}s elapsed)")
print(f"[4/7] simulate_outcomes done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
# 5. Block-length sensitivity (5 / 21 / 63), Base scenario, SPY & v3_exclude
# ---------------------------------------------------------------------------
t0 = time.time()
RESULTS["block_length_sensitivity"] = {}
for name in ["SPY", "v3_exclude"]:
    w, kw = PORTFOLIOS[name]
    sim_kw = {k: v for k, v in kw.items() if k in ("missing", "proxies")}
    RESULTS["block_length_sensitivity"][name] = b2.block_length_sensitivity(
        w, SCENARIOS["Base"]["geo"], n=N, seed=SEED, mean_blocks=(5, 21, 63), prices=prices, **sim_kw)
print(f"[5/7] block_length_sensitivity done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
# 5b. Robustness: restrict the v3 bootstrap pool to 2014-01-01+ (all 13 non-ABNB names already
# listed by then; only ABNB's Dec-2020 IPO gap remains), Base scenario, vs the full-1995+ pool.
# ---------------------------------------------------------------------------
t0 = time.time()
RESULTS["v3_bootstrap_pool_sensitivity_since2014"] = {}
for name in ["v3_exclude", "v3_proxy_BKNG"]:
    w, kw = PORTFOLIOS[name]
    sim_kw = {k: v for k, v in kw.items() if k in ("missing", "proxies")}
    RESULTS["v3_bootstrap_pool_sensitivity_since2014"][name] = b2.simulate_outcomes(
        w, SCENARIOS["Base"]["geo"], n=N, seed=SEED, prices=prices, start="2014-01-01",
        benchmark_returns=spy_ret_full, benchmark_drift_annual=SCENARIOS["Base"]["geo"], **sim_kw)
print(f"[5b/7] v3 since-2014 pool sensitivity done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
# 6. SPY unrecentred (raw historical drift) bootstrap + empirical drawdown frequency
# ---------------------------------------------------------------------------
t0 = time.time()
RESULTS["spy_unrecentred_bootstrap"] = b2.simulate_outcomes(spy_ret_full, drift_annual=None, n=N, seed=SEED)
RESULTS["spy_empirical_drawdown_frequency_1995_2026"] = b2.empirical_drawdown_frequency(
    prices["SPY"], horizons_years=[1, 3, 5], thresholds=[-0.15, -0.20])
print(f"[6/7] SPY sanity check done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
# 7. allocation_scenarios: SPY equity sleeve vs cash, Bear/Base/Bull
# ---------------------------------------------------------------------------
t0 = time.time()
RESULTS["allocation_scenarios_SPY"] = {}
for scen, vals in SCENARIOS.items():
    eq_adj = b2.recentre_arithmetic(spy_ret_full, vals["arith"])
    RESULTS["allocation_scenarios_SPY"][scen] = b2.allocation_scenarios(
        eq_adj, reserve_yield=CASH_ANNUAL, mixes=(1.0, 0.8, 0.7, 0.6, 0.5), n=N, seed=SEED)
print(f"[7/7] allocation_scenarios done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------------------
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, "w") as f:
    json.dump(RESULTS, f, indent=2, default=str)
print(f"Wrote {OUT_JSON} ({OUT_JSON.stat().st_size/1024:.0f} KB)")
