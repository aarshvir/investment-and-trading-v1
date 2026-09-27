# A2 — Investment-committee audit, Loop 10

**Total: 89/100.** One-line verdict: a real, sourced, 20-name full-conviction portfolio, with a clean fact-check of the two newest holdings (RSG, LH) and every Loop-9 must-fix genuinely closed at the root, but the completed-diligence-queue framing in §1 slightly overstates certainty and one dossier still carries an unverifiable supporting figure alongside its otherwise-correct conclusion.

Build audited: content cd5f38e02373, built 2026-09-27T04:19:57 (post v010; RSG and LH replaced EXC and CAH). `python code/lead_guard.py` confirms the build is fresh; `code/lead_verify_gate.py` reads OPEN only because C1 re-runs last, after this audit (per standing instructions, not scored as a defect).

## Loop-9 must-fixes — verified fixed
1. **WEC placeholder thesis** — FIXED. FINAL_REPORT §6 now carries a full one-line thesis for WEC ("a rare, real large-load (data-center) growth pipeline… the main watch-item is financing"). Grepped the current FINAL_REPORT.md for "pending" — no match; all 20 holdings have real one-liners.
2. **RMD near-miss undisclosed** — FIXED. §6 "Diligence errors that changed a verdict or a holding" now names RMD explicitly, describes the fabricated FY2027 guidance, the 9-month-as-full-year mislabelling, the omitted MatrixCare divestiture, and the INCLUDE→INCLUDE-SMALL reassessment.
3. **No cumulative DA tally** — FIXED. A.4 now has a "DA series total (DA4–DA19)" row: 388 facts, 344 pass / 18 minor / 18 fail (all corrected) / 8 unverifiable.
4. **Order-dependence risk-profile sentence** — FIXED (adequately). §6 now states "The risk barely moves: the 2007–09 replay ranges from −54% to −47%… The exact list is a judgement at the margin; the character of the portfolio is not." Independently re-derived from `lead_j_sensitivity.json`: GFC episode range across the 4 alternative orderings is −53.6% to −47.3%, matching.

## Scores

| # | Criterion | Score | Evidence | Gap |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 9 | DA19 (14 facts, RSG/LH) individually registered in A.4; cumulative DA4–DA19 tally now present (388 facts). | The tally's 8 "unverifiable" facts across the series are never itemised anywhere the owner would read (only inside individual DA*.md files) — a minor completeness gap, not a new one. |
| 2 | Backtest & validation rigour | 8 | Not primary focus this loop; unchanged since Loop 9. | — |
| 3 | Calibration & honesty | 8 | RMD disclosure (see above) and the LH/RSG corrections are dated, attributed to DA19, and leave the original text visible per the program's own correction convention. | RSG.md kill-criterion-1 sentence still carries the "+5.2%/+4.4% related-business growth" figures in the main body (struck through with a bracketed correction note, not removed), and the correction section explains the figures don't trace to the cited releases — handled correctly, but the same pattern (an unsourceable supporting number next to a correct conclusion) is now the second time in two loops (RMD, RSG) that a load-bearing-adjacent figure was fabricated-looking; worth a root-cause check on why analyst dossiers keep inventing precise-looking secondary figures. |
| 4 | Company-level diligence | 9 | RSG and LH dossiers independently fact-checked by DA19 (14 facts: 12 pass, 1 minor, 1 fail); the 1 fail (LH's mislabelled "2Q'25" row, actually Q3 2025 data) is corrected with a dated Correction section and an inline bracketed marker on the affected table row — both present, verified by reading LH.md directly. | The LH correction fixes the table row and footnote but the thesis-adjacent narrative elsewhere in §3/§4 that already used the correct Q2'25 comparators was, per DA19's own note, "inconsistently... correctly used" even before the fix — meaning the dossier's error was isolated to one table row, not systemic, but this should be double-checked mechanically (a pre-check rule) rather than relying on a human auditor catching it every time. |
| 5 | Valuation rigour | 9 | RSG (27.0x NTM P/E, oligopolistic waste-services thesis, price implies growth "modestly below" base case) and LH (15.9x NTM P/E, guidance raised twice) both use the reverse-DCF/implied-growth framework consistently with the other 18 holdings; no double counting found. GDDY's Loop-7/8 peer cross-check remains in place. | RSG's NTM P/E of 27.0x is the highest multiple in the portfolio by a wide margin (next is VEEV at 28.4x, but VEEV is SaaS while RSG is an industrial/waste name) — the dossier justifies this via pricing power and margin durability, and DA19 confirms the underlying facts, but §6's one-line table gives no reader-visible flag that RSG is priced richer than typical for its sector; a half-sentence on why an above-market multiple is still "priced for less growth than delivered" for a waste hauler would strengthen criterion 9 as well. |
| 6 | Portfolio construction & risk | 10 | Independently re-summed all 20 weights from `outputs/lead_portfolio_build.json`: 100.0% exactly (`checks` array confirms: max sector 25.0%=cap, max sub-industry 8.32%<12% cap). Recomputed sector weights directly from the table's `sector`/`w` fields: Financials 25.00%, Industrials 21.71%, Health Care 18.56%, Consumer Discretionary 10.24%, Materials 9.42%, Utilities 8.32%, Information Technology 6.75% — all ≤25% cap, matches report exactly. | — |
| 7 | Strategy coherence & mandate fit | 9 | Rule-(j) sensitivity re-verified directly from `lead_j_sensitivity.json`: `n_in_every_ordering`=6, names {ADP, CRH, GDDY, TJX, USB, VEEV} — exact match to §6's text. GFC-replay range across orderings independently recomputed as −53.6% to −47.3%, matching the stated −54% to −47%. | §1's "that completes the queue: every company that passed the quick pass now has full research" is true (336 researched, 0 queued per the build log) but the sentence sits right next to "New results after the next earnings season can still change the list" — the juxtaposition slightly undersells that a completed *initial* queue is not a completed *ongoing* process; a non-technical reader could read "completes the queue" as "done forever." One added clause ("as of today's filings") would remove the ambiguity. |
| 8 | Implementation & monitoring | 8 | Not primary focus this loop; unchanged since Loop 9. | — |
| 9 | Communication for the owner | 8 | §6's "what changed" section (LH, RSG in; EXC, CAH out) is a clean two-line diff; the RMD disclosure is written in plain English with the specific error named. | RSG's high relative multiple (see criterion 5) has no reader-visible caveat in the ranked table itself; this is the same class of issue as prior loops' "communication of a real number needs one more sentence," not a new defect. |
| 10 | Reproducibility & auditability | 9 | content_sha256 cd5f38e02373 traceable through build_history.jsonl; `lead_guard.py` confirms freshness; rule_commitments.jsonl shows the wave-7-labelling commit (second share classes) preceded this build with no selection-logic change, correctly disclosed. | Verification gate reads OPEN for the expected reason (C1 runs last) — not a defect, per standing instruction, but this is now the sixth consecutive loop where the gate is technically open at audit time; if this is permanent by design, STATE.md should say so explicitly rather than relying on the auditor notes to explain it away each loop. |

## Must-fix to reach ≥95 (ranked)

1. **RSG's unsourced "+5.2%/+4.4% related-business growth" figure was left in the dossier body (bracketed, not removed) rather than corrected in place** (criterion 3). This is the second unsourceable precise figure caught adjacent to a correct conclusion in as many loops (RMD, now RSG) — add a mechanical pre-check that any percentage figure in a kill-criterion or thesis sentence must appear verbatim in a cited source (the RMD-triggered pre-check already flags missing guidance quotes; extend it to all quoted percentages, not just guidance).
2. **RSG's above-portfolio-average 27.0x NTM P/E carries no reader-visible flag in §6's ranked table** that it is priced richer than the portfolio norm (criterion 5, 9) — add one clause to RSG's one-line thesis explaining why a premium multiple is still justified (pricing power, industry structure) so a non-technical reader isn't left to infer it.
3. **§1's "completes the queue" phrasing risks being read as "diligence is permanently finished"** rather than "as of today's filings, before the next earnings season" (criterion 7, minor) — add the qualifying clause directly in that sentence rather than only two sentences later.

## Numbers re-computed

| Number | In report | My value | Pass/fail |
|---|---|---|---|
| Sleeve weights sum | 100% | 100.0% (hand-summed all 20 from `outputs/lead_portfolio_build.json` table `w` field) | PASS |
| Financials sector weight | 25.0% cap | 25.00% (USB+MA+AXP+PGR+HBAN, independently grouped by `sector` field) | PASS |
| Max sub-industry weight | ≤12% cap | 8.32% (Electric Utilities = WEC only, since EXC exited this loop) | PASS |
| n_in_every_ordering (rule-j) | 6 | 6, names {ADP, CRH, GDDY, TJX, USB, VEEV} (`lead_j_sensitivity.json`) | PASS |
| GFC-replay range across orderings | −54% to −47% | −53.6% to −47.3% (recomputed from all 4 `episodes["Global financial crisis"]` values) | PASS |

## Facts checked in dossiers

| Ticker | Claim | Source checked | Pass/fail |
|---|---|---|---|
| RSG | Q2 2026 revenue $4,430m, net income $566m, GAAP diluted EPS $1.84 | Verified via DA19 (SEC XBRL companyfacts + 8-K Ex-99.1 accession 0001060391-26-000273) | PASS |
| RSG | FY2026 guidance raised at Q2'26 release (revenue $17.200–17.300B etc.) | Verified via DA19 against both Q4'25 and Q2'26 8-K Ex-99.1 releases, verbatim match | PASS |
| RSG | Net debt/EBITDA ≈2.5x at 2026-06-30 | Verified via DA19 XBRL cross-check; recomputed 13,962/5,537.5=2.52x independently | PASS |
| RSG | Kill criterion 1 related-business-growth figures ("+5.2%/+4.4%") | Verified via DA19: unsourceable against cited releases; correction section present and accurate | FAIL (correctly caught and corrected, original text retained per convention) |
| LH | Q2 2026 revenue $3,731.1m, diluted EPS $3.64, adjusted EPS $4.99 | Verified via DA19 (XBRL + 8-K Ex-99.1) | PASS |
| LH | "2Q'25" table row is mislabelled Q3 2025 data | Verified via DA19; correction section and inline marker both present in LH.md, verdict stated unchanged and correctly so (headline YoY narrative uses the correct Q2'25 figures elsewhere in the dossier) | FAIL (correctly caught and corrected) |
| WEC | §6 one-line thesis is complete, no longer a placeholder | Direct read of FINAL_REPORT.md §6 and grep for "pending" (no match) | PASS |
