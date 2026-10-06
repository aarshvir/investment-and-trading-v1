# Stock-only model challenge — 1 October 2026

**Status:** independent agent proposal for the Codex correction, not a published release or a broker instruction. **Parents:** `v011_2026-09-27_claude` (all-stock 20-name research), `v012_2026-09-27_codex` (company scenarios and limits), and `v013_2026-10-01_codex` (fresh prices, eight-company filing challenge and method repairs). **Price cutoff:** completed US regular session 30 September 2026. **Evidence cutoff:** v013 issuer/SEC search through 30 September, 20:30 UTC. No actual holdings or tax residence were supplied.

## Proposed stock-only slate

This is **100% individual US-listed stocks**: no Treasury, bond, ETF, index fund, or strategic cash allocation. A stock-only portfolio can lose substantially more than the user's previously stated 15–20% tolerable temporary decline. The weights are *risk budgets and research priorities*, not an optimized forecast or proof of alpha. They sum to 100%, the largest name is 8%, and financials and industrials each reach but do not exceed 25%.

| Stock | Target | 30 Sep USD close | $50k / $100k target | Thesis and main underwriting issue |
|---|---:|---:|---:|---|
| MSFT | 8% | 512.90 | 4,000 / 8,000 | Enterprise cloud and software earnings; current quote exceeds the prior $500 discretionary ceiling, and a 5% terminal EPS miss cuts inherited 12.05% base IRR to 10.17%. |
| AMP | 6% | 492.35 | 3,000 / 6,000 | Wealth-management cash generation; current price is below old $500 limit but v013 suspended that buy permission. Its 13.20% inherited case requires an exit P/E rise from 11.19× to 13×; flat P/E produces 7.77%. New $5.5bn buyback authorization is optional, not cash created. |
| NVDA | 4% | 228.38 | 2,000 / 4,000 | AI compute demand and strong filed growth; above old $215 ceiling and inherited 14.33% base is below prior 15% hurdle. Supply and customer-financing commitments add correlated downside risk. |
| ADP | 6% | 258.06 | 3,000 / 6,000 | Recurring payroll processing; archived FCF overstated owner cash by omitting $468.5m FY2026 intangible additions. Flat-P/E sensitivity is only 10.51% after assumed tax/cost at this price. |
| TJX | 6% | 132.31 | 3,000 / 6,000 | Off-price retail moat; archived reverse-growth shortcut is invalid. At ~25.6× adjusted FY2027 EPS, flat-multiple sensitivity is 9.75%. |
| RSG | 5% | 209.87 | 2,500 / 5,000 | Route density and essential waste service; old reverse DCF mixed equity FCF with enterprise WACC. Rebuilt flat-P/E sensitivity is 8.65%. |
| MA | 5% | 551.47 | 2,500 / 5,000 | Global payments network; premium multiple leaves little margin for volume or regulation disappointment. Archived scenario is not comparable to v012 after-cost scenarios. |
| MCK | 6% | 853.81 | 3,000 / 6,000 | Scale in drug distribution; thin margins, working capital and customer concentration matter more than headline revenue. Current underwriting remains inherited from v011. |
| STE | 5% | 210.01 | 2,500 / 5,000 | Sterilization and medical procedure exposure; confirm procedure volumes, debt and the next earnings bridge. Current underwriting remains inherited from v011. |
| BALL | 4% | 56.03 | 2,000 / 4,000 | Packaging franchise; commodity input and capital intensity require a no-re-rating cash case. Current underwriting remains inherited from v011. |
| DOV | 5% | 187.05 | 2,500 / 5,000 | Diversified engineered industrials; cyclical orders and acquisition economics require fresh checks. Current underwriting remains inherited from v011. |
| BR | 4% | 161.10 | 2,000 / 4,000 | Recurring financial-market infrastructure; validate cash conversion, debt and retention in the next filing. Current underwriting remains inherited from v011. |
| AXP | 5% | 304.10 | 2,500 / 5,000 | Premium card network and lending; credit losses and spending cycle are linked. Current underwriting remains inherited from v011. |
| USB | 4% | 57.76 | 2,000 / 4,000 | Diversified bank at lower earnings multiple; deposit funding, losses and CET1 are the binding risks. Current underwriting remains inherited from v011. |
| CRH | 5% | 82.80 | 2,500 / 5,000 | Construction materials and infrastructure spend; volume/cycle and acquisition cash uses require stress. Current underwriting remains inherited from v011. |
| PTC | 4% | 140.30 | 2,000 / 4,000 | Industrial software subscriptions; growth, valuation and implementation churn require updated proof. Current underwriting remains inherited from v011. |
| VEEV | 4% | 285.45 | 2,000 / 4,000 | Life-sciences software and high retention; premium multiple can compress. Current underwriting remains inherited from v011. |
| GDDY | 4% | 95.51 | 2,000 / 4,000 | Recurring domains/merchant software; debt, buybacks and per-share cash reconciliation need refresh. Current underwriting remains inherited from v011. |
| ALLE | 5% | 153.77 | 2,500 / 5,000 | Access-control franchise; above old $145 review ceiling and normalized owner cash awaits refresh. |
| HIG | 5% | 122.36 | 2,500 / 5,000 | Diversified property-casualty underwriting; above old $120 review ceiling, and the September settlement requires capital/tax/reinsurance reconciliation. |

The 20 reference prices all have same-session Yahoo and Cboe observations agreeing within 0.1%, with raw response hashes in `GPT/2026-10-01/MARKET_RECONCILIATION.csv`. They are dated observations, not executable quotes. Amounts are target dollars, not rounded share counts or orders. $100k targets double $50k targets. Whole-share rounding, taxes, FX, spreads and account constraints would produce residual settlement cash; that is not a strategic cash allocation.

## Execution gate: what is and is not buyable at the archived price

**No name earns an unconditional buy-at-current certificate from these frozen files.** v013 swept eight company SEC submission histories overall, but that group includes PAYX and LH, which are absent from this slate. Most proposed names rely on September 25 dossiers. Even the freshly checked names have valuation conflicts. A fully invested *model* does not prove that all twenty can be bought safely at a stale close. The correction should not quietly revive v013-suspended AMP/PAYX orders or v012 limits for MSFT, NVDA, ALLE and HIG. A legitimate fully invested stock-only implementation must obtain current executable prices, refresh operating facts and state a revised common hurdle or relative-value rule; if that gate rejects a name, reallocate only among newly cleared stocks rather than Treasury, ETF or a permanent reserve. No broker trade is implied by this proposal.

The strongest **priority for immediate re-underwriting** is MSFT, AMP and ADP; they have primary-source financials and explicit scenario bridges, but AMP still depends on re-rating and MSFT/ADP have thin or below-hurdle no-rerating returns at the archived prices. NVDA should be a small, high-variance sleeve. PAYX, WEC and LH should not fill the stock-only mandate merely because capital must be invested.

## Changes from Claude's published twenty

Retain fifteen v011 companies: USB, GDDY, VEEV, ADP, MA, TJX, CRH, BR, STE, AXP, DOV, BALL, PTC, RSG and MCK. Remove five for this comparative slate:

- **WEC:** its old 8.32% weight is excessive for a regulated utility whose archived reverse DCF discounts EPS instead of distributable owner cash. At the old $101.45 price, updated $3.81 annual dividend run rate, 7.5% EPS growth and a 15× exit, the 3-year gross return is about 4.43%; at 13× it is near zero. This does not imply a real account must sell WEC.
- **LVS:** the archived 37.47% base annual return shrinks to about 9.81% gross if its entry P/E persists; Macau/Singapore cash use and exit multiple remain unresolved.
- **LH:** June 2026 H1 FCF of $384.4m requires $915.6m in H2 to reach FY2026 guidance midpoint. This may be seasonal but is not independently cleared. A corrected full-year cash bridge would make it eligible again.
- **PGR:** the archived FY1 estimate of $1,012 is malformed and cannot enter a valuation. Rebuild premium growth, combined ratio, reserve adequacy and regulatory capital from filings.
- **HBAN:** this is a second regional bank alongside USB and would amplify credit/deposit correlation without clearly superior decision-critical evidence.

Add MSFT, AMP, NVDA, ALLE and HIG as diversified candidates using v012/v013 company work, while preserving the limits and caveats above. Reduce RSG's 6.98% weight to 5% pending a valid equity valuation. The revised sector layout is financials 25%, industrials 25%, technology 20%, health care 15%, materials 9%, consumer discretionary 6%. These are **classification weights**, not independent risk factors: credit, rates, economic growth and equity valuation remain correlated across sectors.

**PAYX exclusion is deliberate.** Its quarter ended August 31 reported $413.5m operating cash flow less $56.1m capex, below $424.1m dividends paid. That one-quarter deficit is not proof of a broken dividend, but it weakens an immediate 20× terminal P/E thesis. Its inherited 13.29% base falls to 7.34% at unchanged entry P/E. [Primary PAYX 10-Q](https://investor.paychex.com/sec-filings/all-sec-filings/content/0000723531-26-000006/payx-20260831.htm). If subsequent cash generation and integration improve, it can challenge a weaker holding.

## Risk and validation limit

A transparent **hypothetical simultaneous sector shock** of financials −45%, industrials −40%, technology −50%, health care −30%, materials −50%, consumer discretionary −45% would reduce this exact 100%-stock basket by **42.95%** before costs or any correlation spillover. These shock sizes are judgments, not a model probability or a worst-case bound. A severe stock crash could be worse. The archived v011 all-stock historical crisis replay lost roughly 47% in the GFC and 37% during COVID with its different weights; it is a diagnostic, not a backtest of this modified slate. Thus a stock-only mandate cannot credibly promise a 15–20% maximum loss without hedges or guaranteed protection, neither of which the user requested. State that tension plainly and honor the stock-only instruction.

No compounded portfolio CAGR or chance of outperformance is assigned. v011's per-name bases mix assumptions and do not demonstrate a stock-picking edge; v013's 90-price ledger covers only fourteen comparable inherited operating scenarios and does not validate this 20-name basket. The v011 factor replay also lacked full causal point-in-time certification. Forecasts must be locked prospectively and compared with the S&P 500, tax/cost adjusted, at 30/90/365 days. Every stock needs next filing, no-rerating earnings/cash bridge, bear loss, thesis-break and replacement competitor before individual purchase approval.

### Evidence anchors

- Frozen [v011 release notes](../../../../versions/v011_2026-09-27_claude/RELEASE_NOTES.md), archived 20-stock `v4/outputs/lead_portfolio.json`, and [v013 shadow review](../../V011_SHADOW_REVIEW.csv). Do not substitute the concurrently edited live `v4/` working files for the published parent.
- [v013 company challenge](../../company_challenge/COMPANY_CHALLENGE.md), [price reconciliation](../../MARKET_RECONCILIATION.csv), [scenario repricing](../../SCENARIO_REPRICE.json) and [portfolio challenge](../../portfolio_challenger/PORTFOLIO_CHALLENGE.md).
- Primary [Microsoft FY2026 10-K](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), [AMP authorization](https://ir.ameriprise.com/news/news-details/2026/Ameriprise-Financial-Announces-Additional-5-5-Billion-Share-Repurchase-Authorization/default.aspx), [ADP FY2026 10-K](https://www.sec.gov/Archives/edgar/data/8670/000000867026000030/adp-20260630.htm), [TJX Q2 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm), [RSG Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1060391/000106039126000275/rsg-20260630.htm), [NVDA Q2 FY2027 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm), and [HIG 8-K](https://www.sec.gov/Archives/edgar/data/874766/000087476626000064/hig-20260923.htm).
