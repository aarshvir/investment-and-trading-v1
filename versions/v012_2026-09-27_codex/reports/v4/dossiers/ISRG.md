# ISRG — Intuitive Surgical, Inc. — Diligence Dossier (Agent F53, wave 3)

## 1. Verdict
**INCLUDE-SMALL** — the global leader in robotic-assisted surgery, with a large recurring instrument/accessory revenue base and genuine procedure-volume growth, but priced at a rich absolute multiple with two real, evidenced risks the triage did not surface: an active antitrust appeal over instrument-repair tying, and a disclosed ~30% 2026 drawdown tied to Medtronic's Hugo launch. Half weight given the lack of valuation cushion and unresolved litigation. Horizon: 24–36 months.

## 2. Business in plain English
Intuitive makes the da Vinci surgical robot (and the Ion bronchoscopy platform) and sells it to hospitals, then earns recurring revenue from the single-use/limited-use instruments ("EndoWrists") and service contracts consumed in every procedure. Surgeons use it for urology, gynecology, general surgery and increasingly thoracic/bronchoscopic procedures. Moat: a large (and growing) installed base of systems creates a switching-cost and training moat; instruments and service are ~80% of revenue and recur with every procedure regardless of system sales.

## 3. Why the model likes it — durable or artefact?
`b1_live_scores.csv`: pct_roe 0.587, pct_ocf_a 0.833 — solidly good but not extreme (ROE is lower than a typical "quality 5" name because ISRG carries a very large cash/investments balance that dilutes ROE). Value percentiles are low (pct_ep 0.080, pct_fcfp 0.079) — correctly flags an expensive stock. Momentum (mom_12_1 percentile 0.13) and SUE (0.077) are weak — the stock has lagged over the past year and recent earnings surprises have been unremarkable-to-negative, consistent with the ~30% 2026 drawdown discussed below. This is a case where the "quality" score is durable (real moat, real recurring revenue) but the model's own momentum/earnings-surprise signals already reflect real, disclosed bad news — not an artefact.

## 4. Last eight quarters (SEC XBRL, USD millions except EPS; GAAP)
| Quarter | Revenue | YoY | Op. margin | Diluted EPS (GAAP) |
|---|---|---|---|---|
| Q3'24 | 2,038.1 | +17.1% | 28.3% | 1.56 |
| Q4'24 | 2,413.5* | +20.9%* | 30.4%* | 1.89* |
| Q1'25 | 2,253.4 | +19.2% | 25.7% | 1.92 |
| Q2'25 | 2,440.0 | +21.4% | 30.5% | 1.81 |
| Q3'25 | 2,505.1 | +22.9% | 30.3% | 1.95 |
| Q4'25 | 2,866.2* | +18.7%* | 30.2%* | 2.20* |
| Q1'26 | 2,770.8 | +23.0% | 30.9% | 2.28 |
| Q2'26 | 2,892.3 | +18.5% | 33.6% | 2.29 |

*Q4 figures derived as FY − 9-month YTD (FY2024 10-K minus 9-mo 2024 10-Q; FY2025 10-K minus 9-mo 2025 10-Q); not separately XBRL-tagged. Source: `data.sec.gov/api/xbrl/companyfacts/CIK0001035267.json`. Worldwide procedure growth (company-disclosed volume metric, not a GAAP figure): Q2 2026 ≈ +16% YoY (da Vinci ≈+15%, Ion ≈+36%); Q4 2025 ≈+18% YoY (da Vinci ≈+17%, Ion ≈+44%) — procedure growth is decelerating quarter over quarter, which the company itself guided for (see §5).

## 5. Guidance track record (company guides procedure-growth % and gross-margin %, not EPS)
| Release (date) | FY2026 da Vinci procedure growth | Non-GAAP gross margin |
|---|---|---|
| Q4/FY2025 (Jan 2026 release) | 13–15% (vs. 18% actually delivered in 2025 — guided deceleration) | 67–68% |
| Q1 2026 (Apr 2026) | 13.5–15.5% | maintained |
| Q2 2026 (Jul 2026) | 13.5–15.5% (maintained, narrowed toward midpoint on US patient-behavior shifts and international capital-spending pressure), gross-margin guidance raised | raised |

Verdict: **maintained/modestly narrowed**, not clearly raised, across the year — a materially slower growth algorithm than 2025's realized 18%. Sources: 8-K ex-99.1 releases, accessions 0001035267-26-000006 (Q4'25) and 0001035267-26-000047 (Q2'26); WebSearch corroboration of the Jan-2026 initial guide (company IR site).

## 6. Earnings quality & balance sheet
- **FCF conversion:** FY2025 OCF $3,030.5M − capex (`PaymentsToAcquireProductiveAssets`) $539.8M = FCF ≈ $2,490.7M vs GAAP NI $2,856.0M → FCF/NI ≈ 87%. TTM (Q3'25–Q2'26): OCF ≈ $3,706.4M, capex ≈ $483.8M, FCF ≈ $3,222.6M vs TTM NI ≈ $3,138.8M → FCF/NI ≈ 103%.
- **SBC:** $419.4M in H1 2026 alone (vs. $381.4M H1 2025) — SBC is running ≈7–8% of revenue, a real (not disqualifying) GAAP-vs-adjusted-earnings gap driver typical of the sector.
- **Balance sheet (consolidated, 10-Q Q2 2026):** cash $2,760.4M (note: d4's vendor "totalCash" of $5.2B includes short-term marketable-securities investments beyond the strict cash line — a data-conflict worth flagging, resolved in ISRG's favor either way since it carries **no long-term debt** — `LongTermDebt`/`LongTermDebtNoncurrent` tags are absent from XBRL, consistent with a debt-free balance sheet). Stockholders' equity $18,168.4M.
- **Share count:** 358.4M (Apr 2025) → 353.3M (Jul 2026), down ~1.4% — modest buybacks, mostly offsetting SBC dilution rather than aggressively shrinking the count.
- **M&A:** none material; the company continues to invest in R&D (Ion, da Vinci 5) organically.

## 7. Valuation snapshot & reverse DCF
Price $405.18 (25 Sep 2026 close). This is well off a 2026 high — third-party coverage (Motley Fool, TIKR, July 2026) describes an ISRG decline of roughly 30% during 2026, attributed to the Medtronic Hugo competitive launch and guidance/procedure-growth deceleration concerns — consistent with the weak b1 momentum/SUE percentiles above. NTM P/E ≈ 34.5x (on consensus adjusted forward EPS), TTM GAAP P/E ≈ 46.5x — a large GAAP-vs-adjusted gap driven by SBC. **No V1 row exists for ISRG** → `v1_verdict = null`.
Reverse DCF (10-yr FCF growth + terminal 3.5%, WACC 8.5%, EV $136.05B, TTM FCF $3.223B base): **implied 10-yr FCF growth ≈ 12.6%** (range 9.5–15.3% across WACC 7.5–9.5%/terminal 3–4%). My base case: procedure growth guided at 13.5–15.5% for 2026 but explicitly decelerating from 18% (2025) as the installed base matures and China/international capital spending stays soft; a reasonable 10-year average, allowing for continued deceleration plus margin/buyback contribution to EPS, is **≈11–13%/yr**. **implied_vs_base = in_line** (implied sits within, not clearly above, my base range) — but this is a thin, judgment-call reconciliation, not a comfortable margin of safety, which is why the verdict is INCLUDE-SMALL rather than INCLUDE.

## 8. Bull case / Bear case
**Bull:** (1) da Vinci 5 system placements grew ~37% YoY in Q2 2026 (246 vs. 180 units) — an active upgrade cycle that raises the recurring-instrument base; (2) Ion (bronchoscopy) procedure growth of +36% YoY shows a second, earlier-stage growth leg; (3) debt-free balance sheet with a large net-cash position gives full strategic flexibility.
**Bear:** (1) an antitrust jury found evidence of tying/exclusive dealing in the EndoWrist repair market (Rebotix Repair v. Intuitive, N.D. Cal.; summary judgment for Intuitive denied, case settled shortly before trial in 2025); a related case, Restore Robotics Repairs LLC v. Intuitive Surgical, was on appeal at the 11th Circuit as of a December 2025 filing — an adverse appellate outcome could force ISRG to open its high-margin instrument-repair/service market, which the triage's "no red flags" call missed entirely; (2) Medtronic's Hugo and J&J's Ottava are now real, launched competitors, not theoretical ones, and the stock has already re-rated down ~30% in 2026 partly on this; (3) management itself is guiding a sharp deceleration in procedure growth (18%→13-15%) and flagged China-specific capital-spending headwinds.

## 9. Key risks & kill criteria (measurable)
1. Worldwide da Vinci procedure growth < 10% YoY for two consecutive quarters (vs. guided 13.5–15.5% for FY2026).
2. An adverse or unfavorable-settlement outcome in the Restore Robotics 11th Circuit appeal that opens the EndoWrist repair/service market to third parties.
3. Full-year gross-margin guidance cut below the current 67–68% (non-GAAP) range.
4. Two consecutive quarters of da Vinci system placement growth (units) turning negative YoY (a leading indicator ahead of the recurring-revenue base).
5. Net debt/leverage — not applicable today (debt-free); this kill criterion is instead framed as: a debt-funded acquisition or buyback program that takes net cash negative would remove the balance-sheet cushion and should trigger a full re-review.

## 10. Catalysts & calendar
Next earnings: **2026-10-20** (Q3 2026, per `d4_live_snapshot`).

## 11. Red-flag scan
- **Litigation (material, ongoing):** Restore Robotics Repairs LLC v. Intuitive Surgical Inc., 11th Circuit docket 25-14202 (appeal filed per Justia docket, referenced Dec 2025) — antitrust tying/exclusive-dealing claims over EndoWrist repair, following a related case (Rebotix Repair) in which a federal judge denied summary judgment, finding a jury could conclude Intuitive engaged in tying/exclusive dealing to maintain monopoly power; that case settled in 2025. **This dossier opened and read the actual case dockets/rulings cited (FindLaw, MLex, Justia), not a news summary alone**, per the wave-3 mandatory requirement.
- **Auditor:** not independently confirmed in this pass (time-boxed); no restatement or material-weakness disclosure found in available search results — data-conflict/limitation flag: auditor name unconfirmed from a primary source.
- **Competitive:** Medtronic Hugo and J&J Ottava are now marketed competitors; this is disclosed in ISRG's own risk factors and is reflected in the 2026 share-price decline.
- **Insider selling:** not independently checked against primary Form 4s in this pass (time-boxed) — flagged as a coverage gap, not a finding.

## 12. Sources
1. SEC EDGAR submissions/company facts, CIK 0001035267: `data.sec.gov/submissions/CIK0001035267.json`, `data.sec.gov/api/xbrl/companyfacts/CIK0001035267.json` (retrieved 2026-09-26).
2. 10-K FY2025, filed 2026-02-03, accession 0001035267-26-000010; 10-Q Q1 2026 (0001035267-26-000032); 10-Q Q2 2026 (0001035267-26-000058).
3. 8-K earnings releases: Q4/FY2025 (accession 0001035267-26-000006/000008/000010 family, ex-99.1); Q2 2026 (0001035267-26-000047, ex-99.1).
4. Rebotix Repair LLC v. Intuitive Surgical, Inc. — case docket/rulings (Law360, MLex, N.D. Cal.); Restore Robotics Repairs LLC v. Intuitive Surgical Inc., 11th Cir. docket 25-14202 (Justia).
5. Seeking Alpha (2026-08), TIKR.com and Motley Fool (2026-07) commentary on Q2 2026 results and the 2026 share-price decline — secondary sources, used only for narrative color, not for any GAAP figure.
6. `v4/data/b1_live_scores.csv`, `v4/data/d4_live_snapshot.parquet` (as_of 2026-09-25).

## 13. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (10-Q filed 2026-07-21, period ended 2026-06-30). Events checked to 2026-09-25 close. GAAP figures used throughout except where labelled "non-GAAP"/"adjusted" (company-defined, reconciled in its releases). Litigation dates and case status are taken from the case dockets/rulings cited above, not from news summaries alone. This is research, not personal investment advice.
