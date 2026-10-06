# A1 (quant and data) - Loop 11 audit

**Auditor:** A1, former head of quantitative research. **Build audited:** `outputs/lead_portfolio_build.json`, built 2026-10-06T21:54:39, content_sha256 45758e6055db... (`lead_guard.py`: "build fresh"). 20 holdings: DVA DG CVS ACN UDR SYF BKNG SNA CAH BIIB GDDY ACGL ADSK WFC FSLR BR INTU COR WTW V (9 full conviction = 59.3% of weight, 11 half conviction).

## 1. Total score and verdict

**76 / 100.** The arithmetic and risk engine are sound (every constraint and risk figure I recomputed ties out). What fell is the integrity of the new valuation layer. The re-assessments found systematic errors in the valuation method (SBC added back, EPS treated as cash, stale 4.2% risk-free rate). That is disclosed and being repaired, but the repair is incomplete. The largest holding still has an un-repaired discount rate, one holding's re-assessment never reached the build, and the report omits the tech-share and verification-coverage statements that Loop 11 requires. The C1 gate is open for the ninth consecutive loop.

## 2. Criterion table

| # | Criterion | Score | Evidence | Gap(s) |
|---|---|---|---|---|
| 1 | Data integrity and lineage | 8 | Backtest, weights, dividend yield (1.476%), 3-year risk figures and full-history drawdown all re-derive from the data files. Prices and as-of dates are labelled. | UDR "implied vs base" is below in the build but in_line in the register and the verdict log (4 build-vs-register mismatches: UDR, DLTR, DRI, EOG). The GFC note says DG/SYF/GDDY/V had no price and are "13% of the weight"; their weights sum to 17.8% (13% is a time-average; V enters in March 2008). |
| 2 | Backtest and validation rigour | 8 | Top-30 CAGR 12.52% vs SPY 15.10% reproduced. B1 tests 16/16 pass, B1X replication, newey-west stats. | The backtested model now selects only 7 of 20 holdings (top-70 names); 13 come through the analyst route, which has no backtest. The 20 are drawn from 244 eligible names by verdict, margin (a 2-state flag) and a scenario-return tie-breaker; the 11 half-conviction slots come from 140 tied names. Disclosed as "unproven", but the evidence base for the live process is thin. |
| 3 | Calibration and honesty | 8 | Honest odds (78% gain, 50% beat, 86% fall >20%), "cannot be promised" framing, 10-point-edge sizing (22% / 4% reproduced). | Beta 0.56 and TE 12.8% come from one three-year window (full-history beta 0.93, TE 8.4%). "12 names in every ordering" is mostly the 9 INCLUDE names, so the reassurance is overstated. No statement of how few dossiers are independently verified. |
| 4 | Company-level diligence | 7 | Five dossiers sampled (SNA, ACGL, UDR, CVS, DVA) tie to the Q2 2026 releases. All 20 holdings now have an independent check (DV02/DVH1/2/4, DA series). | Independent checks themselves find many failures: INTU 4/8, WTW 4/9, FSLR 4/13 (incl. a one-off tariff refund inflating margin), ADSK 3/10; in the DV02/DV09 samples 11 of 20 names had at least one FAIL and 3 verdicts changed. About 430 dossiers remain unchecked and the bench and exclusions rest on them. DVH1 mis-assessed SNA's WACC as MINOR. |
| 5 | Valuation rigour | 7 | Re-assessment on the 25 Sep rates with FCF, SBC as a cost and sector methods was a real improvement; about 45 verdicts moved. | SNA (10%) still uses WACC 8.0% against a programme basis of about 9.2%: implied growth is about 5.6%, not 2.9%, so "below" probably becomes "in_line". UDR not propagated. Margin of safety is a two-state flag, so "wide margin" is not measured. |
| 6 | Portfolio construction and risk | 8 | All constraints hold exactly after rounding: weights sum 1.0, max name 10.0%, max half-conviction 5.0%, floor 1.5%, Financials 25.00%, Health Care Distributors (CAH+COR) 12.00% = the sub-industry cap. Worst fall -42.66% reproduced exactly; risk shares verified to 4e-7. | Beta/TE from the calm window (see criterion 3); in 4 of 6 stress episodes the sleeve fell as much as the S&P. CAH and COR are near-identical drug wholesalers at the exact cap; Health Care is 24.3% with shared Medicare/pricing-policy exposure. |
| 7 | Strategy coherence and mandate fit | 8 | The all-stock request is answered directly and honestly; the allocation view is kept as a secondary option. | Rule (o) (tech 20-30%) is met at 26.2% only by counting Visa; IT-only is 19.3%. The report states neither figure. |
| 8 | Implementation and monitoring | 8 | Unchanged from Loop 10; kill criteria per holding; weekly checklist; estate-tax and withholding facts. | Next earnings for SNA (15 Oct), WFC (13 Oct), V (27 Oct) fall within weeks of the 25 Sep data cut-off; no refresh of post-cut-off news for the held names other than PTC. |
| 9 | Communication for the owner | 7 | Answer-first section 1; crisis falls; plain-English holdings table. | Section 6 carries roughly 50 near-identical re-assessment bullets; the audit table, A.4 (C1 row) and A.5 ("not yet checked" for 10 verified holdings) are stale or contradictory; rule (o) is not mentioned. |
| 10 | Reproducibility and auditability | 7 | `run_all.py`, pinned requirements, seeds recorded; risk and drawdown reproduce. | Gate OPEN for the ninth consecutive loop; RA/DV verdict changes are agent edits appended by hand; the quarter-label check cannot test 9 of 20 holdings (43.5% of weight). |

**Total: 8+8+8+7+7+8+8+8+7+7 = 76**

## 3. Must-fix to reach >=95 (ranked by score impact)

1. **SNA discount rate (criteria 5, 4).** The 10% holding's reverse DCF uses WACC 8.0%, not the programme basis (5.17% + ERP, about 9.2%). Recomputed: 2.9% implied at 8.0%; about 5.6% at 9.2% on the same FCF base, against a 5-7% base case, i.e. in_line. DVH1 called this MINOR and said the direction was "stronger", which is backwards. Fix: re-run on the programme basis, justify the FCF base (FY25 had 53 weeks), restate implied_vs_base; if in_line, downgrade to INCLUDE-SMALL (5% cap) and rebuild. Then add a WACC-vs-(5.17% + ERP) table for all 20 holdings and re-test the other 8 full-conviction names.
2. **UDR not propagated (criteria 1, 5).** `lead_build_portfolio.py` (about lines 190-195) maps V1/V2R "attractive" to "below" for top-70 names and ignores the RA14 re-assessment (below -> in_line). Fix: let the dossier/F-summary implied_vs_base override; rebuild; assert build implied == register implied for every eligible name (currently 4 mismatches).
3. **Missing disclosures and stale registers (criteria 3, 9).** State rule (o) and both tech figures (26.2% with Visa, 19.3% IT-only; record them in `tech_rule_o`). Make A.4/A.5 read `dv/*.json` (10 verified holdings print "not yet checked") and add the DV/DVH/RA series. Add one sentence on verification coverage (about 70 of 446 unchecked dossiers verified; sample FAIL rate 11 of 20 names), and caveat the bench.
4. **Risk window (criteria 6, 3).** Report beta, volatility and TE by sub-period and full history (beta 0.93-0.98 in every window before the last three years; TE 8.4%; stress ratios near 1) and stop leading with 0.56 and "38% market risk".
5. **Order-dependence statistic (criterion 3).** Report invariance within the half-conviction group (3 of 11) and say about 41% of weight is an order-dependent pick; drop the 12 -> 6 -> 12 history or caveat it; note orderings 1 and 3 are identical.
6. **Gate and controls (criterion 10).** Run C1 last on the frozen build and show PASS once; extend the quarter-label check to non-December fiscal years via XBRL fy/fp; script the RA/DV verdict-change append into `run_all.py`.

## 4. Numbers re-computed (report value vs mine)

| # | Number | Report | Mine | Result |
|---|---|---|---|---|
| 1 | Top-30 backtest CAGR (2012-01 to 2026-08) | 12.5% | 12.52% | PASS |
| 2 | SPY total-return CAGR, same window | 15.1% | 15.10% | PASS |
| 3 | Weights sum; max name; floor; Financials; max sub-industry | 1.0; 10.0%; 1.5%; 25.0%; 12.0% | 1.0; 10.0% (SNA); 1.5% (SYF); 25.00%; 12.00% (CAH+COR) | PASS |
| 4 | Displayed one-decimal weights sum | 100% | 100.0 (Financials shows 25.1 by rounding) | PASS (cosmetic) |
| 5 | Worst fall of the sleeve, 2005-2026 | -42.7% (2008-06-05 to 2009-03-09) | -42.66% (quarterly rebalance, same dates) | PASS |
| 6 | GFC replay, sleeve | -37.4% (87% real data) | -42.8% plain buy-and-hold on the 82% of weight priced at the start; -37.4% is the quarterly-rebalanced figure where V enters from March 2008 | PASS with wording gap |
| 7 | Volatility / tracking error / beta, last 3 years | 13.8% / 12.8% / 0.56 | 13.79% / 12.76% / 0.558 | PASS |
| 8 | Same measures, full history 2005-2026 (not in report) | not reported | vol 19.2%, TE 8.4%, beta 0.93-0.98 in each earlier sub-period | FAIL (omission) |
| 9 | Weighted trailing dividend yield | 1.5% (0.01476) | 1.476% | PASS |
| 10 | Effective bets by weight | 17.4 | 17.38 | PASS |
| 11 | Odds of a 10-point edge: one year / five-year average | 22% / 4% | 21.7% / 4.0% at TE 12.75% | PASS |
| 12 | Names in every ordering | 12 | 12 (9 are the INCLUDE names) | PASS, overstated |
| 13 | Tech share under rule (o) | not stated | 26.19% incl. Visa; 19.34% IT-only | FAIL (omission) |
| 14 | SNA reverse DCF | implied 2.9% at WACC 8.0% | 2.94% at 8.0%; 5.59% at 9.2% | FAIL (basis) |
| 15 | Holdings with independent check | A.5: 10 "not yet checked" | all 20 present in DV/DA files | FAIL (stale) |

## 5. Facts checked against primary sources

| Ticker | Claim | Source | Result |
|---|---|---|---|
| SNA | Q2'26 net sales $1,235.1m (+4.7%), organic +3.0%, EPS $4.96 vs $4.72 | SEC 8-K / company release | PASS |
| SNA | Consolidated operating margin 25.2% | release gives 21.8% before financial services; basis not reproducible | UNVERIFIABLE |
| ACGL | Q2'26 EPS $3.00, 18.0% ROE, BVPS $68.04 | Arch 8-K Ex-99.1 | PASS |
| ACGL | Combined ratio 83.5%; ex-cat/PYD 82.5% | same | PASS |
| UDR | Q2'26 FFOA $0.64; same-store NOI guide 0-1.25% | UDR 8-K | PASS |
| CVS | Q2'26 revenue $106.1bn, adjusted EPS $2.58, MBR 87.4% | CVS 8-K | PASS |
| DVA | Q2'26 revenue $3.554bn, EPS $4.02, FY26 guide maintained at OI $2.15-2.25bn | DaVita 8-K | PASS |
| DVA | Guidance path (Q1 raised, Q2 maintained) | DA5 plus release | PASS |

## 6. Loop-10 must-fixes

C1 staleness: NOT fixed (ninth loop). Quarter-label check: implemented, but covers only December year-ends. RSG/LH second valuation leg: moot (not held now).
