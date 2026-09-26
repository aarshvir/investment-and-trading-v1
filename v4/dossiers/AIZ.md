# Assurant, Inc. (NYSE: AIZ) — Fundamental Diligence Dossier (Agent f2)

**Analysis date:** 2026-09-26
**Basis:** Consolidated, US GAAP, all figures in USD $ millions unless stated otherwise.
**Latest reported period:** Q2 2026 10-Q, period ended 2026-06-30, filed 2026-08-06 [accession 0001267238-26-000041].
**Price reference:** $265.00, NYSE close 2026-09-25 [source: v4/data/d4_live_snapshot.parquet, retrieved 2026-09-25T20:25Z] · Market cap $13,070.8M

---

## RECENCY STATEMENT
Most recent reported period incorporated: Q2 2026 (quarter ended 2026-06-30), published 2026-08-06 [10-Q, accession 0001267238-26-000041; earnings 8-K Ex-99.1, accession 0001267238-26-000039, filed 2026-08-04].
Events checked through: 2026-09-25.
Material events since period end: none found in SEC filings (no 8-Ks filed between 2026-08-06 and 2026-09-25 per EDGAR submissions feed, checked 2026-09-26).
Any invalidation trigger already tripped at time of writing: no.

## DATA QUALITY NOTE
| Item | Statement |
|---|---|
| Primary sources | FY2025 10-K filed 2026-02-19 (accession 0001267238-26-000010); Q1 2026 10-Q filed 2026-05-07; Q2 2026 10-Q filed 2026-08-06; Q3 2025 10-Q filed 2025-11-06; 8-K Ex-99.1 earnings releases dated 2024-02-06 through 2026-08-04; SEC XBRL companyfacts API |
| Secondary/cross-check sources | v4 internal quant pipeline (lead_prelim_rank.csv, d4_live_snapshot.parquet — itself SEC-XBRL/Yahoo-derived); used only as a labeled cross-check, never as the sole source for a headline figure. Independently re-derived and confirmed exact: pipeline TTM revenue $13,456.2M, TTM net income $1,063.5M, TTM OCF $1,870.7M, total assets, equity and cash all match filed figures to the dollar (see §12 methodology note) |
| As-of dates | Filings through 2026-08-06; price/market data 2026-09-25 close; SEC EDGAR pulled 2026-09-26 |
| Consolidated vs standalone | Consolidated |
| Currency and units | USD $ millions unless stated (per-share figures in USD) |
| What is estimated | Q4 2024 and Q4 2025 revenue/net income are derived as FY-minus-9M (standard subtraction, not separately reported); FY2025 "combined-ratio-equivalent" for Global Housing is an analyst calculation (Assurant does not disclose a formal combined ratio); "sustainable operating ROE" in §7 is an analyst estimate range, not a company figure; reverse-DCF implied growth in §7 is valuation.py's mechanical output on an FCF proxy, explicitly labeled illustrative-only per sector convention |
| What is missing | Numeric NAIC RBC ratio (not disclosed in SEC filings — only qualitative "expect to exceed minimum" + A.M. Best "A" rating); exact quarterly capex split (only an annual, tier-4 estimate available); opening-of-2025 Global Housing reserve balance (only year-end 2025 net outstanding liability of $733.4M isolated, so PYD-as-%-of-opening-reserves is not computed); current precise P/B and operating ROE for peers HIG/KMPR/ORI beyond what web search surfaced (FMP statements/quote endpoints gated) |

---

## 1. Verdict
**INCLUDE-SMALL** — A genuinely improving specialty-insurance franchise (Connected Living volume growth, disciplined Global Housing underwriting, shrinking share count, rising holding-company liquidity) trading at a full-but-not-extreme valuation, with a real, company-disclosed EPS deceleration mechanism baked into H2 2026 that the market may not fully be pricing given persistent price-target raises. **Thesis horizon:** 12–24 months.

## 2. The Business
Assurant is a specialty insurance holding company operating two segments. **Global Lifestyle** (77.5% of FY2025 net earned premiums, fees and other income of $9,582.5M [FY2025 10-K, Global Lifestyle segment table, filed 2026-02-19]) sells mobile device protection/trade-in, extended service contracts, and credit/financial-services insurance through mobile carriers and retailers ("Connected Living," $5,378.7M FY2025, +11.9% YoY), plus vehicle and commercial-equipment protection ("Global Automotive," $4,203.8M FY2025, +1.1% YoY) [FY2025 10-K, filed 2026-02-19]. **Global Housing** (22.5% of segment revenue, $2,768.8M FY2025 [FY2025 10-K]) underwrites lender-placed homeowners/flood/manufactured-home insurance plus renters and specialty products — genuine catastrophe-exposed underwriting risk. Global Lifestyle is best analyzed as a capital-light, fee/administration-heavy business with a real but secondary loss-ratio component (its own Adjusted EBITDA margin is only ~8% of revenue [FY2025 10-K] because commissions to carrier/retail partners and cost of trade-in inventory dominate the cost base); Global Housing is the true underwriting business where combined-ratio-style economics and catastrophe exposure matter most. Assurant simplified its portfolio further in FY2025-26: a legacy run-off subsidiary holding fully-reinsured individual life, annuity and long-term-care blocks (reinsured to John Hancock) was classified held-for-sale in Q4 2025 and sold in March 2026 for an $11.2M cumulative loss on sale [FY2025 10-K Note 3; Q2 2026 10-Q Note 4, filed 2026-08-06] — following the larger 2021 Global Preneed divestiture to CUNA Mutual ($1.35B) [company press release, 2021-08-02, pre-dating this dossier's window but relevant context].

## 3. Why the Model Likes It
The 0.80 composite is driven by Quality (0.859) and Momentum (0.834) percentiles, with Value (0.711) more modest [lead_prelim_rank.csv]. Momentum is evidenced, not manufactured: revenue grew every quarter for the last six at +6.7% to +11.3% YoY [derived from 10-K/10-Q XBRL, see §4], adjusted EPS ex-catastrophes grew double-digits, and guidance has been raised three times in the last four releases with the raises subsequently validated by actuals (§5) — this looks like a genuine re-rating on improving fundamentals rather than a hot run into an air pocket, **except** that the improvement in Global Housing profitability (Adjusted EBITDA +28% FY2025 [FY2025 10-K]) is partly a function of $113.1M of favorable prior-year reserve development (PYD) in 2025 on top of $106.7M in 2024 [FY2025 10-K MD&A, filed 2026-02-19] — a two-year tailwind management itself says will not repeat in H2 2026 (§4, §6). Quality (ROE ~15.9% on a full-year-average-equity GAAP basis, rising from 13.4% FY2023 [ratios.py output on 10-K data]; OCF/NI of 2.10x FY2025) is real but partly inflated by that same reserve-development windfall and by two years of below-average catastrophe losses. Value at the 71st percentile is driven by a trailing P/E of ~13x-15x, not by a discount to book — on a P/B basis (~2.15x) the stock is fully valued for its current ROE (§7). **Net read: momentum and quality are directionally real (Connected Living growth, buybacks, improving underwriting discipline) but a meaningful share of the last two years' earnings beats rode a fading reserve-development tailwind, not a permanent step-change in loss experience.**

## 4. Last Two Years of Results
Revenue, GAAP EPS and Assurant's own non-GAAP "Adjusted EPS" figures below are all company-reported (8-K Ex-99.1 exhibits); Q4 2024 and Q4 2025 revenue/net income are derived as FY-minus-9M (labeled). "Net margin" substitutes for operating margin, which is undefined for an insurer (see insurance.md; OPM/EBITDA-margin suppressed).

| Quarter | Revenue ($M) | YoY% | Net margin (GAAP) | GAAP EPS (dil.) | Adj. EPS (incl. cat) | Adj. EPS (ex-cat) | OCF ($M) |
|---|---|---|---|---|---|---|---|
| Q3 2024 | 2,967.7 | — | 4.5% | $2.55 | $3.00 | $5.08 | n/a — not isolated |
| Q4 2024 (derived) | 3,104.8 | — | 6.5% | $3.87 | $4.79 | $5.54 | n/a — not isolated |
| Q1 2025 | 3,074.0 | +6.7% | 4.8% | $2.83 | $3.39 | $5.79 | 392.4 |
| Q2 2025 | 3,158.4 | +8.0% | 7.4% | $4.56 | $5.10 | $5.56 | 265.5 |
| Q3 2025 | 3,231.5 | +8.9% | 8.2% | $5.17 | $5.73 | $5.76 | 505.0 |
| Q4 2025 (derived) | 3,350.4 | +7.9% | 6.7% | $4.41 | $5.61 | $5.75 | 671.0 |
| Q1 2026 | 3,420.1 | +11.3% | 8.0% | $5.41 | $5.95 | $6.33 | 240.3 |
| Q2 2026 | 3,454.2 | +9.4% | 8.6% | $5.95 | $6.41 | $6.60 | 454.4 |

[All figures: respective quarter's 8-K Ex-99.1 press release non-GAAP reconciliation table and consolidated statements, and XBRL companyfacts for revenue/NI/OCF; Q1 2025 hit by ~$3.03/share pre-tax of California wildfire catastrophes, per 8-K filed 2025-01-23 and Q1 2025 10-Q.]

Growth has been accelerating (Q1 2026's +11.3% is the fastest of the eight quarters), driven by Connected Living and lender-placed Homeowners growth in Global Housing. **Resolving the H2-2026-EPS-decline tension:** the quant brief's "consensus $4.52 vs $5.73 a year ago" for Q3 2026 compares to Assurant's own non-GAAP "Adjusted earnings per diluted share" (incl.-cat) of exactly $5.73 for Q3 2025 [Q3 2025 8-K, filed 2025-11-04] — **confirmed non-GAAP, not GAAP** (GAAP diluted EPS for Q3 2025 was $5.17). The mechanism is a disclosed, deliberate guidance assumption: FY2026 guidance "does not contemplate prior year reserve development (PYD) in second half 2026" [Q2 2026 8-K, filed 2026-08-04], while H2 2025 benefited from real favorable PYD (Q3 2025: $27.6M prior-years-related; Q4 2025: $22.1M [Q3/Q4 2025 8-Ks]) plus a $27.5M unfavorable non-run-rate premium-earnings-pattern adjustment booked in Q3 2024 that flattered the Q3-2025-over-Q3-2024 comp [Q3 2024 8-K, filed 2024-11-05]. This is a comp/guidance-conservatism effect, not disclosed evidence of business deterioration — but it is a real headwind to the *reported* growth rate, not merely a modeling artifact.

## 5. Guidance Track Record
| Release (date) | Metric | Prior guidance | New guidance | Verdict |
|---|---|---|---|---|
| Q2 2025 (2025-08-05) | FY2025 Adj. EPS ex-cat / Adj. EBITDA ex-cat | (Q1 2025 guide not separately captured) | "Approaching 10%" growth / "mid-to-high single digits" growth | — |
| Q3 2025 (2025-11-04) | FY2025 Adj. EPS ex-cat / Adj. EBITDA ex-cat | "Approaching 10%" / "mid-to-high single digits" | "Low double-digit growth" / "approaching 10% growth" | **RAISED** |
| Q4/FY2025 (2026-02-10) | FY2025 actual vs. guide | "Low double-digit" EPS growth guided | Actual: $22.81 ex-cat EPS vs $20.35 FY2024 = **+12.1%** (within "low double-digit" band) | **DELIVERED** |
| Q4/FY2025 (2026-02-10) | FY2026 initial guide | n/a (first FY2026 guide) | Adj. EBITDA/EPS ex-cat "consistent with 2025 levels," or "mid-to-high single digits" excluding $113.1M FY2025 PYD | — |
| Q1 2026 (2026-05-05) | FY2026 Adj. EPS/EBITDA ex-cat (headline / ex-PYD) | "Consistent with 2025 levels" / "mid-to-high single digits" ex-PYD | "Low single digits" / "high single digits" ex-PYD (PYD comp footnote shrunk to $94M) | **RAISED** |
| Q2 2026 (2026-08-04) | FY2026 Adj. EPS/EBITDA ex-cat (headline / ex-PYD) | "Low single digits" / "high single digits" ex-PYD | "Mid single digits" / "approximately 10%" ex-PYD (PYD comp footnote now $71M; explicitly assumes zero H2 2026 PYD) | **RAISED** |

[All guidance figures quoted verbatim or paraphrased directly from the "Company Outlook" tables/footnotes of the cited 8-K Ex-99.1 press releases.] Three consecutive raises with one prior full-year cycle actually delivered in-band is a credible, evidenced pattern — not asserted without checking the prior range, per this project's data-integrity standard.

## 6. Earnings Quality & Balance Sheet
**FCF conversion:** OCF/NI = 2.10x FY2025 ($1,833.9M / $872.7M [FY2025 10-K]), up from 1.75x FY2024 — insurers' OCF is inflated by float timing and is not directly distributable (see §7 caveat); the more relevant "free cash" concept is **holding-company liquidity**, which rose from $613M (9/30/25) → $887.4M (12/31/25) → $836M (3/31/26) → $911.5M (6/30/26), all comfortably above the $225M internal minimum [respective 8-K/10-Q Liquidity sections]. **SBC:** not separately isolated within budget; "other adjustments" in the GAAP-to-adjusted EPS bridge are small (≤$0.11/share most quarters). **GAAP-vs-adjusted gap drivers (FY2025, per diluted share):** net realized investment losses ($1.39), intangible amortization ($1.31), restructuring ($0.53, mostly a new Q4 2025 efficiency plan), a $0.21 loss on the LTC subsidiary held-for-sale, tax effects (–$0.71), then reportable catastrophes ($3.85 pre-tax, –$0.81 tax) to reach $22.81 ex-cat from $16.93 GAAP [Q4 2025 8-K reconciliation table, filed 2026-02-10]. **Capital adequacy:** the FY2025 10-K discloses only qualitatively that insurance subsidiaries "expect to exceed minimum RBC requirements" and that all rated subsidiaries carry an A.M. Best "A" (Excellent) rating [FY2025 10-K, filed 2026-02-19] — **no numeric consolidated RBC ratio is disclosed in SEC filings** (n/a — would require state NAIC statutory filings). **Financial leverage** (debt/(debt+equity), carrying value): 27.3% at FY2025-end ($2,206.9M/$8,078.5M), improving to 26.6% at Q2 2026-end ($2,208.1M/$8,306.0M) [10-K Note 18; Q2 2026 10-Q], both comfortably inside the credit facility's 35% maximum covenant [FY2025 10-K, filed 2026-02-19] and within the sector-playbook comfort zone. **Debt maturities:** no maturities until March 2028 ($300M) and February 2030 ($350M) after Assurant refinanced the February-2026 notes early via a $300M 5.55% 2036 issuance in August 2025 [FY2025 10-K, Note 18]. **Buybacks:** repurchased 1.4M shares for $299.9M in FY2025 plus $168.4M dividends; Board authorized an additional $700M program in November 2025 (on top of the November 2023 $600M program), leaving $774.6M unused at 12/31/2025 [FY2025 10-K, Item 5 and Note 18]; diluted share count fell from 53.78M (FY2023) to 49.38M (Q2 2026), roughly –8% [XBRL].

## 7. Valuation Snapshot
**Primary method (P/B vs. sustainable operating ROE), per insurance.md.** Current P/B ≈ 2.15x ($265.00 price / $123.48 book value per share, using Q2 2026 equity $6,097.9M ÷ 49.382M shares [Q2 2026 10-Q] — this exactly matches the quant pipeline's independently-computed $123.48 book value/share and 2.146x P/B [d4_live_snapshot.parquet], a clean cross-check). GAAP ROE on a full-year-average-equity basis was 15.9% in FY2025, up from 15.3% (FY2024) and 13.4% (FY2023) [ratios.py output on 10-K data]. Stripping catastrophes and the FY2025 PYD windfall from net income (adjusted-ex-cat EPS $22.81 × 51.09M diluted shares ≈ $1,165M, less ~$89M after-tax PYD benefit, over average equity of $5,489M) implies a **"cleaned" sustainable operating ROE of roughly 17-20%** (analyst estimate, not company-reported). Applying the justified-multiple relation P/B ≈ (ROE − g)/(COE − g) with a conservative g=4% and a sector-typical COE=10% (insurance.md's own P&C benchmark, chosen over a mechanical CAPM figure because AIZ's trailing beta of 0.542 [d4_live_snapshot.parquet] likely understates true cost of equity given catastrophe tail risk): ROE=18% implies P/B≈2.33x; ROE=16% implies P/B≈2.00x; ROE=17% implies P/B≈2.17x — i.e., **the current 2.15x multiple is roughly what a mid-to-high-teens sustainable ROE justifies; the stock is not obviously cheap on this framework**, though it sits at the low end of the 2-4x band the playbook associates with 15-18% ROE/sub-95%-combined-ratio franchises. **Secondary (P/E on operating EPS):** trailing P/E on FY2025 adjusted-ex-cat EPS ($22.81) is 11.6x; on GAAP EPS ($16.93, TTM $20.94) it is ~15.7x/12.7x — below the 10-16x diversified-P&C band's midpoint, consistent with the Value factor score. **Peers:** The Hartford (HIG) trades at ~1.90x P/B against an ~18.7-20.3% TTM core ROE [gurufocus/company 8-K via web search, 2026-09]; Old Republic (ORI) trades at ~9.0x P/E [AAII, 2026-09-11]; Kemper (KMPR) is currently loss-making (negative TTM ROE) [CNBC/company data, 2026-09-17] and is not a clean comparator right now. AIZ's niche (lender-placed/warranty) has few exact pure-plays, as expected. **Suppressed and why:** EV/EBITDA, EV/Sales and a raw FCF-yield DCF are explicitly not used as primary evidence per insurance.md (debt is not financing against a policyholder-liability balance sheet). Illustratively, valuation.py's reverse-DCF on an OCF-minus-capex FCF proxy ($1,618.8M) against the EV bridge ($13,595.6M) implies the market is pricing in **only –5.8% FCF growth for 10 years at a 10% WACC** — a nonsensical-looking output that itself demonstrates why the sector playbook bans this method here: this year's OCF is flattered by float timing and the same reserve-release dynamic discussed in §4, not a repeatable distributable-cash base.

## 8. Bull Case and Bear Case
### Bull case
1. Global Lifestyle's Connected Living unit grew net earned premiums+fees +11.9% in FY2025 on real mobile-subscriber and financial-services-program growth, not pricing/assumption changes [FY2025 10-K].
2. Balance sheet has gotten safer, not riskier, while returning capital: financial leverage improved from ~29.0% (FY2024) to ~26.6% (Q2 2026), holding-company liquidity nearly doubled from $613M (Q3 2025) to $911.5M (Q2 2026), and the Board added a fresh $700M buyback authorization in November 2025 [FY2025 10-K; Q2 2026 10-Q].
3. Management has been transparent, not evasive, about the H2 2026 reserve-development comp headwind, disclosing the exact dollar mechanics three quarters running — a credibility signal, not a red flag, and the underlying (ex-PYD, ex-cat) FY2026 guide of "approximately 10%" growth as of August 2026 has only been raised, never cut, in the last four releases [Q1/Q2 2026, Q3/Q4 2025 8-Ks].

### Bear case
1. Two consecutive years of unusually large favorable prior-year reserve development ($106.7M FY2024, $113.1M FY2025, both in Global Housing) inflated reported and adjusted EPS; management guides essentially zero incremental PYD for H2 2026, so the "8-for-8 beat, 8-for-8 raise" pattern investors have priced in may not mechanically continue on the *reported* line even if the ex-PYD business is healthy [FY2025 10-K MD&A; Q2 2026 8-K].
2. Global Housing remains genuinely catastrophe-exposed (Hurricane Helene alone cost $92M pre-tax in Q3 2024); FY2025's much lower cat impact ($198.8M vs $245.2M pre-tax) partly reflects a milder hurricane year, not a structural improvement, and can reverse [FY2025 10-K; special 8-Ks, 2024].
3. At ~2.15x P/B against an analyst-estimated 17-20% "cleaned" sustainable ROE and a 10% cost of equity, the stock is priced for continued high-teens returns with little margin of safety; analyst sentiment is already fully bought-in (8 of 8 recent price-target actions were raises, strong-buy consensus, zero downgrades in 90 days per d4_live_snapshot.parquet), leaving asymmetric downside if H2 2026 prints disappoint even modestly relative to the now-elevated bar.

## 9. Key Risks & Kill Criteria — What Would Invalidate This Thesis
1. Global Housing's analyst-computed combined-ratio-equivalent (policyholder benefits + expenses, over net earned premium — see §3/§7 methodology) rises above ~85% for two consecutive quarters (vs. ~79.4% FY2025), signaling the underwriting improvement was reserve-driven, not structural.
2. FY2026 adjusted-EPS-ex-cat guidance is **cut** (not merely decelerated on the already-disclosed PYD comp) at the Q3 2026 (on/around 2026-11-03) or Q4 2026 (~Feb 2027) release versus the August-2026 raised range ("mid single digits" headline / "approximately 10%" ex-PYD).
3. Holding-company liquidity falls back below ~$500M without a clearly disclosed one-off cause (vs. $836-911.5M over the last two quarters).
4. A single reportable-catastrophe quarter exceeds roughly $150M pre-tax in Global Housing (worse than Q3 2024's Hurricane-Helene-driven $138M) with evidence of reinsurance-recoverable strain or a materially higher retention.
5. Financial leverage (debt/total capital, carrying value) rises above ~32% (approaching the 35% covenant) via debt-funded buybacks/M&A, or any rated insurance subsidiary is downgraded from A.M. Best "A."

## 10. Catalysts & Calendar
Next earnings: Q3 2026, estimated 2026-11-03 [d4_live_snapshot.parquet estimate] — **not yet confirmed by the company** in any filing checked (no 8-K scheduling notice found as of 2026-09-25). Watch specifically for: (a) whether Q3 2026 Global Housing results show the guided zero-PYD assumption holding, (b) any update to the "approximately 10%" ex-PYD FY2026 guide, (c) hurricane-season catastrophe pre-announcements (Assurant has issued mid-quarter cat 8-Ks in each of the last several third/fourth quarters, e.g. 2024-07-15, 2024-10-16, 2025-01-23). No investor day or index-event catalyst identified in the filings reviewed.

## 11. Red-Flag Scan
**Auditor:** PricewaterhouseCoopers LLP; unqualified opinion on financial statements and on internal control over financial reporting as of 12/31/2025; no changes to ICFR during Q4 2025 that materially affected it [FY2025 10-K, Item 9A]. **Material weakness / restatement / going concern:** none found — searched the FY2025 10-K text for these terms and for "SEC investigation" / "Department of Justice"; no matches. **Legal proceedings:** Note 26 states only ordinary-course litigation with an established accrual, and management does not believe pending matters are likely to have a material adverse effect [FY2025 10-K, Note 26]. **Insider selling:** checked recent Form 4s via SEC EDGAR/web search — CEO and CFO dispositions in March 2026 were tax-withholding on PSU/RSU vesting (not discretionary open-market sales), one EVP sold under a Rule 10b5-1 plan in June 2026, another sold a small block in August 2026, and the CEO made a charitable gift of shares in September 2026; no cluster of large opportunistic discretionary selling found. **Short-seller reports:** none found in web search. **Other:** the company disclosed a small real-estate rationalization (Miami campus sale agreement, $126M, and two Global Housing operations centers sold/marketed) — immaterial to the thesis but noted for completeness [FY2025 10-K, Item 2].

## 12. Sources
1. SEC EDGAR submissions API, CIK 0001267238: https://data.sec.gov/submissions/CIK0001267238.json (retrieved 2026-09-26)
2. SEC EDGAR XBRL companyfacts API, CIK 0001267238: https://data.sec.gov/api/xbrl/companyfacts/CIK0001267238.json (retrieved 2026-09-26)
3. FY2025 10-K (filed 2026-02-19): https://www.sec.gov/Archives/edgar/data/1267238/000126723826000010/aiz-20251231.htm
4. Q1 2026 10-Q (filed 2026-05-07): https://www.sec.gov/Archives/edgar/data/1267238/000126723826000027/aiz-20260331.htm
5. Q2 2026 10-Q (filed 2026-08-06): https://www.sec.gov/Archives/edgar/data/1267238/000126723826000041/aiz-20260630.htm
6. Q3 2025 10-Q (filed 2025-11-06): https://www.sec.gov/Archives/edgar/data/1267238/000126723825000051/aiz-20250930.htm
7. Q2 2026 earnings 8-K Ex-99.1 (filed 2026-08-04): https://www.sec.gov/Archives/edgar/data/1267238/000126723826000039/aiz-20260630exx991pressrel.htm
8. Q1 2026 earnings 8-K Ex-99.1 (filed 2026-05-05): https://www.sec.gov/Archives/edgar/data/1267238/000126723826000024/aiz-20260331exx991pressrel.htm
9. Q4/FY2025 earnings 8-K Ex-99.1 (filed 2026-02-10): https://www.sec.gov/Archives/edgar/data/1267238/000126723826000006/aiz-20251231exx991pressrel.htm
10. Q3 2025 earnings 8-K Ex-99.1 (filed 2025-11-04): https://www.sec.gov/Archives/edgar/data/1267238/000126723825000049/aiz-20250930exx991pressrel.htm
11. Q2 2025 earnings 8-K Ex-99.1 (filed 2025-08-05): https://www.sec.gov/Archives/edgar/data/1267238/000126723825000042/aiz-20250630exx991pressrel.htm
12. Q1 2025 earnings 8-K Ex-99.1 (filed 2025-05-06): https://www.sec.gov/Archives/edgar/data/1267238/000126723825000024/aiz-20250331exx991pressrel.htm
13. Q4/FY2024 earnings 8-K Ex-99.1 (filed 2025-02-11): https://www.sec.gov/Archives/edgar/data/1267238/000126723825000005/aiz-20241231exx991pressrel.htm
14. Q3 2024 earnings 8-K Ex-99.1 (filed 2024-11-05): https://www.sec.gov/Archives/edgar/data/1267238/000126723824000044/aiz-20240930exx991pressrel.htm
15. Special 8-K, catastrophe pre-announcement (filed 2024-07-15): https://www.sec.gov/Archives/edgar/data/1267238/000126723824000033/aiz-20240715.htm
16. Special 8-K, catastrophe pre-announcement (filed 2024-10-16): https://www.sec.gov/Archives/edgar/data/1267238/000126723824000042/aiz-20241016.htm
17. Special 8-K, Miami campus sale + catastrophe pre-announcement (filed 2025-01-23): https://www.sec.gov/Archives/edgar/data/1267238/000126723825000002/aiz-20250122.htm
18. v4/data/d4_live_snapshot.parquet (Yahoo-sourced quant snapshot), retrieved 2026-09-25T20:25Z
19. v4/outputs/lead_prelim_rank.csv (internal factor pipeline), accessed 2026-09-26
20. WebSearch: Assurant Q3 2025 earnings, adjusted EPS confirmation — gurufocus.com, tradingview.com (accessed 2026-09-26)
21. WebSearch: Assurant Q2 2026 earnings call, PYD guidance color — investing.com transcript, gurufocus.com (accessed 2026-09-26)
22. WebSearch: Assurant Global Preneed divestiture (2021, background context) — finance.yahoo.com, nasdaq.com (accessed 2026-09-26)
23. WebSearch: Assurant insider Form 4 activity 2026 — SEC EDGAR ownership filings via web search (accessed 2026-09-26)
24. WebSearch: Hartford Financial (HIG) P/B and core ROE — gurufocus.com Book Value per Share page, BigGo Finance Q2 2026 earnings summary (accessed 2026-09-26)
25. WebSearch: Kemper (KMPR) and Old Republic (ORI) valuation — AAII investing ideas, CNBC quote page (accessed 2026-09-26)

---

## Disclaimer
This dossier is prepared for internal portfolio-construction research and diligence. It is not investment advice, not a recommendation to buy, sell, or hold any security, and not a personalised financial recommendation. Figures are drawn from public filings and estimates as cited; transcription or interpretation errors are possible. Not a licensed or registered investment adviser opinion. Any investment decision is the reader's own responsibility.
