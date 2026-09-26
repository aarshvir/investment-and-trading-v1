# Independent specialist 5 — implementation, tax and weekly operating policy

Reviewed 26 September 2026. Scope: original Claude handoff's implementation/tax claims and `review/WEEKLY_INVESTMENT_POLICY.md`; public IRS, statute, issuer and broker sources. This is a conditional research review, not a determination of the owner's tax status or authority to trade.

**Verdict: the revised weekly policy is substantially more implementable, but the original tax paragraph must be replaced and no personalized orders are justified before holdings, citizenship/tax status, available cash and exact broker contracts are confirmed.**

## 1. Tax claims: evidence and corrections

| Original claim or implied assumption | Finding | Required correction |
|---|---|---|
| UAE residence alone establishes US nonresident tax treatment | Incomplete | US citizenship and income-tax status are unknown. Estate-tax residence depends on domicile, which is a separate test. Dubai residence does not resolve either question. |
| US estate tax applies “above $60k” | Oversimplified | For a nonresident noncitizen estate, $60,000 is generally the filing threshold, incorporating specified gifts; liability depends on taxable estate, deductions, credit and treaties. |
| “Up to 40%” may be read as 40% on everything over $60k | Misleading if read that way | The rate schedule is graduated. 40% is the top marginal rate; do not calculate 40% × amount over $60k. |
| Irish index half “avoids US estate tax” | Conditional | Irish corporate fund shares generally avoid the domestic-corporation share situs rule for a qualifying nonresident noncitizen; direct US shares elsewhere remain relevant. This is no exemption for the entire portfolio or for a US citizen. |
| Irish ETF “cuts dividend withholding from 30% to 15%” | Correct direction, wrong level of explanation | 15% generally describes US-source portfolio dividends received by an eligible Irish fund; 30% is the usual direct US dividend rate for an eligible nonresident individual without treaty relief. These are different tax layers. |
| Accumulating ETF implies tax-free dividends | False if implied | The fund reinvests dividends after applicable fund-level taxes. Personal treatment still depends on the investor's actual status. |

IRS confirms that estate domicile matters and the filing test is at estate level. Therefore separate IBKR and Vested accounts do not each receive a separate $60,000 allowance; aggregate relevant ownership across accounts. Market value at death matters, so appreciation can cross a threshold. Sources: [IRS NRNC estate FAQ](https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes-for-nonresidents-not-citizens-of-the-united-states), [IRS estate tax overview](https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax-for-nonresidents-not-citizens-of-the-united-states).

The legal share-situs rule turns on domestic corporate issuance, not the exchange currency or broker's location. This supports the conditional Irish corporate-fund distinction; it does not eliminate US estate exposure on separately held US stocks. Source: [26 USC 2104(a)](https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title26-section2104).

Illustration only: a simplified $100,000 taxable US estate, with no gifts, no treaty relief and the full usual $13,000 credit, produces $23,800 tentative tax minus $13,000 = $10,800. This demonstrates why “40% above $60k” is wrong; it is not the owner's estimated liability. Sources: [Form 706 rate schedule](https://www.irs.gov/instructions/i706), [Form 706-NA credit and computation](https://www.irs.gov/instructions/i706na).

For nonresident individuals, US-source dividends are generally subject to 30% withholding unless a treaty or another exception applies. The IRS treaty list has no UAE income-tax treaty entry. That establishes no UAE treaty reduction by itself, but does not establish this investor's personal status. Sources: [IRS Publication 519](https://www.irs.gov/publications/p519), [IRS treaty list](https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z).

The US–Ireland treaty's Article 10 gives a 15% general portfolio dividend ceiling, subject to eligibility. BlackRock's institutional guide illustrates $100 US dividends becoming $85 within an Irish ETF; its public search extract was accessible, but the direct PDF redirected to an error page during this review. Treat the guide as supplementary, not as a verified statement of either fund's actual annual effective tax rate. Sources: [US–Ireland treaty, Article 10](https://www.irs.gov/pub/irs-trty/ireland.pdf), [BlackRock guide](https://www.blackrock.com/institutions/en-zz/literature/investor-guide/etf-guide-for-institutional-investors-2025.pdf).

**Suggested replacement:** “If you are neither a US citizen nor US-domiciled for estate-tax purposes, Irish corporate UCITS fund shares can reduce US-situs estate exposure compared with directly held US corporate shares. The $60,000 figure is generally an estate filing threshold, not a per-account allowance or a flat 40% tax rule. Eligible Irish funds generally incur 15% US withholding on portfolio dividends at fund level, while direct US dividends for a nonresident individual without treaty relief generally face 30%. Accumulation reinvests net income; it does not erase taxes. Confirm citizenship, tax residence, domicile and aggregate assets before choosing the account/product structure.”

## 2. Product identity verified, trading eligibility unverified

| Product | Verified identifier | Domicile / income | Published ongoing fee | Specific listing |
|---|---|---|---:|---|
| iShares Core S&P 500 UCITS ETF | IE00B5BMR087 | Ireland / accumulating | 0.07% TER | London Stock Exchange, CSPX, USD |
| Vanguard S&P 500 UCITS ETF (USD) Accumulating | IE00BFMXXD54 | Ireland / accumulating | 0.07% OCF/TER | London Stock Exchange, VUAA, USD |

Issuer pages retrieved 26 September 2026: iShares page displays key figures dated 24 September; Vanguard page mixes 24–25 September prices and 31 August portfolio data. Fees/identifiers are displayed product attributes, not guaranteed execution-date terms. Same share class can use another ticker or currency on another exchange. Sources: [iShares product page](https://www.ishares.com/uk/individual/en/products/253743/ishares-sp-500-b-ucits-etf-acc-fund), [Vanguard product page](https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-).

These are identity checks, not a recommendation to buy either product. IBKR supports eligible European fractional securities, but eligibility is instrument/account-specific. Do not assume CSPX or VUAA fractions, a particular exchange, or Vested availability. Check the exact ISIN, listing currency, contract, permissions, commission and lot-size treatment in the actual account. Round down where whole shares are required; retain residual cash. Source: [IBKR fractional-share guidance and eligibility list](https://www.interactivebrokers.com/campus/trading-lessons/fractional-shares/).

## 3. Weekly policy audit

The draft correctly distinguishes review frequency from thesis horizon, requires actual holdings for HOLD/REDUCE/SELL, blocks new purchases on material unknowns, counts fund overlap, and says no daily monitoring is active. It also treats 30% equity as a stress-budget ceiling rather than an optimized allocation. Retain these safeguards.

Recommended additions before implementation:

1. **Define the risk denominator.** The $50,000–$100,000 mandate is not automatically all investable wealth. Show both mandate-only exposure and aggregate exposure including the separate algorithmic trading activity. Confirm which capital the 15–20% tolerance covers. Do not declare full household suitability from this number.
2. **Do not convert a ceiling into an immediate rebalance.** Unknown existing holdings mean no instruction to sell down to 30% is warranted. Label the ceiling as a proposed starting design for this mandate; material existing exposures require reconciliation.
3. **Name the reserve instrument.** The 70% reserve assumption is currently unidentified. Cash, broker balances, deposits, money-market funds, Treasury bills and bond ETFs have different liquidity, duration, credit, custody and tax profiles. Do not give every reserve zero loss and the same assumed yield.
4. **Make the trade sheet mechanically reproducible.** Minimum fields: actual shares/cash and timestamp; current/target weight; dollar and share change; approved entry limit; exact contract; estimated spread/fees/FX; settlement or funding constraint; thesis trigger; order expiry; reviewer. Use a fresh quote before submission.
5. **Separate alert design from operating alerts.** The proposed daily drawdown thresholds cannot be enforced by a Sunday review. A weekly report must say whether daily portfolio data and alerts exist; until they do, report observed weekly drawdown and the monitoring gap explicitly. Stop orders are not gap-loss insurance.
6. **Specify no-data behavior.** A failed refresh freezes new discretionary purchases. Do not automatically liquidate holdings because a data provider failed; identify the missing evidence and escalate material thesis risks independently.
7. **Measure turnover explicitly.** Define the proposed 5% one-way threshold as 0.5 × (gross purchases + gross sales) / opening portfolio NAV, with contributions/withdrawals reported separately. Treat it as a review trigger, never a forced trading target.
8. **Use an exceptions-first weekly report.** With ~30 minutes available, lead with decisions and changes; append full evidence. A successful weekly run may legitimately conclude NO CHANGE. Record missed or incomplete runs rather than presenting stale analysis as refreshed.

## 4. Current action status

Candidate research and a paper/shadow portfolio are feasible now. Personalized buy sizes and HOLD/REDUCE/SELL instructions are not yet supportable from unknown holdings and cash. No order was submitted or broker account accessed in this review. The proposed reserve and loss thresholds are governance assumptions, not validated performance guarantees. A schedule alone does not make the methodology an operating daily risk system.

Not financial or individualized tax advice.
