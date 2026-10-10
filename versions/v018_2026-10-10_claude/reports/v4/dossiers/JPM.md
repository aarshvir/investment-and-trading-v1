# JPM — JPMorgan Chase & Co. (Agent F80, wave 5, standard depth)

## 1. Verdict
**INCLUDE-SMALL** — the best-run, best-capitalized US universal bank, but at ~$343 close (2026-09-25) the price already
sits near the top of its own valuation history, and the headline Q2 FY26 profit beat is materially inflated by one-time
gains that a careful reader must strip out. Reservation: size the position assuming ~13% adjusted EPS growth, not the
41% headline growth. Horizon 24–36 months.

## 2. Business in plain English
JPMorgan Chase is the largest US bank by assets, running four main businesses: consumer/community banking (Chase
branches, cards, mortgages), a corporate & investment bank (trading, underwriting, M&A advisory), commercial banking, and
asset & wealth management. It earns net interest income on its ~$2.7 trillion deposit base and loan book, plus fees from
trading, banking and wealth services. Its moat is scale (global balance sheet, technology spend, deposit franchise) and
Dimon-era risk-management discipline that let it out-earn peers through multiple cycles.

## 3. Why the model likes it / durability
b1_live_scores.csv (as_of 2026-09-25): roe 0.174 (pct 0.63), high composite decile 7/quintile 4, live_rank 197 — solidly
quality-and-momentum-driven, not a deep-value pick (bp/ep percentiles mid-range). The triage note called this "the
gold-standard diversified bank... best margins and returns in the group" [triage Q04]. That underlying quality (ROE, net
interest margin discipline, capital return capacity) is durable and structural. What is **not** durable is the specific
Q2 FY26 growth rate — see Section 4 — which is inflated by one-off items, an important distinction the triage's "7%
forward EPS growth, thin 9% street upside" framing did not have visibility into at the time.

## 4. Last several quarters — results (GAAP, consolidated JPMorgan Chase & Co.; $ in millions except EPS)
| Period | Revenue (net of interest exp.) | YoY | Net income | Diluted EPS | Source |
|---|---|---|---|---|---|
| Q2 2026 (Apr–Jun 2026) | $57,347 | **+27.7%** | $21,155 | $7.70 | 10-Q filed 2026-08-06 [1]; earnings release [2] |
| Q1 2026 (Jan–Mar 2026) | $49,836 | +10.0% (vs Q1'25 $45,310) | $16,494 | $5.94 | 10-Q filed 2026-05-01 [3] |
| FY2025 (full year) | $182,447 | — | $57,048 | $20.02 | 10-K filed 2026-02-13 [4] |
| Q2 2025 (Apr–Jun 2025) | $44,912 | — | $14,987 | $5.24 | 10-Q filed 2025-11-04 comparative [5] |
| Q1 2025 (Jan–Mar 2025) | $45,310 | — | $14,643 | $5.07 | 10-Q comparative [3] |

**Critical earnings-quality flag:** the Q2 2026 headline $21.2B net income / $7.70 EPS includes a **$4.6B net gain related
to Visa shares** (Corporate segment) and **$1.0B of gains on certain equity investments** ($763M Corporate, $263M CIB) —
$5.6B pre-tax / ~$4.2B after-tax of one-time items. **Excluding significant items, Q2 2026 net income was $16.9B and EPS
was $6.14**, i.e. adjusted net income grew ~13% YoY, not 41% [6]. Any reverse-DCF or growth extrapolation from Q2 2026
headline numbers overstates JPM's run-rate earnings power materially.

## 5. Guidance track record
JPMorgan does not give formal quarterly EPS/revenue guidance (large-bank convention); it gives NII and expense outlook
commentary on earnings calls. Management's 2026 net-interest-income and expense outlook commentary was not independently
re-verified against the prior-quarter figures in this pass — flagged as a limitation (data_conflicts) rather than
asserting a raise/cut that was not directly checked in the primary transcript.

## 6. Earnings quality & balance sheet (consolidated JPMorgan Chase & Co., not a subsidiary bank entity)
- **Capital:** Standardized CET1 ratio 14.1% at Q2 2026-end, down 20bp QoQ on higher RWA and capital distributions;
  Advanced CET1 ratio 14.2%; CET1 capital $303B [7]. Both figures are well above the ~11.5–12% regulatory requirement —
  ample buffer, consistent with the quality/durability framing in Section 3.
- **Deposits (consolidated):** $2.7137 trillion at 2026-06-30, up from $2.5593T at 2025-12-31 and $2.5485T at
  2025-09-30 [8] — deposit base still growing, a positive funding signal.
- **Credit quality:** Q2 2026 credit costs $2.5B, of which $2.4B net charge-offs and a $149M net reserve build; Card
  Services net charge-off rate 3.34% [7] — charge-offs are running at a level management itself frames as normalizing,
  not spiking; watch this rate (kill criterion #2).
- **Capital return:** Q2 2026 dividends $4.0B ($1.50/share) plus $6.2B of buybacks [7] — capital return continues at a
  healthy pace funded from (adjusted) earnings, not from the one-off gains.
- **Stockholders' equity (consolidated):** $374.598B at 2026-06-30, up from $362.438B at 2025-12-31 [8] — equity is
  climbing, partly mechanically from the AOCI/gain items in Section 4; do not read this quarter's equity build as pure
  organic retained-earnings growth without adjusting for the Visa/equity gains.
- **Litigation/regulatory (consolidated JPMorgan Chase & Co.):** multiple active class actions noted in 2025–26 filings
  and press coverage — alleged credit-card fee practices (filed Oct 2025), an alleged interest-rate-fixing conspiracy
  claim naming JPM among several banks (filed Oct 2025), an employment-discrimination suit (filed Dec 2025), and an
  ERISA/health-plan tobacco-surcharge claim (filed Jan 2026) [9]. None of these were independently confirmed against the
  10-Q's own "Legal Proceedings" note text in this pass (time-boxed); treat the specific claims as media-reported, not
  filing-verified, pending a closer read — flagged in data_conflicts.

## 7. Valuation — reconciliation with V1
`v1_valuation_table.csv`/`v1_valuation.json` contain **no row for JPM** — `v1_verdict = null`; no formal V1 reconciliation
possible.
- **Price/quant snapshot:** px $343.06 (2026-09-25), mktcap ~$911.9B [b1_live_scores.csv].
- **Multiples on adjusted (not headline) EPS:** using the $6.14 Q2-adjusted EPS annualized-run-rate proxy (~4x = $24.56,
  a rough proxy only, not a true annual number) against $343.06 gives a P/E in the ~14x area; on a trailing-4Q reported
  EPS basis ($5.07+$5.24+$7.70+ FY25 remainder — reported figures mix one-offs so this is directional only) the multiple
  is broadly similar, ~14–16x, in line with JPM's own recent history and modestly below the ~17–18x this cycle's peak.
- **Reverse-DCF sense:** for a mega-cap bank, ROE (~18% per triage) **[Corrected 2026-10-08: reported ROE was 24% in Q2 2026 (ROTCE 29%, 23% ex significant items)]** minus payout-adjusted growth is the cleaner lens than
  a pure FCF-yield DCF. At ~14–16x adjusted earnings and ~18% ROE, the price implies the market wants **mid-to-high
  single-digit sustainable EPS growth** (buybacks + modest NII/fee growth), which is *below* the unadjusted 41% headline
  and roughly *in line with* the adjusted ~13% Q2 print and the triage's own "7% forward EPS" estimate.
- **implied_vs_base:** "below" **[Corrected 2026-10-08: corrected to "in_line": on P/TBV-ROTCE the price (3.03x TBV) equals the justified multiple at ~21% sustained ROTCE, see Correction section]** — my base case (mid-to-high single-digit durable EPS growth from NII normalization, fee
  growth and buybacks, once one-off gains roll off) is at or slightly above what the ~14–16x adjusted multiple implies,
  i.e. the stock is not obviously overpriced on adjusted earnings even though the headline print looks extreme.

## 8. Bull case
1. CET1 14.1–14.2%, well capitalized, funding continued buybacks ($6.2B in Q2 alone) and dividends ($1.50/share) [7].
2. Deposit base still growing ($2.71T, +6% since 2025-12-31) [8], a scale advantage smaller banks cannot match.
3. Credit costs (3.34% card NCO rate) still at a manageable, not deteriorating, level this quarter [7].

## 9. Bear case
1. Q2 2026's 41% headline net-income growth and $7.70 EPS are ~40% inflated by one-off Visa-share and equity-investment
   gains; adjusted growth of ~13% is the real run rate — anyone anchoring valuation off the headline number is mispricing
   the stock [6].
2. CET1 ratio fell 20bp QoQ on higher RWA and distributions — capital buffer is trending down, not up, even as buybacks
   continue.
3. Active litigation across credit-card fees, alleged rate-fixing, employment discrimination and ERISA claims adds
   headline/legal-cost risk that was not independently filing-verified in this pass (see Section 6 caveat).

## 10. Key risks & kill criteria (measurable)
1. Standardized CET1 ratio falls below 13.0% (from 14.1% at Q2 2026) for two consecutive quarters.
2. Card Services net charge-off rate rises above 4.0% (from 3.34% at Q2 2026) for two consecutive quarters.
3. Adjusted (excluding-significant-items) EPS growth YoY turns negative for two consecutive quarters.
4. Any of the four active 2025–26 class actions results in a disclosed reserve/settlement exceeding $1B.
5. Deposit base (`Deposits`, consolidated XBRL) declines more than 5% from the 2026-06-30 level of $2.7137T over two
   consecutive quarters.

## 11. Catalysts & calendar
Next earnings: Q3 2026 results expected mid-October 2026 (prior-year cadence: Q3 2025 filed 2025-11-04 as a 10-Q;
earnings release typically precedes the 10-Q by ~2–3 weeks).

## 12. Red-flag scan
No auditor change, restatement or going-concern language identified. Multiple active class-action suits noted (Section
6/9) — media-reported, not independently confirmed against the 10-Q Legal Proceedings note text in this time-boxed pass;
this is itself flagged as a limitation, not a confirmed red flag. No Form 4 insider-selling pattern review completed in
this pass.

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q (period ended 2026-06-30), filed 2026-08-06 [1]. Events checked to
2026-09-25 close via SEC filings and news coverage through that date. GAAP figures are labelled; the $4.6B Visa gain and
$1.0B equity-investment gains are GAAP-included but explicitly flagged as one-off/non-recurring per management's own
"excluding significant items" framing [6] — this is the single most important adjusted-vs-GAAP distinction in this
dossier. Research, not personal investment advice.

## Sources
1. JPM 10-Q, period 2026-06-30, filed 2026-08-06, accession 0001628280-26-054343. https://www.sec.gov/Archives/edgar/data/0000019617/000162828026054343/jpm-20260630.htm
2. JPMorgan Chase 2Q26 earnings release/presentation. https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/2nd-quarter/6cded9fd-a164-4e6c-8cff-377357cf105c.pdf
3. JPM 10-Q, period 2026-03-31, filed 2026-05-01, accession 0001628280-26-029344.
4. JPM 10-K, FY2025, filed 2026-02-13, accession 0001628280-26-008131.
5. JPM 10-Q, period 2025-09-30, filed 2025-11-04, accession 0001628280-25-048859 (comparative prior-year Q2 figures).
6. Investing.com, "JPMorgan Q2 2026 presentation: broad strength drives 41% profit jump" (Visa gain, equity-investment
   gains, adjusted $16.9B/$6.14 EPS excluding significant items). https://www.investing.com/news/company-news/jpmorgan-q2-2026-presentation-broad-strength-drives-41-profit-jump-93CH-4791151
7. JPMorgan Chase Q2 2026 earnings highlights (CET1, capital return, credit costs). https://banksandbankers.com/jpmorgan-q2-2026-record-profit-trading-revenue/ ; https://www.valuethemarkets.com/news/jpmorgan-chase-nyse-jpm-reports-212b-q2-profit
8. SEC EDGAR XBRL companyfacts, CIK0000019617 (Deposits, StockholdersEquity), retrieved 2026-09-27. https://data.sec.gov/api/xbrl/companyfacts/CIK0000019617.json
9. AllAboutLawyer.com summary of active JPM class actions (Oct 2025–Jan 2026 filings) — media source, not independently
   filing-verified in this pass. https://allaboutlawyer.com/jpmorgan-jpm-lawsuit-multiple-class-actions-filed-over-credit-card-fraud-interest-rate-fixing-data-breaches-employment-discrimination-what-chase-customers-need-to-know/
10. b1_live_scores.csv, v4/data, as_of 2026-09-25 (internal quant snapshot).
11. v1_valuation_table.csv / v1_valuation.json, v4/outputs (checked; no JPM row).

## Correction (verification DV24, 2026-10-08)
**Scope:** checked against the 14 Jul 2026 8-K (Ex-99.1 narrative and Ex-99.2 supplement, acc 0001628280-26-048078), 10-Q acc 0001628280-26-054343 and companyfacts. Facts file: `outputs/dv/DV24_factcheck.json`. No verdict change.

**Result.** The earnings table, the Visa gain and equity gains, adjusted net income ($16.9B, $6.14), CET1 (14.1%/14.2%), deposits, equity, card net charge-off rate (3.34%) and capital return all match the release and 10-Q.

**Valuation method (FAIL).** The dossier values JPM with a P/E and an unsourced "ROE ~18% per triage" and asserts implied_vs_base = "below" without a calculation. Banks must be valued on P/TBV against ROTCE. From the release: tangible book value per share $113.35 and ROTCE 29% reported, 23% excluding significant items. At $343.06 P/TBV is 3.03x. Justified P/TBV = (ROTCE - g)/(Ke - g) with Ke 9.6% (5.17% 10-year Treasury on 25 Sep 2026 plus beta ~1.07 x 4.14% ERP; beta is an assumption) and g 4%: ROTCE 23% gives 3.39x ($384), 21% gives 3.04x ($344), 18% gives 2.50x ($283). The price therefore requires ROTCE of about 21% sustained, which equals the average of the last five quarters excluding one-offs (21, 20, 18, 23, 23). Corrected implied_vs_base: **in_line** (was below). Verdict INCLUDE-SMALL unchanged. F80_summary.json updated for implied_vs_base only.

**Minor.** Reported ROE was 24% (about 19% excluding the gains), not 18%. The trailing-EPS formula in s7 is garbled (trailing reported EPS is $23.34, giving 14.7x; ex-items $21.78, 15.8x). The four litigation items and the NII/expense outlook are not in the 10-Q or release text and remain unverified.
