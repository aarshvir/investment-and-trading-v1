# Independent fund implementation cross-review — 26 September 2026

**PASS on identity, currency, fee and specified dated NAV facts.** IB01 and VUAA are usable research implementation candidates for an eligible non-US investor with the correct broker access. Their quoted NAVs are reference values, not executable exchange asks. A completed portfolio plan must preserve that distinction.

| Check | Independent primary-source result | Exact locator |
|---|---|---|
| IB01 identity | iShares $ Treasury Bond 0–1yr UCITS ETF, USD accumulating; Ireland; ISIN **IE00BGSF1X88** | [Issuer page](https://www.ishares.com/uk/individual/en/products/307243/ishares-treasury-bond-0-1yr-ucits-etf), Key Facts; [KIID p1](https://www.ishares.com/gls-download/literature/kiid/ucits_kiid-ishares-treasury-bond-0-1yr-ucits-etf-usd-acc-gb-ie00bgsf1x88-en.pdf#page=1) |
| IB01 selected exchange line | **London Stock Exchange / IB01 / USD**, Bloomberg IB01 LN, SEDOL BJFT383, RIC IB01.L | Issuer page, Listings table, London Stock Exchange row |
| IB01 NAV | **$121.86 as of 24 September 2026** | Issuer page, Overview NAV panel |
| IB01 expense | **0.07% TER** | Issuer page, Key Facts, Total Expense Ratio |
| IB01 interest sensitivity | **0.31 effective duration**, **4.16% weighted-average YTM**, both dated 24 September 2026 | Issuer page, Portfolio Characteristics |
| VUAA identity | Vanguard S&P 500 UCITS ETF, USD accumulating; Ireland; ISIN **IE00BFMXXD54** | [Issuer page](https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-usd-accumulating), Fund facts and Purchase information; [KIID p1](https://fund-docs.vanguard.com/ie00bfmxxd54-en.pdf#page=1) |
| VUAA selected exchange line | **USD – London Stock Exchange / VUAA**, Bloomberg VUAA LN, SEDOL BH3T3H0, Reuters VUAA.L | Issuer page, Purchase information → Fund codes → USD – London Stock Exchange |
| VUAA NAV | **$149.0017 as of 24 September 2026** | Issuer page, Prices and distribution → Historical Prices, September 24 row, NAV(USD) column |
| VUAA expense | **0.07% OCF/TER** | Issuer page, headline OCF/TER; [KIID p2, Charges](https://fund-docs.vanguard.com/ie00bfmxxd54-en.pdf#page=2) |

Both webpages, both KIIDs and both current prospectuses were downloaded in full to `review/ready/raw_funds`; `manifest.json` records retrieval time, bytes and SHA-256. This independent review confirms issuer disclosure, not independent auditing of every underlying holding. The current Vanguard prospectus is dated **4 September 2026**, while a search-engine snippet still described an older April version; the downloaded cover page resolves the version. iShares' prospectus is dated **21 September 2026**.

## Currency and execution traps caught

Vanguard's page defaults to the **VUAG GBP listing** in its headline. Its **£112.80 on September 25** is a GBP market quotation; it is neither $112.80 nor the USD VUAA exchange price. Its September 24 $149.0017 is the common share-class USD NAV. USD VUAA and GBP VUAG are trading lines of the same ISIN, but currency and trading venue must be matched at the broker. A GBP trading line does not make the underlying US-equity exposure currency hedged. Other European exchanges also use the ticker VUAA, including EUR lines. A ticker alone is therefore insufficient.

For IB01, Mexico and Colombia listings also appear under related tickers/currencies. Match **ISIN + LSE + USD**. Share quantities based on dated NAV are planning estimates: executable prices include spread and can differ from NAV, especially with different market hours. Use the current broker bid/ask and an appropriately priced limit; include commissions and currency conversion costs. Do not use a stale NAV as a mandatory purchase price.

IB01's 4.16% YTM is a dated portfolio statistic, not a guaranteed annual return or cash distribution. It is accumulating, so interest is retained in NAV. Deducting 0.07% gives approximately 4.09% as a simplified yield-after-fee illustration, but realized return also depends on rates, reinvestment, price/spread and tax. Duration 0.31 suggests an immediate roughly **−0.31% price change for a +1 percentage-point parallel yield move**, before carry and convexity; this approximation does not cover every risk. It is a short-duration fund, not a bank deposit or principal guarantee. The issuer's broad Cash/Derivatives display category should not be read as an audited percentage of idle bank cash without checking underlying holdings.

## Wrapper eligibility: distinguish tax status from location

[iShares prospectus, PDF pp2–3](https://www.ishares.com/gls-download/literature/prospectus/ishares-plc-prospectus-en.pdf#page=2) restricts offers/sales in the US or for US Persons and provides for action against non-qualified holders. [Vanguard Funds plc prospectus, PDF p4](https://fund-docs.vanguard.com/etf-prospectus-en.pdf#page=4) states that US-person participation is generally restricted, subject to specified exemptions/exceptional circumstances. Do not present either UCITS wrapper as universally suitable for a US person merely because the person lives in Dubai or uses a non-US broker.

Separately, a US tax person owning a foreign investment fund may encounter PFIC taxation/reporting. The [IRS Form 8621 instructions](https://www.irs.gov/instructions/i8621) describe who must file and applicable exceptions. This is a screening issue, not a determination of the user's tax residence, nationality, PFIC liability or entitlement to an exemption. Prospectus US-person definitions and US tax-person definitions need not be identical. For an eligible non-US investor, verify local availability and broker permissions; an Irish domicile does not itself make the holding tax-free. The direct US stocks elsewhere in the portfolio retain their own withholding and estate-tax considerations; UCITS ownership does not remove those from separate direct holdings.

## Portfolio arithmetic and concentration cross-check

The proposed **20% VUAA + 10% direct stocks + 70% reserve totals 100%**. Direct slots are AMP 2%, PAYX 2%, MSFT 2%, NVDA 1.5%, ALLE 1.5%, HIG 1%. If some buy limits do not fill, the unfilled amounts remain reserve and actual equity exposure is below 30%; do not label all target allocations already invested.

Vanguard reports August 31 underlying weights of **8.07902% NVIDIA** and **5.69335% Microsoft**. At a 20% fund weight, these add 1.615804% and 1.138670% of total portfolio capital respectively. The fully filled direct-plus-fund positions therefore become **3.115804% NVIDIA** and **3.138670% Microsoft**. The current report's direct-stock cap must be labeled **direct holdings only** if these slots are retained; an all-in 2% issuer cap would require smaller direct positions. These are dated estimates and should be refreshed as weights move. [Vanguard issuer page, Portfolio data → Holdings details, 31 August 2026](https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-usd-accumulating).

A 30% equity allocation losing 50% produces a 15% portfolio loss only under a flat-reserve assumption. Simultaneous reserve losses, currency moves, costs and uneven equity drawdowns change the outcome. Treat 15–20% as a risk budget for stress testing, not a hard floor established by this allocation.

