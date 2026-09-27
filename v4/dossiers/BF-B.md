# BF-B — Brown-Forman Corporation

## 1. Verdict
**WATCH** — 24–48 month horizon. Valuation has already de-rated to reflect the volume malaise, but management's own fiscal-2027 guidance is for organic **operating income to decline** (not just flat sales); buying ahead of a company-guided earnings decline is not disciplined, even at a reasonable multiple. Re-underwrite on evidence of a turn (see kill criteria).

## 2. Business in plain English
Brown-Forman owns Jack Daniel's, Woodford Reserve, Old Forester, Herradura and other spirits brands, sold worldwide mostly through third-party distributors/retailers with high gross margins (~60%) driven by brand strength and pricing power rather than volume growth. It is family-controlled (Brown family, dual-class B shares), a long-standing dividend grower ("dividend aristocrat"), with concentrated exposure to US whiskey and, increasingly, to trade-policy and consumer-moderation headwinds.

## 3. Why the model likes it / durability
b1 factor data (`v4/data/b1_live_scores.csv`, as-of 2026-09-25): decile 8/10, quintile 4/5; strong quality/profitability (gp_a percentile 41st but roe percentile 50th, ep percentile 78th cheap-on-earnings), and notably weak recent price momentum (mom_12_1 percentile 27th) — consistent with a stock that has been sold off. Triage's own red flags are accurate and current: "US spirits category volume malaise (moderation/GLP-1 headwind)" and "tariff exposure on American whiskey exports to Canada/EU." These are not durable "moat" reasons for the quant score — the model likes it on value/quality factors precisely because the market has already priced in real, ongoing damage; the open question is whether the damage is cyclical (destocking, one-off tariff shock) or a structural volume decline that will keep pushing the "fair" multiple down.

## 4. Last several quarters (net income, from SEC XBRL `NetIncomeLoss`, `https://data.sec.gov/api/xbrl/companyconcept/CIK0000014693/us-gaap/NetIncomeLoss.json`, retrieved 2026-09-27; fiscal year ends April 30, so "FY" quarters below use BF's own Q1=May–Jul, Q2=Aug–Oct, Q3=Nov–Jan, Q4=Feb–Apr)

| Fiscal quarter (period end) | Net income |
|---|---|
| Q1 FY2027 (2026-07-31) | $176M |
| Q4 FY2026 (2026-01-31) | $267M |
| Q3 FY2026 (2025-10-31) | $224M |
| Q2 FY2026 (2025-07-31) | $170M |
| Q4 FY2025 (2025-01-31) | $270M |
| Q3 FY2025 (2024-10-31) | $258M |
| Q2 FY2025 (2024-07-31) | $195M |
| Q4 FY2024 (2024-01-31) | $285M |

**Q1 FY2027 (ended 2026-07-31), from the 10-Q filed 2026-09-02 (accession 0000014693-26-000052) and its EX-99.1 press release (accession 0000014693-26-000048, `fy27_q1xerevergreen.htm`):** net sales **$911M**; organic net sales **−1%** YoY; GAAP diluted EPS **$0.38**; gross margin **60.2%**; operating income **$252M**.

**Guidance track record, quoted verbatim, versus the prior range:**
- Fiscal 2026 outlook (given June 2026 with Q4/FY2026 results): organic net sales and organic operating income guided to decline in the low-single-digit range for FY2026 (per company release "Brown-Forman Reports Fiscal 2026 Results," 2026-06-04) — a **downward revision** from the flat-to-slightly-positive framing the company had used entering FY2026 (per contemporaneous reporting on the June release).
- Fiscal **2027** outlook, first given with FY2026 results (June 2026) and **reaffirmed** at Q1 FY2027 (2026-09-02): *"Organic net sales to be approximately flat"* and *"Organic operating income to decline in the 3% to 5% range."* The Q1 FY2027 release is titled "Brown-Forman Reports First Quarter Fiscal 2027 Results; **Reaffirms** Full Year Outlook" — i.e., guidance was **maintained**, not raised, despite a −1% organic net-sales quarter that is running slightly behind the "approximately flat" full-year target; also guided: effective tax rate ~20–22%, capex $60–70M.
- No numeric guidance was found (or is customary) for quarterly EPS; the company guides fiscal-year organic sales/operating-income ranges only. Where no guidance exists for a metric, that is stated rather than inferred.

## 5. Balance sheet and cash conversion
Consolidated (per `d4_live_snapshot.parquet`, as-of 2026-09-25, keyed off the Q1 FY2027 10-Q, accession 0000014693-26-000052): total debt $2.441B (book/carrying value — confirm gross vs carrying in the 10-Q debt footnote before using for a kill criterion), total cash $301M, TTM EBITDA ≈$1.186B (net leverage ≈1.8x). TTM operating cash flow $1.013B, TTM free cash flow ≈$686M (FCF/NI conversion is solid for a low-capex branded-spirits model, consistent with the June-2026 release's own comment on "doubling" free cash flow for FY2026 versus FY2025, per third-party reporting on that release). Dividend: BF is a long-tenured dividend grower; trailing dividend yield ≈3.5% (`y_trailingAnnualDividendYield` ≈0.03539 in the snapshot) — the dividend is a real component of any base-case total return, not just capital appreciation.

## 6. Red flags
- **Canada boycott/delisting:** Canadian sales fell ~62% in the fiscal Q2 2026 (quarter ended Oct 2025) amid a consumer boycott/provincial delisting of US spirits tied to the tariff dispute; management has said Jack Daniel's is expected to **remain off shelves in most of Canada** through the rest of the fiscal year (per company commentary reported September 2026).
- **Tariffs:** the EU has settled on a 25% tariff on American whiskey; third-party analyst estimates cited in September 2026 press coverage suggest a 50% EU tariff scenario could be roughly a 10-point hit to EBIT — this is an outside analyst's estimate, not a figure the company itself has published, and is flagged here as unverified third-party math, not a fact.
- **Unsolicited take-private/M&A interest:** Sazerac made an unsolicited ~$15B bid for Brown-Forman that the company/family rejected (2026) — a live signal that outside parties see value the market currently doesn't, but also a distraction/overhang while the dual-class family-control structure makes a deal unlikely without Brown-family consent.
- No restatement, no material weakness, no going-concern language identified in the reviewed filings.

## 7. Reverse DCF and valuation vs V1
`v4/outputs/v1_valuation_table.csv` has **no row for BF-B** — v1_verdict = null.
Own reverse DCF: EV $14.07B (from `d4_live_snapshot.parquet`), TTM FCF $0.686B, 7.5% discount rate (staples-level WACC, slightly above peer to reflect elevated near-term earnings risk), 2.5% terminal growth ⇒ **implied 10-year FCF growth ≈ 2.5% p.a.** — i.e., the market is pricing in essentially no more than trend/terminal growth, matching the company's own "approximately flat" FY2027 organic sales guide plus modest long-run pricing. My base case (a return to low-single-digit organic growth by FY2029 once the Canada boycott resolves and tariff dust settles, offset by continued category moderation) is **roughly in line with** that implied 2.5% — `valuation_view_vs_v1.implied_vs_base = "in_line"`. The valuation is fair, not a bargain and not demanding; the WATCH verdict is driven by the guided near-term **earnings decline** (organic operating income −3% to −5% for FY2027, reaffirmed) rather than by the price.

## 8. Bull case
1. Multiple has already de-rated (≈15x NTM per triage) to reflect known bad news (Canada, tariffs, moderation), so a lot of the downside may already be priced — reverse DCF implies only ~2.5% growth is needed.
2. Free cash flow conversion remains strong and the dividend (~3.5% yield) is a real cash return while waiting for volumes to stabilize.
3. Sazerac's unsolicited $15B bid is external evidence that strategic buyers see more value in the brand portfolio than the current price reflects.

## Bear case
1. Fiscal 2027 guidance, reaffirmed as recently as 2026-09-02, is for organic **operating income to decline 3–5%** — the company itself is guiding earnings down, not just flat; the "de-rated multiple" argument doesn't help if the E in P/E keeps falling.
2. The Canada shelf ban has no company-committed end date ("expected to remain off shelves in most of Canada" through the fiscal year) — this is an open-ended, policy-driven revenue loss, not a normal demand cycle.
3. US spirits category volume moderation (GLP-1/health trends) is a structural, not cyclical, headwind that predates the tariff dispute and could persist even after tariffs are resolved.

## 9. Key risks & kill criteria
1. Organic net sales for FY2027 print **below −2%** at any quarterly update (vs. the reaffirmed "approximately flat" full-year guide).
2. Fiscal 2027 organic operating-income guidance is cut below the "3% to 5% range" quoted verbatim in §4 (i.e., a decline worse than 5%) at any quarterly update.
3. Canadian sales remain off-shelf/boycotted for more than **two full fiscal years** from the initial 2025 disruption (i.e., no partial restoration by fiscal Q2 FY2028).
4. Consolidated net debt/EBITDA (confirm gross vs. carrying basis in the 10-Q footnote) rises above **2.5x**.
5. The dividend is cut or its multi-decade growth streak is broken.

## 10. Catalysts & calendar
Next earnings: **2026-12-03** (Q2 FY2027, per `d4_live_snapshot.parquet` `next_earnings_date`).

## 11. Red-flag scan (summary)
No restatement, no disclosed material weakness or going-concern language in the reviewed 10-Q (accession 0000014693-26-000052) or 8-K (accession 0000014693-26-000048) filings. No SEC/DOJ investigation found. Key non-accounting red flags are the Canada boycott, EU/Canada tariff exposure, and the rejected Sazerac approach (all described above with sources).

## 12. Sources
1. https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000014693&type=10-Q (10-Q filing list, retrieved 2026-09-27)
2. https://www.sec.gov/Archives/edgar/data/14693/000001469326000052/0000014693-26-000052-index.htm (10-Q, filed 2026-09-02)
3. https://www.sec.gov/Archives/edgar/data/14693/000001469326000048/fy27_q1xerevergreen.htm (EX-99.1, Q1 FY2027 press release, filed 2026-09-02)
4. https://data.sec.gov/api/xbrl/companyconcept/CIK0000014693/us-gaap/NetIncomeLoss.json (retrieved 2026-09-27)
5. Brown-Forman, "Brown-Forman Reports Fiscal 2026 Results" (2026-06-04): https://www.brown-forman.com/article/brown-forman-reports-fiscal-2026-results-june-4-2026
6. Brown-Forman, "Brown-Forman Reports First Quarter Fiscal 2027 Results; Reaffirms Full Year Outlook" (2026-09-02): https://www.brown-forman.com/article/brown-forman-reports-first-quarter-fiscal-2027-results-reaffirms-full-year-outlook
7. Canada sales/tariff coverage: https://www.fooddive.com/news/brown-forman-canada-sales/807565/ ; https://www.vinetur.com/en/20260904106628/brown-forman-expects-jack-daniels-to-stay-off-shelves-in-most-of-canada.html ; https://www.forbes.com/sites/nathangoldman/2026/09/17/whiskey-tariffs-impact-the-market-for-brown-liquor/
8. Sazerac unsolicited bid: https://whiskeyreviewer.com/2026/05/bankruptcies-lawsuits-and-mergers-spring-update-051826/
9. `v4/data/b1_live_scores.csv`, `v4/data/d4_live_snapshot.parquet` (as of 2026-09-25); `v4/outputs/v1_valuation_table.csv` (checked; no BF-B row)

## Data basis, recency and disclaimer
Most recent period incorporated: Q1 FY2027 10-Q, period ended 2026-07-31, filed 2026-09-02 (accession 0000014693-26-000052); Q1 FY2027 earnings release filed same day (accession 0000014693-26-000048). Checked for events to 2026-09-25 close (and, for the Canada/tariff narrative specifically, to press coverage dated as late as 2026-09-17/09-21, which is data, cited and dated, not filings). GAAP figures are labelled GAAP; organic net sales/operating income are the company's own non-GAAP organic measures, labelled as such. Research only, not personal investment advice.
