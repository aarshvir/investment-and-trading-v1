# B2 — Risk engine: drawdowns, stress tests, probability of outcomes

_Agent B2 · generated 2026-09-25T22:42Z · data cutoff 2026-09-25 · scenarios from `v4/data/r1_scenarios.csv` (R1 complete)_

## Answer first

- **The v3 14-stock portfolio is materially riskier than SPY, in every measure we ran, and shows no detectable edge over it once both are put on the same return assumption.** Unshrunk sample vol is **21.9%/yr (5y)** vs SPY's **17.2%**; it fell more than SPY in **6 of 7** historical crises since 2007 (worst: GFC -60.3% vs SPY -55.2%; COVID -39.8-39.9% vs -33.7%); and a joint bootstrap (same resampled days for both) puts **P(v3 beats SPY over 5y) at 49.3-50.5%** — a coin flip — across Bear/Base/Bull and across two different history windows (full 1995+ and since-2014). This is the same conclusion the lead's audit reached from a different angle (out-of-sample cohorts); B2 now quantifies it with a full risk model.
- **The stated 15-20% drawdown tolerance will very likely be tested by ANY of these portfolios, not just v3.** Under the Base (6%/yr) scenario, 5-year P(drawdown worse than -20%) is **82.6% for SPY alone**, **91.7% for a 50/50 SPY+v3 blend**, and **98.8% for v3 alone**; P(worse than -30%) is 44.5% / 59.5% / 81.7% respectively. The only lever that meaningfully changes this in our runs is a cash reserve: SPY blended 50/50 with T-bills cuts 5y P(DD>-20%) from 83% to 17% (`allocation_scenarios_SPY`).
- **B2 confirms the lead's COVID drawdown finding and refines it.** Replicating the lead's exact assumption (ABNB filled with 0% "zero-fill" returns, monthly rebalance) gives **-36.05%**, matching the lead's **-36.2%** and the external review's **-36.15%** closely. The BKNG-proxy sensitivity gives **-39.16%** (lead: **-40.1%**). Our recommended non-zero-fill default (`missing='exclude'`, renormalise over the 13 real names) gives **-39.90%** — i.e., the true COVID drawdown was almost certainly closer to **-40%** than to the originally reported month-end figure of -26.2%.
- **A caveat that matters for how to read the vol numbers below**: the Ledoit-Wolf shrinkage intensity hit its 1.0 ceiling for every multi-stock portfolio (v3, the 50/50 blend), driven by a handful of extreme single-day moves (NVDA/NTAP/ABNB/RL daily moves of 17-24%). At full shrinkage the estimator collapses all cross-correlation to zero, which understates risk for a concentrated stock portfolio (real average pairwise correlation is 0.29-0.40, not 0). **Use `vol_annual_unshrunk` and `avg_pairwise_correlation`, not `vol_annual`, as the headline vol/correlation read for v3-like portfolios** — this is reported explicitly in every risk_summary output, not hidden.
- Block-length sensitivity (5/21/63 days) moves 5y outcome stats by only 1-3 points — not a first-order concern. The bootstrap's drawdown frequencies are within roughly 2-11 points of SPY's actual 1995-2026 rolling-window empirical frequencies (sanity check requested by the lead), and run consistently a bit higher, which is expected: the bootstrap can recombine bad blocks that never actually occurred back-to-back in the single realized history.

## 1. What was built

- **`v4/code/b2_risk.py`** (747 lines): `load_prices`/`load_sector_map`/`load_flagged_ticks` (D2/D1 readers); `max_drawdown`; `recentre_to_geometric_drift` (log-space, geometric) and `recentre_arithmetic` (simple-return shift, used only by `allocation_scenarios` per spec); `ledoit_wolf_shrinkage` (analytic LW 2004 shrinkage-to-scaled-identity — no sklearn in this environment); `portfolio_daily_path` (rebalanced daily wealth path with explicit `'exclude'|'proxy'|'cash'` missing-history handling, never a silent zero-fill); `risk_summary`; `stress_tests` (+ `find_drawdown_window` for the three crises whose exact dates weren't given); `simulate_outcomes` (Politis-Romano stationary bootstrap, vectorised, joint with a benchmark); `block_length_sensitivity`; `allocation_scenarios`; `empirical_drawdown_frequency`.
- **`v4/code/b2_tests.py`**: 25 unit tests (stdlib `unittest` — no pytest in the pinned environment), all passing. Covers: zero-vol/known-value drawdowns, weights-sum and unknown-ticker validation, single-asset path matches the raw series exactly, `'exclude'` renormalises and reports the correct missing share, `'proxy'` fill is scaled by a beta estimated from real overlapping history (caught and fixed a real bug: `np.cov`'s default `ddof=1` vs `np.var`'s default `ddof=0` were inconsistent, which biased every proxy-beta and every risk-summary beta by a factor of N/(N-1) — now both use `ddof=1`), `'cash'` fill matches a closed-form buy-and-hold check, Ledoit-Wolf output is symmetric/PSD with shrinkage in [0,1], bootstrap indices stay in range, bootstrap median return hits a recentred target within 2 points, self-vs-self joint bootstrap gives exactly 0% "beat probability", `allocation_scenarios` at 100% equity reproduces `simulate_outcomes` bit-for-bit, more cash strictly reduces drawdown risk, and the empirical-frequency helper detects an engineered drawdown and returns exactly 0 on a flat series. Run: `PYTHONPATH='C:\Users\user\eqv4\pylib' python b2_tests.py -v`.
- **`v4/code/b2_run.py`**: the reference runs below; writes `v4/outputs/b2_reference_results.json` (150 KB).

## 2. Risk summary (`risk_summary`)

Trailing windows from 2026-09-25, Ledoit-Wolf shrinkage on daily returns, days where every held name + SPY has a real price (no gap-filling enters the covariance estimate).

| Portfolio | Window | Vol (LW-shrunk) | **Vol (unshrunk sample)** | Shrinkage δ | Beta vs SPY | Tracking error | Eff. bets (weight) | Eff. bets (risk) | Avg pairwise corr | Top-3 PC share |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 5y | 17.2% | 17.2% | 0.00 | 1.00 | 0.0% | 1.0 | 1.0 | n/a | 100% |
| RSP | 5y | 16.1% | 16.1% | 0.00 | 0.86 | 7.0% | 1.0 | 1.0 | n/a | 100% |
| v3 (14-stock) | 3y | 8.6% | **18.8%** | 1.00 | 1.09 | 8.6% | 12.7 | 10.4 | 0.29 | 55.7% |
| v3 (14-stock) | 5y | 9.1% | **21.9%** | 1.00 | 1.16 | 9.3% | 12.7 | 10.4 | 0.38 | 59.3% |
| 50/50 SPY+v3 | 5y | 16.4% | **19.1%** | 1.00 | 1.08 | 4.7% | 3.7 | 1.2 | 0.40 | 61.1% |

v3 sector risk contribution (5y, weight-basis — the degenerate full-shrinkage covariance makes this ≈ w², not a true correlation-aware read): Information Technology 29.5%, Consumer Discretionary 28.7%, Industrials 22.8%, Financials 19.0% (matches the lead's cap-breach finding: IT/Financials/Industrials each ~25-30% of risk, not diversified). `ledoit_wolf_shrinkage` is symmetric/PSD by construction (tested); the δ=1.00 finding is identical across the 3y and 5y windows, which is itself evidence the shrinkage is at its ceiling rather than reading genuine sample noise.

## 3. Stress tests (`stress_tests`) — daily-data replays, buy-and-hold from each window's start

| Crisis | Window (exact) | SPY | RSP | v3 (exclude) | v3 (BKNG proxy) | 50/50 blend |
|---|---|---|---|---|---|---|
| GFC | 2007-10-09 → 2009-03-09 | -55.2% | -59.2% | -60.3% (23.0% wt. missing: CPAY/ALLE/ABNB not yet listed) | **-53.8%** (12.4% missing, 10.6% BKNG-proxied) | -57.4% |
| Q4 2018 | 2018-09-20 → 2018-12-24 | -19.3% | -19.7% | -27.0% (10.6% missing: ABNB) | -25.5% (10.6% proxied) | -23.0% |
| COVID | 2020-02-19 → 2020-03-23 | -33.7% | -39.0% | -39.8% (10.6% missing) | -39.1% (10.6% proxied) | -36.6% |
| 2022 bear | 2022-01-03 → 2022-10-12 | -24.5% | **-20.3%** | -25.3% | -25.3% | -24.9% |
| US downgrade/Eurozone | 2011-07-07 → 2011-10-03 (located by search) | -18.4% | -22.9% | -23.0% (15.7% missing) | -22.0% (5.1% missing, 10.6% proxied) | -20.5% |
| China deval selloff | 2015-07-20 → 2016-02-11 (located) | -13.0% | -15.1% | -13.8% (10.6% missing) | -13.5% (10.6% proxied) | -13.4% |
| Apr 2025 tariff shock | 2025-02-19 → 2025-04-08 (located) | -18.8% | **-16.0%** | -23.1% (0% missing — all 14 listed) | -23.1% (identical: no gap to proxy) | -21.0% |

v3 (either missing-data variant) falls more than SPY in 6 of 7 episodes; the single exception (BKNG-proxied GFC) depends on BKNG's own GFC path and a still-13% real weight gap, so it is not strong evidence of resilience. Search windows were located by scanning for the true running-max-relative minimum inside a bracket, not assumed (`find_drawdown_window`).

## 4. COVID zero-fill / proxy / exclude reconciliation (vs `lead_v3_audit.md` finding #4/#6)

| Method (v3, 2020-02-19→2020-03-23, monthly rebalance) | Total return | Lead/external reported |
|---|---|---|
| `missing='cash', cash_annual=0` (replicates the lead's zero-fill) | **-36.05%** | Lead: -36.2%; external review: -36.15% |
| `missing='proxy', proxies={ABNB:BKNG}` | **-39.16%** | Lead: -40.1% |
| `missing='exclude'` (B2's recommended default — no zero-fill, no single-proxy bet) | **-39.90%** | (new) |
| SPY, same window | -33.7% | — |

**Confirms** both lead numbers within 0.15-0.9 points (residual gap is expected: the lead's number comes from a continuous multi-year monthly-rebalanced path, ours from a fresh start at the window boundary). **Refines**: the zero-fill assumption the original v3/external numbers rest on cushions the true decline (10.6% of the portfolio earning 0% instead of falling with the market); B2's non-zero-fill default puts the real COVID drawdown near **-40%**, not -36%, and nowhere near the originally reported month-end -26.2%.

## 5. Simulated outcomes (`simulate_outcomes`) — Bear/Base/Bull, n=20,000, stationary bootstrap, block=21d

Base scenario (6%/yr geometric target, same target applied to the SPY leg of the joint bootstrap):

| Portfolio | P(profit, 5y) | Median ann. return (5y) | P(beat SPY, 5y) | P(DD>-15%) | P(DD>-20%) | P(DD>-30%) | Expected worst DD |
|---|---|---|---|---|---|---|---|
| SPY | 79.9% | 6.2% | — | 96.5% | 82.6% | 44.5% | -30.1% |
| RSP | 77.2% | 6.4% | 50.1% | 97.0% | 84.8% | 52.6% | -32.9% |
| v3 (exclude, full 1995+ pool) | 71.4% | 6.4% | 49.7% | 100.0% | 98.8% | 81.7% | -42.4% |
| v3 (BKNG proxy, full 1995+ pool) | 71.2% | 6.3% | 49.3% | 99.9% | 98.5% | 80.9% | -42.1% |
| **v3 (exclude, since-2014 pool)** | 75.5% | 6.3% | 50.5% | — | 94.2% | 65.4% | -36.4% |
| 50/50 SPY+v3 | 76.5% | 6.3% | 49.9% | 98.9% | 91.7% | 59.5% | -34.5% |

Bear (2%/yr) / Bull (9%/yr) shift the level but not the ranking: 5y P(profit) for v3 is 58.4%/79.3% (exclude) vs SPY 62.1%/88.7%; P(beat SPY, 5y) stays in a **49.3-50.5%** band across every scenario and both history windows — no combination shows v3 with a statistically meaningful edge over the index once both share the same drift assumption. 1-year numbers (Base): P(profit) 66.7% (SPY) vs 62.1% (v3 exclude); this and the full per-horizon (1y/3y/5y) percentile/drawdown grid for all three scenarios and portfolios are in `b2_reference_results.json`.

**Bootstrap pool honesty note**: the "full 1995+" pool for v3 averages 23% of target weight missing/renormalised (pre-IPO gaps concentrated before 2013-14, when as few as 4 of 14 names existed); the since-2014 pool (5.9% average missing — only ABNB's pre-Dec-2020 gap remains) is more representative of the actual 14-name portfolio and is less pessimistic (5y P(DD>-30%) 65.4% vs 81.7%) but the core finding — much riskier than SPY, no edge over it — holds in both.

**Block-length sensitivity** (5/21/63 days, Base, 5y): P(profit) 70.4-72.5% (v3) / 77.8-80.3% (SPY); P(DD>-30%) 79.8-84.2% (v3) / 44.5-47.3% (SPY); expected worst drawdown moves by ≤0.1pt for v3 (-42.4/-42.4/-42.5%) and ≤0.6pt for SPY (-30.6/-30.1/-30.7%). Not a first-order sensitivity — reported in full, not cherry-picked.

## 6. SPY empirical drawdown frequency vs bootstrap (sanity check)

Actual daily history 1995-2026, overlapping rolling windows (`empirical_drawdown_frequency`) vs a stationary bootstrap using SPY's own **unrecentred** (raw ~11-12%/yr arithmetic) historical drift, for apples-to-apples comparison:

| Horizon | Empirical P(DD>-15%) | Bootstrap P(DD>-15%) | Empirical P(DD>-20%) | Bootstrap P(DD>-20%) | Independent non-overlapping stretches available |
|---|---|---|---|---|---|
| 1y | 37.9% | 40.4% | 18.6% | 20.7% | ~31 |
| 3y | 74.1% | 81.5% | 45.2% | 56.3% | ~10 |
| 5y | 89.6% | 94.1% | 69.0% | 74.7% | ~6 |

The bootstrap runs consistently higher than the single realized history (by 2.1-2.5pt at 1y, 7.4-11.1pt at 3y, 4.5-5.7pt at 5y), which is expected and reassuring rather than a red flag: it can recombine historically-separate bad blocks (e.g., a dot-com-like start into a GFC-like middle) that never actually occurred back-to-back, so it should be somewhat more pessimistic than one realized path sampled from only ~6-31 independent multi-year stretches. The two methods agree to within roughly 2-11 percentage points (mostly single digits) at every horizon.

## 7. Allocation scenarios — SPY equity sleeve vs 4% cash/T-bill reserve (`allocation_scenarios`)

Base scenario (equity leg recentred to R1's 7.28% arithmetic-equivalent target; arithmetic blending only, as specified — not the geometric method used elsewhere):

| Mix (equity/cash) | P(profit, 5y) | Median ann. return | P(DD>-20%) | P(DD>-30%) |
|---|---|---|---|---|
| 100/0 | 78.5% | 5.8% | 83.1% | 45.4% |
| 80/20 | 83.6% | 5.8% | 63.6% | 23.8% |
| 70/30 | 86.3% | 5.7% | 49.3% | 14.0% |
| 60/40 | 89.5% | 5.5% | 33.9% | 6.2% |
| 50/50 | 92.4% | 5.4% | 17.2% | 1.8% |

Cash is the most reliable lever for hitting a 15-20% drawdown tolerance seen anywhere in this analysis: moving from 100% to 50% equity gives up only 0.4 points of median annual return (5.8%→5.4%) while cutting P(DD>-20%) by roughly 5x (83%→17%) and P(DD>-30%) by roughly 25x (45%→2%). Bear/Bull versions of this table are in the JSON. **Scenario analysis, not advice.**

## 8. How to call this on a new (e.g. final v4) portfolio

```python
import sys; sys.path.insert(0, r"V4\code")
import b2_risk as b2

weights = {"AAPL": 0.10, "MSFT": 0.10, ...}   # must sum to 1.0
prices  = b2.load_prices()                     # or pass your own panel

risk = b2.risk_summary(weights, prices=prices)                 # vol, beta, TE, risk contributions, ENB, PCA
stress = b2.stress_tests(weights, prices=prices, missing="exclude")   # 7 named crises + SPY
sim = b2.simulate_outcomes(weights, drift_annual=0.06, horizons=[1, 3, 5],
                            benchmark_returns=prices["SPY"].pct_change(),
                            benchmark_drift_annual=0.06, missing="proxy",
                            proxies={"NEWCO": "PEER_TICKER"})   # P(profit), P(beat SPY), drawdown odds
alloc = b2.allocation_scenarios(b2.recentre_arithmetic(prices["SPY"].pct_change(), 0.0728),
                                 reserve_yield=0.04, mixes=[1.0, 0.8, 0.7, 0.6, 0.5])
```

Always pass an explicit `missing=` choice and check `path.missing_share` / `diagnostics['pool_missing_share_mean']` before trusting a number for a portfolio with young constituents.

## 9. Known limitations

1. **Ledoit-Wolf shrinkage hit its 1.0 ceiling for every multi-name portfolio tested** (see Sec.1/2) because a handful of extreme single-day returns (earnings jumps) inflate the estimator's noise term far above its target-distance term; this is a documented property of shrinkage-to-identity under fat tails, not a bug (unit-tested for correctness on synthetic Gaussian data, where it behaves as expected: `test_shrinkage_toward_identity_reduces_offdiag`). We mitigate by always reporting `vol_annual_unshrunk` alongside it; a single-factor (market-model) shrinkage target would likely be better-behaved for concentrated equity books and is a natural follow-up, not built here.
2. **Survivorship and identity risk are inherited from D2** (d2_report.md §7): roughly half of 2000-04 member-days and a fifth of 2015-19 member-days have no Yahoo price; this module's `'exclude'` renormalisation is honest about the resulting gap (`missing_share`) but cannot recover the missing names' actual returns.
3. **`'proxy'` beta is a single OLS slope over the full common-history overlap**, not time-varying, and assumes zero intercept; for ABNB→BKNG this is a travel-sector-consumer-discretionary proxy, not a true twin (confirmed reasonable but imperfect: BKNG's own COVID crash was deeper than the broad market, which is plausibly right for a travel name but not verified against ABNB's actual (post-IPO) behaviour).
4. **Rebalancing/inclusion decisions are evaluated only at rebalance boundaries**, not intraday or mid-period; a name that IPOs mid-month is excluded for that whole month under `'exclude'`/`'proxy'`. Realistic for a monthly/quarterly-managed portfolio, disclosed via `missing_share`'s step pattern.
5. **252-trading-day-year convention** throughout; horizons are exact multiples of 252 days, not calendar years.
6. **The stationary bootstrap assumes the historical daily-return sample (block-resampled) is representative of the future** beyond its recentred mean; it does not model regime shifts, changing correlation in future unseen crises, or fatter tails than 1995-2026 has shown. Section 6's empirical cross-check is a partial mitigation, not a guarantee.
7. **`allocation_scenarios` blends arithmetically per spec** (not the geometric method used in `simulate_outcomes`); the two are not directly comparable number-for-number, by design.
8. **D2 disclosure**: SPY has 4 entries in `d2_confirmed_errors.csv` (1999-2009, 0.7-3.0% each) but all on the `Close` field (split-adjusted only) — not `Adj Close`, the total-return series this module actually uses for returns — so they do not affect any number in this report; one of the four (2000-04-04) is itself flagged `confirmed_by=0`, i.e. D2's own arbiter thinks Yahoo, not the cross-check source, is right. HIG has 3 `d2_bad_ticks.csv` flags, all 2008 Oct-Dec (during membership), confirmed genuine GFC volatility, not data errors.

## 10. Files produced

| File | Content |
|---|---|
| `code/b2_risk.py` | risk engine module (747 lines) |
| `code/b2_tests.py` | 25 unit tests, all passing |
| `code/b2_run.py` | reference-run script (reproducible; ~90s runtime) |
| `outputs/b2_reference_results.json` | full results: risk_summary, stress_tests, covid_reconciliation, simulate_outcomes (5 portfolios × 3 scenarios × 3 horizons), block_length_sensitivity, v3_bootstrap_pool_sensitivity_since2014, spy_unrecentred_bootstrap, spy_empirical_drawdown_frequency_1995_2026, allocation_scenarios_SPY (150 KB) |
| `outputs/b2_report.md` | this file |
