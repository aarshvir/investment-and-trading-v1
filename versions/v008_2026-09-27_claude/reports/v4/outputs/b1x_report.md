# B1X — Independent replication of the primary backtest

_Agent B1X · generated 2026-09-26 · code `v4/code/b1x_*.py` · no `b1_*.py` file was ever opened or read_

## Answer first

**Yes, the two independent implementations agree**, after B1X's own cross-check against B1 caught and fixed a
real bug in B1X (2x-understated transaction cost). Post-fix, headline (2012-01→2026-08) net-of-cost CAGRs agree
to within **0.01–0.04 percentage points**, mean IC agrees to within **0.04pp**, live composite ranks correlate
at **Spearman ρ=0.976** (top-30 Jaccard 0.76), and SIC-derived sectors agree on **99.4%** of tickers. Both
implementations independently conclude:

1. On the honest point-in-time (PIT) universe, the pre-registered QVMS composite has **no statistically
   significant edge**: mean monthly Spearman IC ≈ 0.007–0.009 (t≈0.9–1.4), top-30/top-quintile excess return vs
   SPY is small and not significant (t between −1.0 and −0.6, net of costs).
2. Restricting the *same* backtest to **today's 503 constituents only** (task 3f bias check) manufactures a
   large, spurious edge — top-30 excess vs SPY jumps to **+4.7%/yr (t=2.2)** and the IC even flips sign — purely
   from hindsight survivor selection. This is a large, quantified warning against judging the live portfolio by
   a "current members" backtest.
3. No further disagreement exceeds the task's investigation thresholds (>1pt CAGR, live-rank corr <0.95).

## What B1X built (own code, independent of B1)

- **Membership**: `d1_membership_monthly.parquet`/`d1_cik_map.csv`/`d1_sector_map.csv` were polled and never
  appeared (checked repeatedly to 02:39; D3's own report confirms it hit the same gap). Used the documented
  fallback, `v4/data/d2_universe_spells.csv` (labelled `d2_universe_spells_fallback` in all outputs) — **the
  same fallback B1 chose independently**, confirming it was the right call.
- **Sectors**: SIC code from `d3_company_meta.csv` (SEC-sourced) run through **D1's own `sic_to_sector()`**
  function (`d1_sic_sector_rules.py` — a deterministic classification table, not backtest logic, so using it
  doesn't compromise independence; it also lets both agents rank within the *same* sector definitions as the
  task requires). 660 CIKs classified into 11 GICS-like sectors; 99.4% match B1's independent sector calls.
- **Panel**: month-ends 2010-01→2026-08 (200 months), universe = PIT member (from spells) with a `d2_close`
  price. `market_cap = d2_close(t) × d3_pit_monthly_lag1.shares_out(t) × split_factor_after(t) × midwindow_
  split_factor(t)`, where both split factors are **derived by B1X from `d2_splits.parquet`** (product of
  `split_ratio` for splits after `t`, and separately for splits between `shares_out_date` and `t`) — never read
  from a precomputed column. **BRK-B** shares scaled ×1500 (Class-A-equivalent fix, per D3's own report §5.6;
  verified: implied market cap moved from ~$0.8B, absurd, to ~$1.24T, correct order of magnitude).
- **Fundamentals**: `d3_pit_monthly_lag1.parquet` (filed<t, D3's own recommendation) for the backtest;
  `d3_pit_monthly.parquet` (filed≤t) for the live snapshot. SUE taken directly from D3's precomputed field.
- **Composite**: Q (7 metrics), V (4), M (12-1 momentum), S (SUE) exactly per STATE.md; each raw ratio
  winsorised at the 1st/99th pct **per month** (lead instruction, per D3's flagged scale errors); sector-neutral
  percentile per metric → mean of available → re-percentiled → family score; composite = mean of ≥3/4 families.
  Financials (`is_financial`): OCF/FCF/accrual/leverage metrics set to **missing, not zero** (D3 report §5: bank
  OCF/leverage are not economically comparable).
- **Bias check (3f)**: the *same* pipeline re-run with the eligible universe forced to today's 503 tickers only,
  every historical month, re-ranking within that smaller cross-section (not just re-weighting the same ranks).
- **Live (3g)**: 2026-09-25, current constituents, non-lag fundamentals. 494/503 (98.2%) get a composite.

## B1 vs B1X — headline numbers (2012-01→2026-08, net of 10bps one-way costs unless noted)

| Metric | B1 | B1X | Diff |
|---|---:|---:|---:|
| Composite IC, mean (monthly) | 0.00703 (t=0.97) | 0.00659 (t=0.91) | 0.00044 |
| Family IC, full period: Q / V / M / S | .0055/.0004/.0074/.0068 | .0045/−.0003/.0069/.0083 | all ≤0.0015 |
| Top-30 EW, net CAGR | 12.641% | 12.679% | **0.04pt** |
| Top-30 excess vs SPY (net) | −2.459% | −2.422% | **0.04pt** |
| Top-quintile EW, net CAGR | 13.497% | 13.512% | **0.01pt** |
| Top-quintile excess vs SPY (net) | −1.604% | −1.589% | **0.01pt** |
| SPY CAGR (bench) | 15.101% | 15.101% | 0.000pt |
| PIT EW-universe CAGR | 13.951% | 13.976% | 0.03pt |
| Avg one-way turnover, top-30/quintile | 31.3%/24.5% | 30.9%/23.7% | ~1pt |
| Live composite: Spearman rank corr | — | **0.976** | (>0.95 bar) |
| Live top-30 Jaccard overlap | — | **0.76** (26/30) | |
| SIC sector agreement | — | **99.4%** | |

All CAGR/IC differences are far inside the task's ">1pt CAGR" / "<0.95 rank-corr" investigation triggers.

## Bug found (in B1X, via this cross-check) and fixed

Transaction cost was originally `cost = one_way_turnover × 10bps` where `one_way_turnover = 0.5·Σ|Δw|` (one
leg only). A monthly rebalance has **two** legs (sell old names, buy new names), each incurring the 10bps
one-way rate, so the correct cost is `2 × one_way_turnover × 10bps`. Pre-fix, B1X's net CAGRs were ~0.4–0.9pt
too high (turnover itself matched B1 almost exactly — 30.9% vs 31.3% — isolating the bug to the cost formula,
not the portfolio construction). Fixed in `b1x_backtest.py`; post-fix agreement is within 0.01–0.04pt (table
above). **This is the kind of error dual independent implementation exists to catch.**

## Explained (non-bug) differences

- **Net share issuance**: B1X uses the balance-sheet share-count change (`shares_out/shares_1y_ago − 1`); B1
  appears to use a cash-flow-based measure. STATE.md doesn't pin down which; both are standard. Likely the main
  driver of the 4/30 live top-30 name mismatches (AES/ALB/COP/KVUE vs AIZ/GL/HIG/TROW — all marginal, similar-
  quality names swapping near the cutoff, not divergent picks).
- **ROE denominator**: B1X averages `equity` and `equity_1y_ago`; B1 likely uses point-in-time equity only
  (raw leverage/accruals/asset-growth *magnitudes* matched B1 to 6 decimal places on spot checks — e.g. CF
  Industries' `mom_12_1`=0.479611 and `sue`=3.241627 were bit-identical — so this is an isolated convention
  choice, not a systemic issue).
- **n_months for composite IC**: B1 176 vs B1X 175 — one month differs in the ≥10-names-with-data threshold;
  immaterial to the means.

## Bias check (task 3f) — full detail

| | Full PIT universe | Today's constituents only | Δ (survivorship) |
|---|---:|---:|---:|
| Mean IC (2012-01+) | +0.0066 (t=0.91) | **−0.0019** (t=−0.28) | −0.0085 |
| Top-30 gross excess vs SPY | −1.60% (t=−0.59) | **+4.65%** (t=2.21) | **+6.26pt** |
| EW-universe CAGR (2012-01+) | 13.98% | 18.67% | +4.7pt |

Confirms and quantifies D2's own survivorship warning (§7): a backtest restricted to known survivors both
inflates returns and flips the factor's apparent skill.

## Known limitations

1. D1's PIT membership/CIK/sector files never materialized during this run; the D2-spells fallback carries
   D2's own membership caveats (§7 of d2_report.md — reconstructed from a community CSV, not authoritative).
2. Market cap is unreliable for ~1% of names with non-standard share structures: **ERIE** (XBRL picked up the
   tiny Class-B share count, not Class-A; mktcap off by >99%) and Up-C/OP-unit names (ARES, IBKR, TKO, BX) —
   **B1 independently flagged the identical set of failure modes**, so this is a shared, known XBRL-sourcing
   gap, not a B1X-specific error. 94.8% of live market caps are within 5% of D4's independent Yahoo snapshot
   (B1 reports 93.4% by its own method).
3. Delisting returns are D2's `Close`-to-`Close` reality (no CRSP-style delisting return); dropped, not
   zeroed, when a next-month return is unavailable.
4. Dual-class tickers sharing one CIK (GOOG/GOOGL, FOX/FOXA, NWS/NWSA) get identical company-level fundamentals
   per class; market cap uses total reported shares, not class-specific float.

## Files produced

`code/b1x_common.py, b1x_build.py, b1x_backtest.py, b1x_live.py, b1x_compare.py` · `data/b1x_panel_full.parquet`
(82,166 rows), `b1x_panel_current.parquet` (94,225 rows), `b1x_live_scores.parquet` (503 rows), `b1x_ic_series_
full.csv`, `b1x_monthly_returns_{full,current}.csv` + `.meta.json` sidecars · `outputs/b1x_results.json`,
`b1x_vs_b1_comparison.json`, this report.
