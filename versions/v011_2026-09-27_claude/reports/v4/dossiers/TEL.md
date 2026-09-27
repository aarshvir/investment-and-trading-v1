# TE Connectivity plc (TEL) — Fundamental Diligence Dossier

**Verdict: INCLUDE** — 12–36 month thesis horizon.
One-sentence reason: a diversified connector/sensor leader is riding a genuine, backlog-confirmed AI-datacenter and broader-electrification demand cycle (orders +$1B YoY to $5.7B in the latest quarter) while the reverse-DCF implies only ≈3.3% ten-year FCF growth versus a reasonable ≈7% base case — a real valuation cushion — with the one identified red flag (a DDTC export-control self-disclosure) being a named, bounded, non-existential risk rather than a reason to pass.

## 1. Business in plain English
TE Connectivity makes connectors, sensors and cable assemblies that let electrical signals and power move reliably between components — sold into automotive (wiring harnesses, EV high-voltage connectors), industrial equipment, aerospace/defense, and, increasingly, AI datacenter and broader digital-infrastructure/energy customers. It does not make chips or systems; it makes the physical interconnect layer nearly every one of those systems needs, which gives it a diversified, moderately capital-intensive, high-switching-cost business (connectors are qualified into a customer's design and rarely re-specified) rather than a single-end-market bet.

## 2. Why the model likes it / is it durable
b1 composite percentile 0.61 (decile 7, quintile 4 — solidly upper-tier), driven by strong Quality (gp_a pct 0.47, roe pct 0.48) and Momentum (mom_12_1 pct 0.74) alongside decent Value (ep pct 0.76, fcfp pct 0.83). live_rank 196. This is a broad, multi-family score (n_families=4 of 4), not a single-factor artefact — the durability case is the AI-datacenter/electrification order book below, which is a real, filed acceleration rather than a one-off re-rating.

## 3. Last 6 quarters (fiscal quarters, TE's fiscal year ends the last Friday of September; $M except EPS; GAAP)
| Quarter end | Revenue | Operating income | Op margin | Net income | Diluted EPS (GAAP) |
|---|---|---|---|---|---|
| 2024-12-27 (FQ1'25) | 3,836.0 | 690.0 | 18.0% | 528.0 | 1.75 |
| 2025-03-28 (FQ2'25) | 4,143.0 | 748.0 | 18.1% | **13.0** | 0.04 |
| 2025-06-27 (FQ3'25) | 4,534.0 | 857.0 | 18.9% | 638.0 | 2.14 |
| 2025-12-26 (FQ1'26) | 4,669.0 | 963.0 | 20.6% | 750.0 | 2.53 |
| 2026-03-27 (FQ2'26) | 4,744.0 | 954.0 | 20.1% | 855.0 | 2.90 |
| 2026-06-26 (FQ3'26) | **5,160.0** | 981.0 | 19.0% | 748.0 | 2.55 |

Source: SEC XBRL companyfacts (data.sec.gov/api/xbrl/companyfacts/CIK0001385157.json), cross-checked against the FQ3'26 10-Q (period end 2026-06-26, filed 2026-07-24, accession 0001104659-26-086509). **FQ2'25 net income of $13M is a genuine, filed one-off**, not an error: TE incurred a large one-time non-cash tax charge that quarter tied to (a) changes in tax law affecting the realizability of deferred tax assets associated with a Swiss subsidiary's ten-year tax credit, following January 2025 OECD global-minimum-tax guidance, and (b) costs of the company's 2025 change of place of incorporation from Switzerland to Ireland (per TE's FY2025 10-K and Q1/Q2 FY2025 disclosures) — confirmed via WebSearch of company/press disclosures, not independently re-read line-by-line in the 10-K in this pass. FQ3'26 revenue of $5.16B (+14% YoY, 12% organic) is a genuine acceleration versus the FQ3'25 print.

## 4. Guidance track record
Per the FQ3'26 earnings release (8-K, accession 0001104659-26-085589, PRNewswire coverage 2026-07-22): TE delivered results *above* its own guidance, with adjusted EPS of $2.94 (guided range beaten) on revenue of $5.16B (vs. Street $5.01B). Orders rose to $5.7B, up more than $1B YoY, with management stating the original $3B AI-cloud-revenue target set for calendar 2027 is now expected to be reached ahead of schedule ("shift left"). Full-year FY2026 guidance (given across the last several releases) has been raised each quarter this fiscal year and now assumes ~15% sales growth and 20%+ adjusted EPS growth — a consistent raise-and-beat pattern, not a single-quarter pop.

## 5. Balance sheet, cash conversion and capital allocation
All figures below are **consolidated** TE Connectivity plc figures, from the FQ3'26 10-Q condensed consolidated balance sheet (period end 2026-06-26, accession 0001104659-26-086509):
- Consolidated cash and cash equivalents: $1,239M. Consolidated long-term debt (noncurrent): $5,530M (the XBRL `LongTermDebtCurrent` tag returned only stale 2016-era values in this pull, so the current portion of long-term debt/commercial paper was not separately cross-tied in this pass — flagged rather than asserted as zero). **Consolidated net debt, noncurrent-debt basis, ≈ $4,291M** (a conservative/approximate figure given the current-portion caveat above).
- Consolidated total assets $26,070M; consolidated goodwill $7,403M (28% of assets — meaningfully lower goodwill intensity than a pure serial-acquirer profile).
- TTM (FQ4'25–FQ3'26) consolidated operating cash flow ≈$4,418M, consolidated capex ≈$1,103M, **consolidated FCF ≈$3,315M** (FCF/NI ≈ well above 100% on a TTM basis once the FQ2'25 tax-charge quarter rolls out of the trailing window — cash conversion is not distorted by that one-off the way GAAP EPS was).
- Estimated TTM consolidated EBITDA (TTM operating income ≈$3,814M + an estimated ~$700–800M D&A, not separately re-verified) ≈$4,500–4,600M → **consolidated net debt/EBITDA ≈0.9–1.0x**, low leverage.
- Capital return: buybacks ran ~$1.35B over the trailing nine months to FQ3'26 (`PaymentsForRepurchaseOfCommonStock`), plus a regular dividend (TTM dividend yield ≈1.9% at the current $218.59 price, per b1_live_scores.csv).

## 6. Valuation — reverse DCF (no V1 systematic valuation row for TEL: `v1_valuation_table.csv` has no TEL entry, so v1_verdict is null)
Inputs: EV ≈ $67,575.7M (market cap $63,284.7M [b1_live_scores.csv, as_of 2026-09-25, px $218.59] + consolidated net debt ≈$4,291M); TTM consolidated FCF $3,315M (FCF yield on EV 4.9%); WACC 8.5%; terminal growth 3.5%; 10-year horizon, solved numerically.
**Implied 10-year FCF growth rate: ≈3.3%/year.**
- **Bear case (10y FCF CAGR ≈ 0%):** the AI-datacenter order surge proves cyclical/pull-forward rather than a structural base-rate shift, auto/industrial end-markets (still the majority of revenue) stay soft on EV-capex digestion, and margin gains reverse.
- **Base case (10y FCF CAGR ≈ 7%):** current mid-teens guided growth (largely AI/data-center- and electrification-driven) normalises toward mid-single-digit organic over the decade as the AI capex cycle matures, with continued modest buyback-driven EPS/FCF-per-share tailwind.
- **Bull case (10y FCF CAGR ≈ 14%):** AI-datacenter connector content per rack keeps rising, the $3B AI-cloud target is reached well ahead of 2027 and becomes a larger, durable base, and auto-electrification content-per-vehicle growth resumes.
**Implied vs. base: BELOW.** 3.3% is well below the 7% base case — the current mid-teens growth guide is not being extrapolated into the price, which is the core reason this clears a full INCLUDE rather than half-weight, subject to the DDTC item below.

### 3-year scenario returns (annualised total return from $218.59; TTM dividend yield ≈1.9%)
| Scenario | 3y FCF CAGR | Exit EV/FCF | Annualised return |
|---|---|---|---|
| Bear | ≈ 0%/yr | 15x (de-rate from 20.4x entry) | **≈ −7.8%/yr** |
| Base | ≈ 7%/yr | 20x | **≈ +8.2%/yr** |
| Bull | ≈ 14%/yr | 23x | **≈ +20.6%/yr** |

## 7. Bull case
1. Orders up >$1B YoY to $5.7B in the latest quarter with management explicitly pulling forward its AI-cloud revenue target — a real, order-book-confirmed demand signal, not narrative.
2. Low leverage (consolidated net debt/EBITDA ≈0.9–1.0x) and strong FCF give room to keep buying back stock and funding capacity expansion for AI/datacenter content without balance-sheet strain.
3. Diversified end-market exposure (auto, industrial, aerospace/defense, AI/energy) means no single cyclical downturn (e.g., an auto slowdown) sinks the whole business, unlike a pure-play connector name.

## 8. Bear case
1. TE has made a voluntary self-disclosure to the U.S. State Department's Directorate of Defense Trade Controls (DDTC) regarding past compliance with U.S. trade-control regulations and is cooperating with an ongoing investigation; the company states it cannot predict timing or outcome, and an unfavorable outcome could include fines or penalties (per TE's own FY2025 Form 10-K risk-factor disclosure, accession 0001104659-25-109150, cross-checked via SEC EDGAR search; the specific page was not independently re-opened line-by-line in this pass).
2. Automotive/industrial still make up the majority of revenue; the current headline growth rate is disproportionately an AI/data-center story, and a normal auto-production or industrial-capex downturn could offset that tailwind.
3. The FQ2'25 net-income collapse to $13M shows real one-time-tax-charge risk tied to the company's recent Ireland redomicile and evolving global minimum-tax rules — a structural item that could recur if tax law changes again.

## 9. Key risks & kill criteria
1. The DDTC export-control investigation results in a fine, penalty or remediation order exceeding $50M, or a formal enforcement action is announced.
2. AI/data-center order momentum reverses (orders decline sequentially for two consecutive quarters) rather than continuing to pull the $3B FY2027 target forward.
3. Automotive or Industrial segment organic revenue growth turns negative for two consecutive quarters.
4. Consolidated net debt/EBITDA rises above 2.0x (from ≈0.9–1.0x today) without a clearly disclosed reason (e.g., large debt-funded M&A).
5. A further one-time tax or legal charge exceeding $500M recurs within the next four quarters, indicating the Ireland-redomicile tax risk is not resolved.

## 10. Catalysts & calendar
- Next earnings: fiscal Q4/full-year 2026, estimated **~28-Oct-2026** (pattern-based on the prior year's Q4/annual results release date of 2025-10-29; not yet confirmed, no accession number to cite since this is a forward estimate).
- Resolution (favorable or unfavorable) of the DDTC investigation is the next material, if unscheduled, catalyst/risk event.

## 11. Red-flag scan
- **DDTC voluntary self-disclosure / ongoing export-control investigation** — a real, disclosed, unresolved matter (see §8.1). This is the dossier's single most important adverse fact.
- One-time tax charge in FQ2'25 (Ireland redomicile / OECD global minimum tax) already flagged in §3 — resolved as a discrete event but the underlying tax-law sensitivity is structural, not fully closed.
- No auditor changes, restatements, or going-concern language found in the filings and news reviewed in this pass.
- Current-portion-of-long-term-debt figure not independently cross-tied in this pass (see §5) — flagged rather than asserted.
- Insider Form 4 filings were not pulled/reviewed in this pass (time-boxed).

## 12. Data basis, recency and disclaimer
All balance-sheet, debt and cash figures above are **consolidated** TE Connectivity plc figures (single reporting entity; not a bank/insurer with regulatory-capital disclosures). Most recent period incorporated: FQ3 2026 10-Q, period ended 2026-06-26, filed 2026-07-24 (accession 0001104659-26-086509). Events and news checked to 2026-09-25. GAAP figures used throughout except where guidance is explicitly labelled non-GAAP/adjusted (management's own basis). This is research, not investment advice: not a recommendation, and not personalised to any individual's circumstances.

## Sources
1. SEC EDGAR, TE Connectivity plc 10-Q, period 2026-06-26, filed 2026-07-24, accession 0001104659-26-086509.
2. SEC EDGAR, TE Connectivity plc 8-K exhibit (FQ3 2026 earnings release), filed 2026-07-22, accession 0001104659-26-085589; PRNewswire, "TE Connectivity delivers results above guidance with 14% sales growth and 19% EPS growth in third quarter of fiscal 2026," 2026-07-22.
3. TE Connectivity FY2025 10-K risk factors (DDTC voluntary disclosure) and FY2025 annual report, cross-checked via WebSearch summaries of SEC EDGAR filing content (globalinvestigationsreview.com coverage), not independently re-opened line-by-line in this pass.
4. data.sec.gov/api/xbrl/companyfacts/CIK0001385157.json (XBRL quarterly figures used in §3/§5).
5. v4/data/b1_live_scores.csv (as_of 2026-09-25) — quant factor context.
6. v4/outputs/Q11_triage.json — prior triage entry for TEL.
