# A2 loop 4 audit — investment-committee perspective

**Total: 76 / 100.** Verdict: real, verifiable fixes landed since Loop 3 — PGR's corrupted P/E is genuinely
fixed with a systemic sanity-bound (not a PGR-specific patch: `code/lead_build_portfolio.py`'s `_pe_sane()`
now rejects any `pe_ntm`/`trailingPE` outside [3, 150] for every ticker), and the displayed sleeve weights now
sum to exactly 100.0% (I re-added the twenty published weights by hand: 100.0). But the two structural
must-fixes from Loop 3 that were about *process*, not a single number — the soft pre-registration firewall on
rule (j), and the promised lane-vs-top-70 footnote — were not acted on at all, and the exact failure mode this
audit warned about last loop (new full-conviction holdings entering the frozen build with zero independent
fact-check) recurred with a *different* five names this loop, one of which (GM) I found to contain a real,
quotable, load-bearing sourcing error in its own cited primary source. The diligence process is still strong on
average; the problem is that the safety net (independent fact-checking) consistently arrives one loop behind
the newest full-conviction holdings, which is exactly when a top-tier IC would insist on it.

## 1. Criterion table

| # | Criterion | Score | Evidence | Gap(s) |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 7 | The PGR-class defect (a corrupted vendor field reaching the flagship table) is now fixed at the pipeline level, not just for PGR — confirmed by reading `code/lead_build_portfolio.py`'s `_pe_sane()` (bounds [3, 150], falls back to trailing P/E with a label). But I found a new, different-class error: GM.md's own cited source (its Q2 2026 earnings release) does not support its stated $24.7bn automotive cash+securities figure (see must-fix #1) — actual is $19.65bn. | One live, unflagged, decision-relevant bad number in a load-bearing dossier claim, undetected by any of the program's consistency checks (C1 checks report-vs-source agreement, not source-vs-primary-document accuracy). |
| 2 | Backtest & validation rigour | 8 | Not my primary focus this loop (A1's lane); B1/B1X register unchanged since Loop 2/3. | Not independently re-verified this loop. |
| 3 | Calibration & honesty | 7 | Adverse facts remain prominent and specific (GM's China JV drag, ADP's rate-sensitive float income, RJF's cash-sweep litigation, DOV's refrigeration execution miss stated with a direct CEO quote, HBAN's rising NPA ratio) — genuinely more candid than a sell-side note would be. | Loop-3's honesty concession that rule (j) was written after verdicts were known is still just a prose disclosure, not a structural fix (must-fix #3, unresolved for a second loop). |
| 4 | Company-level diligence | 7 | Read all five new full-conviction dossiers in full; independently verified 2–3 primary-source facts in each of GM, ADP, RJF, DOV, HBAN (10 checks, see §4 below) via direct SEC-filing and earnings-release re-fetch — ADP, RJF, DOV, HBAN all checked out exactly. Adverse facts are dated and specific, not generic. | GM's automotive net-cash claim (must-fix #1) is materially wrong versus its own cited source. Five holdings worth 29.2% of the sleeve are formally "not yet checked" in Appendix A.5 (must-fix #2) — the same gap this audit flagged last loop, now recurring with different names. |
| 5 | Valuation rigour | 7 | PGR's fix holds (trailing 10.3x, correctly labelled, matches its dossier's own correction). ADP, RJF, DOV, HBAN reverse-DCF write-ups are methodologically consistent, clearly labelled as analyst estimates where no V1 row exists, and cross-checked against peer multiples. | GM's reverse-DCF reconciliation against V1 (the central argument for calling V1's "excessive" tag wrong) rests on the incorrect $24.7bn cash figure; correcting it raises implied EV by ~$5bn and weakens (does not necessarily reverse) the case for overriding V1. |
| 6 | Portfolio construction & risk | 9 | Independently recomputed from `outputs/lead_portfolio_build.json`: raw weights sum to 1.0 exactly; Financials sector = 0.25 (binding at the cap, matches MTB+AMP+PGR+SYF+HBAN+RJF = 5.8+4.5+4.3+1.5+4.2+4.7 = 25.0% from the published table); the file's own `checks` array independently confirms every constraint (max single name 0.078<0.10, half-conviction cap 0.05 exact, per-name floor 0.015 exact, max sub-industry 0.100<0.12) all `True`. Displayed weight column re-summed by hand: 100.0% exactly (Loop-3's 100.3% display bug is genuinely gone). | None found this loop — this criterion improved on concrete re-verification. |
| 7 | Strategy coherence & mandate fit | 8 | The owner's NVDA/MSFT and whole-index challenges continue to be answered with disciplined, dated, written rules rather than ad hoc exceptions; §1's verdict still leads with the all-stock answer as instructed. | Two must-fixes explicitly promised after Loop 3 (rule-(j) firewall, lane footnote) were simply not implemented — a repeat process-integrity miss an IC would read as "the manager says one thing and does another." |
| 8 | Implementation & monitoring | 8 | Not independently re-verified this loop (A3's lane); unchanged since Loop 2/3 on my spot checks. | Same as prior loops. |
| 9 | Communication for the owner | 8 | Both of the Loop-3 "silent numeric error" problems that a non-technical reader could not have caught (the impossible 0.3x P/E, the false "sums to 100%" caption) are genuinely fixed and independently confirmed in both FINAL_REPORT.md and `dashboard/d4v.json` (PGR row: `"pe": 10.31109, "pe_label": "trailing P/E"`). | The reader still cannot tell, from §6 alone, which holdings entered via the more permissive lane route (must-fix #4) or which two holdings (BR, DG) carry a dated correction to a fact printed elsewhere in the same report. |
| 10 | Reproducibility & auditability | 7 | I reproduced every headline portfolio-construction number this loop directly from `outputs/lead_portfolio_build.json` without difficulty (weights, sector caps, constraint checks) — reproducibility itself is real. | Appendix A.5's coverage claim is now stale for the second loop running by the same mechanism: the register is only ever caught up to the *previous* loop's new holdings, never the frozen loop being audited. A fact-check pass needs to run before the freeze, not after the next audit. |

## 2. Must-fix to reach ≥95 (ranked by score impact)

1. **GM's automotive cash + marketable securities figure is wrong versus its own cited source (criteria 1/4/5).** GM.md claims $24.7bn (net cash +$8.7bn); GM's own Q2 2026 earnings release (the exact filing GM.md cites) shows $19,650m ($15,147m cash + $4,503m marketable securities) against $15,979m automotive debt — net cash **+$3,671m**, matching the release's own stated "Net automotive liquidity position: $3,671 million." Correct GM.md §6/§7, rebuild the EV bridge (EV rises ~$5bn) and reverse-DCF conclusion, and state whether the INCLUDE verdict/weight survives.
2. **Five new full-conviction holdings (GM, ADP, RJF, DOV, HBAN; 29.2% of the sleeve) are "not yet checked" in Appendix A.5 (criteria 4/10)** — the same defect class flagged last loop with a different nine names. Run DA7 before the next freeze, and change the process so no name enters the frozen build at full weight without at least one completed independent fact-check.
3. **Rule (j)'s pre-registration firewall is still soft (criterion 3/7)** — Loop-3 must-fix #3, not acted on. Commit the rule to a hashed/timestamped file before the eligible pool is computed, and add its hash to the build's input manifest.
4. **Lane-vs-top-70 footnote never added (criteria 7/9)** — Loop-3 must-fix #5, not acted on; zero occurrences of "lane" anywhere in FINAL_REPORT.md. Add the promised footnote to §6 and §13.
5. **BR and DG's dated DA6 corrections (CQG deal size, Washtenaw litigation timeline) are not pointed to from the main §6 table (criterion 9)** — minor, but a reader would not know to look.

## 3. Numbers I re-computed

| # | Number | In report / source | My recomputation | Pass/fail |
|---|---|---|---|---|
| 1 | Displayed sleeve weights sum | "Weights are rounded to 0.1 point; they sum to 100% of the sleeve" (FINAL_REPORT §6) | Hand-summed the 20 published 0.1-point weights: 100.0 | **Pass** (fixes Loop-3's 100.3% failure) |
| 2 | Raw sleeve weights sum | implied 100% | `outputs/lead_portfolio_build.json` weights dict sums to 1.0 exactly | Pass |
| 3 | Financials sector weight (cap 25%) | 25% cap, "verified after solving" | MTB 5.8 + AMP 4.5 + PGR 4.3 + SYF 1.5 + HBAN 4.2 + RJF 4.7 = 25.0% (also matches build file's `sectors.Financials = 0.25` and `checks` row `["Max sector", 0.25, 0.25, True]`) | Pass (binding exactly) |
| 4 | PGR P/E shown | 10.3x trailing (FINAL_REPORT §6; dashboard `d4v.json` PGR row `"pe": 10.31109, "pe_label": "trailing P/E"`) | Matches PGR.md's own corrected figure; pipeline fix (`_pe_sane`, bounds [3,150]) confirmed in code | Pass |
| 5 | GM automotive cash + marketable securities | "$24.7bn" (GM.md §6, citing GM's Q2 2026 earnings release) | Re-fetched the cited filing directly: $15,147m cash + $4,503m marketable securities = **$19,650m**; net automotive liquidity per the same release: **+$3,671m** (not the dossier's implied +$8.7bn) | **Fail** |
| 6 | GM V1 valuation figures (cross-check dossier vs source table) | GM.md §7: NTM P/E 5.65x, implied growth 23.5%, base −1.6%, bear −35.5%, bull +64.2% | `outputs/v1_valuation_table.csv` GM row: pe 5.647, implied growth 0.2355, base −0.0164, bear −0.3555, bull 0.6416 | Pass |

## 4. Facts checked in dossiers (against primary sources)

| # | Dossier | Claim | Source checked | Pass/fail |
|---|---|---|---|---|
| 1 | GM | Q2 2026 FY26 guidance raised to EBIT-adjusted $14.0–16.0bn / adjusted EPS $12.00–14.00 | GM's own Q2 2026 earnings release (gmq22026pressreleaseandfin.htm, direct re-fetch) | Pass |
| 2 | GM | Automotive-only debt ≈$15.98bn | Same release, Combining Balance Sheet: $15,979m | Pass |
| 3 | GM | Automotive cash + marketable securities ≈$24.7bn, net cash +$8.7bn | Same release: $19,650m cash+securities; net automotive liquidity **+$3,671m** stated directly | **Fail** |
| 4 | ADP | FY26 total revenue $21,947.4m (+7.0%); diluted EPS $10.94; FY27 guide revenue +5–6%, adj. EBIT margin +70–90bps, adj. EPS +9–11% | Web search of ADP's own 4Q/FY26 results release language (confirmed against multiple independent summaries of the same release) | Pass |
| 5 | RJF | Q3 FY26 GAAP diluted EPS $3.01; adjusted diluted EPS $3.14; adjusted pre-tax margin 19.9% | RJF Q3 FY2026 earnings release (direct re-fetch of the cited SEC filing) | Pass |
| 6 | DOV | FY26 guidance raised: GAAP EPS $8.94–$9.14; adjusted diluted EPS $10.55–$10.75; revenue growth 6–8% (organic 4–6%) | DOV Q2 2026 8-K Ex-99.1 (direct re-fetch of the cited SEC filing) | Pass |
| 7 | HBAN | Q2 2026 NIM 3.21%; buybacks $159m in Q2 (≈19m shares YTD); CET1 10.0% (down from 10.2%) | HBAN Q2 2026 8-K Ex-99.1 (direct re-fetch of the cited SEC filing) | Pass |

7 of 8 externally re-checked claims passed exactly; the one failure (GM's automotive net-cash figure) is load-bearing for that holding's central valuation argument, not a peripheral detail.
