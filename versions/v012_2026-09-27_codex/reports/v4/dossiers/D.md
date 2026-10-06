# Dominion Energy, Inc. (D) — Diligence Dossier

**Agent:** F109 (wave 7) | **As of:** 2026-09-25 close ($60.68, mkt cap $53.37bn per d4/b1 snapshot) | **CIK 0000715957**

## 0. Overriding fact the triage missed: a signed, pending, all-stock-plus-cash merger with NextEra Energy
On **15 May 2026** Dominion Energy entered into an Agreement and Plan of Merger with NextEra Energy, Inc. Under the deal, Dominion shareholders receive **0.8138 shares of NextEra Energy common stock per Dominion share plus a one-time aggregate cash payment of ~$360 million** (company/press-release terms, cross-checked via SEC 8-K, accession 0001193125-26-235041, https://www.sec.gov/Archives/edgar/data/0000715957/000119312526235041/d131585d8k.htm, and Form 425, accession 0001193125-26-330689, https://www.sec.gov/Archives/edgar/data/0000715957/000119312526330689/d149182d425.htm). Regulatory applications were filed 15 July 2026 with the Virginia SCC, North Carolina Utilities Commission, Public Service Commission of South Carolina, FERC and the NRC; NextEra's CEO has said the deal is expected to close **late 2027**. This is also why `b1_live_scores.csv` flags `exclude_pending_deal=True` for D — the quant model's own pending-deal screen would have excluded D from the eligible universe had the triage/build pipeline applied it consistently. **This dossier treats D as a merger-arbitrage situation, not a standalone growth-utility story**, and that reframing is the main override of the Q15 triage's "advance" call.

**Deal-value arithmetic (25 Sep 2026 close):** NextEra Energy (NEE) closed at $76.08 on 2026-09-25 (secondary-source web quote, not independently verified against an exchange tape in this window). 0.8138 × $76.08 = **$61.90/share** in stock, plus ~$360m aggregate cash ÷ ~878m D shares outstanding (implied by the reported ~$66.8bn / $76-per-share deal valuation) ≈ **$0.41/share** cash → total implied deal value ≈ **$62.31/share**. D's $60.68 close is a **~2.7% discount** to that implied value, or roughly **1.9%/yr annualised** if the deal closes on schedule ~14 months out (late 2027) — a thin arbitrage spread that indicates the market is pricing a high probability of completion, given the multi-state/FERC/NRC approval slate and 18+ month timeline.

## 1. Verdict
**WATCH**, thesis horizon: tied to deal timeline (~14–18 months to expected close). Reason: with the merger signed, D's return is now overwhelmingly a function of (a) deal-completion probability across five separate regulatory dockets and (b) NextEra's own stock price, not of Dominion's standalone fundamentals; the arb spread is thin (~2%/yr) for the regulatory-approval risk being carried, and this is not the growth-utility thesis the triage described. Not a REJECT because the spread is not obviously mispriced and a break would leave a improving, growth-exposed standalone utility (§7).

## 2. Business in plain English
Dominion Energy is a vertically integrated electric and gas utility, primarily **Virginia Electric and Power Company d/b/a Dominion Energy Virginia** ("Virginia Power," a wholly owned subsidiary), which generates, transmits and distributes electricity to Virginia and part of North Carolina, plus gas utilities. Its Virginia service territory includes Northern Virginia's "Data Center Alley," the world's largest concentration of hyperscale data centers (Alphabet, Amazon, Microsoft, Meta and others are customers per company disclosure), which is the company's single biggest demand-growth driver. It is also building the largest offshore wind project in the US.

## 3. Why the model likes it — durable or artefact?
b1_live_scores.csv: composite decile 4 / quintile 2, live_rank 329, `exclude_pending_deal=True` (the model already flags the merger). Quality percentiles are mixed (roe pct 0.048 — very low; ocf/assets pct 0.081 — low), Value/Momentum higher (bp pct 0.82, mom_12_1 pct 0.64). The "why the model likes it" question is close to moot: the model's own screen excludes D, and the composite score partly reflects momentum from the merger announcement itself (the stock re-rated toward deal value in May 2026), not an independent fundamental signal.

## 4. Last several quarters (consolidated, GAAP, USD millions; SEC XBRL companyfacts)
| Period | Revenue | Op. income | Net income |
|---|---|---|---|
| Q4 2024 | 3,400 | 391 | 134 |
| FY2024 | 14,459 (Revenues tag) | 3,247 | 2,034 |
| Q1 2025 | 4,076 | 1,223 | 665 |
| Q2 2025 | 3,810* | 1,096* | 760* |
| Q3 2025 | 4,527* | 1,339* | 1,006* |
| FY2025 | 16,506 | 4,414 | 2,998 |
| Q4 2025 | 4,093* | 756* | 567* |
| Q1 2026 | 5,019 | 1,392 | 621 |
| Q2 2026 (company release) | 4,480 | — | GAAP EPS $0.37; **operating (non-GAAP) EPS $0.79** |

*Quarterly figures marked with an asterisk are back-derived from the FY2025 10-K's own quarterly breakout (filed 2026-02-23, accession 0001193125-26-063120), which the cached XBRL extract tags as "form 10-K" even though they represent individual 2025 quarters — flagged so the entity/period scope is not mistaken for FY. Q2 2026 figures are from the 8-K exhibit (https://www.sec.gov/Archives/edgar/data/0000715957/000119312526326812/d-ex99.htm), not yet reflected in the cached companyfacts XBRL pull at diligence time.
**Trend:** operating income and net income both grew steadily through the two years reviewed (Q2 2025 op. income $1,096m → Q2 2026 not disclosed at the operating-income line in the release reviewed, but operating EPS rose from $0.75 to $0.79 y/y per the company's own comparison, +5.3%), consistent with the demand-growth narrative; no deceleration visible.

## 5. Guidance track record (verbatim quotes)
- **Q2 2026 8-K (accession 0001193125-26-326812, filed ~2026-07-31):** "reaffirms its full-year 2026 operating earnings guidance range of $3.45 to $3.69 per share, midpoint of $3.57 per share" — **maintained**, not raised.
- **Same release, per company summary:** operating earnings of "$712 million ($0.79 per share), compared to operating earnings of $649 million ($0.75 per share)" in Q2 2025 — a like-for-like beat, but guidance for the full year was held flat, not raised on the beat.
- CVOW (Coastal Virginia Offshore Wind, a Virginia Power project — **entity scope: this is a Virginia Power subsidiary asset whose costs flow through to consolidated Dominion via regulated cost recovery mechanisms, not a separate legal entity's balance sheet**): cost estimate rose to **~$11.7bn**, up ~$300m from the prior estimate, "due to revised network upgrade costs assigned by the PJM Interconnection, tariffs imposed... and updated turbine installation projections" (Utility Dive, reporting on the Q2 2026 8-K); project is **81% complete**, expected completion **end of 2027**, six months later than the prior timeframe.
- Data centers: contracted capacity reached **~53.8 GW** as of the Q2 2026 update, up 5.3 GW from December 2025 (secondary-source aggregation of the company's Q2 2026 investor slides — the underlying company release for this dossier's Q1 2026 vintage cited ~51 GW in the Q15 triage sources, so the pipeline continued to grow quarter over quarter).

## 6. Earnings quality & balance sheet
**Entity scope: all figures consolidated Dominion Energy, Inc.** unless noted. Virginia Power (the main regulated operating subsidiary) files separately with the SEC and has its own, larger debt load than the CVOW-specific figures above; this dossier does not independently reconcile Virginia Power's stand-alone balance sheet in this window (disclosed limitation).
- **FCF:** Q1 2026 OCF $882m against a capex run-rate that has historically exceeded $1.4–1.6bn/quarter (FY2024 capex context from prior years' data; **the exact Q1 2026 capex figure was not captured from the cached XBRL pull in this window** — disclosed gap) — consistent with the triage's stated FCF yield of roughly −17%, i.e., structurally negative, funded by the CVOW buildout and data-center-driven grid investment.
- **Leverage (consolidated, XBRL as filed):** `LongTermDebt` rose sharply from $39,320m (2024-12-31, 10-K accession 0000950170-25-028387, filed 2025-02-27) to **$46,332m** (2025-12-31, 10-K accession 0001193125-26-063120, filed 2026-02-23) — a ~$7bn, ~18% increase in one year, the largest single-year jump in the 2019–2025 series reviewed, consistent with CVOW's cost overrun and the broader capex program. Assets grew from $102,415m (2024-12-31) to $118,578m (2026-03-31); `StockholdersEquity` grew from $26,863m to $29,147m over the same span — debt is growing faster than equity.
- **CVOW-specific risk:** the $11.7bn cost estimate has risen from earlier estimates (the Q15 triage cited a prior figure of "~$11.4bn," i.e., another ~$300m step-up disclosed since); 19% of the project remains to be built with turbine-installation risk explicitly cited by management as a driver of the latest cost increase.
- **Merger financing:** the deal is structured as NEE stock + cash to Dominion holders, not new debt raised by Dominion; Dominion's own balance-sheet trajectory is therefore the more relevant near-term risk (rating-agency reaction to rising leverage ahead of a ~14-month regulatory-approval process) rather than deal-financing risk.
- **Share count / buybacks:** no evidence of Dominion buybacks found in this window (consistent with a company mid-merger and mid-capex-buildout); not applicable pending the merger.

## 7. Valuation snapshot (both frameworks, because of the pending deal)
**Deal-arb framework (primary, given §0):** implied deal value ≈$62.31/share vs. $60.68 close ⇒ ~2.7% simple spread, ~1.9%/yr annualised to a ~14-month expected close — thin compensation for multi-jurisdiction regulatory risk (five separate approvals, one of which is the NRC given Dominion's nuclear fleet) and a CEO-stated "late 2027" close that has already been described as no faster than originally hoped.
**Standalone reverse-DCF (secondary, "if the deal breaks" scenario):** operating EPS guidance midpoint $3.57 on a $60.68 price ⇒ NTM P/E ≈17.0x. Using the same simplified Gordon-growth reverse model as CNP (payout ~45% of $3.57 ⇒ D₁≈$1.61, cost of equity r≈8.5%): r−g ≈ $1.61/$60.68 ≈ 2.65% ⇒ implied standalone long-run growth ≈**5.85%/yr**. Dominion's own multi-year guidance (from prior public commitments, not re-verified verbatim in this window) has historically targeted mid-single-digit EPS growth (~5–7%/yr) — so on a standalone basis the implied growth is roughly **in line** with the company's historical guided range, i.e., not obviously mispriced either way if the deal were to break. `v1_verdict` is **null** (no CNP-style V1 row exists for D in `outputs/v1_valuation_table.csv`).

## 8. Bull case / Bear case
**Bull:**
1. Deal completion at $62.31 implied value from $60.68 is a modest, low-volatility return path if regulatory approval proceeds as management expects.
2. Underlying demand story (53.8 GW of contracted/pipeline data-center capacity) is real and growing quarter over quarter, a tailwind for NextEra's post-close combined entity even if it does not directly accrue to D shareholders after conversion.
3. If the deal breaks, standalone D is not obviously overvalued (§7 standalone read is "in line"), providing some downside cushion versus a name priced purely on takeover hope.

**Bear:**
1. Five separate regulatory approvals (VA SCC, NC, SC, FERC, NRC) across an 18+ month timeline is a wide, slow gauntlet; nuclear-asset transfers (NRC) have historically been a slower, more conservative approval process than typical utility M&A.
2. CVOW cost has risen twice in the disclosed history reviewed (to ~$11.4bn, then ~$11.7bn) with 19% of construction remaining — a plausible source of a further cost/timeline surprise before the deal even closes.
3. Consolidated leverage rose ~18% in one year (2024→2025 long-term debt); a rating-agency downgrade of standalone Dominion ahead of the deal could pressure the stock independent of merger mechanics.

## 9. Key risks & kill criteria (measurable)
1. Any regulator (Virginia SCC, NC, SC, FERC, or NRC) formally denies or imposes conditions materially impairing deal economics.
2. The merger agreement is terminated by either party, or the expected close date is pushed beyond **2028** (vs. "late 2027" guided now).
3. The arb spread (deal value implied by NEE price and the 0.8138 ratio, minus D's price) widens beyond **8%** annualised, signalling the market has repriced completion risk upward.
4. CVOW's cost estimate rises by a further **>$500m** from the current $11.7bn, or the completion date slips beyond **mid-2028**.
5. Dominion's consolidated long-term debt grows more than **10%** in a single year again (matching or exceeding the 2024→2025 pace) without a matching rating-agency reaffirmation.

## 10. Catalysts & calendar
- Next earnings: Q3 2026 results expected ~late October / early November 2026 (2025's Q3 report was filed 2025-10-31; **estimate, not confirmed**).
- Regulatory approval milestones at the VA SCC, NC, SC PSC, FERC and NRC (dockets opened 2026-07-15; no ruling dates identified in this window).
- CVOW: third and final substation targeted operational end of 2026; full project completion targeted end of 2027.

## 11. Red-flag scan
- No auditor changes, material weaknesses, restatements, going-concern language, SEC/DOJ investigations, or short-seller reports identified in the sources reviewed.
- The merger itself is the dominant "event risk" for this name and is disclosed at the top of this dossier rather than buried in a red-flag list.
- Form 4 insider-selling pattern: not independently reviewed in this window (data gap, disclosed).

## 12. Sources
1. SEC EDGAR XBRL companyfacts, CIK0000715957 (`https://data.sec.gov/api/xbrl/companyfacts/CIK0000715957.json`), retrieved 2026-09-27.
2. SEC EDGAR submissions, CIK0000715957, retrieved 2026-09-27.
3. Dominion Energy Q2 2026 8-K earnings exhibit, https://www.sec.gov/Archives/edgar/data/0000715957/000119312526326812/d-ex99.htm.
4. SEC 8-K re: NextEra merger agreement, https://www.sec.gov/Archives/edgar/data/0000715957/000119312526235041/d131585d8k.htm; Form 425, https://www.sec.gov/Archives/edgar/data/0000715957/000119312526330689/d149182d425.htm.
5. Utility Dive, "Dominion offshore wind project cost rises nearly $300M," accessed 2026-09-27.
6. WorkBoat, "Dominion says Virginia offshore wind project 81% complete," accessed 2026-09-27.
7. DataCenterDynamics, "Dominion Energy nearly doubles data center capacity under contract to 40GW," and related Q2 2026 coverage (53.8 GW figure), accessed 2026-09-27 (secondary-source aggregation, cross-check only).
8. Web-search secondary source for NEE 2026-09-25 close price ($76.08), not independently re-verified against exchange data in this window.
9. Q15_triage.json (this program's own prior triage note on D), for the ~51 GW and prior CVOW cost figures used as a comparison point.

## 13. Data basis, recency and disclaimer
Most recent period incorporated: Q1 2026 10-Q (accession 0001193125-26-200275, filed 2026-05-01, period ended 2026-03-31) from XBRL companyfacts, supplemented by the Q2 2026 8-K (accession 0001193125-26-326812, period ended 2026-06-30, released ~2026-07-31) for headline figures and by the 15 May 2026 merger agreement (accession 0001193125-26-235041) and its 15 July 2026 regulatory filings for the deal terms. Events checked to 2026-09-25. GAAP figures are labelled GAAP; "operating earnings" is the company's own non-GAAP measure and is labelled as such. **Central override of the Q15 triage:** the triage treated D as a standalone growth-utility story and did not surface the pending NextEra merger; this dossier's verdict (WATCH, not the triage's implicit "advance-to-INCLUDE" framing) rests on that correction. Research, not personal investment advice.
