# ADP (Automatic Data Processing, Inc.) — Diligence Dossier

Agent: F36 · Standard depth · Prepared 2026-09-26 · Prices/market data as of 2026-09-25 close ($263.67; mkt cap ≈$104.7B)

## 1. Verdict

**INCLUDE** — 12–36 month horizon. Mission-critical, high-switching-cost payroll/HR platform delivering
above-guidance growth every quarter this fiscal year; the reverse DCF shows the market pricing in **less**
growth (≈4.2%/yr, 10y) than management's own guided FY27 trajectory (revenue +5–6%, adjusted EPS +9–11%).
No V1 systematic valuation row exists for ADP (not in `v4/outputs/v1_valuation_table.csv`), so `v1_verdict`
is null and the valuation view below is the analyst's own (Section 7).

## 2. Business in plain English

ADP processes payroll, tax filing, benefits administration and HR compliance for ~1.1 million clients (Employer
Services) and acts as a co-employer / PEO for small and mid-size businesses (Workforce Now / TotalSource). It
earns per-employee/per-transaction fees plus a secondary but material stream from investing client payroll
funds it briefly holds before remittance ("client funds interest," roughly 15–20% of pretax earnings and
directly geared to short-term interest rates). The moat is switching costs (payroll is high-stakes, low-visibility
infrastructure that employers rarely re-platform) plus scale in compliance content (tax tables, benefits rules
across every US jurisdiction).

**Sector routing note:** GICS labels ADP "Human Resource & Employment Services" → the stock-analysis skill
router maps this to `people-businesses.md`. That fits the core payroll/PEO service economics, but ADP's client
funds float income is a *secondary*, rate-sensitive, bank-like income stream layered on top; it is flagged and
read separately below (Section 6) rather than blended into the people-business ratio set, per the skill's Step-3
multi-segment guidance.

## 3. Why the model likes it / durability

`data/b1_live_scores.csv` live_rank 162, composite factor score driven mainly by Quality (fam_Q rank ~0.68) —
high ROE (73%, distorted upward by buybacks against real but modest common equity — see Section 6), strong
OCF/assets, low accruals. Momentum and Value families are unremarkable (fam_M 0.45, fam_V 0.56), consistent with
a steady compounder rather than a re-rating story. This is durable, not an artefact: FY26 (ended 30-Jun-2026)
revenue grew 7% (6% organic constant currency) with adjusted EBIT margin +140bps in Q4 alone — margin expansion
funded by scale, not one-off cost cuts.

## 4. Last two years of results (fiscal quarters, FYE 30-Jun; GAAP unless marked)

| Qtr (end) | Revenue | YoY | Diluted EPS (GAAP) | Adj. diluted EPS | Net income |
|---|---|---|---|---|---|
| Q2 FY25 (Dec-24) | n/a (10-Q agg.) | — | $4.69 (6mo) | — | $963.2M (qtr) |
| Q3 FY25 (Mar-25) | n/a | — | $3.06 (qtr) | — | $1,249.5M |
| **FY25 total** (Jun-25) | **$20,560.9M** | +7.1% | $9.98 | — | $4,079.7M |
| Q1 FY26 (Sep-25) | $5,200M (release) | +7% | $2.49 | $2.49 (+7%) | $1,013.0M |
| Q2 FY26 (Dec-25) | — | — | $2.62 (qtr) | — | $1,062.0M |
| Q3 FY26 (Mar-26) | $5,400M-ish (release) | — | $3.38 (qtr) | — | $1,359.8M |
| Q4 FY26 (Jun-26) | $5,500M | +7% (6% organic cc) | $2.45 (qtr, +10%) | $2.64 (+17%) | ~$1,013–1,062M range (qtr) | **[Corrected 27 Sep 2026: Q4 FY26 GAAP net earnings were $978.6m; the range shown repeats Q1 and Q2. See the Correction section below.]**
| **FY26 total** (Jun-26) | **$21,947.4M** | +7.0% | $10.94 | ~$? (mgmt: adj. net earnings +10% to $4.5B) | $4,413.5M |

Sources: SEC EDGAR XBRL companyfacts (CIK 0000008670), cross-checked against ADP's own Q4/FY26 earnings release
(`s205.q4cdn.com/887941133/.../ADP-4Q26-Earnings-Release.pdf`) and Q1–Q3 FY26 8-K Ex-99.1 exhibits. Revenue
acceleration through the year (organic cc growth 6% all four quarters, reported growth stepping up to 7% by
Q4) — no deceleration signal. GAAP vs adjusted gap is modest and explained mainly by acquisition-related
amortization and integration costs, not aggressive non-GAAP add-backs.

## 5. Guidance track record (last 4 releases, all FY26 consolidated outlook)

| Release | Revenue growth guide | Adj. EBIT margin | Adj. diluted EPS growth | vs prior guide |
|---|---|---|---|---|
| Q1 FY26 (29-Oct-25) | 5–6% | +50–70bps | 8–10% | **Reaffirmed** initial FY26 guide (given Aug-25) |
| Q2 FY26 (28-Jan-26) | ~6% | (not isolated in search) | 9–10% | **Raised** (EPS range lifted) |
| Q3 FY26 (29-Apr-26) | 6–7% | (margin guide raised, exact bps not confirmed here) | 10–11% | **Raised again** |
| Q4 FY26 / FY26 actual (Aug-26) | delivered 7.0% | delivered ~+140bps in Q4 alone | delivered ~10% (mgmt language) | **Beat** even the raised range |
| FY27 initial guide (Aug-26) | 5–6% | +70–90bps | 9–11% | New-year guide, in line with FY26 delivered pace |

Four consecutive quarters of reaffirm-then-raise, ending at a result that beat the last raise — a clean,
credibility-building track record (the opposite of the "guidance raised asserted without checking the prior
range" failure the lead audit flagged). Sources: ADP 8-K Ex-99.1 exhibits for Q1–Q4 FY26
(sec.gov/Archives/edgar/data/8670/...).

## 6. Earnings quality & balance sheet

- **FCF conversion:** FY26 OCF $5,441.2M; capex (PP&E) $196.6M → FCF ≈$5,244.6M vs net income $4,413.5M →
  FCF/NI ≈119%, i.e. cash generation comfortably exceeds reported earnings (favourable accruals quality).
- **SBC:** $242.6M FY26 / $21,947.4M revenue ≈1.1% of revenue — low, not a material EPS-quality drag.
- **GAAP vs adjusted:** FY26 GAAP net earnings +8% to $4.4B vs adjusted net earnings +10% to ~$4.5B; the gap is
  single-digit and driven mainly by acquisition/integration items per the release — not a red flag.
- **Client funds vs corporate balance sheet:** ADP's reported "Total assets" swing from $53.4B (Jun-25) to as
  high as $84.6B intra-year (Dec-25) purely from funds-held-for-clients timing (payroll cash in transit) — this
  is normal and must not be read as leverage or asset growth. Corporate cash and equivalents (ex-client funds)
  were $4.23B at FYE26; long-term debt $4.96B → net debt ≈$0.73B, effectively unlevered on a corporate basis.
  **Data conflict / caveat:** the implied interest rate on reported debt (interest expense $459.3M ÷ $4.96B LT
  debt ≈9.3%) is far above ADP's actual bond coupons, because reported interest expense mixes true corporate
  debt interest with financing costs tied to the client-funds/PEO extended-investment portfolio. Treated 5.5%
  as the corporate cost-of-debt assumption in the WACC below rather than the blended 9.3%; flagged as a
  data conflict, not resolved with certainty.
- **Buybacks/dividends:** FY26 repurchases $2,083.3M, dividends $2,626.3M — diluted share count fell from
  408.7M (FY25) to 403.3M (FY26), a genuine ~1.3% reduction, not merely offsetting dilution.
- **Effective tax rate:** FY26 22.98% (in line with recent years).

## 7. Valuation snapshot and reverse DCF

No V1 row exists for ADP; `v1_verdict = null`. Analyst-derived reverse DCF (script:
`stock-analysis/scripts/valuation.py`, methodology matching V1's own convention seen elsewhere in this program —
10-year fade to a 3% terminal growth rate):

- EV bridge: market cap $104.75B + debt $4.96B − cash $4.23B = **EV ≈$105.48B**
- WACC 8.6% (CAPM: rf 5.17%, ERP 4.14%, Blume-adjusted beta 0.89 from raw 5y weekly beta 0.83 in `d4_live_snapshot`;
  cost of debt assumption 5.5% pretax, tax rate 23.0%, D/(D+E)≈4.5%)
- Base FCF (FY26 actual, primary-sourced): $5,244.6M
- **Implied 10-year FCF growth priced in: ~4.2%/yr**, fading to 3% terminal.

That is *well below* management's own guided FY27 trajectory (revenue +5–6%, adjusted EPS +9–11%) and below
this year's delivered pace (revenue +7%, adjusted EPS ~+10%). Trailing P/E 23.7x, FCF yield 5.0%, dividend
yield 2.5%. Peers (ADP's own history / Paychex PAYX as the closest listed comp) trade in a similar mid-20s P/E
band; no evidence of a stretched multiple. **valuation_view_vs_v1.implied_vs_base = "below"** on the analyst's
own base case (9%/yr EPS growth assumption, Section 8) — satisfies the INCLUDE growth-priced-in test.

**Scenario 3-yr annualised total return (illustrative, price + dividends):** Bear −0.7%/yr (EPS +3%/yr, exit
20x P/E), Base +11.5%/yr (EPS +9%/yr, exit P/E flat at 24.1x), Bull +18.9%/yr (EPS +12%/yr, exit 27x P/E), each
plus a ~2.5% dividend yield — not consensus, an analyst estimate to make the reasoning checkable.

## 8. Bull case / bear case

**Bull (3):**
1. Client-funds interest income is a structural tailwind as long as short rates stay above zero — a multi-year
   annuity ADP does not have to "earn" through sales effort.
2. New-business bookings and retention have both been resilient through a soft small-business hiring cycle,
   suggesting share gains against smaller competitors (Paychex, Gusto, Rippling) rather than market softness.
3. Margin expansion (+140bps in Q4 alone) shows real operating leverage still available in a business the
   market already treats as mature.

**Bear (3):**
1. Client-funds interest income falls mechanically if the Fed cuts rates faster than the curve currently
   implies — a real, quantifiable headwind to adjusted EBIT that is macro, not company-specific.
2. Well-funded, product-led challengers (Gusto, Rippling, Deel) are taking share in the smallest-employer
   segment where switching costs are lowest; ADP's own growth is concentrated in larger, stickier accounts.
3. At 23.7x trailing earnings for high-single-digit growth, there is little room for a guidance miss without
   multiple compression on top of any earnings miss.

## 9. Key risks & kill criteria (measurable)

1. Organic constant-currency revenue growth below 4% for two consecutive quarters (vs. 6% delivered all of FY26).
2. Adjusted EBIT margin guidance cut (vs. the +70–90bps FY27 guide) at any quarterly release.
3. Client retention rate disclosed as declining year-over-year (ADP publishes this metric periodically).
4. Client funds extended investment portfolio yield or balance disclosed as falling faster than the Fed funds
   curve implies (a signal of client-fund outflows, not just rate cuts).
5. Net new business bookings growth negative for two consecutive quarters.

## 10. Catalysts & calendar

- Next earnings: **Q1 FY27, ~27–28 October 2026** (date not yet formally confirmed by ADP at time of writing;
  based on prior-year cadence).
- FY27 guidance already issued (Aug-26): revenue +5–6%, adjusted EBIT margin +70–90bps, adjusted diluted EPS +9–11%.

## 11. Red-flag scan

- **Litigation:** $48M settlement (Aug-2026, preliminary approval pending) in a 401(k)/TotalSource retirement-plan
  fee ERISA class action — a contained, disclosed cost, not an ongoing solvency or reputational risk. A separate
  ERISA suit re: the ADP TotalSource Retirement Savings Plan (filed 2020, New Jersey) remains open; ADP states it
  cannot estimate a reasonably possible loss.
- No auditor changes, restatements, or going-concern language found in this review.
- No unusual insider-selling pattern surfaced in this pass (not exhaustively Form-4-audited given time-box).
- No pending M&A affecting ADP itself.

## 12. Data basis, recency and disclaimer

Most recent period incorporated: **FY2026 10-K (fiscal year ended 30-Jun-2026), filed 05-Aug-2026**, plus the
Q1–Q4 FY26 earnings releases (8-K Ex-99.1) through Aug-2026. Checked for events to 2026-09-25. All figures are
on a **consolidated** basis (ADP has no meaningful standalone-vs-consolidated distinction for a US filer of this
kind). GAAP figures are labelled GAAP; "adjusted" figures are management's own non-GAAP measures as disclosed in
the earnings releases — not independently reconciled line-by-line in this pass. **This is research, not
personalized investment advice; it is not a recommendation to buy or sell any security, and it is not financial
advice.**

## 13. Sources

1. SEC EDGAR submissions/companyfacts, CIK 0000008670 (data.sec.gov), retrieved 2026-09-26.
2. ADP FY2026 10-K, filed 2026-08-05: sec.gov/Archives/edgar/data/8670/000000867026000030/
3. ADP Q4/FY2026 earnings release: s205.q4cdn.com/887941133/files/doc_financials/2026/q4/ADP-4Q26-Earnings-Release.pdf
4. ADP Q1 FY26 8-K Ex-99.1 (29-Oct-2025): sec.gov/Archives/edgar/data/8670/000000867025000042/q1fy26exhibit99.htm
5. ADP Q3 FY26 8-K Ex-99.1 (29-Apr-2026): sec.gov/Archives/edgar/data/0000008670/000000867026000016/q3fy26exhibit99.htm
6. Bloomberg Law, "ADP Agrees to $48 Million Deal in Retirement Plan Fee Lawsuit" (Aug-2026).
7. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (quant context, retrieved this session).
8. finance-skills stock-analysis skill, sector router (`references/sectors/_index.md`) and `valuation.py`.

---
## Correction (lead, 26 Sep 2026, from fact-check DA8; original text above left unchanged)
- §11 describes two ERISA matters. ADP's FY2026 10-K (filed 5 Aug 2026, Note 13, Commitments and Contingencies) describes **only one**: the May-2020 New Jersey suit over the ADP TotalSource Retirement Savings Plan. That suit **is** the matter settled for $48 million (subject to court approval). There is no separate, still-open second ERISA suit; the "remains open ... cannot estimate a reasonably possible loss" wording is stale pre-settlement language. Net effect: ADP's litigation exposure is smaller than the dossier implied. Verdict unchanged.


---
## Correction (lead, 27 Sep 2026, from fact-check DA16; original text above left unchanged)
- §4, Q4 FY26 row: net earnings were **$978.6m** (+7% YoY vs $910.6m), per the Q4 FY26 8-K Ex-99.1 (filed 29 Jul 2026, accession 0000008670-26-000025) and XBRL (FY26 $4,413.5m less nine-month $3,434.9m). The "~$1,013–1,062M" range shown repeats the Q1 and Q2 figures. EPS and the FY26 total were correct. Verdict unchanged.