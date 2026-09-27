# XOM — ExxonMobil Corporation — F59 diligence (2026-09-26)

## 1. Verdict
**WATCH** (12–36 month thesis horizon). ExxonMobil is the highest-quality, lowest-leverage integrated major with genuine multi-year production growth (Permian, Guyana), but roughly half of the last two quarters' earnings strength is a **war-driven oil-price spike** (2026 Iran war / Strait of Hormuz disruption) rather than the durable Permian/Guyana ramp the market is also paying for. On a normalized (pre-spike) FCF base the current close prices in ~4.4%/yr perpetual FCF growth (below XOM's own production plan) — cheap on that basis — but the trailing multiple (20.7x) and NTM multiple (14.2x) sit on top of an earnings run-rate that is not sustainable at post-war oil prices, and the analyst's normalized base case is closer to "fair" than "cheap" once the war premium is stripped out. This differs from the triage call (ADVANCE, quality 5/growth 4/price_vs_growth 3, "cheapest-in-class 14.2x") by adding the earnings-normalization adjustment triage could not do from a data card alone.

## 2. Business in plain English
ExxonMobil explores for, produces, refines and markets oil, natural gas and petrochemicals globally. It sells crude oil and refined products (gasoline, diesel, jet fuel, chemicals) to industrial customers, retailers and consumers. It makes money on the spread between what it costs to find/produce/refine a barrel and what the market pays for the refined product; its economics are exposed to global crude and refining-margin cycles but partly insulated by owning the lowest-cost production per barrel among its integrated-major peers (Permian shale, Guyana deepwater) and by vertically integrating upstream-to-chemicals.

## 3. Why the model likes it — durable or artefact?
b1 quant context (`data/b1_live_scores.csv`, live_rank 99/503, composite decile 9): earnings-yield percentile 0.28 and FCF-yield percentile 0.26 are unremarkable; the real driver is momentum (`mom_12_1` = +47.9%, `pct_mom_12_1` = 0.98, i.e. top-2% 12-month price momentum) and SUE (+6.6, near-maximum earnings-surprise percentile). **Both of those inputs are largely an artefact of the same war-driven oil-price spike, not a durable re-rating** — Q2 2026 EPS beat consensus mainly because Brent/WTI moved with the Iran-war shock (Brent low-$60s in late June 2026 → back over $100 by late July/August; EIA/OilPrice.com, CNBC 2026-07-31/2026-04-21). Quality-family inputs (leverage percentile 0.69, low net debt) are durable and real. **Data conflict:** `b1_live_scores.csv`'s `cik` field for XOM is 2115436; the correct SEC CIK is 0000034088 (confirmed via SEC EDGAR company search) — flagged as a vendor-data error, not used for any filing lookup below.

## 4. Last ~8 quarters (GAAP, consolidated ExxonMobil; $ millions except EPS; source: 10-Q/10-K XBRL, `us-gaap:Revenues`/`NetIncomeLoss`/`EarningsPerShareDiluted`, `data.sec.gov/api/xbrl/companyfacts/CIK0000034088.json`, cross-checked against the Q2 2026 10-Q's own R2.htm statement)

| Quarter | Revenue | YoY | Net income (attrib. XOM) | Diluted EPS |
|---|---|---|---|---|
| Q3 2024 | $90,016M | — | $8,610M | n/a |
| Q4 2024 | $83,426M (derived: FY24 $349,585M − 9mo $266,159M) | — | $7,610M (derived) | n/a |
| Q1 2025 | $83,130M | −0.3% vs Q1'24 | $7,713M | $1.78 |
| Q2 2025 | $81,506M | −12.4% | $7,082M | $1.64 |
| Q3 2025 | $85,294M | −5.2% | $7,548M | n/a |
| Q4 2025 | $82,308M (derived: FY25 $332,238M − 9mo $249,930M) | −1.3% | $6,501M (derived) | n/a |
| Q1 2026 | $85,138M | +2.4% | $4,183M | $1.00 |
| **Q2 2026** | **$116,017M** | **+42.3%** | **$14,525M** | **$3.48** |

Q2 2026 is the outlier: revenue +42% YoY, NI +105% YoY. Per ExxonMobil's own Q2 2026 earnings release (investor.exxonmobil.com, 2026-07-31) and CNBC (2026-07-31, "Exxon and Chevron profits surge on rising oil prices due to Iran war"): drivers were rising oil prices, record Permian production, no Kazakhstan disruption (vs. Q1), and a refining swing from a **$1.3bn Q1 2026 loss to a $5.5bn Q2 2026 profit**. Adjusted EPS $3.52 vs GAAP $3.48. H1 2026 revenue $201,155M vs H1 2025 $164,636M (+22.2%); H1 2026 NI attributable $18,708M vs H1 2025 $14,795M (+26.5%). **Adverse fact:** Q1 2026 was the weak quarter of the pair (EPS $1.00, refining loss) — the "last two quarters" jump is not a clean acceleration, it is high variance around a war-disrupted refining and pricing environment.

## 5. Guidance track record
ExxonMobil does not give quarterly EPS/revenue guidance in the way tech/semis do; it guides capex and the buyback pace and updates its multi-year corporate plan.
- **FY2026 capex:** guided $27–29bn, **maintained** unchanged through 2026 (Hudson Labs Q2 2026 preview; ExxonMobil Q1 2026 8-K, investor.exxonmobil.com).
- **Buyback pace:** $20bn/yr in 2025, **maintained** at that pace through 2026 "assuming reasonable market conditions" (ExxonMobil IR).
- **2030 corporate plan:** raised Dec 2025 — cumulative 2030 earnings/cash-flow potential lifted by ~$5bn **without raising capital spending**; upstream production target confirmed at 5.5 mmboe/d by 2030, with "advantaged assets" (Permian/Guyana/LNG) rising to 65% of volumes (corporate.exxonmobil.com, 2025-12-09). This is a genuine guidance **raise**, not an artefact of the oil-price spike (published before the Iran-war price move fed through to results).

## 6. Earnings quality & balance sheet
**Entity scope: all figures below are consolidated ExxonMobil Corporation** (condensed consolidated balance sheet/cash-flow statement, Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-03, tables R5/R7 of the filing's financial-statement viewer).
- **Balance sheet (30 Jun 2026 vs 31 Dec 2025):** Cash $10,588M (Dec-25: $10,681M). Notes/loans payable (current) $10,139M; long-term debt $32,229M → **gross consolidated debt $42,368M**, net debt **≈$31,780M**. Total equity $266,111M (ExxonMobil share $259,380M + NCI $6,731M). Total assets $464,482M. **Net debt/annualized-Q2-EBITDA is near 0.3–0.4x** and net debt/TTM-normalized-FCF (using FY2025 FCF, see §7) is ~1.3x — both consistent with triage's cited "0.5x net debt/EBITDA," among the lowest leverage of any energy major.
- **Cash flow (H1 2026 vs H1 2025, consolidated statement of cash flows):** OCF $32,260M (H1'25: $24,503M); capex (additions to PP&E) $12,997M (H1'25: $12,181M) → **H1 2026 FCF ≈ $19,263M**. Buybacks (common stock acquired) $10,007M; dividends to XOM shareholders $8,633M — shareholder distributions ($18,640M) below OCF, self-funded.
- **FY2025 (full year, less distorted by the single-quarter war spike):** OCF $51,970M, capex $28,358M → **FY2025 FCF = $23,612M** (10-K FY2025, filed 2026-02-18). This is the base used for the reverse DCF below because H1 2026 annualized (~$38.5bn) is inflated by the Q2 spike.
- **Share count:** diluted shares outstanding fell from ~4.31bn (Mar-25) to ~4.14bn (Mar-26), a ~4%/yr reduction pace from buybacks — a real, durable per-share tailwind independent of the oil-price cycle.
- **SBC:** immaterial for an energy major; no material GAAP-vs-adjusted gap outside the always-disclosed "special items" (asset impairments/identified items), which XOM breaks out by segment in its earnings release.

## 7. Valuation snapshot (vs V1: no V1 row exists for XOM — `v1_verdict = null`; d4 live snapshot as of 2026-09-25 close, calendarised)
Price $160.59 (2026-09-25 close), market cap $660.3bn, EV (filing-based net debt) ≈$692.1bn (d4's Yahoo-sourced EV of $705.2bn uses a slightly higher net-debt figure — a minor, disclosed data conflict, not decision-relevant). Trailing P/E 20.7x; **NTM P/E 14.2x** (matches triage); dividend $4.12/share, ≈2.6% yield; FCF yield (Yahoo, TTM) 3.1%; EV/Sales (NTM) 1.7x. Analyst target mean $172.55 / median $174.50 (22 analysts) — 7–9% above spot. Beat-streak: 8 of last 8 quarters beat consensus EPS, average surprise +6.1% (d4 `beats_last8`/`avg_surprise_pct_last8`).

**Reverse DCF (own construction; single-stage Gordon growth on normalized FY2025 FCF, WACC 8% for a low-beta, investment-grade integrated major, consolidated basis):**
EV ($692.1bn) = FCF₀×(1+g) / (WACC − g), FCF₀ = $23.612bn → **implied perpetual FCF growth g ≈ 4.4%/yr**. That is *below* XOM's own stated 2030 production-growth plan (5.5 mmboe/d by 2030 from a ~4.7–4.8 mmboe/d base, i.e. mid-single-digit volume CAGR) plus ~4%/yr buyback-driven per-share accretion — so on a **normalized** earnings base the market is not paying for more than XOM's own plan delivers. **However**, if the reverse DCF is instead run off the elevated H1 2026 run-rate (annualized FCF ≈$38.5bn), the implied growth rate falls to roughly flat-to-negative — i.e. the stock is only "cheap" if you believe the current war-elevated oil price is durable. **My view: fair, not cheap** — the 14.2x NTM multiple already embeds a meaningful chunk of the current elevated strip price; a return to the pre-war ~$65–70 Brent base case would compress both earnings and, likely, the multiple simultaneously.

## 8. Bull case / Bear case
**Bull (3 points):**
1. Genuine, funded multi-year production growth — Permian output on a confirmed 9% CAGR path, Guyana ramping, 2030 plan raised in Dec 2025 without extra capex.
2. Lowest leverage among integrated majors (net debt ≈$31.8bn on $266bn equity) gives capacity to sustain the $20bn/yr buyback through a commodity downturn that would force peers to cut.
3. If Iran-war disruption to Strait of Hormuz flows persists or recurs, XOM's refining and upstream mix captures disproportionate upside (Q2 2026 showed the operating leverage: refining alone swung $6.8bn quarter-over-quarter).

**Bear (3 points):**
1. Reverse DCF off the actual H1 2026 run-rate implies close to zero further growth is priced for — i.e. much of the "cheap 14.2x" read is an artefact of using a spike-quarter EPS in the denominator; a real reverse DCF off FY2025 normalized FCF is closer to fair value.
2. Oil-price mean reversion risk is unusually high right now: Brent swung $61→$118→$70→$109 within 2026 alone (OilPrice.com; CNBC timeline, 2026-04-21) on a live geopolitical conflict — a ceasefire or de-escalation could reverse Q2's refining/upstream tailwind quickly.
3. California's SB253/261 climate-disclosure litigation (XOM is the plaintiff, suing to strike the laws down, E.D. Cal., filed ~Oct 2025) and the broader California AG climate-deception suit represent ongoing legal/regulatory tail risk and disclosure-compliance cost, even though XOM's own suit is offensive, not defensive.

## 9. Key risks & measurable kill criteria
1. **Brent crude average below $65/bbl for two consecutive quarters** (a return toward XOM's own long-run planning price) without a corresponding capex cut — would invalidate the "cheap on normalized FCF" thesis.
2. **Quarterly refining segment posts a loss for two consecutive quarters** (as it did in Q1 2026) — signals margin normalization is structural, not one-quarter noise.
3. **Net debt rises above $60bn** (roughly 2x the current level) — would break the "lowest-leverage major" thesis that justifies holding through a commodity downturn.
4. **Buyback pace cut below $15bn/yr run-rate** — a direct signal management no longer sees the stock, or FCF, supporting the current $20bn/yr distribution plan.
5. **FTC Pioneer consent order breach or reopening** (five-year board-composition restriction on Pioneer-affiliated directors, through ~2029) — would reintroduce integration/antitrust overhang; currently compliant (FTC denied Sheffield's petition to reopen, 2025-07, ftc.gov).

## 10. Catalysts & calendar
- **Next earnings: 2026-10-30** (Q3 2026, per d4 snapshot).
- Iran-war ceasefire/de-escalation talks (macro catalyst, not company-specific) — any durable resolution is the single biggest swing factor for the next two quarters' refining and upstream results.
- California SB253/261 litigation ruling (E.D. Cal.) — timeline not yet set as of 2026-09-25.

## 11. Red-flag scan
- **Litigation:** XOM v. California (SB253/261 climate-disclosure First Amendment challenge, filed by XOM, E.D. Cal., ~Oct 2025 — offensive, not a liability accrual); separate, longer-running California AG climate-deception suit (People of California v. ExxonMobil et al.) continues in the background — no quantified accrual identified in the filings reviewed.
- **Antitrust:** FTC final consent order on the Pioneer acquisition (bars Scott Sheffield and, for five years, most Pioneer-affiliated individuals from the XOM board); FTC denied Sheffield's petition to reopen the order, 2025-07-— compliant, not a going-forward red flag absent a breach.
- **Auditor/restatement:** none identified in the filings reviewed for the periods covered.
- **Insider selling:** not separately reviewed this pass (time-boxed); flagged as an open item, not a finding either way.
- **No going-concern language; no material-weakness disclosure identified for XOM in the periods reviewed.**

## 12. Sources
1. SEC EDGAR company facts, XOM (CIK 0000034088): `https://data.sec.gov/api/xbrl/companyfacts/CIK0000034088.json` (retrieved 2026-09-26).
2. XOM Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-03, accession 0000034088-26-000093: `https://www.sec.gov/Archives/edgar/data/34088/000003408826000093/0000034088-26-000093-index.htm`; statement tables R2/R5/R7.
3. XOM Form 10-K FY2025, filed 2026-02-18, accession 0000034088-26-000045.
4. ExxonMobil Announces Second-Quarter 2026 Results, investor.exxonmobil.com, 2026-07-31.
5. CNBC, "Exxon and Chevron profits surge on rising oil prices due to Iran war," 2026-07-31.
6. CNBC, "A timeline of how the Iran war shook oil prices — and what comes next," 2026-04-21.
7. OilPrice.com, "Oil Prices Surge 3.7% as U.S.-Iran Standoff Triggers Higher 2026 Forecasts."
8. ExxonMobil, "ExxonMobil Raises Its 2030 Plan," corporate.exxonmobil.com, 2025-12-09.
9. Hudson Labs, "Exxon Mobil Q2 2026 Earnings Preview," hudson-labs.com.
10. FTC, "FTC Denies Sheffield's Petition to Reopen and Set Aside the Exxon-Pioneer Final Order," ftc.gov, 2025-07.
11. ESG Today / S&P Global / ESG Dive, "ExxonMobil sues California over climate disclosure laws," Oct 2025.
12. `v4/data/b1_live_scores.csv`, `v4/data/d4_live_snapshot.parquet` (as_of 2026-09-25), `v4/outputs/Q03_triage.json`.

## 13. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (quarter ended 2026-06-30), Form 10-Q filed 2026-08-03. FY2025 10-K (filed 2026-02-18) used for normalized full-year FCF. Events checked to 2026-09-25 (market close cutoff) via SEC EDGAR filing history and web search. All dollar figures above are GAAP as reported by ExxonMobil unless explicitly labeled "adjusted" (Q2 2026 adjusted EPS $3.52 vs GAAP $3.48). **This is research, not investment advice — not personal investment advice.**


---
## Correction (lead, 26 Sep 2026, from auditor A1 loop 6; original text above left unchanged)
- The data_conflict about XOM's SEC identifier is resolved, not an error: in an August 2026 reorganisation SEC began listing the XOM ticker under **ExxonMobil Holdings Corp (CIK 2115436)**, which appears as a co-registrant on filings of Exxon Mobil Corporation (CIK 34088, the entity whose 10-Q and 10-K this dossier cites). Both identifiers are real; the program's price and fundamentals lineage already links them (outputs/b1_report.md, lineage fix). Verdict unchanged (WATCH).
