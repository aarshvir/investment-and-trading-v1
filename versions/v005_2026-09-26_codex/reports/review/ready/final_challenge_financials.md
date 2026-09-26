# Final independent challenge — consolidated decisions and workbook

**The rebuilt consolidated model passes the numerical review with no remaining arithmetic or modeled-cost exceptions. The review's actionable finding was accepted: PAYX's entry limit is now $101.80, preserving the 12% hurdle under both 30% dividend withholding and the stated 25bp entry/exit cost stress.** The $101.59 reference price still qualifies.

Reviewed `decision_model.json` and `Investment_Decision_Model.xlsx`. Exact SHA-256 hashes and calculation receipts are in `consolidated_financials_audit.json`. There were **1,422 independent numerical checks, zero failures**, **758 formulas with present cached values**, and **zero Excel error cells**. This validates arithmetic and internal consistency, not the truth of future assumptions.

## Findings that pass

- All 42 company scenarios reconcile terminal EPS × multiple, dividend cash flows, gross/withheld IRRs at reference and limit prices, hurdle present values, and total returns. All published limits are below the base-case present value after 30% dividend withholding, before dealing costs.
- The intended portfolio is **15% index + 10% direct shares + 75% reserve = 100%**, or 25% equity. Initial eligible purchases are **15% index + 4% direct shares + 81% reserve**, or 19% equity. Unfilled conditional positions remain in reserve.
- Maximum direct company weight is 2%. Direct financials AMP plus HIG total 3%, below the 5% direct-sector limit. Index financials are additional economic exposure; that distinction must remain visible.
- With the stated 31 August issuer index weights, full look-through NVIDIA is **2.711853%** and Microsoft **2.8540025%**, both below the 3.5% planning cap. These calculations are not a certification of future ETF weights; rebalance checks must use refreshed holdings.
- The $50,000 and $100,000 initial share illustrations each sum exactly to capital. Rounding produces equity weights of **18.73257% and 18.83437%** respectively, slightly below the 19% idealized model. NAV-based ETF quantities are correctly identified as illustrations, not executable orders. Costs are paid from residual cash.
- Microsoft uses the explicitly dated $516.05 September 25 reference in both the JSON and workbook. The $500 entry remains conditional. Other references retain their disclosed dates rather than pretending all quotes share one timestamp.
- Each portfolio terminal scenario independently reconstructs as index/reserve annual compounding plus direct-stock terminal prices and dividends after 30% withholding, divided by limit-price entries. Stock dividends are not reinvested in that calculation. Portfolio wealth CAGR is therefore correctly distinct from cash-flow IRR.
- Full stress losses reconcile to **8.50%, 14.25%, and 18.00%**; initial losses reconcile to **6.10%, 10.71%, and 13.62%**. The tail combines index -60%, direct shares -75%, reserve -2% simultaneously. No annual reserve yield cancels an instantaneous loss.

## Required interpretation and refinements

**PAYX dealing costs — resolved:** after-tax base PV is $102.3359637 before dealing costs. Applying 25bp to entry cash and 25bp to the terminal sale proceeds gives an executable-price ceiling of **$101.8464601**. The revised $101.80 limit preserves the 12% hurdle under that particular stress, before any additional fixed fees. The previous $102 limit was tax-robust but not fully cost-robust. Every published stock limit now passes the same proportional-cost test.

**Workbook labels — resolved:** editable inputs now correctly read C:K, including the third-year dividend. The stress label now reads “Tail shock,” removing the outdated “beyond tolerance” wording when the revised full result is -18%, within the upper end of the user's stated 15–20% band.

**No protection guarantee:** lowering equity to 25% improves the stress fit. It does not create a contractual 20% loss floor. An extreme equity loss or reserve impairment can exceed modeled shocks; stop orders, if used, cannot ensure prices during gaps. The portfolio's three-year base wealth CAGR is a conditional scenario, not a calibrated expected return or promised outcome.

**Full allocation is a conditional comparison:** it assumes all six funded stock slots were bought at their specified limits at the start of the modeled period. In practice they may fill later or never. The published full-case return must not be described as the outcome of today's executable holdings. The initial case is the closer representation, still subject to live prices, access and thesis checks.

**Decision constraints remain active:** the stock limits do not authorize purchases merely because prices fall. Recheck earning power, event developments, capital/remittance constraints, individual exposure and ETF overlap. No requirement to invest forces AIZ, IBKR or any other reserve candidate into a funded slot.

The earlier `cross_review_financials_portfolio.md` analyzed a preliminary 20% index specification. This final challenge supersedes that allocation discussion; do not combine its older stress numbers with the final 15% index portfolio.
