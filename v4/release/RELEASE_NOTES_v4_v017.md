# Claude v4 all-stock release (whole-index diligence, valuation re-assessment) — 6 October 2026

**Author:** Claude. **Status:** completed research release, not a trade instruction. **Data cutoff:** SEC filings and prices as of 25 September 2026 for the base build; every name that entered or stayed after the 5–6 October re-assessments was re-checked against EDGAR up to 6 October 2026 (Schneider's $205 cash bid for PTC, 8-K accession 0001193125-26-413124, is the key post-cutoff event). Macro inputs: Fed funds 3.75–4.00% (16 Sep), 10-year Treasury 5.17% (25 Sep).

**Explicit parents:** v016_2026-10-05_codex, v015_2026-10-04_codex, v014_2026-10-01_codex, v013_2026-10-01_codex, v012_2026-09-27_codex, v011_2026-09-27_claude, v010_2026-09-27_claude, v005_2026-09-26_codex, claude-v3, codex-initial-audit, codex-deep-data-audit.

## What changed
- **Portfolio (20 names, all stocks):** BR, WTW, GDDY, V, CAH, ACGL, WFC, COR, FIS, INTU, ADSK, BIIB, FSLR, BKNG, FDX, ACN, OMC, AMCR, CVS, VZ. 18 of 20 differ from v011; only BR and GDDY are kept. Eight are full conviction, twelve half conviction.
- **Cause:** the valuation method behind v011 had systematic errors (stock pay added back, interest double-counted, earnings treated as cash, stale discount rate, no bank/insurer method). Re-assessing the 12 v011 holdings and 35+ further names moved PTC (pending $205 Schneider takeover), VEEV, MSCI, NOW, SNA, MPC, SWK, TGT, BMY and ZBRA to WATCH or ineligible and cut most others to half conviction. Every change is in outputs/lead_verdict_changes.json and §6.
- **All 500 companies** now have a full dossier and an All-500 register (outputs/all500_register.md, dashboard tab "All 500").
- **Rule (o), owner request:** technology 20–30% (29.3% including payments, 20.9% Information Technology alone). **Rule (p):** the analyst's re-assessed implied-vs-base and base return override the systematic valuation mapping so the ranking equals the register. Both committed in outputs/rule_commitments.jsonl before the build.
- **Verification gate** extended to accept the DV series (same standard).

## Accepted, changed, rejected from Codex v012–v016
Adopted: v016's 40% temporary-drawdown tolerance and the 100%-stock mandate; v015's dated price/event checks as methods. Changed: v4 redesigns the all-stock slate from filings rather than carrying v014/v015 weights or their defensive PG/PEP/PEG substitutions. Rejected: applying v015's old-basket return bands to this portfolio; treating 40% as a floor. Unresolved: v012–v015's individual price and event claims were not re-verified; actual positions, tax facts; Codex entry limits versus this release's valuations.

## Audit status (honest)
Loop 11 scored A1 76, A2 79, A3 77 (average 77.3, below Loop 10's 86.7: the auditors found real problems, which this release fixed in part). Fixed: UDR/analyst-valuation propagation (rule p), SNA discount rate (SNA now above, out), rule (o) and verification disclosure, DV series in A.4/A.5, Codex v012–v016 reconciliation, 40% tolerance and beta caveat. **Not fixed, for budget reasons (5M tokens per 12 hours):** independent verification of 391 of 500 dossiers; a WACC table for all 20; risk figures by sub-period; order-dependence by conviction group; portfolio-level dollar scenarios; no second audit loop after the fixes. Final C1 number trace: 1,216 comparisons, 1,214 matched; the two mismatches (full-conviction wording in §6 and §13) and one footnote were corrected afterwards; verification gate PASS (all 20 holdings independently checked, every FAIL corrected).

## Validation scope
Checks establish calculation consistency and dossier facts against filings for the verified subset; they do not establish future earnings or a stock-selection edge (no tested rule beat the S&P 500 point-in-time). In the verification series 137 of 564 facts failed and were corrected, so unverified dossiers carry the same risk. Research, not licensed investment advice.
