# f7 (Fundamental diligence analyst) — report

**Answer first:** Of the three cyclicals reviewed, two are peak-cycle and should not be sized normally. **CF: REJECT** (Q2 2026 GAAP operating margin 50.5% sits above the 2022 all-time peak; the Street is cutting FY2026 estimates in real time; management names a live, likely-transient geopolitical cause — the Iran conflict/Strait of Hormuz disruption). **MPC: INCLUDE-SMALL** (same Iran-linked margin spike — Q2 2026 refining margin $36.33/bbl vs. a $13–19/bbl 2024–25 band — but MPLX provides real, evidenced non-cyclical ballast CF lacks). **PCAR: INCLUDE** (full weight) — the one name in this batch where earnings are NOT at a peak: FY2025 was a genuine 43%-off-peak trough, Parts+Financial Services already produce ~71% of segment profit, and consensus's 2026–27 recovery doesn't even reclaim the 2023 high.

## What I did

1. Read `CONVENTIONS.md`, `STATE.md`, `lead_v3_audit.md` for standing rules and the specific failure modes to avoid (adverse facts omitted, GAAP/adjusted mixed, "guidance raised" asserted without the prior range).
2. Pulled quant context from `lead_prelim_rank.csv` (QVM preliminary composite; b1 not yet ready) and `d4_live_snapshot.parquet` (NTM consensus, estimate-revision history, analyst targets, next-earnings dates) for all three tickers before touching filings.
3. Attempted to parallelize the three deep dives via the Agent tool; hit the program's 20-concurrent-subagent ceiling (other wave agents were running — dossiers for AIZ, ALL, BMY, DECK, EIX, GD, GL, HST, JBHT, RL, SYF, TGT, TPR, TROW, TRV, UPS are visible alongside mine in `v4/dossiers/`, confirming this). Per instruction not to retry, did all three dives directly myself, sequentially.
4. For each ticker: pulled full-history SEC XBRL company facts (`data.sec.gov/api/xbrl/companyfacts`) and parsed 15–18 years of annual and ~14 quarters of quarterly line items locally (script at `...\scratch_f7\xbrl_extract.py`, reusable); pulled the SEC filing index; fetched and read the last four 8-K earnings-release exhibits, the most recent 10-Q's MD&A, and (for CF) the FY2025 10-K, plus targeted 8-Ks for financing/officer-change events; ran `ratios.py` (CF, MPC) for the DuPont/leverage/cash-flow-quality ratio set and `valuation.py` (CF) for the EV bridge, reverse-DCF and scenario table; ran `lint_report.py` on all three finished dossiers — **all three pass with 0 errors / 0 warnings** (fixed one FAIL on CF: missing not-investment-advice disclaimer, added and re-linted clean).
5. **FMP connector note:** the `statements`, `analyst`, `calendar`, `earningsTranscript`, `secFilings` and `insiderTrades` tools all returned `ACCESS DENIED — requires a higher plan` on this account's tier; only `company` (profile/peers) worked. Pivoted entirely to SEC EDGAR (XBRL + filing index + direct filing fetches) and targeted WebSearch, which in practice gave better primary-source grounding anyway.

## Key numbers

| | CF | MPC | PCAR |
|---|---|---|---|
| Verdict | REJECT | INCLUDE-SMALL | INCLUDE |
| TTM/Q2'26 margin vs. own multi-year range | 41–50.5% op margin vs. 3.7–48.2% (10y) range, **above the 2022 peak** | $36.33/bbl vs. $13–19/bbl (2024–25) band, **~2x** | Truck seg. 3.9–6.9% vs. FY2023 peak-year levels — **trough, not peak** |
| Named driver | Iran conflict / Strait of Hormuz | Same (shared with CF) | NA freight recession easing + EPA 2027 clarity |
| Trailing P/E | 8.67x (looks cheap — the trap) | 13.6x (pipeline; likely adjusted-EPS-based) | 23.4x |
| Mid-cycle P/E (this dossier) | ~14.2x | not cheap once normalized ($/bbl basis) | ~22x (in line with trailing) |
| Balance sheet | Net debt/EBITDA 0.39x — very strong | ~2.5x, rising through the trough | Debt not cleanly isolable from PFS; equity growing, no buybacks |

## Data conflicts found (pipeline vs. primary filings)

- **MPC revenue/COGS:** pipeline TTM revenue $77.4B vs. COGS $134.4B (negative $57B gross profit) — a clear pipeline error; actual FY2025 revenue $132.7B per 10-K/XBRL.
- **MPC EPS basis:** pipeline's "actual" EPS fields are MPC's **adjusted** (non-GAAP) EPS, unlabelled ($10.70 FY2025 adjusted vs. $13.22 GAAP) — exactly the GAAP/adjusted mixing the prior audit flagged, just found inside the pipeline rather than a dossier.
- **MPC debt:** pipeline shows ~$5.4B consolidated debt; actual is $32.8–32.9B (MPC $7.2B + MPLX $25.6B). Pipeline cash ($7.768B) matched exactly, so the error is specific to certain fields.
- **PCAR:** operating income/debt/cash fields are blank in the pipeline — found to be a structural consequence of PACCAR's mixed industrial/financial-services XBRL tagging (sector-routing issue), not necessarily a pipeline bug; no numeric conflict found where the pipeline did report a figure (FY2025 EPS $4.51 matched exactly across pipeline, XBRL and the earnings release).

## Validation performed

- `lint_report.py`: 3/3 dossiers PASS (0 errors after one fix).
- `ratios.py`: run for CF and MPC (4-year annual DuPont/leverage/cash-flow-quality); not run for PCAR (segment mix makes a blended consolidated run misleading per the sector playbook's own routing note — reported segment margins by hand instead, formula shown inline).
- `valuation.py`: run for CF (EV bridge, reverse-DCF, 3-scenario table); not separately re-run for MPC/PCAR given time constraints — `ratios.py`'s own EV-bridge/multiple output was used for those two instead.
- Cross-checked at least one pipeline figure per ticker against a primary filing; found and reported conflicts above.

## Known limitations (by ticker, see each dossier's own limitations note for full detail)

- **CF:** auditor name/tenure/CAMs and full risk-factor diff not extracted; Form-4 transaction codes (sale vs. withholding) not individually verified (SEC ownership-feed access was intermittent — some fetches 503'd).
- **MPC:** annual consolidated debt (2022–2024) was estimated, not directly extracted, so the leverage trend is directionally right but the exact multiple should be re-verified against the 10-K debt note; the $253M "legal settlement" gain's counterparty was not identified.
- **PCAR:** the granular segment-level guidance (truck delivery counts, Parts margin range, FS pre-tax range) referenced in the assignment brief was not found in the press-release exhibits reviewed — only industry-volume and capex/R&D guidance was available; likely sits in the earnings-call transcript, which the FMP connector's plan tier blocked. Consolidated/PFS-only leverage not independently verified. Litigation/auditor/insider-trading red-flag scan was shallower than for CF/MPC given time spent on the other two names.
- All three: a full independent challenge pass (Stage 9, ideally via a second reviewer/subagent) was not performed given the subagent-concurrency constraint — the verdicts above are this analyst's own adversarial read, not independently cross-examined by a second agent.

## Files produced

- `v4\dossiers\CF.md` (~2,300 words, lint PASS)
- `v4\dossiers\MPC.md` (~2,500 words, lint PASS)
- `v4\dossiers\PCAR.md` (~2,300 words, lint PASS)
- `v4\outputs\f7_summary.json` (3 tickers: verdict, horizon, kill_criteria, key_adverse_facts, data_conflicts, next_earnings_date, confidence_in_thesis)
- `v4\outputs\f7_report.md` (this file)
- Working data (not for the record, kept for reproducibility): `C:\Users\user\AppData\Local\Temp\claude\scratch_f7\` — XBRL extracts and `ratios.py`/`valuation.py` input JSONs for all three tickers.
