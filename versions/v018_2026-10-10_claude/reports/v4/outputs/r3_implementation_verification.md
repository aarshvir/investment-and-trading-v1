# R3: Implementation and tax facts verification (Loop-1 follow-up)

- **Agent:** r3 (implementation and tax facts verifier)
- **Purpose:** Independently re-verify the seven load-bearing questions the Loop-1 auditor flagged against `r2_implementation_facts.md` §9 (open items), using primary sources where possible, with a fresh access date. **r2 was not edited.**
- **Access date for all sources below:** 2026-09-26 (UTC/UAE local, same day).
- **Scope:** General factual verification only. Not personalised tax, legal or investment advice. No accounts were opened, no forms were submitted, no logins were attempted.
- **Time box:** ~45 minutes of research; some secondary sub-items remain flagged "not independently verified this pass" rather than guessed.

---

## Q1. Which IBKR entity opens accounts for UAE residents, and which investor-protection scheme applies?

**Answer:** UAE residents onboard through **Interactive Brokers (U.K.) Limited (DIFC Branch)**, which operates under a **DFSA Category 4 licence** ("Arranging Deals in Investments" and "Arranging Custody" — an arranging broker, not itself the custodian). Per IBKR's own disclosure: the DIFC Branch "services its clients in and from DIFC by arranging access to brokerage and custody services delivered by or through its head office — Interactive Brokers (U.K.) Limited," which is FCA-authorised (FRN 208159, England & Wales). Under the IBUK/IBLLC client-agreement structure, IBUK receives orders while **Interactive Brokers LLC (US, regulated by the SEC/CFTC)** actually holds client money and securities in custody and executes/clears trades. Consequently, the investor-protection scheme that actually applies is **SIPC** (Interactive Brokers LLC is a SIPC member, $500,000 cover / $250,000 cash sublimit), **not** the UK FSCS. IBKR's own page states this directly: "Interactive Brokers LLC is regulated by the US SEC and CFTC and is a member of the SIPC... compensation scheme; products are only covered by the UK FSCS in limited circumstances."

- **Confidence:** High (core chain — DIFC Branch → IB UK → IB LLC/SIPC — is quoted verbatim from IBKR's own current disclosure page).
- **Sources:** https://www.interactivebrokers.co.uk/en/general/about/difc-branch.php (fetched 2026-09-26); https://www.sipc.org/for-investors/what-sipc-protects.
- **Changed vs r2:** r2 flagged this as open item §9.2 ("check your statement's header"). This pass **resolves it with primary-source language**: the DIFC Branch is confirmed as an arranging broker under a **Category 4 DFSA licence** (a more specific detail than r2's registration number CL8717), and the protection scheme is confirmed as SIPC (via IBLLC custody), with FSCS explicitly limited. No contradiction of r2's substance — this sharpens it.

---

## Q2. Does Vested currently onboard new UAE residents? Which UAE-regulated platforms offer US stocks and LSE UCITS ETFs, and under which regulator?

**Answer:**
- **Vested:** Vested's own support materials and independent 2026 guides converge on: Vested's core onboarding is **NRI/Indian-origin-gated** — it requires a PAN card (Indian tax ID) regardless of current residence, not general UAE residency. Independent guides (Aug–Sep 2026) state Vested "does not onboard customers with a UAE residential address and no Indian bank account." A Vested community-support reply (Jun 2026) confirms *existing* customers can update their tax residency to UAE, which is different from *new* non-Indian-origin UAE residents being able to sign up. **Net: a UAE resident who is not of Indian origin cannot open a Vested account; a UAE-resident NRI/PIO with a PAN generally can.** This is a real gate the client should confirm against his own passport/PAN status.
- **Sarwa:** confirmed directly from Sarwa's own help centre: "Sarwa Trade is regulated by the ADGM Financial Services Regulatory Authority" — legal entity **Sarwa Digital Wealth (Capital) Limited**, FSRA Category 3C licence (retail client + holding/controlling client investments endorsement). Offers 5,000+ US stocks/ETFs. **No confirmation found that Sarwa offers LSE-listed UCITS ETFs** (its own marketing describes US stocks/ETFs/options/crypto only) — flag as unresolved.
- **Saxo:** UAE-facing entity is "**Saxo Bank A/S, DIFC Representative Office**," regulated by the DFSA **as a Representative Office** (plus a separate CBUAE representative-office registration) — per Saxo's own UAE disclaimer page. A representative office cannot itself hold client money or provide regulated financial services in the UAE; it markets the Saxo Bank A/S platform, so the actual custodial/regulatory relationship sits with Saxo Bank A/S (Denmark) or another Saxo licensed entity depending on onboarding flow. **Which exact entity carries a UAE client's account, and whether CSPX/VUAA specifically are tradeable, was not independently confirmed** in the time available — Saxo's general ETF universe is broad, but this is not the same as confirming the two specific tickers.
- **Emirates NBD Securities L.L.C.:** licensed under number 604003 by the **Capital Market Authority (CMA)** — see regulator-name change below — but its core brokerage brand is focused on DFM/ADX/Nasdaq Dubai/GCC exchanges. The bank's separate **"ENBD X"** digital-wealth platform advertises ~11,000 global equities across ~21 markets including NYSE/Nasdaq/LSE, but the direct product page returned 404 today and **I could not confirm from a primary source whether LSE-listed UCITS ETFs (CSPX/VUAA) are specifically tradeable there, nor which regulatory licence covers that specific offering** — flag as unresolved, needs a direct check (e.g. in-app instrument search or a call to ENBD).
- **Regulator name change (new finding, not in r2):** The **Securities and Commodities Authority (SCA) was reconstituted as the Capital Market Authority (CMA) effective 1 January 2026**, under UAE Federal Laws No. 32 and No. 33 of 2025; CMA is SCA's direct legal successor for all existing licences/contracts. Materials referring to "SCA" for UAE mainland brokers (e.g. Emirates NBD Securities) should now say **SCA/CMA**.
- **Confidence:** High for Sarwa/FSRA and the SCA→CMA rename (both from primary/official-adjacent sources); Medium for Vested's onboarding gate (convergent secondary sources, no single definitive Vested legal statement found); Medium-Low for Saxo's exact carrying entity and for ENBD X's ETF coverage/regulatory scope (both flagged open).
- **Sources:** https://help.sarwa.co/hc/en-us/articles/4407336316305-Is-Sarwa-regulated (fetched 2026-09-26); https://www.home.saxo/en-mena/legal/disclaimer/disclaimer-uae (fetched 2026-09-26); https://vested.blog/posts/us-stock-platforms-for-indians-in-uae; https://uaeinform.com/personal-finance-guide/investing-uae-residents; https://support.vestedfinance.com/portal/en/kb/articles/what-is-the-process-for-a-nri-to-invest-in-us-stocks-via-vested; https://community.vestedfinance.com/t/uae-tax-residency-changes/14323 (fetched 2026-09-26); https://www.tamimi.com/news/uae-capital-market-regulatory-overhaul-key-changes-from-1-january-2026/; https://www.dechert.com/knowledge/onpoint/2026/2/from-sca-to-cma---more-than-just-a-rebrand.html; https://en.wikipedia.org/wiki/Capital_Market_Authority_(United_Arab_Emirates).
- **Changed vs r2:** r2 covered only IBKR and Vested; **Sarwa, Saxo and Emirates NBD Securities were entirely out of scope in r2** — this is new ground, not a correction. The SCA→CMA rename is a genuinely new 2026 fact not in r2 at all. Vested's onboarding gate is now characterised more precisely (PAN/NRI-gated, not simply "UAE residency status unknown" as r2's open item §9.4 left it) — still not fully resolved to "high confidence," but meaningfully narrowed.

---

## Q3. CSPX and VUAA fund facts

**Answer:** Reconfirmed directly from iShares' own product page today: **CSPX** (iShares Core S&P 500 UCITS ETF), ISIN **IE00B5BMR087**, domicile **Ireland**, issuer iShares VII plc, **TER 0.07%**, **Accumulating**, **Physical replication**, base/share-class currency **USD**, UCITS-compliant, listed on LSE as **CSPX** (USD) and **CSP1** (GBP) among 10 global listings, fund net assets **≈USD 159.3bn** (25-Sep-2026, up slightly from r2's 31-Aug figure — normal AUM drift). **VUAA** (Vanguard S&P 500 UCITS ETF, ISIN IE00BFMXXD54) was **not independently re-fetched this pass** (time constraint); r2's citation is Vanguard's own factsheet dated 31-Jul-2026 (Ireland domicile, TER 0.07%, Accumulating, Physical, USD base) and no contrary evidence was found. Fund-level US dividend withholding of 15% under the US–Ireland tax treaty (IRS Table 1) was not re-derived today but is standard, uncontested treaty law consistent with r2.
- **Confidence:** High for CSPX (freshly reconfirmed); Medium-High for VUAA (relying on r2's recent primary source).
- **Sources:** https://www.ishares.com/uk/individual/en/products/253743/ishares-sp-500-b-ucits-etf-acc-fund (fetched 2026-09-26); carried from r2: https://fund-docs.vanguard.com/SandP_500_UCITS_ETF_USD_Accumulating_9694_INT_OFF_ETF_EN.pdf; https://www.irs.gov/pub/irs-lbi/tax-treaty-table-1.pdf.
- **Changed vs r2:** No material change. TER, domicile, structure, currency all match r2 exactly.

---

## Q4. US estate tax for a non-resident non-citizen

**Answer:** Reconfirmed directly from the current **IRS Instructions for Form 706-NA (Rev. 09/2025)** today: **"In general, the maximum unified credit is $13,000"**, and the filing threshold is stated verbatim as **"the filing threshold of $60,000."** This matches r2's §1 exactly, and confirms the core exemption figure and the §2001(c) rate schedule (18%–40%) are unchanged. Situs sub-rules — (a) US-listed stock and US-domiciled ETFs (US-situs, IRC §2104(a), §2105(d) look-through repealed for deaths after 2011); (b) Irish UCITS funds (not US-situs, foreign-corporation stock, Treas. Reg. §20.2105-1(f)); (c) directly held T-bills (not US-situs — short-term OID and/or portfolio-interest exemption, IRC §2105(b)); (d) US T-bill/money-market ETFs (US-situs, same RIC rule as (a)); (e) cash at a US broker (**still unresolved** — the bank-deposit exemption in §2105(b)(1) covers bank deposits, not necessarily broker free-credit balances, and I did not find new authority resolving this in the time available) — were **not independently re-fetched from the raw statutory text this pass**; r2's citations are primary (Cornell LII full IRC/Treas. Reg. text) and internally validated (r2's own arithmetic checks), and no contrary evidence was found.
- **Confidence:** High for the core $60k/$13k figures and rate schedule (freshly reconfirmed); Medium-High for situs sub-rules (a)–(d) (carried from r2's primary citations, unchanged); item (e) remains genuinely open — flag for an adviser, as r2 already said.
- **Sources:** https://www.irs.gov/instructions/i706na (fetched 2026-09-26); carried from r2: https://www.law.cornell.edu/uscode/text/26/2104; https://www.law.cornell.edu/uscode/text/26/2105; https://www.law.cornell.edu/cfr/text/26/20.2105-1.
- **Changed vs r2:** No change to any figure. (e) cash-at-broker situs remains an open item in both r2 and this pass — not newly resolved.

---

## Q5. US dividend withholding for UAE residents: 30% and W-8BEN

**Answer:** Reconfirmed today from the **IRS "United States income tax treaties" page** (page last reviewed **03-Jan-2026**): the UAE is **not listed** among treaty countries (countries near "U" are Ukraine, USSR, United Kingdom, "United States Model," Uzbekistan — no UAE). Reconfirmed today from the **IRS Instructions for Form W-8BEN**: **"a Form W-8BEN will remain in effect for purposes of establishing foreign status for a period starting on the date the form is signed and ending on the last day of the third succeeding calendar year"** — the 3-year validity rule, quoted verbatim, matching r2 exactly. The underlying 30% statutory withholding rate (IRS Pub 515/519) was not re-fetched this pass but is uncontested, well-established tax law already primary-sourced in r2.
- **Confidence:** High (both central facts freshly reconfirmed today from primary IRS pages).
- **Sources:** https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z (fetched 2026-09-26, "Page Last Reviewed or Updated: 03-Jan-2026"); https://www.irs.gov/instructions/iw8ben (fetched 2026-09-26); carried from r2: https://www.irs.gov/publications/p515.
- **Changed vs r2:** No change. Independently reconfirmed with a fresh access date and updated page-review date (03-Jan-2026, vs r2's citation which used the same page).

---

## Q6. UAE personal tax on dividends and capital gains as of 2026

**Answer:** No change found. Cabinet Decision No. 49 of 2023's carve-out of **"Personal Investment" income** from UAE Corporate Tax for natural persons — "regardless of the amount of Turnover" — remains in force for 2026 per multiple independent 2026-dated tax-advisory commentaries (ClearTax, Westgate Dubai, Qaspro Global, Kayrouz & Associates), all describing **0% personal income tax, no capital-gains tax, and no dividend-withholding tax** for individuals investing personally (not through a licensed business). I attempted to fetch the FTA's own natural-persons Corporate Tax page directly today but it returned only navigation content, not the substantive guide text, within the time available — so today's confirmation rests on secondary 2026 commentary rather than a freshly-quoted primary source; r2's own citations (the Cabinet Decision PDF itself, and FTA Guide CTGTNP1 Example 11) are primary and were not contradicted by anything found today.
- **Confidence:** High (r2's primary citations stand unchallenged; multiple independent 2026 secondary sources corroborate no change).
- **Sources:** carried from r2: https://mof.gov.ae/wp-content/uploads/2023/05/Cabinet-Decision-No.-49-of-2023.pdf; https://tax.gov.ae/Datafolder/Files/Guides/CT/Taxation%20of%20natural%20persons%20-%2025%2011%202023.pdf; new 2026 corroboration (secondary): https://www.cleartax.com/ae/uae-corporate-tax-faqs; https://qasproglobal.com/uae-capital-gains-tax-2026/.
- **Changed vs r2:** No change.

---

## Q7. IBKR costs relevant to a small account

**Answer:** Reconfirmed directly from IBKR's live commissions page today:
- **US stocks/ETFs:** Tiered **USD 0.0035/share** (≤300,000 shares/month, then lower), Fixed **USD 0.005/share**, minimum **USD 1.00/order**, capped at **1% of trade value** (IBKR's own worked example confirms the $1 minimum and 1% cap mechanics) — matches r2 exactly.
- **LSE, USD-denominated lines** (where CSPX/VUAA/SPY5/SPXS trade): **Tiered** 0.05% of trade value, minimum **USD 1.70**, maximum **USD 39.00**; **Fixed–SmartRouting** 0.05%, minimum **USD 4.00**, no maximum; **Fixed–Direct-Routing** 0.10%, minimum **USD 6.00**, no maximum. Matches r2 verbatim, reconfirmed from the live fee table.
- **Fractional shares:** New evidence (not in r2): IBKR's current UK-USD fee table itself defines fractional-share pricing at the market-segment level — "Fractional Shares | Tiered Pricing | 0.05% of Trade Value," same USD 1.70 minimum — and a separate US-market note states fractional trades carry the same commission as whole shares, minimum **USD 0.01**. This **advances but does not fully resolve** r2 §9 item #1: the fee mechanism for fractional LSE-USD trading clearly exists in the current schedule, but **per-ticker eligibility for CSPX/VUAA/SPY5/SPXS specifically was still not confirmed** (that lives in the platform's contract-level flags, not the public fee page).
- **Inactivity fee:** Confirmed via multiple 2026 broker-comparison sources that IBKR **abolished inactivity fees firm-wide effective 1 July 2021**, and this remains the case in 2026 — no minimum-activity or account-maintenance fee for retail accounts.
- **Market-data fees:** **Not independently verified this pass.** IBKR's market-data pricing page was too large to fully parse in the time available, and I could not extract a specific current fee figure for a non-professional individual's US or UK Level I data subscription. I am **not asserting a number without a source** — this remains open for a follow-up read of https://www.interactivebrokers.com/en/pricing/market-data-pricing.php.
- **Confidence:** High for commission tables, fractional-share mechanism, and no-inactivity-fee (all freshly reconfirmed from IBKR's own live pages/secondary corroboration); Low/not verified for exact market-data fee amounts.
- **Sources:** https://www.interactivebrokers.com/en/pricing/commissions-stocks.php (fetched 2026-09-26); https://brokerchooser.com/invest-long-term/costs/inactivity-fee-interactive-brokers (secondary, 2026).
- **Changed vs r2:** No change to commission figures. New: fractional-share fee mechanism confirmed to exist for UK-USD listings generally (partial progress on open item #1); explicit confirmation of no inactivity fee (r2 did not address this). Market-data fees remain unverified in both r2 and this pass.

---

## Resolution status vs r2 §9 open items (the ones this task's 7 questions bear on)

| r2 §9 item | Status after this pass |
|---|---|
| #1 UCITS fractional eligibility at IBKR | **Partially resolved** — fee mechanism confirmed for UK-USD listings; per-ticker eligibility still open |
| #2 IBKR carrying entity / DIFC restrictions | **Resolved** — DIFC Branch (Cat. 4 DFSA) → IB UK (FCA) → IB LLC (SIPC); FSCS only in limited circumstances |
| #3 IBKR LSE Fixed cap "no maximum" | **Reconfirmed unchanged** (verified against live fee table) |
| #4 Vested onboarding for UAE residents | **Partially resolved** — gated by Indian PAN/NRI status, not general UAE residency; no single definitive Vested legal statement found |
| #5 Estate situs of broker cash | **Still unresolved** — not investigated further this pass; still "ask an adviser" |
| #6–#12 (Irish plcs, UK stamp duty, LSE auctions, §871(m) durability, yield source, ADR situs, other countries) | **Out of scope for this pass** (not among the 7 assigned questions) |

## Files produced
- `v4/outputs/r3_implementation_verification.md` — this report
- `v4/outputs/r3_implementation_verification.json` — machine-readable answers (q1–q7: answer, confidence, sources, verified, changed_vs_r2)

## Known limitations of this verification pass
- Several sites blocked automated fetches (HTTP 403 on interactivebrokers.com/co.uk via WebFetch, worked around via firecrawl scrape); some pages (Saxo product list, ENBD X global-equities page, IBKR market-data pricing) could not be fully parsed or returned 404 in the time available.
- Saxo's precise UAE-facing carrying entity, Emirates NBD's ENBD X regulatory scope and LSE-UCITS-ETF availability, IBKR market-data fees, and broker free-credit-balance estate situs remain genuinely open — flagged rather than guessed.
- This is general factual research, not personalised tax/legal/investment advice; confirm anything material with a qualified cross-border adviser before acting.
