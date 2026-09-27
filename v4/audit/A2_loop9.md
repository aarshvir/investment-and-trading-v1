# A2 — Investment-committee audit, Loop 9

**Total: 84/100.** One-line verdict: a real, sourced 20-name portfolio with tightened checks and a fixed valuation gap (GDDY), but this build ships a literal placeholder sentence in the client-facing holdings list (WEC) and omits a significant caught-and-reversed dossier error (RMD) from the report an IC member would actually read.

Build audited: content 7ac48e4d, 27 Sep 2026 03:15:09 (post v009; WEC, PTC, MCK, CAH held; RMD researched, reassessed INCLUDE→INCLUDE-SMALL and excluded before this build; SO, PPG, COR out vs v009).

## Scores

| # | Criterion | Score | Evidence | Gap |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 8 | DA18 (24 facts: 20 pass/1 minor/3 fail) individually registered in A.4 with source. | Still no single cumulative DA1–DA18 tally (facts checked / pass / minor / fail) anywhere in FINAL_REPORT or dashboard — carried unfixed 3 loops running (Loop 7, 8, 9). |
| 2 | Backtest & validation rigour | 8 | Not this auditor's primary focus this loop; unchanged since Loop 8. | — |
| 3 | Calibration & honesty | 7 | The TJX/latest-quarter sweep (DA15–17) is complete and disclosed; the WEC guidance-reaffirmation figures were independently re-verified against the 8-K (exact match) in DA18. | RMD was researched, found to cite FY2027 guidance that does not exist in the referenced 8-K, mislabelled 9-month buyback/dividend figures as full-year, and omitted a MatrixCare divestiture — a severe, load-bearing error caught by DA18 and reversed by re-assessment (verdict INCLUDE→INCLUDE-SMALL, excluded from this build). None of that episode appears in FINAL_REPORT (§6 "what changed", §3, or §11) — only in STATE.md's internal log and da18_factcheck.json. An investor reading only the deliverable would never learn this near-miss happened, which is exactly the kind of "prior error conceded" criterion 3 asks for. |
| 4 | Company-level diligence | 8 | WEC.md itself is thorough (§1 verdict, quantified guidance, financing watch-item) and independently fact-checked (DA18, all WEC facts PASS). | FINAL_REPORT §6's one-line thesis for WEC reads literally "**WEC** (INCLUDE): thesis line pending; see dossier" — traced to `code/lead_report_sections.py` line 204, `r.get('thesis')` returning empty for WEC specifically, falling back to its placeholder string, which then shipped verbatim into the published report and `outputs/lead_report_sections.md`. All 19 other holdings have a real one-liner; only WEC is broken. |
| 5 | Valuation rigour | 9 | The Loop-7/8 must-fix (GDDY single-leg valuation) is now fixed: GDDY.md has an added peer cross-check (WIX, VRSN, TCX, SHOP) at EV/EBITDA ~10.8x and EV/FCF ~8.8x, a discount to all four, corroborating the reverse-DCF. Re-derived the reverse-DCF arithmetic by hand (EV/base FCF/WACC 8.5%/g 3%) — consistent with prior loops. | Carried-forward item now closed; no new valuation gap found this loop. |
| 6 | Portfolio construction & risk | 9 | Independently re-summed all 20 weights = 100.0% PASS. Financials sector: USB 5.59+MA 5.64+AXP 4.58+PGR 4.63+HBAN 4.56 = 25.0%, exactly at cap, PASS. Sub-industry cap independently recomputed by grouping the build's own `sub` field: Electric Utilities = EXC 5.29 + WEC 6.71 = **12.00%**, exactly at the 12% cap and not exceeding it — PASS (this loop's designated check, previously flagged unverified in Loop 8). | — |
| 7 | Strategy coherence & mandate fit | 8 | Rule-(j) sensitivity is honestly disclosed: only 9 of 20 held under every alternative ordering (down from 14 in the prior build), and FINAL_REPORT states this plainly ("a judgement at the margin; the character of the portfolio is not") rather than hiding the increased fragility, as STATE.md flagged it should. Re-verified `n_in_every_ordering=9` and the 9 named tickers against `lead_j_sensitivity.json` — match. | The bench "next 20" table is well-populated, but the widening order-dependence (9/20 vs 14/20 last loop, as the eligible pool grows) deserves one added sentence quantifying how much the *risk profile* — not just the name list — would change under the alternative orderings shown (currently only a GFC range is given, −59% to −46%, no comment on sector-mix swings). |
| 8 | Implementation & monitoring | 8 | Not primary focus; unchanged since Loop 8. | — |
| 9 | Communication for the owner | 7 | "What changed" section is a clean two-line diff and the sector-limit binding explanation is precise and matches the checks file. | The WEC placeholder sentence (see criterion 4) is a direct, visible communication failure in the exact table a non-technical investor is told to read first (§6); this is worse than a missing footnote — it is broken prose that reads like an unfinished draft was shipped. |
| 10 | Reproducibility & auditability | 9 | Rule (m) (fact-check-before-release gate) is now written into the build script's rule block (commit 9c2125ac, per loop_fixes.json["8"]) alongside (a)-(l), closing the Loop-7/8 must-fix. content_sha256 (7ac48e4d) traceable through build_history.jsonl. | — |

## Must-fix to reach ≥95 (ranked)

1. **WEC's holding one-liner is a literal unfilled placeholder in the published report** (criteria 4, 9). Root cause identified: `code/lead_report_sections.py:204`, `r.get('thesis')` is empty for the WEC candidate record though `dossiers/WEC.md` §1 has a complete, quotable verdict sentence. Fix the data pipeline that populates the `thesis` field for WEC (likely a wave-6 ingestion gap specific to this name), rebuild, and grep the rebuilt FINAL_REPORT.md for "pending" to confirm no other name is affected before the next release.
2. **The RMD near-miss (fabricated guidance figures, mislabelled 9-month-as-full-year data, an omitted divestiture, caught by DA18 and reversed) is not disclosed anywhere in FINAL_REPORT**, only in STATE.md's internal log. Fix: add one sentence to §6 "what changed" or §11 naming RMD, the error class, and the reassessed verdict — the process worked, but only if the owner can see that it worked.
3. **No cumulative DA1–DA18 tally** (criterion 1, carried unfixed for the third loop running). One line or dashboard tile: total facts checked across the whole series, and pass/minor/fail counts.
4. **Rule-(j) order-dependence has widened (9/20 vs 14/20 last loop) but only the return range is quantified, not the sector-mix swing** under the alternative orderings (criterion 7, minor, new observation).

## Numbers re-computed

| Number | In report | My value | Pass/fail |
|---|---|---|---|
| Sleeve weights sum | 100% | 100.0% (hand-summed all 20 from `weights`) | PASS |
| Financials sector weight | 25.0% cap | 25.0% (USB+MA+AXP+PGR+HBAN, re-derived from `weights`) | PASS |
| Electric Utilities sub-industry weight | 12% cap (from `checks`) | 12.00% (EXC 5.29% + WEC 6.71%, independently grouped by `sub` field) | PASS |
| n_in_every_ordering (rule-j sensitivity) | 9 | 9 (`lead_j_sensitivity.json`, names match: ADP CAH CRH EXC GDDY LVS TJX USB VEEV) | PASS |
| GDDY peer cross-check multiples | EV/EBITDA ~10.8x, EV/FCF ~8.8x (discount to WIX/VRSN/TCX/SHOP) | Confirmed present in GDDY.md addendum, consistent with the reverse-DCF conclusion ("below base case") | PASS |

## Dossier facts checked

| Ticker | Claim | Source checked | Pass/fail |
|---|---|---|---|
| WEC | Q2 2026 operating revenues $2,062.1M (+2.6% YoY); GAAP diluted EPS $0.91 vs $0.76 prior year; FY2026 EPS guidance $5.51–$5.61 reaffirmed | DA18 fact record, cross-checked against WEC Q2 2026 8-K Ex-99.1, accession 0000783325-26-000080 | PASS |
| RMD | FY2027 guidance range and 9-month buyback/dividend figures | DA18 correction note: guidance range does not exist in the cited 8-K; 9-month figures were actually full-year; MatrixCare divestiture omitted | FAIL (correctly caught and reassessed; verdict INCLUDE→INCLUDE-SMALL, excluded from this build) |
| PTC | Fiscal-quarter table label (Sept year-end) | DA18 correction: one fiscal quarter mislabelled early — corrected in dossier | FAIL (corrected) |
| Portfolio (Electric Utilities sub-industry) | EXC + WEC sit exactly at the 12% sub-industry cap | Hand-recomputed from `outputs/lead_portfolio_build.json` `table`/`weights`/`sub` fields | PASS |
| GDDY | Reverse-DCF (EV $14.89bn / base FCF $1.8bn / WACC 8.5% / g 3%) corroborated by a second, peer-multiple valuation leg | GDDY.md §7 addendum, re-derived arithmetic, cross-checked against da17_factcheck.md sourced peer multiples | PASS |
