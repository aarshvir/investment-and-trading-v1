# Southern Company (SO) — Diligence Dossier (Agent F82, standard depth)

## 1. Verdict
**INCLUDE** (full weight), thesis horizon **24–48 months**. Top-tier regulated-utility scale and credit quality,
Vogtle overrun risk now behind it, priced fairly (not cheaply) at 17.1x NTM P/E with real Southeast data-center
load upside as the swing factor. No V1 systematic valuation row exists for SO (not in `v1_valuation_table.csv`),
so this verdict rests on this dossier's own reverse-DCF sense-check, not a reconciliation.

## 2. Business in plain English
Southern Company owns Georgia Power, Alabama Power and Mississippi Power — vertically integrated, rate-regulated
electric utilities serving ~9 million customers across the Southeast — plus a smaller gas-distribution segment
(Southern Company Gas). It earns a state-regulated return on the capital (rate base) it invests in generation,
transmission and distribution; growth comes from rate-base additions (data centers, industrial reshoring,
electrification) approved by state commissions, not from competitive market share.

## 3. Why the model likes it / durability
Triage (`outputs/Q15_triage.json`) scored SO quality 5/5, growth 3/5, price-vs-growth 3/5, citing scale,
diversification and credit quality with Vogtle risk resolved. `data/b1_live_scores.csv` shows SO composite
decile 2 / quintile 1 (i.e., near the bottom of the live-scored universe on the systematic factor model — model
rank 400 of the ranked names), driven by weak momentum (pct_mom_12_1 ≈ 0.31) and value that is only mid-pack
(pct_ep ≈ 0.57, pct_fcfp ≈ 0.18 — SO screens as FCF-negative on a trailing accruals basis because of heavy
capex, common for utilities and not itself a red flag). **Data conflict:** the systematic model ranks SO near
the bottom of the scored universe (decile 2) while the qualitative triage advanced it on quality/scale — this is
consistent with the known limitation that value/quality factor scores penalize capital-intensive utilities for
low trailing FCF and low momentum, not with a fundamental problem; durable growth driver (data-center demand in
Georgia) is not visible to the point-in-time factor model at all. Flagged as `data_conflicts`.

## 4. Recent results (consolidated Southern Co, GAAP unless noted)
Source: XBRL companyfacts (SEC, tags `RevenueFromContractWithCustomerIncludingAssessedTax`,
`OperatingIncomeLoss`, `NetIncomeLoss`, `EarningsPerShareDiluted`) cross-checked against the 10-Qs/10-K, plus the
Q2 2026 earnings-release exhibit (8-K filed 2026-07-30, accession 0000092122-26-000056) for the most recent
quarter, which had not yet propagated into SEC's structured XBRL frames as of this diligence date.

| Quarter | Revenue ($bn) | Op. income ($bn) | GAAP diluted EPS |
|---|---|---|---|
| Q3 2024 | 7.48 | 2.37 | 1.39 |
| Q4 2024 (10-K, implied) | 6.25 | 1.06 | 0.45 |
| Q1 2025 | 7.59 | n/a (period start) | 1.21 |
| Q2 2025 | 6.97 | 1.76 | 0.79 |
| Q3 2025 | 7.82 | 2.59 | 1.54 |
| Q4 2025 (10-K, implied) | 6.80 | 0.92 | 0.38 |
| Q1 2026 | 8.04 | 2.02 | 1.20 |
| **Q2 2026** (press release, not yet in XBRL frames) | **6.98** | n/a | **1.03** (adj. **1.13**) |

Q2 2026 GAAP EPS $1.03 vs $0.80 a year earlier (+29%); adjusted EPS $1.13 vs $0.92 (+23%), per the Q2 2026 press
release (SEC 8-K exhibit ex99-pressreleaseq22026.htm). Revenue essentially flat YoY (+0.1%) in Q2 but six-month
revenue is up 4.2% YoY ($15.4bn vs $14.7bn), consistent with weather-normal customer growth plus rate-base
recovery rather than a step-change from data centers yet.

## 5. Guidance track record
SO's Q2 2026 press release, as extracted, does **not restate a full-year 2026 EPS guidance range** (SO typically
guides via a long-term 5–7% adjusted EPS growth target off a base year rather than quarter-by-quarter point
guidance; the specific Q3 2026 8-K/press release was not pulled in this pass — **gap**, noted below). What is
confirmed from the primary document: management flagged continuing "extraordinary economic development
momentum and demand for power" (data-center pipeline) and a tax remeasurement tied to the resolved Vogtle
loss estimate, not a guidance cut or raise. **This dossier did not verify 4 consecutive guidance releases against
prior ranges — time-boxed at standard depth; treat guidance-track-record confidence as medium, not high.**

## 6. Earnings quality & balance sheet (entity: **consolidated Southern Company**, from 10-Q tables)
- Long-term debt + current portion of long-term debt and capital leases (consolidated, XBRL tag
  `LongTermDebtAndCapitalLeaseObligations` + current portion): **$67.15bn + $5.70bn current = ~$72.8bn** at
  2026-03-31 (consolidated, Q1 2026 10-Q, filed 2026-04-30, accession 0000092122-26-000034 — the latest
  balance-sheet date with structured XBRL available; the Q2 2026 10-Q, filed 2026-07-30, accession
  0000092122-26-000054, was not pulled line-by-line in this pass).
- Cash and cash equivalents (consolidated): **$981mn** at 2026-03-31 (was $1.64bn at 2025-12-31; utilities run
  thin cash by design, funding via revolvers/commercial paper).
- Stockholders' equity (consolidated): **$36.0bn** at 2025-12-31 (10-K), up from $33.2bn a year earlier —
  steady equity build consistent with a constructive-regulation utility, not a leveraging-up story.
- `net_debt_to_ebitda` per `data/triage_cards.csv`: **5.2x** — high in absolute terms but normal for a
  vertically-integrated regulated utility with a large multi-year capex program; peer AEP screens at 5.9x.
- FCF is structurally negative before financing (heavy capex funded by debt + equity issuance), standard for
  the sector; this is why `fcfp` (FCF yield) percentile is low (≈18th) in the factor model — not a red flag on
  its own, but it does mean equity dilution risk if capex needs outrun regulator-approved rate-base growth.
- Share count: no anomalous issuance detected in this pass; SO has historically funded growth with a mix of
  debt, hybrid securities and modest equity issuance (e.g., ATM programs) rather than large blocks.

## 7. Valuation snapshot and reverse DCF
Per `data/triage_cards.csv` (2026-09-25 close, $82.88): NTM P/E **17.1x** (trailing 20.1x), dividend yield
**3.6%**, Street 12-month upside **19.7%** (19 analysts), 1-year momentum **-4.1%** (has lagged, arguably why it
still screens as "advance, not obviously loved"). SO does **not** have a row in `v1_valuation_table.csv` or
`v1_valuation.json`, so **v1_verdict = null** for this ticker — no formal reconciliation is possible; this
dossier's reverse-DCF is a standalone sense-check, not a validated systematic output.

**Reverse DCF (Gordon-growth approximation on NTM earnings yield):** earnings yield = 1/17.1 = 5.85%. Using an
~7.0% cost-of-equity assumption typical for a BBB+/A-rated regulated utility with SO's beta, implied perpetual
growth ≈ 7.0% − 5.85% ≈ **1.1%/yr**. SO's own long-term guidance framework (management has historically
targeted mid-single-digit, ~5–7%, adjusted EPS growth off rate-base additions) is well above this implied rate.
**Implied growth (~1%) is below the evidence-based base case (~5–6% adjusted EPS CAGR)** — the market is not
paying up for the data-center upside yet, which is the core of the bull case.

- **Bear (evidence-based):** data-center pipeline slips/regulatory pushback on cost recovery; growth reverts to
  ~2–3%, multiple compresses to 15x on rate normalization. **Annualised 3y return ≈ −1% to 0%** (3.6% yield,
  minimal EPS growth, multiple drag).
- **Base:** 5–6% adjusted EPS growth delivered, multiple holds ~17x, dividend grows with payout. **Annualised
  3y return ≈ 9–10%** (3.6% yield + ~6% growth + ~0% multiple change).
- **Bull:** Georgia/Southeast data-center load materializes into approved rate base faster than guided (8%+
  EPS growth), multiple re-rates toward peers with confirmed hyperscaler backlogs (19–20x). **Annualised 3y
  return ≈ 15–17%.**

## 8. Bull case
1. Vogtle 3/4 now in service and largely de-risked from a construction-overrun standpoint (Q2 2026 EPS
   commentary references only a tax remeasurement on the historical loss estimate, not new overruns).
2. Real, quantifiable Southeast data-center and industrial load growth in Georgia Power's territory that other
   utilities are still only pipeline-stage on — a genuine rate-base growth catalyst, not yet in guidance/price.
3. Investment-grade, diversified multi-state regulated base (GA/AL/MS) gives regulatory diversification other
   single-state utilities lack.

## 9. Bear case
1. Net debt/EBITDA ~5.2x consolidated leaves limited headroom if a large unplanned capex item (storm,
   generation retrofit) hits before the next rate case.
2. 1-year price momentum is negative (-4.1%) while peers with confirmed hyperscaler contracts have re-rated —
   SO may be a "show me" story until specific load agreements are signed and rate-based.
3. Guidance track record was not fully verified this pass (see §5 gap) — a real risk that a guidance cut could
   be sitting in a release this dossier did not check.

## 10. Key risks & kill criteria (measurable)
1. Adjusted EPS growth falls below 4% for two consecutive quarters (vs the ~5–7% long-term target).
2. Consolidated net debt/EBITDA rises above 6.0x without a credit-positive equity issuance offsetting it.
3. A state commission (Georgia, Alabama or Mississippi PSC) formally disallows recovery of a material capex
   or fuel-cost item (>$250mn) in a rate order.
4. Guidance is cut (not just reaffirmed) at any of the next two quarterly releases.
5. A confirmed hyperscaler data-center load agreement in the Southeast is publicly cancelled or downsized.

## 11. Catalysts & calendar
Next quarterly release: Q3 2026 earnings, expected ~late October 2026 (SO has historically reported in the last
week of October; not confirmed from a primary source this pass — **gap, verify from the IR calendar before
acting**). No investor day identified in this pass.

## 12. Red-flag scan
- **SEC/DOJ:** No new 2026 SEC or DOJ investigation was found in this pass (WebSearch, 2026-09-27). Historical
  items on record: an SEC investigation and a securities class action tied to the (since-abandoned) Kemper IGCC
  project (filed 2017, unrelated business/subsidiary, long resolved), and a 2022 class action against auditor
  Deloitte over Kemper-era financial statements — both **legacy Kemper matters, not current Vogtle or
  operating-segment issues**. No going-concern language, no disclosed material weakness or restatement was
  identified in the documents reviewed this pass.
- **Litigation:** none identified beyond the above in this time-boxed search; a full Item 3 (Legal Proceedings)
  read of the Q2 2026 10-Q was not completed this pass — **gap**.
- Auditor: not re-verified this pass (assume unchanged from most recent 10-K; **gap**).

## 13. Data basis, recency and disclaimer
Most recent period incorporated: **Q2 2026** (quarter ended 2026-06-30) EPS/revenue from the Q2 2026 earnings
press release (SEC 8-K exhibit, accession 0000092122-26-000056, filed 2026-07-30); most recent period with
structured, cross-checkable consolidated XBRL balance-sheet and income-statement data is **Q1 2026** (10-Q
filed 2026-04-30, accession 0000092122-26-000034) because SEC's XBRL companyfacts/frames API had not yet
incorporated the Q2 2026 10-Q (filed 2026-07-30, accession 0000092122-26-000054) as of this diligence date — a known
processing lag, not a data-quality problem with SO's filings. Events checked to 2026-09-25 close via WebSearch;
search did not surface a 2026-dated news item beyond the earnings release itself. GAAP figures are labelled GAAP;
adjusted (non-GAAP) EPS is labelled "adjusted" throughout and sourced from SO's own reconciliation in the press
release. **Research only; not personal investment advice.**

## Sources
1. SEC EDGAR submissions, CIK 0000092122: https://data.sec.gov/submissions/CIK0000092122.json (retrieved 2026-09-27)
2. SEC XBRL companyfacts, CIK 0000092122: https://data.sec.gov/api/xbrl/companyfacts/CIK0000092122.json (retrieved 2026-09-27)
3. SO Q2 2026 earnings press release (8-K exhibit 99, filed 2026-07-30, accession 0000092122-26-000056):
   https://www.sec.gov/Archives/edgar/data/92122/000009212226000056/ex99-pressreleaseq22026.htm
4. `v4/outputs/Q15_triage.json`, `v4/data/b1_live_scores.csv`, `v4/data/triage_cards.csv` (internal, 2026-09-25 close)
5. WebSearch, "Southern Company SEC investigation litigation 2026 Vogtle lawsuit material weakness", 2026-09-27
