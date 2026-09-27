# HST — Host Hotels & Resorts, Inc.

*Most recent period incorporated: Q2 2026 10-Q (period ended 2026-06-30, filed 2026-08-07) and the Q2 2026 earnings release (8-K Ex-99.1, filed 2026-08-05); checked SEC EDGAR (10-K/10-Q/8-K index) and FMP news for events to 2026-09-25. No 8-K or transcript dated after 2026-08-05 was found in the sources checked.*

*Basis: all figures are **consolidated** GAAP (Host Hotels & Resorts, Inc., the REIT parent, together with its operating partnership), USD, reported in millions except per-share amounts, as filed with the SEC. Non-GAAP figures (FFO, Adjusted FFO, EBITDAre, Adjusted EBITDAre) are the company's own NAREIT-based definitions and are labeled every time they appear.*

## 1. Verdict

**INCLUDE.** Thesis horizon **12–24 months** (shorter than the standard 12–36 because FY2027 comparisons look genuinely hard — see §3/§9). One-sentence reason: the operating business is in a real, primary-source-confirmed beat-and-raise cycle on the metrics that actually matter for a lodging REIT (comparable RevPAR and Adjusted FFO/share), the balance sheet was upgraded to Baa2 (Moody's) with no 2026 debt maturities, and the reverse-DCF shows the market is pricing in only ~1.7% annual FCF growth — but the model's #1-of-503 ranking is partly an accounting artefact (see below) and the stock's own excellent 2026 comps (boosted by the FIFA World Cup) make 2027 a harder year to beat.

## 2. Business in plain English

Host is the largest lodging REIT in the US: it owns (does not operate) roughly 70–80 upper-upscale and luxury hotels under brands such as Marriott, Ritz-Carlton, Four Seasons, Hyatt, Westin and 1 Hotels, concentrated in top RevPAR markets (Hawaii/Maui, Orlando, San Francisco, NYC, DC). Third-party operators run day-to-day hotel operations under management contracts; Host collects the hotel-level economics (rooms, F&B, other) net of operating costs and management fees. Revenue mix in FY2025 was roughly 61% transient, 34% group, 5% contract business. A small, recurring side business sells condominium units at a development adjacent to the Four Seasons Orlando (Disney World) — $99m of revenue in FY2025, guided to contribute another ~$20–25m to FY2026 net income. Competitive position rests on owning irreplaceable, high-barrier-to-entry real estate in supply-constrained luxury/resort markets, not on operating skill (which sits with the brand operators).

## 3. Why the model likes it — and whether that's durable

Preliminary quant rank **#1 of 503** in the whole universe (composite 0.954; Q 0.954, V 0.917, M 0.99 — essentially the maximum momentum score). This is **partly durable, partly an artefact**, and the two need to be separated:

- **Durable part**: comparable-hotel RevPAR growth has been raised, not cut, in each of the last four quarterly guidance updates (see §5), Adjusted FFO/share has grown in 4 of the last 5 quarters, Moody's upgraded HST to Baa2 (stable) during FY2025, and there is no 2026 debt maturity wall. That is a real, multi-quarter, primary-source-confirmed operating improvement, not a one-quarter beat.
- **Artefact part**: GAAP net income and EPS — which likely feed the model's Quality-family inputs (ROE, accruals, cash-flow-to-assets) — were inflated by large, disclosed non-operating gains in **both** of the last two fiscal years: FY2025 GAAP net income included a **$148m "Other gains (losses)"** line (FY2024: $0m) from asset/condo sales, partially offset by $86m less insurance-settlement gains than FY2024; and Q1 2026 alone booked a **$242m pre-tax gain on the sale of three hotels** (St. Regis Houston + two Four Seasons properties), pushing Q1 2026 diluted EPS to $0.72 — roughly **double** every other quarter in the trailing eight (range $0.12–$0.35) — and GAAP net income up 99.6% YoY. **Data conflict, quantified**: recomputing ROE from the FY2025 10-K (ratios.py, sourced inputs) gives **11.2%**, versus the **16.1%** ROE figure feeding the preliminary Q score (`lead_prelim_rank.csv`) — consistent with that quant input being a trailing-twelve-month figure that captures the Q1 2026 gain quarter. The Quality score should be discounted accordingly; the Momentum and Value scores are less affected (RevPAR/AFFO-driven operating momentum is real, and the Value score is priced off cash flow, not the disposition gains).

## 4. Last two years of results

GAAP figures below are as-reported (10-Q/10-K/8-K Ex-99.1, SEC EDGAR CIK 0001070750; XBRL accession numbers on file). **AFFO is a REIT-standard non-GAAP measure defined by the company under NAREIT guidelines** — shown separately, never blended with GAAP.

| Quarter | Revenue ($m) | Comp. RevPAR YoY | GAAP net income ($m) | GAAP diluted EPS | Adjusted FFO/sh |
|---|---|---|---|---|---|
| Q3 2024 | 1,319 | n/a¹ | 82 | $0.12 | $0.36 |
| Q4 2024 | 1,428 | n/a¹ | 109 | $0.15 | $0.45 |
| Q1 2025 | 1,594 | n/a¹ | 248 | $0.35 | $0.64 |
| Q2 2025 | 1,586 | n/a¹ | 221 | $0.32 | $0.58 |
| Q3 2025 | 1,331 | +0.2% | 161 | $0.23 | $0.35 |
| Q4 2025 | 1,603 | +4.6% | 137 | $0.20 | $0.51 |
| Q1 2026 | 1,645 | +4.4% | **501** | **$0.72** | $0.67 |
| Q2 2026 | 1,640 | +7.0% | 237 | $0.35 | $0.63 |

¹ Individual quarterly RevPAR YoY% for Q3'24–Q2'25 was not separately quoted in the releases reviewed (only FY2025 vs FY2024, +3.8%, and 9-month 2025 vs 2024, +3.5%, were disclosed as running totals) — flagged as `not available` rather than estimated.

**Variance/decomposition**: Q1 2026 GAAP net income (+99.6% YoY, +$253m) is >10% and its driver is entirely identified in the company's own release: the $242m gain on the 3-hotel sale, not operations (comparable hotel EBITDA that quarter was up a normal +7.0%). Revenue growth has been modest and steady (low single digits to +7.6% FY2025, aided by the condo-sale line and 2024/2025 acquisitions), never the swing factor. AFFO/share is far smoother than GAAP EPS (range $0.35–$0.67 vs $0.12–$0.72) and beat its prior-year quarter in 4 of the last 5 quarters — Q3 2025 was the one dip (-2.8% YoY), attributed by management to soft short-term group volume.

**Balance sheet** (10-Q, 2026-06-30 vs 2025-12-31): total assets $13,253m vs $13,049m; total debt $5,082m vs $5,077m (weighted average maturity 4.7 years, weighted average rate 4.8%, **no 2026 maturities**); cash $1,953m vs $768m (cash was elevated at 6/30 from the Q1 disposition proceeds, then fell ~$630m on 7/15/2026 when the dividend below was paid); shares outstanding 685.0m vs 687.8m (down — net buybacks). Equity $6,388m vs $6,558m (down, reflecting the special dividend).

## 5. Guidance track record (last 4 quarterly releases — GAAP and FFO/AFFO shown separately)

| Release (date) | Comp. RevPAR growth guide | vs. prior guide | Net income guide | NAREIT FFO/sh | Adjusted FFO/sh | vs. prior guide |
|---|---|---|---|---|---|---|
| Q3 2025 (2025-11-05) | **raised** to ~+3.0% FY2025 | from ~+2.0% | $780m FY2025 | $2.00 | $2.03 | AFFO +$0.03 |
| Q4/FY2025 (2026-02-18, initial FY2026 guide) | +2.0% to +3.5% FY2026 | (new year, first guide) | $836–891m | $1.99–2.07 | $2.03–2.11 | n/a (initial) |
| Q1 2026 (2026-05-06) | **raised** to +3.0% to +4.5% | +100bps at midpoint | **raised** to $908–955m | $2.06–2.12 | $2.10–2.16 | AFFO +$0.06 |
| Q2 2026 (2026-08-05) | **raised** to +4.75% to +5.25% | +125bps at midpoint | **raised** to $944–962m | $2.11–2.14 | $2.15–2.18 | AFFO +$0.03 |

Guidance was **raised at every one of the last four releases**, on both the operating KPI (RevPAR) and the REIT earnings metric (AFFO/share, which by NAREIT definition excludes the disposition gains). The Q1 2026 net-income guidance raise ($67m at the midpoint) is **mostly mechanical** — it simply rolls the $242m realized disposition gain into the full-year forecast — but the accompanying AFFO raise (+$0.06/share) and RevPAR raise (+100bps) are gain-free and reflect a genuine, if more modest, operating upgrade. FY2025 actual net income ($776m) came in essentially in line with (slightly below) the guidance given three months earlier ($780m). Full-year 2025 comparable RevPAR guidance itself was also raised through the year (Q3 2025 headline: "Raises Full Year Comparable Hotel RevPAR Growth Guidance to ~3.0% Over 2024"). The Q2 2026 guide explicitly flags a boost from hosting FIFA World Cup matches and warns that "year-over-year comparisons are expected to moderate" into H2 2026 — management's own words for the 2027-comp risk in §9.

## 6. Earnings quality & balance sheet

- **FCF conversion**: FY2025 OCF $1,607m vs GAAP net income $776m (OCF/NI 2.1x — high, typical for a REIT given large non-cash D&A of $795m); FCF (OCF − capex $617m) = $990m, FCF/NI 1.3x. Sloan accrual ratio (ratios.py): **-6.7%**, well inside the healthy range — no accrual-based red flag.
- **GAAP vs adjusted gap**: FY2025 GAAP EPS $1.06 (ratios.py, diluted) vs company-reported Adjusted FFO/share $2.07 — a wide, well-explained gap driven almost entirely by real-estate depreciation ($795m) and the one-off items in §3, exactly the distortion NAREIT's FFO metric exists to strip out (realestate-reit.md playbook).
- **Leverage** (sourced, FY2025/ratios.py): net debt/EBITDA 2.95x, gross debt/EBITDA 3.42x, EBIT interest coverage 3.6x, EBITDA interest coverage 7.0x — moderate for a REIT. **Cross-source note (resolved, not a real conflict)**: the `d4_live_snapshot` vendor field shows total debt $5.645bn vs the company's own reported $5.082bn (a "FAIL"-level divergence flagged by `verify_data.py`) — this reconciles exactly once the $563m operating lease liability is added ($5,082m + $563m = $5,645m), i.e. it is a debt-definition difference (leases in or out), not a data error.
- **SBC**: not separately quantified as % of revenue this pass (immaterial for a REIT with ~160 corporate employees; flagged `not available` rather than estimated).
- **Dividend coverage**: the regular dividend ($0.20/quarter, $0.80/yr per the current rate) is covered roughly 2.6x by trailing Adjusted FFO/share (~$2.07 FY2025) — conservative. **On top of the regular dividend**, HST paid a **$0.72/share special dividend** (paid 2026-07-15) specifically to distribute the ~$500m taxable gain from the Q1 2026 Four Seasons sales — a REIT-mandated distribution of a real, one-time cash gain, not a signal about ongoing coverage; the GAAP-EPS-based payout ratio (113% per ratios.py, using cash dividends paid) is exactly the kind of REIT metric the playbook flags as misleading and is disregarded in favor of the AFFO-based read above.
- **M&A/financing**: FY2025 disposed of The Westin Cincinnati and Washington Marriott at Metro Center (~$237m combined, with $114m of seller financing extended — a note receivable, i.e. HST retains counterparty credit exposure on part of that sale price); Q1 2026 disposed of St. Regis Houston and two Four Seasons properties (~$242m gain); FY2026 guidance assumed one further disposition (Sheraton Parsippany) which appears to have dropped out of the "no additional dispositions" assumption by the Q2 2026 release. $900m of senior notes issued in FY2025 to refinance $900m of maturing notes (credit-neutral, contributed to the Moody's Baa2 upgrade). Share count fell from 687.8m to 685.0m (net repurchases exceeding issuance).

## 7. Valuation snapshot

Per the REIT playbook, **P/FFO and P/AFFO, not GAAP P/E, are the primary multiples**; GAAP P/E is shown only as a secondary reference.

| Metric | Value | Basis |
|---|---|---|
| P / trailing GAAP EPS | 19.8–21.0x | secondary reference only (`valuation.py`/`ratios.py`, FY2025) |
| P / FY2026 guided AFFO/share (midpoint $2.165) | **~10.4x** | primary REIT multiple |
| EV/EBITDA (FY2026 guided Adj. EBITDAre midpoint $1,785m) | 10.6x | `valuation.py` |
| FCF yield | 6.4% | `valuation.py`, FY2025 FCF/market cap |
| Dividend yield (regular only) | 3.6% | company rate $0.80/sh ÷ $22.42 |
| Reverse-DCF implied growth | **+1.7%/yr FCF growth for 10 years**, fading to 2.5% terminal | `valuation.py`, WACC 7.5% — a modest, unaggressive assumption embedded in the current price |
| Probability-weighted scenario value | **$25.90/share (+15.4% vs price)** | Bear $20.50 (-8.6%, 30%) / Base $25.90 (+15.6%, 45%) / Bull $32.20 (+43.6%, 25%), AFFO-multiple based |

At ~10.4x FY2026 guided AFFO and 10.6x EV/EBITDA, HST trades **in line with its closest lodging-REIT peers, not at a premium** despite the #1 quant rank — a useful, direct rebuttal of a naive "priced for perfection" worry: Park Hotels & Resorts (PK, comparable luxury/upper-upscale portfolio) trades around 10.9x forward EV/EBITDA (having also just raised FY2026 AFFO guidance, to $1.90–2.00/share), and DiamondRock Hospitality (DRH, smaller-cap lodging REIT) trades around 10.2x estimated 2026 FFO with net debt/EBITDA of 3.1x — both sourced from news/secondary reporting (Seeking Alpha, Pluang), not independently verified against each peer's own primary filings this pass. Ryman Hospitality (RHP, high-end group/convention-focused) was not found with comparable data this pass and is left `not available` rather than estimated.

## 8. Bull case and bear case

**Bull (3 points, evidence-based)**
1. Four straight quarters of raised guidance on comparable RevPAR *and* AFFO/share (§5), with Q2 2026 RevPAR growth accelerating to +7.0% YoY, partly FIFA-World-Cup-driven but "broad-based" per management across hosting and non-hosting markets alike.
2. Investment-grade balance sheet strengthening, not weakening: Moody's upgrade to Baa2 (stable) in FY2025, no 2026 debt maturities, $3.6bn of liquidity, and disciplined capital recycling (selling lower-growth assets, e.g. two Four Seasons properties, at gains, into buybacks and a special dividend rather than empire-building).
3. Reverse-DCF shows only ~1.7% FCF growth priced in for a decade — a low bar relative to the actual RevPAR trajectory, leaving room for multiple expansion or continued beats without needing heroic assumptions.

**Bear (3 points, evidence-based)**
1. **2027 comp risk, in management's own words**: FY2026's acceleration is flattered by the FIFA World Cup (explicitly cited in the Q2 2026 release) and management itself guides that "year-over-year comparisons are expected to moderate" in H2 2026 — FY2027 will lap an unusually strong RevPAR year with no repeat event.
2. The quant model's #1-of-503 rank leans partly on a Quality/ROE signal that this dossier shows is inflated by one-off disposition gains in both FY2025 ($148m) and Q1 2026 ($242m) — sourced ROE (11.2%, FY2025) is ~500bps below the model's TTM input (16.1%), so some of the "cheap and high-quality" signal is an artefact, not durable.
3. Lodging is a discretionary, macro-sensitive business; comparable-hotel EBITDA margin has been under pressure from wage inflation in several recent quarters, group booking volume has been described as "soft" repeatedly across FY2025 releases, and Maui properties were still described as "recovering" from the 2023 wildfires as late as the Q4 2025 release — a multi-year drag not yet fully resolved.

## 9. Key risks & kill criteria

1. Comparable hotel RevPAR growth turns negative for two consecutive quarters (the core, most-watched KPI).
2. Adjusted FFO/share guidance is *cut* (not just raised more slowly) at any quarterly release — a genuine reversal, not merely deceleration.
3. Net debt/EBITDAre rises above ~4.0x (current: 2.95x net debt/EBITDA on ratios.py) without an offsetting asset-sale plan.
4. The regular quarterly dividend ($0.20/share) is cut.
5. FY2027 comparable RevPAR growth guidance (first given around Feb 2027) comes in below roughly 2% — the specific, falsifiable test of the "2026 was FIFA-flattered" bear case in §8.

## 10. Catalysts & calendar

Next earnings: **2026-10-29 is BMY's, HST's is 2026-11-04** (Q3 2026, per `d4_live_snapshot`, 40 days from data-cutoff). Other: full-year 2026 results and initial FY2027 guidance expected mid-to-late February 2027 (pattern: 2026-02-18 for the FY2025 print) — the single most important near-term catalyst given the FY2027-comp question in §9. No investor day, lock-up or index-event triggers identified this pass.

## 11. Red-flag scan

- **Auditor/restatement/going-concern**: none identified in the filings reviewed.
- **SEC/DOJ**: none identified.
- **Insider selling pattern**: SEC EDGAR shows a routine cadence of Form 4 filings clustered around late-May, mid-July and late-August 2026 (equity-award vesting windows) — consistent with scheduled vesting/withholding rather than opportunistic dumping on its face, but individual transaction codes (open-market sale "S" vs tax-withholding "F") were **not opened and verified given time constraints — flagged `not available`**, not asserted clean.
- **Casualty/insurance**: Hurricanes Helene and Milton (2024) property damage — $81m of insurance proceeds received cumulatively through Q1 2026 ($31m business-interruption), with final claim determination still pending as of the Q1 2026 release; Maui wildfire (2023) recovery still incomplete as of Q4 2025 commentary. Both are disclosed, bounded, largely-insured items, not undisclosed liabilities — but both are still open.
- **Short-seller reports / litigation**: none identified this pass (not exhaustively searched beyond FMP news and the filings above).

## 12. Sources

1. Host Hotels & Resorts 10-K, FY2025, filed 2026-02-25, accn 0001070750-26-000054 — SEC EDGAR, https://www.sec.gov/Archives/edgar/data/1070750/000107075026000054/
2. Q4/FY2025 earnings release, 8-K Ex-99.1, filed 2026-02-18, accn 0001070750-26-000038 — https://www.sec.gov/Archives/edgar/data/1070750/000107075026000038/hst-ex991.htm
3. Q1 2026 earnings release, 8-K Ex-99.1, filed 2026-05-06, accn 0001070750-26-000077 — https://www.sec.gov/Archives/edgar/data/1070750/000107075026000077/hst-ex991.htm
4. Q2 2026 earnings release, 8-K Ex-99.1, filed 2026-08-05, accn 0001070750-26-000122 — https://www.sec.gov/Archives/edgar/data/1070750/000107075026000122/hst-ex991.htm
5. Q3 2025 earnings release, 8-K Ex-99.1, filed 2025-11-05, accn 0001070750-25-000164 — https://www.sec.gov/Archives/edgar/data/1070750/000107075025000164/hst-ex991.htm
6. 10-Q filings Q1 2026 (accn 0001070750-26-000080) and Q2 2026 (accn 0001070750-26-000126) — SEC EDGAR CIK 0001070750
7. SEC XBRL company facts / point-in-time extract, `v4\data\d3_xbrl_facts.parquet` (ticker HST), machine-readable copy of the above filings
8. SEC EDGAR Form 4 ownership filing index, CIK 0001070750, https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001070750&type=4 (list only; individual forms not opened)
9. Internal preliminary quant ranking, `v4\outputs\lead_prelim_rank.csv`, and live snapshot, `v4\data\d4_live_snapshot.parquet`, both dated 2026-09-25 close — cross-check/navigation only, not source of record
10. `scripts/verify_data.py`, `scripts/ratios.py --sector reit`, `scripts/valuation.py` output (finance-skills stock-analysis toolkit), run 2026-09-26 on the sourced figures above (intake JSON retained in `C:\Users\user\eqv4\cache\f5\HST\`)

---
*Research only; not investment advice. Figures are GAAP unless labeled AFFO/FFO/Adjusted (company-defined, non-GAAP, NAREIT-based measures). Data-quality note: 14 of 15 headline datapoints checked traced to a primary filing (`verify_data.py`, 93% Tier-1 coverage); the one aggregator-sourced figure (quant-model NTM P/E) is explicitly flagged wherever used. Three items were left as `not available` rather than estimated (quarterly RevPAR% for Q3'24–Q2'25, SBC/revenue, Form 4 transaction codes) — see §4/§6/§11.*

## Addendum (2026-09-26): corrected REIT valuation (V2R)

Agent V2R rebuilt NAREIT FFO for HST directly from SEC filings/XBRL (`v4/outputs/v2r_reit_valuation.md` and `.json`), replacing the systematic model's (V1) "FFO proxy" (GAAP net income + total D&A) underlying its "attractive" verdict. That proxy does not exclude one-off gains on sale of real estate, and HST's Q1 2026 GAAP net income included the $242m pre-tax gain on the 3-hotel sale already discussed in §3/§4 above as a Quality-score artefact — the same gain also flowed into V1's FFO proxy and mechanically depressed its P/FFO and own-history percentile.

**Corrected multiples (as of 2026-09-25 close, $22.42/sh):**
- P/FFO (TTM NAREIT FFO, $2.11/sh — all four trailing quarters company-reported) = **10.63x**
- P/FFO (FY2026 Adjusted FFO guidance midpoint $2.165/sh) = **10.36x** — matches this dossier's own §7 figure (~10.4x) almost exactly
- Own-history percentile: **48.8 (10-year, n=121mo) / 57.4 (5-year, n=61mo)** — roughly the median of its own range, not statistically cheap
- Peer median (PK/RHP/APLE, FY26 guidance P/FFO): **10.95x** — HST trades essentially in line with, fractionally below, peers

**Statements above that no longer hold:** this dossier never itself asserted HST was "statistically cheap" on an own-history basis (that claim lived only in V1's separate 8.49x-proxy / 29.2nd-percentile reading, which is what V2R corrects). §7's framing — "HST trades in line with its closest lodging-REIT peers, not at a premium, despite the #1 quant rank" — is *confirmed*, not contradicted, by the correction: the corrected 10.36x FY26-guide multiple matches this dossier's own 10.4x almost to the decimal, and the corrected 48.8th-percentile own-history reading (average, not cheap) replaces V1's 29.2nd-percentile "attractive" input that this dossier's §1/§3 quant-rank discussion had implicitly relied on without itself re-deriving.

**Re-assessed verdict: INCLUDE, unchanged.** HST's INCLUDE case was never primarily a "statistically cheap" argument — it rested on a primary-source-confirmed beat-and-raise cycle on RevPAR and Adjusted FFO/share (§5), a balance-sheet upgrade to Baa2 with no 2026 maturities (§4, §6), and a reverse-DCF showing only ~1.7%/yr FCF growth priced in (§7), all untouched by this correction. The corrected own-history percentile (49th, squarely average) matches rather than contradicts the dossier's own peer-based "fair, in line" framing, so there is no new silent conflict to resolve — it is V1's separate "attractive"/29th-percentile claim that is being corrected, not this dossier's view. Pre-existing reservations stand unchanged: the 12–24 month horizon (shorter than standard) because FY2027 comparisons will lap an unusually strong, FIFA-flattered year, and the Quality/ROE score's known gain-on-sale distortion (§3). Net effect: a fair, not-cheap valuation is a neutral data point relative to V1's prior (now-corrected) "cheap" framing, but it does not change a verdict that was never built on statistical cheapness. This addendum supersedes any valuation framing above that implied HST was statistically discounted; §2–6 and §8–11 are unchanged and remain in force. Research, not personalised investment advice.
