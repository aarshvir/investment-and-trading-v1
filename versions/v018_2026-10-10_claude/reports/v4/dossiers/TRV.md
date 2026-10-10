# Travelers Companies, Inc. (NYSE: TRV) — Fundamental Diligence Dossier

**Prepared by:** f1 (fundamental diligence analyst) | **Data cutoff:** 2026-09-25 close | **Most recent period incorporated:** Q2 2026 (10-Q filed 2026-07-17, period ended 2026-06-30); checked for events to 2026-09-25. Next scheduled report: Q3 2026 on 2026-10-16. **Basis:** consolidated GAAP financial statements throughout (Travelers reports on a single consolidated basis; core/adjusted figures are the company's own non-GAAP measure, labeled as such wherever used).

**Data quality note:** all financial figures below are sourced to SEC EDGAR primary filings (10-Q/10-K, 8-K earnings-release exhibits) or SEC XBRL company facts (a machine-readable copy of the same filings), each cited by number in §12; quant/peer context is sourced to the v4 internal `lead_prelim_rank.csv` and `d4_live_snapshot.parquet`, labeled as such. Two data points are explicitly derived (FY minus 9-month YTD, both from officially reported figures) rather than directly reported, and are flagged inline (¹/²) where used. No figure in this dossier is estimated, interpolated, or recalled from training-data memory. **This dossier is research output for internal investment-process use, not personalised investment advice; it is not a recommendation to buy or sell any security, and the reader is responsible for their own decisions.**

## 1. Verdict: INCLUDE — thesis horizon 12–24 months
Well-run, disciplined P&C underwriter trading at a reasonable multiple of a *currently cycle-elevated* earnings base; include at full weight but size and monitor with the explicit assumption that 2026 combined-ratio/ROE levels will not persist into 2027–28. **[Corrected 2026-10-06: full weight is not supported after re-testing the valuation: at 2.29x book the price needs a sustained ROE of about 16.7% at a 9.0% cost of equity, in line with (not below) the 17.5% evidence-based base; verdict cut INCLUDE to INCLUDE-SMALL (half weight), see Re-assessment (RA14)]**

## 2. Business in plain English
Travelers is the third-largest U.S. property-casualty insurer, organized in three segments: **Business Insurance** (commercial P&C for companies of all sizes), **Bond & Specialty Insurance** (surety bonds, management/professional liability), and **Personal Insurance** (auto and homeowners for individuals). It sells almost entirely through independent agents and brokers, and makes money two ways: underwriting profit (premiums minus claims and expenses) and investment income earned on the "float" (reserves held before claims are paid). Competitive position: top-3 scale in commercial lines with a long underwriting track record; mid-pack but improving scale in personal auto/home.

## 3. Why the model likes it — and whether that's durable
b1-family prelim scores (source: internal `lead_prelim_rank.csv`): Q 0.858, V 0.438, M 0.938 (12-1m return +32.6%), composite 0.878. **Adversarial read: a meaningful share of this is an artefact, not a moat.** The quant pipeline's Quality/Value inputs (gross-profit/assets, EBIT/EV, generic leverage) are the *generic* factor set — per the insurance sector playbook (finance-skills `references/sectors/insurance.md`) these are undefined or misleading for underwriters, and the ROE/earnings-yield inputs that actually drive the Q/V scores are trailing GAAP figures currently inflated by (a) a favorable catastrophe base effect and (b) large reserve releases (see §4, sourced to Q2-26 8-K/10-Q, §12 sources #1-2). Momentum (M=0.938) is largely a reflection of the same base effect via the +46–120% YoY EPS growth run reported in §4. **Durable part:** per the Q2-26 earnings release (§12 #1), the *underlying* (ex-cat, ex-reserve-development) combined ratio is genuinely stable-to-improving (84.1% Q2-26 vs 84.7% Q2-25, consolidated) — a real, if modest, structural positive. **Not durable:** per the same release, the full 6.7-point YoY consolidated combined-ratio improvement in Q2-26 (90.3%→83.6%) is attributable to lower catastrophes and higher reserve releases, not underlying pricing/loss-cost improvement.

## 4. Results — last 8 quarters + FY trend (GAAP; SEC XBRL, source #6, cross-checked to press releases #1–#5)
| Quarter | Revenue ($B) | YoY growth | Net income ($B) | Diluted EPS (GAAP) | Core/adj. EPS |
|---|---|---|---|---|---|
| Q3 2024 | 11.90 | — | 1.260 | 5.42 | n/a¹ |
| Q4 2024 | 12.01² | — | 2.082² | 8.96² | n/a¹ |
| Q1 2025 | 11.81 | — | 0.395 | 1.70 | n/a¹ |
| Q2 2025 | 12.12 | — | 1.509 | 6.53 | 6.51 |
| Q3 2025 | 12.47 | +4.8% | 1.888 | 8.24 | n/a¹ |
| Q4 2025 | 12.43² | +3.5%² | 2.496² | 11.06 | 11.13 |
| Q1 2026 | 11.92 | +1.0% | 1.711 | 7.78 | n/a¹ |
| Q2 2026 | 12.15 | +0.3% | 2.208 | 10.26 | 10.04 |

¹ Not individually re-extracted for this dossier (non-GAAP core EPS is only pulled for the two most recent comparable quarters and FY2025); ² derived as FY minus 9-month YTD (both officially reported XBRL figures — simple subtraction, not an estimate).

**Combined ratio (the sector-correct substitute for "operating margin" — see playbook):**
- Q2 2026 consolidated **83.6%** vs Q2 2025 **90.3%** (−6.7 pts); underlying (ex-cat, ex-reserve-dev.) **84.1%** vs **84.7%** (−0.6 pt — nearly flat). 1H26 consolidated 86.1% vs 1H25 96.3% (−10.2 pts); underlying flat at 84.7% both years.
- Q4 2025 consolidated **80.2%** (full-year 2025 core ROE 19.4%, core EPS $27.59 +26% YoY).
- **The gap between the 6.7–10.2 pt "recorded" improvement and the ~flat underlying ratio is the single clearest evidence that reported earnings growth in 2026 is substantially a base effect, not a structural repricing gain.**

**Root cause of the base effect:** the January 2025 Southern California wildfires (Palisades and Eaton fires, named explicitly in the 10-Q catastrophe table) drove catastrophe losses of $927M pre-tax in Q2-25 alone and $3.193B pre-tax in 1H-25, vs. $518M and $1.279B in the 2026 equivalents — a swing of ~$1.9B pre-tax in 1H alone. Net favorable prior-year reserve development also rose (1H26 $991M vs 1H25 $693M pre-tax, ~4.6 pt combined-ratio benefit), concentrated in Business Insurance workers' comp/commercial property and Bond & Specialty general-liability management-liability lines across "multiple accident years." Bond & Specialty's *underlying* combined ratio actually **worsened** 1.6–2.5 pts YoY — a genuine (small) negative offsetting the Business Insurance and Personal Insurance gains.

## 5. Guidance track record
Travelers, like most P&C carriers, **gives no formal quantitative EPS or margin guidance** in its earnings releases (confirmed: no "outlook," "guidance," or forward numeric target found in the last 5 earnings releases reviewed). This item does not apply; see §8/§9 for the qualitative read on forward trajectory instead.

## 6. Earnings quality & balance sheet
- **FCF/OCF:** FY2025 operating cash flow $10.606B vs GAAP NI $6.288B (≈1.7x). TRV does not separately tag capex (immaterial for an asset-light underwriter), so FCF≈OCF. Caveat per sector playbook: high OCF/NI is partly mechanical (a growing book generates float-driven cash before it is earned) and should not be read as a generic "quality" signal the way it would for an industrial company.
- **SBC:** $256M FY2025 = 0.5% of revenue — immaterial dilution risk.
- **GAAP vs. core gap:** small and explained (per source #1: net realized investment gains/losses; Q2-26 core EPS $10.04 vs GAAP EPS $10.26, driven by $48M after-tax realized gains).
- **Debt:** $9.068B at 2026-06-30 ($9.267B at FY25-end), debt-to-capital 21.5% (comfortably investment-grade; company's own reconciliation table, 10-Q). **[Corrected 2026-10-06: on 21 Jul 2026 Travelers also sold $750M of 4.950% senior notes due 2031 (8-K filed 24 Jul 2026, acc 0001193125-26-316247; proceeds for general corporate purposes), so pro-forma debt is about $9.82B and debt-to-capital about 22.9% against the 25% ceiling of the 15-25% target range]** **Data conflict:** `lead_prelim_rank.csv` carries `debt_lt`+`debt_st` = $6.161B for TRV — a **~32% ($2.9B) understatement** of the company's own reported debt figure. The quant pipeline's debt tag appears to miss part of TRV's long-term debt stack; this understates TRV's leverage factor input and should be corrected before the next live-scoring run.
- **Buybacks/capital return:** FY2025 buybacks $3.004B (up from ~$1.0B FY2023/24), dividends $979M; Q2-26 alone $1.311B repurchased, $3.915B authorization remaining. Share count reduction is a real contributor to per-share growth on top of NI growth — disentangle the two when reading EPS growth rates.
- **Book value (per source #1, Q2-26 release):** $158.81/share (+5% YoY); ex-AOCI $168.20 (+6% YoY) — genuine compounding, not just multiple-driven.
- **Legacy tail risk:** standard, long-disclosed asbestos & environmental reserve exposure (10-Q Note 15) — monitored for decades, no new deterioration flagged this quarter.

## 7. Valuation snapshot
*(`scripts/ratios.py`/`scripts/valuation.py` were deliberately not run: their outputs — EV/EBITDA, FCF-based DCF, generic ROCE/current-ratio — are the specific metrics the insurance sector playbook states are undefined or misleading for underwriters. The P/B-anchored-to-ROE and peer-comparison approach below is the playbook's mandated substitute.)*

NTM P/E (d4, calendarized) **11.6x**; P/B **2.29x** (2.16x ex-AOCI). Peer set (same live snapshot, consistent methodology): CB 1.71x P/B / 14.8% ROE / 11.6x P/E; HIG 1.75x / 22.1% / 9.2x; ACGL 1.39x / 19.9% / 9.8x; WRB 2.68x / 20.2% / 13.8x; CINF 1.50x / 21.5% / 18.3x. TRV's P/B sits at the high end of this set but is supported by a genuinely-improving (not just cat-lucky) underlying combined ratio. Reverse-DCF sense: at 2.2x book against a currently-elevated ~20-25% core ROE, the market is *not* extrapolating peak profitability indefinitely — it is roughly consistent with core ROE settling in the mid-teens, which is a reasonable, not aggressive, assumption given the underlying-ratio evidence in §4. **[Corrected 2026-10-06: 'mid-teens' is not what 2.2x book prices at a cost of equity consistent with a 5.17% 10-year Treasury: the justified P/B = (ROE-g)/(COE-g) with g=3% requires a sustained ROE of 15.1% / 16.7% / 17.9% at COE of 8.3% / 9.0% / 9.5% (V1 used a 7.74% COE and so got 14.1%); the evidence-based base is about 17.5%, so implied_vs_base is in_line, not below]**

## 8. Bull case / Bear case
**Bull:** (1) Underlying combined ratio is stable-to-improving even after stripping cat/reserve noise — real pricing discipline, not just luck. (2) Aggressive, well-covered capital return ($3.9B buyback authorization, rising dividend, book value compounding at 5-6%/yr ex the cyclicality). (3) Diversified three-segment model with only one segment (Bond & Specialty) showing underlying deterioration.
**Bear:** (1) ~$2B of the 1H26 pre-tax earnings improvement vs 1H25 is a catastrophe base effect (LA wildfires) that will not repeat — 2027 comps get harder. (2) Reserve releases ($991M pre-tax 1H26) are running above historical norms across multiple segments; a reversal to flat/adverse development would remove a real chunk of "beat" (avg EPS surprise +57.9% over the last 8 quarters per d4 — a magnitude that itself signals estimates/base-effects are unusually distorted, not stable outperformance). (3) Hard-market commercial pricing cycles historically compress once capital rebuilds (which is exactly what's happening industry-wide); Bond & Specialty's underlying ratio is already worsening.

## 9. Key risks & kill criteria — thesis is invalidated if any of the following are observed (source: company 10-Q/8-K disclosures each quarter)
1. Consolidated combined ratio > 95% for two consecutive quarters (vs 83.6% now).
2. Net favorable prior-year reserve development flips to **net adverse** in Business Insurance or Bond & Specialty for two consecutive quarters.
3. Core ROE < 12% for two consecutive quarters (vs ~19-25% now).
4. Personal Insurance underlying combined ratio rises back above ~90%.
5. A single catastrophe/accumulation net of reinsurance exceeding ~15-20% of shareholders' equity ($33.1B, i.e. >$5-6.6B net).

## 10. Catalysts & calendar
Next earnings: **2026-10-16** (Q3 2026 — falls inside Atlantic hurricane season, the highest-cat-risk reporting quarter). No investor day or index event identified in this pass.

## 11. Red-flag scan
No auditor change (no Item 4.01 8-K in the filing history reviewed), no restatement, no going-concern or material-weakness language found, no SEC/DOJ investigation disclosed. "No material changes" to FY2025 10-K risk factors per the Q2-26 10-Q. Standard, long-managed asbestos/environmental legacy exposure only. 40 Form 4 filings by insiders between 2026-02-19 and 2026-08-31 (SEC EDGAR) — buy/sell direction not individually tabulated in this pass; no Schedule 13D/G activist stake or cluster-sale 8-K surfaced.

## 12. Sources
1. TRV Q2 2026 earnings release (8-K Ex-99.1, filed 2026-07-17): https://www.sec.gov/Archives/edgar/data/86312/000008631226000143/a991pressrelease63026.htm
2. TRV Q2 2026 10-Q (filed 2026-07-17): https://www.sec.gov/Archives/edgar/data/0000086312/000008631226000145/trv-20260630.htm
3. TRV Q4/FY2025 earnings release (8-K Ex-99.1, filed 2026-01-21): https://www.sec.gov/Archives/edgar/data/86312/000008631226000008/a991pressrelease123125.htm
4. TRV FY2025 10-K (filed 2026-02-12): https://www.sec.gov/Archives/edgar/data/0000086312/000008631226000065/trv-20251231.htm
5. TRV SEC submissions index: https://data.sec.gov/submissions/CIK0000086312.json
6. TRV SEC XBRL company facts (revenue/NI/EPS/equity/OCF/SBC/buybacks time series): https://data.sec.gov/api/xbrl/companyfacts/CIK0000086312.json
7. TRV Form 4 filing history (SEC EDGAR atom feed): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000086312&type=4&output=atom
8. v4 internal: `data/lead_prelim_rank.csv`, `data/d4_live_snapshot.parquet` (quant context, analyst estimates, peer snapshot)


## Re-assessment (RA14, 2026-10-06)

**Scope.** Price $363.04 as of 25 Sep 2026; EDGAR checked to 6 Oct 2026; 10-year Treasury 5.17% (FRED DGS10, 25 Sep 2026); Fed funds 3.75-4.00%; equity risk premium 5.0% (4.5-5.5% tested). Insurer: P/B against ROE, not a DCF on cash flow. Research only.

**Recency.** After the Q2 release (acc 0000086312-26-000143) and 10-Q (acc 0000086312-26-000145): 8-K 24 Jul (acc 0001193125-26-316247, Item 8.01) underwriting agreement for $750M of 4.950% senior notes due 2031 (prospectus supplement acc 0001193125-26-312518; net proceeds about $744M for general corporate purposes); 8-K 7 Aug (acc 0001104659-26-092716, Item 5.02) election of Anthony Jabbour as the ninth director, benign; Form 3/A, 13F-HR and N-PX, routine. No merger, no 13D, no rating action found. Travelers gives no quantitative guidance (confirmed again in the Q2 release). Q2 facts re-verified verbatim: combined ratio 83.6% (90.3%), underlying 84.1% (84.7%), catastrophes $518M ($927M), net favourable development $578M ($315M), core ROE 24.9%, book value per share $158.81 (adjusted $168.20), 4.3M shares repurchased at an average $304.06 for $1.311B, dividend declared $1.25 per share, debt-to-capital 21.5%.

### Corrections

| # | Wrong or stale text | Corrected value | Source | Effect |
|---|---|---|---|---|
| 1 | V1 cost of equity 7.74% (beta 0.62 x ERP 4.14%) behind "implied ROE 14.1%" | At a 5.17% 10-year Treasury: 8.3% (V1 beta, ERP 5.0%), **9.0% central (beta 0.77, the P&C peer range 0.6-0.9)**, 9.5%. Justified P/B = (ROE - g)/(COE - g), g = 3%: the price of 2.286x book ($363.04 / $158.81; 2.16x adjusted book) requires a sustained **ROE of 15.1% / 16.7% / 17.9%** | FRED DGS10; Q2 release | Required ROE +2.6 pts vs V1 (central) |
| 2 | "Core ROE settling in the mid-teens is a reasonable assumption" (§7) | Evidence: FY2025 core ROE 19.4% (catastrophes 8.4 pts, favourable development 2.4 pts, underlying combined ratio 83.9%); FY2024 17.2%. LTM 24.2% is flattered by 1H26 catastrophes of $1.279B (6.0 pts) vs $3.193B (14.8 pts) and development of 4.6 pts. Normalised at underlying 84.7%, catastrophes 8.0 pts (FY2024-25 average), development 2.4 pts: combined ratio about 90.3%, underwriting gain about $4.3B on about $44B earned premium, plus net investment income about $4.4B, less interest about $0.45B, tax about 19%: core ROE about 19% today. The cycle softens (Business Insurance renewal premium change 4.8%, Bond & Specialty underlying ratio +1.8 pts), so the 10-year base is **about 17.5% (range 15-19%)** | Q4 2025 release acc 0000086312-26-000008; Q2 release; own arithmetic | **implied_vs_base: in_line** (16.7% vs 17.5%; below only if COE is 8.3% or less) |
| 3 | Value on the base path | Justified P/B at 17.5% ROE: 2.42x (COE 9.0%) = $384, +6% vs price; range $318 (15% ROE) to $423 (19%) | Own arithmetic | Price is inside the fair range, no cushion; P/B is in the 97.7th percentile of its own history (V1) |
| 4 | V1 scenarios bear -7.8% / base -0.5% / bull +17.2% | V1's base uses ROE 12.1% (own-history median) and exit P/B 1.46x, below FY2024-25 delivery (17.2%, 19.4%). Restated (ROE on opening book per share $158.81; 85% of net income returned, buybacks at 2.3x book; dividend $5.00 growing 7% a year): **bear ROE 11% / exit 1.4x = -9.5% a year; base ROE 17.5% / exit 2.15x = +7.3% (book per share $200.9, EPS about $35 in year 3); bull ROE 21% / exit 2.6x = +16.2%; probability-weighted (30/45/25) +4.5%** | Own arithmetic | Base below cost of equity |
| 5 | Capital position | Buybacks in Q2 averaged $304.06, 16% below today's price; authorisation remaining $3.915B; new $750M notes lift debt-to-capital from 21.5% to about 22.9% (ceiling 25%), limiting extra debt-funded buyback room | Q2 release; 8-K 24 Jul | Supports payout but not above-trend |

### Verdict

**INCLUDE -> INCLUDE-SMALL.** At 2.29x book the price needs about the 17% ROE the business earns at mid-cycle, so there is no margin of safety to pay for full weight; the franchise (underlying combined ratio 84.1%, book value +5% in the half year, repurchases) and the lack of any fired kill criterion keep it in the sleeve at half weight. Next test: Q3 results on 16 Oct 2026 (hurricane season).

### Fields changed

verdict INCLUDE -> INCLUDE-SMALL; thesis_one_line (added); valuation_view_vs_v1 (added: implied_vs_base in_line, dossier_view fair); scenario_returns_3y (bear -0.095 / base +0.073 / bull +0.162) and scenario_basis; kill_criteria (added a sixth: underlying combined ratio); key_adverse_facts; data_conflicts; confidence_in_thesis. Unchanged: business description, quarterly table, red-flag scan, §5.
