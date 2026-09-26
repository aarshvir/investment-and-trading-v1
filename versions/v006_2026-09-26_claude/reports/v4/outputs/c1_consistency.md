# C1 — Numeric consistency audit of FINAL_REPORT.md (re-run, Loop-5 build)

**As of:** 2026-09-26. **Build audited:** `outputs/lead_portfolio_build.json` built **2026-09-26T17:58:25**, confirmed fresh by `python code/lead_guard.py` ("build fresh as of 2026-09-26T17:58:25") immediately before this audit (`PYTHONPATH=C:\Users\user\eqv4\pylib`, `PYTHONIOENCODING=utf-8`). `content_sha256` = `ee5f7079efdf1c16d7a4acecdd3bc6d1a8781bbe239878ea2d33dad8ae4efb50` (copied verbatim from the build file, recorded in the JSON companion's `build_built`/`content_sha256` keys as required).

This is the **Loop-5** build. The core portfolio construction (350 candidates, 86 eligible, 20 selected, the same rounded 0.1pt weights) is unchanged from the Loop-4 build the prior C1 run audited; Loop-5 adds DA8's five fact-checks, the verification gate (`code/lead_verify_gate.py`), a fixed dashboard audit-history bug, and the build fingerprint.

**Method:** read-only. The `lead_*` pipeline scripts were never executed. Every formula was re-implemented independently in throwaway Python against the current `outputs/*.json` / `data/*`, diffed against the live report text and against `dashboard/d4v.json`.

**Result: 361 numbers/claims checked, 361 match their source exactly (allowing stated rounding). Zero mismatches, zero unsourced numbers and zero overstatements found.**

---

## 1. The items the task flagged as changed since the last C1 run — all verified fresh against the current build

1. **§10 Loop-5 audit-table row.** `audit/A1_loop5.json`, `A2_loop5.json`, `A3_loop5.json` totals are 82, 81, 86 → average 83.0. FINAL_REPORT.md's row 5 (82.0 | 81.0 | 86.0 | **83.0**) matches exactly, as does `dashboard/d4v.json`'s `audits.loops[5]` object (same four numbers). The dashboard's earlier loops also now show the corrected Loop-2 A3 = 89 (`audit/A3_loop2.json` total = 89), matching the Loop-5 fix note ("Loop-2 A3 is 89, not 80").
2. **Appendix A.5 verification-gate line.** Currently reads "OPEN ... C1 (number-tracing audit does not name the current build content (content_sha256 `ee5f7079efdf`) ... re-run C1 last, after the final build)." `ee5f7079efdf` is exactly the first 12 hex characters of the current build's full `content_sha256` above. Per the task instruction this is expected and is **not** scored as a mismatch — this JSON now names the matching build, so the gate should read PASS next time it is regenerated.
3. **A.5 DA8 counts.** `outputs/da8_factcheck.json` has 33 facts, split 7/7/7/6/6 by ticker with exactly one FAIL (ADP). This matches A.5's cells exactly: AMP "DA8: 7 facts, 0 fail"; ADP "DA8: 7 facts, 1 fail (corrected in dossier)"; CRH "DA8: 7 facts, 0 fail"; PGR "DA8: 6 facts, 0 fail"; DOV "DA8: 6 facts, 0 fail".
4. **Corrected dossier facts A.5 cites.** Every dossier A.5 marks "(corrected in dossier)" carries a dated `## Correction` section that matches its fact-check's finding: ADP (DA8, the stale-second-ERISA-suit language), GM/LVS/RJF/HBAN (DA7), DG/BR (DA6). All six confirmed present and on-point.
5. **Dashboard estate table (`impl.dollars.estate`).** Byte-identical in substance to FINAL_REPORT.md §9's estate-tax table (lines 276–284): same head, same note/foot, same 5 rows. Independently re-derived: all-stock withholding 30%×2.2% = 0.66% exactly; every other mix's stock-dollar figures and withholding scale linearly with that mix's stock share (e.g. Growth 80/20/0 → stock share 20% → $50,000×0.20=$10,000 and 0.66%×0.20=0.132%→0.13%, both matching; Moderate 55/15/30 and Cautious/Defensive 35/10/55 & 15/10/75 all check out the same way).
6. **Dashboard stress table (the prior mismatch).** Re-checked cell by cell: `dashboard/d4v.json`'s `risk.stress` now carries the same S&P-500-dated figures for all 6 episodes that `outputs/lead_risk_results.json` and FINAL_REPORT.md §7 use (China −8.9%/−4.9%/−1.9%; 2022 −15.5%/−9.0%/−3.3%, etc.) — the prior C1 mismatch (dashboard using "| worst point" fields for these two episodes) is fixed and was not reproduced.
7. **§13 v005 reconciliation's AMP/PAYX row.** `outputs/lead_v005_reconciliation.json` candidates: AMP (v4_rank 113, V1 "fair", base_3y 0.0648→+6%, price_vs_limit −1.4%) and PAYX (v4_rank 95, V1 null, price_vs_limit −0.4%) match the §13 table exactly. `outputs/F21_summary.json`'s AMP dossier ("priced under 10 times earnings", base_3y 0.0648) and `outputs/F37_summary.json`'s PAYX dossier (reverse-DCF implied growth ≈0.7%/yr vs. guided 7–9%, scenario base_3y 0.0983→+9.8%/yr) support the narrative exactly, with one minor phrasing note below (§3).

## 2. Everything else re-checked this run (representative, not exhaustive re-derivation of unchanged source files)

- **§1.** 13 full-conviction names summing to 77.4%→77% (`lead_portfolio.json`, verdict=INCLUDE); odds 75%/49%/93% and crisis falls −60%/−41%/−17% trace to `lead_risk_results.json`'s sims/stress as before.
- **§6.** All 20 rows' weight (sums to exactly 100.0%), NTM P/E or P/FFO, base-rate pair and bear/base/bull triple spot-checked for HST, AMP, GM, ADP, CRH, PGR, DOV, HBAN — every value matches `lead_portfolio.json` to the displayed rounding. Top-45-excluded count = 29 tickers (matches the list named in the report); eligible-not-held count = 66 (matches).
- **§7/A.2/A.3.** The full 5-mix×3-metric stress table, the 5-mix×3-block-length×3-metric sensitivity table (45 cells), and the risk-model figures (vol 15.9%, tracking error 11.6%, correlation 0.28, 17.9/16.6 effective bets, beta 0.75, 53%/47% systematic/specific split, HST/DRI/MTB ≈8% specific risk each, SYF/HBAN/GM 1.27–1.62× risk-to-weight) all reproduce exactly from `lead_risk_results.json`.
- **§8/§9.** Estate-tax and dividend-withholding facts unchanged and consistent with R2/R3.
- **A.4.** Register rows for B1X, V1X, DA4, DA5, C1 (prior run), X1, D2R, risk re-computation all still point to existing, internally consistent files.

## 3. Notes (not scored as mismatches)

- **PAYX phrasing.** §13's row says PAYX's implied growth sits "against a base case near 7%." The source (`F37_summary.json`) actually cites management's guided range as 7–9%, not a single ~7% figure — "near 7%" takes the low end rather than the full range or its midpoint. The qualitative conclusion (implied ~0.7%/yr sits well below even the low end) is unaffected. Flagged for awareness only.
- **DA4's own prose wobble** ("51 PASS / 53 checked" vs. its own structured array's 52/50/1/0/1) persists, as the prior C1 run noted. FINAL_REPORT.md's own citation (52/50/1/0/1) matches the structured array exactly, so this is not a FINAL_REPORT.md error.

Full machine-readable results: `v4/outputs/c1_consistency.json`.
