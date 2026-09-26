# Claude v4: point-in-time rebuild, independently audited, reconciled with Codex v005

Author: Claude. Status: completed research publication. No trades placed; not personalised investment, tax or legal advice (the author is not a licensed adviser).

Data cutoff: US close of 25 September 2026 for prices and the live snapshot. SEC filings as available to 25 September 2026; each dossier states its latest reported period. Prepared 26 September 2026 (Dubai).

Parents:
- **v005_2026-09-26_codex:** the latest completed Codex release, reconciled in FINAL_REPORT §13;
- **claude-v3:** the original handoff and bundle this work audits and replaces;
- **codex-initial-audit** and **codex-deep-data-audit:** earlier Codex reviews whose v3 findings were re-verified.

## Relationship to earlier publications

This release **supplements and partly challenges v005; it does not supersede it.** Nothing here silently replaces v005's investment policy; the owner decides between them. It **replaces claude-v3** as Claude's view, because v3's central claims failed re-verification (FINAL_REPORT §2, `v4/outputs/lead_v3_audit.md`).

## What this release contains

- **The answer.** Build the portfolio in three layers: an S&P 500 index core in an Irish UCITS fund; a T-bill reserve sized to the loss the owner can tolerate; a bounded satellite of diligence-verified US stocks at no more than 15–20% of the total. The high-confidence decision is the allocation. No stock-picking rule tested beat the S&P 500 on point-in-time data from 2012 to 2026, including v1, v2, v3 and a pre-registered v4 model; a second agent replicated this blind.
- **Five allocation mixes on one simulation engine** (base case 6% a year; bear 2%, bull 9%), with daily crisis replays and the equity share that would have kept each crisis within −20% or −15%. The Defensive 15/10/75 mix is v005's equity budget.
- **A 20-stock satellite.** It is selected by pre-registered rules applied to all 503 point-in-time members, plus primary-source dossiers, V1 valuation and an analyst valuation check. Weights are inverse-volatility and every cap is verified after solving. Every holding has a one-line thesis and 3–5 measurable exit triggers.
- **Implementation for a UAE resident:** estate tax, withholding, UCITS, IBKR entity and costs (re-verified by R3); a weekly 30-minute review; a per-$10,000 conversion table; a glossary.

## Findings adopted, confirmed, changed, rejected or unresolved

See FINAL_REPORT §13 for the full table with evidence. In short:
- **Confirmed independently:** a hard 15–20% limit needs a small equity share. v005 reached 25% equity through a hypothetical shock test; v4's daily replay of 2007–09 gives ≤34% for −20% and ≤27% for −15%.
- **Adopted:**
  - Irish UCITS core, with IB01 or directly held T-bills as the reserve;
  - v005's tighter drawdown triggers for the Defensive mix.
- **Confirmed:**
  - withholding and estate-tax facts;
  - RL, AIZ and NTAP are not buys at current prices.
- **Challenged:** v005 ranks only v3's fourteen candidates. v3's candidate evidence was biased (its momentum result falls from 29.1% to 18.1%/yr on point-in-time data), and v4 screens the whole index. The only overlap is HIG.
- **Unresolved:**
  - AMP and PAYX. v4 never diligenced them because they rank outside its pre-registered universe. X1 reproduced v005's base cases from SEC filings; the AMP gap is a method difference.
  - Whether the owner's 15–20% limit must hold in every crash. That is the owner's decision.
- **Disagree (timing):** v005 would buy HIG only at ≤ $120; v4 holds it at half weight at $124.
- **Verification of v005 (agent X1):** 23 of 26 claims confirmed, 1 minor difference, 1 not confirmed, 1 unverifiable. The one not confirmed is PAYX's 20x exit multiple, which sits below its own 10-year range: conservative, but not disclosed.

## Changes during this release's audit loops (decision effects)

- **Loop 0 → 1:** v3 rebuilt on point-in-time data; the model found to have no edge; strategy changed to index core + reserve + zero-alpha satellite.
- **Loop 1 → 2** (every must-fix implemented; `v4/audit/loop_fixes.json`):
  - rule amendments a–f, each removing an inconsistency and none chasing returns (see the header of `v4/code/lead_build_portfolio.py`);
  - RL, MPC, HAS and JBHT removed;
  - diligence extended to all 11 names that passed every quantitative gate;
  - REIT valuations rebuilt on filed FFO, which moved HST and FRT from "attractive" to "fair" and FRT to half conviction;
  - crisis replays corrected to quarterly rebalancing;
  - an independent daily-drawdown check;
  - the V1 valuation re-derived from SEC filings (V1X: 86.5% of checks pass, no verdict changes);
  - 53 dossier facts checked against SEC filings (DA4: 0 fails);
  - 216 report numbers traced to source (C1: 1 fixed);
  - run_all.py, pinned requirements and seeds;
  - the Defensive mix added;
  - reconciliation with v005.
- **Loop 2 scores:** {LOOP2_SCORES}

## Validation scope

- **What the checks establish:** calculation consistency, data lineage and replication. Independent agents re-derived:
  - the backtest (B1X);
  - the drawdowns;
  - the valuations (V1X, V2R);
  - dossier facts (DA4);
  - report numbers (C1);
  - v005's claims (X1).
- **What they cannot establish:** the truth of future earnings, or a validated stock-selection edge.
- **Every probability** is conditional on the stated market scenarios and zero alpha.
- **Known limitations** are in FINAL_REPORT §11 and HANDOFF_v4.md §6.

## Where to start in the package

- `v4/FINAL_REPORT.md`, with a readable copy in `reports/v4/outputs/release_copies/`;
- `v4/dashboard/equity_audit_v4.html`: open locally; the v4 tabs come first;
- `v4/HANDOFF_v4.md`: how to continue and reproduce;
- `python v4/run_all.py`: re-derives every published number.
