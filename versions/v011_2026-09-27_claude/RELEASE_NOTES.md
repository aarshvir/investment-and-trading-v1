# Claude v4, wave 7: the full-diligence queue is complete (336 companies); 20 full-conviction stocks

Author: Claude. Status: completed research publication. No trades placed. This is research, not personalised investment, tax or legal advice; the author is not a licensed adviser.

**Data cutoff:** prices and the live snapshot are at the US close of 25 September 2026. SEC filings are those available to 25 September 2026. Prepared 27 September 2026 (Dubai). Portfolio build 2026-09-27T04:50:23 (content fingerprint cd5f38e02373). Verification gate: PASS.

**Parents:**
- **v010_2026-09-27_claude:** the previous Claude release, updated here.
- **v005_2026-09-26_codex:** the latest Codex release, reconciled in FINAL_REPORT §13.
- **Earlier history:** claude-v3, codex-initial-audit, codex-deep-data-audit.

## Relationship to earlier publications

This release **updates v010**. It **supplements and partly challenges v005; it does not supersede it.** v005 remains Codex's defensive 15/10/75 recommendation. This release answers the owner's all-stock brief. The owner chooses between them.

## What changed since v010

- **The diligence queue is complete.** Wave 7 researched the last 23 queued companies, among them Intel, PayPal, KKR, Realty Income, Chipotle, Yum, Labcorp and Republic Services.
  - Every S&P 500 company that passed the quick screen now has full SEC-filing research: 336 companies, of which 214 pass every test.
  - Three second share classes (GOOG, FOXA, NWSA) are judged with their sibling.
  - The queue is complete *as of the data cutoff*. Each new quarter and each weekly review can still change a verdict.
- **Holdings (all 20 full conviction):** WEC 8.3%, RSG 7.0%, TJX 6.4%, MA 5.6%, USB 5.6%, LH 5.6%, STE 5.3%, BALL 5.2%, DOV 5.2%, ADP 4.9%, BR 4.6%, PGR 4.6%, AXP 4.6%, HBAN 4.6%, MCK 4.5%, CRH 4.2%, LVS 3.8%, PTC 3.8%, VEEV 3.2%, GDDY 3.0%.
  - Added: Republic Services and Labcorp.
  - Removed: Exelon and Cardinal Health. Both are still eligible; they were outranked.
- **Verification:**
  - DA19 fact-checked Republic Services and Labcorp. It found one Labcorp results-table row whose figures belonged to a different quarter, now corrected. It also found one Republic Services supporting figure that cannot be traced to a filing; that figure is now marked.
  - DA20 added a second, peer-multiple valuation for both. It corroborates both reverse DCFs. Republic Services' 27x earnings is mid-pack against its waste-industry peers, and its leverage is the lowest of the group.
  - Cumulative across DA4–DA20: 397 facts checked and 20 failures, every one corrected in its dossier.
- **New mechanical check:** `code/lead_quarter_label_check.py` maps each results-table row to the SEC's own calendar-quarter figure and flags a label that disagrees.
  - It catches the uncorrected Labcorp row, and it reports zero flags on the current dossiers.
  - It covers the 12 December-year-end holdings. The other 8 still rely on the independent fact-check.
- **Honest disclosure of order-dependence:** the report now shows the full history of names chosen under every selection ordering tested: 12 → 12 → 16 → 14 → 9 → 6. The tie-breaker now decides much of the list. The 2007–09 replay stays between −54% and −47% across orderings.
- **Holdings above 25x earnings are flagged in §6:** VEEV, RSG and MA. They have the least room for a disappointment.

## Honest odds (base-case market of 6% a year; no assumed stock-picking edge)

- **5-year odds:** a 79% chance of a gain, a 50% chance of beating the S&P 500, and an 84% chance of a fall worse than 20% at some point.
- **The owner's "10 points a year" goal:** a single year 10 points ahead happens about 20% of the time. Averaging 10 points ahead over 5 years has about a 3% chance.
- **Past crises, replayed at today's weights:**

  | Crisis | This portfolio | S&P 500 |
  |---|---|---|
  | 2007–09 | −47% | −55% |
  | COVID crash (2020) | −37% | −34% |
  | 2022 | −17% | −24% |

  GDDY and VEEV (6% of the weight) had no share price in 2007–09, so that replay measures the other 94%.
- **Risk:** tracking error 11.8%, beta 0.59, about 19 independent bets.
- **Costs for a non-US holder:**
  - Withholding: about 0.49% of the portfolio a year (30% of a 1.6% snapshot yield).
  - US estate tax applies above about $60,000 of directly held US shares.

## Audit loops

| Loop | A1 / A2 / A3 | Note |
|---|---|---|
| 9 | 84 / 84 / 80 | Basis of v010 (fixes applied) |
| 10 | 85 / 89 / 86 | Wave-7 build; all Loop-10 fixes applied before this release (audit/loop_fixes.json "10") |

Final C1 number trace against this build's content: 331 checked, 331 matched, 0 mismatches. Verification gate: PASS.

## Validation scope

- **What the checks establish:** calculation consistency, data lineage, replication, and dossier facts against SEC filings. The evidence is B1X, V1X, V2R, DA4–DA20, C1, X1, the risk re-computation and the daily-drawdown check.
- **What they cannot establish:** the truth of future earnings, or a validated stock-selection edge. No rule tested beat the S&P 500 on point-in-time data for 2012–2026.
- **Probabilities:** every probability is conditional on the stated scenarios and on zero alpha.
