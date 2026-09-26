# Independent audit rubric — v4 US equity research program

Auditors score the **output** (final report + dashboard), the **artefacts** (code, data, dossiers, handoff) and the
**investment strategy**. Each criterion is scored 0–10 and must be justified with specific evidence (file/line, number,
or quote). Total = sum (max 100). Be adversarial: re-compute at least 5 headline numbers yourself from the data files;
open at least 5 dossiers and check at least 3 facts per dossier against primary sources (SEC filings or company releases).
Do not reward effort, volume, page count or error counts — reward correctness, evidence and decision-usefulness.

Anchors for every criterion: **10** = would pass a top-tier institutional investment committee / fund due-diligence review
unchanged · **9** = minor, non-decision-relevant gaps · **8** = several gaps or one decision-relevant gap ·
**6–7** = material gaps · **≤5** = unreliable.

| # | Criterion | What a 10 requires |
|---|---|---|
| 1 | Data integrity & lineage | Every material number traceable to a dated source; second-source validation of prices and reported fundamentals with pass rates; missing data explicit (never silently filled); horizon/basis of every valuation multiple declared (NTM vs FY) |
| 2 | Backtest & validation rigour | Point-in-time index membership and as-filed fundamentals; pre-registered model (no tuning on the test window); transaction costs; long sample incl. stress regimes; statistics with t-stats/CIs; subperiod stability; residual biases quantified and disclosed |
| 3 | Calibration & honesty of claims | Every probability/expected return is conditional on stated, sourced assumptions; empirically calibrated where possible; ranges not points; no claim exceeds its evidence; limitations prominent; prior errors conceded |
| 4 | Company-level diligence | Primary-source (SEC/company) evidence for every holding; latest quarter, guidance, balance sheet, cash conversion, capital allocation, adverse facts, bull/bear, measurable kill criteria; facts checked correct |
| 5 | Valuation rigour | Consistent horizon (NTM), coherent methods (no double counting), reverse-DCF/implied expectations, peer/own-history context, business-model-appropriate metrics (banks/insurers/payments/asset managers) |
| 6 | Portfolio construction & risk | Feasible constraints verified after solving; diversification (sector/sub-industry/factor/theme); risk contributions; daily-data drawdowns; historical stress tests; correlation/AI-theme concentration addressed |
| 7 | Strategy coherence & mandate fit | Answers the owner's actual question (target-independent conviction, 10–20 stocks, ranked & weighted) and fits his constraints (UAE residency, $50–100k, stated drawdown tolerance, weekly review, ~30 min/week) with explicit trade-offs |
| 8 | Implementation & monitoring | Structure/tax facts cited (estate tax, withholding, UCITS), entry/rebalance/sell rules, kill criteria, weekly review checklist, refresh process, what would change the view |
| 9 | Communication for the owner | Answer-first, numbers not adjectives, plain English for a non-technical reader, visuals drawn to scale, exactly one next step, no jargon without explanation, disclaimers present but not preachy |
| 10 | Reproducibility & auditability | Code runs end-to-end from documented commands; data files + meta sidecars; handoff lets a new analyst reproduce every headline number; versions and seeds recorded |

Output format for each auditor (write to `v4\audit\<auditor_id>_loop<N>.md`):
1. Total score /100 and one-line verdict.
2. Table: criterion, score, evidence for the score, specific gap(s).
3. "Must-fix to reach ≥95" list — concrete, testable, ranked by score impact.
4. Numbers you re-computed (value in report vs your value, pass/fail).
5. Facts you checked in dossiers (claim, source checked, pass/fail).
