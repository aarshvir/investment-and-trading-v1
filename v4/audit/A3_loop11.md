# Auditor A3 — Loop 11 — v4 "US equity conviction portfolio"

**Persona:** former CIO of a private bank serving UAE high-net-worth clients (suitability, cross-border structuring, communicating to non-technical owners). Weighting: criteria 3, 7, 8, 9 most; all ten scored.
**Build judged:** `outputs/lead_portfolio_build.json`, content_sha256 `45758e6055db...`, built 2026-10-06T21:54:39 (`code/lead_guard.py`: fresh). Holdings: DVA DG CVS ACN UDR SYF BKNG SNA CAH BIIB GDDY ACGL ADSK WFC FSLR BR INTU COR WTW V. Verification gate reads OPEN only because C1 runs last (not scored).
**Read:** FINAL_REPORT (full), dashboard `d4v.json` (hero, answer, next), lead_portfolio_build / lead_risk_results, lead_verify_gate output, outputs/dv/DVH1, STATE.md tail, WTW/SNA/DVA/SYF dossiers, the shared `versions/catalog.json`, LATEST_HANDOFF.md and Codex v016 release notes and brief. Nothing under `versions/` or `review/` was edited.

## 1. Total score and verdict

**77/100** (Loop 10: 86). The numbers still reproduce and the all-stock answer is direct and candid about odds. The drop is about what the report no longer says, not about arithmetic. Between 27 Sep and 5 Oct Codex published v012 to v016 (v014 is a 100%-stock, 20-name book; v016 records the owner's 5 Oct clarification that a temporary drawdown of up to 40% is tolerable and hands Claude a redo brief). FINAL_REPORT §13 still reconciles only v005 and the report still frames risk around 15-20%. The owner's tech 20-30% request (rule (o)) is nowhere in the report or dashboard. The verdict says all 500 were "researched in full" without saying how few were independently checked. 18 of 20 holdings changed from v011 in nine days and the Verdict does not say so.

## 2. Criterion scores

| # | Criterion | Score | Evidence | Gaps |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 8 | Re-computed: weights sum 1.0; 0.1pt-rounded weights sum 100.0; sector caps hold (Financials 0.2500, HC 0.2431, IT 0.1934); yield 1.476% = report 1.5%; drawdown/vol/TE/beta reproduce from d2_adjclose. DVA, SNA, WFC, SYF figures match SEC XBRL. | A.4 register stale (stops at DA20; DV02/DV09/DVH1-4 absent; wave 8 "159 researched"; C1 row cites the 27 Sep build). §6 intro still says "triage of all 455 names ... strongest then researched in full", contradicting §1 (all 500) and the hero ("500 got full research so far" after a "quick pass"). Prices are 25 Sep, 11 days old at audit; Q3 earnings begin within days. |
| 2 | Backtest & validation rigour | 9 | Unchanged (no engine change); disclosed residual survivorship (+1.0 pt/yr vs RSP). | Carried, disclosed. |
| 3 | Calibration & honesty | 7 | Good: no promise to beat the index; 4% chance of +10 pts over 5 years; errors list. Weak: (a) "Every one of the 500 ... researched in full" with no statement that only ~70 of 446 non-held dossiers have any independent check (the Loop-11 brief item); (b) Verdict leads with GFC replay -37% but the report's own tail anchor is -42.7% (§7), which the Verdict omits; (c) the holdings' own base cases average +16.1%/yr (bear -3.0%, bull +33.0%, weighted from `table`) while the Verdict says "index-like, no edge" (6%); the gap is never reconciled or even stated; (d) ~50 near-identical re-assessment bullets in §6 read as boilerplate and bury the 4-5 real errors. | See must-fix 3, 4. |
| 4 | Company-level diligence | 8 | All 20 holdings have at least one independent check (gate); 12 have DV-series checks this week. DVH1 found valuation-method FAILs in 4 of 7 sampled holdings (WTW, V, WFC, INTU) and corrected them: the process works. My checks all pass (section 5). | DVA, DG, CVS, UDR, SYF, BKNG rely on DA4-DA6 (26 Sep, 3-7 facts) that pre-date their 5-6 Oct re-assessments; the re-assessed valuations (UDR RA14, BKNG RA10) have no independent check. WTW §6 exit comparator still reads "vs 4-6% in the last four quarters"; DVH1 says Q1'26 organic was 3%, so the name sits exactly at its trigger line (repeats Loop-10 must-fix 3). SNA (10%, full conviction) carries an unexplained -11.2% OCF decline and an unresolved data conflict in its own dossier, and its WACC is not tied to 5.17% (DVH1 MINOR). |
| 5 | Valuation rigour | 7 | The RA/DV re-assessment (SBC as cost, FCF not EPS, rf 5.17%) is the right fix and is disclosed. | Method errors were present in most sampled holdings until DVH1, which implies holdings without a DV-series re-derivation (e.g. DVA, DG, CVS, BKNG, ADSK, ACN, FSLR, BR) rest on author re-assessment only. 13 of 20 enter on the analyst route ("implied below base") with base cases the report itself calls optimistic. |
| 6 | Portfolio construction & risk | 9 | Constraints verified exactly after solving; 17 effective bets; beta 0.56; TE 12.7%; replay and daily drawdown recompute within 0.5 pt (-36.9 vs -37.4 GFC; buy-and-hold vs daily-rebalanced convention). | Worst fall -42.7% sits just beyond the owner's newly stated 40% review line; not discussed. Displayed Financials weights add to 25.1% (rounding; cap holds unrounded). |
| 7 | Strategy coherence & mandate fit | 6 | Answers the owner's all-stock request directly; keeps the allocation view as secondary. | (a) Does not reflect the owner's 5 Oct 40% tolerance / stock-only restatement (catalog `latest_completed` = v016); the Verdict and §7 still revolve around 15-20% and the Defensive mix. (b) Rule (o) (owner request: tech 20-30%) is absent from FINAL_REPORT and the dashboard. The build gives IT 19.3% (below 20%) and 26.2% with Visa (Payments); the report must state both. (c) 18 of 20 names differ from v011 (only GDDY and BR carry over); not headlined, and nothing tells a reader who started building v011 what to do. (d) No comparison with Codex's v014/v015 20-name stock book, the direct competitor to this portfolio. |
| 8 | Implementation & monitoring | 7 | Estate tax, withholding, IBKR/UCITS facts cited and re-verified; per-$10k formula; kill triggers for each name; weekly checklist. | The all-stock path has no rule for -20% (§9 says only that "tolerance is reached"). At $100k all-stock the report shows the estate-tax exposure (~$10.8k) but recommends no mitigation (cap US-situs at ~$60k, or a UCITS core for the excess) for the owner's chosen structure. The entry plan (3 tranches over ~6 weeks) runs straight through Q3 earnings for most holdings with no refresh instruction. The next-step text offers two decisions plus a reading task. |
| 9 | Communication for the owner | 7 | Answer-first Verdict, honest odds, per-$10k table. | The Verdict is ~25 lines before the owner reaches the all-stock risk number he cares about; "a 86% chance" typo; the largest holding SNA has the least plain-English line in the list ("INCLUDE - high-ROE ... no formal numeric guidance to break (a governance point...)"); dashboard "next step" is not one step; no dollar outcomes for a $50k or $100k stake. |
| 10 | Reproducibility & auditability | 8 | Guard/gate/commitments work; every number I re-derived reproduces. | A.4/A.5 stale as above; STATE plans to publish "v012" with parents v011 and v005, but v012-v016 already exist (Codex) and `latest_by_author.Claude` is v011: numbering and parents must follow RESEARCH_VERSIONING.md. |
| | **Total** | **77** | | |

Amendments: rule (o) was committed before the build (cdef8c5f, 5 Oct) and the swaps list is empty, so no result-chasing. The disclosure gap, not the rule, is the issue.

## 3. Must-fix to reach >=95 (ranked)

1. **Reconcile Codex v012-v016 and the 5 Oct mandate in FINAL_REPORT §13, §1, §7 and the dashboard Reconciliation tab.** Record adopted/changed/rejected/unresolved for v014 (100%-stock 20-name book), v015, v016 (40% tolerance, brief requirements). Restate the Verdict risk text against 40% (sleeve worst fall -42.7%, 86% chance of a >20% fall) and demote the 15-20% framing. Set the release's explicit parents to v016, v015, v014, v013, v012, v011 and a free number (v017). Verify by grep: §13 names every v012-v016 id; the catalog parents list matches.
2. **State rule (o) and the tech figures in §1 and §6** (both: 26.2% incl. Visa under the Payments sub-industry; 19.3% IT-only), say it was an owner request committed before the build, and add the same line to hero/answer in `d4v.json`. Also fix the contradictory coverage text: §6 intro ("triage of 455, strongest researched in full"), hero ("quick pass; 500 got full research so far"), A.4 (add DV02, DV09, DVH1-4, correct wave 8 count) so all say the same thing as §1.
3. **Say how much is independently verified.** Add to §1 and A.5: "All 500 have a full dossier; N of them (including all 20 holdings) have an independent check; the rest do not." Add portfolio-level scenarios: weighted bottom-up bear/base/bull (-3% / +16% / +33% a year, 3-yr) next to the zero-alpha 6% case, with $50k and $100k ending values and one sentence on why the owner should plan on the lower figure. Add the -43% tail to the Verdict bullet.
4. **Headline the turnover**: "18 of 20 names changed since v011 because the valuation method was corrected (list the causes); if you bought v011, here is what to do" in one paragraph; collapse the ~50 identical re-assessment bullets into a table.
5. **Independent re-check of the six holdings whose only checks pre-date re-assessment** (DVA, DG, CVS, UDR, SYF, BKNG), and correct the WTW §6 trigger text to "3% in Q1'26 and 5% in Q2'26 (at the threshold)". Fix §13 "only overlap is HIG" (now SNA, held at 10% at $369 vs Codex's $310 entry limit; state the disagreement).
6. **Implementation for the all-stock path**: what to do at -20% and -40%, an explicit estate-tax mitigation for amounts above ~$60k, an instruction to refresh prices/earnings before each tranche, one single next step.

## 4. Numbers re-computed

| Item | Report | Mine | Result |
|---|---|---|---|
| Weights sum / cap checks | 1.0; caps true | 1.0000; Fin 0.2500, HC 0.2431, IT 0.1934, max name 0.10 | pass |
| Rounded weights sum | 100.0% | 100.0 (displayed Financials 25.1) | pass (rounding) |
| Sleeve worst fall 2005-26 | -42.7% (2008-06-05 to 2009-03-09) | -42.66% on 2009-03-09 | pass |
| S&P worst fall | -55.2% | -55.19% | pass |
| GFC / COVID / 2022 replay | -37.4 / -34.4 / -10.1 | -36.9 / -34.1 / -9.6 | pass (within convention) |
| 3-yr vol / TE / beta | 13.8% / 12.8% / 0.56 | 13.7% / 12.7% / 0.556 | pass |
| Dividend yield | 1.5% (1.476%) | 1.476% | pass |
| Withholding drag | 0.44% | 30% x 1.476% = 0.443% | pass |
| Full-conviction share | 59% | 59.3% | pass |
| Weighted bottom-up base/bear/bull | not stated | +16.1% / -3.0% / +33.0% a year | gap (unreconciled with the 6% case) |
| Verification coverage | not stated | all 20 covered (gate); six rely on 26 Sep checks | gap |

## 5. Facts checked in dossiers (SEC XBRL companyfacts; issuer releases via DVH1)

| Ticker | Claim | Source | Result |
|---|---|---|---|
| DVA | Shareholders' deficit $(651,082)K at 2025-12-31 | SEC XBRL 10-K | PASS |
| DVA | Q1'26 revenue $3.416bn, EPS $2.87; Q2'26 revenue $3.554bn, EPS $4.02 | SEC XBRL 10-Q | PASS |
| SNA | Q2'26 diluted EPS $4.96; H1 OCF $640.2m; cash $1,644.7m; LTD $887.0m | SEC XBRL 10-Q | PASS |
| SNA | Quarterly net-sales table mixes XBRL and release bases (~$9m a quarter) | DVH1 | MINOR (growth rates right) |
| WFC | Q2'26 net income $6,407m, EPS $2.00, non-interest expense $13,661m; Q1 EPS $1.60, expense $14,330m | SEC XBRL 10-Q | PASS |
| SYF | Q1'26 NI $805m, EPS $2.27; Q2'26 NI $885m, EPS $2.59 | SEC XBRL 10-Q | PASS |
| UDR | Q1'26 revenue $425.8m, EPS $0.57 | SEC XBRL 10-Q | PASS |
| UDR | Q2'26 revenue $425.4m, EPS $0.21 | not yet in companyfacts feed | UNVERIFIABLE |
| WTW | Kill criterion comparator "4-6% in last four quarters" | DVH1: Q1'26 organic 3% | FAIL (corrected only in the Correction section, not in the §6 trigger text) |
| WTW | Reverse DCF EPS-based, CoE 9.5% | DVH1 | FAIL, corrected |
| V | Reverse DCF rf 4.2%, SBC added back | DVH1 | FAIL, corrected |
| INTU | Q4 EPS, capex, SBC reading | DVH1 | FAIL x4, corrected |

Machine-readable copy in `A3_loop11.json`.
