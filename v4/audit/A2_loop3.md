# A2 loop 3 audit — investment-committee perspective

**Total: 78 / 100.** Verdict: the diligence and process discipline are genuinely strong (whole-index triage, pre-committed
amendments, 10/10 independently re-checked facts across the nine new holdings pass) but a self-flagged-as-corrupted data
point (PGR's NTM P/E) reached the flagship table and dashboard unfixed, and the report's own claim that the sleeve weights
"sum to 100%" is false by 0.3 points once you actually add the displayed numbers — exactly the kind of thing this audit
exists to catch, and exactly the kind of thing a real IC would catch on page one. Loop 2's A2 score (89) is not sustained
this loop because of these two concrete, reproducible defects, not because the diligence quality declined — diligence
quality, if anything, improved.

## 1. Criterion table

| # | Criterion | Score | Evidence | Gap(s) |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 7 | PGR's own dossier (F23) explicitly says its d4 `pe_ntm` field is corrupted and "should not be used... under any circumstance"; the report/dashboard used it anyway (0.3x, see must-fix #1). Every other spot-checked number (AMP AUM, BX AUM, CRH Arcosa terms, PGR Florida credit, LVS S&P upgrade and ownership, CMCSA spin-off, EG ADC, BR CQG, NOW Moveworks) traced correctly. | One live, unflagged, decision-relevant bad number in the deliverable itself. |
| 2 | Backtest & validation rigour | 8 | Not my primary focus this loop (A1's lane); B1X/B1 register unchanged since loop 2, still shows no edge, point-in-time membership. | Not independently re-verified this loop beyond spot use. |
| 3 | Calibration & honesty | 8 | Adverse facts are surfaced prominently and specifically (NOW's two open DOJ matters, LVS's controlled-company structure, EG's two reserve surprises in five quarters, AMP's thin equity base, CMCSA's unfinalized spin terms) rather than buried. | Minor: dossier "implied growth" figures (e.g. EG bear/base/bull −8%/+4%/+9%) and the report's total-return bear/base/bull column (−10%/+15%/+28%) are different constructs (growth assumption vs. total return with multiple change); confirmed both trace correctly to source (F22_summary.json) but the report never explains they are different quantities. |
| 4 | Company-level diligence | 9 | I independently checked ≥1 load-bearing, primary-sourced claim in each of 8 of the 9 new dossiers (LVS ×2, PGR, CRH, CMCSA, EG, BR, NOW, AMP, BX ×2 — 10 checks total) against SEC filings, company press releases and news wires. All 10 passed exactly (see below). Adverse facts are specific and dated, not generic. | Appendix A.5 still shows "not yet checked" for all 9 new holdings, understating the audit coverage that (per this loop) now actually exists informally; needs a formal DA6 pass. |
| 5 | Valuation rigour | 7 | Methods are consistent and well-reconciled where V1 exists (AMP, CMCSA — both show explicit V1-vs-dossier reconciliation with a stated view on which is more conservative); reverse-DCF used consistently for the 7 non-V1 names with disclosed discount-rate assumptions. | The PGR NTM P/E error (must-fix #1) sits squarely in this criterion — a full-conviction holding's headline multiple is nonsensical in the published table. |
| 6 | Portfolio construction & risk | 8 | I independently recomputed the sector-cap constraint from raw weights in `outputs/lead_portfolio_build.json`: Financials = MTB+AMP+PGR+SYF+BX+EG = 7.6584+6.0851+5.8924+1.5+1.5+2.3642 = 25.0001% — matches the stated 25% cap exactly, confirming the solve is genuinely binding, not approximate. Raw weights sum to 1.0000000000000002 (correct). | The *displayed*, rounded weight column sums to 100.3%, contradicting the report's own caption (must-fix #2) — a solver-vs-presentation gap, not a solver error. |
| 7 | Strategy coherence & mandate fit | 9 | The response to the owner's mid-run challenges (why no NVDA/MSFT; why not the whole index) is genuinely disciplined: STATE.md shows the growth-lane rule (g), the triage-advance rule (h), the volatility-gate removal (i), and the final-size rule (j) each written down with an explicit rationale tied to internal consistency (never to a specific ticker's return) before or concurrent with the results they govern. The lane path is honestly disclosed in code comments and STATE.md. | STATE.md's 12:38 entry states the size rule was written "before running the build" in the same breath as citing the approximate size of the eligible pool — a softer, but real, pre-registration-firewall gap (must-fix #3). Also, the report never flags in the reader-facing table which holdings entered via the lane vs. the original top-70 gate (must-fix #5). |
| 8 | Implementation & monitoring | 8 | §8/§9 UAE-specific facts (estate tax, withholding, broker entities) and the weekly checklist are specific and actionable; three genuinely unanswerable items are labeled as such with workarounds, which is honest rather than a coverage gap dressed up as a "pass." | Not independently re-verified this loop (A3's lane). |
| 9 | Communication for the owner | 6 | The prose is answer-first and largely jargon-explained (§12 glossary is thorough). | A non-technical reader has no way to catch either the "0.3x P/E" (looks like an incredible bargain, is actually a data bug) or the false "sum to 100%" claim — both are exactly the kind of silent numeric error criterion 9 exists to prevent, and both are visible in the very table the owner is told to use to size positions (§9's per-$10,000 table). |
| 10 | Reproducibility & auditability | 8 | The register of independent checks (A.4) is genuinely extensive and I was able to trace the report's numbers back to `outputs/lead_portfolio_build.json`, `F22_summary.json` etc. without difficulty — reproducibility is real, not just claimed. | C1's "216 checked, 215 matched" consistency pass evidently checked report-vs-source-file agreement, not source-file plausibility — it would not have caught the PGR bug because the bug is upstream of C1's comparison (the source file itself is wrong, and C1 confirms the report faithfully reproduces the wrong source). A future C1 needs a sanity-bound pass (e.g., NTM P/E outside [3,60] flagged) as well as a source-matches-report pass. |

## 2. Must-fix to reach ≥95 (ranked by score impact)

1. **PGR's NTM P/E (0.3x, criteria 1/5/9).** Fix `code/lead_build_portfolio.py`'s unguarded `P['pe'] = S.loc[t,'pe_ntm']`; sanity-bound or override per-dossier where a dossier explicitly flags the field as corrupted; regenerate FINAL_REPORT.md §6 and dashboard/d4v.json; verify by grepping the regenerated outputs for the bad value.
2. **Rounded weights summing to 100.3% against a report caption claiming 100% (criteria 6/9).** Use largest-remainder rounding for the displayed column, or correct the caption; add an automated check on the *displayed*, not just raw, weights.
3. **Final-size tie-break rule's pre-registration firewall is soft (criterion 7).** Commit the rule to a separately timestamped file before the build script reads diligence outputs; disclose actual sequencing honestly rather than only asserting pre-commitment.
4. **Nine new holdings marked "not yet checked" in Appendix A.5 despite this loop's informal checks now covering 8 of them (criteria 4/10).** Run a formal DA6 pass mirroring DA4/DA5 and update the table.
5. **Lane-vs-top-70 eligibility path not flagged per holding in the reader-facing table (criterion 7/9).** Add a footnote (parallel to the existing ‡) marking which holdings entered via the lane/triage route.

## 3. Numbers I re-computed

| # | Number | In report | My recomputation | Pass/fail |
|---|---|---|---|---|
| 1 | Raw sleeve weights sum | implied 100% | 1.0000000000000002 (from `outputs/lead_portfolio_build.json`) | Pass |
| 2 | **Displayed (rounded) sleeve weights sum** | "sum to 100% of the sleeve" (FINAL_REPORT §6) | 100.3% (sum of the 20 published 0.1-point weights) | **Fail** |
| 3 | Financials sector weight (cap 25%) | 25% (cap, "verified after solving") | MTB 7.6584 + AMP 6.0851 + PGR 5.8924 + SYF 1.5 + BX 1.5 + EG 2.3642 = 25.0001% | Pass (binding exactly) |
| 4 | PGR NTM P/E | 0.3x (FINAL_REPORT §6; d4v.json `"pe": 0.27478`) | Dossier's own corrected figure: trailing P/E 10.3x; d4's `pe_ntm` field independently confirmed corrupted (matches dossier's own diagnosis of `pe_ntm=0.27`) | **Fail** |
| 5 | EG/BX scenario_returns_3y provenance | EG −10%/+15%/+28%; BX +0%/+16%/+23% (FINAL_REPORT §6) | `outputs/F22_summary.json`: EG bear −0.10/base 0.146/bull 0.28; BX bear 0.002/base 0.157/bull 0.227 | Pass (traces correctly, though the quantity differs from the dossier's prose "implied growth" figures — see criterion 3) |

## 4. Facts checked in dossiers (against primary sources)

| # | Dossier | Claim | Source checked | Pass/fail |
|---|---|---|---|---|
| 1 | LVS | S&P upgraded LVS/Sands China from BBB- to BBB in 2026, citing disciplined leverage (~2.5x through the Singapore expansion, 3.0x downgrade threshold) | S&P Global Ratings research update; GGRAsia, Casino.org (via web search) | Pass |
| 2 | LVS | Adelson family/trusts hold ~59.7% of voting power | Schedule 13D/A coverage (StockTitan), confirming 59.7% as of 22-Jul-2026 | Pass |
| 3 | PGR | $950m Florida "policyholder credit" accrued Sept 2025 under Florida's 3-year profit cap, payable to ~2.7m policyholders in early 2026 | CBS Miami, Florida governor's office release, Insurance Journal, Carrier Management (all corroborate $950m/~2.7m policyholders) | Pass |
| 4 | CRH | $8.5bn all-cash Arcosa acquisition, 11.5x 2026E EBITDA, $175m run-rate synergies by year 3, expected close Q1 2027 | CNBC, CRH press release, Businesswire (all confirm $8.5bn / $150-per-share / 11.5x / Q1 2027 close) | Pass |
| 5 | CMCSA | NBCUniversal/Sky spin-off announced 29-Jun-2026; ~12-month timeline; Comcast retains up to 19.9% of NBCUniversal for up to a year post-close | CNBC, NewscastStudio, Comcast IR release | Pass |
| 6 | EG | $1.2bn Adverse Development Cover with Longtail Re (Stone Ridge affiliate), effective 1-Oct-2025, two layers ($700m + $500m) above $5.4bn of NA liability reserves, ~$122m consideration for the second layer | Everest IR release, Businesswire, Artemis.bm, Reinsurance News | Pass |
| 7 | BR | CQG acquisition completed ~1-May-2026 | Broadridge press release / Morningstar / PRNewswire (completion dated 30-Apr-2026, announced 1-May-2026 — trivial one-day dating difference, not material) | Pass (minor date nuance, immaterial) |
| 8 | NOW | Moveworks $2.85bn acquisition under active DOJ "second request" antitrust review, not yet closed | TechCrunch, Bloomberg, Lexology, PYMNTS | Pass |
| 9 | AMP | Combined AUM+AUA reached a record $1.8 trillion in Q2 2026, +14% YoY | TradingView (Q2 2026 earnings recap: AUA/AUM/AUM record $1.812T), SEC 8-K | Pass |
| 10 | BX | Total AUM $1.35tn (+11% YoY), fee-earning AUM $961.6bn (+8% YoY) at Q2 2026 | Investing.com, Pulse2, SEC 10-Q (all confirm $1.35tn / $961.6bn) | Pass |

10 of 10 externally-checked facts passed. The one material failure found this loop (PGR's NTM P/E) is a report-generation/data-pipeline defect, not a dossier sourcing defect — the dossier itself correctly identified and disclaimed the bad number; the report simply didn't use the dossier's own correction.
