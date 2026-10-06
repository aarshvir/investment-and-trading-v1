# CVX — Chevron Corporation (Agent F83, wave 5)

## 1. Verdict
**INCLUDE-SMALL** (half weight). Reservation: reverse DCF at the 25 Sep 2026 close implies growth broadly consistent with consensus, but the thesis is fully commodity-price dependent (oil-price beta) and the Hess/Guyana integration, while ahead of schedule, is still early — size half-weight to respect the Q03 triage's own red flag. Horizon: 24–36 months.

## 2. Business in plain English
Chevron is an integrated oil major: it explores for and produces crude oil/natural gas (upstream — the main profit driver) and refines/markets fuels and chemicals (downstream). It just closed the Hess acquisition, adding low-cost, high-margin Guyana offshore production and Bakken shale acreage. It earns on the spread between production cost and commodity price, with downstream providing some counter-cyclical balance.

## 3. Why the model likes it / durability
Q03 triage: "best-in-class consolidated balance sheet (0.6x net debt/EBITDA), now adding Hess's low-cost Guyana growth assets... genuine multi-year production growth at a cheap 13.9x NTM multiple." Confirmed and, if anything, strengthened: Q2 2026 production was **+20% YoY** (+674 MBOED), driven by Hess/Guyana (+275 MBOED), Bakken (+180 MBOED) and organic U.S. onshore growth (+110 MBOED) [1][2]. Chevron captured **50% more Hess synergies than originally targeted** ($1.5bn realized, six months ahead of schedule) [1]. This is durable: Guyana is a multi-decade, low-breakeven resource, not a one-quarter item — the growth driver is structural, not a comp artefact.

## 4. Last two years of results (selected, GAAP unless marked "adj.")
| Quarter | Revenue | Net income | Adj. EPS | OCF |
|---|---|---|---|---|
| **Q2 2026** | **$70.06B** | **$12.1B** | **$6.06 (adj.)** | **$19.7B** |

Beat consensus: adj. EPS $6.06 vs Street $5.11; revenue $70.06B vs Street $62.26B [1][2]. Full 8-quarter table not rebuilt this pass (time-box; Q2'26 filing-sourced figures are the load-bearing comparison). Source: Chevron 10-Q for period ended 2026-06-30 (SEC EDGAR, accession 0000093410-26-000167) [2]; Chevron 8-K Ex-99.18, Q2 2026 (accession 0000093410-26-000162, filed ~Jul 2026) [3].

## 5. Guidance track record
Chevron does not issue formal quarterly EPS/revenue guidance in the way CAT or CBOE do; it guides capex, buyback pace and production targets. Management has reiterated **$10–20bn/year share-repurchase** capacity depending on market conditions, and confirmed the Hess synergy target was raised (captured, not merely reiterated) mid-execution [1]. We did not independently pull a formal prior-vs-current production-guidance range from the Q1 2026 8-K this pass — **data gap**.

## 6. Earnings quality & balance sheet — entity scope
- **Consolidated net debt**: ~$28.6B at 30 Jun 2026 TTM basis, net debt/CFFO (operating cash flow) **0.6x** (net debt $28.6B vs TTM OCF $45.3B) — consistent with, and confirming, the Q03 triage's "0.6x net debt/EBITDA"-style characterization, though note the two ratios (net debt/CFFO vs net debt/EBITDA) are not identical denominators — **flagged, not corrected**, since both point to the same "very low leverage" conclusion [4].
- **Net Debt Ratio** 13.1%, **Debt Ratio** 16.3% (consolidated; aggregator cross-check derived from the 10-Q, accession 0000093410-26-000167) [4] — independently re-deriving these directly from that filing's own balance sheet was not completed this pass (data gap); treat as a cross-check, not a filing-verified figure.
- **Shareholder returns**: 2025 dividends paid $12.8B; quarterly dividend raised 5% to $1.71/share (38th consecutive annual increase); 2025 buybacks $12.1B [4] — these are FY2025 figures carried into the balance-sheet discussion for context; 2026 YTD buyback/dividend figures not independently pulled this pass (data gap).
- FCF conversion, SBC%, and Hess-acquisition financing detail (how much was cash vs stock vs new debt): not independently rebuilt this pass — **data gap**, time-boxed under addendum §5 priority order.

## 7. Valuation — reconciliation with V1
**No V1 row exists for CVX** in `outputs/v1_valuation_table.csv` or `v1_valuation.json` — `v1_verdict = null`; valuation view here is independent, not reconciled against a systematic model.

Own reverse-DCF sense: price ~$204–206 (25 Sep 2026 area, aggregator cross-check) [5], forward P/E ~13.0–13.5x, consensus next-12m EPS growth ~16.7% (from ~$10.79 to ~$12.59, aggregator estimate, oil-price-sensitive and not a primary-source number) [5]. At a mid-teens forward multiple for an integrated major with high-single-digit-to-low-teens underlying production growth (ex-commodity-price effects) once Hess is fully absorbed, the price is **not** demanding a heroic growth assumption — a mid-teens multiple is toward the lower end of CVX's own 10-year range (qualitative; not independently re-derived from D3 history this pass). **implied_vs_base = in_line to below**, i.e. the market is not obviously over-extrapolating the Hess-driven production beat, which supports the INCLUDE-SMALL sizing rather than a full-weight INCLUDE (oil-price risk is exogenous and not captured by any reverse-DCF growth number).

## 8. Bull case
1. Hess/Guyana integration is running ahead of plan (synergies 50% above target, captured 6 months early) — de-risks the single biggest event-risk of the past 18 months.
2. Best-in-class consolidated leverage (net debt/CFFO 0.6x) gives capacity to keep buying back $10–20bn/year through a commodity down-cycle without cutting the 38-year dividend streak.
3. Guyana is a low-breakeven, multi-decade resource — production growth here is structurally different from mature legacy fields.

## 9. Bear case
1. Thesis is fundamentally oil-price dependent; Q2'26's revenue/EPS beat is partly commodity-price driven, and a downside oil shock overwhelms any production-growth story (triage's own red flag).
2. Integration risk is "still early" per Q03 triage — synergy capture to date is real, but full operational integration of Hess's asset base and workforce is multi-year.
3. Downstream refining margins and any regulatory/carbon-policy shift are not assessed this pass (data gap) and are a real tail risk for an integrated major.

## Kill criteria (measurable)
1. Consolidated net debt/CFFO (or net debt/EBITDA) rises above 1.5x for two consecutive quarters (vs 0.6x now) — signals leverage-funded buybacks/dividend under commodity stress.
2. Quarterly production growth YoY falls below 5% for two consecutive quarters (vs +20% in Q2'26), indicating Hess/Guyana growth has stalled.
3. Quarterly dividend is cut or frozen (breaking the 38-year consecutive-increase streak).
4. Share buybacks fall below the low end of the $10bn/year guided range for two consecutive quarters without a stated commodity-price rationale.
5. Brent/WTI sustained below a level that makes Guyana/Permian marginal barrels uneconomic (specific breakeven price not independently sourced this pass — data gap; set a placeholder review trigger at WTI <$55/bbl sustained for a full quarter pending that data).

## 10. Catalysts & calendar
Next earnings: **Q3 2026, 23 Oct 2026** (aggregator estimate; not independently confirmed against a primary IR press release — data gap) [6].

## 11. Red-flag scan
No auditor change, restatement, going-concern language, or SEC/DOJ litigation identified in sources reviewed this pass. Hess acquisition itself carried arbitration risk (Exxon/Guyana pre-emption dispute) prior to closing; post-close litigation status not independently re-verified this pass (data gap — flag for the next fact-check pass given this was a material, contested deal).

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (period end 2026-06-30), Form 10-Q filed on SEC EDGAR ~Jul 2026 (accession 0000093410-26-000167). Checked for events to 2026-09-25. GAAP figures (revenue, net income, OCF) are as reported; EPS figures cited ($6.06) are labelled "adjusted" per the earnings release. Leverage ratios, price, forward-P/E and consensus-growth figures in §6–7 are aggregator/Street cross-checks, not independently re-derived from the 10-Q's own tables this pass — flagged as lower-confidence than the filing-sourced production/earnings figures. Hess-arbitration post-close status and full capital-structure detail are data gaps under the time-box. **Research, not personal investment advice.**

## Sources
1. Investing.com, "Chevron Q2 2026 slides: production records, Hess synergies ahead" (summarizing company release), https://www.investing.com/news/company-news/chevron-q2-2026-slides-production-records-hess-synergies-ahead-93CH-4829036
2. Chevron Corp 10-Q, period 2026-06-30, https://www.sec.gov/Archives/edgar/data/0000093410/000009341026000167/cvx-20260630.htm
3. Chevron Corp 8-K Ex-99.18, https://www.sec.gov/Archives/edgar/data/0000093410/000009341026000162/a06302026ex9918-k.htm
4. OilNOW, "Chevron CFO says Hess portfolio, including Guyana, adds 250,000 b/d" and aggregator leverage/dividend cross-check, https://oilnow.gy/featured/chevron-cfo-says-hess-portfolio-including-guyana-adds-250000-b-d-to-production-growth/
5. Aggregator price/forward-PE/consensus-growth cross-check (accessed 2026-09-27, various: CNN Markets, GuruFocus, stockanalysis.com).
6. Aggregator earnings-calendar estimate (unconfirmed against primary IR release), accessed 2026-09-27.
