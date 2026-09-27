# IBKR — Interactive Brokers Group, Inc.

## 1. Verdict
**INCLUDE-SMALL** (12–36 month horizon). Reservation: earnings are structurally levered to trading volumes and short-term interest income, both of which are running above normal; the reverse-DCF implied growth already sits below a reasonable base case, but a normalization of volatility/rates could cut realized growth well below what today's price needs.

## 2. Business in plain English
IBKR is a low-cost, highly automated electronic broker serving active retail and institutional traders across 200+ markets in 27 currencies. It earns commissions on trades, spreads/fees on margin lending and stock loan, and net interest on ~$180bn+ of customer cash and margin balances. Its moat is technology and cost structure: it can profitably serve accounts that full-service brokers can't, which drives industry-leading account growth.

## 3. Why the model likes it / durability
b1 factors show top-decile quality (ROE 19.1%, pct_roe 69%) and strong momentum (pct_mom_12_1 93%), with the growth/quality signal coming from real operating leverage (customer accounts +34% YoY, DARTs +36% YoY in Q2 2026 — company release) rather than an accounting artefact. The durable part is the account/volume growth (low-cost model taking share); the less durable part is net interest income, which depends on the level of short rates and margin balances, both currently elevated.

## 4. Structural note — read EPS, not consolidated net income
IBKR Group's public stock (ticker IBKR) represents a minority (~15–16%) economic interest in the operating partnership IBG LLC (majority held by the Peterffy family / employees). Consolidated net income and consolidated equity are **not** what accrues to IBKR shareholders. All figures below use `NetIncomeLossAvailableToCommonStockholdersDiluted` and per-share GAAP diluted EPS (post the 2025 4-for-1 stock split; SEC EDGAR companyfacts, CIK 0001381197).

## 5. Last quarters — results (GAAP, consolidated revenue net of interest expense; EPS to common)
| Qtr | Total net revenue ($m) | YoY | Net income to common ($m) | Diluted EPS |
|---|---|---|---|---|
| Q2'25 | 1,480 | — | 224 | 0.51 |
| Q3'25 | 1,655 | — | 263 | 0.59 |
| Q4'25 | 1,643 | — | 284 (984 FY − 700 9mo) | 0.64 |
| Q1'26 | 1,669 | +17.0% | 267 | 0.59 |
| Q2'26 | 1,896 | +28.1% | 312 | 0.69 |

Source: SEC EDGAR companyfacts (`RevenuesNetOfInterestExpense`, `NetIncomeLossAvailableToCommonStockholdersDiluted`); confirmed against company 2Q2026 press release (interactivebrokers.com), which reports GAAP net revenue $1.90bn (+28.1% YoY), adjusted net revenue $1.88bn (+27.2%), pre-tax margin 77% (7th straight quarter >70%), customer accounts 5.19m (+34%), DARTs 4.82m (+36%), customer equity $930.3bn (+40%). FY2025 diluted EPS $2.22 vs FY2024 $1.73 (+28.3%, both post-split, per 10-K filed 2026-02-27, accession 0001381197-26-000062).

## 6. Balance sheet & cash conversion
Consolidated basis (entity: IBKR Group Inc. consolidated, includes broker-dealer regulatory capital, not just parent): cash $7.71bn (Jun-30-26) vs $4.96bn (Dec-31-25); consolidated stockholders' equity (parent + minority note: this line is parent-attributable equity per XBRL tag, $5.90bn Jun-30-26 vs $5.36bn Dec-31-25 — the much larger noncontrolling-interest equity sits separately on the balance sheet and is not shown here). IBKR is a capital-light agency/market-making broker; FCF broadly tracks net income (minimal capex, no meaningful long-term debt at the parent level — funding is via customer margin balances and short-term broker financing, disclosed in the 10-Q's (accession 0001381197-26-000147) borrowings note).

## 7. Guidance track record
IBKR does not give formal quarterly EPS/revenue guidance; management commentary each quarter covers volume/account trends and pricing initiatives, not point guidance. No "raise/cut vs prior range" table applies — noted per addendum requirement.

## 8. Valuation
V1 systematic table has no row for IBKR (`v1_valuation_table.csv`/`v1_valuation.json` do not cover this ticker) → `v1_verdict = null`, no reconciliation possible; treated as an in-house reverse DCF only.
TTM diluted EPS (Q3'25–Q2'26): 0.59+0.64+0.59+0.69 = **$2.51**. Price (25-Sep-2026 close) $89.24 → trailing P/E ≈ 35.6x.
Reverse DCF (10-yr explicit + Gordon terminal, r=9% cost of equity, terminal g=4%): price implies **~10.8%/yr** EPS growth for 10 years.
My base case: 12–15%/yr (mid-teens account growth continuing to decelerate from the current 30%+ pace, plus buybacks, partially offset by normalizing net-interest income as short rates likely ease over the cycle). Implied (10.8%) sits **below** my base case → dossier view: **fair-to-cheap on a reverse-DCF basis**, but the "base case" itself assumes volumes stay well above the 2019–2022 run-rate; a genuine volume/vol mean-reversion would make the 35.6x trailing multiple look expensive.

## 9. Bull case
1. Account growth (+34% YoY) and DART growth (+36% YoY) show the low-cost model is still taking share from full-service brokers globally, especially outside the US.
2. Pre-tax margin of 77%, 7 consecutive quarters >70%, shows genuine operating leverage, not one-off.
3. Buybacks/organic float growth of the public share class increase EPS to common faster than consolidated net income grows.

## 10. Bear case
1. ~40–50% of revenue is net interest income; a Fed easing cycle mechanically compresses this segment even if balances keep growing.
2. Elevated retail trading activity (DARTs +36%) is partly cyclical (2025–26 volatility); a quiet market would cut commission revenue.
3. Public shareholders own a minority economic stake in a franchise still majority-controlled by insiders (Peterffy family/IBG LLC), a structural governance/valuation discount that can't fully close.

## 11. Key risks & kill criteria
1. Net interest income falls >15% YoY for two consecutive quarters (rate-cut driven, not offset by balance growth).
2. DART growth decelerates below 10% YoY for two consecutive quarters.
3. Pre-tax margin falls below 70% for two consecutive quarters.
4. Any new SEC/FINRA/CFTC enforcement action with a fine >$25m (given the firm's AML/SAR/OFAC settlement history: $38m 2020 SAR settlement, $11.5m OFAC penalty disclosed 2025).
5. Diluted EPS to common growth turns negative YoY in any quarter.

## 12. Catalysts & calendar
Next earnings: ~mid/late-October 2026 (Q3 2026, based on historical cadence of reporting in the third week of the month following quarter-end).

## 13. Red-flag scan
- No auditor change, restatement, or going-concern language found in the FY2025 10-K or 2026 10-Qs reviewed.
- Historical AML/SAR enforcement: SEC/FINRA/CFTC $38m combined penalty (2020, disclosed) and a 2025 OFAC settlement (~$11.5–11.8m per public reporting) for non-egregious, self-disclosed sanctions violations — pattern of AML/compliance friction worth monitoring, not a going-concern issue.
- 2022 SEC information request re: off-channel business communications (industry-wide sweep) — status of resolution not independently confirmed in filings pulled; flagged as unresolved item to verify in the next 10-Q.
- Governance: dual-class-like economic structure (public minority interest in IBG LLC) is disclosed prominently in the 10-K risk factors.

## 14. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (10-Q filed 2026-08-06, accession 0001381197-26-000147) and the company's 2Q2026 earnings release (interactivebrokers.com). SEC EDGAR CIK 0001381197 (submissions + companyfacts XBRL, pulled 2026-09-27). Events checked to 2026-09-25 close via web search. GAAP figures used throughout unless labelled "adjusted." **Research only; not personal investment advice.**

## 15. Sources
1. SEC EDGAR submissions, CIK 0001381197 — https://data.sec.gov/submissions/CIK0001381197.json
2. SEC EDGAR companyfacts XBRL, CIK 0001381197 — https://data.sec.gov/api/xbrl/companyfacts/CIK0001381197.json
3. Interactive Brokers Group 2Q2026 earnings release — https://www.interactivebrokers.com/mkt/getFileNew.php?file=latestEarningsPR
4. IBKR Q2 2026 earnings call transcript — https://www.fool.com/earnings/call-transcripts/2026/07/21/interactive-brokers-ibkr-q2-2026-earnings-call-transcript/
5. SEC AML/SAR enforcement action (2020) — https://www.sec.gov/newsroom/press-releases/2020-178
6. Reporting on 2025 OFAC settlement — https://www.steel-eye.com/news/interactive-brokers-ofac-fine-sanctions-violations
7. v4/data/b1_live_scores.csv (factor scores, as_of 2026-09-25); v4/outputs/Q05_triage.json (prior triage note)
