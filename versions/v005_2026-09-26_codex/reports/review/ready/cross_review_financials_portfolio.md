# Independent portfolio arithmetic check — preliminary specification

Reviewed root's proposed specification on 26 September 2026 before the consolidated decision-model file was available. The final-file audit remains to be appended after that file exists.

Full intended allocation: 20% VUAA; AMP 2%, PAYX 2%, MSFT 2%, NVDA 1.5%, ALLE 1.5%, HIG 1%; 70% reserve. Direct stocks sum to 10%, total equities 30%, reserve 70%, portfolio 100%. Initial eligible AMP/PAYX plus VUAA sum to 24% equities and 76% reserve, assuming both meet their entry limits. Unfilled stock allocations must remain in reserve, not be redistributed automatically.

Direct financial stocks AMP+HIG total 3% when both are filled, below a 5% direct-sector cap. Initially AMP is 2%. VUAA's financial-company holdings are additional economic exposure and must be disclosed. The same look-through issue applies to MSFT and NVDA: their direct weights are not the total company exposure. Maximum direct stock weight is 2%; a cap on total company exposure requires the ETF holdings, not merely this direct list.

Financial allocation is consistent with the valuation decisions only if AMP is at or below $500 and HIG is at or below $120. HIG is not an initial purchase at the reference $125.69. AIZ/IBKR do not need to be included to satisfy the requirement to make a decision; their lower entry thresholds are explicit decisions, and the portfolio has other eligible opportunities.

The following are arithmetic stress illustrations, not estimated probabilities, historical backtests or maximum losses. Reserve return is an immediate marked-value assumption; no annual interest is used to cancel an instantaneous equity shock.

| Simultaneous shock | Full 30% equity / 70% reserve | Initial 24% equity / 76% reserve |
|---|---:|---:|
| Index -40%, direct shares -50%, reserve unchanged | -13.00% | -10.00% |
| Index -55%, direct shares -65%, reserve unchanged | -17.50% | -13.60% |
| Index -55%, direct shares -65%, reserve -1% | -18.20% | -14.36% |
| All equity goes to zero, reserve unchanged | -30.00% | -24.00% |

Thus the cash-heavy construction plausibly reduces exposure to a 15–20% temporary-loss tolerance, but it cannot guarantee that limit. The final report should retain that distinction. A reserve fund can also have market, liquidity, custody and currency risks; it is not identical to insured cash.

Valuation-model check completed separately: all 12 financial-stock scenario IRRs reproduce their reference prices to less than $0.0000001; EPS is grown exactly three annual periods; all four practical price limits are below their respective maximum entry under 30% dividend-withholding sensitivity. No probability-weighted expected return or standalone buyback yield was added.
