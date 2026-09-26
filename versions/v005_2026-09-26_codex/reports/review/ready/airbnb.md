# Airbnb underwriting — 26 September 2026

**Avoid a new purchase around $151–$157; buy at $120 or below if the operating thesis remains intact.** This is a valuation decision, not an unresolved-data label. At $120 the base case produces a 13.82% three-year annualized return; at the corroborated September 24 close of $151.39 it produces only 5.33%. The September 25 page disagrees internally ($157.47 header, $157.25 table), but either value strengthens the same conclusion. [Dated price observations](https://stockanalysis.com/stocks/abnb/history/).

For a small existing holding, review for HOLD rather than sell solely because it is above the new-buy price. A large position merits a reduction decision based on competing returns, taxes and overall risk; the user’s holdings remain unknown. Proposed initial position at the limit: 1% of total capital; maximum 1.5%, including portfolio review. No order should remain unattended through a material new disclosure.

## Actual economics and accounting baseline

The FY2025 10-K gives $12.241bn revenue, $2.544bn operating income, $2.511bn net income and 623m diluted weighted-average shares. FY2024 revenue was $11.102bn and operating income $2.553bn: revenue grew while operating profit stalled. FY2025 cash-flow SBC was $1.592bn, making an adjusted EBITDA or FCF multiple particularly easy to overstate. The full 10-K and latest shareholder letter are archived with hashes under `raw_airbnb`. [FY2025 10-K, statements pp50–53](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm).

The Q2 2026 filing reports revenue $3.608bn, operating income $758m, net income $816m, SBC $487m and 597m diluted shares. The low quarterly tax expense includes a $77m prior-year benefit; the reported $1.37 EPS should not be capitalized as a normal quarterly run rate. Using operating profit plus interest income less interest expense and an ordinary 22% tax rate yields about $1.18 per share for that quarter. This is an analyst normalization, not reported EPS, and the seasonal quarter is not annualized. [Q2 10-Q, income statement and tax note](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000027/abnb-20260630.htm).

The business has real momentum: management raised FY2026 revenue growth to at least the mid-teens and adjusted EBITDA margin to at least 35.5%, and guided Q3 revenue to $4.69–$4.77bn. Q2 nights/seats rose 10%; pricing/mix contributed to faster revenue. Our $14.2bn FY2026 base is 16.0% above FY2025 and is consistent with that direction. We do not assume a 35.5% *GAAP operating* margin: SBC and other adjustments explain why those are different measures. [Q2 shareholder letter, outlook pp7 and financial results pp13–15](https://www.sec.gov/Archives/edgar/data/1559720/000119312526337928/d70413dex991.htm).

## Independent scenarios

Valuation = (revenue × operating margin + recurring net interest) × (1 − tax) ÷ diluted shares × P/E. All future inputs are analyst assumptions. Operating margins retain SBC and depreciation; the share reduction reflects net repurchases after dilution. No buyback yield or net-cash premium is added. Interest is included explicitly, so no separate capitalization of the same cash balance is added. Guest funds are excluded from discretionary corporate cash.

| Scenario | FY2026 revenue | FY2027 / 2028 / 2029 growth | FY2029 revenue | Operating margin | Net interest / tax / diluted shares | EPS / P/E | Sep2029 terminal price | 3-year return at $151.39 / $120 |
|---|---:|---|---:|---:|---|---|---:|---|
| Bear | $13.95bn | −5% / 3% / 5% | $14.33bn | 17% | $0.20bn / 24% / 610m | $3.28 / 20x | $65.70 | −24.29% / −18.19% |
| Base | $14.20bn | 12% / 10% / 8% | $18.89bn | 26% | $0.35bn / 22% / 580m | $7.08 / 25x | $176.93 | 5.33% / 13.82% |
| Bull | $14.60bn | 18% / 15% / 12% | $22.19bn | 30% | $0.45bn / 20% / 560m | $10.15 / 30x | $304.58 | 26.24% / 36.41% |

FY2029 ends December 2029, three months after the assumed September 2029 exit. The terminal multiple therefore uses current-fiscal-year forecast earnings, not trailing earnings. All three dividends are zero in each case. Consequently cash-flow IRR and terminal-price CAGR coincide here. No scenario probability is claimed.

The base margin assumes five percentage points of operating leverage from FY2025, supported by scale, pricing, customer-service efficiency and slower expense growth. That is already favorable: it is the principal sensitivity, not a free certainty. The bull requires sustained category expansion and new-product monetization; the bear combines a consumer downturn, slower bookings and a less efficient cost base. The 25x base P/E grants a meaningful premium for the brand/network while requiring better earnings quality than an SBC-excluding comparison.

At a 13% return hurdle, the exact purchase ceiling is **$122.62**; the chosen $120 limit leaves another 2.1% discount. Conditional bear/base/bull present values are $45.53/$122.62/$211.09. This wide range is a scenario map, not a statistically estimated confidence interval. If the base margin is only 23% rather than 26%, EPS and value decline materially; the next refresh must change the entry price rather than preserve an attractive-looking old target.

## Cash, dilution and what changes the decision

The corrected company TTM FCF is $4.827bn. It is not automatically owner earnings: SBC remains a recurring cost, cash taxes differ from book taxes and Airbnb collects its own service fees before stays. Customer funds held for others are a matching fiduciary balance, not an extra distributable asset. Conversely, subtracting all customer money from FCF would also be wrong. Reserve Now, Pay Later can change the timing of the company's advance fee cash; therefore compare trailing periods and fee liabilities, not one quarter. The model avoids these distortions by starting with operating earnings and keeping SBC as an expense. [Q2 shareholder letter, FCF chart and cash balance discussion](https://www.sec.gov/Archives/edgar/data/1559720/000119312526337928/d70413dex991.htm); [Q2 filing, FCF reconciliation](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000027/abnb-20260630.htm).

Reassess or cancel the limit if nights/seats growth falls below 5% for two quarters, marketing and product costs prevent operating margin improvement, SBC stays above 15% of revenue while shares stop declining, or regulation materially restricts supply in important markets. Material guest/host trust failures and cancellation/credit problems also change the thesis. A falling share price alone does not prove the limit became attractive. Catalysts are sustained nights growth, international repeat usage, evidence of actual profit from new services/hotels and cash conversion after payment-product changes. Do not capitalize management's claims about AI savings without observing total costs and margins.

The completed recommendation is therefore **price discipline, with a defined entry and exit-review framework**, rather than a momentum purchase after a pullback. `airbnb.json` and `build_airbnb.py` retain the assumptions and reproduce the arithmetic.
