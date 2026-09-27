# v4 — how to reproduce every number (runbook)

Data cutoff: US close 2026-09-25. All scripts are in `v4/code/`, all outputs in `v4/data/` and `v4/outputs/`.

## One command
- `python run_all.py --list` prints the canonical run order (the table below, as code).
- `python run_all.py` re-derives every published number offline, in about 10 minutes. It runs the checks (B2 unit tests, B1 look-ahead tests, the independent daily-drawdown check), then the lead stages: portfolio → risk → views → report → dashboard.
- `python run_all.py --stages all` re-runs everything from the D1 downloads (network; anything downloaded after 2026-09-25 will differ).
- Exact library versions: `requirements.txt` (Python 3.11.9). Install with `python -m pip install --target C:\Users\user\eqv4\pylib -r requirements.txt`.
- **Freshness guard:** `lead_build_portfolio.py` records a sha256 manifest of every input: scores, valuation table, live snapshot, calibration, verdict JSONs and dossiers. `lead_risk.py`, `lead_views.py`, `lead_report_sections.py` and `lead_assemble.py` call `lead_guard.check_build_fresh()` and stop with `StaleBuildError` if any input changed or appeared after the build (`python code/lead_guard.py` checks it by hand).
- **Independent checks added in Loop 2:**
  - `lead_check_daily_dd.py` re-derives B1's daily worst falls without B1's code: top 30 −43.7% (B1 −44.4%); sleeve rule −41.8% (B1 −41.7%); both on 2020-03-23.
  - `v1x_verify.py` (agent V1X) re-derives every holding's valuation from SEC filings.
  - `d2r_repair.py` (agent D2R) re-downloads the "no price data" list into new files, leaving D2's untouched.
  - `lead_check_risk_contrib.py` re-derives the sleeve's volatility, tracking error, correlation and risk shares from raw prices without the risk engine's code.
  - `lead_report_appendix.py` writes FINAL_REPORT Appendix A (statistics, simulation method, risk model, register of independent checks, per-holding verification).

- **Shared-workspace reconciliation:** `lead_reconcile_v005.py` compares v4 with the latest completed Codex release (v005, read-only) and feeds FINAL_REPORT §13 and the dashboard tab. Releases are published with `tools/publish_research_release.py` (see the project-root `RESEARCH_VERSIONING.md`).

## Environment
- Python 3.11.9 with packages installed to `C:\Users\user\eqv4\pylib`:
  - pandas 3.0.6
  - numpy 2.4.6
  - scipy 1.17.1
  - yfinance 1.7.0 (+ curl_cffi 0.16.3)
  - pyarrow 25.0.1
  - statsmodels 0.15.0
  - requests 2.34.2
  - markdown 3.11
- Recreate with: `python -m pip install --target C:\Users\user\eqv4\pylib pandas==3.0.6 numpy==2.4.6 scipy==1.17.1 yfinance==1.7.0 curl_cffi==0.16.3 pyarrow==25.0.1 statsmodels==0.15.0 requests==2.34.2 markdown==3.11 lxml beautifulsoup4 openpyxl`
- Every command below runs from `v4/code` with `PYTHONPATH='C:\Users\user\eqv4\pylib'` (Git Bash) and, on Windows consoles, `PYTHONIOENCODING=utf-8`.
- Raw downloads are cached under `C:\Users\user\eqv4\cache\<agent>`. A re-run reuses the cache; delete it to re-download. Downloads made after 2026-09-25 will differ.

## Pipeline order (each stage writes a `.meta.json` sidecar and a report in `v4/outputs/`)

| Stage | Scripts (in order) | Main outputs |
|---|---|---|
| D1 membership & IDs | `d1_fetch_sources.py`, `d1_fja.py`, `d1_wiki.py`, `d1_wiki_snapshots.py`, `d1_wiki_reconstruct.py`, `d1_membership.py`, `d1_sec_fetch.py`, `d1_identity.py`, `d1_cik_sector.py`, `d1_out_current.py` | `data/d1_membership_monthly.parquet`, `d1_membership_intervals.csv`, `d1_cik_map.csv`, `d1_sector_map.csv` |
| D2 prices | `d2_universe.py`, `d2_download.py`, `d2_build.py`, `d2_validate.py`, `d2_report.py` | `data/d2_adjclose.parquet`, `d2_close.parquet`, `d2_ret_monthly.parquet`, `d2_splits.parquet` |
| D3 SEC fundamentals | `d3_universe.py`, `d3_pull.py`, `d3_extract.py`, `d3_lineage.py`, `d3_build_pit.py`, `d3_validate.py` | `data/d3_pit_monthly_lag1.parquet`, `d3_eps_quarterly_pit.parquet`, `d3_xbrl_facts.parquet` |
| D4 live snapshot | `d4_universe.py`, `d4_fetch_yahoo.py`, `d4_fetch_indep_prices.py`, `d4_fetch_sec.py`, `d4_build_snapshot.py`, `d4_validate.py`, `d4_events.py`, `d4_changelog.py`, `d4_report.py` | `data/d4_live_snapshot.parquet` |
| R1 / R2 / R3 research | `r1_base_rates.py`, `r1_cma_scenarios.py`; `r2_implementation_calcs.py`; `r3_ff_factors.py`, `r3_largecap_longonly.py`, `r3_pit_beat_rates.py`, `r3_stock_base_rates.py`, `r3_confidence_calibration.py`, `r3_build_report.py` | `data/r1_scenarios.csv`, `outputs/r2_*`, `outputs/r3_evidence_base.md` |
| B1 backtest (pre-registered model) | `b1_panel.py`, `b1_backtest.py`, `b1_phaseb.py`, `b1_sleeve.py`, `b1_tests.py`, `b1_report.py` | `outputs/b1_results.json`, `b1_report.md`, `data/b1_live_scores.csv`, `data/b1_strategy_returns_monthly.parquet` |
| B1X independent replication | `b1x_build.py`, `b1x_backtest.py`, `b1x_live.py`, `b1x_compare.py` | `outputs/b1x_vs_b1_comparison.json` |
| B2 risk module | `b2_tests.py` (25 tests), `b2_run.py` | `outputs/b2_reference_results.json` |
| V1 valuation | `v1_valuation.py` | `outputs/v1_valuation_table.csv`, `v1_valuation.json` |
| Diligence | Agent-written dossiers in `v4/dossiers/*.md`; verdict JSONs `outputs/f*_summary.json`; linted with the finance-skills `lint_report.py` | — |
| Lead: portfolio | `lead_build_portfolio.py` (rules fixed before the verdicts were read; constraint checks printed), `lead_risk.py` | `outputs/lead_portfolio_build.json`, `lead_risk_results.json` |
| Lead: report + dashboard | `lead_views.py`, `lead_report_sections.py`, `lead_assemble.py` | `FINAL_REPORT.md` (data-driven sections regenerated), `dashboard/equity_audit_v4.html` |
| Lead verifications of v3 | `lead_check_addition_bias.py`, `lead_check_v3_drawdown.py`, `lead_check_drift_and_benchmark.py` | `outputs/lead_v3_audit.md` |

## Seeds and fixed choices
- Bootstraps:
  - B2 reference runs use seed 42.
  - `lead_risk.py` uses seed 7, with 20,000 paths and a stationary-bootstrap mean block of 21 days. It also re-runs the base case with 5- and 63-day blocks (`block_sensitivity_base` in `lead_risk_results.json`).
  - B1's unit tests (`b1_tests.py`) use seed 20260926; B1's Dirichlet test (`b1_phaseb.py`) uses seed 42.
- Model perturbations: B1's Dirichlet(α=5) weight test uses 500 draws.
- Audit sampling: DA2 uses seed 20260926.
- Pre-registered model: see `STATE.md`, section "Pre-registered primary model", frozen before any v4 backtest.
- Sleeve rules: the header of `lead_build_portfolio.py`, fixed before the diligence verdicts were read. Amendments after Loop 1 are logged with reasons in `STATE.md`:
  - (a) a missing valuation makes a name ineligible;
  - (b) so does a negative V1 base case;
  - (c) so does an incomplete valuation with no base case;
  - (d) half conviction halves the per-name cap (5%), and capacity the caps cannot absorb goes to the index fund.
  - (e) the analyst's own reconciled valuation must also be cheap or fair;
  - (f) REITs use the FFO-based verdict rebuilt from filings (V2R) instead of V1's net-income-plus-depreciation proxy.

## Verify quickly
- `python b2_tests.py -v` should report 25 passing tests.
- `python b1_tests.py` should report no look-ahead violations.
- `python lead_build_portfolio.py` should print its constraint table with every check passing.
