## 1. Verdict

**You asked for an all-stock portfolio of 5–20 US companies, researched across the whole S&P 500, with no index fund or T-bills for now. The answer is the 20 stocks in §6.**

- **How they were chosen.** Every S&P 500 company got at least a quick research pass. So far 313 of the strongest, including the eight largest AI and cloud companies, have been researched in full from SEC filings. Another 24 passed the quick pass and are queued for full research, so a later round may still displace some holdings. The 20 held are the best of the 200 that passed every test: 20 at full conviction, together 100% of the portfolio (TJX, WEC, STE, MA, USB, BALL, DOV, EXC, ADP, CAH, BR, MCK, PGR, AXP, HBAN, CRH, LVS, PTC, VEEV, GDDY), and 0 at half conviction.
- **What is excluded, and why.** Great companies whose price already assumes more growth than the evidence supports stay out, including Microsoft, Alphabet, Amazon, Meta, NVIDIA and Apple. §6 names every eligible stock not held and every top-45 name that failed, with the reason.
- **Honest odds.** In the base-case market (6% a year), with no assumed stock-picking edge: a 79% chance of a gain over 5 years, a 50% chance of beating the S&P 500, and a 84% chance of a fall worse than 20% at some point along the way.
- **In past crises** (today's holdings on daily prices): −48% in 2007–09 (S&P 500 −55%); −37% in the 2020 COVID crash (−34%); −15% in 2022 (−24%). GDDY, VEEV had no share price in 2007–09 (7% of the weight); that replay spreads their weight across the other holdings, so it measures 93% of today's portfolio.
- **Beating the index by 10 points a year cannot be promised.** No rule tested here beat the S&P 500 over 2012–2026, and 86–93% of professional large-cap funds trail it over 10–20 years. The portfolio's own numbers size the gap: it strays from the index by about 12% a year, so with no real edge a single year 10 points ahead happens about 20% of the time, but averaging 10 points ahead over 5 years has about a 3% chance. The edge on offer is depth and discipline: every company screened, prices checked against realistic growth, written exit triggers. That guards against overpaying and unexamined risks; whether it adds return is unproven.
- **Before investing directly:** directly held US shares count toward the ~$60,000 US estate-tax threshold for non-US persons (at $100,000 all in stock you would be above it), and 30% of every US dividend is withheld: on this portfolio's 1.8% yield (weight-averaged trailing dividend yield of the 20 holdings, a snapshot that moves with prices and payouts at every refresh; 25 Sep 2026 snapshot `data/d4_live_snapshot.parquet`; recorded in `outputs/lead_params.json`) that costs about 0.53% of the portfolio a year (§8, §9).

### If you later want less risk: the allocation view

The rest of this section keeps the earlier analysis. It holds the same stocks as a bounded satellite next to an S&P 500 index fund (Irish-domiciled UCITS) and a T-bill reserve sized to the loss you can tolerate. Measured by certainty rather than return, that allocation choice matters more than the stock picks.

- **Where 90% confidence is achievable, and where it is not.** Under the base-case market scenario (6% a year, the median of institutional forecasts), these combinations clear 90% odds of a gain:
  - the **Moderate** mix (55% index / 15% stocks / 30% T-bills): **94%** over 10 years;
  - the **Cautious** mix (35/10/55): **94%** over 5 years and **99%** over 10 years;
  - the **Defensive** mix (15/10/75, the equity budget Codex release v005 chose): **99%** over 5 years and **over 99%** over 10 years;

  Below 90%: Index only 100/0/0: 80% over 5 years, 88% over 10 years; Growth 80/20/0: 80% over 5 years, 88% over 10 years; Moderate 55/15/30: 87% over 5 years. More T-bills buy certainty with lower returns: the median 5-year return is +6.4% a year for Index only, +6.4% a year for Growth, +6.0% a year for Moderate, +5.5% a year for Cautious, +4.9% a year for Defensive. These odds depend on the scenario (bear-to-bull ranges in §7). No single stock and no stock basket earns 90% confidence.
- **Why stocks are only a satellite.** Our pre-registered model did not beat the S&P 500 over 2012–2026. Neither did v1, v2 or v3 (§5). Any stock has a 65–70% chance of a gain over a year and a 43–46% chance of beating the index, whatever its score.
- **What the satellite is for.** Owning verified businesses at fair prices, and diversifying away from an index whose ten largest stocks are 40% of its value. It is not a bet that it will outperform. Expect roughly index-like returns, give or take about 12% a year (its measured tracking error).
- **Your drawdown tolerance decides the reserve, not the stock list:**
  - With no reserve, a fall worse than 20% within 5 years is likely: 81% for the index.
  - With 30% in T-bills the odds fall to 50%; with 55%, to 11%.
  - If 15–20% is a pain threshold you would ride through, the Moderate mix balances return and risk. If it is a hard limit in ordinary bear markets, the Cautious mix fits: it stays above −20% in 89% of simulated 5-year paths.
  - **If the limit must hold even in a 2008-style crash, hold about a third or less in equities.** In the 2007–09 replay (quarterly rebalancing) the Moderate mix fell −39.7% at its worst point and the Cautious mix −25.6%. Staying within −20% through that crash would have needed about 35% or less in equities; within −15%, about 28%.
  - **That is the Defensive mix (15% index / 10% stocks / 75% T-bills)**, the equity budget Codex's release v005 reached independently with a hypothetical shock test. In the 2007–09 replay it fell −12.9%. Its chance of a gain over 5 years is 99%, and its chance of a fall worse than 20% within 5 years is under 1%. The price is return: a median of +4.9% a year, against +6.0% for the Moderate mix. The two workstreams agree on this risk arithmetic; §13 records where they differ.

## 6. The stock satellite, ranked and weighted

**How these 20 were chosen.** Every S&P 500 company got at least a quick research pass: a triage of all 455 names without a dossier (quality, growth, red flags, and whether the price already assumes more growth than is plausible). The strongest were then researched in full from SEC filings, alongside the 40 earlier dossiers and the eight largest AI and cloud companies. A stock is eligible when its full diligence verdict is INCLUDE (full conviction) or INCLUDE-SMALL (half conviction, with a named reservation), and the growth its price implies is at or below the analyst's evidence-based base case (for names in the model's top 70, the systematic valuation must also be fair or attractive). Of the eligible names, the best 20 are held: full conviction first, then the widest margin of safety, then the higher base-case return, with at most two per industry and five per sector (rule (l), added in the third research wave, before any build used it, so the 25% sector cap cannot squeeze full-conviction names below half-conviction weights).

Weights are inverse to volatility: steadier stocks get more. Full-conviction names get up to 10% and half-conviction names up to 5%. No sector exceeds 25% and no sub-industry 12%, and every cap is verified after solving. The rules and every amendment are logged with their reasons in STATE.md. Amendments (a)–(i) were written before the results they govern. Rule (j), the order used to pick the best 20, was written after the diligence verdicts were known but before the ranked list was produced; it is a judgement call, not a pre-registered test. The last tie-breaker (base-case 3-year return) only orders names within the same conviction and margin-of-safety group. For many names it is the systematic model's scenario, which assumes the valuation multiple drifts back toward its own history; that favours deeply de-rated stocks (CMCSA's +62% a year base case is mostly a re-rating from a 6x P/E), and the analysts often called those scenarios optimistic.

| # | Stock | Sector | Weight in sleeve | Diligence | NTM P/E (REITs: P/FFO) | Base rate for similar stocks, 12 months: gain / beat S&P* | 3-yr bear / base / bull, a year† | Exit if (first trigger) |
|---|---|---|---|---|---|---|---|---|
| 1 | **USB** U.S. Bancorp | Financials | 5.6% | INCLUDE § | 10.5x | 71% / 43% | +0% / +12% / +20% | Basel III standardized CET1 ratio falling below 9.5% (from 10.8% currently; per quarterly earnings releases / 10-Q regulatory-capital disclosures, consolidated). |
| 2 | **EXC** Exelon | Utilities | 5.3% | INCLUDE § | 13.5x | 71% / 43% | −2% / +10% / +14% | FY2026 adjusted operating EPS guidance is cut below the current $2.81–$2.91 range. |
| 3 | **CAH** Cardinal Health | Health Care | 5.0% | INCLUDE § | 17.0x | 70% / 44% | −6% / +10% / +18% | Non-GAAP diluted EPS guidance is cut (vs. raised or maintained) at any quarterly release — breaks the core track record this thesis rests on. |
| 4 | **GDDY** GoDaddy | Information Technology | 3.1% | INCLUDE § | 11.1x | 67% / 51% | −5% / +15% / +28% | Core segment organic revenue growth <2% for two consecutive quarters (loss of the pricing/renewal engine). |
| 5 | **VEEV** Veeva Systems | Health Care | 3.5% | INCLUDE § | 28.4x | 67% / 51% | −0% / +13% / +24% | Total revenue growth falls below 12% YoY for two consecutive quarters (from the current steady 16–18%). |
| 6 | **ADP** Automatic Data Processing | Industrials | 5.3% | INCLUDE § | 21.0x | 67% / 43% | −1% / +12% / +19% | Organic constant-currency revenue growth below 4% for two consecutive quarters (vs. 6% delivered all of FY26) |
| 7 | **MA** Mastercard | Financials | 5.6% | INCLUDE § | 25.6x | 72% / 42% | +0% / +13% / +21% | Net revenue growth falls below 8% YoY (reported) for two consecutive quarters. |
| 8 | **TJX** TJX Companies | Consumer Discretionary | 6.8% | INCLUDE § | 23.1x | 72% / 42% | +3% / +10% / +18% | Marmaxx US comp sales below 2% for two consecutive quarters (current run-rate: +1%) |
| 9 | **CRH** CRH plc | Materials | 4.5% | INCLUDE § | 13.4x | 67% / 43% | −15% / +11% / +29% | Net debt/adjusted EBITDA rises above 3.0x (vs approximately 1.8x today, 2.4x pro forma guided for the Arcosa close) |
| 10 | **LVS** Las Vegas Sands | Consumer Discretionary | 4.2% | INCLUDE § | 11.5x | 68% / 45% | −8% / +38% / +79% | Sands China mass-market GGR growth falls below the overall Macau market's growth rate for two consecutive quarters. |
| 11 | **BR** Broadridge Financial Solutions | Industrials | 5.0% | INCLUDE § | 15.2x | 68% / 45% | −1% / +12% / +22% | Recurring-revenue growth (constant currency) falls below 5% for two consecutive quarters (below the low end of every guidance range issued in FY2026/FY2027) |
| 12 | **STE** Steris | Health Care | 5.6% | INCLUDE § | 17.9x | 73% / 42% | +1% / +10% / +17% | Any subsequent quarterly update that lowers FY2027 adjusted EPS guidance below the current $11.10 floor (per 8-K Ex-99.1 releases). |
| 13 | **AXP** American Express | Financials | 4.6% | INCLUDE § | 15.8x | 73% / 42% | −5% / +12% / +21% | Net write-off rate (principal, interest & fees; consolidated, per the quarterly statistical supplement) rises above 3.0% for two consecutive quarters (vs. 2.2-2.3% today). |
| 14 | **PGR** Progressive Corporation | Financials | 4.6% | INCLUDE § | 10.3x (trailing) | 75% / 45% | −11% / +14% / +26% | Quarterly GAAP combined ratio above 96 (the company's own ceiling) for two consecutive quarters. |
| 15 | **DOV** Dover Corporation | Industrials | 5.5% | INCLUDE § | 16.9x | 75% / 45% | −6% / +10% / +20% | Climate & Sustainability Technologies segment organic growth or margin deteriorates for a second consecutive quarter (vs the Q2 2026 refrigeration-driven miss), indicating the production problem is structural, not a one-quarter event. |
| 16 | **WEC** WEC Energy Group | Utilities | 6.7% | INCLUDE § | 17.2x | 75% / 45% | 0% / +10% / +16% | Full-year EPS guidance cut (vs. maintained/raised) at any quarterly release |
| 17 | **BALL** Ball Corporation | Materials | 5.6% | INCLUDE § | 12.9x | 75% / 45% | +1% / +16% / +25% | Global aluminum packaging shipment growth turns negative for two consecutive quarters (currently +4.3% in Q2'26 - a clean, quantifiable proxy for the substitution thesis losing steam). |
| 18 | **PTC** PTC Inc. | Information Technology | 4.1% | INCLUDE § | 15.5x | 69% / 46% | −6% / +12% / +24% | Constant-currency ARR growth (ex-divested businesses) falls below 6% YoY for two consecutive quarters. |
| 19 | **MCK** McKesson Corporation | Health Care | 4.8% | INCLUDE § | 18.2x | 68% / 43% | −2% / +11% / +22% | Oncology & Multispecialty segment revenue growth falls below 15% for two consecutive quarters |
| 20 | **HBAN** Huntington Bancshares | Financials | 4.6% | INCLUDE § | 9.2x | 71% / 49% | +2% / +18% / +28% | Nonperforming-asset ratio rises above 1.00% (vs 0.85% at 2Q26) for two consecutive quarters. |

Weights are rounded to 0.1 point; they sum to 100% of the sleeve.

\* How often S&P 500 stocks in the same model-score band and volatility band rose, or beat the index, over the following 12 months in 2011–2025 (B1 calibration). These describe the group a stock belongs to, not a forecast for that stock; they barely differ across the list because the model score did not predict returns.

† 3-year bear / base / bull returns, annualised. For names marked §, the analyst's own scenarios (dossier section 7); for the others, V1's scripted scenarios, with bear, base and bull valuations drawn from each company's own history. 

**What each holding is for** (one line each, from its dossier; full dossiers in `v4/dossiers/`):

- **USB** (INCLUDE): A diversified super-regional bank with payments and wealth scale, priced like it can't grow despite five straight quarters of improving margins and credit quality.
- **EXC** (INCLUDE): America's cheapest large regulated power-and-gas utility, guided to grow earnings 5-7% a year through 2029 while the market prices in less.
- **CAH** (INCLUDE): One of three dominant US drug wholesalers, raising profit guidance every quarter while its price implies almost no growth at all.
- **GDDY** (INCLUDE): GoDaddy sells domains and web tools to small businesses with sticky renewals, buys back stock aggressively, and trades as if cash flow will shrink.
- **VEEV** (INCLUDE): The dominant, sticky life-sciences cloud software provider to pharma, with four straight quarters of raised guidance and a debt-free balance sheet, priced for far less growth than it keeps delivering.
- **ADP** (INCLUDE): The dominant payroll and HR-outsourcing platform, still beating its own raised guidance every quarter, priced for less growth than management itself expects.
- **MA** (INCLUDE): Global card-payment duopolist with mid-teens revenue growth and low debt, priced for only about 7% a year of future growth.
- **TJX** (INCLUDE): TJ Maxx/Marshalls/HomeGoods off-price retailer with near-net-cash leverage and 62% ROE, priced for less growth than it has actually been delivering.
- **CRH** (INCLUDE): The largest US-focused building-materials group, cheap versus peers with 12 straight years of margin gains, now buying the #1 US aggregates position via a debt-funded Arcosa deal.
- **LVS** (INCLUDE): Owner of Macau's mass-market recovery and Singapore's monopoly casino, priced as if cash flow shrinks for a decade while it buys back stock.
- **BR** (INCLUDE): The near-monopoly plumbing behind proxy voting and bank back-office processing, growing recurring revenue and cash flow at high-single/low-double digits, priced as if it will barely grow at all.
- **STE** (INCLUDE): The leading hospital-sterilization and infection-prevention company, growing across all three segments with FY2027 guidance reiterated and its big lawsuit overhang largely settled.
- **AXP** (INCLUDE): Premium closed-loop card network with best-in-class, stable credit quality and strong EPS growth, priced for less growth than it is delivering.
- **PGR** (INCLUDE): The largest and most data-driven US auto insurer, still growing policies 7% a year with combined ratios 7-10 points inside its own profitability ceiling.
- **DOV** (INCLUDE): Diversified industrial group riding real AI-data-center cooling demand, low debt, and a share price pricing in far less growth than management is currently delivering.
- **WEC** (INCLUDE): A regulated Wisconsin utility with a rare, real large-load (data-center) growth pipeline layered on top of the normal rate-base growth story, guiding 7–8% EPS growth through 2030 off a record $37.5B five-year capital plan — and the reverse DCF implies the market is pricing in materially *less* growth than that guide. The main watch-item is financing (heavy equity issuance), not the demand story.
- **BALL** (INCLUDE): A pure-play global aluminum-can maker riding the plastic-to-aluminum substitution wave, growing double-digit EPS with a credible guidance track record.
- **PTC** (INCLUDE): PLM/CAD software maker whose reported revenue drop is just a divested-unit accounting artifact, while real ARR growth is 9%+ and beating raised guidance.
- **MCK** (INCLUDE): America's largest drug distributor, increasingly an oncology-and-specialty growth platform, priced by the market as if free cash flow will shrink even though guidance points to double-digit growth.
- **HBAN** (INCLUDE): Midwest regional bank that just finished integrating two Texas/South mergers, with margins and book value already rising while the stock still prices in almost no growth.

**What changed since the previous draft** (release v009 (wave-5 build, 27 Sep 2026 02:34)):

- **Removed:** PPG (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); COR (third name in sub-industry); SO (third name in sub-industry). 
- **Added:** WEC, PTC, MCK, from the latest round of full research on names that passed the quick pass (names researched: 313; still queued: 24).

**Financials binds two limits at once:** it holds the maximum five names and sits at the 25% sector cap (25.0%). Eligible full-conviction Financials left out by the five-name limit: RJF, MSCI, WTW, V. The cap also trims the weights of the five held, so each sits below what its volatility alone would give it.

§ Entered through the analyst route (20 of 20): outside the model's top 70, so eligibility rests on the full diligence verdict and the analyst's own valuation (price-implied growth at or below the evidence-based base case). The other 0 are in the model's top 70 and also had to pass the systematic valuation (fair or attractive against their own history).

**How much does the selection order matter?** Rule (j) was re-run under 4 alternative orderings (base return before margin of safety; margin of safety before conviction; model rank instead of base return; conviction then model rank only). Each keeps 9–20 of the 20 names; 9 are chosen under every ordering (ADP, CAH, CRH, EXC, GDDY, LVS, TJX, USB, VEEV). The risk barely moves: the 2007–09 replay ranges from −59% to −46%. The exact list is a judgement at the margin; the character of the portfolio is not (outputs/lead_j_sensitivity.json).

**Diligence errors that changed a verdict or a holding** (caught by the independent fact-checks before release; each dossier carries a dated correction):

- **RMD** (2026-09-27, DA18): The dossier quoted FY2027 revenue and EPS guidance that does not exist in the cited 8-K, reported full-year buybacks and dividends as nine-month figures, and omitted a disclosed divestiture (MatrixCare). Re-assessed on a guidance-free base case: price still implies growth below the base case, but conviction cut from full to half. It dropped out of the 20 and Cardinal Health (already fact-checked by DA10 and DA16) returned.
- **GM** (2026-09-26, A2 loop 4 / DA7): Automotive net cash stated as +$8.7bn using consolidated (GM Financial-inclusive) cash; the automotive-only figure is +$3.7bn. Valuation re-run by the author; verdict unchanged (INCLUDE).
- **RJF** (2026-09-26, DA7): Bank capital ratios were consolidated, not Raymond James Bank's; parent debt omitted $3.5bn of senior notes. Kill criterion restated on the bank's own 16.4% ratio against a 15% trigger; verdict unchanged.

**Order-dependence is rising:** 9 names are chosen under every ordering tested, against 14 in release v009 (wave-5 build, 27 Sep 2026 02:34). As more companies pass every test, more of them tie on conviction and margin of safety, so the final tie-breaker decides more of the list. The risk profile moves much less than the names (see the range above).

**Eligible but not held: 180 names.** Each passed every test and is a candidate replacement if a holding's exit trigger fires. The first 20, in the order they would be picked:

| Next in line | Stock | Sector | Conviction | Price implies growth … the base case | Base-case return a year | Why not held |
|---|---|---|---|---|---|---|
| 1 | **MSCI** MSCI | Financials | full | below | +12% | five-per-sector limit |
| 2 | **WTW** Willis Towers Watson | Financials | full | below | +12% | five-per-sector limit |
| 3 | **V** Visa Inc. | Financials | full | below | +11% | five-per-sector limit |
| 4 | **RJF** Raymond James Financial | Financials | full | below | +11% | five-per-sector limit |
| 5 | **PPG** PPG Industries | Materials | full | below | +10% | outranked in the selection order |
| 6 | **COR** Cencora | Health Care | full | below | +10% | two-per-industry limit |
| 7 | **SO** Southern Company | Utilities | full | below | +10% | two-per-industry limit |
| 8 | **ACGL** Arch Capital Group | Financials | full | below | +9% | outranked in the selection order |
| 9 | **GM** General Motors | Consumer Discretionary | full | below | +9% | outranked in the selection order |
| 10 | **WFC** Wells Fargo | Financials | full | below | +9% | outranked in the selection order |
| 11 | **TEL** TE Connectivity | Information Technology | full | below | +8% | outranked in the selection order |
| 12 | **DUK** Duke Energy | Utilities | full | below | +8% | two-per-industry limit |
| 13 | **DRI** Darden Restaurants | Consumer Discretionary | full | below | +7% | outranked in the selection order |
| 14 | **ALLE** Allegion | Industrials | full | below | +7% | outranked in the selection order |
| 15 | **MTB** M&T Bank | Financials | full | in line with | +10% | outranked in the selection order |
| 16 | **BRK-B** Berkshire Hathaway | Financials | full | in line with | +9% | outranked in the selection order |
| 17 | **AMP** Ameriprise Financial | Financials | full | in line with | +6% | outranked in the selection order |
| 18 | **HST** Host Hotels & Resorts | Real Estate | full | in line with | +6% | outranked in the selection order |
| 19 | **CMCSA** Comcast | Communication Services | half | below | +62% | outranked in the selection order |
| 20 | **BKNG** Booking Holdings | Consumer Discretionary | half | below | +39% | outranked in the selection order |

The other 160 are listed, with their position in the selection order and the reason they missed, in `outputs/lead_j_sensitivity.json` (bench_near_misses) and in the dashboard's ranking tab.

**Every name ranked in the top 45 by the model that the process excluded, with the reason:** CF (rank 1: diligence REJECT); TGT (rank 2: valuation demanding vs own history); SNDK (rank 4: valuation excessive vs own history; valuation incomplete (no base case); the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH); JBHT (rank 7: the analyst's own valuation in dossier section 7 calls it expensive); TRV (rank 9: valuation demanding vs own history; own valuation base case -1%/yr); MU (rank 10: own valuation base case -37%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH); AES (rank 11: pending takeover; valuation missing (not yet valued); no diligence dossier); TPR (rank 12: valuation demanding vs own history; own valuation base case -7%/yr); MPC (rank 13: own valuation base case -17%/yr); WDC (rank 15: valuation excessive vs own history; own valuation base case -58%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH); BAC (rank 19: valuation excessive vs own history; own valuation base case -2%/yr; the analyst's own valuation in dossier section 7 calls it full); TROW (rank 20: diligence WATCH); NTAP (rank 21: valuation excessive vs own history; own valuation base case -17%/yr; the analyst's own valuation in dossier section 7 calls it full; diligence WATCH); NUE (rank 23: valuation excessive vs own history; own valuation base case -10%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH); EXPD (rank 26: valuation excessive vs own history; no diligence dossier); MGM (rank 27: diligence WATCH); WSM (rank 28: valuation excessive vs own history; own valuation base case -22%/yr; no diligence dossier); COP (rank 30: valuation demanding vs own history; own valuation base case -24%/yr; no diligence dossier); AIZ (rank 31: valuation excessive vs own history; own valuation base case -4%/yr); NEM (rank 32: own valuation base case -29%/yr); APA (rank 33: own valuation base case -6%/yr; no diligence dossier); ROST (rank 34: valuation excessive vs own history; own valuation base case -4%/yr; no diligence dossier); ODFL (rank 36: valuation excessive vs own history; own valuation base case -6%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH); VLO (rank 37: own valuation base case -29%/yr; no diligence dossier); COF (rank 38: valuation excessive vs own history; diligence WATCH); HAS (rank 41: own valuation base case -6%/yr); ALB (rank 44: valuation excessive vs own history; own valuation base case -1%/yr); BBY (rank 45: valuation demanding vs own history).

## 7. Risk

**Historical stress replays** (daily data; the sleeve at today's weights, buy-and-hold through each episode; the mixes combine the S&P 500, the sleeve and 4% T-bills, rebalanced quarterly as the operating rules say):

| Episode | Dates (S&P peak → trough) | Stock sleeve | S&P 500 | Moderate 55/15/30 | Cautious 35/10/55 | Defensive 15/10/75 | Max equity share to stay within −20% / −15% |
|---|---|---|---|---|---|---|---|
| Global financial crisis | 2007-10-09 → 2009-03-09 | −48.3% | −55.2% | −39.7% | −25.6% | −12.2% | 35% / 28% |
| US downgrade / euro crisis | 2011-07-07 → 2011-10-03 | −17.3% | −18.4% | −12.5% | −7.7% | −3.9% | 100% / 83% |
| China devaluation sell-off | 2015-07-20 → 2016-02-11 | −11.4% | −13.0% | −8.2% | −4.4% | −1.4% | 100% / 100% |
| Q4 2018 rate scare | 2018-09-20 → 2018-12-24 | −18.1% | −19.3% | −13.1% | −8.1% | −4.0% | 100% / 79% |
| COVID crash | 2020-02-19 → 2020-03-23 | −37.1% | −33.7% | −24.0% | −15.3% | −8.5% | 58% / 44% |
| 2022 inflation bear market | 2022-01-03 → 2022-10-12 | −14.9% | −24.5% | −15.3% | −8.9% | −3.2% | 89% / 68% |

The last column is the largest share of the portfolio in equities (index and stocks in the Moderate mix's 55:15 proportions, the rest in T-bills) that would have kept that episode's worst point within the loss limit.


**The worst fall to plan around.** Over the full daily history (2005-01-04 to 2026-09-25) at today's weights, the stock sleeve's worst fall was **−48.9%** (peak 2007-12-10, trough 2009-03-09, recovered 2009-11-09). The S&P 500's worst fall over the same days was −55.2% (2007-10-09 to 2009-03-09). The crisis replays above use the S&P 500's own peak and trough dates, so they can show a smaller figure for the sleeve (GFC: −48.3%). Treat −49% as the sleeve's tail-risk anchor. In the Moderate mix the 2007–09 replay cost −39.7% and in the Cautious mix −25.6%; set those against your 15–20% tolerance.


**Simulated outcomes by allocation.** 20,000 possible 5- and 10-year futures, each built by stitching together blocks of real market days from 2005–2026 and re-centred on the bear, base or bull market return. The stock satellite is assumed to have no edge. The method and its settings are in Appendix A.

| Allocation (index / stocks / T-bills) | P(gain) 5 yrs: base (bear–bull) | P(gain) 10 yrs: base (bear–bull) | P(fall > 15% within 5 yrs) | P(fall > 20% within 5 yrs) | Median 5-yr return a.r. | Bad year (5th pct, 1 yr) |
|---|---|---|---|---|---|---|
| Index only (100/0/0) | 80% (63%–88%) | 88% (66%–95%) | 96% | 81% | +6.4% | −20.1% |
| Growth (80/20/0) | 80% (63%–88%) | 88% (67%–95%) | 95% | 80% | +6.4% | −20.0% |
| Moderate (55/15/30) | 87% (74%–93%) | 94% (81%–98%) | 74% | 50% | +6.0% | −12.8% |
| Cautious (35/10/55) | 94% (87%–98%) | 99% (94%–over 99%) | 34% | 11% | +5.5% | −6.8% |
| Defensive (15/10/75) | 99% (98%–over 99%) | over 99% (over 99%–over 99%) | 1% | under 1% | +4.9% | −2.0% |

**The stock satellite on its own** (base case, zero assumed alpha): P(gain) 66% over 1 year and 79% over 5. P(beating the S&P 500) is 49% over 1 year and 50% over 5, a coin flip by construction. P(a fall worse than 20% within 5 years) is 84%.

**Diversification.** The 20 stocks behave like about **19 independent positions** once their tendency to move together is counted (19 if only the weights are counted). About **45%** of the sleeve's day-to-day risk comes from the market as a whole (its sensitivity to the S&P 500, beta, is 0.59); the rest is specific to the companies. The largest company-specific risks are ADP (7%), BALL (7%), USB (6%). Per dollar invested, the riskiest holdings are HBAN, AXP and USB: each adds 1.4–1.4 times as much of the sleeve's risk as its weight alone would suggest. Measured over the last three years of daily prices, the sleeve's volatility is 13.5% and it strays from the S&P 500 by about 11.8% a year. An independent re-computation and the method are in Appendix A.

## 9. Operating rules and the weekly 30-minute review

- **Entry:** three equal tranches about three weeks apart, using limit orders near the last close. Never buy a stock in the two trading days before its earnings date.
- **Rebalance quarterly, not weekly.** A holding is sold only if it drops out of the top quarter of the ranking or a pre-written kill criterion fires. A position is trimmed if it exceeds 1.5× its target weight. Most weeks the right action is no trade.
- **Drawdowns trigger reviews, not panic.** At −10% for the portfolio, review every thesis; at −15%, review the equity/reserve mix; at −20%, the stated tolerance is reached. Stop orders are not used, because gaps fill below the trigger.
- **Evaluate the satellite honestly.** After 12 and 24 months, compare it with the S&P 500 on the same dates. If it trails by more than 20 points over 24 months (about a 1-in-8 outcome if it has no edge, given its 12% tracking error), fold it into the index.
- **Weekly checklist (about 30 minutes):**
  1. Check the moves.
  2. Check any earnings or guidance changes against each dossier's kill criteria.
  3. Scan the news for M&A, regulation, management or accounting issues.
  4. Check weight drift.
  5. Log the decision, including "no trade".
  6. At quarter-end, re-run the model and review the replacement list.


**Turning percentages into amounts** (arithmetic only; which mix to use and how much to invest are your decisions):

- Amount in a layer = your total × that layer's share. Amount in one stock = your total × the stock layer's share × the stock's weight in the sleeve.
- Units to buy in one tranche = that stock's amount ÷ 3 ÷ today's price, rounded down. Alternatively, use IBKR's "cash quantity" to buy a dollar amount in fractional shares.
- **Minimum-commission rule:** IBKR charges at least about $1 per US stock order. If a stock's amount is under about $300, buy it in one order instead of three: a $1 charge on a $100 order costs 1%.

| Per $10,000 invested | Index fund (core + unfilled sleeve) | Individual stocks | T-bill reserve | A 10% sleeve position (full conviction) | A 5% sleeve position (half conviction) |
|---|---|---|---|---|---|
| **All stock (0/100/0): your portfolio** | $0 | $10,000 | $0 | $1,000 | $500 |
| Index only (100/0/0) | $10,000 | $0 | $0 | – | – |
| Growth (80/20/0) | $8,000 | $2,000 | $0 | $200 | $100 |
| Moderate (55/15/30) | $5,500 | $1,500 | $3,000 | $150 | $75 |
| Cautious (35/10/55) | $3,500 | $1,000 | $5,500 | $100 | $50 |
| Defensive (15/10/75) | $1,500 | $1,000 | $7,500 | $100 | $50 |

Scale every figure by your total ÷ 10,000. Worked example of the arithmetic (an illustrative total, not a suggestion): at $80,000 all in stock, a holding with a 7.0% weight is $80,000 × 7.0% = $5,600, bought as three tranches of about $1,870; a 1.5% holding is $1,200, three tranches of $400. In the Moderate mix the same 7.0% holding would be $80,000 × 15% × 7.0% = $840.


**Estate tax and withholding at your size** (general information; confirm with a cross-border tax adviser; assumes you are not a US citizen or green-card holder):

| Allocation | Individual US stocks at $50k / $100k (US-situs) | Below the ~$60k US estate-tax threshold? | Dividend withholding drag on those stocks (30% × 1.8% yield) |
|---|---|---|---|
| **All stock (0/100/0): your portfolio** | $50,000 / $100,000 | **At $50k yes; at $100k no.** Above about $60,000 of US shares, a non-US person's estate can owe US estate tax (up to 40% on the excess) | 0.53% of the total portfolio a year (30% of a 1.8% dividend yield) |
| Growth (80/20/0) | $10,000 / $20,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.11% of the total portfolio a year |
| Moderate (55/15/30) | $7,500 / $15,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.08% of the total portfolio a year |
| Cautious (35/10/55) | $5,000 / $10,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.05% of the total portfolio a year |
| Defensive (15/10/75) | $5,000 / $10,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.05% of the total portfolio a year |

A US-domiciled ETF (VOO, SPY) or a US T-bill ETF would count toward the $60k threshold; the UCITS versions do not (R2).
