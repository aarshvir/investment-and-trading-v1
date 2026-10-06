# D2 - Price history & total returns (S&P 500 members since 2000 + benchmarks)

_Agent D2 · generated 2026-09-25T20:57:24Z · market-data cutoff US close 2026-09-25 · all numbers from `v4/outputs/d2_qc_summary.json` and `d2_validation_results.json`_

## Answer first

- **Built**: daily Close (split-adj.), Adj Close (total-return), Volume, dividends and splits for **1,172 Yahoo symbols** (1,136 equities that were S&P 500 members at any time since 2000, plus 36 benchmarks/ETFs/UCITS lines), 1995-01-03 → 2026-09-25 (7,986 NYSE trading days). Monthly total-return panel: 380 month-ends (1995-01-31 → 2026-08-31).
- **Current constituents**: all 503 have Yahoo data ending 2026-09-25 (check (c): 503/503 pass). All 36/36 benchmark/ETF/UCITS symbols returned data.
- **Survivorship (the main limitation)**: of 633 historical, non-current member symbols, **408 (64.5%) have no Yahoo data at all** (of the 596 from the fja05680 list: 380; 20 of those are explained by later ticker renames). Measured on index member-days, Yahoo prices exist for only **50% of 2000-04, 58% of 2005-09, 69% of 2010-14, 79% of 2015-19 and 93% of 2020-26** (best case incl. detected renames: 52%, 61%, 72%, 83%, 95%). A Yahoo-only backtest therefore sees roughly half of the 2000-04 index; the missing half is dominated by acquired and failed companies. B1 must treat pre-2015 results as survivorship-biased.
- **Identity risk**: 76 symbols are flagged `reuse_suspect` (Yahoo now serves a different company under the old symbol, e.g. WB = Weibo not Wachovia). Reverse-merger histories (T = SBC before 2005, JCI = Tyco before 2016, JPM = Chase before 2001, WEN = Triarc before 2008) cannot be detected from prices; join prices to membership through D1's CIK-level identifiers, not raw tickers.
- **Second-source validation** (Stooq blocked by a JavaScript bot challenge → CNBC public endpoints used): 60 tickers × 25 random dates since 2010: **96.7% of Yahoo Closes within 0.5%** (current 99.8%, historical 90.6%); 48 of 49 misses are constant corporate-action adjustment offsets (spin-offs/special dividends adjusted differently), so 99.93% agree up to a constant; daily returns on the same dates agree within 0.5pp for 99.8%.
- **Benchmark integrity**: SPY Adj Close vs ^SP500TR 2009-12-31→2026-09-25: CAGR 14.25% vs 14.36% → **tracking difference -0.11%/yr** (expected ≈ −0.1%; IVV -0.09%, VOO -0.07%). ^GSPC matches CNBC/FRED within 0.01% on 99.80%/99.92% of days. RSP (equal-weight, TR) vs ^GSPC (cap-weight, price): 0.08%/yr, daily correlation 0.953.
- **Data quality**: Adj Close internally consistent with Yahoo dividends (1 mismatch in 51,183 dividend events; 0 tickers with factor > 1 or decreasing); 0 non-positive equity prices; 481 daily moves >50% flagged in `d2_bad_ticks.csv` (110 inside a valid index membership); CNBC confirms 199/209 checkable large moves as real. **Yahoo spin-off double counts corrected** in Adj Close: ABT@2004-05-03 x1.0742, CNP@2002-10-01 x1.1110, DHR@2016-07-05 x1.5555, DLX@2001-01-02 x1.3350, ETN@2001-01-02 x1.1910 (raw kept in `d2_adjclose_yahoo_raw.parquet`).

## 1. What was built (method)

**Universe** (`d2_universe.csv`, script `d2_universe.py`):
- Wikipedia *List of S&P 500 companies* table 1 → 503 current symbols (https://en.wikipedia.org/wiki/List_of_S%26P_500_companies, retrieved 2026-09-25T20:24:24Z).
- The *Selected changes* table no longer lives on that page; it moved to *Historical components of the S&P 500* (https://en.wikipedia.org/wiki/Historical_components_of_the_S%26P_500); all Added/Removed tickers were taken (37 equity symbols appear only there, 8 of them only in pre-2000 changes; kept and tagged `wiki_pre2000_only`).
- fja05680 *S&P 500 Historical Components & Changes (Updated).csv* (https://raw.githubusercontent.com/fja05680/sp500/master/S%26P%20500%20Historical%20Components%20%26%20Changes%20%28Updated%29.csv): union of all tickers on any row dated ≥ 2000-01-01 → 1097 symbols; last row 2026-08-18; Wikipedia changes after that date applied (+BE@2026-09-21, -TAP@2026-09-21, +P@2026-09-21, -TTD@2026-09-21, +ILMN@2026-09-21, -BLDR@2026-09-21). Reconstructed final membership equals the Wikipedia current list exactly (0 differences). No `-YYYYMM` suffixes occur in this file vintage (rule implemented, 0 stripped).
- Normalised to Yahoo style (`.`→`-`, e.g. BRK-B, BF-B); original symbols kept in `ticker_orig`. 36 benchmark/ETF/UCITS symbols added. Total 1172 symbols.

**Download** (`d2_download.py`): `yf.download(batch, start='1995-01-01', end='2026-09-26', auto_adjust=False, actions=True, group_by='ticker', threads=6)` in batches of 60 (threads capped at 6 per CONVENTIONS instead of `True`, which would use 2×CPU threads); every batch cached as long-format parquet in `C:\Users\user\eqv4\cache\d2\batches`; all empty symbols retried one-by-one with `Ticker.history` and exponential backoff (2 clean 'no data' answers required); a Yahoo chart-metadata pass (longName, exchange, currency, instrumentType, firstTradeDate) supports identity checks. No rate-limit errors occurred. The first pass ran ~15 min after the 2026-09-25 close while the daily bar was still live, so the last 3+ weeks were re-downloaded later (`refresh` phase) and patched in; see §6.

**Panels** (`d2_build.py`): wide parquet, index = NYSE trading days (the ^GSPC calendar; no stock-only trading days found), columns = Yahoo symbols. UCITS `.L` lines are kept in separate `d2_ucits_*` files on their own LSE calendar (mixing calendars would create UK-only rows and misaligned daily returns). Monthly returns = Adj Close(last NYSE trading day of month) / Adj Close(previous month-end) − 1, NaN if either end is missing (no filling); September 2026 is incomplete at the cutoff, so the last row is 2026-08-31. 26 cells are NaN because a stock traded during a month but not on the month-end day. Series that end mid-month (delistings) get a separate partial-month return in `d2_final_partial_month.csv` — not a CRSP-style delisting return.

## 2. Coverage and survivorship bias

| Status | Current constituents | Historical (non-current) members | Benchmarks/ETFs |
|---|---|---|---|
| active | 503 | 208 | 36 |
| ended_before_2026-09-25 | 0 | 17 | 0 |
| no_data | 0 | 408 | 0 |

Member-day coverage (share of (member, trading-day) pairs since 2000 for which Yahoo has a price). *strict* = same ticker; *valid* = strict excluding reuse-suspect tickers; *best* = valid plus detected rename successors (heuristic, §5):

| Era | Member-days | Strict | Valid | Best (incl. renames) | Tickers with missing days (best) |
|---|---|---|---|---|---|
| 2000-2004 | 620,616 | 50.2% | 50.2% | 52.5% | 340 |
| 2005-2009 | 625,982 | 58.5% | 58.5% | 61.4% | 290 |
| 2010-2014 | 625,796 | 68.7% | 68.7% | 71.9% | 190 |
| 2015-2019 | 634,675 | 79.2% | 79.2% | 82.7% | 149 |
| 2020-2026 | 852,277 | 93.5% | 93.5% | 95.1% | 61 |

Average number of index members with a Yahoo price on a given day:

| Year | 2000 | 2002 | 2005 | 2008 | 2010 | 2012 | 2015 | 2018 | 2020 | 2022 | 2024 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Members | 492 | 495 | 496 | 497 | 498 | 497 | 501 | 506 | 505 | 504 | 503 | 503 |
| With price (strict) | 232 | 250 | 265 | 304 | 327 | 341 | 368 | 412 | 441 | 464 | 483 | 499 |
| With price (best) | 241 | 261 | 278 | 319 | 343 | 357 | 385 | 431 | 457 | 474 | 488 | 500 |

**Most important missing members by era** (ranked by missing member-days in the era after renames; names/reasons from the Wikipedia changes table where available — the table is sparse before 2011, so many older names are blank; D1's membership file will carry authoritative names):

- **2000-2004** (340 symbols with missing days; showing missing days in era / total member-days since 2000): `CMA` (Comerica; Market capitalization changes.) 1256d/6156d; `AGN` (Allergan; Allergan was acquired by AbbVie. || Allergan was acquired by…) 1256d/5121d; `ARNC` (Arconic; Arconic separated into 2 companies - Howmet remained in the …) 1256d/5096d; `CBS` 1256d/5013d; `APC` (Anadarko Petroleum; Occidental Petroleum acquired Anadarko Petroleum.) 1256d/4931d; `AET` (Aetna; CVS acquired Aetna.) 1256d/4758d; `CA` (CA Technologies; CA was acquired by Broadcom.) 1256d/4742d; `BCR` (CR Bard; Becton Dickinson acquired CR Bard.) 1256d/4527d; `BBBY` (Bed Bath & Beyond; Market capitalization changes.) 1256d/4418d; `AABA` 1256d/4392d; `CEG` (Constellation Energy; Constellation was acquired by Exelon) 1256d/4233d; `CCE` (Coca-Cola Enterprises; Coca-Cola Enterprises merged with European bottlers.) 1256d/4127d; `AVP` (Avon Products; Market capitalization changes.) 1256d/3827d; `BMS` (Bemis; BMS changed to AMCR post merger with Amcor; subsequently ren…) 1256d/3755d; `BR` (Broadridge Financial Solutions) 1256d/3650d
- **2005-2009** (290 symbols with missing days; showing missing days in era / total member-days since 2000): `DOW` (Dow; The Dow Chemical Company renamed to DowDuPont Inc.) 1259d/6327d; `CMA` (Comerica; Market capitalization changes.) 1259d/6156d; `EA` (Electronic Arts; An investor consortium comprising Saudi Arabia's Public Inve…) 1259d/6048d; `CTXS` (Citrix Systems; Vista Equity Partners acquired Citrix Systems.) 1259d/5724d; `GPS` (Gap; Market capitalization changes.) 1259d/5557d; `FOXA` (21st Century Fox; 21st Century Fox merged with Disney and some parts spun off …) 1259d/5476d; `AGN` (Allergan; Allergan was acquired by AbbVie. || Allergan was acquired by…) 1259d/5121d; `ARNC` (Arconic; Arconic separated into 2 companies - Howmet remained in the …) 1259d/5096d; `APC` (Anadarko Petroleum; Occidental Petroleum acquired Anadarko Petroleum.) 1259d/4931d; `AET` (Aetna; CVS acquired Aetna.) 1259d/4758d; `CA` (CA Technologies; CA was acquired by Broadcom.) 1259d/4742d; `BCR` (CR Bard; Becton Dickinson acquired CR Bard.) 1259d/4527d; `BBBY` (Bed Bath & Beyond; Market capitalization changes.) 1259d/4418d; `AABA` 1259d/4392d; `COL` (Rockwell Collins; UTX acquired Rockwell Collins.) 1259d/4379d
- **2010-2014** (190 symbols with missing days; showing missing days in era / total member-days since 2000): `DOW` (Dow; The Dow Chemical Company renamed to DowDuPont Inc.) 1258d/6327d; `CMA` (Comerica; Market capitalization changes.) 1258d/6156d; `EA` (Electronic Arts; An investor consortium comprising Saudi Arabia's Public Inve…) 1258d/6048d; `CTXS` (Citrix Systems; Vista Equity Partners acquired Citrix Systems.) 1258d/5724d; `GPS` (Gap; Market capitalization changes.) 1258d/5557d; `FOXA` (21st Century Fox; 21st Century Fox merged with Disney and some parts spun off …) 1258d/5476d; `AGN` (Allergan; Allergan was acquired by AbbVie. || Allergan was acquired by…) 1258d/5121d; `ARNC` (Arconic; Arconic separated into 2 companies - Howmet remained in the …) 1258d/5096d; `APC` (Anadarko Petroleum; Occidental Petroleum acquired Anadarko Petroleum.) 1258d/4931d; `AVB` (AvalonBay Communities; Equity Residential (now Vivmark Residential) acquired Avalon…) 1258d/4931d; `AET` (Aetna; CVS acquired Aetna.) 1258d/4758d; `CA` (CA Technologies; CA was acquired by Broadcom.) 1258d/4742d; `BCR` (CR Bard; Becton Dickinson acquired CR Bard.) 1258d/4527d; `DFS` (Discover Financial; Capital One acquired Discover Financial.) 1258d/4499d; `BBBY` (Bed Bath & Beyond; Market capitalization changes.) 1258d/4418d
- **2015-2019** (149 symbols with missing days; showing missing days in era / total member-days since 2000): `K` (Kellanova; Mars Inc. acquired Kellanova.) 1258d/6525d; `IPG` (Interpublic Group; Omnicom Group acquired (The) Interpublic Group.) 1258d/6516d; `WBA` (Walgreens Boots Alliance; Sycamore Partners acquired Walgreen Boots Alliance.) 1258d/6452d; `HES` (Hess Corporation; Chevron acquired Hess.) 1258d/6426d; `MRO` (Marathon Oil; ConocoPhillips acquired Marathon Oil.) 1258d/6265d; `CMA` (Comerica; Market capitalization changes.) 1258d/6156d; `EA` (Electronic Arts; An investor consortium comprising Saudi Arabia's Public Inve…) 1258d/6048d; `SEE` (Sealed Air; Market capitalization changes.) 1258d/6028d; `CTXS` (Citrix Systems; Vista Equity Partners acquired Citrix Systems.) 1258d/5724d; `XLNX` (Xilinx; Advanced Micro Devices acquired Xilinx.) 1258d/5566d; `GPS` (Gap; Market capitalization changes.) 1258d/5557d; `LEG` (Leggett & Platt; Market capitalization changes.) 1258d/5527d; `TIF` (Tiffany & Co; LVMH Moet Hennessy-Louis Vuitton SE acquired Tiffany & Co.) 1258d/5169d; `JWN` (Nordstrom; Market capitalization changes.) 1258d/5149d; `AGN` (Allergan; Allergan was acquired by AbbVie. || Allergan was acquired by…) 1258d/5121d
- **2020-2026** (61 symbols with missing days; showing missing days in era / total member-days since 2000): `AVB` (AvalonBay Communities; Equity Residential (now Vivmark Residential) acquired Avalon…) 1663d/4931d; `EA` (Electronic Arts; An investor consortium comprising Saudi Arabia's Public Inve…) 1654d/6048d; `HOLX` (Hologic; Blackstone Inc. and TPG Inc. acquired Hologic.) 1574d/2521d; `K` (Kellanova; Mars Inc. acquired Kellanova.) 1494d/6525d; `IPG` (Interpublic Group; Omnicom Group acquired (The) Interpublic Group.) 1485d/6516d; `WBA` (Walgreens Boots Alliance; Sycamore Partners acquired Walgreen Boots Alliance.) 1421d/6452d; `HES` (Hess Corporation; Chevron acquired Hess.) 1395d/6426d; `ANSS` (Ansys; Synopsys acquired Ansys.) 1392d/2031d; `JNPR` (Juniper Networks; Hewlett Packard Enterprise acquired Juniper Networks.) 1385d/4804d; `DFS` (Discover Financial; Capital One acquired Discover Financial.) 1351d/4499d; `MRO` (Marathon Oil; ConocoPhillips acquired Marathon Oil.) 1234d/6265d; `CTRA` (Coterra Energy; Devon Energy acquired Coterra Energy.) 1152d/1152d; `WRK` 1134d/2267d; `CMA` (Comerica; Market capitalization changes.) 1125d/6156d; `PXD` (Pioneer Natural Resources; ExxonMobil acquired Pioneer Natural Resources.) 1094d/3931d

_Only the top 40 per era are stored in `d2_qc_summary.json`; the full list is `d2_coverage.csv` (status=no_data, member_days_since2000)._

## 3. Independent second-source validation

**Stooq** (`https://stooq.com/q/d/l/?s={sym}&i=d`) was probed at 2026-09-25T20:41:06Z: every request returned HTTP 200 with an HTML page "This site requires JavaScript to verify your browser" (SHA-256 proof-of-work challenge), not CSV. Solving it programmatically would circumvent bot detection, so Stooq was **not used**. Fallback: CNBC's public market-data endpoints (no key/login): daily bars `ts-api.cnbc.com/harmony/app/bars/<SYM>/1D/.../adjusted/...` (split-adjusted, not dividend-adjusted, i.e. the same definition as Yahoo `Close`; history back to 1995) and the quote service `quote.cnbc.com/.../restQuote` (latest close). FRED (SP500, VIXCLS, DGS10, DTB3) and CBOE (VIX history) were used for index series. Nasdaq's API hung without a browser User-Agent and was not pursued (no impersonation).

**(i) Random sample** — 40 current constituents + 20 historical members still trading (seeded, reuse suspects excluded), 25 random common dates since 2010 each (1500 observations):

| Metric | All | Current | Historical |
|---|---|---|---|
| Yahoo Close within 0.5% of CNBC | 96.7% | 99.8% | 90.6% |
| … within 0.1% | 96.5% | | |
| within 0.5% or constant adjustment offset | 99.93% | | |
| Daily return within 0.5pp (same dates) | 99.8% | | |
| Daily return within 0.1pp | 99.7% | | |

Outliers (49 obs in 6 tickers: BBWI, CLF, FTI, MSI, NKTR, NOV) were investigated on the full common history (`d2_validation_outliers.csv`, `d2_validation_ratio_steps.csv`). 48 are **constant multiplicative offsets** that start/stop exactly at spin-off or special-distribution dates (e.g. NOV 2014 NOW Inc. spin-off booked by Yahoo as a 1.109 'split'; FTI 2008 JBT and 2021 Technip Energies spin-offs; MSI 2011 Motorola Mobility; BBWI/L Brands special dividends; CLF 2019) — the two vendors adjust these corporate actions differently; neither price is 'wrong'. The remaining miss is NKTR (sub-$1 price rounded to cents by Yahoo before a 1:15 reverse split → ~0.9% level error).
Across the entire 1995-2026 common history of all 60 sampled tickers there are 10 persistent Yahoo/CNBC ratio steps (>0.5%) in 7 tickers: yahoo_recorded_split(or spin-off encoded as split): 5; yahoo_recorded_large_dividend (Close drops, Adj Close adjusted): 4; no_yahoo_action (possible corporate action missing in Yahoo, or CNBC-only adjustment): 1.

**(iii) Large moves** (>50% daily) of still-trading tickers checked against CNBC: 199/209 confirmed as real price moves; not confirmed: 10 — see `d2_confirmed_errors.csv`. Unconfirmed cases are mostly spin-offs/special distributions where Yahoo's `Close` drops but `Adj Close` is correct (MO 2008 PMI, ROK 2001, SSP 2008, KDP 2018, WEN 2003), plus 100× unit breaks (SPXS.L 2014-01-02; MI 2026-05-18, a reused symbol) and JCI 2007-07-02 (Tyco reverse split + spin-offs; Yahoo Adj Close −53% that day is artificial).

**(iv) Yahoo values contradicted by ≥2 independent sources** (panels NOT modified; corrections listed in `d2_confirmed_errors.csv`, 30 rows incl. single-source cases):

| Symbol | Date | Yahoo | Reference | Source(s) | Error |
|---|---|---|---|---|---|
| ^GSPC | 2021-08-11 | 4442.41 | 4447.70 | CNBC .SPX = FRED SP500 | -0.12% |
| ^VIX | 2008-11-28 | 55.28 | 55.84 | CBOE VIX_History = FRED VIXCLS | -1.00% |
| ^VIX | 2014-08-29 | 12.09 | 11.98 | CBOE VIX_History = FRED VIXCLS | +0.92% |
| ^VIX | 2014-10-15 | 25.27 | 26.25 | CBOE VIX_History = FRED VIXCLS | -3.73% |
| ^VIX | 2014-12-01 | 14.16 | 14.29 | CBOE VIX_History = FRED VIXCLS | -0.91% |
| ^VIX | 2014-12-05 | 11.89 | 11.82 | CBOE VIX_History = FRED VIXCLS | +0.59% |
| ^VIX | 2014-12-09 | 15.35 | 14.89 | CBOE VIX_History = FRED VIXCLS | +3.09% |
| ^VIX | 2021-08-11 | 16.17 | 16.06 | CBOE VIX_History = FRED VIXCLS | +0.68% |
| ^VIX | 2026-02-06 | 20.37 | 17.76 | CBOE VIX_History = FRED VIXCLS | +14.70% |
| ^SP500TR | 2014-12-09 | 3758.87 | 3766.83 | CNBC .SPXTR; arbiter=^GSPC daily return (yahoo consistent=Fa | -0.21% |
| ^SP500TR | 2019-03-12 | 5556.77 | 5573.44 | CNBC .SPXTR; arbiter=^GSPC daily return (yahoo consistent=Fa | -0.30% |
| ^SP500TR | 2019-07-03 | 5982.90 | 6018.54 | CNBC .SPXTR; arbiter=^GSPC daily return (yahoo consistent=Fa | -0.59% |
| SPY | 2009-07-16 | 93.11 | 94.15 | CNBC SPY; arbiter=SPY/^GSPC ratio (yahoo consistent=False, c | -1.10% |

## 4. Benchmark integrity

| Pair | Window | CAGR a | CAGR b | Ann. difference | TE (monthly, ann.) | Daily corr |
|---|---|---|---|---|---|---|
| SPY AdjClose vs ^SP500TR | 2009-12-31→2026-09-25 | 14.25% | 14.36% | **-0.11%** | 0.28% | 0.9984 |
| IVV AdjClose vs ^SP500TR | 2009-12-31→2026-09-25 | 14.28% | 14.36% | **-0.09%** | 0.35% | 0.9984 |
| VOO AdjClose vs ^SP500TR (since inception) | 2010-09-09→2026-09-25 | 14.92% | 15.00% | **-0.07%** | 0.33% | 0.9986 |
| SPY Close (price) vs ^GSPC (price) | 2009-12-31→2026-09-25 | 12.26% | 12.28% | **-0.02%** | 0.83% | 0.9970 |
| ^SP500TR vs ^GSPC (dividend contribution) | 2009-12-31→2026-09-25 | 14.36% | 12.28% | **2.09%** | 0.19% | 0.9999 |
| RSP AdjClose (EW, TR) vs ^GSPC (CW, price) | 2009-12-31→2026-09-25 | 12.35% | 12.28% | **0.08%** | 5.07% | 0.9533 |
| RSP AdjClose (EW, TR) vs ^SP500TR (CW, TR) | 2009-12-31→2026-09-25 | 12.35% | 14.36% | **-2.01%** | 5.06% | 0.9532 |

SPY's −0.1%/yr tracking difference matches its 0.0945% expense ratio plus the UIT dividend cash drag — the Yahoo Adj Close methodology is sound for total-return work. RSP vs ^GSPC is not like-for-like (equal-weight total return vs cap-weight price index); vs ^SP500TR RSP lagged by ~2%/yr over 2010-2026 (mega-cap concentration).

Index series vs independent sources:

| Series | Reference | Days | within 0.01% | within 0.1% | max abs diff (date) |
|---|---|---|---|---|---|
| ^GSPC | CNBC .SPX | 7,985 | 99.80% | 99.99% | 0.12% (2021-08-11) |
| GSPC | FRED SP500 | 2,513 | 99.92% | 99.96% | 0.12% (2021-08-11) |
| ^SP500TR | CNBC .SPXTR | 7,973 | 99.92% | 99.96% | 0.59% (2019-07-03) |
| ^VIX | CNBC .VIX | 7,985 | 99.81% | 99.84% | 14.70% (2026-02-06) |
| VIX | CBOE VIX_History | 7,982 | 99.84% | 99.86% | 14.70% (2026-02-06) |
| SPY | CNBC SPY | 7,983 | 99.76% | 99.91% | 3.00% (2000-04-04) |
| ^TNX (CBOE) vs FRED DGS10 (Treasury CMT) | | 7,925 | median |diff| 1.0 bp | p95 3.3 bp | corr Δ 0.975 |
| ^IRX (CBOE 13w) vs FRED DTB3 (3m bill, discount basis) | | 7,925 | median |diff| 1.0 bp | p95 4.0 bp | corr Δ 0.809 |

UCITS listings (month-end basis vs ^SP500TR gross TR; London 16:30 vs New York 16:00 closes add timing noise):

| Listing | Currency | Window | Ann. difference vs ^SP500TR | TE (monthly, ann.) | Note |
|---|---|---|---|---|---|
| CSPX.L | None | 2010-10-31..2026-08-31 (month-ends) | -0.36% | 3.68% |  |
| IUSA.L | None | 2009-02-28..2026-08-31 (month-ends) | -1.81% | 9.85% |  |
| SPXS.L | None | 2010-06-30..2026-08-31 (month-ends) | -28.86% | 23.99% |  |
| SPY5.L | None | 2012-04-30..2026-08-31 (month-ends) | -0.45% | 3.39% |  |
| VUAA.L | None | 2019-06-30..2026-08-31 (month-ends) | -0.11% | 3.94% |  |

CSPX.L/VUAA.L/SPY5.L lag gross TR by roughly the expected TER + 15% US dividend withholding inside an Irish fund (≈0.25-0.35%/yr). IUSA.L is quoted in GBp (pence) and SPXS.L carries a 100× unit break on 2014-01-02 — use them only after FX/unit repair.

## 5. Data-quality checks (counts)

| Check | Result |
|---|---|
| (a) daily |return| > 50% (Close or Adj Close), rate series ^IRX/^TNX excluded | 481 events in 94 symbols; by category {'persistent_move': 320, 'spike_reversal': 148, 'distribution_close_only': 9, 'unit_100x_break': 3, 'split_related': 1}; 147 are in reuse-suspect symbols; 110 occur during a valid index membership ({'persistent_move': 78, 'spike_reversal': 27, 'distribution_close_only': 4, 'split_related': 1}) — almost all genuine (AAPL 2000-09-29, 2008-09 financials, PCG 2019, APA/OXY 2020-03-09, GL 2024-04-11). Flagged, not deleted (`d2_bad_ticks.csv`). |
| (b) stale runs ≥10 identical closes | 465 runs in 28 symbols; current constituents: 199 runs, **0 during S&P 500 membership** (all are in thin pre-US-listing histories of SW, FERG, AMCR, CRH etc.; flagged `thin_pre_history`); runs during any membership: 85 in CPWR, CSR, EP, GR, SII (reuse/OTC data). T-bill ETFs (BIL/SHV/SGOV) and ^IRX have genuine flat runs. |
| (c) last date = 2026-09-25 for current constituents | 503/503 pass |
| (d) non-positive prices | 9 rows, all in ['^IRX'] (negative T-bill yields, genuine); 0 equity/ETF rows |
| (e) Adj Close factor f=Adj/Close: f≤1 and non-decreasing; jumps match dividends | 0 tickers f>1; 0 decreasing; 1 of 51,183 factor jumps disagree with Yahoo's dividend by >5% |
| (f) same-day split + dividend (spin-off double count) | 25 events: {'small_dividend_with_split (plausible stock dividend + cash)': 12, 'ambiguous_flagged': 6, 'double_count_corrected': 5, 'plausible': 2}; corrected: ABT@2004-05-03 x1.0742, CNP@2002-10-01 x1.1110, DHR@2016-07-05 x1.5555, DLX@2001-01-02 x1.3350, ETN@2001-01-02 x1.1910; ambiguous (flagged only): DXC@2015-11-30, EXPE@2011-12-21, JCI@2007-07-02, RIG@2007-11-27, TMUS@2013-05-01, XRX@2017-01-03 |
| (g) OHLC consistency (Close outside High-Low) | 1866 rows, {'SPXS.L': 699, 'SPY5.L': 523, 'CSPX.L': 354, 'IUSA.L': 177, 'VUAA.L': 109, '^IRX': 2, 'AV': 1, 'NFX': 1} — overwhelmingly LSE UCITS lines |
| (h) bars on non-NYSE days | 2 rows ({'2026-05-25': 1, '2026-09-07': 1}) dropped from panels, listed in `d2_offcalendar_bars.csv` |
| (i) duplicate (ticker, date) rows in downloads | 0 |

**Yahoo corporate-action conventions** (important for users): `Close` is split-adjusted only, so spin-offs and special dividends appear as price drops in `Close`. Yahoo books a spin-off either as a non-round 'split' (NOV 2014: 1.109; FTI 2021: 1.344; DHR 2016: 1.319) or as a large cash 'dividend' (MO 2008, KDP 2018); either way `Adj Close` is usually right. The exception is when Yahoo does both on the same day (DHR 2016-07-05: split 1.319 **and** a $24.56 dividend → +61% Adj Close 'return'); these double counts are corrected in `d2_adjclose.parquet`/`d2_ret_monthly.parquet` (list in `d2_adj_corrections.csv`).

## 6. Identity, renames, and the live bar

- **Renames** (`d2_rename_candidates.csv`): an fja05680 row change with one removal and one addition not explained by the Wikipedia changes table (±10 days) is a rename candidate. The Wikipedia table is <35% complete before 2010 and ≥84% from 2011, so only swaps from 2011 are evaluated (earlier 1-1 swaps were mostly unlisted index replacements, e.g. ENRNQ→NVDA). Accepted 24 (successor's Yahoo series must cover ≥90% of the old member-days after its first bar, ≥250 days, <20% zero-volume): HRS->LHX@2019-06-01, TMK->GL@2019-08-08, BHGE->BKR@2019-10-18, CBS->PSKY@2019-12-05, JEC->J@2019-12-10, UTX->RTX@2020-04-03, CTL->LUMN@2020-09-18, MYL->VTRS@2020-11-17, LB->BBWI@2021-08-03, VIAC->PSKY@2022-02-17, BLL->BALL@2022-05-10, FB->META@2022-06-09, ANTM->ELV@2022-06-28, NLOK->GEN@2022-11-08, PKI->RVTY@2023-05-16, RE->EG@2023-07-10, ABC->COR@2023-08-30, PEAK->DOC@2024-03-04, FLT->CPAY@2024-03-25, PARA->PSKY@2025-08-08, FI->FISV@2025-11-11, MMC->MRSH@2026-01-14, BK->BNY@2026-05-21, EQR->VMRK@2026-08-18. Rejected merger-type swaps (e.g. WRK→SW: SW's pre-2024 history is thin OTC data) are listed with reasons.
- **Flags in `d2_coverage.csv`**: {'series_starts_after_membership': 76, 'series_starts_after_member_start': 26, 'thin_pre_history': 22, 'thin_during_membership': 5}. `series_starts_after_membership` = the Yahoo series begins after the symbol left the index (certainly another security); `name_mismatch_vs_wikipedia` = Yahoo longName shares no token with any Wikipedia name for that symbol; `thin_pre_history` = years with >20% zero-volume days (pre-listing OTC data).

## 7. Known limitations (read before using)

1. **Survivorship**: Yahoo purges delisted symbols; roughly half of 2000-04 member-days and a fifth of 2015-19 member-days have no price. Missing names are disproportionately acquired (positive takeover premia) and failed (large negative returns) companies, so the direction of the bias in any factor backtest is not knowable from this data alone. Delisting returns (CRSP-style) are unavailable.
2. **Ticker identity**: symbols are not permanent IDs. Reuse (WB, STI, MI, COMS, NE, CPWR, EP…) is flagged; reverse-merger histories (T/SBC, JPM/Chase, JCI/Tyco, WEN/Triarc, LHX/Harris-style) are not detectable from prices. Use D1 CIK mapping.
3. **Adjustments are as of 2026-09-25**, not point-in-time; spin-offs are handled inconsistently by Yahoo (see §5). Close-to-close returns from `d2_close` are NOT total returns.
4. **Pre-listing histories**: several current constituents (SW, FERG, AMCR, CRH…) carry thin OTC/ADR histories before their US primary listing; do not use them for beta/volatility estimation (see `thin_years`).
5. **Index errors**: a few single-day Yahoo errors in ^VIX, ^GSPC, ^SP500TR and SPY are confirmed by two sources (§3 iv); corrections are listed, panels are unmodified.
6. **UCITS**: IUSA.L quoted in GBp; SPXS.L has a 100× unit break (2014-01-02); LSE OHLC fields are often inconsistent. Use CSPX.L/VUAA.L for USD UCITS work.
7. **Membership spells** used for coverage statistics are D2's reconstruction from fja05680 + Wikipedia (a community file); D1 owns the authoritative membership.
8. **Second source** is CNBC (Stooq unreachable for automated clients); CNBC and Yahoo may share upstream vendors, so agreement is strong but not fully independent evidence. FRED/CBOE are independent for indices.

## 8. Files produced

| File | Rows × cols / rows | Content |
|---|---|---|
| `data/d2_adjclose.parquet` | 7,986 × 760 | Adj Close (total-return), NYSE days × symbols; double counts corrected |
| `data/d2_adjclose_yahoo_raw.parquet` | 7,986 × 760 | unmodified Yahoo Adj Close |
| `data/d2_close.parquet` | 7,986 × 760 | Close (split-adjusted only) |
| `data/d2_volume.parquet` | 7,986 × 760 | Volume |
| `data/d2_ret_monthly.parquet` | 380 × 765 | monthly total returns (month-end to month-end, no fill) |
| `data/d2_dividends.parquet` | 51,183 × 5 | dividends (+ fund capital gains), long |
| `data/d2_splits.parquet` | 1,154 × 3 | splits, long |
| `data/d2_ucits_adjclose.parquet` | 4,479 × 6 | UCITS Adj Close (LSE calendar) |
| `data/d2_ucits_close.parquet` | 4,479 × 6 | UCITS Close |
| `data/d2_ucits_volume.parquet` | 4,479 × 6 | UCITS Volume |
| `data/d2_coverage.csv` | 1,172 rows | per-symbol coverage, status, membership overlap, identity flags |
| `data/d2_universe.csv` | 1,172 rows | download universe with provenance |
| `data/d2_universe_spells.csv` | 1,145 rows | D2 membership spells (coverage helper) |
| `data/d2_members_with_price_daily.csv` | 6,723 rows | members vs members-with-price per day |
| `data/d2_rename_candidates.csv` | 298 rows | heuristic ticker renames |
| `data/d2_bad_ticks.csv` | 481 rows | flagged >50% daily moves |
| `data/d2_bad_ticks_crosscheck.csv` | 242 rows | CNBC check of large moves |
| `data/d2_stale_runs.csv` | 465 rows | runs of ≥10 identical closes |
| `data/d2_adj_corrections.csv` | 25 rows | same-day split+dividend events and corrections |
| `data/d2_adj_corrections_cnbc.csv` | missing | CNBC evidence for those events |
| `data/d2_confirmed_errors.csv` | 30 rows | Yahoo values contradicted by other sources |
| `data/d2_offcalendar_bars.csv` | 2 rows | bars on non-NYSE days (excluded) |
| `data/d2_final_partial_month.csv` | 17 rows | partial last-month return for series ending mid-month |
| `data/d2_validation_sample.csv` | 1,500 rows | 60×25 CNBC comparison |
| `data/d2_validation_sample_fullseries.csv` | 60 rows | full-history agreement per sampled ticker |
| `data/d2_validation_outliers.csv` | 6 rows | diagnosis of sample outliers |
| `data/d2_validation_ratio_steps.csv` | 10 rows | Yahoo/CNBC adjustment-step events |
| `data/d2_validation_latest_close.csv` | missing | 2026-09-25 close vs CNBC, all current constituents |
| `outputs/d2_qc_summary.json` | json | all QC numbers |
| `outputs/d2_validation_results.json` | json | all validation numbers |
| `outputs/d2_universe_summary.json` | json | universe build summary |

Scripts: `v4/code/d2_common.py`, `d2_universe.py`, `d2_download.py` (phases batch/retry/meta/refresh), `d2_build.py`, `d2_validate.py` (parts sample/latest/bench/badticks/errors), `d2_report.py`. Every dataset has a `.meta.json` sidecar. Raw caches: `C:\Users\user\eqv4\cache\d2\` (batches, singles, refresh, meta, validation, raw).

## 9. Sources

- Yahoo Finance chart API via yfinance 1.7 — prices, dividends, splits, metadata.
- Wikipedia: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies ; https://en.wikipedia.org/wiki/Historical_components_of_the_S%26P_500
- GitHub fja05680/sp500: https://raw.githubusercontent.com/fja05680/sp500/master/S%26P%20500%20Historical%20Components%20%26%20Changes%20%28Updated%29.csv
- CNBC: https://ts-api.cnbc.com/harmony/app/bars/ (daily bars), https://quote.cnbc.com/quote-html-webservice/restQuote/ (quotes)
- FRED: https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500 | VIXCLS | DGS10 | DTB3 ; CBOE: https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv
- Stooq (attempted, blocked): https://stooq.com/q/d/l/?s={sym}&i=d
