# Replacement investment decision pack

Prepared26 September2026 Dubai. Start with the first four tabs of `../Investment_Review.html` or `Investment_Decision_Memo.pdf`.

## Current decisions

- AMP: new-money candidate at or below$500, up to2% of capital.
- PAYX: new-money candidate at or below$101.80, up to2%.
- Funded conditional slots: MSFT≤500, NVDA≤215, ALLE≤145, HIG≤120. Price and unchanged fundamentals must both qualify.
- Other candidates have explicit lower entry/reconsideration prices but no additional funded allocation.
- Initial model19% equity/81% reserve; maximum25% equity/75% reserve. Tail stress18% is not a guaranteed maximum loss.

## Files

`INVESTMENT_DECISION_MEMO.md` and `Investment_Decision_Memo.pdf` give the decisions, assumptions,14 company scenarios, new-money portfolios and risk tradeoff. `Investment_Decision_Model.xlsx` contains inputs, formulas and cached results. `decision_model.json`, `decision_table.csv` and `scenarios.csv` contain the numerical record. `WEEKLY_POLICY_V2.md` defines the Sunday research process, including buy, hold, reduce and sell criteria.

The five company reports—technology, quality_compounders, financials, airbnb and industrials_payments—contain source definitions, normalization bridges and operating assumptions. Their JSON files preserve detailed drivers. The final consolidated model governs any later entry-price refinements; historical intermediate audit files retain earlier alternatives.

`final_challenge_financials.md` and `consolidated_financials_audit.json` document the final1,422 numerical checks. `quality_portfolio_challenge.md` explains why the equity ceiling fell from30% to25%. `cross_review_industrials_payments.md` checks three additional company models. `funds_cross_review.md` verifies fund identity, currency, fees and published portfolio statistics. Raw source snapshots and hashes are in the accompanying folders.

The prior25 dashboard tabs remain available as an audit archive. Current replacement decisions occupy the first four tabs, bringing the total to29. Original deep audits remain under `../deep_audit`; original research was not overwritten. No profit probability, strategy track record, guaranteed drawdown floor or live broker quote is certified.

## Reproduction

Run the company model builders only when deliberately refreshing their inputs. For consolidation, run `build_decision_pack.py`, then `publish_decision_pack.py`, `build_pdf.py`, `publish_dashboard.py`, and `audit_consolidated_financials.py`. The last dashboard publisher incorporates the prior builder and then adds the current views; running only `../build_dashboard.py` would restore the audit-only front page. Preserve dated versions before a weekly revision.

Weekly refresh is active for Sunday18:00 Dubai. It performs research, not intraday monitoring or order submission. Unknown personal holdings and tax status are not assumed. Before execution, verify live price, eligibility, costs, business developments and portfolio capacity. No trades or paid data purchases have been made.
