# Claude v4: an all-stock US portfolio chosen from the whole S&P 500, independently audited, reconciled with Codex v005

Author: Claude. Status: completed research publication. No trades placed. This is research, not personalised investment, tax or legal advice; the author is not a licensed adviser.

**Data cutoff:** prices and the live snapshot are at the US close of 25 September 2026. SEC filings are those available to 25 September 2026; each dossier states its latest reported period. Prepared 26 September 2026 (Dubai). Portfolio build 2026-09-26T18:08:34 (content fingerprint ee5f7079efdf; holdings and weights identical to every build since 17:17). Verification gate: PASS (all 20 holdings independently fact-checked; C1 traced 361 numbers, 0 mismatches).

**Parents:**
- **v005_2026-09-26_codex:** the latest completed Codex release, reconciled in FINAL_REPORT §13.
- **claude-v3:** the original handoff and bundle this work audits and replaces.
- **codex-initial-audit** and **codex-deep-data-audit:** earlier Codex reviews whose v3 findings were re-verified.

An earlier, never-published draft of these notes (`v4/release/RELEASE_NOTES_draft.md`) described the previous index-core answer. It is kept for the record and is superseded by this file.

## Relationship to earlier publications

**This release supplements and partly challenges v005; it does not supersede it.**
- v005 remains Codex's recommendation: a defensive 15/10/75 equity budget.
- This release answers a different brief that the owner set later: an all-stock portfolio of 5–20 US companies, with no index fund or T-bills for now.
- The owner decides between the two. §1 and §7 of the report show both the all-stock answer and the lower-risk allocation view, on the same simulation engine.

This release **replaces claude-v3** as Claude's view, because v3's central claims failed re-verification (FINAL_REPORT §2).

## What this release contains

### The answer: 20 US stocks chosen from the whole S&P 500

- **Full conviction (13, 77% of the portfolio):** HST 7.8%, DOV 7.4%, DRI 7.2%, ADP 7.1%, BR 6.7%, CRH 6.2%, GM 5.8%, MTB 5.8%, LVS 5.7%, RJF 4.7%, AMP 4.5%, PGR 4.3%, HBAN 4.2%.
- **Half conviction (7):** UDR 5.0%, CVS 3.6%, CMCSA 3.5%, DG 3.1%, BKNG 3.1%, DVA 2.8%, SYF 1.5%.
- **Constraints:** inverse-volatility weights, at most 10% per name (5% at half conviction), 25% per sector (Financials sits exactly at the cap) and 12% per sub-industry. Every cap is verified after rounding, and the weights sum to 100.0%.

### How the 20 were chosen

1. Every company without a dossier had a quick triage pass (455 names), and 40 earlier dossiers were carried forward.
2. 133 companies then had full diligence from SEC filings. This covers the strongest triage names in two waves of 45 each, plus the eight largest AI and cloud companies.
3. 86 companies pass every test: an INCLUDE or INCLUDE-SMALL verdict, and a price that implies growth at or below the analyst's evidence-based base case. Names in the model's top 70 must also pass the systematic valuation.
4. Rule (j) picks the best 20 of the 86: conviction first, then margin of safety, then base-case return, with at most two names per sub-industry.

**Deliberately excluded:** Microsoft, NVIDIA, Alphabet, Amazon, Meta and Apple. They are great businesses whose prices already assume more growth than the evidence supports.

**Still to do:** 189 triage-passed companies await full research. A later wave may displace some holdings.

### Honest odds (base-case market of 6% a year; no assumed stock-picking edge)

- **Next 5 years:** 75% chance of a gain, 49% chance of beating the S&P 500, and 93% chance of a fall worse than 20% at some point.
- **Crisis replays at today's weights:**
  - 2007–09: −60%, against −55% for the S&P 500. DG, SYF and GM had no share price then (10% of weight). The old GM went bankrupt in 2009, so the real loss would likely have been worse.
  - 2020 COVID crash: −41% (S&P −34%).
  - 2022: −17% (S&P −24%).
- **The owner's "10 points a year" goal cannot be promised.** With the portfolio's 11.6% tracking error and no edge, a single year 10 points ahead happens about 19% of the time. Averaging 10 points ahead over 5 years has about a 3% chance.

### Implementation for a UAE resident

- **Estate tax:** above about $60,000 of directly held US shares, a non-US person's estate can owe US estate tax. At $100,000 all in stock the owner would be above that threshold.
- **Withholding:** 30% of every US dividend is withheld, costing about 0.66% of the portfolio a year.
- **Practical guides:** a per-$10,000 table (all-stock row first), IBKR order steps and a weekly 30-minute review.

## Findings adopted, confirmed, changed, rejected or unresolved

FINAL_REPORT §13 has the full table with evidence. In short:

- **Confirmed:**
  - A hard 15–20% loss limit needs a small equity share: v4's 2007–09 daily replay agrees with v005's shock test.
  - Withholding and estate-tax facts.
  - RL, AIZ and NTAP are not buys at current prices.
- **Confirmed since the last draft:**
  - AMP (v005's first purchase) passes v4's own full diligence and is held at full conviction.
  - PAYX (v005's other first purchase) was researched in full in wave 2. It passes every v4 test (half conviction; its price implies about 0.7% a year of cash-flow growth) but is not held, because 20 names outranked it.
- **Adopted:** the Irish UCITS vehicles and v005's drawdown triggers for the lower-risk allocation view.
- **Challenged:**
  - v005 ranks only v3's fourteen candidates. v4 screens the whole index, and v3's candidate evidence was biased on point-in-time data.
  - v005 recommends a defensive equity budget; this release answers the owner's later all-stock brief.
- **Unresolved:** whether the owner's 15–20% loss limit must hold in every crash. That is the owner's decision.
- **No longer applicable:** HIG, which the earlier draft held, is no longer in the portfolio.

## Changes during this release's audit loops

Audit scores (A1 quant, A2 investment committee, A3 client and compliance):

| Loop | Scores | What changed |
|---|---|---|
| 0 → 1 | 41/42/45 → 85/76/80 | v3 rebuilt on point-in-time data; the stock-scoring model was found to have no edge |
| 2 | 88/89/80 | Rule amendments (a)–(f); REIT valuations rebuilt on FFO; quarterly-rebalanced crisis replays; DA4 and C1 checks |
| 3 | 78/78/76 | Owner switched to all-stock; whole-index triage; wave-1 diligence; rules (g)–(j) |
| 4 | 79/76/84 | Verdict re-centred on the all-stock answer; wave-2 diligence |
| 5 | 82/81/86 | Loop-4 fixes verified; Loop-5 fixes listed below |

**Loop-4 fixes:**
- **Fact-checks:** DA6 and DA7 checked 11 holdings (55 facts). All 7 failures are corrected in the dossiers, with originals kept, and no verdict changed. The GM net-cash figure is +$3.7bn, not +$8.7bn. RJF's bank-capital exit trigger was restated on the correct basis: 16.4% against 15%.
- **Rule (j) sensitivity:** tested under four alternative orderings. They keep 15–20 of the same 20 names, 12 are chosen every time, and the 2007–09 replay ranges from −54% to −62%.
- **Rule-change firewall:** the build now refuses to run on selection rules that have not been committed (sha256, time and reason in `outputs/rule_commitments.jsonl`). Rule (j) is disclosed as written after the wave-1 verdicts were known.
- **Number tracing:** C1 was re-run on the current build. 350 numbers were traced and 349 matched; the one dashboard mismatch is fixed.

**Loop-5 fixes:**
- **Every holding independently fact-checked:** DA8 covered AMP, ADP, CRH, PGR and DOV (33 facts: 1 fail, 4 minor, all corrected in the dossiers; PGR and DOV exact). All 20 holdings now have an independent multi-fact check of their dossier against SEC filings (DA4–DA8).
- **Verification gate:** `code/lead_verify_gate.py` blocks packaging unless every holding has a DA-series check, every FAIL is answered by a dated correction in its dossier, and the final C1 number-tracing audit names the current build's content fingerprint (`content_sha256`, logged in `outputs/build_history.jsonl`). This release passed the gate.
- **Dashboard:** the audit-history table misread one Loop-2 score (fixed), and the estate-tax and withholding table now also appears on the Implementation tab.
- **Next research wave:** the wave-3 prompt adds an entity-scope rule (consolidated vs segment vs subsidiary figures), the most common error the fact-checks found.

## Validation scope

- **What the checks establish:** calculation consistency, data lineage, replication and dossier facts against SEC filings. The evidence is B1X, V1X, V2R, DA4–DA8, C1, X1, `lead_check_risk_contrib` and `lead_check_daily_dd`.
- **What they cannot establish:** the truth of future earnings, or a validated stock-selection edge. No rule tested beat the S&P 500 on point-in-time data for 2012–2026.
- **Conditioning:** every probability is conditional on the stated market scenarios and zero alpha.
- **Known limitations:** FINAL_REPORT §11 and HANDOFF_v4.md.

## Where to start in the package

- `v4/FINAL_REPORT.md`, with a readable copy in `reports/v4/outputs/release_copies/`.
- `v4/dashboard/equity_audit_v4.html`: open it locally; the v4 tabs come first.
- `v4/HANDOFF_v4.md`: how to continue and reproduce.
- `python v4/run_all.py`: re-derives every published number.
