# T-Mobile US, Inc. (NASDAQ: TMUS) — Fundamental Diligence Dossier

**Prepared by:** F48 (fundamental diligence analyst, wave 2) | **Data cutoff:** 2026-09-25 close | **Most recent period incorporated:** Q2 2026 10-Q (filed 2026-07-23, period ended 2026-06-30). Checked for events to 2026-09-25 (an 8-K dated 2026-09-01/filed 2026-09-03 was reviewed by index only — routine debt-related filing, not an earnings event). Next scheduled report: ~2026-10-22/23 (based on the 2025-10-23 Q3 reporting date). **Basis:** consolidated GAAP figures are labeled "GAAP"; Core Adjusted EBITDA and Adjusted Free Cash Flow are T-Mobile's own defined non-GAAP measures and are labeled at every use — never blended into a GAAP line. **Scorecard gates:** not applicable — this dossier does not use a disqualifying-gate checklist; the quant composite cited in §3 is context, not a pass/fail gate.

**Data-quality note:** every figure is sourced to SEC EDGAR primary filings (10-Q/10-K, 8-K Ex-99.1 earnings releases) or SEC XBRL company facts, each cited in §12. Quant context is from `v4/data/b1_live_scores.csv`. **No V1 valuation row exists for TMUS** in `v4/outputs/v1_valuation_table.csv` or `v1_valuation.json` — per program instructions, `v1_verdict` is set to null rather than fabricated; §7 below is this dossier's own valuation read only. Research output for internal process use, not personalized investment advice.

## 1. Verdict: INCLUDE-SMALL (half weight) — thesis horizon 12–36 months
T-Mobile is compounding Core Adjusted EBITDA and Adjusted Free Cash Flow at double digits, has raised guidance (not just met it) at multiple releases in the trailing year, and is returning capital aggressively (share count down ~4% in two quarters). The named reservation: **postpaid net-account growth has decelerated for essentially every recent quarter on a year-over-year basis** (396k in Q3'25, +26% YoY → 261k Q4'25 → 217k Q1'26, +6% YoY → 277k Q2'26, **−13% YoY**) even as revenue and EBITDA keep growing, and net debt is large (~$80bn) and still being used to fund heavy buybacks. The core "best network, best value" moat is real and primary-source-evidenced, but the deceleration in the volume metric that most directly reflects new-customer competitiveness, plus the leverage load, argue for a smaller position rather than a full-conviction one.

## 2. Business in plain English
T-Mobile is the second-largest US wireless carrier, selling postpaid and prepaid mobile phone service, fixed-wireless home internet/broadband, and (via joint ventures) fiber broadband, to consumers and businesses. It makes money on monthly service revenue per account/line, and its competitive position rests on having built out the largest contiguous 5G network (using mid-band spectrum acquired via the Sprint merger) faster than AT&T or Verizon, which it has converted into genuine customer-growth and churn advantages ("best network, best value, best experiences," per every release reviewed) — now expanding into fixed-wireless and fiber (via the Metronet/Lumos joint ventures) and absorbing UScellular's spectrum and customer base via a 2025–26 acquisition.

## 3. Why the model likes it — durable or artefact?
Quant snapshot (`b1_live_scores.csv`, as of 2026-09-25): composite 0.823 (decile 9, live_rank 88/503). Family scores: Q 0.866, V 0.765, M 0.249, S 0.638. ROE 18.8%, gross-profit/assets 14.1%, earnings yield 6.0%, FCF/price 10.4%, 12-1 month momentum **−23.0%** (the stock is down ~23% over the trailing year, per triage), SUE 0.26.
- **Quality (87th pctile) and Value (76th pctile) are corroborated by primary sources:** ROE, FCF yield and the guide-raise pattern in §5 are all real and filed. The 10.4% FCF/price is consistent with the company's own FY2026 Adjusted FCF guidance ($18.4–18.8bn midpoint $18.6bn) against the ~$177.5bn market cap in `b1_live_scores.csv` (≈10.5%) — internally consistent.
- **Momentum (25th pctile) is the interesting one to unpack, and it is *not* simply "the market is wrong."** The stock's 23% pullback coincides with a real, filed deceleration in postpaid net-account growth (see verdict) even as headline service-revenue growth stays "industry-leading" (9–11% YoY every quarter shown) — i.e., the market may be pricing a genuine volume-growth slowdown that the revenue/EBITDA lines partly mask via ARPA (average-revenue-per-account) gains and cost discipline. This is a case where the momentum signal and an adverse fact plausibly agree, rather than one being an artefact of the other.
- **Earnings-surprise (64th pctile)** is unremarkable — consistent with a company that guides conservatively and then raises (§5), rather than one that manages to a beat-the-Street number.

## 4. Last 8 quarters (GAAP unless noted; primary-sourced to 10-Q/10-K XBRL and Ex-99.1 releases, §12 #2–#5)
| Quarter | Service revenue ($B) | YoY growth | Postpaid net account adds (000s) | YoY chg. | GAAP net income ($B) | GAAP diluted EPS | Core Adj. EBITDA ($B) | Adj. FCF ($B) |
|---|---|---|---|---|---|---|---|---|
| Q3 2025 | 18.2 | +9% | 396 | +26% | 2.7 | $2.41 | 8.7 | 4.8 |
| Q4 2025 | 18.7 | n/a¹ | 261 | n/a¹ | 2.1 | $1.88 | 8.4 | 4.2 |
| FY2025 | 71.3 | — | 1,200 (full yr) | — | 11.0 | $9.72 | 33.9 | 18.0 |
| Q1 2026 | 18.8 | +11% | 217 | +6% | 2.5 | $2.27 | 9.2 | 4.6 |
| Q2 2026 | 19.0 | +9% | 277 | **−13%** | 3.2 | $2.99 | 9.5 | 4.8 |

¹ Q4 2025 YoY comparisons for service revenue/net adds were "industry-leading"/"industry best" per the release but a specific YoY % was not restated in the sourced Ex-99.1; not fabricated here.

**Variance decomposition (company's own releases):**
- **Q1 2026 GAAP net income fell 15% YoY and diluted EPS fell 12% YoY** despite Core Adjusted EBITDA growing +12% YoY — the release attributes this explicitly to **UScellular merger-related costs, including accelerated depreciation, net of tax, of $476 million ($0.43/share)**. This is exactly the kind of GAAP-vs-adjusted gap the program's prior audit (`lead_v3_audit.md`) flagged as a recurring risk of being mixed up or omitted; it is disclosed and quantified by the company itself and is treated here as a one-off merger-integration cost, not an operating deterioration (Core Adjusted EBITDA and Adjusted FCF both grew through the same period).
- **Q2 2026 net income (+1% YoY) also included** a smaller residual UScellular merger-cost drag ($146m net of tax, $0.14/share) — the integration cost is fading but not yet zero.
- **Postpaid net-account deceleration is the clearest adverse trend**, not decomposed away by any one-off in the releases: 396k (Q3'25) → 261k (Q4'25) → 217k (Q1'26) → 277k (Q2'26), i.e., every one of the last three quarters shown is below the Q3'25 level, and Q2'26 is down 13% YoY against an easier prior-year comp. Postpaid ARPA growth (2–4% YoY each quarter) is real but is not a full offset if account growth continues to slow.

## 5. Guidance track record (last four releases; both numbers quoted every time)
| Release | Action | What changed |
|---|---|---|
| 2025-10-23 (Q3'25) | **Raised** ("Raises Guidance Across the Board" per the release headline) | Full detail not re-extracted this pass beyond the headline framing — flagged as a gap, not fabricated. |
| 2026-02-11 (Q4/FY25 → initial FY2026 guide) | New FY2026 guide issued | Initial FY2026 ranges set (not compared to a "prior" FY2026 range since this was the first one). |
| 2026-04-28 (Q1'26) | **Raised** ("Raises Guidance" per release headline; Q1 exceeded internal expectations) | Full prior-vs-current table not re-extracted this pass — flagged as a gap. |
| 2026-07-23 (Q2'26) | **Raised (cash flow only); reiterated (accounts/profitability)** — verified against the company's own side-by-side table | Postpaid net account additions: unchanged at 950k–1,050k (FY2026). Core Adjusted EBITDA: unchanged at $37.1bn–$37.5bn. **Net cash from operations: raised to $28.4bn–$28.8bn from $28.1bn–$28.7bn** (midpoint +$200m). **Adjusted Free Cash Flow: raised to $18.4bn–$18.8bn from $18.1bn–$18.7bn** (midpoint +$200m). Effective tax rate range unchanged at 25–26%. |

The Q2 2026 release is the one release in this sample independently verified against the company's own explicit "Previous / Current / Change" guidance table (source #4, §12) — a genuine, numbers-quoted raise on cash flow, with account and profitability guidance held flat rather than also raised, which is a more conservative and more credible signal than "raised across the board" would be. The Q3'25 and Q1'26 "raised" characterizations are taken from the releases' own headlines but the specific prior-vs-current numeric ranges were not re-extracted in this time-boxed pass (disclosed gap, not treated as fabricated evidence for the verdict).

## 6. Earnings quality & balance sheet
- **GAAP vs adjusted gap is well-explained and shrinking:** the Q1 2026 GAAP EPS decline (−12% YoY) and Q2 2026 near-flat GAAP net income growth (+1% YoY) are both directly attributed by the company to UScellular merger-related accelerated depreciation and integration costs ($476m and $146m net-of-tax respectively) — a real, quantified, disclosed item, not an unexplained gap. Core Adjusted EBITDA (+12%, +12% YoY in Q1/Q2 2026) is the cleaner read on underlying trading performance.
- **Legacy litigation cost still flowing through adjustments:** the Q2 2026 release's non-GAAP reconciliation footnotes still exclude "the settlement of certain litigation and compliance costs associated with the **August 2021 cyberattack**, net of insurance recoveries" — i.e., five years on, data-breach litigation costs are still being adjusted out of Core Adjusted EBITDA. Not large enough to size, but a real, recurring red flag for the "adjusted" framing.
- **SBC** is modest: ~$214m (Q2 2026 quarter) on ~$21bn quarterly revenue (service + equipment) ≈ ~1% of revenue.
- **Balance sheet and leverage:** long-term debt was $86.28bn at FY2025 (XBRL `LongTermDebt`, includes current portion) against cash of $5.60bn (FY2025) — net debt ≈ **$80.7bn**. Against FY2025 Core Adjusted EBITDA of $33.9bn, that is **≈2.4x net debt/EBITDA** (this dossier's own calculation from XBRL primary data; T-Mobile's own investor-materials leverage definition may differ slightly by including securitization/tower-related items not captured in the `LongTermDebt` XBRL tag, so this figure is presented as an estimate, not a company-reported number). Cash fell further to $2.83bn by Q2 2026 as buybacks accelerated.
- **Capital return is large and running ahead of the authorization pace:** Q2 2026 alone: $2.2bn of buybacks + $1.1bn of dividends = $3.3bn of stockholder returns, against an $18.2bn authorization running through 31 December 2026; cumulative since program inception, $54.6bn ($44.2bn buybacks + $10.4bn dividends). Weighted-average diluted shares fell from 1,131m (FY2025) to 1,082m (Q2 2026 quarter), a ~4.3% reduction in two quarters — an aggressive pace that is drawing down cash (see above) rather than being funded entirely from the quarter's own FCF.
- **Governance:** Srini Gopalan (former T-Mobile COO, ex-CEO of Deutsche Telekom's German unit) became CEO effective 1 November 2025, succeeding long-tenured CEO Mike Sievert, who moved to a newly created Vice Chairman advisory role through December 2026. This is a completed, orderly transition (not a live catalyst), but the current CEO has under one year of tenure as of this review — a modest key-person/strategy-continuity item to track, not a red flag.

## 7. Valuation snapshot (this dossier's own reverse read — no V1 row exists)
NTM P/E ≈12.6x and FCF yield ≈10.4% (per `b1_live_scores.csv`), against 47.6% cited "street upside" in the triage note (not independently re-verified against current analyst targets this pass). A simple reverse read using the company's own guidance: FY2026 Adjusted FCF guided at $18.4–18.8bn (midpoint $18.6bn) against a ~$177.5bn market cap (`b1_live_scores.csv`, 2026-09-25) is a ~10.5% FCF yield for a business still growing Core Adjusted EBITDA and Adjusted FCF at high single-to-low-double digits and returning most of it to shareholders — a genuinely attractive combination if the net-account deceleration in §4 stabilizes rather than continues, and a much less attractive one if it does not (revenue growth would then depend increasingly on ARPA/price alone, a slower and more competitively contested lever). **Dossier view: fair-to-cheap on the numbers as guided, with the net-account trend as the swing factor** — this dossier does not have an independent DCF/reverse-DCF tool run against TMUS this pass (no V1 row; time-boxed), so this read is qualitative and should be treated as lower-confidence than the STLD/UBER valuation sections in this batch.

**3-year annualised scenario returns (this dossier's own simple build — no V1 row):** bear **−7.1%/yr** (net-add deceleration persists, FCF/share flat, exit P/FCF compresses to 7.0x from ~9.6x now), base **+10.1%/yr** (FCF/share +8%/yr, multiple flat), bull **+19.0%/yr** (deceleration reverses, FCF/share +12%/yr, multiple re-rates to 11.0x) — each includes a ~$4.08/share/yr run-rate dividend (Q2'26 dividend annualised), undiscounted.

## 8. Bull case and bear case
**Bull (3 points):**
1. Core Adjusted EBITDA and Adjusted FCF are compounding at low-double-digit rates with guidance being raised (not just met) on cash flow at the most recent release, against numbers explicitly quoted in the company's own table (§5).
2. Aggressive, sustained capital return (share count down ~4.3% in two quarters, $54.6bn cumulative since program inception) directly benefits per-share metrics even if top-line account growth slows.
3. Fixed-wireless/fiber (Metronet, Lumos) and the UScellular spectrum/customer absorption are genuine incremental growth vectors beyond the core postpaid-phone business, not yet fully reflected in the net-account figures being watched here.

**Bear (3 points):**
1. Postpaid net-account growth has gone from +26% YoY (Q3'25) to −13% YoY (Q2'26) in three quarters — a real, filed deceleration in the metric that most directly measures competitive customer-acquisition strength, not adequately explained away by ARPA gains alone.
2. Net debt of ~$80bn (≈2.4x EBITDA by this dossier's estimate) is being drawn down further (cash fell from $5.6bn to $2.8bn in two quarters) to fund buybacks running ahead of quarterly FCF — a capital-allocation pace that has less room to continue if EBITDA growth itself decelerates.
3. UScellular merger-integration costs are still flowing through GAAP results (accelerated depreciation charges in both Q1 and Q2 2026) — full clean-quarter comparability has not yet been reached, and the true post-integration run-rate is not yet visible.

## 9. Key risks & kill criteria (measurable)
1. Postpaid net account additions turn negative (net losses) in any quarter.
2. Full-year guidance is CUT (not just reiterated) on Core Adjusted EBITDA or Adjusted Free Cash Flow at any release.
3. Net debt/Core Adjusted EBITDA (this dossier's estimate, currently ~2.4x) rises above 3.0x.
4. Postpaid net-account YoY growth stays negative for two additional consecutive quarters beyond Q2 2026 (i.e., through Q4 2026), confirming a structural rather than transitory slowdown.
5. The current $18.2bn buyback/dividend authorization (through 31 Dec 2026) is not renewed or is renewed at a materially smaller size while cash continues to draw down.

## 10. Catalysts & calendar
- Next earnings: **~2026-10-22/23** (Q3 2026 results; estimated from the 2025-10-23 Q3 2025 reporting date, not yet confirmed by the company).
- Buyback/dividend authorization ($18.2bn) runs through **31 December 2026** — a renewal/re-sizing decision is a near-term catalyst.
- Metronet/Lumos fiber joint-venture build-out and UScellular integration are multi-quarter execution items with no single hard date identified in this pass.

## 11. Red-flag scan
No auditor changes, material weaknesses, restatements, or going-concern language identified in the sections reviewed. No SEC/DOJ investigation of TMUS itself identified in this pass (not exhaustively searched — disclosed limitation). The **2021 cyberattack litigation/settlement costs are still being excluded from Core Adjusted EBITDA as of the Q2 2026 release** (§6) — a real, if not newly material, ongoing legal-cost item. Insider Form 4 pattern and short-seller reports were **not independently checked in this pass** (time-boxed; disclosed gap).

## 12. Sources
1. SEC EDGAR — T-Mobile US Inc, CIK 0001283699: submissions JSON and companyfacts JSON (`data.sec.gov/submissions/CIK0001283699.json`, `.../api/xbrl/companyfacts/CIK0001283699.json`), retrieved 2026-09-26.
2. 8-K Ex-99.1, "T-Mobile Delivers Continued Strong Account Growth… Q2 Results," filed 2026-07-23. `sec.gov/Archives/edgar/data/1283699/000128369926000100/tmus06302026ex991.htm`
3. 8-K Ex-99.1, Q1 2026 results, filed 2026-04-28. `sec.gov/Archives/edgar/data/1283699/000128369926000062/tmus03312026ex991.htm`
4. 8-K Ex-99.1, "T-Mobile Delivers Best-in-Class Customer Results in Q4… Full Year 2025 Results," filed 2026-02-11. `sec.gov/Archives/edgar/data/1283699/000128369926000007/tmus12312025ex991.htm`
5. 8-K Ex-99.1, "T-Mobile Delivers Record Customer Growth… Raises Guidance Across the Board," Q3 2025, filed 2025-10-23. `sec.gov/Archives/edgar/data/1283699/000128369925000153/tmus09302025ex991.htm`
6. T-Mobile Newsroom, "Srini Gopalan to Succeed Mike Sievert as T-Mobile CEO on November 1, 2025." `t-mobile.com/news/business/srini-gopalan-new-ceo` (web search, cross-check only; leadership-transition fact not disputed).
7. `v4/data/b1_live_scores.csv` (as_of 2026-09-25); `v4/outputs/Q01_triage.json`; confirmed no TMUS row exists in `v4/outputs/v1_valuation_table.csv` / `v1_valuation.json`.

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q, period ended 2026-06-30, filed 2026-07-23. Checked for events to 2026-09-25 (one routine 8-K dated 2026-09-01 reviewed by index only, not an earnings/guidance event). GAAP vs adjusted: all figures above are labeled GAAP or (Core Adjusted EBITDA / Adjusted FCF) non-GAAP as T-Mobile itself defines them; never blended without a label. No V1 systematic valuation exists for this ticker — this dossier's valuation view is qualitative only. Research, not personal investment advice.
