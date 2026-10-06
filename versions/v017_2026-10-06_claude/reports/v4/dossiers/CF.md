# CF Industries Holdings, Inc. (NYSE: CF) — Diligence Dossier

Agent f7 | Prepared 2026-09-26 | Most recent period incorporated: Q2 2026 (10-Q filed 2026-08-06, period ended 2026-06-30); checked for events to 2026-09-25. Sector routing: GICS Materials / Fertilizers & Agricultural Chemicals → **chemicals-cement.md** playbook ("Agricultural Inputs" row), with the **Deep Cyclicals** overlay (`13-situations.md` §2) as the governing lens throughout.

**Data quality note:** GAAP figures are sourced from SEC XBRL/filings and carry a filing citation; NTM consensus, analyst targets and estimate-revision history are aggregator-sourced (Yahoo-derived, via the internal `d4` pipeline) and are cross-checks/context only, labelled as such throughout. Mid-cycle figures in §7 are this analyst's estimates built per the deep-cyclical method, with the margin assumption and its sensitivity stated explicitly. Auditor tenure/CAM detail and Form-4 transaction codes were not independently verified in this pass (see §11). **This dossier is research for an internal, self-directed portfolio process — it is not personalised investment advice, and it is not a solicitation to buy or sell any security; the reader is responsible for their own decisions.**

## 1. Verdict

**REJECT** (for a diversified $50–100k moderate-risk account at today's price; revisit as **WATCH** on a pullback toward mid-cycle valuation, roughly $85–95/share, or on independent-source confirmation that the Iran-related nitrogen supply loss is becoming structural rather than a reversible war disruption). Thesis horizon if revisited: 12–36 months.

**One-sentence reason:** Every marker in the deep-cyclical "peak" checklist is flashing simultaneously — Q2 2026 operating margin (50.5%) is *above* the prior all-time-high quarter (2022) **[Corrected 2026-10-06: wrong: Q1 2022 (57.8%) and Q2 2022 (52.5%) were higher than 50.5%; Q2 2026 sits inside the 2022 peak range]**, the quant model's Value/Momentum scores are being driven by a trailing-earnings base the Street is already marking down in real time, and management itself attributes the spike to a named, live, geopolitical supply shock (the Iran conflict) that outside forecasters expect to fade in 2027 — the textbook low-P/E-at-peak trap.

## 2. Business in plain English

CF Industries is the largest nitrogen fertilizer producer in North America, making ammonia, granular urea, UAN (urea-ammonium-nitrate solution) and ammonium nitrate at plants in the US, Canada and the UK, plus a 50%-owned JV in Trinidad. Customers are agricultural cooperatives, independent fertilizer distributors, commodity traders and industrial buyers (explosives, diesel exhaust fluid, emissions-control reagents). CF makes money on the spread between global nitrogen product prices (set by worldwide supply/demand, since nitrogen is a globally traded commodity) and its own input cost, which is overwhelmingly North American natural gas (~34% of FY2025 production cost per the 10-K) — historically cheaper than the gas Europe and much of Asia pay, which is CF's structural cost-curve advantage. Its competitive position is a low-cost, first-quartile North American producer with scale, deep-water logistics, and a growing low-carbon-ammonia option (Blue Point JV, Donaldsonville CCS).

## 3. Why the model likes it — durable or artefact?

Preliminary QVM percentiles (sector-neutral within Materials, `lead_prelim_rank.csv`): **Q = 0.913** (91st pctile), **V = 0.922** (92nd pctile), **M = 0.788** (79th pctile), preliminary composite = 0.875 (S/earnings-momentum family not yet live). ROE(TTM, pipeline) 28.3%; independently recomputed via `ratios.py` on FY2025 GAAP: ROE 34.7%, ROIC 29.3%, EBIT margin 32.5% — all genuinely high in absolute terms, which is exactly the problem: **both Q and V are largely a function of the trailing-earnings base, and that base is elevated, not typical.** V in particular (earnings yield 9.4%, FCF yield 11.0%, EBIT/EV 15.3%) mechanically looks cheap only because the denominator (trailing/NTM earnings) is a cyclical peak. This is **not a durable Quality signal** — it is a cyclical-margin artefact layered on top of a genuinely well-run, low-cost, low-leverage balance sheet. Momentum (79th pctile) is real (12-1m price return has been strong) but is itself largely a re-rating on the same peak earnings. Strip out the cycle and CF's underlying business quality is good-but-not-exceptional for the sector (10-yr median EBIT margin ~24%, see §7), which is why the Q score should be discounted, not the headline used at face value.

## 4. Last two years of results (quarterly; GAAP; source: 10-Q/10-K XBRL, CIK 0001324404)

| Quarter | Net sales ($M) | YoY growth | Op. margin (GAAP) | GAAP diluted EPS | Notable one-offs (pre-tax) |
|---|---|---|---|---|---|
| Q3 2024 | 1,370 | — | 26.6% | 1.55 | — |
| Q4 2024 (derived: FY–9M) | 1,524 | — | 28.9% | ~1.86 **[Corrected 2026-10-06: reported Q4 2024 diluted EPS was $1.89]** | — |
| Q1 2025 | 1,663 | — | 27.4% | 1.85 | — |
| Q2 2025 | 1,890 | — | 34.3% | 2.37 | — |
| Q3 2025 | 1,659 | +21.1% | 35.0% | 2.19 | Loss on sale of Ince (UK) facility, $23M |
| Q4 2025 (derived: FY–9M) | 1,872 | +22.8% | 33.0% | ~2.56 **[Corrected 2026-10-06: reported Q4 2025 diluted EPS was $2.59 (8-K 0001324404-26-000003)]** | Asset impairment $76M (Donaldsonville electrolyzer $51M + Yazoo City $25M); Yazoo City ammonia-release incident 2025-11-05 |
| Q1 2026 | 1,986 | +19.4% | 43.5% | 3.98 | Orica litigation settlement gain $170M; insurance recovery $25M; 45Q credits $24M |
| Q2 2026 | 2,222 | +17.6% | **50.5%** | 4.73 | Add'l Yazoo City AN-asset impairment $23M; insurance BI recovery $50M; 45Q credits ~$19M |

FY2025 revenue $7,084M (+19.3% YoY); FY2025 GAAP EPS $8.97; TTM (through Q2'26) revenue $7,739M, TTM operating margin **41.1%**, TTM GAAP EPS $13.23 (`d4_live_snapshot.parquet`) **[Corrected 2026-10-06: from filings, TTM GAAP EPS is $13.49 (2.19 + 2.59 + 3.98 + 4.73), so trailing P/E at $114.67 is 8.5x]**. **Acceleration, not deceleration:** margin has stair-stepped up every quarter since Q4 2025, culminating in Q2 2026's 50.5% — above the prior all-time peak quarter (Q1 2022: 57.8%; Q2 2022: 52.5%, i.e. Q2'26 sits inside the 2022 peak range). CF does not publish a distinct "adjusted EPS"; its primary non-GAAP metric is (Adjusted) EBITDA — Q1 2026 $983M, Q2 2026 $1,190M, FY2025 $2,893M, FY2024 $2,284M. GAAP EPS above is *not* cleaned of the one-offs listed in the last column; netting them (H1 2026: –$23M impairment +$25M +$50M insurance +$170M litigation +$43M 45Q credits ≈ +$265M pre-tax non-operating benefit) suggests true underlying H1 2026 operating strength, while still very high, is somewhat below the raw GAAP print.

## 5. Guidance track record (last 4 releases; source: 8-K Item 2.02 exhibits)

| Release | Date | Metric guided | Prior guide | New guide | Verdict vs prior |
|---|---|---|---|---|---|
| Q3 2025 | 2025-11-05 | FY2025 gross ammonia production | ~10.5M tons nameplate (implicit) | "approximately 10 million tons" | Baseline (no distinct prior FY25 quantitative guide found this early) |
| Q3 2025 | 2025-11-05 | FY2025 capex | n/a | "~$925M" ($575M own network + $300–400M Blue Point JV total) | New |
| Q4/FY2025 | 2026-02-18 | FY2026 gross ammonia production | FY2025 actual 10.12M tons | **"approximately 9.5 million tons"** | **Cut** — explicitly due to the Nov-2025 Yazoo City incident |
| Q4/FY2025 | 2026-02-18 | FY2026 capex | ~$925M (FY25) | **"~$1.3B total / ~$950M ex-partner funding"** | **Raised** (Blue Point JV ramp) |
| Q4/FY2025 | 2026-02-18 | Yazoo City restart | n/a (incident 3 months old) | "no production resumption until Q4 2026 at earliest" | New |
| Q1 2026 | 2026-05-06 | FY2026 production/capex | 9.5M tons / $1.3B | Reiterated unchanged | **Maintained** |
| Q1 2026 | 2026-05-06 | Yazoo City restart | "Q4 2026 at earliest" | "late fourth quarter of 2026 at the earliest" | **Maintained** (language tightened slightly) |
| Q2 2026 | 2026-08-05 | FY2026 production/capex | 9.5M tons / $1.3B / ~$950M ex-NCI | Reiterated ("~$950M" + "$40M capitalized interest") | **Maintained** |
| Q2 2026 | 2026-08-05 | **Yazoo City restart** | "late Q4 2026 at earliest" (May-26) | **"first half of 2027"** | **CUT** — a real, quotable ~2-quarter slippage on the single most important non-price catalyst in this name |

CF does not give formal EPS or revenue guidance (consistent across all four releases reviewed); it guides production volumes, capex, and (via separate press releases) share buyback/dividend actions. The Yazoo City timeline slip between the May and August 2026 releases is the clearest "guidance cut" in the window and should not be missed by only reading headline production/capex numbers, which were held flat.

## 6. Earnings quality & balance sheet

**FCF conversion:** FY2025 FCF (CFO $2,752M – capex $950M) = $1,802M; FCF/NI ≈ 1.24x (healthy, aided by D&A > maintenance capex historically). **`ratios.py` quality warning:** capex ran below 90% of depreciation in FY2022–FY2024 (0.53x–0.57x) — consistent with under-investing in / harvesting the existing asset base during that window, which flattered FCF; FY2025 capex/depreciation flipped to 1.06x as Blue Point JV and Yazoo-City-rebuild capex ramped, and management guides ~$950M own-account capex for FY2026 (vs. ~$900M annual D&A) — i.e. the FCF tailwind from under-depreciation is now reversing. **SBC** is small (~0.5–0.6% of revenue: $45M SBC / $7,084M FY2025 revenue). **GAAP-vs-adjusted gap:** CF publishes GAAP EPS and Adjusted EBITDA only (no adjusted EPS); H1 2026 GAAP results embed a **$170M unexplained-at-first litigation settlement gain** (subsequently identified via web search: Orica/Nelson Brothers AN-purchase-agreement litigation settled March 2026, cash received April 2026) plus insurance recoveries netting against Yazoo City impairments — a combined ~$265M pre-tax of non-recurring items inflating H1 2026 GAAP income. **Leverage:** net debt/EBITDA (trailing, FY2025) **0.39x**; gross debt/EBITDA 1.01x; interest coverage 14.8x EBIT / 20.6x EBITDA — very safe on a trailing basis. On a **mid-cycle EBITDA** basis (§7, ~$2.6B), net debt/mid-cycle-EBITDA is still only ~0.5x — CF's balance sheet would comfortably survive the next trough; this is a genuine strength, independent of the cyclical-earnings problem. **Debt maturities:** four series of senior notes, $743M–$989M each, maturing 2034/2035/2043/2044 — no refinancing wall in the foreseeable trough years; $750M revolver undrawn, no L/Cs outstanding, in full covenant compliance (10-Q). **M&A/financing:** Blue Point One JV (CF 40% / JERA 35% / Mitsui 25%, formed April 2025) is consolidated as a VIE; CF funded $156M of its capital calls in H1 2026; no CF-level debt raised for it (equity-funded pro rata by partners). **Share count:** aggressive, sustained buybacks through *both* the trough and peak — diluted shares fell from 233.9M (2017) to 162.2M (2025), a cumulative ~31% reduction over 8 years including the 2024 trough year, then a further ~10% cut in 2025 alone (16.6M shares, $1.34B); new $2.0B authorization (Oct 2025) had ~$1.48B remaining as of Q2 2026. Quarterly dividend raised 20% in July 2026 (to $0.60/share) — a genuine capital-return positive, but also a classic "high yield declared on peak EPS" signature per the Deep Cyclicals checklist (§2.1).

## 7. Valuation snapshot

| Basis | P/E | EV/EBITDA | FCF yield |
|---|---|---|---|
| Trailing TTM (pipeline, EPS $13.23) | 8.67x | — | — |
| FY2025 GAAP (own calc, `ratios.py`) | 10.2–11.9x (basic vs. current-share-count convention) | 5.8x | 10.4% (mkt cap) |
| NTM consensus (d4, EPS≈$12.07, calendarised) | 9.50x | — | — |
| **Mid-cycle (this dossier)** | **~14.2x** | **~7.1x** | **~9.0%** |

**Mid-cycle build (`13-situations.md` §2.2 method):** 10-year (2016–2025) GAAP operating-margin range is 3.7% (2016 trough) to 48.2% (2022 peak) — a >13x span, unambiguously a deep cyclical. **Median** (not mean) margin over that window ≈ **24%**. Applying 24% to FY2025 revenue ($7,084M, a reasonable current-capacity proxy) gives mid-cycle EBIT ≈ $1,700M; after normalized interest (~$150M) and a 21% normalized tax rate, mid-cycle net income ≈ $1,224M → **mid-cycle EPS ≈ $8.10** on ~151M current shares. At today's price ($114.67) that is **14.2x mid-cycle earnings** — above the framework's 10–14x indicative anchor — versus the 8.7x trailing multiple that makes the stock look cheap. Mid-cycle EV/EBITDA (EBITDA ≈ EBIT + ~$900M normalized D&A = $2.6B) is **7.1x**, inside the 5–8x heavy-industry anchor, i.e. roughly fair-to-full, not cheap. Sensitivity: ±200bps on the margin assumption (22%–26%) moves mid-cycle EPS to roughly $7.20–$9.00 and the implied mid-cycle P/E to 12.7x–15.9x. **`valuation.py` scenario table** (bear: cycle reverts toward trough, EPS $6.00 × 9x; base: mid-cycle, EPS $8.10 × 12x; bull: structural tightness persists + Blue Point optionality, EPS $11.50 × 11x; probabilities 30/45/25): **probability-weighted fair value ≈ $91.6/share, ~20% below the current price.** (A plain perpetuity-style DCF on the same mid-cycle FCF at an 8.5% WACC **[Corrected 2026-10-06: the 8.5% rate is not tied to the 5.17% 10-year Treasury (25 Sep 2026) plus an equity risk premium; a cost of equity near 9.5-10% would reduce the DCF upside]** instead implies ~15–48% *upside* — flagged explicitly as a methodological tension: a DCF that discounts a "mid-cycle" cash flow to perpetuity implicitly assumes that estimate is precise and durable forever, which is exactly the assumption a deep-cyclical framework exists to distrust; the multiple-based scenario table is weighted more heavily here.) Closest peers to sanity-check: Nutrien (NTR, 2026 EPS growth guided ~26.5% per Zacks vs. CF's ~68–84% depending on source — CF is the most extreme swing of the group), Yara International (YAR/YARIY, ~61% 2026 growth), LSB Industries (smaller, more leveraged, similar spread economics) — not independently re-underwritten in this pass; noted as the natural next step before sizing.

## 8. Bull case / Bear case

**Bull (3):**
1. **Live, unresolved supply shock could persist or worsen.** The Iran conflict has curtailed an estimated 50–60% of Middle East ammonia/urea capacity at points in 2026 and shut the Strait of Hormuz to LNG/ammonia exports; if this drags on or escalates, 2027 nitrogen prices could stay elevated well past the current Street expectation of normalization.
2. **Balance sheet and capital return are genuinely best-in-class.** Net debt/mid-cycle-EBITDA ~0.5x, no near-term maturities, $750M undrawn revolver, buybacks sustained through the 2024 trough, dividend just raised 20% — this is not a leveraged cyclical that can be forced into a fire sale in the next downturn.
3. **Structural, non-cyclical optionality is not yet in the price.** Blue Point (1.5M tons nameplate, CF's 40% share, production 2029) and Donaldsonville CCS (45Q credits already flowing, ~$19–24M/quarter and rising) add a genuinely durable, contracted/subsidized earnings stream on top of the cyclical core, which the mid-cycle valuation above does not credit at all.

**Bear (3):**
1. **The central driver of today's margin is explicitly named by management as a war-related supply disruption**, not a structural change — CEO Chris Bohn: "the conflict with Iran has further constrained global nitrogen supply." Outside forecasters (World Bank, CSIS, IFPRI, farmdoc) already expect prices to ease in 2027 as exports recover and new supply (including CF's own Blue Point and competitors') comes online — which is precisely what the FY2027 consensus EPS (-27% vs FY2026, and itself likely still too high) is starting to price.
2. **The Street is cutting numbers in real time, not raising them, for CF specifically** — FY2026 consensus EPS fell from $17.61 (90 days ago) to $15.10 (now), with 6 downward vs. 0 upward revisions in the last 30 days — the opposite pattern to MPC's re-rating, and a sign the peak may already be behind the stock even before a formal top-line reversal shows up.
3. **A major safety incident (Yazoo City ammonia release/explosion, 2025-11-05) triggered a shelter-in-place order for the entire town, a still-unresolved ~$48M+ of impairments, active plaintiff-side litigation solicitation, and a guidance slip on the restart timeline** (Q4 2026 → H1 2027 as of the Aug-2026 release) — a real operational and reputational tail risk layered on top of the cyclical one.

## 9. Key risks & kill criteria (thesis-invalidation triggers)

Any of the following would invalidate the "this is a mid-cycle-normalisation story" thesis and should trigger an active re-underwrite (for REJECT, these are also the conditions that would flip the verdict toward INCLUDE on a future pass):

1. **De-escalation of the Iran conflict / Strait of Hormuz reopening to normal flow** — watch for a >25% pullback in benchmark urea/UAN prices (NOLA/Gulf) within two quarters of any ceasefire or sanctions relief; this is the single biggest swing factor.
2. **Two consecutive quarters of GAAP operating margin below 30%** (i.e. reverting toward the 24% median) would confirm the cycle has turned — exit or re-underwrite at that point rather than before.
3. **Net debt/EBITDA > 2.5x** (mid-cycle-adjusted) would be a genuine balance-sheet concern; currently nowhere close (0.4–0.5x), but watch if Blue Point capital calls or a large debt-financed buyback push this materially.
4. **Yazoo City restart slips again past H1 2027**, or the incident investigation (OSHA/state) results in a materially larger fine/settlement or a permanent capacity reduction at the site.
5. **Global nitrogen capacity additions (Blue Point, Dangote, others) come online faster than 1.5%/yr demand growth absorbs**, per the company's own 10-K framing of the long-run supply/demand balance — a leading indicator of the next down-cycle, visible years before the P&L.

## 10. Catalysts & calendar

- **Next earnings:** ~2026-11-04 (Q3 2026, aggregator estimate — not yet confirmed via an 8-K calendar notice; verify closer to the date).
- Any ceasefire, sanctions, or Strait-of-Hormuz news flow on Iran — the single highest-frequency catalyst for this name right now.
- Blue Point civil construction start (permits received July 2026; construction was slated to begin August 2026) — watch for an on-schedule confirmation or slippage in the Q3 release.
- Yazoo City rebuild progress updates (targeted H1 2027 restart).
- Officer transition: VP/Corporate Controller & Chief Accounting Officer Richard A. Hoker announced retirement (8-K, 2026-09-03), effective **2027-03-03** — routine (retirement, long lead time, no stated dispute), but worth a name-check against any future accounting-related 8-K.
- No lock-up or index-event triggers identified in this pass.

## 11. Red-flag scan

- **Safety/operational:** Yazoo City ammonia release/explosion, 2025-11-05 — town-wide evacuation/shelter-in-place ordered, no injuries reported, site idled; cumulative impairments to date ≈ $48M (AN-asset-group, Q4'25 $25M + Q2'26 $23M) plus a separate, unrelated $51M Donaldsonville electrolyzer impairment (management concluded the project would not earn an acceptable return, pivoted to CCS instead). Plaintiffs'-bar activity (multiple law-firm blog posts soliciting Yazoo County claimants) indicates likely toxic-tort litigation exposure not yet reflected in a specific reserve as of the last filing reviewed.
- **Auditor/controls:** No auditor change, no material weakness, no going-concern language identified in the FY2025 10-K excerpt reviewed; auditor name/tenure and full CAM list were not independently extracted in this pass (source access limitation, not a finding) — verify directly in the 10-K Item 8/9A before final sizing.
- **Investigations/litigation:** No SEC/DOJ/EPA investigation identified. Orica/Nelson Brothers AN-purchase-agreement litigation settled March 2026 in CF's favor (~$170M cash received). PLNL (Trinidad, 50%-owned) faces an ongoing natural-gas-supply contingency — the gas-supply contract with NGC was renewed only through January 2027; non-renewal risk could trigger an impairment of the $36M carrying investment (small in size, but a recurring pattern worth tracking).
- **Insider trading:** 40 Form-4 filings identified in the trailing ~3 months (Mar–May 2026 window pulled), including a 7-filing same-day cluster on 2026-04-30 consistent with scheduled equity-vesting/tax-withholding activity; **transaction codes (sale vs. withholding) were not individually verified in this pass** due to an intermittent SEC-access issue — flagged as a data gap, not a confirmed finding, and should be closed out (via each Form 4's `nonDerivativeTable` transaction code) before relying on "no unusual insider selling" as a clean bill of health, especially given the cluster falls inside the Iran-driven price spike window.
- **Short-seller reports:** None identified via search in this pass.

## 12. Sources

1. SEC EDGAR, CF Industries Holdings CIK 0001324404, XBRL company facts API: `https://data.sec.gov/api/xbrl/companyfacts/CIK0001324404.json` (retrieved 2026-09-26).
2. SEC EDGAR filing index: `https://data.sec.gov/submissions/CIK0001324404.json` (retrieved 2026-09-26).
3. Form 10-Q, period 2026-06-30, filed 2026-08-06: `https://www.sec.gov/Archives/edgar/data/1324404/000132440426000019/cf-20260630.htm`.
4. Form 10-K, FY2025, filed 2026-02-25: `https://www.sec.gov/Archives/edgar/data/1324404/000132440426000007/cf-20251231.htm`.
5. 8-K Ex-99.1, Q2 2026 earnings release (2026-08-05): `https://www.sec.gov/Archives/edgar/data/1324404/000132440426000017/cf-08052026_ex991xearnings.htm`.
6. 8-K Ex-99.1, Q1 2026 earnings release (2026-05-06): `https://www.sec.gov/Archives/edgar/data/1324404/000132440426000011/cf-05062026_ex991xearnings.htm`.
7. 8-K Ex-99.1, Q4/FY2025 earnings release (2026-02-18): `https://www.sec.gov/Archives/edgar/data/1324404/000132440426000003/cf-02182026_ex991xearnings.htm`.
8. 8-K Ex-99.1, Q3 2025 earnings release (2025-11-05): `https://www.sec.gov/Archives/edgar/data/1324404/000132440425000028/cf-11052025_ex991xearnings.htm`.
9. 8-K, officer retirement (2026-09-03): `https://www.sec.gov/Archives/edgar/data/1324404/000110465926105054/tm2624720d1_8k.htm`.
10. SEC EDGAR Form 4 ownership feed, CF CIK 0001324404 (retrieved 2026-09-26): `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001324404&type=4&owner=include&count=40&output=atom`.
11. World Bank Blogs, "Fertilizer prices surge as Strait of Hormuz disruptions tighten supplies" (2026): `https://blogs.worldbank.org/en/opendata/fertilizer-prices-surge-as-strait-of-hormuz-disruptions-tighten-`.
12. CNBC, "Fertilizer prices surge amid Iran war, sparking food security warnings" (2026-03-25): `https://www.cnbc.com/2026/03/25/fertilizer-price-iran-war-food-security-inflation-urea-potash-nitrogen-farmers.html`.
13. CSIS, "Iran, Fertilizer, and Food Security: Risks, Impacts, and Policy Responses" (2026): `https://www.csis.org/analysis/iran-fertilizer-and-food-security-risks-impacts-and-policy-responses`.
14. Local news on Yazoo City incident: Vicksburg Post, WLBT, Mississippi Free Press (November 2025, various dates) — company confirmed no injuries, site idled.
15. v4 pipeline internal data: `v4\outputs\lead_prelim_rank.csv` (Q/V/M/prelim factor scores), `v4\data\d4_live_snapshot.parquet` (NTM consensus, analyst targets, estimate-revision history) — cross-check only, not primary.
16. `ratios.py` and `valuation.py` outputs computed in this pass from the SEC XBRL figures above (inputs archived at `C:\Users\user\AppData\Local\Temp\claude\scratch_f7\cf_ratios_input.json` and `cf_valuation_input.json`).

**Data-quality/limitations note:** auditor name/tenure/CAMs, full risk-factor diff vs. prior year, and Form-4 transaction-code detail were not fully extracted in this pass (noted inline above) — these are the highest-value follow-ups before final position sizing, not blocking issues for the REJECT/WATCH verdict, which rests on the cyclicality evidence in §3, §4 and §7.

## Correction (verification DV08, 2026-10-06)

Auditor DV08 checked this dossier against SEC EDGAR (10-Q acc 0001324404-26-000019, 10-K acc 0001324404-26-000007, 8-K Ex-99.1 of 2025-11-05, 2026-02-18, 2026-05-06, 2026-08-05, 8-K acc 0001104659-26-105054). One wording error (Sec 1) and minor figure slips were found; no verdict-relevant error.

| # | Wrong text | Correct value | Source / accession |
|---|---|---|---|
| 1 | Q4 2024 EPS "~1.86 (derived)" and Q4 2025 EPS "~2.56 (derived)" (Sec 4) | Reported $1.89 and $2.59 | 8-K 0001324404-26-000003 |
| 2 | TTM GAAP EPS $13.23, P/E 8.67x (Sec 4, 7) | TTM GAAP EPS $13.49 from the four reported quarters; trailing P/E 8.5x | Releases / XBRL |
| 3 | Sec 1: Q2 2026 margin 50.5% "above the prior all-time-high quarter (2022)" | Q1 2022 57.8% and Q2 2022 52.5% were higher; Q2 2026 is inside the 2022 peak range | XBRL |
| 4 | Perpetuity DCF at an 8.5% WACC (Sec 7) | Discount rate not tied to the 5.17% 10-year Treasury plus an equity risk premium; about 9.5-10% cost of equity would shrink the upside the dossier already down-weights | Recomputation basis |

Verified and unchanged: Q1 and Q2 2026 net sales, margins, EPS and adjusted EBITDA; the other six quarterly rows (sales, margin); FY2025 revenue, EPS and free cash flow; all guidance quotes (production, capex, Yazoo City restart path of Q4 2026, late Q4 2026, first half of 2027); H1 2026 one-off items ($170M litigation gain, insurance recoveries, impairment, 45Q credits); 2022 peak margins; buyback, dividend and SBC figures; the officer-retirement 8-K. The Orica counterparty name is not in the filings read.

**Verdict change: none.** REJECT stands. No change to `v4/outputs/f7_summary.json`.
