# HANDOFF v4: US equity research, point-in-time rebuild (independently audited)

Data to the US close of Friday 25 September 2026. Written 26 September 2026 (UAE time) for Aarsh and for whoever continues the work. Research and general information only; not personalised investment, tax or legal advice (the author is not a licensed adviser; no trades are placed).

Numbers that change whenever the pipeline re-runs (weights, probabilities, stress results) live only in `FINAL_REPORT.md` and the dashboard, which are generated from the data. This handoff points to them rather than copying them, so it cannot go stale.

---

## 0. The answer in one minute

- **The high-confidence decision is the allocation, not the stock picks.** Build three layers:
  1. an S&P 500 index core in an Irish-domiciled UCITS fund (CSPX or VUAA): not US-situs for estate tax, with 15% dividend withholding inside the fund;
  2. a T-bill reserve sized to the loss you can live with;
  3. a bounded satellite of diligence-verified US stocks at no more than 15–20% of the total.
- **Why stocks are only a satellite.** The pre-registered v4 model and the old v1, v2 and v3 models all trailed the S&P 500 over 2012–2026 on point-in-time data. A second agent replicated this independently. The satellite is sized and simulated with zero assumed alpha. Its job is owning verified businesses at fair prices and diversifying away from the index's mega-cap concentration.
- **Where 90% confidence is achievable.** At the base-case market return of 6% a year, the Moderate mix (55% index / 15% stocks / 30% T-bills) held 10 years and the Cautious mix (35/10/55) held 5 years both clear a 90% chance of a gain. No single stock and no stock basket does (`FINAL_REPORT.md` §1 and §7).
- **The drawdown decision is yours.** A 15–20% limit that must hold even in a 2008 repeat needs roughly a third or less in equities (§1 and §7 give the exact figures).
- **One next step for the owner:** decide which of the three drawdown answers is yours (§1; dashboard "One next step").

## 1. Where things are

| What | Where |
|---|---|
| Deliverable (report) | `v4/FINAL_REPORT.md`: plain-English sections 1–13 (§12 is a glossary; §13 reconciles with Codex v005) and Appendix A. The appendix holds the technical detail, the register of independent checks and a per-holding verification table. |
| Dashboard (what the owner reads) | https://claude.ai/artifact/U2RjG3tNLgLfVCF55x6cEf. Source: `v4/dashboard/equity_audit_v4.html`, built by `code/lead_assemble.py` plus `dashboard/v4tabs.js`, with data object `dashboard/d4v.json`. v4 tabs come first; older tabs are kept and labelled superseded. |
| Build log and every decision with its time | `v4/STATE.md` |
| Agent contract (paths, rate limits, output rules) | `v4/CONVENTIONS.md` |
| How to reproduce | `v4/README_RUN.md`, `v4/run_all.py`, `v4/requirements.txt` |
| Company dossiers | `v4/dossiers/<TICKER>.md` (primary-source, linted); verdict JSONs in `v4/outputs/F*_summary.json` / `f*_summary.json`; one-line theses and kill criteria in `v4/outputs/lead_holding_notes.json` |
| Backtest | `v4/outputs/b1_report.md`, `b1_results.json`; replication `b1x_report.md` |
| Valuation | `v4/outputs/v1_valuation_table.csv`, `v1_valuation.json`; independent re-derivation `v1x_verification.md` |
| Risk and allocation odds | `v4/outputs/lead_risk_results.json` (stress replays, worst fall, equity-share limits, bootstrap settings and sensitivity) |
| Data audits | `v4/audit/da1_data_audit.md` (prices), `da2_data_audit.md` (SEC fundamentals), `da3_data_audit.md` (estimates); `v4/outputs/da4_factcheck.md` (dossier facts); `d2r_report.md` (price-coverage repair) |
| Implementation facts (UAE) | `v4/outputs/r2_implementation_facts.md`, verified and extended by `r3_implementation_verification.md` |
| Independent audit loops | `v4/audit/RUBRIC.md`, `A1/A2/A3_loop<N>.md/.json`, `loop_fixes.json` |
| Lead's own mistakes, logged | `v4/outputs/lead_error_log.md` |
| v3 findings (what was wrong) | `v4/outputs/lead_v3_audit.md` |

## 2. How the answer was reached

1. **Audit v3.** Fifteen findings were re-computed from v3's own files: the "90%" was an assumption, momentum carried look-ahead bias, the real worst fall was −36% not −26%, and weight caps were broken.
2. **Build point-in-time data.**
   - D1: S&P 500 membership since 2000.
   - D2: total-return prices for 1,172 symbols, validated against three vendors.
   - D3: as-filed SEC XBRL fundamentals, usable only after their filing date.
   - D4: a live snapshot of all 503 members, with NTM valuation calendarised.
   - Three deep data audits (DA1–DA3) followed, then DA4 on dossier facts.
3. **Pre-register a model before any test** (STATE.md): quality, value, 12-1 momentum and earnings surprise; sector-neutral; equal-weighted; monthly; 10 bps costs.
4. **Backtest 2012–2026 on point-in-time members (B1), then replicate blind (B1X).** No variant beat the S&P 500. Calibrated base rates show P(12m gain) of 65–70% and P(beat S&P) of 43–46%, flat across score deciles.
5. **Choose the strategy from the evidence:** index core, T-bill reserve and a zero-alpha satellite (STATE.md 02:55).
6. **Select the satellite with rules fixed before the diligence verdicts were read** (STATE.md 03:00), amended only to remove inconsistencies the auditors found (§3 below).
7. **Run risk (B2 module, `lead_risk.py`):** daily-data crisis replays, a stationary bootstrap under Bear 2% / Base 6% / Bull 9% scenarios, the worst-fall anchor, and the equity share that would have kept each crisis within −20% or −15%.
8. **Audit loops:** three independent auditors score everything on a 100-point rubric (§5 below). Every must-fix is implemented before the next loop.

## 3. Sleeve rules and every amendment

Base rules (fixed 03:00, before the verdicts were read), in `code/lead_build_portfolio.py`:
- **Eligibility:** official point-in-time rank in the top 70; 1-year volatility ≤ 45%; no pending takeover; V1 valuation verdict attractive or fair; diligence verdict INCLUDE or INCLUDE-SMALL.
- **Diversification:** at most 2 names per GICS sub-industry.
- **Weights:** inverse-volatility; sector ≤ 25%; sub-industry ≤ 12%; every constraint verified after solving (`code/lead_portfolio.py`).

Amendments after Loop 1. Each removes an internal inconsistency an auditor found, and none uses returns:

| | Amendment | Trigger |
|---|---|---|
| a | A missing V1 valuation makes a name ineligible | RL entered Loop 1 because its valuation row arrived after the build |
| b | A negative V1 base case makes a name ineligible | A "fair price" holding cannot have a negative own-valuation base case |
| c | A V1 valuation with no base case is incomplete, so ineligible | Same logic as (a) |
| d | INCLUDE-SMALL halves the per-name cap (5%). Capacity the caps cannot absorb goes to the index fund | With few names in few sectors, the old rule pushed half-conviction names to the full 10% cap |
| e | The analyst's own reconciled valuation (dossier §7 / T2 notes) must also be cheap or fair | JBHT's dossier valued it about 31% below the price while V1 said "fair" |
| f | REITs use the FFO-based verdict rebuilt from filings (V2R), not V1's proxy | V1's REIT "FFO" (net income + total depreciation) counted one-off property-sale gains, flattering HST and FRT |

A freshness guard (`code/lead_guard.py`) records a sha256 manifest of every build input. Downstream scripts stop if anything changed or appeared after the build.

## 4. Reproduce every number

- `python run_all.py --list` prints the canonical order.
- `python run_all.py` re-derives every published number offline (checks, then the lead stages).
- `--stages all` re-runs from the downloads (network; data after 2026-09-25 will differ).
- Python 3.11.9 with the exact library versions in `requirements.txt`, installed to `C:\Users\user\eqv4\pylib`. Set `PYTHONPATH` to that folder and `PYTHONIOENCODING=utf-8` on Windows.
- Seeds:
  - allocation bootstrap: seed 7, 20,000 paths, mean block 21 trading days, with 5- and 63-day sensitivity runs;
  - B1 Dirichlet test: seed 42;
  - B1 unit tests: seed 20260926.
- Independent cross-checks that should keep matching:
  - B1X vs B1: within 0.04 pts/yr;
  - daily worst falls, `lead_check_daily_dd.py`: top 30 −43.7% vs −44.4%, sleeve rule −41.8% vs −41.7%;
  - V1X vs V1;
  - DA4 and DA5 dossier facts; every holding's dossier has been fact-checked by at least one independent agent or auditor;
  - `lead_check_risk_contrib.py`: sleeve risk re-derived from raw prices, and the run fails on any mismatch;
  - V1X/V2R valuation re-derivations and C1's report-number trace. The full register is FINAL_REPORT Appendix A.4.

## 5. Audit loops

Rubric: `audit/RUBRIC.md`, 10 criteria × 10 points. Personas stay the same every loop so scores are comparable:
- **A1:** quant and data (former head of quant research);
- **A2:** investment committee (former PM at a top-tier long-only fund);
- **A3:** client and compliance (former CIO of a private bank serving UAE clients).

Auditors run on the prompt `prompts/A_auditor.md`, with the exact persona and focus text in `prompts/A_personas.md`. Scores and "what changed" for every loop are in `FINAL_REPORT.md` §10 and the dashboard tab "Independent audit scores". Loop 0 scored v3 as delivered: 41 / 42 / 45. Loop 1 scored the first v4 draft: 85 / 76 / 80. Loop 2 scored the reconciled 20-name build: 88 / 89 / 89.

To run the next loop:
1. Finish all fixes.
2. Run `python run_all.py`.
3. Check `python code/lead_guard.py`.
4. Freeze the deliverable (do not edit while auditors work).
5. Launch A1–A3 with {LOOP} = N+1.
6. Implement every must-fix.
7. Add a `loop_fixes.json` entry.

## 6. Known limitations (all disclosed in the report)

- No stock-selection edge was found. Every probability assumes zero alpha for the satellite.
- **Survivorship.** Free price data lacks many delisted companies, and the residual bias is measured at +1.0 pt/yr against RSP. DA1 showed the "no price data" list contains download failures; D2R re-downloads it into separate files. The backtest has not been re-run on the repaired data (see `d2r_report.md` for the expected impact).
- **Sample start.** The backtest starts in 2012 because as-filed XBRL data starts in 2009–2011. 2007–09 is covered only by price-based stress replays.
- **Estimates.** No point-in-time analyst-estimate history exists in free data, so NTM valuation is a live overlay only.
- **Simulation method.** Simulations rebalance daily (B2's method); crisis replays rebalance quarterly, as the operating rules say.
- **Tax.** Tax facts assume the owner is neither a US citizen nor a green-card holder. Still unverified: IBKR market-data fees, and the estate-tax situs of idle cash at a US broker.

## 7. Operating the portfolio (owner)

- **Weekly, about 30 minutes:** follow the checklist in `FINAL_REPORT.md` §9 and the dashboard's Implementation tab. Most weeks the right action is no trade.
- **Quarterly:**
  1. Refresh D4 (live snapshot) and B1 live scores.
  2. Refresh V1 valuations.
  3. Update the dossiers of held names for the new quarter's results.
  4. Re-run `lead_build_portfolio.py` onward.
  5. Replace a holding only if it leaves the top quarter of the ranking or a kill criterion fires.
- **Fold the satellite into the index** if it trails the S&P 500 by more than the threshold in §9 over 24 months. The threshold is derived from its tracking error.

## 8. Lessons for whoever continues

- **Stale inputs.** Never build from inputs that are still being written. The freshness guard now enforces this.
- **Background agents can hang.** F9 waited for hours on an interactive directory-request tool. Ban interactive tools in agent prompts, and check transcript activity rather than waiting.
- **Rate limits.** Two session limits were hit overnight. Use Sonnet for grunt agents, keep concurrency moderate, and resume killed agents rather than restarting them.
- **Generated vs static text.** Keep every number that can change in generated sections. Static text is where stale numbers hide; agent C1 checks it before each audit loop.
- **Conflicting valuations.** A dossier and the valuation model can disagree silently. Every dossier now ends its valuation section with an explicit reconciliation with V1.

## 9. Shared workspace: Codex and Claude releases

A parallel Codex workstream exists in this workspace. The shared rules are in the project root: `CLAUDE.md`, `AGENTS.md`, `RESEARCH_VERSIONING.md` and `LATEST_HANDOFF.md`, plus `versions/catalog.json`.
- **Numbered releases are immutable.** Everything under `versions/vNNN_*` is a snapshot. Publish a new version, never overwrite.
- **Publishing.** Use `python tools/publish_research_release.py --author Claude --package <zip> --notes <notes.md> --summary "..." --parents <release IDs> --data-cutoff "..."`.
- **Reconciling before publishing.** The latest completed Codex release when this work began was **v005_2026-09-26_codex**: a conservative decision pack with 25% maximum equity and AMP/PAYX entry limits. v4 records what it adopts, confirms, changes, rejects or leaves open from v005:
  - generated in `FINAL_REPORT.md` §13 and the dashboard tab "Reconciliation with Codex v005";
  - built by `code/lead_reconcile_v005.py`;
  - claim checks in `outputs/x1_v005_verification.md`.
- **Neither release overrides the other.** A higher version number means newer, not better. The owner decides.
- **Do not edit Codex's `review/` workstream**, and do not edit any release folder.

## Update 26 Sep 2026 13:40 (Loop-4 build, frozen for audit)
- Mandate now all-stock (owner's choice); §1/hero lead with the 20 stocks; allocation view kept as the lower-risk option.
- Research coverage: 455 triaged + 40 earlier dossiers; 133 full diligence verdicts (waves 1 F19–F33 and 2 F34–F48); 189 triage-advanced names still queued (data/full_diligence_wave2.json "queued"). Next: wave 3 (F49+) on the next 45, same order, after the Loop-4 audit so the freeze is not disturbed.
- Holdings (Loop-4): full HST DOV DRI ADP BR CRH GM MTB LVS RJF AMP PGR HBAN; half UDR CVS CMCSA DG BKNG DVA SYF. 86 eligible.
- Helpers: code/lead_check_implied.py (lists summaries missing implied_vs_base), code/lead_add_implied.py (records an agent's stated value with its source).
- Pending: Loop-4 audit (A1–A3 via prompts/A_personas.md incl. "Notes added from Loop 4"), fixes, then numbered release via tools/publish_research_release.py (parents v005_2026-09-26_codex claude-v3 codex-initial-audit codex-deep-data-audit).

## Update 26 Sep 2026 18:12 — published v006_2026-09-26_claude
- Release v006 = the Loop-5 build (content_sha256 ee5f7079…), verification gate PASS (DA4–DA8 cover all 20 holdings; C1 361/361).
- Next release must name v006_2026-09-26_claude as a parent. Before packaging: rebuild → `python code/lead_verify_gate.py` must PASS (fact-check any new holding with a DA-series agent; re-run C1 LAST so it records the new content_sha256) → `python code/lead_package_release.py` → tools/publish_research_release.py.
- Rule changes: `python code/lead_commit_rules.py "<reason>"` before any build (the build refuses otherwise).
- Wave 3 (F49–F63) launched 18:12; queue after it: data/full_diligence_wave3.json "queued".

## Update 26 Sep 2026 19:20 — published v007_2026-09-26_claude
- Wave 3 (F49–F63) folded in; 178 researched, 116 eligible; holdings 16 full + 4 half (see FINAL_REPORT §6). Rules (k) and (l) committed. Next release must name v007 as a parent.
- Standard sequence for any new build: commit rule changes → build (run_all) → `code/lead_dossier_precheck.py` on new holdings → DA-series fact-check of new holdings → append dated corrections (+ inline "[Corrected …]" markers on operative sentences) → audit loop → C1 last → `code/lead_verify_gate.py` PASS → package → publish.

## Update 27 Sep 2026 01:30 — published v008_2026-09-27_claude
- Wave 4 folded in: 223 researched, 148 eligible; 20 full-conviction holdings. Next release parent = v008.
- New tools: code/lead_xbrl_crosstie.py (dossier debt/cash/equity vs SEC XBRL, latest two balance-sheet dates); rule (m) written in STATE.md.

## Update 27 Sep 2026 02:40 — published v009_2026-09-27_claude
- Wave 5 folded in: 268 researched, 172 eligible, 68 queued; 20 full-conviction holdings. Next release parent = v009. Remaining queue: data/full_diligence_wave5.json "queued".

## Update 27 Sep 2026 03:40 — published v010_2026-09-27_claude
- Wave 6 folded in: 313 researched, 200 eligible, 24 queued; next release parent = v010. Diligence prompts now require verbatim quotes for guidance (pre-check type "guidance_unquoted").
