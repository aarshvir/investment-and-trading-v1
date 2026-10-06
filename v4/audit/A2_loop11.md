# A2 - Investment-committee audit, Loop 11

**Total: 79/100.** Verdict: mechanically sound (weights, caps, risk figures and every sampled company fact reproduce) and the whole-index research plus re-assessments are real progress. However, the final selection ranks seven top-70 names on valuation scenarios that the program's own re-assessments call wrong, so three holdings (12.6% of weight) are in the portfolio on an artefact. Owner-set rule (o) is not stated in the report, and the verification record is overstated by omission.

Build audited: content_sha256 45758e60..., built 2026-10-06T21:54:39 (`lead_guard.py`: fresh). The gate reads OPEN only because C1 runs last (not scored).

## Loop-10 must-fix status
1. RSG kill-criterion figure: moot, RSG is no longer held.
2. RSG 27x flag: moot; V at 24.5x is now the highest multiple held and has no flag in the table. Minor.
3. "Completes the queue" wording: FIXED (section 1 now says research is not finished for good).

## Scores
| # | Criterion | Score | Evidence | Gap |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 8 | Build, risk file and C1 fingerprint consistent. | One stock carries two different valuations in the same deliverable: UDR is "+22% base, implied below" in the section 6 table and build, but "+8%, in line" in the All-500 register and in F14_summary/RA14 (V1 base called an artefact of a 24x exit multiple). A.5 prints "not yet checked" for 10 holdings that DV02/DVH1/DVH2/DVH4 did check. |
| 2 | Backtest & validation | 8 | Unchanged since loop 10; not the focus. | - |
| 3 | Calibration & honesty | 8 | Corrections list is long, dated and candid; section 1 odds are conditional; Codex v005 handled fairly. | The DV verification series (6 files, 43 names, 408 facts: 229 pass, 99 FAIL, 58 minor, 22 unverifiable; 9 verdict changes) is absent from A.4's "DA series total" (397 facts, 20 fail) and nowhere says only about 97 of 500 dossiers are independently checked. A "researched in full" reader is not told the failure rate of unchecked dossiers is about 24% of facts. |
| 4 | Company diligence | 8 | 5 holdings sampled (ACN, UDR, DG, CVS, WFC): all facts match filings. All 20 holdings have an independent check. | DV found 4 FAIL of 8 on INTU, 4 of 9 on WTW, 4 of 12 on FSLR, 3 of 10 on ADSK: corrected, but the 224-name bench that the 20 were chosen from is largely unchecked. ACN's section 6 line "new bookings just turned negative" is stale: Q4 FY26 (1 Oct) bookings were +4% USD, +5% LC; the dossier's own recency note says so. |
| 5 | Valuation rigour | 7 | RA series fixed real method errors (SBC, interest double count, 5.17% rate). | Selection tie-break "base-case 3-yr return" mixes V1 scripted scenarios (top-70 names: BKNG +39%, CVS +36%, DG +35%, SYF +31%, ACN +30%, UDR +22%, DVA +20%) with analyst scenarios (+8% to +20%) for the rest. Analyst figures for the same names are DG +9.7%, CVS +11.4%, BKNG +13.4%, SYF +16.9%, ACN +12.0%, DVA +10.0%, UDR +8.3%. DG's own dossier says V1's 35% is wrong (margin of safety "2-5 points"). |
| 6 | Portfolio construction & risk | 9 | Weights sum 100.00%; Financials exactly 25.00%; Health Care Distributors (CAH+COR) exactly 12.00% = cap; SNA 10.00% = cap; half-conviction max 5.00%; floor 1.5%. Risk file matches report (GFC -37.4%, worst fall -42.7%, vol 13.8%, TE 12.8%, ENB 17). | Caps hold, but what gets capped is chosen by the flawed ranking above. |
| 7 | Strategy coherence & mandate fit | 7 | Answers the all-stock request directly; honest on beating the index. | Rule (o) (owner-set technology 20-30%) appears nowhere in FINAL_REPORT (grep: no match). Tech is 26.2% only if Visa is counted; IT-only is 19.3%, below the band. The report was required to state both. Section 6 "How these 20 were chosen" still describes a 455-name triage and "40 earlier dossiers", contradicting section 1 (all 500 researched). Rule-(j) sensitivity (12 in every ordering; GFC replay -45% to -37%, re-verified) does not test the ordering that matters: analyst-consistent bases. |
| 8 | Implementation & monitoring | 8 | Unchanged; exit triggers present for all 20 with current values. | ACN next-earnings date in the build (2026-10-01) is already past. |
| 9 | Communication | 7 | Answer-first section 1; per-holding one-liners. | Section 6 table is titled "ranked" but is ordered top-70 names first, then the rest, not by rank or weight; section 6 carries about 55 near-identical correction bullets; A.5 stale; SYF and ALL have blank thesis/exit cells in the All-500 register. |
| 10 | Reproducibility | 8 | Fingerprint, build history, rule commitments (rule (o) committed cdef8c5f before the build). | Gate OPEN again at audit time; A.5 not driven by DV results. |

## Rule amendments
Rule (o): justified as an owner instruction, committed before the build; it did not bind (swaps = []), so it is not result-chasing. The failure is disclosure, not design. The Visa/payments/interactive-media definition of technology is non-GICS and must be said.

## Must-fix to reach >=95 (ranked by impact)
1. Make the ranking input consistent. In `lead_build_portfolio.py`, for names on the V1 path use the analyst's re-assessed `scenario_returns_3y` and `implied_vs_base` from the latest F-summary (UDR must be in_line). Re-run; on analyst bases DVA, DG and UDR rank 58, 73 and 212 of 244 (my recomputation from `lead_portfolio_build.json` candidates) and drop out of the 20, replaced by bench names. Show analyst scenarios in the section 6 table and add this ordering to `lead_j_sensitivity.json`. Verify: no holding's displayed base differs from the All-500 register.
2. State rule (o) in sections 1 and 6 and the dashboard: owner-set 20-30% technology, 26.2% with Visa and payments, IT-only 19.3%, and that it did not force any swap. Rewrite the stale "How these 20 were chosen" paragraph to the 500-name process.
3. Add DV02/DV09/DVH1-DVH4 to A.4 and the cumulative tally (408 facts, 99 fail), state "about 97 of 500 independently checked, 403 not", and make A.5 read DV results (10 holdings wrongly say "not yet checked").
4. Refresh post-cutoff one-liners and exit triggers (ACN bookings line; ACN earnings date), fill SYF/ALL thesis cells, and order the section 6 table by rank.

## Numbers re-computed
| Number | Report | Mine | Result |
|---|---|---|---|
| Weights sum (20 names) | 100% | 1.000000 | PASS |
| Financials weight | 25.0% | 25.00% | PASS |
| Largest sub-industry | <=12% | 12.00% (CAH 6.35 + COR 5.65) | PASS (at cap) |
| Full-conviction weight | 59% (9 names) | 59.27% | PASS |
| GFC replay / worst fall | -37.4% / -42.7% | -37.42% / -42.66% (lead_risk_results.json) | PASS |
| Order-dependence | 12 in every ordering; -45% to -37% | 12; -45.1% to -36.96% | PASS |
| Sleeve vol / TE / effective bets | 13.8% / 12.8% / 17 | 13.79% / 12.75% / 17.4 | PASS |
| Technology share | not stated | 26.19% incl. Visa; IT-only 19.34% | FAIL (omitted) |
| UDR base case | +22% (table) vs +8% (register) | F14_summary +8.3%, RA14 +8.3% | FAIL (inconsistent) |

## Facts checked (primary sources)
See the JSON `fact_checks`: ACN (3), UDR (3), DG (3), CVS (3), WFC (1) against SEC 8-K releases; all numeric facts pass. The stale ACN thesis line and the V1 base cases for UDR, DG and CVS fail.
