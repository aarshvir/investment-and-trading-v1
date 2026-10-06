# US equity conviction portfolio — v4 (point-in-time rebuild, independently audited)

Data to the US close of Friday 25 September 2026 · prepared for Aarsh · research and general information, not personalised investment, tax or legal advice (the author is not a licensed adviser; no trades are placed).

<!-- SECTION:VERDICT -->
## 1. Verdict

### Read this first: what changed since v011, how much is independently verified, and your 40% tolerance

- **18 of the 20 holdings are new since v011** (WTW, V, CAH, ACGL, WFC, COR, FIS, INTU, ADSK, BIIB, FSLR, BKNG, FDX, ACN, OMC, AMCR, CVS, VZ); 2 are kept (BR, GDDY). 18 v011 names left (ADP, AXP, BALL, CRH, DOV, HBAN, LH, LVS, MA, MCK, PGR, PTC, RSG, STE, TJX, USB, VEEV, WEC). The cause is not market moves: on 5–6 October every v011 holding was re-tested and the first valuation method was found to have systematic errors (stock-based pay added back as if free, interest income counted twice, earnings used as cash, a discount rate that pre-dated the Fed's 16 September rise and the 5.17% 10-year Treasury yield of 25 September, and a bank-style method not applied to banks and insurers). PTC (Schneider's $205 cash bid) and VEEV went to WATCH, and most full-conviction names moved to half conviction. Every change is listed with its reason in §6. These are research findings, not instructions to trade.

- **Technology share (your 20–30% request, rule (o), committed before the build).** Counting Information Technology plus Interactive Media and Payments companies, technology is **29.3%** of the portfolio; Information Technology alone is **20.9%**. The rule did not need to force any swap in this build. Payments companies such as Visa are classified by GICS as Financials, so whether they count as tech is a judgement; both figures are shown.

- **How much is independently verified.** All 500 companies have a full dossier (research from SEC filings), but only **109 of them have been independently fact-checked or re-assessed by a second analyst**, which includes **20 of the 20 holdings** (the release gate requires this for every holding). The other 391 dossiers are researched but not independently verified; in the new verification series 137 of 564 facts (24%) failed and were corrected in the dossiers, so treat any unchecked name's numbers as unverified. Verification of the rest is limited by the research budget, not skipped by choice.

- **Your 40% drawdown tolerance (Codex release v016, 5 October).** Codex recorded that you now accept a temporary fall of up to 40% while the thesis holds, with the all-stock mandate unchanged. This release adopts that. The worst replayed falls for this kind of all-stock portfolio (§4) are close to or beyond 40%, so 40% is a review trigger, not a guaranteed floor. The risk figures in §3 that use a three-year beta of about 0.56 understate market sensitivity: the Loop-11 auditors found betas of 0.93–0.98 in every earlier window, so plan for market-like risk.

**You asked for an all-stock portfolio of 5–20 US companies, researched across the whole S&P 500, with no index fund or T-bills for now. The answer is the 20 stocks in §6.**

- **How they were chosen.** Every one of the 500 S&P 500 companies was researched in full from SEC filings (three second share classes are judged with their sibling), including those the quick first pass had screened out: rule (n) lets any of them qualify on full diligence. Research is not finished for good: each new quarter of results and each weekly review can change a verdict or the list. The 20 held are the best of the 240 that passed every test: 8 at full conviction, together 50% of the portfolio (BR, ACGL, V, CAH, GDDY, COR, WFC, WTW), and 12 at half conviction.
- **What is excluded, and why.** Great companies whose price already assumes more growth than the evidence supports stay out, including Microsoft, Alphabet, Amazon, Meta, NVIDIA and Apple. §6 names every eligible stock not held and every top-45 name that failed, with the reason.
- **Honest odds.** In the base-case market (6% a year), with no assumed stock-picking edge: a 79% chance of a gain over 5 years, a 49% chance of beating the S&P 500, and a 86% chance of a fall worse than 20% at some point along the way.
- **In past crises** (today's holdings on daily prices): −37% in 2007–09 (S&P 500 −55%); −34% in the 2020 COVID crash (−34%); −12% in 2022 (−24%). GDDY, AMCR, V had no share price in 2007–09 (13% of the weight); that replay spreads their weight across the other holdings, so it measures 87% of today's portfolio.
- **Beating the index by 10 points a year cannot be promised.** No rule tested here beat the S&P 500 over 2012–2026, and 86–93% of professional large-cap funds trail it over 10–20 years. The portfolio's own numbers size the gap: it strays from the index by about 13% a year, so with no real edge a single year 10 points ahead happens about 22% of the time, but averaging 10 points ahead over 5 years has about a 4% chance. The edge on offer is depth and discipline: every company screened, prices checked against realistic growth, written exit triggers. That guards against overpaying and unexamined risks; whether it adds return is unproven.
- **Before investing directly:** directly held US shares count toward the ~$60,000 US estate-tax threshold for non-US persons (at $100,000 all in stock you would be above it), and 30% of every US dividend is withheld: on this portfolio's 1.9% yield (weight-averaged trailing dividend yield of the 20 holdings, a snapshot that moves with prices and payouts at every refresh; 25 Sep 2026 snapshot `data/d4_live_snapshot.parquet`; recorded in `outputs/lead_params.json`) that costs about 0.56% of the portfolio a year (§8, §9).

### If you later want less risk: the allocation view

The rest of this section keeps the earlier analysis. It holds the same stocks as a bounded satellite next to an S&P 500 index fund (Irish-domiciled UCITS) and a T-bill reserve sized to the loss you can tolerate. Measured by certainty rather than return, that allocation choice matters more than the stock picks.

- **Where 90% confidence is achievable, and where it is not.** Under the base-case market scenario (6% a year, the median of institutional forecasts), these combinations clear 90% odds of a gain:
  - the **Moderate** mix (55% index / 15% stocks / 30% T-bills): **95%** over 10 years;
  - the **Cautious** mix (35/10/55): **95%** over 5 years and **99%** over 10 years;
  - the **Defensive** mix (15/10/75, the equity budget Codex release v005 chose): **over 99%** over 5 years and **over 99%** over 10 years;

  Below 90%: Index only 100/0/0: 80% over 5 years, 88% over 10 years; Growth 80/20/0: 80% over 5 years, 88% over 10 years; Moderate 55/15/30: 88% over 5 years. More T-bills buy certainty with lower returns: the median 5-year return is +6.4% a year for Index only, +6.4% a year for Growth, +6.0% a year for Moderate, +5.5% a year for Cautious, +4.9% a year for Defensive. These odds depend on the scenario (bear-to-bull ranges in §7). No single stock and no stock basket earns 90% confidence.
- **Why stocks are only a satellite.** Our pre-registered model did not beat the S&P 500 over 2012–2026. Neither did v1, v2 or v3 (§5). Any stock has a 65–70% chance of a gain over a year and a 43–46% chance of beating the index, whatever its score.
- **What the satellite is for.** Owning verified businesses at fair prices, and diversifying away from an index whose ten largest stocks are 40% of its value. It is not a bet that it will outperform. Expect roughly index-like returns, give or take about 13% a year (its measured tracking error).
- **Your drawdown tolerance decides the reserve, not the stock list:**
  - With no reserve, a fall worse than 20% within 5 years is likely: 81% for the index.
  - With 30% in T-bills the odds fall to 48%; with 55%, to 10%.
  - If 15–20% is a pain threshold you would ride through, the Moderate mix balances return and risk. If it is a hard limit in ordinary bear markets, the Cautious mix fits: it stays above −20% in 90% of simulated 5-year paths.
  - **If the limit must hold even in a 2008-style crash, hold about a third or less in equities.** In the 2007–09 replay (quarterly rebalancing) the Moderate mix fell −38.0% at its worst point and the Cautious mix −24.3%. Staying within −20% through that crash would have needed about 37% or less in equities; within −15%, about 29%.
  - **That is the Defensive mix (15% index / 10% stocks / 75% T-bills)**, the equity budget Codex's release v005 reached independently with a hypothetical shock test. In the 2007–09 replay it fell −11.7%. Its chance of a gain over 5 years is over 99%, and its chance of a fall worse than 20% within 5 years is under 1%. The price is return: a median of +4.9% a year, against +6.0% for the Moderate mix. The two workstreams agree on this risk arithmetic; §13 records where they differ.
<!-- /SECTION:VERDICT -->

## 2. What was wrong with v3 (verified, and fixed in v4)

v3 should not be funded as delivered. Fifteen findings were re-computed from its own files (full table: `v4/outputs/lead_v3_audit.md`, dashboard tab "What was wrong with v3"). The four that change the decision:

| Finding | v3 said | Re-computed | v4 fix |
|---|---|---|---|
| "90% odds of profit over 5 years" | a finding | an assumption: at a 6% market return the same simulation gives 75%, at 4% it gives 66% | odds shown under three sourced scenarios (2% / 6% / 9%), plus empirically calibrated hit rates |
| Momentum evidence | 29.1%/yr for ten years | **18.1%/yr** once a stock counts only after it joined the index (look-ahead bias) | every backtest uses point-in-time index membership |
| Out-of-sample test of the conviction filter | "no better than a random stock" | worse: picks returned 10.3% vs 14.5% for their universe (Sep-2024 cohort) and 7.0% vs 17.9% (Sep-2025) | pre-registered model tested over 16 years |
| Worst fall | −26.2% | **−36.2%** on daily data (−40.1% with ABNB's pre-listing months proxied); the S&P fell −33.9% | daily-data drawdowns, no zero-filled history |

Also fixed: weight caps broken by renormalisation (RL/ABNB 10.63% vs a 10% cap); forward P/E mixing fiscal years (NVDA 14.3x vs 16.7x on a next-twelve-months basis); expected returns that double-counted buybacks and scaled the whole market return by beta; a price-index benchmark against total-return stocks (−1.8 pts/yr); missing data counted as a pass.

## 3. The market we are investing into (R1, sources in `v4/outputs/r1_cma_research.md`)

- The S&P 500 closed at 7,743 on 25 September 2026. Shiller CAPE is about 41, the 99th percentile since 1881. The forward P/E is 19.2 because consensus expects EPS growth of +32% in 2026 and +15% in 2027. The 10-year Treasury yields 5.17% and the 3-month bill 4.24%. The ten largest companies are 40% of the index.
- Scenarios for US large-cap equities (nominal, compound, 5–10 years): **Bear 2% · Base 6% · Bull 9%**. The base case sits on the median of twelve institutional forecasts (6.3%) and a 43-advisor survey (6.4%). Cash earns about 4%. Volatility is about 16%.
- A 90% chance of a five-year gain needs about 9.6% a year. Under the three scenarios the S&P 500's five-year gain probability is 61% / 79% / 89%.

## 4. What "90% confident" can honestly mean (R3, `v4/outputs/r3_evidence_base.md`)

- **Holds for a diversified equity portfolio over 10–15 years.** The US market was positive in 95.4% of rolling 10-year windows and 99.5% of 15-year windows since 1926. Across 39 developed markets there was still a 12% chance of losing to inflation over 30 years.
- **Does not hold for a single stock.** A stock beats the market in about 44% of years (Bessembinder 2018). S&P 500 members beat the index 28–31% of the time in 2023–25.
- **Does not hold for a stock-picking tilt beating the index.** A realistic prior for a 15–30 stock quality/value/momentum tilt is **+1%/yr** over the index (range 0 to +2%). Its tracking error is about 7%, and it trails the index in roughly 44% of calendar years. 86–93% of US large-cap funds lagged the S&P 500 over 10–20 years.

<!-- SECTION:EVIDENCE -->
## 5. Evidence: does the v4 model add value? No — and that shapes everything

**The test.** Before running anything, we froze a model built only from well-replicated research (STATE.md, 26 Sep 2026):
- **The model:** quality, value, 12-1 momentum and earnings surprise, sector-neutral and equal-weighted.
- **The universe:** the stocks actually in the S&P 500 at each month-end, from 2012 to August 2026 (D1 membership).
- **The data:** as-filed SEC fundamentals, using only filings made before each month-end (D3), and total-return prices (D2).
- **The costs:** 10 bps per trade.

A second agent rebuilt the model without seeing the first agent's code. It matched within 0.04 points a year (B1X).

**The result** (`v4/outputs/b1_report.md`):

| Strategy, 2012-01 → 2026-08 | Return a year | Versus the S&P 500, a year | Could that gap be luck? | Worst fall (daily) |
|---|---|---|---|---|
| Model top 30, monthly | 12.5% | −2.6 pts | Yes, easily | −44.4% |
| Model top quintile (~85 names) | 13.3% | −1.8 pts | Yes, easily | — |
| Sleeve rule as pre-committed (top 20, vol ≤ 45%, inverse-vol, quarterly) | 10.8% | −4.3 pts | Borderline: more likely a real shortfall | −41.7% |
| 70% S&P 500 + 30% that sleeve | 13.9% | −1.2 pts | Borderline: more likely a real shortfall | −36.1% |
| Equal-weight S&P 500 (point-in-time) | 14.0% | −1.1 pts | Yes, easily | — |
| **S&P 500 (SPY, total return)** | **15.1%** | — | — | −33.7% |

*How to read this table.* "Versus the S&P 500" is the gap you would have experienced. "Could that gap be luck?" asks whether a gap that size could appear by chance when there is no real difference. None of the strategies shows a gap large enough to prove skill; the sleeve rule's shortfall is closer to real than to luck. The exact statistics (t-stats and 95% ranges) are in Appendix A.1. Both daily worst falls were re-derived independently without B1's code: the top 30 fell −43.7% (B1: −44.4%) and the sleeve rule −41.8% (B1: −41.7%), both on 23 March 2020.

- **A higher model score did not mean a higher return.** The decile table is not monotonic; the top decile's next-12-month return was 1.6 points below the bottom decile's. Every tested variant lagged the index:
  - portfolio sizes of 20, 30, 40 and 50 names;
  - monthly, quarterly and annual rebalancing, and a buffer rule;
  - each factor family alone;
  - 500 random family weightings, only 1.4% of which beat the S&P;
  - costs doubled and tripled, a one-month trading lag, and dropping 2020–21.

  The only positive variant was momentum alone: +0.95 pts a year, too small to tell apart from luck.
- **The old models fail the same test:**
  - v1 (low-volatility tilt): −3.8 pts a year.
  - v2 (momentum + value): −1.5 pts a year.
  - v3's conviction filter, annual rebalance: −1.7 pts a year.
- **How v3 fooled itself.** The same model tested on *today's* S&P 500 members earns 18.6% a year, versus 12.5% on the stocks that were actually in the index. That is a 6.0-point illusion created by knowing which companies survived and grew into the index. For momentum over v3's own ten-year window the illusion is 12.5 points: 27.9% vs 15.4%.
- **This is consistent with the wider evidence** (R3). These factor premia shrank sharply in US large caps after 2010, value most of all. 86–93% of professional large-cap funds trailed the S&P 500 over 10–20 years.
- **Calibrated odds** (every S&P 500 stock-month, 2011–2025, flat across score deciles):

  | Measure | Odds |
  |---|---|
  | Chance a stock gains over the next 12 months | **65–70%** |
  | Chance it beats the S&P 500 | **43–46%** |
  | Chance it beats the S&P 500 over 36 months | **39–41%** |
  | Chance it falls more than 20% at some point in the year | **50–61%** |

**What this means.** No honest process can promise that a basket of individual stocks will beat the index. v3's claims implied one could, and the data refutes them. That does not rule out owning stocks. It means choosing them by business quality and by price against realistic growth, and expecting roughly index-like odds of beating the market rather than a guaranteed edge. The owner chose an all-stock portfolio (§6). §1 and §7 show what that means for risk, and what a lower-risk allocation would look like.

**Residual limitation.** Free price data lacks many acquired or failed companies. That flatters every backtested strategy by about 1.0 point a year against the real equal-weight ETF (RSP): 14.0% vs 13.0%. It cannot turn the negative result positive.
<!-- /SECTION:EVIDENCE -->

<!-- SECTION:PORTFOLIO -->
## 6. The stock satellite, ranked and weighted

**How these 20 were chosen.** Every S&P 500 company got at least a quick research pass: a triage of the 455 names that then had no dossier (all 500 now have a full dossier) (quality, growth, red flags, and whether the price already assumes more growth than is plausible). The strongest were then researched in full from SEC filings, alongside the 40 earlier dossiers and the eight largest AI and cloud companies. A stock is eligible when its full diligence verdict is INCLUDE (full conviction) or INCLUDE-SMALL (half conviction, with a named reservation), and the growth its price implies is at or below the analyst's evidence-based base case (for names in the model's top 70, the systematic valuation must also be fair or attractive). Of the eligible names, the best 20 are held: full conviction first, then the widest margin of safety, then the higher base-case return, with at most two per industry and five per sector (rule (l), added in the third research wave, before any build used it, so the 25% sector cap cannot squeeze full-conviction names below half-conviction weights).

Weights are inverse to volatility: steadier stocks get more. Full-conviction names get up to 10% and half-conviction names up to 5%. No sector exceeds 25% and no sub-industry 12%, and every cap is verified after solving. The rules and every amendment are logged with their reasons in STATE.md. Amendments (a)–(i) were written before the results they govern. Rule (j), the order used to pick the best 20, was written after the diligence verdicts were known but before the ranked list was produced; it is a judgement call, not a pre-registered test. The last tie-breaker (base-case 3-year return) only orders names within the same conviction and margin-of-safety group. For many names it is the systematic model's scenario, which assumes the valuation multiple drifts back toward its own history; that favours deeply de-rated stocks (CMCSA's +62% a year base case is mostly a re-rating from a 6x P/E), and the analysts often called those scenarios optimistic.

| # | Stock | Sector | Weight in sleeve | Diligence | NTM P/E (REITs: P/FFO) | Base rate for similar stocks, 12 months: gain / beat S&P* | 3-yr bear / base / bull, a year† | Exit if (first trigger) |
|---|---|---|---|---|---|---|---|---|
| 1 | **CVS** CVS Health | Health Care | 4.9% | INCLUDE-SMALL | 10.6x | 67% / 45% | −5% / +11% / +68% | Aetna Medical Benefit Ratio rises above 92% for two consecutive quarters (vs 87.4% in Q2 2026). |
| 2 | **ACN** Accenture | Information Technology | 3.8% | INCLUDE-SMALL | 12.0x | 63% / 48% | +12% / +12% / +50% | Local-currency revenue growth below 3% (the bottom of the FY26 guide) for two consecutive quarters |
| 3 | **BKNG** Booking Holdings | Consumer Discretionary | 4.3% | INCLUDE-SMALL | 13.8x | 63% / 48% | +11% / +13% / +86% | Room-night or gross-bookings growth falls below 3% YoY for two consecutive quarters (currently +5% / +9%). |
| 4 | **CAH** Cardinal Health | Health Care | 6.4% | INCLUDE § | 17.0x | 70% / 44% | −7% / +10% / +18% | Non-GAAP diluted EPS guidance is cut (vs. raised or maintained) at any quarterly release — breaks the core track record this thesis rests on. |
| 5 | **BIIB** Biogen | Health Care | 4.5% | INCLUDE-SMALL § | 14.7x | 68% / 46% | −15% / +14% / +38% | GAAP diluted EPS below $1.50 for two consecutive quarters excluding clearly-labeled, auditor-confirmed one-off deal/restructuring charges |
| 6 | **FDX** FedEx | Industrials | 5.0% | INCLUDE-SMALL § | 14.3x | 68% / 46% | −9% / +13% / +32% | CY2026 continuing-operations adjusted diluted EPS guidance ($16.90–$18.10) is **cut** (not just reaffirmed) at any subsequent quarterly release. |
| 7 | **GDDY** GoDaddy | Information Technology | 5.9% | INCLUDE § | 11.1x | 67% / 51% | −7% / +12% / +22% | Core segment organic revenue growth <2% for two consecutive quarters (loss of the pricing/renewal engine). |
| 8 | **ACGL** Arch Capital Group | Financials | 7.5% | INCLUDE § | 9.8x | 74% / 43% | −3% / +9% / +20% | Combined ratio excluding cat/prior-year-development exceeds 90% in any reported quarter (vs 82.3-82.5% in the last two) |
| 9 | **ADSK** Autodesk | Information Technology | 4.3% | INCLUDE-SMALL § | 15.3x | 67% / 51% | −2% / +15% / +32% | Quarterly revenue growth decelerates below 10% YoY for two consecutive quarters (from the current 16-18% run-rate). |
| 10 | **WFC** Wells Fargo | Financials | 5.1% | INCLUDE § | 10.6x | 72% / 42% | −8% / +9% / +18% | CET1 ratio (Standardized Approach, consolidated) falls below 9.0% (vs 10.26% now and an 8.50% regulatory minimum+buffer) |
| 11 | **AMCR** Amcor | Materials | 4.9% | INCLUDE-SMALL § | 10.0x | 67% / 43% | −2% / +12% / +24% | Leverage (net debt / [LTM adjusted EBITDA + SBC], company's own metric) exceeds 3.8x at any quarter-end (vs the 3.5-3.6x management is itself targeting for Dec-2026). |
| 12 | **VZ** Verizon | Communication Services | 5.0% | INCLUDE-SMALL § | 9.0x | 72% / 42% | −4% / +11% / +22% | Company-defined net unsecured debt to consolidated adjusted EBITDA above 2.8x at any quarter-end (2.5x at 30 Jun 2026; release schedule). |
| 13 | **FSLR** First Solar | Information Technology | 3.4% | INCLUDE-SMALL § | 8.2x | 65% / 48% | −11% / +14% / +34% | Quarterly net sales YoY growth negative for two consecutive quarters (currently 1 of 2: Q2 2026) |
| 14 | **BR** Broadridge Financial Solutions | Industrials | 9.0% | INCLUDE § | 15.2x | 68% / 45% | −1% / +12% / +22% | Recurring-revenue growth (constant currency) falls below 5% for two consecutive quarters (below the low end of every guidance range issued in FY2026/FY2027) |
| 15 | **INTU** Intuit | Information Technology | 3.6% | INCLUDE-SMALL § | 11.3x | 65% / 48% | −9% / +18% / +41% | TurboTax or Credit Karma segment revenue growth turns negative for 2 consecutive quarters |
| 16 | **OMC** Omnicom Group | Communication Services | 4.4% | INCLUDE-SMALL § | 6.7x | 67% / 44% | −10% / +12% / +25% | Organic growth (Core Ops) falls below 3% for two consecutive quarters. |
| 17 | **COR** Cencora | Health Care | 5.6% | INCLUDE § | 15.5x | 67% / 44% | −7% / +8% / +20% | Adjusted diluted EPS guidance is cut at any quarterly release (breaking the current raise streak). |
| 18 | **WTW** Willis Towers Watson | Financials | 4.0% | INCLUDE § | 13.3x | 67% / 44% | −6% / +12% / +25% | Consolidated organic revenue growth (as reported, quarterly) falls below 3% for two consecutive quarters (vs 4-6% in the last four quarters) |
| 19 | **FIS** Fidelity National Information Services | Financials | 1.5% | INCLUDE-SMALL § | 5.4x | 68% / 43% | +2% / +20% / +34% | Adjusted-EPS guidance is cut again at the Q3'26 or Q4'26 release (any reduction to the low end of the current $6.15-6.24 range). |
| 20 | **V** Visa Inc. | Financials | 6.9% | INCLUDE § | 24.5x | – / – | −2% / +11% / +19% | Net revenue growth falls below 8% YoY (constant-currency) for two consecutive fiscal quarters. |

Weights are rounded to 0.1 point; they sum to 100% of the sleeve.

\* How often S&P 500 stocks in the same model-score band and volatility band rose, or beat the index, over the following 12 months in 2011–2025 (B1 calibration). These describe the group a stock belongs to, not a forecast for that stock; they barely differ across the list because the model score did not predict returns.

† 3-year bear / base / bull returns, annualised. For names marked §, the analyst's own scenarios (dossier section 7); for the others, the base case is the analyst's re-assessed return where one exists and otherwise V1's scripted scenario, with bear and bull valuations drawn from each company's own history. 

**What each holding is for** (one line each, from its dossier; full dossiers in `v4/dossiers/`):

- **CVS** (INCLUDE-SMALL): America's largest drugstore-and-health-insurance company is fixing the Medicare cost overruns that crushed its stock and now trades cheaply, but still carries heavy debt.
- **ACN** (INCLUDE-SMALL): The world's largest IT consulting and outsourcing firm, priced at less than half its historical multiple, even though growth has genuinely slowed and new bookings just turned negative.
- **BKNG** (INCLUDE-SMALL): The world's largest online travel agent, cheaper than almost any point in its history, buying back massive amounts of stock while EU regulators circle.
- **CAH** (INCLUDE): One of three dominant US drug wholesalers, raising profit guidance every quarter while its price implies almost no growth at all.
- **BIIB** (INCLUDE-SMALL): Alzheimer's drug Leqembi and a newly bought eye-disease franchise are growing fast, but a big debt-funded acquisition just wrecked short-term profits.
- **FDX** (INCLUDE-SMALL): The world's largest express-and-ground delivery network, cutting costs faster than promised and priced for an earnings decline that isn't happening, but mid-transition with no permanent CFO.
- **GDDY** (INCLUDE): GoDaddy sells domains and web tools to small businesses with sticky renewals, buys back stock aggressively, and trades as if cash flow will shrink.
- **ACGL** (INCLUDE): A top-tier specialty insurer whose underwriting is still very profitable, priced by the market as if its earnings power is fading fast -- it isn't, yet.
- **ADSK** (INCLUDE-SMALL): Design-and-build software leader growing double digits at a mid-teens P/E, about to take on real integration and leverage risk from its largest-ever acquisition.
- **WFC** (INCLUDE): Money-center bank freed from a seven-year Fed asset cap, growing deposits and profits again, priced as if it will barely grow at all.
- **AMCR** (INCLUDE-SMALL): Newly merged Amcor-Berry is the world's largest consumer-packaging maker, cheap on paper, but it just missed its own (already-cut) cash-flow guidance.
- **VZ** (INCLUDE-SMALL): America's second-largest mobile carrier, priced as if its cash flow will shrink for a decade while a new CEO is delivering growth and raised targets.
- **FSLR** (INCLUDE-SMALL): America's only scaled non-Chinese solar-panel maker, backed by a 45GW backlog and tax credits, priced as if its cash flow barely grows.
- **BR** (INCLUDE): The near-monopoly plumbing behind proxy voting and bank back-office processing, growing recurring revenue and cash flow at high-single/low-double digits, priced for about 3% free-cash-flow growth against a 6% like-for-like base.
- **INTU** (INCLUDE-SMALL): Tax and small-business software platform still growing double digits, priced as if growth stalls forever, despite a costly recent restructuring.
- **OMC** (INCLUDE-SMALL): Now the world's largest ad holding company after merging with Interpublic; cheap on depressed post-merger earnings, but integration is only 10 months old.
- **COR** (INCLUDE): Drug wholesaler with a growing specialty-oncology business, raising profit guidance every quarter despite a real pattern of goodwill write-downs.
- **WTW** (INCLUDE): Global insurance broker turning around post-Aon-merger-collapse, expanding margins and buying back stock, priced for almost no growth at all.
- **FIS** (INCLUDE-SMALL): Bank core-processing giant swapped a non-cash-generating Worldpay stake for a big, high-margin issuer-processing business -- cheap, but now more levered and integrating.
- **V** (INCLUDE): The world's dominant card-payment network, growing mid-teens EPS with a fortress balance sheet, priced for less growth than it is guiding to.

**What changed since the previous draft** (release v011 (wave-7 build, 27 Sep 2026 04:50)):

- **Removed:** USB (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); VEEV (diligence WATCH; price implies more growth than the analyst's base case (above)); ADP (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); MA (third name in sub-industry); TJX (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); CRH (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); LVS (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); STE (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); LH (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); AXP (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); PGR (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); DOV (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); WEC (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); BALL (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); PTC (diligence WATCH; price implies more growth than the analyst's base case (above)); RSG (eligible, but outside the best 20 (conviction, margin of safety, base-case return)); MCK (third name in sub-industry); HBAN (eligible, but outside the best 20 (conviction, margin of safety, base-case return)). 
- **Added:** CVS, ACN, BKNG, CAH, BIIB, FDX, ACGL, ADSK, WFC, AMCR, VZ, FSLR, INTU, OMC, COR, WTW, FIS, V, from the latest round of full research on names that passed the quick pass (names researched: 500; still queued: 0).

**Financials binds two limits at once:** it holds the maximum five names and sits at the 25% sector cap (25.0%). Eligible Financials (full or half conviction) left out by the five-name limit: SYF, CINF, PFG, AON, BRO. The cap also trims the weights of the five held, so each sits below what its volatility alone would give it.

§ Entered through the analyst route (17 of 20): outside the model's top 70, so eligibility rests on the full diligence verdict and the analyst's own valuation (price-implied growth at or below the evidence-based base case). The other 3 are in the model's top 70 and also had to pass the systematic valuation (fair or attractive against their own history).

**How much does the selection order matter?** Rule (j) was re-run under 4 alternative orderings (base return before margin of safety; margin of safety before conviction; model rank instead of base return; conviction then model rank only). Each keeps 9–20 of the 20 names; 8 are chosen under every ordering (ACGL, BR, CAH, COR, GDDY, V, WFC, WTW). The risk barely moves: the 2007–09 replay ranges from −43% to −37%. The exact list is a judgement at the margin; the character of the portfolio is not (outputs/lead_j_sensitivity.json).

**Diligence errors that changed a verdict or a holding** (caught by the independent fact-checks before release; each dossier carries a dated correction):

- **RMD** (2026-09-27, DA18): The dossier quoted FY2027 revenue and EPS guidance that does not exist in the cited 8-K, reported full-year buybacks and dividends as nine-month figures, and omitted a disclosed divestiture (MatrixCare). Re-assessed on a guidance-free base case: price still implies growth below the base case, but conviction cut from full to half. It dropped out of the 20 and Cardinal Health (already fact-checked by DA10 and DA16) returned.
- **GM** (2026-09-26, A2 loop 4 / DA7): Automotive net cash stated as +$8.7bn using consolidated (GM Financial-inclusive) cash; the automotive-only figure is +$3.7bn. Valuation re-run by the author; verdict unchanged (INCLUDE).
- **RJF** (2026-09-26, DA7): Bank capital ratios were consolidated, not Raymond James Bank's; parent debt omitted $3.5bn of senior notes. Kill criterion restated on the bank's own 16.4% ratio against a 15% trigger; verdict unchanged.
- **PTC** (2026-10-05, RA1 re-assessment): Schneider Electric agreed on 4 Oct 2026 to buy PTC for $205 cash (8-K acc. 0001193125-26-413124); upside is capped at the deal price and the remaining return is deal-spread only. Verdict INCLUDE -> WATCH; implied vs base below -> above. Removed from the eligible list.
- **MCK** (2026-10-05, RA1 re-assessment): Its own guidance now trips the oncology kill criterion; conviction cut. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> below. Conviction cut from full to half.
- **HBAN** (2026-10-05, RA1 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the right method for the sector; the valuation margin narrowed. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line. Conviction cut from full to half.
- **TJX** (2026-10-05, RA2 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the right method for the sector; the valuation margin narrowed. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line. Conviction cut from full to half.
- **LH** (2026-10-05, RA2 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the right method for the sector; the valuation margin narrowed. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line. Conviction cut from full to half.
- **VEEV** (2026-10-05, RA2 re-assessment): The reverse DCF added back stock-based compensation and double-counted interest income; corrected, the price implies more growth than the base case. Verdict INCLUDE -> WATCH; implied vs base below -> above. Removed from the eligible list.
- **STE** (2026-10-05, RA3 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the right method for the sector; the valuation margin narrowed. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line. Conviction cut from full to half.
- **BALL** (2026-10-05, RA3 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the right method for the sector; the valuation margin narrowed. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line. Conviction cut from full to half.
- **PGR** (2026-10-05, RA3 re-assessment): Scenarios restated on combined-ratio drivers (bear -15.6%, base +4.8%, bull +15.3% a year). Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> below. Conviction cut from full to half.
- **WEC** (2026-10-05, RA4 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the right method for the sector; the valuation margin narrowed. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line. Conviction cut from full to half.
- **RSG** (2026-10-05, RA4 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the right method for the sector; the valuation margin narrowed. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line. Conviction cut from full to half.
- **LVS** (2026-10-05, RA4 re-assessment): Re-run at the 25 Sep 2026 rates (10-year Treasury 5.17%); still below, but with a thinner margin. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> below. Conviction cut from full to half.
- **DRI** (2026-10-06, RA11 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **EG** (2026-10-06, RA12 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE-SMALL -> INCLUDE-SMALL; implied vs base below (dossier: cheap, -11.9% implied growth) -> in_line.
- **GL** (2026-10-06, RA12 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE-SMALL -> INCLUDE-SMALL; implied vs base not stated (dossier: reasonable-to-slightly-cheap; V1 fair) -> in_line.
- **GM** (2026-10-06, RA12 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> below.
- **HIG** (2026-10-06, RA12 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE-SMALL -> INCLUDE-SMALL; implied vs base not stated (V1 fair; implied ROE 11.8% GAAP basis) -> below.
- **HST** (2026-10-06, RA12 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base not stated (dossier view fair; 1.7% priced in) -> in_line.
- **MPC** (2026-10-06, RA13 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE-SMALL -> WATCH; implied vs base in_line -> above.
- **MTB** (2026-10-06, RA13 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base in_line -> in_line.
- **RJF** (2026-10-06, RA13 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **SWK** (2026-10-06, RA13 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE-SMALL -> WATCH; implied vs base below -> above.
- **TGT** (2026-10-06, RA14 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE-SMALL -> WATCH; implied vs base not stated (dossier: reverse-DCF 'undemanding'; no F-summary entry; V1 verdict 'demanding') -> above.
- **TPR** (2026-10-06, RA14 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE; implied vs base below (V1 reverse-DCF 1.9%; no stated implied_vs_base in the summary) -> below.
- **TRV** (2026-10-06, RA14 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below (dossier: market prices core ROE 'in the mid-teens' against 20-25% delivered; V1 implied ROE 14.1%) -> in_line.
- **UDR** (2026-10-06, RA14 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE-SMALL -> INCLUDE-SMALL; implied vs base below -> in_line.
- **MA** (2026-10-06, RA5 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **USB** (2026-10-06, RA5 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **AXP** (2026-10-06, RA6 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **MSCI** (2026-10-06, RA6 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> WATCH; implied vs base below -> above.
- **ADP** (2026-10-06, RA7 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **CRH** (2026-10-06, RA7 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **DOV** (2026-10-06, RA7 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **EXC** (2026-10-06, RA8 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **PPG** (2026-10-06, RA8 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **SO** (2026-10-06, RA9 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **NOW** (2026-10-06, RA9 re-assessment): Re-assessed at the 25 Sep 2026 rates (Fed hike 16 Sep; 10-year Treasury 5.17%) with free cash flow, SBC as a cost and the sector-appropriate method; the valuation margin narrowed or a kill criterion had fired. Verdict INCLUDE-SMALL -> WATCH; implied vs base below -> above.
- **TEL** (2026-10-06, DVH1): Independent fact-check found valuation inputs that did not survive primary sources; restated valuation sits in line with the base case rather than below it. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **ALLE** (2026-10-06, DVH1): Independent fact-check found valuation inputs that did not survive primary sources; restated valuation sits in line with the base case rather than below it. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **BRK-B** (2026-10-06, DVH1): Independent fact-check found valuation inputs that did not survive primary sources; restated valuation sits in line with the base case rather than below it. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> in_line.
- **ALL** (2026-10-06, RA10 re-assessment): Re-assessed at 25 Sep 2026 rates with free cash flow, SBC as a cost and the sector-appropriate method. Verdict INCLUDE-SMALL -> INCLUDE-SMALL; implied vs base not stated -> in_line.
- **AMP** (2026-10-06, RA10 re-assessment): Re-assessed at 25 Sep 2026 rates with free cash flow, SBC as a cost and the sector-appropriate method. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base in_line -> in_line.
- **BKNG** (2026-10-06, RA10 re-assessment): Re-assessed at 25 Sep 2026 rates with free cash flow, SBC as a cost and the sector-appropriate method. Verdict INCLUDE-SMALL -> INCLUDE-SMALL; implied vs base not stated -> below.
- **BMY** (2026-10-06, RA10 re-assessment): Re-assessed at 25 Sep 2026 rates with free cash flow, SBC as a cost and the sector-appropriate method. Verdict INCLUDE-SMALL -> WATCH; implied vs base fair (not stated) -> above.
- **BX** (2026-10-06, RA10 re-assessment): Re-assessed at 25 Sep 2026 rates with free cash flow, SBC as a cost and the sector-appropriate method. Verdict INCLUDE-SMALL -> INCLUDE-SMALL; implied vs base cheap-to-fair (not stated) -> in_line.
- **ZBRA** (2026-10-06, DVH4): Independent fact-check found the valuation inputs did not survive primary sources. Verdict INCLUDE-SMALL -> WATCH; implied vs base below -> above.
- **SNA** (2026-10-06, A1 loop 11 / RA15): The reverse DCF used an 8.0% discount rate; the programme basis is about 9.2% (10-year Treasury 5.17% plus equity risk premium). Recomputed on owner free cash flow after stock compensation, the price implies 6.1% growth against an evidenced base of about 5%. Verdict INCLUDE -> INCLUDE-SMALL; implied vs base below -> above, so SNA (the largest holding at 10%) is no longer eligible.

**Order-dependence over time** (names chosen under every ordering tested): 12 (v006) → 12 (v007) → 16 (v008) → 14 (v009) → 9 (v010) → 6 (v011) → 8 (this build). The count has fallen as the eligible pool grew; the tie-breaker now decides much of the list, while the 2007–09 replay stays within the range shown above.

**Eligible but not held: 220 names.** Each passed every test and is a candidate replacement if a holding's exit trigger fires. The first 20, in the order they would be picked:

| Next in line | Stock | Sector | Conviction | Price implies growth … the base case | Base-case return a year | Why not held |
|---|---|---|---|---|---|---|
| 1 | **SYF** Synchrony Financial | Financials | half | below | +17% | five-per-sector limit |
| 2 | **CPAY** Corpay | Financials | half | below | +14% | two-per-industry limit |
| 3 | **BRO** Brown & Brown | Financials | half | below | +13% | five-per-sector limit |
| 4 | **TRMB** Trimble Inc. | Information Technology | half | below | +12% | two-per-industry limit |
| 5 | **AON** Aon plc | Financials | half | below | +12% | five-per-sector limit |
| 6 | **CINF** Cincinnati Financial | Financials | half | below | +12% | five-per-sector limit |
| 7 | **PFG** Principal Financial Group | Financials | half | below | +11% | five-per-sector limit |
| 8 | **GIS** General Mills | Consumer Staples | half | below | +11% | outranked in the selection order |
| 9 | **FE** FirstEnergy | Utilities | half | below | +11% | outranked in the selection order |
| 10 | **ZBH** Zimmer Biomet | Health Care | half | below | +11% | outranked in the selection order |
| 11 | **TSN** Tyson Foods | Consumer Staples | half | below | +11% | outranked in the selection order |
| 12 | **ROP** Roper Technologies | Information Technology | half | below | +11% | outranked in the selection order |
| 13 | **FDS** FactSet | Financials | half | below | +11% | outranked in the selection order |
| 14 | **PNC** PNC Financial Services | Financials | half | below | +11% | outranked in the selection order |
| 15 | **PEG** Public Service Enterprise Group | Utilities | half | below | +11% | outranked in the selection order |
| 16 | **HSY** Hershey Company (The) | Consumer Staples | half | below | +11% | outranked in the selection order |
| 17 | **NI** NiSource | Utilities | half | below | +11% | outranked in the selection order |
| 18 | **VICI** Vici Properties | Real Estate | half | below | +11% | outranked in the selection order |
| 19 | **EQIX** Equinix | Real Estate | half | below | +11% | outranked in the selection order |
| 20 | **TYL** Tyler Technologies | Information Technology | half | below | +11% | two-per-industry limit |

The other 200 are listed, with their position in the selection order and the reason they missed, in `outputs/lead_j_sensitivity.json` (bench_near_misses) and in the dashboard's ranking tab.

**Every name ranked in the top 45 by the model that the process excluded, with the reason:** CF (rank 1: diligence REJECT); TGT (rank 2: valuation demanding vs own history; diligence WATCH; price implies more growth than the analyst's base case (above)); SNDK (rank 4: valuation excessive vs own history; valuation incomplete (no base case); the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); JBHT (rank 7: the analyst's own valuation in dossier section 7 calls it expensive); TRV (rank 9: valuation demanding vs own history; own valuation base case -1%/yr); MU (rank 10: own valuation base case -37%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); AES (rank 11: pending takeover; valuation missing (not yet valued); the analyst's own valuation in dossier section 7 calls it full; diligence REJECT; price implies more growth than the analyst's base case (above)); TPR (rank 12: valuation demanding vs own history; own valuation base case -7%/yr); MPC (rank 13: own valuation base case -17%/yr; diligence WATCH; price implies more growth than the analyst's base case (above)); WDC (rank 15: valuation excessive vs own history; own valuation base case -58%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); SWK (rank 17: diligence WATCH; price implies more growth than the analyst's base case (above)); BAC (rank 19: valuation excessive vs own history; own valuation base case -2%/yr; the analyst's own valuation in dossier section 7 calls it full); TROW (rank 20: diligence WATCH); NTAP (rank 21: valuation excessive vs own history; own valuation base case -17%/yr; the analyst's own valuation in dossier section 7 calls it full; diligence WATCH; price implies more growth than the analyst's base case (above)); NUE (rank 23: valuation excessive vs own history; own valuation base case -10%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); BMY (rank 24: diligence WATCH; price implies more growth than the analyst's base case (above)); EXPD (rank 26: valuation excessive vs own history; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); MGM (rank 27: diligence WATCH); WSM (rank 28: valuation excessive vs own history; own valuation base case -22%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); COP (rank 30: valuation demanding vs own history; own valuation base case -24%/yr; the analyst's own valuation in dossier section 7 calls it full; diligence WATCH); AIZ (rank 31: valuation excessive vs own history; own valuation base case -4%/yr); NEM (rank 32: own valuation base case -29%/yr); APA (rank 33: own valuation base case -6%/yr; diligence WATCH); ROST (rank 34: valuation excessive vs own history; own valuation base case -4%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); ODFL (rank 36: valuation excessive vs own history; own valuation base case -6%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); VLO (rank 37: own valuation base case -29%/yr; the analyst's own valuation in dossier section 7 calls it expensive; diligence WATCH; price implies more growth than the analyst's base case (above)); COF (rank 38: valuation excessive vs own history; diligence WATCH); HAS (rank 41: own valuation base case -6%/yr); ALB (rank 44: valuation excessive vs own history; own valuation base case -1%/yr); BBY (rank 45: valuation demanding vs own history).
<!-- /SECTION:PORTFOLIO -->

<!-- SECTION:RISK -->
## 7. Risk

**Historical stress replays** (daily data; the sleeve at today's weights, buy-and-hold through each episode; the mixes combine the S&P 500, the sleeve and 4% T-bills, rebalanced quarterly as the operating rules say):

| Episode | Dates (S&P peak → trough) | Stock sleeve | S&P 500 | Moderate 55/15/30 | Cautious 35/10/55 | Defensive 15/10/75 | Max equity share to stay within −20% / −15% |
|---|---|---|---|---|---|---|---|
| Global financial crisis | 2007-10-09 → 2009-03-09 | −37.2% | −55.2% | −37.9% | −24.3% | −10.7% | 37% / 29% |
| US downgrade / euro crisis | 2011-07-07 → 2011-10-03 | −18.6% | −18.4% | −12.7% | −7.9% | −4.0% | 100% / 81% |
| China devaluation sell-off | 2015-07-20 → 2016-02-11 | −9.7% | −13.0% | −7.9% | −4.2% | −1.2% | 100% / 100% |
| Q4 2018 rate scare | 2018-09-20 → 2018-12-24 | −18.8% | −19.3% | −13.2% | −8.1% | −4.0% | 100% / 79% |
| COVID crash | 2020-02-19 → 2020-03-23 | −33.5% | −33.7% | −23.5% | −15.0% | −8.1% | 59% / 45% |
| 2022 inflation bear market | 2022-01-03 → 2022-10-12 | −11.6% | −24.5% | −14.8% | −8.6% | −2.8% | 91% / 70% |

The last column is the largest share of the portfolio in equities (index and stocks in the Moderate mix's 55:15 proportions, the rest in T-bills) that would have kept that episode's worst point within the loss limit.


**The worst fall to plan around.** Over the full daily history (2005-01-04 to 2026-09-25) at today's weights, the stock sleeve's worst fall was **−41.5%** (peak 2007-12-10, trough 2008-11-20, recovered 2009-12-14). The S&P 500's worst fall over the same days was −55.2% (2007-10-09 to 2009-03-09). The crisis replays above use the S&P 500's own peak and trough dates, so they can show a smaller figure for the sleeve (GFC: −37.2%). Treat −41% as the sleeve's tail-risk anchor. In the Moderate mix the 2007–09 replay cost −37.9% and in the Cautious mix −24.3%; set those against your 15–20% tolerance.


**Simulated outcomes by allocation.** 20,000 possible 5- and 10-year futures, each built by stitching together blocks of real market days from 2005–2026 and re-centred on the bear, base or bull market return. The stock satellite is assumed to have no edge. The method and its settings are in Appendix A.

| Allocation (index / stocks / T-bills) | P(gain) 5 yrs: base (bear–bull) | P(gain) 10 yrs: base (bear–bull) | P(fall > 15% within 5 yrs) | P(fall > 20% within 5 yrs) | Median 5-yr return a.r. | Bad year (5th pct, 1 yr) |
|---|---|---|---|---|---|---|
| Index only (100/0/0) | 80% (63%–88%) | 88% (66%–95%) | 96% | 81% | +6.4% | −20.1% |
| Growth (80/20/0) | 80% (63%–89%) | 88% (67%–96%) | 95% | 79% | +6.4% | −19.6% |
| Moderate (55/15/30) | 88% (74%–93%) | 95% (81%–98%) | 73% | 48% | +6.0% | −12.5% |
| Cautious (35/10/55) | 95% (87%–98%) | 99% (94%–over 99%) | 32% | 10% | +5.5% | −6.6% |
| Defensive (15/10/75) | over 99% (98%–over 99%) | over 99% (over 99%–over 99%) | 1% | under 1% | +4.9% | −1.8% |

**The stock satellite on its own** (base case, zero assumed alpha): P(gain) 65% over 1 year and 79% over 5. P(beating the S&P 500) is 49% over 1 year and 49% over 5, a coin flip by construction. P(a fall worse than 20% within 5 years) is 86%.

**Diversification.** The 20 stocks behave like about **17 independent positions** once their tendency to move together is counted (18 if only the weights are counted). About **37%** of the sleeve's day-to-day risk comes from the market as a whole (its sensitivity to the S&P 500, beta, is 0.56); the rest is specific to the companies. The largest company-specific risks are BR (12%), GDDY (10%), ACGL (8%). Per dollar invested, the riskiest holdings are GDDY, ACN and INTU: each adds 1.4–1.5 times as much of the sleeve's risk as its weight alone would suggest. Measured over the last three years of daily prices, the sleeve's volatility is 14.0% and it strays from the S&P 500 by about 12.9% a year. An independent re-computation and the method are in Appendix A.
<!-- /SECTION:RISK -->

## 8. Implementation for a UAE resident (R2, `v4/outputs/r2_implementation_facts.md`)

- **Precondition for everything in this section:** you are neither a US citizen nor a US green-card holder (for US estate tax, a "non-resident not a citizen"). If either applies, US estate and income tax reach your worldwide assets and none of the mitigation below holds.
- **US estate tax.** Non-US persons have only a ~$60,000 exemption (a $13,000 credit that is not inflation-indexed). Rates run 18–40%. There is no US–UAE estate treaty. Illustrative tax: $80k of US-situs assets → $5,200; $100k → $10,800. Individual US stocks and US-domiciled ETFs are US-situs. Irish UCITS funds (CSPX, VUAA, SPY5, SPXS) are not.
- **Dividends.** A UAE resident suffers 30% US withholding; there is no US–UAE income-tax treaty. Capital gains are generally not US-taxed, and the UAE levies no personal income tax.
- **Index core.** At a 1.11% yield the all-in annual tax drag is: VOO 0.36%, CSPX/VUAA 0.24%, SPY5 0.20%, SPXS 0.12% (SPXS is swap-based and carries counterparty risk).
- **Brokers** (re-verified on the brokers' own pages on 26 Sep 2026, R3: `v4/outputs/r3_implementation_verification.md`).
  - IBKR: about $0.005 per US share (minimum $1); LSE ETFs 0.05% of trade value; no inactivity fee. UAE residents are onboarded by Interactive Brokers (U.K.) Ltd's DIFC branch, regulated by the DFSA as an arranging broker. Custody sits with Interactive Brokers LLC in the US, so the protection scheme is SIPC, not the UK's FSCS.
  - Vested: 0.25% per trade (maximum $35); US stocks and ETFs only; it clears through a US broker, so everything held there is US-situs. It appears to onboard only Indian-origin clients (PAN/NRI), so check eligibility before relying on it.
  - Sarwa is regulated in Abu Dhabi (ADGM FSRA); R3 found no evidence that it offers LSE-listed UCITS funds. The UAE's securities regulator (SCA) was renamed the Capital Market Authority on 1 January 2026.
- **Three open items that public sources cannot settle.** They are marked permanently open: only the broker or a cross-border tax adviser can answer them. Each has a simple workaround that avoids depending on the answer.
  1. *Whether idle cash at a US broker counts as US-situs for estate tax.* Workaround: keep the reserve in directly held T-bills or a UCITS T-bill fund (for example IB01), not as a large idle broker cash balance.
  2. *Whether CSPX or VUAA can be bought in fractional units at IBKR.* Workaround: the IBKR order ticket shows whether "cash quantity" is offered for the instrument. If not, buy whole units (VUAA was about $149 a unit at its 24 September NAV).
  3. *IBKR market-data fees.* Optional: delayed quotes are free, and the weekly review needs no live data.
- **Implication.** A stock sleeve is necessarily US-situs, so its size relative to ~$60k matters. Confirm specifics with a qualified cross-border tax adviser.

<!-- SECTION:OPERATING -->
## 9. Operating rules and the weekly 30-minute review

- **Entry:** three equal tranches about three weeks apart, using limit orders near the last close. Never buy a stock in the two trading days before its earnings date.
- **Rebalance quarterly, not weekly.** A holding is sold only if it drops out of the top quarter of the ranking or a pre-written kill criterion fires. A position is trimmed if it exceeds 1.5× its target weight. Most weeks the right action is no trade.
- **Drawdowns trigger reviews, not panic.** At −10% for the portfolio, review every thesis; at −15%, review the equity/reserve mix; at −20%, the stated tolerance is reached. Stop orders are not used, because gaps fill below the trigger.
- **Evaluate the satellite honestly.** After 12 and 24 months, compare it with the S&P 500 on the same dates. If it trails by more than 20 points over 24 months (about a 1-in-8 outcome if it has no edge, given its 13% tracking error), fold it into the index.
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

| Allocation | Individual US stocks at $50k / $100k (US-situs) | Below the ~$60k US estate-tax threshold? | Dividend withholding drag on those stocks (30% × 1.9% yield) |
|---|---|---|---|
| **All stock (0/100/0): your portfolio** | $50,000 / $100,000 | **At $50k yes; at $100k no.** Above about $60,000 of US shares, a non-US person's estate can owe US estate tax (up to 40% on the excess) | 0.56% of the total portfolio a year (30% of a 1.9% dividend yield) |
| Growth (80/20/0) | $10,000 / $20,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.11% of the total portfolio a year |
| Moderate (55/15/30) | $7,500 / $15,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.08% of the total portfolio a year |
| Cautious (35/10/55) | $5,000 / $10,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.06% of the total portfolio a year |
| Defensive (15/10/75) | $5,000 / $10,000 | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | 0.06% of the total portfolio a year |

A US-domiciled ETF (VOO, SPY) or a US T-bill ETF would count toward the $60k threshold; the UCITS versions do not (R2).
<!-- /SECTION:OPERATING -->

<!-- SECTION:AUDIT -->
## 10. Independent audit loops

Three independent auditors score the whole deliverable on the same 100-point rubric each loop (v4/audit/RUBRIC.md): **A1** quant & data (ex-head of quant research), **A2** investment committee (ex-PM, top-tier long-only fund), **A3** client & compliance (ex-private-bank CIO, UAE clients). Loop 0 scored the original v3 deliverable. Every must-fix item is implemented before the next loop; reports are in v4/audit/.

| Loop | A1 quant & data | A2 investment committee | A3 client & compliance | Average | What changed after this loop |
|---|---|---|---|---|---|
| 0 (v3 baseline) | 41.0 | 42.0 | 45.0 | **42.7** | Baseline: v3 as delivered. Main deficiencies found: infeasible and breached weight caps; drawdown understated by ~10 points (−36% vs −26%); '90%' was an assumption; no point-in-time validation; no UAE implementation or sell rules in the dashboard. All are being rebuilt in v4. |
| 1 | 85.0 | 76.0 | 80.0 | **80.3** | RL removed (valuation demanding once valued) and rules amended: missing, incomplete or negative-base-case valuation = ineligible; the analyst's own valuation must also be fair or better (JBHT out); half conviction halves the cap, unfilled sleeve capacity goes to the index fund. Freshness guard on every input. Thesis lines and verbatim kill criteria for all holdings; three dossier-vs-model valuation conflicts reconciled in writing. Sample-covariance risk contributions; independent daily drawdown check (−43.7% vs −44.4%); crisis replays rebalanced quarterly, with a dated worst-fall anchor and the equity share that would have kept each crisis within −20%/−15%. 95% ranges next to t-stats; bootstrap seed, block length and sensitivity published. Per-$10,000 table and formula; estate-tax precondition; broker and tax facts re-verified (R3); 53 dossier facts re-checked against SEC filings (DA4: 0 fails); glossary; run_all.py and pinned requirements. Diligence extended to all 11 names that pass every quantitative gate. |
| 2 | 88.0 | 89.0 | 89.0 | **88.7** | Plain-English core sections with a technical Appendix A (t-stats, 95% ranges, simulation method and block sensitivity, risk model, register of 11 independent checks, per-holding verification). Price-coverage repair documented: 0 of 408 recovered, root cause in the retry logic; Comerica merged into Fifth Third on 1 Feb 2026 (primary sources); the connected current-listings database cannot fill delisted histories. UDR's corrected REIT valuation added to its dossier and thesis. Risk: tracking error on the sample convention; market-versus-company-specific risk split; effective bets by risk (15 of 20); risk per unit of weight; independent re-computation matches to 5e-7 and now fails the run on any mismatch. §6 explains what changed since the previous draft (HAS, RL, MPC, JBHT out; 9 names added; FRT to half weight) and lists every excluded name in the top 45. Base-rate column relabelled so it cannot be read as a per-stock forecast. §8 marks the three facts only a broker or adviser can settle, each with a workaround. Dossier fact-checks extended to the 8 holdings no auditor had checked (DA5); valuation re-derivation extended to the 8 holdings added in Loop 2 (V1X). |
| 3 | 78.0 | 78.0 | 76.0 | **77.3** | Verdict, hero and answer cards now lead with the all-stock 20-name portfolio the owner asked for (how chosen, honest odds, crisis falls, estate-tax note); the index/T-bill allocation view is kept below as the lower-risk option. PGR's corrupted 0.3x P/E replaced by a sanity-bounded P/E (trailing basis labelled); weights rounded so they sum exactly to 100%. NOW dossier corrected (Moveworks closed Dec 2025). Rule (j) disclosed as written after verdicts were known. §6 lists all 30 eligible-but-not-held names in selection order. 2007–09 replay discloses that DG, SYF and NOW (8% of weight) had no prices and were renormalised out. Research coverage stated plainly: 88 full dossiers, 231 triage-passed names still queued. Loop-3 auditor fact-checks added to the per-holding verification register. |
| 4 | 79.0 | 76.0 | 84.0 | **79.7** | Wave 2 of full diligence (45 names, 133 researched in total, 86 eligible) folded into the build; 13 full-conviction holdings. GM net-cash error corrected by its author (+$3.7bn, not +$8.7bn; verdict unchanged). DA7 fact-checked GM, LVS, RJF, HBAN (27 facts, 5 fails, all corrected in the dossiers; RJF's bank-capital kill criterion restated on the correct standalone basis, 16.4% vs a 15% trigger). A.5 marks failures corrected in the dossier. Rule (j) sensitivity under four alternative orderings (15–20 of 20 names kept, 12 in every ordering, 2007–09 replay −54% to −62%). Pre-registration firewall: rule changes must be committed (sha256, time, reason) before the build runs. §6 marks the 11 holdings that entered through the analyst route and labels whose scenarios are shown; analyst-vs-model labels now show direction. All-stock rows in the per-$10k and estate-tax tables and the dashboard; withholding and tracking-error sizing of the 10-point goal in §1. Superseded Ledoit-Wolf risk block renamed. C1 number-tracing re-run against the current build. v005 reconciliation: PAYX now researched (buyable, not held). |
| 5 | 82.0 | 81.0 | 86.0 | **83.0** | Dashboard audit-history bug fixed (Loop-2 A3 is 89, not 80: the .md fallback had overwritten the JSON total). Verification gate (code/lead_verify_gate.py): no release unless every holding has an independent DA-series fact-check with every FAIL corrected in its dossier, and C1 names the current build's content fingerprint; A.5 prints the gate status. DA8 fact-checks AMP, ADP, CRH, PGR, DOV. Build content fingerprint (content_sha256) and append-only outputs/build_history.jsonl. A.5 register reads auditors' structured fact_checks from Loop 6. Estate-tax and withholding table added to the dashboard Implementation tab. Wave-3 diligence prompt adds an entity-scope rule and a required-fields self-check. |
| 6 | 84.0 | 82.0 | 87.0 | **84.3** | Wave-3 diligence (45 names; 178 researched, 116 eligible) and rules (k) V1 input-defect guard and (l) five names per sector, both committed before the build. DA9/DA10 fact-checked all six new holdings (42 facts, 1 fail, 1 minor, corrected). Inline correction markers on operative dossier sentences (RJF, MSCI). XOM CIK reconciled (ExxonMobil Holdings Corp co-registrant). A.4 register lists every DA check, the whole-market triage and each diligence wave. Dividend-yield source named. Rule-(j) near-miss list with positions. Weights sum exactly. New mechanical dossier pre-check (found an MSCI period mislabel). Written process rule: pre-check + independent fact-check before any release, enforced by the verification gate. |
| 7 | 85.0 | 84.0 | 84.0 | **84.3** | Wave-4 diligence (223 researched, 148 eligible; 20 full-conviction holdings). DA11/DA12 fact-checked the six new holdings (42 facts; PPG debt corrected), DA13 sourced BR's $227m gain and corrected BR's untraceable debt figure and GDDY's debt basis. §6 exit triggers shown in full (were truncated at 110 characters). Bench shown as a table of the next 20; margins to the 20th name in lead_j_sensitivity.json. Assembly fails on any dashboard/audit-score mismatch. New XBRL numeric cross-tie (code/lead_xbrl_crosstie.py). Rule (m) written: pre-checks and an independent fact-check before any holding is released. |
| 8 | 86.0 | 85.0 | 87.0 | **86.0** | Wave-5 diligence (268 researched, 172 eligible; TJX, SO in). DA14 fact-checked TJX and SO (TJX prior-year-column error corrected). Latest-quarter sweep of all 20 holdings (DA15–DA17, 69 facts): ADP Q4 net earnings corrected, EXC blanks filled, no other swaps. GDDY second valuation leg (peer EV/EBITDA and EV/FCF) corroborates the reverse DCF. Rule (m) text placed with rules (a)-(l) in the build script. §6 states when Financials binds both sector limits. Dividend yield labelled a snapshot. Quarterly net-income cross-tie added (its limit on table cells recorded). |
| 9 | 84.0 | 84.0 | 80.0 | **82.7** | Wave-6 diligence (313 researched, 200 eligible). DA18 fact-checked WEC, RMD, MCK, PTC: PTC quarter labels and WEC arithmetic corrected; RMD's non-existent guidance and mislabelled figures led to a re-assessment, a downgrade to half conviction and its exit from the 20 (CAH returned). WEC's missing thesis line fixed at the root (long verdict paragraphs); the build now fails if any holding would show a placeholder thesis. §6 lists every diligence error that changed a verdict or a holding, and states the rise in order-dependence (9 names in every ordering vs 14 in v009). A.4 adds a cumulative DA-series tally. New pre-check flags guidance figures without a verbatim source quote (it flags the RMD lines); future diligence prompts require the quote. |
| 10 | 85.0 | 89.0 | 86.0 | **86.7** | Final wave 7 completed the diligence queue (336 researched, 214 eligible); RSG and LH in. DA19 fact-checked both (LH quarter mislabel corrected, RSG untraceable figure marked). New quarter-label check (code/lead_quarter_label_check.py) maps table rows to SEC XBRL quarters (catches the uncorrected LH row; 0 flags on current dossiers; December year-ends only). DA20 second valuation leg for RSG and LH: both corroborate their reverse DCFs; RSG's 27x is mid-pack against waste peers. §1 says the queue is complete as of the data cutoff; §6 shows the full order-dependence history and flags holdings above 25x earnings. |
| 11 | 76.0 | 79.0 | 77.0 | **77.3** | Whole-index diligence (all 500 dossiers; All-500 register and dashboard tab). Rule (o) technology 20-30% with both figures stated (including payments, and Information Technology alone). Twelve holdings re-assessed 5 Oct (RA1-RA4) and 35 further names re-tested or fact-checked (RA5-RA15, DV02, DV09, DVH1-DVH6) after the valuation method showed systematic errors; PTC, VEEV, MSCI, NOW, SNA and others lost eligibility or conviction. Rule (p): the analyst's re-assessed implied-vs-base and base return now override the systematic mapping in the ranking, so the build equals the All-500 register (UDR, DVA, DG, SYF out). Verification gate extended to the DV series. SNA re-run at the programme discount rate (9.2%): above. A 'Read this first' block states turnover versus v011, the technology share, how few of the 500 are independently verified, and the 40% tolerance with the beta caveat. Section 13 records Codex v012-v016 (adopted, changed, rejected, unresolved) with explicit parents. A.4 and A.5 read the DV series. Not done for budget reasons: independent verification of the remaining dossiers, per-holding discount-rate table, risk figures by sub-period, order-dependence by conviction group, portfolio-level dollar scenarios. |
<!-- /SECTION:AUDIT -->

## 11. Method, data lineage and limitations

- **Universe:** point-in-time S&P 500 membership since 2000 (D1).
- **Prices:** total-return prices 1995–2026 for 1,172 symbols. Validated against CNBC, Cboe and FMP; the S&P 500 total-return benchmark tracks the official index to −0.11%/yr (D2).
- **Fundamentals:** as-filed SEC XBRL fundamentals, usable only after their filing date: 3.46M facts, 629 companies (D3).
- **Live data:** all 503 constituents, prices confirmed by Cboe and CNBC, valuation on a calendarised NTM basis (D4).
- **Evidence and structure:** market scenarios (R1), UAE implementation (R2), factor evidence and base rates (R3).
- **Deep data audits:** DA1 prices and corporate actions, DA2 SEC fundamentals against the filing documents, DA3 estimates against FMP.
- **Residual survivorship:** free price data lacks many acquired or failed companies. Point-in-time price coverage is about 69% of index members in 2010–14, 79% in 2015–19 and 93% in 2020–26. The residual bias is measured against RSP and disclosed with every backtest number.
- **No point-in-time analyst-estimate history exists in free data.** Estimate revisions and NTM valuation are therefore live overlays only, never backtested return drivers.
- **The "no price data" list, re-examined (DA1 → D2R).** DA1 found that D2's downloader recorded "no data" too eagerly: it gave up after two tries about two seconds apart. D2R confirmed that defect in the code and re-attempted all 499 affected symbols twice, 45 minutes apart, with proper back-off. It recovered **none** of the 408 no-data symbols, so point-in-time coverage is unchanged (69% of member-days in 2010–14, 79% in 2015–19, 93% in 2020–26; `v4/outputs/d2r_report.md`). With nothing recovered, the promised cross-vendor validation had nothing to validate.
  - **Why nothing came back:** Yahoo drops a company's price history once it is acquired or taken private, and these symbols had already gone by the time D2 ran. Comerica, DA1's first example, merged into Fifth Third on 1 February 2026 (1.8663 Fifth Third shares per Comerica share; Fifth Third's release of 2 February 2026 and its Q1 2026 10-Q). DA1's other two examples, Electronic Arts and Kellanova, are also absent from a current-listings database, consistent with their announced take-private and acquisition. So the gap is mostly genuine survivorship, not a download fault.
  - **Why no connected source can fill the gap:** the connected market database (Shibui) holds only currently listed securities; none of 18 acquired S&P 500 names tested was present. Closing the gap needs a vendor that keeps delisted histories, such as CRSP or Norgate.
  - **What it means for the conclusion:** the gap is the residual survivorship bias measured above, +1.0 pt/yr against RSP. B1X's independent check found that using today's survivors instead of point-in-time members inflates returns by about 6 points a year. A gap of this kind cannot turn the negative result positive; its exact size stays unmeasured.
- **The backtest starts in 2012, not earlier.** As-filed XBRL fundamentals only begin in 2009–2011, so the model's history excludes the 2008 crisis. The stress tests in §7 replay 2007–09 for today's sleeve using prices only.
- **Reproducibility.** Every number in this report is regenerated by the scripts listed in `v4/README_RUN.md` and `v4/run_all.py`, in order, with pinned library versions (`v4/requirements.txt`). The simulations use a stationary block bootstrap (mean block 21 trading days), 20,000 paths and random seed 7. B1's 500 random family weightings use seed 42 (Dirichlet, α = 5); its unit tests use seed 20260926. A freshness guard stops publication if any input changed after the portfolio was built.
- **Two data defects found during diligence, and how they are handled.** (1) Comfort Systems (FIX): a mis-dated duplicate figure in the company's own SEC data feed made the valuation model read its revenue about 2.8 times too low, producing a false "excessive" verdict. A scan of all 92 names the model values found no other case; rule (k) now discards any model verdict built on a revenue figure that disagrees with an independent source by more than 1.6 times, and such names are judged on their full diligence instead. (2) ExxonMobil (XOM) is the only one of 503 names whose SEC company identifier differs between two input files (2115436 vs 34088). This is resolved: an August 2026 reorganisation created ExxonMobil Holdings Corp (CIK 2115436), which files as a co-registrant with Exxon Mobil Corporation (CIK 34088), and the backtest's data lineage already links the two (outputs/b1_report.md). No figure is affected. XOM is rated WATCH and not held.

## 12. Plain-English glossary

- **Index fund (UCITS, Irish-domiciled):** a fund that simply owns all S&P 500 companies. The Irish legal wrapper keeps it outside US estate tax and halves the US tax on its dividends.
- **T-bill:** a short-term US government IOU (3–12 months). It is the closest thing to risk-free cash in dollars and currently pays about 4% a year.
- **Satellite / sleeve:** the small part of the portfolio held in individual stocks, next to the index core.
- **Backtest:** replaying a rule on past data to see how it would have done.
- **Point-in-time:** using only what was knowable on each past date: the companies actually in the index then, and the accounts filed by then.
- **Look-ahead and survivorship bias:** the two classic backtest cheats. Look-ahead uses information that was not yet public. Survivorship tests only today's winners and forgets the companies that shrank, were bought or went bust.
- **Pre-registered:** the model was written down and frozen before any test was run, so it could not be tuned to the answer.
- **Pts/yr (percentage points a year):** the difference between two annual returns, e.g. 12.5% vs 15.1% is −2.6 pts/yr.
- **t-stat:** how many standard errors a result sits from zero. Between −2 and +2 means "could easily be luck".
- **95% range (confidence interval):** the band that would contain the true value in 95 of 100 repeats of the experiment.
- **Volatility:** how much a price typically swings in a year (one standard deviation, as a %).
- **Tracking error:** how far a portfolio's yearly return typically strays from the index, in either direction.
- **Beta:** how much a stock or portfolio tends to move when the index moves 1% (a beta of 0.8 means about 0.8%).
- **Drawdown / worst fall:** the largest fall from a previous high to a later low, before recovering.
- **Stress replay:** re-running today's holdings through a past crisis (e.g. 2008, 2020) on daily prices.
- **Stationary bootstrap:** a simulation that builds thousands of possible futures by stitching together random blocks of real past days. It keeps the real clustering of good and bad days.
- **Scenario (bear / base / bull):** an assumed long-run market return of 2% / 6% / 9% a year. The odds in this report are conditional on the scenario.
- **Calibrated odds / base rate:** how often something actually happened historically to stocks like this one (same score band and volatility). It is not a forecast for the specific stock.
- **NTM P/E:** share price divided by the next twelve months of expected earnings per share. Lower means cheaper per dollar of profit.
- **P/FFO:** the REIT version of P/E. FFO (funds from operations) adds back property depreciation, which overstates real costs for landlords.
- **P/B and justified P/B:** price relative to book value (net assets), used for banks and insurers. The justified P/B is what the return on equity supports.
- **Reverse DCF:** instead of forecasting cash flows to get a price, start from today's price and solve for the growth the market is assuming. Then ask whether that growth is plausible.
- **Own-history percentile:** where today's valuation sits within the company's own past range (0 = cheapest ever, 100 = dearest).
- **Kill criterion:** a measurable condition, written in advance, that means the investment case is broken and the stock is sold.
- **INCLUDE / INCLUDE-SMALL:** the diligence verdict. INCLUDE is held at full weight (up to 10% of the sleeve). INCLUDE-SMALL is investable with a named reservation and held at half weight (up to 5%).
- **US-situs:** an asset the US treats as located in the US for estate tax (US shares and US-domiciled ETFs). Irish UCITS funds are not US-situs.
- **Withholding tax:** tax taken at source from dividends before you receive them: 30% for a UAE resident on US shares, 15% inside an Irish fund.

<!-- SECTION:V005 -->
## 13. Relationship to Codex release v005

A second AI workstream (Codex) published a completed decision pack, **v005_2026-09-26_codex** (prepared 2026-09-25 21:16 UTC; data 2026-09-24 reference prices; MSFT 2026-09-25; individual filing periods disclosed). The shared workspace rules require each new release to check the previous one and record what it adopts, confirms, changes, rejects or leaves open, with evidence. This v4 release neither silently replaces v005 nor inherits its conclusions unchecked. Where the two differ, the evidence is below and the owner decides.

| Topic | Status | Codex v005 | Claude v4 (evidence) | Effect on this release |
|---|---|---|---|---|
| **A hard 15–20% loss limit needs a small equity share** | CONFIRMED independently | Maximum 25% equity (15% index + 10% direct, at least 75% reserve); a hypothetical tail shock (index −60%, stocks −75%, reserve −2%) loses 18.0% at full deployment. | Daily-data replay of 2007–09 with quarterly rebalancing: staying within −20% needed ≤37% in equities, within −15% ≤29%. The Defensive mix (v005's budget) fell -11.7% in that replay. | v4 adds the Defensive 15/10/75 mix to every allocation table, with simulated odds on the same engine as the other mixes. |
| **Whether 15–20% must hold in every crash** | UNRESOLVED (owner decision) | Treats 15–20% as the design objective for the whole portfolio, hence 75–81% reserve. | Shows the trade-off instead. Base case, median 5-year return +4.9%/yr for Defensive vs +6.0%/yr for Moderate; P(fall > 20% within 5 yrs) 0% vs 48%. The 15–20% figure comes from the earlier Codex review notes; to Claude the owner described his risk appetite as 'not very risk-averse, not extremely risk-taking'. | v4 does not override v005: the owner chooses which sentence describes his limit (the one next step). |
| **Irish UCITS index core and a short-Treasury reserve** | ADOPTED | VUAA (IE00BFMXXD54) for the index; IB01 (IE00BGSF1X88, 0–1 yr Treasuries) plus cash for the reserve. | CSPX or VUAA for the core; directly held T-bills or a UCITS T-bill fund for the reserve. IB01 is such a fund; both keep the reserve outside US estate tax. | v4 names IB01 as one eligible reserve fund, alongside direct T-bills. |
| **Dividend withholding and US estate tax** | CONFIRMED | 30% withholding on direct US dividends; Irish funds 15% internally; direct US shares are US-situs. | Same facts, re-verified against IRS and issuer pages on 26 Sep 2026 (R2, R3). | None. |
| **Which stocks are candidates** | CHALLENGED | Ranks only the original fourteen v3 candidates and says so ('not a claim to have found the best fourteen investments in the entire market'). | v3's candidate list rested on biased evidence: its momentum result falls from 29.1%/yr to 18.1%/yr once stocks count only after joining the index, and its conviction filter failed out of sample. v4 screens all 503 point-in-time members with pre-registered rules plus primary-source diligence. The only overlap is HIG. | v4's satellite is not built from v3's list. v4 also found no stock-selection edge, so neither workstream's picks should be expected to beat the index. |
| **AMP and PAYX as first purchases** | AMP CONFIRMED (eligible, not held); PAYX CONFIRMED as buyable (eligible, not held) | BUY NOW at ≤ $500 (AMP) and ≤ $101.80 (PAYX), 2% slots each, base 3-yr IRRs 12.8% / 12.2% after withholding. | Once v4 extended research to every S&P 500 company, its own full diligence (F21) first rated AMP INCLUDE at full conviction (cut to INCLUDE-SMALL, half conviction, in the 6 October re-assessment RA10), fairly priced at under 10x forward earnings. AMP passes every v4 test but is not held: eligible, but outside the best 20 (conviction, margin of safety, base-case return). PAYX was researched in full in wave 2 (F37): INCLUDE-SMALL (half conviction), with the price implying about 0.7% a year of cash-flow growth against management's own guided 7–9% earnings growth, and a base-case return of about +9.8% a year. It passes every v4 test but is not held: 20 names outranked it under rule (j). Its named reservation is a slowdown in the Management Solutions unit (75% of revenue) and an April 2026 data breach. | Both names now pass v4's own full diligence, so v005's judgement that they are sound purchases at those limits is confirmed; v4 keeps both on its bench of eligible names (neither is in the current 20). PAYX closed at $101.37 on 25 Sep 2026, just under v005's $101.80 limit. X1 reproduced both v005 base cases to the cent from SEC filings. AMP's 13x exit multiple sits near its 10-year average P/E. PAYX's 20x sits below its whole 10-year P/E range (about 24–34x): conservative, but v005 does not say so. The AMP gap between v005 (13–14% IRR, cash-flow model) and v4's valuation model (+6.5%/yr, price-to-book relative to peers) is a method choice, not an error on either side. |
| **RL, AIZ, NTAP at current prices** | CONFIRMED | RL: avoid (reconsider at $265). AIZ: buy only ≤ $235. NTAP: buy only ≤ $150. | V1 rates RL 'demanding' (base −7.8%/yr), AIZ 'excessive' (−3.9%/yr) and NTAP 'excessive' (−17.2%/yr); none is held. | None. |
| **HIG entry price** | RESOLVED (HIG no longer held) | Buy only at ≤ $120 (12% hurdle). | HIG remains eligible (fair valuation, +2.7%/yr base case) but fell outside v4's best 20 once research covered the whole index. | None: the thin-margin name was displaced by stronger ideas. |
| **MSFT and NVDA** | CONFIRMED (not at current prices) | Buy below $500 (MSFT, price $516) and below $215 (NVDA, price $225). | Full diligence (F17, F18): MSFT WATCH, since the price implies about 12.7% a year of growth against a ~10.9% base case. NVDA INCLUDE-SMALL on quality, but on trailing cash flow its price implies more than the base case. | Both workstreams like the businesses and decline to buy at the 25 September prices. |
| **Drawdown response rules** | ADOPTED for the Defensive mix | Freeze additions at −8% from the high-water mark, re-underwrite at −12%, capital preservation at −15%. | Review theses at −10%, the equity/reserve mix at −15%, tolerance reached at −20% (sized for the Moderate/Cautious mixes). | v4 keeps its triggers for Moderate/Cautious; for the Defensive mix v005's tighter triggers apply. |
| **Dollar illustrations** | CHANGED (presentation) | Unit counts for $50,000 and $100,000. | Research-only presentation: a per-$10,000 table and the formula, no order sheet in the owner's dollars. | None on substance. |

**v005's fourteen candidates, seen through v4's gates** (prices at the 25 September close):

| v005 rank | Stock | v005 decision | v005 max entry | Price 25 Sep | vs limit | v4 model rank | v4 valuation (base 3-yr, a year) | v4 status |
|---|---|---|---|---|---|---|---|---|
| 1 | **AMP** | BUY NOW | $500.00 | $493.00 | −1.4% | 113 | fair (+6%) | eligible, but outside the best 20 (conviction, margin of safety, base-case return) |
| 2 | **PAYX** | BUY NOW | $101.80 | $101.37 | −0.4% | 95 | – | eligible, but outside the best 20 (conviction, margin of safety, base-case return) |
| 3 | **MSFT** | BUY BELOW | $500.00 | $516.17 | +3.2% | 152 | – | diligence WATCH; price implies more growth than the analyst's base case (above) |
| 4 | **NVDA** | BUY BELOW | $215.00 | $225.07 | +4.7% | 103 | – | price implies more growth than the analyst's base case (above) |
| 5 | **ALLE** | BUY BELOW | $145.00 | $154.47 | +6.5% | 164 | – | eligible, but outside the best 20 (conviction, margin of safety, base-case return) |
| 6 | **HIG** | BUY BELOW | $120.00 | $124.23 | +3.5% | 22 | fair (+3%) | eligible, but outside the best 20 (conviction, margin of safety, base-case return) |
| 7 | **CPAY** | BUY BELOW | $350.00 | $398.11 | +13.7% | 339 | – | third name in sub-industry |
| 8 | **AIZ** | BUY BELOW | $235.00 | $265.00 | +12.8% | 31 | excessive (−4%) | valuation excessive vs own history; own valuation base case -4%/yr |
| 9 | **SNA** | BUY BELOW | $310.00 | $369.20 | +19.1% | 94 | – | price implies more growth than the analyst's base case (above) |
| 10 | **NTAP** | BUY BELOW | $150.00 | $201.15 | +34.1% | 21 | excessive (−17%) | valuation excessive vs own history; own valuation base case -17%/yr; the analyst's own valuation in dossier section 7 calls it full; diligence WATCH; price implies more growth than the analyst's base case (above) |
| 11 | **IBKR** | BUY BELOW | $65.00 | $89.24 | +37.3% | 232 | – | eligible, but outside the best 20 (conviction, margin of safety, base-case return) |
| 12 | **ABNB** | AVOID CURRENT PRICE | $120.00 | $157.47 | +31.2% | 40 | fair (+19%) | eligible, but outside the best 20 (conviction, margin of safety, base-case return) |
| 13 | **AME** | AVOID CURRENT PRICE | $185.00 | $250.74 | +35.5% | 157 | – | eligible, but outside the best 20 (conviction, margin of safety, base-case return) |
| 14 | **RL** | AVOID CURRENT PRICE | $265.00 | $357.10 | +34.8% | 62 | demanding (−8%) | valuation demanding vs own history; own valuation base case -8%/yr |

**Verification of v005's inherited claims** (agent X1, `v4/outputs/x1_v005_verification.md`): 23 of 26 checked claims confirmed against v4's price data, issuer pages and SEC filings. Exceptions: MINOR DIFFERENCE: MSFT reference close $516.05 on 2026-09-25 ('reconciled') (Both independent sources show $516.17, a $0.12 (0.02%) gap from the memo's $516.05. No disclosed header/row conflict for MSFT (unlike NVDA/AMP/HIG/AIZ/IBKR on 25-Sep), so calling it 'reconciled' is not supported by any source found. Immaterial to the BUY BELOW $500 decision either way.); UNVERIFIABLE: IB01 effective duration 0.31 years (Duration was not displayed on any page reachable via WebFetch/WebSearch; the factsheet PDF returned as unparseable binary content. Plausible given the fund's stated 0-1yr maturity mandate, but not independently confirmed within the time available.); NOT CONFIRMED: PAYX 20.0x terminal P/E multiple is inside PAYX's own 10-year P/E history (10-year average P/E ~28-29x; cited 10-year range ~23.6x (2020 low) to ~34.3x (2025 high). 20.0x sits below the entire cited range, i.e. NOT inside PAYX's own 10-year history. This makes the model more conservative than history (not an overstatement of value), but quality_compounders.md does not disclose that the multiple is below-range.). Method disagreement: AMP valuation and recommendation strength: Both figures independently reproduce correctly from each workstream's own stated methodology and inputs (verified above); the gap is a methodology choice (absolute three-scenario cash-flow IRR vs. relative P/B-to-peers), not a sourcing or arithmetic error in either model. Not adjudicated by this verification -- flagged for the next release to reconcile or to explicitly justify preferring the DDM basis over the peer-relative basis for a wealth-management/asset-management hybrid like AMP.

Parents recorded for this release (explicit, per RESEARCH_VERSIONING.md): v016_2026-10-05_codex, v015_2026-10-04_codex, v014_2026-10-01_codex, v013_2026-10-01_codex, v012_2026-09-27_codex, v011_2026-09-27_claude, v010_2026-09-27_claude, v005_2026-09-26_codex, claude-v3, codex-initial-audit, codex-deep-data-audit.

### Codex releases v012–v016 (27 Sep – 5 Oct 2026): adopted, changed, rejected, unresolved

- **Adopted:** v016's mandate recast: you accept a temporary fall of up to 40% while the thesis holds, and the mandate stays 100% individual US stocks with no bond ETF or cash sleeve. v015's dated two-feed price checks and bounded event audit, and v013/v012's method repairs, are accepted as historical evidence and as methods.
- **Changed:** this release is the all-stock redesign that v016's brief asked the next allocator to build. It re-underwrites candidates on filings (all 500 dossiers) instead of carrying over v014/v015 weights, and it does not carry over their PG/PEP/PEG defensive substitutions, which were motivated by the old 15–20% tolerance.
- **Rejected:** applying v015's old-basket return bands (4–8% a year) to this different portfolio; treating 40% as a guaranteed loss floor; treating several agent reviews as independent economic sources (the same applies to this report's own audits).
- **Unresolved:** v012–v015's individual price and event claims were not re-verified here; actual positions and tax/account facts; prices and filings after 25 September were checked only for the names re-assessed on 5–6 October; Codex's entry limits are not reconciled against this release's valuations for names that differ.
<!-- /SECTION:V005 -->

<!-- SECTION:APPX -->
## Appendix A. Technical notes (for specialists)

The core sections above are written for a non-specialist. This appendix holds the statistics and methods behind them, and the register of independent checks.

### A.1 Backtest statistics (2012-01 to 2026-08, against the S&P 500 total return)

| Strategy | Compound gap a year | Average yearly gap | 95% range for the average gap | t-stat (Newey-West) |
|---|---|---|---|---|
| Model top 30, monthly | −2.6% | −2.0% | −5.6% to +1.5% | −1.12 |
| Model top quintile (~85 names) | −1.8% | −1.6% | −4.2% to +1.1% | −1.16 |
| Sleeve rule as pre-committed | −4.3% | −3.7% | −7.7% to +0.3% | −1.81 |
| 70% S&P 500 + 30% sleeve rule | −1.2% | −1.1% | −2.3% to +0.1% | −1.81 |
| Equal-weight S&P 500 (point-in-time) | −1.1% | −0.8% | −3.4% to +1.8% | −0.60 |

The t-stat is the average monthly gap divided by its standard error. The Newey-West method widens that error to allow for correlated neighbouring months. Values between −2 and +2 are within what chance alone produces. Every 95% range contains zero or lies almost entirely below it: there is no evidence of an edge. B1's 500 random re-weightings of the four factor families (a Dirichlet test) found 1.4% that beat the S&P 500. Daily worst falls were re-derived without B1's code: top 30 −43.7%, sleeve rule −41.8% (B1: −44.4% and −41.7%).

### A.2 Simulation method and sensitivity

Allocation odds use a stationary block bootstrap (Politis-Romano) of daily returns from 2005-01-03 to 2026-09-25: 20,000 paths, geometric blocks with a mean of 21 trading days, random seed 7. Each path is re-centred to the scenario's compound market return (bear 2%, base 6%, bull 9%), and T-bills earn 4%. The stock satellite is simulated with zero alpha. The mix is rebalanced daily to its target weights, a simplification against the quarterly rule; the crisis replays in §7 rebalance quarterly. Changing the block length barely moves the base-case odds:

| Allocation | 5-day blocks: P(gain 5y / 10y), P(fall >20% in 5y) | 21-day blocks | 63-day blocks |
|---|---|---|---|
| Index only (100/0/0) | 78% / 86%, 86% | 79% / 88%, 81% | 81% / 88%, 79% |
| Growth (80/20/0) | 78% / 86%, 85% | 80% / 88%, 79% | 82% / 89%, 76% |
| Moderate (55/15/30) | 86% / 94%, 47% | 87% / 95%, 47% | 89% / 95%, 46% |
| Cautious (35/10/55) | 94% / 98%, 7% | 95% / 99%, 10% | 95% / 99%, 14% |
| Defensive (15/10/75) | 99% / over 99%, under 1% | 99% / over 99%, under 1% | over 99% / over 99%, under 1% |

### A.3 Risk model

Sleeve risk uses the plain sample covariance of 754 days of returns (2023-09-25 to 2026-09-25), complete cases only. Results: volatility 14.0%, tracking error 12.9% (sample standard deviation), average pairwise correlation 0.20. The effective number of bets is 18.2 by weight (1/Σw²) and 17.2 by risk (1/Σ risk-share²). B2's Ledoit-Wolf shrinkage hit its 1.0 ceiling (intensity 1.0); risk shares from that estimator are proportional to squared weights, so they are not used. A one-factor split against the S&P 500 attributes 37% of variance to the market (portfolio beta 0.56) and 63% to company-specific moves. The two need not sum to exactly 100%, because the residuals are estimated.

An independent re-computation from raw D2 prices, without the risk engine's code (`code/lead_check_risk_contrib.py`), reproduces volatility, correlation, tracking error and every risk share to within 4.7e-07 (pass: True).


### A.4 Register of independent checks

| Check | What it re-derived | Result | File |
|---|---|---|---|
| B1X | Blind re-implementation of the whole backtest | Matches B1 within 0.04 pts/yr; live-rank correlation 0.976 | `outputs/b1x_report.md` |
| Daily drawdown check | Daily worst falls of the top 30 and the sleeve rule, without B1's code | −43.7% vs −44.4%; −41.8% vs −41.7%; same day (23 Mar 2020) | `outputs/lead_check_daily_dd.json` |
| V1X | Valuation inputs and methods of the Loop-1 holdings, from SEC filings | 261 of 297 checks pass (87.9%); no verdict or base-case sign changes | `outputs/v1x_verification.md` |
| V2R | REIT funds from operations rebuilt from filings | HST: attractive → fair; FRT: attractive → fair; UDR: attractive → attractive; PSA: fair → fair | `outputs/v2r_reit_valuation.md` |
| Q01–Q15 triage | Quick research pass on every S&P 500 company without a dossier: quality, growth, red flags, price vs growth | 455 scored, 296 advanced to full-diligence queue | `outputs/Q*_triage.json` |
| Diligence wave 1 | Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria) | 45 names researched; 250 still queued after this wave | `data/full_diligence_wave1.json` |
| Diligence wave 2 | Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria) | 45 names researched; 205 still queued after this wave | `data/full_diligence_wave2.json` |
| Diligence wave 3 | Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria) | 45 names researched; 160 still queued after this wave | `data/full_diligence_wave3.json` |
| Diligence wave 4 | Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria) | 45 names researched; 114 still queued after this wave | `data/full_diligence_wave4.json` |
| Diligence wave 5 | Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria) | 45 names researched; 68 still queued after this wave | `data/full_diligence_wave5.json` |
| Diligence wave 6 | Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria) | 45 names researched; 23 still queued after this wave | `data/full_diligence_wave6.json` |
| Diligence wave 7 | Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria) | 23 names researched; 0 still queued after this wave | `data/full_diligence_wave7.json` |
| Diligence wave 8 | Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria) | 159 names researched; 0 still queued after this wave | `data/full_diligence_wave8.json` |
| DA series total (DA4–DV09) | All independent dossier fact-checks against SEC filings, cumulative | 961 facts: 654 pass, 101 minor, 157 fail (every fail corrected in its dossier), 49 unverifiable | `outputs/da*_factcheck.json` |
| DA4 | Load-bearing dossier facts (6 holdings, 4 excluded names) against SEC filings | 52 facts: 50 pass, 1 minor, 0 fail, 1 unverifiable | `outputs/da4_factcheck.md` |
| DA5 | Load-bearing dossier facts of the 8 holdings no auditor had checked | 40 facts: 36 pass, 1 minor, 1 fail, 2 unverifiable | `outputs/da5_factcheck.md` |
| DA6 | Load-bearing dossier facts of BKNG, BR, BX, CMCSA, DG, EG, NOW against SEC filings | 27 facts: 23 pass, 1 minor, 2 fail, 1 unverifiable | `outputs/da6_factcheck.md` |
| DA7 | Load-bearing dossier facts of GM, HBAN, LVS, RJF against SEC filings | 26 facts: 18 pass, 3 minor, 5 fail, 0 unverifiable | `outputs/da7_factcheck.md` |
| DA8 | Load-bearing dossier facts of ADP, AMP, CRH, DOV, PGR against SEC filings | 33 facts: 28 pass, 4 minor, 1 fail, 0 unverifiable | `outputs/da8_factcheck.md` |
| DA9 | Load-bearing dossier facts of AXP, MA, MSCI against SEC filings | 21 facts: 20 pass, 1 minor, 0 fail, 0 unverifiable | `outputs/da9_factcheck.md` |
| DA10 | Load-bearing dossier facts of CAH, COR, VEEV against SEC filings | 21 facts: 20 pass, 0 minor, 1 fail, 0 unverifiable | `outputs/da10_factcheck.md` |
| DA11 | Load-bearing dossier facts of BALL, EXC, STE against SEC filings | 21 facts: 19 pass, 2 minor, 0 fail, 0 unverifiable | `outputs/da11_factcheck.md` |
| DA12 | Load-bearing dossier facts of GDDY, PPG, USB against SEC filings | 19 facts: 18 pass, 0 minor, 1 fail, 0 unverifiable | `outputs/da12_factcheck.md` |
| DA13 | Load-bearing dossier facts of BR, GDDY against SEC filings | 3 facts: 1 pass, 1 minor, 1 fail, 0 unverifiable | `outputs/da13_factcheck.md` |
| DA14 | Load-bearing dossier facts of SO, TJX against SEC filings | 14 facts: 13 pass, 0 minor, 1 fail, 0 unverifiable | `outputs/da14_factcheck.md` |
| DA15 | Load-bearing dossier facts of BALL, DOV, EXC, MA, SO, STE, USB against SEC filings | 14 facts: 13 pass, 1 minor, 0 fail, 0 unverifiable | `outputs/da15_factcheck.md` |
| DA16 | Load-bearing dossier facts of ADP, AXP, BR, CAH, HBAN, PGR, PPG against SEC filings | 30 facts: 25 pass, 1 minor, 1 fail, 3 unverifiable | `outputs/da16_factcheck.md` |
| DA17 | Load-bearing dossier facts of COR, CRH, GDDY, LVS, TJX, VEEV against SEC filings | 29 facts: 28 pass, 0 minor, 0 fail, 1 unverifiable | `outputs/da17_factcheck.md` |
| DA18 | Load-bearing dossier facts of MCK, PTC, RMD, WEC against SEC filings | 24 facts: 20 pass, 1 minor, 3 fail, 0 unverifiable | `outputs/da18_factcheck.md` |
| DA19 | Load-bearing dossier facts of LH, RSG against SEC filings | 14 facts: 12 pass, 1 minor, 1 fail, 0 unverifiable | `outputs/da19_factcheck.md` |
| DA20 | Load-bearing dossier facts of LH, RSG against SEC filings | 9 facts: 5 pass, 2 minor, 2 fail, 0 unverifiable | `outputs/da20_factcheck.md` |
| DVH1 | Load-bearing dossier facts of ACGL, ACN, ALLE, BRK-B, INTU, SNA, TEL, V, WFC, WTW against SEC filings | 69 facts: 41 pass, 9 minor, 18 fail, 1 unverifiable | `outputs/dv/DVH1_factcheck.md` |
| DV02 | Load-bearing dossier facts of ADSK, AEE, AEP, AES, AFL, AIG, AIZ, AJG, AKAM, ALB against SEC filings | 74 facts: 53 pass, 8 minor, 12 fail, 1 unverifiable | `outputs/dv/DV02_factcheck.md` |
| DVH2 | Load-bearing dossier facts of APP, BIIB against SEC filings | 45 facts: 27 pass, 8 minor, 6 fail, 4 unverifiable | `outputs/dv/DVH2_factcheck.md` |
| DVH3 | Load-bearing dossier facts of RTX against SEC filings | 28 facts: 13 pass, 7 minor, 6 fail, 2 unverifiable | `outputs/dv/DVH3_factcheck.md` |
| DVH4 | Load-bearing dossier facts of ABNB, CRM, DECK, EOG, EXPE, FRT, FSLR, LMT, ULTA, ZBRA against SEC filings | 119 facts: 55 pass, 18 minor, 37 fail, 9 unverifiable | `outputs/dv/DVH4_factcheck.md` |
| DVH5 | Load-bearing dossier facts of F, FIS, LDOS, PCG against SEC filings | 55 facts: 34 pass, 8 minor, 9 fail, 4 unverifiable | `outputs/dv/DVH5_factcheck.md` |
| DVH6 | Load-bearing dossier facts of AMCR, BRO, CPAY, FDX, KKR, OMC, PYPL, VZ against SEC filings | 101 facts: 42 pass, 15 minor, 29 fail, 15 unverifiable | `outputs/dv/DVH6_factcheck.md` |
| DV09 | Load-bearing dossier facts of CI, CIEN, CINF, CL, CLX, CME, CMG, CMI, CMS, CNC against SEC filings | 73 facts: 40 pass, 8 minor, 20 fail, 5 unverifiable | `outputs/dv/DV09_factcheck.md` |
| C1 | Every number in the report traced to its source file | 1216 checked, 1214 matched, 2 mismatch (each fixed before release); audited build 2026-10-06T22:46:25 | `outputs/c1_consistency.md` |
| X1 | Claims inherited from Codex's release v005 | 23 of 26 confirmed; minor difference 1, not confirmed 1, unverifiable 1 | `outputs/x1_v005_verification.md` |
| Risk re-computation | Sleeve volatility, tracking error, correlation and risk shares from raw prices | pass: True | `outputs/lead_check_risk_contrib.json` |
| D2R | Re-download of the 408 'no price data' symbols | Root cause found (retry logic); 0 recovered because the names were acquired and purged; coverage unchanged | `outputs/d2r_report.md` |
| R3 | UAE implementation and tax facts | IBKR entity and protection confirmed; fund, withholding and estate-tax facts re-verified; open items labelled | `outputs/r3_implementation_verification.md` |
| DA1–DA3 | Prices and corporate actions; SEC fundamentals against filing documents; estimates | See each report for pass rates and fixes | `audit/da1_data_audit.md, da2, da3` |

### A.5 Per-holding verification

**Verification gate: PASS.** Every holding has an independent multi-fact check of its dossier against SEC filings (the DA series), and every failed fact is answered by a dated correction in the dossier. A release cannot be packaged unless this gate passes.

| Stock | Valuation model (V1) | Independent valuation check | Analyst view vs V1 | Dossier facts checked by |
|---|---|---|---|---|
| **CVS** | attractive | V1X: 13/14 checks pass; verdict unchanged | cheap (consistent) | A1 (loop 11); A2 (loop 11); A3 (loop 6); DA5: 5 facts, 0 fail |
| **ACN** | attractive | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A2 (loop 11); DVH1: 6 facts, 0 fail |
| **BKNG** | attractive | V1X: 13/14 checks pass; verdict unchanged | attractive (differs from V1) | A2 (loops 1–2); DA6: 4 facts, 0 fail |
| **CAH** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A1 (loop 6); A2 (loop 6); DA10: 7 facts, 0 fail; DA16: 5 facts, 0 fail |
| **BIIB** | attractive | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | DVH2: 24 facts, 2 fail (corrected in dossier) |
| **FDX** | attractive | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | DVH6: 15 facts, 6 fail (corrected in dossier) |
| **GDDY** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A1 (loop 7); A1 (loop 8); A2 (loop 7); A2 (loop 8); A2 (loop 9); DA12: 6 facts, 0 fail; DA13: 1 facts, 0 fail; DA17: 5 facts, 0 fail |
| **ACGL** | attractive | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A1 (loop 11); DVH1: 6 facts, 0 fail |
| **ADSK** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (–) | DV02: 10 facts, 3 fail (corrected in dossier) |
| **WFC** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A2 (loop 11); A3 (loop 11); DVH1: 6 facts, 1 fail (corrected in dossier) |
| **AMCR** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (–) | DVH6: 13 facts, 2 fail (corrected in dossier) |
| **VZ** | attractive | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | DVH6: 12 facts, 2 fail (corrected in dossier) |
| **FSLR** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | DVH4: 13 facts, 4 fail (corrected in dossier) |
| **BR** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A2 (loop 3); A3 (loop 6); A3 (loop 7); A3 (loop 8); DA13: 2 facts, 1 fail (corrected in dossier); DA16: 4 facts, 0 fail; DA6: 4 facts, 1 fail (corrected in dossier) |
| **INTU** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | DVH1: 8 facts, 4 fail (corrected in dossier) |
| **OMC** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | DVH6: 13 facts, 2 fail (corrected in dossier) |
| **COR** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A2 (loop 6); A2 (loop 7); A3 (loop 6); DA10: 7 facts, 1 fail (corrected in dossier); DA17: 5 facts, 0 fail |
| **WTW** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A3 (loop 11); DVH1: 9 facts, 4 fail (corrected in dossier) |
| **FIS** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (–) | DVH5: 12 facts, 1 fail (corrected in dossier) |
| **V** | – | Dossier reconciles with V1 in §7 (added after V1X ran) | cheap (consistent) | A3 (loop 11); DVH1: 8 facts, 1 fail (corrected in dossier) |

Every holding carries a primary-source dossier. The fact-check sources are independent agents or auditors who re-read the SEC filings or company releases behind the dossier's load-bearing numbers.
<!-- /SECTION:APPX -->
