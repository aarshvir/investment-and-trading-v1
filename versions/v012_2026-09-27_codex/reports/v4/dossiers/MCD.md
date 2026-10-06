# MCD (McDonald's Corporation) — Diligence Dossier

Agent: F36 · Standard depth · Prepared 2026-09-26 · Prices/market data as of 2026-09-25 close ($236.50; mkt cap ≈$167.4B)

## 1. Verdict

**INCLUDE-SMALL** — 24–36 month horizon; named reservation: US comparable-sales/traffic momentum has
decelerated for three straight quarters and the balance sheet carries high, buyback-driven leverage (negative
book equity), so this is a lower-conviction "half-weight" holding rather than a full-conviction one despite a
clearly favourable reverse-DCF read. No V1 systematic valuation row exists for MCD; `v1_verdict = null`.

## 2. Business in plain English

McDonald's is the world's largest quick-service-restaurant franchisor by system sales: ~95% of its ~43,000+
restaurants are owned and run by independent franchisees who pay McDonald's rent (McDonald's owns or leases
much of the underlying real estate) plus a royalty on sales. McDonald's own P&L is therefore mostly a real-estate/
royalty annuity on other operators' sales, not a direct food-service P&L — which is why its operating margins
(mid-to-high 40s%) look nothing like a typical restaurant operator's. It competes on value, speed and brand
ubiquity, currently leaning on "McValue" promotions to defend US traffic.

**Sector routing note:** GICS "Restaurants" maps to `aviation-hotels.md` under the stock-analysis skill router,
with an explicit cross-read to `fmcg-consumer.md` for the asset-light franchisor/royalty angle — the skill's own
mapping table flags this exact distinction ("Lodging... Distinguish the owner... from the asset-light
franchisor or manager, which is a royalty on system-wide RevPAR" — the restaurant analogue is systemwide sales).
This dossier reads MCD primarily as a brand-royalty annuity (fmcg-consumer lens: same-store/systemwide sales,
franchisee health) with same-store sales and franchisee economics as the operative KPIs, not restaurant-level
unit economics.

## 3. Why the model likes it / is the reason durable?

`data/b1_live_scores.csv` live_rank 369; triage (Q09) scored quality 5 / growth 3 / price_vs_growth 4, citing
"31.7% margins," franchise moat and international growth against a backdrop of US traffic softness. This is
durable: MCD's margin structure is structural (royalty economics), not cyclical, and international
Developmental Licensed Markets growth (+1.9% comp Q2 2026) continues even as the US decelerates.

## 4. Last two years of results (calendar quarters; GAAP)

| Qtr (end) | Revenue | YoY | Operating income | Op. margin | Diluted EPS | Net income | Global comp sales |
|---|---|---|---|---|---|---|---|
| Q3 2024 (Sep-24) | $6,873M | — | $3,188M | 46.4% | $3.13 | — | — |
| **FY2024 total** | **$25,920M** | — | $11,712M | 45.2% | $11.39 | $8,223M | — |
| Q1 2025 (Mar-25) | $5,956M | — | $2,648M | 44.5% | $2.60 | $1,868M | — |
| Q2 2025 (Jun-25) | $6,843M | — | $3,232M | 47.2% | $3.14 | $2,253M | — |
| Q3 2025 (Sep-25) | $7,078M | — | $3,357M | 47.4% | $3.18 | $2,278M | — |
| **FY2025 total** | **$26,885M** | +3.7% | $12,393M | 46.1% | $11.95 | $8,563M | — |
| Q1 2026 (Mar-26) | $6,517M | +9.4% | $2,953M | 45.3% | $2.78 | $1,983M | "strongest revenue growth in 8 quarters" (secondary source) |
| **Q2 2026 (Jun-26)** | **$7,099M** | +3.7% | $3,338M | 47.0% | $3.32/$3.38 adj. | $2,362M | **+1.3% global / +0.8% US** |

Revenue and net income have grown steadily; the story is in the **comp-sales deceleration inside a still-growing
top line**: Q2 2026 US comparable sales of +0.8% (management attributes the shortfall to "inconsistent
restaurant execution and lower consumer awareness" of new value offerings, per the earnings call) versus
+47.2–47.4% operating margins in the year-ago quarters that have not yet been matched again in 2026 (Q1 2026
45.3%, Q2 2026 47.0% — recovering but not yet back to the Q2/Q3 2025 peak). Systemwide sales still grew 5% (4%
constant currency) in Q2 2026 to $37B, and 90-day active loyalty users grew 13% to ~220 million — both signs the
platform (digital/loyalty/delivery) is still compounding even as in-restaurant traffic is soft.

## 5. Guidance track record

McDonald's gives full-year (not quarterly-range) guidance. FY2026 guidance issued with FY2025 results (Feb-2026):
operating margin "mid-to-high 40% range," capex $3.7–3.9B (majority for ~2,600 new restaurant openings), net
unit growth contributing ~2.5% to systemwide sales growth in constant currency, FCF conversion "low-to-mid 80%
range." This full-year guidance was **reaffirmed, not cut,** at the Q1 2026 release despite the US comp-sales
miss — a mild positive (management is not (yet) walking back the year), but also means the deceleration has not
yet been tested against a guidance cut, which is exactly the kill-criterion to watch (Section 9).

## 6. Earnings quality & balance sheet

- **FCF conversion:** TTM through Q2 2026 (FY2025 $10,551M − H1 2025 $4,426M + H1 2026 $5,222M) OCF ≈$11,347M;
  TTM capex (same construction) ≈$3,586M → **FCF ≈$7,761M**. Net income TTM ≈$8,678M (FY2025 $8,563M − H1 2025
  $4,121M + H1 2026 $4,345M) → FCF/NI ≈89%, a healthy cash-conversion ratio for a franchisor.
  **Data conflict:** `d4_live_snapshot` (Yahoo) shows TTM free cash flow of only $6,262M, about 24% below this
  SEC-sourced $7,761M figure — likely a difference in the trailing window or capex classification. The SEC-
  sourced figure is used here as the primary number (directly reconcilable to 10-K/10-Q line items); the gap is
  disclosed, not resolved.
- **SBC:** ~$99M for H1 2026 vs ~$13.6B H1 revenue — under 1%, immaterial to EPS quality.
- **Leverage/capital structure:** stockholders' equity was **−$1,023M** at 30-Jun-2026 (negative, driven by
  cumulative buybacks exceeding retained capital — this has been MCD's structure for years and is a known,
  intentional capital-allocation choice, not a solvency signal on its own). Long-term debt $39.86B + current
  portion ~$0.7–0.9B ≈ **total debt ≈$40.7B**; cash only $822M → **net debt ≈$39.9B**. Using FY2025 operating
  income $12,393M plus an estimated $1.6–1.8B of D&A, adjusted EBITDA ≈$14.0–14.2B → **net debt/EBITDA ≈2.8x**,
  in line with MCD's historically stated leverage target and investment-grade (BBB+/Baa1-area) ratings — a
  business-model-appropriate level for a contracted, royalty-like cash-flow stream, but it does remove any
  balance-sheet margin for error if systemwide sales were to actually decline.
- **Buybacks/dividends:** H1 2026 buybacks $1,251M, dividends $2,640M; diluted share count fell from 717.9M (H1
  2025) to 712.3M (H1 2026), a genuine ~0.8% reduction.
- **Effective tax rate:** FY2025 ≈21.4% (in line with recent history).

## 7. Valuation snapshot and reverse DCF

No V1 row exists for MCD; `v1_verdict = null`. Analyst reverse DCF (`valuation.py`, 10y fade to 3% terminal):

- EV bridge: market cap $167.36B + debt $40.7B − cash $0.82B = **EV ≈$207.24B**
- WACC 6.8% (rf 5.17%, ERP 4.14%, Blume-adjusted beta 0.61 from an unusually low raw beta 0.414 in
  `d4_live_snapshot`; cost of debt 4.0% pretax — this is MCD's actual TTM effective/embedded interest rate
  (interest expense run-rate ÷ total debt), i.e. an *embedded* cost of legacy fixed-rate issuance, not
  necessarily today's *marginal* borrowing rate, flagged as a modelling choice; tax rate 21.4%; debt weight ≈20%)
- Base FCF (TTM through Q2 2026, primary-sourced): $7,761M
- **Implied 10-year FCF growth priced in: ~2.8%/yr**, fading to 3% terminal (i.e., the market is barely pricing
  *any* real growth above the terminal rate).

This analyst's base case (Section 8) assumes ~7%/yr EPS growth (mid-single-digit systemwide sales growth plus
margin recovery toward the guided high-40s% range plus buybacks) over the next three years — well above the
~2.8%/yr the reverse DCF says is priced in. Trailing P/E 19.5x, FCF yield 4.6%, dividend yield 3.1%.
**valuation_view_vs_v1.implied_vs_base = "below."**

**Scenario 3-yr annualised total return (illustrative, price + dividends):** Bear −0.9%/yr (EPS +2%/yr, exit 16x
P/E), Base +10.1%/yr (EPS +7%/yr, exit P/E flat at 19.2x), Bull +19.2%/yr (EPS +11%/yr, exit 22x P/E), each plus
a ~3.1% dividend yield — not consensus, an analyst estimate to make the reasoning checkable.

## 8. Bull case / bear case

**Bull (3):**
1. Systemwide sales (+5%, +4% cc) and loyalty engagement (+13% 90-day actives to ~220M) are still compounding
   even while US in-restaurant traffic is soft — the platform is bigger than the comp-sales headline.
2. Operating margin has already recovered from a Q1 2026 trough (45.3%) back to 47.0% in Q2 2026, suggesting the
   value-menu-driven margin pressure is moderating, not structural.
3. At ~2.8%/yr implied growth, the reverse DCF gives a wide margin of safety versus a business with a
   multi-decade record of mid-single-digit systemwide growth even through prior soft-traffic cycles.

**Bear (3):**
1. US comparable sales have now decelerated for three consecutive quarters (to +0.8% in Q2 2026), and
   management's own explanation ("inconsistent restaurant execution," "lower consumer awareness" of value
   offerings) describes an execution problem the company itself has not yet fixed — this could persist.
2. Net debt/EBITDA ≈2.8x on a negative-equity balance sheet leaves little room for a real downturn in
   systemwide sales without credit-metric pressure; MCD's capital-return policy has structurally prioritised
   buybacks/dividends over deleveraging.
3. Franchise-system litigation (Section 11) — while mostly narrowed in McDonald's favour — signals ongoing
   friction in the franchisee relationship that is a second-order but real operating risk for a business
   entirely dependent on franchisee execution and goodwill.

## 9. Key risks & kill criteria (measurable)

1. US comparable sales negative (turning from decelerating-positive to outright negative) for two consecutive
   quarters.
2. Full-year operating-margin guidance (currently "mid-to-high 40% range") formally cut at any quarterly release.
3. Net debt/EBITDA rising above 3.5x (vs. ≈2.8x estimated here).
4. A credit-rating downgrade by S&P/Moody's/Fitch below the current investment-grade tier.
5. Systemwide sales growth (constant currency) below 3% for two consecutive quarters.

## 10. Catalysts & calendar

- Next earnings: **Q3 2026, on or about 22 October 2026** (one source shows a confirmed 22-Oct date; another
  shows an unconfirmed estimate of 29-Oct to 5-Nov — treated here as **estimated**, not confirmed by the company).
- Ongoing: McPherson/Manning-line Black-franchisee discrimination litigation — a federal judge narrowed the case
  significantly on 21-Sep-2026 (dismissing most of ~480 claims across 48 plaintiffs) but did not dismiss it
  entirely; monitor for further rulings or settlement.

## 11. Red-flag scan

- **Litigation:** Black-franchisee racial-discrimination suits (McPherson v. McDonald's USA and related cases)
  — largely narrowed in McDonald's favour on 21-Sep-2026, with some claims allowed to proceed; McDonald's denies
  discriminating. Broader franchise-system disputes over fees/territory continue in the background, as is
  typical for a system this size. No auditor changes, restatements, or going-concern language identified in
  this pass.
- **Leverage:** negative stockholders' equity is longstanding and intentional (see Section 6) — disclosed here
  as a structural fact, not flagged as a new deterioration.
- **Insider selling:** not separately Form-4-audited in this time-boxed pass — a gap to close before upgrading
  conviction.

## 12. Data basis, recency and disclaimer

Most recent period incorporated: **Q2 2026 10-Q (quarter ended 30-Jun-2026), filed 07-Aug-2026**, plus the FY2025
10-K (filed 24-Feb-2026) for full-year detail and guidance. Checked for events to 2026-09-25, including the
21-Sep-2026 franchise-discrimination-suit ruling. All figures are on a **consolidated** basis. GAAP figures throughout; where "adjusted" EPS is quoted
(Q2 2026 $3.38 adjusted vs $3.32 GAAP-diluted per differing secondary sources) it is labelled and not treated as
GAAP. **This is research, not personalized investment advice; it is not a recommendation to buy or sell any
security, and it is not financial advice.**

## 13. Sources

1. SEC EDGAR submissions/companyfacts, CIK 0000063908 (data.sec.gov), retrieved 2026-09-26.
2. McDonald's Q2 2026 10-Q (filed 07-Aug-2026): sec.gov/Archives/edgar/data/0000063908/000006390826000073/mcd-20260630.htm
3. McDonald's Q2 2026 earnings release, Exhibit 99.1: corporate.mcdonalds.com/content/dam/sites/corp/nfl/pdf/MCD%20Q226%20Earnings%20Release%20-%20Exhibit%2099.1.pdf
4. McDonald's Q1 2026 10-Q (filed 07-May-2026): sec.gov/Archives/edgar/data/0000063908/000006390826000051/mcd-20260331.htm
5. McDonald's FY2025 10-K (filed 24-Feb-2026), guidance section (operating margin, capex, unit growth, FCF conversion).
6. "McDonald's race discrimination lawsuit largely dismissed," TheGrio, 24-Sep-2026; Law360, "McDonald's Beats Most Of Black Franchisees' Bias Claims."
7. Investing.com earnings-call transcript summaries, Q1/Q2 2026 (secondary source for management commentary on US traffic execution — flagged as secondary).
8. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (quant context; noted data conflict on TTM FCF, Section 6).
