# R2: Implementation, structure and cross-border tax facts for a UAE-resident investor

- **Agent:** r2 (implementation, structure and cross-border tax facts)
- **As of:** 2026-09-26. Sources were retrieved on 2026-09-26 UTC. Page and document dates are given in §10.
- **Scope:** General, factual information with primary-source citations. **This is not personalised tax, legal or investment advice.** The rules below are applied to a hypothetical individual who is tax-resident in the UAE and who is **not** a US citizen, not a green-card holder and not US-domiciled (a US "nonresident alien", or NRA). Cross-border estate and withholding rules have many nuances. **Confirm anything you would act on with a qualified cross-border (US/UAE and, where relevant, Irish) tax adviser.**
- **Citations:** Bracketed tags such as [S2] refer to the numbered source list in §10.

---

## 0. Summary

1. **US estate tax still applies to NRAs.** An NRA gets only a **USD 13,000 unified credit** [S4][S2]. That shelters about **USD 60,000** of US-situs assets, and the figure is not inflation-indexed. Rates follow the §2001(c) schedule, from **18% to 40%** [S3][S8]. The 2026 USD 15m basic exclusion [S71] applies only to US citizens and domiciliaries, not to NRAs [S2][S4].
   - **US-situs** includes shares of any US-incorporated company and **US-domiciled ETFs such as VOO**, no matter which broker holds them (IBKR, Vested or any other) [S5][S2][S6].
   - An executor must file **Form 706-NA** when US-situs assets exceed USD 60,000. It is due 9 months after death [S2][S11].
   - The **UAE has no estate or gift tax treaty with the US** [S12].
   - Illustrative tax: **USD 80k of US-situs assets gives USD 5,200 of tax; USD 100k gives USD 10,800** (arithmetic in §1.3).
2. **There is no US–UAE income tax treaty** [S17][S18]. US-source dividends paid to a UAE resident are withheld at **30%** [S19][S20].
   - Form W-8BEN establishes foreign status but **does not reduce the rate** for UAE residents [S21].
   - **Capital gains** are generally **not taxed by the US** for an NRA who is in the US for fewer than 183 days and has no US trade or business. Trading for your own account through a broker is not a trade or business [S20].
   - **Direct T-bill interest** is generally exempt, either as short-term OID (maturity of 183 days or less) or as portfolio interest with W-8BEN documentation [S19]. Directly held T-bills are also non-US-situs for estate tax [S6]. **T-bill or money-market ETFs are US-situs**, because they are US funds [S2][S6].
3. **The UAE levies no personal income tax** [S24][S25].
   - Cabinet Decision No. 49 of 2023 takes **"Personal Investment" income** out of UAE Corporate Tax for individuals, whatever the amount [S26].
   - The FTA's own example is an individual who invests personal savings in listed securities. That income is not subject to Corporate Tax [S27].
4. **Irish-domiciled UCITS S&P 500 ETFs are generally not US-situs** because they are shares of a foreign corporation [S7][S2]. They also face lower US dividend withholding.
   - **Physical funds (CSPX, VUAA, SPY5)** suffer **15%** withholding at fund level under the US–Ireland treaty [S18]. A UAE resident holding VOO suffers **30%**.
   - **Swap-based SPXS** avoids US dividend withholding under the §871(m) "qualified index" exception [S35][S34]. The trade-off is counterparty risk and regulatory-change risk [S30][S37].
   - Ireland deducts no tax on these ETFs for non-residents [S38]. Irish inheritance tax (CAT) exempts fund units held by non-Irish-resident, non-Irish-domiciled holders and heirs [S39].
5. **Tax drag at the current ~1.11% S&P 500 dividend yield** [S31] (withholding drag plus fund cost, per year):

   | Vehicle | Annual drag | Per year on USD 80k |
   |---|---:|---:|
   | VOO held by a UAE resident | ≈0.36% | ≈USD 290 |
   | CSPX / VUAA | ≈0.24% | ≈USD 189 |
   | SPY5 | ≈0.20% | ≈USD 157 |
   | SPXS | ≈0.12% | ≈USD 96 |

   - The recurring gap between VOO and CSPX is about **USD 100 a year on USD 80k**.
   - On top of that, VOO leaves the whole USD 80k exposed to US estate tax (USD 5,200 at today's value).
   - Actual 2025 returns ranked the vehicles in the same order (§4.5).
6. **A stock-picking sleeve of US-incorporated companies is necessarily US-situs.**
   - UCITS funds are diversified pools that cannot hold more than 5–10% in one issuer, or up to 20–35% for index funds [S37]. There is no single-stock UCITS wrapper.
   - US-listed shares of **foreign-incorporated** issuers are not US-situs [S5][S15]. Examples include Linde plc and Accenture plc (both Ireland) and Chubb Ltd (Switzerland) [S42]. However, they can bring other countries' withholding tax and, for Irish plcs, possible exposure to Irish inheritance tax (§6).
7. **Brokers**
   - **IBKR:** UAE residents can generally trade both US ETFs and LSE UCITS ETFs. The EU/UK PRIIPs block on US ETFs is aimed at EEA/UK retail clients [S50][S70].
     - US stocks: Pro Fixed pricing is **USD 0.005/share, minimum USD 1**. IBKR Lite is for US residents only [S43].
     - LSE USD-quoted ETFs: **0.05% of trade value**, minimum USD 4 on Fixed, or a USD 39 cap on Tiered [S43].
     - FX conversion costs **0.2 bp**, minimum USD 2 [S44].
     - Fractional shares are available on 10,500+ US stocks and ETFs. For European listings, eligibility depends on liquidity [S45][S46].
   - **Vested:** US stocks and ETFs only. Trades go through VF Securities, Inc., which clears through **DriveWealth LLC** [S53][S54].
     - Commission is **0.25% of trade value (max USD 35)** on the Basic plan [S51].
     - Accounts carry SIPC cover of **USD 500k (USD 250k cash)** [S56].
     - There is **no LSE UCITS ETF access**. Vested's UCITS "Global Funds" are mainly active mutual funds sold under India's LRS [S55].
     - **US stocks and US ETFs held at Vested are US-situs.** They count toward the same USD 60k threshold as US holdings at IBKR.
8. **Execution basics**
   - Use limit orders. A stop order becomes a market order and can fill far from the stop, for example after an earnings gap [S57][S58][S60][S67].
   - In Dubai time (GST, UTC+4, no daylight saving) during northern summer time [S66]:
     - LSE: **11:00–19:30**
     - NYSE/Nasdaq: **17:30–24:00**
     - Overlap: **17:30–19:30**
   - LSE shifts to **12:00–20:30** from 26 Oct 2026, and NYSE to **18:30–01:00** from 2 Nov 2026 (§7.3).
   - Settlement is **US T+1** (since 28 May 2024) and **UK T+2** until the UK moves to T+1 on **11 Oct 2027** [S61][S62].

---

## 1. US estate tax for nonresident aliens

### 1.1 Rules

| Item | Fact | Source |
|---|---|---|
| Who is taxed | An estate tax applies to the taxable estate of "every decedent nonresident not a citizen of the United States" | §2101(a) [S8] |
| How it is computed | Tentative tax under the §2001(c) schedule on (taxable estate + adjusted taxable gifts), less tentative tax on adjusted taxable gifts | §2101(b) [S8] |
| Credit | "A credit of $13,000 shall be allowed against the tax imposed by section 2101." The instructions say "In general, the maximum unified credit is $13,000." | §2102(b)(1) [S4]; Instr. 706-NA (Rev. 09/2025) [S2] |
| Effective exemption | USD 13,000 credit = tentative tax on USD 60,000 (verified in §1.3), so about USD 60,000 is sheltered. The amount is statutory and not indexed. | [S3][S4] |
| Rates | 18% on the first USD 10k, rising in steps to 40% above USD 1m (full schedule in §1.2) | §2001(c) [S3] |
| Filing | "The executor must file Form 706-NA if the date of death value of the decedent's U.S.-situated assets, together with the gift tax specific exemption and the amount of adjusted taxable gifts, exceeds the filing threshold of $60,000." | [S2]; IRS page updated 27-Jun-2026 [S1] |
| Due date | Within 9 months after death | §6075(a) [S11] |
| US-situs stock | Stock owned by an NRA is US property "only if issued by a domestic corporation". The instructions say "Stock of corporations organized in or under U.S. law is property located in the United States, and all other corporate stock is property located outside the United States." | §2104(a) [S5]; [S2] |
| US-domiciled ETFs and mutual funds (e.g., VOO) | These are shares of a US-organised fund taxed as a corporation (a regulated investment company, or RIC), so US-situs. The only look-through relief for regulated investment company (RIC) shares, §2105(d), "shall not apply to estates of decedents dying after December 31, 2011". Broker location is irrelevant. | [S6][S2][S5] |
| Foreign-corporation stock (incl. Irish UCITS ETFs) | Not US-situs: "Shares of stock issued by a corporation which is not a domestic corporation, regardless of the location of the certificates" | Treas. Reg. §20.2105-1(f) [S7]; [S2] |
| ADRs of foreign companies | IRS PLR 200243031 (2002): ADRs representing shares of a foreign corporation "do not constitute shares of stock issued by a domestic corporation and, therefore, are not property within the United States under § 2104(a)". A PLR binds only the requesting taxpayer and "may not be used or cited as precedent". Practice treats ADRs as non-US-situs, but this is not formally settled. | [S15] |
| Bank deposits, portfolio debt, short-term OID debt | Not US-situs: certain bank deposits, debt whose interest would be portfolio interest, and short-term (183 days or less) OID obligations, e.g., directly held T-bills | §2105(b)(1)–(4) [S6]; [S1][S2] |
| Deductions | Debts and expenses are deductible only pro rata, and only if the return discloses the non-US part of the gross estate. The marital deduction is generally available only if the surviving spouse is a US citizen. | §2106(a)(1),(b) [S9]; IRS FAQ (updated 20-Sep-2026) [S13] |
| Gift tax | US gift tax does not apply to transfers of **intangible property** (e.g., shares) by an NRA, with limited expatriate exceptions | §2501(a)(2) [S10] |
| Treaty | The IRS lists estate/gift treaties with 15 countries: Australia, Austria, Canada, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan, Netherlands, South Africa, Switzerland, UK. **The UAE is not listed.** | IRS page updated 08-Sep-2026 [S12] |
| Transfer certificate (practical) | A US custodian normally needs an IRS transfer certificate before releasing a deceased NRA's US assets. Below the USD 60k threshold, Form 706-NA is not filed; an affidavit route applies ("Part B"). IRS processing takes "12 to 18 months". | IRS page updated 05-May-2026 [S14] |
| 2025–26 legislation | "Estates of decedents who die during 2026 have a basic exclusion amount of $15,000,000" (IR-2025-103, 09-Oct-2025). That applies to US citizens and domiciliaries. The NRA rules (USD 60k threshold, USD 13k credit) are unchanged in the IRS instructions (Rev. 09/2025) and in IRS pages updated June–September 2026. | [S71][S2][S1][S13][S16] |

### 1.2 Rate schedule (IRC §2001(c)) [S3]

| Taxable amount | Tentative tax |
|---|---|
| ≤ 10,000 | 18% |
| 10,000–20,000 | 1,800 + 20% of excess over 10,000 |
| 20,000–40,000 | 3,800 + 22% over 20,000 |
| 40,000–60,000 | 8,200 + 24% over 40,000 |
| 60,000–80,000 | 13,000 + 26% over 60,000 |
| 80,000–100,000 | 18,200 + 28% over 80,000 |
| 100,000–150,000 | 23,800 + 30% over 100,000 |
| 150,000–250,000 | 38,800 + 32% over 150,000 |
| 250,000–500,000 | 70,800 + 34% over 250,000 |
| 500,000–750,000 | 155,800 + 37% over 500,000 |
| 750,000–1,000,000 | 248,300 + 39% over 750,000 |
| > 1,000,000 | 345,800 + 40% over 1,000,000 |

### 1.3 Illustrative arithmetic (no deductions, no prior gifts, no treaty)

- **USD 60,000:** 8,200 + 24% × (60,000 − 40,000) = 8,200 + 4,800 = **13,000**. The credit of 13,000 cancels it, so the tax is **USD 0**. This confirms why about USD 60k is sheltered.
- **USD 80,000:**
  - Tentative tax = 13,000 + 26% × (80,000 − 60,000) = 13,000 + 5,200 = **18,200**.
  - Less the 13,000 credit = **USD 5,200**. That is 6.5% of the total, or 26% of the excess over 60k.
- **USD 100,000:**
  - Tentative tax = 18,200 + 28% × (100,000 − 80,000) = 18,200 + 5,600 = **23,800**.
  - Less 13,000 = **USD 10,800**. That is 10.8% of the total, or 27% of the excess over 60k.

Ladder computed by `code/r2_implementation_calcs.py`:

| US-situs value at death | Tentative tax | Credit used | US estate tax | % of value | 706-NA required? |
|---:|---:|---:|---:|---:|:--|
| 50,000 | 10,600 | 10,600 | 0 | 0.0% | No |
| 60,000 | 13,000 | 13,000 | 0 | 0.0% | No |
| 70,000 | 15,600 | 13,000 | 2,600 | 3.7% | Yes |
| 80,000 | 18,200 | 13,000 | **5,200** | 6.5% | Yes |
| 90,000 | 21,000 | 13,000 | 8,000 | 8.9% | Yes |
| 100,000 | 23,800 | 13,000 | **10,800** | 10.8% | Yes |
| 150,000 | 38,800 | 13,000 | 25,800 | 17.2% | Yes |
| 200,000 | 54,800 | 13,000 | 41,800 | 20.9% | Yes |

The tax is measured on value **at the date of death**, not on cost. A USD 50k US-situs holding crosses USD 60k in 3.7 years at 5%/yr, 2.7 years at 7%/yr or 1.9 years at 10%/yr (constant-growth arithmetic).

---

## 2. US income-tax side: dividends, gains, interest

| Item | Fact | Source |
|---|---|---|
| Statutory rate | "Most types of U.S. source income received by a foreign person are subject to U.S. tax of 30%." For NRAs, "Dividends are generally taxed at a 30% (or lower treaty) rate. The brokerage company or payer of the dividends should withhold this tax at source." | Pub 515 (2026) [S19]; Pub 519 [S20] |
| US–UAE income tax treaty | **None.** The UAE is absent from the IRS "tax treaties A to Z" list (updated 03-Jan-2026) and from IRS Table 3, "List of Tax Treaties" (updated through 26-Sep-2025). No signed treaty or public negotiation was found. So 30% applies to US dividends paid to a UAE resident. | [S17][S18] |
| Form W-8BEN | Establishes that the holder is not a US person and is the beneficial owner, and claims treaty benefits where available (none for the UAE). Valid from signing until the last day of the third following calendar year. Without it, a payer may withhold at 30% or apply backup withholding under §3406, currently 24%. Backup withholding can apply to reportable payments including dividends and broker proceeds (Form 1099-B). | Instr. W-8BEN (Rev. Oct 2021) [S21]; IRS backup withholding page (updated 28-Jun-2026) [S22] |
| Capital gains | "If you were in the United States for less than 183 days during the tax year, capital gains (other than gains listed earlier) are tax exempt unless they are effectively connected with a U.S. trade or business." "If your only U.S. business activity is trading in stocks… through a U.S. resident broker… you are not engaged in a trade or business in the United States." | Pub 519 (for 2025 returns) [S20] |
| Fund capital-gain / interest-related dividends | "Certain interest-related dividends and short-term capital gain dividends paid by a mutual fund or other RIC are exempt from chapter 3 withholding." In practice this depends on the fund designating them and on the broker's systems. | Pub 515 [S19] |
| T-bills / short-term debt | Interest and OID on obligations payable in 183 days or less from original issue "are not subject to chapter 3 withholding". Interest on longer registered obligations can qualify as **portfolio interest**, which is exempt if the holder's non-US status is documented, e.g., by W-8BEN. | Pub 515 [S19]; Pub 519 [S20] |
| Bank deposit interest | Not subject to chapter 3 withholding if not connected with a US trade or business | Pub 515 [S19] |
| Dividends from foreign-incorporated companies | "Dividends paid by a foreign corporation are generally not subject to chapter 3 withholding." The issuer's home country may withhold instead (not researched here). | Pub 515 [S19] |
| Publicly traded partnerships (PTPs, e.g., many MLPs) | Brokers must withhold **10% of the gross amount realised** on transfers of PTP interests by foreign persons, effective for transfers on or after 1 Jan 2023 (§1446(f)). In addition, "If you are a member of a partnership that at any time during the tax year is engaged in a trade or business in the United States, you are considered to be engaged in a trade or business in the United States." The partner's share of profits is then ECI, withheld on distributions and reported on Form 1040-NR. This matters if a stock-picking sleeve includes PTP units. | Pub 515 [S19]; Pub 519 [S20] |

---

## 3. UAE side

| Item | Fact | Source |
|---|---|---|
| Personal income tax | "The UAE does not levy income tax on individuals." PwC (last reviewed 09-Sep-2026): "There is currently no personal income tax in the United Arab Emirates." A Dec-2025 news item claiming a 2026 personal income tax now returns HTTP 404 and is contradicted by both sources above. | u.ae [S24]; PwC [S25] |
| Corporate Tax law | Federal Decree-Law No. 47 of 2022 (Corporate Tax Law) | [S26] |
| Natural persons | Individuals are subject to Corporate Tax only if their **Business** turnover exceeds **AED 1,000,000** in a calendar year (Art. 2(1)). Turnover from "a. Wage. b. Personal Investment income. c. Real Estate Investment income" is **not** Business "regardless of the amount of Turnover" (Art. 2(2)). An individual with no taxable Business "shall not be required to register" (Art. 2(3)). In force from 1 Jun 2023. | Cabinet Decision No. 49 of 2023 [S26] |
| "Personal Investment" definition | "Investment activity that a natural person conducts for their personal account that is neither conducted through a Licence or requiring a Licence from a Licensing Authority in the State, nor considered as a commercial business in accordance with the Federal Decree-Law No. 50 of 2022." | Art. 1 [S26] |
| FTA worked example | Example 11: an individual in the UAE invests personal savings in listed securities and "does not require a Licence". "The income derived… is Personal Investment income and accordingly is not subject to Corporate Tax." | FTA guide CTGTNP1 (Nov 2023) [S27] |
| Boundary caveat | Investing through a licensed business or company, or activity amounting to commercial business under the Commercial Transactions Law, falls outside the Personal Investment carve-out | [S26][S27] |
| Currency | The AED is pegged to the USD. The CBUAE rate on 01-Jun-2026 was USD 1 = AED 3.6725, so USD-denominated holdings carry negligible AED/USD currency risk while the peg holds. | CBUAE [S68] |

---

## 4. Irish-domiciled UCITS S&P 500 ETFs

### 4.1 Fund facts (issuer factsheets)

| | iShares Core S&P 500 UCITS ETF (USD Acc) | Vanguard S&P 500 UCITS ETF (USD Acc) | State Street SPDR S&P 500 UCITS ETF (Dist) | Invesco S&P 500 UCITS ETF Acc |
|---|---|---|---|---|
| LSE tickers | **CSPX** (USD), **CSP1** (GBP) | **VUAA** (USD), VUAG (GBP) | **SPY5** (USD), SPX5 (GBP). Primary listing is Deutsche Börse. | **SPXS** (USD; Bloomberg SPXS LN) |
| ISIN | IE00B5BMR087 | IE00BFMXXD54 | IE00B6YX5C33 | IE00B3YCGJ38 |
| Legal issuer / domicile | iShares VII plc / Ireland | Vanguard Funds plc / Ireland | SSGA SPDR ETFs Europe I plc / Ireland | Invesco Markets plc / Ireland |
| TER / OCF | **0.07%** | **0.07%** | **0.03%** | **0.05%**, plus a **0.07% swap fee** included in the swap return and not charged separately |
| Replication | Physical | Physical (full; sampling if impractical) | Physical ("Replicated") | **Synthetic (swap)** |
| Income | Accumulating | Accumulating | Quarterly distribution | Accumulating |
| Benchmark | S&P 500 (net TR) | S&P 500 Net TR (SPTR500N) | S&P 500 Net TR (SPTR500N) | S&P 500 Net TR (SPTR500N) |
| Size | Share class USD 156,147m; fund USD 159,305m (31-Aug-2026) | Fund USD 86,036m; share class USD 34,182m (31-Jul-2026) | Share class USD 21,155m; fund USD 43,564m (31-Aug-2026) | Fund USD 58,763m (31-Aug-2026). 100:1 split on 15-Dec-2025; NAV USD 15.43/share. |
| Launch | 18/19-May-2010 | 14-May-2019 | 19-Mar-2012 | 20-May-2010 |
| Source | [S28] | [S29] | [S31] | [S30] |

Notes:
- SPY5 was renamed "State Street SPDR S&P 500 UCITS ETF (Dist)" on 19-Feb-2026 [S31].
- Vanguard defines the benchmark precisely: "The S&P 500 Net Total Return Index represents price-plus-net cash dividend return. Net cash dividend equals reinvested dividends less 30% withholding tax." [S29] That is why Irish physical funds can beat their benchmark: they pay 15%, not 30%.

### 4.2 Withholding mechanics

| Layer | Direct US ETF (e.g., VOO) held by a UAE resident | Irish physical UCITS (CSPX, VUAA, SPY5) | Irish synthetic UCITS (SPXS) |
|---|---|---|---|
| US tax on dividends from S&P 500 companies | None at fund level, because VOO is a US fund | **15%**, withheld from the fund under the US–Ireland treaty. IRS Table 1 shows 15% general and 5% direct rates for Ireland; the treaty dates from 1997. | **~0%**. The fund receives the index return through swaps. Swaps on a "qualified index" such as the S&P 500 are outside §871(m) dividend-equivalent withholding. |
| Tax on the fund's payout to the investor | **30%** US withholding on each distribution | Accumulating funds make no payout. For SPY5, Ireland deducts nothing for non-residents: ETF units held in a recognised clearing system are exempt (TDM §4.2.3), as are declared non-residents (§4.2.8). There is also no US withholding, because the dividend comes from a foreign corporation (Pub 515). | No payout (accumulating) |
| Net US withholding borne | **30%** | **15%**, borne inside the fund | **~0%**, less the 0.07% swap fee |
| US estate situs | **US-situs** | **Not US-situs** (foreign corporation) | **Not US-situs** |
| Irish inheritance tax (CAT) | n/a | Units of Irish investment undertakings are **exempt** where the deceased and the beneficiary are neither domiciled nor ordinarily resident in Ireland (CATCA 2003 s.75) | Same |
| Sources | [S19][S20][S6] | [S18][S23][S38][S39][S7][S19] | [S30][S34][S35][S36][S39] |

**Synthetic profile. The different tax outcome comes with different risks:**
- **Counterparty risk.** SPXS depends on swap counterparties paying the index return. If a counterparty fails, the fund falls back on its own equity basket, "which could be lower than the index performance" [S30].
- **UCITS limit on that exposure.** Exposure to any one OTC counterparty is capped at **10% of assets** where the counterparty is a credit institution, 5% otherwise (Directive 2009/65/EC Art. 52(1)) [S37].
- **Invesco's controls.** Invesco says it uses up to six counterparties and periodically resets swaps to zero [S34].
- **Regulatory risk.** The 0% outcome rests on Treas. Reg. §1.871-15(l). Its "qualified index" test requires:
  - 25 or more components;
  - no component above 15% and the top five at 40% or less;
  - a dividend yield no higher than 1.5 times the S&P 500's;
  - listed futures or options on the index.

  Treasury can change these rules. The phase-in of wider §871(m) rules has been deferred several times; Notice 2024-44 excludes non-delta-one transactions issued before 1-Jan-2027 [S35][S36].
- **Headroom on concentration.** On 31-Aug-2026 the top S&P 500 weights were NVIDIA 7.93%, Apple 7.06%, Microsoft 5.74%, Amazon 3.92% and Alphabet A 3.06% [S28]. That is well inside the 15% and 40% limits, but it is worth monitoring.

### 4.3 S&P 500 dividend yield used

| Yield | As of | Source |
|---|---|---|
| **1.11%** (index dividend yield) — base case | 31-Aug-2026 | State Street SPY5 factsheet [S31] |
| 1.05% (estimate from trailing dividends through June 2026) | 24-Sep-2026 | multpl.com, secondary [S33] |
| 1.31% (VOO's 2025 distributions of USD 7.068 ÷ 31-Dec-2024 close of USD 538.81) | 2025 | Yahoo Finance, secondary [S69] |

### 4.4 Tax-drag arithmetic

Drag = dividend yield × withholding rate borne + fund cost. It is measured against the gross S&P 500 total return.

| Vehicle | Withholding borne | Withholding drag (1.11% × rate) | Fund cost | **All-in drag/yr** | USD/yr on 50k | on 80k | on 100k | US-situs? |
|:--|---:|---:|---:|---:|---:|---:|---:|:--:|
| VOO held directly by UAE resident | 30% | 0.333% | 0.03% | **0.363%** | 182 | 290 | 363 | **Yes** |
| CSPX (physical, Acc) | 15% | 0.167% | 0.07% | **0.236%** | 118 | 189 | 236 | No |
| VUAA (physical, Acc) | 15% | 0.167% | 0.07% | **0.236%** | 118 | 189 | 236 | No |
| SPY5 (physical, Dist) | 15% | 0.167% | 0.03% | **0.197%** | 98 | 157 | 197 | No |
| SPXS (synthetic, Acc) | ~0% | 0.000% | 0.05% + 0.07% swap | **0.120%** | 60 | 96 | 120 | No |

- **Fund-cost sources:** VOO 0.03% (a full-replication US ETF with USD 1,675bn fund assets, 30-Jun-2026) [S32]; CSPX [S28]; VUAA [S29]; SPY5 [S31]; SPXS [S30]. Withholding rates are from §2 and §4.2.
- **Sensitivity of the VOO–CSPX gap:**

  | Yield | Gap per year | Per year on USD 80k |
  |---|---:|---:|
  | 1.05% | 0.117% | USD 94 |
  | 1.11% | 0.127% | USD 101 |
  | 1.31% | 0.157% | USD 125 |

- **Modelling simplifications:**
  - VOO's expense ratio is paid out of income, so distributions run about 0.03% below the index yield. This overstates VOO's drag by about 0.01%.
  - Securities-lending income, tracking error and bid-ask spreads are ignored.
- **One-off trading costs** are small against these recurring drags (§5, §6.3).

### 4.5 Empirical cross-check: calendar-year 2025 total returns

| Vehicle | 2025 return | Basis | Source |
|---|---:|---|---|
| S&P 500 Net TR (30% withholding convention) | 17.43% | index | [S31][S30][S28] |
| CSPX | 17.58% | NAV | [S28] |
| VUAA | 17.58% | NAV | [S29] |
| SPY5 | 17.59% | NAV, net of fees | [S31] |
| SPXS | **17.75%** | NAV | [S30] |
| VOO, gross | 17.82% | market price, adjusted close | Yahoo [S69] (secondary) |
| VOO after 30% withholding on its 4 distributions (net amount reinvested) | **≈17.39%** | computed from the Yahoo data | [S69] + §2 |

For a UAE holder the 2025 ranking was SPXS > SPY5 ≈ CSPX = VUAA > VOO. That matches the model in §4.4: about 0.43 points of 30% withholding drag on VOO. Limitations: this is one year only, and it mixes NAV returns with a market-price return.

---

## 5. Brokers

### 5.1 Interactive Brokers (IBKR)

| Item | Fact | Source |
|---|---|---|
| UAE presence | IBKR opened a DIFC (Dubai) office on 16-Oct-2024. **Interactive Brokers (U.K.) Limited (DIFC Branch)** is regulated by the DFSA "to carry in and from the DIFC the financial services of Arranging Deals in Investments and Arranging Custody" (DIFC reg. no. CL8717). Head office: IB UK, FCA-authorised (FRN 208159). | [S47][S48] |
| Carrying entity | Depending on when and how the account was opened, a UAE-resident account may be carried by IB UK or by Interactive Brokers LLC (US). **Check your statement's header.** Neither changes the US estate situs of what you hold (§1.1). | [S48][S49][S70] |
| Protection | Interactive Brokers LLC is a SIPC member. For IB UK accounts: "IBUK custodies certain of your securities positions and cash with its US affiliate… To the extent that your securities and cash are custodied at IBLLC, they are protected by SIPC for a maximum coverage of $500,000 (with a cash sublimit of $250,000)", plus IBKR's excess-SIPC policy. The UK FSCS applies "only… in limited circumstances". Protection covers broker failure, not market losses. | [S49][S48][S56] |
| Access to LSE UCITS ETFs and US ETFs | IBKR blocks US ETFs (no PRIIPs KID) for **EEA and UK retail clients**. That rule is scoped by client residence and classification, so UAE residents are generally not caught. Secondary guides (Aug-2026) confirm UAE residents trading both CSPX/VUAA-type UCITS ETFs and US-listed ETFs. Trading permissions for "United Kingdom" stocks/ETFs must be enabled in the account. | IBKR PRIIPs FAQ [S50]; [S70] |
| US stocks/ETFs, IBKR Pro **Fixed** | **USD 0.005/share**, minimum **USD 1.00**/order, maximum **1% of trade value**. Regulatory fees are passed through: SEC fee USD 0.0000206 × sale value; FINRA TAF USD 0.000195 × shares sold. | [S43] |
| US stocks/ETFs, IBKR Pro **Tiered** | **USD 0.0035/share** for 300,000 shares/month or fewer (lower above that), minimum **USD 0.35**, maximum 1% of trade value, **plus** exchange, clearing (NSCC/DTC USD 0.0002/share), regulatory and pass-through fees | [S43] |
| IBKR Lite (USD 0 commissions) | Eligibility: "US Residents Only". **Not available to UAE residents.** | [S43] |
| LSE, **USD-denominated** lines (CSPX, VUAA, SPY5, SPXS) | **Fixed:** 0.05% of trade value, minimum **USD 4.00**, no maximum shown. **Tiered:** 0.05% (at EUR 50m/month or less), minimum USD 1.70, **maximum USD 39.00**, plus exchange/clearing fees. Direct-routed Fixed: 0.10%, minimum USD 6. | [S43] |
| LSE, **GBP-denominated** lines (CSP1, VUAG) | Fixed 0.05%, minimum GBP 3.00. Tiered 0.05%, minimum GBP 1.00. | [S43] |
| Fractional shares, US | "Fractional Shares on 10,500+ U.S. Stocks & ETFs", from USD 1. Commission is the same as for whole shares unless noted. | [S45][S43] |
| Fractional shares, Europe/UK | Available for "European stocks and ETFs listed on select exchanges, and with average daily volume above $5 million and market cap above $5 billion" (IBKR, 31-May-2022). IBKR's UK price table has fractional-order minimums. **Whether the CSPX/VUAA/SPXS/SPY5 LSE lines are fractional-eligible was not verified**; check the contract in TWS/Client Portal. At about USD 831 NAV/share (CSPX, 24-Sep-2026), whole-share rounding is a minor issue on USD 50–100k. | [S46][S43][S28] |
| FX | Spot FX commission **0.20 basis points × trade value** (at USD 1bn/month or less), **minimum USD 2.00** per order. **Auto-conversion** adds or subtracts about **0.03%** on the rate instead of a commission. | [S44] |
| Dividend withholding at IBKR | IBKR applies US law: 30% on US dividends for a UAE resident with W-8BEN (§2) | [S19][S21] |

### 5.2 Vested (Vested Finance / VF Securities)

| Item | Fact | Source |
|---|---|---|
| Legal structure | Vested Finance, Inc. is an SEC-registered investment adviser. **VF Securities, Inc.** is a FINRA/SIPC-member broker-dealer. "VF Securities, Inc can affect securities transactions for you through our clearing firm, **DriveWealth LLC**." BrokerCheck shows VF Securities introducing accounts to DriveWealth, LLC (CRD 165429) "on a fully disclosed basis". It does not itself hold customer funds or securities. | Form CRS (30-Apr-2025) [S53]; BrokerCheck [S54] |
| Instruments | "10,000+ US Stocks and ETFs" plus OTC securities. Fractional orders are filled by DriveWealth "from its own account on a Principal basis at the National Best Bid or Offer". **No LSE-listed UCITS ETFs.** Vested's "Global Funds" are UCITS **mutual funds**, mainly actively managed (BlackRock, Fidelity and others), offered under India's Liberalised Remittance Scheme. Whether UAE-resident NRIs can buy them was **not verified**. | [S51][S52][S55] |
| Fees (NRI pricing page) | Basic plan USD 0/month; Premium USD 4.99/month. Brokerage **0.25% of trade amount (max USD 35)** on Basic, 0.15% (max USD 35) on Premium. OTC trades 0.5% / 0.25%. Withdrawals in local currency are free above USD 100 (USD 3 below); USD withdrawals cost USD 5 each. The Form CRS also lists a USD 5 account-opening fee (sometimes waived), USD 5 per outgoing international wire charged by DriveWealth, and USD 65 for transfers to another US broker. | [S51][S53] |
| Extended hours | Pre-market 4:00–9:30 ET and after-hours 16:00–20:00 ET are offered. See §7 on the risks. | [S51][S60] |
| SIPC | Coverage up to **USD 500,000 including USD 250,000 cash**. "There is no requirement that a customer reside in or be a citizen of the United States." Shares lent under Vested's optional fully-paid lending programme are **not SIPC-covered while on loan**. Non-US-stock products on the site "are not FINRA regulated and not protected by the SIPC". | [S56][S53][S52] |
| Estate situs | Every US stock or US ETF held via Vested/DriveWealth is **US-situs**, just as at IBKR. Holdings at both brokers are **added together** against the USD 60k threshold. | [S5][S2] |
| Withholding | 30% on US dividends for a UAE resident, with no treaty (§2) | [S19][S17] |

---

## 6. Practical implications (general, illustrative, not advice)

### 6.1 Implications table

| # | Observation | Basis | Illustration |
|---|---|---|---|
| 1 | US-situs assets above **USD 60k** at death mean a Form 706-NA filing and potential tax at 26–40% marginal rates | [S2][S3][S4] | USD 80k gives USD 5,200 tax; USD 100k gives USD 10,800 |
| 2 | US-situs holdings **aggregate across brokers** (IBKR plus Vested plus any other) | [S5] | USD 45k of US stocks at IBKR + USD 25k of VOO at Vested = USD 70k, so USD 2,600 tax |
| 3 | Direct US dividend payers (stocks or US ETFs) carry **30%** withholding with no refund route for a UAE resident | [S19][S17] | USD 50k at a 1.11% yield pays USD 555 of dividends a year, of which USD 166.50 is withheld |
| 4 | Irish **physical** UCITS cut US withholding to **15% (fund level)** and are **not US-situs** | [S18][S7][S2] | About 0.167%/yr withholding drag vs 0.333% for VOO |
| 5 | Irish **synthetic** UCITS reach about **0%** US withholding under current §871(m) rules, in exchange for counterparty and regulatory risk | [S30][S35][S37] | About 0.12%/yr all-in (fees only) |
| 6 | **Single US-incorporated stocks cannot be held in a UCITS wrapper**, so a stock-picking sleeve of US companies is US-situs | [S5][S37] | A USD 70k stock sleeve gives a USD 2,600 exposure even if all index money is in UCITS |
| 7 | US-listed **foreign-incorporated** issuers and ADRs are generally **not US-situs** [S5][S15], and their dividends are not US-withheld [S19]. They are not tax-free: home-country withholding can apply, and **Irish-incorporated plcs may be Irish-situs property for Irish CAT**. Revenue's guidance says: "Property located in the State is liable to inheritance tax irrespective of the residence or ordinary residence of the disponer or the successor." Thresholds are EUR 400k/40k/20k depending on relationship, and the rate is 33%. The s.75 fund exemption does **not** cover operating companies. | [S40][S41][S39][S42] | EDGAR lists Ireland as the state of incorporation for LIN, ACN, TT, AON, JCI, WTW, STE, ALLE, SW, CRH, PNR; Switzerland for CB, GRMN, BG; Jersey for AMCR, APTV; Bermuda for EG, IVZ, NCLH; Netherlands for LYB [S42] |
| 8 | Keeping **US-situs value at or below USD 60k** keeps US estate tax at zero **at today's prices**. Growth erodes the headroom. | [S2][S4] | USD 50k at 7%/yr passes USD 60k in about 2.7 years |
| 9 | Accumulating vs distributing (UCITS) creates no US tax, and capital gains carry no US tax for an NRA (<183 days). The UAE has no personal income tax. | [S20][S24][S26] | Choosing between CSPX and SPY5 is about cost, cash-flow preference and tracking, not UAE/US tax |
| 10 | One-off LSE commission is about 0.05%; the difference in recurring drag is about 0.13%/yr | [S43] | USD 80k: about USD 39–40 once for CSPX at IBKR vs about USD 1 for VOO, against about USD 101/yr of extra drag for VOO |
| 11 | Estate administration friction exists **even below USD 60k**: the IRS transfer-certificate/affidavit process takes 12–18 months | [S14] | Relevant to heirs' access to US-custodied assets |
| 12 | **PTPs** (e.g., MLP units) trigger 10% withholding on **gross sale proceeds**. A member of a partnership engaged in a US trade or business "is considered to be engaged in a trade or business in the United States", so its share of profits is effectively connected income (ECI). That means withholding on distributions and a US return (1040-NR). | [S19][S20] | A USD 10k PTP sale has USD 1,000 withheld, whatever the gain. Holding PTPs can create a US filing obligation. |

### 6.2 Scenario grid

Assumptions:
- All individual stocks are US-incorporated.
- The stock sleeve yields the same as the index (1.11%). This is a placeholder; replace it with the real holdings' yields.
- There are no deductions or prior gifts, and values are those at death.
- For Irish UCITS rows, the withholding column is the fund-level 15% embedded in NAV.

Source: `outputs/r2_estate_tax_scenarios.csv`.

| Total | Stocks % | Index vehicle | US-situs | 706-NA? | Illustr. US estate tax | % of total | Annual US-dividend withholding | Index fund cost/yr |
|---:|---:|:--|---:|:--:|---:|---:|---:|---:|
| 50,000 | 0% | US ETF (VOO) | 50,000 | No | 0 | 0.0% | 166 | 15 |
| 50,000 | 0% | Irish UCITS (CSPX/VUAA) | 0 | No | 0 | 0.0% | 83 | 35 |
| 50,000 | 25% | US ETF | 50,000 | No | 0 | 0.0% | 166 | 11 |
| 50,000 | 25% | Irish UCITS | 12,500 | No | 0 | 0.0% | 104 | 26 |
| 50,000 | 50% | US ETF | 50,000 | No | 0 | 0.0% | 166 | 8 |
| 50,000 | 50% | Irish UCITS | 25,000 | No | 0 | 0.0% | 125 | 18 |
| 50,000 | 75% | US ETF | 50,000 | No | 0 | 0.0% | 166 | 4 |
| 50,000 | 75% | Irish UCITS | 37,500 | No | 0 | 0.0% | 146 | 9 |
| 50,000 | 100% | none | 50,000 | No | 0 | 0.0% | 166 | 0 |
| 100,000 | 0% | US ETF (VOO) | 100,000 | **Yes** | **10,800** | 10.8% | 333 | 30 |
| 100,000 | 0% | Irish UCITS | 0 | No | 0 | 0.0% | 166 | 70 |
| 100,000 | 25% | US ETF | 100,000 | **Yes** | **10,800** | 10.8% | 333 | 22 |
| 100,000 | 25% | Irish UCITS | 25,000 | No | 0 | 0.0% | 208 | 52 |
| 100,000 | 50% | US ETF | 100,000 | **Yes** | **10,800** | 10.8% | 333 | 15 |
| 100,000 | 50% | Irish UCITS | 50,000 | No | 0 | 0.0% | 250 | 35 |
| 100,000 | 75% | US ETF | 100,000 | **Yes** | **10,800** | 10.8% | 333 | 8 |
| 100,000 | 75% | Irish UCITS | 75,000 | **Yes** | **3,900** | 3.9% | 291 | 18 |
| 100,000 | 100% | none | 100,000 | **Yes** | **10,800** | 10.8% | 333 | 0 |

How to read the grid:
- **At USD 50k total**, no split creates a filing obligation at today's values. The UCITS choice still roughly halves the index sleeve's withholding cost and leaves headroom for growth.
- **At USD 100k**, the index vehicle decides the outcome:
  - With VOO, every split is about USD 10.8k exposed.
  - With UCITS, the exposure is zero up to about a 60% US-stock sleeve.
  - With a 75% stock sleeve, the exposure is USD 3,900.

### 6.3 One-off cost examples (list prices only)

Figures exclude bid-ask spreads and venue fees.

| Order size | IBKR Fixed, US ETF | IBKR LSE USD line, Fixed / Tiered | Vested Basic | IBKR FX conversion (IdealPro vs auto) |
|---:|---:|---:|---:|---:|
| 50,000 | ~1.00 | 25.00 / 25.00 | 35.00 | 2.00 vs ~15 |
| 80,000 | ~1.00 | 40.00 / 39.00 | 35.00 | 2.00 vs ~24 |
| 100,000 | ~1.00 | 50.00 / 39.00 | 35.00 | 2.00 vs ~30 |

The ~USD 1 US figure is the USD 1.00 minimum. For VOO priced above USD 500 (it closed 2025 at USD 627 [S69]), USD 0.005/share × shares is below USD 1 for orders up to USD 100k, so the minimum applies. The FX column matters only when converting AED or another currency; funds already held in USD need no conversion [S43][S44][S51].

---

## 7. Order-execution education (generic)

### 7.1 Order types (SEC / Investor.gov)

- **Market order:** executes promptly but "does not guarantee the execution price". The price "often deviates from the last-traded price or 'real time' quote", and a large order can fill at several prices [S57][S59].
- **Limit order:** "can only be executed at the limit price or lower" for a buy, or "at the limit price or higher" for a sell. The price is protected, but the order may not fill [S57][S59].
- **Stop (stop-loss) order:** "When the stop price is reached, a stop order becomes a market order."
  - "The stop price is not the guaranteed execution price… The execution price… can deviate significantly from the stop price."
  - A stop can be "triggered by a short-term, intraday price move" that fills "substantially worse than the stock's closing price for the day".
  - Firms differ on whether they trigger on last sale or on quotes [S58].
- **Stop-limit order:** controls the price, but "may not be executed if the stock's price moves away from the specified limit price" [S58].
- **Gap risk:** if news comes out overnight and a stock opens beyond your stop, the triggered market order fills at whatever is available. That can be far from the stop. This follows directly from [S58] together with [S60].
- **Fund issuer tips** (State Street): "Always use a limit order". "Try to trade when the underlying market is also trading", which for LSE-listed S&P 500 UCITS ETFs means the US session. "Try to avoid trading in the first and last 10 minutes of the trading day" [S67].

### 7.2 Earnings dates and extended hours

- US regular trading hours are **9:30 a.m.–4:00 p.m. ET** [S60].
- "Companies may announce important news or financial information outside of regular trading hours." Such news can cause "significant price changes… during extended hours trading" [S60].
- The SEC lists these extended-hours risks [S60]:
  - lack of liquidity;
  - higher volatility;
  - "Uncertain Prices" (extended-hours prices may not match the next open);
  - unlinked markets;
  - wider quote spreads.
- Practical implications for this investor:
  - An earnings release is a common source of the overnight gaps that make stop orders fill far away.
  - Some platforms (e.g., Vested) offer 4:00–20:00 ET extended sessions [S51]. The SEC risks above apply to them.

### 7.3 Trading hours in Dubai time (GST = UTC+4, no daylight saving [S66])

Inputs:
- **US session:** NYSE/Nasdaq regular session, 09:30–16:00 ET [S60].
- **LSE session:** Main Market, 08:00–16:30 UK time. LSEG's 21-Jul-2026 release says: "Trading will continue on the London Stock Exchange's Main Market between 08:00 and 16:30." The separate "LSE 24" venue (17:00–07:50) is planned for H1-2027, starting with ETPs [S63].
- **US daylight saving:** starts the second Sunday of March and ends the first Sunday of November [S65]. In 2026 that is 8-Mar to 1-Nov.
- **UK summer time (BST):** 29-Mar to 25-Oct-2026; 28-Mar to 31-Oct-2027 [S64].

| Period (trading days) | NYSE/Nasdaq (GST) | LSE (GST) | Overlap (GST) |
|---|---|---|---|
| 9-Mar – 27-Mar-2026 (US EDT, UK GMT) | 17:30–24:00 | 12:00–20:30 | 17:30–20:30 |
| 30-Mar – 23-Oct-2026 (EDT, BST), **includes today** | **17:30–24:00** | **11:00–19:30** | **17:30–19:30** |
| 26-Oct – 30-Oct-2026 (EDT, GMT) | 17:30–24:00 | 12:00–20:30 | 17:30–20:30 |
| 2-Nov-2026 – 12-Mar-2027 (EST, GMT) | 18:30–01:00 (next day) | 12:00–20:30 | 18:30–20:30 |

In summer time, an after-close US earnings release (after 16:00 ET) arrives **after midnight GST**. A pre-market release arrives before 17:30 GST.

### 7.4 Settlement

- **US:** T+1 for most broker-dealer transactions in stocks and ETFs since **28-May-2024** [S61].
- **UK:** "currently operates on a T+2 (2-day) settlement cycle". UK markets move to **T+1 on 11-Oct-2027** (FCA page updated 13-Aug-2026) [S62]. LSE trades in UCITS ETFs therefore settle T+2 today.

---

## 8. Method, validation checks, limitations, files

**What I did:**
- Pulled primary texts:
  - US statutes and regulations (IRC §§2001, 2101–2106, 2501, 6075; Treas. Reg. §§20.2105-1, 1.871-15), IRS publications, instructions and pages;
  - the UAE Cabinet Decision and FTA guide;
  - Irish Revenue manuals;
  - fund-issuer factsheets;
  - broker pricing and disclosure pages;
  - SEC investor bulletins, FCA and LSEG pages.
- Recomputed all arithmetic in `code/r2_implementation_calcs.py`.
- Raw downloads are cached in `C:\Users\user\eqv4\cache\r2\` (not synced).

**Validation checks. All passed; 0 failed:**
1. **§2001(c) schedule continuity:** each bracket's base equals the previous bracket's base plus its rate × width (11/11 boundaries).
2. **Credit calibration:** tentative tax on USD 60,000 is exactly USD 13,000, so the net tax is 0.
3. **Worked examples:** USD 80k gives USD 5,200 and USD 100k gives USD 10,800. These are asserted in code.
4. **UAE treaty absence (3/3 IRS sources agree):** A-to-Z income-treaty list (03-Jan-2026), Table 3 (through 26-Sep-2025) and the estate/gift treaty list (08-Sep-2026).
5. **Fund cost cross-check (3/3):** issuer factsheet TERs match secondary listings (justETF/search snippets) for VUAA 0.07%, SPY5 0.03% and SPXS 0.05%. CSPX's 0.07% comes from the issuer factsheet only.
6. **Yield triangulation:** 1.11% (issuer factsheet), 1.05% (multpl) and 1.31% (VOO 2025 distributions) are mutually consistent. Sensitivity is reported.
7. **Empirical check:** the 2025 return ordering matches the drag model (§4.5).
8. **UAE personal income tax:** the government portal and PwC (09-Sep-2026) agree. The one contrary news item is dead (404).
9. **EDGAR incorporation check:** 28 tickers queried; 21 returned a non-US state of incorporation. The 7 blanks were not used.

**Limitations:**
- All tax figures are illustrative:
  - no deductions or credits beyond USD 13k;
  - values taken at death;
  - FX peg assumed.
- Broker prices are list prices from public pages. Individual account terms may differ.
- The VOO 2025 check uses market prices from Yahoo, a secondary source.
- IBKR pages were parsed from HTML. Confirm commission caps in the platform.

**Files produced:**

| File | Rows × columns | Contents |
|---|---|---|
| `v4/outputs/r2_implementation_facts.md` | — | This report |
| `v4/outputs/r2_estate_tax_scenarios.csv` (+ `.meta.json`) | 18 × 11 | §6.2 grid |
| `v4/outputs/r2_tax_drag.csv` (+ `.meta.json`) | 15 × 12 | 5 vehicles × 3 yield assumptions |
| `v4/code/r2_implementation_calcs.py` | — | Script that reproduces all tables in §1.3, §4.4, §6.2 and §6.3 |
| `v4/outputs/r2_report.md` | — | Output-contract pointer to this file |

---

## 9. Facts not verified / open items (confirm before relying)

1. **UCITS fractional eligibility at IBKR.** Whether the CSPX, VUAA, SPY5 or SPXS LSE lines are fractional-eligible; only IBKR's general criteria were found [S46].
2. **IBKR carrying entity and restrictions.** Which IBKR entity carries this investor's account, and whether a DIFC-onboarded (IB UK) account has any product restrictions beyond the EEA/UK PRIIPs scope. The IBKR FAQ text was seen only via search snippet; the page itself is a JavaScript application [S50].
3. **IBKR LSE Fixed cap.** The "no maximum" on IBKR Fixed for LSE USD lines comes from HTML table parsing [S43].
4. **Vested for UAE residents.** Whether Vested currently onboards new UAE residents, and whether "Global Funds" (UCITS) are open to UAE-resident NRIs.
5. **Estate situs of cash at US brokers.** How uninvested cash held at a US broker-dealer (IB LLC, DriveWealth) is treated. The bank-deposit exemption (§2105(b)(1)) covers deposits with banks, not necessarily broker free-credit balances. **Unresolved; ask an adviser.**
6. **Irish plcs traded in the US.** Irish CAT treatment of US-listed Irish plcs held through DTC (where the shares are "located"), and home-country dividend withholding (Irish DWT, Swiss WHT) for UAE residents on foreign-incorporated US listings. Not researched in detail.
7. **Other taxes on UCITS ETFs.** Whether UK stamp duty/SDRT or UK inheritance tax could apply to Irish-domiciled ETFs merely because they are listed on the LSE. Believed not to, but not verified here.
8. **LSE auctions.** Exact LSE auction times (about 07:50–08:00 opening and 16:30–16:35 closing, from secondary snippets). Only the 08:00–16:30 continuous session was confirmed from LSEG [S63].
9. **§871(m) durability.** Whether the "qualified index" exception lasts. It is regulatory and can change; SPXS's advantage depends on it [S35][S36].
10. **S&P 500 yield source.** An official S&P DJI dividend-yield figure was not retrieved directly. I used the fund issuer's "Index Dividend Yield" (1.11%) [S31].
11. **ADR situs.** The IRS position is a non-precedential PLR [S15].
12. **Other countries' taxes.** Rules for a person who is also a citizen or tax resident of another country (e.g., on moving back to a home country) are out of scope. Foreign-fund rules there may differ materially.

---

## 10. Sources

All retrieved 2026-09-26 UTC. Page dates are given where the page shows one.

| # | Source | URL |
|---|---|---|
| S1 | IRS, "Some nonresidents with U.S. assets must file estate tax returns" (updated 27-Jun-2026) | https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns |
| S2 | IRS, Instructions for Form 706-NA (Rev. 09/2025) | https://www.irs.gov/instructions/i706na |
| S3 | 26 U.S.C. §2001 (rate schedule), Cornell LII | https://www.law.cornell.edu/uscode/text/26/2001 |
| S4 | 26 U.S.C. §2102 (credit), Cornell LII | https://www.law.cornell.edu/uscode/text/26/2102 |
| S5 | 26 U.S.C. §2104 (stock situs), Cornell LII | https://www.law.cornell.edu/uscode/text/26/2104 |
| S6 | 26 U.S.C. §2105 (property without the US; RIC rule sunset), Cornell LII | https://www.law.cornell.edu/uscode/text/26/2105 |
| S7 | 26 CFR §20.2105-1 (foreign-corporation stock), Cornell LII | https://www.law.cornell.edu/cfr/text/26/20.2105-1 |
| S8 | 26 U.S.C. §2101 | https://www.law.cornell.edu/uscode/text/26/2101 |
| S9 | 26 U.S.C. §2106 | https://www.law.cornell.edu/uscode/text/26/2106 |
| S10 | 26 U.S.C. §2501 | https://www.law.cornell.edu/uscode/text/26/2501 |
| S11 | 26 U.S.C. §6075 | https://www.law.cornell.edu/uscode/text/26/6075 |
| S12 | IRS, "Estate & gift tax treaties (international)" (updated 08-Sep-2026) | https://www.irs.gov/businesses/small-businesses-self-employed/estate-gift-tax-treaties-international |
| S13 | IRS, FAQ on estate taxes for nonresidents not citizens (updated 20-Sep-2026) | https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes-for-nonresidents-not-citizens-of-the-united-states |
| S14 | IRS, Transfer certificate filing requirements for nonresident non-citizen estates (updated 05-May-2026) | https://www.irs.gov/businesses/small-businesses-self-employed/transfer-certificate-filing-requirements-for-the-estates-of-nonresidents-not-citizens-of-the-united-states |
| S15 | IRS PLR 200243031 (released 25-Oct-2002) | https://www.irs.gov/pub/irs-wd/0243031.pdf |
| S16 | IRS, "Estate tax for nonresidents not citizens of the United States" (updated 28-Jun-2026) | https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax-for-nonresidents-not-citizens-of-the-united-states |
| S17 | IRS, "United States income tax treaties – A to Z" (updated 03-Jan-2026) | https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z |
| S18 | IRS Tax Treaty Table 1 (Rev. May 2023); Table 3 (updated through 26-Sep-2025); tables page (updated 23-Feb-2026) | https://www.irs.gov/pub/irs-lbi/tax-treaty-table-1.pdf ; https://www.irs.gov/pub/irs-lbi/table-3-list-of-tax-treaties.pdf ; https://www.irs.gov/individuals/international-taxpayers/tax-treaty-tables |
| S19 | IRS Publication 515 (2026) | https://www.irs.gov/publications/p515 |
| S20 | IRS Publication 519 (for 2025 returns) | https://www.irs.gov/publications/p519 |
| S21 | IRS, Instructions for Form W-8BEN (Rev. Oct 2021) | https://www.irs.gov/instructions/iw8ben |
| S22 | IRS, Backup withholding (updated 28-Jun-2026) | https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding |
| S23 | IRS, Ireland tax treaty documents (updated 08-Aug-2026) | https://www.irs.gov/businesses/international-businesses/ireland-tax-treaty-documents |
| S24 | UAE Government portal, "Taxation" (no page date) | https://u.ae/en/information-and-services/finance-and-investment/taxation |
| S25 | PwC Worldwide Tax Summaries, UAE individual (last reviewed 09-Sep-2026) | https://taxsummaries.pwc.com/united-arab-emirates/individual/taxes-on-personal-income |
| S26 | UAE MoF, Cabinet Decision No. 49 of 2023 (8-May-2023; effective 1-Jun-2023) | https://mof.gov.ae/wp-content/uploads/2023/05/Cabinet-Decision-No.-49-of-2023.pdf |
| S27 | FTA, Corporate Tax Guide "Taxation of Natural Persons" CTGTNP1 (Nov 2023) | https://tax.gov.ae/Datafolder/Files/Guides/CT/Taxation%20of%20natural%20persons%20-%2025%2011%202023.pdf |
| S28 | iShares CSPX factsheet (Aug 2026; data 31-Aug-2026) | https://www.ishares.com/uk/individual/en/literature/fact-sheet/cspx-ishares-core-s-p-500-ucits-etf-fund-fact-sheet-en-gb.pdf |
| S29 | Vanguard VUAA factsheet (31-Jul-2026) | https://fund-docs.vanguard.com/SandP_500_UCITS_ETF_USD_Accumulating_9694_INT_OFF_ETF_EN.pdf |
| S30 | Invesco SPXS factsheet (31-Aug-2026) | https://www.invesco.com/content/dam/invesco/emea/en/product-documents/etf/share-class/factsheet/IE00B3YCGJ38_factsheet_en.pdf |
| S31 | State Street SPY5 factsheet (31-Aug-2026) | https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-spy5-gy.pdf |
| S32 | Vanguard VOO factsheet (30-Jun-2026): expense ratio 0.03%, fund net assets USD 1,675,038m | https://fund-docs.vanguard.com/F0968.pdf |
| S33 | multpl.com, S&P 500 dividend yield (24-Sep-2026; secondary) | https://www.multpl.com/s-p-500-dividend-yield |
| S34 | Invesco, "Does synthetic replication offer an advantage?" | https://www.invesco.com/nl/en/insights/does-synthetic-replication-offer-an-advantage.html |
| S35 | 26 CFR §1.871-15 (para. (l) qualified index), Cornell LII | https://www.law.cornell.edu/cfr/text/26/1.871-15 |
| S36 | IRS Notice 2024-44 (22-May-2024) | https://www.irs.gov/pub/irs-drop/n-24-44.pdf |
| S37 | Directive 2009/65/EC (UCITS), Arts. 52–53, EUR-Lex | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009L0065 |
| S38 | Irish Revenue, Tax and Duty Manual Part 27-01A-02 "Investment Undertakings" (last updated Jan 2026) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-27/27-01a-02.pdf |
| S39 | Irish Revenue, CAT Notes for Guidance Part 9 (s.75), as amended to Finance Act 2024 | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/cat/2024/part09.pdf |
| S40 | Irish Revenue, CAT Notes for Guidance Part 3 (s.11) | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/cat/2024/part03.pdf |
| S41 | Irish Revenue, CAT group thresholds (published 24-Sep-2025; thresholds from 2-Oct-2024) | https://www.revenue.ie/en/gains-gifts-and-inheritance/cat-thresholds-rates-and-aggregation-rules/cat-thresholds.aspx |
| S42 | SEC EDGAR submissions API, `stateOfIncorporation` (queried 2026-09-26) | https://data.sec.gov/submissions/ (e.g., CIK0001707925.json for Linde plc) |
| S43 | IBKR, Commissions – Stocks, ETFs (US and UK tables) | https://www.interactivebrokers.com/en/pricing/commissions-stocks.php |
| S44 | IBKR, Commissions – Spot currencies | https://www.interactivebrokers.com/en/pricing/commissions-spot-currencies.php |
| S45 | IBKR, Fractional trading | https://www.interactivebrokers.com/en/trading/fractional-trading.php |
| S46 | IBKR press release, European fractional shares (31-May-2022) | https://www.interactivebrokers.com/en/general/about/mediaRelations/6-1-22-frac-shares.php |
| S47 | IBKR press release, DIFC office (16-Oct-2024) | https://www.interactivebrokers.com/en/general/about/mediaRelations/10-16-24.php |
| S48 | IB UK, DIFC Branch page | https://www.interactivebrokers.co.uk/en/general/about/difc-branch.php |
| S49 | IB UK, Client Protection page | https://www.interactivebrokers.co.uk/en/general/security-investor-protection.php |
| S50 | IBKR Knowledge Base, "FAQ: PRIIPs regulation" (redirects to a JavaScript FAQ app; content via search snippet) | https://www.ibkrguides.com/kb/en-us/article-2993.htm |
| S51 | Vested, Pricing (NRIs) | https://vestedfinance.com/pricing/ |
| S52 | Vested, Homepage and disclosures | https://vestedfinance.com/ |
| S53 | Vested IA & BD Form CRS (30-Apr-2025) | https://files.brokercheck.finra.org/crs_315194.pdf |
| S54 | FINRA BrokerCheck report, VF Securities (CRD 315194) | https://files.brokercheck.finra.org/firm/firm_315194.pdf |
| S55 | Vested blog, "Global Funds" launch (31-Oct-2025) | https://vestedfinance.com/blog/vested-updates/a-new-chapter-in-global-investing-global-funds-by-vested/ |
| S56 | SIPC, "What SIPC Protects" | https://www.sipc.org/for-investors/what-sipc-protects |
| S57 | Investor.gov, "Types of Orders" | https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders |
| S58 | Investor.gov, "Stop, Stop-Limit, and Trailing Stop Orders – Investor Bulletin" (13-Jul-2017; updated 18-Aug-2026) | https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15 |
| S59 | Investor.gov, "Understanding Order Types – Investor Bulletin" (12-Jul-2017; updated 18-Aug-2026) | https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14 |
| S60 | Investor.gov, "Extended-Hours Trading: Investor Bulletin" (06-Jun-2022) | https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-42 |
| S61 | Investor.gov, "New 'T+1' Settlement Cycle – What Investors Need To Know" (27-Mar-2024) | https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin |
| S62 | FCA, "About T+1 settlement" (updated 13-Aug-2026) | https://www.fca.org.uk/markets/about-t1-settlement |
| S63 | LSEG press release, "London Stock Exchange to launch LSE 24" (21-Jul-2026) | https://www.lseg.com/en/media-centre/press-releases/2026/london-stock-exchange-to-launch-lse-24 |
| S64 | GOV.UK, "When do the clocks change?" | https://www.gov.uk/when-do-the-clocks-change |
| S65 | 15 U.S.C. §260a (US daylight saving time), Cornell LII | https://www.law.cornell.edu/uscode/text/15/260a |
| S66 | timeanddate.com, Time zones in UAE (GST UTC+4, no DST; secondary) | https://www.timeanddate.com/time/zone/united-arab-emirates |
| S67 | State Street, "Top tips for trading ETFs" | https://www.ssga.com/au/en_gb/intermediary/insights/education/best-practices-when-trading-etfs |
| S68 | CBUAE, FX rates June 2026 (USD = AED 3.6725 on 01-Jun-2026) | https://centralbank.ae/media/dlcdkjd2/fx_jun26_en.pdf |
| S69 | Yahoo Finance via yfinance, VOO daily history 2024-12-20 to 2026-01-05 (secondary; cached `eqv4\cache\r2\voo_2025_hist.csv`) | https://finance.yahoo.com/quote/VOO/history |
| S70 | vested.blog, "IBKR UAE Account Setup (2026)" (Aug-2026; secondary) | https://vested.blog/posts/ibkr-uae-account-setup-guide |
| S71 | IRS news release IR-2025-103, 2026 inflation adjustments incl. OBBB amendments (09-Oct-2025) | https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill |
