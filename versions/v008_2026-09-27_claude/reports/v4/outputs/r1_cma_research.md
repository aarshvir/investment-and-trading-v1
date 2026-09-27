# R1: Capital-market assumptions and market regime (US large caps)

**Agent:** r1. **Written:** 2026-09-26. **Market data cutoff:** US close 2026-09-25 (S&P 500 at 7,743.41).
**Citation format:** `[Sx · date]` points to the numbered source list in §8, which gives each URL, its publication or as-of date, and the retrieval date. `[R1]` marks a number R1 computed from those sources. The code and datasets are listed in §7.

---

## 1. Answer first

### Recommended scenarios for US large-cap equities (S&P 500 total return, nominal, annualized compound, 5–10-year horizon, before fees and taxes)

| Scenario | Nominal return (compound) | Real return (approx.)¹ | Main anchors |
|---|---|---|---|
| **Bear** | **2.0%** | ≈ −0.3% | Research Affiliates 3.2% [S5 · 2026-05-21]; Vanguard low end 4.1% [S2 · 2026-06-30]; CAPE regressions give 2.6–5.0% [R1]; BlackRock "global risk premia rise" scenario 2.0% [S3 · 2026-06-30]; Goldman bear case 3% (secondary source) [S7 · 2025-11]; GMO −6%/yr over 7 years as the tail case [S4 · 2026-06-30] |
| **Base** | **6.0%** | ≈ 3.6% | Median of 12 institutional point estimates is 6.3% [R1 from S1–S13]. Horizon survey of 43 advisors: average 6.39%, median 6.7% [S14 · 2026-08]. Trimmed about 0.3pp because the five estimates dated 2026 have a median of 4.9% and CAPE is at about 41 |
| **Bull** | **9.0%** | ≈ 6.5% | BlackRock "starting point" 8.97% over 10 years and 9.44% over 5 years [S3 · 2026-06-30]; Damodaran implied return 8.84% [S15 · 2026-09-01]; Horizon survey maximum 9.1% [S14]; Goldman bull case 10% (secondary source) [S7] |
| *Reference only: prior v3 assumption* | *10.0%* | *≈ 7.5%* | *Above every institutional base case. Only BlackRock's AI-boom scenario sheet (15.9%) and Goldman's bull case reach it* |

¹ Real return = (1+nominal)/(1+2.34%) − 1. The 2.34% is the 10-year breakeven inflation rate: the 5.17% nominal 10-year Treasury yield minus the 2.83% 10-year TIPS yield [S18 · 2026-09-25].

**Cash / T-bill reserve sleeve:** assume **4.0%** for 1–3-year planning and **3.5%** for 10-year averages, with ±1pp sensitivity.
- Today's rates: 13-week bill 4.18% coupon-equivalent, 3-month CMT 4.24%, 1-year 4.50%, 2-year 4.81% [S18 · 2026-09-25]. The front end of the curve slopes up, so the market is not pricing rate cuts.
- Long-run cash assumptions in the CMAs are lower: JPM 3.1%, Schwab 3.3%, Northern Trust 3.3%, Horizon average 3.46%, Research Affiliates 3.5%, Vanguard 3.0–4.0%, BlackRock 3.66%, Morgan Stanley 3.7% (dates in §2).

**One-year return volatility:** **16%** annualized (range 15–17%). Use 19–20% for stress tests.
- CMA volatility assumptions: JPM 16.47% [S1], Horizon average 16.43% [S14], Invesco 16.6% [S12], BNY 15.9% [S13], Vanguard median 15.0% [S2]. BlackRock's 19.35% is the high outlier [S3].
- Realized volatility: daily returns 1950–2026 give 15.8% annualized; calendar-year standard deviation 1950–2025 is 17.0% [R1].
- **Compound vs arithmetic:** the scenario returns are compound (geometric). A simulator that draws arithmetic annual returns should use mean ≈ g + σ²/2. For the base case that is 6.0% + 1.3% ≈ 7.3%. JPM shows the same gap: 6.70% compound vs 7.94% arithmetic [S1].

### Why this matters for the "90% odds of profit over 5 years" claim

In an i.i.d. lognormal model with 16% volatility, a **90% chance of a 5-year gain requires an expected compound return of about 9.6% a year** [R1]. The prior 10%/yr assumption produces the 90%. The table shows the same model under each scenario (full table in `r1_scenarios.csv`):

| P(event) under the model (σ = 16%, cash = 4%) | Bear 2% | Base 6% | Bull 9% | 25/50/25 blend² | Prior 10% |
|---|---|---|---|---|---|
| 5-year total return > 0 | 61% | 79% | 89% | 77% | 91% |
| 10-year total return > 0 | 65% | 88% | 96% | 84% | 97% |
| 5-year return beats cash | 39% | 61% | 74% | 59% | 78% |
| 5-year cumulative loss worse than −20% | 18% | 7.5% | 3.4% | 9.2% | 2.5% |

² The 25/50/25 weights are R1's judgment, not sourced. Report scenario-conditional probabilities; if a single blended number is shown, state the weights.

Historical comparison [R1, Shiller data S17]:
- Since 1926, 88% of rolling 5-year windows had a positive nominal total return.
- Starting from CAPE ≥ 30, only 59% did. That is 90 monthly starts but only 12 distinct start years: 1929, 1997–2002 and 2017–2021.
- Starting from CAPE ≥ 35, only 24% did (start years 1998–2001 and 2021).

### Where the market stands (2026-09-25)

The valuation measures disagree sharply, and that disagreement explains the spread in the CMAs.
- **Cyclical and trailing measures are stretched.**
  - Shiller CAPE is about 41.2, in the 99th percentile since 1881; the record is 44.2 in December 1999 [S17, R1].
  - Trailing P/E is 25.8, above its 5-year average of 24.4 and 10-year average of 23.6 [S16 · 2026-09-25].
- **Forward P/E is only 19.2.** That is near its 10-year average of 19.0 [S16 · 2026-09-25], because consensus expects CY2026 EPS growth of +32.0% and CY2027 growth of +15.4% [S16].
- **Rates are high and risk premia thin.**
  - The 10-year Treasury yields 5.17% [S18], so the forward earnings yield (5.21%) is about the same as the 10-year yield [R1].
  - Damodaran's implied ERP is 4.14%, but that figure assumes about 14% analyst growth [S15 · 2026-09-01].
- **Concentration is near its highest level on record.** The top 10 companies are 40.4% of the S&P 500 (SPY holdings) [S20 · 2026-09-24]. JPM's 1996–2026 series peaked around 41–42% (read from chart) and stood at 37.9% on 2026-06-30 [S19].
- **Implied volatility is low.** VIX closed at 14.9 [S21 · 2026-09-25].

---

## 2. Institutional capital-market assumptions for US large caps

Returns are nominal USD, annualized compound, unless noted. "Real" is as published where available. Otherwise R1 derived it using the firm's own inflation assumption or, if none, the 2.34% breakeven. Derived values are marked *d*.

| # | Institution / edition | Published | Data as of | Horizon | Nominal | Real | Vol | Cash | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **J.P. Morgan AM**, 2026 LTCMA (30th ed.). Building blocks: revenue 6.0%, buybacks 3.0%, dividends 1.7%, margins −0.5%, dilution −1.5%, valuation −2.0%. **The 2027 edition was not found as of 2026-09-26.** | 2025-10-20 | 2025-09-30 | 10–15y | **6.7%** | 4.1% *d* (JPM inflation 2.5%) | 16.47% | 3.1% | [S1] |
| 2 | **Vanguard** VCMM. Range 4.1–6.1% (2pp band around the median; midpoint shown). US equities 4.2–6.2%; the prior run (Mar-2026) was 4.9–6.9% | 2026-07-22 | 2026-06-30 | 10y | **≈5.1%** | ≈3.1% *d* (inflation 1.5–2.5%) | 15.0% | 3.0–4.0% | [S2] |
| 3 | **BlackRock BII**, CMA Aug-2026, "Starting point" scenario (MSCI USA). 5-year: 9.44%. 10-year interquartile range 4.14–14.02%. Other scenarios: AI productivity boom 15.94%; global risk premia rise 2.02% | 2026-08 | 2026-06-30 | 10y | **8.97%** | ≈6.5% *d* | 19.35% | 3.66% (5y 3.79%) | [S3] |
| 4 | **GMO** 7-Year Forecast 2Q-2026, US Large, published as **real**: −8.1% ("normal" rates) or −5.0% ("low" rates). US cash +1.2% real | 2026-07 | 2026-06-30 | 7y | **≈−6.0%** *d* | **−8.1%** | – | 1.2% real | [S4] |
| 5 | **Research Affiliates** AAI, US Large Cap (via Fortune). Large Cap Growth 1.7% | 2026-05-21 | ~Apr/May-2026 | 10y | **3.2%** | 0.6% (inflation 2.6%) | – | 3.5% | [S5] (secondary) |
| 6 | **AQR** 2026 CMA, US Large. Prior year 4.1% real | 2026-01-14 | 2025-12-31 | 5–10y | **6.3%** | **3.9%** | – | 1.3% real | [S6] |
| 7 | **Goldman Sachs** Portfolio Strategy (Oppenheimer). Reported: about 6% EPS growth, −1%/yr valuation, 1.4% dividend yield; range 3–10%. GS US strategist Snider said 7%/yr on 2026-06-29 [S8] | 2025-11-12 | 2025-11 | 10y | **6.5%** | ≈4.1% *d* | – | – | [S7] (secondary) |
| 8 | **Morgan Stanley WM** GIC Annual CMA. Blocks: shareholder yield 4.1, valuation −1.6, nominal growth 3.9. **Stale**: no 2026 edition is publicly accessible | 2025-03-27 | 2025-03-13 | 7y | **6.3%** | ≈3.9% *d* | – | 3.7% | [S9] |
| 9 | **Charles Schwab** 2026 LTCME (2026–2035). Prior year 6.0% | 2026-01-02 | 2025-10-31 | 10y | **5.9%** | 3.4% *d* (inflation 2.4%) | – | 3.3% | [S10] |
| 10 | **Northern Trust AM** CMA 2026 edition (MSCI USA). 2025 edition: 7.5% | 2025-12 | 2025-09-30 | 10y | **6.8%** | ≈4.4% *d* | – | 3.3% | [S11] |
| 11 | **Invesco** 2026 CMA, USD, Q2 update (S&P 500). Arithmetic 6.2%. Blocks: dividends 1.31, buybacks 1.81, earnings growth 4.04, inflation 2.19, valuation −4.52 | 2026-07 | 2026-03-31 | 10y | **4.9%** | 2.7% *d* (inflation 2.19%) | 16.6% | – | [S12] |
| 12 | **BNY Investments** 2026 CMA, broad **US equity** (not large-cap specific). 2025 edition: 7.5% | 2026-01 | 2025-12-31 | 10y | **7.6%** | ≈5.1% *d* | 15.9% | – | [S13] |
| 13 | **Horizon Actuarial** 2026 survey of 43 advisors, US Large Cap average. Median 6.7%; interquartile range 5.4–7.0%; range 4.4–9.1%; 20-year average 7.02%; arithmetic 7.66%; inflation 2.44% | 2026-08 | 2026 | 10y | **6.39%** | ≈3.9% *d* | 16.43% | 3.46% | [S14] |
| 14 | **Damodaran** implied return (market-implied, not a CMA): ERP 4.14% + T-bond 4.75%. Depends on ~14% consensus growth | 2026-09-01 | 2026-09-01 | perpetuity | **8.84%** | – | – | – | [S15] |

**Summary of rows 1–12** (excludes the Horizon aggregate and Damodaran) [R1]:

| Statistic | Value |
|---|---|
| Median nominal return | **6.3%** |
| Mean | 5.2% (pulled down by GMO) |
| Interquartile range | 5.1–6.7% |
| Full range | −6.0% (GMO, derived) to 9.0% (BlackRock) |
| Median real return | ≈3.9% |
| Median of the five estimates with 2026 data dates (Vanguard, BlackRock, GMO, Research Affiliates, Invesco) | 4.9% |

**What the table shows:**
- The dispersion is regime-driven. Methods that anchor on normalized or cyclical earnings (CAPE-type) are low or negative: GMO, Research Affiliates, Vanguard, Invesco. Methods that capture the current earnings surge and AI-driven growth are high: BlackRock, which describes structural "mega forces" such as AI as "the new anchor for returns" [S3], and Damodaran.
- The building-block houses (JPM, Northern Trust, AQR, Goldman, Schwab) sit in the middle at 5.9–6.8%.
- Institutions change their numbers a lot. Goldman's published 10-year S&P 500 views went from 3% (Kostin, 2024-10) to 6.5% (Oppenheimer, 2025-11) to 7% (Snider, 2026-06) [S7, S8]. BlackRock's own scenario sheets span 2.0% to 15.9% for the same asset and horizon [S3]. **Treat CMAs as scenario anchors, not forecasts.**

---

## 3. Valuation and regime indicators (latest available as of 2026-09-26)

| Indicator | Value | As of | Source |
|---|---|---|---|
| S&P 500 close | 7,743.41 | 2026-09-25 | [S21] |
| All-time closing high | 7,798.99 (index now −0.7% below it) | 2026-08-13 | [S21, R1] |
| 2026 YTD price return; largest YTD decline | +13.1%; −9.1% | 2026-09-25 | [S21, R1] |
| **Forward 12M P/E** (FactSet) | **19.2** (5y avg 19.8, 10y avg 19.0; 20.4 on 2026-06-30) | 2026-09-25 (price of 09-24) | [S16] |
| **Trailing 12M P/E** (FactSet) | **25.8** (5y avg 24.4, 10y avg 23.6) | 2026-09-25 | [S16] |
| Consensus EPS growth CY2026 / CY2027 | **+32.0% / +15.4%** (revenue +12.3% / +9.2%). Q3-26 estimate +29.1% | 2026-09-25 | [S16] |
| Bottom-up 12M target price | 9,275.04 (+20.4%) | 2026-09-25 | [S16] |
| **Shiller CAPE** | **≈41.2** (Aug avg 41.12; Sept-1 close 40.58). 99th percentile since 1881; median since 1881 is 16.6, since 1990 is 26.4; record 44.2 (Dec-1999) | 2026-09-25 (est.) | [S17, R1] |
| JPM Guide to the Markets | Forward P/E 20.4x vs 30y avg 17.2x; CAPE 40.7x vs 28.8x; dividend yield 1.4% vs 2.0%; earnings yield minus Baa yield −0.5% vs +0.7% | 2026-06-30 | [S19] |
| **10-year Treasury** | **5.17%** (2y 4.81%, 5y 4.98%, 30y 5.49%) | 2026-09-25 | [S18] |
| **3-month T-bill** | **4.24%** (CMT); 13-week 4.18% coupon-equivalent (4.08% discount); 1-year 4.50% | 2026-09-25 | [S18] |
| 10-year TIPS real yield; implied breakeven | 2.83%; ≈2.34% | 2026-09-25 | [S18, R1] |
| **Damodaran implied ERP** | **4.14%** (T-bond 4.75%; 4.28% on 2026-08-01); implied return 8.84% | 2026-09-01 | [S15] |
| Forward earnings yield minus 10y yield | ≈ +0.04pp (5.21% − 5.17%) | 2026-09-25 | [S16, S18, R1] |
| Shiller excess CAPE yield | 1.01% | 2026-09 | [S17] |
| **Top-10 weight in S&P 500** | **40.4%** by company (Alphabet share classes combined), 38.8% by holding line; top-5 30.3%; top-20 50.6% | 2026-09-24 | [S20, R1] |
| Top-10 weight (JPM GTM) | 37.9% of market cap vs 33.7% of earnings | 2026-06-30 | [S19] |
| VIX | 14.87 (mean since 1990: 19.4; median 17.6) | 2026-09-25 | [S21, R1] |
| Realized volatility, last 12 months | 13.0% | 2026-09-25 | [S21, R1] |

**Reading the regime.** Prices, trailing multiples and concentration are at or near record levels. Forward multiples are near average only because analysts expect earnings to rise about 50% over CY2026–27 [S16]. The equity premium over bonds is close to zero on a forward-earnings basis. So outcomes hinge on whether the AI-driven earnings step-up holds (bull) or proves cyclical and margins mean-revert (bear). That is the reason to show scenario-conditional probabilities rather than one number.

---

## 4. Historical base rates (R1 calculations; data in `v4/data/r1_base_rates.csv`)

### 4.1 How often rolling windows have positive total returns (S&P 500)

Data: Shiller monthly nominal total return, all monthly starts, windows ending by 2026-08 [S17]. Return columns are annualized nominal.

| Sample | Horizon | % windows positive (nominal) | % positive (real) | Median return | 5th pct | 25th pct | Windows |
|---|---|---|---|---|---|---|---|
| 1926+ | 1y | 75.2% | 70.9% | 13.6% | −21.3% | 0.2% | 1,196 |
| 1926+ | 3y | 84.8% | 76.7% | 11.5% | −7.9% | 5.8% | 1,172 |
| 1926+ | 5y | 88.2% | 77.4% | 11.2% | −4.6% | 5.6% | 1,148 |
| 1926+ | 10y | 95.4% | 87.0% | 10.8% | 0.5% | 7.1% | 1,088 |
| 1950+ | 1y | 79.1% | 74.0% | 13.9% | −15.1% | 3.4% | 908 |
| 1950+ | 3y | 89.6% | 80.8% | 11.8% | −5.4% | 7.4% | 884 |
| 1950+ | 5y | 92.4% | 78.0% | 12.0% | −0.8% | 6.5% | 860 |
| 1950+ | 10y | 97.1% | 84.2% | 11.1% | 2.7% | 7.3% | 800 |
| 1990+ | 1y | 82.7% | 81.3% | 13.9% | −18.4% | 5.9% | 428 |
| 1990+ | 3y | 84.7% | 81.9% | 12.2% | −9.2% | 8.3% | 404 |
| 1990+ | 5y | 86.1% | 76.3% | 12.3% | −2.0% | 2.8% | 380 |
| 1990+ | 10y | 92.8% | 90.0% | 9.7% | −0.6% | 7.1% | 320 |

Cross-checks:
- Exact month-end S&P 500 total return (^SP500TR, 1990+) [S21]: 83.9% / 85.4% / 87.1% / 92.5% positive for 1/3/5/10 years, within 1.2pp of the Shiller-based figures.
- Agent r3's independent CRSP market series (1926-07 to 2026-07; file `r3_market_horizon_base_rates.csv`): 75.6% / 84.6% / 88.5% / 95.4%, within 0.4pp.

**Stocks vs T-bills.** Calendar-year windows, S&P 500 total return vs 3-month T-bill (Damodaran 1928–2025) [S22, R1]:

| Start years | 1y | 3y | 5y | 10y |
|---|---|---|---|---|
| 1928+ | 67.3% | 80.2% | 77.7% | 85.4% |
| 1950+ | 71.1% | 85.1% | 77.8% | 85.1% |
| 1990+ | 77.8% | 82.4% | 78.1% | 88.9% |

Long-run averages from the same data:

| Period | S&P 500 compound return | T-bill compound return | Calendar-year std. dev. | Share of negative years |
|---|---|---|---|---|
| 1928–2025 | 10.0% | 3.4% | 19.4% | 26.5% |
| 1950–2025 | 11.6% | 4.1% | 17.0% | 21.1% |
| 1990–2025 | 10.7% | 2.8% | 17.2% | 19.4% |

### 4.2 Drawdowns

**(a) Chance of seeing a drawdown during a holding period.** This measure does not depend on how episodes are defined. Data: ^GSPC daily closes, price only (excludes dividends), every trading-day start [S21, R1].

| Starts | Window | Max drawdown in window ≥10% / ≥20% / ≥30% | Price ever ≥10% / ≥20% / ≥30% below entry | Below entry at window end | Median max drawdown |
|---|---|---|---|---|---|
| 1928+ | 1y | 62.8% / 23.4% / 10.7% | 37.3% / 17.6% / 7.1% | 30.1% | −12.3% |
| 1950+ | 1y | 55.8% / 15.6% / 6.6% | 31.4% / 12.0% / 3.8% | 25.4% | −10.5% |
| 1990+ | 1y | 52.4% / 16.0% / 8.5% | 31.5% / 13.5% / 5.2% | 19.3% | −10.2% |
| 1928+ | 5y | 97.6% / 74.8% / 45.6% | 56.1% / 36.5% / 23.6% | 19.5% | −28.5% |
| 1950+ | 5y | 96.9% / 69.3% / 41.5% | 50.8% / 30.3% / 18.5% | 15.8% | −27.1% |
| 1990+ | 5y | 93.0% / 58.1% / 49.2% | 50.6% / 34.6% / 26.6% | 22.4% | −27.8% |

**(b) Drawdown episodes, all-time high to recovery.** Data: ^GSPC daily, price only [S21, R1]. An episode starts at an all-time high and ends when the index regains it. Durations are medians unless noted.

| Episodes since | Depth | Count (one every X years) | Median depth | Peak→trough (months) | Trough→recovery (months) | Peak→recovery (months, max) |
|---|---|---|---|---|---|---|
| 1950 | ≥10% | 24 (3.2y) | −19.8% | 5.9 | 4.9 | 14.2 (max 90) |
| 1950 | ≥20% | 11 (7.0y) | −33.5% | 14.6 | 15.2 | 24.5 (max 90) |
| 1950 | ≥30% | 6 (12.8y) | −42.1% | 17.4 | 35.0 | 52.4 (max 90) |
| 1928 | ≥20% | 12 (8.2y) | −33.7% | 15.8 | 17.5 | 25.1 (max 300: 1929→1954) |
| 1928 | ≥30% | 7 (14.1y) | −48.2% | 17.8 | 48.6 | 65.6 |
| 1990 | ≥20% | 4 (9.2y) | −41.5% | 13.1 | 31.9 | 45.1 (max 86) |
| 1990, total return (^SP500TR) | ≥20% | 4 | −40.6% | 13.1 | 25.4 | 38.5 (max 74) |

- Dividends shorten recovery: since 1990, the median ≥20% recovery took 38.5 months on a total-return basis vs 45.1 months on price.
- This definition nests later sell-offs inside earlier underwater periods (for example, 1937–38 falls inside 1929–54). That undercounts episodes before 1955.

**(c) Swing (zigzag) declines.** This is the conventional way to count bear markets. A decline of at least r from a swing high counts as one decline; it ends when the index rallies at least r from its low [S21, R1].

| Threshold | Count | Median depth | Median months, peak → regain prior high |
|---|---|---|---|
| ≥20% | 27 since 1928 (one every 3.7y); 13 since 1950 (5.9y); 6 since 1990 (6.1y) | −32.9% / −32.0% / −32.9% | 28.6 / 24.5 / 29.4 |
| ≥10% | 103 since 1928 (~1/yr); 57 since 1950 (1.35y) | −16.9% / −15.4% | 8.6 / 9.2 |
| ≥30% | 13 since 1928; 6 since 1950 | −46.3% / −42.1% | 65.6 / 52.4 |

The count of 27 swings of ≥20% since 1928 matches Ned Davis Research's count of 27 bear markets since 1928: one every 3.5 years, with an average decline of −35% and average length of 289 days (data as of Dec-2024) [S24]. The zigzag method splits 2000–02 and 2007–09 into two declines each.

**(d) Declines within a calendar year.** Data: ^GSPC daily, price [S21, R1].

| Years | Median largest decline | Mean largest decline | Years with a ≥10% decline | Years with a ≥20% decline | ≥10%-decline years that still ended positive |
|---|---|---|---|---|---|
| 1950–2025 | −10.5% | −13.7% | 55% | 17% | 55% |
| 1928–2025 | −13.1% | −16.3% | 63% | 26% | 50% |

2026 to date: largest decline −9.1%, price return +13.1%.

### 4.3 Starting valuation vs subsequent returns

**Published evidence.** Asness (2012) sorted every rolling decade since 1926 by starting Shiller P/E [S23 · 2012-11]:
- **Top decile (CAPE 25.1–46.1):** average **0.5%** real a year over the next 10 years; worst −6.1%; best 6.3%.
- **9th decile (21.1–25.1):** 0.9% average; worst −4.4%; best 8.3%.
- Ten-year returns "fall nearly monotonically as starting Shiller P/E's increase."

**R1 replication.** Shiller data, monthly starts from 1926-01 to 2016-08, next-10-year real total return [S17, R1; `r1_cape_deciles.csv`]:

| CAPE decile | CAPE range | Avg real 10y | Worst | Best | % positive |
|---|---|---|---|---|---|
| 1 | 5.6–9.7 | 10.5% | 4.3% | 18.8% | 100% |
| 5 | 14.8–16.9 | 7.3% | −2.2% | 16.1% | 92% |
| 8 | 21.0–23.1 | 3.4% | −4.0% | 13.1% | 61% |
| 9 | 23.1–26.4 | 5.7% | −3.7% | 12.3% | 87% |
| **10** | **26.5–44.2** | **1.8%** | **−5.9%** | **11.7%** | **64%** |

**Regression, full sample (1926–2016 starts), next-10-year real return on starting CAPE:**
- log(CAPE): R² = 0.30, slope t = −4.2 (Newey-West, 120 lags). At today's CAPE of 41.2 the fitted value is **+0.2%/yr real**, about **2.6% nominal**, with a residual standard deviation of ±4.4%/yr.
- Earnings-yield version (1/CAPE): R² = 0.27, fitted 2.7% real, about **5.0% nominal**.
- 5-year horizon: R² = 0.15, fitted 0.4–2.4% real, residual standard deviation 7.3%/yr.

**Conditional history** (thin samples):
- CAPE ≥ 30, 10-year: start years 1929 and 1997–2002. 5-year: those years plus 2017–2021.
- CAPE ≥ 35: start years 1998–2001, plus 2021 for the 5-year horizon.

| Starting CAPE | 10-year nominal | 5-year nominal |
|---|---|---|
| ≥ 30 | median **1.2%/yr**, worst −4.0%, positive in 56% of starts (57 months) | positive in 59% of starts |
| ≥ 35 | positive in 32% of starts | positive in 24% of starts |

**Big caveat.** CAPE regressions have been badly biased since 1990. A model fit on 1926–1989 and tested on 1990–2016 starts **under-predicted realized 10-year real returns by 6.5pp/yr on average, in 99.7% of months** (5-year horizon: 10.7pp/yr, 97.6% of months) [R1]. Current CAPE (41) is also near the edge of the historical range, so fitted values are extrapolations. This is why CAPE-driven CMAs (GMO −8.1% real, Research Affiliates 0.6% real) set the bear anchor rather than the base.

**Forward P/E evidence.** JPM's scatter of S&P 500 forward P/E vs subsequent 5-year annualized total return (1994–2026) puts the fitted line at about 5%/yr for the 20.4x of 2026-06-30. This is read from the chart and is approximate. The 1-year relationship is very noisy [S19 · 2026-06-30]. At today's 19.2x the line implies about 6%/yr, consistent with the base case.

### 4.4 Volatility

| Measure | Value | Source |
|---|---|---|
| Realized, daily returns annualized: 1928–2026 / 1950–2026 / 1990–2026 / last 10y / last 1y | 18.9% / 15.8% / 18.0% / 18.1% / 13.0% | [S21, R1] |
| Monthly total return 1988–2026, annualized | 14.7% | [S21, R1] |
| Calendar-year standard deviation: 1928–2025 / 1950–2025 | 19.4% / 17.0% | [S22, R1] |
| CMA assumptions | JPM 16.47%, Horizon average 16.43%, Invesco 16.6%, BNY 15.9%, Vanguard 15.0%, BlackRock 19.35% | §2 |
| VIX | 14.87 on 2026-09-25 (mean since 1990 19.4) | [S21] |

**Recommendation:** σ = 16% (range 15–17%). Returns have fat tails and volatility clusters. For 1-year risk use the historical figures in §4.2 (a 15–23% chance of a ≥20% drawdown within a year) rather than normal-model tails.

---

## 5. How the scenarios were built

All three scenarios use the same identity:

> return ≈ dividend yield + net buyback yield + aggregate nominal earnings growth + annual change in P/E

The inputs come from:
- **Dividend yield ≈ 1.3%.** JPM GTM gives 1.4% [S19]. Shiller trailing dividends of 81.70 on 7,743 give about 1.1% [S17, R1].
- **Net buyback yield ≈ 1.2%.** JPM's blocks are +3.0% buybacks and −1.5% dilution [S1]; Invesco's buyback yield is 1.81% [S12].
- **P/E change** is taken from today's forward P/E of 19.2x [S16].

1. **Bear, 2.0% nominal.** This is the valuation-mean-reversion outcome.
   - Blocks: 1.3% dividends, plus about 0.7% net buybacks, plus about 3.0% earnings growth as margins mean-revert from about 15%, minus about 3.1%/yr de-rating. Margins were 15.1% in 2Q26 (estimate), near the top of JPM's 2002–2026 series [S19]. The de-rating equals forward P/E falling from 19.2x to 14x over 10 years; CAPE falling from 41 to 29 would be about −3.4%/yr.
   - External anchors: Research Affiliates 3.2%, BlackRock risk-premia scenario 2.0%, Goldman bear case 3%, CAPE fits of 2.6–5.0% nominal, and the 1.2% historical median from CAPE ≥ 30 starts.
   - It is not the tail. GMO's −6%/yr over 7 years and the −4%/yr worst decade from CAPE ≥ 30 starts are stress cases.
2. **Base, 6.0% nominal.** This is the institutional consensus, trimmed slightly.
   - Blocks: 1.3% dividends, plus 1.2% net buybacks, plus about 4.5% earnings growth (roughly nominal GDP with flat margins), minus about 1.1%/yr P/E drift from 19.2x to the 30-year average of 17.2x [S19].
   - Anchors: median of 12 firms 6.3%, Horizon average 6.4%, JPM 6.7%, AQR 6.3%, Goldman 6.5%.
   - Why trim: most of these were set before the 2026 rally, and the five estimates dated 2026 have a median of 4.9%.
3. **Bull, 9.0% nominal.** This assumes the AI and earnings step-up persists without multiple compression.
   - Blocks: 1.3% dividends, plus 1.5% net buybacks, plus about 6.5% earnings growth, minus about 0.3%/yr P/E drift (19.2x to 18.6x).
   - Anchors: BlackRock 8.97% (10y) and 9.44% (5y), Damodaran implied 8.84% (which uses about 14% analyst growth), Horizon maximum 9.1%.
   - Supporting data: consensus EPS growth of +32% for CY26 and +15.4% for CY27 [S16]. JPM GTM consensus EPS is $340 for 2026, $398 for 2027 and $456 for 2028 [S19 · 2026-06-30].
   - A double-digit assumption would need P/E expansion from already-high levels or sustained earnings growth well above GDP.
4. **Cash, 4.0%.** Today's bills pay 4.2–4.5% and the market is not pricing cuts (2-year yield 4.81% [S18]). Long-run CMA cash assumptions are 3.1–3.7%, so use 3.5% for 10-year averages.
5. **Volatility, 16%.** This is the median of the CMA volatility assumptions, which bracket realized volatility since 1950.

**Practical rules for downstream agents:**
- Always state which scenario a probability depends on.
- Show all three scenarios, and the blend only with its weights.
- Keep compound and arithmetic means separate.
- Prefer a historical block bootstrap (e.g. the monthly total-return series in `v4/data`) for drawdown questions, because it keeps fat tails and clustering.

---

## 6. Limitations

- **CMAs are not reliable forecasts.** Their track records are mixed and they are revised sharply: Goldman went 3% → 6.5% → 7% within 20 months; Vanguard's US equity range fell 0.7pp in a single quarter (Mar to Jun 2026). Ten-year regression residuals are about ±4.4%/yr.
- **The estimates are not strictly comparable.** Horizons differ (5–15 years; GMO 7-year real; Morgan Stanley 7-year and dated March 2025; BNY is broad US equity). Dates range from 2025-03 to 2026-09. Market moves since then (S&P +13% YTD) mean older estimates are likely somewhat too high on a price basis, but earnings also rose.
- **Some figures are secondary.** Research Affiliates is from Fortune; I did not access its interactive tool because that would mean accepting a site disclaimer. Goldman is from TKer, Seeking Alpha and Yahoo Finance, because the GS report returned 403. The 3–10% Goldman range and its building blocks come from secondary summaries.
- **Some estimates are stale or missing.**
  - JPM's 2027 LTCMA was not released as of 2026-09-26; it is likely in Oct-2026. GMO's and Vanguard's Q3 updates are also due in Oct-2026. Refresh then.
  - Morgan Stanley's 2026 GIC update was not publicly accessible.
  - The Horizon survey aggregates many of the listed firms, so it is not an independent data point.
- **Data caveats.**
  - Shiller prices are monthly averages, which smooths returns and understates drawdown depth.
  - Shiller's Jul–Sep 2026 dividends are forward-filled and Aug/Sep CPI are Shiller estimates. The 2026-09-25 CAPE is R1's scaling of the Sept-1 value.
  - ^GSPC drawdowns are price-only.
  - Overlapping windows sharply reduce effective sample sizes: about 9 independent 10-year periods since 1926, and only 2–3 historical episodes with CAPE ≥ 30.
  - The US is a survivor market; global evidence such as Japan after 1990 shows longer losing spells.
- **The probability model is simple.** It assumes i.i.d. lognormal returns, with no valuation mean reversion or fat tails. Real-world 5-year gain frequencies have been higher than the model gives at equal mean because of historical mean reversion, but they have been much lower from CAPE ≥ 30 starts.

---

## 7. Files produced and validation

**Code**
- `v4/code/r1_base_rates.py`
- `v4/code/r1_cma_scenarios.py`

**Data** (each has a `.meta.json` with sources, retrieval time and caveats)

| File | Rows | Contents |
|---|---|---|
| `v4/data/r1_base_rates.csv` | 674 | Long-format base rates |
| `v4/data/r1_drawdown_episodes.csv` | 217 | Episode lists for 4 series plus zigzag ≥10/20/30% |
| `v4/data/r1_cape_deciles.csv` | 10 | Next-10-year real return by starting-CAPE decile |
| `v4/data/r1_cma_survey.csv` | 14 | §2 table with URLs |
| `v4/data/r1_regime_indicators.csv` | 23 | §3 table with URLs |
| `v4/data/r1_scenarios.csv` | 5 | Scenarios and model probabilities |

**Reports**
- `v4/outputs/r1_cma_research.md` (this file)
- `v4/outputs/r1_report.md` (short summary per CONVENTIONS)

**Raw cache** (`C:\Users\user\eqv4\cache\r1\`): PDFs and xlsx for JPM, GMO, AQR, Horizon (2025 and 2026), Northern Trust, Invesco, BNY, Morgan Stanley, JPM GTM, FactSet, Asness 2012, BlackRock, Vanguard; Shiller ie_data.xls; Damodaran histretSP.xls and ERPbymonth.xlsx; US Treasury CSVs; SPY holdings; yfinance CSVs for ^GSPC, ^SP500TR and ^VIX.

**Validation: 14 automated checks, all passed** (listed in `r1_base_rates.meta.json`):
- R1's real total return reproduces Shiller's own column (maximum difference 4e-16).
- The ^GSPC last close equals the lead's 7,743.41.
- The Shiller vs ^SP500TR 1-year positive shares agree within 5pp (82.7% vs 83.9%).
- Known bear markets are detected: the 2007 peak gives −56.8% and the 1929 peak gives −86.2%.
- The zigzag method finds the nested 1937, 1946, 1961 and 1966 bears and the recent 2020 and 2022 bears.
- All fractions lie in [0, 1], there are no duplicate rows, and the share of positive windows rises with horizon.

**Manual checks, all passed:**
- Agent r3's CRSP base rates agree within 0.4pp.
- The FactSet close (7,704.13 on 09-24) and the Yahoo close (7,743.41 on 09-25) are consistent.
- JPM GTM's CAPE of 40.7x (2026-06-30) is consistent with Shiller's June figure of 40.15.
- JPM's building blocks were checked against the rendered PDF exhibit. **A search-engine summary had wrongly attributed the ACWI bar to US large cap; this was corrected.**

---

## 8. Sources (all retrieved 2026-09-26 unless noted)

| ID | Source | Date | URL |
|---|---|---|---|
| S1 | J.P. Morgan AM, *2026 Long-Term Capital Market Assumptions* (full report; USD matrix; Exhibit 6). Press release: https://am.jpmorgan.com/us/en/asset-management/institutional/about-us/media/press-releases/jp-morgan-releases-2026-long-term-capital-market-assumptions/ | Published 2025-10-20; estimates as of 2025-09-30 | https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/portfolio-insights/ltcma/noindex/ltcma-full-report.pdf |
| S2 | Vanguard, *Vanguard Capital Markets Model forecasts* (table data from embedded chart i0PwL-3) | Published 2026-07-22; VCMM run 2026-06-30 | https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html |
| S3 | BlackRock Investment Institute, *Capital market assumptions* (xlsx: sheets "Starting point", "AI productivity boom", "Global risk premia rise"). Page: https://www.blackrock.com/institutions/en-us/insights/thought-leadership/capital-market-assumptions | August 2026; data as of 2026-06-30 | https://www.blackrock.com/blk-inst-c-assets/images/tools/blackrock-investment-institute/cma/blackrock-capital-market-assumptions.xlsx |
| S4 | GMO, *7-Year Asset Class Forecast: 2Q 2026*. PDF: https://www.gmo.com/globalassets/articles/gmo-7-year-asset-class-forecast/2026/gmo-7-year-asset-class-forecastjun26.pdf | As of 2026-06-30 | https://www.gmo.com/americas/research-library/gmo-7-year-asset-class-forecast-2q-2026_gmo7yearassetclassforecast/ |
| S5 | Fortune (S. Tully), Research Affiliates AAI forecasts | 2026-05-21 | https://fortune.com/2026/05/21/bond-yields-today-highest-since-2007-stocks-outlook/ |
| S6 | AQR, *2026 Capital Market Assumptions for Major Asset Classes* (Exhibits 1, 3, 7). Web: https://www.aqr.com/Insights/Research/Alternative-Thinking/2026-Capital-Market-Assumptions-for-Major-Asset-Classes | Published 2026-01-14; estimates as of 2025-12-31 | https://www.aqr.com/-/media/AQR/Documents/Alternative-Thinking/AQR-Alternative-Thinking---2026-Capital-Market-Assumptions.pdf |
| S7 | Goldman Sachs Portfolio Strategy, *Building Long-Term Returns: Our 10-Year Forecasts* (primary returned 403: https://www.gspublishing.com/content/research/en/reports/2025/11/12/0c292cc7-ce42-4fba-a026-744231e9f4f4.html). Components and range via Seeking Alpha: https://seekingalpha.com/news/4520573-decade-ahead-goldman-projects-6_5-percent-annual-return-for-s-and-p-500 | Report 2025-11-12; TKer 2025-11-13 | https://www.tker.co/p/goldman-sachs-10-year-return-forecast-2025 |
| S8 | Yahoo Finance / Business Insider, "Why Goldman has backed away from its forecast for a lost decade in stocks" (B. Snider interview 2026-06-29) | 2026-07-04 | https://finance.yahoo.com/markets/stocks/articles/why-goldman-backed-away-forecast-094002338.html |
| S9 | Morgan Stanley WM GIC, *Annual Update of GIC Capital Market Assumptions* (morganstanley.com/gicreport resolves here) | 2025-03-27 | https://www.morganstanley.com/assets/pdfs/2d9493c3-822f-4f18-8c28-ba3ad25e8473.pdf |
| S10 | Charles Schwab, *Schwab's 2026 Long-Term Capital Market Expectations* | Published 2026-01-02; data 2025-10-31 | https://www.schwab.com/learn/story/schwabs-long-term-capital-market-expectations |
| S11 | Northern Trust AM, *Capital Market Assumptions 10-Year Outlook: 2026 Edition* | Released Dec-2025; data 2025-09-30 | https://ntam.northerntrust.com/content/dam/northerntrust/investment-management/global/en/documents/thought-leadership/2026/cma/2026-capital-market-assumptions-report.pdf |
| S12 | Invesco Solutions, *2026 Capital Market Assumptions, USD, Q2 Update* (Figure 4a, Figure 6) | Estimates as of 2026-03-31; PDF 2026-07-23 | https://www.invesco.com/content/dam/invesco/emea/en/pdf/invesco-capital-market-assumption-usd.pdf |
| S13 | BNY Investments, *Capital Market Assumptions 2026: Endurance Under Pressure* | Data 2025-12-31; PDF 2026-01-23 | https://www.bny.com/content/dam/imemea/pdfs/endurance-under-pressure-capital-market-assumptions-2026-full.pdf |
| S14 | Horizon Actuarial Services, *Survey of Capital Market Assumptions: 2026 Edition* (Exhibits 4, 20, 21). Landing page: https://www.horizonactuarial.com/survey-of-capital-market-assumptions | August 2026 (PDF 2026-08-26) | https://www.horizonactuarial.com/_files/ugd/f76a4b_a73ade7e6ba748f192d531c974bbea2a.pdf |
| S15 | A. Damodaran, implied ERP (home page "Implied ERP on September 1, 2026"; ERPbymonth.xlsx). Home page: https://pages.stern.nyu.edu/~adamodar/ | 2026-09-01 | https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPbymonth.xlsx |
| S16 | FactSet, *Earnings Insight* (J. Butters), via https://www.factset.com/earningsinsight | 2026-09-25 | https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_092526.pdf |
| S17 | R. Shiller, *ie_data.xls* (monthly S&P composite, dividends, earnings, CPI, GS10, CAPE), from https://shillerdata.com/ | File saved 2026-09-02; data to Sept-2026 | https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/70fec4f5-727f-4e53-b5f1-179af109c5fa/ie_data.xls |
| S18 | U.S. Treasury, daily par yield curve, bill rates and real yield curve (2026 CSVs). Bills: …type=daily_treasury_bill_rates…; real: …type=daily_treasury_real_yield_curve… | 2026-09-25 | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv |
| S19 | J.P. Morgan AM, *Guide to the Markets – U.S.* (pages 5, 6, 8) | Data as of 2026-06-30 | https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/market-insights/guide-to-the-markets/mi-guide-to-the-markets-us.pdf |
| S20 | State Street, SPDR S&P 500 ETF (SPY) daily holdings | Holdings as of 2026-09-24 | https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx |
| S21 | Yahoo Finance via yfinance 1.7: ^GSPC (1927-12-30 to 2026-09-25), ^SP500TR (1988-01-04 onward), ^VIX (1990-01-02 onward) | Through 2026-09-25 | https://finance.yahoo.com/quote/%5EGSPC/ |
| S22 | A. Damodaran, *Historical Returns on Stocks, Bonds, Bills…* (histretSP.xls, annual 1928–2025) | Updated 2026-01-01 | https://pages.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls |
| S23 | C. Asness, "An Old Friend: The Stock Market's Shiller P/E," AQR (table: results from different starting Shiller P/Es, 1926–2012). PDF: https://www.aqr.com/-/media/AQR/Documents/Insights/White-Papers/An-Old-Friend-The-Stock-Markets-Shiller-PE.pdf | November 2012 | https://www.aqr.com/Insights/Research/White-Papers/An-Old-Friend-The-Stock-Markets-Shiller-PE |
| S24 | Hartford Funds, "10 Things You Should Know About Bear Markets" (Ned Davis Research data) | NDR 3/2025; table as of 12/2024 | https://www.hartfordfunds.com/practice-management/client-conversations/managing-volatility/bear-markets.html |
