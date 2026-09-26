## 1. Verdict

**You asked for an all-stock portfolio of 5–20 US companies, researched across the whole S&P 500, with no index fund or T-bills for now. The answer is the 20 stocks in §6.**

- **How they were chosen.** Every S&P 500 company got at least a quick research pass. So far 133 of the strongest, including the eight largest AI and cloud companies, have been researched in full from SEC filings. Another 189 passed the quick pass and are queued for full research, so a later round may still displace some holdings. The 20 held are the best of the 86 that passed every test: 13 at full conviction, together 77% of the portfolio (HST, DOV, DRI, ADP, BR, CRH, GM, MTB, LVS, RJF, AMP, PGR, HBAN), and 7 at half conviction.
- **What is excluded, and why.** Great companies whose price already assumes more growth than the evidence supports stay out, including Microsoft, Alphabet, Amazon, Meta, NVIDIA and Apple. §6 names every eligible stock not held and every top-45 name that failed, with the reason.
- **Honest odds.** In the base-case market (6% a year), with no assumed stock-picking edge: a 75% chance of a gain over 5 years, a 49% chance of beating the S&P 500, and a 93% chance of a fall worse than 20% at some point along the way.
- **In past crises** (today's holdings on daily prices): −60% in 2007–09 (S&P 500 −55%); −41% in the 2020 COVID crash (−34%); −17% in 2022 (−24%). DG, SYF, GM had no share price in 2007–09 (10% of the weight); that replay spreads their weight across the other holdings, so it measures 90% of today's portfolio. The old General Motors went bankrupt in 2009 (today’s GM listed in 2010), so the real 2007–09 loss for this portfolio would likely have been worse.
- **Beating the index by 10 points a year cannot be promised.** No rule tested here beat the S&P 500 over 2012–2026, and 86–93% of professional large-cap funds trail it over 10–20 years. The portfolio's own numbers size the gap: it strays from the index by about 12% a year, so with no real edge a single year 10 points ahead happens about 19% of the time, but averaging 10 points ahead over 5 years has about a 3% chance. The edge on offer is depth and discipline: every company screened, prices checked against realistic growth, written exit triggers. That guards against overpaying and unexamined risks; whether it adds return is unproven.
- **Before investing directly:** directly held US shares count toward the ~$60,000 US estate-tax threshold for non-US persons (at $100,000 all in stock you would be above it), and 30% of every US dividend is withheld: on this portfolio's 2.2% yield that costs about 0.66% of the portfolio a year (§8, §9).

### If you later want less risk: the allocation view

The rest of this section keeps the earlier analysis. It holds the same stocks as a bounded satellite next to an S&P 500 index fund (Irish-domiciled UCITS) and a T-bill reserve sized to the loss you can tolerate. Measured by certainty rather than return, that allocation choice matters more than the stock picks.

- **Where 90% confidence is achievable, and where it is not.** Under the base-case market scenario (6% a year, the median of institutional forecasts), these combinations clear 90% odds of a gain:
  - the **Moderate** mix (55% index / 15% stocks / 30% T-bills): **94%** over 10 years;
  - the **Cautious** mix (35/10/55): **94%** over 5 years and **98%** over 10 years;
  - the **Defensive** mix (15/10/75, the equity budget Codex release v005 chose): **99%** over 5 years and **over 99%** over 10 years;

  Below 90%: Index only 100/0/0: 80% over 5 years, 88% over 10 years; Growth 80/20/0: 79% over 5 years, 87% over 10 years; Moderate 55/15/30: 86% over 5 years. More T-bills buy certainty with lower returns: the median 5-year return is +6.4% a year for Index only, +6.4% a year for Growth, +6.1% a year for Moderate, +5.5% a year for Cautious, +5.0% a year for Defensive. These odds depend on the scenario (bear-to-bull ranges in §7). No single stock and no stock basket earns 90% confidence.
- **Why stocks are only a satellite.** Our pre-registered model did not beat the S&P 500 over 2012–2026. Neither did v1, v2 or v3 (§5). Any stock has a 65–70% chance of a gain over a year and a 43–46% chance of beating the index, whatever its score.
- **What the satellite is for.** Owning verified businesses at fair prices, and diversifying away from an index whose ten largest stocks are 40% of its value. It is not a bet that it will outperform. Expect roughly index-like returns, give or take about 12% a year (its measured tracking error).
- **Your drawdown tolerance decides the reserve, not the stock list:**
  - With no reserve, a fall worse than 20% within 5 years is likely: 81% for the index.
  - With 30% in T-bills the odds fall to 53%; with 55%, to 14%.
  - If 15–20% is a pain threshold you would ride through, the Moderate mix balances return and risk. If it is a hard limit in ordinary bear markets, the Cautious mix fits: it stays above −20% in 86% of simulated 5-year paths.
  - **If the limit must hold even in a 2008-style crash, hold about a third or less in equities.** In the 2007–09 replay (quarterly rebalancing) the Moderate mix fell −41.7% at its worst point and the Cautious mix −27.2%. Staying within −20% through that crash would have needed about 33% or less in equities; within −15%, about 26%.
  - **That is the Defensive mix (15% index / 10% stocks / 75% T-bills)**, the equity budget Codex's release v005 reached independently with a hypothetical shock test. In the 2007–09 replay it fell −14.1%. Its chance of a gain over 5 years is 99%, and its chance of a fall worse than 20% within 5 years is under 1%. The price is return: a median of +5.0% a year, against +6.1% for the Moderate mix. The two workstreams agree on this risk arithmetic; §13 records where they differ.

## 6. The stock satellite, ranked and weighted

**How these 20 were chosen.** Every S&P 500 company got at least a quick research pass: a triage of all 455 names without a dossier (quality, growth, red flags, and whether the price already assumes more growth than is plausible). The strongest were then researched in full from SEC filings, alongside the 40 earlier dossiers and the eight largest AI and cloud companies. A stock is eligible when its full diligence verdict is INCLUDE (full conviction) or INCLUDE-SMALL (half conviction, with a named reservation), and the growth its price implies is at or below the analyst's evidence-based base case (for names in the model's top 70, the systematic valuation must also be fair or attractive). Of the eligible names, the best 20 are held: full conviction first, then the widest margin of safety, then the higher base-case return, with at most two per industry.

Weights are inverse to volatility: steadier stocks get more. Full-conviction names get up to 10% and half-conviction names up to 5%. No sector exceeds 25% and no sub-industry 12%, and every cap is verified after solving. The rules and every amendment are logged with their reasons in STATE.md. Amendments (a)–(i) were written before the results they govern. Rule (j), the order used to pick the best 20, was written after the diligence verdicts were known but before the ranked list was produced; it is a judgement call, not a pre-registered test. The last tie-breaker (base-case 3-year return) only orders names within the same conviction and margin-of-safety group. For many names it is the systematic model's scenario, which assumes the valuation multiple drifts back toward its own history; that favours deeply de-rated stocks (CMCSA's +62% a year base case is mostly a re-rating from a 6x P/E), and the analysts often called those scenarios optimistic.

| # | Stock | Sector | Weight in sleeve | Diligence | NTM P/E (REITs: P/FFO) | Base rate for similar stocks, 12 months: gain / beat S&P* | 3-yr bear / base / bull, a year† | Exit if (first trigger) |
|---|---|---|---|---|---|---|---|---|
| 1 | **HST** Host Hotels & Resorts | Real Estate | 7.8% | INCLUDE | 10.4x P/FFO (2026 guidance) | 71% / 41% | −27% / +6%‡ / +49% | Comparable hotel RevPAR growth turns negative for two consecutive quarters (the core, most-watched KPI). |
| 2 | **DVA** DaVita | Health Care | 2.8% | INCLUDE-SMALL | 10.8x | 62% / 45% | −18% / +20% / +63% | Normalized non-acquired treatment growth is negative for two consecutive quarters (reversing the +0.1%/+0.3% s |
| 3 | **DG** Dollar General | Consumer Staples | 3.1% | INCLUDE-SMALL | 15.2x | 62% / 45% | +20% / +35% / +51% | Same-store sales growth turns negative for two consecutive quarters (from +3.5% currently). |
| 4 | **CVS** CVS Health | Health Care | 3.6% | INCLUDE-SMALL | 10.6x | 67% / 45% | −5% / +36% / +68% | Aetna Medical Benefit Ratio rises above 92% for two consecutive quarters (vs 87.4% in Q2 2026). |
| 5 | **MTB** M&T Bank | Financials | 5.8% | INCLUDE | 10.7x | 71% / 41% | +3% / +10% / +23% | NIM falls below ~3.55% for two consecutive quarters (vs. 3.70% now, and below management's own 'mid-3.60s' 2H2 |
| 6 | **DRI** Darden Restaurants | Consumer Discretionary | 7.2% | INCLUDE | 17.2x | 67% / 45% | −18% / +7% / +22% | Consolidated same-restaurant sales growth turns negative for two consecutive quarters (currently +3.1-4.6% dep |
| 7 | **UDR** UDR, Inc. | Real Estate | 5.0% | INCLUDE-SMALL | 13.5x P/FFO (2026 guidance) | 71% / 43% | −7% / +22% / +57% | Same-store NOI growth negative for two consecutive quarters (FY26 guide is barely positive at +0.625% midpoint |
| 8 | **SYF** Synchrony Financial | Financials | 1.5% | INCLUDE-SMALL | 7.2x | 70% / 44% | +14% / +31%‡ / +53% | NCO rate exceeds 6.00% (top of management's own through-cycle band) for two consecutive quarters. |
| 9 | **BKNG** Booking Holdings | Consumer Discretionary | 3.1% | INCLUDE-SMALL | 13.8x | 63% / 48% | +11% / +39% / +86% | Room-night or gross-bookings growth falls below 3% YoY for two consecutive quarters (currently +5% / +9%). |
| 10 | **AMP** Ameriprise Financial | Financials | 4.5% | INCLUDE § | 9.8x | 74% / 43% | −13% / +6% / +68% | TTM ROE falls below 40% (vs. ~62% now) for two consecutive quarters - would indicate faster-than-expected mean |
| 11 | **GM** General Motors | Consumer Discretionary | 5.8% | INCLUDE § | 5.6x | 68% / 46% | −15% / +9% / +20% | Adjusted EBIT-adjusted guidance cut (vs the current $14.0–16.0bn FY26 range) at any of the next two quarterly  |
| 12 | **ADP** Automatic Data Processing | Industrials | 7.1% | INCLUDE § | 21.0x | 67% / 43% | −1% / +12% / +19% | Organic constant-currency revenue growth below 4% for two consecutive quarters (vs. 6% delivered all of FY26) |
| 13 | **CMCSA** Comcast | Communication Services | 3.5% | INCLUDE-SMALL § | 6.2x | 67% / 43% | +24% / +62% / +90% | The NBCUniversal/Sky spin-off is delayed beyond Q4 2027 (18+ months from announcement) or is restructured so e |
| 14 | **CRH** CRH plc | Materials | 6.2% | INCLUDE § | 13.4x | 67% / 43% | −15% / +11% / +29% | Net debt/adjusted EBITDA rises above 3.0x (vs approximately 1.8x today, 2.4x pro forma guided for the Arcosa c |
| 15 | **LVS** Las Vegas Sands | Consumer Discretionary | 5.7% | INCLUDE § | 11.5x | 68% / 45% | −8% / +38% / +79% | Sands China mass-market GGR growth falls below the overall Macau market's growth rate for two consecutive quar |
| 16 | **BR** Broadridge Financial Solutions | Industrials | 6.7% | INCLUDE § | 15.2x | 68% / 45% | −1% / +12% / +22% | Recurring-revenue growth (constant currency) falls below 5% for two consecutive quarters (below the low end of |
| 17 | **RJF** Raymond James Financial | Financials | 4.7% | INCLUDE § | 11.3x | 73% / 42% | −2% / +11% / +20% | Adjusted pretax margin falls below 18% for two consecutive quarters |
| 18 | **PGR** Progressive Corporation | Financials | 4.3% | INCLUDE § | 10.3x (trailing) | 75% / 45% | −11% / +14% / +26% | Quarterly GAAP combined ratio above 96 (the company's own ceiling) for two consecutive quarters. |
| 19 | **DOV** Dover Corporation | Industrials | 7.4% | INCLUDE § | 16.9x | 75% / 45% | −6% / +10% / +20% | Climate & Sustainability Technologies segment organic growth or margin deteriorates for a second consecutive q |
| 20 | **HBAN** Huntington Bancshares | Financials | 4.2% | INCLUDE § | 9.2x | 71% / 49% | +2% / +18% / +28% | Nonperforming-asset ratio rises above 1.00% (vs 0.85% at 2Q26) for two consecutive quarters. |

Weights are rounded to 0.1 point; they sum to 100% of the sleeve.

\* How often S&P 500 stocks in the same model-score band and volatility band rose, or beat the index, over the following 12 months in 2011–2025 (B1 calibration). These describe the group a stock belongs to, not a forecast for that stock; they barely differ across the list because the model score did not predict returns.

† 3-year bear / base / bull returns, annualised. For names marked §, the analyst's own scenarios (dossier section 7); for the others, V1's scripted scenarios, with bear, base and bull valuations drawn from each company's own history. 

‡ The analyst's own valuation is more cautious than V1's base case (HST, SYF): treat that base case as optimistic; each dossier's section 7 ends with a written reconciliation.

**What each holding is for** (one line each, from its dossier; full dossiers in `v4/dossiers/`):

- **HST** (INCLUDE): Host owns top hotels with beating forecasts and an improved credit rating; shares trade in line with peers, but next year's comparisons will be tougher.
- **DVA** (INCLUDE-SMALL): The largest US dialysis provider is boosting earnings mainly through debt-funded buybacks, not patient growth, while Warren Buffett's Berkshire slowly sells its large stake.
- **DG** (INCLUDE-SMALL): America's largest small-town discount retailer, cheap versus its own history, with sales and profit genuinely recovering after a bad 2023-2024 stretch.
- **CVS** (INCLUDE-SMALL): America's largest drugstore-and-health-insurance company is fixing the Medicare cost overruns that crushed its stock and now trades cheaply, but still carries heavy debt.
- **MTB** (INCLUDE): M&T Bank's lending profits keep improving as deposit costs fall and loan quality improves, with analysts raising forecasts, not cutting them.
- **DRI** (INCLUDE): Owner of Olive Garden and LongHorn Steakhouse, growing sales in every restaurant brand at a modest discount to its own normal price.
- **UDR** (INCLUDE-SMALL): An apartment landlord buying back its own stock, which trades cheaply versus peers, though rent growth has stalled and Southern-market supply weighs on results.
- **SYF** (INCLUDE-SMALL): Synchrony lends through store credit cards for Amazon, Lowe's and others; profit growth has come mostly from fewer bad-loan charges, now leveling off.
- **BKNG** (INCLUDE-SMALL): The world's largest online travel agent, cheaper than almost any point in its history, buying back massive amounts of stock while EU regulators circle.
- **AMP** (INCLUDE): Capital-light wealth and asset manager growing assets under management double-digits, returning most earnings to shareholders, priced under 10 times earnings.
- **GM** (INCLUDE): America's #2 automaker, priced by the market for stagnation while its own guidance keeps rising and its core auto business is net-cash, not net-debt.
- **ADP** (INCLUDE): The dominant payroll and HR-outsourcing platform, still beating its own raised guidance every quarter, priced for less growth than management itself expects.
- **CMCSA** (INCLUDE-SMALL): Comcast's cable/broadband and NBCUniversal/Sky businesses are splitting into two companies; the stock is priced as if cash flow will keep shrinking for a decade, which is more pessimistic than the actual business has ever delivered.
- **CRH** (INCLUDE): The largest US-focused building-materials group, cheap versus peers with 12 straight years of margin gains, now buying the #1 US aggregates position via a debt-funded Arcosa deal.
- **LVS** (INCLUDE): Owner of Macau's mass-market recovery and Singapore's monopoly casino, priced as if cash flow shrinks for a decade while it buys back stock.
- **BR** (INCLUDE): The near-monopoly plumbing behind proxy voting and bank back-office processing, growing recurring revenue and cash flow at high-single/low-double digits, priced as if it will barely grow at all.
- **RJF** (INCLUDE): Well-run wealth-management and investment-banking firm delivering on a stated 20% margin target, priced for much less growth than its own recent run-rate.
- **PGR** (INCLUDE): The largest and most data-driven US auto insurer, still growing policies 7% a year with combined ratios 7-10 points inside its own profitability ceiling.
- **DOV** (INCLUDE): Diversified industrial group riding real AI-data-center cooling demand, low debt, and a share price pricing in far less growth than management is currently delivering.
- **HBAN** (INCLUDE): Midwest regional bank that just finished integrating two Texas/South mergers, with margins and book value already rising while the stock still prices in almost no growth.

**What changed since the previous draft** (Loop-3 build, 26 Sep 2026 12:44):

- **Removed:** SWK; BMY; EG; BX; NOW. Each still passes every test; it was displaced by a newly researched name ranked ahead of it in the selection order.
- **Added:** GM, ADP, RJF, DOV, HBAN, from the latest round of full research on names that passed the quick pass (names researched: 133; still queued: 189).

§ Entered through the analyst route (11 of 20): outside the model's top 70, so eligibility rests on the full diligence verdict and the analyst's own valuation (price-implied growth at or below the evidence-based base case). The other 9 are in the model's top 70 and also had to pass the systematic valuation (fair or attractive against their own history).

**How much does the selection order matter?** Rule (j) was re-run under 4 alternative orderings (base return before margin of safety; margin of safety before conviction; model rank instead of base return; conviction then model rank only). Each keeps 15–20 of the 20 names; 12 are chosen under every ordering (ADP, BR, CRH, DG, DOV, DRI, DVA, GM, HBAN, LVS, PGR, RJF). The risk barely moves: the 2007–09 replay ranges from −62% to −54%. The exact list is a judgement at the margin; the character of the portfolio is not (outputs/lead_j_sensitivity.json).

**Eligible but not held (66 names, next in line first).** Each passed every test; they lost only on the selection order above or the two-per-industry limit, and are the first replacements if a holding's exit trigger fires: FIS (half conviction, price implies growth below the base case); SWK (half conviction, price implies growth below the base case); INTU (half conviction, price implies growth below the base case); BMY (half conviction, price implies growth below the base case); NOW (half conviction, price implies growth below the base case); BX (half conviction, price implies growth below the base case); ADSK (half conviction, price implies growth below the base case); EG (half conviction, price implies growth below the base case); CPAY (half conviction, price implies growth below the base case); FSLR (half conviction, price implies growth below the base case); BRO (half conviction, price implies growth below the base case); AJG (half conviction, price implies growth below the base case); LDOS (half conviction, price implies growth below the base case); OMC (half conviction, price implies growth below the base case); CINF (half conviction, price implies growth below the base case); PNC (half conviction, price implies growth below the base case); PEG (half conviction, price implies growth below the base case); VICI (half conviction, price implies growth below the base case); EQIX (half conviction, price implies growth below the base case); TYL (half conviction, price implies growth below the base case); BLK (half conviction, price implies growth below the base case); CMS (half conviction, price implies growth below the base case); PPL (half conviction, price implies growth below the base case); MCD (half conviction, price implies growth below the base case); DPZ (half conviction, price implies growth below the base case); REGN (half conviction, price implies growth below the base case); WYNN (half conviction, price implies growth below the base case); ABT (half conviction, price implies growth below the base case); PAYX (half conviction, price implies growth below the base case); EOG (half conviction, price implies growth below the base case); AZO (half conviction, price implies growth below the base case); RDDT (half conviction, price implies growth below the base case); SYK (half conviction, price implies growth below the base case); LLY (half conviction, price implies growth below the base case); APD (half conviction, price implies growth below the base case); DIS (half conviction, price implies growth below the base case); EXPE (half conviction, price implies growth below the base case); ADBE (half conviction, price implies growth below the base case); SRE (half conviction, price implies growth below the base case); AVGO (half conviction, price implies growth in line with the base case); ABNB (half conviction, price implies growth in line with the base case); FRT (half conviction, price implies growth in line with the base case); NXPI (half conviction, price implies growth in line with the base case); SCHW (half conviction, price implies growth in line with the base case); EME (half conviction, price implies growth in line with the base case); ALGN (half conviction, price implies growth in line with the base case); UBER (half conviction, price implies growth in line with the base case); APH (half conviction, price implies growth in line with the base case); NFLX (half conviction, price implies growth in line with the base case); ALL (half conviction, price implies growth in line with the base case); TMUS (half conviction, price implies growth in line with the base case); CBRE (half conviction, price implies growth in line with the base case); FANG (half conviction, price implies growth in line with the base case); RCL (half conviction, price implies growth in line with the base case); DLR (half conviction, price implies growth in line with the base case); FITB (half conviction, price implies growth in line with the base case); GL (half conviction, price implies growth in line with the base case); VRSN (half conviction, price implies growth in line with the base case); DLTR (half conviction, price implies growth in line with the base case); GS (half conviction, price implies growth in line with the base case); LMT (half conviction, price implies growth in line with the base case); DAL (half conviction, price implies growth in line with the base case); HIG (half conviction, price implies growth in line with the base case); CSGP (half conviction, price implies growth in line with the base case); ES (half conviction, price implies growth in line with the base case); ADI (half conviction, price implies growth in line with the base case).

**Every name ranked in the top 45 by the model that the process excluded, with the reason:** CF (rank 1: diligence REJECT); TGT (rank 2: valuation demanding vs own history); SNDK (rank 4: valuation excessive vs own history; valuation incomplete (no base case); the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH); JBHT (rank 7: the analyst's own valuation in dossier section 7 calls it expensive); TRV (rank 9: valuation demanding vs own history; own valuation base case -1%/yr); MU (rank 10: own valuation base case -37%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH); AES (rank 11: pending takeover; valuation missing (not yet valued); no diligence dossier); TPR (rank 12: valuation demanding vs own history; own valuation base case -7%/yr); MPC (rank 13: own valuation base case -17%/yr); WDC (rank 15: valuation excessive vs own history; own valuation base case -58%/yr; no diligence dossier); BAC (rank 19: valuation excessive vs own history; own valuation base case -2%/yr; the analyst's own valuation in dossier section 7 calls it full); TROW (rank 20: diligence WATCH); NTAP (rank 21: valuation excessive vs own history; own valuation base case -17%/yr; no diligence dossier); NUE (rank 23: valuation excessive vs own history; own valuation base case -10%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH); EXPD (rank 26: valuation excessive vs own history; no diligence dossier); MGM (rank 27: diligence WATCH); WSM (rank 28: valuation excessive vs own history; own valuation base case -22%/yr; no diligence dossier); CRM (rank 29: no diligence dossier); COP (rank 30: valuation demanding vs own history; own valuation base case -24%/yr; no diligence dossier); AIZ (rank 31: valuation excessive vs own history; own valuation base case -4%/yr); NEM (rank 32: own valuation base case -29%/yr; no diligence dossier); APA (rank 33: own valuation base case -6%/yr; no diligence dossier); ROST (rank 34: valuation excessive vs own history; own valuation base case -4%/yr; no diligence dossier); ODFL (rank 36: valuation excessive vs own history; own valuation base case -6%/yr; no diligence dossier); VLO (rank 37: own valuation base case -29%/yr; no diligence dossier); COF (rank 38: valuation excessive vs own history; no diligence dossier); HAS (rank 41: own valuation base case -6%/yr); ALB (rank 44: valuation excessive vs own history; own valuation base case -1%/yr); BBY (rank 45: valuation demanding vs own history).

## 7. Risk

**Historical stress replays** (daily data; the sleeve at today's weights, buy-and-hold through each episode; the mixes combine the S&P 500, the sleeve and 4% T-bills, rebalanced quarterly as the operating rules say):

| Episode | Dates (S&P peak → trough) | Stock sleeve | S&P 500 | Moderate 55/15/30 | Cautious 35/10/55 | Defensive 15/10/75 | Max equity share to stay within −20% / −15% |
|---|---|---|---|---|---|---|---|
| Global financial crisis | 2007-10-09 → 2009-03-09 | −59.7% | −55.2% | −41.7% | −27.2% | −14.1% | 33% / 26% |
| US downgrade / euro crisis | 2011-07-07 → 2011-10-03 | −25.3% | −18.4% | −13.7% | −8.6% | −4.7% | 100% / 76% |
| China devaluation sell-off | 2015-07-20 → 2016-02-11 | −15.9% | −13.0% | −8.9% | −4.9% | −1.9% | 100% / 100% |
| Q4 2018 rate scare | 2018-09-20 → 2018-12-24 | −20.9% | −19.3% | −13.5% | −8.3% | −4.3% | 100% / 77% |
| COVID crash | 2020-02-19 → 2020-03-23 | −40.7% | −33.7% | −24.5% | −15.7% | −8.9% | 57% / 43% |
| 2022 inflation bear market | 2022-01-03 → 2022-10-12 | −16.6% | −24.5% | −15.5% | −9.0% | −3.3% | 87% / 67% |

The last column is the largest share of the portfolio in equities (index and stocks in the Moderate mix's 55:15 proportions, the rest in T-bills) that would have kept that episode's worst point within the loss limit.


**The worst fall to plan around.** Over the full daily history (2005-01-04 to 2026-09-25) at today's weights, the stock sleeve's worst fall was **−59.7%** (peak 2007-10-09, trough 2009-03-09, recovered 2010-03-05). The S&P 500's worst fall over the same days was −55.2% (2007-10-09 to 2009-03-09). The crisis replays above use the S&P 500's own peak and trough dates, so they can show a smaller figure for the sleeve (GFC: −59.7%). Treat −60% as the sleeve's tail-risk anchor. In the Moderate mix the 2007–09 replay cost −41.7% and in the Cautious mix −27.2%; set those against your 15–20% tolerance.


**Simulated outcomes by allocation.** 20,000 possible 5- and 10-year futures, each built by stitching together blocks of real market days from 2005–2026 and re-centred on the bear, base or bull market return. The stock satellite is assumed to have no edge. The method and its settings are in Appendix A.

| Allocation (index / stocks / T-bills) | P(gain) 5 yrs: base (bear–bull) | P(gain) 10 yrs: base (bear–bull) | P(fall > 15% within 5 yrs) | P(fall > 20% within 5 yrs) | Median 5-yr return a.r. | Bad year (5th pct, 1 yr) |
|---|---|---|---|---|---|---|
| Index only (100/0/0) | 80% (63%–88%) | 88% (66%–95%) | 96% | 81% | +6.4% | −20.1% |
| Growth (80/20/0) | 79% (62%–88%) | 87% (66%–95%) | 96% | 83% | +6.4% | −21.1% |
| Moderate (55/15/30) | 86% (73%–92%) | 94% (80%–98%) | 77% | 53% | +6.1% | −13.7% |
| Cautious (35/10/55) | 94% (86%–97%) | 98% (93%–over 99%) | 37% | 14% | +5.5% | −7.4% |
| Defensive (15/10/75) | 99% (97%–over 99%) | over 99% (over 99%–over 99%) | 2% | under 1% | +5.0% | −2.6% |

**The stock satellite on its own** (base case, zero assumed alpha): P(gain) 64% over 1 year and 75% over 5. P(beating the S&P 500) is 49% over 1 year and 49% over 5, a coin flip by construction. P(a fall worse than 20% within 5 years) is 93%.

**Diversification.** The 20 stocks behave like about **17 independent positions** once their tendency to move together is counted (18 if only the weights are counted). About **53%** of the sleeve's day-to-day risk comes from the market as a whole (its sensitivity to the S&P 500, beta, is 0.75); the rest is specific to the companies. The largest company-specific risks are HST (8%), DRI (8%), MTB (8%). Per dollar invested, the riskiest holdings are SYF, HBAN and GM: each adds 1.3–1.6 times as much of the sleeve's risk as its weight alone would suggest. Measured over the last three years of daily prices, the sleeve's volatility is 15.9% and it strays from the S&P 500 by about 11.6% a year. An independent re-computation and the method are in Appendix A.

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

| Allocation | Individual US stocks at $50k / $100k (US-situs) | Below the ~$60k US estate-tax threshold? | Dividend withholding drag on those stocks (30% × 2.2% yield) |
|---|---|---|---|
| **All stock (0/100/0): your portfolio** | $50,000 / $100,000 | **At $50k yes; at $100k no.** Above about $60,000 of US shares, a non-US person's estate can owe US estate tax (up to 40% on the excess) | 0.66% of the total portfolio a year (30% of a 2.2% dividend yield) |
| Growth (80/20/0) | $10,000 / $20,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.13% of the total portfolio a year |
| Moderate (55/15/30) | $7,500 / $15,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.10% of the total portfolio a year |
| Cautious (35/10/55) | $5,000 / $10,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.07% of the total portfolio a year |
| Defensive (15/10/75) | $5,000 / $10,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.07% of the total portfolio a year |

A US-domiciled ETF (VOO, SPY) or a US T-bill ETF would count toward the $60k threshold; the UCITS versions do not (R2).
