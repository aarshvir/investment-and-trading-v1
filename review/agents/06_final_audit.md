# Final adversarial audit of the replacement review

Review date: 26 September 2026. Market-data cutoff: supplied 24 September 2026 US close.

**Verdict:** Accept the central conclusion that the original allocation is not ready for deployment. Accept the replacement as an audit and proposed research policy, conditional on the presentation corrections below. Do not describe it as a completed investment mandate, independently certified 497-company database, or new approved portfolio.

This specialist reviewed the lead investment-committee document and weekly policy, specialist reports 01–03, the supplied portfolio source and reproduction code, the 497-row ledgers, data summaries and the company-triage JSON. Primary-source spot checks independently reopened NVIDIA, Microsoft and NetApp releases. This is synthesis review with targeted source checks, not a second full external audit of all 14 companies or all source files.

## Required corrections communicated to the lead

1. **Source-file count:** the source manifest has **67 entries**, and `source_bundle/equity_project` has **67 files**. Replace the draft's 64-file claim. Inventorying a file is not proof of reading its entire contents; describe the work as bundle inventory plus targeted code/data review where appropriate.
2. **Dollar drawdown denominator:** 36.1509% drawdown means loss from the contemporaneous portfolio peak. Say **“a $100,000 portfolio peak would fall about $36,151”**; do not imply that the historical dollar drawdown necessarily equals 36.15% of initial invested capital. The same conversion for a $50,000 peak is about $18,075.
3. **Allocation units:** specify **2% of total portfolio capital per directly held stock and 5% of total portfolio capital per sector within the direct-stock sleeve**. Reporting aggregate fund look-through exposures is essential, but it is not automatically the same as imposing a 2% issuer cap on direct plus indirect exposures. Define the latter separately if intended.
4. **Sensitivity conventions:** agent 01 changes the assumed **index** annual drift and keeps the original stock/index spread; its 50/50 portfolio drift is roughly the stated index drift plus 0.68 percentage point. Agent 03 and the lead's 66%/75% figures change assumed **blend** drift directly. Hence 69.5% and 66.1% at a “4%” label are different experiments. Label both; do not merge their rows.
5. **Next-step implication:** receiving a holdings export permits actual-exposure assessment and identification of applicable actions. It does not complete missing valuation, consensus or company-underwriting gates. Avoid implying that holdings disclosure alone makes the first report's candidates approved buys.

## Numerical and methodological checks accepted

| Claim | Final-audit check | Result |
|---|---|---|
| 497 stock records | Counted both universe ledger and mechanical diagnostic CSV | 497 in each |
| 503 records to 497 | Summary explicitly lists FDXF, FOX, GOOG, HONA, NWS, Q exclusions | Six omissions, not three |
| Independent price/consensus validation | Ledger summary carries zero externally certified quotes and zero externally certified consensus records | Lead disclosure is appropriately limited |
| Original portfolio limits | Read weight-construction loop and checked exact weights/sector totals in risk output | RL and ABNB 10.6325%; Financials, Industrials and IT 26.2450% each |
| Feasible invested maximum | Two consumer names at 10% each plus three other sectors at 25% each | 95%; fully invested constraint set infeasible |
| Drawdown | Reproduction retains daily path with monthly resets; month-end path agrees to roughly 7.5e-14 numerical error | Monthly 26.1770%; daily monthly-rebalanced 36.1509%; current-holdings retrospective replay only |
| Missing history | Risk output and original fill-zero code | ABNB has 52 missing monthly observations in 121; original treatment is prelisting cash |
| NVIDIA valuation | Recomputed from draft's rounded inputs | 224.58 / 9.307 = 24.13x; /15.683 = 14.32x; implied EPS growth 68.51% |
| Microsoft valuation | Read independently calculated company ledger | Current FY 25.1992x, vendor next FY 21.0311x; forecast inputs unverified |
| Diagnostic return | Diagnostic summary and calculation inspected | 11.3614% to 9.5654%; rounded 11.36% to 9.57%; not an investable forecast |
| Editorial audit grade | Added all ten stated component scores | 43/100; subjective rubric, not calibrated probability |
| Stress table | Recomputed equity fraction × equity shock × starting scenario capital | All eight 30%/full-equity dollar comparisons correct |
| Position risk example | 0.25% capital /25% assumed position stress | 1% of capital; illustrative loss budget, not a stop guarantee |

The original portfolio weights are rounded to a sum of 99.98% in the delivered JSON. The diagnostic normalizes that immaterial discrepancy; the risk reproduction reconstructs unrounded weights. Tiny differences in weighted expected-return decimals do not constitute a material contradiction.

The original 90% headline cannot be interpreted as a calibrated probability of investor success. The simulation recenters returns to an assumed monthly drift and keeps expected-return uncertainty outside the model. Profiting after five years is also different from respecting a 15–20% intraperiod loss tolerance. Twenty thousand generated paths narrow simulation noise conditional on the model; they do not establish forecast accuracy. The lead's distinctions among stability, confidence, arithmetic reconciliation and independent verification should be preserved.

## Primary-source spot checks

- NVIDIA's Q2 FY2027 release supports revenue of $96.221 billion and +106% growth, GAAP/non-GAAP diluted EPS of $2.46/$2.22, and the change to include stock compensation in non-GAAP results. These are historical reported results, not authentication of vendor forecast EPS. [NVIDIA release](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/).
- Microsoft's Q4 FY2026 release supports quarterly revenue of $90.007 billion and annual revenue of $331.839 billion. Q4 operating income grew 18%; Q4 net income grew 31% GAAP and 22% adjusted. The release identifies a $0.27 diluted-EPS benefit from additional discrete items; the company's OpenAI-adjusted EPS is therefore not automatically fully normalized earnings. [Microsoft release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast).
- NetApp's Q1 FY2027 release supports revenue of $2.025 billion, +30%; operating cash flow of $503 million versus $673 million; capital expenditure of $102 million versus $53 million; and FCF of $401 million versus $620 million. Those reconcile to approximately -25% operating cash flow and -35% FCF. [NetApp release](https://investors.netapp.com/news/news-details/2026/NetApp-Reports-First-Quarter-of-Fiscal-Year-2027-Results/default.aspx).

The company-triage JSON correctly labels all 14 names as research priorities with unresolved diligence, rather than approved investments. A priority number is an ordering for resolving uncertainty, not a ranking of expected return or an investment recommendation. Preserve that distinction wherever these rows are displayed.

## Proposed policy accepted with limitations

The 30% equity/70% reserve framework is coherent **only as a declared stress-budget example**: 30% × 50% equity decline = 15% portfolio decline with a flat reserve. The draft appropriately states that it is neither optimized nor an instruction to buy a particular product. Do not infer universal suitability from a single loss-tolerance answer. Existing investments, income/liquidity needs, liabilities, withdrawal needs and instrument risks remain necessary.

For perspective, a 5% reserve loss would contribute another 3.5 percentage points to portfolio loss: the -50% equity example becomes -18.5%; the -60% example becomes -21.5%. This arithmetic illustrates why “liquidity reserve” is not sufficient product specification and why the proposed 20% boundary is not guaranteed.

The 8%/12%/15% drawdown thresholds, 0.5% quote-reconciliation tolerance, two-week ordinary switch confirmation and 5% one-way turnover review threshold are governance proposals. They are not empirically optimal or prospectively validated. A weekly scheduled research report does not deliver daily alerts or order execution. A serious thesis break should override an ordinary two-week confirmation rule; the policy already provides that exception.

A reserve, a broad equity fund and individual stocks should be accounted for separately. A 50% index/50% stock mix remains 100% equity. Aggregate issuer, sector and factor overlap still needs measurement even if direct-stock sleeve limits are respected.

## Residual limitations that must remain visible

- No independently reconciled consensus dataset, exchange-price certification or order-ready valuation exists for the 497-name universe.
- Primary headline verification is much narrower than two years of complete company underwriting, transcript review, financial-statement reconciliation and independent estimates.
- The corrected diagnostic retains original growth/rerating assumptions and introduces assumed 4% risk-free return and 4% equity-risk premium; it is a sensitivity, not a new return model validated by this audit.
- Historical simulation retains survivor-universe selection, current-holdings hindsight and limited regimes. Reported probabilities remain conditional; no real-world calibration was established.
- The original 100/30 research pages can be preserved as legacy work but cannot be relabeled as newly completed due diligence.
- Multiple agents share model family and overlapping source material. Separate workstreams help identify errors but do not equal six independent financial institutions or prove investment skill.
- No user holdings have been supplied to this reviewer. No actual HOLD/REDUCE/SELL instructions or executed orders are established by this review.

No source or lead files were modified by this specialist; only this audit report was authored.

## Late-arriving reports 04 and 05

The completed underwriting and implementation/tax reports were read before closing this audit. Their scope and conclusions are consistent with the lead's limited approval status. Report 04 explicitly separates research-priority ordering from buy ranking and does not publish unsupported fair values. Report 05 separates estate filing thresholds from tax liability, fund-level dividend withholding from investor taxation, and product identity from broker eligibility. This synthesis reviewer did not independently repeat every legal citation or the newly introduced company-commitment figures; their primary-source checking remains attributed to those specialists.

Carry three implementation points from report 05 into the final operating policy: define whether the 15–20% tolerance applies to this mandate or aggregate investments; a proposed 30% ceiling must not become an instruction to sell unknown existing positions; and failed data refreshes should freeze discretionary new purchases without automatically liquidating holdings. US citizenship, income-tax residence and estate domicile remain open questions before relying on the conditional Irish-fund discussion.

## Closure after lead revisions

Re-read the revised investment-committee memo and weekly policy. **All five required corrections above are resolved:** 67-file count, portfolio-peak denominator for dollar drawdown, direct-stock cap denominators and look-through distinction, explicit separation of the two drift-sensitivity experiments, and confirmation that holdings disclosure does not waive buy evidence gates. The policy also now defines the provisional mandate-capital denominator, disclaims liquidation of unknown existing holdings, and freezes new discretionary buys on failed data refreshes without automatic sales.

The saved dashboard validation record reports 23 rendered tabs, no recorded JavaScript errors, 14 company dossiers, functioning search and no mobile page overflow. This is a review of the lead's saved test evidence, not a separate browser test. The lead reports successful creation of the Sunday 18:00 Asia/Dubai weekly research automation; that operational step does not establish daily monitoring, forecast validity or trading authorization.

**Publication conclusion:** the audit and proposed operating process may be released with their stated limitations. Residual economic work remains: independently reconciled prices/consensus, completed company forecasts and valuations, prospective validation, reserve/product suitability, actual holdings and tax-status reconciliation. Closure resolves presentation findings; it does not approve the original portfolio or any new investment allocation.
