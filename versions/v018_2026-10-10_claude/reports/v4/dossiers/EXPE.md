# EXPE — Expedia Group, Inc. — F20 diligence dossier

## 1. Verdict
**INCLUDE-SMALL** (half weight) — thesis horizon 12–36 months. The valuation cushion here is unusually wide (the price implies *negative* 10-year FCF growth against a company that just raised full-year guidance for the second consecutive quarter) **[Corrected 2026-10-06: the FY2026 guide was held at the Q1 release (7 May 2026) and raised once, at Q2 (5 Aug 2026); acc 0001324424-26-000031 / -000051]**, which argues for a full-weight INCLUDE. The reservation that caps it at half weight is specific and very recent: on 23-Sep-2026 (two days before this valuation snapshot) EXPE fell ~7% on reports that Meta's "Muse" AI agent can search, compare and book directly with a hotel or airline — removing the reason a traveller would route through an OTA and the take-rate fee that comes with it. That is a live, structural, unresolved risk to the business model, not yet visible in a single quarter of results, and it should be sized for rather than dismissed because the multiple is cheap.

## 2. Business in plain English
Expedia Group runs online travel brands (Expedia.com, Hotels.com, Vrbo, Orbitz) that let consumers book hotels, flights, cars and vacation rentals, and — increasingly important — a B2B "white-label" business (Expedia Partner Solutions) that supplies travel-booking technology to banks, airlines and other partners under their own brand. It earns a commission/margin (take rate) on gross bookings, not the full travel spend. Competitive position: one of three scaled US-based OTAs (with Booking Holdings and Airbnb) with real technology and inventory-supply moats, but a business model — search-driven customer acquisition — that is exposed to whoever controls the search/discovery layer (historically Google; now also AI agents).

## 3. Why the model likes it — durable or artefact?
Triage (Q02) and b1_live_scores.csv both flag this as a genuine, ongoing acceleration, not a one-off: B2B gross bookings +21% (per Q2 call), EBITDA margin expanding, and — critically — guidance has now been **raised** twice in 2026 (not just met) **[Corrected 2026-10-06: raised once (Q2); Q1 held the full-year range; the quarterly guides were beaten at Q4-25, Q1 and Q2]**, which rules out the "beat happened because the guide was sandbagged and nothing changed" explanation for at least the full-year outlook. b1 composite percentile is high (live_rank 3, decile 10/quintile 5 — the model's best-ranked name in this batch), driven by strong Value-family and SUE (earnings-surprise) percentiles, consistent with the reverse-DCF finding that the market has not yet priced in the improvement.

## 4. Last quarters — results table (GAAP, USD millions except EPS)
Source: SEC XBRL company facts (`data.sec.gov/api/xbrl/companyfacts/CIK0001324424.json`) for Q3-24 through Q3-25 and Q1/Q2-26 (all directly tagged as discrete 3-month periods); all figures are **consolidated** GAAP. Q4-24 and Q4-25 are not separately tagged in interim XBRL — Q4-25 sourced directly from the 8-K earnings-release exhibit, Q4-24 derived (FY2024 10-K total minus the sum of the three quarterly 10-Qs, labelled).

| Quarter | Revenue | YoY | Op. income (GAAP) | Op. margin | Net income (GAAP) | Diluted EPS (GAAP) | Adjusted EPS |
|---|---|---|---|---|---|---|---|
| Q3-24 | 3,929 | — | 607 | 15.5% | 425 | 2.87 | **[Corrected 2026-10-06: Q3-24 is revenue 4,060 / op income 762 / NI 684 / EPS 5.04; the row shows values that do not match the filing (they look like prior-year columns) (XBRL acc 0001324424-24-000052)]** n/a (not pulled) |
| Q4-24 (derived) | ~3,315 | — | ~371 | ~11.2% | ~548 | ~2.10 (derived) | **[Corrected 2026-10-06: Q4-24 reported: revenue 3,184 / op income 216 / NI 299 / EPS 2.20 (Q4-25 release, acc 0001324424-26-000005)]** n/a |
| Q1-25 | 2,889 | — | -110 | -3.8% | -135 | -0.99 | **[Corrected 2026-10-06: Q1-25 is revenue 2,988 / op income -70 / NI -200 / EPS -1.56 (XBRL acc 0001324424-25-000028)]** n/a |
| Q2-25 | 3,558 | — | 451 | 12.7% | 386 | 2.80 | **[Corrected 2026-10-06: Q2-25 is revenue 3,786 / op income 485 / NI 330 / EPS 2.48 (XBRL acc 0001324424-25-000042)]** n/a |
| Q3-25 | 4,412 | — | 1,036 | 23.5% | 959 | 7.33 | n/a |
| Q4-25 | 3,547 | +6.4%* | 420 | 11.8% | 205 | 1.60 | **[Corrected 2026-10-06: YoY is +11.4% vs 3,184]** **3.78** |
| **Q1-26** | **3,426** | **+18.6%** | **[Corrected 2026-10-06: YoY is +14.7% vs 2,988 (release: 15%)]** **251** | **7.3%** | **-6** | **-0.05** | **1.96** |
| **Q2-26** | **4,315** | **+21.3%** | **[Corrected 2026-10-06: YoY is +14.0% vs 3,786 (release: 14%)]** **800** | **18.5%** | **878** | **7.16** | **5.76** |

*YoY vs prior-year XBRL quarters where both are available. Full-year comparison: FY2025 revenue $13.69bn / EPS $8.95 (10-K) vs FY2024 revenue $13.69bn — 2025 total-revenue growth was modest for the full year, with the acceleration concentrated in H2-2025 and 2026 (B2B mix shift). **[Corrected 2026-10-06: FY2025 revenue was $14,733m and diluted EPS $9.81 (+8% revenue); FY2024 was $13,691m and $8.95 (Q4-25 release, acc 0001324424-26-000005)]**

**GAAP-vs-adjusted flag (a live example of the lead_v3_audit lesson):** Q2-2026 GAAP net income ($878m, EPS $7.16, +188% YoY) grew *faster* than adjusted net income (+29% YoY, adjusted EPS $5.76, +36% YoY) — the reverse of the usual pattern where adjusted exceeds GAAP. Management's own reconciliation attributes this to a favourable, non-recurring tax item **[Corrected 2026-10-06: a $280m gain on minority equity investments ($2.29/share), not a tax item]** plus the adjusted metric's use of a normalised long-term tax rate; adjusted EPS growth (+36%) is the more decision-useful, comparable figure and should be used for any run-rate extrapolation — **do not annualise the $7.16 GAAP EPS.** **[Corrected 2026-10-06: the Q2 reconciliation shows no tax item: the gap is a $280m ($2.29/share) gain on minority equity investments versus a $102m loss a year ago; the tax provision rose to $152m from $101m (acc 0001324424-26-000051)]**

## 5. Guidance track record (four most recent releases, quoted numbers)
| Release | Guided | Actual | Result |
|---|---|---|---|
| Q4-25 (Feb-26) | FY26 gross bookings +6–8%; Q1-26 GB +10–12% | Q1-26 GB +13%, revenue +15% | **Beaten** above the top of the Q1 range |
| Q1-26 (May-26) | FY26 unchanged: GB $127–129bn (+6–8%), rev $15.6–16.0bn (+6–9%), EBITDA margin +100–125bps; Q2-26 GB $32.5–33.1bn (+7–9%), rev $4.11–4.19bn (+9–11%) | Q2-26 GB +12%, revenue +14% | **Beaten** above the top of the Q2 range; FY guide held (not yet raised) |
| Q2-26 (Aug-26) | **FY26 raised**: GB $129.5–130.8bn (+8–9%, up from $127–129bn/+6–8%), revenue $16.05–16.22bn (+9–10%, up from $15.6–16.0bn/+6–9%), EBITDA margin expansion +150–175bps (up from +100–125bps) | *(pending — reports 29-Oct-2026)* | — |

Two consecutive quarters of beat-and-hold followed by a genuine full-year raise (not just a beat) is a stronger guidance-credibility signal than a company that only ever beats a conservative number without ever raising the annual bar.

## 6. Earnings quality & balance sheet
- FCF: FY2025 free cash flow $3,110m (management-reported; TTM figure through H1-2026 quoted by the company as $5,026m for "the first six months of 2026," which reads as a trailing-12-month figure in the release — flagged as ambiguous phrasing in the source document, treated as approximate). **[Corrected 2026-10-06: not ambiguous: $5,026m is the six-month FCF (OCF 5,409 less capex 383); TTM FCF is 3,110 - 3,677 + 5,026 = $4,459m]**
- OCF is structurally seasonal and lumpy: Q1 is strongly cash-generative (advance bookings collected, e.g. +$3.93bn OCF in Q1-2026) while Q3 typically shows a cash *outflow* (e.g. −$1.49bn in Q3-2024) as travel is delivered and merchant-model payables to hotels/airlines are settled — this is normal for the OTA merchant model, not a red flag, but means quarterly OCF/FCF should never be read in isolation.
- SBC: ~$100–115m/quarter, roughly 2.5–3% of quarterly revenue — modest and stable, not a distortive share of the P&L.
- Balance sheet (30-Jun-2026): cash & equivalents $6,682m + short-term investments $445m = $7,127m; long-term debt (noncurrent) $5,459m → **net cash ~$1,668m** (matches V1's independently sourced net-debt figure exactly). Total assets $29,061m. Diluted shares 114.5m (Q2-26), down from ~117.0m (Q4-25) **[Corrected 2026-10-06: these are common shares outstanding excluding 5.5m Class B (total 120.0m); Q2 diluted weighted average was 122.6m]** — active buyback (~880k shares / $200m repurchased in Q2-26 alone; FY2025 repurchased ~9m shares for $1.7bn).
- No pending M&A or pending-deal exclusion flag found; no pending debt-maturity wall identified in the window reviewed.

## 7. Valuation snapshot — V1 says attractive; I agree, with one reservation
`v4/outputs/v1_valuation.json` / `v1_valuation_table.csv` (as of 2026-09-25, price $264.17): NTM P/E 11.2x, own-history percentile **1.3rd** (essentially the cheapest EXPE has ever traded on this measure across 156 months), peer median (Hotels/Resorts/Cruise sub-industry, n=8, incl. ABNB/BKNG/CCL/HLT) 13.1x. FCF yield 10.8% (SBC-adjusted 12.5%). **[Corrected 2026-10-06: SBC was added back; after deducting SBC ($412m TTM) the yield on V1's FCF is about 9.5%, and implied growth on the programme basis (Ke 10.0%) is -1.6% to -5.8%/yr depending on the FCF base]** WACC 9.77% (beta 1.29 Blume-adjusted). **Reverse DCF: the price implies FCF *declining* ~1.5%/yr for 10 years** — against a trailing 5-year delivered FCF CAGR of +22.1%, a 10-year delivered CAGR of +7.3%, and sell-side consensus FY1 growth of +7.1%. Street 12-month target range $235–430 (mean $339) brackets the current $264.17 price on the low side — "within Street target range," not an outlier call. V1 verdict: **attractive** (score 0.485), base-case 3-year annualised return **+5.3%**, bear **−31.3%**, bull **+66.5%**.

**My view: cheap, and I agree with V1.** The implied growth (−1.5%/yr) is below every historical and consensus reference point, including a scenario where Muse-style AI agents materially erode OTA take rates over the coming decade — it would take a genuinely severe disintermediation outcome (not merely "AI agents exist") to justify pricing FCF as a *shrinking* asset for ten years, especially with B2B (which does not depend on Expedia's own consumer-facing search rankings in the same way) now the fastest-growing, highest-margin segment **[Corrected 2026-10-06: B2B is fastest-growing but its adjusted EBITDA margin is 24.8% versus 33.2% for B2C, and fell 258 bps YoY in Q2]**. `implied_vs_base = below`. The AI-agent risk is real enough, and fresh enough (2 days old at the valuation date), to keep this at INCLUDE-SMALL rather than full weight until at least one more quarter's data shows whether Muse-style agents are actually diverting volume.

## 8. Bull case
1. B2B (Expedia Partner Solutions) is the fastest-growing, highest-incremental-margin segment **[Corrected 2026-10-06: Q2 incremental margin: B2B about 13% (EBITDA +$38m on revenue +$284m) versus B2C about 81%]** and is structurally less exposed to consumer search/AI-agent disintermediation, since the partner (a bank, an airline) — not Expedia's own SEO/SEM — drives the customer relationship.
2. Valuation is priced for FCF decline versus a company that just raised full-year guidance twice in six months **[Corrected 2026-10-06: raised once (Q2); held at Q1]**; even a moderate deceleration to consensus-level growth (+7%) would be well above what is priced in.
3. Balance sheet is net-cash and buying back stock aggressively (~$1.7bn in FY2025, another ~$200m in Q2-26 alone) at a multiple management evidently views as cheap.

## 9. Bear case
1. **Muse (Meta) and equivalent AI-agent booking tools are a genuine structural threat** — an agent that can search, compare and complete a booking directly with the underlying supplier removes both Expedia's traffic-acquisition role and its take-rate fee; this is not a hypothetical, it moved the stock 7% in a day industry-wide (EXPE, ABNB, BKNG all fell together on 23-Sep-2026).
2. A wrongful-death lawsuit tied to a Vrbo listing's smoke-detector disclosures is a live reputational and legal tail risk for the Vrbo brand specifically, at a time when Vrbo is supposed to be recovering.
3. Q2-2026's headline GAAP EPS growth (+188%) is inflated by a favourable tax item **[Corrected 2026-10-06: inflated by a $280m minority-investment gain, not a tax item]** versus a much slower +29% adjusted net-income growth — a reminder that the "cheap on trailing P/E" read can be optically flattered by non-recurring items in exactly the way v3's process was criticised for missing.

## 10. Key risks & kill criteria (measurable)
1. Gross bookings growth falls below 5% YoY for two consecutive quarters (a proxy for AI-agent-driven volume diversion actually showing up in the numbers).
2. B2B gross bookings growth (the segment carrying the bull case) decelerates below 10% YoY for two consecutive quarters.
3. Full-year guidance is cut (not merely held) at any subsequent quarterly release.
4. Net debt/EBITDA (TTM EBITDA ≈ EBIT $2,507m + D&A $901m ≈ $3,408m; current net debt ≈ $1,668m net cash, i.e. currently net-cash) turns net-debt-positive by more than 1.0x EBITDA without a clearly value-accretive acquisition.
5. A court ruling or regulatory finding materially adverse to Expedia in the Vrbo wrongful-death litigation.

## 11. Catalysts & calendar
- Next earnings: **Q3-2026, 29-Oct-2026 after market close** (confirmed). **[Corrected 2026-10-06: not confirmed on EDGAR; the d4 snapshot shows 2026-11-05 flagged as an estimate and web sources conflict (29 Oct vs 5 Nov)]**
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

## Correction (verification DVH4, 2026-10-06)

**Sources: Expedia Group (CIK 1324424) 8-K Ex-99.1 acc 0001324424-26-000051 (Q2 2026), -000031 (Q1 2026), -000005 (Q4 2025); 10-Q acc 0001324424-26-000053; XBRL company facts (10-Qs acc 0001324424-24-000052, -25-000028, -25-000042, -25-000051).**

1. **Stale prior-year columns in the results table (FAIL).** Wrong: Q3-24 3,929/607/425/2.87; Q4-24 ~3,315/~371/~548/~2.10; Q1-25 2,889/-110/-135/-0.99; Q2-25 3,558/451/386/2.80; Q4-25 YoY +6.4%; Q1-26 YoY +18.6%; Q2-26 YoY +21.3%; FY2025 revenue $13.69bn / EPS $8.95. Correct: Q3-24 4,060/762/684/5.04; Q4-24 3,184/216/299/2.20; Q1-25 2,988/-70/-200/-1.56; Q2-25 3,786/485/330/2.48; Q4-25 YoY +11.4%; Q1-26 +14.7%; Q2-26 +14.0%; FY2025 revenue $14,733m, EPS $9.81, FY2024 $13,691m / $8.95. Q3-25 through Q2-26 levels are correct.
2. **"Raised guidance twice" (FAIL).** The FY2026 guide was held at Q1 (GB $127-129B, revenue $15.6-16.0B) and raised once at Q2 (to GB $129.5-130.8B, revenue $16.05-16.22B, EBITDA margin +1.5-1.75pts). The Q1 and Q2 quarterly guides were beaten. Wording corrected in s1, s3 and s8, and in the F20 summary.
3. **Q2 GAAP EPS driver (FAIL).** It is a $280m gain on minority equity investments ($2.29/share), not a favourable tax item (tax provision rose to $152m). "Do not annualise GAAP EPS" still holds.
4. **B2B margin claim (FAIL).** Q2-26 adjusted EBITDA margin: B2B 24.8% (down 258 bps YoY) versus B2C 33.2%. B2B is the fastest-growing segment, not the highest-margin one; the bull-case point should not rest on margin.
5. **FCF and SBC (FAIL).** $5,026m is six-month FCF; TTM company-defined FCF is $4,459m (helped by deferred merchant bookings float, +$4,998m in H1). V1's "SBC-adjusted yield 12.5%" is higher than the raw 10.8%, i.e. SBC was added back; deducting SBC ($412m TTM) gives about 9.5% on V1's FCF.
6. **Valuation method (programme basis).** Ke = 5.17% + 1.1675 (Blume of raw 1.25) x 4.14% = 10.00%; equity value $31.70bn; ten years then 3.0%. Implied FCF growth is -5.8%/yr on TTM FCF after SBC of $4,047m, -1.6%/yr on V1's $3,022m, and +1.0%/yr even on a float-free $2.5bn. All sit well below the consensus +7% and dossier base, so **implied_vs_base stays "below"** and the verdict stays INCLUDE-SMALL.
7. Verified, no change: Q2-26, Q1-26, Q4-25 and Q3-25 levels, adjusted EPS, all s5 guidance ranges, net cash $1,668m, TTM EBITDA $3,408m, buyback figures, SBC share of revenue. Press items (Muse, Vrbo suit, next earnings date) are not on EDGAR.

**Verdict:** INCLUDE-SMALL unchanged; implied_vs_base unchanged (below); scenarios unchanged (V1-derived, not recomputed). F20_summary.json: thesis_one_line, key_adverse_facts[2], confidence_in_thesis and reconciliation text corrected; no verdict, implied or scenario values changed.
