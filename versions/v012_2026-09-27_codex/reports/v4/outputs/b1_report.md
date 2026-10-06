# B1 — Point-in-time factor backtest engine (Phase B)

_Agent B1 · generated 2026-09-25T22:58:40Z · returns 2012-01-31 → 2026-08-31 (176 months) · membership source: **D1_membership_monthly**_

## Answer first

**No — on a point-in-time S&P 500 universe the pre-registered composite (Q+V+M+S, equal weights) has not added value after costs over 2012-01…2026-08.**

- Primary **top-30 EW** (monthly, 10 bps/trade): CAGR **12.5%** vs SPY TR 15.1% → excess **-2.6%/yr**, NW t = **-1.12**, 95% CI of annualised mean excess [-5.6%, 1.5%]; vs the PIT equal-weight universe -1.5%/yr (t = -0.83).
- Primary **top-quintile EW**: CAGR 13.3%; vs PIT EW -0.7%/yr (t = -0.84); vs SPY -1.8%/yr (t = -1.16).
- Q5−Q1 (gross): 0.34%/yr, NW t = 0.18. Composite rank IC (1m) mean 0.0070 (NW t 0.98); 12m IC 0.0047 (t 0.32).
- Decile table is **not monotonic** (Spearman decile vs mean fwd-12m = -0.31; 4/9 increasing steps; D10−D1 = -1.6%).
- FF5+UMD alpha of top-30 (net, vs rf): -2.3%/yr, t = -1.37 — the portfolio mostly loads on known factors (UMD, RMW, SMB, HML all significant) that did not pay in large caps in this window.
- Risk: top-30 daily max drawdown **-44.4%** (2020-03-23) vs SPY -33.7% over the same window; monthly vol 15.5% vs SPY 14.0%.
- Rolling windows, top-30 vs SPY: positive excess in 35% of 12m, 21% of 36m and 5% of 60m windows (vs PIT EW: 42% / 28% / 9%).
- **Implication for the program:** the composite score is not evidence of stock-picking edge. It can still be used as a screen (it modestly sorts downside risk: bottom decile has the worst p10 and drawdown frequency), but conviction/probability language must come from the calibration tables below (which are nearly flat across deciles), not from the backtest.

## Headline statistics (net of 10 bps per unit traded; 2012-01…2026-08)

| Strategy | CAGR | Vol | Sharpe | MaxDD (m) | Excess vs SPY | t | Excess vs PIT EW | t | IR vs SPY | Turnover (1-way/yr) |
|---|---|---|---|---|---|---|---|---|---|---|
| Top-30 EW | 12.5% | 15.5% | 0.74 | -33.7% | -2.6% | -1.12 | -1.5% | -0.83 | -0.28 | 3.80 |
| Top quintile EW | 13.3% | 14.4% | 0.83 | -26.5% | -1.8% | -1.16 | -0.7% | -0.84 | -0.30 | 2.97 |
| Bottom quintile EW | 12.3% | 17.5% | 0.66 | -30.0% | -2.8% | -0.97 | -1.7% | -1.00 | -0.25 | 2.96 |
| PIT EW universe (bench) | 14.0% | 15.1% | 0.84 | -26.8% | -1.1% | -0.60 | — | — | -0.16 | 0.33 |
| PIT EW scored names | 13.9% | 15.1% | 0.83 | -26.8% | -1.2% | -0.68 | -0.1% | -1.95 | -0.18 | 0.34 |
| SPY TR | 15.1% | 14.0% | 0.97 | -23.9% | | | | | | |
| RSP (EW ETF) | 13.0% | 15.0% | 0.79 | -26.7% | | | | | | |
| ^SP500TR | 15.2% | 14.0% | 0.97 | -23.9% | | | | | | |

Sharpe uses ^IRX (3-month T-bill) as rf. NW t = Newey-West (3 lags) t-stat of mean monthly excess. Costs: 10 bps × Σ|Δw| (buys + sells) each rebalance; turnover shown one-way.

**Subperiods (top-30 net vs SPY / vs PIT EW):**

| Period | Top-30 CAGR | SPY | Excess | t | PIT EW | Excess | t |
|---|---|---|---|---|---|---|---|
| 2012-2014 | 22.4% | 20.3% | 2.1% | 0.85 | 23.6% | -1.2% | -0.36 |
| 2015-2019 | 6.4% | 11.6% | -5.2% | -2.29 | 10.9% | -4.5% | -1.84 |
| 2020-2026 | 13.0% | 15.5% | -2.5% | -0.52 | 12.3% | 0.7% | 0.33 |

**Calendar years:**

| Year | Top-30 | Top-Q | PIT EW | SPY | RSP | Top-30 − SPY | Top-30 − PIT EW | PIT EW − RSP |
|---|---|---|---|---|---|---|---|---|
| 2012 | 15.9% | 18.0% | 19.7% | 16.0% | 17.2% | -0.1% | -3.8% | 2.5% |
| 2013 | 31.8% | 35.7% | 37.1% | 32.3% | 35.5% | -0.5% | -5.3% | 1.6% |
| 2014 | 19.9% | 19.4% | 15.0% | 13.5% | 14.1% | 6.5% | 4.9% | 0.9% |
| 2015 | -1.6% | 0.4% | -1.6% | 1.2% | -2.7% | -2.9% | -0.1% | 1.1% |
| 2016 | 7.9% | 12.1% | 16.1% | 12.0% | 14.5% | -4.1% | -8.2% | 1.6% |
| 2017 | 19.8% | 19.7% | 20.6% | 21.7% | 18.5% | -1.9% | -0.9% | 2.1% |
| 2018 | -8.4% | -6.6% | -7.3% | -4.6% | -7.8% | -3.8% | -1.1% | 0.6% |
| 2019 | 16.8% | 23.8% | 31.0% | 31.2% | 28.9% | -14.4% | -14.2% | 2.1% |
| 2020 | -0.9% | 4.2% | 12.4% | 18.3% | 12.7% | -19.2% | -13.3% | -0.3% |
| 2021 | 31.3% | 32.1% | 29.8% | 28.7% | 29.4% | 2.5% | 1.5% | 0.4% |
| 2022 | -10.0% | -11.4% | -11.2% | -18.2% | -11.6% | 8.2% | 1.2% | 0.4% |
| 2023 | 11.6% | 12.8% | 15.8% | 26.2% | 13.7% | -14.6% | -4.3% | 2.2% |
| 2024 | 19.5% | 15.0% | 12.6% | 24.9% | 12.8% | -5.4% | 6.9% | -0.2% |
| 2025 | 13.9% | 10.0% | 11.2% | 17.7% | 11.2% | -3.8% | 2.7% | 0.0% |
| 2026 | 27.3% | 19.9% | 15.2% | 13.1% | 15.5% | 14.2% | 12.1% | -0.3% |

**Exploratory extension (2010-01 start; thin fundamentals in 2010-11 — not headline):** top-30 CAGR 12.4%, excess vs SPY -1.9% (t -0.86), vs PIT EW -1.4% (t -0.85).

## Signal diagnostics

| Signal | mean rank IC (1m) | NW t | months |
|---|---|---|---|
| composite_1m | 0.0070 | 0.98 | 176 |
| composite_12m | 0.0047 | 0.32 | 165 |
| family_Q_1m | 0.0052 | 0.87 | 198 |
| family_V_1m | -0.0002 | -0.02 | 200 |
| family_M_1m | 0.0079 | 0.75 | 200 |
| family_S_1m | 0.0070 | 1.31 | 186 |

**Decile table** (time-series mean of cross-sectional decile means; formation 2011-12…2025-08):

| Decile | mean fwd-12m TR | mean 1m TR ×12 | stock-months |
|---|---|---|---|
| 1 | 15.2% | 14.9% | 7525 |
| 2 | 13.3% | 12.7% | 7503 |
| 3 | 14.1% | 13.9% | 7516 |
| 4 | 14.4% | 13.4% | 7507 |
| 5 | 15.1% | 14.8% | 7559 |
| 6 | 14.4% | 14.9% | 7471 |
| 7 | 14.0% | 15.3% | 7524 |
| 8 | 14.7% | 13.9% | 7499 |
| 9 | 13.8% | 14.1% | 7520 |
| 10 | 13.6% | 14.2% | 7508 |

**FF5 + UMD regression** (monthly net return − rf; NW 3 lags):

| Portfolio | alpha/yr | t | Mkt | SMB | HML | RMW | CMA | UMD | R² |
|---|---|---|---|---|---|---|---|---|---|
| primary_top30_ew | -2.3% | -1.37 | 0.99 | 0.23 | 0.20 | 0.29 | 0.14 | 0.16 | 0.87 |
| primary_topquintile_ew | -1.4% | -1.35 | 0.96 | 0.14 | 0.15 | 0.21 | 0.14 | 0.11 | 0.93 |
| pit_ew_universe | -0.3% | -0.36 | 0.97 | 0.15 | 0.15 | 0.14 | 0.13 | -0.05 | 0.95 |

## Calibration (every PIT stock-month with a composite, formation 2011-12…2025-08)

P(·) are empirical frequencies. Overlapping 12-month windows make stock-months dependent: `CI` uses raw n (too narrow), `CI n_eff` uses n/12 (conservative). fwd-12m excludes names without a price 12 months later.

| Decile | n | P(fwd12>0) | CI n_eff | P(excess vs SPY>0) | CI n_eff | median fwd12 | p10 | p90 | P(maxDD<−20%) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6986 | 65.3% | [61%, 69%] | 45.1% | [41%, 49%] | 11.1% | -28.5% | 56.2% | 60.8% |
| 2 | 6965 | 66.3% | [62%, 70%] | 43.5% | [39%, 48%] | 11.0% | -24.5% | 50.0% | 54.7% |
| 3 | 6976 | 67.0% | [63%, 71%] | 44.6% | [41%, 49%] | 11.6% | -22.8% | 49.9% | 53.6% |
| 4 | 6967 | 68.4% | [64%, 72%] | 45.6% | [42%, 50%] | 11.9% | -20.3% | 49.6% | 51.3% |
| 5 | 7017 | 69.8% | [66%, 73%] | 46.2% | [42%, 50%] | 12.8% | -19.7% | 48.4% | 50.9% |
| 6 | 6936 | 68.7% | [65%, 72%] | 44.5% | [41%, 49%] | 11.9% | -20.0% | 48.2% | 50.3% |
| 7 | 6984 | 68.5% | [65%, 72%] | 44.0% | [40%, 48%] | 11.4% | -20.0% | 47.7% | 50.5% |
| 8 | 6959 | 70.1% | [66%, 74%] | 46.4% | [42%, 51%] | 12.5% | -19.3% | 48.0% | 49.8% |
| 9 | 6982 | 68.7% | [65%, 72%] | 44.5% | [41%, 49%] | 11.5% | -19.8% | 47.0% | 49.5% |
| 10 | 6969 | 66.7% | [63%, 70%] | 43.6% | [40%, 48%] | 11.0% | -21.6% | 49.1% | 52.6% |

Decile × vol-tercile table: `v4/outputs/b1_calibration_by_decile_vol.csv` (also in b1_results.json).

Portfolio level (top-30, rolling windows vs SPY): P(12m excess>0) = 34.5%, P(36m) = 20.6%, P(60m) = 5.1% (windows overlap heavily; 117 60-month windows ≈ 3 independent observations).

## Live scores (as of 2026-09-25, same code path)

`v4/data/b1_live_scores.csv/.parquet`: 503 constituent lines, 496 with a composite; coverage flags {'full': 476, 'composite_from_3_of_4_families': 20, 'insufficient_families_no_composite': 7}. Pending-deal targets (WBD, KVUE, TECH, AES, NSC, D) are flagged `exclude_pending_deal` and skipped by the live top-30. Given the backtest, the live ranking is a **screen, not a forecast**.

Live top-30 (entity level): CF, TGT, EXPE, SNDK, DLTR, HST, JBHT, ALL, TRV, MU, TPR, MPC, DVA, WDC, GL, SWK, DG, BAC, TROW, NTAP, HIG, NUE, BMY, CVS, EXPD, MGM, WSM, CRM, COP, AIZ

## Coverage and survivorship

| Year | PIT members | with Yahoo price (valid identity) | with composite |
|---|---|---|---|
| 2011 | 499 | 352 | 334 |
| 2012 | 499 | 357 | 344 |
| 2013 | 499 | 367 | 358 |
| 2014 | 499 | 375 | 368 |
| 2015 | 499 | 386 | 380 |
| 2016 | 499 | 404 | 399 |
| 2017 | 499 | 422 | 418 |
| 2018 | 499 | 433 | 429 |
| 2019 | 499 | 444 | 439 |
| 2020 | 499 | 456 | 450 |
| 2021 | 499 | 463 | 457 |
| 2022 | 499 | 471 | 465 |
| 2023 | 499 | 480 | 474 |
| 2024 | 500 | 485 | 478 |
| 2025 | 500 | 491 | 485 |
| 2026 | 500 | 498 | 492 |

Mean share of PIT members priced: 86.9%; with composite: 85.7%. Holdings that lost their price mid-month (delisting): 0 stock-months in the whole panel (Yahoo purges delisted symbols, so such names are mostly absent altogether rather than delisting in-sample; the −30% distress sensitivity therefore has almost nothing to act on — the missing names are the survivorship problem).

**Biggest missing PIT members by era** (no valid Yahoo series; months missing):

- 2010-11 (exploratory): AA (Alcoa; 24 mo); AET (Aetna; 24 mo); AGN (Allergan; 24 mo); ALTR (Altera; 24 mo); AKS (AK Steel; 24 mo); APOL (Apollo Education Group; 24 mo); APC (Anadarko Petroleum; 24 mo); BMS (Bemis;Bemis Company; 24 mo); BHI (Baker Hughes; 24 mo); ARG (Airgas; 24 mo); AVB (AvalonBay Communities; 24 mo); AVP (Avon Products; 24 mo)
- 2012-14: AA (Alcoa; 37 mo); ALTR (Altera; 37 mo); AGN (Allergan; 37 mo); AET (Aetna; 37 mo); COG (Cabot Oil & Gas; 37 mo); CMA (Comerica; 37 mo); COL (Rockwell Collins; 37 mo); APC (Anadarko Petroleum; 37 mo); ARG (Airgas; 37 mo); BBBY (Bed Bath & Beyond; 37 mo); AVP (Avon Products; 37 mo); AVB (AvalonBay Communities; 37 mo)
- 2015-19: ALXN (Alexion Pharmaceuticals; 60 mo); ADS (Alliance Data Systems; 60 mo); AVB (AvalonBay Communities; 60 mo); KSU (Kansas City Southern; 60 mo); LEG (Leggett & Platt; 60 mo); HES (Hess Corporation; 60 mo); IPG (Interpublic Group; 60 mo); JNPR (Juniper Networks; 60 mo); GPS (Gap; 60 mo); JWN (Nordstrom; 60 mo); ETFC (E-Trade; 60 mo); FLIR (FLIR Systems; 60 mo)
- 2020-26: EA (Electronic Arts; 79 mo); AVB (AvalonBay Communities; 79 mo); HOLX (Hologic; 75 mo); K (Kellanova; 71 mo); IPG (Interpublic Group; 70 mo); WBA (Walgreens Boots Alliance; 67 mo); HES (Hess Corporation; 66 mo); JNPR (Juniper Networks; 66 mo); ANSS (Ansys; 66 mo); DFS (Discover Financial; 64 mo); MRO (Marathon Oil; 58 mo); CTRA (Coterra Energy; 55 mo)

**Residual survivorship estimate:** PIT EW universe vs RSP (actual EW S&P 500 ETF, after its ~0.20% fee and quarterly rebalancing): excess CAGR 1.0%/yr (t 4.48). Our priced universe is biased upward by roughly this amount vs the true index. This bias is of the same order as the strategy excess estimates, so it cannot turn the negative composite result positive, but it means all absolute CAGRs here are optimistic by ~0.5–1%/yr.

## Method (pre-registered, frozen in STATE.md)

- Universe_t = PIT members at month-end t ∩ entities with a valid Yahoo total-return price at t; entity→series via CIK; member tickers now owned (SEC company_tickers) by a different CIK or flagged `reuse_suspect` by D2 are rejected; dual-class lines collapse to one entity per CIK.
- Fundamentals: `d3_pit_monthly_lag1` (facts filed strictly before t). Market cap = Close_t × split factor after t × PIT shares (split-basis ambiguity between share-count date and t resolved by D2 split table and a trailing-median check; BRK Class-A-equivalent shares ×1,500 for BRK-B; share counts that jump >2.5× vs trailing 12m median or imply <$250m / >$8tn cap set missing). Live validation vs `equity_project/info.json` (Yahoo marketCap): 467/500 within 5% (rule ≥90%: PASS); failures: ARES (0.247), IBKR (0.262), TKO (0.396), VMRK (0.488), BX (0.634), MLM (0.853), SPG (0.854), CPT (0.875), UDR (0.892), PCG (0.894), CHTR (0.896), BXP (0.899), DLR (0.918), INTC (0.921), ESS (0.932), GEN (0.937), MCHP (1.054), HCA (1.054), CTSH (1.055), ON (1.055), LLY (1.057), DELL (1.057), OMC (1.059), C (1.06), SPGI (1.061), DDOG (1.078), PYPL (1.079), BRK-B (1.152), ECHO (1.205), STZ (None), ERIE (None), V (None), CVNA (None).
- Metrics exactly as STATE.md; Q/V ratios winsorised at 1st/99th pct per month (lead instruction after D3); sector-neutral mid-rank percentiles within D1's SIC→GICS-like sector rules (sectors <5 valid names pooled); families need ≥50% of metrics; composite needs ≥3 of 4 families; financials (D3 flag or SIC 6000-6411) have GP/A, accruals, leverage, EBIT/EV missing.
- Portfolios formed at month-end close t, held to t+1; names without a t+1 price are dropped from that month's return (primary treatment).
- No-look-ahead tests (`v4/code/b1_tests.py`): see `v4/outputs/b1_tests_output.txt`.

## Limitations (Phase A)

1. Membership = D1's CIK-level PIT file (primary lines; secondary share classes dropped). Entity -> Yahoo series: D1's current Yahoo symbol first (renames / legal successors), then the ticker at t; any symbol now owned by a different CIK (SEC company_tickers) or flagged reuse_suspect by D2 is rejected. The earlier D2-spells run is kept as a sensitivity (`b1_results_d2spells.json`).
2. Survivorship: ~15–30% of member-months before 2020 have no price (acquired/failed names); these are excluded, which biases absolute returns upward (see RSP gap).
3. Up-C / dual-class / OP-unit structures (BX, ARES, IBKR, TKO, SPG, CPT, UDR, CHTR…) have Class-A-only market caps, which is internally consistent with Class-A net income but understates EV-based metrics.
4. 2010-11 has thin XBRL coverage; the headline starts 2012-01 (lead instruction).
5. Legacy replications use B1's PIT data (XBRL TTM, SIC-based sectors) with backtest3.py's formulas; they differ from the v3 originals in data vintage (Yahoo latest-restated annuals) by design.

## Phase B — variants, plateaus, legacy replications, bias, robustness

**All variants (net, 2012-01…2026-08 unless noted; none selected on results):**

| Strategy | CAGR | Vol | MaxDD (m) | Excess vs SPY | t | Excess vs PIT EW | t | Turnover 1-way/yr | Avg names |
|---|---|---|---|---|---|---|---|---|---|
| primary top-30 monthly (baseline) | 12.5% | 15.5% | -33.8% | -2.6% | -1.12 | -1.5% | -0.83 | 3.80 | 30 |
| primary top-20 monthly | 13.0% | 15.9% | -34.0% | -2.1% | -0.71 | -1.0% | -0.38 | 4.00 | 20 |
| primary top-40 monthly | 12.7% | 15.3% | -30.1% | -2.4% | -1.11 | -1.3% | -0.85 | 3.59 | 40 |
| primary top-50 monthly | 13.8% | 15.0% | -29.5% | -1.3% | -0.59 | -0.2% | -0.16 | 3.40 | 50 |
| primary top-30 quarterly | 13.9% | 15.6% | -31.8% | -1.2% | -0.43 | -0.1% | -0.02 | 2.26 | 30 |
| primary top-30 annual (end-Sep) | 12.8% | 15.6% | -27.0% | -1.9% | -0.75 | -0.8% | -0.42 | 0.79 | 30 |
| primary top-30, <=25% sector (7 names), <=2 per SIC4 | 12.9% | 15.5% | -31.1% | -2.2% | -0.94 | -1.1% | -0.61 | 3.78 | 30 |
| primary buffer: buy top-10%, hold while top-25% | 13.6% | 14.8% | -28.0% | -1.5% | -0.81 | -0.4% | -0.35 | 1.83 | 63 |
| primary top-quintile monthly | 13.3% | 14.4% | -26.5% | -1.8% | -1.16 | -0.8% | -0.84 | 2.97 | 85 |
| primary bottom-quintile monthly | 12.3% | 17.5% | -30.0% | -2.8% | -0.97 | -1.7% | -1.00 | 2.96 | 85 |
| QVM-only composite top-30 | 13.0% | 15.3% | -28.7% | -2.1% | -0.93 | -1.0% | -0.63 | 3.34 | 30 |
| QVM-only composite top-quintile | 13.7% | 14.6% | -28.6% | -1.4% | -0.75 | -0.3% | -0.35 | 2.60 | 86 |
| family Q alone top-30 | 14.1% | 15.0% | -27.2% | -1.0% | -0.50 | 0.1% | 0.02 | 1.88 | 30 |
| family Q alone top-quintile | 13.4% | 14.7% | -24.2% | -1.7% | -1.02 | -0.6% | -0.77 | 1.44 | 86 |
| family V alone top-30 | 12.0% | 19.9% | -39.6% | -3.1% | -0.60 | -2.0% | -0.45 | 2.33 | 30 |
| family V alone top-quintile | 13.2% | 17.8% | -35.3% | -1.9% | -0.47 | -0.8% | -0.19 | 1.72 | 85 |
| family M alone top-30 | 16.1% | 16.6% | -25.1% | 0.9% | 0.62 | 2.1% | 0.88 | 4.25 | 30 |
| family M alone top-quintile | 14.7% | 14.4% | -21.1% | -0.4% | -0.21 | 0.7% | 0.31 | 3.17 | 86 |
| family S alone top-30 | 14.3% | 15.3% | -24.4% | -0.8% | -0.37 | 0.3% | 0.20 | 4.16 | 30 |
| family S alone top-quintile | 13.7% | 14.7% | -24.8% | -1.4% | -0.99 | -0.3% | -0.37 | 3.19 | 82 |
| low-volatility quintile (1y daily vol) | 11.4% | 11.7% | -20.6% | -3.7% | -1.54 | -2.6% | -1.28 | 1.02 | 86 |
| legacy v2 weights top-30 monthly | 13.6% | 15.1% | -28.7% | -1.5% | -0.62 | -0.4% | -0.22 | 3.52 | 30 |
| legacy v2 weights top-quintile monthly | 13.7% | 14.1% | -25.0% | -1.4% | -0.78 | -0.3% | -0.31 | 2.83 | 70 |
| legacy v2 weights top-30 annual (end-Sep) | 12.7% | 15.6% | -33.9% | -2.1% | -0.84 | -1.0% | -0.46 | 0.77 | 30 |
| legacy v1 weights top-30 monthly | 11.3% | 12.1% | -18.6% | -3.8% | -1.66 | -2.7% | -1.26 | 2.65 | 30 |
| legacy v1 weights top-quintile monthly | 11.5% | 12.3% | -19.8% | -3.6% | -1.89 | -2.5% | -1.47 | 2.12 | 70 |
| legacy v1 weights top-30 annual (end-Sep) | 11.0% | 12.4% | -22.7% | -3.7% | -1.55 | -2.6% | -1.23 | 0.72 | 30 |
| legacy v3 conviction-filter proxy, monthly | 13.9% | 13.9% | -24.3% | -1.2% | -0.59 | -0.1% | -0.11 | 3.60 | 26 |
| legacy v3 conviction-filter proxy, annual (late-Sep) | 13.0% | 14.6% | -26.8% | -1.7% | -0.75 | -0.6% | -0.28 | 0.75 | 25 |
| primary top-30 monthly @ 20 bps | 11.7% | 15.5% | -34.6% | -3.4% | -1.54 | -2.3% | -1.34 | n/a | n/a |
| primary top-30 monthly @ 25 bps | 11.2% | 15.5% | -35.0% | -3.9% | -1.75 | -2.8% | -1.60 | n/a | n/a |
| primary top-30 monthly @ 30 bps | 10.8% | 15.5% | -35.4% | -4.3% | -1.96 | -3.2% | -1.86 | n/a | n/a |
| primary top-30 monthly, 1-month implementation lag | 13.3% | 15.8% | -30.5% | -1.5% | -0.57 | -0.3% | -0.12 | 3.79 | 30 |
| primary top-30 without 5 largest excess contributors | 10.6% | 15.2% | -33.8% | -4.5% | -2.18 | -3.5% | -2.25 | 3.78 | 30 |
| lead rule: sleeve_top20_invvol_q (as implemented) | 10.8% | 14.7% | -30.0% | -4.3% | -1.81 | -3.2% | -1.54 | 2.45 | 20 |
| lead rule: top20_ew_q | 11.6% | 15.3% | -32.2% | -3.5% | -1.34 | -2.4% | -1.05 | 2.40 | 20 |
| lead rule: top30_invvol_q | 11.4% | 14.2% | -26.6% | -3.7% | -1.84 | -2.6% | -1.54 | 2.31 | 30 |
| lead rule: top30_ew_q | 11.5% | 14.6% | -28.2% | -3.6% | -1.75 | -2.5% | -1.47 | 2.28 | 30 |
| lead rule: blend_SPY70_sleeve30 | 13.9% | 13.6% | -23.6% | -1.2% | -1.81 | -0.1% | -0.27 | n/a | n/a |
| lead rule: blend_SPY50_sleeve50 | 13.0% | 13.6% | -24.7% | -2.1% | -1.81 | -1.0% | -0.83 | n/a | n/a |

**Plateau test — 500 Dirichlet(alpha=5) family weightings, top-30 monthly net:** excess CAGR vs SPY p5/p50/p95 = -2.5% / -1.8% / -0.8% (1% of draws positive); vs PIT EW -1.4% / -0.7% / 0.3% (14% positive). Portfolio size (20/30/40/50), rebalance frequency (monthly/quarterly/annual) and the buffer rule all sit on the same plateau: **a flat-to-negative one**. The only positive point estimate is momentum alone (family M top-30, 1.0% vs SPY, t 0.62) - not significant, and not selectable after the fact.

**Membership-source robustness (D1 CIK-level membership = primary; D2 fja05680 spells = sensitivity):**

| Membership | Strategy | CAGR | Excess vs SPY | t | Excess vs PIT EW | IC 1m | IC t | % members priced | % scored |
|---|---|---|---|---|---|---|---|---|---|
| D1 CIK-level membership (primary) | primary_top30_ew | 12.52% | -2.58% | -1.12 | -1.49% | 0.0070 | 0.98 | 86.9% | 85.7% |
| D1 CIK-level membership (primary) | primary_topquintile_ew | 13.26% | -1.84% | -1.16 | -0.75% | 0.0070 | 0.98 | 86.9% | 85.7% |
| D1 CIK-level membership (primary) | pit_ew_universe | 14.00% | -1.10% | -0.60 | n/a | 0.0070 | 0.98 | 86.9% | 85.7% |
| D2 fja05680 spells (sensitivity) | primary_top30_ew | 12.64% | -2.46% | -0.96 | -1.31% | 0.0070 | 0.97 | 86.4% | 81.5% |
| D2 fja05680 spells (sensitivity) | primary_topquintile_ew | 13.50% | -1.60% | -0.97 | -0.45% | 0.0070 | 0.97 | 86.4% | 81.5% |
| D2 fja05680 spells (sensitivity) | pit_ew_universe | 13.95% | -1.15% | -0.63 | n/a | 0.0070 | 0.97 | 86.4% | 81.5% |

Live composite rank Spearman D1 vs D2-spells: **0.988**; live top-30 overlap 27/30 (only D1: COP, CRM, DG; only D2: APA, NEM, ROST). Material difference (>0.5 pt CAGR or rank rho <0.97): **NO**.

**Walk-forward (each calendar year out-of-sample; frozen rules; primary top-30 net):**

| Year | Top-30 | SPY | PIT EW | Excess vs SPY | Excess vs PIT EW |
|---|---|---|---|---|---|
| 2012 | 15.9% | 16.0% | 19.7% | -0.1% | -3.8% |
| 2013 | 31.8% | 32.3% | 37.1% | -0.5% | -5.3% |
| 2014 | 19.9% | 13.5% | 15.0% | 6.5% | 4.9% |
| 2015 | -1.6% | 1.2% | -1.6% | -2.9% | -0.1% |
| 2016 | 7.9% | 12.0% | 16.1% | -4.1% | -8.2% |
| 2017 | 19.8% | 21.7% | 20.6% | -1.9% | -0.9% |
| 2018 | -8.4% | -4.6% | -7.3% | -3.8% | -1.1% |
| 2019 | 16.8% | 31.2% | 31.0% | -14.4% | -14.2% |
| 2020 | -0.9% | 18.3% | 12.4% | -19.2% | -13.3% |
| 2021 | 31.3% | 28.7% | 29.8% | 2.5% | 1.5% |
| 2022 | -10.0% | -18.2% | -11.2% | 8.2% | 1.2% |
| 2023 | 11.6% | 26.2% | 15.8% | -14.6% | -4.3% |
| 2024 | 19.5% | 24.9% | 12.6% | -5.4% | 6.9% |
| 2025 | 13.9% | 17.7% | 11.2% | -3.8% | 2.7% |
| 2026 | 27.3% | 13.1% | 15.2% | 14.2% | 12.1% |

2014 onward: positive excess vs SPY in **31%** of years, vs PIT EW in 46%; worst three years vs SPY: 2020 (-19.2%), 2023 (-14.6%), 2019 (-14.4%). Majority-of-years rule vs SPY: **FAIL**.

**Punishing the strategy (primary top-30):**

| Stress | CAGR | Excess vs SPY | t | Excess vs PIT EW | t | Share of years beating SPY |
|---|---|---|---|---|---|---|
| costs 20 bps (2x) | 11.7% | -3.4% | -1.54 | -2.3% | -1.34 | 27% |
| costs 25 bps | 11.2% | -3.9% | -1.75 | -2.8% | -1.60 | 27% |
| costs 30 bps (3x) | 10.8% | -4.3% | -1.96 | -3.2% | -1.86 | 27% |
| 1-month implementation lag, 10 bps | 13.3% | -1.5% | -0.57 | -0.3% | -0.12 | - |

| Robustness | CAGR | Excess vs SPY | t | Excess vs PIT EW | t |
|---|---|---|---|---|---|
| exclude 2020-21 | 12.3% | -1.6% | -0.67 | -0.7% | -0.36 |
| drop 5 largest contributors | 10.6% | -4.5% | -2.18 | -3.4% | -2.25 |
| start 2010-01 (exploratory) | 12.4% | -2.6% | -1.12 | -1.5% | -0.83 |
| 25 bps costs | 11.2% | -3.9% | -1.75 | -2.8% | -1.60 |

Dropped contributors (sum of w x (r - r_EW)): {'MU': 0.061, 'LRCX': 0.0463, 'URI': 0.0458, 'WDC': 0.0396, 'NEM': 0.0321}.

**Legacy-model replications on the PIT infrastructure** (backtest3.py pillar formulas; v2 = Q.20 G.10 V.35 M.35; v1 = Q.25 G.18 V.20 M.14 R.23; v3 conviction proxy = handoff 9.3 loop 3):

| Model | CAGR | Excess vs SPY | t | Excess vs PIT EW | t | Avg names |
|---|---|---|---|---|---|---|
| v2_top30_monthly | 13.6% | -1.5% | -0.62 | -0.4% | -0.22 | 30.0 |
| v2_topQ_monthly | 13.7% | -1.4% | -0.78 | -0.3% | -0.31 | 69.6 |
| v2_top30_annual_sep | 12.7% | -2.1% | -0.84 | -1.0% | -0.46 | 30.0 |
| v1_top30_monthly | 11.3% | -3.8% | -1.66 | -2.7% | -1.26 | 30.0 |
| v1_topQ_monthly | 11.5% | -3.6% | -1.89 | -2.5% | -1.47 | 69.6 |
| v1_top30_annual_sep | 11.0% | -3.7% | -1.55 | -2.6% | -1.23 | 30.0 |
| v3_conviction_monthly | 13.9% | -1.2% | -0.59 | -0.1% | -0.11 | 26.1 |
| v3_conviction_annual_sep | 13.0% | -1.7% | -0.75 | -0.6% | -0.28 | 25.2 |

v3 conviction proxy, 12-month buy-and-hold from late September (compare handoff 9.3: Sep-2024 28 picks, 10.3%, 64% up, 39% beat S&P):

| Start | Picks | Avg fwd-12m | % up | % beat SPY | Universe % up | Universe avg |
|---|---|---|---|---|---|---|
| 2012-09-28 | 24 | 21.2% | 92% | 46% | 90% | 29.4% |
| 2013-09-30 | 16 | 10.9% | 75% | 19% | 88% | 18.6% |
| 2014-09-30 | 23 | 5.0% | 57% | 57% | 54% | 0.6% |
| 2015-09-30 | 18 | 20.6% | 89% | 50% | 78% | 15.8% |
| 2016-09-30 | 17 | 34.9% | 82% | 65% | 78% | 18.1% |
| 2017-09-29 | 33 | 17.6% | 73% | 36% | 71% | 15.0% |
| 2018-09-28 | 41 | 2.5% | 66% | 56% | 59% | 5.3% |
| 2019-09-30 | 33 | 7.3% | 58% | 42% | 52% | 1.8% |
| 2020-09-30 | 21 | 14.1% | 71% | 33% | 91% | 40.5% |
| 2021-09-30 | 33 | -16.8% | 21% | 48% | 25% | -13.0% |
| 2022-09-30 | 11 | 20.4% | 91% | 36% | 71% | 15.2% |
| 2023-09-29 | 29 | 33.0% | 97% | 38% | 85% | 29.8% |
| 2024-09-30 | 24 | 13.3% | 71% | 38% | 57% | 8.2% |
| 2025-09-30 | 31 | n/a | n/a | n/a | n/a | n/a |

**Bias quantification (same code, same dates; 'today' = the 503 current constituents at every date = the v3 approach):**

| Test | Today's constituents | PIT membership | Bias (CAGR pts/yr) |
|---|---|---|---|
| Primary top-30 (net) | 18.6% | 12.5% | **6.0%** |
| Primary top-quintile (net) | 17.5% | 13.3% | 4.3% |
| EW universe | 18.7% | 14.0% | 4.7% (RSP 13.0%) |
| momentum top50 gross 2012-01..2026-08 | 26.9% | 16.1% | **10.9%** |
| momentum top50 gross 2016-10..2026-08 (lead v3-audit window) | 27.9% | 15.4% | **12.5%** |

Today's-constituents excess vs SPY for the primary top-30 would have been 3.5%/yr (vs -2.6% PIT): the v3-style test manufactures a positive result out of a negative one. (Today's top-30 and today's EW universe end with the same terminal wealth to 5 digits - checked: different monthly paths, correlation 0.92 - a coincidence.)

**Residual survivorship (PIT EW - RSP):** mean 0.9%/yr (NW t 4.48), CAGR gap 1.0%, PIT above RSP in 80% of years. PIT EW excludes unpriced (acquired/failed) members; the gap to RSP (which holds them, rebalances quarterly and charges ~0.20%) estimates residual survivorship + construction differences. Conclusions sensitive to a bias of this size: absolute CAGR levels and small positive/negative excess estimates; not the sign of a -1% to -2.5%/yr excess.

| Year | PIT EW | RSP | Gap | Today EW |
|---|---|---|---|---|
| 2012 | 19.7% | 17.2% | 2.5% | 22.9% |
| 2013 | 37.1% | 35.5% | 1.6% | 40.7% |
| 2014 | 15.0% | 14.1% | 0.9% | 18.9% |
| 2015 | -1.6% | -2.7% | 1.1% | 3.7% |
| 2016 | 16.1% | 14.5% | 1.6% | 19.3% |
| 2017 | 20.6% | 18.5% | 2.1% | 27.0% |
| 2018 | -7.3% | -7.8% | 0.6% | -2.4% |
| 2019 | 31.0% | 28.9% | 2.1% | 35.0% |
| 2020 | 12.4% | 12.7% | -0.3% | 20.8% |
| 2021 | 29.8% | 29.4% | 0.4% | 31.9% |
| 2022 | -11.2% | -11.6% | 0.4% | -10.5% |
| 2023 | 15.8% | 13.7% | 2.2% | 23.4% |
| 2024 | 12.6% | 12.8% | -0.2% | 20.3% |
| 2025 | 11.2% | 11.2% | 0.0% | 16.5% |
| 2026 | 15.2% | 15.5% | -0.3% | 17.4% |

**Delisting treatment:** Yahoo purges most delisted symbols, so names rarely delist in-sample; the -30%/0% sensitivity changes nothing when the count is ~0. The survivorship problem is the unpriced members (see coverage) rather than in-sample delistings. (top-30 holding-months without a next price: 0).

**Lead's pre-fixed construction rule** (v4/code/lead_portfolio.py; quarter-end; composite rank among names with 1y vol <= 45%; top-N with <=2 per SIC-4 and <=25% of names per sector; inverse-vol weights 3-8% with 25% sector weight cap via build_weights (caps never broken, residual = T-bill cash); held quarterly; 10 bps). Historical pending-deal exclusion cannot be applied (no PIT deal data):

| Construction | CAGR | daily MaxDD | Excess vs SPY | t | TE | Excess vs PIT EW | t | P(12m ex>0) | P(36m) | P(60m) | worst 12m rel. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sleeve_top20_invvol_q (as implemented) | 10.8% | -41.7% | -4.3% | -1.81 | 8.8% | -3.2% | -1.54 | 39% | 29% | 4% | - |
| top20_ew_q | 11.6% | -42.9% | -3.5% | -1.34 | 8.9% | -2.4% | -1.05 | 45% | 34% | 11% | - |
| top30_invvol_q | 11.4% | -39.8% | -3.7% | -1.84 | 7.5% | -2.6% | -1.54 | 35% | 23% | 6% | - |
| top30_ew_q | 11.5% | -41.0% | -3.6% | -1.75 | 7.5% | -2.5% | -1.47 | 39% | 26% | 7% | - |
| blend_SPY70_sleeve30 | 13.9% | -36.1% | -1.2% | -1.81 | 2.6% | -0.1% | -0.27 | 39% | 30% | 6% | -11.1% |
| blend_SPY50_sleeve50 | 13.0% | -37.7% | -2.1% | -1.81 | 4.4% | -1.0% | -0.83 | 39% | 30% | 5% | -18.1% |

Failed-member sensitivity (as_instructed (SIVB,SBNY 2023-03; FRC 2023-05)): PIT EW CAGR 14.00% -> 13.96% (-0.05%/yr); top-30 excess vs adjusted PIT EW -1.44%; adjusted PIT EW - RSP 0.92%.

Failed-member sensitivity (harsh (FRC total loss from 2023-02-28)): PIT EW CAGR 14.00% -> 13.96% (-0.05%/yr); top-30 excess vs adjusted PIT EW -1.44%; adjusted PIT EW - RSP 0.92%.

Live sleeve under the same rule (2026-09-25, pending-deal names excluded; a screen, not a forecast): CF 4.2%, TGT 5.6%, DLTR 4.3%, HST 6.8%, JBHT 4.5%, ALL 4.2%, TRV 5.5%, TPR 4.3%, MPC 5.0%, DVA 4.1%, GL 5.8%, SWK 4.8%, BAC 5.1%, TROW 4.5%, NTAP 4.2%, NUE 5.4%, BMY 6.2%, CVS 5.5%, EXPD 5.5%, MGM 4.5%; cash 0.0%.

**DA2 data-audit fixes** (BRK EPS /1500; EPS cells with |EPS|>$500 or >50x the row's median |EPS| set missing before SUE is recomputed with D3's formula; APA revenue-based fields missing from 2021-03; ERIE Class-B share count and share-count placeholders (<1% of trailing median) set missing): live top-70 rank changes 20 (max |change| 6); entered top-70: none; left: none. HIG's live SUE/fam_S is unchanged (its bad EPS cells are historical); HAL loses its SUE (bad quarters inside its 13-quarter window). Cell counts are in the b1_panel meta (`da2_fixes`).

**Lineage fix:** XOM (entity CIK 34088) was wrongly rejected as ticker reuse because SEC now lists XOM under ExxonMobil Holdings Corp (CIK 2115436, reorganisation 2026-08); fixed with D3 lineage / D1 multi-CIK links (reuse check + fundamentals fallback). Affects the D1 run only. Live top-70 rank changes: 23 (max |change| 3); XOM live rank now 99.

**backtest-expert evaluator (primary top-30):** trade = one contiguous holding spell of a name in the monthly top-30 (entry at month-end t, exit when it leaves the top-30); trade return = compounded monthly TR over the spell (absolute mode) or minus SPY TR over the same months (excess mode); max drawdown = daily top-30 portfolio MDD; parameters = 6 (portfolio size, rebalance frequency, 3 free family weights, composite family threshold) although none were tuned; costs modelled (10 bps).

- absolute_spell_return: args `--total-trades 1597 --win-rate 59.30 --avg-win-pct 12.37 --avg-loss-pct 8.36 --max-drawdown-pct 44.38 --years-tested 14 --num-parameters 6 --slippage-tested --output-dir ` -> Score: 84/100 — Verdict: Deploy JSON: C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\outputs\b1_backtest_expert\absolute_spell_return\backtest_eval_2026-09-26_025910.json Markdown: C:\Users\user\OneDrive\D
- excess_vs_spy_spell_return: args `--total-trades 1597 --win-rate 46.27 --avg-win-pct 9.65 --avg-loss-pct 8.81 --max-drawdown-pct 44.38 --years-tested 14 --num-parameters 6 --slippage-tested --output-dir C` -> Score: 60/100 — Verdict: Refine Red flags: 1 [HIGH] Negative expectancy (-0.269%) — strategy loses money on average. JSON: C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\outputs\b1_backtest_expert\excess_v

The absolute mapping scores well only because long-only equity spells are usually positive (market beta); the excess mapping - the one that measures the model - flags negative expectancy. **Verdict: not deployable as an alpha source; at most a risk screen.**

## Files

- `v4/data/b1_panel.parquet` 106,806 rows
- `v4/data/b1_strategy_returns_monthly.parquet` 176 rows
- `v4/data/b1_calibration_panel.parquet` 76,118 rows
- `v4/data/b1_live_scores.parquet` 503 rows
- `v4/data/b1_live_scores.csv` 503 rows
- `v4/outputs/b1_results.json` 
- `v4/outputs/b1_coverage_monthly.csv` 214 rows
- `v4/outputs/b1_calibration_by_decile.csv` 10 rows
- `v4/outputs/b1_calibration_by_decile_vol.csv` 30 rows
- `v4/outputs/b1_tests_output.txt` 

Code: `v4/code/b1_common.py`, `b1_panel.py`, `b1_backtest.py`, `b1_tests.py`, `b1_report.py`.