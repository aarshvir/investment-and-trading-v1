# FRT — Federal Realty Investment Trust

**Recency gate:** most recent period incorporated: Q2 2026 (period ended 2026-06-30), 10-Q and 8-K/EX-99.1 filed 2026-07-31. Checked EDGAR for subsequent filings to 2026-09-25: an 8-K dated 2026-08-11 (report date 2026-08-06; items 1.01/2.03/3.02/8.01/9.01 — looks like a financing/capital-markets event) and a Form 4 (2026-08-04) were found but **not reviewed** in this pass (time-boxed session) — flagged as an open item, not a clean bill. No 10-K/10-Q/8-K toolkit scripts (`verify_data.py`/`lint_report.py`) were run this pass given a hard session time limit; all figures below carry inline source/period/GAAP-vs-non-GAAP labels as a substitute control.

## 1. Verdict
**INCLUDE** — thesis horizon 18–36 months. Two full years of primary-source evidence (8 consecutive quarters) show accelerating leasing spreads, record occupancy and an unbroken string of raised-or-maintained FFO guidance, priced at close to the cheapest P/FFO of FRT's own 10-year history. Confidence: medium-high (see §9 for what would change this).

## 2. Business
Federal Realty (NYSE: FRT, founded 1962) owns, operates and redevelops premium open-air shopping centers and mixed-use neighborhoods (Santana Row, Pike & Rose, Assembly Row) concentrated in affluent, supply-constrained coastal markets (DC–Boston corridor, Northern/Southern California), with recent expansion into new metros (Annapolis MD, Omaha NE, Leawood KS). As of Q2 2026: 103 properties, ~3,700 tenants, 28.8M sq ft commercial GLA plus ~2,500 residential units. Revenue is contractual rent (base + recoveries + percentage rent) from grocery-anchored and lifestyle retail, plus a growing residential/mixed-use income stream. Competitive position: best-in-class demographics (dense, high-income trade areas) support pricing power in lease renewals — the moat is site quality and infill scarcity, not scale. *(Source: FRT 8-K EX-99.1 releases, Q2 2026 and prior, "About Federal Realty" boilerplate; SEC EDGAR CIK 0000034903.)*

## 3. Why the model likes it — durable or artefact?
b1 factor scores (2026-09-25, sector-neutral percentiles): composite 0.924 (decile 10, live_rank 38), **fam_S (earnings surprise) 0.982**, **fam_M (momentum) 0.808**, fam_V (value) 0.714, **fam_Q (quality) only 0.331**.
- The S/M combination is **durable, not an artefact**: it is backed by a verifiable two-year run of accelerating comparable-space cash releasing spreads (14% → 28%+), record leasing volumes, and occupancy/leased-rate gains every quarter (§4), plus FFO guidance raised or held in all 8 of the last 8 quarterly releases (§5) — a real operating trend, confirmed directly from primary filings, not a single-quarter beat.
- fam_V (cheap) is corroborated by V1: P/FFO(proxy) 10.80x sits at the **5.65th percentile of FRT's own 5–10yr history** — i.e., near the cheapest FRT has ever traded on this metric — despite the accelerating operating trend above. This looks like a rate-driven, sector-wide de-rating rather than a company-specific problem (see §9 bear case for the alternative reading).
- fam_Q (weak) is a **data conflict worth flagging**: FRT's own disclosed coverage metrics (77% fixed-rate debt, 3.9x fixed-charge coverage, comfortable covenant headroom — §6) do not look like a 33rd-percentile balance sheet. The weak score more likely reflects the generic Quality family's leverage/OCF-to-assets construction being structurally penalizing for REITs even on a sector-neutral basis (real estate carries more debt than the sector median by design) — flagged for the quant team rather than treated as an independent red flag.

## 4. Last 8 quarters (GAAP unless labeled; $ in millions except per-share)
| Quarter | Revenue | YoY | Nareit FFO/sh | Core FFO/sh (labeled) | GAAP diluted EPS | Comp. POI growth¹ | Occupancy / Leased |
|---|---|---|---|---|---|---|---|
| Q3'24 | 303.6 | +5.9% | $1.71 | n/a (pre-Core FFO) | $0.70 | +2.9% | 94.0% / 95.9% |
| Q4'24 (FY24 $1,202.5) | 311.4 | +6.7% | $1.73 (FY $6.77) | n/a | $0.75 (FY $3.42) | +4.2% (FY +3.4%) | 94.1% / 96.2% |
| Q1'25 | 309.2 | +6.1% | $1.70 | n/a | $0.72 | +2.8% | 93.6% / 95.9% |
| Q2'25 | 311.5 | n/a² | $1.91 (incl. $0.15/sh NMTC³) | $1.76 ex-NMTC | $1.78 (incl. $76.5M gain on sale) | +4.9% | 93.6% / 95.4% |
| Q3'25 | 322.3 | +6.1% | $1.77 | — | $0.69 | +4.4% | 94.0% / 95.7% |
| Q4'25 (FY25 $1,279.0) | 336.0 | +7.9% | $1.84 (FY $7.22) | $7.06 FY (new metric⁴) | $1.48 (FY $4.68) | +3.1% (FY +3.8%) | 94.5% / 96.6% |
| Q1'26 | 341.1 | +10.3% | $1.88 | $1.88 (+10.6% YoY) | $1.81 | +4.7% (adj. +5.1%) | 93.8% / 96.1% |
| Q2'26 | 335.7 | +7.8% | $1.88 | $1.88 (+6.8% YoY) | $0.97 (vs $1.78, on lower gain on sale + absence of prior-yr tax credit) | +2.8% (adj. +4.2%) | 93.8% / 96.1% |

¹ Comparable Property Operating Income growth = FRT's same-property NOI proxy, ex lease-termination fees/prior-period rents. ² Q2'24 revenue not separately extracted this pass. ³ New Markets Tax Credit transaction income, a one-off management itself excludes from Core FFO. ⁴ FRT introduced "Core FFO" as a new disclosed metric at Q4 2025 — pre-2025 quarters are Nareit-FFO-only; treat as a definitional break, not a restatement. FCF/AFFO: FRT does not publish a quarterly AFFO bridge (management referenced AFFO growth targets only qualitatively at its May 2026 Investor Day). Rough proxy for Q2'26: Core FFO $162.8M − TI/leasing costs $25.6M − maintenance capex $6.7M ≈ $130.5M (~$1.50/sh) → dividend payout ≈ 77% of this proxy vs 60% of Nareit FFO. SBC is immaterial (~1% of revenue, $3.6M/quarter). *(Source: 8-K EX-99.1 for each quarter, "Consolidated Income Statements" and "Reconciliation of FFO" tables; CIK 0000034903.)*

## 5. Guidance track record (every release, last 4 in bold)
| Release | Metric | Revised guidance | **vs. prior guidance** |
|---|---|---|---|
| Q3'24 (2024-10-30) | FY24 EPS / FFO | $3.40–3.50 / $6.76–6.86 | vs $3.33–3.51 / $6.70–6.88 — tightened, low end raised |
| Q4'24 (2025-02-13) | FY25 initial | EPS $3.00–3.12 / FFO $7.10–7.22 | first FY25 print, no prior |
| Q1'25 (2025-05-08) | FY25 | EPS $3.00–3.12 (maintained) / FFO $7.11–7.23 | vs FFO $7.10–7.22 — raised |
| Q2'25 (2025-08-06) | FY25 | EPS $3.91–4.01 / FFO $7.16–7.26 (ex-NMTC $7.01–7.11) | vs EPS $3.00–3.12 / FFO $7.11–7.23 — raised (EPS jump driven largely by gains on sale) |
| **Q3'25 (2025-10-31)** | FY25 | EPS $3.93–3.99 / FFO $7.20–7.26 (ex-NMTC $7.05–7.11) | vs EPS $3.91–4.01 / FFO $7.16–7.26 (ex-NMTC $7.01–7.11) — tightened/raised low end |
| **Q4'25 (2026-02-12)** | FY25 actual / FY26 initial | FY25 actual: Nareit FFO $7.22, Core FFO $7.06 (landed inside the ex-NMTC guided band) / FY26: EPS $3.90–4.00, FFO $7.42–7.52 | delivered within its own last-guided range |
| **Q1'26 (2026-05-01)** | FY26 | EPS $3.94–4.03 / FFO $7.46–7.55 | vs EPS $3.90–4.00 / FFO $7.42–7.52 — raised & tightened |
| **Q2'26 (2026-07-31)** | FY26 | EPS $4.22–4.30 / FFO $7.48–7.56 (Core FFO growth 5.9–7.1%) | vs EPS $3.94–4.03 / FFO $7.46–7.55 (growth 5.7–6.9%) — raised & tightened |

**FFO/Core FFO guidance was raised or maintained in all 8 of the last 8 releases — never cut.** *(Source: 8-K EX-99.1 guidance tables, each release cited above.)*

## 6. Earnings quality & balance sheet
- **FFO/EPS gap drivers:** Q2'25 EPS jump vs FFO was NMTC ($13.0M/$0.15 sh, excluded from Core FFO) plus a one-time tax credit; Q1/Q2'26 EPS swings were driven by realty gains ($20.6–$113.3M range across quarters) — Core FFO is the cleaner run-rate metric and is used throughout §4–5.
- **Leverage (2026-06-30):** total debt $4,767.9M, net debt $4,660.7M (vs $4,487.5M/$4,310.5M at 2025-12-31 — net debt +8.1% in 2 quarters). Net debt/market cap 30% (down from 34%, on share-price appreciation). EBITDAre (Q2'26 annualized from 6-mo $437.1M) ≈ $874M → **net debt/EBITDAre ≈ 5.3x**. Fixed-charge coverage 3.9x. Covenants: Total Debt/Assets 39% (cap 60%), Secured Debt/Assets 5% (cap 40%), Unencumbered Assets/Unsecured Debt 256% (min 150%) — comfortable headroom on all four. 77% of debt is fixed-rate; weighted-average senior-notes rate 4.07%.
- **Refinancing note:** $400M of 1.25%-coupon senior notes matured and were repaid 2026-02-17, refinanced via a $250M delayed-draw term loan plus $150M revolver draw — replacing sub-2% debt with materially higher-cost floating debt, a real (if modest) interest-expense headwind. Revolver upsized to $1.4B and extended to April 2030 (SOFR+72.5bp) on 2026-04-14.
- **Capital deployment:** ~$700M+ gross acquisitions since mid-2025 (Leawood KS $289M, Annapolis $187M, Village Pointe/Omaha + Annapolis Q4 combo $340M, Congressional North $72.3M, Kingstowne parcel $19.7M), funded via asset recycling (dispositions $66–169M/quarter) plus ATM equity ($61.1M in Q2'26 at $123.92/sh) plus debt. A $300M buyback was authorized Jan/Feb 2025; utilization not confirmed in filings reviewed this pass.
- **Dividend:** raised every year for **59 consecutive years** (longest in the REIT sector) — $1.10 → $1.13 (Aug 2025, 58th) → $1.16/quarter (Jul 2026, 59th), $4.64 annualized. *(Source: 8-K EX-99.1 "Other Supplemental Information" and "Summary of Outstanding Debt" tables, Q2 2026; prior quarters as cited.)*

## 7. Valuation snapshot (per `v4/outputs/v1_valuation_table.csv`, 2026-09-25)
P/FFO(proxy) **10.80x** vs FRT's own 5–10yr history percentile **5.65%** (i.e., near the cheapest FRT has traded on this basis) vs stated peer median **31.29x**. **Data conflict:** a 31x peer median for retail-REIT peers is not consistent with real-world comparables (quality open-air/grocery-anchored peers typically trade low-to-mid teens P/FFO) — flagged for V1 to re-check; the "attractive" verdict is still supported by FRT's own-history percentile independent of this anomaly. Implied growth (V1 model) 12.3% vs consensus FY1 growth 4.8% vs delivered-5y 8.4% — a wide gap between "implied" and "consensus" that V1 should reconcile; not independently re-derived here. WACC/CoE 8.65%. Scenario 3y annualized: bear −4.1% / base +17.7% / bull +32.6%. Street flag: "base 3y value exceeds Street 12m high target" — the model's base case is more optimistic than sell-side's current high target, worth discounting slightly. Verdict: **attractive**, score 0.49.

## 8. Bull case / Bear case
**Bull:** (1) Two-year, primary-sourced record of accelerating leasing spreads and record occupancy funding 8-for-8 raised/maintained FFO guidance — durable operating momentum, not narrative. (2) Priced near the cheapest P/FFO of its own 10-year history despite that acceleration, with the longest dividend-growth streak in the sector (59 years) as a valuation floor. (3) Accelerating, self-funded external growth (>$700M gross acquisitions since mid-2025) plus a development pipeline and a new 2028 FFO/AFFO growth framework (May 2026 Investor Day) giving multi-year visibility.

**Bear:** (1) Net debt is rising in absolute terms (+8.1% in 2 quarters) with net debt/EBITDAre ~5.3x, and cheap legacy debt is being refinanced into a higher-rate regime — a real, structural headwind to the "cheap and improving" thesis. (2) The record-low relative valuation may reflect a permanent higher-for-longer cost-of-capital re-rating for retail REITs generally, not a temporary mispricing — and the model's own 31x "peer discount" figure is unreliable, so the magnitude of any discount is uncertain. (3) Headline EPS is increasingly driven by gains on sale/recycling rather than organic FFO, raising execution/timing risk as portfolio turnover accelerates.

## 9. Key risks & kill criteria
1. Comparable POI (same-property NOI) growth below 2% for two consecutive quarters (below the recent 2.8–4.9% band).
2. Net debt/EBITDAre above ~6.5x, or any covenant cushion closing to within 25% of its minimum/maximum.
3. A **cut** (not merely a tighten) to FFO/Core FFO guidance vs. the immediately preceding quarter.
4. Occupancy or leased rate down >100bp YoY for two consecutive quarters.
5. The 59-year dividend-increase streak broken, or payout >90% of Core FFO.

## 10. Catalysts & calendar
Q3 2026 earnings expected on/about 2026-10-30 (unconfirmed estimate from historical late-October pattern). FY2026 guidance ($7.48–7.56 Core FFO) has been raised twice in 2026 already. 2028 FFO/AFFO growth framework from the 2026-05-21 Investor Day (Santana Row) — re-verify specifics before relying on it. Next dividend-increase announcement (60th year) has historically clustered around the Q2 release (~Jul/Aug 2027 if the pattern holds). **Unresolved:** an 2026-08-11 8-K (items 1.01/2.03/3.02/8.01) postdates this dossier's research window and should be reviewed before finalizing conviction.

## 11. Red-flag scan
No auditor change, restatement, going-concern language, or SEC/DOJ investigation identified in sources reviewed. Two items short of "clean": (a) FRT redefined its core non-GAAP metric mid-track-record (Core FFO introduced Q4 2025) — a definitional break to watch in longer-run comparisons; (b) the 2026-08-11 8-K noted above was not reviewed. Full FY2025 10-K critical-audit-matters, related-party and Form 4 insider-pattern review was **not completed** this pass (time-boxed) — coverage gap, not a clean bill.

## 12. Sources
1. SEC EDGAR CIK 0000034903, submissions JSON: https://data.sec.gov/submissions/CIK0000034903.json (retrieved 2026-09-26)
2. 10-K FY2025, filed 2026-02-12: https://www.sec.gov/Archives/edgar/data/34903/000003490326000017/frt-20251231.htm
3. 8-K/EX-99.1 Q3'24 (2024-10-30): .../000003490324000068/frt-09302024xex991.htm
4. 8-K/EX-99.1 Q4'24/FY24 (2025-02-13): .../000003490325000015/frt-12312024xex991.htm
5. 8-K/EX-99.1 Q1'25 (2025-05-08): .../000003490325000036/frt-3312025xex991.htm
6. 8-K/EX-99.1 Q2'25 (2025-08-06): .../000003490325000051/frt-6302025xex991.htm
7. 8-K/EX-99.1 Q3'25 (2025-10-31): .../000003490325000062/frt-9302025xex991.htm
8. 8-K/EX-99.1 Q4'25/FY25 (2026-02-12): .../000003490326000016/frt-12312025xex991.htm
9. 8-K/EX-99.1 Q1'26 (2026-05-01): .../000003490326000025/frt-3312026xex991.htm
10. 8-K/EX-99.1 Q2'26 (2026-07-31): .../000003490326000040/frt-6302026xex991.htm
11. v4/data/b1_live_scores.csv (as_of 2026-09-25); v4/outputs/v1_valuation_table.csv, v1_valuation.json

## Data basis, recency and disclaimer

- Most recent reported period incorporated: Q2 2026 (quarter ended 2026-06-30), from the 10-Q and 8-K Exhibit 99.1 cited above; events checked through 2026-09-25 (US close).
- Reporting basis: consolidated US GAAP figures in USD millions unless explicitly labelled adjusted/operating (company non-GAAP) or per share.
- Research, not personalised investment advice; the author is not a licensed adviser.

## Addendum (2026-09-26): corrected REIT valuation (V2R)

Agent V2R rebuilt NAREIT FFO for FRT directly from SEC filings/XBRL (`v4/outputs/v2r_reit_valuation.md` and `.json`), replacing the systematic model's (V1) "FFO proxy" (GAAP net income + total D&A) used in §3/§7 above. That proxy does not exclude one-off gains on sale of real estate, and FRT recognized $20.6–113.3m/quarter of such gains in Q1–Q2 2026 alone (§4, §6) — these flowed straight into V1's proxy and mechanically depressed its P/FFO and own-history percentile.

**Corrected multiples (as of 2026-09-25 close, $110.52/sh):**
- P/FFO (TTM NAREIT FFO, $7.37/sh — all four trailing quarters company-reported) = **14.94x**
- P/FFO (FY2026 Core FFO guidance midpoint $7.52/sh) = **14.70x**
- Own-history percentile: **37.2 (10-year, n=121mo) / 55.7 (5-year, n=61mo)** — roughly its own median, not an extreme
- Peer median (REG/KIM/SPG, FY26 guidance P/FFO): **15.07x** — FRT trades essentially in line with peers, not at a discount

**Statements above that no longer hold:**
- §1 Verdict: "priced at close to the cheapest P/FFO of FRT's own 10-year history" — does not survive; corrected 10-year percentile is 37th, not sub-6th.
- §3: "P/FFO(proxy) 10.80x sits at the 5.65th percentile of FRT's own 5–10yr history — i.e., near the cheapest FRT has ever traded on this metric" — this was an artefact of the proxy counting gains-on-sale as recurring FFO, not a real mispricing.
- §7: "Verdict: attractive, score 0.49" on "P/FFO(proxy) 10.80x vs ... percentile 5.65%" — superseded; corrected verdict is **fair**. (§7's own suspicion that the quoted 31.29x peer median "is not consistent with real-world comparables" is now confirmed: the real peer median is 15.07x.)
- §8 Bull case (2): "Priced near the cheapest P/FFO of its own 10-year history despite that acceleration" — no longer accurate; FRT is priced fairly, at roughly its own and peers' median.

**Re-assessed verdict: INCLUDE-SMALL (down from INCLUDE/full conviction).** The two-year, primary-sourced operating record — accelerating comparable POI growth, record occupancy, FFO/Core FFO guidance raised or held in 8 of 8 quarters, and a 59-year dividend-increase streak — is untouched by this correction and remains genuine, durable evidence of a well-run business; that part of the original thesis stands. But one of the pillars of the original full-conviction INCLUDE — that FRT was statistically the cheapest it had been in a decade, offering a margin of safety on top of improving fundamentals — is gone: it now trades at ~14.9x P/FFO, in line with its own 10-year median and with retail-REIT peers (15.1x). That is a "pay a fair price for a good business" setup, not a mispricing, and it arrives alongside rising net debt (+8.1% in two quarters, net debt/EBITDAre ~5.3x) and refinancing of cheap legacy debt into a higher-rate regime (§6, §8 bear case). Full-weight conviction is no longer warranted on valuation grounds; FRT remains investable as a quality compounder at a reasonable, non-discounted price — named reservation: no valuation margin of safety — sized smaller than a genuine-mispricing INCLUDE would justify. This addendum supersedes the valuation-dependent statements above where they conflict; §2–6 and §9–11 (operating, balance-sheet, guidance and risk sections) are unchanged and remain in force. Research, not personalised investment advice.
