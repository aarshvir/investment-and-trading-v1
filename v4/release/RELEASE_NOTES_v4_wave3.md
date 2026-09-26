# Claude v4, wave 3: 178 companies researched in full; a revised 20-stock all-stock portfolio

Author: Claude. Status: completed research publication. No trades placed. This is research, not personalised investment, tax or legal advice; the author is not a licensed adviser.

**Data cutoff:** prices and the live snapshot are at the US close of 25 September 2026. SEC filings are those available to 25 September 2026; each dossier states its latest reported period. Prepared 26 September 2026 (Dubai). Portfolio build 2026-09-26T19:16:27 (content fingerprint 9bc2eb705a37). Verification gate: PASS.

**Parents:**
- **v006_2026-09-26_claude:** the previous Claude release, which this release updates.
- **v005_2026-09-26_codex:** the latest Codex release, reconciled in FINAL_REPORT §13.
- **claude-v3**, **codex-initial-audit** and **codex-deep-data-audit:** the earlier history.

## Relationship to earlier publications

This release **updates v006**. It replaces v006's 20-stock list with a list re-selected after 45 more companies were researched in full.

It **supplements and partly challenges v005; it does not supersede it.**
- v005 remains Codex's defensive 15/10/75 recommendation.
- This release answers the owner's all-stock brief.
- The owner chooses between them.

## What changed since v006, and why

### More research
Wave 3 researched 45 more companies in full from SEC filings, in the same pre-committed order.
- Companies researched in full: 178 (was 133).
- Companies passing every test: 116 (was 86).
- Triage-passed companies still queued: 147.

### The portfolio

| | Holdings |
|---|---|
| **Full conviction (16, 89% of the portfolio)** | HST 7.0%, DOV 6.7%, DRI 6.4%, ADP 6.4%, MA 6.2%, CAH 6.0%, BR 6.0%, CRH 5.5%, COR 5.5%, GM 5.1%, LVS 5.0%, PGR 4.9%, AXP 4.9%, HBAN 4.8%, VEEV 4.3%, MSCI 4.2% |
| **Half conviction (4)** | CVS 3.0%, CMCSA 2.9%, DG 2.6%, BKNG 2.6% |
| **Added** | Mastercard, American Express, MSCI, Cardinal Health, Cencora, Veeva: all full conviction from wave 3 |
| **Removed** | M&T Bank, Raymond James and Ameriprise (still eligible and full conviction, but outside the five-per-sector limit for Financials); UDR, DaVita and Synchrony (half conviction, outranked) |

AMP, a v005 first purchase, is therefore now eligible but not held, like PAYX. §13 records this.

### Two new rules
Both rules were committed (sha256, time, reason) before any build used them.
- **(k) V1 input-defect guard.** Wave-3 diligence found that the valuation model had read Comfort Systems' revenue 2.8 times too low, from a mis-dated figure in the company's own SEC data feed. A scan of all 92 modelled names found no other case. Any model verdict built on a revenue figure that disagrees with an independent source by more than 1.6 times is now discarded, and the name is judged on its full diligence.
- **(l) At most five names per sector.** The 25% sector cap is applied after selection, so many names in one sector would squeeze full-conviction holdings below half-conviction weights. Disclosure: this rule was written after the wave-3 verdicts showed several new full-conviction Financials, and before any build or weight was computed with them.

### Rule (j) sensitivity (now re-run on every build)
Four alternative selection orders were tested. 12 names are chosen under every one of them, and the 2007–09 replay stays in a narrow range. The near-miss list gives every bench name's position and the reason it missed.

### Verification
- **Independent fact-checks:** every holding has an independent multi-fact check of its dossier against SEC filings. DA9 and DA10 covered the six new names (42 facts: 1 fail, 1 minor, both corrected). Operative sentences that were wrong now carry inline "[Corrected …]" markers, and the original wording is kept.
- **Mechanical pre-check (new):** `code/lead_dossier_precheck.py` now runs before fact-checks. It flags missing summary fields, balance-sheet figures without an entity scope, mislabelled year-over-year periods and filings cited without an accession number. It found an MSCI period mislabel, since clarified.
- **XOM identifier reconciled:** ExxonMobil Holdings Corp is a co-registrant after an August 2026 reorganisation. XOM is not held.
- **Final number trace:** the verification gate passed, and C1 traced all 282 report numbers against this exact build, 0 mismatches.

## Honest odds (base-case market of 6% a year; no assumed stock-picking edge)

- **Next 5 years:** 76% chance of a gain, 49% chance of beating the S&P 500, 91% chance of a fall worse than 20% at some point.
- **The owner's "10 points a year" goal:** a single year 10 points ahead of the index happens about 19% of the time; averaging that over 5 years has about a 2% chance.
- **Past crises, replayed at today's weights:**
  - 2007–09: −56%, against −55% for the S&P 500. DG, VEEV, GM and MSCI had no share price for all or part of that window, so the replay covers 87% of the weight; the old GM went bankrupt in 2009.
  - COVID crash: −37%.
  - 2022: −16%, against −24%.
- **Risk profile:** tracking error 11.2%, beta 0.67, and about 17 effective independent bets.
- **Cost of holding US shares directly:** withholding takes about 0.5% of the portfolio a year (30% of a 1.7% dividend yield), and US estate tax applies above about $60,000 of directly held US shares.

## Audit loops

| Loop | Scores (A1 quant / A2 investment committee / A3 client) | Main change |
|---|---|---|
| 5 | 82 / 81 / 86 | Basis of v006 |
| 6 | 84 / 82 / 87 | Wave-3 build; all Loop-6 fixes applied before this release (audit/loop_fixes.json "6") |

## Validation scope

- **What the checks establish:** calculation consistency, data lineage, replication and dossier facts against SEC filings. The evidence is B1X, V1X, V2R, DA4–DA10, C1, X1, the risk re-computation and the daily-drawdown check.
- **What they cannot establish:** the truth of future earnings, or a validated stock-selection edge. No rule tested beat the S&P 500 on point-in-time data for 2012–2026.
- **Conditioning:** every probability is conditional on the stated market scenarios and on zero alpha.

## Where to start in the package

- `v4/FINAL_REPORT.md`.
- `v4/dashboard/equity_audit_v4.html`.
- `v4/HANDOFF_v4.md`.
- `python v4/run_all.py`.
