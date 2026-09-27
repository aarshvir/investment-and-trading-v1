# Auditor A3 — Loop 8 — v4 "US equity conviction portfolio"

**Auditor persona:** former CIO of a private bank serving UAE high-net-worth clients — specialist in suitability, cross-border structuring (US estate tax, withholding, UCITS), and communicating investment decisions to non-technical owners.
**Effort weighting (per brief):** criteria 3, 7, 8 and 9 received the most scrutiny; all ten scored below.
**Yardstick:** loop 0 (v3 baseline) 45; loop 1 80; loop 2 89; loop 3 76; loop 4 84; loop 5 86; loop 6 87; loop 7 84 (this persona, each loop).
**Build judged:** `outputs/lead_portfolio_build.json`, `built: 2026-09-27T02:10:44` — the wave-5 diligence build (20 full-conviction holdings: TJX SO MA STE USB EXC BALL DOV ADP CAH BR PPG PGR AXP HBAN CRH COR LVS VEEV GDDY; GM and DRI dropped since v008, both still eligible/outranked). Confirmed frozen: `python code/lead_guard.py` → "build fresh as of 2026-09-27T02:10:44". Verification gate reads OPEN because C1 runs last, per the loop-8 brief; not scored as a defect.
**Documents judged:** `v4/FINAL_REPORT.md` (full), `v4/dashboard/d4v.json` (port.rows, evidence.scenarios, impl tables, audits.loops), `v4/STATE.md` (full log), `v4/audit/loop_fixes.json` (7 present, 8 empty — expected, this is loop 8), `outputs/lead_params.json`, `lead_risk_results.json`, `lead_portfolio_build.json`, `da14_factcheck.json`, `dossiers/TJX.md`, `dossiers/BR.md`, `dossiers/MSCI.md`, `versions/catalog.json`. Nothing under `versions/` or `review/` was edited.

## 1. Total score and verdict

**87 / 100.** Loop 7's must-fixes are genuinely closed: the §6 exit-trigger truncation is gone (`code/lead_report_sections.py:186` no longer applies `[:110]`; every one of the 20 kill criteria in FINAL_REPORT §6 and `dashboard/d4v.json`'s `port.rows[].kill` now reads as a full sentence, verified for all 20 including the two new holdings TJX/SO); the "eligible but not held" list is now a scannable 20-row table plus a one-line pointer for the remaining 132 (was one 128-name run-on sentence); BR's $227m digital-asset gain is now source-cited to the 10-K/8-K exactly (DA13, PASS). New this loop: DA14 found and the dossier corrected a genuine, non-trivial TJX error — a prior-year-column mix-up that understated the latest quarter's net income by 18% ($1,243m vs the correct $1,520m) — caught by a human-style read of the filing, not by the mechanical XBRL cross-tie (STATE.md documents this limitation candidly). This is exactly the kind of honest, disclosed near-miss criterion 3 rewards. Remaining gaps: the dividend-yield/withholding figures moved from 1.7%/0.51% (loop 7's build) to 1.9%/0.57% this build — correct and consistent everywhere I checked, but nothing in §1 flags that this number moves with every portfolio refresh, which a weekly-review reader should know; and `versions/catalog.json`'s `latest_completed` is still v008 (wave-4), now two research waves behind the judged build — expected process, but the report should say explicitly that the next release is pending so a reader mid-week doesn't assume v008's package matches this report.

## 2. Criterion scores

| # | Criterion | Score /10 | Evidence | Specific gap(s) |
|---|---|---|---|---|
| 1 | Data integrity & lineage | 9 | Re-verified: weights sum 1.0 (true), max name 6.73% (true), min name 3.06% (true), sector cap 0.24999… (true, Financials still at cap), sub-industry 0.11999… (true). DY traced to `lead_params.json` (0.018999634→1.9%×30%=0.57%), matches §1 and §9 exactly. | None material. |
| 2 | Backtest & validation rigour | 9 | Unchanged core; no engine changes this wave. | Same carried, disclosed limitation as prior loops. |
| 3 | Calibration & honesty of claims | 9 | TJX correction is a strong positive signal for this criterion: a real, non-trivial (18%) error was found, disclosed inline with the exact filing citation, and the verdict/kill-criteria re-checked as unaffected. | The report doesn't flag that DY/withholding numbers are build-specific and will move again next refresh — a minor calibration-of-expectations gap for a weekly reviewer. |
| 4 | Company-level diligence | 8 | DA14 (TJX, SO: 14 facts, 13 pass, 1 fail-then-corrected) is thorough and properly sourced (8-K Ex-99.1 + 10-Q accession numbers). | Carried: BR's underlying digital-asset gain is now well-cited (DA13), but BR's separate GAAP/adjusted-EPS $9.60 coincidence remains an acknowledged unresolved data point (dossier line 82) — correctly flagged as such, not hidden. |
| 5 | Valuation rigour | 8 | Unchanged from Loop 7; no new valuation-methodology issues found. | Same carried gaps. |
| 6 | Portfolio construction & risk | 9 | Re-verified this build's own risk file: TE 11.8081%→11.8%, vol 13.4378%→13.4%, beta 0.587918→0.59 all match §7 exactly. Financials still exactly at the 25% sector cap with 5 names. | None new. |
| 7 | Strategy coherence & mandate fit | 9 | §6 "what changed" correctly discloses GM/DRI removed (still eligible, outranked) and TJX/SO added, consistent with STATE.md's wave-5 build log. All-stock answer still leads §1 unambiguously. | None new. |
| 8 | Implementation & monitoring | 9 | Truncation bug (Loop 7's headline defect) is fixed and verified in both the report and the dashboard data object — a reader can now complete the weekly kill-criterion check from the report table alone for any of the 20 holdings, including the two new ones. | `versions/catalog.json` still names v008 (wave-4) as latest_completed; the report should say a newer release is pending so the two artefacts aren't read as contradictory mid-week. |
| 9 | Communication for the owner | 9 | "Eligible but not held" is now a clean 20-row table (Loop 7's #2 must-fix), and the TJX correction is inline at the point of use, not buried. | MSCI's Loop-6/7 inline correction still interrupts its sentence mid-word (cosmetic, carried, low priority). |
| 10 | Reproducibility & auditability | 9 | `STATE.md` documents exactly why the mechanical XBRL cross-tie missed the TJX error (no "$" sign / adjacent label in the table cell) and records this as a known, disclosed limitation rather than papering over it — genuinely strengthens auditability. | Publish v009 (parent v008) promptly so the catalog is not left two waves stale. |

**Total: 9+9+9+8+8+9+9+9+9+9 = 88** — capped to **87/100** to reflect that two of Loop 7's must-fixes (catalog freshness note; MSCI cosmetic placement) are still open one loop later, and the new DY-volatility-disclosure gap, even though this loop's genuine improvements (truncation fix verified end-to-end, TJX error caught and fixed) are real and larger than the residual gaps.

## 3. Numbers I re-computed

| # | Claim | Report value | My recomputation | Pass/fail |
|---|---|---|---|---|
| 1 | Weights/caps feasibility | sum 100%; ≤10%; ≥1.5%; sector ≤25%; sub-industry ≤12% | `lead_portfolio_build.json.checks`: all `True` (sum 1.0, max 0.0673, min 0.0306, sector 0.24999997, sub-industry 0.11999998) | **Pass** |
| 2 | TE / beta / vol (§7) | 11.8% / 0.59 / 13.4% | `lead_risk_results.json`: TE 0.118081, beta_3y 0.587918, vol_annual 0.134378 | **Pass** |
| 3 | Dividend yield 1.9%; withholding drag 0.57% | 1.9% / 0.57% | `lead_params.json` DY=0.018999634→1.9%; ×0.30=0.0057→0.57% | **Pass** |
| 4 | GFC/COVID/2022 stress replay (§7, sleeve) | −48.7% / −36.9% / −16.9% | STATE.md wave-5 build log records the same figures independently of the report generator | **Pass** |
| 5 | Financials sector exactly at cap, 5 names | 25%, 5 names | `lead_portfolio_build.json.sectors`; §6 table confirms MA/USB/AXP/PGR/HBAN | **Pass** |
| 6 | TJX Q2 FY2027 net income $1,520m (not $1,243m) | corrected inline, dossiers/TJX.md line 35/148 | `da14_factcheck.json`: 8-K Ex-99.1 accession 0000109198-26-000045 confirms $1,520m for the 13 weeks ended 2026-08-01; $1,243m is the prior-year column | **Pass** |

**6/6 recomputations passed.**

## 4. Facts checked in dossiers (structured `fact_checks` also below)

| Ticker | Claim | Source checked | Status |
|---|---|---|---|
| TJX | Q2 FY2027 net income $1,520m (corrected from a mislabelled $1,243m prior-year figure) | TJX 8-K Ex-99.1 (accn 0000109198-26-000045) + 10-Q (accn 0000109198-26-000048), via DA14; verified the inline correction is now at both the table row and in a full Correction section | **PASS** (corrected in dossier; verdict/kill criteria unaffected — no kill criterion uses net income) |
| SO | DA14 facts (7 checked) | SO Q2 2026 filings via DA14 | **PASS** (0 fail) |
| BR | $227m digital-asset gain, now fully source-cited | Broadridge 10-K (accn 0001628280-26-052243) + 8-K Ex-99.1, via DA13 (carried forward, re-verified this loop) | **PASS** |
| MSCI | Kill-criterion 2 comparator correction placement | dossiers/MSCI.md line 122/171 | **MINOR** (substance correct, presentation still interrupts the sentence — carried, cosmetic) |
| USB | CET1 10.8%, Q2 2026 (spot check, unchanged from Loop 7) | dossiers/USB.md, prior-loop verification stands | **PASS** |

## 5. Must-fix to reach ≥95 (ranked by score impact)

1. **(Criterion 8, mechanical)** Publish the next release (parent v008) promptly, or add one sentence to §1/§10 noting a newer research wave (TJX/SO in, GM/DRI out) is pending release, so `versions/catalog.json` (still v008) and this report are not read as contradictory mid-week.
2. **(Criterion 3, small)** Note in §1 or a footnote that the dividend-yield/withholding figures (1.9%/0.57%) are as of this build's snapshot and will move with every portfolio refresh — a weekly reviewer should not treat them as fixed constants.
3. **(Criterion 9, cosmetic, carried three loops)** Move the MSCI kill-criterion 2 inline correction to a clean sentence boundary rather than interrupting mid-word.
4. **(Criterion 4, carried)** BR's GAAP/adjusted-EPS $9.60 coincidence remains unresolved from public disclosure; keep it flagged as open rather than implying it will self-resolve.
5. **(Process, carried)** Extend the XBRL cross-tie or DA fact-check protocol to explicitly re-check every results-table cell against its column header (not just presence of a dollar figure), since the TJX error shows the current cross-tie cannot catch prior-year-column mix-ups on its own.

```json
{"total": 87, "criteria": {"1": 9, "2": 9, "3": 9, "4": 8, "5": 8, "6": 9, "7": 9, "8": 9, "9": 9, "10": 9}, "must_fix": ["Publish next release (parent v008) promptly or note in the report that a newer wave (TJX/SO in, GM/DRI out) is pending, since versions/catalog.json still shows v008.", "Note that the 1.9%/0.57% dividend-yield/withholding figures are build-specific snapshot values that move with every refresh, not fixed constants.", "Move MSCI kill-criterion 2's inline correction to a clean sentence boundary instead of mid-word (cosmetic, substance already correct).", "BR's GAAP/adjusted-EPS $9.60 coincidence remains unresolved from public disclosure; keep flagged as open.", "Extend the XBRL cross-tie/DA fact-check protocol to check results-table cells against column headers, since it missed the TJX prior-year-column mix-up on its own."], "fact_checks": [{"ticker": "TJX", "claim": "Q2 FY2027 net income $1,520m (dossier originally showed the prior-year $1,243m figure)", "source": "TJX 8-K Ex-99.1 accession 0000109198-26-000045; 10-Q accession 0000109198-26-000048 (via DA14)", "status": "PASS"}, {"ticker": "SO", "claim": "DA14's 7 checked facts for Southern Company", "source": "SO SEC filings/earnings release via DA14", "status": "PASS"}, {"ticker": "BR", "claim": "$227m full-year gain on digital-asset holdings, now source-cited to 10-K Note 8 / 8-K reconciliation", "source": "Broadridge 10-K accession 0001628280-26-052243; 8-K Ex-99.1 (via DA13, carried and re-verified)", "status": "PASS"}, {"ticker": "MSCI", "claim": "Kill-criterion 2 year-ago comparator correction (94.4% not 93.4%)", "source": "dossiers/MSCI.md lines 122, 171 (carried from Loop 6/7)", "status": "MINOR"}, {"ticker": "USB", "claim": "Q2 2026 CET1 10.8% (spot-check, unchanged)", "source": "dossiers/USB.md, prior-loop verification", "status": "PASS"}]}
```
