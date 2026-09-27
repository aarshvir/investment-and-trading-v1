# Claude v4, wave 6: 313 companies researched in full; one fabricated-guidance error caught before release

Author: Claude. Status: completed research publication. No trades have been placed. This is research, not personalised investment, tax or legal advice; the author is not a licensed adviser.

**Data cutoff:** prices and the live snapshot are at the US close of 25 September 2026. SEC filings are those available to 25 September 2026. Prepared 27 September 2026 (Dubai). Portfolio build 2026-09-27T03:34:07 (content fingerprint 7ac48e4da848). Verification gate: PASS.

**Parents:** v009_2026-09-27_claude (the previous Claude release, which this updates); v005_2026-09-26_codex (reconciled in FINAL_REPORT §13); claude-v3, codex-initial-audit, codex-deep-data-audit.

## Relationship to earlier publications

This release **updates v009**. It **supplements and partly challenges v005; it does not supersede it.** v005 is Codex's defensive 15/10/75 recommendation. This release answers the owner's all-stock brief. The owner chooses between them.

## What changed since v009

- **Coverage:** wave 6 researched 45 more companies in full, including J&J, Honeywell, RTX, Thermo Fisher, CME, Duke Energy, Apollo, Citigroup, ResMed, McKesson, PTC and WEC. That makes 313 researched and 200 eligible; 24 triage-passed names remain queued.
- **Holdings (all 20 full conviction):** TJX 6.8%, WEC 6.7%, STE 5.6%, MA 5.6%, USB 5.6%, BALL 5.6%, DOV 5.5%, EXC 5.3%, ADP 5.3%, CAH 5.0%, BR 5.0%, MCK 4.8%, PGR 4.6%, AXP 4.6%, HBAN 4.6%, CRH 4.5%, LVS 4.2%, PTC 4.1%, VEEV 3.5%, GDDY 3.1%.
  - **Added:** WEC, McKesson, PTC.
  - **Removed:** Southern Company, PPG, Cencora. All three are still eligible; they were outranked.
- **Caught before release: ResMed.** DA18 found three problems in the ResMed dossier:
  - it quoted FY2027 guidance that does not exist in the cited 8-K;
  - it reported full-year buybacks and dividends as nine-month figures;
  - it omitted a disclosed divestiture.

  A guidance-free re-assessment cut ResMed to half conviction, so it dropped out and Cardinal Health (already fact-checked twice) returned. §6 now lists every diligence error that changed a verdict or a holding.
- **Other fact-check corrections:**
  - PTC's quarter labels were one quarter early; now corrected.
  - WEC had an arithmetic slip; now corrected.
  - McKesson was clean.
  - Cumulative across DA4–DA18: 374 facts checked, 17 failures, every one corrected in its dossier.
- **New controls:**
  - Future diligence must quote the source sentence for every guidance figure, and a pre-check flags unquoted guidance (it flags the ResMed lines).
  - The build now fails if any holding would show a placeholder thesis. This fixes the root cause of WEC's missing thesis line in the audited draft.
- **Order-dependence, stated honestly:** 9 of the 20 names are chosen under every selection ordering tested, against 14 in v009. With 200 eligible names, the final tie-breaker decides more of the list. The 2007–09 replay ranges from −59% to −46% across orderings. The actual rule sits at the safer end (−46%); ranking by model score alone gives −59%.

## Honest odds (base-case market of 6% a year; no assumed stock-picking edge)

- **Over 5 years:** a 79% chance of a gain, a 50% chance of beating the S&P 500, and an 84% chance of a fall worse than 20% at some point along the way.
- **The owner's "10 points a year" goal:** beating the index by 10 points happens in about 20% of single years. Averaging it over 5 years has about a 3% chance.
- **Past crises, replayed with today's holdings:**

  | Crisis | This portfolio | S&P 500 |
  |---|---|---|
  | 2007–09 | −48% | −55% |
  | 2020 COVID crash | −37% | −34% |
  | 2022 | −15% | −24% |

  GDDY and VEEV (7% of the weight) had no share price in 2007–09, so that replay measures the other 93% of the portfolio.
- **Risk:** tracking error 11.8%, beta 0.59, about 19 independent bets.
- **Costs and tax:**
  - US dividend withholding costs about 0.53% of the portfolio a year (30% of a 1.8% snapshot yield).
  - US estate tax applies above about $60,000 of directly held US shares.

## Audit loops

| Loop | A1 / A2 / A3 | Note |
|---|---|---|
| 8 | 86 / 85 / 87 | Basis of v009 |
| 9 | 84 / 84 / 80 | Wave-6 build. The scores fell on the WEC placeholder thesis and the undisclosed ResMed episode; both are fixed in this release (audit/loop_fixes.json "9"). |

Final C1 number trace against this build's content: 320 checked, 319 matched; the one mismatch (a DA6 row count in Appendix A.4 that dropped a CONFIRMED fact) was fixed before release. Verification gate: PASS.

## Validation scope

- **Checks performed:** calculation consistency, data lineage, replication, and dossier facts against SEC filings (B1X, V1X, V2R, DA4–DA18, C1, X1, the risk re-computation, the daily-drawdown check).
- **Limits:** these checks cannot establish future earnings or a validated stock-selection edge.
- **Conditioning:** every probability is conditional on the stated scenarios and on zero alpha.
