# PYPL — PayPal Holdings, Inc. (NASDAQ: PYPL)

## 1. Verdict
**INCLUDE-SMALL** (half weight) — 18–30 month horizon. Reservation: branded-checkout share loss and margin compression are real and ongoing; the position is a bet that a 10x-ish multiple already discounts a turnaround that hasn't yet shown up in the numbers, not a bet that the turnaround is confirmed.

## 2. Business in plain English
PayPal operates a two-sided digital-payments network — merchants accept PayPal/Venmo/Braintree, consumers pay with them — monetizing via take-rate on payment volume, plus interest income on customer balances and lending. Its moat is network effects (more merchants → more consumers → more merchants) and stored-credential convenience, but that moat is eroding at the point of sale as Apple Pay, card-network click-to-pay, and embedded checkout reduce PayPal's branded-checkout advantage. New CEO Enrique Lores (since 2025) is running a stated "transformation" focused on branded-checkout stabilization, Venmo monetization and Braintree/financial-services diversification. (Source: 8-K EX-99.1, filed 2026-07-28, accession 0001633917-26-000080.)

## 3. Why the model likes it / is it durable?
Triage/b1 flags quality=4 (pct_roe 0.97, pct_bp 0.85 — cheap on book value, high ROE), growth=2, price_vs_growth=3. High ROE is partly an artefact of heavy buybacks shrinking the equity base, not purely organic profitability growth — flagged as a **data conflict**: quant ROE looks excellent, but TM$ (transaction margin dollars) growth has been low-single-digit and non-GAAP operating margin *contracted* 248bps YoY in Q2'26, i.e. the ROE strength is partly a capital-structure effect, not a widening moat.

## 4. Last two quarters (10-Q/8-K; GAAP unless labelled non-GAAP)
| Metric | Q2'26 (3mo to 6/30/26) | Q2'25 | Q1'26 (3mo to 3/31/26) | Q1'25 |
|---|---|---|---|---|
| Net revenue | $8.7bn (+5%; +3% FXN) | — | $8.4bn (+7%; +5% FXN) | — |
| Transaction margin $ (TM$, non-GAAP) | $3.9bn (+1%) | — | $3.8bn (+3%) | — |
| GAAP operating margin | 16.4% (−171bps YoY) | — | not separately quoted in extract | — |
| Non-GAAP operating margin | 17.4% (−248bps YoY) | — | — | — |
| GAAP diluted EPS | $1.25 (−3%) | — | $1.21 (−6%) | — |
| Non-GAAP diluted EPS | $1.38 (−1%) | — | $1.34 (+1%) | — |
| Total payment volume (TPV) | $486.4bn (+10%; +9% FXN) | — | $464.0bn (+11%; +8% FXN) | — |
| Active accounts | 439m (+0.3% YoY; −0.04% QoQ) | — | — | — |
| GAAP FCF | $1,775m | $692m | — | — |
| Cash flow from operations | $2.0bn | — | — | — |
Source: 8-K EX-99.1 press releases, 2Q'26 filed 2026-07-28 (accession 0001633917-26-000080) and 1Q'26 filed 2026-05-05 (accession 0001633917-26-000065). Revenue growth decelerated from +7% (Q1) to +5% (Q2); GAAP/non-GAAP EPS both declined YoY in both quarters despite double-digit TPV growth — a sign that take-rate/margin compression, not volume, is the swing factor.

## 5. Guidance track record (last two releases; company gives no formal >2-quarter numeric range beyond FY and next quarter)
- **1Q'26 release (filed 2026-05-05), "May 2026 Guidance"**: FY'26 non-GAAP EPS **"Low-single digit decline to slightly positive"** vs FY25 base $5.31; FY'26 GAAP EPS **"Mid-single digit decline"** vs FY25 base $5.41; 2Q'26 non-GAAP EPS guided **"High-single digit decline or approximately (-9%)"** vs 2Q'25 $1.40. (Quoted verbatim from the "Financial Guidance" table, EX-99.1.)
- **2Q'26 release (filed 2026-07-28), "July 2026 Guidance"**: **"PayPal is raising full year non-GAAP TM$ and EPS guidance and reaffirming GAAP EPS guidance."** FY'26 non-GAAP EPS raised to **"~$5.38"** (from the May range of low-single-digit decline to slightly positive off $5.31, i.e. an upward revision to a point estimate above the prior range's midpoint); FY'26 GAAP EPS guide **unchanged at "Mid-single digit decline"** vs $5.41. New 3Q'26 guide: GAAP EPS "Low-single digit decline," non-GAAP EPS "Low-single digit decline," both vs 3Q'25 base ($1.30 / $1.34).
- **Verdict: non-GAAP EPS guidance raised; GAAP EPS guidance maintained/reaffirmed.** This is a genuine improvement versus the prior range, not a case of "raised" being asserted without checking the prior number — both figures are quoted above.

## 6. Earnings quality & balance sheet
- GAAP vs non-GAAP EPS gap (~$0.13/share in Q2'26) driven mainly by amortization of acquired intangibles, stock-based comp, and restructuring/transformation charges — standard for PayPal, not a new adjustment.
- Cash flow: Q2'26 FCF $1,775m vs $692m in Q2'25 — a large favorable swing, but management flags it is affected by **"the net timing impact between originating buy now, pay later (BNPL) receivables as held for sale and the subsequent sale of those receivables,"** hence the separate "adjusted FCF" line ($1,832m Q2'26 vs $656m Q2'25). Treat the YoY FCF comparison as partly a BNPL-securitization-timing effect, not pure underlying cash generation improvement.
- Balance sheet: cash/investments $15.3bn vs debt $13.4bn as of 6/30/26 — net cash positive, consolidated basis (per EX-99.1 "Balance Sheet and Liquidity" bullets).
- Capital return: **"Returned $1.5 billion to stockholders by repurchasing approximately 33 million shares of common stock in 2Q'26"** — buybacks remain the primary EPS-growth lever while revenue growth decelerates; no dividend.
- No pending M&A disclosed in the two releases reviewed.

## 7. Valuation snapshot & reverse DCF
- Price used: $55.04 (2026-09-25 close, per b1_live_scores.csv); b1 data shows NTM-style metrics consistent with triage's cited "9.7x NTM P/E."
- On FY26 non-GAAP EPS guide (~$5.38): P/E ≈ **10.2x**.
- **v1_valuation_table.csv / v1_valuation.json have no row for PYPL** (`companies["PYPL"]` = null in v1_valuation.json). v1_verdict = null.
- Reverse DCF (perpetuity on FCF): FY26 adjusted FCF run-rate (H1'26 ≈ $1.83bn Q2 + a comparable Q1 print) annualizes to roughly $6–7bn; against a $48.6bn market cap that is a ~12–14% FCF yield. Using an equity cost of capital of 9.5%–10% (higher than a typical mega-cap given competitive/regulatory overhang), the Gordon-growth relationship (P = FCF·(1+g)/(r−g)) implies the market is pricing in **roughly flat-to-negative (0% to −3%/yr) perpetual FCF growth** — i.e., the market has essentially given up on PYPL growing, despite double-digit TPV growth and raised non-GAAP EPS guidance. **implied_vs_base = "below"** the company's own near-term trajectory (positive non-GAAP EPS revision, high-single-digit TPV growth), which is what makes this a turnaround-optionality trade rather than a pure re-rating call.
- Peers: Block (SQ), Fiserv (FI), Global Payments (GPN) trade at a range of multiples; PYPL is toward the cheap end of large-cap payments, consistent with the market pricing in continued share loss at branded checkout.

## 8. Bull case
1. Non-GAAP EPS guidance was just raised (to ~$5.38 from a range that could have been below $5.31), and management explicitly frames this as transformation progress, not one-off.
2. TPV growth remains double-digit (+10% Q2'26) even as active-account growth has stalled — showing existing users/merchants are transacting more, a base to monetize if branded-checkout share stabilizes.
3. Reverse DCF shows the market pricing in flat-to-negative FCF growth; any evidence the turnaround is working (Venmo monetization, Braintree profitability) is upside optionality not currently paid for.

## 9. Bear case / kill criteria (measurable)
1. **Active accounts decline on a QoQ basis for two consecutive quarters** (Q2'26 was already −0.04%/−0.2m QoQ — one quarter's worth of the trigger already logged; source: EX-99.1, 2026-07-28).
2. **Non-GAAP operating margin contracts for a third consecutive quarter** (was −248bps YoY in Q2'26, following contraction in Q2'25 comparisons cited in the same release).
3. **FY guidance is cut** (as opposed to raised/reaffirmed) in the next (3Q'26) release — would reverse the current positive guidance-revision trend.
4. **Net revenue growth decelerates below 3% YoY** for two consecutive quarters (was +5% in Q2'26, down from +7% in Q1'26 — already decelerating, so this is a near-term watch item, not a distant tail risk).
5. A material adverse ruling or new consent order tied to the CFPB's Venmo civil investigative demand (unauthorized funds transfers/collections practices) or an expansion of the 2026 DOJ minority-lending-fee-waiver settlement scope.

## 10. Catalysts & calendar
- Next earnings: Q3 2026 — **estimated late October 2026** based on prior-year cadence (Q2'26 was reported 2026-07-28, and 3Q'26 guidance was already given in that release, implying an Oct 2026 report); not independently confirmed against an official investor-relations calendar in this pass.
- Watch: any update on the CFPB Venmo civil investigative demand; further BNPL-receivables securitization activity (affects reported FCF comparability); holiday-quarter (Q4) branded-checkout share commentary.

## 11. Red-flag scan
- **DOJ settlement**: PayPal agreed (per press reporting, ~May 2026) to waive $30m in transaction fees to resolve a DOJ investigation alleging its 2020 $530m minority-owned-business support initiative disadvantaged non-minority-owned businesses in violation of federal anti-discrimination law in lending. (Secondary source — Gurufocus/press summary; I did not locate and read the underlying DOJ settlement document or an 8-K disclosing it in this pass, so this is flagged as **unverified against a primary source** and should be re-checked before being relied upon for a legal conclusion.)
- **CFPB civil investigative demand**: reported to be seeking documents on Venmo's "unauthorized funds transfers and collections processes" — again a secondary-source (Payments Dive) report; no primary CFPB order or PayPal 8-K/10-K risk-factor citation was opened in this pass.
- **Securities class action**: a federal securities-fraud class action covering purchasers between Feb 25, 2025 and Feb 2, 2026 alleging PayPal concealed that its sales/operations could not deliver on its targets — again sourced from plaintiffs'-firm summaries (Kessler Topaz, Levi & Korsinsky), not the underlying complaint or a PayPal 10-Q litigation footnote.
- **Data conflict**: none found between quant scores and filings beyond the ROE/buyback point noted in section 3.
- No auditor change, material weakness or going-concern language found in the documents actually opened (the two 8-K earnings releases).

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (three months ended 2026-06-30), per 8-K filed 2026-07-28 (accession 0001633917-26-000080); prior-quarter comparison from 8-K filed 2026-05-05 (accession 0001633917-26-000065). Events checked to 2026-09-25 via WebSearch for litigation/regulatory news — several items found but **not verified against primary sources in this pass** (see section 11); treat those as leads to confirm, not established facts. GAAP figures and non-GAAP figures are labelled throughout as given in the source releases. **Research only — not personal investment advice.**

## Sources
1. PayPal Holdings 8-K, Exhibit 99.1, "PayPal Reports Second Quarter 2026 Results," filed 2026-07-28, accession 0001633917-26-000080. https://www.sec.gov/Archives/edgar/data/1633917/000163391726000080/pypl2q-26earningsrelease.htm
2. PayPal Holdings 8-K, Exhibit 99.1, "PayPal Reports First Quarter 2026 Results," filed 2026-05-05, accession 0001633917-26-000065. https://www.sec.gov/Archives/edgar/data/1633917/000163391726000065/pypl1q-26earningsrelease.htm
3. SEC EDGAR filing index, PayPal Holdings CIK 0001633917. https://data.sec.gov/submissions/CIK0001633917.json
4. v4/data/b1_live_scores.csv (price, quant factor scores, as_of 2026-09-25).
5. WebSearch, "PayPal SEC investigation OR DOJ OR CFPB lawsuit 2026," retrieved 2026-09-27 (secondary sources: gurufocus.com, paymentsdive.com, ktmc.com, zlk.com — not independently verified against primary filings in this pass; flagged in section 11).
