# D3 — SEC XBRL point-in-time (as-filed) fundamentals — report

Agent D3 · built 2026-09-26 (data cutoff: US close 2026-09-25) · code `v4/code/d3_*.py`

## 1. Answer first

- **Status: done.** The as-filed, point-in-time (PIT) monthly fundamentals panel is built:
  **`v4/data/d3_pit_monthly.parquet` has 114,701 rows × 75 columns: 659 CIKs × 208 month-ends, from 2009-06-30 to 2026-09-25.**
  A stricter version with a one-trading-day lag is in `d3_pit_monthly_lag1.parquet`: it only uses facts with `filed < t`, which is the backtest rule in CONVENTIONS.
  The quarterly diluted-EPS table for SUE is `d3_eps_quarterly_pit.parquet` (1,353,303 rows).
  Every value is taken from SEC XBRL `companyfacts`, as filed. A restatement only enters the panel on the date it was filed.
- **Checks against the old Yahoo statements (named 25 companies, fiscal years 2021–2025).**
  - Net income: 100 of 100 company-years match within 1%.
  - Revenue: 90 of 100 match within 1%, and 100 of 100 within 5%.
  - All 10 revenue misses come from how the total is defined, not from errors. For CVX and XOM, the XBRL `Revenues` tag is "total revenues *and other income*". For JPM, XBRL gives total net revenue as JPM reported it.
  - Wider check on every legacy ticker (497 tickers, about 1,990 company-years): revenue matches within 1% for 93.5% and within 5% for 97.6%. Net income matches within 1% for 98.1%.
- **No look-ahead.**
  - No row uses a fact filed after its month-end (0 of 114,701 rows).
  - In a truncation test and a perturbation test, 0 of 6,800 feature comparisons changed (200 random company-dates).
  - Restatement check: Apple's FY2009 revenue was **$36.537B** in the original 10-K (filed 2009-10-27). The panel uses that figure at month-ends Oct–Dec 2009. The 10-K/A filed 2010-01-25 restated it to **$42.905B**, and the panel switches from 2010-01-29. Test passes.
- **Coverage** of constituents that could be mapped to a CIK (fja05680 membership):
  - `rev_ttm` is 66% in 2010, 91% in 2011, and at least 96.7% every year from 2012. `ni_ttm`, `assets` and `ocf_ttm` are at least 98.8% from 2012.
  - Enough EPS history for SUE: 90% in 2012, then 93–96%.
  - Measured over *all* constituents, including tickers I could not map, coverage is 67% (2012), 84% (2019) and 99% (2026). The gap is a mapping problem, not a data problem. Recently delisted or renamed tickers (AVB, EQR, EA, BK, MMC, K, IPG, WBA, HES, …) are missing from the SEC's current ticker file.
- **D1's full historical CIK map `v4/data/d1_cik_map.csv` was not present when I finished.** Only `d1_current_constituents.csv` existed. The resume command is ready and has been tested end to end:
  `PYTHONPATH='C:\Users\user\eqv4\pylib' python v4/code/d3_pull.py --ciks-from v4/data/d1_cik_map.csv`
  It keeps only rows with confidence high or medium. It then downloads, extracts and builds **only the missing CIKs** and re-assembles all outputs, in about 1 minute plus downloads. After that, run `python v4/code/d3_validate.py` to refresh coverage.

## 2. Files produced

| File | Rows | Content |
|---|---|---|
| `v4/data/d3_xbrl_facts.parquet` | 3,559,336 | Long table of the selected concepts for 659 CIKs. Columns: cik, ticker, taxonomy, concept, unit, val, start, end, fy, fp, form, filed, frame, accn, plus `requested` (False = extra fallback concept added by D3). |
| `v4/data/d3_pit_monthly.parquet` | 114,701 | PIT features at month-end t, using facts with `filed <= t`. This is the task specification. |
| `v4/data/d3_pit_monthly_lag1.parquet` | 114,665 | The same features using facts with `filed < t` (filing date plus 1 trading day). **Use this one for backtests.** |
| `v4/data/d3_eps_quarterly_pit.parquet` | 1,353,303 | For each month_end and CIK: q=0..12 split-adjusted diluted EPS, with period_end, filed date, and a `derived` flag. |
| `v4/data/d3_universe.csv` | 629 | CIK universe: 500 current constituents (Wikipedia CIK column) and 129 historical fja tickers still in the SEC current ticker file. |
| `v4/data/d3_ticker_cik_map.csv` | 869+ | fja/Wikipedia ticker → CIK, with method (`wikipedia_current_cik`, `sec_company_tickers_current` or `unmapped`) and membership dates. |
| `v4/data/d3_lineage.csv` | 33 | Predecessor CIKs found with the SEC frames API. See §3.4. |
| `v4/data/d3_universe_extra_d1.csv` | 2 | CIKs added through `--ciks-from`. So far this is the test run: CELG 816284 and TWX 1105705, labelled `d3_manual_test_historical`. |
| `v4/data/d3_company_meta.csv` | 659 | SEC submissions metadata: name, SIC, fiscal year end, filer category, former names. |
| `v4/outputs/d3_validation.json` | — | All validation results. |
| `v4/outputs/d3_validation_fy_compare.csv` | 3,968 | Company-year comparison of XBRL and Yahoo revenue and net income. |
| `v4/outputs/d3_coverage_monthly.csv` | 208 | Coverage for each month. |

Every dataset has a `.meta.json` sidecar. Raw JSON is cached gzipped in `C:\Users\user\eqv4\cache\d3\` (not in OneDrive): `companyfacts/` and `submissions/` (about 175 MB), `frames/`, and per-CIK shards. Scripts:
- `d3_common.py`
- `d3_universe.py`
- `d3_pull.py` (downloader and resume entry point)
- `d3_extract.py`
- `d3_lineage.py`
- `d3_pit_core.py` (PIT engine)
- `d3_build_pit.py`
- `d3_validate.py`

## 3. Method

### 3.1 Sources and etiquette

- Current constituents come from Wikipedia "List of S&P 500 companies", table 1, which has a CIK column (https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
- Historical membership comes from fja05680/sp500 `S&P 500 Historical Components & Changes (Updated).csv`, whose last snapshot is 2026-08-18. I used every ticker that appears on or after the snapshot in force on 2009-01-01: 869 tickers. They were mapped with https://www.sec.gov/files/company_tickers.json, which lists current tickers only. 631 mapped and 238 did not.
- For each CIK I downloaded XBRL `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` and `https://data.sec.gov/submissions/CIK##########.json`. Requests used the CONVENTIONS User-Agent, at most 3.3 requests per second shared across 3 threads, with backoff on 429, 5xx and 403. All 1,258 initial requests succeeded.
- Predecessor links come from `https://data.sec.gov/api/xbrl/frames/us-gaap/{concept}/USD/{frame}.json`.

### 3.2 Point-in-time engine (`d3_pit_core.py`)

- **Versions.** The state at date E holds, for every (concept, period), the value from the **latest filing with `filed <= E`**. Ties on the same day go to the later accession number. The state is recomputed at every filing date. Month-end t takes the state at the last filing date ≤ t (main panel) or < t (lag-1 panel).
- **Filings used.** Only periodic reports: 10-K, 10-Q, their /A amendments, 10-KT, 10-QT, and the annual 20-F/40-F of US-GAAP filers. Facts from 8-K, S-1, proxies and 6-K are kept in the facts table but not used.
- **Periods.** Duration is measured as end − start in days: 84–98 days is a quarter and 350–380 days is a year, which handles 52/53-week fiscal years. Quarterly flows come from direct 3-month facts. Otherwise they are **derived from same-start year-to-date facts**: Q2 = 6M − 3M, Q3 = 9M − 6M, Q4 = FY − 9M. The derivation runs twice, so Q4 = (FY − 6M) − Q3 also works. This matters because most 10-Q cash-flow statements are year-to-date only.
- **TTM** is the sum of the latest 4 **consecutive** quarters. Each quarter must start 1–5 days after the previous one ends, and the whole window must span 350–380 days. The latest annual value is used instead when it ends at least as late (`rev_ttm_src` = `4q` or `annual`).
- **Instant items** are read at the latest balance-sheet date known at t (`bs_date`, the latest `Assets` date). Values for goodwill and intangibles may be up to 190 days older than that date. Sum components must share the same date: cash plus short-term investments, and the debt pieces. `*_1y_ago` is the same concept at bs_date − 365 ± 15 days, as known at t.
- **Stock splits.**
  - Splits are detected from restated comparatives: the same period's weighted shares reported ×r, or its EPS ÷r, in a later filing, where r is a simple split ratio.
  - A split counts only after one confirmation from shares or two from EPS. Only confirmations filed ≤ t count (PIT).
  - Older-vintage EPS is divided by r and share counts are multiplied by r, but only once the split has been revealed at t.
  - Splits were detected in 179 CIKs. Of 166 simple-ratio Yahoo splits (D2, 2010–2026, current tickers), 154 (93%) coincide with an XBRL-detected split in the same company.
- **SUE** = (EPS_q0 − EPS_q4) / std(EPS_q(i) − EPS_q(i+4), i = 1..8, ddof=1), using split-adjusted diluted EPS. It needs at least 6 differences and a standard deviation above 0. Eight prior year-on-year differences need **13 quarters (q0..q12)**, not 12. They are stored both wide (`eps_q0..eps_q12`) and long. Quarters are aligned by date: q_i ends about i × 91 days before q0, ±20 days. Q4 EPS is derived as FY − 9M when no 3-month fact exists (11% of EPS rows are derived).

### 3.3 Concept fallback rules (explicit order)

For flow items the rule is applied **per fiscal period**, and TTM is computed from the merged series.

| Feature | Rule |
|---|---|
| `rev_ttm` | **Priority:** RevenuesNetOfInterestExpense > Revenues > RegulatedAndUnregulatedOperatingRevenue > RevenueFromContractWithCustomerExcludingAssessedTax > …IncludingAssessedTax > SalesRevenueNet > industry totals used before 2018 (HealthCareOrganizationRevenue, OilAndGasRevenue, RefiningAndMarketingRevenue, FoodAndBeverageRevenue, RealEstateRevenueNet, ElectricUtilityRevenue). ASC-606 revenue plus RevenueNotFromContractWithCustomer is used when `Revenues` is absent. SalesRevenueGoodsNet + SalesRevenueServicesNet is the last resort.<br>**Consistency check:** if several candidates exist, the one within 1.5% of GrossProfit + cost of revenue (or OperatingIncomeLoss + CostsAndExpenses) wins. This fixes GIS, NTAP and BLK, where `Revenues` tags only part of revenue.<br>**Banks:** InterestIncomeExpenseNet + NoninterestIncome, if no total exists or the chosen value is less than 50% of it.<br>**REITs:** add OperatingLeaseLeaseIncome when the only revenue tag is a small ASC-606 figure. |
| `gp_ttm` | GrossProfit, else revenue − (CostOfRevenue > CostOfGoodsAndServicesSold > CostOfGoodsSold). NaN for banks and insurers. |
| `opinc_ttm` / `ebit_ttm` | OperatingIncomeLoss. `ebit_ttm` falls back to pretax + interest (`ebit_src`). |
| `ni_ttm` | NetIncomeLoss > NetIncomeLossAvailableToCommonStockholdersBasic > ProfitLoss |
| `ocf_ttm` | NetCashProvidedByUsedInOperatingActivities > …ContinuingOperations |
| `capex_ttm` | PaymentsToAcquirePropertyPlantAndEquipment > PaymentsToAcquireProductiveAssets (reported as a positive outflow) |
| `da_ttm` | DepreciationDepletionAndAmortization > DepreciationAndAmortization > DepreciationAmortizationAndAccretionNet |
| `sbc_ttm` | ShareBasedCompensation > AllocatedShareBasedCompensationExpense |
| `div_ttm` | PaymentsOfDividendsCommonStock > PaymentsOfDividends |
| `buyback_ttm` / `issuance_ttm` | PaymentsForRepurchaseOfCommonStock > PaymentsForRepurchaseOfEquity; ProceedsFromIssuanceOfCommonStock |
| `interest_ttm` | InterestExpense > InterestExpenseNonoperating > InterestExpenseDebt |
| `tax_ttm` / `pretax_ttm` | IncomeTaxExpenseBenefit; IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest > …MinorityInterestAndIncomeLossFromEquityMethodInvestments |
| `rd_ttm`, `sga_ttm`, `cogs_ttm` | Extras: R&D, SG&A, cost of revenue |
| `assets`, `equity` | Assets; StockholdersEquity > StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest (plus `_1y_ago`) |
| `liabilities` | Liabilities > LiabilitiesAndStockholdersEquity − equity including NCI > L&SE − equity − MinorityInterest (`liabilities_src`) |
| `cash_sti` | Cash (CashAndCashEquivalentsAtCarryingValue > …IncludingRestricted > CashAndDueFromBanks) + one short-term investment tag (ShortTermInvestments > MarketableSecuritiesCurrent > AvailableForSaleSecuritiesDebtSecuritiesCurrent) at the same date, 0 if absent |
| `total_debt` | Long-term debt [LongTermDebt (includes current portion) > LongTermDebtNoncurrent + LongTermDebtCurrent > LongTermDebtAndCapitalLeaseObligations (+Current)] + max(ShortTermBorrowings, CommercialPaper), max so the two are not double counted. Else DebtCurrent. Else short-term only. NaN when no debt tag exists at bs_date (96 of 628 rows in the last month, mostly debt-free or bank filers). `debt_src` records the choice. |
| `shares_out` | `dei:EntityCommonStockSharesOutstanding` if its cover date ≥ bs_date − 45 days and it is within 0.5–2× the NI/EPS-implied share count (`shares_ref_ni_eps`). Else CommonStockSharesOutstanding (plausible, ≤190 days old). Else the latest-quarter diluted weighted average. Split-adjusted. `shares_src` and `shares_out_date` record the choice. `shares_1y_ago` uses the same source about 1 year earlier; it is dropped if the 1-year ratio falls outside 0.25–4× (a scale error). |
| Flags | `is_financial` (SIC 6000–6499, or no current assets plus bank/insurer tags), `no_current_assets`, `n_concepts_present`, `last_filed_date`, `last_form`, `last_period_end`, `staleness_days` = t − last_period_end, `max_filed_used`, `lineage_ciks`, `n_splits_known` |

### 3.4 Company lineage (new CIKs after holding-company reorganisations)

Several current constituents re-registered under a **new CIK**. Their XBRL history under the new CIK is short:
- XOM: ExxonMobil Holdings, first filing 2026-08-03
- BLK: new holding company, 2024
- GOOGL: Alphabet, 2015
- DIS, CI, MDT, ETN, APA, AVGO, LIN, ICE, BG, …

`d3_lineage.py` finds the predecessor automatically. The successor's first filings contain comparative figures (prior-year net income, prior year-end assets and equity). The frames API shows which other CIK reported the **identical** values: at least 2 matches across at least 2 concepts, with float tolerance only.

It found 33 links. Examples:
- XOM ← Exxon Mobil Corp (34088)
- GOOGL ← Google Inc.
- BLK ← old BlackRock (1364742)
- DIS ← TWDC
- MDT ← Medtronic Inc
- ETN ← Eaton Corp
- AVGO ← Broadcom Ltd ← Avago
- DD and DOW ← Dow Chemical
- DXC ← CSC
- PSKY ← Paramount Global

Only the primary predecessor is chained. Parallel co-filers (Broadcom Cayman L.P.) are ignored.

The engine adds the predecessor's facts filed before the successor's first periodic filing to the successor's state. As a result, XOM's September 2026 TTM uses Exxon's FY2025 10-K. Successor rows start at the successor's own first filing. Predecessor rows carry the successor's ticker and stop when the successor starts filing, so the panel has **no duplicate (month_end, ticker)**.

## 4. Validation (see `d3_validation.json`)

| Check | Result |
|---|---|
| (a) Named 25 (AAPL … V), fiscal years in `fund_all.pkl`, revenue within 1% | **90/100 pass** (5% tolerance: 100/100). Misses: CVX FY22–25 (+2.0 to +4.8%) and XOM FY22–25 (+2.6 to +3.8%), where XBRL `Revenues` includes equity-affiliate and other income while Yahoo uses sales and other operating revenue. JPM FY23 and FY24 (+2.0%, +4.8%), where XBRL is total net revenue as reported ($158.1B for 2023, per JPM's 10-K) and Yahoo uses a different bank revenue definition. |
| (a) Named 25, net income within 1% | **100/100 pass** |
| (a) Broad: all 497 legacy tickers | Revenue 1,859/1,988 = **93.5%** within 1% (97.6% within 5%). Net income 1,942/1,980 = **98.1%** within 1%. Remaining revenue differences are mostly definitional: insurers 1–3%, asset managers, excise taxes (MO), utilities' derivative revenue, banks. |
| (b) Coverage by month | Table below and `d3_coverage_monthly.csv` |
| (c) Restatement spot-check (AAPL FY2009, 10-K → 10-K/A) | **Pass.** $36.537B at 2009-10-30, 11-30 and 12-31; $42.905B from 2010-01-29. A scan found 758 annual Revenues/NetIncomeLoss periods restated by more than 2% after first filing, across 278 companies. That is why the as-filed approach matters. |
| (d) No fact filed after t | **Pass.** Every row has `max_filed_used <= month_end` (0 violations; the lag-1 file has `< month_end`). The build asserts this. Truncation test (recompute from facts filed ≤ t only) plus perturbation test (facts filed after t ×1000 + 7): **0 mismatches in 6,800** comparisons over 17 features and 200 random company-dates. |
| (e) Split detection vs D2 Yahoo splits | 154/166 (93%) simple-ratio splits since 2010 confirmed in the same company. |
| (e) Month-over-month jumps | 30 `rev_ttm` changes above 10× and 77 `shares_out` changes above 3×, out of about 114k rows. These are mostly real events (IPOs and spin-offs moving from partial to full TTM, reverse splits) or early-XBRL scale errors. **B1 should winsorise ratios.** |

**Coverage by year** (mean over months; % of that month's S&P 500 constituents).
- "all" = share of all constituents.
- "mapped" = share of constituents resolved to a CIK through the ticker map and lineage, with a date-validity check against ticker re-use.

| Year | Constituents | Mapped | rev_ttm (all) | ni_ttm (all) | assets (all) | equity (all) | ocf_ttm (all) | EPS ≥8q (all) | SUE (all) | rev_ttm (mapped) | SUE (mapped) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2009 | 499 | 316 | 0.8 | 1.8 | 35.6 | 35.3 | 0.9 | 0.0 | 0.0 | 1.2 | 0.0 |
| 2010 | 498 | 326 | 43.4 | 44.8 | 57.0 | 56.6 | 44.9 | 30.6 | 0.4 | 66.2 | 0.6 |
| 2011 | 497 | 334 | 61.3 | 63.1 | 66.0 | 65.8 | 63.1 | 57.9 | 42.6 | 91.2 | 63.2 |
| 2012 | 497 | 344 | 66.9 | 68.4 | 68.8 | 68.6 | 68.4 | 65.2 | 62.0 | 96.7 | 89.6 |
| 2013 | 497 | 353 | 69.3 | 70.4 | 70.8 | 70.6 | 70.2 | 67.8 | 66.2 | 97.5 | 93.1 |
| 2014 | 498 | 360 | 71.2 | 71.8 | 72.1 | 71.8 | 71.7 | 69.2 | 68.2 | 98.6 | 94.4 |
| 2015 | 501 | 373 | 73.3 | 73.7 | 73.9 | 73.9 | 73.7 | 71.6 | 70.7 | 98.5 | 95.0 |
| 2016 | 505 | 393 | 76.4 | 76.8 | 76.9 | 76.9 | 76.6 | 74.8 | 73.8 | 98.3 | 94.9 |
| 2017 | 506 | 408 | 79.4 | 80.0 | 80.1 | 80.0 | 79.8 | 77.8 | 76.8 | 98.4 | 95.3 |
| 2018 | 505 | 416 | 81.1 | 81.7 | 81.8 | 81.8 | 81.5 | 79.7 | 78.3 | 98.6 | 95.2 |
| 2019 | 505 | 427 | 84.1 | 84.2 | 84.5 | 84.5 | 84.0 | 82.3 | 81.1 | 99.4 | 95.8 |
| 2020 | 505 | 442 | 87.1 | 87.1 | 87.4 | 87.4 | 87.1 | 85.0 | 83.9 | 99.6 | 95.9 |
| 2021 | 505 | 451 | 89.2 | 89.2 | 89.3 | 89.3 | 89.2 | 86.9 | 86.0 | 99.8 | 96.2 |
| 2022 | 504 | 464 | 91.8 | 91.9 | 92.1 | 92.1 | 91.9 | 89.4 | 88.6 | 99.6 | 96.1 |
| 2023 | 503 | 476 | 94.1 | 94.3 | 94.6 | 94.6 | 94.3 | 92.0 | 90.8 | 99.4 | 95.9 |
| 2024 | 503 | 484 | 95.6 | 95.6 | 96.1 | 96.1 | 95.6 | 92.8 | 91.9 | 99.4 | 95.6 |
| 2025 | 503 | 490 | 97.3 | 97.3 | 97.4 | 97.4 | 97.3 | 94.3 | 92.9 | 99.9 | 95.3 |
| 2026 | 503 | 499 | 99.1 | 99.1 | 99.1 | 99.1 | 99.1 | 96.1 | 94.5 | 99.8 | 95.3 |

For mapped constituents, `ni_ttm`, `assets`, `equity` and `ocf_ttm` all exceed 98.6% every year from 2012. Unmapped tickers with the most months are AVB, EQR, EA, BK, MMC, K, IPG, WBA, HES, JNPR, DFS, MRO, CMA, PXD, SEE, ABC, PKI, CTXS, ANTM, BLL, … These are renamed, acquired or delisted companies, and D1's map will resolve them. Some are data that already exists in the panel under the new ticker: EQR → VMRK (same CIK 906107), ANTM → ELV, ABC → COR, BLL → BALL, PKI → RVTY.

## 5. Limitations / open issues

1. **XBRL phase-in.** Large accelerated filers start with periods after June 2009, and everyone else by mid-2011. The first TTM from XBRL alone appears around early 2010 for large filers. Backtests that need about 95% coverage should start in **2012** (SUE needs 13 quarters of history).
2. **Survivorship and mapping.** Historical members are included only if their ticker still exists in the SEC current ticker file, or through lineage. 238 of 869 fja tickers since 2009 are unmapped. Ticker re-use (APC→ARKO, BBT→Beacon, EP, EQ, DYN, Q, SNDK, CEG, …) is caught by a date-validity check in coverage, but those CIKs are still in the panel as other companies. **Join by (ticker, date) only through D1's date-aware map**, then run the `--ciks-from` resume.
3. **IFRS filers** (20-F with ifrs-full) are not covered. US-GAAP 20-F/40-F annual facts are used, annual only.
4. **Financials.** Banks and insurers have no gross profit or current assets (`is_financial` = 91 of 628 in the last month). Their revenue definitions differ from data vendors (JPM, MS, SYF, insurers). Operating cash flow for banks is volatile (JPM TTM −$162.5B at 2026-09), so bank OCF, FCF and accrual ratios are not comparable.
5. **Revenue definitions.** Integrated oils include other income (+2–5% vs Yahoo). MO and PM are gross of excise taxes. Utilities that use ASC-606 revenue only may be 1–3% low.
6. **Multi-class shares.**
   - GOOGL, META, FOX, NWS, BRK: companyfacts has no dei cover count, so CommonStockSharesOutstanding or diluted weighted shares are used instead.
   - **BRK reports Class-A-equivalent shares and EPS.** Multiply by 1,500 for B-share equivalents, or price it with BRK-A.
   - For market cap between the share-count date and t, apply splits after `shares_out_date` (D2 split table).
7. **Derived quarters** (Q4 = FY − 9M) can mix vintages when a 10-K restates the year but the 9-month figure has not yet been re-reported. Q4 EPS is approximate (EPS is not strictly additive).
8. **Early-XBRL scale errors** (for example shares tagged in thousands) are only partly neutralised by the plausibility rules. Winsorise.
9. **8-K recasts are excluded.** A restatement enters only through 10-K, 10-Q or their amendments, on the day it is filed. Filed date is the EDGAR filing date; after-hours acceptances carry the next business day. **Use `d3_pit_monthly_lag1` for backtests.**
10. **Lineage accounting predecessors.** DD's pre-2017 state uses Dow Chemical (its accounting predecessor), which is correct for DowDuPont's own filings. Ticker DD in 2009–2017 was E.I. du Pont (CIK 30554), which is not in my universe. D1's map should point there.
11. **Recent new CIKs without a filer predecessor** (for example the HONA spin-off, first filings pending) have no data yet.

## 6. How to re-run / extend

```
# from PROJECT, Git Bash
export PYTHONPATH='C:\Users\user\eqv4\pylib'
python v4/code/d3_universe.py            # sources -> universe + membership (cached; --refresh to re-download)
python v4/code/d3_pull.py                # download companyfacts+submissions (resumable), extract, build
python v4/code/d3_lineage.py             # predecessor discovery (frames API, cached)
python v4/code/d3_extract.py && python v4/code/d3_build_pit.py --rebuild
python v4/code/d3_validate.py
python v4/code/d3_pull.py --ciks-from v4/data/d1_cik_map.csv   # when D1's map exists (only missing CIKs)
```
