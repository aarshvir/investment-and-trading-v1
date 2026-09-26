# Independent market-data validation

**Verdict:** The headline earnings claims for all 14 final holdings are substantially supported by dated company or SEC sources available before the 24 September 2026 close. The data cannot be dismissed as fabricated merely because figures differ from older remembered results. However, valuation-period ambiguity, mixed accounting definitions, unreconciled vendor fields and missing event adjustments prevent treating the original portfolio as investment-ready.

Scope: source bundle read-only; examined `info.json`, `dash2.json`, `universe.csv`, `close.pkl`, `close10.pkl`, `deep.pkl`, `est_all.pkl`, `edgar.pkl`, and relevant extraction/selection scripts. Web checks were conducted on 25–26 September 2026; **information cutoff remains 24 September 2026**, even when a webpage now displays later stock quotes. This is a targeted 14-holding data audit, not full re-audit of every line in all 467 releases or all 497 companies.

## 1. What the date checks establish

- All 14 saved `regularMarketTime` fields resolve to 24 September 2026 at approximately 20:00 UTC, the US regular-session close.
- Saved `close.pkl` runs from 25 September 2023 to 24 September 2026; `close10.pkl` runs from 25 September 2015 to 24 September 2026.
- The 14 last closes match `info.currentPrice` to less than $0.000015. This is **internal consistency within a common vendor family**, not independent exchange-price certification.
- Each holding has nine cached EDGAR documents; the latest filing dates match the table below. Retrieval does not prove substantive reading of nine complete reports or transcripts.
- `s1_info.py` resumes cached records whenever they already contain `marketCap`; it does not enforce one retrieval time. `edgar.py` similarly skips already-cached tickers. Neither preserves a proper per-field retrieval/publication/period/as-of ledger. This is a reproducibility weakness even though the sampled quote timestamps match.
- NVIDIA statements in the vendor tables use month-end column labels, e.g. 31 July 2026, whereas its actual quarter ended 26 July. Fiscal dates should come from filings, not vendor-normalized labels.
- `info.NVDA.prevName` says “Usual Stablecoin” with `nameChangeDate=2026-09-24`. This is a conspicuous metadata anomaly requiring quarantine; it does **not** establish that the separately corroborated earnings or prices are wrong.

## 2. Primary-source checks for every holding

“Verified” below applies only to the stated reported figure and period. It does not certify forward estimates, intrinsic value, recommendation, portfolio return, or loss probability.

| Ticker | Reporting period / release date | Corroborated facts | Status and decision-relevant qualification |
|---|---|---|---|
| NVDA | Q2 FY2027 ended 26 Jul 2026 / 26 Aug | Revenue $96.221bn, +106%; gross margin 75%; GAAP EPS $2.46, non-GAAP $2.22 | **Verified.** Company changed its non-GAAP treatment of stock compensation from Q1 FY2027; compare estimates and prior periods on consistent basis. [Company release](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/) |
| CPAY | Q2 ended 30 Jun 2026 / 5 Aug | Revenue $1.3388bn, +21%; organic growth 10%; adjusted EPS growth 36% | **Verified.** GAAP net income declined 13%, so adjusted growth cannot substitute for earnings-quality reconciliation. [SEC exhibit](https://www.sec.gov/Archives/edgar/data/1175454/000117545426000045/ex991q2_2026.htm) |
| AMP | Q2 ended 30 Jun 2026 / 23 Jul | Adjusted operating EPS $11.07, +22%; adjusted operating ROE excluding AOCI 55% | **Verified with definition.** 55% is explicitly adjusted and excludes AOCI, not a directly comparable generic GAAP ROE. [SEC exhibit](https://www.sec.gov/Archives/edgar/data/820027/000082002726000038/q22026er.htm) |
| RL | Q1 FY2027 ended 27 Jun 2026 / 6 Aug | Reported revenue +14%, constant-currency +13%; outlook updated | **Verified.** “Raised or updated” is not equivalent to nine guidance increases: every claimed raise requires comparison with the prior range. [Company release](https://investor.ralphlauren.com/static-files/5aefed21-3753-4099-9db7-7d24334251e9) |
| AME | Q2 ended 30 Jun 2026 / 4 Aug | Sales $2.04bn, +15%; adjusted EPS $2.09, +17%; GAAP EPS $1.77 | **Verified.** Material acquisition completed after this balance-sheet date; see event adjustment below. [SEC exhibit](https://www.sec.gov/Archives/edgar/data/1037868/000103786826000173/ametek8kexhibit99108042026.htm) |
| SNA | Q2 ended 4 Jul 2026 / 23 Jul | Net sales $1.2351bn, +4.7%, organic +3%; gross margin 51.4%; diluted EPS $4.96 versus $4.72 | **Verified.** Total revenue including financing was $1.3348bn, +4.2%; this explains approximate +4% vendor growth versus +4.7% product sales. “No formal guidance” should mean no revenue/EPS forecast: capex and tax-rate guidance exists. [SEC exhibit](https://www.sec.gov/Archives/edgar/data/91440/000009144026000141/q22026pressreleaseforpress.htm) |
| ABNB | Q2 ended 30 Jun 2026 / 6 Aug | Revenue approximately $3.6bn, +17%; net income $816m; nights/seats growth +10% | **Verified.** Newsroom $1.3bn and 35% margin refer to adjusted EBITDA; independently reconcile any FCF claim to the shareholder-letter cash-flow reconciliation before using it in valuation. [Company release](https://news.airbnb.com/airbnb-q2-2026-financial-results) |
| NTAP | Q1 FY2027 ended 31 Jul 2026 / 2 Sep | Revenue $2.025bn, +30%; all-flash array revenue +47%; GAAP EPS $1.88, adjusted $2.58; guidance raised | **Verified.** Operating cash flow fell 25%, FCF fell 35% to $401m. Revenue acceleration alone is incomplete evidence. [Company release](https://investors.netapp.com/news/news-details/2026/NetApp-Reports-First-Quarter-of-Fiscal-Year-2027-Results/default.aspx) |
| PAYX | Q1 FY2027 ended 31 Aug 2026 / 23 Sep | Revenue $1.6305bn, +6%; diluted EPS $1.21, +14%; adjusted EPS $1.34 | **Verified and current before cutoff.** Release occurred just one day before quote cutoff; any older earnings estimate snapshot must be checked for post-release updates. [SEC exhibit](https://www.sec.gov/Archives/edgar/data/723531/000072353126000004/payx-ex99_1.htm) |
| MSFT | Q4 FY2026 ended 30 Jun 2026 / 29 Jul | Quarterly revenue $90.007bn, +18%; annual revenue $331.839bn; operating income +18%; net income +31% GAAP / +22% adjusted | **Verified.** $90bn is quarterly revenue, not a forecast. Adjusted EPS still includes other discrete benefits; normalize separately. [Company release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast) |
| IBKR | Q2 ended 30 Jun 2026 / 21 Jul | GAAP and adjusted EPS $0.69; GAAP net revenue $1.896bn, adjusted $1.875bn | **Verified.** Net revenue grew about 28.1% ($1.896bn / $1.480bn − 1), whereas saved `info.revenueGrowth` is 26%; period/definition reconciliation remains open. [SEC exhibit](https://www.sec.gov/Archives/edgar/data/1381197/000138119726000118/ibkr-ex99_1.htm) |
| HIG | Q2 ended 30 Jun 2026 / 23 Jul | Net income to common approximately $1.3bn, +31%; core earnings $945m, +1%; core EPS $3.42 | **Verified.** $251m tax benefit connected to Hartford Funds sale contributes to GAAP growth. Underlying Business Insurance combined ratio worsened from 88.0 to 89.3. [Company release](https://ir.thehartford.com/news/news-details/2026/The-Hartford-Reports-Strong-Second-Quarter-2026-Financial-Results/) |
| ALLE | Q2 ended 30 Jun 2026 / 23 Jul | Revenue $1.1515bn, +12.7%, organic +6.9%; adjusted EPS $2.40, +17.6%; adjusted operating margin 24.2% | **Verified.** Original 22.1% margin is GAAP, so avoid mixing margin definitions. [Company release](https://investor.allegion.com/news-and-events/news-releases/2026/07-23-2026-110034749) |
| AIZ | Q2 ended 30 Jun 2026 / 4 Aug | GAAP EPS $5.95, +30%; adjusted EPS $6.41, +26%; segment premiums/fees/other income $3.32bn, +9% | **Verified.** Ex-catastrophe adjusted EPS $6.60 is a third earnings definition; reserve releases/catastrophe normalization matter. [Company release](https://s21.q4cdn.com/997934001/files/doc_financials/2026/q2/AIZ-2026-06-30-Ex-99-1-Press-Release_FINAL.pdf) |

All source release dates precede the specified cutoff. No specific headline earnings claim above was contradicted. The qualifications are economically important omissions or definition mismatches, not grounds for accusing the prior model of inventing the figures.

## 3. The most important valuation correction

The portfolio's label “forward P/E” hides its horizon. For NVDA, the saved ratio is exactly $224.58 / $15.68263 = **14.32x**. The EPS denominator is the `+1y` estimate, whereas the `0y` estimate is $9.30713 and gives **24.13x**. With NVIDIA's fiscal calendar, those correspond to FY2028 and FY2027 respectively. The next-year estimate implies **68.5% earnings growth** over the current-year estimate. These are consensus assumptions, not reported earnings or a demonstrated 14x next-twelve-month valuation.

The same issue affects MSFT: **21.03x next fiscal year** versus **25.20x current fiscal year**. Its current fiscal year was already FY2027 following June 2026 year-end; next fiscal year is FY2028. Cross-company comparisons using next fiscal years therefore cover different portions of calendar time.

| Ticker | Saved price | Saved forward P/E | Price / saved current-FY EPS | Current-FY EPS | Next-FY EPS in trend | Implied EPS growth |
|---|---:|---:|---:|---:|---:|---:|
| NVDA | 224.58 | 14.32 | 24.13 | 9.307 | 15.683 | 68.5% |
| CPAY | 400.32 | 12.73 | 14.61 | 27.393 | 31.448 | 14.8% |
| AMP | 485.15 | 9.39 | 10.43 | 46.527 | 51.668 | 11.1% |
| RL | 351.86 | 16.82 | 18.62 | 18.898 | 20.914 | 10.7% |
| AME | 247.74 | 25.85 | 29.71 | 8.339 | 9.585 | 14.9% |
| SNA | 367.71 | 17.19 | 18.54 | 19.830 | 21.360 | 7.7% |
| ABNB | 151.39 | 24.47 | 28.49 | 5.313 | 6.245 | 17.5% |
| NTAP | 197.24 | 17.74 | 19.71 | 10.006 | 11.121 | 11.1% |
| PAYX | 101.59 | 15.89 | 17.04 | 5.961 | 6.400 | 7.4% |
| MSFT | 497.93 | 21.03 | 25.20 | 19.760 | 23.676 | 19.8% |
| IBKR | 89.82 | 28.10 | 33.19 | 2.707 | 3.196 | 18.1% |
| HIG | 125.69 | 9.19 | 9.85 | 12.758 | 13.678 | 7.2% |
| ALLE | 152.48 | 15.60 | 17.02 | 8.956 | 9.773 | 9.1% |
| AIZ | 261.86 | 11.17 | 11.76 | 22.265 | 23.433 | 5.2% |

These calculations **reproduce vendor snapshots**, not validate consensus independently. Saved `info.forwardEps` differs slightly from `trend[+1y,current]` for ABNB, SNA and PAYX, so the table must not imply exact identity for every row. For NVDA the saved next-FY estimates range from $9.80 to $18.746 across 53 analysts. At unchanged $224.58, this is 22.92x to 11.98x; consensus uncertainty is economically larger than the two-decimal precision suggests. This is analyst dispersion, not a calibrated prediction interval.

A contemporaneously accessed [Yahoo quote page](https://finance.yahoo.com/quote/NVDA/) also displayed a 24.88x forward ratio dated 23 September alongside $224.58 close dated 24 September. That discrepancy is **unresolved**, with potential horizon/basis/staleness differences. It is not appropriate to silently overwrite the cache with the webpage number. The release validates reported results; it does not validate a vendor's consensus.

## 4. Event and accounting repairs required

1. **AME pro forma leverage:** AMETEK completed the $5bn cash Indicor Instrumentation acquisition on 26 August, after the June balance sheet. Rebuild cash, debt, interest, acquired EBITDA and goodwill before passing a balance-sheet gate. [Completion announcement](https://investors.ametek.com/news-releases/news-release-details/ametek-completes-acquisition-indicor-instrumentation)
2. **NVDA FCF reconciliation:** Saved `info.freeCashflow` is $41.810bn. Summing the four latest quarterly `deep.q_cf.Free Cash Flow` rows gives $127.006bn. Definitions or periods differ radically. Do not use the former as an unqualified trailing-twelve-month FCF number until reconciled to filings; test whether the model actually consumes this field before quantifying impact.
3. **Financial companies:** CPAY is classified in Financials but is a payments operating business; replacing leverage with an ROE test is not an adequate balance-sheet check. IBKR, AMP, HIG and AIZ need their own regulatory-capital, liquidity, underwriting or client-asset measures.
4. **Management guidance:** Document the metric, old range, new range, FX basis, acquisition perimeter and date. An “updated outlook” phrase alone cannot count as a positive revision; absent coverage must be unknown rather than pass.
5. **Cash flow and earnings quality:** Explain the NTAP cash-flow decline, HIG tax benefit, CPAY GAAP/adjusted gap, and NVDA accounting-basis change rather than copying growth headlines into durable-growth scores.

## 5. What remains unverified and how to improve the data gate

**Unverified:** all 14 exact closes against a separate exchange-authorized end-of-day feed; consensus EPS against another estimate dataset with explicit fiscal period and basis; the full four-year financial histories; all nine guidance decisions per issuer; every balance-sheet metric after post-quarter transactions; all forecast probabilities. NVIDIA's close was corroborated by multiple public secondary quote pages, but this does not establish independent underlying feed provenance.

Required field ledger: company identifier and share class, source URL or accession, units/currency, GAAP or adjusted basis, fiscal period end, publication time, retrieval time, valuation cutoff, estimate horizon, transformation, reviewer, and reconciliation status. Freeze each weekly snapshot. Do not overwrite historical vintages.

Use **reported**, **management forecast**, **analyst estimate**, and **model assumption** as four visibly separate classes. Calendarize EPS to a documented NTM basis; also display current-FY, next-FY and normalized trailing valuations. Apply hard quarantine only to material unresolved fields, and propagate the uncertainty to position size and recommendation status.

For a weekly buy/hold/sell process, the first job is to detect changed facts and reconcile fresh releases; it is not to rerun static confidence percentages. Day-to-year flexibility does not make long-horizon fundamentals a validated short-term trading signal, and a 15–20% loss tolerance cannot be certified by this data audit.
