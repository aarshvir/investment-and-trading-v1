# Claude v4, wave 5: 268 companies researched in full; every holding's latest quarter re-verified

Author: Claude. Status: completed research publication. No trades placed. This is research, not personalised investment, tax or legal advice; the author is not a licensed adviser.

**Data cutoff:** prices and the live snapshot are at the US close of 25 September 2026. SEC filings are those available to 25 September 2026; each dossier states its latest reported period. Prepared 27 September 2026 (Dubai). Portfolio build 2026-09-27T02:34:17 (content fingerprint 174b254450b3). Verification gate: PASS.

**Parents:**
- **v008_2026-09-27_claude:** the previous Claude release, updated here.
- **v005_2026-09-26_codex:** the latest Codex release, reconciled in FINAL_REPORT §13.
- **Earlier history:** claude-v3, codex-initial-audit, codex-deep-data-audit.

## Relationship to earlier publications

This release **updates v008**. It **supplements and partly challenges v005; it does not supersede it.** v005 remains Codex's defensive 15/10/75 recommendation, while this release answers the owner's all-stock brief. The owner chooses between them.

## What changed since v008

### More research
Wave 5 researched 45 more companies in full, including Berkshire Hathaway, JPMorgan, Home Depot, P&G, Chevron, Caterpillar, Palo Alto Networks, Synopsys, Starbucks, Prologis and Southern Company.
- **Researched in full:** 268 companies (was 223).
- **Eligible:** 172 companies (was 148).
- **Still queued:** 68 triage-passed companies.
- **Re-runs:** two batches misread "research only" and wrote no files; both were re-run.
- **Duplicate removed:** NWSA is the same company as NWS.

### Portfolio: 20 full-conviction stocks
- **Weights:** TJX 6.7%, SO 6.4%, MA 5.6%, STE 5.6%, USB 5.6%, EXC 5.6%, BALL 5.5%, DOV 5.5%, ADP 5.2%, CAH 5.0%, BR 5.0%, PPG 4.8%, PGR 4.6%, AXP 4.6%, HBAN 4.6%, CRH 4.5%, COR 4.5%, LVS 4.1%, VEEV 3.5%, GDDY 3.1%.
- **Added:** TJX and Southern Company.
- **Removed:** GM and Darden. Both are still eligible; they were outranked.
- **Selection sensitivity:** 14 of the 20 are chosen under every alternative selection order tested.

### Verification
- **New holdings:** TJX and SO passed both mechanical checks. DA14 then found one error: TJX's latest-quarter net income was the prior-year column ($1,243m shown; $1,520m actual). It has been corrected.
- **Sweep of all 20 holdings for the same class of error (DA15–DA17, 69 facts).** It found one more error: ADP's Q4 FY26 net earnings are $978.6m; the dossier had repeated the Q1 and Q2 figures. That is corrected, Exelon's blank cells were filled from its 8-K, and no other prior-period swaps were found.
- **Mechanical checks:** the XBRL cross-tie now also checks quarterly net income in prose. It does not read unlabelled table cells, a limitation recorded in STATE.md; those still depend on the independent fact-check.
- **GoDaddy:** a second valuation leg now supports the verdict. Peer EV/EBITDA and EV/FCF against WIX, VRSN, TCX and SHOP corroborate the reverse-DCF view.
- **Rule (m):** it is now written next to rules (a)–(l) in the build script.

## Honest odds (base-case market of 6% a year; no assumed stock-picking edge)

- **Next 5 years:** 79% chance of a gain, 50% chance of beating the S&P 500, and 83% chance of a fall worse than 20% at some point.
- **Owner's "10 points a year" goal:** a single year that far ahead happens about 20% of the time; averaging it over 5 years has about a 3% chance.
- **Past crises (replayed at today's weights):**

  | Crisis | This portfolio | S&P 500 |
  |---|---|---|
  | 2007–09 | −49% | −55% |
  | COVID crash (2020) | −37% | −34% |
  | 2022 | −17% | −24% |

  GDDY and VEEV had no share price in 2007–09 (7% of the weight), so that replay measures the other 93%.
- **Risk profile:** tracking error 11.8%, beta 0.59, and about 18 independent bets.
- **Costs and tax:** withholding takes about 0.57% of the portfolio a year (30% of a 1.9% snapshot dividend yield). US estate tax applies above about $60,000 of directly held US shares.

## Audit loops

| Loop | A1 / A2 / A3 | Note |
|---|---|---|
| 7 | 85 / 84 / 84 | Basis of v008 |
| 8 | 86 / 85 / 87 | Wave-5 build; all Loop-8 fixes applied before this release (audit/loop_fixes.json "8") |

Final C1 number trace against this build's content: 312 checked, 312 matched, 0 mismatches. Verification gate: PASS.

## Validation scope

- **What the checks establish:** calculation consistency, data lineage, replication, and dossier facts checked against SEC filings. Evidence: B1X, V1X, V2R, DA4–DA17, C1, X1, the risk re-computation and the daily-drawdown check.
- **What they cannot establish:** the truth of future earnings, or a validated stock-selection edge. No rule tested beat the S&P 500 on point-in-time data for 2012–2026.
- **Conditioning:** every probability is conditional on the stated market scenarios and on zero alpha.
