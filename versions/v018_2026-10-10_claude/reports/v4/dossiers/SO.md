# Southern Company (SO) — Diligence Dossier (Agent F82, standard depth)

## 1. Verdict
**INCLUDE** (full weight), thesis horizon **24–48 months**. Top-tier regulated-utility scale and credit quality,
Vogtle overrun risk now behind it, priced fairly (not cheaply) at 17.1x NTM P/E with real Southeast data-center
load upside as the swing factor. No V1 systematic valuation row exists for SO (not in `v1_valuation_table.csv`),
so this verdict rests on this dossier's own reverse-DCF sense-check, not a reconciliation. **[Corrected 2026-10-06: the 'INCLUDE' and 'priced fairly' framing rested on a ~1% implied growth figure that was an artefact of a 7.0% cost of equity (only 1.8 points above the 5.17% Treasury) and of treating earnings yield as cash; on a dividend basis at a consistent discount rate the implied growth is about in line with the base case, so conviction is cut to half (INCLUDE-SMALL). See Re-assessment RA9 below]]**

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
prior ranges — time-boxed at standard depth; treat guidance-track-record confidence as medium, not high.** **[Corrected 2026-10-06: the 2026 adjusted EPS guidance is $4.50 to $4.60 (maintained in Q1 and Q2; on 30 Jul 2026 management said it expects results 'at or near the top' of that range, per Q2 call transcript, secondary source; the filed release carries no range). Management's longer-term framework, per Q1 2026 slides (secondary source), is 8-9% adjusted EPS growth through 2028 and 7-8% after, not the 5-7% quoted here. Guidance has not been cut]]**

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
  debt, hybrid securities and modest equity issuance (e.g., ATM programs) rather than large blocks. **[Corrected 2026-10-06: SO issued about 31.1m shares in H1 2026 (forward-sale settlements, $2.5bn proceeds); average shares were 1,137m in Q2 2026 versus 1,101m a year earlier (+3.3%); on 3-6 Aug 2026 it also issued $2.73bn of convertible senior notes (2.125% due 2027 and 3.50% due 2029; 2026A conversion price about $104.56) and in March 2026 $1.3bn of 6.00% junior subordinated notes; a new 2026 ATM programme of up to 50m shares was set up in June (10-Q 0000092122-26-000054, 8-Ks 0000092122-26-000058/-060/-063). Per-share growth is diluted by about 3-4% a year at present; management's stated remaining equity need through 2030 is $1.1bn (Q2 call, secondary)]]**

## 7. Valuation snapshot and reverse DCF
Per `data/triage_cards.csv` (2026-09-25 close, $82.88): NTM P/E **17.1x** (trailing 20.1x), dividend yield
**3.6%**, Street 12-month upside **19.7%** (19 analysts), 1-year momentum **-4.1%** (has lagged, arguably why it
still screens as "advance, not obviously loved"). SO does **not** have a row in `v1_valuation_table.csv` or
`v1_valuation.json`, so **v1_verdict = null** for this ticker — no formal reconciliation is possible; this
dossier's reverse-DCF is a standalone sense-check, not a validated systematic output.

**Reverse DCF (Gordon-growth approximation on NTM earnings yield):** earnings yield = 1/17.1 = 5.85%. Using an
~7.0% cost-of-equity assumption typical for a BBB+/A-rated regulated utility with SO's beta, implied perpetual
growth ≈ 7.0% − 5.85% ≈ **1.1%/yr**. **[Corrected 2026-10-06: wrong method: earnings yield is not a cash yield for a utility that retains about a third of earnings and has negative free cash flow (H1 2026 operating cash flow $4.28bn less property additions $6.64bn = -$2.36bn), and 7.0% is only 1.8 points over the 5.17% Treasury. Dividend-based test at 8.5% (5.17% + 0.7 floored beta x 4.75%): implied perpetual growth 8.5% - $3.12/$82.88 = 4.7%; implied 10-year dividend/EPS growth (payout held at about 66%, terminal 3.5%) = 7.0%]]** SO's own long-term guidance framework (management has historically
targeted mid-single-digit, ~5–7%, adjusted EPS growth off rate-base additions) is well above this implied rate.
**Implied growth (~1%) is below the evidence-based base case (~5–6% adjusted EPS CAGR)** — the market is not
paying up for the data-center upside yet, which is the core of the bull case. **[Corrected 2026-10-06: implied growth is about in line with, not below, the evidence-based base case: 4.7% / 7.0% / 8.3% at 7.7% / 8.5% / 9.0% versus a base of about 7% (consensus FY26 +6.7%, FY27 +7.3%). implied_vs_base = in_line; the data-center upside is only worth a premium if management's 8-9% path is delivered]]**

- **Bear (evidence-based):** data-center pipeline slips/regulatory pushback on cost recovery; growth reverts to
  ~2–3%, multiple compresses to 15x on rate normalization. **Annualised 3y return ≈ −1% to 0%** (3.6% yield,
  minimal EPS growth, multiple drag). **[Corrected 2026-10-06: restated -1.4% a year on FY27 $4.74, +3%/yr, 13.5x, dividends included]]**
- **Base:** 5–6% adjusted EPS growth delivered, multiple holds ~17x, dividend grows with payout. **Annualised
  3y return ≈ 9–10%** (3.6% yield + ~6% growth + ~0% multiple change). **[Corrected 2026-10-06: restated +8.5% a year on FY27 $4.92 (consensus), +7%/yr, 16.0x, dividends included]]**
- **Bull:** Georgia/Southeast data-center load materializes into approved rate base faster than guided (8%+
  EPS growth), multiple re-rates toward peers with confirmed hyperscaler backlogs (19–20x). **Annualised 3y
  return ≈ 15–17%.** **[Corrected 2026-10-06: restated +16.7% a year on FY27 $4.97, +9%/yr, 19.0x]]**

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

---
## Re-assessment (RA9, 2026-10-06)
Scope: independent re-test of the valuation behind "implied vs base". Data cutoff: EDGAR to 2026-10-06 (no 8-K after 6 Aug 2026; Forms 4 on 5 Oct are routine). Price $82.88 (25 Sep 2026), 1,150.4m shares outstanding. Original text above is unchanged. Research only, not personal advice.

| # | Wrong or stale text | Corrected value | Source | Effect |
|---|---|---|---|---|
| 1 | Cost of equity ~7.0% | 5.17% 10-year Treasury (FRED DGS10, 25 Sep 2026) + beta x 4.75% ERP. Raw beta 0.316 (d4), Blume-adjusted 0.54 gives 7.7%; a floor beta of 0.7 gives 8.5%; SO itself paid 6.00% on junior subordinated debt in March 2026, so an equity cost below about 8% is not credible. Central 8.5%, range 7.7-9.0% | FRED; 10-Q 0000092122-26-000054 | The original 1.8-point equity premium was too thin |
| 2 | Implied growth = cost of equity minus NTM earnings yield (~1.1%) | Dividend discount basis (utility free cash flow is negative: H1 2026 operating cash flow $4,280m, property additions $6,639m). Annualised dividend $3.04 after the April 8-cent raise (per Q1 slides, secondary), next-year $3.12. Perpetual implied dividend growth: 3.9% / 4.7% / 5.2% at 7.7% / 8.5% / 9.0%. Two-stage (10 years, terminal 3.5%) implied growth: 4.7% / 7.0% / 8.3% | RA9 arithmetic on $82.88 | Implied about equals the base case: in_line, not below |
| 3 | Base case 5-6% adjusted EPS CAGR; "5-7% long-term target" | Guidance range for 2026: $4.50-$4.60, "at or near the top" (Q2 call, secondary); framework 8-9% through 2028 then 7-8% (Q1 slides, secondary); consensus FY26 $4.59 (+6.7%) and FY27 $4.92 (+7.3%) from d4. FY25 adjusted EPS $4.30 (+6.2%) and H1 2026 $2.46 versus $2.15 (+14%) per filed releases. Base re-set to ~7% | 8-K 0000092122-26-000008 and -000056 (filed releases carry no guidance); secondary sources flagged | Evidence base case is higher than the dossier said, but so is the correct implied rate |
| 4 | "No anomalous issuance" | 31.1m shares issued in H1 2026 ($2.5bn); average shares +3.3% year on year; $2.73bn converts and $1.3bn junior subordinated notes issued in 2026; $1.75bn 3.25% senior notes repaid after quarter end | 10-Q 0000092122-26-000054; 8-K 0000092122-26-000063 | Dilution and leverage are real; offset by a stated remaining equity need of $1.1bn through 2030 (secondary) |
| 5 | Scenarios -0.5% / +9.5% / +16% | Re-built on FY30 EPS x NTM multiple plus dividends: bear -1.4% (FY27 $4.74, +3%/yr, 13.5x), base +8.5% (FY27 $4.92, +7%/yr, 16.0x), bull +16.7% (FY27 $4.97, +9%/yr, 19.0x) | arithmetic by RA9 | Base return of 8.5% a year equals the 8.5% hurdle: no margin of safety |
| 6 | Guidance track record "not verified" | 2026 range maintained at Q1 and Q2 and expected at or near the top; no cut found; kill criterion 4 has not fired | Q2 call (secondary) | Gap narrowed; primary slides not on EDGAR |

Verdict: **INCLUDE reduced to INCLUDE-SMALL.** At a discount rate consistent with a 5.17% Treasury the market price asks for about the growth management and consensus already expect (7.0% implied versus about 7% base), the free-cash-flow gap is funded by debt and equity, and shares are being diluted 3-4% a year. A quality utility at a fair price, not at a margin of safety. Re-promote below roughly $70 (dividend value at 5% growth and 8.5%) or if EPS growth of 8-9% is delivered with no further equity beyond $1.1bn.
