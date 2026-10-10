# DVH3 verification, 6 Oct 2026

Scope: RTX. Research only; not personal advice. Full table: `DVH3_factcheck.json` (28 facts: 13 PASS, 7 MINOR, 6 FAIL, 2 UNVERIFIABLE).

Sources: Q2 2026 10-Q (acc 0000101829-26-000027), 8-K Ex-99 releases of 23 Jul 2026 (acc 0000101829-26-000025), 21 Apr 2026 (-000009) and 27 Jan 2026 (-000003), XBRL company facts, d4 live snapshot. Press-sourced items (Q2 call transcript, Q3 date) are labelled.

| Area | Result |
|---|---|
| Quarterly figures (Q1 2025 to Q2 2026, FY2025) | All revenue, operating income, GAAP net income and diluted EPS cells pass, with correct period labels. Q3 2025 operating income is directly tagged. |
| Guidance | Sales, EPS and organic ranges (Q1 and Q2) pass verbatim. **FAIL:** the dossier says FY2026 FCF guidance was not re-confirmed at Q2; the Q2 release raised it to $8.50-$8.75B from $8.25-$8.75B. |
| Balance sheet | Consolidated cash, debt, equity and net debt/equity (0.44x) pass. Net debt/TTM EBITDA gap filled: 1.95x. |
| Dividend | **FAIL:** quarterly dividend is $0.73 ($0.68 before April 2026), not $0.60-$0.64; the XBRL $1.46 for Q2 is two real $0.73 declarations. |
| Red flags | **FAIL:** SEC investigation (powder metal), DOJ deferred prosecution agreements with a monitor engaged April 2026, State Department consent agreement and DCMA cost-accounting claims are live in the 10-Q, not "prior years". RTX expects no material adverse effect. |
| Valuation method | **FAIL:** 8% WACC not tied to the 5.17% Treasury, SBC not deducted, TTM FCF ($8.36/share) about 32% above the FY2026 guide ($6.32/share; H1 2026 helped by $1.5B more factoring). Programme basis (Ke 7.33%, ten years then 3.0%, equity basis, FCF after SBC): implied 10-year FCF growth 7.7%; the dossier's own base path is worth 1.08x the market price. **implied_vs_base: below -> in line.** |
| Other | Q3 2026 earnings 20 Oct 2026, not about 27 Oct (FAIL, low severity). The 24.6x triage multiple is NTM, not stale. Scenario returns re-derive within 0.7 point (not changed). |

Verdict changes: none (INCLUDE-SMALL unchanged). Implied-vs-base changed for RTX (below -> in line). `F105_summary.json` RTX entry updated (implied_vs_base, reconciliation, kill criteria 4 and 5, next_earnings_date, two adverse-fact lines). Dossier `RTX.md` carries 12 inline corrections and a `## Correction (verification DVH3, 2026-10-06)` section.

Limits: beta is the snapshot's Yahoo value (raw 0.287, Blume 0.52), not a recomputed regression; Ke of 7.33% is low and results are sensitive (base path 0.93x at Ke 8.0%). Noncontrolling-interest distributions and the pension deficit are not deducted. The call-transcript operating figures (AOG, MRO, turnaround) and the Q3 date are press-sourced and not on EDGAR. FY2025 10-K auditor and restatement check rests on the EDGAR filing list, not a full re-read.
