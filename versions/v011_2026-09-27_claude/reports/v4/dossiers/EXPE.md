# EXPE — Expedia Group, Inc. — F20 diligence dossier

## 1. Verdict
**INCLUDE-SMALL** (half weight) — thesis horizon 12–36 months. The valuation cushion here is unusually wide (the price implies *negative* 10-year FCF growth against a company that just raised full-year guidance for the second consecutive quarter), which argues for a full-weight INCLUDE. The reservation that caps it at half weight is specific and very recent: on 23-Sep-2026 (two days before this valuation snapshot) EXPE fell ~7% on reports that Meta's "Muse" AI agent can search, compare and book directly with a hotel or airline — removing the reason a traveller would route through an OTA and the take-rate fee that comes with it. That is a live, structural, unresolved risk to the business model, not yet visible in a single quarter of results, and it should be sized for rather than dismissed because the multiple is cheap.

## 2. Business in plain English
Expedia Group runs online travel brands (Expedia.com, Hotels.com, Vrbo, Orbitz) that let consumers book hotels, flights, cars and vacation rentals, and — increasingly important — a B2B "white-label" business (Expedia Partner Solutions) that supplies travel-booking technology to banks, airlines and other partners under their own brand. It earns a commission/margin (take rate) on gross bookings, not the full travel spend. Competitive position: one of three scaled US-based OTAs (with Booking Holdings and Airbnb) with real technology and inventory-supply moats, but a business model — search-driven customer acquisition — that is exposed to whoever controls the search/discovery layer (historically Google; now also AI agents).

## 3. Why the model likes it — durable or artefact?
Triage (Q02) and b1_live_scores.csv both flag this as a genuine, ongoing acceleration, not a one-off: B2B gross bookings +21% (per Q2 call), EBITDA margin expanding, and — critically — guidance has now been **raised** twice in 2026 (not just met), which rules out the "beat happened because the guide was sandbagged and nothing changed" explanation for at least the full-year outlook. b1 composite percentile is high (live_rank 3, decile 10/quintile 5 — the model's best-ranked name in this batch), driven by strong Value-family and SUE (earnings-surprise) percentiles, consistent with the reverse-DCF finding that the market has not yet priced in the improvement.

## 4. Last quarters — results table (GAAP, USD millions except EPS)
Source: SEC XBRL company facts (`data.sec.gov/api/xbrl/companyfacts/CIK0001324424.json`) for Q3-24 through Q3-25 and Q1/Q2-26 (all directly tagged as discrete 3-month periods); all figures are **consolidated** GAAP. Q4-24 and Q4-25 are not separately tagged in interim XBRL — Q4-25 sourced directly from the 8-K earnings-release exhibit, Q4-24 derived (FY2024 10-K total minus the sum of the three quarterly 10-Qs, labelled).

| Quarter | Revenue | YoY | Op. income (GAAP) | Op. margin | Net income (GAAP) | Diluted EPS (GAAP) | Adjusted EPS |
|---|---|---|---|---|---|---|---|
| Q3-24 | 3,929 | — | 607 | 15.5% | 425 | 2.87 | n/a (not pulled) |
| Q4-24 (derived) | ~3,315 | — | ~371 | ~11.2% | ~548 | ~2.10 (derived) | n/a |
| Q1-25 | 2,889 | — | -110 | -3.8% | -135 | -0.99 | n/a |
| Q2-25 | 3,558 | — | 451 | 12.7% | 386 | 2.80 | n/a |
| Q3-25 | 4,412 | — | 1,036 | 23.5% | 959 | 7.33 | n/a |
| Q4-25 | 3,547 | +6.4%* | 420 | 11.8% | 205 | 1.60 | **3.78** |
| **Q1-26** | **3,426** | **+18.6%** | **251** | **7.3%** | **-6** | **-0.05** | **1.96** |
| **Q2-26** | **4,315** | **+21.3%** | **800** | **18.5%** | **878** | **7.16** | **5.76** |

*YoY vs prior-year XBRL quarters where both are available. Full-year comparison: FY2025 revenue $13.69bn / EPS $8.95 (10-K) vs FY2024 revenue $13.69bn — 2025 total-revenue growth was modest for the full year, with the acceleration concentrated in H2-2025 and 2026 (B2B mix shift).

**GAAP-vs-adjusted flag (a live example of the lead_v3_audit lesson):** Q2-2026 GAAP net income ($878m, EPS $7.16, +188% YoY) grew *faster* than adjusted net income (+29% YoY, adjusted EPS $5.76, +36% YoY) — the reverse of the usual pattern where adjusted exceeds GAAP. Management's own reconciliation attributes this to a favourable, non-recurring tax item plus the adjusted metric's use of a normalised long-term tax rate; adjusted EPS growth (+36%) is the more decision-useful, comparable figure and should be used for any run-rate extrapolation — **do not annualise the $7.16 GAAP EPS.**

## 5. Guidance track record (four most recent releases, quoted numbers)
| Release | Guided | Actual | Result |
|---|---|---|---|
| Q4-25 (Feb-26) | FY26 gross bookings +6–8%; Q1-26 GB +10–12% | Q1-26 GB +13%, revenue +15% | **Beaten** above the top of the Q1 range |
| Q1-26 (May-26) | FY26 unchanged: GB $127–129bn (+6–8%), rev $15.6–16.0bn (+6–9%), EBITDA margin +100–125bps; Q2-26 GB $32.5–33.1bn (+7–9%), rev $4.11–4.19bn (+9–11%) | Q2-26 GB +12%, revenue +14% | **Beaten** above the top of the Q2 range; FY guide held (not yet raised) |
| Q2-26 (Aug-26) | **FY26 raised**: GB $129.5–130.8bn (+8–9%, up from $127–129bn/+6–8%), revenue $16.05–16.22bn (+9–10%, up from $15.6–16.0bn/+6–9%), EBITDA margin expansion +150–175bps (up from +100–125bps) | *(pending — reports 29-Oct-2026)* | — |

Two consecutive quarters of beat-and-hold followed by a genuine full-year raise (not just a beat) is a stronger guidance-credibility signal than a company that only ever beats a conservative number without ever raising the annual bar.

## 6. Earnings quality & balance sheet
- FCF: FY2025 free cash flow $3,110m (management-reported; TTM figure through H1-2026 quoted by the company as $5,026m for "the first six months of 2026," which reads as a trailing-12-month figure in the release — flagged as ambiguous phrasing in the source document, treated as approximate).
- OCF is structurally seasonal and lumpy: Q1 is strongly cash-generative (advance bookings collected, e.g. +$3.93bn OCF in Q1-2026) while Q3 typically shows a cash *outflow* (e.g. −$1.49bn in Q3-2024) as travel is delivered and merchant-model payables to hotels/airlines are settled — this is normal for the OTA merchant model, not a red flag, but means quarterly OCF/FCF should never be read in isolation.
- SBC: ~$100–115m/quarter, roughly 2.5–3% of quarterly revenue — modest and stable, not a distortive share of the P&L.
- Balance sheet (30-Jun-2026): cash & equivalents $6,682m + short-term investments $445m = $7,127m; long-term debt (noncurrent) $5,459m → **net cash ~$1,668m** (matches V1's independently sourced net-debt figure exactly). Total assets $29,061m. Diluted shares 114.5m (Q2-26), down from ~117.0m (Q4-25) — active buyback (~880k shares / $200m repurchased in Q2-26 alone; FY2025 repurchased ~9m shares for $1.7bn).
- No pending M&A or pending-deal exclusion flag found; no pending debt-maturity wall identified in the window reviewed.

## 7. Valuation snapshot — V1 says attractive; I agree, with one reservation
`v4/outputs/v1_valuation.json` / `v1_valuation_table.csv` (as of 2026-09-25, price $264.17): NTM P/E 11.2x, own-history percentile **1.3rd** (essentially the cheapest EXPE has ever traded on this measure across 156 months), peer median (Hotels/Resorts/Cruise sub-industry, n=8, incl. ABNB/BKNG/CCL/HLT) 13.1x. FCF yield 10.8% (SBC-adjusted 12.5%). WACC 9.77% (beta 1.29 Blume-adjusted). **Reverse DCF: the price implies FCF *declining* ~1.5%/yr for 10 years** — against a trailing 5-year delivered FCF CAGR of +22.1%, a 10-year delivered CAGR of +7.3%, and sell-side consensus FY1 growth of +7.1%. Street 12-month target range $235–430 (mean $339) brackets the current $264.17 price on the low side — "within Street target range," not an outlier call. V1 verdict: **attractive** (score 0.485), base-case 3-year annualised return **+5.3%**, bear **−31.3%**, bull **+66.5%**.

**My view: cheap, and I agree with V1.** The implied growth (−1.5%/yr) is below every historical and consensus reference point, including a scenario where Muse-style AI agents materially erode OTA take rates over the coming decade — it would take a genuinely severe disintermediation outcome (not merely "AI agents exist") to justify pricing FCF as a *shrinking* asset for ten years, especially with B2B (which does not depend on Expedia's own consumer-facing search rankings in the same way) now the fastest-growing, highest-margin segment. `implied_vs_base = below`. The AI-agent risk is real enough, and fresh enough (2 days old at the valuation date), to keep this at INCLUDE-SMALL rather than full weight until at least one more quarter's data shows whether Muse-style agents are actually diverting volume.

## 8. Bull case
1. B2B (Expedia Partner Solutions) is the fastest-growing, highest-incremental-margin segment and is structurally less exposed to consumer search/AI-agent disintermediation, since the partner (a bank, an airline) — not Expedia's own SEO/SEM — drives the customer relationship.
2. Valuation is priced for FCF decline versus a company that just raised full-year guidance twice in six months; even a moderate deceleration to consensus-level growth (+7%) would be well above what is priced in.
3. Balance sheet is net-cash and buying back stock aggressively (~$1.7bn in FY2025, another ~$200m in Q2-26 alone) at a multiple management evidently views as cheap.

## 9. Bear case
1. **Muse (Meta) and equivalent AI-agent booking tools are a genuine structural threat** — an agent that can search, compare and complete a booking directly with the underlying supplier removes both Expedia's traffic-acquisition role and its take-rate fee; this is not a hypothetical, it moved the stock 7% in a day industry-wide (EXPE, ABNB, BKNG all fell together on 23-Sep-2026).
2. A wrongful-death lawsuit tied to a Vrbo listing's smoke-detector disclosures is a live reputational and legal tail risk for the Vrbo brand specifically, at a time when Vrbo is supposed to be recovering.
3. Q2-2026's headline GAAP EPS growth (+188%) is inflated by a favourable tax item versus a much slower +29% adjusted net-income growth — a reminder that the "cheap on trailing P/E" read can be optically flattered by non-recurring items in exactly the way v3's process was criticised for missing.

## 10. Key risks & kill criteria (measurable)
1. Gross bookings growth falls below 5% YoY for two consecutive quarters (a proxy for AI-agent-driven volume diversion actually showing up in the numbers).
2. B2B gross bookings growth (the segment carrying the bull case) decelerates below 10% YoY for two consecutive quarters.
3. Full-year guidance is cut (not merely held) at any subsequent quarterly release.
4. Net debt/EBITDA (TTM EBITDA ≈ EBIT $2,507m + D&A $901m ≈ $3,408m; current net debt ≈ $1,668m net cash, i.e. currently net-cash) turns net-debt-positive by more than 1.0x EBITDA without a clearly value-accretive acquisition.
5. A court ruling or regulatory finding materially adverse to Expedia in the Vrbo wrongful-death litigation.

## 11. Catalysts & calendar
- Next earnings: **Q3-2026, 29-Oct-2026 after market close** (confirmed).
- Watch for further AI-agent/OTA-disintermediation commentary industry-wide (Muse, Google AI Mode, OpenAI shopping features) — this is now a live theme, not a background risk factor.
- No investor day, lock-up or index event identified in the window reviewed.

## 12. Red-flag scan
- **Litigation:** Vrbo wrongful-death lawsuit (smoke-detector disclosure) — active, reputational risk to a recovering brand; no dollar exposure quantified in the sources reviewed. Historical Helms-Burton (Cuba) litigation and a resolved 2021 stockholder Special Litigation Committee matter — both legacy/resolved, not current risk.
- **Accounting:** no restatement, no auditor change, no going-concern language identified. GAAP-vs-adjusted EPS divergence in Q2-26 flagged above and explained by management, not a fraud indicator, but a reason to prefer adjusted figures for trend analysis.
- **Regulatory / SEC:** no active SEC investigation into Expedia or Vrbo found in the sources reviewed (explicitly checked and not found — absence of evidence, not proof of absence, given the time-boxed search).
- **Insider activity:** not separately pulled within this time box (gap disclosed).
- **Competitive/technology:** the Muse/AI-agent story is the single most important new fact this quarter and is flagged prominently above rather than buried in a risk-factor list.

## 13. Sources
1. SEC EDGAR — EXPE submissions & XBRL company facts: `https://data.sec.gov/submissions/CIK0001324424.json`, `https://data.sec.gov/api/xbrl/companyfacts/CIK0001324424.json` (retrieved 2026-09-26).
2. Expedia Q4-2025, Q1-2026 and Q2-2026 earnings releases (8-K exhibits): `.../000132442426000005/earningsrelease-q42025.htm`, `.../000132442426000031/earningsrelease-q12026.htm`, `.../000132442426000051/earningsrelease-q22026.htm`.
3. `v4/outputs/v1_valuation.json` and `v1_valuation_table.csv` (internal, this program) — systematic reverse-DCF valuation, 2026-09-25.
4. Simply Wall St News, "Expedia Stock Faces New AI Booking Threat From Muse," Sept 2026; 24/7 Wall St / AOL, "Travel Booking Stocks Tumble as Muse Threatens to Bypass Them," 23-Sep-2026.
5. Skift, "Expedia Bets Against the All-Powerful AI Travel Agent," 23-Sep-2026.
6. GeekWire / Skift, coverage of Expedia's 10-K agentic-AI risk-factor language, Q4-2025 10-K.
7. `v4/data/b1_live_scores.csv`, `v4/outputs/Q02_triage.json` (internal, this program).

## 14. Data basis, recency and disclaimer
Most recent period incorporated: **Q2-2026, 10-Q filed 2026-08-06** (period end 2026-06-30). Checked for events to **2026-09-25**, including the 23-Sep-2026 Muse/AI-agent sell-off, which is incorporated into the valuation view above (the $264.17 price used already reflects that news). GAAP figures are labelled GAAP; "adjusted EBITDA," "adjusted EPS" and "adjusted net income" are management's own non-GAAP measures, quoted from the earnings releases and explicitly labelled — the Q2-26 GAAP/adjusted divergence is called out rather than smoothed over. **This is research, not personalized investment advice.**
