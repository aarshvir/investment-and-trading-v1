# A2 - Investment-committee audit, Loop 12

**Total: 76/100.** Verdict: the mechanics hold (weights, caps, risk figures and every sampled company number reproduce), three of the four Loop-11 must-fixes are done, and "500 of 500 checked" is real. But the largest position (GD, 10%) was created in the last verification pass by a discount-rate choice the report itself says not to trust, the operating rules (sections 7 and 9) still contradict the 40% mandate and the model-rank sell rule, and several Loop-11 stale items are still in the deliverable.

Build audited: content_sha256 98c5d007..., built 2026-10-10T11:06:44 (`lead_guard.py`: fresh). The gate reads OPEN only because C1 runs last (not scored).

## Loop-11 must-fix status
1. Ranking inputs (rule p): MOSTLY FIXED. Analyst scenarios now feed 472 of 473 names; ACN/SYF/BKNG show analyst bases (+12/+17/+13%). One miss: UDR still carries V1's +21.9% base in the build and All-500 register (F14_summary and RA14 say +8.3%). It is on the bench, so no holding changes, but the named defect is not closed. Bear/bull for ACN, SYF, BKNG are still V1's, so ACN reads "+12% / +12% / +50%" (bear equals base).
2. Rule (o) disclosure: FIXED (section 1 gives 21.9% incl. payments/FIS and 20.2% IT-only; I recomputed 21.87% and 20.17%; swaps = []). Section 6 "How these 20 were chosen" is only half-rewritten: it still says "triage of the 455 names ... alongside the 40 earlier dossiers".
3. DV series in A.4/A.5 and coverage statement: FIXED. All 500 tickers have 3-38 checked facts (median about 8); 929 fails of 4,583 facts.
4. Stale content: NOT FIXED. ACN section 6 line "new bookings just turned negative" is unchanged (Q4 FY26 on 1 Oct was +4%/+5%); ACN next-earnings in the build is still 2026-10-01; SYF and ALL (and now GD) have blank thesis cells in all500_register.

## Scores
| # | Criterion | Score | Evidence | Gap |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 8 | Build, risk file, fingerprint consistent; sampled filings match. | "NTM P/E" column mixes bases: ADBE 8.7x is on non-GAAP EPS (price 235.47 / about $27), GAAP is about 12x; basis not declared. ADBE correction DV01 is itself wrong (see facts). Data is 25 Sep, 15 days old at build; ACN reported 1 Oct, GD named a CEO 8 Oct. |
| 2 | Backtest & validation | 8 | Unchanged; not the focus. | - |
| 3 | Calibration & honesty | 8 | 22% fact-failure rate disclosed; 500/500 stated; 40% tolerance adopted with a beta caveat; Codex v012-v016 reconciled. | Section 1 says "only 500 of them" and "the other 0 dossiers" (template text), and still says "treat any unchecked name's numbers as unverified" though none are unchecked; "checked" means about 8 load-bearing facts per name at a 22% failure rate, which the report does not say. Bottom-up "+12%" silently drops GD (10% of weight, no scenario) and renormalises; the sensitivity file shows 10.7% for the same portfolio. Section 1 says beta about 0.56; section 7 and my recomputation say 0.61. |
| 4 | Company diligence | 8 | Sampled GD, ADBE, UBER, SYF, FIS: every headline number matches filings. All 20 holdings have an independent check. | GD (10%) dossier says litigation, auditor, insider and EAC-history checks "should be re-verified before this dossier is relied on for sizing"; they were not. Its three EPS guidance raises are not in the cited release (DV18, confirmed by me). ADBE net-cash correction and "$650M AI-first ARR" fail (below). ACN stale. |
| 5 | Valuation rigour | 7 | RA/DV series fixed real method errors; reverse DCF on FCF after SBC at programme Ke. | GD's "price implies growth below base" depends on Ke 7.43% (Blume beta 0.545, raw 0.321). My reproduction: implied growth 1.6% / 3.5% at 7.43%, but 5.7% / 7.7% at beta 0.95 (Ke 9.1%), against a base of about 6% (guide) or 4.8% (consensus): the label flips to in-line or above. V1 calls GD "demanding" (implied 5.4%); dossier fair value is -3.8%; no 3-year scenario exists. Names ranked 71+ skip the V1 gates (a)-(c) that would have excluded GD (no base case, V1 demanding); 17 of 20 holdings take that route. No Ke table for the 20. |
| 6 | Portfolio construction & risk | 8 | Weights 100.00%; Financials and Industrials exactly 25.00%; CAH+COR 12.00%; GD 10.00%; half-conviction max 4.84%; floor 1.70%. Vol, TE, beta, drawdown reproduce. | Weight follows the conviction label, not return: full-conviction names (ex-GD) average +9.5% base on 47% of weight, half-conviction +14.6% on 43%; WFC is a 6.7% position with a +5.0% base, below the 5.17% Treasury and the report's own 6% no-edge market. The owner asked to beat the index. Two sectors are 50% of the book. |
| 7 | Strategy coherence & mandate fit | 7 | Answers the all-stock request directly; honest on odds and crashes. | Section 7 ("set those against your 15-20% tolerance") and section 9 ("at -20%, the stated tolerance is reached") contradict section 1's adopted 40%; worst fall is -43%. Section 1 still spends 18 lines on the index/T-bill allocation the owner declined. "Margin of safety" tier is binary and almost all names are "below", so the order is effectively conviction then base return from mixed sources. |
| 8 | Implementation & monitoring | 7 | Kill criteria for all 20 with current values; per-$10,000 table; estate-tax maths. | Sell rule "falls out of the top quarter of the ranking" is undefined; if read as model rank, 10 holdings (46.6% of weight: WFC, AMCR, FSLR, BR, INTU, UBER, OMC, COR, WTW, FIS, ranks 155-422) fail it on day one, and section 5 says the rank has no predictive value. Drawdown rule "review the equity/reserve mix" has no reserve in an all-stock book. WFC reports 13 Oct, three days after the build; ACN date stale. |
| 9 | Communication | 7 | Answer-first; per-holding one-liners; dollar scenarios added. | GD one-liner is "Thesis horizon: 12-36 months." (SYF's is a 60-word verdict paragraph); "each adds 1.4-1.4 times"; "17 independent positions (17 if only the weights are counted)"; "Loop-11 auditors" and "§3/§4" references in client text (risk is §7); table "#" is the model rank, which the report says did not predict returns; section 6 carries about 60 correction bullets. |
| 10 | Reproducibility | 8 | Guard fresh; rule commitments; build history; sensitivity file regenerates. | Gate OPEN at audit time; no WACC/Ke table; UDR mismatch shows the "build equals register" claim was not machine-checked for base values. |

## Rule amendments
Rule (p) is justified by internal consistency (it answers Loop-11 must-fix 1, committed before the build) and is not result-chasing. Rule (o) did not bind. No new rule this build. The concern is not a rule but the unequal gates: top-70 names face V1 valuation gates and analyst-route names do not, and the final 10% position sits on the weaker route. Turnover is also high: 4 of 20 names changed in four days after a verification pass (GD, ADBE, UBER, SYF in; V, CVS, VZ, ADSK out), 18 of 20 versus v011.

## Must-fix to reach >=95 (ranked by impact)
1. Re-underwrite GD before it carries 10%. In dossiers/GD.md and F-summary add a Ke table (raw beta 0.32, Blume 0.545, market-like 0.95) with implied growth at each, 3-year bear/base/bull returns, and complete the litigation, auditor, EAC-history and unbilled-revenue checks the dossier lists as needed "before sizing". If implied_vs_base is not "below" at beta 0.95, cut GD to half conviction (5% cap) and re-run. Verify: GD row in section 6 shows scenarios; build weights change accordingly.
2. Publish a Ke/WACC table for all 20 holdings (raw beta, Blume beta, Ke at programme and at beta 0.95, implied growth, label at each) and state which labels flip. Section 1 itself says three-year betas understate market sensitivity; the valuation must not rely on them. Verify: table in Appendix A; any holding that flips is re-ranked.
3. Make sections 7 and 9 and the dashboard consistent with the 40% mandate and the all-stock book: replace "15-20% tolerance" and "-20% tolerance reached" with 40%-based review levels (for example -20%, -30%, -40%); delete the equity/reserve instruction for the all-stock case; replace "top quarter of the ranking" with an explicit rule (kill criterion, or implied_vs_base turning "above", or conviction downgrade) and show it does not sell 47% of the book on day one. Fix lead_assemble.py line 163 and lead_report_sections.py line 351.
4. Close the carried-over stale items: ACN line (bookings +4% USD, +5% LC) and ACN earnings date; thesis cells for SYF, ALL, GD in the register; UDR base 8.3% in the build (find why the F14 scenario is not read); finish the section 6 selection paragraph (no "455 names", "40 earlier dossiers").
5. Fix the template and basis defects: "only 500 of them" and "the other 0"; state that checks cover about 8 load-bearing facts per name with a 22% failure rate; label the P/E basis (GAAP vs non-GAAP) and show ADBE/INTU on GAAP or SBC-adjusted EPS; say GD is excluded from the bottom-up figure (or give it a scenario) and show bear/base/bull from one source; reconcile 0.56 vs 0.61; correct ADBE net debt (see below).

## Numbers re-computed
| Number | Report | Mine | Result |
|---|---|---|---|
| Weights sum (20 names) | 100% (0.1-point table sums to 100.0) | 1.000000 | PASS |
| Financials / Industrials | 25.0% / 25.0% | 25.00% / 25.00% | PASS (at cap) |
| Largest sub-industry | 12% | CAH 6.38 + COR 5.62 = 12.00% | PASS |
| Full-conviction weight | 57% (8 names) | 57.06% | PASS |
| Technology share | 21.9% incl. payments; 20.2% IT | 21.87%; 20.17% | PASS |
| 3-year vol / tracking error / beta | 14.4% / 12.5% / 0.61 (section 1: 0.56) | 14.39% / 12.55% / 0.606 | PASS (section 1 beta FAIL) |
| Worst daily fall since 2005 | -43.2% | -42.8% (day-renormalised weights, trough 9 Mar 2009) | PASS (within 0.4 pt) |
| Beta to SPY 2012-2023 / 2018-2023 | not stated | 0.98 / 0.99 | confirms the report's caveat |
| 16% weight with no 2007-09 price | SYF, GDDY, AMCR, UBER | 1.81+5.78+4.84+3.26 = 15.69% | PASS |
| Single-year +10 pts / 5-year average +10 pts | 21% / 4% | 21.3% / 3.7% (TE 12.5%) | PASS |
| Bottom-up bear/base/bull | -4% / +12% / +29% | -4.3% / +11.9% / +29.4% over the 90% with a scenario; 10.7% base with GD at zero | PASS but GD omission undisclosed |
| $50,000 in 3 years (base) | $70,036 | $70,040 | PASS |
| Eligible, not held | 187 | 207 eligible - 20 = 187 | PASS |
| Verification tally | 4,583 facts, 929 fail; DV 909 of 4,186 | 4,583; 929; DV 909/4,186 (21.7%) | PASS |
| Dossiers with an independent check | 500 of 500 | 500 tickers with at least 3 checked facts | PASS |
| GD reverse DCF | +1.6% / +3.5% implied at Ke 7.43% | 1.57% / 3.51% (terminal 3%, 10 years) | PASS; at beta 0.95: 5.7% / 7.7% |
| UDR base case | +8.3% (RA14) | build and register still +21.9% | FAIL |

## Facts checked (primary sources)
See JSON `fact_checks`. GD Q2 FY26 revenue $14.1bn +8.1%, EPS $4.24, backlog $136.5bn, debt $7,516M and cash $4,333M, all PASS (8-K Ex-99.1, which has no outlook section, so the three EPS guidance steps remain UNVERIFIABLE in the cited filing). ADBE Q3 FY26 revenue $6.76bn, EPS $4.62/$6.13, FY guide, Q4 guide: PASS. ADBE net cash about $0.9bn: FAIL (total debt is $6,363M including $1,597M current, so net debt is about $0.7bn). ADBE "AI-first ARR above $650M": UNVERIFIABLE (release gives only "more than 150%"). UBER Q2 gross bookings $58.0bn, adjusted EBITDA $2.8bn, net income $2.4bn incl. $1.6bn revaluation gain, Q3 guide: PASS. SYF Q2 net earnings $885M, EPS $2.59, NCO 5.43%, NIM 15.08%, FY EPS guide $9.25-9.50: PASS. FIS Q2 adjusted EPS $1.48 (+8.8%), GAAP $0.45, revenue about $3.38bn, guidance cut, FCF $2.15-2.25bn: PASS.
