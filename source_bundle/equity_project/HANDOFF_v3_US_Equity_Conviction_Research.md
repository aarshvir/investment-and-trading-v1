# HANDOFF v3 — US Equity Multi-Agent Research: Inputs, Methodology, Outputs (end-to-end)

**Owner:** Aarsh (Dubai, UAE resident) · **Prepared by:** Claude (claude.ai chat) · **Market data as of:** US close 24 Sep 2026 · **Handoff date:** 25 Sep 2026

> **Purpose:** A single file that lets a new chat or coding session continue without asking the owner anything already answered. It contains:
> - every owner instruction, verbatim;
> - every output delivered;
> - the full methodology (v0 → v3), with every parameter;
> - all results, the errors found and fixed, and open items;
> - the complete source code (Appendix A), the dashboard template (Appendix B) and key result files (Appendix C).
>
> A zip with all scripts and the downloaded data ships alongside.

---

## 0. TL;DR — current state (read first)

**The final answer is the v3 "Conviction portfolio".** It is target-independent: the owner explicitly asked that it NOT depend on his 15% hurdle or anyone's target. It has 14 US stocks, ranked and weighted, chosen by 10 independent "lens agents" voting on all 497 S&P 500 stocks. Each verdict was stress-tested with 500 threshold re-runs.

**Key honest findings:**
- **No individual stock can carry 90% confidence.** A point-in-time test of the conviction filter showed its picks rose in only 56–64% of cases over the next year. That is no better than the whole universe (58–61%).
- **Portfolio-level ~90% is attainable:** 50% S&P 500 index fund + 50% the 14 stocks → **90% simulated odds of profit over 5 years**, 10.7% expected per year.
- **Self-grade: 92/100.** Missing: earnings-call transcripts and an order sheet.

**Live dashboard (16 tabs):** https://claude.ai/artifact/U2RjG3tNLgLfVCF55x6cEf
- First tab: "★ Conviction portfolio (final)".
- Then 7 v2 tabs and 8 v1 tabs. All tabs are kept; never remove any.

**Next action pending from the owner:** USD amount + broker (IBKR or Vested). Then produce a click-by-click order sheet covering both the index half (Irish-domiciled UCITS S&P 500 fund) and the 14 stocks.

### 0.1 Final portfolio (v3)

"Robustness" = share of 500 re-runs, with every lens threshold moved ±20% at random, in which the stock stayed on the conviction list.

| Rank | Ticker | Company | Tier | Weight | Robustness | Lenses passed | Conservative E[R] | Fwd P/E | Volatility |
|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA | Nvidia | Core | 10.0% | 98% | 10/10 | 19.0% | 14.3 | 38% |
| 2 | CPAY | Corpay | Core | 7.3% | 100% | 10/10 | 11.9% | 12.7 | 37% |
| 3 | AMP | Ameriprise | Core | 7.0% | 99% | 9/10 | 15.0% | 9.4 | 26% |
| 4 | RL | Ralph Lauren | Core | 10.6% | 100% | 9/10 | 11.2% | 16.8 | 35% |
| 5 | AME | Ametek | Core | 8.4% | 98% | 9/10 | 8.4% | 25.8 | 24% |
| 6 | SNA | Snap-on | Conviction | 7.3% | 82% | 9/10 | 9.2% | 17.2 | 20% |
| 7 | ABNB | Airbnb | Conviction | 10.6% | 70% | 9/10 | 9.1% | 24.5 | 36% |
| 8 | NTAP | NetApp | Supporting | 8.0% | 60% | 9/10 | 12.9% | 17.7 | 44% |
| 9 | PAYX | Paychex | Supporting | 5.5% | 55% | 9/10 | 10.7% | 15.9 | 30% |
| 10 | MSFT | Microsoft | Supporting | 8.2% | 66% | 10/10 | 9.3% | 21.0 | 33% |
| 11 | IBKR | Interactive Brokers | Supporting | 4.0% | 55% | 9/10 | 10.3% | 28.1 | 40% |
| 12 | HIG | Hartford | Supporting | 4.0% | 60% | 9/10 | 9.1% | 9.2 | 20% |
| 13 | ALLE | Allegion | Supporting | 5.1% | 58% | 9/10 | 9.7% | 15.6 | 27% |
| 14 | AIZ | Assurant | Supporting | 4.0% | 50% | 10/10 | 8.8% | 11.2 | 22% |

**Portfolio statistics** (20,000-path block bootstrap on 10 years of monthly returns, re-centred to the conservative expected return):

| Metric | Value |
|---|---|
| Expected return | 11.4% per year |
| Volatility | 18.9% |
| Odds of profit, 1 year | 72% |
| Odds of profit, 5 years | 87% |
| Odds of doubling in 5 years | 28% |
| Median 5-year annualised return | 9.7% |
| 5th-percentile 1-year return | −20.3% |
| Odds of a 1-year loss of 20% or worse | 5.2% |
| Odds of 15%+ in 1 year | 41% |
| Replay: 2022 | −19.1% |
| Replay: COVID (Feb–Mar 2020) | −21.8% |
| 10-year max drawdown | −26.2% |

**Blends** (same simulation; the S&P expected return is set at 10%):

| Mix | E / yr | Volatility | 1-yr odds of profit | 5-yr odds of profit | 5th-pct 1-yr |
|---|---|---|---|---|---|
| 100% 14 stocks | 11.4% | 18.9% | 72% | 87% | −19.6% |
| 50% index / 50% stocks | 10.7% | 16.7% | 75% | **90%** | −16.1% |
| 70% index / 30% stocks | 10.4% | 16.0% | 76% | 91% | −14.9% |
| 100% S&P index | 10.0% | 15.2% | 76% | 92% | −13.4% |

**Near-misses and why they were excluded:**

| Ticker | Reason |
|---|---|
| TPR | Same sub-industry as RL (1 name per sub-industry) |
| TROW | Same sub-industry as AMP |
| ADP | Conservative E 7.7% < 8% |
| EOG | E 6.4%; revenue shrinking |
| ITW | E 7.7% |
| V | E 6.9% |
| BMY | E 7.4% |
| CB | E 6.1% |
| TRV | E 3.2% |
| EBAY | E 6.9% |

**UAE-resident note:** Hold the index half via an Irish-domiciled UCITS S&P 500 fund (e.g., iShares CSPX or Vanguard VUAA; verify tickers and TER at order time). This avoids US estate tax on US-situs assets above $60k and cuts dividend withholding from 30% to 15%.


---

## 1. Owner profile & standing interaction contract (MUST follow)

- **Who:** Ex-Bain partner (Bain Dubai; Accenture Strategy London; IIT Delhi / IIM Ahmedabad). Now a Director in the MD's Office at DAMAC Properties. Lives in Dubai, UAE. **Completely non-technical.**
- **Output style:**
  - MBB/Bain-partner grade: structured, answer-first (verdict in the first sentence), numbers not adjectives.
  - Tables over prose for comparisons.
  - Exactly **one next step** at the end, never a menu.
- **Formats:**
  - **HTML** for anything he reads, with a dark aesthetic: background `#0a0e1a`, gold accent `#c8a35a`.
  - **Markdown** for handoffs and prompts.
- **Instructions to him:**
  - Always click-by-click, assuming a "30-year-old noob" (e.g., "Windows key → type PowerShell → Enter → paste exactly …").
  - Explain mechanisms like to a smart 18-year-old with no tech knowledge.
- **Autonomy:** Maximum. Do everything possible without him. Don't question an instruction more than once; just do it. His time budget is ~30 min/week.
- **Honesty:**
  - Honest 1–100 self-grades with no diplomatic inflation.
  - Never grant an innumerate target to preserve rapport. Correct the premise first, then deliver the closest legitimate version.
  - Concede errors plainly and fix them in the same turn.
  - Zero invented detail.
- **Iteration rule (flagged twice by owner):** When iterating on a dashboard or artifact, **build on the existing benchmark file**. Only ADD or improve. **NEVER rebuild from scratch, simplify, or remove features.**
- **Voice input:** He dictates via Whisper Flow, so expect transcription errors. Decode from context rather than asking (examples in §2.1).
- **Token use:** Optimise token usage without compromising quality.
- **Claude auth:** $200 Max subscription is his only Claude auth. **Never use API keys for Claude work.**
- **Investment context relevant to this project:**
  - UAE resident, with US brokerage via **Interactive Brokers (IBKR)** and **Vested**.
  - Runs an algorithmic/IBKR trading practice separately. Has used a Minervini VCP methodology.
  - Earlier personal conviction ranking: LLY > META > NVDA > AMZN > PLTR.
  - Idle cash is the intended funding source; keep a 6–12-month expense buffer outside equities.
- **Tax flags for a UAE resident holding US stocks** (raise when constructing orders):
  - US estate tax on US-situs assets above **$60k** for non-resident aliens (up to 40%).
  - **30% US withholding** on dividends (no US–UAE income-tax treaty).
  - Mitigation to discuss: Irish-domiciled UCITS ETFs for large allocations.
- **Disclaimer:** Always add a short "not financial advice" line.

---

## 2. Full chat log (owner's words + what was delivered)

### Turn 1 — Owner
> "Top 10 stocks in US market if i need to buy today. think deep. you know my investment profile. target 20%+ guaranteed low risk YOY returns"

**Delivered:** Pushback on the premise. "Guaranteed" = the ~5% 10-yr Treasury; the S&P historical average is ~10%; Buffett ~20% with −50% drawdowns.

**v0 list** (news-based, NOT screened):

| Stock | Weight |
|---|---|
| GOOGL | 14% |
| META | 12% |
| MSFT | 12% |
| LLY | 10% |
| AMZN | 10% |
| NVDA | 10% |
| BRK-B | 10% |
| AVGO | 8% |
| V | 8% |
| TSM | 6% |

Also covered: 3-tranche entry and the UAE estate-tax flag.

### Turn 2 — Owner
> "do an end to end audit and show me that you did analysis on atleast 50 stocks and which stocks"

**Delivered:**
- Conceded that v0 was ~10 names, not a screen. Self-grade **58/100**.
- Screened 100 stocks (his 90-stock daily-routine universe + 10 quality adds) with live yfinance data.
- 5 pillars: Quality 25, Risk 25, Growth 20, Valuation 20, Trend 10. Plus gates.
- 7/10 of v0 survived. META, MSFT and AMZN dropped; CVX, BLK and ABBV added.
- **Artifact:** https://claude.ai/artifact/9dYtL85m4iVSaktuBtuAjW

### Turn 3 — Owner
> "I'm not happy with the amount of the analysis. I want this to be a detailed analysis that will wow even the top private equity firms, banks, or investment houses. It should be a detailed analysis where 510 agents should come together, talk to each other, refute each other's analyses, provide inputs, and have handoffs, etc. At the end, there should be 2 to 3 audit agents that do an end-to-end audit and make sure that I get the maximum amount of output: 1. explore the top 500 company universe … 2. short list of 100 … 3. 1-page output for each of those 100 … 4. short list down to 30 … 5. extreme, in-depth, multiple analysis and ranking … multiple valuation, momentum, dips, pricing, Warren Buffett … Read the last 2 years of earnings reports … 6. MBB/Blackstone level of diligence on each of those 30 … confidence score on each stock, upside and downside … build a kickass dashboard … Just wow me."

**Decoded:** "510 agents" = "5 to 10 agents".

**Delivered (v1):**
- 15 specialist agents + 3 auditors, run as rule-based analysis modules with file handoffs (explicitly disclosed as modules, not separate AI models).
- Funnel: 497 → 100 (one-pagers) → 30 (deep dives) → final 10.
- Web-verified diligence notes for 8 names.
- 8 self-caught model errors.
- **Artifact (v1 dashboard, the BENCHMARK to build on):** https://claude.ai/artifact/U2RjG3tNLgLfVCF55x6cEf
- Self-grade **78/100**.

### Turn 4 — Owner
> "Keep running till your self-grade goes above 90, and at least my hurdle rate is 15%. I need a realistic chance of making 15%+ and at least a 1-in-4 chance of making 0.5%+. Of course, you have to do an in-depth analysis. I think you have done a very cursory analysis, and I'm not happy with it. You have to go deep and find me the best answers. Please deploy multiple parallel agents and do the analysis into a very, very good"

**Decoded:** "0.5%+" = **50%+** (0.5 as a decimal). Alternatives 20%/25% were also reported. Confirm with the owner only if it changes the build.

**Delivered (v2):**
- Point-in-time backtest **proved v1's low-volatility tilt was wrong**.
- Redesigned model (v3 scoring) validated.
- 467 SEC earnings releases read.
- 3-method expected returns with shrinkage.
- Resampled optimiser; 20,000-path bootstrap.
- 7 more errors fixed.
- Self-grade **91/100**.
- **v2 dashboard not yet built.**

### Turn 5 — Owner (this handoff)
> "Give me your output and the entire chat logic that I gave to you, everything detailed in Markdown format. I want to give it to another code chat to work on it."

### Turn 6 — Owner
> "Keep running recurring loops in 8-10 agents in parallel in 2-3 audit loops, and then check your self-grade score and work on improving it. You will keep running this loop if required overnight till you reach a score of 95+."

**Delivered:**
- Told the owner that the chat cannot run overnight: work stops when a reply is sent.
- Ran 3 audit loops as parallel auditor modules (§8).
- Hand-read diligence notes for all 20 v2 holdings.
- **v2 dashboard published** on the same artifact link. v1 tabs were kept and 7 v2 tabs added.
- Honest grade **92/100**. 95+ needs transcripts, point-in-time analyst-estimate history, and a survivorship-free index history. These are data-access limits, not compute limits.

### Turn 7 — Owner
> "Okay, forget about all this. I can keep giving you all shitty numbers, and you'll come up with different answers or different points in time. Rather, this analysis: you have your own self-score of 90+, where you are convinced that you would want to put money in these 10 to 20 stocks, rank them, and divide. This should be based on thorough analysis of all 500 stocks again, right? It's not based on my hurdle rate. It's not based on anyone else's hurdle rate. It's not based on someone else's answer. You have to be convinced that these are 90 stocks, these are whatever stocks on which I'm 90% confident, or any key investor would be 90% confident to put their money in. Keep running these loops with 8-10 parallel agents, multiple audit agents, till you get to your own score of 90+. Give me a perfect answer."

**Decoded:** "these are 90 stocks" = the stocks one would be **90% confident** in.

**Owner's valid critique:** earlier answers moved with the target (the hurdle-optimised v2). The fix is a **target-independent conviction engine (v3)**. Three loops were run (§9), and the conviction tab was added as the dashboard's first tab. Answer: no stock earns 90%; the portfolio reaches ~90% 5-year odds when blended 50/50 with an index.

### Turn 8 — Owner (this handoff)
> "Give the entire output, the entire inputs you got, and your entire methodology as an output in Markdown format so that I can just transfer to another chat. Tell me what you did end-to-end"


### 2.1 Decoding table (Whisper errors)

| Heard | Meant |
|---|---|
| "510 agents" | 5–10 agents (15 + 3 auditors built) |
| "1-in-4 chance of making 0.5%+" | 1-in-4 chance of making 50%+ (most likely). Also report 20% and 25% odds |
| "short the short list" | cut the shortlist down |
| "these are 90 stocks" (Turn 7) | the stocks one would be 90% confident in |

---


## 3. The owner's mandate (consolidated, latest wins)
1. **Latest (Turn 7) — governs:** Pick 10–20 stocks I'm genuinely convinced of, ranked and weighted.
   - Based on a thorough analysis of all ~500 S&P 500 stocks.
   - **Not** tied to his 15% hurdle, anyone's hurdle, or anyone else's answer.
   - The target is stocks that he, or any key investor, would be "90% confident" putting money into.
   - Run loops with 8–10 parallel agents plus multiple audit agents until the self-score is 90+.
   - "Give me a perfect answer."
2. **Earlier requirements still in force:**
   - Funnel 500 → 100 (1-page each) → 30 (deep MBB/Blackstone-grade diligence) → ranked.
   - Methods: multiple valuations, momentum, dips, pricing, Buffett lens, last 2 years of earnings reports.
   - Per-stock confidence score, upside and downside.
   - HTML dashboard (dark `#0a0e1a` / gold `#c8a35a`).
   - 2–3 audit agents.
3. **Stored preference:** 15% hurdle rate (kept in his profile, but explicitly **not** to drive stock selection per Turn 7).
4. **Honesty standard:** no inflated grades; correct premises with data (per-stock 90% is unattainable; see §9.3).

## 4. Environment & data sources (reproduction)

- **Python 3.12:** `yfinance`, `pandas`, `numpy`, `scipy`, `requests`, `lxml`. Node + `jsdom` was used only for headless render tests.
- **Universe:** Wikipedia "List of S&P 500 companies" (503 rows). Dual share classes removed (GOOG, FOX, NWS) → **497** usable.
- **yfinance endpoints used:**
  - Prices: `download` (3y and 11y daily, auto-adjusted).
  - Company data: `Ticker.info`.
  - Statements: `income_stmt`, `balance_sheet`, `cashflow` (annual, 4–5 yrs), `quarterly_income_stmt`, `quarterly_cashflow` (5 qtrs).
  - Estimates and actions: `get_earnings_dates(limit=12)` (8 reported qtrs = 2 yrs of reports), `eps_trend`, `eps_revisions`, `earnings_estimate`, `revenue_estimate`, `upgrades_downgrades`, `insider_purchases`, `news`.
- **Units gotcha:** `info['dividendYield']` is in **percent** (0.44 = 0.44%). Use `trailingAnnualDividendYield` (a fraction).
- **SEC EDGAR:**
  - Ticker→CIK map: `https://www.sec.gov/files/company_tickers.json`.
  - Filings list: `https://data.sec.gov/submissions/CIK##########.json`. Filter 8-K with items containing `2.02` since 2024-07-01.
  - Exhibit 99.1: via `/Archives/edgar/data/{cik}/{acc}/index.json`.
  - Send a User-Agent header. Stay ≤10 req/s (the script used 4 threads with a 0.15s sleep).
- **Runtime lessons:**
  - Background `nohup` jobs died when the tool call returned. Run in the foreground with `timeout 280–290` and **batch** (the info pull ran in 2×260 batches with ThreadPoolExecutor(16–20)).
  - SLSQP resampling at 150 runs × 4 portfolios timed out; 40 runs works.
- **Web research used:**
  - SEC 8-K releases for AIZ, CAH, HIG, BKNG, MDT, CL; call highlights for BMY.
  - McLean & Pontiff (2016, *Journal of Finance*): anomaly returns are **26% lower out-of-sample, 58% lower post-publication**. This justifies the 58% alpha shrink.

### 4.1 Run order (scripts in Appendix A)

| # | Script | Output |
|---|---|---|
| 1 | Universe pull (inline, §A.0) | `universe.csv` |
| 2 | Price pull (inline) | `close/high/low/volume.pkl` (3y) |
| 3 | `s1_info.py` (run until 503/503) | `info.json` |
| 4 | `s1_agents.py` (Stage 1, 497 → 100) | `s1.pkl` |
| 5 | `s2_pull.py 50` ×2 | `deep.pkl` |
| 6 | `s2_agents.py` (diligence + valuation) | `s2.pkl` |
| 7 | `s3_committee.py` | `s3_100.pkl`, `s3_30.pkl`, `overrides.pkl` |
| 8 | `audit.py` | `audit.json` |
| 9 | `cio.py` | `port.json` (v1 portfolio) |
| 10 | `assemble.py` | `dash.json` → inject into `dash_tpl.html` → `equity_audit_497.html` (**v1 dashboard**) |
| 11 | 11-yr price pull (inline) | `close10.pkl` |
| 12 | `bt_pull.py 250` ×2 | `fund_all.pkl` (statements for all 497) |
| 13 | `backtest.py` / `backtest2.py "<weights>" out.json` | point-in-time backtests |
| 14 | `bt10.py` | 10-yr factor backtest |
| 15 | `est_pull.py 200` ×2 | `est_all.pkl` (estimates for all 497) |
| 16 | `v3.py` | `v3.pkl` (**v2 scoring** + 3 return methods) |
| 17 | `edgar.py` | `edgar.pkl` (467 releases) |
| 18 | `edgar_read.py` | `edgar_read.json` |
| 19 | `opt.py` | `K.pkl`, `port2.json` (frontier + Recommended) |
| 20 | `assemble2.py` | `dash2.json` (v2 dashboard data, **not yet rendered**) |

---

### 4.2 Additional run order (Turns 6–7)

| # | Script | Output |
|---|---|---|
| 21 | `audit_loop1.py` | `audit_loop1.json`: holdings integrity, survivorship vs RSP, sensitivity |
| 22 | `notes2.py` | Hand-read notes for 20 v2 holdings + grade into `dash2.json` |
| 23 | Dashboard v2 | `v2tabs.js` injected into `dash_tpl.html` → `dash_tpl_v2.html` (replace `__DATA__` = `dash.json`, `__DATA2__` = `dash2.json`) |
| 24 | `conv.py` | `conv.pkl`: 10 lenses + 500 perturbations, all 497 |
| 25 | `edgar2.py "T1,T2,..."` then `edgar_read.py` | Release reader for new candidates (loop 2), then re-run `conv.py` |
| 26 | `backtest3.py "dict(Q=.20,G=.10,V=.35,M=.35,R=0)" out.json` | `bt_frames.pkl` → inline conviction-filter PIT test → `bt_conv.json` |
| 27 | `conv_port.py` | `conv_port.json`: final 14 + odds. Then the inline blend step adds `blend` to it |
| 28 | Inline assembly | Writes `CV` and `grade3` into `dash2.json`. `cvtab.js` is injected into `dash_tpl_v2.html` → `dash_tpl_v3.html` → `equity_audit_v3.html` |

## 5. v1 architecture (Turn 3) — agents, weights, gates

### Stage 1: Screening committee (497 stocks)

Percentiles are **sector-relative** for Quality and Valuation.

| Agent | Measures | Weight |
|---|---|---|
| A1 Quality & Moat (Buffett lens) | ROE, op margin, FCF margin, gross margin (sector-rel); FCF/NI conversion; net debt/EBITDA | 22% |
| A2 Growth | Revenue growth, EPS growth, forward/trailing EPS growth | 16% |
| A3 Valuation | Fwd P/E (sector-rel), EV/EBITDA (sector-rel), FCF yield, Street upside | 18% |
| A4 Momentum | Minervini 7-pt trend template, 6m RS vs S&P, 12m return, distance from 52w high | 12% |
| A5 Risk | Vol, downside vol, 3y max DD, worst rolling 12m, beta | 20% |
| A6 Street | Rec mean, target upside, short % float, # analysts | 12% |
| A7 Red Team | See below | — |

**A7 Red Team:**
- **Hard vetoes:** no forward profit; negative FCF (non-financials); 3y drawdown worse than −60%.
- **Soft flags (−2 each):** net debt >4× EBITDA; FCF/NI <0.5; payout >100%; short interest >8%; shrinking revenue; possible cyclical peak (EPS growth >200% with fwd P/E <12).

**Refutation rounds (logged):**

| Rule | Adjustment |
|---|---|
| Value-trap: Valuation >.75 & Momentum <.30 & Quality <.5 | −6 (kept if Quality ≥ .5) |
| Bubble: Momentum >.80 & Valuation <.25 & Growth <.70 | −6 |
| Cash-burn growth: Growth >.8 & FCF yield <1% | −3 |
| Risk refutes Street: Street >.8 & Risk <.25 | −4 |
| Buffett endorse: Quality >.8 & Risk >.7 & Valuation >.45 | +4 |
| Capital-allocation overrule of the red team | Cash-conversion flag withdrawn when OCF/NI ≥0.9 (growth capex, e.g., hyperscalers) |

**Shortlist:** top 100 non-vetoed, max 22 per sector.

### Stage 2: Diligence team (100 stocks)

**A8 Forensic Accountant:**
- Piotroski F-score (9 tests; N/A for banks/insurers).
- Altman Z (non-financials).
- Accruals ((NI−OCF)/TA).
- Interest cover.

**A9 Capital Allocation:**
- ROIC = EBIT(1−t) / (debt + equity − cash).
- 3y share-count change, buybacks, dividends.
- Growth-capex normalisation: FCF₀ = 0.7 × normalised NI when capex >1.5× D&A and OCF/NI ≥0.6, or when OCF/NI ≥0.9 and FCF <0.7 × NI.

**A10 Earnings Record:**
- Last 8 reported quarters: beats, average surprise.
- 90-day change in +1y EPS; revisions up/down (30d).
- Upgrades/downgrades (90d); insider net shares; news.

**A11 Intrinsic Value** — up to 4 methods; **median** used, each clipped to 0.3–2.5× price:
1. **Multiples:** EPS₊₁ᵧ × (0.7 × own fwd P/E + 0.3 × sector median).
2. **DCF:**
   - 5 years at g₁, then a 5-year linear fade to 3% terminal.
   - g₁ = median of (4y revenue CAGR, consensus EPS growth, revenue growth). The EPS term is dropped as a "one-off" when it is negative while CAGR is >5%. Clip −5%..30%.
   - WACC = weighted (Rf 4.9% + 4.5% × Blume-adjusted β clipped 0.7–1.4) and debt at Rf+1.5% after tax; floor 7.5%.
   - Plus reverse DCF (implied growth).
3. **Justified P/B** (banks & insurers only): (ROE − g)/(COE − g). Payment networks, exchanges/data, insurance brokers and asset managers are routed to DCF.
4. **Street mean target.**

**Scenarios:**
- Base = median fair value, clipped −30%..+45%.
- Bull = mean(10% EPS beat × 1.1 re-rate, Street high, base × 1.15).
- Bear = mean(15% EPS miss × 0.8 de-rate, p × e^(−vol), worst 12m loss (if negative), Street low), capped ≤ p × (1 − 0.5 × vol).
- Probability weights 25/50/25.

**Buffett checklist (8):**
1. ROE >15% in 3 of 4 yrs.
2. Interest cover >8× or net cash.
3. Operating margin stable/rising.
4. FCF positive every year.
5. Share count flat or shrinking.
6. ROIC >12%.
7. EPS grew in most years.
8. Fwd P/E <22.

### Stage 3: Investment committee

**s3 weights:** Screen 25, Intrinsic value 25, Earnings 15, Buffett 15, Forensic 10, Capital 10.

**Devil's-advocate vetoes:**
- Altman Z <1.8 **and** weak debt (cover <4 or ND/EBITDA >3.5). Four vetoes were overturned where debt was healthy: EXPE, BLK, CPAY, FANG.
- ≤3/8 beats.
- +1y EPS cut >10% in 90 days.
- Probability-weighted return < −5%.
- Peak-cycle trap.
- **Mandate:** vol >55%.

**Confidence (0–100):**

| Component | Weight |
|---|---|
| Data completeness | 15 |
| Agent agreement (1 − std of 6 agents / .35) | 20 |
| Analyst target dispersion | 15 |
| Beats/8 | 15 |
| Valuation-method dispersion | 20 |
| Balance sheet (Z, cover) | 15 |

**Top 30:** max 6 per sector. **Final rank** = 35% reward/risk (exp ÷ |bear|) + 25% confidence + 20% (Buffett + capital) + 20% earnings momentum.

**Tiers:**
- **A:** exp ≥8%, stability ≥0.7, confidence ≥50, rank ≤15.
- **B:** exp ≥3%.
- **C:** rest.

**Audit agents:**
- **X1 Data:** coverage, stale prices (0), price mismatches (0), 8 outliers flagged.
- **X2 Method & Robustness:** 500-run ±50% weight perturbation; top-30 median stability 100%. Fragile: VLTO, HAS, CSCO, UNP.
- **X3 Output:** scenario ordering (0 errors); reconciliation with earlier answers; 40% calibration haircut on modelled returns.

**CIO (v1):** one name per sub-industry, ≤3 per sector, ≤2 insurers, stability ≥0.7, exp ≥7%. Weights ∝ conf × exp / vol, clipped 5–15%.

### v1 results

**Final 10:**

| Stock | Weight |
|---|---|
| AIZ | 15.0% |
| HIG | 12.0% |
| MDT | 11.5% |
| BKNG | 10.7% |
| MA | 10.4% |
| CL | 10.2% |
| ADSK | 9.7% |
| CAH | 8.6% |
| BMY | 6.7% |
| NVDA | 5.1% |

**Portfolio stats:**

| Metric | Value |
|---|---|
| Model expected return | 17.3% |
| Calibrated expected (×0.6) | 10.4% |
| Volatility | 14.1% |
| 3y max drawdown | −12.3% |
| P(20%+), calibrated | 27% |
| Forward P/E | 13.3× |
| Confidence | 63 |

**Megacap outcomes:** MSFT #64/100, GOOGL #62, AAPL vetoed (overpriced), META #248/497, AMZN #140/497.

---

## 6. v2 "Hurdle-15" (Turn 4) — what changed and why

### 6.1 Backtest agent: v1 was wrong (point-in-time, 3 years)

Method:
- Rebalance each late September using fundamentals with a 90-day reporting lag and prices to date.
- Forward 12-month returns measured.
- Current S&P 500 constituents only (**survivorship bias**).

**v1 model (Q.25 G.18 V.20 M.14 R.23):**

| Start | S&P | Equal-wt univ | v1 top 30 | IC | Low-vol pillar IC | Momentum IC | Vetoed stocks |
|---|---|---|---|---|---|---|---|
| Sep-2023 | 33.8% | 35.4% | 23.9% | −0.072 | −0.136 | +0.18 | 47.0% |
| Sep-2024 | 15.8% | 14.5% | 10.6% | +0.132 | −0.051 | +0.20 | 38.8% |
| Sep-2025 | 15.7% | 17.9% | 8.0% | −0.178 | −0.255 | +0.14 | 39.0% |

**v3 composite — two untuned weightings, both positive every year:**

| Start | Q.20 G.10 V.35 M.35 R0: top 30 | IC | Top vs bottom quintile | Q.25 G.15 V.30 M.30 R0: top 30 | IC |
|---|---|---|---|---|---|
| Sep-2023 | 36.4% | .135 | 37.2 vs 22.4 | 35.8% | .112 |
| Sep-2024 | 21.3% | .212 | 21.0 vs −0.2 | 26.6% | .209 |
| Sep-2025 | 30.3% | .131 | 26.5 vs 1.4 | 27.0% | .079 |

**10-year monthly factor test** (top 50 equal-weight, current constituents, so survivorship-biased; compare vs equal-weight universe):

| Style | CAGR | Vol | Max DD | P(12m ≥15%) | P(12m ≥50%) | 2022 |
|---|---|---|---|---|---|---|
| Momentum 12-1 | 29.1% | 22.2% | −20.3% | 71% | 21% | −1.5% |
| Low volatility | 9.9% | 12.8% | −20.9% | 34% | 0% | −1.7% |
| Momentum + low vol | 11.4% | 13.8% | −19.8% | 40% | 0% | −11.6% |
| Momentum + trend, vol-capped | 15.5% | 16.8% | −20.2% | 49% | 2.8% | −7.3% |
| Equal-weight universe | 17.6% | 16.7% | −23.9% | 59% | 4.6% | −10.5% |
| S&P 500 | 13.9% | 15.4% | −24.8% | 48% | 0.9% | −19.4% |

**Conclusion:** Low-vol is removed as a return driver and kept as a constraint only. Momentum and value carry the model.

### 6.2 v3 scoring (all 497) — `v3.py`

**Pillars:**

| Pillar | Weight | Inputs |
|---|---|---|
| P_mom | 30% | 12-1 month momentum, 6m return, trend template/7 |
| P_emom | 20% | 90d change in +1y EPS, net revisions per analyst (30d), beat rate (8q), avg surprise, upgrades − downgrades (90d) |
| P_val | 30% | Building-block E[R] percentile, FCF yield (sector-rel), fwd P/E (sector-rel, lower better) |
| P_q | 20% | Stage-1 quality percentile |

**Gates:** stage-1 veto; vol ≤60%; fwd P/E >0. → **391 pass.**

**Growth-artifact guard:** if consensus g >35% while revenue growth <10%, set g = max(revenue growth, 0) + 10%. Fixed: MRK, FCX, ON, SW, IP, PSKY, TTWO, BA, WY, MOS.

**Beta:** 3-year weekly vs ^GSPC, replacing noisy 1-year daily betas.

### 6.3 Three independent expected-return methods (12-month)

1. **E_bb (building blocks)** = trailing dividend yield + net buyback yield (clip −5%..8%) + clip(0.7 × g, −25%, 30%) + re-rate.
   - g = +1y/0y consensus EPS growth, clipped −30%..60%, with a 30% optimism haircut.
   - Re-rate = clip((fair/fwd P/E)^(1/3) − 1, ±10%). Fair = sector median fwd P/E × (0.8 + 0.4 × Quality pct) × (1 + clip(g − sector median g, −0.2, 0.3)).
   - Total E_bb clipped −30%..40%.
2. **E_fac (factor)** = 10% market expectation × clip(0.67β₃ᵧ + 0.33, 0.6, 1.6) + α.
   - α = clip(2.8% × (v3 percentile among gated − 0.5)/0.44, ±3%).
   - The 2.8% top-end alpha = backtest top-30 excess over equal-weight (+6.7pp average) × (1 − 58%) McLean-Pontiff shrink.
3. **E_scen** = 0.6 × the v1 scenario expected return (only for the old 100).

**Combining:**
- E_final = mean of available methods. E_spread = max − min.
- **Shrinkage (Black-Litterman style):**
  - wc = conf2/100 × (1 − clip(E_spread/0.4, 0, 0.5)).
  - E_sh = wc × E_final + (1 − wc) × (10% × adjusted β).

### 6.4 Earnings-release reader (SEC EDGAR) — `edgar.py`, `edgar_read.py`

- **Scope:** 52 candidates (top 45 v3 gated, max 8/sector, plus the v1 portfolio). **467** 8-K Item 2.02 releases since Jul-2024 (≈9 per company).
- **Regex reading:**
  - Guidance **raise / cut / maintain**.
  - Counts: "record", "headwind", impairment, restructuring, investigation/subpoena, material weakness, going concern, buyback, AI, tariff.
  - gscore = (raises − cuts)/n.
- **Highest raisers:**
  - CAH 9/9
  - MDT 7/9
  - 6/9 each: PFE, BMY, ADSK, ADP, DD, FTNT, GPN, INCY
- **Cutters:** FCX (3 cuts), NEM (3 cuts / 2 raises), MO (3/5), GM (3/3), FANG (4/4).
- **Caveat:** insurers/networks that don't guide score 0 (neutral). Regex has some false positives, and "impairment" counts include tables. **No call transcripts were read.**

### 6.5 Confidence v2 & ranking of the 52

**conf2** = 100 × (0.30 × method agreement + 0.15 × completeness + 0.20 × beat rate + 0.20 × clip(0.5 + gscore, 0, 1) + 0.15 × quality). Method agreement = 1 − clip(E_spread/0.35).

**score2** = 35% E_final pct + 25% v3 + 15% conf2 + 15% gscore + 10% quality.

**Top 15:**

| # | Stock | score2 | E_final | conf2 | gscore |
|---|---|---|---|---|---|
| 1 | EXPE | 84.5 | 18.5% | 83 | 0.44 |
| 2 | HPE | 75.0 | 19.7% | 79 | 0.44 |
| 3 | GEN | 71.8 | 19.3% | 82 | 0.56 |
| 4 | CPAY | 71.2 | 12.2% | 83 | 0.44 |
| 5 | BMY | 69.6 | 8.8% | 93 | 0.67 |
| 6 | MMM | — | — | — | — |
| 7 | INCY | — | — | — | — |
| 8 | NVDA | — | — | — | — |
| 9 | BIIB | — | — | — | — |
| 10 | ADSK | — | — | — | — |
| 11 | GPN | — | — | — | — |
| 12 | SWK | — | — | — | — |
| 13 | NTAP | — | — | — | — |
| 14 | VTRS | — | — | — | — |
| 15 | AIZ | — | — | — | — |

### 6.6 CIO v2: optimiser + probability engine — `opt.py`

**Eligible (29 names):** E_sh ≥9%, conf2 ≥50, Quality ≥0.35.

**Constraints:**
- Max weight 10% if conf2 ≥75, else 7%.
- Sector ≤30%. **Sub-industry ≤12%.**
- Portfolio vol cap.
- Covariance: 3y weekly, shrunk 30% toward the diagonal.

**Optimiser:** maximise E_sh (SLSQP). **Resampled efficiency:** 40 runs, perturbing E by N(0, clip(E_spread/2, 2%, 12%)), then averaging weights. The "Recommended" portfolio = the resampled Hurdle trimmed to its 20 most robust names (weight × hit-rate).

**Probability engine:**
- Monthly returns of the portfolio over 10 years, re-centred to the forward E.
- Stationary-ish block bootstrap (3-month blocks), 20,000 paths.
- Stress replays: 2022 calendar year; Feb–Mar 2020.

---

## 7. v2 results (Hurdle-15 portfolio — SUPERSEDED by v3 §0.1; kept for record)

### 7.1 Recommended 20-stock portfolio

| Stock | Weight | Stock | Weight |
|---|---|---|---|
| GEN | 8.2% | BIIB | 4.6% |
| HPE | 7.8% | BBY | 4.6% |
| FIX | 6.7% | ADI | 4.5% |
| ADSK | 6.1% | AMP | 4.2% |
| SWK | 5.7% | DD | 4.1% |
| GPN | 5.2% | NEM | 3.9% |
| BKNG | 5.2% | NVDA | 3.8% |
| EXPE | 5.1% | INCY | 3.7% |
| VTRS | 4.9% | JBHT | 3.5% |
| IVZ | 4.7% | TROW | 3.5% |

**Portfolio stats:**

| Metric | Value |
|---|---|
| Expected return, conservative (shrunk) | **14.2%** |
| Expected return, raw model | 17.7% |
| Volatility | 16.8% |
| Beta | 1.16 |
| Weighted confidence | 75 |

**Probabilities (bootstrap):**

| Outcome | Probability |
|---|---|
| Return ≥ 0 | 75% |
| ≥15% | **46%** |
| ≥20% | 37% |
| ≥25% | 29% |
| ≥50% | **4%** |
| ≤ −10% | 11% |
| ≤ −20% | 4% (understated; honest estimate ~8–10%) |

**Distribution:** 5th percentile −18.1%, median 13.0%, 95th +47.9%.

**Stress replays:** 2022 −16.5%; COVID Feb–Mar 2020 −20.9%; 10-year max drawdown −27.8%.

**Concentration notes:** asset managers (IVZ + AMP + TROW) ≈12.4%; online travel (BKNG + EXPE) ≈10.3%.

### 7.2 Frontier

| Portfolio | # | E (shrunk) | Vol | β | P≥15% | P≥20% | P≥25% | P≥50% | P≤−20% | 2022 | COVID |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Guardian (resampled, vol 14%) | 17 | 12.1% | 14.3% | 0.90 | 42% | 30% | 21% | 0.9% | 2.1% | −15.6% | −18.5% |
| Balanced (resampled, 16%) | 25 | 13.1% | 15.1% | 1.07 | 44% | 34% | 24% | 1.4% | 2.6% | −18.1% | −18.1% |
| Hurdle (resampled, 18%) | 27 | 13.7% | 16.7% | 1.19 | 46% | 36% | 27% | 3.5% | 4.1% | −16.4% | −21.7% |
| Stretch (resampled, 22%) | 28 | 13.7% | 17.1% | 1.23 | 46% | 36% | 28% | 3.9% | 4.6% | −16.8% | −22.5% |
| **Recommended (20 names)** | 20 | **14.2%** | 16.8% | 1.16 | **46%** | 37% | 29% | 4.1% | 4.0% | −16.5% | −20.9% |
| Concentrated Hurdle (non-resampled) | 15 | 15.2% | 18.0% | 1.24 | 48% | 40% | 32% | 6.2% | 5.3% | −20.9% | −23.7% |
| S&P 500 reference | — | ~10% | ~15% | 1.00 | — | — | — | — | — | — | — |

### 7.3 v1 → v2 names

- **Kept:** ADSK, BKNG, NVDA.
- **Dropped:** AIZ, HIG, MDT, MA, CL, CAH, BMY. These were defensive/low-vol, and the backtest showed that tilt lagged.
- **Coverage gap:** most new names (GEN, HPE, FIX, SWK, GPN, VTRS, IVZ, BIIB, BBY, AMP, DD, JBHT, TROW) have machine-read releases only. They have **no human-style diligence notes yet** (open item).

---

## 7b. Feasibility maths the owner must see (M4 calibrated pushback)

**The 50%+ target:**
- Lognormal: P(R ≥ 50%) ≥ 25% with a 15% expected return has **no solution**.
- The minimum requirement is E ≥ ~19.5% at σ ≈ 67%. That implies roughly a **1-in-3 chance of losing 30%+**.
- This is incompatible with his low-risk brief. Deliver the closest legitimate version: **~29% odds of 25%+** and ~37% odds of 20%+.

**The 15% hurdle:**
- It sits at the edge. The conservative estimate is 14.2%; the raw model is 17.7%.
- Concentrating to 15 names lifts the conservative E to 15.2%, but P(≥15%) only moves from 46% to 48%, with a bigger downside.
- The recommendation stays the diversified 20.

---


---

## 8. Audit loops after v2 (Turn 6)

Three auditors ran in parallel threads (`audit_loop1.py`).

### Auditor 1 — Holdings integrity
- All 20 v2 holdings pass their gates.
- Release-to-company name match: 179/180 releases.
- **NVDA:** EDGAR returned the **CFO commentary (EX-99.2)**, not the press release. Its guidance score was set to neutral. `edgar2.py` now excludes "cfo" files and accepts "pr.htm".

### Auditor 2 — Survivorship bias

Compares an equal-weight basket of today's constituents with the real equal-weight S&P ETF (RSP):

| 12m from | RSP actual | EW of today's members | Bias | v2 top-30 vs RSP |
|---|---|---|---|---|
| Sep-2023 | 28.3% | 35.4% | +7.1 pts | +8.0 pts |
| Sep-2024 | 7.2% | 14.5% | +7.3 pts | +14.1 pts |
| Sep-2025 | 13.3% | 17.9% | +4.6 pts | +17.0 pts |

The alpha estimate compares like with like (top 30 vs EW survivors), so it is unaffected. Absolute backtest returns are now labelled as inflated.

### Auditor 3 — Assumption sensitivity

v2 Recommended portfolio's shrunk expected return under different assumptions:

| Case | E |
|---|---|
| Base | 14.2% |
| Market prior 8% | 12.4% |
| Market prior 12% | 15.9% |
| Growth haircut 50% | 13.8% |
| No growth haircut | 14.7% |
| Alpha zero | 13.4% |
| Alpha unshrunk | 14.3% |

**Conclusion:** the market assumption dominates; stock-picking edge adds about 1 point.

### Hand-read notes
Latest SEC release highlights were written for all 20 v2 holdings. They sit in `dash2.json` → `N2`. Weak spots found:
- **SWK:** margin helped by one-off tariff refunds.
- **INCY:** one-time CMS benefit.
- **TROW:** $6.5B outflows.
- **GPN:** big gap between GAAP and adjusted profit.

---

## 9. v3 Conviction engine (Turn 7) — methodology

**Principle:** conviction = agreement across independent lenses, robust to the analyst's own assumptions. Not optimised to any return target. Script: `conv.py`. Portfolio: `conv_port.py`.

### 9.1 Multi-year Buffett data for all 497 (from `fund_all.pkl`, last 4 fiscal years)

| Field | Definition |
|---|---|
| `roe_yrs` | Number of years with ROE > 12% |
| `fcf_pos` | FCF (OCF + capex) positive in every year (≥3 years needed) |
| `ni_pos` | Net income positive in every year |
| `cagr4` | Revenue CAGR |
| `upyrs` | Years of revenue growth |
| `om_stable` | Latest operating margin ≥ average − 3 pts |
| `sh_chg` | Diluted share-count change |

### 9.2 Ten lens-agents

Base thresholds are shown. `f` = perturbation multiplier. `fin` = Financials or Real Estate.

| # | Lens | Pass rule |
|---|---|---|
| 1 | **Quality (Buffett)** [HARD] | `roe_yrs ≥ ceil(3·min(f,1.33))` AND (`fcf_pos` OR fin & `ni_pos`) AND stage-1 `A_Quality ≥ 0.5f` |
| 2 | Durable growth | `cagr4 ≥ 5%·f` AND latest `revg ≥ −2%·f` AND `upyrs ≥ nyrs−2` |
| 3 | **Balance sheet** [HARD] | fin: `ROE > 10%·f`; others: `net debt/EBITDA ≤ 2.5/f`; AND not stage-1 vetoed |
| 4 | Valuation sanity | `fpe > 0` AND (`fpe ≤ 1.35/f ×` sector median fwd P/E OR PEG `fpe/(g·100) ≤ 1.5/f`) AND building-block `E_bb ≥ 6%·f` |
| 5 | Earnings momentum | 90-day change in +1y EPS `≥ −2%·f` AND beat rate (last 8 quarters) `≥ 62.5%·f` |
| 6 | Price health | trend template `≥ round(4f)` AND within `25%/f` of the 52-week high |
| 7 | **Risk** [HARD] | `vol ≤ 45%/f` AND 3-yr max drawdown `≥ −45%/f` |
| 8 | Validated model (v2) | v3 composite percentile `≥ 0.60f` |
| 9 | Classic model (v1) | stage-1 composite percentile `≥ 0.50f` |
| 10 | Management & red flags | no guidance cut in the last 4 SEC releases (read companies only; others neutral) AND ≤1 red-team flag |

**Rules:**
- **Conviction:** passes ≥9 of 10 AND all three HARD lenses.
- **Robustness (stability):** 500 runs. Each run draws 8 independent multipliers `f ~ U(0.8, 1.2)` for the lens families q, g, b, v, e, m, r, p. Stability = share of runs in which the stock qualifies.
- **Conservative E:** `E_cons = 0.5·E_final + 0.5·10%·clip(0.67β₃ᵧ + 0.33, 0.6, 1.6)`. `E_final` is the v2 three-method mean.
- **Conviction score:** `100 × (0.35·stability + 0.25·passes/10 + 0.20·pct(E_cons) + 0.20·A_Quality)`.

**Pass counts (base thresholds, of 497):**

| Lens | Stocks passing |
|---|---|
| Quality | 151 |
| Durable growth | 249 |
| Balance sheet | 287 |
| Valuation sanity | 315 |
| Earnings momentum | 368 |
| Price health | 269 |
| Risk | 334 |
| v2 model | 199 |
| v1 model | 249 |
| Management | 449 |

**Outcome:** 31 stocks pass the base conviction rule; **11** have stability ≥0.7; **6** have stability ≥0.9 (NVDA, CPAY, AMP, RL, AME, EOG). EOG was later excluded for low expected return.

### 9.3 Loops run in Turn 7

1. **Loop 1: vote + perturbation** across all 497.
2. **Loop 2: release reader.** Every candidate with stability ≥0.5 not yet read was sent through EDGAR (`edgar2.py`): 14 companies, 126 more releases, **593 total**. Management lens re-run.
   - Auditor check of flagged cuts: **MSFT's flag was a regex false positive** (a "compared to our guidance" sentence) and was corrected in `conv.py`.
   - ITW (2024) and TPR (2025) cuts were real but older than the last 4 releases.
   - Guidance records over the last 4 releases (R = raise):
     - RL R,R,R,R
     - TPR R,R,R,R
     - AME R,.,R,R
     - ALLE R,.,R,R
     - ABNB R,.,R,R
     - ITW R,.,R,R
     - EOG, SNA, IBKR, V, CB: no formal raises (no guidance issued)
3. **Loop 3: point-in-time test of the conviction filter** (`backtest3.py` frames, `bt_conv.json`).
   - The PIT proxy uses: not vetoed, Q pct ≥0.6, revenue growth ≥3%, ROE >10% (fin) or ND/EBITDA ≤2.5, earnings yield >0, vol ≤45%, max drawdown ≥−45%, trend ≥4, v3 composite pct ≥0.6.

   | Start | Picks | Avg 12m return | % of picks up | % beating S&P | % of all stocks up | Universe avg |
   |---|---|---|---|---|---|---|
   | Sep-2023 | 0 (data coverage) | – | – | – | 88% | 35.4% |
   | Sep-2024 | 28 | 10.3% | 64% | 39% | 61% | 14.5% |
   | Sep-2025 | 34 | 7.0% | 56% | 29% | 58% | 17.9% |

   **Interpretation:** quality-and-safety filters do not raise one-year hit rates. Per-stock 90% confidence is unattainable. Confidence belongs at the portfolio and multi-year level.

### 9.4 Portfolio construction (v3, `conv_port.py`)
- **Candidates:** stability ≥0.5 AND `E_cons ≥ 8%`, taken in conviction-score order.
- **Diversification:** max **1 name per GICS sub-industry**.
- **Weights:** ∝ `cscore × (0.5 + stability)`, clipped 4–10%, sector ≤25%, renormalised iteratively.
- **Odds:** 20,000-path block bootstrap (3-month blocks) on 10 years of monthly returns, re-centred to E. Horizons 12 and 60 months. The S&P uses the same method with E = 10%.

### 9.5 Hand-read latest-release notes (v3 finalists)
Stored in `dash2.json` → `CV.NC`. Examples:
- **CPAY:** revenue +21%, adjusted EPS +36%, FY outlook raised.
- **RL:** revenue +14%, ahead of expectations.
- **AME:** record sales $2.04B (+15%), guidance raised.
- **NTAP:** record revenue +30%; FY27 guidance "significantly raised".
- **ABNB:** revenue +17%, FCF margin 35%.
- **MSFT:** revenue $90.0B (+18%).
- **ALLE:** adjusted EPS +17.6%, outlook raised.
- **PAYX:** double-digit EPS growth.
- **SNA:** sales +4.7%.
- **IBKR:** EPS $0.69.
- **NVDA, AMP, HIG, AIZ:** notes from earlier turns.

---

## 10. Self-grade history and current rubric

**History:**

| Stage | Grade |
|---|---|
| v0 news-based list | 58 |
| v1 dashboard | 78 |
| v2 analysis | 91 |
| v2 + audit loops | 92 |
| **v3 conviction** | **92** |

**Current rubric (v3):**

| Criterion | Score | Note |
|---|---|---|
| Universe & data breadth | 10 | All 497; 10 lenses |
| Primary-source reading | 9 | 593 SEC releases machine-read; latest release hand-read for all 14 finalists |
| Valuation rigour | 9 | 3-method E, conservative blend, valuation-sanity lens |
| Out-of-sample validation | 9 | PIT tests of v1, v2 and the conviction filter |
| Robustness | 10 | 500 perturbations; per-stock stability |
| Risk & odds | 9 | 1- and 5-yr bootstraps vs S&P on the same basis |
| Error discovery | 10 | 19 errors found and fixed |
| Honesty | 10 | Per-stock 90% shown unattainable with data |
| Company-level depth | 8 | No call transcripts or expert calls |
| Actionability | 8 | Order sheet pending amount and broker |
| **Total** | **92** | |

**To reach 95+:** earnings-call transcripts; point-in-time consensus history; survivorship-free index membership; hand-written notes for all 31 base-conviction names; the order sheet.

### 10.1 Errors 16–19 (errors 1–15 are in §10b.1)
16. NVDA EDGAR pulled the CFO commentary instead of the press release → exhibit filter fixed.
17. Survivorship bias was unmeasured → measured against RSP (+4.6 to +7.3 pts/yr).
18. MSFT "guidance cut" was a regex false positive → corrected.
19. Hurdle-driven answers shifted with the target → replaced by the target-independent v3 conviction engine.

---

## 11. Open items (priority order)
1. **Order sheet** (after the owner gives amount + broker):
   - 50% UCITS S&P 500 index fund + 50% the 14 stocks at §0.1 weights.
   - 3 tranches: now, after Q3 earnings (late Oct), mid-Nov.
   - Limit orders; fractional shares on IBKR.
   - Click-by-click steps for a non-technical user.
   - Flag US estate tax and dividend withholding.
2. **Monthly re-run cadence** of the conviction engine (momentum decays). Turnover cap; only swap names whose stability falls below 0.5.
3. **Data upgrades for 95+:** transcripts; point-in-time estimates; survivorship-free universe.
4. **Better NLP** for the release reader (regex false positives exist). Hand-written notes for all base-conviction names.
5. **Dashboard:** keep all 16 tabs. Add, never remove (owner's rule).


## 10b. v2 self-grade rubric (91/100) and errors 1–15

| Criterion | Score | Evidence / gap |
|---|---|---|
| Universe & data breadth | 10/10 | 497 stocks, 11y prices, statements, estimates |
| Primary-source reading | 9/10 | 467 SEC releases machine-read; 8 read in full |
| Valuation rigour | 9/10 | 3 methods, reverse DCF, shrinkage, disagreement tracked |
| Out-of-sample validation | 9/10 | 3y point-in-time + 10y factor test (survivorship bias, short sample) |
| Risk modelling | 9/10 | 20k block bootstrap incl. 2020/2022, resampled optimiser |
| Portfolio vs mandate | 9/10 | Frontier with odds for 15/20/25/50% |
| Error discovery | 10/10 | 15 errors found and fixed (list below) |
| Honesty of probabilities | 10/10 | Shrunk vs raw both shown |
| Company-level qualitative depth | **7/10** | No call transcripts or expert calls; new names lack notes |
| Actionability | 9/10 | Order sheet pending amount/broker |

**To reach 95+:**
1. Human-style diligence notes for all 20 holdings from the EDGAR text: guidance, segment trends, risks, capital return.
2. Earnings-call transcripts.
3. Point-in-time analyst-estimate history to backtest P_emom.
4. Longer point-in-time fundamental history.
5. A survivorship-free universe (historical S&P membership).

### 10b.1 All 15 model errors found and fixed

**v1 (8):**
1. Red-team cash-conversion flag misfired on AI capex spenders. Fixed with the OCF/NI appeal.
2. DCF used one-off gains as the growth base (GOOGL DCF $73). One-off detector added; 8 names corrected.
3. Visa/Mastercard valued like banks (V at $120 via P/B). Routed to DCF.
4. Growth-capex FCF understated DCFs (LLY, MSFT, +9 more). Owner-earnings normalisation added.
5. Bear case too mild for stocks with no down year (SNDK −3%). Volatility floor added.
6. Altman Z vetoed asset-light firms. Veto now requires weak debt too; 4 vetoes overturned.
7. Low-risk mandate not enforced (75%-vol stock in top 30). Vol >55% veto added.
8. Three correlated insurers in the final 10. Sub-industry and insurer caps added.

**v2 (7):**
9. Low-vol tilt lost in all 3 backtest years. Removed as a return driver.
10. Dividend-yield unit bug (0.44% read as 44%). Switched to `trailingAnnualDividendYield`.
11. One-off EPS depressions gave fake 60% growth (MRK and 9 others). Growth guard added.
12. Noisy or negative 1y betas. Replaced with 3y weekly.
13. Optimiser maximised estimation error (airlines, autos). Shrinkage, quality floor, confidence caps and resampling added.
14. Hidden sub-industry concentration. 12% cap added.
15. Backtested alpha overstated. 58% McLean-Pontiff shrink applied.

---


## 12. File inventory and published links
- **Working dir:** `/home/claude/deep/` (everything is in `equity_project_bundle_v3.zip`).
- **Data files:** `universe.csv`, `close/high/low/volume.pkl` (3y), `close10.pkl` (11y), `info.json`, `fund_all.pkl`, `est_all.pkl`, `deep.pkl`, `edgar.pkl` (593 release texts), `edgar_read.json`.
- **Stage outputs:** `s1.pkl`, `s2.pkl`, `s3_100.pkl`, `s3_30.pkl`, `v3.pkl`, `K.pkl`, `conv.pkl`, `bt_frames.pkl`.
- **Results:** `port.json` (v1), `port2.json` (v2), `conv_port.json` (v3), `backtest.json`, `bt_v3.json`, `bt_v3b.json`, `bt10.json`, `bt_conv.json`, `audit.json`, `audit_loop1.json`.
- **Dashboard:**
  - Templates: `dash_tpl.html` (v1), `dash_tpl_v2.html`, `dash_tpl_v3.html` (**current benchmark**).
  - Injection pieces: `v2tabs.js`, `cvtab.js`.
  - Data: `dash.json`, `dash2.json`.
- **Published pages:**
  - Current dashboard (v3, 16 tabs): https://claude.ai/artifact/U2RjG3tNLgLfVCF55x6cEf
  - Earlier 100-stock audit page: https://claude.ai/artifact/9dYtL85m4iVSaktuBtuAjW


## Appendix A — Complete source code

### A.0 Inline one-off steps (universe, prices, dashboard injection)
```python
import pandas as pd, requests, yfinance as yf
from io import StringIO
r=requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies',headers={'User-Agent':'Mozilla/5.0'},timeout=30)
t=pd.read_html(StringIO(r.text))[0].rename(columns={'Symbol':'t','Security':'name','GICS Sector':'sector','GICS Sub-Industry':'sub'})
t['t']=t['t'].str.replace('.','-',regex=False); t[['t','name','sector','sub']].to_csv('universe.csv',index=False)
U=t.t.tolist(); px=yf.download(U+['^GSPC'],period='3y',auto_adjust=True,progress=False,threads=True)
for k in ['Close','Volume','High','Low']: px[k].to_pickle(k.lower()+'.pkl')
# after s1_agents.py:
U=pd.read_pickle('s1.pkl').t.tolist(); yf.download(U+['^GSPC'],period='11y',auto_adjust=True,progress=False,threads=True)['Close'].to_pickle('close10.pkl')
# dashboard (current):
h=open('dash_tpl_v3.html').read().replace('__DATA__',open('dash.json').read(),1).replace('__DATA2__',open('dash2.json').read(),1)
open('equity_audit_v3.html','w').write(h)
```

### A.1 `s1_info.py` — Stage-1 data pull
```python
import yfinance as yf, pandas as pd, json, time, sys, os, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
U=pd.read_csv('universe.csv').t.tolist()
I=json.load(open('info.json')) if os.path.exists('info.json') else {}
todo=[s for s in U if not I.get(s,{}).get('marketCap')][:int(sys.argv[1])]
def f(s):
    for k in range(2):
        try: return s,yf.Ticker(s).info
        except Exception: time.sleep(1)
    return s,{}
with ThreadPoolExecutor(20) as ex:
    for s,v in ex.map(f,todo): I[s]=v
json.dump(I,open('info.json','w'),default=str)
print('have',sum(1 for v in I.values() if v.get('marketCap')),'of',len(U))
```

### A.2 `s1_agents.py` — Stage 1: 7 screening agents + red team + refutation
```python
# STAGE 1: Screening Committee — 7 specialist agents + red team + refutation rounds. 503 -> 100
import pandas as pd, numpy as np, json, warnings
warnings.filterwarnings('ignore')
U=pd.read_csv('universe.csv'); I=json.load(open('info.json'))
C=pd.read_pickle('close.pkl').ffill(); spx=C['^GSPC'].dropna()
rows=[]
for _,u in U.iterrows():
    s=u.t; i=I.get(s,{}); 
    if s not in C or C[s].dropna().shape[0]<300: continue
    c=C[s].dropna(); r=c.pct_change().dropna(); r1=r.iloc[-252:]
    sma50,sma150,sma200=c.rolling(50).mean(),c.rolling(150).mean(),c.rolling(200).mean()
    hi52,lo52=c.iloc[-252:].max(),c.iloc[-252:].min(); p=float(c.iloc[-1])
    al=pd.concat([r1,spx.pct_change().iloc[-252:]],axis=1).dropna()
    roll=(c/c.shift(252)-1).dropna()
    mc=i.get('marketCap') or np.nan; fcf=i.get('freeCashflow'); ni=i.get('netIncomeToCommon'); rev=i.get('totalRevenue')
    ebitda=i.get('ebitda'); debt=i.get('totalDebt') or 0
    rows.append(dict(t=s,name=u['name'],sector=u.sector,sub=u['sub'],price=p,mcap=mc/1e9 if mc==mc else np.nan,
     fpe=i.get('forwardPE'),tpe=i.get('trailingPE'),evebitda=i.get('enterpriseToEbitda'),pb=i.get('priceToBook'),ps=i.get('priceToSalesTrailing12Months'),
     fcfy=(fcf/mc) if (fcf and mc==mc and mc>0) else np.nan, divy=i.get('dividendYield'),payout=i.get('payoutRatio'),
     roe=i.get('returnOnEquity'),roa=i.get('returnOnAssets'),gm=i.get('grossMargins'),om=i.get('operatingMargins'),pm=i.get('profitMargins'),
     fcfm=(fcf/rev) if (fcf and rev) else np.nan, de=i.get('debtToEquity'), cr=i.get('currentRatio'),
     nd_ebitda=((debt-(i.get('totalCash') or 0))/ebitda) if ebitda and ebitda>0 else np.nan,
     cash_conv=(fcf/ni) if (fcf and ni and ni>0) else np.nan, ocf_conv=((i.get('operatingCashflow') or np.nan)/ni) if (ni and ni>0) else np.nan,
     revg=i.get('revenueGrowth'),epsg=i.get('earningsGrowth'),
     fwd_epsg=(i['forwardEps']/i['trailingEps']-1) if i.get('forwardEps') and i.get('trailingEps') and i['trailingEps']>0 else np.nan,
     rec=i.get('recommendationMean'),nan=i.get('numberOfAnalystOpinions'),tgt=i.get('targetMeanPrice'),tgt_hi=i.get('targetHighPrice'),tgt_lo=i.get('targetLowPrice'),
     short=i.get('shortPercentOfFloat'),insider=i.get('heldPercentInsiders'),inst=i.get('heldPercentInstitutions'),
     vol=float(r1.std()*np.sqrt(252)),dvol=float(r1[r1<0].std()*np.sqrt(252)),
     beta=float(np.cov(al.iloc[:,0],al.iloc[:,1])[0,1]/al.iloc[:,1].var()),
     mdd3y=float((c/c.cummax()-1).min()),worst12m=float(roll.min()),
     ret12=float(p/c.iloc[-252]-1),ret6=float(p/c.iloc[-126]-1),ret3=float(p/c.iloc[-63]-1),ret1m=float(p/c.iloc[-21]-1),
     rs6=float((p/c.iloc[-126])/(spx.iloc[-1]/spx.iloc[-126])-1),
     off_hi=p/hi52-1,above_lo=p/lo52-1,
     tt=int(p>sma50.iloc[-1])+int(sma50.iloc[-1]>sma150.iloc[-1])+int(sma150.iloc[-1]>sma200.iloc[-1])+int(sma200.iloc[-1]>sma200.iloc[-22])+int(p>sma200.iloc[-1])+int(p/hi52-1>-0.25)+int(p/lo52-1>0.30),
     summary=(i.get('longBusinessSummary') or '')[:900], website=i.get('website'),employees=i.get('fullTimeEmployees'),
     tgt_disp=((i.get('targetHighPrice') or np.nan)-(i.get('targetLowPrice') or np.nan))/p))
df=pd.DataFrame(rows); df=df[~df.t.isin(['GOOG','FOX','NWS'])].reset_index(drop=True); df['upside']=df.tgt/df.price-1
# percentile helpers: sector-relative for valuation & quality (Pb/PE norms differ by sector), absolute for risk & momentum
def pr(col,asc=True,by_sector=False,clip=None):
    s=df[col].astype(float)
    if clip: s=s.clip(*clip)
    s=s.fillna(s.median())
    return (s.groupby(df.sector).rank(pct=True,ascending=asc) if by_sector else s.rank(pct=True,ascending=asc))
pos=lambda col: df[col].where(df[col]>0)
df['fpe_p']=pos('fpe'); df['eve_p']=pos('evebitda')
A={}
A['Quality']=(pr('roe',clip=(-1,1.5),by_sector=True)+pr('om',by_sector=True)+pr('fcfm',clip=(-1,1),by_sector=True)+pr('gm',by_sector=True)+pr('cash_conv',clip=(-1,3))+pr('nd_ebitda',False,clip=(-5,10)))/6
A['Growth']=(pr('revg',clip=(-.5,1.5))+pr('epsg',clip=(-1,2))+pr('fwd_epsg',clip=(-.5,1)))/3
A['Valuation']=(pr('fpe_p',False,True)+pr('eve_p',False,True)+pr('fcfy',True,True,(-.2,.2))+pr('upside',clip=(-.5,1)))/4
A['Momentum']=(df.tt/7+pr('rs6')+pr('ret12',clip=(-1,3))+pr('off_hi'))/4
A['Risk']=(pr('vol',False)+pr('dvol',False)+pr('mdd3y')+pr('worst12m')+pr('beta',False))/5
A['Street']=(pr('rec',False)+pr('upside',clip=(-.5,1))+pr('short',False)+pr('nan'))/4
for k,v in A.items(): df['A_'+k]=v
W={'Quality':.22,'Growth':.16,'Valuation':.18,'Momentum':.12,'Risk':.20,'Street':.12}
df['raw']=100*sum(W[k]*df['A_'+k] for k in W)
# Red-team agent: hard vetoes and soft flags
flags={}; veto={}; capex_note=[]
for i_,r in df.iterrows():
    f=[];v=[]
    if r.fpe!=r.fpe or r.fpe<=0: v.append('No forward profit')
    if r.sector not in('Financials','Real Estate') and r.fcfy==r.fcfy and r.fcfy<0: v.append('Burning cash (negative FCF)')
    if r.mdd3y<-0.60: v.append('Fell >60% in 3 yrs')
    if r.sector not in('Financials','Real Estate','Utilities') and r.nd_ebitda==r.nd_ebitda and r.nd_ebitda>4: f.append('High leverage (net debt >4x EBITDA)')
    if r.cash_conv==r.cash_conv and r.cash_conv<0.5 and r.sector not in('Financials','Real Estate'):
        if r.ocf_conv==r.ocf_conv and r.ocf_conv>=0.9: capex_note.append(r.t)
        else: f.append('Weak cash conversion (<50% of profit)')
    if r.payout==r.payout and r.payout>1.0 and r.sector!='Real Estate': f.append('Pays out >100% of earnings')
    if r.short==r.short and r.short>0.08: f.append('High short interest')
    if r.revg==r.revg and r.revg<0: f.append('Shrinking revenue')
    if r.epsg==r.epsg and r.epsg>2 and r.fpe==r.fpe and r.fpe<12: f.append('Possible cyclical peak earnings')
    flags[r.t]=f; veto[r.t]=v
df['flags']=df.t.map(flags); df['veto']=df.t.map(veto)
# Refutation rounds between agents (logged)
debate=[]; adj=np.zeros(len(df))
for i_,r in df.iterrows():
    notes=[]
    if r.A_Valuation>0.75 and r.A_Momentum<0.30:
        if r.A_Quality<0.5: notes.append(('Momentum refutes Valuation','Cheap but falling and mediocre quality: value trap. Penalty -6.',-6))
        else: notes.append(('Quality defends Valuation','Cheap and falling, but high quality: possible genuine dip. Kept, no penalty.',0))
    if r.A_Momentum>0.80 and r.A_Valuation<0.25:
        if r.A_Growth<0.70: notes.append(('Valuation refutes Momentum','Expensive rally not backed by growth: bubble risk. Penalty -6.',-6))
        else: notes.append(('Growth defends Momentum','Expensive but growth is top-30%: premium earned. No penalty.',0))
    if r.A_Growth>0.80 and (r.fcfy==r.fcfy and r.fcfy<0.01) and r.sector not in('Financials','Real Estate'):
        notes.append(('Quality refutes Growth','Fast growth with <1% FCF yield: growth not yet converting to cash. Penalty -3.',-3))
    if r.A_Street>0.80 and r.A_Risk<0.25: notes.append(('Risk refutes Street','Analysts love it but price swings are extreme. Penalty -4.',-4))
    if r.A_Quality>0.80 and r.A_Risk>0.70 and r.A_Valuation>0.45: notes.append(('Buffett lens endorses','Wonderful business, calm stock, fair price. Bonus +4.',4))
    if r.t in capex_note: notes.append(('Capital-allocation agent overrules red team','Low free cash flow is heavy growth capex, not weak earnings: operating cash flow covers >=90% of profit. Cash-conversion flag withdrawn.',0))
    for k in r['flags']: notes.append(('Red team flag',k+'. Penalty -2.',-2))
    adj[i_]=sum(n[2] for n in notes); debate.append(notes)
df['debate']=debate; df['adj']=adj; df['s1']=df.raw+df.adj
df['vetoed']=df.veto.map(len)>0
df=df.sort_values('s1',ascending=False).reset_index(drop=True); df['rank500']=df.index+1
# shortlist 100 with sector cap 22
sl=[];cnt={}
for _,r in df[~df.vetoed].iterrows():
    if cnt.get(r.sector,0)>=22: continue
    sl.append(r.t); cnt[r.sector]=cnt.get(r.sector,0)+1
    if len(sl)==100: break
df['short100']=df.t.isin(sl)
df.to_pickle('s1.pkl')
print('universe',len(df),'vetoed',df.vetoed.sum(),'debates',sum(len(d)>0 for d in df.debate))
print(pd.Series(cnt).sort_values(ascending=False).to_string())
print(df[df.short100][['rank500','t','sector','s1','A_Quality','A_Growth','A_Valuation','A_Momentum','A_Risk']].head(25).round(2).to_string())
```

### A.3 `s2_pull.py` — Stage-2 data pull (100)
```python
import yfinance as yf, pandas as pd, pickle, os, sys, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
df=pd.read_pickle('s1.pkl'); T=df[df.short100].t.tolist()
D=pickle.load(open('deep.pkl','rb')) if os.path.exists('deep.pkl') else {}
todo=[t for t in T if t not in D or not D[t].get('ok')][:int(sys.argv[1])]
def g(fn):
    try:
        x=fn(); return x
    except Exception as e: return None
def pull(t):
    k=yf.Ticker(t); o={}
    o['q_inc']=g(lambda:k.quarterly_income_stmt); o['a_inc']=g(lambda:k.income_stmt)
    o['a_cf']=g(lambda:k.cashflow); o['a_bs']=g(lambda:k.balance_sheet); o['q_cf']=g(lambda:k.quarterly_cashflow)
    o['ed']=g(lambda:k.get_earnings_dates(limit=12)); o['trend']=g(lambda:k.eps_trend); o['rev']=g(lambda:k.eps_revisions)
    o['ee']=g(lambda:k.earnings_estimate); o['re']=g(lambda:k.revenue_estimate); o['ud']=g(lambda:k.upgrades_downgrades)
    o['ins']=g(lambda:k.insider_purchases); o['news']=g(lambda:k.news)
    o['ok']=o['a_inc'] is not None and o['q_inc'] is not None
    return t,o
with ThreadPoolExecutor(12) as ex:
    for t,o in ex.map(pull,todo): D[t]=o
pickle.dump(D,open('deep.pkl','wb'))
print('done',sum(1 for t in T if D.get(t,{}).get('ok')),'of',len(T))
```

### A.4 `s2_agents.py` — Stage 2: forensic, capital, earnings, valuation, Buffett
```python
# STAGE 2/3: Forensic, Capital-Allocation, Earnings-Momentum, Intrinsic-Value, Bull & Bear agents on the 100
import pandas as pd, numpy as np, pickle, json, warnings
warnings.filterwarnings('ignore')
df=pd.read_pickle('s1.pkl'); D=pickle.load(open('deep.pkl','rb')); I=json.load(open('info.json'))
C=pd.read_pickle('close.pkl').ffill()
RF=0.049; ERP=0.05; TG=0.03
sec_fpe=df[df.fpe>0].groupby('sector').fpe.median()
def row(t,names):
    if t is None: return None
    for n in names:
        if n in t.index: return t.loc[n].astype(float)
    return None
def v(s,k=0):
    try:
        x=s.iloc[k]; return float(x) if x==x else np.nan
    except Exception: return np.nan
out={}
for t in df[df.short100].t:
    o=D[t]; i=I[t]; r=df[df.t==t].iloc[0]; A,Q,CF,BS=o['a_inc'],o['q_inc'],o['a_cf'],o['a_bs']
    NONBANK=['Transaction & Payment Processing Services','Financial Exchanges & Data','Insurance Brokers','Asset Management & Custody Banks']
    fin=(r.sector=='Real Estate') or (r.sector=='Financials' and r['sub'] not in NONBANK)
    rev=row(A,['Total Revenue','Operating Revenue']); ni=row(A,['Net Income Common Stockholders','Net Income'])
    gp=row(A,['Gross Profit']); ebit=row(A,['EBIT','Operating Income']); opi=row(A,['Operating Income','EBIT'])
    intexp=row(A,['Interest Expense','Interest Expense Non Operating']); sh=row(A,['Diluted Average Shares','Basic Average Shares'])
    eps=row(A,['Diluted EPS','Basic EPS']); taxr=row(A,['Tax Rate For Calcs'])
    ocf=row(CF,['Operating Cash Flow','Cash Flow From Continuing Operating Activities']); capex=row(CF,['Capital Expenditure'])
    buyb=row(CF,['Repurchase Of Capital Stock','Common Stock Payments']); divp=row(CF,['Cash Dividends Paid','Common Stock Dividend Paid'])
    nin=row(A,['Normalized Income']); dep=row(CF,['Depreciation And Amortization','Depreciation Amortization Depletion'])
    ta=row(BS,['Total Assets']); tl=row(BS,['Total Liabilities Net Minority Interest']); eq=row(BS,['Stockholders Equity','Common Stock Equity'])
    debt=row(BS,['Total Debt']); cash=row(BS,['Cash Cash Equivalents And Short Term Investments','Cash And Cash Equivalents'])
    ca=row(BS,['Current Assets']); cl=row(BS,['Current Liabilities']); re_=row(BS,['Retained Earnings']); ltd=row(BS,['Long Term Debt'])
    yrs=[str(c.year) for c in A.columns][:4] if A is not None else []
    def ser(s,n=4): return [None if s is None or k>=len(s) or s.iloc[k]!=s.iloc[k] else float(s.iloc[k]) for k in range(n)]
    fcf=(ocf+capex) if (ocf is not None and capex is not None) else ocf
    n_y=min(4,len(rev.dropna())) if rev is not None else 0
    cagr=(v(rev,0)/v(rev,n_y-1))**(1/(n_y-1))-1 if n_y>=2 and v(rev,n_y-1)>0 else np.nan
    om_s=(opi/rev) if (opi is not None and rev is not None) else None
    roe_s=(ni/eq) if (ni is not None and eq is not None) else None
    tax=np.clip(v(taxr,0) if taxr is not None and v(taxr,0)==v(taxr,0) else 0.21,0,0.35)
    ic=(v(debt,0) if debt is not None else 0)+v(eq,0)-(v(cash,0) if cash is not None else 0)
    roic=v(ebit,0)*(1-tax)/ic if (ebit is not None and ic and ic>0) else np.nan
    sh_chg=(v(sh,0)/v(sh,min(3,len(sh.dropna())-1))-1) if sh is not None and len(sh.dropna())>=2 else np.nan
    cover=v(ebit,0)/abs(v(intexp,0)) if (intexp is not None and v(intexp,0) and v(intexp,0)==v(intexp,0) and v(intexp,0)!=0) else np.nan
    # Piotroski F-score
    F=[];
    try:
        roa0,roa1=v(ni,0)/v(ta,0),v(ni,1)/v(ta,1)
        F+=[roa0>0, v(ocf,0)>0, roa0>roa1, v(ocf,0)>v(ni,0)]
        lev0=(v(ltd,0) if ltd is not None else 0)/v(ta,0); lev1=(v(ltd,1) if ltd is not None else 0)/v(ta,1); F.append(lev0<=lev1)
        F.append((v(ca,0)/v(cl,0))>=(v(ca,1)/v(cl,1)) if ca is not None and cl is not None else False)
        F.append(v(sh,0)<=v(sh,1)*1.005 if sh is not None else False)
        F.append((v(gp,0)/v(rev,0))>=(v(gp,1)/v(rev,1)) if gp is not None else False)
        F.append(v(rev,0)/v(ta,0)>=v(rev,1)/v(ta,1))
    except Exception: pass
    fscore=int(sum(bool(x) for x in F)) if (F and not fin) else np.nan
    Z=np.nan
    if not fin:
        try: Z=1.2*(v(ca,0)-v(cl,0))/v(ta,0)+1.4*v(re_,0)/v(ta,0)+3.3*v(ebit,0)/v(ta,0)+0.6*(r.mcap*1e9)/v(tl,0)+1.0*v(rev,0)/v(ta,0)
        except Exception: pass
    accr=(v(ni,0)-v(ocf,0))/v(ta,0) if ocf is not None else np.nan
    # Earnings record (last 8 reported quarters ~ 2 years of reports)
    ed=o['ed']; beats=avgs=np.nan; eq_hist=[]
    if ed is not None and len(ed):
        e=ed.dropna(subset=['Reported EPS']).head(8)
        if len(e): beats=int((e['Surprise(%)']>0).sum()); avgs=float(e['Surprise(%)'].clip(-50,50).mean())
        eq_hist=[dict(d=str(ix.date()),est=None if x['EPS Estimate']!=x['EPS Estimate'] else float(x['EPS Estimate']),act=float(x['Reported EPS']),s=float(x['Surprise(%)']) if x['Surprise(%)']==x['Surprise(%)'] else None) for ix,x in e.iterrows()][::-1]
        nxt=ed[ed['Reported EPS'].isna()]; next_date=str(nxt.index[-1].date()) if len(nxt) else None
    else: next_date=None
    nq=len(eq_hist)
    tr=o['trend']; rv=o['rev']
    eps1y=float(tr.loc['+1y','current']) if tr is not None and '+1y' in tr.index and tr.loc['+1y','current']==tr.loc['+1y','current'] else (i.get('forwardEps') or np.nan)
    eps0y=float(tr.loc['0y','current']) if tr is not None and '0y' in tr.index else np.nan
    rev90=(tr.loc['+1y','current']/tr.loc['+1y','90daysAgo']-1) if tr is not None and '+1y' in tr.index and tr.loc['+1y','90daysAgo'] else np.nan
    up30=int(rv.loc['+1y','upLast30days']) if rv is not None and '+1y' in rv.index and rv.loc['+1y','upLast30days']==rv.loc['+1y','upLast30days'] else 0
    dn30=int(rv.loc['+1y','downLast30days']) if rv is not None and '+1y' in rv.index and rv.loc['+1y','downLast30days']==rv.loc['+1y','downLast30days'] else 0
    ud=o['ud']; ups=downs=0
    if ud is not None and len(ud):
        u=ud[ud.index>=pd.Timestamp.now(tz=ud.index.tz)-pd.Timedelta(days=90)] if ud.index.tz else ud[ud.index>=pd.Timestamp.now()-pd.Timedelta(days=90)]
        ups=int((u.Action=='up').sum()); downs=int((u.Action=='down').sum())
    ins=o['ins']; ins_net=np.nan
    try:
        x=ins.set_index(ins.columns[0]); ins_net=float(x.loc['Net Shares Purchased (Sold)'].iloc[0])
    except Exception: pass
    news=[]
    for n_ in (o['news'] or [])[:5]:
        c_=n_.get('content',{}); news.append(dict(title=c_.get('title'),date=(c_.get('pubDate') or '')[:10],src=(c_.get('provider') or {}).get('displayName'),url=((c_.get('canonicalUrl') or {}).get('url'))))
    # quarterly series
    qrev=row(Q,['Total Revenue','Operating Revenue']); qeps=row(Q,['Diluted EPS','Basic EPS']); qopi=row(Q,['Operating Income'])
    qs=[dict(q=str(c.date()),rev=None if qrev is None or qrev.iloc[k]!=qrev.iloc[k] else float(qrev.iloc[k]),eps=None if qeps is None or qeps.iloc[k]!=qeps.iloc[k] else float(qeps.iloc[k]),
             om=None if (qopi is None or qrev is None or qrev.iloc[k]!=qrev.iloc[k] or qopi.iloc[k]!=qopi.iloc[k]) else float(qopi.iloc[k]/qrev.iloc[k])) for k,c in enumerate(Q.columns)][::-1] if Q is not None else []
    q_yoy=(qs[-1]['rev']/qs[0]['rev']-1) if len(qs)>=5 and qs[0]['rev'] and qs[-1]['rev'] else np.nan
    # ---------- Intrinsic value agent ----------
    p=r.price; badj=float(np.clip(0.67*r.beta+0.33,0.7,1.4)); coe=RF+0.045*badj
    E_=r.mcap*1e9; D_=(v(debt,0) if debt is not None else 0) or 0
    wacc=(E_*coe+D_*(RF+0.015)*(1-tax))/(E_+D_) if not fin else coe
    wacc=max(wacc,0.075)
    methods={}
    fpe_now=p/eps1y if eps1y and eps1y>0 else np.nan
    if eps1y==eps1y and eps1y>0:
        tgt_mult=0.7*fpe_now+0.3*sec_fpe.get(r.sector,20)
        methods['Multiples (fwd EPS x blended P/E)']=eps1y*tgt_mult
    g_cons=(eps1y/eps0y-1) if (eps0y==eps0y and eps0y>0 and eps1y==eps1y) else np.nan
    oneoff=(g_cons==g_cons and g_cons<0 and cagr==cagr and cagr>0.05)
    cands=[x for x in [cagr, (np.nan if oneoff else g_cons), r.revg] if x==x]
    g1=float(np.clip(np.median(cands),-0.05,0.30)) if cands else 0.05
    f0=v(fcf,0) if fcf is not None else np.nan
    ocfc=(v(ocf,0)/v(ni,0)) if (ocf is not None and ni is not None and v(ni,0)>0) else np.nan
    capex_adj=False
    nn=v(nin,0) if (nin is not None and v(nin,0)==v(nin,0) and v(nin,0)>0) else v(ni,0)
    growth_capex=(capex is not None and dep is not None and v(dep,0)>0 and abs(v(capex,0))>1.5*v(dep,0))
    if not fin and nn==nn and nn>0 and (f0!=f0 or f0<0.7*nn) and ((ocfc==ocfc and ocfc>=0.9) or (growth_capex and ocfc==ocfc and ocfc>=0.6)):
        f0=0.7*nn; capex_adj=True
    sh_now=(r.mcap*1e9)/p
    netdebt=(v(debt,0) if debt is not None else 0)-(v(cash,0) if cash is not None else 0)
    def dcf(g0):
        pv=0; f=f0
        for y in range(1,11):
            g=g0 if y<=5 else g0+(TG-g0)*(y-5)/5
            f*=1+g; pv+=f/(1+wacc)**y
        return (pv+f*(1+TG)/(wacc-TG)/(1+wacc)**10-netdebt)/sh_now
    impl_g=np.nan
    if not fin and f0==f0 and f0>0:
        methods['DCF (5-yr growth, 5-yr fade)']=dcf(g1)
        lo,hi=-0.3,0.8
        for _ in range(60):
            mid=(lo+hi)/2; lo,hi=(mid,hi) if dcf(mid)<p else (lo,mid)
        impl_g=mid
    if fin and r.pb and r.pb>0 and r.roe==r.roe and r.sector=='Financials':
        bvps=p/r.pb; roe_=float(np.clip(r.roe,0,0.35)); jpb=(roe_-TG)/(coe-TG)
        methods['Justified P/B (ROE vs cost of equity)']=bvps*jpb
    if r.tgt==r.tgt: methods['Street mean target (12m)']=float(r.tgt)
    mv={k:float(x) for k,x in methods.items() if x==x and x>0}
    # clip each method to +/-60% band to limit model blow-ups
    mv_c={k:float(np.clip(x,p*0.3,p*2.5)) for k,x in mv.items()}
    fair=float(np.median(list(mv_c.values()))) if mv_c else p
    disp=float(np.std(list(mv_c.values()))/p) if len(mv_c)>1 else 0.5
    base=float(np.clip(fair,p*0.7,p*1.45))
    bull_f=eps1y*1.10*fpe_now*1.10 if eps1y==eps1y and eps1y>0 else p*1.3
    bull=float(np.nanmean([bull_f, r.tgt_hi if r.tgt_hi==r.tgt_hi else np.nan, base*1.15]))
    bear_f=eps1y*0.85*fpe_now*0.80 if eps1y==eps1y and eps1y>0 else p*0.7
    emp=p*(1+max(r.worst12m,-0.6)) if r.worst12m<0 else np.nan
    bear=float(np.nanmean([bear_f, p*np.exp(-r.vol), emp, r.tgt_lo if r.tgt_lo==r.tgt_lo else np.nan]))
    bear=min(bear,p*(1-0.5*r.vol))
    bull=max(bull,base*1.05,p*1.05); bear=min(bear,base*0.95,p*0.97)
    exp=0.25*bull+0.5*base+0.25*bear
    # Buffett checklist
    roe_list=[x for x in ser(roe_s) if x is not None]; om_list=[x for x in ser(om_s) if x is not None]
    fcf_list=[x for x in ser(fcf) if x is not None]; eps_list=[x for x in ser(eps) if x is not None]
    B={'ROE above 15% in 3 of last 4 years':sum(x>0.15 for x in roe_list)>=3 if len(roe_list)>=3 else False,
       'Conservative debt (interest cover >8x or net cash)':(cover==cover and cover>8) or ((v(cash,0) if cash is not None else 0)>(v(debt,0) if debt is not None else 0)),
       'Operating margin stable or rising':(om_list[0]>=np.mean(om_list)-0.02) if len(om_list)>=3 else False,
       'Positive free cash flow every year':(len(fcf_list)>=3 and all(x>0 for x in fcf_list)) if not fin else (len(roe_list)>=3 and all(x>0 for x in roe_list)),
       'Share count flat or shrinking':sh_chg==sh_chg and sh_chg<=0.01,
       'Return on capital above 12%':(roic==roic and roic>0.12) if not fin else (r.roe==r.roe and r.roe>0.12),
       'EPS grew in most years':sum(eps_list[k]>eps_list[k+1] for k in range(len(eps_list)-1))>=max(1,len(eps_list)-2) if len(eps_list)>=3 else False,
       'Sensible price (forward P/E under 22)':fpe_now==fpe_now and fpe_now<22}
    out[t]=dict(t=t,fin=fin,yrs=yrs,rev_a=ser(rev),ni_a=ser(ni),fcf_a=ser(fcf),om_a=ser(om_s),roe_a=ser(roe_s),eps_a=ser(eps),
        cagr=cagr,roic=roic,sh_chg=sh_chg,cover=cover,fscore=fscore,Z=Z,accr=accr,buyback=-v(buyb,0) if buyb is not None else np.nan,div=-v(divp,0) if divp is not None else np.nan,
        beats=beats,nq=nq,avg_surp=avgs,eq_hist=eq_hist,next_date=next_date,eps0y=eps0y,eps1y=eps1y,rev90=rev90,up30=up30,dn30=dn30,ups=ups,downs=downs,ins_net=ins_net,news=news,
        qs=qs,q_yoy=q_yoy,wacc=wacc,impl_g=impl_g,g1=g1,methods=mv,fair=fair,disp=disp,base=base,bull=bull,bear=bear,exp=exp,
        exp_ret=exp/p-1,up=bull/p-1,down=bear/p-1,base_ret=base/p-1,capex_adj=capex_adj,g_cons=g_cons,oneoff=oneoff,buffett=B,bscore=int(sum(B.values())),fpe_now=fpe_now)
pickle.dump(out,open('s2.pkl','wb'))
x=pd.DataFrame(out).T
print(x[['fscore','Z','roic','beats','nq','rev90','bscore','exp_ret','up','down','disp']].astype(float).describe().round(2).to_string())
print(x.loc[['NVDA','GOOGL','LLY','V','JPM','MSFT','AAPL'],['cagr','roic','fscore','beats','rev90','bscore','base_ret','up','down','exp_ret']].to_string())
```

### A.5 `s3_committee.py` — Stage 3 committee, vetoes, confidence, top 30
```python
# STAGE 3: Investment Committee (100 -> 30) + confidence + final ranking
import pandas as pd, numpy as np, pickle
df=pd.read_pickle('s1.pkl'); O=pickle.load(open('s2.pkl','rb'))
X=pd.DataFrame(O).T.reset_index(drop=True)
S=df[df.short100].merge(X,on='t'); 
num=lambda c: pd.to_numeric(S[c],errors='coerce')
def pr(s,asc=True): s=pd.to_numeric(s,errors='coerce'); return s.fillna(s.median()).rank(pct=True,ascending=asc)
S['C_forensic']=(pr(num('fscore'))+pr(num('Z').clip(upper=10))+pr(num('accr'),False))/3
S['C_capital']=(pr(num('roic').clip(upper=1.5))+pr(num('sh_chg'),False))/2
S['C_earn']=(pr(num('beats'))+pr(num('avg_surp').clip(-20,20))+pr(num('rev90').clip(-.3,.5))+pr(num('up30')-num('dn30'))+pr(num('ups')-num('downs')))/5
S['C_value']=(pr(num('exp_ret'))+pr(num('base_ret')))/2
S['C_buffett']=num('bscore')/8
S['C_screen']=pr(S.s1)
W={'C_screen':.25,'C_forensic':.10,'C_capital':.10,'C_earn':.15,'C_value':.25,'C_buffett':.15}
S['s3']=100*sum(W[k]*S[k] for k in W)
# Devil's-advocate vetoes (logged)
V=[];OVR=[]
for _,r in S.iterrows():
    v=[]
    if not r.fin and r.sector!='Utilities' and r.Z==r.Z and r.Z<1.8:
        weak=(r.cover==r.cover and r.cover<4) or (r.nd_ebitda==r.nd_ebitda and r.nd_ebitda>3.5)
        if weak: v.append('Distress-zone balance sheet (Altman Z < 1.8 and weak debt cover)')
        else: OVR.append((r.t,'Altman Z %.1f is below 1.8, but interest cover and net debt are healthy. Z-score misreads asset-light models. Veto overturned.'%r.Z))
    if 'Possible cyclical peak earnings' in r['flags'] and r.vol>0.5: v.append('Peak-cycle trap: earnings boom in a highly volatile cyclical')
    if r.beats==r.beats and r.beats<=3: v.append('Missed estimates in 5+ of last 8 quarters')
    if r.rev90==r.rev90 and r.rev90<-0.10: v.append('Analysts cut next-year EPS >10% in 90 days')
    if r.vol>0.55: v.append('Mandate breach: volatility %.0f%% conflicts with your low-risk brief'%(100*r.vol))
    if r.exp_ret<-0.05: v.append('Own valuation models say it is overpriced (probability-weighted return < -5%)')
    V.append(v)
S['veto3']=V
# Confidence agent (0-100)
agent_cols=['A_Quality','A_Growth','A_Valuation','A_Momentum','A_Risk','A_Street']
agree=1-S[agent_cols].std(axis=1)/0.35
comp=S[['fpe','evebitda','roe','om','revg','tgt','nan','fscore','Z','roic','beats','rev90']].notna().mean(axis=1)
S['conf']=100*(0.15*comp+0.20*agree.clip(0,1)+0.15*pr(S.tgt_disp,False)+0.15*(num('beats')/8)+0.20*pr(num('disp'),False)+0.15*(0.5*pr(num('Z').clip(upper=10))+0.5*pr(num('cover').clip(upper=50))))
S['conf']=S.conf.round(0)
S=S.sort_values('s3',ascending=False).reset_index(drop=True); S['rank100']=S.index+1
pick=[];cnt={}
for _,r in S[S.veto3.map(len)==0].iterrows():
    if cnt.get(r.sector,0)>=6: continue
    pick.append(r.t); cnt[r.sector]=cnt.get(r.sector,0)+1
    if len(pick)==30: break
S['top30']=S.t.isin(pick)
T=S[S.top30].copy()
T['rr']=num('exp_ret')[T.index]/num('down')[T.index].abs()
def p2(s,asc=True): s=pd.to_numeric(s,errors='coerce'); return s.rank(pct=True,ascending=asc)
T['final']=100*(0.35*p2(T.rr)+0.25*T.conf/100+0.20*(0.5*T.C_buffett+0.5*T.C_capital)+0.20*T.C_earn)
T=T.sort_values('final',ascending=False).reset_index(drop=True); T['rank30']=T.index+1
T['tier']=np.where((T.rank30<=10)&(T.exp_ret>0.08),'A: Buy now',np.where(T.exp_ret>0.03,'B: Accumulate on dips','C: Watchlist'))
pickle.dump(OVR,open('overrides.pkl','wb')); S.to_pickle('s3_100.pkl'); T.to_pickle('s3_30.pkl')
print('vetoed in 100:',(S.veto3.map(len)>0).sum()); print(pd.Series(cnt).to_string())
print(T[['rank30','t','sector','final','conf','exp_ret','up','down','rr','bscore','beats','tier']].round(2).to_string())
print('Dropped with veto (top by s3):'); print(S[S.veto3.map(len)>0][['rank100','t','s3','veto3']].head(12).to_string())
```

### A.6 `audit.py` — v1 audit agents X1–X3
```python
# AUDIT AGENTS X1 (data), X2 (method & robustness), X3 (output reconciliation)
import pandas as pd, numpy as np, pickle, json
df=pd.read_pickle('s1.pkl'); S=pd.read_pickle('s3_100.pkl'); T=pd.read_pickle('s3_30.pkl'); C=pd.read_pickle('close.pkl')
I=json.load(open('info.json')); OVR=pickle.load(open('overrides.pkl','rb'))
A={}
# X1 data integrity
fields=['fpe','evebitda','roe','om','fcfy','revg','epsg','tgt','beta','vol']
cov={f:float(df[f].notna().mean()) for f in fields}
last=C.index[-1]; stale=[t for t in df.t if C[t].dropna().index[-1]<last-pd.Timedelta(days=5)]
mism=[]
for t in df.t:
    cp=I[t].get('currentPrice') or I[t].get('regularMarketPrice'); p=float(df.loc[df.t==t,'price'].iloc[0])
    if cp and abs(cp/p-1)>0.05: mism.append((t,round(p,2),cp))
outl=df[(df.fpe>150)|(df.revg>2)|(df.epsg>10)][['t','fpe','revg','epsg']].round(2).values.tolist()
A['X1']=dict(universe=int(len(df)),coverage=cov,stale=stale,price_mismatch=mism[:15],n_mismatch=len(mism),outliers=outl[:20],n_outliers=len(outl),asof=str(last.date()),
  deep_complete=int(sum(1 for t in S.t if S.loc[S.t==t,'nq'].iloc[0]>=6)))
# X2 robustness: Monte Carlo on committee weights (+/-50% random perturbation), 500 runs
keys=['C_screen','C_forensic','C_capital','C_earn','C_value','C_buffett']; base=np.array([.25,.10,.10,.15,.25,.15])
elig=S[S.veto3.map(len)==0].reset_index(drop=True); M=elig[keys].values
rng=np.random.default_rng(7); hits=np.zeros(len(elig))
for _ in range(500):
    w=base*rng.uniform(0.5,1.5,6); w/=w.sum(); sc=M@w; top=np.argsort(-sc)[:30]; hits[top]+=1
elig['stab']=hits/500
stab=dict(zip(elig.t,elig.stab.round(2)))
T['stability']=T.t.map(stab)
sec_uni=df.sector.value_counts(normalize=True); sec_30=T.sector.value_counts(normalize=True)
A['X2']=dict(runs=500,stability={t:stab[t] for t in T.t},median_stab=float(T.stability.median()),
  fragile=[t for t in T.t if stab[t]<0.5],sector_tilt={s:(float(sec_30.get(s,0)),float(sec_uni.get(s,0))) for s in sec_uni.index},
  overrides=OVR, vetoes_applied=int((S.veto3.map(len)>0).sum()),
  veto_leak=int(sum(len(v)>0 for v in T.veto3)))
# X3 output reconciliation
chk=[]
for _,r in T.iterrows():
    ok=(r.bull>r.base>r.bear) and 0<=r.conf<=100 and r.up>0 and r.down<0
    if not ok: chk.append(r.t)
A['X3']=dict(scenario_order_fail=chk,n30=int(len(T)),exp_basket=float(T.exp_ret.mean()),top10_exp=float(T.head(10).exp_ret.mean()),
  prior_list={t:(int(S.loc[S.t==t,'rank100'].iloc[0]) if (S.t==t).any() else None, bool((T.t==t).any())) for t in ['NVDA','GOOGL','TSM','LLY','V','BRK-B','AVGO','BLK','ABBV','CVX','META','MSFT','AMZN']},
  prior_rank500={t:int(df.loc[df.t==t,'rank500'].iloc[0]) for t in ['NVDA','GOOGL','LLY','V','BRK-B','AVGO','BLK','ABBV','CVX','META','MSFT','AMZN'] if (df.t==t).any()})
T.to_pickle('s3_30.pkl'); json.dump(A,open('audit.json','w'),default=float)
print(json.dumps({k:{kk:vv for kk,vv in v.items() if kk not in('stability','sector_tilt','coverage')} for k,v in A.items()},default=float,indent=0)[:3500])
print(T[['rank30','t','stability']].to_string())
```

### A.7 `cio.py` — v1 portfolio
```python
import pandas as pd, numpy as np, pickle, json
from scipy.stats import norm
T=pd.read_pickle('s3_30.pkl'); C=pd.read_pickle('close.pkl').ffill(); df=pd.read_pickle('s1.pkl')
T['tier']=np.where((T.exp_ret>=0.08)&(T.stability>=0.7)&(T.conf>=50)&(T.rank30<=15),'A: Buy now',
          np.where(T.exp_ret>=0.03,'B: Accumulate on dips','C: Watchlist'))
pick=[];sec={};sub={};grp_c={}
for _,r in T.sort_values('final',ascending=False).iterrows():
    if r.stability<0.7 or r.exp_ret<0.07: continue
    grp='Insurance' if 'Insurance' in r['sub'] else r['sub']
    if sec.get(r.sector,0)>=3 or sub.get(r['sub'],0)>=1 or grp_c.get(grp,0)>=2: continue
    pick.append(r.t); sec[r.sector]=sec.get(r.sector,0)+1; sub[r['sub']]=sub.get(r['sub'],0)+1; grp_c[grp]=grp_c.get(grp,0)+1
    if len(pick)==10: break
P=T.set_index('t').loc[pick]
raw=P.conf/100*P.exp_ret/P.vol; w=(raw/raw.sum()).clip(0.05,0.15); w=w/w.sum()
for _ in range(5): w=(w.clip(0.05,0.15)); w=w/w.sum()
r=C[pick].pct_change().dropna().iloc[-252:]; cov=r.cov()*252; wv=w.values
vol=float(np.sqrt(wv@cov.values@wv)); mu=float((P.exp_ret*w).sum())
r3=C[pick].pct_change().dropna(); path=(1+r3@wv).cumprod(); mdd=float((path/path.cummax()-1).min())
spx=C['^GSPC'].dropna(); sr=spx.pct_change().dropna()
HC=0.6
port=dict(haircut=HC,exp_cal=mu*HC,p20_cal=float(1-norm.cdf((np.log(1.2)-(mu*HC-vol**2/2))/vol)),pm20_cal=float(norm.cdf((np.log(0.8)-(mu*HC-vol**2/2))/vol)),pick=pick,w=w.round(4).to_dict(),exp=mu,vol=vol,mdd3y=mdd,
  p20=float(1-norm.cdf((np.log(1.2)-(mu-vol**2/2))/vol)),pm20=float(norm.cdf((np.log(0.8)-(mu-vol**2/2))/vol)),
  bull=float((P.up*w).sum()),bear=float((P.down*w).sum()),fpe=float(1/(w/P.fpe).sum()),conf=float((P.conf*w).sum()),
  spx=dict(vol=float(sr.iloc[-252:].std()*np.sqrt(252)),mdd3y=float((spx/spx.cummax()-1).min()),ret1y=float(spx.iloc[-1]/spx.iloc[-252]-1)),
  ret1y_hind=float((1+r@wv).prod()-1), sectors=sec)
T.to_pickle('s3_30.pkl'); json.dump(port,open('port.json','w'),default=float)
print(json.dumps(port,indent=0,default=float)); print(T[['rank30','t','tier','stability','conf','exp_ret']].head(16).to_string())
```

### A.8 `assemble.py` — v1 dashboard data
```python
import pandas as pd, numpy as np, pickle, json
df=pd.read_pickle('s1.pkl'); S=pd.read_pickle('s3_100.pkl'); T=pd.read_pickle('s3_30.pkl')
A=json.load(open('audit.json')); P=json.load(open('port.json')); O=pickle.load(open('s2.pkl','rb'))
sec_fpe=df[df.fpe>0].groupby('sector').fpe.median().to_dict()
def cl(x):
    if isinstance(x,(float,np.floating)): return None if (x!=x or np.isinf(x)) else round(float(x),4)
    if isinstance(x,(np.integer,)): return int(x)
    if isinstance(x,(np.bool_,)): return bool(x)
    if isinstance(x,dict): return {k:cl(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [cl(v) for v in x]
    return x
U=[cl(dict(t=r.t,n=r['name'],s=r.sector,p=r.price,mc=r.mcap,rk=r.rank500,sc=r.s1,q=r.A_Quality,g=r.A_Growth,v=r.A_Valuation,m=r.A_Momentum,rk_=r.A_Risk,st=r.A_Street,
   fpe=r.fpe,rg=r.revg,vol=r.vol,dd=r.mdd3y,up=r.upside,sl=bool(r.short100),vt=list(r.veto),fl=list(r['flags']))) for _,r in df.iterrows()]
DIL={
'AIZ':dict(src='https://www.sec.gov/Archives/edgar/data/0001267238/000126723826000039/aiz-20260630exx991pressrel.htm',notes=['Record Q2 2026: adjusted EPS ex-catastrophes rose 19% to $6.60; GAAP net income up 27%.','Global Lifestyle (device protection, auto service contracts) is the engine: adjusted EBITDA +21%, with Connected Living up 29%.','Full-year 2026 outlook raised; Lifestyle now guided to low-double-digit EBITDA growth.','Capital return continues: $123M returned in Q2 (buybacks plus dividends).','Watch: Global Housing benefited from unusually low claims frequency and catastrophe losses. Hurricane season (Aug to Oct) is the main near-term risk.']),
'CAH':dict(src='https://www.sec.gov/Archives/edgar/data/0000721371/000072137126000037/a26q4_x063026xex991xnewsre.htm',notes=['FY2026 revenue $254B (+14%); non-GAAP EPS $10.95 ex a one-off tariff refund (+33%).','Specialty pharma is the growth engine: segment profit +21%, specialty revenue growth above 25%.','FY2027 guide: EPS $12.40 to $12.60, 13% to 15% growth, above the long-term target.','$1.4B of buybacks in FY26 and a new $5B authorisation; adjusted FCF $5.0B.','Watch: thin-margin distribution model, drug-pricing policy and opioid-litigation overhang.']),
'HIG':dict(src='https://insurancenewsnet.com/oarticle/the-hartford-reports-strong-second-quarter-2026-financial-results',notes=['Q2 2026 core EPS $3.42; trailing core ROE 18.7%.','Business Insurance premiums +5% at an 89.3 underlying combined ratio (profitable underwriting).','New $4.2B buyback through 2028, part-funded by selling Hartford Funds to Wellington.','Net investment income +22% to $800M, helped by higher yields.','Watch: reserve strengthening in general liability and commercial auto; personal-lines premiums fell 7%.']),
'BKNG':dict(src='https://www.sec.gov/Archives/edgar/data/0001075531/000107553126000036/q2-26bkngearningsrelease.htm',notes=['Q2 2026 beat on every line: room nights +5%, gross bookings +9% to $51B, adjusted EPS +15%.','Free cash flow $3.6B in the quarter (+16%); share count down about 6% from buybacks.','Cost programme savings target raised to about $650M run-rate by end-2027.','FY26 guide: high-single-digit revenue growth, low-to-mid-teens adjusted EPS growth.','Watch: Middle East conflict hitting long-haul travel (about 7% of room nights touch the region); EU regulatory probes of its commission model.']),
'BMY':dict(src='https://www.marketbeat.com/instant-alerts/bristol-myers-squibb-q2-earnings-call-highlights-2026-07-30/',notes=['Q2 2026 revenue about $13B (+5%); growth portfolio +14% to $7.6B, now about 60% of sales.','Full-year revenue and EPS guidance raised; Eliquis +21%, Camzyos +59%, Breyanzi +41%.','Pipeline readouts (milvexian, Cobenfy in Alzheimer\'s psychosis) slipped to early 2027.','BEAR CASE IS REAL: Eliquis loses exclusivity in Europe in 2027 and in the US in April 2028, a $1.5B to $2B revenue step-down starting 2027.','Low multiple prices in the patent cliff; upside depends on pipeline hits.']),
'MDT':dict(src='https://www.sec.gov/Archives/edgar/data/0001613103/000162828026059697/exhibit991-fy27q1earningsr.htm',notes=['Q1 FY27 (to July 2026): revenue $9.8B, +13.7% organic, about 2 points above guidance; FY27 guidance raised.','Cardiac ablation surging (+88% globally) on Sphere-9 and Affera; heart-rhythm business +15%.','Hugo surgical robot scaling; diabetes business separation planned before fiscal year-end.','48-year record of annual dividend increases.','Watch: part of Q1 growth came from an extra selling week; robot competition from Intuitive.']),
'CL':dict(src='https://www.sec.gov/Archives/edgar/data/0000021665/000002166526000041/q22026pressreleasetables.htm',notes=['Q2 2026: net sales +4.9%, organic +2.4%; base-business EPS +8%.','Gross margin up 140bps to 61.5%; full-year base EPS guidance raised to mid-single-digit growth.','Global toothpaste share 41.3% (up 0.2pts); manual toothbrush share 32.7%.','Advertising up 15% to defend brands; first-half operating cash flow +17%.','Watch: slow organic growth (1% to 4% guide) caps upside; this is a ballast holding, not a growth engine.']),
'NVDA':dict(src='https://finance.yahoo.com/quote/NVDA/',notes=['Fiscal Q2 2027 revenue grew 106% year on year to $96.2B.','Forward P/E about 14x on consensus, cheaper than the S&P 500 despite leading growth.','Next-year EPS estimates rose about 24% in 90 days (42 upward revisions, 0 down in 30 days).','Customers (Meta, Google) building their own chips with Broadcom: a long-run share risk.','Weighted at only about 5% because it is the most volatile name in the portfolio.'])}
def bullbear(r,o):
    b=[];x=[]
    if r.revg==r.revg and r.revg>0.10: b.append(f'Revenue growing {r.revg*100:.0f}% a year')
    if o['roic']==o['roic'] and o['roic']>0.20: b.append(f'High return on capital ({o["roic"]*100:.0f}%)')
    if o['beats']==o['beats'] and o['beats']>=7: b.append(f'Beat earnings estimates in {o["beats"]} of last {o["nq"]} quarters')
    if o['rev90']==o['rev90'] and o['rev90']>0.03: b.append(f'Analysts raised next-year EPS by {o["rev90"]*100:.0f}% in 90 days')
    if o['sh_chg']==o['sh_chg'] and o['sh_chg']<-0.02: b.append(f'Share count down {abs(o["sh_chg"])*100:.0f}% (buybacks)')
    if r.fpe==r.fpe and r.fpe>0 and r.fpe<sec_fpe.get(r.sector,20)*0.85: b.append(f'Cheaper than its sector ({r.fpe:.1f}x vs {sec_fpe.get(r.sector,20):.1f}x forward P/E)')
    if r.fcfy==r.fcfy and r.fcfy>0.05: b.append(f'Free-cash-flow yield {r.fcfy*100:.1f}%')
    if o['bscore']>=6: b.append(f'Passes {o["bscore"]}/8 Buffett tests')
    if r.tt>=6: b.append('Price in a healthy uptrend (trend template 6+/7)')
    if r.vol>0.35: x.append(f'Volatile: price swings about {r.vol*100:.0f}% a year')
    if o['down']<-0.25: x.append(f'Bear case is a {o["down"]*100:.0f}% fall')
    if o['rev90']==o['rev90'] and o['rev90']<-0.02: x.append(f'Analysts cut next-year EPS {o["rev90"]*100:.0f}% in 90 days')
    if r.fpe==r.fpe and r.fpe>sec_fpe.get(r.sector,20)*1.3: x.append(f'Expensive vs sector ({r.fpe:.1f}x vs {sec_fpe.get(r.sector,20):.1f}x)')
    if r.nd_ebitda==r.nd_ebitda and r.nd_ebitda>3: x.append(f'Leveraged: net debt {r.nd_ebitda:.1f}x EBITDA')
    if r.revg==r.revg and r.revg<0.03: x.append(f'Slow growth ({r.revg*100:.1f}%)')
    if o['ins_net']==o['ins_net'] and o['ins_net']<0: x.append('Insiders net sellers over 6 months')
    om=[v for v in o['om_a'] if v is not None]
    if len(om)>=3 and om[0]<om[-1]-0.03: x.append('Operating margin lower than 3 years ago')
    if o['disp']>0.35: x.append('Valuation methods disagree widely (lower certainty)')
    for f in r['flags']: x.append(f)
    return b[:7],x[:7]
def company(t):
    r=S[S.t==t].iloc[0]; o=O[t]; b,x=bullbear(r,o); tt=T[T.t==t]
    d=dict(t=t,n=r['name'],s=r.sector,sub=r['sub'],p=r.price,mc=r.mcap,sum=r.summary,web=r.website,emp=r.employees,rk500=r.rank500,rk100=r.rank100,s1=r.s1,s3=r.s3,
      ag=dict(Quality=r.A_Quality,Growth=r.A_Growth,Valuation=r.A_Valuation,Momentum=r.A_Momentum,Risk=r.A_Risk,Street=r.A_Street),
      cm=dict(Screen=r.C_screen,Forensic=r.C_forensic,Capital=r.C_capital,Earnings=r.C_earn,Value=r.C_value,Buffett=r.C_buffett),
      k=dict(fpe=r.fpe,tpe=r.tpe,eve=r.evebitda,pb=r.pb,fcfy=r.fcfy,divy=r.divy,roe=r.roe,om=r.om,gm=r.gm,revg=r.revg,epsg=r.epsg,de=r.de,nde=r.nd_ebitda,vol=r.vol,beta=r.beta,dd=r.mdd3y,r12=r.ret12,r6=r.ret6,offhi=r.off_hi,tt=r.tt,short=r.short,ins=r.insider,rec=r.rec,nan=r.nan,tgt=r.tgt,tlo=r.tgt_lo,thi=r.tgt_hi),
      debate=[list(z) for z in r.debate],veto3=list(r.veto3),top30=bool(r.top30),conf=r.conf,
      bull_pts=b,bear_pts=x,**{kk:o[kk] for kk in ['yrs','rev_a','ni_a','fcf_a','om_a','roe_a','eps_a','cagr','roic','sh_chg','cover','fscore','Z','accr','buyback','div','beats','nq','avg_surp','eq_hist','next_date','eps0y','eps1y','rev90','up30','dn30','ups','downs','ins_net','news','qs','q_yoy','wacc','impl_g','g1','methods','fair','disp','base','bull','bear','exp','exp_ret','up','down','base_ret','buffett','bscore','capex_adj','oneoff']})
    if len(tt): tt=tt.iloc[0]; d.update(rk30=int(tt.rank30),final=tt.final,tier=tt.tier,stab=tt.stability,rr=tt.rr)
    if t in DIL: d['dil']=DIL[t]
    return cl(d)
C100={t:company(t) for t in S.t}
agents=[
 ('Stage 1: Screening committee (497 stocks)',[('A1 Quality & Moat (Buffett lens)','Return on equity, margins, cash conversion, leverage, ranked within each sector.'),('A2 Growth','Revenue, earnings and forward EPS growth.'),('A3 Valuation','Forward P/E and EV/EBITDA vs sector, FCF yield, analyst upside.'),('A4 Momentum & Trend','Minervini 7-point trend template, 6-month relative strength vs S&P, 12-month return.'),('A5 Risk','Volatility, downside volatility, 3-year max drawdown, worst 12-month loss, beta.'),('A6 Street Sentiment','Analyst ratings, target upside, coverage breadth, short interest.'),('A7 Red Team','Hard vetoes (no profit, cash burn, fell >60%) and soft flags (leverage, weak cash conversion, shrinking revenue, peak-cycle earnings).')]),
 ('Stage 2: Diligence team (100 stocks)',[('A8 Forensic Accountant','Piotroski F-score, Altman Z, accruals, interest cover from 4 years of statements.'),('A9 Capital Allocation','Return on invested capital, buybacks vs dilution, dividends, growth-capex adjustment.'),('A10 Earnings Record','Last 8 quarterly reports (2 years): beats/misses, surprise size, 90-day estimate revisions, upgrades vs downgrades.'),('A11 Intrinsic Value','Up to 4 methods: forward multiple, 10-year DCF with reverse-DCF implied growth, justified P/B for banks and insurers, Street target. Bear, base and bull prices.')]),
 ('Stage 3: Investment committee (100 to 30 to ranked)',[('A12 Bull Advocate','Builds the strongest data-backed case for each stock.'),('A13 Bear Advocate / Devil\'s Advocate','Vetoes: distress balance sheet, serial misses, falling estimates, overvaluation, low-risk mandate breach.'),('A14 Confidence Officer','Scores 0 to 100 from data completeness, agent agreement, analyst dispersion, earnings reliability, valuation-method agreement and balance-sheet strength.'),('A15 Portfolio Construction (CIO)','Picks the final 10 with sector, sub-industry and insurance caps; weights by confidence x return / volatility.')]),
 ('Audit layer',[('X1 Data Integrity Auditor','Coverage, stale prices, price reconciliation, outliers.'),('X2 Methodology & Robustness Auditor','500-run weight-sensitivity test, veto consistency, sector tilt, overturned vetoes.'),('X3 Output Reconciliation Auditor','Scenario ordering, reconciliation with prior answers, calibration haircut on returns.')])]
dstats={}
for d in df.debate:
    for z in d: dstats[z[0]]=dstats.get(z[0],0)+1
self_fix=[('Cash-conversion flag misfired on AI spenders','Red team flagged GOOGL, MSFT, META, AMZN, LLY for weak cash conversion. The capital-allocation agent showed operating cash covers profit and the gap is growth capex. Flag withdrawn for these names.'),
 ('DCF used one-off profits as the growth base','GOOGL\'s trailing EPS includes one-off investment gains, so forecast growth looked negative (DCF of $73). The auditor added a one-off detector. 8 companies were corrected.'),
 ('Payment networks were valued like banks','Visa and Mastercard were run through a bank P/B model (Visa at $120). They were re-routed to DCF, alongside exchanges, data firms and asset managers.'),
 ('Growth-capex companies had understated DCFs','LLY, MSFT and others building capacity had depressed FCF. Normalised owner earnings (70% of profit) were applied when capex exceeds 1.5x depreciation. 11 companies adjusted.'),
 ('Bear cases were too gentle for stocks that only went up','SNDK showed a 3% bear case because its short history had no down year. A volatility-based floor was added; its bear case is now -58%.'),
 ('Altman Z-score wrongly vetoed asset-light firms','EXPE, BLK, CPAY and FANG failed Z but have healthy interest cover. Veto now requires weak debt metrics as well. 4 vetoes overturned.'),
 ('Low-risk mandate was not enforced','A 75%-volatility memory stock reached the top 30. The mandate agent now vetoes volatility above 55%.'),
 ('Portfolio had 3 correlated insurers','CIO rules tightened to one stock per sub-industry and at most two insurers.')]
out=dict(asof=A['X1']['asof'],U=U,C=C100,top30=[c for c in T.t],P=P,A=A,agents=agents,dstats=dstats,self_fix=self_fix,sec_fpe=sec_fpe,
  funnel=dict(u=len(df),veto1=int(df.vetoed.sum()),s100=100,veto3=int((S.veto3.map(len)>0).sum()),s30=30,final=10))
json.dump(cl(out),open('dash.json','w'))
import os; print(os.path.getsize('dash.json')/1e6,'MB')
```

### A.9 `bt_pull.py` — Statements for all 497
```python
import yfinance as yf, pandas as pd, pickle, os, sys, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
U=pd.read_pickle('s1.pkl').t.tolist()
F=pickle.load(open('fund_all.pkl','rb')) if os.path.exists('fund_all.pkl') else {}
todo=[t for t in U if t not in F][:int(sys.argv[1])]
def g(t):
    k=yf.Ticker(t); o={}
    for nm,fn in [('inc',lambda:k.income_stmt),('bs',lambda:k.balance_sheet),('cf',lambda:k.cashflow)]:
        try: o[nm]=fn()
        except Exception: o[nm]=None
    return t,o
with ThreadPoolExecutor(20) as ex:
    for t,o in ex.map(g,todo): F[t]=o
pickle.dump(F,open('fund_all.pkl','wb')); print('have',len(F),'of',len(U))
```

### A.10 `backtest.py` — PIT backtest v1
```python
# BACKTEST AGENT: point-in-time replay of the screening model, 3 out-of-sample years
import pandas as pd, numpy as np, pickle, json, warnings
from scipy.stats import spearmanr
warnings.filterwarnings('ignore')
F=pickle.load(open('fund_all.pkl','rb')); C=pd.read_pickle('close10.pkl').ffill(); U=pd.read_pickle('s1.pkl')[['t','sector']]
sec=dict(zip(U.t,U.sector))
def row(d,names):
    if d is None: return None
    for n in names:
        if n in d.index: return d.loc[n]
    return None
def at(s,cut):  # latest annual value with period end <= cut, and the prior one
    if s is None: return (np.nan,np.nan)
    s=s.dropna(); s=s[[c for c in s.index if c<=cut]].sort_index(ascending=False)
    return (float(s.iloc[0]) if len(s) else np.nan, float(s.iloc[1]) if len(s)>1 else np.nan)
spx=C['^GSPC']
res={}; allrows=[]
for yr in [2023,2024,2025]:
    t0=pd.Timestamp(f'{yr}-09-29'); t1=pd.Timestamp(f'{yr+1}-09-24') if yr==2025 else pd.Timestamp(f'{yr+1}-09-27')
    i0=C.index[C.index<=t0][-1]; i1=C.index[C.index<=t1][-1]; cut=t0-pd.Timedelta(days=90)
    rows=[]
    for t,o in F.items():
        if t not in C or C[t].loc[:i0].dropna().shape[0]<300 or np.isnan(C[t].loc[i1]): continue
        I,B,CF=o['inc'],o['bs'],o['cf']
        rev=at(row(I,['Total Revenue','Operating Revenue']),cut); ni=at(row(I,['Net Income Common Stockholders','Net Income']),cut)
        opi=at(row(I,['Operating Income','EBIT']),cut); gp=at(row(I,['Gross Profit']),cut); eb=at(row(I,['EBITDA','Normalized EBITDA']),cut)
        sh=at(row(I,['Diluted Average Shares','Basic Average Shares']),cut); eq=at(row(B,['Stockholders Equity','Common Stock Equity']),cut)
        debt=at(row(B,['Total Debt']),cut); cash=at(row(B,['Cash Cash Equivalents And Short Term Investments','Cash And Cash Equivalents']),cut)
        ocf=at(row(CF,['Operating Cash Flow']),cut); cx=at(row(CF,['Capital Expenditure']),cut)
        eps=at(row(I,['Diluted EPS','Basic EPS']),cut)
        if np.isnan(rev[0]) or np.isnan(sh[0]): continue
        c=C[t].loc[:i0].dropna(); p=float(c.iloc[-1]); mc=p*sh[0]; r=c.pct_change().iloc[-252:]
        sma50,sma150,sma200=c.rolling(50).mean().iloc[-1],c.rolling(150).mean().iloc[-1],c.rolling(200).mean().iloc[-1]
        hi,lo=c.iloc[-252:].max(),c.iloc[-252:].min()
        fcf=ocf[0]+(cx[0] if cx[0]==cx[0] else 0)
        al=pd.concat([r,spx.loc[:i0].pct_change().iloc[-252:]],axis=1).dropna()
        rows.append(dict(t=t,sector=sec.get(t),roe=ni[0]/eq[0] if eq[0] and eq[0]>0 else np.nan,om=opi[0]/rev[0],gm=gp[0]/rev[0] if gp[0]==gp[0] else np.nan,
          fcfm=fcf/rev[0],nde=((debt[0] if debt[0]==debt[0] else 0)-(cash[0] if cash[0]==cash[0] else 0))/eb[0] if eb[0] and eb[0]>0 else np.nan,
          revg=rev[0]/rev[1]-1 if rev[1] and rev[1]>0 else np.nan, epsg=eps[0]/eps[1]-1 if eps[1] and eps[1]>0 else np.nan,
          ey=ni[0]/mc, fcfy=fcf/mc, sy=rev[0]/mc, ret12=p/c.iloc[-252]-1, ret6=p/c.iloc[-126]-1,
          tt=int(p>sma50)+int(sma50>sma150)+int(sma150>sma200)+int(p>sma200)+int(p/hi-1>-.25)+int(p/lo-1>.3),
          vol=r.std()*np.sqrt(252), mdd=(c.iloc[-756:]/c.iloc[-756:].cummax()-1).min(),
          beta=np.cov(al.iloc[:,0],al.iloc[:,1])[0,1]/al.iloc[:,1].var(),
          veto=(ni[0]<=0) or (fcf<0 and sec.get(t) not in('Financials','Real Estate')) or ((c.iloc[-756:]/c.iloc[-756:].cummax()-1).min()<-0.6),
          fwd=float(C[t].loc[i1]/p-1)))
    d=pd.DataFrame(rows)
    def pr(col,asc=True,bys=False,clip=None):
        s=d[col].astype(float); s=s.clip(*clip) if clip else s; s=s.fillna(s.median())
        return s.groupby(d.sector).rank(pct=True,ascending=asc) if bys else s.rank(pct=True,ascending=asc)
    d['Q']=(pr('roe',True,True,(-1,1.5))+pr('om',True,True)+pr('fcfm',True,True,(-1,1))+pr('gm',True,True)+pr('nde',False,False,(-5,10)))/5
    d['G']=(pr('revg',clip=(-.5,1.5))+pr('epsg',clip=(-1,2)))/2
    d['V']=(pr('ey',True,True,(-.5,.5))+pr('fcfy',True,True,(-.3,.3))+pr('sy',True,True))/3
    d['M']=(d.tt/6+pr('ret6')+pr('ret12',clip=(-1,3)))/3
    d['R']=(pr('vol',False)+pr('mdd')+pr('beta',False))/3
    W=dict(Q=.25,G=.18,V=.20,M=.14,R=.23)
    d['score']=sum(W[k]*d[k] for k in W)
    e=d[~d.veto]
    q=e.score.rank(pct=True)
    top10=e.nlargest(10,'score'); top30=e.nlargest(30,'score'); topq=e[q>=0.8]; botq=e[q<=0.2]
    ic=spearmanr(e.score,e.fwd).correlation
    pic={k:spearmanr(e[k],e.fwd).correlation for k in ['Q','G','V','M','R']}
    res[yr]=dict(n=len(d),n_elig=len(e),spx=float(spx.loc[i1]/spx.loc[i0]-1),ew=float(d.fwd.mean()),elig_ew=float(e.fwd.mean()),
       top10=float(top10.fwd.mean()),top30=float(top30.fwd.mean()),topq=float(topq.fwd.mean()),botq=float(botq.fwd.mean()),vetoed=float(d[d.veto].fwd.mean()),
       ic=float(ic),pillar_ic=pic,top10_names=top10.t.tolist(),hit15_top30=float((top30.fwd>=0.15).mean()),hit15_all=float((e.fwd>=0.15).mean()),
       top30_vol=float(top30.vol.mean()),all_vol=float(e.vol.mean()))
json.dump(res,open('backtest.json','w'),default=float)
for y,v in res.items():
    print(y,'n',v['n'],'SPX %.1f%% EW %.1f%% | top10 %.1f%% top30 %.1f%% topQ %.1f%% botQ %.1f%% vetoed %.1f%% | IC %.3f | hit15 top30 %.0f%% vs all %.0f%%'%(100*v['spx'],100*v['ew'],100*v['top10'],100*v['top30'],100*v['topq'],100*v['botq'],100*v['vetoed'],v['ic'],100*v['hit15_top30'],100*v['hit15_all']))
    print('   pillar IC',{k:round(x,3) for k,x in v['pillar_ic'].items()})
```

### A.11 `backtest2.py` — PIT backtest, weights as argument
```python
# BACKTEST AGENT: point-in-time replay of the screening model, 3 out-of-sample years
import pandas as pd, numpy as np, pickle, json, warnings
from scipy.stats import spearmanr
warnings.filterwarnings('ignore')
F=pickle.load(open('fund_all.pkl','rb')); C=pd.read_pickle('close10.pkl').ffill(); U=pd.read_pickle('s1.pkl')[['t','sector']]
sec=dict(zip(U.t,U.sector))
def row(d,names):
    if d is None: return None
    for n in names:
        if n in d.index: return d.loc[n]
    return None
def at(s,cut):  # latest annual value with period end <= cut, and the prior one
    if s is None: return (np.nan,np.nan)
    s=s.dropna(); s=s[[c for c in s.index if c<=cut]].sort_index(ascending=False)
    return (float(s.iloc[0]) if len(s) else np.nan, float(s.iloc[1]) if len(s)>1 else np.nan)
spx=C['^GSPC']
import sys
WTS=eval(sys.argv[1]); res={}; allrows=[]
for yr in [2023,2024,2025]:
    t0=pd.Timestamp(f'{yr}-09-29'); t1=pd.Timestamp(f'{yr+1}-09-24') if yr==2025 else pd.Timestamp(f'{yr+1}-09-27')
    i0=C.index[C.index<=t0][-1]; i1=C.index[C.index<=t1][-1]; cut=t0-pd.Timedelta(days=90)
    rows=[]
    for t,o in F.items():
        if t not in C or C[t].loc[:i0].dropna().shape[0]<300 or np.isnan(C[t].loc[i1]): continue
        I,B,CF=o['inc'],o['bs'],o['cf']
        rev=at(row(I,['Total Revenue','Operating Revenue']),cut); ni=at(row(I,['Net Income Common Stockholders','Net Income']),cut)
        opi=at(row(I,['Operating Income','EBIT']),cut); gp=at(row(I,['Gross Profit']),cut); eb=at(row(I,['EBITDA','Normalized EBITDA']),cut)
        sh=at(row(I,['Diluted Average Shares','Basic Average Shares']),cut); eq=at(row(B,['Stockholders Equity','Common Stock Equity']),cut)
        debt=at(row(B,['Total Debt']),cut); cash=at(row(B,['Cash Cash Equivalents And Short Term Investments','Cash And Cash Equivalents']),cut)
        ocf=at(row(CF,['Operating Cash Flow']),cut); cx=at(row(CF,['Capital Expenditure']),cut)
        eps=at(row(I,['Diluted EPS','Basic EPS']),cut)
        if np.isnan(rev[0]) or np.isnan(sh[0]): continue
        c=C[t].loc[:i0].dropna(); p=float(c.iloc[-1]); mc=p*sh[0]; r=c.pct_change().iloc[-252:]
        sma50,sma150,sma200=c.rolling(50).mean().iloc[-1],c.rolling(150).mean().iloc[-1],c.rolling(200).mean().iloc[-1]
        hi,lo=c.iloc[-252:].max(),c.iloc[-252:].min()
        fcf=ocf[0]+(cx[0] if cx[0]==cx[0] else 0)
        al=pd.concat([r,spx.loc[:i0].pct_change().iloc[-252:]],axis=1).dropna()
        rows.append(dict(t=t,sector=sec.get(t),roe=ni[0]/eq[0] if eq[0] and eq[0]>0 else np.nan,om=opi[0]/rev[0],gm=gp[0]/rev[0] if gp[0]==gp[0] else np.nan,
          fcfm=fcf/rev[0],nde=((debt[0] if debt[0]==debt[0] else 0)-(cash[0] if cash[0]==cash[0] else 0))/eb[0] if eb[0] and eb[0]>0 else np.nan,
          revg=rev[0]/rev[1]-1 if rev[1] and rev[1]>0 else np.nan, epsg=eps[0]/eps[1]-1 if eps[1] and eps[1]>0 else np.nan,
          ey=ni[0]/mc, fcfy=fcf/mc, sy=rev[0]/mc, ret12=p/c.iloc[-252]-1, ret6=p/c.iloc[-126]-1,
          tt=int(p>sma50)+int(sma50>sma150)+int(sma150>sma200)+int(p>sma200)+int(p/hi-1>-.25)+int(p/lo-1>.3),
          vol=r.std()*np.sqrt(252), mdd=(c.iloc[-756:]/c.iloc[-756:].cummax()-1).min(),
          beta=np.cov(al.iloc[:,0],al.iloc[:,1])[0,1]/al.iloc[:,1].var(),
          veto=(ni[0]<=0) or (fcf<0 and sec.get(t) not in('Financials','Real Estate')) or ((c.iloc[-756:]/c.iloc[-756:].cummax()-1).min()<-0.6),
          fwd=float(C[t].loc[i1]/p-1)))
    d=pd.DataFrame(rows)
    def pr(col,asc=True,bys=False,clip=None):
        s=d[col].astype(float); s=s.clip(*clip) if clip else s; s=s.fillna(s.median())
        return s.groupby(d.sector).rank(pct=True,ascending=asc) if bys else s.rank(pct=True,ascending=asc)
    d['Q']=(pr('roe',True,True,(-1,1.5))+pr('om',True,True)+pr('fcfm',True,True,(-1,1))+pr('gm',True,True)+pr('nde',False,False,(-5,10)))/5
    d['G']=(pr('revg',clip=(-.5,1.5))+pr('epsg',clip=(-1,2)))/2
    d['V']=(pr('ey',True,True,(-.5,.5))+pr('fcfy',True,True,(-.3,.3))+pr('sy',True,True))/3
    d['M']=(d.tt/6+pr('ret6')+pr('ret12',clip=(-1,3)))/3
    d['R']=(pr('vol',False)+pr('mdd')+pr('beta',False))/3
    W=WTS
    d['score']=sum(W[k]*d[k] for k in W)
    e=d[~d.veto]
    q=e.score.rank(pct=True)
    top10=e.nlargest(10,'score'); top30=e.nlargest(30,'score'); topq=e[q>=0.8]; botq=e[q<=0.2]
    ic=spearmanr(e.score,e.fwd).correlation
    pic={k:spearmanr(e[k],e.fwd).correlation for k in ['Q','G','V','M','R']}
    res[yr]=dict(n=len(d),n_elig=len(e),spx=float(spx.loc[i1]/spx.loc[i0]-1),ew=float(d.fwd.mean()),elig_ew=float(e.fwd.mean()),
       top10=float(top10.fwd.mean()),top30=float(top30.fwd.mean()),topq=float(topq.fwd.mean()),botq=float(botq.fwd.mean()),vetoed=float(d[d.veto].fwd.mean()),
       ic=float(ic),pillar_ic=pic,top10_names=top10.t.tolist(),hit15_top30=float((top30.fwd>=0.15).mean()),hit15_all=float((e.fwd>=0.15).mean()),
       top30_vol=float(top30.vol.mean()),all_vol=float(e.vol.mean()))
json.dump(res,open(sys.argv[2],'w'),default=float)
for y,v in res.items():
    print(y,'n',v['n'],'SPX %.1f%% EW %.1f%% | top10 %.1f%% top30 %.1f%% topQ %.1f%% botQ %.1f%% vetoed %.1f%% | IC %.3f | hit15 top30 %.0f%% vs all %.0f%%'%(100*v['spx'],100*v['ew'],100*v['top10'],100*v['top30'],100*v['topq'],100*v['botq'],100*v['vetoed'],v['ic'],100*v['hit15_top30'],100*v['hit15_all']))
    print('   pillar IC',{k:round(x,3) for k,x in v['pillar_ic'].items()})
```

### A.12 `backtest3.py` — PIT backtest + saves frames (for conviction test)
```python
# BACKTEST AGENT: point-in-time replay of the screening model, 3 out-of-sample years
import pandas as pd, numpy as np, pickle, json, warnings
from scipy.stats import spearmanr
warnings.filterwarnings('ignore')
F=pickle.load(open('fund_all.pkl','rb')); C=pd.read_pickle('close10.pkl').ffill(); U=pd.read_pickle('s1.pkl')[['t','sector']]
sec=dict(zip(U.t,U.sector))
def row(d,names):
    if d is None: return None
    for n in names:
        if n in d.index: return d.loc[n]
    return None
def at(s,cut):  # latest annual value with period end <= cut, and the prior one
    if s is None: return (np.nan,np.nan)
    s=s.dropna(); s=s[[c for c in s.index if c<=cut]].sort_index(ascending=False)
    return (float(s.iloc[0]) if len(s) else np.nan, float(s.iloc[1]) if len(s)>1 else np.nan)
spx=C['^GSPC']
import sys
WTS=eval(sys.argv[1]); res={}; allrows=[]
for yr in [2023,2024,2025]:
    t0=pd.Timestamp(f'{yr}-09-29'); t1=pd.Timestamp(f'{yr+1}-09-24') if yr==2025 else pd.Timestamp(f'{yr+1}-09-27')
    i0=C.index[C.index<=t0][-1]; i1=C.index[C.index<=t1][-1]; cut=t0-pd.Timedelta(days=90)
    rows=[]
    for t,o in F.items():
        if t not in C or C[t].loc[:i0].dropna().shape[0]<300 or np.isnan(C[t].loc[i1]): continue
        I,B,CF=o['inc'],o['bs'],o['cf']
        rev=at(row(I,['Total Revenue','Operating Revenue']),cut); ni=at(row(I,['Net Income Common Stockholders','Net Income']),cut)
        opi=at(row(I,['Operating Income','EBIT']),cut); gp=at(row(I,['Gross Profit']),cut); eb=at(row(I,['EBITDA','Normalized EBITDA']),cut)
        sh=at(row(I,['Diluted Average Shares','Basic Average Shares']),cut); eq=at(row(B,['Stockholders Equity','Common Stock Equity']),cut)
        debt=at(row(B,['Total Debt']),cut); cash=at(row(B,['Cash Cash Equivalents And Short Term Investments','Cash And Cash Equivalents']),cut)
        ocf=at(row(CF,['Operating Cash Flow']),cut); cx=at(row(CF,['Capital Expenditure']),cut)
        eps=at(row(I,['Diluted EPS','Basic EPS']),cut)
        if np.isnan(rev[0]) or np.isnan(sh[0]): continue
        c=C[t].loc[:i0].dropna(); p=float(c.iloc[-1]); mc=p*sh[0]; r=c.pct_change().iloc[-252:]
        sma50,sma150,sma200=c.rolling(50).mean().iloc[-1],c.rolling(150).mean().iloc[-1],c.rolling(200).mean().iloc[-1]
        hi,lo=c.iloc[-252:].max(),c.iloc[-252:].min()
        fcf=ocf[0]+(cx[0] if cx[0]==cx[0] else 0)
        al=pd.concat([r,spx.loc[:i0].pct_change().iloc[-252:]],axis=1).dropna()
        rows.append(dict(t=t,sector=sec.get(t),roe=ni[0]/eq[0] if eq[0] and eq[0]>0 else np.nan,om=opi[0]/rev[0],gm=gp[0]/rev[0] if gp[0]==gp[0] else np.nan,
          fcfm=fcf/rev[0],nde=((debt[0] if debt[0]==debt[0] else 0)-(cash[0] if cash[0]==cash[0] else 0))/eb[0] if eb[0] and eb[0]>0 else np.nan,
          revg=rev[0]/rev[1]-1 if rev[1] and rev[1]>0 else np.nan, epsg=eps[0]/eps[1]-1 if eps[1] and eps[1]>0 else np.nan,
          ey=ni[0]/mc, fcfy=fcf/mc, sy=rev[0]/mc, ret12=p/c.iloc[-252]-1, ret6=p/c.iloc[-126]-1,
          tt=int(p>sma50)+int(sma50>sma150)+int(sma150>sma200)+int(p>sma200)+int(p/hi-1>-.25)+int(p/lo-1>.3),
          vol=r.std()*np.sqrt(252), mdd=(c.iloc[-756:]/c.iloc[-756:].cummax()-1).min(),
          beta=np.cov(al.iloc[:,0],al.iloc[:,1])[0,1]/al.iloc[:,1].var(),
          veto=(ni[0]<=0) or (fcf<0 and sec.get(t) not in('Financials','Real Estate')) or ((c.iloc[-756:]/c.iloc[-756:].cummax()-1).min()<-0.6),
          fwd=float(C[t].loc[i1]/p-1)))
    d=pd.DataFrame(rows)
    def pr(col,asc=True,bys=False,clip=None):
        s=d[col].astype(float); s=s.clip(*clip) if clip else s; s=s.fillna(s.median())
        return s.groupby(d.sector).rank(pct=True,ascending=asc) if bys else s.rank(pct=True,ascending=asc)
    d['Q']=(pr('roe',True,True,(-1,1.5))+pr('om',True,True)+pr('fcfm',True,True,(-1,1))+pr('gm',True,True)+pr('nde',False,False,(-5,10)))/5
    d['G']=(pr('revg',clip=(-.5,1.5))+pr('epsg',clip=(-1,2)))/2
    d['V']=(pr('ey',True,True,(-.5,.5))+pr('fcfy',True,True,(-.3,.3))+pr('sy',True,True))/3
    d['M']=(d.tt/6+pr('ret6')+pr('ret12',clip=(-1,3)))/3
    d['R']=(pr('vol',False)+pr('mdd')+pr('beta',False))/3
    W=WTS
    d['score']=sum(W[k]*d[k] for k in W)
    allrows.append(d.assign(yr=yr))
    e=d[~d.veto]
    q=e.score.rank(pct=True)
    top10=e.nlargest(10,'score'); top30=e.nlargest(30,'score'); topq=e[q>=0.8]; botq=e[q<=0.2]
    ic=spearmanr(e.score,e.fwd).correlation
    pic={k:spearmanr(e[k],e.fwd).correlation for k in ['Q','G','V','M','R']}
    res[yr]=dict(n=len(d),n_elig=len(e),spx=float(spx.loc[i1]/spx.loc[i0]-1),ew=float(d.fwd.mean()),elig_ew=float(e.fwd.mean()),
       top10=float(top10.fwd.mean()),top30=float(top30.fwd.mean()),topq=float(topq.fwd.mean()),botq=float(botq.fwd.mean()),vetoed=float(d[d.veto].fwd.mean()),
       ic=float(ic),pillar_ic=pic,top10_names=top10.t.tolist(),hit15_top30=float((top30.fwd>=0.15).mean()),hit15_all=float((e.fwd>=0.15).mean()),
       top30_vol=float(top30.vol.mean()),all_vol=float(e.vol.mean()))
json.dump(res,open(sys.argv[2],'w'),default=float); pd.concat(allrows).to_pickle('bt_frames.pkl')
for y,v in res.items():
    print(y,'n',v['n'],'SPX %.1f%% EW %.1f%% | top10 %.1f%% top30 %.1f%% topQ %.1f%% botQ %.1f%% vetoed %.1f%% | IC %.3f | hit15 top30 %.0f%% vs all %.0f%%'%(100*v['spx'],100*v['ew'],100*v['top10'],100*v['top30'],100*v['topq'],100*v['botq'],100*v['vetoed'],v['ic'],100*v['hit15_top30'],100*v['hit15_all']))
    print('   pillar IC',{k:round(x,3) for k,x in v['pillar_ic'].items()})
```

### A.13 `bt10.py` — 10-yr factor test
```python
# 10-YEAR PRICE-FACTOR BACKTEST (monthly rebalance, top 50 equal weight) — tests which style can clear 15%
import pandas as pd, numpy as np, json
C=pd.read_pickle('close10.pkl').ffill(); spx=C.pop('^GSPC')
M=C.resample('ME').last(); Ms=spx.resample('ME').last()
R=M.pct_change(); Rs=Ms.pct_change()
D=C.pct_change()
vol=D.rolling(252).std().resample('ME').last()*np.sqrt(252)
mom12_1=M.shift(1)/M.shift(12)-1; mom6=M/M.shift(6)-1
sma200=C.rolling(200).mean().resample('ME').last(); hi=C.rolling(252).max().resample('ME').last()
trend=((M>sma200).astype(int)+(M/hi>0.75).astype(int))
def pr(x): return x.rank(axis=1,pct=True)
S={'Momentum (12-1)':pr(mom12_1),'Low volatility':pr(-vol),'Momentum + low vol':(pr(mom12_1)+pr(-vol))/2,
   'Momentum + trend, vol-capped':pr(mom12_1).where(vol<0.45)+0.25*trend,'Equal-weight universe':pr(M*0+1)}
out={}
for k,sc in S.items():
    rets=[]
    for i in range(13,len(M)-1):
        s=sc.iloc[i].dropna()
        if k=='Equal-weight universe': pick=s.index
        else: pick=s.nlargest(50).index
        rets.append(R.iloc[i+1][pick].mean())
    r=pd.Series(rets,index=M.index[14:])
    eq=(1+r).cumprod(); r12=(1+r).rolling(12).apply(np.prod,raw=True)-1
    yrs=len(r)/12
    out[k]=dict(cagr=float(eq.iloc[-1]**(1/yrs)-1),vol=float(r.std()*np.sqrt(12)),mdd=float((eq/eq.cummax()-1).min()),
      p15=float((r12.dropna()>=0.15).mean()),p25=float((r12.dropna()>=0.25).mean()),p50=float((r12.dropna()>=0.50).mean()),ploss20=float((r12.dropna()<=-0.20).mean()),
      worst12=float(r12.min()),y2022=float((1+r['2022']).prod()-1),y2020=float((1+r['2020-02':'2020-03']).prod()-1))
rs=Rs.iloc[14:]; eq=(1+rs).cumprod(); r12=(1+rs).rolling(12).apply(np.prod,raw=True)-1; yrs=len(rs)/12
out['S&P 500']=dict(cagr=float(eq.iloc[-1]**(1/yrs)-1),vol=float(rs.std()*np.sqrt(12)),mdd=float((eq/eq.cummax()-1).min()),p15=float((r12.dropna()>=0.15).mean()),p25=float((r12.dropna()>=0.25).mean()),p50=float((r12.dropna()>=0.5).mean()),ploss20=float((r12.dropna()<=-0.2).mean()),worst12=float(r12.min()),y2022=float((1+rs['2022']).prod()-1),y2020=float((1+rs['2020-02':'2020-03']).prod()-1))
json.dump(out,open('bt10.json','w'))
print(pd.DataFrame(out).T.round(3).to_string())
```

### A.14 `est_pull.py` — Estimates for all 497
```python
import yfinance as yf, pandas as pd, pickle, os, sys, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
U=pd.read_pickle('s1.pkl').t.tolist(); D=pickle.load(open('deep.pkl','rb'))
E=pickle.load(open('est_all.pkl','rb')) if os.path.exists('est_all.pkl') else {}
for t in U:
    if t in D and t not in E: E[t]=dict(trend=D[t]['trend'],rev=D[t]['rev'],ed=D[t]['ed'],ud=D[t]['ud'])
todo=[t for t in U if t not in E][:int(sys.argv[1])]
def g(t):
    k=yf.Ticker(t); o={}
    for nm,fn in [('trend',lambda:k.eps_trend),('rev',lambda:k.eps_revisions),('ed',lambda:k.get_earnings_dates(limit=12)),('ud',lambda:k.upgrades_downgrades)]:
        try: o[nm]=fn()
        except Exception: o[nm]=None
    return t,o
with ThreadPoolExecutor(16) as ex:
    for t,o in ex.map(g,todo): E[t]=o
pickle.dump(E,open('est_all.pkl','wb')); print('have',len(E))
```

### A.15 `v3.py` — v2 scoring (v3 model) + 3 return methods
```python
# V3 "HURDLE-15" MODEL: momentum + earnings momentum + value (building-block E[R]) + quality guardrail; risk as constraint, not a return pillar
import pandas as pd, numpy as np, pickle, json, warnings
warnings.filterwarnings('ignore')
df=pd.read_pickle('s1.pkl'); E=pickle.load(open('est_all.pkl','rb')); F=pickle.load(open('fund_all.pkl','rb')); I=json.load(open('info.json'))
C=pd.read_pickle('close10.pkl').ffill()
def v(x):
    try: x=float(x); return x if x==x else np.nan
    except Exception: return np.nan
rows=[]
for _,r in df.iterrows():
    t=r.t; e=E.get(t,{}); i=I.get(t,{}); tr=e.get('trend'); rv=e.get('rev'); ed=e.get('ed'); ud=e.get('ud')
    if tr is not None and ('current' not in tr.columns or '90daysAgo' not in tr.columns): tr=None
    if rv is not None and ('upLast30days' not in rv.columns or 'downLast30days' not in rv.columns): rv=None
    if ed is not None and ('Reported EPS' not in ed.columns or 'Surprise(%)' not in ed.columns): ed=None
    if ud is not None and 'Action' not in getattr(ud,'columns',[]): ud=None
    eps0=v(tr.loc['0y','current']) if tr is not None and '0y' in tr.index else np.nan
    eps1=v(tr.loc['+1y','current']) if tr is not None and '+1y' in tr.index else np.nan
    e90=v(tr.loc['+1y','90daysAgo']) if tr is not None and '+1y' in tr.index else np.nan
    rev90=eps1/e90-1 if e90 and e90>0 and eps1==eps1 else np.nan
    up=v(rv.loc['+1y','upLast30days']) if rv is not None and '+1y' in rv.index else np.nan
    dn=v(rv.loc['+1y','downLast30days']) if rv is not None and '+1y' in rv.index else np.nan
    nan=i.get('numberOfAnalystOpinions') or np.nan
    netrev=(np.nan_to_num(up)-np.nan_to_num(dn))/max(nan,1) if nan==nan else np.nan
    beats=surp=np.nan
    if ed is not None and len(ed):
        x=ed.dropna(subset=['Reported EPS']).head(8)
        if len(x): beats=(x['Surprise(%)']>0).mean(); surp=x['Surprise(%)'].clip(-30,30).mean()
    ups=dns=0
    if ud is not None and len(ud):
        try:
            cut=pd.Timestamp.now(tz=ud.index.tz)-pd.Timedelta(days=90) if ud.index.tz else pd.Timestamp.now()-pd.Timedelta(days=90)
            u=ud[ud.index>=cut]; ups=int((u.Action=='up').sum()); dns=int((u.Action=='down').sum())
        except Exception: pass
    # shareholder yield
    cf=F.get(t,{}).get('cf'); bb=0.0; iss=0.0
    if cf is not None and len(cf.columns):
        c0=cf.columns[0]
        for nm in ['Repurchase Of Capital Stock','Common Stock Payments']:
            if nm in cf.index and v(cf.loc[nm,c0])==v(cf.loc[nm,c0]): bb=-v(cf.loc[nm,c0]); break
        for nm in ['Issuance Of Capital Stock','Common Stock Issuance']:
            if nm in cf.index and v(cf.loc[nm,c0])==v(cf.loc[nm,c0]): iss=v(cf.loc[nm,c0]); break
    mc=(i.get('marketCap') or np.nan)
    dy=i.get('trailingAnnualDividendYield') or 0
    nby=np.clip((bb-iss)/mc,-0.05,0.08) if mc==mc and mc>0 else 0
    g=np.clip(eps1/eps0-1,-0.3,0.6) if (eps0==eps0 and eps0>0 and eps1==eps1) else (r.fwd_epsg if r.fwd_epsg==r.fwd_epsg else np.nan)
    c=C[t].dropna(); p=float(c.iloc[-1])
    mom=float(c.iloc[-22]/c.iloc[-253]-1) if len(c)>260 else np.nan
    rows.append(dict(t=t,eps0=eps0,eps1=eps1,rev90=rev90,netrev=netrev,beats8=beats,surp=surp,ups=ups,dns=dns,dy=dy,nby=nby,g=g,mom121=mom))
X=df.merge(pd.DataFrame(rows),on='t')
art=(X.g>0.35)&(X.revg.fillna(0)<0.10)
X['g_artifact']=art; X.loc[art,'g']=np.clip(X.loc[art,'revg'].fillna(0),0,None)+0.10
sec_fpe=X[X.fpe>0].groupby('sector').fpe.median(); sec_g=X.groupby('sector').g.median()
def pr(s,asc=True,bys=False,clip=None):
    s=pd.to_numeric(s,errors='coerce'); s=s.clip(*clip) if clip else s; s=s.fillna(s.median())
    return s.groupby(X.sector).rank(pct=True,ascending=asc) if bys else s.rank(pct=True,ascending=asc)
# Building-block expected return (fundamental method)
HC_G=0.70  # haircut analysts' next-year EPS growth by 30% (assumption: consensus runs optimistic)
Qp=X.A_Quality
fair=X.sector.map(sec_fpe)*(0.8+0.4*Qp)*(1+np.clip(X.g.fillna(0)-X.sector.map(sec_g).fillna(0),-0.2,0.3))
rer=np.clip((fair/X.fpe.where(X.fpe>0))**(1/3)-1,-0.10,0.10).fillna(-0.05)
X['bb_yield']=X.dy.fillna(0)+X.nby.fillna(0); X['bb_growth']=np.clip(HC_G*X.g.fillna(0),-0.25,0.30); X['bb_rerate']=rer
X['E_bb']=np.clip(X.bb_yield+X.bb_growth+X.bb_rerate,-0.3,0.40)
# Pillars
X['P_mom']=(pr(X.mom121,clip=(-1,3))+pr(X.ret6,clip=(-1,3))+X.tt/7)/3
X['P_emom']=(pr(X.rev90,clip=(-.5,1))+pr(X.netrev)+pr(X.beats8)+pr(X.surp)+pr(X.ups-X.dns))/5
X['P_val']=(pr(X.E_bb)+pr(X.fcfy,True,True,(-.2,.2))+pr(X.fpe.where(X.fpe>0),False,True))/3
X['P_q']=X.A_Quality
W=dict(P_mom=.30,P_emom=.20,P_val=.30,P_q=.20)
X['v3']=100*sum(W[k]*X[k] for k in W)
X['gate']=~X.vetoed & (X.vol<=0.60) & (X.fpe>0)
X['gate_why']=np.where(X.vetoed,'Stage-1 veto',np.where(X.vol>0.60,'Volatility >60%',np.where(~(X.fpe>0),'No forward profit','')))
X=X.sort_values('v3',ascending=False).reset_index(drop=True); X['rank_v3']=X.index+1
gp=X.v3.where(X.gate).rank(pct=True)
W3=C.resample('W-FRI').last().pct_change().iloc[-156:]; sw=W3['^GSPC']
b3={t:(np.cov(W3[t].dropna(),sw[W3[t].dropna().index])[0,1]/sw[W3[t].dropna().index].var()) if t in W3 and W3[t].notna().sum()>100 else np.nan for t in X.t}
X['beta3']=X.t.map(b3)
badj=np.clip(0.67*X.beta3.fillna(1)+0.33,0.6,1.6)
X['alpha']=np.clip(0.028*(gp-0.5)/0.44,-0.03,0.03).fillna(-0.02)
X['E_fac']=0.10*badj+X.alpha
S2=pickle.load(open('s2.pkl','rb'))
X['E_scen']=X.t.map(lambda t: 0.6*S2[t]['exp_ret'] if t in S2 else np.nan)
X['E_final']=X[['E_bb','E_fac','E_scen']].mean(axis=1)
X['E_spread']=X[['E_bb','E_fac','E_scen']].max(axis=1)-X[['E_bb','E_fac','E_scen']].min(axis=1)
X.to_pickle('v3.pkl')
g=X[X.gate]
print('gated',len(g)); print(g[['rank_v3','t','sector','v3','P_mom','P_emom','P_val','P_q','E_bb','vol','fpe','g','rev90']].head(40).round(2).to_string())
```

### A.16 `edgar.py` — EDGAR downloader (v2 pool)
```python
# EARNINGS-RELEASE READER AGENT: pulls every 8-K Item 2.02 press release (last ~2 years) from SEC EDGAR and reads it
import requests, json, re, time, pickle, os, pandas as pd, numpy as np
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Independent equity research (personal, non-commercial) research-bot@proton.me','Accept-Encoding':'gzip, deflate'}
X=pd.read_pickle('v3.pkl'); g=X[X.gate]
pool=[];cnt={}
for _,r in g.iterrows():
    if cnt.get(r.sector,0)>=8: continue
    pool.append(r.t); cnt[r.sector]=cnt.get(r.sector,0)+1
    if len(pool)==45: break
prev=json.load(open('port.json'))['pick']; pool=list(dict.fromkeys(pool+prev))
tk=requests.get('https://www.sec.gov/files/company_tickers.json',headers=H,timeout=30).json()
cik={v['ticker'].replace('.','-'):str(v['cik_str']).zfill(10) for v in tk.values()}
OUT=pickle.load(open('edgar.pkl','rb')) if os.path.exists('edgar.pkl') else {}
def get(u):
    for k in range(3):
        try:
            time.sleep(0.15); r=requests.get(u,headers=H,timeout=30)
            if r.status_code==200: return r
        except Exception: pass
        time.sleep(1)
    return None
def txt(html):
    html=re.sub(r'(?is)<(script|style).*?</\1>',' ',html); t=re.sub(r'(?s)<[^>]+>',' ',html)
    t=re.sub(r'&nbsp;|&#160;',' ',t); t=re.sub(r'&amp;','&',t); t=re.sub(r'&#8217;|&rsquo;',"'",t); t=re.sub(r'&#\d+;|&\w+;',' ',t)
    return re.sub(r'\s+',' ',t)
def one(t):
    if t in OUT or t not in cik: return t,OUT.get(t)
    c=cik[t]; r=get(f'https://data.sec.gov/submissions/CIK{c}.json')
    if r is None: return t,None
    rec=r.json()['filings']['recent']; docs=[]
    for i,f in enumerate(rec['form']):
        if f=='8-K' and '2.02' in (rec['items'][i] or '') and rec['filingDate'][i]>='2024-07-01':
            acc=rec['accessionNumber'][i].replace('-','')
            ix=get(f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/index.json')
            if ix is None: continue
            items=[x['name'] for x in ix.json()['directory']['item'] if x['name'].lower().endswith(('.htm','.html'))]
            ex=[x for x in items if re.search(r'ex-?99|exh?99|ex99|pressrel|earningsrel|q\d.*release',x.lower())] or [x for x in items if x!=rec['primaryDocument'][i] and 'index' not in x.lower()]
            if not ex: continue
            d=get(f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/{ex[0]}')
            if d is None: continue
            docs.append(dict(date=rec['filingDate'][i],url=f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/{ex[0]}',text=txt(d.text)[:60000]))
        if len(docs)>=9: break
    return t,docs
with ThreadPoolExecutor(4) as ex:
    for t,d in ex.map(one,pool): OUT[t]=d
pickle.dump(OUT,open('edgar.pkl','wb'))
print('companies',len([t for t in pool if OUT.get(t)]),'of',len(pool),'releases',sum(len(OUT[t]) for t in pool if OUT.get(t)))
```

### A.17 `edgar2.py` — EDGAR downloader for a ticker list (fixed exhibit filter)
```python
# EARNINGS-RELEASE READER AGENT: pulls every 8-K Item 2.02 press release (last ~2 years) from SEC EDGAR and reads it
import requests, json, re, time, pickle, os, pandas as pd, numpy as np
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Independent equity research (personal, non-commercial) research-bot@proton.me','Accept-Encoding':'gzip, deflate'}
import sys
pool=sys.argv[1].split(',')
tk=requests.get('https://www.sec.gov/files/company_tickers.json',headers=H,timeout=30).json()
cik={v['ticker'].replace('.','-'):str(v['cik_str']).zfill(10) for v in tk.values()}
OUT=pickle.load(open('edgar.pkl','rb')) if os.path.exists('edgar.pkl') else {}
def get(u):
    for k in range(3):
        try:
            time.sleep(0.15); r=requests.get(u,headers=H,timeout=30)
            if r.status_code==200: return r
        except Exception: pass
        time.sleep(1)
    return None
def txt(html):
    html=re.sub(r'(?is)<(script|style).*?</\1>',' ',html); t=re.sub(r'(?s)<[^>]+>',' ',html)
    t=re.sub(r'&nbsp;|&#160;',' ',t); t=re.sub(r'&amp;','&',t); t=re.sub(r'&#8217;|&rsquo;',"'",t); t=re.sub(r'&#\d+;|&\w+;',' ',t)
    return re.sub(r'\s+',' ',t)
def one(t):
    if t in OUT or t not in cik: return t,OUT.get(t)
    c=cik[t]; r=get(f'https://data.sec.gov/submissions/CIK{c}.json')
    if r is None: return t,None
    rec=r.json()['filings']['recent']; docs=[]
    for i,f in enumerate(rec['form']):
        if f=='8-K' and '2.02' in (rec['items'][i] or '') and rec['filingDate'][i]>='2024-07-01':
            acc=rec['accessionNumber'][i].replace('-','')
            ix=get(f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/index.json')
            if ix is None: continue
            items=[x['name'] for x in ix.json()['directory']['item'] if x['name'].lower().endswith(('.htm','.html'))]
            ex=[x for x in items if re.search(r'ex-?99|exh?99|ex99|pressrel|earningsrel|q\d.*release|pr\.htm',x.lower()) and 'cfo' not in x.lower()] or [x for x in items if x!=rec['primaryDocument'][i] and 'index' not in x.lower()]
            if not ex: continue
            d=get(f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/{ex[0]}')
            if d is None: continue
            docs.append(dict(date=rec['filingDate'][i],url=f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/{ex[0]}',text=txt(d.text)[:60000]))
        if len(docs)>=9: break
    return t,docs
with ThreadPoolExecutor(4) as ex:
    for t,d in ex.map(one,pool): OUT[t]=d
pickle.dump(OUT,open('edgar.pkl','wb'))
print('companies',len([t for t in pool if OUT.get(t)]),'of',len(pool),'releases',sum(len(OUT[t]) for t in pool if OUT.get(t)))
```

### A.18 `edgar_read.py` — Release reader
```python
import pickle, re, json, pandas as pd, numpy as np
E=pickle.load(open('edgar.pkl','rb'))
RAISE=re.compile(r'\b(rais(e|es|ed|ing)|increas(e|es|ed|ing)|lift(s|ed)?|boost(s|ed)?|upgrad(e|ed)|above the high end|improv(e|es|ed))\b[^.]{0,120}\b(guidance|outlook|forecast|expectations?)\b|\b(guidance|outlook|forecast)\b[^.]{0,60}\b(rais(e|ed)|increas(e|ed))\b',re.I)
CUT=re.compile(r'\b(lower(s|ed|ing)?|reduc(e|es|ed|ing)|cut(s)?|withdr(aw|ew)|below)\b[^.]{0,120}\b(guidance|outlook|forecast)\b|\b(guidance|outlook)\b[^.]{0,60}\b(lowered|reduced|cut)\b',re.I)
KEEP=re.compile(r'\b(reaffirm(s|ed)?|maintain(s|ed)?|reiterat(e|es|ed)|confirm(s|ed)?)\b[^.]{0,120}\b(guidance|outlook)\b',re.I)
FLAG=dict(record=r'\brecord\b',headwind=r'\bheadwinds?\b',impair=r'\bimpairment',restruct=r'\brestructuring\b',investig=r'\b(investigation|subpoena)\b',weakness=r'\bmaterial weakness\b',goingc=r'\bgoing concern\b',buyback=r'\b(share repurchase|buyback|repurchased)\b',ai=r'\b(artificial intelligence|\bAI\b|generative)\b',tariff=r'\btariffs?\b')
res={}
for t,docs in E.items():
    if not docs: continue
    rows=[]
    for d in docs:
        tx=d['text'][:40000]
        sents=re.split(r'(?<=[.!?])\s+',tx)
        gs=[s for s in sents if re.search(r'\b(guidance|outlook)\b',s,re.I) and 30<len(s)<420]
        rows.append(dict(date=d['date'],url=d['url'],raise_=bool(RAISE.search(tx[:15000])),cut=bool(CUT.search(tx[:15000])),keep=bool(KEEP.search(tx[:15000])),
             **{k:len(re.findall(p,tx,re.I)) for k,p in FLAG.items()},gsent=gs[:3],head=tx[:500]))
    df=pd.DataFrame(rows).sort_values('date')
    n=len(df); r_=int(df.raise_.sum()); c_=int(df.cut.sum()); k_=int(df.keep.sum())
    last=df.iloc[-1]
    res[t]=dict(n=n,raises=r_,cuts=c_,keeps=k_,gscore=(r_-c_)/n,last_date=last.date,last_url=last.url,last_raise=bool(last.raise_),last_cut=bool(last.cut),
       record=int(df.record.sum()),headwind=int(df.headwind.sum()),impair=int(df.impair.sum()),restruct=int(df.restruct.sum()),investig=int(df.investig.sum()),
       weakness=int(df.weakness.sum()),goingc=int(df.goingc.sum()),ai=int(df.ai.sum()),tariff=int(df.tariff.sum()),
       timeline=[dict(d=x.date,r=bool(x.raise_),c=bool(x.cut),k=bool(x.keep),rec=int(x.record),hw=int(x.headwind)) for x in df.itertuples()],
       latest_guidance=list(dict.fromkeys(sum([x for x in df.gsent.iloc[-2:]],[])))[:4])
json.dump(res,open('edgar_read.json','w'))
T=pd.DataFrame(res).T[['n','raises','cuts','keeps','gscore','last_date','last_raise','last_cut','record','headwind','impair','investig','weakness']]
print(T.sort_values('gscore',ascending=False).to_string())
```

### A.19 `opt.py` — v2 optimiser + bootstrap
```python
# CIO v2: candidate ranking + mandate optimizer + fat-tailed probability engine (10-yr block bootstrap)
import pandas as pd, numpy as np, json, pickle
from scipy.optimize import minimize
X=pd.read_pickle('v3.pkl').set_index('t'); ER=json.load(open('edgar_read.json')); C=pd.read_pickle('close10.pkl').ffill()
pool=[t for t in ER if t in X.index and X.loc[t,'gate']]
K=X.loc[pool].copy()
K['gscore']=[ER[t]['gscore'] for t in pool]; K['gcut']=[ER[t]['cuts'] for t in pool]
comp=K[['fpe','roe','revg','rev90','beats8','E_scen','beta3','fcfy']].notna().mean(axis=1)
agree=1-np.clip(K.E_spread/0.35,0,1)
K['conf2']=(100*(0.30*agree+0.15*comp+0.20*K.beats8.fillna(.5)+0.20*np.clip(0.5+K.gscore,0,1)+0.15*K.A_Quality)).round(0)
pr=lambda s: s.rank(pct=True)
K['score2']=100*(0.35*pr(K.E_final)+0.25*pr(K.v3)+0.15*pr(K.conf2)+0.15*pr(K.gscore)+0.10*pr(K.A_Quality))
K=K.sort_values('score2',ascending=False); K['rank52']=range(1,len(K)+1)
badj=np.clip(0.67*K.beta3.fillna(1)+0.33,0.6,1.6)
wc=(K.conf2/100)*(1-np.clip(K.E_spread.fillna(0.2)/0.4,0,0.5))
K['E_prior']=0.10*badj; K['E_sh']=wc*K.E_final+(1-wc)*K.E_prior
el=K[(K.E_sh>=0.09)&(K.conf2>=50)&(K.A_Quality>=0.35)].index.tolist()
M=C[el].resample('ME').last().pct_change().iloc[-121:].dropna(how='all')
Wk=C[el].resample('W-FRI').last().pct_change().iloc[-157:]
S=Wk.cov()*52; S=0.7*S+0.3*np.diag(np.diag(S))   # shrink toward diagonal
mu0=K.loc[el,'E_sh'].values.copy(); mu=mu0.copy(); subs=K.loc[el,'sub'].values; secs=K.loc[el,'sector'].values; caps=np.where(K.loc[el,'conf2']>=75,0.10,0.07)
def solve(vol_cap):
    n=len(el); x0=np.ones(n)/n
    cons=[{'type':'eq','fun':lambda w:w.sum()-1},{'type':'ineq','fun':lambda w:vol_cap**2-w@S.values@w}]
    for s in set(secs): cons.append({'type':'ineq','fun':lambda w,s=s:0.30-w[secs==s].sum()})
    for s in set(subs): cons.append({'type':'ineq','fun':lambda w,s=s:0.12-w[subs==s].sum()})
    r=minimize(lambda w:-(w@mu)+0.5*np.sum(np.maximum(w-0.0,0)**2)*0.02,x0,bounds=[(0,c) for c in caps],constraints=cons,method='SLSQP',options={'maxiter':200,'ftol':1e-7})
    w=pd.Series(r.x,index=el); w=w[w>0.02]; w=w/w.sum(); return w
def boot(w,E,n=20000,blk=3,seed=1):
    rng=np.random.default_rng(seed); m=M[w.index].fillna(0).values@w.values
    m=m-m.mean()+(1+E)**(1/12)-1; T=len(m); out=np.empty(n)
    for i in range(n):
        idx=np.concatenate([np.arange(s,s+blk)%T for s in rng.integers(0,T,12//blk)]); out[i]=np.prod(1+m[idx])-1
    return out
def stats(w):
    E=float((w*K.loc[w.index,'E_sh']).sum()); Eraw=float((w*K.loc[w.index,'E_final']).sum()); v=float(np.sqrt(w.values@S.loc[w.index,w.index].values@w.values))
    b=boot(w,E); hist=(1+(M[w.index].fillna(0)@w)).cumprod()
    y22=float((1+M[w.index].fillna(0).loc['2022']@w).prod()-1); c20=float((1+M[w.index].fillna(0).loc['2020-02':'2020-03']@w).prod()-1)
    return dict(E=E,E_raw=Eraw,vol=v,p15=float((b>=.15).mean()),p20=float((b>=.20).mean()),p25=float((b>=.25).mean()),p50=float((b>=.5).mean()),p0=float((b>=0).mean()),
      pl10=float((b<=-.10).mean()),pl20=float((b<=-.20).mean()),p5=float(np.percentile(b,5)),p50th=float(np.median(b)),p95=float(np.percentile(b,95)),
      y2022=y22,covid=c20,mdd10=float((hist/hist.cummax()-1).min()),n=int(len(w)),beta=float((w*K.loc[w.index,'beta3']).sum()),conf=float((w*K.loc[w.index,'conf2']).sum()),
      w=w.round(4).to_dict())
# Resampled efficiency (Michaud): perturb expected returns by their own method disagreement, re-optimise 150x, average weights
rng=np.random.default_rng(42); sd=np.clip(K.loc[el,'E_spread'].fillna(0.15).values/2,0.02,0.12)
def resampled(vc,runs=40):
    global mu; acc=pd.Series(0.0,index=el); hits=pd.Series(0,index=el)
    for _ in range(runs):
        mu=mu0+rng.normal(0,sd); w=solve(vc); acc[w.index]+=w; hits[w.index]+=1
    mu=mu0.copy(); w=acc/runs; w=w[w>0.015]; return w/w.sum(), (hits/runs)
P={}
for name,vc in [('Guardian',0.14),('Balanced',0.16),('Hurdle',0.18),('Stretch',0.22)]:
    w,h=resampled(vc); P[name]=stats(w); P[name]['vol_cap']=vc; P[name]['hit']=h[h>0].round(2).to_dict()
spx=C['^GSPC'].resample('ME').last().pct_change().iloc[-121:].dropna()
P['S&P 500 (for reference)']=dict(E=0.10,vol=float(spx.std()*np.sqrt(12)))
pickle.dump(K,open('K.pkl','wb')); json.dump(P,open('port2.json','w'),default=float)
for k,v in P.items():
    if 'w' not in v: continue
    print(k,'n',v['n'],'E %.1f%% vol %.1f%% beta %.2f | P15 %.0f%% P20 %.0f%% P25 %.0f%% P50 %.1f%% P>=0 %.0f%% P<=-20 %.1f%% | median %.1f%% 5th %.1f%% 95th %.1f%% | 2022 %.1f%% covid %.1f%% conf %.0f'%(100*v['E'],100*v['vol'],v['beta'],100*v['p15'],100*v['p20'],100*v['p25'],100*v['p50'],100*v['p0'],100*v['pl20'],100*v['p50th'],100*v['p5'],100*v['p95'],100*v['y2022'],100*v['covid'],v['conf']))
    print('   ',{a:round(b,3) for a,b in sorted(v['w'].items(),key=lambda z:-z[1])})
print(K[['rank52','sector','score2','E_final','conf2','gscore','v3','vol']].head(25).round(3).to_string())

# Recommended = resampled Hurdle trimmed to its 20 most robust names (weight x hit-rate), re-normalised
h=pd.Series(P['Hurdle']['hit']); w=pd.Series(P['Hurdle']['w'])
keep=(w*h.reindex(w.index).fillna(0)).nlargest(20).index; wr=w[keep]/w[keep].sum()
P['Recommended']=stats(wr); P['Recommended']['hit']=h.reindex(keep).round(2).to_dict()
json.dump(P,open('port2.json','w'),default=float)
v=P['Recommended']; print('REC n',v['n'],'E %.1f%% (raw %.1f%%) vol %.1f%% beta %.2f | P15 %.0f%% P20 %.0f%% P25 %.0f%% P50 %.1f%% P>=0 %.0f%% P<=-10 %.0f%% P<=-20 %.1f%% | 5th %.1f%% median %.1f%% 95th %.1f%% | 2022 %.1f%% covid %.1f%% mdd10 %.1f%% conf %.0f'%(100*v['E'],100*v['E_raw'],100*v['vol'],v['beta'],100*v['p15'],100*v['p20'],100*v['p25'],100*v['p50'],100*v['p0'],100*v['pl10'],100*v['pl20'],100*v['p5'],100*v['p50th'],100*v['p95'],100*v['y2022'],100*v['covid'],100*v['mdd10'],v['conf']))
print({a:round(b,3) for a,b in sorted(v['w'].items(),key=lambda z:-z[1])})
print(K.loc[list(v['w'].keys()),['sector','sub','E_sh','conf2','gscore','vol']].round(3).to_string())
```

### A.20 `assemble2.py` — v2 dashboard data
```python
import pandas as pd, numpy as np, json, pickle
K=pickle.load(open('K.pkl','rb')); X=pd.read_pickle('v3.pkl'); ER=json.load(open('edgar_read.json')); P2=json.load(open('port2.json'))
BT=dict(v1=json.load(open('backtest.json')),v3=json.load(open('bt_v3.json')),v3b=json.load(open('bt_v3b.json')),f10=json.load(open('bt10.json')))
def cl(x):
    if isinstance(x,(float,np.floating)): return None if (x!=x or np.isinf(x)) else round(float(x),4)
    if isinstance(x,(np.integer,)): return int(x)
    if isinstance(x,(np.bool_,)): return bool(x)
    if isinstance(x,dict): return {str(k):cl(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [cl(v) for v in x]
    return x
C2={}
for t,r in K.iterrows():
    e=ER[t]
    C2[t]=cl(dict(t=t,n=r['name'],s=r.sector,sub=r['sub'],p=r.price,rk=int(r.rank52),v3=r.v3,pm=r.P_mom,pe=r.P_emom,pv=r.P_val,pq=r.P_q,
      Ebb=r.E_bb,by=r.bb_yield,bg=r.bb_growth,br=r.bb_rerate,Efac=r.E_fac,Escen=r.E_scen,Ef=r.E_final,Esh=r.E_sh,Esp=r.E_spread,conf=r.conf2,
      g=r.g,rev90=r.rev90,beats=r.beats8,mom=r.mom121,vol=r.vol,beta=r.beta3,fpe=r.fpe,fcfy=r.fcfy,roe=r.roe,revg=r.revg,dd=r.mdd3y,art=bool(r.g_artifact),
      nrel=e['n'],raises=e['raises'],cuts=e['cuts'],keeps=e['keeps'],gs=e['gscore'],tl=e['timeline'],url=e['last_url'],flags=dict(record=e['record'],headwind=e['headwind'],investig=e['investig'],weakness=e['weakness'],goingc=e['goingc'],tariff=e['tariff'],ai=e['ai'])))
U3=[cl(dict(t=r.t,n=r['name'],s=r.sector,rk=int(r.rank_v3),v3=r.v3,pm=r.P_mom,pe=r.P_emom,pv=r.P_val,pq=r.P_q,E=r.E_final,vol=r.vol,gate=bool(r.gate),why=r.gate_why)) for _,r in X.iterrows()]
fix2=[('My v1 model had the wrong risk tilt','A point-in-time backtest showed the low-volatility pillar lost money in all 3 test years (information coefficient −0.14, −0.05, −0.26), and v1\'s top 30 lagged the S&P by 10, 5 and 8 points. Low-vol was removed as a return driver and kept only as a constraint.'),
 ('Dividend-yield unit bug','Yields under 0.5% were being read as 44% to 47% (for example NVDA, REGN, AAPL). Switched to the trailing-yield field and re-ran everything.'),
 ('One-off earnings made growth look explosive','Merck, Freeport and 8 others showed 60% EPS growth because last year\'s EPS was depressed by one-off charges. Growth is now capped at revenue growth + 10pts when the two diverge.'),
 ('1-year betas were noisy (some negative)','Replaced with 3-year weekly betas for all 497 stocks.'),
 ('Optimiser maximised estimation error','A raw return-maximiser piled into cyclicals with the shakiest forecasts (airlines, autos). Fixed with confidence-weighted shrinkage toward a market prior (Black-Litterman style), a quality floor, confidence-based position caps, and 40-run resampled optimisation.'),
 ('Hidden concentration','Sub-industry cap of 12% added (online travel, asset managers).'),
 ('Alpha from the backtest overstated','Backtested excess return was shrunk 58%, in line with McLean and Pontiff\'s published post-publication decay of return predictors.')]
grade=[('Universe & data breadth','497 stocks, 11 years of prices, 4-5 years of statements, full estimate history',10,10),
 ('Primary-source reading','467 SEC earnings releases (2 years, 52 companies) read by machine for guidance raises, cuts and red flags; 8 releases read in full',9,10),
 ('Valuation rigour','3 independent methods (building-block, factor, scenario/DCF) with reverse DCF, shrinkage and disagreement tracking',9,10),
 ('Out-of-sample validation','3-year point-in-time backtest plus 10-year factor test; found and fixed my own model\'s flaw',9,10),
 ('Risk modelling','20,000-path block bootstrap on 10 years including COVID and 2022, stress replays, resampled optimisation',9,10),
 ('Portfolio vs mandate','Efficient frontier with explicit odds for 15%, 20%, 25% and 50% outcomes',9,10),
 ('Error discovery','15 model errors found and fixed across v1 and v2',10,10),
 ('Honesty of probabilities','Shrunk estimates reported next to raw; limits stated',10,10),
 ('Company-level qualitative depth','Guidance trajectories for 52 companies; deep human-style notes for only 8. No earnings-call transcripts or expert calls',7,10),
 ('Actionability','Exact weights; order sheet needs your amount and broker',9,10)]
out=dict(C2=C2,U3=U3,P2=P2,BT=BT,fix2=fix2,grade=grade)
json.dump(cl(out),open('dash2.json','w')); import os; print(os.path.getsize('dash2.json')/1e6,'MB', sum(g[2] for g in grade))
```

### A.21 `audit_loop1.py` — Audit loops (Turn 6)
```python
# AUDIT LOOP 1 (3 auditors in parallel): holdings integrity, survivorship-bias quantification, assumption sensitivity
import pandas as pd, numpy as np, json, pickle, yfinance as yf, re, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
K=pickle.load(open('K.pkl','rb')); P=json.load(open('port2.json')); E=pickle.load(open('edgar.pkl','rb')); w=pd.Series(P['Recommended']['w'])
def holdings():
    out=[]
    for t in w.index:
        r=K.loc[t]; docs=E.get(t) or []
        nm=re.sub(r'[^A-Za-z ]','',r['name']).split()[0].lower()
        ok=sum(1 for d in docs if nm in d['text'][:3000].lower())
        out.append(dict(t=t,w=w[t],vol=r.vol,conf=r.conf2,Ebb=r.E_bb,Efac=r.E_fac,Escen=r.E_scen,spread=r.E_spread,fpe=r.fpe,art=bool(r.g_artifact),docs=len(docs),name_match=ok))
    return pd.DataFrame(out)
def survivorship():
    px=yf.download(['RSP','SPY'],start='2023-09-20',end='2026-09-25',auto_adjust=True,progress=False)['Close']
    bt=json.load(open('backtest.json')); v3=json.load(open('bt_v3.json')); res={}
    for y,(a,b) in {'2023':('2023-09-29','2024-09-27'),'2024':('2024-09-27','2025-09-26'),'2025':('2025-09-26','2026-09-24')}.items():
        r=lambda s:float(px[s].loc[:b].iloc[-1]/px[s].loc[:a].iloc[-1]-1)
        res[y]=dict(RSP=r('RSP'),EW_survivors=bt[y]['ew'],bias=bt[y]['ew']-r('RSP'),v3_top30=v3[y]['top30'],v3_vs_RSP=v3[y]['top30']-r('RSP'),v3_vs_EWsurv=v3[y]['top30']-bt[y]['ew'])
    return res
def sensitivity():
    ws=w; k=K.loc[ws.index]; badj=np.clip(0.67*k.beta3.fillna(1)+0.33,0.6,1.6)
    def Esh(mkt=0.10,hc=0.70,amax=0.028):
        bb=np.clip(k.bb_yield+np.clip(hc*k.g.fillna(0),-0.25,0.30)+k.bb_rerate,-0.3,0.4)
        fac=mkt*badj+np.clip(amax*(k.alpha/0.028),-0.03,0.03)
        ef=pd.concat([bb,fac,k.E_scen],axis=1).mean(axis=1); sp=pd.concat([bb,fac,k.E_scen],axis=1).max(axis=1)-pd.concat([bb,fac,k.E_scen],axis=1).min(axis=1)
        wc=(k.conf2/100)*(1-np.clip(sp/0.4,0,0.5)); return float((ws*(wc*ef+(1-wc)*mkt*badj)).sum())
    base=Esh(); rows={'Base case':base}
    for lab,kw in [('Market prior 8%',dict(mkt=0.08)),('Market prior 12%',dict(mkt=0.12)),('Growth haircut 50%',dict(hc=0.5)),('No growth haircut',dict(hc=1.0)),('Alpha zero',dict(amax=0.0)),('Alpha unshrunk (6.7%)',dict(amax=0.067))]: rows[lab]=Esh(**kw)
    return rows
with ThreadPoolExecutor(3) as ex:
    f1,f2,f3=ex.submit(holdings),ex.submit(survivorship),ex.submit(sensitivity)
    H,S,T=f1.result(),f2.result(),f3.result()
print(H.round(3).to_string()); print(json.dumps({k:{a:round(b,3) for a,b in v.items()} for k,v in S.items()})); print({k:round(v,4) for k,v in T.items()})
json.dump(dict(surv=S,sens=T),open('audit_loop1.json','w'))
```

### A.22 `notes2.py` — v2 holdings notes
```python
import json
N={
'GEN':['Q1 FY27 (to 3 Jul 2026): revenue beat its own guidance range; non-GAAP EPS grew high-teens; full-year guidance raised.','Model sees it as deep value: about 7x forward earnings with 5 guidance raises in 9 quarters.','Watch: acquisition-funded balance sheet (check leverage); consumer cyber-safety is a mature market.'],
'HPE':['Fiscal Q3 2026: record revenue of $12.2B, up 34%; operating profit also a record.','Raised outlook for both fiscal 2026 and 2027 on record order backlog; plans to return at least 75% of free cash flow in Q4.','Watch: most volatile holding (about 57% a year); AI-server margins are thin and lumpy.'],
'FIX':['Q2 2026: revenue $3.27B vs $2.17B a year ago (+51%); EPS $12.53 vs $6.53; operating cash flow $1.14B.','Mechanical and electrical contractor riding data-centre and factory construction.','Watch: does not issue formal guidance; 27x forward P/E; construction cycles turn fast; about 57% volatility.'],
'ADSK':['Fiscal Q2 2027: revenue +16% to $2.05B.','Raised full-year billings and revenue growth guidance, partly from the MaintainX acquisition; margin guidance held.','Watch: acquisition integration; AI disruption risk to design software is debated.'],
'SWK':['Q2 2026: sales $4.0B flat (organic +3%); gross margin up about 6 points; free cash flow $698M.','Raised 2026 GAAP EPS range to $4.60 to $5.45.','Watch: about 2.5 points of that margin gain came from one-off tariff refunds, so underlying improvement is smaller than the headline.'],
'GPN':['Q2 2026: adjusted EPS $3.46 (+12%), but GAAP EPS only $0.05 because of deal-related charges.','Normalised revenue +4%; $1.2B returned to shareholders year to date; capital-return plan reaffirmed.','Watch: big gap between adjusted and GAAP profit; slow growth; about 5x forward P/E prices in scepticism.'],
'BKNG':['Q2 2026: room nights +5%, gross bookings +9%, adjusted EPS +15%; beat guidance on every line.','Cost programme savings target raised to about $650M; heavy buybacks.','Watch: Middle East conflict hits long-haul travel; EU scrutiny of commissions.'],
'EXPE':['Q2 2026: gross bookings +12%, revenue +14%, with B2B +23%; beat guidance and raised full-year guidance.','B2B (powering other travel sellers) is the growth engine.','Watch: shares travel-cycle risk with BKNG (combined about 10% of the portfolio); about 51% volatility.'],
'VTRS':['Q2 2026: revenue $3.8B (+5%); adjusted EBITDA $1.2B; GAAP net loss of $119M.','Raised 2026 guidance midpoints for all metrics; about $550M returned; gross leverage down to 2.9x.','Watch: generic-drug pricing pressure; GAAP losses from charges.'],
'IVZ':['Q2 2026: record $45.1B of net long-term inflows (ETFs, index, private markets); AUM $2.5T.','Adjusted operating margin 37.5%.','Watch: fees fall with markets, so this is a leveraged bet on markets staying up; no formal guidance.'],
'BIIB':['Q2 2026: revenue $2.7B (+3%); newer drugs +24% to $1.06B.','Guidance updated for stronger underlying business; the Apellis acquisition dilutes 2026 EPS by about $0.85.','Watch: legacy multiple-sclerosis franchise decline; deal integration; biotech binary risk.'],
'BBY':['Q2 FY27: comparable sales +4.1%; adjusted EPS +15% to $1.47.','Raised FY27 comparable-sales guide to 1.9% to 3.0% and adjusted EPS guide to $6.70 to $6.90.','Watch: consumer-electronics demand is cyclical and tariff-exposed.'],
'ADI':['Fiscal Q3 2026: record revenue of $4.02B led by data centre and industrial; trailing free cash flow $4.9B (36% of revenue).','$1.7B returned in the quarter; guided to a record fourth quarter.','Watch: analog chips are cyclical; 23x forward P/E.'],
'AMP':['Q2 2026: adjusted operating EPS $11.07 (+22%); adjusted ROE 55%.','Wealth-management asset growth drives earnings.','Watch: market-linked; the third asset manager in the book (cap watched).'],
'DD':['Q2 2026: beat its own guidance and raised full-year 2026 guidance; organic sales +4%.','Free-cash-flow conversion 127%; announced $250M of buybacks for Q3.','Watch: post-separation execution; industrial demand cycle.'],
'NEM':['Q2 2026: about 1.3M ounces of gold; record Q2 free cash flow of $2.2B; on track for full-year guidance.','A cash machine while gold prices stay high.','Watch: pure gold-price bet (about 50% volatility); the release reader logged 3 guidance cuts in 2 years; you are already heavy in precious metals via India SIPs.'],
'NVDA':['Fiscal Q2 2027: revenue $96.2B, +106% year on year and +18% on the prior quarter; gross margin 75%.','Estimates rose about 24% in 90 days; only about 14x forward earnings.','Watch: beta about 2.2, the highest in the book; customers building their own chips. Audit note: EDGAR pulled the CFO commentary, not the press release, so its guidance score is treated as neutral.'],
'INCY':['Q2 2026: revenue $1.67B (+38%), flattered by a one-time CMS-related benefit; ex that, net sales +17%.','Raised 2026 net-sales guidance to $5.13B to $5.26B; Opzelura +173%.','Watch: Jakafi (about half of sales) faces patent expiry later this decade (verify date); valuation methods disagree widely (low confidence, small weight).'],
'JBHT':['Q2 2026: revenue $3.50B (+19%); operating income +32%; EPS $1.91 vs $1.31.','Freight recovery showing up in margins.','Watch: trucking is highly cyclical; no formal guidance; 23x forward P/E.'],
'TROW':['Q2 2026: record $1.9T AUM, but net client outflows of $6.5B; adjusted EPS $2.57.','Returned $441M via dividends and buybacks.','Watch: the steady shift from active funds to index funds (outflows) is structural; smallest weight for a reason.']}
d=json.load(open('dash2.json')); d['N2']=N
d['AL']=json.load(open('audit_loop1.json'))
d['grade2']=[('Universe & data breadth',10,'497 stocks, 11 yrs prices, statements, full estimate set'),('Primary-source reading',9,'467 SEC releases machine-read; 20 holdings read by hand (latest release)'),
 ('Valuation rigour',9,'3 methods, shrinkage, reverse DCF; new sensitivity test shows E ranges 12.4% to 15.9%'),('Out-of-sample validation',9,'3-yr point-in-time + 10-yr factor test; survivorship bias now measured (+6.3 pts/yr) and neutralised in the alpha estimate'),
 ('Risk modelling',9,'20k-path bootstrap incl. 2020/2022; resampled optimiser'),('Portfolio vs mandate',9,'Frontier with odds for 15/20/25/50%'),('Error discovery',10,'17 errors found and fixed'),
 ('Honesty of probabilities',10,'Shrunk vs raw; assumption ranges shown'),('Company-level qualitative depth',8,'Primary-source notes for all 20 holdings; still no call transcripts, expert calls or segment models'),('Actionability',9,'Exact weights; order sheet needs amount and broker')]
d['fix3']=[('NVDA release reader read the wrong exhibit','EDGAR returned NVIDIA\'s CFO commentary (exhibit 99.2), not the press release, so its guidance score was understated. Treated as neutral; the downloader regex needs "pr.htm" added.'),
 ('Survivorship bias was unmeasured','Compared with the real equal-weight S&P ETF (RSP), today\'s-constituent returns were inflated by 7.1, 7.3 and 4.6 points. The alpha estimate already compares like with like; absolute backtest returns are now labelled as inflated.')]
json.dump(d,open('dash2.json','w')); print('ok',sum(g[1] for g in d['grade2']))
```

### A.23 `conv.py` — v3 conviction engine
```python
# CONVICTION ENGINE: 10 independent lens-agents vote on all 497; 500-run threshold-perturbation audit; target-independent
import pandas as pd, numpy as np, pickle, json, warnings
warnings.filterwarnings('ignore')
X=pd.read_pickle('v3.pkl'); F=pickle.load(open('fund_all.pkl','rb')); ER=json.load(open('edgar_read.json'))
def row(d,ns):
    if d is None: return None
    for n in ns:
        if n in d.index: return d.loc[n].astype(float)
    return None
B=[]
for t in X.t:
    o=F.get(t,{}); I,BS,CF=o.get('inc'),o.get('bs'),o.get('cf')
    rev=row(I,['Total Revenue','Operating Revenue']); ni=row(I,['Net Income Common Stockholders','Net Income']); opi=row(I,['Operating Income','EBIT'])
    eq=row(BS,['Stockholders Equity','Common Stock Equity']); ocf=row(CF,['Operating Cash Flow']); cx=row(CF,['Capital Expenditure']); sh=row(I,['Diluted Average Shares','Basic Average Shares'])
    def s(x): return x.dropna().sort_index(ascending=False).iloc[:4] if x is not None else pd.Series(dtype=float)
    rv,nn,op,e_,oc,c_,shs=map(s,[rev,ni,opi,eq,ocf,cx,sh])
    roe=(nn/e_.reindex(nn.index)).dropna(); fcf=(oc+c_.reindex(oc.index).fillna(0)).dropna()
    n=len(rv); cagr=(rv.iloc[0]/rv.iloc[n-1])**(1/(n-1))-1 if n>=3 and rv.iloc[n-1]>0 else np.nan
    upyrs=int(sum(rv.iloc[k]>rv.iloc[k+1] for k in range(n-1))) if n>=2 else 0
    om=(op/rv.reindex(op.index)).dropna()
    B.append(dict(t=t,roe_yrs=int((roe>0.12).sum()),roe_n=len(roe),fcf_pos=bool(len(fcf)>=3 and (fcf>0).all()),ni_pos=bool(len(nn)>=3 and (nn>0).all()),cagr4=cagr,upyrs=upyrs,nyrs=n,
       om_stable=bool(len(om)>=3 and om.iloc[0]>=om.mean()-0.03),sh_chg=(shs.iloc[0]/shs.iloc[-1]-1) if len(shs)>=2 else np.nan))
X=X.merge(pd.DataFrame(B),on='t')
fin=X.sector.isin(['Financials','Real Estate'])
secpe=X[X.fpe>0].groupby('sector').fpe.median(); X['pe_rel']=X.fpe/X.sector.map(secpe)
X['v3p']=X.v3.rank(pct=True); X['s1p']=X.s1.rank(pct=True)
badj=np.clip(0.67*X.beta3.fillna(1)+0.33,0.6,1.6); X['E_cons']=0.5*X.E_final+0.5*0.10*badj
def cuts_recent(t):
    e=ER.get(t); return None if not e else sum(1 for x in e['timeline'][-4:] if x['c'])
X['cuts4']=X.t.map(cuts_recent); X.loc[X.t=='MSFT','cuts4']=0  # auditor: regex false positive (compared-to-guidance sentence), not a cut
def lenses(f):  # f: dict of threshold multipliers (1 = base)
    L={}
    L['Quality (Buffett)']=(X.roe_yrs>=np.ceil(3*min(f['q'],1.33)).clip(1,4)) & (X.fcf_pos|fin&X.ni_pos) & (X.A_Quality>=0.5*f['q'])
    L['Durable growth']=(X.cagr4>=0.05*f['g']) & (X.revg.fillna(-1)>=-0.02*f['g']) & (X.upyrs>=X.nyrs-2)
    L['Balance sheet']=np.where(fin,(X.roe>0.10*f['b']),(X.nd_ebitda.fillna(0)<=2.5/f['b'])) & ~X.vetoed
    L['Valuation sanity']=(X.fpe>0) & ((X.pe_rel<=1.35/f['v'])|((X.fpe/(X.g.clip(lower=0.01)*100))<=1.5/f['v'])) & (X.E_bb>=0.06*f['v'])
    L['Earnings momentum']=(X.rev90.fillna(0)>=-0.02*f['e']) & (X.beats8.fillna(0.5)>=0.625*f['e'])
    L['Price health']=(X.tt>=np.round(4*f['m'])) & (X.off_hi>=-0.25/f['m'])
    L['Risk']=(X.vol<=0.45/f['r']) & (X.mdd3y>=-0.45/f['r'])
    L['Validated model (v2)']=X.v3p>=0.60*f['p']
    L['Classic model (v1)']=X.s1p>=0.50*f['p']
    L['Management & red flags']=(X.cuts4.fillna(0)==0) & (X['flags'].map(len)<=1)
    return pd.DataFrame(L)
base=lenses({k:1 for k in 'qgbvemrp'})
X['passes']=base.sum(axis=1); hard=base[['Quality (Buffett)','Balance sheet','Risk']].all(axis=1)
X['conv_base']=(X.passes>=9)&hard
rng=np.random.default_rng(11); hits=np.zeros(len(X))
for _ in range(500):
    f={k:rng.uniform(0.8,1.2) for k in 'qgbvemrp'}; L=lenses(f); ok=(L.sum(axis=1)>=9)&L[['Quality (Buffett)','Balance sheet','Risk']].all(axis=1); hits+=ok.values
X['stab']=hits/500
for c in base.columns: X['L_'+c]=base[c].values
X['cscore']=100*(0.35*X.stab+0.25*X.passes/10+0.20*X.E_cons.rank(pct=True)+0.20*X.A_Quality)
X.to_pickle('conv.pkl')
C=X[X.stab>=0.5].sort_values('cscore',ascending=False)
print('base conviction:',int(X.conv_base.sum()),'| stab>=0.9:',int((X.stab>=0.9).sum()),'| stab>=0.7:',int((X.stab>=0.7).sum()))
print('lens pass rates:',{c:int(base[c].sum()) for c in base.columns})
print(C[['t','sector','sub','cscore','stab','passes','E_cons','fpe','vol','cagr4','roe_yrs','cuts4']].head(40).round(3).to_string())
```

### A.24 `conv_port.py` — v3 portfolio + odds
```python
import pandas as pd, numpy as np, json
X=pd.read_pickle('conv.pkl').set_index('t'); C=pd.read_pickle('close10.pkl').ffill()
cand=X[(X.stab>=0.5)&(X.E_cons>=0.08)].sort_values('cscore',ascending=False)
pick=[];sub=set();sec={}
for t,r in cand.iterrows():
    if r['sub'] in sub: continue
    pick.append(t); sub.add(r['sub']); sec[r.sector]=sec.get(r.sector,0)+1
w=(X.loc[pick,'cscore']*(0.5+X.loc[pick,'stab'])); w=w/w.sum()
for _ in range(50):
    w=w.clip(0.04,0.10); w=w/w.sum()
    for s in set(X.loc[pick,'sector']):
        m=X.loc[pick,'sector']==s; tot=w[m].sum()
        if tot>0.25: w[m]*=0.25/tot
    w=w/w.sum()
M=C[pick].resample('ME').last().pct_change().iloc[-121:].fillna(0); Ms=C['^GSPC'].resample('ME').last().pct_change().iloc[-121:].fillna(0)
E=float((w*X.loc[pick,'E_cons']).sum()); pm=(M@w).values; sm=Ms.values
def boot(m,E,months,n=20000,blk=3,seed=5):
    rng=np.random.default_rng(seed); m=m-m.mean()+(1+E)**(1/12)-1; T=len(m); out=np.empty(n)
    for i in range(n):
        idx=np.concatenate([np.arange(s,s+blk)%T for s in rng.integers(0,T,months//blk)]); out[i]=np.prod(1+m[idx])-1
    return out
b1,b5=boot(pm,E,12),boot(pm,E,60); s1,s5=boot(sm,0.10,12,seed=6),boot(sm,0.10,60,seed=6)
vol=float(pm.std()*np.sqrt(12)); hist=np.cumprod(1+pm)
res=dict(pick=pick,w=w.round(4).to_dict(),E=E,vol=vol,p_pos1=float((b1>0).mean()),p_pos5=float((b5>0).mean()),p_double5=float((b5>=1).mean()),ann5_med=float(np.median(1+b5)**(1/5)-1),
  p5_1=float(np.percentile(b1,5)),p5_5=float(np.percentile(b5,5)),p_loss20_1=float((b1<=-.2).mean()),p15_1=float((b1>=.15).mean()),
  spx=dict(p_pos1=float((s1>0).mean()),p_pos5=float((s5>0).mean()),vol=float(sm.std()*np.sqrt(12))),
  y2022=float(np.prod(1+M.loc['2022'].values@w.values)-1),covid=float(np.prod(1+M.loc['2020-02':'2020-03'].values@w.values)-1),mdd10=float((hist/np.maximum.accumulate(hist)-1).min()),
  sectors=X.loc[pick].groupby('sector').size().to_dict())
json.dump(res,open('conv_port.json','w'),default=float)
print(json.dumps({k:(round(v,3) if isinstance(v,float) else v) for k,v in res.items() if k!='w'},default=float))
print({t:round(w[t],3) for t in w.sort_values(ascending=False).index})
print(X.loc[pick,['sector','stab','passes','cscore','E_cons','fpe','vol']].round(3).to_string())
```

### `v2tabs.js` — v2 dashboard tabs (injected)
```javascript
const D2=__DATA2__;
const P2=D2.P2,REC=P2.Recommended,C2=D2.C2;
TABS.unshift(['v2v','v2 · Verdict (Hurdle-15)'],['v2bt','v2 · Backtest'],['v2fr','v2 · Frontier & odds'],['v2c','v2 · Candidates (52)'],['v2rel','v2 · Release reader'],['v2u','v2 · Ranking (497)'],['v2g','v2 · Audit loops & grade']);
TABS.forEach(t=>{if(!t[1].startsWith('v2'))t[1]='v1 · '+t[1]});
cur='v2v';
const card2=(t)=>{const c=C2[t];if(!c)return'';const nt=D2.N2[t];const tl=(c.tl||[]).map(x=>`<span title="${x.d}" class="pill" style="border-color:${x.r?'var(--up)':x.c?'var(--down)':'var(--line)'}">${x.d.slice(2,7)} ${x.r?'▲':x.c?'▼':x.k?'=':'·'}</span>`).join('');
 return `<div class="card ${REC.w[t]?'hi':''}"><div class="hdr" style="border:0;padding:0"><div><h3>${esc(c.n)} (${t})</h3><div class="mute sm">${esc(c.s)} · ${esc(c.sub)}${REC.w[t]?` · <b style="color:var(--gold)">Portfolio ${pct(REC.w[t])}</b>`:''}</div></div><div style="text-align:right"><div class="big" style="font-size:26px">${usd(c.p)}</div><div class="sm mute">Confidence ${n(c.conf,0)} · v2 rank ${c.rk}/52</div></div></div>
 <div class="kv" style="margin-top:8px"><span>Conservative expected return (shrunk)</span><b>${sp(c.Esh)}</b><span>Building blocks: yield + growth + re-rating</span><span>${sp(c.Ebb)} = ${pct(c.by)} + ${pct(c.bg)} + ${pct(c.br)}</span><span>Factor model / scenario model</span><span>${sp(c.Efac)} / ${c.Escen==null?'n/a':sp(c.Escen)}</span><span>Methods disagree by</span><span>${pct(c.Esp,0)}</span>
 <span>Momentum / earnings momentum / value / quality</span><span>${Math.round(c.pm*100)} / ${Math.round(c.pe*100)} / ${Math.round(c.pv*100)} / ${Math.round(c.pq*100)}</span><span>Fwd P/E · volatility · 3-yr beta</span><span>${n(c.fpe)}x · ${pct(c.vol,0)} · ${n(c.beta,2)}</span><span>Guidance record (${c.nrel} releases)</span><span><span class="ok">${c.raises} raises</span> / <span class="bad">${c.cuts} cuts</span> / ${c.keeps} held</span></div>
 <div style="margin-top:8px">${tl}</div>${nt?`<ul class="pts sm">${nt.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`:''}<p class="sm"><a href="${c.url}" target="_blank" rel="noopener">Latest SEC earnings release</a>${C[t]?` · <a href="#" data-deep="${t}">Full v1 deep dive</a>`:''}</p></div>`};
function wireDeep(){document.querySelectorAll('a[data-deep]').forEach(a=>a.onclick=e=>{e.preventDefault();go(C[a.dataset.deep].rk30?'deep':'one',a.dataset.deep)})}
R.v2v=()=>{const w=REC.w,ks=Object.keys(w).sort((a,b)=>w[b]-w[a]);
$('#app').innerHTML=`<h1>v2: a 20-stock portfolio at the edge of your 15% hurdle.</h1><p class="lede">A point-in-time backtest showed my v1 model's low-volatility tilt lagged the market in all three test years. The redesigned model (momentum, earnings upgrades, value and quality) beat the market in all three years with two different weightings. After shrinking every forecast for optimism, the portfolio's conservative expected return is <b>${pct(REC.E)}</b> (raw model ${pct(REC.E_raw)}), with a <b>${pct(REC.p15,0)}</b> chance of 15%+.</p>
<div class="tally"><div><b>${pct(REC.E,1)}</b><span>conservative expected return</span></div><div><b>${pct(REC.p15,0)}</b><span>chance of 15%+</span></div><div><b>${pct(REC.p25,0)}</b><span>chance of 25%+</span></div><div><b>${pct(REC.p50,0)}</b><span>chance of 50%+</span></div><div><b>${pct(REC.vol,0)}</b><span>volatility (S&amp;P about 15%)</span></div><div><b>${pct(REC.y2022,0)}</b><span>replayed through 2022</span></div></div>
<h2>Mandate scorecard</h2><div class="scroll"><table><thead><tr><th>Your requirement</th><th>Result</th><th>Status</th></tr></thead><tbody>
<tr><td>15% a year hurdle</td><td>${pct(REC.E)} conservative (${pct(REC.E_raw)} raw); sensitivity range 12.4% to 15.9% depending on the market assumption</td><td class="warn">At the edge</td></tr>
<tr><td>Realistic chance of 15%+</td><td>${pct(REC.p15,0)} (roughly a coin flip)</td><td class="ok">Met</td></tr>
<tr><td>1-in-4 chance of 50%+ (read "0.5%" as 50%)</td><td>${pct(REC.p50,1)}. Needs about 67% volatility, which carries about a 1-in-3 chance of losing 30%+</td><td class="bad">Not achievable at acceptable risk</td></tr>
<tr><td>If you meant 25%+</td><td>${pct(REC.p25,0)}</td><td class="ok">Met</td></tr><tr><td>Chance of losing money in a year</td><td>${pct(1-REC.p0,0)}; 5th-percentile year ${sp(REC.p5)}</td><td class="mute">Accepted risk</td></tr></tbody></table></div>
<h2>The 20 holdings</h2><p class="mute">Each card shows the three return methods, the guidance record from 9 quarterly SEC releases (▲ raised, ▼ cut, = held), and notes from the latest release.</p><div class="grid">${ks.map(card2).join('')}</div><p class="mute sm">Not financial advice. Backtests use today's index members, which flatters absolute returns (measured at +6.3 points a year versus the real equal-weight S&amp;P ETF).</p>`;wireDeep();};
R.v2bt=()=>{const b=D2.BT,yrs=['2023','2024','2025'],f=D2.BT.f10,S=D2.AL.surv;
$('#app').innerHTML=`<h2 style="margin-top:0">Backtest: what I got wrong, and the fix</h2><p class="mute">Each September, the model was run using only information available then (statements with a 90-day lag, prices to date), and returns were measured over the next 12 months.</p>
<div class="scroll"><table><thead><tr><th>12 months from late Sept…</th>${yrs.map(y=>`<th class="num">${y}</th>`).join('')}</tr></thead><tbody>
<tr><td>S&amp;P 500</td>${yrs.map(y=>`<td class="num">${pct(b.v1[y].spx)}</td>`).join('')}</tr><tr><td>Real equal-weight S&amp;P (RSP ETF)</td>${yrs.map(y=>`<td class="num">${pct(S[y].RSP)}</td>`).join('')}</tr>
<tr><td>Equal-weight of today's members (survivorship-inflated)</td>${yrs.map(y=>`<td class="num">${pct(b.v1[y].ew)}</td>`).join('')}</tr>
<tr><td class="bad">v1 model top 30 (low-vol tilt)</td>${yrs.map(y=>`<td class="num bad">${pct(b.v1[y].top30)}</td>`).join('')}</tr>
<tr><td class="ok">v2 model top 30 (weighting A)</td>${yrs.map(y=>`<td class="num ok">${pct(b.v3[y].top30)}</td>`).join('')}</tr><tr><td class="ok">v2 model top 30 (weighting B)</td>${yrs.map(y=>`<td class="num ok">${pct(b.v3b[y].top30)}</td>`).join('')}</tr>
<tr><td>v1 rank correlation with next-year return (IC)</td>${yrs.map(y=>`<td class="num">${n(b.v1[y].ic,3)}</td>`).join('')}</tr><tr><td>v2 rank correlation (IC)</td>${yrs.map(y=>`<td class="num">${n(b.v3[y].ic,3)}</td>`).join('')}</tr>
<tr><td>Low-volatility pillar IC (why v1 failed)</td>${yrs.map(y=>`<td class="num bad">${n(b.v1[y].pillar_ic.R,3)}</td>`).join('')}</tr><tr><td>Momentum pillar IC</td>${yrs.map(y=>`<td class="num ok">${n(b.v1[y].pillar_ic.M,3)}</td>`).join('')}</tr></tbody></table></div>
<h2>Ten-year style test (monthly, top 50)</h2><div class="scroll"><table><thead><tr><th>Style</th><th class="num">CAGR</th><th class="num">Volatility</th><th class="num">Worst fall</th><th class="num">12m ≥15%</th><th class="num">12m ≥50%</th><th class="num">2022</th></tr></thead><tbody>${Object.entries(f).map(([k,v])=>`<tr><td>${k}</td><td class="num">${pct(v.cagr)}</td><td class="num">${pct(v.vol)}</td><td class="num">${pct(v.mdd)}</td><td class="num">${pct(v.p15,0)}</td><td class="num">${pct(v.p50,0)}</td><td class="num">${pct(v.y2022)}</td></tr>`).join('')}</tbody></table></div>
<p class="sm mute">Absolute numbers are inflated by survivorship bias; compare styles against each other. The edge carried into forecasts was cut by 58%, following McLean &amp; Pontiff (2016).</p>`;};
R.v2fr=()=>{const ks=Object.keys(P2).filter(k=>P2[k].w);
$('#app').innerHTML=`<h2 style="margin-top:0">Frontier: how much risk buys how much return</h2><p class="mute">Odds come from 20,000 simulated years built from 10 years of real monthly returns (including COVID and 2022), re-centred on each portfolio's conservative expected return.</p>
<div class="scroll"><table><thead><tr><th>Portfolio</th><th class="num">Names</th><th class="num">Expected</th><th class="num">Volatility</th><th class="num">Beta</th><th class="num">≥15%</th><th class="num">≥20%</th><th class="num">≥25%</th><th class="num">≥50%</th><th class="num">≤−20%</th><th class="num">2022</th><th class="num">COVID</th></tr></thead><tbody>${ks.map(k=>{const v=P2[k];return`<tr${k==='Recommended'?' style="outline:1px solid var(--gold)"':''}><td><b>${k}</b></td><td class="num">${v.n}</td><td class="num">${pct(v.E)}</td><td class="num">${pct(v.vol)}</td><td class="num">${n(v.beta,2)}</td><td class="num">${pct(v.p15,0)}</td><td class="num">${pct(v.p20,0)}</td><td class="num">${pct(v.p25,0)}</td><td class="num">${pct(v.p50,1)}</td><td class="num">${pct(v.pl20,1)}</td><td class="num">${pct(v.y2022)}</td><td class="num">${pct(v.covid)}</td></tr>`}).join('')}</tbody></table></div>
<h2>Sensitivity: what moves the recommended portfolio's expected return</h2><div class="scroll"><table><tbody>${Object.entries(D2.AL.sens).map(([k,v])=>`<tr><td>${k}</td><td class="num">${pct(v)}</td></tr>`).join('')}</tbody></table></div><p class="sm mute">The biggest single lever is what the overall market does (the 10% prior). Stock-picking edge adds about 1 point.</p>`;};
R.v2c=()=>{const ks=Object.keys(C2).sort((a,b)=>C2[a].rk-C2[b].rk);$('#app').innerHTML=`<h2 style="margin-top:0">All 52 release-read candidates</h2><div class="grid">${ks.map(card2).join('')}</div>`;wireDeep();};
R.v2rel=()=>{const rows=Object.values(C2).map(c=>({t:c.t,n:c.n,nrel:c.nrel,r:c.raises,c:c.cuts,k:c.keeps,gs:c.gs,hw:c.flags.headwind,inv:c.flags.investig,url:c.url}));
$('#app').innerHTML=`<h2 style="margin-top:0">Earnings-release reader: 467 SEC filings</h2><p class="mute">Every 8-K Item 2.02 earnings release since July 2024 was read for guidance raises, cuts and maintains, plus red-flag language. Companies that don't give guidance (many insurers and payment networks) score neutral. Keyword reading can misfire; see the audit notes.</p><div class="scroll"><table id="rt"></table></div>`;
table('rt',[['t','Ticker',v=>`<b>${v}</b>`],['n','Company',v=>esc(v)],['nrel','Releases',v=>v,'num'],['r','Raises',v=>`<span class="ok">${v}</span>`,'num'],['c','Cuts',v=>`<span class="bad">${v}</span>`,'num'],['k','Held',v=>v,'num'],['gs','Net score',v=>n(v,2),'num'],['hw','"Headwind" mentions',v=>v,'num'],['inv','Investigation mentions',v=>v,'num'],['url','Latest',v=>`<a href="${v}" target="_blank" rel="noopener">SEC</a>`]],rows,{sort:'gs',asc:false});};
R.v2u=()=>{$('#app').innerHTML=`<h2 style="margin-top:0">v2 ranking of all 497</h2><div class="scroll" style="max-height:700px"><table id="u3"></table></div>`;
table('u3',[['rk','#',v=>v,'num'],['t','Ticker',v=>`<b>${v}</b>`],['n','Name',v=>esc(v)],['s','Sector'],['v3','Score',v=>n(v,0),'num'],['pm','Momentum',v=>Math.round(v*100),'num'],['pe','Earnings mom.',v=>Math.round(v*100),'num'],['pv','Value',v=>Math.round(v*100),'num'],['pq','Quality',v=>Math.round(v*100),'num'],['E','Expected (3-method)',v=>sp(v),'num'],['vol','Volatility',v=>pct(v,0),'num'],['why','Gate',(v,r)=>r.gate?'<span class="ok">Pass</span>':`<span class="bad">${v}</span>`]],D2.U3,{sort:'rk'});};
R.v2g=()=>{const g=D2.grade2,tot=g.reduce((a,b)=>a+b[1],0);
$('#app').innerHTML=`<h2 style="margin-top:0">Audit loops & self-grade: ${tot}/100</h2><p class="mute">Grade history: 58 (first list), 78 (v1 dashboard), 91 (v2 analysis), ${tot} (after audit loops). The honest ceiling in this environment is about 93. Reaching 95+ needs data I can't get here: earnings-call transcripts, point-in-time analyst-estimate history, and a survivorship-free index history.</p>
<div class="scroll"><table><thead><tr><th>Criterion</th><th class="num">Score</th><th>Evidence / gap</th></tr></thead><tbody>${g.map(([a,s,e])=>`<tr><td>${a}</td><td class="num"><b>${s}</b>/10</td><td class="w">${esc(e)}</td></tr>`).join('')}</tbody></table></div>
<h2>Errors found and fixed in v2 and the audit loops</h2><div class="grid">${D2.fix2.concat(D2.fix3).map(([h,b])=>`<div class="card"><h4>${esc(h)}</h4><p class="sm">${esc(b)}</p></div>`).join('')}</div>
<h2>Audit loop results</h2><div class="grid"><div class="card"><h4>Loop 1 · Holdings integrity</h4><p class="sm">All 20 holdings pass gates; 180 of 180 releases matched to the right company, except NVIDIA (CFO commentary pulled instead of the press release; neutralised).</p></div><div class="card"><h4>Loop 2 · Survivorship bias</h4><p class="sm">Today's-member equal-weight beat the real equal-weight S&amp;P ETF by ${Object.values(D2.AL.surv).map(x=>pct(x.bias)).join(', ')}. The alpha estimate compares like with like, so it is unaffected; absolute backtest returns are labelled as inflated.</p></div><div class="card"><h4>Loop 3 · Assumption sensitivity</h4><p class="sm">Expected return ranges ${pct(Math.min(...Object.values(D2.AL.sens)))} to ${pct(Math.max(...Object.values(D2.AL.sens)))}. The 15% hurdle depends mostly on the market, not on stock picking.</p></div></div>`;};
```

### `cvtab.js` — v3 conviction tab (injected)
```javascript
TABS.unshift(['cv','★ Conviction portfolio (final)']);cur='cv';
R.cv=()=>{const V=D2.CV,P=V.P,b=P.blend,rows=V.rows,inp=rows.filter(r=>r.inp).sort((a,b)=>b.w-a.w);
const note=t=>V.NC[t]||(D2.N2&&D2.N2[t])||(C[t]&&C[t].dil&&C[t].dil.notes.slice(0,3))||[];
const tier=s=>s>=0.9?'<span class="tag tA">Core ≥90%</span>':s>=0.7?'<span class="tag tB">Conviction</span>':'<span class="tag tC">Supporting</span>';
$('#app').innerHTML=`<h1>No stock earns 90% confidence. A portfolio can.</h1><p class="lede">Ten independent lens-agents voted on all ${V.n497} S&amp;P 500 stocks. The vote was re-run 500 times with every threshold moved ±20%. Only <b>${V.core}</b> stocks stay on the conviction list in 90%+ of those runs. I also back-tested the conviction filter itself: its picks rose in only 56–64% of cases over the following year, no better than a random stock. So 90% confidence per stock is not something anyone can honestly claim. What does reach about 90% is making money over 5 years with the portfolio below held alongside an index core.</p>
<div class="tally"><div><b>${V.n497}</b><span>stocks voted on by 10 lenses</span></div><div><b>${V.base}</b><span>pass 9 of 10 lenses</span></div><div><b>${V.s70}</b><span>survive 70%+ of 500 re-runs</span></div><div><b>${V.core}</b><span>survive 90%+ (core)</span></div><div><b>${pct(b['50% index'].p5,0)}</b><span>5-yr odds of profit, 50/50 with index</span></div></div>
<h2>The 14 stocks, ranked and weighted</h2><div class="scroll"><table><thead><tr><th>#</th><th>Stock</th><th>Tier</th><th class="num">Weight</th><th class="num">Robustness</th><th class="num">Lenses passed</th><th class="num">Expected (conservative)</th><th class="num">Fwd P/E</th><th class="num">Volatility</th></tr></thead><tbody>${inp.map((r,i)=>`<tr><td>${i+1}</td><td><b>${r.t}</b><br><span class="mute sm">${esc(r.n)}</span></td><td>${tier(r.stab)}</td><td class="num"><b>${pct(r.w)}</b></td><td class="num">${pct(r.stab,0)}</td><td class="num">${r.passes}/10</td><td class="num">${sp(r.E)}</td><td class="num">${n(r.fpe)}x</td><td class="num">${pct(r.vol,0)}</td></tr>`).join('')}</tbody></table></div>
<h2>Odds: stocks alone vs blended with an S&amp;P index fund (same simulation)</h2><div class="scroll"><table><thead><tr><th>Mix</th><th class="num">Expected / yr</th><th class="num">Volatility</th><th class="num">1-yr odds of profit</th><th class="num">5-yr odds of profit</th><th class="num">Bad year (5th pct)</th></tr></thead><tbody>${Object.entries(b).map(([k,v])=>`<tr><td>${k==='0% index'?'100% conviction stocks':k==='100% index'?'100% S&P index':k+' / rest conviction stocks'}</td><td class="num">${pct(v.E)}</td><td class="num">${pct(v.vol)}</td><td class="num">${pct(v.p1,0)}</td><td class="num"><b>${pct(v.p5,0)}</b></td><td class="num">${pct(v.p5th1)}</td></tr>`).join('')}</tbody></table></div>
<p class="sm mute">Replays of the 14 stocks: 2022 ${pct(P.y2022)}, COVID crash ${pct(P.covid)}, worst fall in 10 yrs ${pct(P.mdd10)}. For a UAE resident, hold the index part via an Irish-domiciled S&amp;P 500 fund, which avoids US estate tax and halves dividend withholding.</p>
<h2>Lens votes (✓ pass) for every candidate that survives at least half the re-runs</h2><div class="scroll"><table><thead><tr><th>Stock</th><th class="num">Robust</th>${V.lens.map(l=>`<th class="sm">${l}</th>`).join('')}</tr></thead><tbody>${rows.map(r=>`<tr><td><b>${r.t}</b>${r.inp?' <span class="tag tA">in</span>':''}</td><td class="num">${pct(r.stab,0)}</td>${V.lens.map(l=>`<td>${r.votes[l]?'<span class="ok">✓</span>':'<span class="bad">✗</span>'}</td>`).join('')}</tr>`).join('')}</tbody></table></div>
<h2>What the latest earnings releases say</h2><div class="grid">${inp.map(r=>`<div class="card"><h4>${r.t}: ${esc(r.n)} (${pct(r.w)})</h4><ul class="pts sm">${note(r.t).map(x=>`<li>${esc(x)}</li>`).join('')}</ul></div>`).join('')}</div>
<h2>Point-in-time test of the conviction filter</h2><div class="scroll"><table><thead><tr><th>Start</th><th class="num">Picks</th><th class="num">Avg return</th><th class="num">% of picks up</th><th class="num">% beating S&amp;P</th><th class="num">% of all stocks up</th></tr></thead><tbody>${Object.entries(V.BT).filter(([y,v])=>v.n>0).map(([y,v])=>`<tr><td>Sep ${y}</td><td class="num">${v.n}</td><td class="num">${pct(v.mean)}</td><td class="num">${pct(v.pos,0)}</td><td class="num">${pct(v.beat_spx,0)}</td><td class="num">${pct(v.univ_pos,0)}</td></tr>`).join('')}</tbody></table></div>
<h2>Self-grade: ${D2.grade3.reduce((a,g)=>a+g[1],0)}/100</h2><div class="scroll"><table><tbody>${D2.grade3.map(([a,s,e])=>`<tr><td>${a}</td><td class="num"><b>${s}</b>/10</td><td class="w">${esc(e)}</td></tr>`).join('')}</tbody></table></div><p class="mute sm">Not financial advice.</p>`;};
```

## Appendix B — Current dashboard template `dash_tpl_v3.html` (BENCHMARK: extend, never regress)
```html
<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>The 497-to-10 Equity Audit</title>
<link href="https://fonts.googleapis.com/css2?family=Spectral:wght@400;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0e1a;--panel:#10172a;--panel2:#141d33;--line:#243049;--ink:#e8e3d5;--mute:#8e97ad;--gold:#c8a35a;--gold2:#e3c98f;--up:#6fbf8e;--down:#d9776b;--amber:#d8b25e;--blue:#7ea6d8;
box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
:root[data-theme="light"]{--bg:#f6f3ec;--panel:#fff;--panel2:#faf7f0;--line:#ddd6c6;--ink:#1c2233;--mute:#5d6477;--gold:#94702c;--gold2:#6d521f;--up:#2e7d4f;--down:#b04a3e;--amber:#94702c;--blue:#2f5f9a}
html{scroll-padding-top:env(safe-area-inset-top,0px)}*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14.5px/1.55 "IBM Plex Sans",system-ui,-apple-system,Segoe UI,sans-serif;font-variant-numeric:tabular-nums}
h1,h2,h3,h4{font-family:Spectral,Georgia,serif;font-weight:600;margin:0;letter-spacing:-.01em}
h1{font-size:clamp(28px,4.2vw,46px);line-height:1.1;max-width:24ch}
h2{font-size:24px;color:var(--gold);margin:38px 0 6px}h3{font-size:18px;margin:0 0 8px}h4{font-size:15px;margin:0 0 6px;color:var(--gold2)}
p{max-width:80ch;margin:.45em 0}.mute{color:var(--mute)}.sm{font-size:12.5px}
nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
nav .in{max-width:1280px;margin:0 auto;display:flex;gap:2px;overflow-x:auto;padding:0 16px}
nav button{background:none;border:0;border-bottom:2px solid transparent;color:var(--mute);font:inherit;font-size:13.5px;padding:13px 12px;white-space:nowrap;cursor:pointer}
nav button[aria-selected="true"]{color:var(--gold);border-bottom-color:var(--gold)}
nav button:focus-visible,button:focus-visible,select:focus-visible,input:focus-visible,th:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.wrap{max-width:1280px;margin:0 auto;padding:30px 18px 80px}
.lede{font-size:17px;color:var(--mute);max-width:76ch;margin-top:14px}
.tally{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));margin:26px 0 0;border-top:1px solid var(--gold);border-bottom:1px solid var(--line)}
.tally div{padding:15px 14px;border-right:1px solid var(--line)}.tally div:last-child{border-right:0}
.tally b{display:block;font-family:Spectral,serif;font-size:34px;line-height:1;color:var(--gold)}.tally span{color:var(--mute);font-size:12.5px}
.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:6px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:13px}
th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;white-space:nowrap}
th{color:var(--mute);font-weight:600;background:var(--panel);position:sticky;top:0}
th.s{cursor:pointer}th.s:hover{color:var(--gold)}tr:last-child td{border-bottom:0}
tbody tr.click{cursor:pointer}tbody tr.click:hover td{background:var(--panel2)}
td.w{white-space:normal;min-width:220px}.num{text-align:right}
.ok{color:var(--up)}.bad{color:var(--down)}.warn{color:var(--amber)}
.tag{display:inline-block;padding:1px 7px;border-radius:3px;font-size:11.5px;border:1px solid var(--line);color:var(--mute)}
.tA{border-color:var(--up);color:var(--up)}.tB{border-color:var(--amber);color:var(--amber)}.tC{border-color:var(--line);color:var(--mute)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:14px;margin-top:14px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:16px}
.card.hi{border-color:var(--gold)}
.kv{display:grid;grid-template-columns:1fr auto;gap:3px 12px;font-size:13px}.kv span:nth-child(odd){color:var(--mute)}
.bars div{display:grid;grid-template-columns:118px 1fr 40px;gap:8px;align-items:center;font-size:12.5px;margin:4px 0}
.bars i{display:block;height:7px;border-radius:4px;background:var(--gold)}.bars em{display:block;background:var(--line);border-radius:4px}
ul.pts{margin:6px 0 0;padding-left:18px}ul.pts li{margin:3px 0}
.controls{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 12px}
.controls button,.controls input,.controls select{background:var(--panel);color:var(--ink);border:1px solid var(--line);border-radius:4px;padding:7px 11px;font:inherit;font-size:13px}
.controls button[aria-pressed="true"]{border-color:var(--gold);color:var(--gold)}
.hdr{display:flex;flex-wrap:wrap;gap:18px;align-items:flex-end;justify-content:space-between;border-bottom:1px solid var(--gold);padding-bottom:14px}
.hdr .big{font-family:Spectral,serif;font-size:40px;line-height:1}
.pill{display:inline-block;margin:2px 6px 2px 0;padding:2px 8px;border-radius:12px;background:var(--panel2);border:1px solid var(--line);font-size:12px}
.callout{border-left:3px solid var(--gold);padding:10px 16px;background:var(--panel);margin:16px 0;border-radius:0 6px 6px 0}
.flow{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0;margin-top:14px}
.flow>div{border:1px solid var(--line);border-left:0;padding:14px;background:var(--panel)}.flow>div:first-child{border-left:1px solid var(--line)}
.flow b{font-family:Spectral,serif;font-size:30px;color:var(--gold);display:block}
svg text{fill:var(--mute);font-size:11px;font-family:"IBM Plex Sans",sans-serif}
a{color:var(--gold2)}
[hidden]{display:none!important}
</style></head><body>
<nav><div class="in" role="tablist" id="tabs"></div></nav>
<div class="wrap" id="app"></div>
<script>
const D=__DATA__;
const C=D.C,P=D.P,A=D.A;
const $=s=>document.querySelector(s);
const pct=(x,d=1)=>x==null?'–':(x*100).toFixed(d)+'%';
const sp=(x,d=0)=>x==null?'–':(x>0?'+':'')+(x*100).toFixed(d)+'%';
const n=(x,d=1)=>x==null?'–':Number(x).toFixed(d);
const usd=x=>x==null?'–':'$'+Number(x).toLocaleString(undefined,{maximumFractionDigits:x<100?2:0});
const bn=x=>x==null?'–':(Math.abs(x)>=1e9?'$'+(x/1e9).toFixed(1)+'B':'$'+(x/1e6).toFixed(0)+'M');
const cls=x=>x==null?'':(x>=0?'ok':'bad');
const tierTag=t=>!t?'':`<span class="tag ${t[0]==='A'?'tA':t[0]==='B'?'tB':'tC'}">${t}</span>`;
const esc=s=>(s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const TABS=[['verdict','Verdict'],['top30','Top 30 ranking'],['deep','Deep dives (30)'],['one','One-pagers (100)'],['uni','Universe (497)'],['agents','Agent room'],['audit','Audit'],['method','Method & glossary']];
let cur='verdict', deepT=D.top30[0], oneT=Object.keys(C)[0];
function tabs(){$('#tabs').innerHTML=TABS.map(([k,l])=>`<button role="tab" aria-selected="${k===cur}" data-k="${k}">${l}</button>`).join('');
 document.querySelectorAll('#tabs button').forEach(b=>b.onclick=()=>go(b.dataset.k));}
function go(k,t){cur=k;if(t){if(k==='deep')deepT=t;else oneT=t}tabs();R[k]();window.scrollTo(0,0)}
function table(id,cols,rows,opt={}){let sk=opt.sort||cols[0][0],asc=opt.asc??true;const el=document.getElementById(id);
 function draw(){const rs=[...rows].sort((a,b)=>{let x=a[sk],y=b[sk];if(x==null)return 1;if(y==null)return -1;return(x>y?1:x<y?-1:0)*(asc?1:-1)});
  el.innerHTML='<thead><tr>'+cols.map(([k,l,f,al])=>`<th class="s ${al||''}" tabindex="0" data-k="${k}">${l}${sk===k?(asc?' ▲':' ▼'):''}</th>`).join('')+'</tr></thead><tbody>'+
  rs.map(r=>`<tr class="${opt.click?'click':''}" data-t="${r.t}">`+cols.map(([k,l,f,al])=>`<td class="${al||''}">${f?f(r[k],r):(r[k]??'–')}</td>`).join('')+'</tr>').join('')+'</tbody>';
  el.querySelectorAll('th').forEach(th=>{const f=()=>{const k=th.dataset.k;if(sk===k)asc=!asc;else{sk=k;asc=true}draw()};th.onclick=f;th.onkeydown=e=>{if(e.key==='Enter')f()}});
  if(opt.click)el.querySelectorAll('tbody tr').forEach(tr=>tr.onclick=()=>opt.click(tr.dataset.t));}
 draw();}
const R={};
R.verdict=()=>{const w=P.w,pk=P.pick;const spx=P.spx;
$('#app').innerHTML=`<h1>497 stocks in, 10 out. Expect about ${pct(P.exp_cal,0)} a year, with a 1-in-4 shot at 20%+.</h1>
<p class="lede">Fifteen specialist agents screened the whole S&P 500 and argued over it. They cut it to 100, pulled two years of quarterly reports and four years of statements for each, then cut to 30 and ranked them. Three auditors then checked the work, and caught eight mistakes in my own models. The final portfolio is cheaper and calmer than the market. It still cannot promise 20% a year, and nothing honest can.</p>
<div class="tally"><div><b>${D.funnel.u}</b><span>stocks screened</span></div><div><b>${D.funnel.veto1}</b><span>vetoed at stage 1</span></div><div><b>100</b><span>full diligence, 1 page each</span></div><div><b>30</b><span>deep dives, ranked</span></div><div><b>10</b><span>in the portfolio</span></div><div><b>${D.self_fix.length}</b><span>model errors caught by audit</span></div></div>
<h2>The portfolio</h2><p class="mute">Eight core holdings passed every gate (confidence 50+, 70%+ stability across 500 re-weightings). BKNG and ADSK are satellites: high upside but lower confidence, so they carry smaller weights than their returns alone would give. Click a row to open the full deep dive.</p>
<div class="scroll"><table id="pt"></table></div>
<div class="grid"><div class="card hi"><h3>Portfolio vs S&amp;P 500</h3><div class="kv">
<span>Calibrated expected 12-month return</span><b>${pct(P.exp_cal)}</b><span>Model expected (before 40% haircut)</span><span>${pct(P.exp)}</span>
<span>Chance of a 20%+ year (calibrated)</span><b>${pct(P.p20_cal,0)}</b><span>Portfolio bull case / bear case</span><span>${sp(P.bull)} / ${sp(P.bear)}</span>
<span>Volatility (portfolio vs S&amp;P)</span><span>${pct(P.vol)} vs ${pct(spx.vol)}</span><span>Worst fall, last 3 yrs (vs S&amp;P)</span><span>${pct(P.mdd3y)} vs ${pct(spx.mdd3y)}</span>
<span>Weighted forward P/E (S&amp;P about 19x)</span><span>${n(P.fpe)}x</span><span>Weighted confidence</span><span>${n(P.conf,0)}/100</span></div></div>
<div class="card"><h3>What changed from my earlier answers</h3><p>The megacaps I leaned on did not survive a full-universe screen at today's prices. <b>MSFT</b> ranked #${C.MSFT?.rk100??'–'} of 100 and <b>GOOGL</b> #${C.GOOGL?.rk100??'–'}, because their valuation models show little upside after the rally and heavy AI capex. <b>AAPL</b> was vetoed as overpriced by our own models. <b>META</b> (#248 of 497) and <b>AMZN</b> (#140) never made the 100. <b>NVDA</b> survives every round, but at a 5% weight because of its volatility. <b>LLY</b>, <b>V</b> and <b>AVGO</b> are in the top 30 but not the final 10.</p></div>
<div class="card"><h3>How to read the confidence number</h3><p>100 means every agent agrees, data is complete, analysts agree with each other, the company reliably beats estimates, all valuation methods land close together, and the balance sheet is strong. Below 50 means proceed with a smaller position.</p><p class="mute sm">Not financial advice. A passed screen is a hypothesis, not a promise.</p></div></div>`;
const rows=pk.map(t=>{const c=C[t];return{t,n:c.n,w:w[t],tier:c.tier,conf:c.conf,bear:c.down,base:c.base_ret,bull:c.up,exp:c.exp_ret,why:(c.bull_pts[0]||''),risk:(c.dil?c.dil.notes.find(x=>x.startsWith('Watch')||x.startsWith('BEAR'))||c.bear_pts[0]:c.bear_pts[0])||''}});
table('pt',[['t','Stock',(v,r)=>`<b>${v}</b><br><span class="mute sm">${esc(r.n)}</span>`],['w','Weight',v=>pct(v),'num'],['tier','Tier',v=>tierTag(v)],['conf','Confidence',v=>n(v,0),'num'],['bear','Bear',v=>`<span class="bad">${sp(v)}</span>`,'num'],['base','Base',v=>`<span class="${cls(v)}">${sp(v)}</span>`,'num'],['bull','Bull',v=>`<span class="ok">${sp(v)}</span>`,'num'],['exp','Expected',v=>`<b>${sp(v)}</b>`,'num'],['why','Strongest reason',v=>esc(v),'w'],['risk','Key risk',v=>esc(v),'w']],rows,{sort:'w',asc:false,click:t=>go('deep',t)});};
R.top30=()=>{const rows=D.top30.map(t=>{const c=C[t];return{t,n:c.n,s:c.s,rk:c.rk30,tier:c.tier,final:c.final,conf:c.conf,stab:c.stab,bear:c.down,base:c.base_ret,bull:c.up,exp:c.exp_ret,rr:c.rr,b:c.bscore,f:c.fscore,beats:c.beats,inp:P.pick.includes(t)}});
$('#app').innerHTML=`<h2 style="margin-top:0">Top 30, ranked</h2><p class="mute">Final score = 35% reward-to-risk (expected return ÷ bear-case loss), 25% confidence, 20% quality and capital allocation, 20% earnings momentum. Top right of the chart is best: big upside, small downside. Bubble size = confidence.</p>
<div class="card" style="margin:12px 0"><svg id="sc" viewBox="0 0 900 380" width="100%" role="img" aria-label="Upside versus downside for the top 30"></svg></div>
<div class="scroll"><table id="t30"></table></div>`;
scatter(rows);
table('t30',[['rk','#',v=>v,'num'],['t','Stock',(v,r)=>`<b>${v}</b>${r.inp?' <span class="tag tA">Portfolio</span>':''}<br><span class="mute sm">${esc(r.n)}</span>`],['s','Sector'],['tier','Tier',v=>tierTag(v)],['final','Score',v=>n(v,0),'num'],['conf','Confidence',v=>n(v,0),'num'],['stab','Stability',v=>pct(v,0),'num'],['bear','Bear',v=>`<span class="bad">${sp(v)}</span>`,'num'],['base','Base',v=>`<span class="${cls(v)}">${sp(v)}</span>`,'num'],['bull','Bull',v=>`<span class="ok">${sp(v)}</span>`,'num'],['exp','Expected',v=>`<b>${sp(v)}</b>`,'num'],['rr','Reward/risk',v=>n(v,2),'num'],['b','Buffett /8',v=>v,'num'],['f','Piotroski /9',v=>v??'n/a','num'],['beats','Beats /8',v=>v,'num']],rows,{sort:'rk',click:t=>go('deep',t)});};
function scatter(rows){const W=900,H=380,L=60,B=40,T=16,Rr=20;const xs=rows.map(r=>r.bear),ys=rows.map(r=>r.bull);
 const x0=Math.min(...xs)-0.03,x1=0,y0=0,y1=Math.max(...ys)+0.05;const X=v=>L+(v-x0)/(x1-x0)*(W-L-Rr),Y=v=>H-B-(v-y0)/(y1-y0)*(H-B-T);
 let s='';for(let v=Math.ceil(x0*10)/10;v<=0.001;v+=0.1){s+=`<line x1="${X(v)}" x2="${X(v)}" y1="${T}" y2="${H-B}" stroke="var(--line)"/><text x="${X(v)}" y="${H-B+16}" text-anchor="middle">${Math.round(v*100)}%</text>`}
 for(let v=0;v<=y1;v+=0.1){s+=`<line x1="${L}" x2="${W-Rr}" y1="${Y(v)}" y2="${Y(v)}" stroke="var(--line)"/><text x="${L-8}" y="${Y(v)+4}" text-anchor="end">+${Math.round(v*100)}%</text>`}
 s+=`<text x="${(W+L)/2}" y="${H-6}" text-anchor="middle">Bear case (how far it could fall)</text><text transform="translate(14,${H/2}) rotate(-90)" text-anchor="middle">Bull case upside</text>`;
 rows.forEach(r=>{const col=r.tier[0]==='A'?'var(--up)':r.tier[0]==='B'?'var(--amber)':'var(--mute)';s+=`<g style="cursor:pointer" data-t="${r.t}"><circle cx="${X(r.bear)}" cy="${Y(r.bull)}" r="${4+r.conf/12}" fill="${col}" fill-opacity=".35" stroke="${col}"/><text x="${X(r.bear)+8}" y="${Y(r.bull)-6}" style="fill:var(--ink)">${r.t}</text></g>`});
 const el=$('#sc');el.innerHTML=s;el.querySelectorAll('g[data-t]').forEach(g=>g.onclick=()=>go('deep',g.dataset.t));}
function scen(c){const W=640,H=64,vals=[c.bear,c.p,c.base,c.bull],lo=Math.min(...vals)*0.95,hi=Math.max(...vals)*1.03,X=v=>20+(v-lo)/(hi-lo)*(W-40);
 const m=(v,l,col,y)=>`<line x1="${X(v)}" x2="${X(v)}" y1="18" y2="40" stroke="${col}" stroke-width="2"/><text x="${X(v)}" y="${y}" text-anchor="middle" style="fill:${col}">${l} ${usd(v)}</text>`;
 return `<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Bear, base and bull price targets"><rect x="${X(c.bear)}" y="26" width="${X(c.bull)-X(c.bear)}" height="8" rx="4" fill="var(--line)"/>${m(c.bear,'Bear','var(--down)',56)}${m(c.p,'Now','var(--ink)',12)}${m(c.base,'Base','var(--gold)',56)}${m(c.bull,'Bull','var(--up)',12)}</svg>`}
function eqChart(h){if(!h||!h.length)return'<p class="mute">No earnings history available.</p>';const W=560,H=150,B=34,mx=Math.max(...h.map(e=>Math.max(e.act||0,e.est||0)))*1.15,mn=Math.min(0,...h.map(e=>Math.min(e.act||0,e.est||0)));const bw=(W-40)/h.length;const Y=v=>H-B-(v-mn)/(mx-mn)*(H-B-10);
 let s='';h.forEach((e,i)=>{const x=30+i*bw;if(e.est!=null)s+=`<rect x="${x+4}" y="${Y(Math.max(e.est,0))}" width="${bw/2-6}" height="${Math.abs(Y(0)-Y(e.est))}" fill="var(--line)"/>`;
 s+=`<rect x="${x+bw/2}" y="${Y(Math.max(e.act,0))}" width="${bw/2-6}" height="${Math.abs(Y(0)-Y(e.act))}" fill="${(e.s??0)>=0?'var(--up)':'var(--down)'}" fill-opacity=".8"/><text x="${x+bw/2}" y="${H-B+13}" text-anchor="middle">${e.d.slice(2,7)}</text><text x="${x+bw/2}" y="${H-B+26}" text-anchor="middle" style="fill:${(e.s??0)>=0?'var(--up)':'var(--down)'}">${e.s==null?'':sp(e.s/100)}</text>`});
 return `<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Estimated versus actual EPS for the last 8 quarters">${s}</svg><p class="mute sm">Grey = analyst estimate, colour = actual EPS; the % is the surprise.</p>`}
function qChart(q){if(!q||!q.length)return'';const W=560,H=120,mx=Math.max(...q.map(x=>x.rev||0))*1.1,bw=(W-40)/q.length;let s='';
 q.forEach((x,i)=>{if(!x.rev)return;const h=(x.rev/mx)*(H-40);s+=`<rect x="${30+i*bw+6}" y="${H-28-h}" width="${bw-12}" height="${h}" fill="var(--gold)" fill-opacity=".55"/><text x="${30+i*bw+bw/2}" y="${H-28-h-4}" text-anchor="middle" style="fill:var(--ink)">${bn(x.rev)}</text><text x="${30+i*bw+bw/2}" y="${H-12}" text-anchor="middle">${x.q.slice(0,7)}${x.om!=null?' · '+pct(x.om,0):''}</text>`});
 return `<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Quarterly revenue">${s}</svg><p class="mute sm">Quarterly revenue, with operating margin next to each date.</p>`}
function bars(o){return '<div class="bars">'+Object.entries(o).map(([k,v])=>`<div><span>${k}</span><em><i style="width:${Math.max(2,(v||0)*100)}%"></i></em><span class="num">${v==null?'–':Math.round(v*100)}</span></div>`).join('')+'</div>'}
function company(t,full){const c=C[t];if(!c)return'';const k=c.k;
 const meth=Object.entries(c.methods||{}).map(([m,v])=>`<tr><td>${m}</td><td class="num">${usd(v)}</td><td class="num ${cls(v/c.p-1)}">${sp(v/c.p-1)}</td></tr>`).join('');
 const bf=Object.entries(c.buffett).map(([q,ok])=>`<div>${ok?'<span class="ok">✓</span>':'<span class="bad">✗</span>'} ${q}</div>`).join('');
 const yrs=c.yrs||[];const ann=[['Revenue',c.rev_a,bn],['Net income',c.ni_a,bn],['Free cash flow',c.fcf_a,bn],['Operating margin',c.om_a,v=>pct(v)],['Return on equity',c.roe_a,v=>pct(v)],['Diluted EPS',c.eps_a,v=>v==null?'–':'$'+n(v,2)]];
 const annT=`<table><thead><tr><th></th>${yrs.map(y=>`<th class="num">${y}</th>`).join('')}</tr></thead><tbody>${ann.map(([l,a,f])=>`<tr><td>${l}</td>${yrs.map((y,i)=>`<td class="num">${f(a?a[i]:null)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
 const deb=(c.debate||[]).map(d=>`<li><b>${esc(d[0])}:</b> ${esc(d[1])}</li>`).join('')||'<li class="mute">No disputes. All agents broadly agreed.</li>';
 const news=(c.news||[]).map(x=>`<li>${x.url?`<a href="${x.url}" target="_blank" rel="noopener">${esc(x.title)}</a>`:esc(x.title)} <span class="mute sm">${x.src||''} ${x.date||''}</span></li>`).join('');
 const dil=c.dil?`<div class="card hi"><h4>Diligence notes from the latest earnings reports (web-verified)</h4><ul class="pts">${c.dil.notes.map(x=>`<li>${esc(x)}</li>`).join('')}</ul><p class="sm"><a href="${c.dil.src}" target="_blank" rel="noopener">Primary source</a></p></div>`:(full?`<div class="card"><h4>Diligence notes</h4><p class="mute">Earnings-release text not web-verified in this session. Analysis rests on the reported numbers, estimates and news below.</p></div>`:'');
 const veto=c.veto3&&c.veto3.length?`<div class="callout"><b class="bad">Vetoed by the devil's advocate:</b> ${c.veto3.map(esc).join('; ')}</div>`:'';
 return `<div class="hdr"><div><div class="mute sm">${esc(c.s)} · ${esc(c.sub)}</div><h2 style="margin:4px 0">${esc(c.n)} (${t})</h2>
 <span class="pill">Rank ${c.rk500} of 497</span><span class="pill">Rank ${c.rk100} of 100</span>${c.rk30?`<span class="pill">Rank ${c.rk30} of 30</span>`:''} ${tierTag(c.tier)} ${P.pick.includes(t)?`<span class="tag tA">In portfolio: ${pct(P.w[t])}</span>`:''}</div>
 <div style="text-align:right"><div class="big">${usd(c.p)}</div><div class="mute sm">Market cap ${n(c.mc,0)}B · Confidence <b style="color:var(--gold)">${n(c.conf,0)}</b>/100${c.stab!=null?` · Stability ${pct(c.stab,0)}`:''}</div></div></div>
 ${veto}
 <div class="grid"><div class="card hi" style="grid-column:1/-1"><h4>12-month scenarios</h4>${scen(c)}<div class="kv" style="margin-top:6px"><span>Bear (25% weight) / Base (50%) / Bull (25%)</span><span><span class="bad">${sp(c.down)}</span> / <span class="${cls(c.base_ret)}">${sp(c.base_ret)}</span> / <span class="ok">${sp(c.up)}</span></span><span>Probability-weighted expected return</span><b>${sp(c.exp_ret)}</b><span>Calibrated (after 40% haircut for analyst optimism)</span><span>${sp(c.exp_ret*0.6)}</span></div></div>
 <div class="card"><h4>Valuation methods</h4><table><tbody>${meth}</tbody></table><div class="kv" style="margin-top:8px"><span>Median fair value</span><b>${usd(c.fair)}</b><span>Methods disagree by</span><span>${pct(c.disp,0)} of price</span><span>Discount rate (WACC)</span><span>${pct(c.wacc)}</span><span>Growth assumed (years 1 to 5)</span><span>${pct(c.g1)}</span><span>Growth the price implies (reverse DCF)</span><span>${pct(c.impl_g)}</span></div>${c.capex_adj?'<p class="sm warn">FCF normalised for growth capex (see Agent room).</p>':''}${c.oneoff?'<p class="sm warn">One-off profit distortion detected; excluded from growth input.</p>':''}</div>
 <div class="card"><h4>Buffett checklist: ${c.bscore}/8</h4><div style="font-size:13px">${bf}</div></div>
 <div class="card"><h4>Forensic accounting</h4><div class="kv"><span>Piotroski F-score (9 = strongest)</span><b>${c.fscore??'n/a (bank/insurer)'}</b><span>Altman Z (below 1.8 = distress)</span><span>${c.Z==null?'n/a':n(c.Z)}</span><span>Accruals (lower = cleaner earnings)</span><span>${pct(c.accr)}</span><span>Interest cover</span><span>${c.cover==null?'–':n(c.cover,1)+'x'}</span><span>Net debt / EBITDA</span><span>${n(k.nde)}x</span></div></div>
 <div class="card"><h4>Capital allocation</h4><div class="kv"><span>Return on invested capital</span><b>${pct(c.roic)}</b><span>Share count change (about 3 yrs)</span><span class="${c.sh_chg<0?'ok':'warn'}">${sp(c.sh_chg,1)}</span><span>Buybacks last year</span><span>${bn(c.buyback)}</span><span>Dividends last year</span><span>${bn(c.div)}</span><span>Revenue CAGR (4 yrs)</span><span>${pct(c.cagr)}</span></div></div>
 <div class="card" style="grid-column:1/-1"><h4>Two years of earnings reports: ${c.beats}/${c.nq} beats, average surprise ${sp((c.avg_surp||0)/100,1)}</h4>${eqChart(c.eq_hist)}</div>
 <div class="card"><h4>Latest quarters</h4>${qChart(c.qs)}<div class="kv"><span>Latest quarter revenue vs a year ago</span><b class="${cls(c.q_yoy)}">${sp(c.q_yoy)}</b></div></div>
 <div class="card"><h4>Four-year financials</h4><div style="overflow-x:auto">${annT}</div></div>
 <div class="card"><h4>Wall Street view</h4><div class="kv"><span>Analysts / average rating (1 = strong buy)</span><span>${k.nan??'–'} / ${n(k.rec)}</span><span>Target low / mean / high</span><span>${usd(k.tlo)} / ${usd(k.tgt)} / ${usd(k.thi)}</span><span>Next-year EPS estimate, 90-day change</span><span class="${cls(c.rev90)}">${sp(c.rev90,1)}</span><span>Estimate revisions up / down (30 days)</span><span>${c.up30} / ${c.dn30}</span><span>Upgrades / downgrades (90 days)</span><span>${c.ups} / ${c.downs}</span><span>Next earnings date</span><span>${c.next_date||'–'}</span></div></div>
 <div class="card"><h4>Key numbers</h4><div class="kv"><span>Forward P/E (sector median)</span><span>${n(k.fpe)}x (${n(D.sec_fpe[c.s])}x)</span><span>EV/EBITDA</span><span>${n(k.eve)}x</span><span>FCF yield / dividend yield</span><span>${pct(k.fcfy)} / ${k.divy==null?'–':n(k.divy,2)+'%'}</span><span>Revenue growth / EPS growth</span><span>${sp(k.revg)} / ${sp(k.epsg)}</span><span>Volatility / beta</span><span>${pct(k.vol,0)} / ${n(k.beta,2)}</span><span>3-yr max drawdown</span><span class="bad">${pct(k.dd,0)}</span><span>12-month / 6-month return</span><span>${sp(k.r12)} / ${sp(k.r6)}</span><span>Trend template (of 7)</span><span>${k.tt}</span></div></div>
 <div class="card"><h4>Agent scores: screening (0 to 100)</h4>${bars(c.ag)}<h4 style="margin-top:12px">Agent scores: investment committee</h4>${bars(c.cm)}</div>
 <div class="card"><h4 class="ok">Bull advocate</h4><ul class="pts">${c.bull_pts.map(x=>`<li>${esc(x)}</li>`).join('')||'<li class="mute">No strong data-backed bull points.</li>'}</ul><h4 class="bad" style="margin-top:12px">Bear advocate</h4><ul class="pts">${c.bear_pts.map(x=>`<li>${esc(x)}</li>`).join('')||'<li class="mute">No material data-backed bear points.</li>'}</ul></div>
 <div class="card"><h4>Debate log (who refuted whom)</h4><ul class="pts">${deb}</ul></div>
 ${dil}
 <div class="card"><h4>What the company does</h4><p class="sm">${esc(c.sum)}${c.sum&&c.sum.length>=899?'…':''}</p></div>
 ${news?`<div class="card"><h4>Latest news</h4><ul class="pts sm">${news}</ul></div>`:''}</div>`}
R.deep=()=>{$('#app').innerHTML=`<div class="controls"><label class="sm mute" for="ds" style="align-self:center">Company</label><select id="ds">${D.top30.map(t=>`<option value="${t}" ${t===deepT?'selected':''}>#${C[t].rk30} ${t}: ${esc(C[t].n)}</option>`).join('')}</select><button id="pv">Previous</button><button id="nx">Next</button></div><div id="dv">${company(deepT,true)}</div>`;
 const i=D.top30.indexOf(deepT);$('#ds').onchange=e=>go('deep',e.target.value);$('#pv').onclick=()=>go('deep',D.top30[(i+29)%30]);$('#nx').onclick=()=>go('deep',D.top30[(i+1)%30]);}
R.one=()=>{const ks=Object.keys(C).sort((a,b)=>C[a].rk100-C[b].rk100);
 $('#app').innerHTML=`<h2 style="margin-top:0">100 one-pagers</h2><p class="mute">Every company that survived the first screen gets the same page. The top 30 also get the Deep-dive tab, with web-verified earnings notes for the portfolio names.</p><div class="controls"><select id="os">${ks.map(t=>`<option value="${t}" ${t===oneT?'selected':''}>#${C[t].rk100} ${t}: ${esc(C[t].n)}${C[t].top30?' (Top 30)':''}${C[t].veto3.length?' (vetoed)':''}</option>`).join('')}</select><button id="pv">Previous</button><button id="nx">Next</button></div><div>${company(oneT,false)}</div>`;
 const i=ks.indexOf(oneT);$('#os').onchange=e=>go('one',e.target.value);$('#pv').onclick=()=>go('one',ks[(i+99)%100]);$('#nx').onclick=()=>go('one',ks[(i+1)%100]);}
R.uni=()=>{let f='all',q='';$('#app').innerHTML=`<h2 style="margin-top:0">The full universe: ${D.U.length} S&amp;P 500 stocks</h2><p class="mute">Agent scores are percentiles (0 to 100). Valuation and quality are ranked within each sector, so banks are compared with banks, not with software firms.</p>
 <div class="controls"><button data-f="all" aria-pressed="true">All</button><button data-f="sl" aria-pressed="false">Shortlisted 100</button><button data-f="vt" aria-pressed="false">Vetoed</button><input id="uq" type="search" placeholder="Search ticker, name, sector" aria-label="Search"></div><div class="scroll" style="max-height:680px"><table id="ut"></table></div>`;
 const cols=[['rk','#',v=>v,'num'],['t','Ticker',(v,r)=>`<b>${v}</b>${r.sl?' <span class="tag tA">100</span>':''}`],['n','Name',v=>esc(v)],['s','Sector'],['sc','Score',v=>n(v,0),'num'],['q','Quality',v=>Math.round(v*100),'num'],['g','Growth',v=>Math.round(v*100),'num'],['v','Value',v=>Math.round(v*100),'num'],['m','Momentum',v=>Math.round(v*100),'num'],['rk_','Risk',v=>Math.round(v*100),'num'],['st','Street',v=>Math.round(v*100),'num'],['fpe','Fwd P/E',v=>n(v),'num'],['rg','Rev growth',v=>sp(v),'num'],['vol','Volatility',v=>pct(v,0),'num'],['dd','3y worst fall',v=>pct(v,0),'num'],['up','Analyst upside',v=>sp(v),'num'],['vt','Veto / flags',(v,r)=>v.length?`<span class="bad">${v.join(', ')}</span>`:(r.fl.length?`<span class="warn sm">${r.fl.join(', ')}</span>`:'')]];
 const draw=()=>table('ut',cols,D.U.filter(r=>(f==='all'||(f==='sl'?r.sl:r.vt.length))&&(!q||(r.t+' '+r.n+' '+r.s).toLowerCase().includes(q))),{sort:'rk',click:t=>{if(C[t])go('one',t)}});
 document.querySelectorAll('.controls button').forEach(b=>b.onclick=()=>{f=b.dataset.f;document.querySelectorAll('.controls button').forEach(x=>x.setAttribute('aria-pressed',x===b));draw()});$('#uq').oninput=e=>{q=e.target.value.toLowerCase();draw()};draw();}
R.agents=()=>{const F=D.funnel;
 $('#app').innerHTML=`<h2 style="margin-top:0">The agent room</h2><p class="mute">Fifteen specialist agents and three auditors. Each has one mandate, hands its output to the next stage as a file, and can penalise or overrule the others. Honest note: these are specialist analysis modules I designed and ran, not fifteen separate AI models. What makes them agents is the separation: each sees the problem through one lens only, and disagreements are resolved by explicit, logged rules rather than by my judgment in the moment.</p>
 <div class="flow"><div><b>${F.u}</b>S&amp;P 500 stocks enter. 7 screening agents score each one.</div><div><b>−${F.veto1}</b>Red team vetoes: no profit, burning cash, or fell more than 60%.</div><div><b>100</b>Shortlist (max 22 per sector). Hand-off to the diligence team.</div><div><b>−${F.veto3}</b>Devil's advocate vetoes after diligence.</div><div><b>30</b>Ranked by the committee (max 6 per sector).</div><div><b>10</b>Portfolio, built by the CIO agent.</div></div>
 ${D.agents.map(([st,ag])=>`<h2>${st}</h2><div class="grid">${ag.map(([a,m])=>`<div class="card"><h4>${a}</h4><p class="sm">${m}</p></div>`).join('')}</div>`).join('')}
 <h2>Stage-1 debate outcomes (${Object.values(D.dstats).reduce((a,b)=>a+b,0)} logged)</h2><div class="scroll"><table><thead><tr><th>Debate type</th><th class="num">Times</th></tr></thead><tbody>${Object.entries(D.dstats).sort((a,b)=>b[1]-a[1]).map(([k,v])=>`<tr><td>${k}</td><td class="num">${v}</td></tr>`).join('')}</tbody></table></div>
 <h2>Errors the agents caught in my own models</h2><p class="mute">Each was found by an auditor or a rival agent, then fixed and re-run before anything reached you.</p><div class="grid">${D.self_fix.map(([h,b])=>`<div class="card"><h4>${h}</h4><p class="sm">${b}</p></div>`).join('')}</div>
 <h2>Vetoes overturned on appeal</h2><div class="scroll"><table><tbody>${A.X2.overrides.map(([t,m])=>`<tr><td><b>${t}</b></td><td class="w">${m}</td></tr>`).join('')}</tbody></table></div>`;}
R.audit=()=>{const x1=A.X1,x2=A.X2,x3=A.X3;
 $('#app').innerHTML=`<h2 style="margin-top:0">Audit report</h2><p class="mute">Three independent auditors checked the data, the method and the outputs.</p>
 <div class="grid"><div class="card hi"><h3>X1 · Data integrity</h3><div class="kv"><span>Universe checked</span><b>${x1.universe}</b><span>Price date</span><span>${x1.asof}</span><span>Stale prices (over 5 days old)</span><span class="ok">${x1.stale.length}</span><span>Price mismatches vs quote (over 5%)</span><span class="ok">${x1.n_mismatch}</span><span>Extreme outliers flagged</span><span class="warn">${x1.n_outliers}</span><span>Deep-dive companies with 6+ quarters of reports</span><span class="ok">${x1.deep_complete}/100</span></div>
 <h4 style="margin-top:12px">Field coverage</h4>${bars(Object.fromEntries(Object.entries(x1.coverage).map(([k,v])=>[k,v])))}<p class="sm mute">Outliers kept but flagged: ${x1.outliers.map(o=>o[0]).join(', ')}. Mostly cyclical peaks or one-off accounting items.</p></div>
 <div class="card hi"><h3>X2 · Method & robustness</h3><p class="sm">I re-ran the committee 500 times with every agent weight randomly moved ±50%. Stability is the share of runs in which a stock stayed in the top 30.</p><div class="kv"><span>Median stability of the top 30</span><b>${pct(x2.median_stab,0)}</b><span>Fragile names (under 50%)</span><span class="warn">${x2.fragile.join(', ')||'none'}</span><span>Vetoes applied after diligence</span><span>${x2.vetoes_applied}</span><span>Vetoed stocks leaking into the top 30</span><span class="ok">${x2.veto_leak}</span></div>
 <p class="sm">Fragile names were barred from the portfolio. Known biases: the universe is today's S&amp;P 500 (survivorship bias), and the 3-year window has no full bear market, so risk looks lower than it will in a crash.</p></div>
 <div class="card hi"><h3>X3 · Output reconciliation</h3><div class="kv"><span>Scenario order errors (bull > base > bear)</span><span class="ok">${x3.scenario_order_fail.length}</span><span>Top 30 average expected return (model)</span><span>${sp(x3.exp_basket)}</span><span>Calibration haircut applied</span><span>40%</span><span>Portfolio calibrated expected</span><b>${pct(P.exp_cal)}</b></div>
 <h4 style="margin-top:12px">Reconciliation with my earlier answers</h4><table><thead><tr><th>Stock</th><th class="num">Rank of 497</th><th>Top 30?</th></tr></thead><tbody>${Object.entries(x3.prior_rank500).map(([t,r])=>`<tr><td>${t}</td><td class="num">${r}</td><td>${x3.prior_list[t]&&x3.prior_list[t][1]?'<span class="ok">Yes</span>':'<span class="mute">No</span>'}</td></tr>`).join('')}</tbody></table></div></div>
 <h2>Stability of each top-30 name</h2><div class="scroll"><table id="stb"></table></div>
 <h2>Sector tilt: top 30 vs the universe</h2><div class="scroll"><table><thead><tr><th>Sector</th><th class="num">Top 30</th><th class="num">Universe</th></tr></thead><tbody>${Object.entries(x2.sector_tilt).map(([s,[a,b]])=>`<tr><td>${s}</td><td class="num">${pct(a,0)}</td><td class="num">${pct(b,0)}</td></tr>`).join('')}</tbody></table></div>`;
 table('stb',[['t','Stock',v=>`<b>${v}</b>`],['rk','Rank',v=>v,'num'],['s','Stability',v=>`<span class="${v>=0.7?'ok':v>=0.5?'warn':'bad'}">${pct(v,0)}</span>`,'num']],D.top30.map(t=>({t,rk:C[t].rk30,s:x2.stability[t]})),{sort:'rk',click:t=>go('deep',t)});}
R.method=()=>{$('#app').innerHTML=`<h2 style="margin-top:0">Method</h2><div class="grid">
 <div class="card"><h4>Data (all live, ${D.asof})</h4><p class="sm">Full S&amp;P 500 list; 3 years of daily prices; company fundamentals; for the 100: 4 years of annual income, cash-flow and balance-sheet statements, 5 recent quarters, the last 8 quarterly earnings reports (estimate vs actual), EPS estimate trends and revisions, analyst upgrades and downgrades, insider activity and news. For the portfolio names, the latest earnings releases were read from SEC filings and company releases.</p></div>
 <div class="card"><h4>Stage 1 weights</h4><p class="sm">Quality 22%, Risk 20%, Valuation 18%, Growth 16%, Momentum 12%, Street 12%. Then refutation rounds: value-trap, bubble, cash-burn, risk-vs-hype, Buffett endorsement, red-team flags (−2 each).</p></div>
 <div class="card"><h4>Stage 3 weights</h4><p class="sm">Screen score 25%, Intrinsic value 25%, Earnings record 15%, Buffett checklist 15%, Forensic 10%, Capital allocation 10%. Final ranking: reward/risk 35%, confidence 25%, quality 20%, earnings momentum 20%.</p></div>
 <div class="card"><h4>Scenarios</h4><p class="sm">Base = median of up to 4 valuation methods, capped at −30% to +45%. Bull = average of a 10% earnings beat with a 10% re-rating, the highest Street target, and base +15%. Bear = average of a 15% earnings miss with a 20% de-rating, a 1-sigma volatility shock, the worst 12-month loss in 3 years, and the lowest Street target. Weights 25/50/25.</p></div>
 <div class="card"><h4>Tiers</h4><p class="sm"><b>A: Buy now</b> = expected 8%+, stability 70%+, confidence 50+, rank 15 or better. <b>B: Accumulate on dips</b> = expected 3%+. <b>C: Watchlist</b> = the rest.</p></div>
 <div class="card"><h4>Limits</h4><p class="sm">Analyst targets run optimistic, hence the 40% haircut. DCFs are sensitive to growth and discount-rate inputs. There was no bear market in the 3-year window. Earnings-call transcripts were not read in full; released numbers and releases were. Yahoo Finance data has occasional glitches, which the auditors flagged.</p></div></div>
 <h2>Glossary</h2><div class="grid">${[['Forward P/E','Price ÷ next year\'s expected profit per share. 15x = you pay $15 for $1 of profit.'],['DCF','Discounted cash flow: adds up all future cash the company will make, shrunk for time and risk, to get a fair price today.'],['Reverse DCF','Works backwards: what growth rate does today\'s price assume? If it is higher than realistic, the stock is priced for perfection.'],['WACC','The minimum return investors demand from this company. Future cash is discounted at this rate.'],['Piotroski F-score','9 yes/no accounting health tests. 7 to 9 is strong, 0 to 3 is weak.'],['Altman Z-score','Bankruptcy-risk formula. Below 1.8 is the danger zone (misleading for asset-light firms).'],['ROIC','Return on invested capital: profit per $1 put into the business. Buffett loves 15%+.'],['Accruals','Profit not backed by cash. High accruals can mean aggressive accounting.'],['Volatility','How wildly the price swings in a typical year.'],['Reward/risk','Expected return ÷ bear-case loss. Above 1 means you expect to make more than you could lose.'],['Stability','How often a stock stayed in the top 30 when agent weights were shuffled. High = the verdict doesn\'t depend on my assumptions.'],['Confidence','How much the evidence agrees (0 to 100).']].map(([a,b])=>`<div class="card"><h4>${a}</h4><p class="sm">${b}</p></div>`).join('')}</div>`;}
const D2=__DATA2__;
const P2=D2.P2,REC=P2.Recommended,C2=D2.C2;
TABS.unshift(['v2v','v2 · Verdict (Hurdle-15)'],['v2bt','v2 · Backtest'],['v2fr','v2 · Frontier & odds'],['v2c','v2 · Candidates (52)'],['v2rel','v2 · Release reader'],['v2u','v2 · Ranking (497)'],['v2g','v2 · Audit loops & grade']);
TABS.forEach(t=>{if(!t[1].startsWith('v2'))t[1]='v1 · '+t[1]});
cur='v2v';
const card2=(t)=>{const c=C2[t];if(!c)return'';const nt=D2.N2[t];const tl=(c.tl||[]).map(x=>`<span title="${x.d}" class="pill" style="border-color:${x.r?'var(--up)':x.c?'var(--down)':'var(--line)'}">${x.d.slice(2,7)} ${x.r?'▲':x.c?'▼':x.k?'=':'·'}</span>`).join('');
 return `<div class="card ${REC.w[t]?'hi':''}"><div class="hdr" style="border:0;padding:0"><div><h3>${esc(c.n)} (${t})</h3><div class="mute sm">${esc(c.s)} · ${esc(c.sub)}${REC.w[t]?` · <b style="color:var(--gold)">Portfolio ${pct(REC.w[t])}</b>`:''}</div></div><div style="text-align:right"><div class="big" style="font-size:26px">${usd(c.p)}</div><div class="sm mute">Confidence ${n(c.conf,0)} · v2 rank ${c.rk}/52</div></div></div>
 <div class="kv" style="margin-top:8px"><span>Conservative expected return (shrunk)</span><b>${sp(c.Esh)}</b><span>Building blocks: yield + growth + re-rating</span><span>${sp(c.Ebb)} = ${pct(c.by)} + ${pct(c.bg)} + ${pct(c.br)}</span><span>Factor model / scenario model</span><span>${sp(c.Efac)} / ${c.Escen==null?'n/a':sp(c.Escen)}</span><span>Methods disagree by</span><span>${pct(c.Esp,0)}</span>
 <span>Momentum / earnings momentum / value / quality</span><span>${Math.round(c.pm*100)} / ${Math.round(c.pe*100)} / ${Math.round(c.pv*100)} / ${Math.round(c.pq*100)}</span><span>Fwd P/E · volatility · 3-yr beta</span><span>${n(c.fpe)}x · ${pct(c.vol,0)} · ${n(c.beta,2)}</span><span>Guidance record (${c.nrel} releases)</span><span><span class="ok">${c.raises} raises</span> / <span class="bad">${c.cuts} cuts</span> / ${c.keeps} held</span></div>
 <div style="margin-top:8px">${tl}</div>${nt?`<ul class="pts sm">${nt.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`:''}<p class="sm"><a href="${c.url}" target="_blank" rel="noopener">Latest SEC earnings release</a>${C[t]?` · <a href="#" data-deep="${t}">Full v1 deep dive</a>`:''}</p></div>`};
function wireDeep(){document.querySelectorAll('a[data-deep]').forEach(a=>a.onclick=e=>{e.preventDefault();go(C[a.dataset.deep].rk30?'deep':'one',a.dataset.deep)})}
R.v2v=()=>{const w=REC.w,ks=Object.keys(w).sort((a,b)=>w[b]-w[a]);
$('#app').innerHTML=`<h1>v2: a 20-stock portfolio at the edge of your 15% hurdle.</h1><p class="lede">A point-in-time backtest showed my v1 model's low-volatility tilt lagged the market in all three test years. The redesigned model (momentum, earnings upgrades, value and quality) beat the market in all three years with two different weightings. After shrinking every forecast for optimism, the portfolio's conservative expected return is <b>${pct(REC.E)}</b> (raw model ${pct(REC.E_raw)}), with a <b>${pct(REC.p15,0)}</b> chance of 15%+.</p>
<div class="tally"><div><b>${pct(REC.E,1)}</b><span>conservative expected return</span></div><div><b>${pct(REC.p15,0)}</b><span>chance of 15%+</span></div><div><b>${pct(REC.p25,0)}</b><span>chance of 25%+</span></div><div><b>${pct(REC.p50,0)}</b><span>chance of 50%+</span></div><div><b>${pct(REC.vol,0)}</b><span>volatility (S&amp;P about 15%)</span></div><div><b>${pct(REC.y2022,0)}</b><span>replayed through 2022</span></div></div>
<h2>Mandate scorecard</h2><div class="scroll"><table><thead><tr><th>Your requirement</th><th>Result</th><th>Status</th></tr></thead><tbody>
<tr><td>15% a year hurdle</td><td>${pct(REC.E)} conservative (${pct(REC.E_raw)} raw); sensitivity range 12.4% to 15.9% depending on the market assumption</td><td class="warn">At the edge</td></tr>
<tr><td>Realistic chance of 15%+</td><td>${pct(REC.p15,0)} (roughly a coin flip)</td><td class="ok">Met</td></tr>
<tr><td>1-in-4 chance of 50%+ (read "0.5%" as 50%)</td><td>${pct(REC.p50,1)}. Needs about 67% volatility, which carries about a 1-in-3 chance of losing 30%+</td><td class="bad">Not achievable at acceptable risk</td></tr>
<tr><td>If you meant 25%+</td><td>${pct(REC.p25,0)}</td><td class="ok">Met</td></tr><tr><td>Chance of losing money in a year</td><td>${pct(1-REC.p0,0)}; 5th-percentile year ${sp(REC.p5)}</td><td class="mute">Accepted risk</td></tr></tbody></table></div>
<h2>The 20 holdings</h2><p class="mute">Each card shows the three return methods, the guidance record from 9 quarterly SEC releases (▲ raised, ▼ cut, = held), and notes from the latest release.</p><div class="grid">${ks.map(card2).join('')}</div><p class="mute sm">Not financial advice. Backtests use today's index members, which flatters absolute returns (measured at +6.3 points a year versus the real equal-weight S&amp;P ETF).</p>`;wireDeep();};
R.v2bt=()=>{const b=D2.BT,yrs=['2023','2024','2025'],f=D2.BT.f10,S=D2.AL.surv;
$('#app').innerHTML=`<h2 style="margin-top:0">Backtest: what I got wrong, and the fix</h2><p class="mute">Each September, the model was run using only information available then (statements with a 90-day lag, prices to date), and returns were measured over the next 12 months.</p>
<div class="scroll"><table><thead><tr><th>12 months from late Sept…</th>${yrs.map(y=>`<th class="num">${y}</th>`).join('')}</tr></thead><tbody>
<tr><td>S&amp;P 500</td>${yrs.map(y=>`<td class="num">${pct(b.v1[y].spx)}</td>`).join('')}</tr><tr><td>Real equal-weight S&amp;P (RSP ETF)</td>${yrs.map(y=>`<td class="num">${pct(S[y].RSP)}</td>`).join('')}</tr>
<tr><td>Equal-weight of today's members (survivorship-inflated)</td>${yrs.map(y=>`<td class="num">${pct(b.v1[y].ew)}</td>`).join('')}</tr>
<tr><td class="bad">v1 model top 30 (low-vol tilt)</td>${yrs.map(y=>`<td class="num bad">${pct(b.v1[y].top30)}</td>`).join('')}</tr>
<tr><td class="ok">v2 model top 30 (weighting A)</td>${yrs.map(y=>`<td class="num ok">${pct(b.v3[y].top30)}</td>`).join('')}</tr><tr><td class="ok">v2 model top 30 (weighting B)</td>${yrs.map(y=>`<td class="num ok">${pct(b.v3b[y].top30)}</td>`).join('')}</tr>
<tr><td>v1 rank correlation with next-year return (IC)</td>${yrs.map(y=>`<td class="num">${n(b.v1[y].ic,3)}</td>`).join('')}</tr><tr><td>v2 rank correlation (IC)</td>${yrs.map(y=>`<td class="num">${n(b.v3[y].ic,3)}</td>`).join('')}</tr>
<tr><td>Low-volatility pillar IC (why v1 failed)</td>${yrs.map(y=>`<td class="num bad">${n(b.v1[y].pillar_ic.R,3)}</td>`).join('')}</tr><tr><td>Momentum pillar IC</td>${yrs.map(y=>`<td class="num ok">${n(b.v1[y].pillar_ic.M,3)}</td>`).join('')}</tr></tbody></table></div>
<h2>Ten-year style test (monthly, top 50)</h2><div class="scroll"><table><thead><tr><th>Style</th><th class="num">CAGR</th><th class="num">Volatility</th><th class="num">Worst fall</th><th class="num">12m ≥15%</th><th class="num">12m ≥50%</th><th class="num">2022</th></tr></thead><tbody>${Object.entries(f).map(([k,v])=>`<tr><td>${k}</td><td class="num">${pct(v.cagr)}</td><td class="num">${pct(v.vol)}</td><td class="num">${pct(v.mdd)}</td><td class="num">${pct(v.p15,0)}</td><td class="num">${pct(v.p50,0)}</td><td class="num">${pct(v.y2022)}</td></tr>`).join('')}</tbody></table></div>
<p class="sm mute">Absolute numbers are inflated by survivorship bias; compare styles against each other. The edge carried into forecasts was cut by 58%, following McLean &amp; Pontiff (2016).</p>`;};
R.v2fr=()=>{const ks=Object.keys(P2).filter(k=>P2[k].w);
$('#app').innerHTML=`<h2 style="margin-top:0">Frontier: how much risk buys how much return</h2><p class="mute">Odds come from 20,000 simulated years built from 10 years of real monthly returns (including COVID and 2022), re-centred on each portfolio's conservative expected return.</p>
<div class="scroll"><table><thead><tr><th>Portfolio</th><th class="num">Names</th><th class="num">Expected</th><th class="num">Volatility</th><th class="num">Beta</th><th class="num">≥15%</th><th class="num">≥20%</th><th class="num">≥25%</th><th class="num">≥50%</th><th class="num">≤−20%</th><th class="num">2022</th><th class="num">COVID</th></tr></thead><tbody>${ks.map(k=>{const v=P2[k];return`<tr${k==='Recommended'?' style="outline:1px solid var(--gold)"':''}><td><b>${k}</b></td><td class="num">${v.n}</td><td class="num">${pct(v.E)}</td><td class="num">${pct(v.vol)}</td><td class="num">${n(v.beta,2)}</td><td class="num">${pct(v.p15,0)}</td><td class="num">${pct(v.p20,0)}</td><td class="num">${pct(v.p25,0)}</td><td class="num">${pct(v.p50,1)}</td><td class="num">${pct(v.pl20,1)}</td><td class="num">${pct(v.y2022)}</td><td class="num">${pct(v.covid)}</td></tr>`}).join('')}</tbody></table></div>
<h2>Sensitivity: what moves the recommended portfolio's expected return</h2><div class="scroll"><table><tbody>${Object.entries(D2.AL.sens).map(([k,v])=>`<tr><td>${k}</td><td class="num">${pct(v)}</td></tr>`).join('')}</tbody></table></div><p class="sm mute">The biggest single lever is what the overall market does (the 10% prior). Stock-picking edge adds about 1 point.</p>`;};
R.v2c=()=>{const ks=Object.keys(C2).sort((a,b)=>C2[a].rk-C2[b].rk);$('#app').innerHTML=`<h2 style="margin-top:0">All 52 release-read candidates</h2><div class="grid">${ks.map(card2).join('')}</div>`;wireDeep();};
R.v2rel=()=>{const rows=Object.values(C2).map(c=>({t:c.t,n:c.n,nrel:c.nrel,r:c.raises,c:c.cuts,k:c.keeps,gs:c.gs,hw:c.flags.headwind,inv:c.flags.investig,url:c.url}));
$('#app').innerHTML=`<h2 style="margin-top:0">Earnings-release reader: 467 SEC filings</h2><p class="mute">Every 8-K Item 2.02 earnings release since July 2024 was read for guidance raises, cuts and maintains, plus red-flag language. Companies that don't give guidance (many insurers and payment networks) score neutral. Keyword reading can misfire; see the audit notes.</p><div class="scroll"><table id="rt"></table></div>`;
table('rt',[['t','Ticker',v=>`<b>${v}</b>`],['n','Company',v=>esc(v)],['nrel','Releases',v=>v,'num'],['r','Raises',v=>`<span class="ok">${v}</span>`,'num'],['c','Cuts',v=>`<span class="bad">${v}</span>`,'num'],['k','Held',v=>v,'num'],['gs','Net score',v=>n(v,2),'num'],['hw','"Headwind" mentions',v=>v,'num'],['inv','Investigation mentions',v=>v,'num'],['url','Latest',v=>`<a href="${v}" target="_blank" rel="noopener">SEC</a>`]],rows,{sort:'gs',asc:false});};
R.v2u=()=>{$('#app').innerHTML=`<h2 style="margin-top:0">v2 ranking of all 497</h2><div class="scroll" style="max-height:700px"><table id="u3"></table></div>`;
table('u3',[['rk','#',v=>v,'num'],['t','Ticker',v=>`<b>${v}</b>`],['n','Name',v=>esc(v)],['s','Sector'],['v3','Score',v=>n(v,0),'num'],['pm','Momentum',v=>Math.round(v*100),'num'],['pe','Earnings mom.',v=>Math.round(v*100),'num'],['pv','Value',v=>Math.round(v*100),'num'],['pq','Quality',v=>Math.round(v*100),'num'],['E','Expected (3-method)',v=>sp(v),'num'],['vol','Volatility',v=>pct(v,0),'num'],['why','Gate',(v,r)=>r.gate?'<span class="ok">Pass</span>':`<span class="bad">${v}</span>`]],D2.U3,{sort:'rk'});};
R.v2g=()=>{const g=D2.grade2,tot=g.reduce((a,b)=>a+b[1],0);
$('#app').innerHTML=`<h2 style="margin-top:0">Audit loops & self-grade: ${tot}/100</h2><p class="mute">Grade history: 58 (first list), 78 (v1 dashboard), 91 (v2 analysis), ${tot} (after audit loops). The honest ceiling in this environment is about 93. Reaching 95+ needs data I can't get here: earnings-call transcripts, point-in-time analyst-estimate history, and a survivorship-free index history.</p>
<div class="scroll"><table><thead><tr><th>Criterion</th><th class="num">Score</th><th>Evidence / gap</th></tr></thead><tbody>${g.map(([a,s,e])=>`<tr><td>${a}</td><td class="num"><b>${s}</b>/10</td><td class="w">${esc(e)}</td></tr>`).join('')}</tbody></table></div>
<h2>Errors found and fixed in v2 and the audit loops</h2><div class="grid">${D2.fix2.concat(D2.fix3).map(([h,b])=>`<div class="card"><h4>${esc(h)}</h4><p class="sm">${esc(b)}</p></div>`).join('')}</div>
<h2>Audit loop results</h2><div class="grid"><div class="card"><h4>Loop 1 · Holdings integrity</h4><p class="sm">All 20 holdings pass gates; 180 of 180 releases matched to the right company, except NVIDIA (CFO commentary pulled instead of the press release; neutralised).</p></div><div class="card"><h4>Loop 2 · Survivorship bias</h4><p class="sm">Today's-member equal-weight beat the real equal-weight S&amp;P ETF by ${Object.values(D2.AL.surv).map(x=>pct(x.bias)).join(', ')}. The alpha estimate compares like with like, so it is unaffected; absolute backtest returns are labelled as inflated.</p></div><div class="card"><h4>Loop 3 · Assumption sensitivity</h4><p class="sm">Expected return ranges ${pct(Math.min(...Object.values(D2.AL.sens)))} to ${pct(Math.max(...Object.values(D2.AL.sens)))}. The 15% hurdle depends mostly on the market, not on stock picking.</p></div></div>`;};

TABS.unshift(['cv','★ Conviction portfolio (final)']);cur='cv';
R.cv=()=>{const V=D2.CV,P=V.P,b=P.blend,rows=V.rows,inp=rows.filter(r=>r.inp).sort((a,b)=>b.w-a.w);
const note=t=>V.NC[t]||(D2.N2&&D2.N2[t])||(C[t]&&C[t].dil&&C[t].dil.notes.slice(0,3))||[];
const tier=s=>s>=0.9?'<span class="tag tA">Core ≥90%</span>':s>=0.7?'<span class="tag tB">Conviction</span>':'<span class="tag tC">Supporting</span>';
$('#app').innerHTML=`<h1>No stock earns 90% confidence. A portfolio can.</h1><p class="lede">Ten independent lens-agents voted on all ${V.n497} S&amp;P 500 stocks. The vote was re-run 500 times with every threshold moved ±20%. Only <b>${V.core}</b> stocks stay on the conviction list in 90%+ of those runs. I also back-tested the conviction filter itself: its picks rose in only 56–64% of cases over the following year, no better than a random stock. So 90% confidence per stock is not something anyone can honestly claim. What does reach about 90% is making money over 5 years with the portfolio below held alongside an index core.</p>
<div class="tally"><div><b>${V.n497}</b><span>stocks voted on by 10 lenses</span></div><div><b>${V.base}</b><span>pass 9 of 10 lenses</span></div><div><b>${V.s70}</b><span>survive 70%+ of 500 re-runs</span></div><div><b>${V.core}</b><span>survive 90%+ (core)</span></div><div><b>${pct(b['50% index'].p5,0)}</b><span>5-yr odds of profit, 50/50 with index</span></div></div>
<h2>The 14 stocks, ranked and weighted</h2><div class="scroll"><table><thead><tr><th>#</th><th>Stock</th><th>Tier</th><th class="num">Weight</th><th class="num">Robustness</th><th class="num">Lenses passed</th><th class="num">Expected (conservative)</th><th class="num">Fwd P/E</th><th class="num">Volatility</th></tr></thead><tbody>${inp.map((r,i)=>`<tr><td>${i+1}</td><td><b>${r.t}</b><br><span class="mute sm">${esc(r.n)}</span></td><td>${tier(r.stab)}</td><td class="num"><b>${pct(r.w)}</b></td><td class="num">${pct(r.stab,0)}</td><td class="num">${r.passes}/10</td><td class="num">${sp(r.E)}</td><td class="num">${n(r.fpe)}x</td><td class="num">${pct(r.vol,0)}</td></tr>`).join('')}</tbody></table></div>
<h2>Odds: stocks alone vs blended with an S&amp;P index fund (same simulation)</h2><div class="scroll"><table><thead><tr><th>Mix</th><th class="num">Expected / yr</th><th class="num">Volatility</th><th class="num">1-yr odds of profit</th><th class="num">5-yr odds of profit</th><th class="num">Bad year (5th pct)</th></tr></thead><tbody>${Object.entries(b).map(([k,v])=>`<tr><td>${k==='0% index'?'100% conviction stocks':k==='100% index'?'100% S&P index':k+' / rest conviction stocks'}</td><td class="num">${pct(v.E)}</td><td class="num">${pct(v.vol)}</td><td class="num">${pct(v.p1,0)}</td><td class="num"><b>${pct(v.p5,0)}</b></td><td class="num">${pct(v.p5th1)}</td></tr>`).join('')}</tbody></table></div>
<p class="sm mute">Replays of the 14 stocks: 2022 ${pct(P.y2022)}, COVID crash ${pct(P.covid)}, worst fall in 10 yrs ${pct(P.mdd10)}. For a UAE resident, hold the index part via an Irish-domiciled S&amp;P 500 fund, which avoids US estate tax and halves dividend withholding.</p>
<h2>Lens votes (✓ pass) for every candidate that survives at least half the re-runs</h2><div class="scroll"><table><thead><tr><th>Stock</th><th class="num">Robust</th>${V.lens.map(l=>`<th class="sm">${l}</th>`).join('')}</tr></thead><tbody>${rows.map(r=>`<tr><td><b>${r.t}</b>${r.inp?' <span class="tag tA">in</span>':''}</td><td class="num">${pct(r.stab,0)}</td>${V.lens.map(l=>`<td>${r.votes[l]?'<span class="ok">✓</span>':'<span class="bad">✗</span>'}</td>`).join('')}</tr>`).join('')}</tbody></table></div>
<h2>What the latest earnings releases say</h2><div class="grid">${inp.map(r=>`<div class="card"><h4>${r.t}: ${esc(r.n)} (${pct(r.w)})</h4><ul class="pts sm">${note(r.t).map(x=>`<li>${esc(x)}</li>`).join('')}</ul></div>`).join('')}</div>
<h2>Point-in-time test of the conviction filter</h2><div class="scroll"><table><thead><tr><th>Start</th><th class="num">Picks</th><th class="num">Avg return</th><th class="num">% of picks up</th><th class="num">% beating S&amp;P</th><th class="num">% of all stocks up</th></tr></thead><tbody>${Object.entries(V.BT).filter(([y,v])=>v.n>0).map(([y,v])=>`<tr><td>Sep ${y}</td><td class="num">${v.n}</td><td class="num">${pct(v.mean)}</td><td class="num">${pct(v.pos,0)}</td><td class="num">${pct(v.beat_spx,0)}</td><td class="num">${pct(v.univ_pos,0)}</td></tr>`).join('')}</tbody></table></div>
<h2>Self-grade: ${D2.grade3.reduce((a,g)=>a+g[1],0)}/100</h2><div class="scroll"><table><tbody>${D2.grade3.map(([a,s,e])=>`<tr><td>${a}</td><td class="num"><b>${s}</b>/10</td><td class="w">${esc(e)}</td></tr>`).join('')}</tbody></table></div><p class="mute sm">Not financial advice.</p>`;};

tabs();R[cur]();
</script></body></html>
```

## Appendix C — Key result files
### `conv_port.json`
```json
{
 "pick": [
  "NVDA",
  "CPAY",
  "AMP",
  "RL",
  "AME",
  "SNA",
  "ABNB",
  "NTAP",
  "PAYX",
  "MSFT",
  "IBKR",
  "HIG",
  "ALLE",
  "AIZ"
 ],
 "w": {
  "NVDA": 0.0997,
  "CPAY": 0.0728,
  "AMP": 0.0696,
  "RL": 0.1063,
  "AME": 0.0835,
  "SNA": 0.0732,
  "ABNB": 0.1063,
  "NTAP": 0.0803,
  "PAYX": 0.0546,
  "MSFT": 0.0824,
  "IBKR": 0.04,
  "HIG": 0.04,
  "ALLE": 0.0511,
  "AIZ": 0.04
 },
 "E": 0.11361673867909997,
 "vol": 0.1892840899368008,
 "p_pos1": 0.7192,
 "p_pos5": 0.86855,
 "p_double5": 0.2768,
 "ann5_med": 0.09712446619527748,
 "p5_1": -0.2030581568808236,
 "p5_5": -0.20074786120986196,
 "p_loss20_1": 0.05225,
 "p15_1": 0.4099,
 "spx": {
  "p_pos1": 0.76245,
  "p_pos5": 0.92025,
  "vol": 0.15220479943220616
 },
 "y2022": -0.19057467605706846,
 "covid": -0.21820562211144123,
 "mdd10": -0.2617701602601189,
 "sectors": {
  "Consumer Discretionary": 2,
  "Financials": 5,
  "Industrials": 4,
  "Information Technology": 3
 },
 "blend": {
  "0% index": {
   "E": 0.11361673867909997,
   "vol": 0.18924295383586007,
   "p1": 0.71525,
   "p5": 0.86935,
   "p5th1": -0.19625035131549148
  },
  "50% index": {
   "E": 0.10680836933954999,
   "vol": 0.16670261317530027,
   "p1": 0.74615,
   "p5": 0.90125,
   "p5th1": -0.16110683098763112
  },
  "70% index": {
   "E": 0.10408502160372998,
   "vol": 0.1597886611860519,
   "p1": 0.755,
   "p5": 0.91035,
   "p5th1": -0.14926087011642683
  },
  "100% index": {
   "E": 0.1,
   "vol": 0.15220479943220616,
   "p1": 0.76275,
   "p5": 0.91935,
   "p5th1": -0.13365852345155532
  }
 }
}
```

### `bt_conv.json`
```json
{
 "2023": {
  "n": 0,
  "mean": NaN,
  "median": NaN,
  "pos": NaN,
  "beat_spx": NaN,
  "univ_pos": 0.8762886597938144,
  "univ_mean": 0.35412946570745407,
  "worst": NaN
 },
 "2024": {
  "n": 28,
  "mean": 0.10342205075809448,
  "median": 0.08968636042265676,
  "pos": 0.6428571428571429,
  "beat_spx": 0.39285714285714285,
  "univ_pos": 0.6130346232179226,
  "univ_mean": 0.1447384391297167,
  "worst": -0.4810979780110819
 },
 "2025": {
  "n": 34,
  "mean": 0.0699321749327657,
  "median": 0.032762149921497064,
  "pos": 0.5588235294117647,
  "beat_spx": 0.29411764705882354,
  "univ_pos": 0.5757575757575758,
  "univ_mean": 0.17912035075901556,
  "worst": -0.4055088907575748
 }
}
```

### `audit_loop1.json`
```json
{
 "surv": {
  "2023": {
   "RSP": 0.2831716884158413,
   "EW_survivors": 0.35412946570745407,
   "bias": 0.07095777729161279,
   "v3_top30": 0.36351525835945336,
   "v3_vs_RSP": 0.08034356994361208,
   "v3_vs_EWsurv": 0.009385792651999292
  },
  "2024": {
   "RSP": 0.07164815360232768,
   "EW_survivors": 0.1447384391297167,
   "bias": 0.07309028552738903,
   "v3_top30": 0.21281725942494115,
   "v3_vs_RSP": 0.14116910582261347,
   "v3_vs_EWsurv": 0.06807882029522444
  },
  "2025": {
   "RSP": 0.13284675409406943,
   "EW_survivors": 0.17912035075901556,
   "bias": 0.046273596664946126,
   "v3_top30": 0.3030518058344892,
   "v3_vs_RSP": 0.17020505174041978,
   "v3_vs_EWsurv": 0.12393145507547365
  }
 },
 "sens": {
  "Base case": 0.1420127845534253,
  "Market prior 8%": 0.1242953051850359,
  "Market prior 12%": 0.15925142860603372,
  "Growth haircut 50%": 0.13838068450573093,
  "No growth haircut": 0.14693881548979285,
  "Alpha zero": 0.13420407975478854,
  "Alpha unshrunk (6.7%)": 0.14302283041517486
 }
}
```

### `port2.json`
```json
{
 "Guardian": {
  "E": 0.12130377699194116,
  "E_raw": 0.1497830859044501,
  "vol": 0.14294161916564935,
  "p15": 0.4151,
  "p20": 0.30465,
  "p25": 0.2054,
  "p50": 0.00885,
  "p0": 0.76245,
  "pl10": 0.086,
  "pl20": 0.02135,
  "p5": -0.146159404696103,
  "p50th": 0.11478010327347543,
  "p95": 0.38358962694666693,
  "y2022": -0.15642589421484743,
  "covid": -0.18453869660510758,
  "mdd10": -0.26565939588770515,
  "n": 17,
  "beta": 0.8998117113105094,
  "conf": 77.58501050832376,
  "w": {
   "GEN": 0.0245,
   "MMM": 0.0691,
   "INCY": 0.0517,
   "BIIB": 0.0724,
   "ADSK": 0.0975,
   "NTAP": 0.0228,
   "VTRS": 0.0665,
   "AIZ": 0.1035,
   "BKNG": 0.0826,
   "NEM": 0.0617,
   "HAS": 0.0585,
   "BBY": 0.0351,
   "DD": 0.0551,
   "AMP": 0.0475,
   "TROW": 0.0767,
   "JBHT": 0.0507,
   "EMR": 0.024
  },
  "vol_cap": 0.14,
  "hit": {
   "GEN": 1.0,
   "MMM": 1.0,
   "INCY": 1.0,
   "BIIB": 1.0,
   "ADSK": 1.0,
   "NTAP": 1.0,
   "VTRS": 1.0,
   "AIZ": 1.0,
   "BKNG": 1.0,
   "NEM": 1.0,
   "HAS": 1.0,
   "BBY": 1.0,
   "DD": 1.0,
   "AMP": 1.0,
   "TROW": 1.0,
   "JBHT": 1.0,
   "EMR": 1.0
  }
 },
 "Balanced": {
  "E": 0.131134213128918,
  "E_raw": 0.15796608547412377,
  "vol": 0.15148960431762218,
  "p15": 0.44365,
  "p20": 0.33535,
  "p25": 0.2397,
  "p50": 0.01435,
  "p0": 0.7657,
  "pl10": 0.0921,
  "pl20": 0.0256,
  "p5": -0.15317707039366915,
  "p50th": 0.12602808078536132,
  "p95": 0.40882664960006115,
  "y2022": -0.18087826116655814,
  "covid": -0.1815262283477903,
  "mdd10": -0.2571812798051887,
  "n": 25,
  "beta": 1.0716836445703102,
  "conf": 77.12353986451306,
  "w": {
   "EXPE": 0.0252,
   "HPE": 0.0357,
   "GEN": 0.0608,
   "CPAY": 0.02,
   "MMM": 0.0599,
   "INCY": 0.0296,
   "NVDA": 0.0402,
   "BIIB": 0.0522,
   "ADSK": 0.0657,
   "GPN": 0.0359,
   "SWK": 0.0265,
   "VTRS": 0.0459,
   "AIZ": 0.0924,
   "BKNG": 0.0622,
   "NEM": 0.0336,
   "ADI": 0.0267,
   "HAS": 0.0296,
   "BBY": 0.031,
   "DD": 0.0317,
   "FIX": 0.0217,
   "KEYS": 0.0191,
   "AMP": 0.0423,
   "TROW": 0.0587,
   "JBHT": 0.0361,
   "ANET": 0.0174
  },
  "vol_cap": 0.16,
  "hit": {
   "EXPE": 0.32,
   "HPE": 0.57,
   "GEN": 0.75,
   "CPAY": 0.32,
   "MMM": 0.7,
   "INCY": 0.5,
   "NVDA": 0.62,
   "BIIB": 0.72,
   "ADSK": 0.72,
   "GPN": 0.57,
   "SWK": 0.5,
   "NTAP": 0.25,
   "VTRS": 0.75,
   "AIZ": 0.95,
   "BKNG": 0.68,
   "NEM": 0.6,
   "IVZ": 0.22,
   "ADI": 0.38,
   "HAS": 0.52,
   "BBY": 0.65,
   "DD": 0.45,
   "FIX": 0.48,
   "KEYS": 0.25,
   "AMP": 0.65,
   "TROW": 0.85,
   "JBHT": 0.55,
   "ANET": 0.32,
   "FCX": 0.12,
   "EMR": 0.2
  }
 },
 "Hurdle": {
  "E": 0.13727165091024285,
  "E_raw": 0.16395657255252916,
  "vol": 0.16741205132048909,
  "p15": 0.4564,
  "p20": 0.3617,
  "p25": 0.27445,
  "p50": 0.03485,
  "p0": 0.74325,
  "pl10": 0.11575,
  "pl20": 0.04075,
  "p5": -0.18346410301518537,
  "p50th": 0.1279199814873716,
  "p95": 0.4632754114572778,
  "y2022": -0.1636694645966914,
  "covid": -0.2174740280915073,
  "mdd10": -0.2741466915939943,
  "n": 27,
  "beta": 1.1905468659512475,
  "conf": 75.0444465250967,
  "w": {
   "EXPE": 0.0426,
   "HPE": 0.0649,
   "GEN": 0.0684,
   "CPAY": 0.0249,
   "MMM": 0.0272,
   "INCY": 0.0309,
   "NVDA": 0.032,
   "BIIB": 0.0386,
   "ADSK": 0.0514,
   "GPN": 0.0436,
   "SWK": 0.0478,
   "VTRS": 0.041,
   "BKNG": 0.0432,
   "NEM": 0.0325,
   "IVZ": 0.0395,
   "ADI": 0.0374,
   "HAS": 0.0235,
   "BBY": 0.0384,
   "DD": 0.0345,
   "FIX": 0.0557,
   "KEYS": 0.0219,
   "AMP": 0.0353,
   "TROW": 0.0288,
   "JBHT": 0.0289,
   "ANET": 0.0175,
   "FCX": 0.0269,
   "EMR": 0.0225
  },
  "vol_cap": 0.18,
  "hit": {
   "EXPE": 0.48,
   "HPE": 0.72,
   "GEN": 0.72,
   "CPAY": 0.32,
   "MMM": 0.28,
   "INCY": 0.5,
   "NVDA": 0.48,
   "BIIB": 0.57,
   "ADSK": 0.6,
   "GPN": 0.65,
   "SWK": 0.68,
   "NTAP": 0.1,
   "VTRS": 0.57,
   "AIZ": 0.15,
   "BKNG": 0.52,
   "NEM": 0.45,
   "IVZ": 0.6,
   "ADI": 0.48,
   "HAS": 0.32,
   "BBY": 0.5,
   "DD": 0.38,
   "FIX": 0.7,
   "KEYS": 0.22,
   "AMP": 0.55,
   "TROW": 0.45,
   "JBHT": 0.4,
   "ANET": 0.28,
   "FCX": 0.38,
   "EMR": 0.32
  }
 },
 "Stretch": {
  "E": 0.1370452504153708,
  "E_raw": 0.16136596690974148,
  "vol": 0.17112328513124792,
  "p15": 0.4577,
  "p20": 0.36355,
  "p25": 0.27845,
  "p50": 0.0385,
  "p0": 0.73845,
  "pl10": 0.12175,
  "pl20": 0.0461,
  "p5": -0.19201613475060922,
  "p50th": 0.1285099805618366,
  "p95": 0.4715905598031409,
  "y2022": -0.1683478641132239,
  "covid": -0.22620367669522168,
  "mdd10": -0.2745302926341624,
  "n": 28,
  "beta": 1.2271190929738516,
  "conf": 74.91847235970555,
  "w": {
   "EXPE": 0.0485,
   "HPE": 0.0615,
   "GEN": 0.0512,
   "CPAY": 0.0356,
   "MMM": 0.0292,
   "INCY": 0.0363,
   "NVDA": 0.0324,
   "BIIB": 0.0304,
   "ADSK": 0.0516,
   "GPN": 0.0425,
   "SWK": 0.0492,
   "NTAP": 0.0169,
   "VTRS": 0.0304,
   "BKNG": 0.0443,
   "NEM": 0.025,
   "IVZ": 0.0388,
   "ADI": 0.0247,
   "HAS": 0.021,
   "BBY": 0.0294,
   "DD": 0.0256,
   "FIX": 0.0712,
   "KEYS": 0.0271,
   "AMP": 0.0288,
   "TROW": 0.0265,
   "JBHT": 0.0324,
   "ANET": 0.0253,
   "FCX": 0.0358,
   "EMR": 0.0285
  },
  "vol_cap": 0.22,
  "hit": {
   "EXPE": 0.57,
   "HPE": 0.65,
   "GEN": 0.57,
   "CPAY": 0.45,
   "MMM": 0.32,
   "INCY": 0.55,
   "NVDA": 0.5,
   "BIIB": 0.48,
   "ADSK": 0.55,
   "GPN": 0.65,
   "SWK": 0.7,
   "NTAP": 0.22,
   "VTRS": 0.45,
   "AIZ": 0.08,
   "BKNG": 0.5,
   "NEM": 0.35,
   "IVZ": 0.55,
   "ADI": 0.35,
   "HAS": 0.22,
   "BBY": 0.35,
   "DD": 0.25,
   "FIX": 0.72,
   "KEYS": 0.32,
   "AMP": 0.52,
   "TROW": 0.38,
   "JBHT": 0.5,
   "ANET": 0.4,
   "FCX": 0.52,
   "EMR": 0.42
  }
 },
 "S&P 500 (for reference)": {
  "E": 0.1,
  "vol": 0.15283767035087614
 },
 "Recommended": {
  "E": 0.14198557367291953,
  "E_raw": 0.1766870545949394,
  "vol": 0.1678034294151754,
  "p15": 0.46425,
  "p20": 0.37065,
  "p25": 0.28605,
  "p50": 0.04135,
  "p0": 0.74515,
  "pl10": 0.11355,
  "pl20": 0.03965,
  "p5": -0.1814371394419736,
  "p50th": 0.13019234486662123,
  "p95": 0.4790609023284444,
  "y2022": -0.16530325599719098,
  "covid": -0.2093560683818353,
  "mdd10": -0.27763933496820314,
  "n": 20,
  "beta": 1.1614704127121578,
  "conf": 74.53722767536507,
  "w": {
   "GEN": 0.0819,
   "HPE": 0.0777,
   "FIX": 0.0667,
   "SWK": 0.0572,
   "ADSK": 0.0615,
   "GPN": 0.0522,
   "IVZ": 0.0473,
   "VTRS": 0.0491,
   "BKNG": 0.0517,
   "BIIB": 0.0462,
   "EXPE": 0.051,
   "AMP": 0.0423,
   "BBY": 0.046,
   "ADI": 0.0448,
   "INCY": 0.037,
   "NVDA": 0.0383,
   "NEM": 0.0389,
   "DD": 0.0413,
   "TROW": 0.0345,
   "JBHT": 0.0346
  },
  "hit": {
   "GEN": 0.72,
   "HPE": 0.72,
   "FIX": 0.7,
   "SWK": 0.68,
   "ADSK": 0.6,
   "GPN": 0.65,
   "IVZ": 0.6,
   "VTRS": 0.57,
   "BKNG": 0.52,
   "BIIB": 0.57,
   "EXPE": 0.48,
   "AMP": 0.55,
   "BBY": 0.5,
   "ADI": 0.48,
   "INCY": 0.5,
   "NVDA": 0.48,
   "NEM": 0.45,
   "DD": 0.38,
   "TROW": 0.45,
   "JBHT": 0.4
  }
 }
}
```

### `bt_v3.json`
```json
{
 "2023": {
  "n": 485,
  "n_elig": 375,
  "spx": 0.33817706958587435,
  "ew": 0.35412946570745407,
  "elig_ew": 0.3200945877458139,
  "top10": 0.39928996501244757,
  "top30": 0.36351525835945336,
  "topq": 0.37227696682468375,
  "botq": 0.22412760892911668,
  "vetoed": 0.4701574587585004,
  "ic": 0.13535737854135851,
  "pillar_ic": {
   "Q": -0.0850383578970927,
   "G": 0.020564149536723104,
   "V": 0.013538245113121135,
   "M": 0.1803364722047452,
   "R": -0.13607165115215164
  },
  "top10_names": [
   "WSM",
   "NUE",
   "LEN",
   "PHM",
   "APA",
   "CF",
   "LRCX",
   "NTAP",
   "NVR",
   "PSX"
  ],
  "hit15_top30": 0.6333333333333333,
  "hit15_all": 0.7306666666666667,
  "top30_vol": 0.34594898147673625,
  "all_vol": 0.2822417280239112
 },
 "2024": {
  "n": 491,
  "n_elig": 391,
  "spx": 0.15780820118021355,
  "ew": 0.1447384391297167,
  "elig_ew": 0.08261521533804085,
  "top10": 0.19459416804548818,
  "top30": 0.21281725942494115,
  "topq": 0.20960297966787858,
  "botq": -0.0015267526894125244,
  "vetoed": 0.38764024415516923,
  "ic": 0.21238401715201136,
  "pillar_ic": {
   "Q": -0.0296059940105468,
   "G": 0.14475013717641377,
   "V": 0.04190210913352269,
   "M": 0.20224524328972407,
   "R": -0.05140647233041932
  },
  "top10_names": [
   "IBKR",
   "SYF",
   "PEG",
   "T",
   "ACGL",
   "GDDY",
   "GEN",
   "EBAY",
   "PHM",
   "KIM"
  ],
  "hit15_top30": 0.5,
  "hit15_all": 0.35805626598465473,
  "top30_vol": 0.26782571132134564,
  "all_vol": 0.253554667534449
 },
 "2025": {
  "n": 495,
  "n_elig": 412,
  "spx": 0.1565661385830599,
  "ew": 0.17912035075901556,
  "elig_ew": 0.13666731422670603,
  "top10": 0.4709667661867993,
  "top30": 0.3030518058344892,
  "topq": 0.26512528411761316,
  "botq": 0.013955793545649473,
  "vetoed": 0.3898510863169859,
  "ic": 0.13137570795918835,
  "pillar_ic": {
   "Q": -0.12120130063586856,
   "G": -0.16935243817204443,
   "V": 0.11302463188683567,
   "M": 0.14180652663108392,
   "R": -0.2553698393303525
  },
  "top10_names": [
   "SYF",
   "IBKR",
   "EXPE",
   "WDC",
   "UAL",
   "LRCX",
   "FOXA",
   "LDOS",
   "EME",
   "TEL"
  ],
  "hit15_top30": 0.4666666666666667,
  "hit15_all": 0.38106796116504854,
  "top30_vol": 0.4124107798296789,
  "all_vol": 0.3184920673682163
 }
}
```

### `backtest.json`
```json
{
 "2023": {
  "n": 485,
  "n_elig": 375,
  "spx": 0.33817706958587435,
  "ew": 0.35412946570745407,
  "elig_ew": 0.3200945877458139,
  "top10": 0.22864067300262514,
  "top30": 0.2392374140524645,
  "topq": 0.25517581827472796,
  "botq": 0.2542085466283894,
  "vetoed": 0.4701574587585004,
  "ic": -0.0724608032768233,
  "pillar_ic": {
   "Q": -0.0850383578970927,
   "G": 0.020564149536723104,
   "V": 0.013538245113121135,
   "M": 0.1803364722047452,
   "R": -0.13607165115215164
  },
  "top10_names": [
   "MRK",
   "AMGN",
   "MO",
   "ABBV",
   "SNA",
   "IBKR",
   "GILD",
   "CF",
   "ADP",
   "MCK"
  ],
  "hit15_top30": 0.7,
  "hit15_all": 0.7306666666666667,
  "top30_vol": 0.2304553362581262,
  "all_vol": 0.2822417280239112
 },
 "2024": {
  "n": 491,
  "n_elig": 391,
  "spx": 0.15780820118021355,
  "ew": 0.1447384391297167,
  "elig_ew": 0.08261521533804085,
  "top10": 0.08266219370563078,
  "top30": 0.10629294165420765,
  "topq": 0.12120718892793159,
  "botq": 0.06211842457181433,
  "vetoed": 0.38764024415516923,
  "ic": 0.13218089911549907,
  "pillar_ic": {
   "Q": -0.0296059940105468,
   "G": 0.14475013717641377,
   "V": 0.04190210913352269,
   "M": 0.20224524328972407,
   "R": -0.05140647233041932
  },
  "top10_names": [
   "PEG",
   "ACGL",
   "IBKR",
   "VICI",
   "JNJ",
   "MO",
   "CB",
   "EG",
   "LMT",
   "CL"
  ],
  "hit15_top30": 0.4,
  "hit15_all": 0.35805626598465473,
  "top30_vol": 0.1915743409688935,
  "all_vol": 0.253554667534449
 },
 "2025": {
  "n": 495,
  "n_elig": 412,
  "spx": 0.1565661385830599,
  "ew": 0.17912035075901556,
  "elig_ew": 0.13666731422670603,
  "top10": -0.009671945033195805,
  "top30": 0.08009844197833352,
  "topq": 0.06085989359744871,
  "botq": 0.30631869819375773,
  "vetoed": 0.3898510863169859,
  "ic": -0.17793684558763853,
  "pillar_ic": {
   "Q": -0.12120130063586856,
   "G": -0.16935243817204443,
   "V": 0.11302463188683567,
   "M": 0.14180652663108392,
   "R": -0.2553698393303525
  },
  "top10_names": [
   "MO",
   "FOXA",
   "VICI",
   "CME",
   "DUK",
   "WRB",
   "HIG",
   "CINF",
   "VZ",
   "SO"
  ],
  "hit15_top30": 0.26666666666666666,
  "hit15_all": 0.38106796116504854,
  "top30_vol": 0.26077428440708317,
  "all_vol": 0.3184920673682163
 }
}
```

### `bt10.json`
```json
{
 "Momentum (12-1)": {
  "cagr": 0.2911064285947784,
  "vol": 0.22158770931258576,
  "mdd": -0.20341541918573736,
  "p15": 0.7129629629629629,
  "p25": 0.5,
  "p50": 0.21296296296296297,
  "ploss20": 0.0,
  "worst12": -0.09083564329566207,
  "y2022": -0.014968460348730561,
  "y2020": -0.1906704622152422
 },
 "Low volatility": {
  "cagr": 0.09903044835272734,
  "vol": 0.1283604866389363,
  "mdd": -0.2086492563531076,
  "p15": 0.3425925925925926,
  "p25": 0.07407407407407407,
  "p50": 0.0,
  "ploss20": 0.0,
  "worst12": -0.07228637205430843,
  "y2022": -0.016523434740856158,
  "y2020": -0.2086492563531076
 },
 "Momentum + low vol": {
  "cagr": 0.11422488950157894,
  "vol": 0.13819337446289387,
  "mdd": -0.19816012219937074,
  "p15": 0.39814814814814814,
  "p25": 0.10185185185185185,
  "p50": 0.0,
  "ploss20": 0.0,
  "worst12": -0.11587450086020257,
  "y2022": -0.11587450086020257,
  "y2020": -0.19816012219937085
 },
 "Momentum + trend, vol-capped": {
  "cagr": 0.15499969207285225,
  "vol": 0.1684866077071093,
  "mdd": -0.20227871854437118,
  "p15": 0.49074074074074076,
  "p25": 0.26851851851851855,
  "p50": 0.027777777777777776,
  "ploss20": 0.0,
  "worst12": -0.11411995585707668,
  "y2022": -0.07312494426840987,
  "y2020": -0.20227871854437118
 },
 "Equal-weight universe": {
  "cagr": 0.17598247531099576,
  "vol": 0.1668417487481744,
  "mdd": -0.23879737258733225,
  "p15": 0.5925925925925926,
  "p25": 0.24074074074074073,
  "p50": 0.046296296296296294,
  "ploss20": 0.0,
  "worst12": -0.11662038998170432,
  "y2022": -0.10522588378679132,
  "y2020": -0.23525368260441493
 },
 "S&P 500": {
  "cagr": 0.13863054069353442,
  "vol": 0.15375294491346947,
  "mdd": -0.24769522239058828,
  "p15": 0.48148148148148145,
  "p25": 0.19444444444444445,
  "p50": 0.009259259259259259,
  "ploss20": 0.0,
  "worst12": -0.1944282720342927,
  "y2022": -0.1944282720342927,
  "y2020": -0.1987059226914264
 }
}
```

### `port.json`
```json
{
 "haircut": 0.6,
 "exp_cal": 0.10358482434309348,
 "p20_cal": 0.2652154534541603,
 "pm20_cal": 0.012576526565416173,
 "pick": [
  "AIZ",
  "CAH",
  "HIG",
  "BKNG",
  "MA",
  "CL",
  "ADSK",
  "BMY",
  "MDT",
  "NVDA"
 ],
 "w": {
  "AIZ": 0.15,
  "CAH": 0.0862,
  "HIG": 0.1199,
  "BKNG": 0.1068,
  "MA": 0.1044,
  "CL": 0.1021,
  "ADSK": 0.0972,
  "BMY": 0.0667,
  "MDT": 0.1154,
  "NVDA": 0.0513
 },
 "exp": 0.1726413739051558,
 "vol": 0.14145485194664892,
 "mdd3y": -0.1234246285945364,
 "p20": 0.44466168143453,
 "pm20": 0.0031934065651873927,
 "bull": 0.3753306933099564,
 "bear": -0.1787163808249262,
 "fpe": 13.32385069567863,
 "conf": 62.662962766161954,
 "spx": {
  "vol": 0.12967614047744416,
  "mdd3y": -0.1890220618428401,
  "ret1y": 0.1606153136367825
 },
 "ret1y_hind": 0.056416691452730205,
 "sectors": {
  "Financials": 3,
  "Health Care": 3,
  "Consumer Discretionary": 1,
  "Consumer Staples": 1,
  "Information Technology": 2
 }
}
```


*End of handoff. Not financial advice.*
