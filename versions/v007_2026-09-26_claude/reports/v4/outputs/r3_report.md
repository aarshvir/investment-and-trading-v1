# R3 report (conventions summary) — evidence base, factor research, base rates

Built 2026-09-25T20:53:07Z. **The full deliverable is [`r3_evidence_base.md`](r3_evidence_base.md)**; this file is the conventions summary.

## Answer first
- **"90% confident" is achievable only for diversified equity exposure over ≥10–15 years** (US market positive in 95.4%–99.5% of 10–15-year windows since 1926). It is not achievable for beating the index:
  - a single stock beats it ~44% of years (Bessembinder 2018);
  - S&P 500 members did so only 28–31% of the time in 2023–25;
  - 86–93% of large-cap funds lag over 10–20 years (SPIVA YE2025).
- **Prior for our 15–30 stock large-cap Q+V+M+S tilt:** gross alpha +1%/yr (0 to +2%), TE ~7%, IR ~0.15. Expect to lag in ~44% of years.
- **Evidence behind the prior:** the French big-cap long-only mix returned +1.9%–+2.3%/yr gross over 1963–2026, but only +0.5%–+1.1% since 2010. Live factor ETFs returned -3.3% to +1.0%/yr net.
- **Haircuts:**
  - keep ≤40% of published-factor backtest alpha;
  - multiply by ~0.45 again for long-only large-cap versions of long-short factors;
  - require t ≥ 3.
- **The legacy `close10.pkl` inflates equal-weight returns by ~5.7%/yr** (survivorship). Its stock closes are also dividend-adjusted while `^GSPC` is price-only.

## What I did
1. Downloaded and validated the French factor and size×characteristic portfolio files, then computed statistics for 3 windows plus full history.
2. Ran a publication-decay check and quantified the large-cap long-only capture.
3. Measured live factor ETFs against SPY.
4. Extracted and verified SPIVA YE2025, MY2026 and Persistence YE2025, plus published stock base rates (Bessembinder, J.P. Morgan, Dimensional, S&P DJI).
5. Computed point-in-time S&P 500 beat rates on D2 data, and survivorship-biased `close10` base rates with a bias estimate.
6. Built calibration tables for P(outperform), IC→hit rate, and Harvey–Liu haircuts.

## Validation
- Factors: 9/9.
- Long-only capture: 13/13.
- Stock base rates: 4/4.
- The PIT cross-check against S&P DJI is within 1–2 points.
- Source verification status is recorded per row in the CSVs.

## Limitations
See §6 of `r3_evidence_base.md`.

## Files
| File | Rows | meta.json |
|---|---|---|
| `v4/data/r3_calendar_year_beat_rates.csv` | 11 | yes |
| `v4/data/r3_confidence_calibration.csv` | 75 | yes |
| `v4/data/r3_etf_factor_evidence.csv` | 8 | yes |
| `v4/data/r3_factor_corr.csv` | 15 | yes |
| `v4/data/r3_factor_pub_decay.csv` | 5 | yes |
| `v4/data/r3_factor_stats.csv` | 24 | yes |
| `v4/data/r3_ff_factors_monthly.parquet` | 1201 | yes |
| `v4/data/r3_largecap_longonly_monthly.parquet` | 1201 | yes |
| `v4/data/r3_largecap_longonly_stats.csv` | 42 | yes |
| `v4/data/r3_literature.csv` | 29 | yes |
| `v4/data/r3_market_horizon_base_rates.csv` | 6 | yes |
| `v4/data/r3_pit_beat_rates.csv` | 70 | yes |
| `v4/data/r3_published_base_rates.csv` | 19 | yes |
| `v4/data/r3_random_portfolio_base_rates.csv` | 21 | yes |
| `v4/data/r3_random_portfolio_te.csv` | 6 | yes |
| `v4/data/r3_spiva.csv` | 74 | yes |
| `v4/data/r3_stock_base_rates.csv` | 4 | yes |
| `v4/data/r3_survivorship_bias_estimate.csv` | 1 | yes |

Scripts: `v4/code/r3_build_report.py`, `v4/code/r3_confidence_calibration.py`, `v4/code/r3_curated_sources.py`, `v4/code/r3_ff_factors.py`, `v4/code/r3_french_lib.py`, `v4/code/r3_largecap_longonly.py`, `v4/code/r3_literature_records.py`, `v4/code/r3_pit_beat_rates.py`, `v4/code/r3_stock_base_rates.py`

Raw cache: `C:/Users/user/eqv4/cache/r3/` (French zips, Yahoo downloads, SPIVA/JPM/Bessembinder source text).
