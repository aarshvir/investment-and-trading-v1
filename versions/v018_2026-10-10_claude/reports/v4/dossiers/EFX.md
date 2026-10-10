# Equifax Inc. (EFX) — Diligence Dossier

**Agent:** F64 | **As of:** 2026-09-25 close ($148.11, `d4_live_snapshot.parquet`) | **Depth:** Standard

## 1. Verdict
**INCLUDE-SMALL** (24–36 month horizon), with a specific, named reservation: an open CFPB investigation into
data accuracy and dispute handling at Workforce Solutions — the business unit that houses the Work Number
database, Equifax's single most important competitive moat — has been running since July 2023 with three
civil investigative demands through August 2024 and no disclosed resolution as of the 2026-07-21 10-Q.
Fundamentals are reaccelerating (revenue growth +3.8% → +14.3% YoY over the last six quarters), the company has
beaten its own quarterly guidance in every recent quarter, and this dossier's own reverse DCF shows the price
implies materially less growth than the evidence-based base case — genuinely cheap — but the regulatory
overhang on the core data asset, plus two other open legal matters, keeps this from being a full-weight
INCLUDE.

## 2. Business in plain English
Equifax is one of three major U.S. consumer credit bureaus (with Experian and TransUnion), selling credit
reports and scores to lenders (USIS segment) and, through its **Workforce Solutions** segment, operating "The
Work Number" — a database of payroll/employment records sourced from employer payroll systems — which lenders,
employers and government agencies use to instantly verify income and employment for mortgages, auto loans,
background checks and benefits eligibility. Workforce Solutions is the higher-margin, harder-to-replicate
asset (44.9% segment operating margin in 2Q26) because building an equivalent payroll-data network from
scratch is extremely difficult; USIS is the more commoditized, more mortgage-cyclical bureau business.

## 3. Why the model likes it — durable or artefact?
Triage (Q10) called margin and momentum "depressed by the weak mortgage-origination/hiring cycle, not any
structural loss of moat," at 15.2x NTM P/E. **Independently confirmed and refined from XBRL**: quarterly
revenue YoY growth has *accelerated* over the last six quarters — Q1 2025 +3.8%, Q2 2025 +7.4%, Q3 2025 +7.2%,
Q4 2025 +9.2%, Q1 2026 +14.3%, Q2 2026 +10.6% (own calculation, differencing 10-Q/10-K XBRL revenue figures) —
so the "depressed" framing is becoming dated; growth is clearly re-accelerating, not merely stable. Operating
margins (17–20% consolidated over the same period) remain below Equifax's stronger historical cycles, so there
is real margin-recovery optionality if mortgage volumes normalize. `b1_live_scores.csv`, however, shows a much
weaker quant picture than the fundamentals suggest: composite decile **3/10**, live_rank **394**, 12-1 month
price momentum **−25.4%** (percentile 3.8%, i.e. among the worst in the universe) and SUE percentile only
16.7% despite EFX beating guidance every recent quarter (`d4`: 8 beats, 0 misses in the last 8 reported
quarters, avg surprise +4.3%) — a genuine **data conflict** between weak price momentum/quant scores and
strong, accelerating, primary-source fundamentals. This gap is most consistent with the market pricing in the
open legal/regulatory overhang (§11) and macro mortgage-cycle uncertainty, not a fundamental problem.

## 4. Last eight quarters, GAAP (SEC 10-Q/10-K, XBRL `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax`
/ `OperatingIncomeLoss` / `EarningsPerShareDiluted`, consolidated; calendar fiscal year)

| Quarter | Revenue ($M) | YoY | Op. margin (GAAP) | Diluted EPS (GAAP) | Adjusted EPS |
|---|---|---|---|---|---|
| 1Q 2025 | 1,442.0 | +3.8% | 16.3% | $1.06 | n/a (not pulled) |
| 2Q 2025 | 1,537.0 | +7.4% | 20.2% | $1.53 | n/a |
| 3Q 2025 | 1,544.9 | +7.2% | 17.1% | $1.29 | n/a |
| 4Q 2025* | 1,550.6* | +9.2%* | — | — | n/a |
| 1Q 2026 | 1,648.9 | +14.3% | 17.4% | $1.42 | n/a |
| 2Q 2026 | 1,700.1 | +10.6% | 18.5% | $1.54 | **$2.25** (+13% YoY) |
| **FY 2025 total** | **6,074.5** | **+7.0%** | — | — | — |

\* 4Q 2025 derived (FY2025 total minus the sum of the three 10-Qs; not separately confirmed by a discrete
XBRL tag). TTM (3Q25–2Q26) operating cash flow **$1.612bn**, capex **$0.507bn**, TTM FCF **$1.105bn** (own
calculation, differencing YTD cumulative cash-flow XBRL figures since Equifax's 10-Qs report cash flow on a
year-to-date basis only, not discretely by quarter). Segment detail (2Q26 10-Q): Workforce Solutions revenue
+7% YoY (Verification Services +7%, within which Government +double-digit; Employer Services +3%); USIS
"delivered strong revenue growth of 21% [Q1 2026]... well above their 6-to-8% Long-Term Financial Framework,"
per management's own characterization, driven by a temporary U.S. Mortgage revenue spike (+38% in Q1 2026,
before rates rose after the disclosed "Iran conflict").

## 5. Guidance track record (last 3 releases, quoted from 8-K Exhibit 99.1 press releases)
- **4Q 2025 release (2026-02-04):** issued initial FY2026 guidance: revenue midpoint **$6.72bn** (~+10.5%
  reported), organic constant-currency growth ~10%, Adjusted EPS midpoint **$8.50** (+11% YoY), Adjusted
  EBITDA midpoint $2.12bn (+10%); Q4 2025 itself beat guidance by $30M above the midpoint. Assumes U.S.
  mortgage market down low-single-digits in 2026.
- **1Q 2026 release (2026-04-21):** Q1 2026 revenue **$1.649bn, $37M above the midpoint** of the February
  guidance (a real beat). Management explicitly **maintained** (did not raise) full-year local-currency
  growth guidance "due to the reduction in U.S. mortgage activity from higher rates since the Iran conflict...
  and the uncertainty in the global macroeconomic environment" — only a small, FX-driven technical increase
  to the reported-revenue and EPS ranges (+$25M revenue, +$0.04 EPS). A genuinely conservative management
  response to a beat, not a "raise on every beat" pattern.
- **2Q 2026 release (2026-07-21):** FY2026 guidance updated to revenue **$6.710–6.780bn**, Adjusted EPS
  **$8.39–8.69** — essentially the same midpoint as the prior update (narrowed range, not a fresh raise).
  Q3 2026 guide: revenue $1.680–1.710bn (+8.7–10.7%).
- **Net:** Equifax has beaten its own quarterly guidance in every recent release but has held its full-year
  guidance broadly flat rather than chasing the beats upward, citing mortgage-market and macro uncertainty —
  a **conservative, "beat-but-hold" pattern**, the opposite of CRM/CSCO's more aggressive raises in this
  batch. This is a credible, disciplined guidance style, not a red flag.

## 6. Earnings quality & balance sheet
- **Entity scope: all figures below are consolidated**, from the Condensed Consolidated Balance Sheet in the
  10-Q for the period ended 2026-06-30 (filed 2026-07-21, accession 0000033185-26-000028), compared to
  2025-12-31 (10-K) and 2025-06-30 (year-ago 10-Q).
- **FCF conversion:** TTM FCF **$1.105bn** vs TTM GAAP net income (Q3'25 $160.2M + Q4'25 derived $NaN[not **[Corrected 2026-10-08: placeholder; TTM net income is $691.4M]**
  separately pulled] + Q1'26 $171.5M + Q2'26 $183.9M — partial figure only; full-year 2025 FCF was disclosed
  by the company as **"$1.13 billion, up almost 40%"** (4Q 2025 release) — a strong, company-confirmed
  cash-conversion improvement, consistent with this dossier's own TTM calculation.
- **SBC:** $43.3M in 1Q 2026 (2.6% of that quarter's revenue) — modest and stable, up slightly from $33.5M a
  year earlier; not a quality concern.
- **GAAP vs. adjusted gap:** 2Q 2026 adjusted EPS $2.25 vs GAAP diluted EPS $1.54 — a large, ~46% gap. Per the
  company's own non-GAAP reconciliation footnote, adjusted EPS excludes (among other items) **"accrual for
  legal and regulatory matters related to the 2017 cybersecurity incident"** — i.e., Equifax is still
  adjusting out costs related to its 2017 data breach nine years later, a genuine and unusual longevity for a
  "one-off" adjustment; also excludes acquisition-related amortization, a gain on sale of an equity investment,
  and FX on intercompany loans. The size and persistence of this gap warrants tracking, not just accepting the
  adjusted number at face value.
- **Balance sheet (consolidated, 10-Q):** cash & equivalents $170.1M (Dec-25: $180.8M) — a thin cash position
  for a $17.4bn market-cap company, though the company maintains a $2.0bn revolving credit facility (~$0.6bn
  available per the 10-Q) as its primary liquidity backstop; noncurrent debt $4,057M (Dec-25: $4,323M, **[Corrected 2026-10-08: omits $1,410.3M of short-term debt and current maturities; total debt $5,467M]**
  essentially flat/slightly declining); total assets $11,982M; total liabilities $7,462M (Dec-25: $6,840M);
  stockholders' equity **$4,380M**, down from $4,797M at Dec-25 **[Corrected 2026-10-08: wrong: Dec-25 equity $4,604.3M, liabilities $7,126.0M]** — driven by buybacks/dividends running ahead
  of retained-earnings growth over the period. Net debt ≈ $4,057M − $170M = ~$3.89bn; against TTM FCF
  $1.105bn, net debt/FCF ≈ **3.5x** **[Corrected 2026-10-08: corrected: net debt $5,297M, 4.8x TTM FCF; kill criterion 4 already exceeded]** — a real leverage level to monitor, though within the range Equifax has
  run historically post its Cloud technology transformation investment (~$3bn cumulative per management
  commentary).
- **Capital return / M&A:** repurchased 3.1M shares in H1 2026 on the open market (~$1.5bn remaining
  authorization as of 2026-06-30, after the Board terminated the prior authorization and approved a new
  $3bn program on 2025-04-21); quarterly dividend raised to $0.56/share effective Q1 2026. **Pending
  acquisition:** July 2026 definitive agreement to acquire **Círculo de Crédito** (Mexican credit bureau) for
  enterprise value **$750M** (purchase price $825M, net of ~$75M cash acquired), expected to close 4Q 2026,
  subject to regulatory approval — a modest, complementary international bolt-on, not a leverage concern at
  this size.

## 7. Valuation snapshot
No `v1_valuation_table.csv`/`v1_valuation.json` row exists for EFX in this run — **v1_verdict is null**, per
the wave-4 instructions, and there is nothing to reconcile. `d4_live_snapshot.parquet` (2026-09-25): NTM P/E
15.2x, FY1 P/E 14.6x, FCF yield 5.45% (Yahoo-derived; this dossier's own TTM FCF/market-cap works out to
~6.35%, a modest cross-check difference, likely a capex-definition gap, flagged as a data conflict).

**Own reverse DCF** (two-stage: TTM FCF $1.105bn, cost of equity 10.7% from CAPM [beta 1.305, rf 4.2%, ERP **[Corrected 2026-10-08: rf should be 5.17%: cost of equity 11.7%; with SBC-deducted FCF $1,013M implied growth is 8.3%/yr, in line with the 8-10% base]**
5%], 10-year explicit growth then 3% terminal growth, versus the current $17.4bn market cap) implies the
market is pricing in only **≈5.3%/yr** FCF growth for 10 years. This analyst's own base case — blending
Workforce Solutions' structural high-single/low-double-digit growth (10% in Q1 2026), USIS's 6–8%
long-term-framework (management's own stated algorithm, currently running well above it on a temporary
mortgage bump), and further margin recovery as mortgage volumes normalize and the Cloud-migration capex cycle
tapers — is roughly **8–10%/yr** revenue growth with faster FCF growth as margins expand (FCF grew ~40% in
2025 alone on the company's own disclosure). The base case is comfortably **above** the 5.3%/yr the price
implies. **valuation_view_vs_v1.implied_vs_base = "below."** **[Corrected 2026-10-08: restated to in_line]** This supports INCLUDE/INCLUDE-SMALL eligibility
on valuation grounds; the verdict is capped at INCLUDE-SMALL by the open regulatory/legal items below, not by
price.

## 8. Bull case / Bear case
**Bull:** (1) revenue growth has clearly re-accelerated for six straight quarters (+3.8% to +14.3% YoY) while
the stock's 12-month momentum is deeply negative (−25%) — a genuine, evidence-based disconnect between price
and fundamentals that a mortgage-cycle recovery (rates normalizing) would likely close; (2) Workforce
Solutions' Work Number data asset has no readily replicable competitor and continues to post high-single/
low-double-digit growth even in a soft hiring/mortgage backdrop; (3) management's conservative "beat-but-hold"
guidance style (holding the full-year range flat despite Q1 2026's $37M beat) suggests the reported numbers
are not being managed aggressively upward, which should mean more credible beats if the cycle turns.
**Bear:** (1) the CFPB's Workforce-Solutions investigation (open since July 2023, three CIDs through August
2024, no resolution disclosed as of 2026-07-21) targets the FCRA-compliance practices of the company's single
most valuable data asset — an adverse finding could force costly changes to how Work Number data is sourced,
verified or licensed; (2) a separate FCRA class-action lawsuit (filed August 2022, over a "previously-disclosed
coding issue" that miscalculated some credit scores for three weeks) reached an agreement in principle to
settle in June 2026, with a **$100M accrual (net $40M after a $60M insurance receivable)** booked in 2Q 2026 —
final court approval is not yet confirmed, so the ultimate cost is not fully locked in; (3) an antitrust
lawsuit (filed May 2024, Eastern District of Pennsylvania) alleges anticompetitive conduct specifically in the
Workforce Solutions electronic-verification market — disputed by the company, unresolved, and thematically
consistent with the CFPB probe (both target the same business line).

## 9. Key risks & kill criteria (measurable)
1. Consolidated revenue growth (GAAP, YoY) falls back below 5% for two consecutive quarters (from +10.6% in
   Q2 2026) — a signal the re-acceleration has stalled.
2. The CFPB investigation into Workforce Solutions results in a public enforcement action, consent order, or
   disclosed monetary penalty (currently: investigation ongoing, no action disclosed).
3. The FCRA class-action settlement (agreement in principle, June 2026) fails court approval, or the final
   settled/reserved amount exceeds $200M (from the $100M gross accrual booked in 2Q 2026).
4. Net debt/TTM FCF rises above 4.5x (from ~3.5x currently) without a corresponding disclosed reason.
5. Full-year Adjusted EPS guidance (currently $8.39–8.69 for FY2026) is cut at any quarterly update — a break
   from the "beat-but-hold" pattern in the opposite (negative) direction.

## 10. Catalysts & calendar
Next earnings: **2026-10-20** (Q3 2026, per `d4_live_snapshot.parquet`). Círculo de Crédito acquisition
targeted to close 4Q 2026 (company's own disclosure). No investor-day date found in the documents reviewed.

## 11. Red-flag scan
- **Regulatory (entity: consolidated, Workforce Solutions segment):** CFPB Civil Investigative Demands
  (July 2023, March 2024, August 2024) into data accuracy and FCRA compliance at Workforce Solutions;
  company states it is "unable to predict the outcome... including whether the investigation will result in
  any actions or proceedings" (10-Q, period 2026-06-30, filed 2026-07-21) — open, unresolved, material given
  the segment's importance to the moat thesis.
- **Litigation (entity: consolidated, FCRA class action, N.D. Georgia, filed 2022-08-03):** agreement in
  principle to settle reached June 2026; **$100M accrual, $60M insurance receivable, $40M net charge** booked
  in 2Q 2026; final settlement terms and court approval not yet confirmed as of the 10-Q reviewed.
- **Litigation (entity: consolidated, antitrust, E.D. Pennsylvania, filed 2024-05-28):** putative class action
  alleging anticompetitive conduct in the electronic income/employment verification market; disputed,
  unresolved.
- **Litigation (entity: consolidated, separate inquiry-dispute matters, various federal courts):** a **$30.0M**
  accrual was booked in 4Q 2025 for a nationwide settlement-in-principle on a different set of claims
  (consumer credit-file inquiry disputes) — smaller and apparently on a separate track from the FCRA coding-
  issue matter above; notice of settlement filed with courts, final approval pending.
- No auditor changes, material weakness, going-concern language or restatement found in the 10-Q reviewed;
  "no material changes" stated versus the 2025 Form 10-K risk factors.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (period ended 2026-06-30), Form 10-Q filed 2026-07-21 (accession
0000033185-26-000028), plus the Q1 2026 10-Q (filed 2026-04-21), FY2025 10-K (filed 2026-02-19) and the three
related 8-K Exhibit 99.1 earnings releases (2026-02-04, 2026-04-21, 2026-07-21) for the guidance track record
and quarterly history. Note: Q3 2026 results (due 2026-10-20) had not been filed as of this dossier's cutoff.
Events checked to 2026-09-25 close. All figures are **GAAP unless labelled "adjusted,"** per the company's own
reconciliations. Research, not personalized investment advice; not a recommendation.

## 13. Sources
1. SEC EDGAR, Equifax Inc. Form 10-Q, period 2026-06-30, filed 2026-07-21 (accession 0000033185-26-000028):
   `https://www.sec.gov/Archives/edgar/data/33185/000003318526000028/efx-20260630.htm`
2. SEC EDGAR, Form 10-Q, period 2026-03-31, filed 2026-04-21 (accession 0000033185-26-000016).
3. SEC EDGAR, Form 10-K, FY2025, filed 2026-02-19 (accession 0000033185-26-000010).
4. 8-K Exhibit 99.1, Q2 2026 earnings release, filed 2026-07-21 (accession 0000033185-26-000024):
   `https://www.sec.gov/Archives/edgar/data/33185/000003318526000024/exhibit99120260630.htm`
5. 8-K Exhibit 99.1, Q1 2026 earnings release, filed 2026-04-21 (accession 0000033185-26-000016).
6. 8-K Exhibit 99.1, Q4/FY2025 earnings release, filed 2026-02-04 (accession 0000033185-26-000004).
7. SEC EDGAR XBRL company facts API: `https://data.sec.gov/api/xbrl/companyfacts/CIK0000033185.json`
8. `v4/data/b1_live_scores.csv` and `v4/data/d4_live_snapshot.parquet` (2026-09-25 snapshot).
9. `v4/outputs/Q10_triage.json` (triage entry for EFX).
10. `v4/outputs/v1_valuation_table.csv` (checked — no EFX row exists in this run).

## Correction (verification DV14, 2026-10-08)

**Verdict unchanged: INCLUDE-SMALL. implied_vs_base restated: below -> in_line.**
1. Section 7, valuation: the reverse DCF used a risk-free rate of 4.2% (CAPM cost of equity 10.7%), but the 10-year Treasury was 5.17% on 25 Sep 2026; it also used free cash flow before stock-based compensation. Recomputed on the same two-stage form (terminal growth 3%, market cap $17.4bn): FCF after SBC is $1,013M (operating cash flow $1,612.4M less capex $507M less SBC $92.3M); at a cost of equity of 11.7% (5.17% + 1.305 x 5% ERP) the price implies 8.3% a year of FCF growth for ten years (7.1% at a 4.5% ERP), not 5.3%. That sits at the low end of the dossier's own 8-10% base, so implied_vs_base is in_line, not below. The base-case 3-year return of +8.7% a year is below the 11.0-11.7% cost of equity, which is consistent with in_line and argues for half weight; the open CFPB matter remains the second reservation.
2. Section 6, balance sheet: the dossier's net debt (noncurrent debt $4,057M less cash $170M, about $3.89bn) omits $1,410.3M of short-term debt and current maturities. Total debt is $5,467M and net debt $5,297M at 30 Jun 2026, so net debt/TTM FCF is 4.8x, not 3.5x (Dec-25: $5,361M debt, 4.6x). Kill criterion 4 (net debt/TTM FCF above 4.5x) was therefore already exceeded when written and should be reset: use net debt/adjusted EBITDA (about 2.5x on the $2.12bn guided midpoint). Source: Q2 Ex-99.1 balance sheet, acc 0000033185-26-000024.
3. Section 6: the Dec-25 comparatives are wrong. Equifax shareholders' equity was $4,604.3M (not $4,797M) and total liabilities $7,126.0M (not $6,840M); the fall to $4,380.2M is $224M. June 2026 figures are correct. The "Q4'25 derived $NaN" placeholder should read: TTM net income $691.4M, so TTM FCF is about 160% of net income.
4. Verified unchanged: Q2 2026 revenue $1,700.1M, GAAP EPS $1.54, adjusted EPS $2.25; all three guidance releases (initial $6.72bn / $8.50 midpoints, April +$25M / +$0.04, July $6.710-6.780bn / $8.39-8.69); Q3 guide; Círculo terms.
