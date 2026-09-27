# BAC — Bank of America Corporation (NYSE: BAC)

## 1. Verdict
**INCLUDE-SMALL** (half weight) — 24–36 month horizon. Second-largest US bank, delivering accelerating YoY EPS growth (+18% Q4-25 → +25% Q1-26 → +34% Q2-26) on higher net interest income, improving efficiency and low, falling credit costs, all while returning ~$8B/quarter to shareholders. Reservation, and the reason this is not a full-weight INCLUDE: price/book is at a 15-year-plus high (94th own-history percentile) and credit costs are unusually low in the cycle — the systematic valuation model (V1) independently flags the stock as "excessive." I partly disagree with V1's magnitude (see §7) but not its direction, so size is capped at half weight pending either a pullback in P/B or further evidence the current ROE level is durable through a full credit cycle.

## 2. Business in plain English
Bank of America is the second-largest US bank by assets, with four main businesses: Consumer Banking (deposits, cards, small-business lending — #1 in US consumer deposits), Global Wealth & Investment Management (Merrill, Private Bank), Global Banking (corporate/commercial lending and investment banking) and Global Markets (sales & trading). It makes money on the spread between what it pays depositors and earns on loans/securities (net interest income, ~50% of revenue) plus fees (wealth management, trading, investment banking). Competitive position: one of four "too big to fail" US universal banks (with JPMorgan, Citi, Wells Fargo), with the largest low-cost deposit base as its structural advantage.

## 3. Why the model likes it — durable or artefact?
b1_live_scores.csv (25 Sep 2026): live_rank 19/~500, composite decile 10 (top decile), quality (fam_Q) and value (fam_V) factor scores both strong. This ranks BAC as one of the most attractive names in the whole triage batch. Cross-checking against the primary filings, the strong quant read is **substantially confirmed** by real operating momentum, not just a cheap multiple: NII, revenue and EPS have all been growing and *accelerating* YoY for at least three straight quarters (see §4), and the efficiency ratio has improved from 63% (2Q25) to 59% (2Q26). The one place the quant read and the systematic valuation model disagree with each other is P/B: BAC's P/B is at a 15-year-plus high (V1: 94.35th own-history percentile) even though the b1 value factor score treats it as statistically cheap versus the market on other measures (P/E, FCF yield) — a genuine internal tension addressed in §7.

## 4. Last quarters — results table (GAAP, consolidated; all $ figures in US dollars, billions unless per-share)
Source for every cell in this table: BAC 8-K Ex-99.1 earnings press releases, as filed with SEC EDGAR (accession numbers and URLs in §Sources below; one release per quarter shown).

| Quarter | Net income | Diluted EPS | YoY EPS | Revenue (net of interest exp.) | YoY rev. | NII (FTE) | Efficiency ratio | Net charge-off ratio | CET1 (Standardized) |
|---|---|---|---|---|---|---|---|---|---|
| 3Q25 | $8.5B | $1.06 | — | $28.1B | +11% | $15.4B | — | 0.58% | 11.6% |
| 4Q25 | $7.6B | $0.98 | +18% | $28.4B | +7% | $15.9B | 61% | 0.54% | 11.4%(→11.5% restated basis per 2Q26 table) |
| 1Q26 | $8.6B | $1.11 | +25% | $30.3B | +7% | $15.9B | 61% | 0.48% | 11.2% |
| 2Q26 | $9.1B | $1.21 | +34% | $31.6B | +15% | $16.2B | 59% | 0.47% | 11.2% |

FY2025 full-year net income: $30.5B (company-stated headline). Sequential (QoQ) growth in 2Q26 was boosted by Global Markets (sales & trading revenue +33% YoY, 17th consecutive quarter of YoY growth) and GWIM (asset-management fees +19% YoY on higher market valuations) alongside the core NII tailwind — i.e., growth is broad-based across segments, not a single-line artefact.

## 5. Guidance track record
Banks generally do not give point EPS guidance; BAC instead frames forward NII/expense expectations qualitatively on earnings calls (not fully captured in the Ex-99.1 press releases reviewed here — a coverage gap, flagged). Each of the four reviewed releases described NII as growing YoY (+9% in 1Q26 and 2Q26, +10% in 4Q25) "driven by higher loan and deposit balances and fixed-rate asset repricing, partially offset by the impact of lower interest rates" — a consistent narrative across quarters, not a reversal. No formal raise/cut table is applicable in the addendum sense.

## 6. Earnings quality & balance sheet (bank-appropriate metrics)
- **CET1 (Standardized):** 11.2% at 2Q26, down from 11.6% a year earlier — capital ratio has been drawn down modestly to fund $8.0B of shareholder returns in 2Q26 alone (buybacks + dividends), while still "well above the regulatory minimum" (company's words).
- **Credit quality:** net charge-off ratio improved steadily from 0.58% (3Q25) to 0.47% (2Q26); nonperforming loans ratio ~0.47–0.52% and provisions have been trending down or flat — credit costs are benign, arguably unusually so for this point in a rate cycle (a risk noted in §8/§9, not a red flag on its own).
- **ROE:** return on average common shareholders' equity improved from ~11.0% (implied, 4Q25) to 12.0% (1Q26) to 12.7% (2Q26) — an accelerating trend, not a static number.
- **GAAP vs adjusted:** figures above are GAAP except NII (FTE) and efficiency ratio, which are standard fully-taxable-equivalent bank convention, clearly labelled by the company; no aggressive non-GAAP adjustment identified.
- No pending M&A or major litigation disclosed in the reviewed press releases.

## 7. Valuation — V1 reconciliation (required)
**V1 systematic valuation (outputs/v1_valuation.json, v1_valuation_table.csv), method = justified P/B = (ROE−g)/(COE−g):**
- Price used: $56.70 (25-Sep-2026). P/B: 1.374x, at the **94.35th percentile of its own 15-year (177-month) history** — i.e., BAC has rarely been this expensive on book value.
- COE 9.58% (beta 1.06, rf 5.17%, ERP 4.14%); implied ROE priced in: 12.03%; delivered TTM ROE: 11.18%; historical (15-yr) ROE 20th/50th/80th percentile: 4.25% / 7.96% / 10.33%.
- Scenarios: **bear** −16.4%/yr (ROE reverts to 15-yr 20th pctile 4.25%), **base** −1.9%/yr (ROE reverts to 15-yr median 7.96%), **bull** +11.7%/yr (ROE holds near 15-yr 80th pctile 10.33%).
- V1 verdict: **"excessive"** (score −0.67), driven mainly by the P/B percentile term and the negative base-case return vs. the 9.58% hurdle rate; sanity check: base 3-yr value ($53.56/sh incl. dividends) sits below the Street's 12-month low target ($62).

**Do I agree?** Partly. I agree with the *direction* — P/B at a 15-year-plus high is a real and fair caution, and I would not call this stock cheap. I disagree with the *magnitude* of V1's base case, because its base-case ROE assumption (7.96%, the 15-year median) is anchored heavily to the 2011–2021 near-zero-rate decade, when the whole US bank sector's ROE was structurally depressed — not obviously the right "base" for the next 3 years given the primary-source evidence in §4 that BAC's own ROE has been *rising*, not falling, for at least three consecutive quarters (11.0% → 12.0% → 12.7%). If I instead assume ROE holds near its current ~12% run-rate as the base case, the same P/B formula implies a fair P/B of roughly (0.12−0.03)/(0.0958−0.03) ≈ 1.37x — almost exactly today's multiple — which would put the base-case return closer to the dividend yield plus modest per-share book-value growth (roughly low-single-digits, still below the 9.58% cost-of-equity hurdle, but nowhere near V1's −1.9%). Reconciliation: **both readings agree BAC is fully priced, not undervalued** — the disagreement is only about how far above fair value it sits, and I lean less negative than V1 because the ROE trend is the opposite of what V1's mean-reversion assumption implies.
- `v1_verdict`: "excessive"; `v1_base_3y`: −0.0188 (−1.9%/yr); `dossier_view`: "full"; `consistent`: **false** (I agree on direction/richness, disagree on the size of the gap); reconciliation as above.
- **Implied vs. my own base case:** using my adjusted ~12% ROE base case against the ~12.03% ROE the market is implicitly paying for, implied is **"in_line"** — not clearly cheap, which is why this is INCLUDE-SMALL rather than a full-weight INCLUDE, and not clearly overpriced enough on fundamentals alone to be a REJECT (V1's harsher framing would push toward WATCH/REJECT; I land one notch more constructive given the accelerating ROE evidence).

## 8. Bull case / Bear case
**Bull (3 points):**
1. EPS growth has accelerated for three straight quarters (+18% → +25% → +34% YoY) on broad-based segment strength (Global Markets' 17th consecutive quarter of YoY sales & trading growth; GWIM AUM +17%), not a single one-off item.
2. Efficiency ratio improving (63%→59% YoY) and net charge-offs falling (0.58%→0.47%) simultaneously — operating leverage and credit quality are moving the same direction.
3. CET1 of 11.2%, still comfortably above requirement, supports continued large capital returns (~$8B/quarter) even as the ratio normalizes down from a post-stress-test peak.

**Bear (3 points):**
1. P/B at a 15-year-plus high (94th percentile) — even V1's own bull case (+11.7%/yr) requires ROE to sustain near a 15-year 80th-percentile level; this is priced for continued strength, not a business trading at a margin of safety.
2. Credit costs (0.47% net charge-off ratio) are low in absolute and historical terms; a turn in consumer or commercial credit (which the model has no way to time) would hit both NCOs and CET1 simultaneously.
3. Much of the recent NII acceleration is explicitly attributed to "fixed-rate asset repricing" (i.e., a one-time structural tailwind from replacing low-yielding legacy securities/loans) — once that repricing cycle completes, NII growth should mechanically decelerate even without a rate cut.

## 9. Key risks & kill criteria (measurable)
1. Net charge-off ratio rises above 0.65% for two consecutive quarters (vs. 0.47% now).
2. CET1 (Standardized) falls below 10.5% (vs. 11.2% now) without a clearly stated, temporary reason.
3. YoY EPS growth turns negative for any quarter (from the current +18%/+25%/+34% accelerating trend) absent a one-off/non-repeating item.
4. NII growth decelerates to flat-or-negative YoY for two consecutive quarters (from +9–10% now), signalling the fixed-rate-asset-repricing tailwind has fully played out.
5. P/B rises further into a new multi-year high (>1.45x) without a corresponding rise in delivered ROE above ~12.5%, widening the gap V1 already flags.

## 10. Catalysts & calendar
- Next earnings: **Q3 2026 — estimated mid-October 2026** (historical pattern: 15-Oct-2025 for 3Q25, 14-Jan/14-Apr/14-Jul-2026 for the three most recent quarters; not yet confirmed by an IR calendar posting as of 26-Sep-2026 — treat as an estimate, likely ~14-Oct-2026).
- Federal Reserve rate-path decisions remain the single largest swing factor for NII given BAC's asset-sensitive balance sheet (explicitly cited each quarter as a partial offset).
- Annual CCAR/stress-test results (typically released by the Fed each June) drive next year's buyback/dividend capacity — none due before the next earnings date.

## 11. Red-flag scan
- No auditor change, restatement, or going-concern language identified in the reviewed press releases.
- No SEC/DOJ investigation or material litigation disclosed in the documents reviewed (a full 10-K/10-Q litigation-note read was **not** completed in this standard-depth pass — flagged as a coverage gap).
- A data conflict already logged by V1 itself: D3 TTM revenue ($121.1B) vs. Yahoo TTM revenue ($113.9B) differ by 5.9%, and the D3 figure implies an implausible >100% EBIT margin — V1 substituted the Yahoo TTM revenue figure for its reverse-DCF; I did not independently resolve this vendor discrepancy but flag it as inherited, not re-verified.
- Form 4 insider-selling pattern was **not** reviewed in this pass — flagged as a coverage gap.

## 12. Data basis, recency and disclaimer
All figures are in US dollars ($), reported on a **consolidated** basis (Bank of America Corporation, not a standalone bank-only entity), and are in billions unless a per-share or percentage/ratio figure is stated. Most recent period incorporated: 2Q26 (period ended 30 Jun 2026), 10-Q filed 31 Jul 2026 and earnings press release (Ex-99.1) furnished 14 Jul 2026. Checked for events to 25 Sep 2026 close. GAAP figures throughout except NII (FTE) and efficiency ratio, which are standard bank fully-taxable-equivalent conventions, clearly labelled. This is research, not personalized investment advice, and not a recommendation to buy or sell; consult a licensed financial adviser before acting.

## Sources
1. SEC EDGAR submissions: https://data.sec.gov/submissions/CIK0000070858.json (retrieved 26 Sep 2026)
2. 8-K Ex-99.1 earnings releases: 2Q26 (14 Jul 2026, accession 0000070858-26-000353); 1Q26 (15 Apr 2026, 0000070858-26-000222); 4Q25/FY25 (14 Jan 2026, 0000070858-26-000020); 3Q25 (15 Oct 2025, 0000070858-25-000390) — all https://www.sec.gov/Archives/edgar/data/70858/...
3. v4/outputs/v1_valuation.json and v4/outputs/v1_valuation_table.csv (BAC row) — systematic valuation model, read in full per addendum requirement
4. v4/outputs/Q04_triage.json (triage note on BAC)
5. v4/data/b1_live_scores.csv (25 Sep 2026 factor snapshot)
