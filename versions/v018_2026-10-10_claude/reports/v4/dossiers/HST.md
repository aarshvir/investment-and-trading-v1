# HST — Host Hotels & Resorts, Inc.

*Most recent period incorporated: Q2 2026 10-Q (period ended 2026-06-30, filed 2026-08-07) and the Q2 2026 earnings release (8-K Ex-99.1, filed 2026-08-05); checked SEC EDGAR (10-K/10-Q/8-K index) and FMP news for events to 2026-09-25. No 8-K or transcript dated after 2026-08-05 was found in the sources checked.*

*Basis: all figures are **consolidated** GAAP (Host Hotels & Resorts, Inc., the REIT parent, together with its operating partnership), USD, reported in millions except per-share amounts, as filed with the SEC. Non-GAAP figures (FFO, Adjusted FFO, EBITDAre, Adjusted EBITDAre) are the company's own NAREIT-based definitions and are labeled every time they appear.*

## 1. Verdict

**INCLUDE.** Thesis horizon **12–24 months** (shorter than the standard 12–36 because FY2027 comparisons look genuinely hard — see §3/§9). One-sentence reason: the operating business is in a real, primary-source-confirmed beat-and-raise cycle on the metrics that actually matter for a lodging REIT (comparable RevPAR and Adjusted FFO/share), the balance sheet was upgraded to Baa2 (Moody's) with no 2026 debt maturities, and the reverse-DCF shows the market is pricing in only ~1.7% annual FCF growth **[Corrected 2026-10-06: the 1.7% is V1's figure (WACC 9.27%, trailing capex of only $249m), mislabelled in §7 as WACC 7.5%; with actual capex (about $560-590m) and a 9.0% WACC (10-year Treasury 5.17%) the price implies about 3.4% a year on FY2026E free cash flow (1.3% on TTM), in line with a 2.5% base; verdict now INCLUDE-SMALL, see Re-assessment (RA12)]** — but the model's #1-of-503 ranking is partly an accounting artefact (see below) and the stock's own excellent 2026 comps (boosted by the FIFA World Cup) make 2027 a harder year to beat.

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

- **FCF conversion**: FY2025 OCF $1,607m vs GAAP net income $776m (OCF/NI 2.1x — high, typical for a REIT given large non-cash D&A of $795m); FCF (OCF − capex $617m) = $990m, FCF/NI 1.3x. **[Corrected 2026-10-06: $1,607m is the trailing-twelve-month figure to Q2 2026; FY2025 operating cash flow was $1,510m (10-K XBRL, accession 0001070750-26-000054), so FY2025 OCF/NI was 1.9x and FCF $893m (OCF less capex $617m), not $990m]** Sloan accrual ratio (ratios.py): **-6.7%**, well inside the healthy range — no accrual-based red flag.
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
| EV/EBITDA (FY2026 guided Adj. EBITDAre midpoint $1,785m) | 10.6x | `valuation.py`  **[Corrected 2026-10-06: the Q2 2026 release guides Adjusted EBITDAre of $1,820-1,840m (midpoint $1,830m); on EV $19.34bn this is 10.6x, unchanged]**|
| FCF yield | 6.4% | `valuation.py`, FY2025 FCF/market cap  **[Corrected 2026-10-06: FY2025 FCF was $893m, 5.8% of market cap; FY2026E free cash flow after SBC, one-offs and $590m capex is about $0.85bn (5.4% of equity value)]**|
| Dividend yield (regular only) | 3.6% | company rate $0.80/sh ÷ $22.42 |
| Reverse-DCF implied growth | **+1.7%/yr FCF growth for 10 years**, fading to 2.5% terminal | `valuation.py`, WACC 7.5% — a modest, unaggressive assumption embedded in the current price  **[Corrected 2026-10-06: WACC 7.5% is below the cost of capital implied by rf 5.17%; corrected implied growth about 3.4% (9.0% WACC, FCFF $1.09bn, EV $19.34bn), 1.3% on TTM FCFF, vs a 2.5% base: in_line, not 'modest' (RA12)]**|
| Probability-weighted scenario value | **$25.90/share (+15.4% vs price)** | Bear $20.50 (-8.6%, 30%) / Base $25.90 (+15.6%, 45%) / Bull $32.20 (+43.6%, 25%), AFFO-multiple based |

At ~10.4x FY2026 guided AFFO and 10.6x EV/EBITDA, HST trades **in line with its closest lodging-REIT peers, not at a premium** despite the #1 quant rank — a useful, direct rebuttal of a naive "priced for perfection" worry: Park Hotels & Resorts (PK, comparable luxury/upper-upscale portfolio) trades around 10.9x forward EV/EBITDA (having also just raised FY2026 AFFO guidance, to $1.90–2.00/share), and DiamondRock Hospitality (DRH, smaller-cap lodging REIT) trades around 10.2x estimated 2026 FFO with net debt/EBITDA of 3.1x — both sourced from news/secondary reporting (Seeking Alpha, Pluang), not independently verified against each peer's own primary filings this pass. Ryman Hospitality (RHP, high-end group/convention-focused) was not found with comparable data this pass and is left `not available` rather than estimated.

## 8. Bull case and bear case

**Bull (3 points, evidence-based)**
1. Four straight quarters of raised guidance on comparable RevPAR *and* AFFO/share (§5), with Q2 2026 RevPAR growth accelerating to +7.0% YoY, partly FIFA-World-Cup-driven but "broad-based" per management across hosting and non-hosting markets alike.
2. Investment-grade balance sheet strengthening, not weakening: Moody's upgrade to Baa2 (stable) in FY2025, no 2026 debt maturities, $3.6bn of liquidity, and disciplined capital recycling (selling lower-growth assets, e.g. two Four Seasons properties, at gains, into buybacks and a special dividend rather than empire-building).
3. Reverse-DCF shows only ~1.7% FCF growth priced in for a decade — a low bar relative to the actual RevPAR trajectory, leaving room for multiple expansion or continued beats without needing heroic assumptions. **[Corrected 2026-10-06: corrected to about 3.4% a year, which is at or above the 2.5% base once FIFA-flattered 2026 is excluded; this bull point does not hold as stated]**

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

---
## Re-assessment (RA12, 2026-10-06)

**Scope.** Valuation and recency re-test of INCLUDE (10-year Treasury 5.17% on 25 Sep 2026, FRED DGS10; Fed funds 3.75-4.00% after the 16 Sep 2026 hike). Price $22.42 (25 Sep 2026, d4 snapshot). Old verdict INCLUDE, dossier view "fair"; new verdict **INCLUDE-SMALL**, implied_vs_base **in_line**.

**Recency (EDGAR submissions CIK 0001070750, pulled 6 Oct 2026).** After the Q2 10-Q (7 Aug 2026, accession 0001070750-26-000126): Forms 4 on 21 and 25 Aug, Forms 144 on 19 and 21 Aug (routine insider notices), Schedule 13G/A 14 Aug (passive holder, accession 0001284812-26-000179). No 8-K after 5 Aug, no merger agreement, 13D, S-4, rating action or management change. Q3 results 4 Nov 2026.

**Guidance, quoted from the Q2 release (5 Aug 2026, accession 0001070750-26-000122).** "we are increasing our 2026 comparable hotel Total RevPAR and RevPAR growth guidance ranges to 4.75% to 5.25% over 2025"; Adjusted FFO per diluted share $2.15-2.18 (Adjusted FFO $1,480-1,498m on 688.6m diluted shares); Adjusted EBITDAre $1,820-1,840m; capital expenditures "approximately $550 million to $630 million"; "Assumes no additional dispositions and no acquisitions"; and "continued recovery at our Maui properties ... however the timing of Maui's full recovery remains uncertain". The release attributes part of the Q2 RevPAR gain to the World Cup.

**Claims checked.**
| Claim | Status | Source |
|---|---|---|
| FY2025 OCF $1,607m, FCF $990m | WRONG | $1,607m is TTM to Q2 2026 (FY25 $1,510m - H1-25 $749m + H1-26 $845m = $1,606m); FY25 OCF $1,510m; FCF $893m |
| Reverse DCF "+1.7%/yr at WACC 7.5%" | WRONG basis | V1's 1.75% used WACC 9.27% and trailing capex $249m (D3 field); actual capex: FY25 $617m cash ($644m spend), TTM about $562m, FY26 guide $550-630m |
| FY2026 Adj. EBITDAre midpoint $1,785m | STALE | Q2 release $1,820-1,840m |
| $0.72 special dividend paid 15 Jul; cash fell $630m | CONFIRMED | Q2 release; payable was inside accounts payable of $736m at 30 Jun |
| Total debt $5,082m, cash $1,953m, no 2026 maturities | CONFIRMED | 10-Q balance sheet; net debt after the July dividend $3.76bn |
| Condominium and insurance one-offs in AFFO | NOT IN DOSSIER | FY26 AFFO includes $16-20m condo contribution and $7m business-interruption gain; AFFO also adds back $26m stock compensation |

**Corrected reverse DCF.** Enterprise value = 685.0m shares x $22.42 = $15.36bn plus OP units (694.7m diluted shares: $15.58bn) + debt $5.08bn - cash $1.95bn + $0.63bn dividend payable = **$19.34bn**. Free cash flow to the firm (REIT, no tax shield):
- FY2026E: AFFO mid-point $1,489m - stock compensation $26m (a cost, not added back) - condo and insurance one-offs $25m - capex $590m + interest expense $241m = **$1,089m**.
- TTM: OCF $1,606m - capex $562m + cash interest $234m = $1,278m.
Discount rate: Ke = rf 5.17% + beta 1.10 (d4) x ERP 4.14% = 9.7%; marginal pre-tax debt cost 6.6%; weights 75/25 gives **WACC about 9.0%** (V1: 9.27%). 10 years constant growth then 3% terminal.
| WACC | 8.0% | 8.5% | 9.0% | 9.27% | 10.0% |
|---|---|---|---|---|---|
| Implied growth, FCFF $1,089m (FY26E) | 1.1% | 2.3% | **3.4%** | 4.0% | 5.6% |
| Implied growth, FCFF $1,278m (TTM) | -0.9% | 0.3% | 1.3% | 1.9% | 3.4% |
Base case (my assumption): **2.5%** a year (RevPAR +4.75-5.25% in 2026 includes World Cup demand; management says comparisons "are expected to moderate" and wage costs are rising; V1's 10-year FFO growth is 1.4%). Implied 3.4% versus base 2.5%: **in_line**. At 10.4x AFFO against peers at 10.95x (V2R), the stock is fairly valued with no margin of safety.

**Why INCLUDE-SMALL.** INCLUDE needs a margin of safety; the corrected method shows none (FCF yield 5.4-5.8%, implied growth at or above base, valuation at the 49th percentile of its own history). The beat-and-raise cycle, Baa2 rating and 2.95x net debt/EBITDA are real, but 2026 is flattered by a one-off event and the FY2027 test is open. No kill criterion has fired.

**Scenarios, 3-year annualised (new; V1 had bear -27.4%, base +6.2%, bull +49.3% on a mis-built FFO proxy; the dossier's $20.50 / $25.90 / $32.20 values were not annualised).** Own arithmetic from AFFO per share $2.165 (FY26 mid-point), regular dividend $0.80 a year, price $22.42. Bear: AFFO -5% a year (World Cup reversal, wage and Maui drag), exit 8.5x = $15.78 + $2.40 dividends = **-6.8%**. Base: AFFO +2%, exit 10.4x = $23.89 + $2.40 = **+5.5%**. Bull: AFFO +6%, exit 11.5x = $29.65 + $2.40 = **+12.7%**. Probability weights 30/45/25 give about +3.6% a year, below the earlier +15.4% (+11% over three years versus 15% in 12-24 months).

**Added kill criterion (6):** FY2027 Adjusted FFO per share guidance (about Feb 2027) below the FY2026 guide mid-point of $2.165.

**Effect.** F16 summary updated: verdict, thesis_one_line, kill_criteria, key_adverse_facts, data_conflicts, confidence_in_thesis, valuation_view_vs_v1.implied_vs_base and scenario_returns_3y. (`f5_summary.json` holds the older F5 HST entry and was left as published.) Analyst file `v4/outputs/ra12_reassess.json`.
