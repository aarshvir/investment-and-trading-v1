# CMG — Chipotle Mexican Grill, Inc.

## 1. Verdict
**WATCH** — 12–24 month horizon. The operating story has genuinely improved (traffic turned positive for two straight quarters after a 2025 decline — triage's red flag is now partly stale), but at the current price the market is implying roughly **13% annualised FCF growth for 10 years**, well above what continued margin compression and a low-single-digit comp algorithm can plausibly deliver. This is the textbook case the addendum warns about: a good business priced for more than it can deliver is WATCH, not INCLUDE.

## 2. Business in plain English
Chipotle operates (and franchises internationally, minimally) fast-casual Mexican restaurants with an assemble-in-front-of-you format, digital ordering/Chipotlane drive-through pickup, and a highly standardized, capital-light unit economic model (~mid-40% restaurant-level margins historically). It makes money from high unit volumes and strong per-store economics rather than menu pricing power, and is expanding units domestically and, slowly, internationally through partner-operated stores.

## 3. Why the model likes it / durability
b1 factor data (`v4/data/b1_live_scores.csv`, as-of 2026-09-25): decile 5/10, quintile 3/5 — a mid-pack quant score, not a standout, driven by very strong profitability (roe percitle 89th, ocf_a percentile 95th) offset by weak recent value (bp percentile 18th, i.e., expensive on book) and mixed momentum. Triage's stated red flag — "three consecutive quarters of negative comps, driven by traffic/frequency declines" — was accurate as of when that triage ran (comps were negative in fiscal Q2–Q4 2025, per company releases: Q3 2025 comp +0.3% but transactions −0.8%; Q4 2025 comp **−2.5%** with transactions **−3.2%**; full-year 2025 comp −1.7%, transactions −2.9%). **That has changed**: Q1 2026 comp +0.5% (transactions +0.6%) and Q2 2026 comp +2.2% (transactions +1.0%) — two consecutive quarters of positive traffic, the company's own Q2 2026 release calling it the "second consecutive quarter of improving transaction comp." The triage's red flag is therefore **partly overturned by more recent data**, which is exactly the kind of update this dossier exists to catch — but margin has not recovered alongside traffic (see §4), so the "quality" score may be lagging a genuine profitability deceleration.

## 4. Last several quarters (revenue, from SEC XBRL `Revenues`, `https://data.sec.gov/api/xbrl/companyconcept/CIK0001058090/us-gaap/Revenues.json`, retrieved 2026-09-27)

| Quarter (period end) | Revenue | Comparable sales (company releases) |
|---|---|---|
| Q2 2026 (2026-06-30) | $3,349M | **+2.2%** (avg check +1.2%, transactions +1.0%) |
| Q1 2026 (2026-03-31) | $3,088M | +0.5% (transactions +0.6%) |
| Q4 2025 (2026-02-03 release, FY end 2025-12-31) | n/a in this XBRL cut | **−2.5%** (transactions −3.2%) |
| Q3 2025 (2025-09-30) | $3,003M | +0.3% (transactions **−0.8%**) |
| Q2 2025 (2025-06-30) | $3,063M | — |
| Q1 2025 (2025-03-31) | $2,875M | +0.5% (per Q1 2025 release, transactions +0.6% offset by check −0.1%) |
| Q3 2024 (2024-09-30) | $2,794M | — |
| Q2 2024 (2024-06-30) | $2,973M | — |
| Q1 2024 (2024-03-31) | $2,702M | — |

**Q2 2026 (13 weeks ended 2026-06-30), from the 10-Q filed 2026-07-31 (accession 0001058090-26-000066) and its EX-99.1 press release (accession 0001058090-26-000063, `cmg-20260729xex991.htm`):** total revenue **$3.3B, +9.3%** YoY; comparable restaurant sales **+2.2%** ("a 1.2% increase in average check and a 1.0% increase in transactions"); restaurant-level operating margin **25.2%**, down from 27.4% a year ago; operating margin **15.7%**, down from 18.2%; GAAP diluted EPS $0.32 (roughly flat YoY on this basis, post the 50:1 stock split).

**Guidance track record, quoted verbatim, versus the prior range:**
- Q1 2026 release (2026-04-29): full-year 2026 comparable-sales guidance **"about flat"**, with pricing guided at 1–2% for the year.
- Q2 2026 release (2026-07-29, EX-99.1): *"For 2026, management is anticipating the following: Full year comparable restaurant sales growth in the low single digit range; 350 to 370 new restaurant openings, which includes 10 to 15 international partner-operated restaurants. Around 80% of new company-owned restaurants will have a Chipotlane; An estimated underlying full year effective tax rate between 24% and 26% before discrete items."* The release's own headline is **"CHIPOTLE RAISES FULL YEAR COMPARABLE SALES GUIDANCE ON STRONG Q2 MOMENTUM"** — a genuine **raise** from "about flat" to "low single digit," confirmed by the headline framing as well as the numeric change.
- No numeric restaurant-level-margin or EPS guidance was given for FY2026 in the release; that is stated rather than inferred.

## 5. Balance sheet and cash conversion
Consolidated, per the Yahoo-derived quant snapshot (`d4_live_snapshot.parquet`, as-of 2026-09-25, keyed off the Q2 2026 10-Q, accession 0001058090-26-000066): total debt $5.419B. Cross-checked directly against SEC XBRL companyfacts (`https://data.sec.gov/api/xbrl/companyfacts/CIK0001058090.json`), the standard long-term/carrying-value debt concepts (`LongTermDebt`, `DebtInstrumentCarryingAmount`, `LongTermDebtAndCapitalLeaseObligations`) show essentially **$0** — confirming this $5.419B is not funded debt at all but almost entirely operating-lease liabilities (Chipotle carries no meaningful term debt or bonds). This figure should not be read as a leverage red flag in the way a term-loan balance would be; it is a real fixed obligation (store rent) but of a fundamentally different, less-refinancing-risk character than bank/bond debt. Total cash $678M; TTM EBITDA $2.275B; TTM operating cash flow $2.328B; TTM free cash flow ≈$1.116B — very strong FCF conversion (FCF/NI comfortably >1x given depreciation-heavy, low-net-debt store economics), consistent with the business's long-standing reputation for high-quality earnings. No dividend; capital return is via buybacks.

## 6. Red flags
- **2026 multistate Salmonella outbreak:** the first lawsuit tied to a 2026 multistate Salmonella outbreak was filed in Minnesota federal court in August 2026 (plaintiff hospitalized); Chipotle has said jalapeños are the likely vehicle but had not, as of the reporting found, identified the specific supplier. This is a live, ongoing food-safety/legal matter, not historical.
- **Prior securities-fraud class action (2024):** a securities-fraud class action naming Chipotle and former CEO Brian Niccol (who departed for Starbucks in 2024) and food-safety officer Laurie Schalow was filed in November 2024 in the Central District of California, related to earlier food-safety-linked disclosures; this predates the current CEO/management team but is a live case to track for outcome/settlement risk.
- **Margin compression alongside the traffic recovery:** restaurant-level margin fell 220bps and operating margin fell 250bps YoY in Q2 2026 even as comps turned positive — the "quality" score in the b1 factors may not yet reflect this; decompose whether it is wage/food inflation, marketing spend to drive the traffic recovery, or new-unit drag before assuming margins snap back with comps.
- No restatement, no material weakness, no going-concern language found in the reviewed filings.

## 7. Reverse DCF and valuation vs V1
`v4/outputs/v1_valuation_table.csv` has **no row for CMG** — v1_verdict = null.
Own reverse DCF: EV $45.25B (from `d4_live_snapshot.parquet`), TTM FCF $1.116B, 8.5% discount rate, 3% terminal growth ⇒ **implied 10-year FCF growth ≈ 12.9% p.a.** My base case: unit growth of ~8–9% (350–370 net openings on a base of roughly 3,700+ restaurants) plus low-single-digit comps (per the just-raised guide) gets top-line growth to roughly 10–12%, but with restaurant-level margin still contracting (−220bps YoY in the latest quarter) rather than expanding, FCF growth should run **at or below revenue growth**, i.e., a realistic base case is closer to **8–10%** than 13%. The market's implied growth is **above** that base case — `valuation_view_vs_v1.implied_vs_base = "above"`. This is consistent with the b1 value factors (bp percentile only 18th — expensive on book) even as quality/profitability factors are strong; the stock is priced for a full margin recovery *and* sustained double-digit growth simultaneously, which is a high bar given §4's margin trend.

## 8. Bull case
1. Traffic has now inflected positive for two consecutive quarters (Q1 +0.6%, Q2 +1.0%) after three quarters of decline in 2025 — the "Recipe for Growth" initiatives (value perception, digital/Chipotlane throughput) appear to be working, and guidance has been raised accordingly.
2. Unit growth ("350 to 370 new restaurant openings," quoted in §4, for 2026) continues at a high absolute rate on an already-large base, and ~80% of new company units will have a Chipotlane, historically Chipotle's highest-margin, highest-volume format.
3. Balance sheet is essentially debt-free (ex-leases) with strong FCF generation, giving management flexibility to keep investing in the turnaround without financial strain.

## Bear case
1. Restaurant-level margin (25.2%) and operating margin (15.7%) both fell meaningfully YoY even in the "recovery" quarter — the market's implied ~13% FCF growth requires margins to stop falling and likely re-expand, which has not yet happened in the data.
2. The 2026 Salmonella outbreak is an open legal and reputational risk with an unidentified supplier as of the last update found — Chipotle has prior, expensive experience (a $25M DOJ fine tied to earlier foodborne-illness cases) with food-safety events denting traffic for multiple quarters.
3. Guidance was only raised to "low single digit" comps, not high-single or double-digit — management itself is not calling for the kind of growth the current EV implies over a 10-year horizon.

## 9. Key risks & kill criteria
1. Comparable restaurant sales growth prints **negative** for any quarter (a reversal of the current two-quarter positive-traffic trend).
2. Restaurant-level operating margin falls below **24%** (i.e., more than 100bps below the Q2 2026 25.2% print) for two consecutive quarters.
3. The 2026 Salmonella outbreak is linked to a Chipotle-controlled (not third-party supplier) failure, or the case count/lawsuit count materially expands beyond the single Minnesota filing found here.
4. Full-year 2026 comparable-sales guidance is **cut** from the current "low single digit" range at the Q3 2026 report (2026-10-28).
5. New-unit growth (openings) falls materially below the guided 350–370 range for 2026, signalling real-estate or capital-allocation strain.

## 10. Catalysts & calendar
Next earnings: **2026-10-28** (Q3 2026, per `d4_live_snapshot.parquet` `next_earnings_date`).

## 11. Red-flag scan (summary)
Live 2026 Salmonella-outbreak litigation (first suit filed August 2026 in Minnesota federal court, supplier not yet identified) and a pending 2024-origin securities class action (Central District of California) are the two material legal items; no restatement, material weakness or going-concern language found in the reviewed 10-Q (accession 0001058090-26-000066) or 8-K (accession 0001058090-26-000063).

## 12. Sources
1. https://www.sec.gov/Archives/edgar/data/1058090/000105809026000066/0001058090-26-000066-index.htm (10-Q, filed 2026-07-31)
2. https://www.sec.gov/Archives/edgar/data/1058090/000105809026000063/cmg-20260729xex991.htm (EX-99.1, Q2 2026 press release, filed 2026-07-29)
3. https://data.sec.gov/api/xbrl/companyconcept/CIK0001058090/us-gaap/Revenues.json (retrieved 2026-09-27)
4. https://ir.chipotle.com/2026-04-29-CHIPOTLE-ANNOUNCES-FIRST-QUARTER-2026-RESULTS (Q1 2026 release, for prior guidance)
5. https://newsroom.chipotle.com/2026-02-03-CHIPOTLE-ANNOUNCES-FOURTH-QUARTER-AND-FULL-YEAR-2025-RESULTS (Q4/FY2025 comp sales)
6. https://ir.chipotle.com/2025-10-29-CHIPOTLE-ANNOUNCES-THIRD-QUARTER-2025-RESULTS (Q3 2025 comp sales)
7. Salmonella-outbreak lawsuit: https://www.streetinsider.com/PRNewswire/FIRST+LAWSUIT+FILED+AGAINST+CHIPOTLE+MEXICAN+GRILL+IN+MULTISTATE+SALMONELLA+OUTBREAK/26873252.html
8. 2024 securities class action background: https://en.wikipedia.org/wiki/Brian_Niccol (context) and case reporting cross-checked via web search, 2026-09-27
9. `v4/data/b1_live_scores.csv`, `v4/data/d4_live_snapshot.parquet` (as of 2026-09-25); `v4/outputs/v1_valuation_table.csv` (checked; no CMG row)

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q, period ended 2026-06-30, filed 2026-07-31 (accession 0001058090-26-000066); Q2 2026 earnings release filed 2026-07-29 (accession 0001058090-26-000063). Checked for events to 2026-09-25 close (Salmonella-litigation news dated August 2026 is cited and dated, not a filing). GAAP figures are labelled GAAP; adjusted diluted EPS (~$0.33 for Q2 2026 vs GAAP $0.32) is the company's own non-GAAP measure, labelled as such. Research only, not personal investment advice.
