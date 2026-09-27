# f6 — Fundamental diligence analyst: JBHT, UPS, GD

## Answer first
- **JBHT (J.B. Hunt): INCLUDE-SMALL**, 12–24mo. Real freight-cycle inflection (Q2'26 revenue +19.4% YoY, intermodal op. income +58%) but it is one quarter old, valuation (31.4x trailing / 24.1x NTM P/E) already prices meaningful recovery, and OCF fell YoY despite higher earnings.
- **UPS: WATCH**, 12–24mo. Restructuring narrative is real but unproven in GAAP (Q2'26 GAAP op. margin 4.1% vs. adjusted 9.2% — the widest gap in two years); dividend frozen 7 quarters at an 80–90% GAAP payout ratio, buybacks at $0 in H1'26, and active Teamsters litigation over the restructuring itself.
- **GD (General Dynamics): INCLUDE**, 12–36mo. Three consecutive quarters of guidance raises with exact prior ranges quoted, record $136.5B backlog (1.4x book-to-bill), Marine Systems margin improving (not deteriorating, contrary to the historical execution-risk narrative), lowest leverage of the three. Main risk is structural (multi-decade program execution, FY2027 appropriations timing), not company-specific.

## What was done
Read `CONVENTIONS.md`, `STATE.md`, `lead_v3_audit.md` first. Used `lead_prelim_rank.csv` (preliminary Q/V/M ranks — official `b1_live_scores.csv` not yet ready) and `d4_live_snapshot.parquet` for quant/market context. **Delegation to one sub-agent per ticker was attempted but failed** — the Agent tool's concurrent-subagent limit was reached (many sibling agents from this overnight multi-agent run were already active); per instructions this was not retried, and all three dossiers were researched and written directly by this agent instead. FMP's connector (`statements`/`earningsTranscript`/`insiderTrades`/`secFilings`) was rate-limited for the entire session (shared plan, concurrent load) and was not used; all figures come from SEC EDGAR direct fetches (`data.sec.gov` XBRL + `www.sec.gov/Archives` filings, which had a brief maintenance outage mid-session that recovered), the locally cached `d3_xbrl_facts.parquet`/`d4_validation_sec.csv`, and WebSearch/WebFetch against company IR releases, 8-K earnings exhibits, and earnings-call transcripts. Ran `finance-skills:stock-analysis`'s `scripts/ratios.py` and `scripts/valuation.py` for each ticker (inputs disclosed inline in each dossier) and `scripts/lint_report.py` on each finished dossier, fixing all error-level findings (all three now lint PASS or PASS-WITH-WARNINGS, 0 errors).

## Key numbers (verified against primary SEC sources in this session)
| | JBHT | UPS | GD |
|---|---|---|---|
| FY2025 revenue (GAAP) | $11.999B | $88.661B | $52.550B |
| NTM P/E (calendarized) | 24.1x | 12.0x | 18.5x |
| Net debt/EBITDA | ~1.0x | ~1.8–2.2x | ~1.0x |
| Next earnings | 2026-10-15 | 2026-10-27 | 2026-10-28 |

## Validation checks performed
- Cross-checked every headline financial figure against SEC XBRL (`data.sec.gov/api/xbrl/companyfacts`) and, where available, `v4/data/d4_validation_sec.csv`'s independent SEC-validated figures — pass for all three tickers' FY2025 revenue/NI.
- **Found and reported a material data-quality issue**: `lead_prelim_rank.csv`'s `rev` field is wrong for JBHT (43–57% understated) and UPS (~15–16% understated) versus SEC-validated figures, while `ni`, `opinc`, `ocf`, `capex` fields all reconcile exactly to independently-rebuilt TTM figures — isolating the bug to the revenue field specifically. Separately verified the Q/V/M/prelim percentile scores do not appear to depend on the broken `rev` column. For GD, the file's `rev`/`ni` fields are internally correct but appear to **predate GD's Q2 2026 earnings release** — a staleness gap, not a wrong-number bug.
- Ran `lint_report.py` on all three dossiers: JBHT and UPS/GD all pass with 0 errors (UPS and GD carry 1–2 heuristic warnings on aggregator-citation style, addressed where practical).

## Known limitations
- No sub-agent parallelism was available this session (see above); all three tickers were researched sequentially by one agent, which is slower and means depth is not perfectly even across the three (GD's FY2025 10-K narrative sections — risk factors, legal proceedings — were not independently re-read in full; JBHT's got the deepest primary-document read since SEC Archives came back up earliest in the session).
- Some granular items flagged as follow-ups rather than completed: exact debt maturity schedules for all three; SBC% of revenue for all three; a full Form 4 insider-trading pattern for all three (FMP was rate-limited); GD's EAC/estimate-at-completion adjustment history; UPS's and GD's current-year (FY2025) legal-proceedings section (2023-era pension/litigation figures used for UPS, flagged as such).
- `ratios.py` inputs used some estimated D&A/interest/tax figures where the cached XBRL slice pulled in-session didn't have the exact period — each dossier discloses this inline and the estimates are directionally reasonable (checked against reported margin/EPS growth for internal consistency).

## Files produced
- `v4/dossiers/JBHT.md` (~2,500 words), `v4/dossiers/UPS.md` (~2,700 words), `v4/dossiers/GD.md` (~2,500 words)
- `v4/outputs/f6_summary.json` (3 ticker objects: JBHT, UPS, GD) + `v4/outputs/f6_summary.json.meta.json`
- `v4/outputs/f6_report.md` (this file)
