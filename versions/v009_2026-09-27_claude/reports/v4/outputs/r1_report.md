# r1_report: CMA and market-regime research (summary)

The full deliverable, with a source URL and date for every number, is **`v4/outputs/r1_cma_research.md`**.
Data cutoff is the US close on 2026-09-25 (S&P 500 at 7,743.41).

## Answer first

**Recommended return scenarios for US large caps** (S&P 500 total return, nominal, compound, 5–10 years):

| Scenario | Nominal | Real (approx.) |
|---|---|---|
| Bear | 2.0% | −0.3% |
| Base | 6.0% | 3.6% |
| Bull | 9.0% | 6.5% |

**Other assumptions:**
- **Cash / T-bill sleeve:** 4.0% (use 3.5% for 10-year averages).
- **Volatility:** 16% a year (range 15–17%).
- **Simulators using arithmetic returns:** set the mean to g + σ²/2 (base case ≈ 7.3%).

**Evidence behind the scenarios:**
- **12 institutional estimates** (JPM, Vanguard, BlackRock, GMO, Research Affiliates, AQR, Goldman, Morgan Stanley, Schwab, Northern Trust, Invesco, BNY):
  - median 6.3%; interquartile range 5.1–6.7%;
  - range from −6.0% (GMO, 7-year, derived from −8.1% real) to 8.97% (BlackRock, 10-year);
  - the five estimates with 2026 data dates have a median of 4.9%.
- **Horizon 2026 survey of 43 advisors:** average 6.39%, median 6.7%.
- **JPM 2027 LTCMA:** not yet released (the 2026 edition says 6.7%).

**The prior "90% odds of profit over 5 years" depends on the return assumption.** With 16% volatility it needs about 9.6%/yr expected compound return. Under the recommended scenarios, P(5-year gain) is 61% (bear), 79% (base) and 89% (bull).

**Regime:**
- Valuation: CAPE is about 41.2 (99th percentile since 1881), but the FactSet forward P/E is 19.2 because consensus expects EPS growth of +32% in CY26 and +15.4% in CY27.
- Rates: the 10-year Treasury yields 5.17% and the 3-month bill 4.24%. The forward earnings yield is only 0.04pp above the 10-year yield. Damodaran's implied ERP is 4.14% (2026-09-01).
- Concentration and volatility: the top 10 companies are 40.4% of the index, and the VIX is 14.9.

## What I did

- Collected 13 institutional CMAs plus Damodaran's implied return, using primary PDFs and xlsx files where possible.
- Collected regime indicators from FactSet, Shiller, US Treasury, JPM Guide to the Markets and SPY holdings.
- Computed base rates from Shiller monthly data (1871–2026), daily ^GSPC and ^SP500TR, and Damodaran annual data (1928–2025): rolling returns, stocks vs bills, drawdown episodes (two definitions), holding-window drawdown probabilities, intra-year declines, CAPE deciles and regressions with an out-of-sample check, and volatility.

## Key base rates (details in §4 of the research file)

**Rolling returns:** the share of positive nominal windows since 1926 was 75% for 1 year, 85% for 3 years, 88% for 5 years and 95% for 10 years.

**Drawdowns since 1950:**
- Within a 1-year window: a ≥20% drawdown occurred 16% of the time.
- Within a 5-year window: 69% of the time.
- Once the index fell ≥20% from an all-time high, the median time to regain that high was 24.5 months.
- There have been 27 swings of ≥20% since 1928, matching Ned Davis Research's count of bear markets.

**Starting CAPE:**
- Top decile (CAPE 26.5–44): average next-10-year real return 1.8%.
- Starting CAPE ≥ 30: the median 10-year nominal return was 1.2%/yr.
- But CAPE models have under-predicted realized returns by about 6.5pp/yr since 1990.

## Validation

**Automated checks: 14 of 14 passed** (listed in `v4/data/r1_base_rates.meta.json`).

**Manual cross-checks, all passed:**
- Agent r3's CRSP-based base rates agree within 0.4pp.
- ^SP500TR vs Shiller agree within 1.2pp.
- FactSet and Yahoo closes are consistent.
- JPM GTM's CAPE is consistent with Shiller's.
- JPM building blocks were verified against the rendered PDF, which corrected a search-summary error.

## Limitations

- The Research Affiliates and Goldman figures come from secondary sources.
- Morgan Stanley's latest public CMA is from 2025-03.
- Horizons and dates differ across institutions.
- The high-CAPE historical samples are thin: 2–3 episodes.
- Shiller prices are monthly averages, which smooths returns and drawdowns.
- The probability model is illustrative: i.i.d. lognormal returns.
- Refresh in October 2026, when JPM's 2027 LTCMA and GMO's and Vanguard's Q3 updates are due.

## Files

**Code:**
- `v4/code/r1_base_rates.py`
- `v4/code/r1_cma_scenarios.py`

**Data** (each has a `.meta.json`):

| File | Rows |
|---|---|
| `v4/data/r1_base_rates.csv` | 674 |
| `v4/data/r1_drawdown_episodes.csv` | 217 |
| `v4/data/r1_cape_deciles.csv` | 10 |
| `v4/data/r1_cma_survey.csv` | 14 |
| `v4/data/r1_regime_indicators.csv` | 23 |
| `v4/data/r1_scenarios.csv` | 5 |

**Raw downloads:** `C:\Users\user\eqv4\cache\r1\`
