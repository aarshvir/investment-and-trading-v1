# Audit 1 — filing-level cash flow, debt and lease reconciliation

Prepared 26 September 2026 Dubai; investment-information cutoff 24 September 2026 US close. The finance-skills financial-analyst workflow was applied: scope, completeness checks, calculation, interpretation and follow-up. This is a targeted six-company field audit, not an audit opinion or certification of the entire universe.

**Conclusion: the source tables support several important corrections, including corrections to our earlier review.** The original vendor `info.freeCashflow` must not enter valuations as an unqualified trailing cash-flow number. NVIDIA and Microsoft have large, reproducible mismatches. Airbnb's rounded $1.3bn/35% FCF claim is supportable; the earlier suggestion that it necessarily confused EBITDA and FCF was too strong.

## 1. NVIDIA: two legitimate definitions; the saved headline matches neither

All amounts below are USD millions. The [FY2026 10-K, cash-flow statement p55](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) and [Q2 FY2027 10-Q, p8](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf) provide:

| Measure | FY ended 25 Jan 2026 | H1 ended 26 Jul 2026 | H1 ended 27 Jul 2025 | Rebuilt TTM |
|---|---:|---:|---:|---:|
| Operating cash | 102,718 | 74,421 | 42,779 | 134,360 |
| PPE/intangible cash purchases | 6,042 | 4,434 | 3,122 | 7,354 |
| Related principal payments | 101 | 92 | 73 | 120 |
| CFO less purchases | 96,676 | 69,987 | 39,657 | **127,006** |
| Company-defined FCF | 96,575 | 69,895 | 39,584 | **126,886** |

Transformation: TTM = FY + current H1 − prior H1. [The company's non-GAAP reconciliation](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/) deducts both purchases and principal. Saved quarterly FCF sums to $127,006m, matching the conventional definition exactly; individual quarterly vendor components still contain small differences. Saved `info.freeCashflow` is **$41,809.874944m**, $85,196.125056m below conventional TTM. Its precise vendor formula remains unknown. Quarantine that field; retain both independently rebuilt definitions with explicit names. Neither historical cash measure alone proves sustainable owner earnings.

## 2. Airbnb: resolve the apparent contradiction in favor of the filing

[Q2 2026 10-Q, MD&A pp25–26, non-GAAP summary and reconciliations](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000027/abnb-20260630.htm): quarterly revenue $3,608m; CFO $1,270m; capex $17m; FCF **$1,253m**, or **34.73%**; adjusted EBITDA **$1,261m**, or **34.95%**. Both legitimately round to $1.3bn and 35%. They are distinct fields, not interchangeable calculations. Quarterly EBITDA includes a $487m stock-compensation add-back.

The filing's FCF paragraph distinguishes advance collections of Airbnb's own service fees from customer money held for others. The latter does not affect FCF except interest; service-fee timing and Reserve Now, Pay Later do. Accordingly, normalize own fee timing and dilution, but do not subtract all guest balances from FCF. Release the rounded quarterly FCF claim from quarantine. Do not convert this one-quarter check into approval of saved $3,206.875m vendor TTM FCF or a valuation.

## 3. NetApp: reconstruct the cash deterioration, then test the explanation

[Q1 FY2027 10-Q, cash-flow statement p6 and MD&A pp27–28](https://www.sec.gov/Archives/edgar/data/1002047/000119312526380207/ntap-20260731.htm) supports this year-on-year CFO bridge (USDm):

| Driver | Change in cash contribution |
|---|---:|
| Net income | +142 |
| Depreciation/amortization | −18 |
| Noncash lease cost | 0 |
| Stock compensation | +15 |
| Deferred taxes | −14 |
| Other noncash items | −61 |
| Receivables | −149 |
| Inventory | −230 |
| Other operating assets | −224 |
| Payables | +126 |
| Accrued expenses | +165 |
| Deferred revenue | +80 |
| Other operating liabilities | −2 |
| **Total CFO change** | **−170** |

CFO $673m→$503m; capex $53m→$102m; FCF $620m→**$401m**. Exact changes: −25.26% CFO and −35.32% FCF. Management attributes inventory growth to strategic components and finished goods. That is an explanation, not independent proof of recoverability. [The official supplemental table](https://investors.netapp.com/news/news-details/2026/NetApp-Reports-First-Quarter-of-Fiscal-Year-2027-Results/default.aspx) shows inventory turns falling 14→6 and FCF margin 39.8%→19.8%. Monitor subsequent collections, component consumption, write-downs and gross margin. Cash conversion remains an underwriting concern after the arithmetic passes.

## 4. Corpay: reported 'FCF' is a different measure

[Q2 earnings exhibit, non-GAAP definition and Exhibit 1](https://www.sec.gov/Archives/edgar/data/1175454/000117545426000045/ex991q2_2026.htm) labels adjusted net income as free cash flow. H1 adjusted income is **$861.554m**; Q2 $464.384m. The [10-Q cash-flow statement p5](https://www.sec.gov/Archives/edgar/data/1175454/000117545426000050/cpay-20260630.htm) gives H1 CFO $1,413.479m less capex $105.529m = **$1,307.950m** conventional FCF. The $446.396m difference is not an arithmetic error; the definitions differ. Neither is automatically distributable cash.

The earnings exhibit reports **2.55x** management leverage. The original cached vendor net-debt/EBITDA ratio rounds to **2.7x**, while the company reports **2.55x** under its management definition. The latter is not a same-basis correction of the former. Their numerator/denominator bridge remains unresolved; neither is independently replicated covenant leverage. The 10-Q pp40–42 warns that even unrestricted cash includes customer deposits and operating/regulatory requirements. Restricted cash is $7,004.803m; customer deposits $8,915.786m; securitization debt $2,300m. Do not net all cash against corporate debt. Saved `info.freeCashflow` $1,946.175872m exceeds saved operating cash $1,847.283968m; its period and transformation require repair before use.

## 5. AMETEK: financing capacity is not funded debt

[June 10-Q p5 and Note 12 p17](https://www.sec.gov/Archives/edgar/data/1037868/000103786826000175/ame-20260630.htm): cash **$495.446m**; current debt **$980.633m**; long-term debt **$1,055.541m**; carrying debt **$2,036.174m**. The $4bn acquisition term facility had not been drawn at June-end. Tranches: $1.625bn/three years, $1.625bn/four years, $0.750bn/five years. Up to $1bn of the revolver could support the deal; prior $5bn bridge commitments had terminated. Vendor debt $2,310.944m is not this carrying-debt definition; the difference is not automatically an error.

[The August 26 completion release](https://investors.ametek.com/news-releases/news-release-details/ametek-completes-acquisition-indicor-instrumentation) and [8-K Item 8.01](https://www.sec.gov/Archives/edgar/data/1037868/000103786826000191/ame-20260826.htm) establish $5bn all-cash completion, but do not publish a complete closing balance sheet. The funding commitments cannot be substituted for actual drawdowns.

**Illustrative bridge, not reported actual:** unchanged pre-deal net debt $1,540.728m + $5,000m cash purchase = $6,540.728m before intervening cash generation, acquired cash, fees, assumed debt and other changes. Actual post-close debt, acquired EBITDA and leverage remain quarantined. Do not assert an actual post-deal leverage ratio until those inputs are available.

## 6. Microsoft: quantify both cash and lease measures

[FY2026 10-K p53 and Note 13 pp77–78](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm) was downloaded in full and parsed locally after the web reader failed. Annual CFO **$182,935m** − cash PPE **$115,948m** = **$66,987m**; saved quarterly FCF sums identically. Saved headline FCF is **$16,545.500160m**, a $50,441.499840m shortfall.

Note 13 identifies operating-lease cash $6,443m, finance-lease interest cash $2,547m, and finance-lease principal $3,101m. CFO already includes the first two. CFO−PPE−finance principal = **$63,886m**, a separate analyst cash measure. Do not deduct operating lease cash twice. New finance ROU assets $24,608m are noncash additions, not current cash payments. Uncommenced leases $329.1bn are future commitments, not all current recognized debt; some are conditional.

[The Q4 call's CFO commentary](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4) changes building lives from 15 to 25 years at FY27 start, shifting more future leases to operating classification. The resulting ~$175bn calendar-2026 capex guidance is not evidence that economic investment fell. Quarantine economic-investment trend comparisons until a consistent lease bridge is attached.

## Evidence controls and completion limits

`01_filing_ledger.json` and CSV hold field-level periods, units, transformations, source locators, source hashes and statuses. `raw_filing/manifest.json` records downloaded bytes, UTC retrieval and SHA-256. Raw documents are originals; extracted `.facts.json` files preserve selected inline-XBRL tags, unit/scale and fiscal contexts. These extracted facts are not a full taxonomy audit. The AMETEK closing webpage was read in the web tool but its direct archive download timed out; the 8-K is archived.

Arithmetic passes permit use of the specified historical fields, not recommendation approval. Outstanding: exact vendor FCF definitions, complete corporate-cash/customer-funds bridges, AMETEK closing capital structure, Corpay covenant reconciliation, subsequent cash-conversion tests and valuation forecasts. No post-cutoff results are substituted. No source snippet was promoted to a verified filing value. No trades or portfolio allocations were approved by this audit.

## Additional provider corroboration

The authenticated FMP annual cash-flow response archived in `raw/fmp_nvda_cashflow_annual.json` independently reproduces the transformation of NVIDIA's FY2026 issuer figures: CFO $102,718m, signed capex −$6,042m, conventional FCF $96,676m. This corroborates extraction and vendor mapping; both ultimately depend on the same issuer filing. It is not independent evidence of business economics or a second issuer source. The response's zero optional `incomeTaxesPaid` and `interestPaid` fields must not be treated as proven zero cash payments. Microsoft’s actual displayed annual response likewise gives FY2026 CFO $182,935m, signed capex −$115,948m and FCF $66,987m. Its retained JSON contains selected fields transcribed from the complete Raw UI display because the download did not complete; it is not a byte-for-byte raw response. The provider access ledger records this distinction. Both corroborations are included in the 33-row field ledger.
