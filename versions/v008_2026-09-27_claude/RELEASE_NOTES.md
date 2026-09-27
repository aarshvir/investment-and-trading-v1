# Claude v4, wave 4: 223 companies researched in full; 20 full-conviction stocks

Author: Claude. Status: completed research publication. No trades placed. This is research, not personalised investment, tax or legal advice; the author is not a licensed adviser.

**Data cutoff:** prices and the live snapshot are at the US close of 25 September 2026. SEC filings are those available to 25 September 2026; each dossier states its latest reported period. Prepared 27 September 2026 (Dubai). Portfolio build 2026-09-27T01:24:52 (content fingerprint d5c7e7554954). Verification gate: PASS.

**Parents:**
- **v007_2026-09-26_claude:** the previous Claude release, which this release updates.
- **v005_2026-09-26_codex:** the latest Codex release, reconciled in FINAL_REPORT §13.
- **claude-v3**, **codex-initial-audit** and **codex-deep-data-audit:** the earlier history.

## Relationship to earlier publications

This release **updates v007**. It replaces v007's list with one re-selected after 45 more companies were researched in full.

It **supplements and partly challenges v005; it does not supersede it.**
- v005 remains Codex's defensive 15/10/75 recommendation.
- This release answers the owner's all-stock brief.
- The owner chooses between them.

## What changed since v007

### More research
Wave 4 researched 45 more companies in full, in the same pre-committed order. They include Salesforce, Cisco, PepsiCo, Nike, Lowe's, Medtronic, US Bancorp, Capital One, Exelon and STERIS.

- **Companies researched in full:** 223 (was 178).
- **Companies passing every test:** 148 (was 116).
- **Triage-passed companies still queued:** 105.
- **Duplicate removed from the queue:** FOXA, the same company as FOX.

### The portfolio: all 20 holdings are now full conviction
- **Holdings (weights):** EXC 7.5%, STE 5.8%, BALL 5.7%, MA 5.7%, DOV 5.7%, USB 5.6%, DRI 5.4%, ADP 5.4%, CAH 5.1%, BR 5.1%, PPG 4.9%, CRH 4.6%, COR 4.6%, PGR 4.6%, AXP 4.6%, HBAN 4.5%, GM 4.3%, LVS 4.2%, VEEV 3.6%, GDDY 3.1%.
- **Added:** Exelon, STERIS, Ball, US Bancorp, PPG, GoDaddy.
- **Removed:** Host Hotels, MSCI, CVS, Comcast, Dollar General, Booking. All six are still eligible; newly researched full-conviction names outranked them.
- **Sensitivity of the pick to the tie-break rule:** 16 of the 20 are chosen under every alternative selection order tested.

### Verification
- **Pre-check and cross-tie:** every new holding was pre-checked mechanically, including a new cross-tie of dossier debt, cash and equity figures against SEC XBRL (`code/lead_xbrl_crosstie.py`).
- **Independent fact-checks:** DA11–DA13 checked the new holdings. They found:
  - **PPG:** debt overstated by about $0.7bn.
  - **Broadridge:** a debt figure that traced to no filing; debt is about $3.25bn, not $3.52bn.
  - **GoDaddy:** gross debt used where carrying value is the conventional basis.
  - **STERIS and Ball:** two immaterial slips.

  All are corrected, and no verdict changed.
- **Rule (m):** now written. No name is released as a holding until it passes the pre-checks and an independent fact-check, with every failure corrected.

### Report fixes from audit loop 7
- **Exit triggers:** §6 now shows every holding's first exit trigger in full. Before this release they were cut off at 110 characters.
- **Bench table:** the next 20 eligible names appear in a table. The full bench, with each name's margin to the 20th holding, is in `outputs/lead_j_sensitivity.json`.
- **Dashboard safeguard:** the build now fails if a review score shown on the dashboard differs from the reviewer's own file.

### Pending deals noted
F66 and F69 found that FOX (Roku) and MKC (Unilever Foods) have signed deals that the data set does not flag. Both are rated WATCH and are not eligible. The flag will be corrected at the next data refresh.

## Honest odds (base-case market of 6% a year; no assumed stock-picking edge)

- **Next 5 years:** 78% chance of a gain; 50% chance of beating the S&P 500; 87% chance of a fall worse than 20% at some point.
- **The owner's "10 points a year" goal:**
  - A single year 10 points ahead of the index happens about 20% of the time.
  - Averaging 10 points ahead over 5 years has about a 3% chance.
- **Past crises, replayed at today's weights:**

  | Crisis | This portfolio | S&P 500 |
  |---|---|---|
  | 2007–09 | −51% | −55% |
  | 2020 COVID crash | −39% | −34% |
  | 2022 | −19% | −24% |

  GDDY, VEEV and GM had no share price in 2007–09 (11% of the weight), so the 2007–09 replay measures the other 89%. The old GM went bankrupt in 2009, so the real loss would likely have been worse.
- **Risk profile:** tracking error 11.6%, beta 0.64, about 18 independent bets.
- **Holding costs for a non-US owner:**
  - US dividend withholding: about 0.5% of the portfolio a year (30% of a 1.7% yield).
  - US estate tax applies above about $60,000 of directly held US shares.

## Audit loops

| Loop | A1 / A2 / A3 | Note |
|---|---|---|
| 6 | 84 / 82 / 87 | Basis of v007 |
| 7 | 85 / 84 / 84 | Wave-4 build; all Loop-7 fixes applied before this release (audit/loop_fixes.json "7") |

The final C1 number trace ran against this build's content (d5c7e7554954): 297 checked, 296 matched; the one mismatch (a missing wave-4 row in the Appendix A.4 register) was fixed before release. Verification gate: PASS.

## Validation scope

- **What the checks establish:** calculation consistency, data lineage, replication, and dossier facts checked against SEC filings. Evidence: B1X, V1X, V2R, DA4–DA13, C1, X1, the risk re-computation and the daily-drawdown check.
- **What they cannot establish:** the truth of future earnings, or a validated stock-selection edge. No rule tested beat the S&P 500 on point-in-time data for 2012–2026.
- **Probabilities:** every one is conditional on the stated market scenarios and on zero alpha.
