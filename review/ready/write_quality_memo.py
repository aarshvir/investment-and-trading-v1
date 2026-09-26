from pathlib import Path
import json
p=Path('review/ready');x=json.loads((p/'quality_compounders.json').read_text())
intro='''# Quality companies: capital-deployment decisions

**Buy a modest Paychex starter at $101.80 or below. Set lower entry levels for Allegion and Snap-on. Pass on Ralph Lauren at the reference price.** These decisions replace audit-only status for this four-company sleeve. A company can be thoroughly researched and still be too expensive.

Research date: 26 September 2026. Decision prices: externally corroborated 24 September regular-session closes. Intended holding period: approximately three years, reviewed weekly; the thesis can require an earlier exit. This is a valuation framework for new capital, not a personalized instruction to sell existing positions. Portfolio sizing belongs in the consolidated investment decision.

## Decision table

| Rank | Company | Reference | Decision / limit | Model maximum entry | Base-case gross IRR | Bear / bull IRR |
|---|---|---:|---|---:|---:|---:|
'''
for c in x['companies']:
 s=c['scenarios'];intro+=f"| {c['rank']} | {c['ticker']} | ${c['price']:.2f} | {c['decision']}; ${c['limit_price']:.2f} | ${c['maximum_entry_model']:.2f} | {s['base']['irr']:.1%} | {s['bear']['irr']:.1%} / {s['bull']['irr']:.1%} |\n"
intro+='''
Maximum entry is the present value of base-case dividends and terminal value at a 12% required return, or 14% for Ralph Lauren. Practical limits round down and also clear the same hurdle under an illustrative 30% dividend-withholding sensitivity. This does not assume that tax rate applies to the investor. Required returns and terminal multiples are investment judgments, not measured probabilities or assurances. The low/high values are scenarios, not statistical confidence intervals. Interim drawdowns can exceed the three-year bear result.

All prices remain frozen at 24 September because newer public displays were inconsistent: Ralph Lauren's 25 September history showed a $354.82 close above its $354.40 high, while Allegion's header and historical row differed. A broker quote should be checked immediately before using any limit. The resulting uncertainty changes neither the valuation arithmetic nor the limit levels.

## Paychex â€” buy a modest starter, limit $101.80

The case is recurring payroll and compliance work at a price that no longer needs a premium multiple to produce a useful return. I assume slower growth than an extrapolation of acquisition-assisted results, charge interest, retain ordinary stock compensation, and do not add a separate buyback yield.

FY2026 adjusted EPS was $5.51 versus GAAP $4.89. Management's FY2027 growth range of 7â€“9% implies adjusted EPS of $5.896â€“$6.006; midpoint $5.951. That is company guidance arithmetic, not a sell-side estimate. My economic FY2027 anchor is $5.85 after allowing approximately $0.10 for recurring integration costs. FY2029 base EPS of $6.60 comes from $7.6bn revenue, 43.8% economic operating margin, $265m interest, $30m other income, 24% tax and 356m diluted shares. This keeps shares approximately flat and retains acquisition financing. A 20Ã— multiple is a 5% earnings yield on modestly growing, recurring revenue; 14Ã— in the bear case allows substantial compression. [FY2026 release](https://www.sec.gov/Archives/edgar/data/723531/000119312526280314/payx-ex99_1.htm), [latest guidance and reconciliation](https://www.sec.gov/Archives/edgar/data/723531/000072353126000004/payx-ex99_1.htm).

The cash audit matters. FY2026 CFO less capital expenditure was $2,321.8m, but TTM through August 2026 is $2,016.7m. Further deducting TTM stock compensation, net purchased receivables and other asset purchases produces a conservative $1,711.5m owner-cash diagnostic, about $4.80 per diluted share. It is not the same definition as GAAP cash flow or company adjusted EPS. The latest quarter's lower CFO reflects payroll-tax, client-refund and bonus timing; a recovery must be demonstrated, not assumed. Corporate cash and investments are $934.2m against debt carrying value of $4,558m; restricted and client funds are excluded from surplus cash. The 10-K's short-rate sensitivity implies about $18â€“20m after-tax annual income change for a mechanically scaled 100bp move, around $0.05 EPS, though reinvestment and longer-term effects differ. [FY2026 10-K, cash flow statement and Market Risk Factors](https://investor.paychex.com/sec-filings/all-sec-filings/content/0001193125-26-307785/0001193125-26-307785.pdf), [Q1 FY2027 10-Q, cash flow and liquidity](https://investor.paychex.com/sec-filings/all-sec-filings/content/0000723531-26-000006/payx-20260831.htm).

**What changes the decision:** two quarters of Management Solutions growth below 3% accompanied by reduced EPS guidance; normalized FY2027 EPS below $5.50; conservative annual owner cash below $1.7bn without a documented reversal; or a dividend sustained through new debt. Near-term catalysts are improvement from 4% Management Solutions growth, Paycor cross-selling and cash conversion. Price weakness alone is not permission to average down.

## Allegion â€” buy below $145

The installed base, specification relationships and security requirements make this a good business. Americas demand is strong, but construction exposure, acquisition spending and international execution justify a price buffer. FY2026 management adjusted EPS guidance is $8.85â€“$9.00, versus GAAP $7.95â€“$8.10. I add back the specified $0.60 acquisition amortization but retain $0.30 restructuring/M&A/other costs, giving a $8.625 economic midpoint. FY2029 base EPS is $10.40: $5.05bn revenue, 23.8% economic operating margin, $100m interest, 19.5% tax and 85m shares. The 19.5Ã— base multiple rewards the franchise while allowing cyclical compression to 15Ã—. [Latest company results and guidance](https://investor.allegion.com/news-and-events/news-releases/2026/07-23-2026-110034749).

FY2025 CFO minus capex was $685.7m versus $582.9m in 2024. Cash after FY2025 SBC of $29.8m was $655.9m; the earnings valuation already charges SBC. H1 2026 FCF fell to $260.8m from $275.4m, producing TTM FCF of $671.1m. Receivables timing is management's explanation; subsequent collections remain a weekly monitoring item. June debt less cash was $1,710.5m before leases. FY2025 acquisition cash of $592.2m is a real use of capital even though excluded from conventional FCF. [FY2025 comparative financial statements](https://investor.allegion.com/news-and-events/news-releases/2026/02-17-2026-110034304), [10-K cash flows and Note 14](https://www.sec.gov/Archives/edgar/data/1579241/000157924126000007/alle-20251231.htm).

**What changes the decision:** two quarters of negative Americas organic growth with more than 200bp margin deterioration; annual cash conversion below 80% of adjusted income with worsening receivables; or acquisition leverage materially above 3Ã— EBITDA without credible funding/deleveraging. The catalysts are electronic access, nonresidential demand and international ERP recovery. The current reference price produces about 11.5% base IRR; $145 creates room above the 12% hurdle.

## Snap-on â€” buy below $310

The distribution network and diagnostic franchise remain attractive, but the valuation must reflect modest growth and a customer-finance operation. FY2025 GAAP EPS of $19.19 included a $0.31 legal benefit: $18.88 after that adjustment, compared with similarly adjusted 2024 EPS of $19.19. I do not automatically remove pension expense. FY2026 $19.80 is an analyst estimate anchored in these results and H1 recovery, not a claim that consensus is validated. FY2029 base EPS of $23 assumes industrial sales of $5.55bn at 23% operating margin, $265m finance operating profit, $50m interest, $45m other income, 22% tax, $25m minority income and 51m diluted shares. [FY2025 results](https://www.sec.gov/Archives/edgar/data/91440/000009144026000008/q42025pressreleaseforpress.htm), [H1 2026 results](https://www.sec.gov/Archives/edgar/data/91440/000009144026000141/q22026pressreleaseforpress.htm).

Conventional TTM FCF is $1,108.5m. Subtracting net finance-loan originations of $11.0m and SBC of $32.1m gives $1,065.4m as an owner-cash cross-check. Financing receivables are not distributable cash; their origination appears in investing. The quarter's finance receivables past due were $61.0m/$1,945.7m, or 3.14%, down from 3.53% at year-end; $18.7m remained more than 90 days overdue and accruing. These facts support resilience, not immunity from credit stress. [FY2025 10-K, Note 13](https://www.sec.gov/Archives/edgar/data/91440/000009144026000045/sna-20260103.htm), [Q2 10-Q, Note 4 and cash flows](https://www.sec.gov/Archives/edgar/data/91440/000009144026000144/sna-20260704.htm).

**What changes the decision:** past-due finance receivables above 5%, rising credit provisions with weaker sales, or two quarters of negative organic tools growth and significant margin loss. At $367.71 the base IRR is only 6.7%. A good company is not automatically a good purchase at that price. Existing holders require a separate tax and opportunity-cost decision.

## Ralph Lauren â€” pass at $351.86; reconsider below $265

Premiumization is working, but the share price already recognizes substantial durability. FY2026 adjusted EPS of $16.59 compares with GAAP $15.11 and ongoing transformation/restructuring addbacks of $1.48. FY2027 has 53 weeks; management's 5â€“6% constant-currency sales growth is on a comparable 52-week basis, with currency subtracting 0.5â€“1 point and the extra week adding roughly one point. The model therefore does not extrapolate Q1's 22% EPS increase. FY2029 base EPS is $21: $9.25bn revenue, 16.6% economic operating margin, zero net interest, 21% tax and 58m shares. The 18.5Ã— base multiple and 14% hurdle reflect discretionary spending, fashion and brand risk. [FY2026 comparative results](https://corporate.ralphlauren.com/pr_260521_Q4FY26_EarningsResults.html), [Q1 FY2027 SEC release](https://www.sec.gov/Archives/edgar/data/1037038/000162828026053896/rl-20260627ex991xpressrele.htm).

FY2026 FCF fell to $746.1m from $1,018.9m because capital spending increased, including real estate. The latest quarter reverses that comparison: TTM FCF is $1,043.2m; after SBC and finance-lease principal the owner-cash diagnostic is $904.3m. Operating rents already reduce earnings and are not subtracted again from an EPS-derived equity value. FY2026 lease liabilities were $1,770.5m, including $233m finance leases. June inventories were down 4.8% against the prior-year quarter; comparing them with March would misstate the seasonal pattern. [FY2026 10-K, Note 13 and cash flow statement](https://www.sec.gov/Archives/edgar/data/1037038/000162828026037074/rl-20260328.htm), [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1037038/000162828026053992/rl-20260627.htm).

**What changes the decision:** inventory growth exceeding sales by more than 10 points for two quarters with markdown pressure; constant-currency growth below 2%; economic margin below 14%; or brand/channel deterioration. The purchase hurdle can also be met by stronger verified cash earnings, not only by a lower price. Current base IRR of 4.5% is inadequate compensation for these risks.

## Scenario arithmetic

All scenario EPS, revenue/margin drivers, terminal multiples and future dividends are analyst assumptions. Historical facts and management guidance are identified above. Scenarios use a September 2029 exit. PAYX and RL use FY2029 earnings already completed by exit; ALLE and SNA use the current FY2029 at exit. No extra fourth forecast year is hidden in the multiple.

Annualized return is the IRR of the purchase, dividends at the end of holding years 1, 2 and 3, and sale proceeds at the end of year 3. It is not a price CAGR with dividends added as an extra yield. No buyback yield is added; the modeled diluted share count captures dilution and any repurchases once. No net cash is added separately because EPS already includes financing/investment income. Dividend payments are gross; the 30% withholding column is a sensitivity, not a tax determination.

| Name / case | Terminal FY2029 EPS | Multiple | Terminal price | Dividends years 1 / 2 / 3 | Gross IRR | IRR with 30% dividend withholding |
|---|---:|---:|---:|---|---:|---:|
'''
for c in x['companies']:
 for name,s in c['scenarios'].items():
  intro+=f"| {c['ticker']} / {name} | ${s['terminal_eps']:.2f} | {s['terminal_pe']:g}Ã— | ${s['terminal_price']:.2f} | {' / '.join('$'+format(d,'.2f') for d in s['dividends_by_holding_year'])} | {s['irr']:.1%} | {s['irr_dividend_withholding_30pct']:.1%} |\n"
intro+='''
The accompanying JSON contains exact model inputs, driver calculations, IRRs and maximum-entry present values. The source manifest records hashes of downloaded SEC/issuer documents. A failed PDF download is explicitly retained as failed; the equivalent Ralph Lauren SEC release and 10-Q were successfully archived. This work is targeted primary-document underwriting, not a claim of an external audit opinion or a fully validated trading backtest.
'''
(p/'quality_compounders.md').write_text(intro,encoding='utf8')
