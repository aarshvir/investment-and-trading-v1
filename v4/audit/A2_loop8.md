# A2 — Investment-committee audit, Loop 8

**Total: 85/100.** One-line verdict: a real, sourced, mostly self-consistent 20-name portfolio that a fundamental IC could review productively; still held back by one uncorrected valuation gap (GDDY), one process rule not actually written where the other rules live, and a newly-demonstrated class of dossier error (prior-year-column mix-ups) that has only been checked for the two names it was caught on.

Build audited: content 174b254450b3, 27 Sep 2026 02:10:44 (post v008; TJX and SO added, GM and DRI removed).

## Scores

| # | Criterion | Score | Evidence | Gap |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 8 | Every DA1–DA14 pass/fail rate is individually listed in A.4; TJX/SO XBRL cross-tie run before release. | No single cumulative DA1–DA14 tally (facts checked / pass / minor / fail) anywhere in FINAL_REPORT or dashboard — carried unfixed from Loop 7 must-fix #5. |
| 2 | Backtest & validation rigour | 8 | Not this auditor's focus; B1X/daily-DD checks unchanged since Loop 7, still hold. | — |
| 3 | Calibration & honesty | 8 | TJX net-income error (18% understatement) disclosed with a dated, inline "[Corrected …]" marker; verdict re-affirmed unchanged rather than silently kept. | STATE.md admits the new numeric cross-tie tool did **not** catch the TJX error ("table cells carry no '$' and no adjacent label") — a real, named blind spot, but the 18 other dossiers have not been re-swept for the same prior-year-column pattern. |
| 4 | Company-level diligence | 9 | TJX.md §5 flags its own gap ("not independently re-pulled from Q1 FY2027 release... gap, time-boxed") — good self-disclosure discipline; DA14 checked 7 facts per new name against primary 8-K/10-Q sources. | See above: the newly-discovered defect class is checked in only 2 of 20 dossiers. |
| 5 | Valuation rigour | 8 | GDDY's reverse-DCF math re-derives cleanly by hand (EV $14.89bn / base FCF $1.8bn / WACC 8.5% / g 3% ⇒ ≈ −7.7%/yr priced in, matches dossier). | GDDY (3.1% weight, sole IT holding) still rests on **one** valuation leg with no peer EV/FCF or EV/sales cross-check, despite being an explicit Loop-7 must-fix ("add a second corroborating valuation approach... to GDDY.md section 7") — not done in this build; loop_fixes.json["7"] does not list it either. Carried unfixed 2 loops running. |
| 6 | Portfolio construction & risk | 9 | Re-summed the §6 weight table by hand: 5.6+5.6+5.0+3.1+3.5+5.2+5.6+6.7+4.5+4.8+4.1+5.0+5.6+4.6+4.6+5.5+5.5+4.5+6.4+4.6 = **100.0%**, PASS. Financials sector re-summed: USB 5.6 + MA 5.6 + AXP 4.6 + PGR 4.6 + HBAN 4.6 = **25.0%**, exactly at the disclosed cap, PASS. GM/DRI removal is honestly framed ("still passes every test; displaced") not silently dropped. | Sub-industry cap (12%) not independently re-verified by me this loop for the new TJX/SO pair — low risk (different sub-industries) but unchecked. |
| 7 | Strategy coherence & mandate fit | 9 | §6 explains selection mechanics, rule-(j) sensitivity (14/20 held under every ordering re-verified against lead_j_sensitivity.json — `n_in_every_ordering` matches the 14 names quoted), and gives the bench with a `base_return_gap_to_20th` field (the Loop-6/7 must-fix) now present for all 152 names. | — |
| 8 | Implementation & monitoring | 8 | Not primary focus; unchanged since Loop 7. | — |
| 9 | Communication for the owner | 9 | §6 "what changed" is a plain two-line diff (TJX/SO in, GM/DRI out, why); exit triggers are the full sentence, not truncated. | — |
| 10 | Reproducibility & auditability | 9 | build_history.jsonl / rule_commitments.jsonl / lead_verify_gate.py chain intact; content hash traceable end to end. | Rule (m) (fact-check-before-release gate) is described only in STATE.md's narrative log, not written into `code/lead_build_portfolio.py`'s docstring alongside rules (a)–(l) as the Loop-7 must-fix explicitly asked ("add rule (m) to STATE.md documenting this explicitly... alongside (a)-(l)"). Checked the file header directly (lines 1–17): amendments listed stop at (f); rules 2–4 don't mention (m) either. Carried unfixed. |

## Must-fix to reach ≥95 (ranked)

1. **GDDY valuation is still single-leg** (criterion 5, carried from Loop 7 unfixed). Add a peer EV/FCF or EV/sales cross-check to GDDY.md §7 before the next release; it is the sole IT-sector, non-V1-covered holding at 3.1% weight.
2. **Rule (m) still not written as a lettered rule where (a)–(l) actually live** (criterion 10, carried from Loop 7 unfixed). Add it verbatim to the `code/lead_build_portfolio.py` docstring (or STATE.md's rules list), not only the dated log entry.
3. **The prior-year-column defect class found in TJX (DA14) has not been swept across the other 19 holdings** (criterion 3/4, new this loop). The dossier_precheck/xbrl_crosstie tools are confirmed *not* to catch it; run a targeted manual re-check of the "latest quarter" row in all 20 dossiers' results tables against the filed period caption.
4. **No cumulative DA1–DA14 tally** (criterion 1, carried from Loop 7, minor). One line/tile: total facts checked, pass/minor/fail counts across the whole series.

## Numbers re-computed

| Number | In report | My value | Pass/fail |
|---|---|---|---|
| Sleeve weights sum | 100% | 100.0% (hand-summed all 20) | PASS |
| Financials sector weight | 25.0% cap | 25.0% (USB+MA+AXP+PGR+HBAN) | PASS |
| GDDY reverse-DCF implied FCF decline | −7.7%/yr | ≈ −7.6% to −7.8% (re-solved 2-stage FCFF at stated WACC/g/EV/FCF) | PASS |
| n_in_every_ordering (rule-j sensitivity) | 14 | 14 (lead_j_sensitivity.json) | PASS |
| DA14 fact count/result | 14 facts, 1 fail | 14 facts, 1 fail confirmed in da14_factcheck.json | PASS |

## Dossier facts checked

| Ticker | Claim | Source checked | Pass/fail |
|---|---|---|---|
| TJX | Q2 FY2027 net income corrected to $1,520m (was $1,243m, a prior-year-column error) | DA14 correction cross-referenced against TJX 8-K Ex-99.1 accession 0000109198-26-000045 | PASS (error correctly found and fixed) |
| GDDY | Net debt/EBITDA ≈1.90x on carrying value (not 1.93x on gross principal) | DA13 correction, GDDY Q2-26 10-Q debt note, accession 0001609711-26-000088 | PASS |
| SO | Multi-registrant filing correctly scoped to consolidated "Southern" parent, not a subsidiary | DA14 methodology note, cross-checked against combined 10-Q structure | PASS |
| Portfolio (all holdings) | Every held name is INCLUDE (full conviction); table marks all 20 with "§" (analyst route) | FINAL_REPORT §6 table, cross-checked against outputs/lead_portfolio_build.json candidate records | PASS |
| GM / DRI removal | Both "still eligible... displaced," not silently dropped | lead_j_sensitivity.json bench_near_misses positions 5 (GM) and 7 (DRI) | PASS |
