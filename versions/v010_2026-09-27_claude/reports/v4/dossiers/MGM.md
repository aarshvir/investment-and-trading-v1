# MGM Resorts International (NYSE: MGM) — Diligence Dossier
Agent f10 | As of 2026-09-25 close ($32.58) | Most recent period incorporated: Q2 FY2026 (period ended 2026-06-30), 10-Q filed 2026-07-29; checked for events to 2026-09-25 (includes the confirmed 2026-09-24 withdrawal of the People Incorporated proposal).

## 1. Verdict
**WATCH.** Thesis horizon 12–24 months. The stock round-tripped a takeover premium (+16% on the bid, -11% on its withdrawal) that nets out close to zero, so the real story is operating, not deal-driven: Las Vegas Strip Resorts is genuinely improving (2nd straight quarter of YoY growth) but Regional Operations and MGM China are both shrinking on a profit basis, Consolidated Adjusted EBITDA has fallen YoY for two consecutive quarters even as GAAP net income has been flattered by one-off gains, and the balance sheet's ~1.5x conventional net-debt/EBITDA hides a much heavier ~$23.8bn triple-net lease obligation to VICI/other landlords. Move to INCLUDE-SMALL only once Adjusted EBITDA stabilizes.

## 2. Business
MGM Resorts owns/operates casino resorts on the **Las Vegas Strip** (its largest, highest-margin segment: Bellagio, MGM Grand, Aria, Cosmopolitan, etc.), a **Regional Operations** portfolio of US regional casinos, **MGM China** (Macau, via ~56%-owned MGM China Holdings), plus **MGM Digital** (LeoVegas and other consolidated European/international iGaming) and a 50/50 unconsolidated JV, **BetMGM** (US sports betting/iGaming). Most domestic real estate is monetized via **triple-net sale-leaseback master leases**, principally with VICI Properties — MGM operates the casinos but does not own most of the underlying real estate. **Routing:** primary playbook `aviation-hotels.md` (Resorts & Casinos — yield×occupancy, perishable capacity); the lease structure is read through a REIT-tenant/rent-coverage lens (cf. `realestate-reit.md` logic) because conventional leverage metrics understate the fixed obligation; BetMGM (equity-method, ~4% of consolidated Adjusted EBITDA) is a minor secondary item, not large enough to warrant a full `exchanges-payments.md` overlay.

## 3. Why the model likes it — durable or artefact?
b1 composite 95.9th percentile (live_rank 24), driven by Value (83rd pct — genuinely cheap post-selloff) and high Momentum/SUE inputs that are now **likely stale**: the b1 snapshot's `as_of` is 2026-09-25 but factor construction typically uses data through the last rebalance, and the 11% single-day drop on the 2026-09-24 deal withdrawal plus the Macau EBITDAR miss (see §6) will not be reflected until the next rebalance — **treat the Momentum leg as about to roll over, not as a current green light.** Quality is **flagged as incomplete**: `gp_a` (gross-profit/assets) is blank in b1_live_scores.csv for MGM and `n_Q` = 6 vs. 7 for SWK/HAS — the Quality family score rests on one fewer input, plausibly because MGM's lease-heavy balance sheet does not map cleanly onto a gross-profit/assets construct. **Data conflict, logged.**

## 4. Last 8 quarters (GAAP; $ in millions; SEC XBRL cross-checked to 8-K press releases)
| Qtr end | Revenue | GAAP EPS | Adj. EPS | Consol. Adj. EBITDA | YoY Adj. EBITDA | Note |
|---|---|---|---|---|---|---|
| 2024-09-30 | 4,183.1 | 0.61 | n/a | n/a | | |
| 2024-12-31¹ | 4,346.6 | ~0.52 | n/a | $528m | | |
| 2025-03-31 | 4,277.1 | 0.51 | n/a | $637m | | |
| 2025-06-30 | 4,404.9 | 0.18 | 0.79 | $648m | +2% | |
| 2025-09-30 | 4,250.5 | **-1.05** | 0.24 | $506m | | goodwill impairment drives GAAP loss |
| 2025-12-31¹ | 4,605.3 | 1.11 | 1.60 | $635m | +20% | |
| 2026-03-31 | 4,454.7 | 0.48 | 0.49 | $580m | **-9%** | |
| 2026-06-30 | 4,451.0 | 1.11 | 0.59 | $610m | **-6%** | GAAP EPS flattered vs. Adj. EBITDA decline (see §6) |
¹ Derived as FY10-K minus 9-month 10-Q (not separately disclosed).
MGM does **not** issue formal quantitative EPS/revenue/EBITDA guidance in any of the five releases reviewed — confirmed by absence of numeric outlook ranges; closest proxy is qualitative capital-allocation/development commentary (§5).

## 5. "Guidance": none issued; qualitative outlook only
MGM gives no point or range guidance for revenue, EBITDA or EPS in any of the last five earnings releases (Q2 FY26 through Q2 FY25). Management commentary is directional only: continued Las Vegas Strip growth investment, MGM Osaka (Japan integrated resort) "on track for 2030 opening," and capital-return priorities (buybacks over dividend — MGM pays no regular dividend). Per the dossier template's instruction, this is stated rather than inferred.

## 6. Earnings quality & balance sheet
- **GAAP vs. Adjusted divergence is the central earnings-quality finding.** Q2 FY26: GAAP net income $292.4m (EPS $1.11) vs. $49.0m (EPS $0.18) a year earlier — a huge GAAP improvement — while **Consolidated Adjusted EBITDA fell 6% YoY** ($610m vs. $648m) and **Adjusted EPS fell 25%** ($0.59 vs. $0.79). The GAAP headline is driven by one-off property/disposition gains (MGM Northfield Park was sold 2026-04-21) and other non-operating items excluded from Adjusted EPS; the underlying operating trend is negative for two straight quarters (Q1 FY26 Adjusted EBITDA -9% YoY; Q2 FY26 -6%). Q3 FY25's GAAP loss (-$1.05/share vs. Adjusted +$0.24) was itself driven by a goodwill impairment. **A reader who quotes only the GAAP EPS trend would reach the opposite conclusion from the Adjusted-EBITDA trend.**
- **Segment profit is narrowly led by one segment.** Q2 FY26 Segment Adjusted EBITDAR: Las Vegas Strip Resorts $735m (+3% YoY, genuine growth); Regional Operations $280m (-9% YoY reported, flat same-store ex the Northfield disposition); **MGM China $257m (-15% YoY)** despite flat revenue and management's "market share gains" framing — margin compression from a $21m YoY increase in intercompany branding fees and (by inference from peer price action, see §9) broader Macau softness.
- **Lease-adjusted leverage is far higher than the conventional ratio.** Balance sheet (Q2 FY26 10-Q/8-K Ex-99.2): cash $2,547.4m, long-term debt (net) $6,068.4m → conventional net debt **$3,521.1m**, matching the D3/V1 figure exactly (cross-check passed). Conventional net debt/TTM-EBITDA ≈ 1.4-1.6x looks comfortable. But **operating lease liabilities are $23,778.5m** — nearly 4x conventional debt — almost entirely the triple-net master leases with VICI Properties (plus Beau Rivage/MGM National Harbor ground subleases and MGM China land concessions). Triple-net lease rent expense was $552.2m in the quarter (~$2.2bn annualized). Rent coverage (Consol. Adj. EBITDA + rent) / rent ≈ (610+552)/552 ≈ **2.1x** — a REIT-tenant credit metric, not a leverage ratio, and a more honest read of balance-sheet risk than net-debt/EBITDA alone. Lease-adjusted leverage ≈ (3,521 + 23,779) / (~4.6bn annualized EBITDAR) ≈ **~5.9x** vs. the conventional ~1.5x — a roughly 4-turn gap.
- **BetMGM contribution is small relative to its narrative weight:** equity income of $23.1m in Q2 FY26 (vs. $21.8m a year earlier) — modestly growing, profitable, but only ~4% of consolidated Adjusted EBITDA.
- **Capital return:** $164m of buybacks in Q2 FY26 alone, $1.4bn remaining authorization; no regular dividend.

## 7. Valuation snapshot
NTM P/E 16.9x — 57th percentile of ~10 years of own history (mid-range, not a screaming discount despite the price decline, because forward estimates have also fallen). EV $11.92bn **excludes the $23.8bn operating lease liability** — the "cheap EV/EBIT" read embedded in the quant screen therefore overstates cheapness on a lease-adjusted basis. FCF yield 10.7%. WACC 8.02% (beta 1.19, elevated). Reverse DCF implied 10y growth -6.9% vs. consensus FY1 +1.2% and a delivered 10y CAGR of +7.1% (5y +22.1%, though this is flattered by the post-COVID low base) — a real "priced for shrinkage" setup, but note the segment-level EBITDAR deterioration in §6 gives that pessimism some grounding. **Street targets ($40-57, mean $49.33, 19 analysts, "buy") sit entirely above the current $32.58 price and almost certainly predate the 2026-09-24 withdrawal and the Q2 Macau/regional EBITDAR softness — treat as stale, not as a live 23%+ implied margin of safety. Independent re-run of `scripts/valuation.py` reproduces V1's EV bridge exactly (EV $11,918.8m; net debt $3,521.1m, matching §6) and gives an FCF-anchored reverse-DCF implied growth of -9.2%/yr, slightly more bearish than V1's -6.9%.**

## 8. Deal speculation vs. fundamentals (People Incorporated proposal) — quantified
D4's corporate-events file records a $48.30/share cash proposal from **People Incorporated** on 2026-06-01 and its withdrawal on 2026-09-24; **both the proposal and the withdrawal are independently confirmed in MGM's own Q2 FY26 8-K** (forward-looking-statements section names "any acquisition proposal from People Incorporated" explicitly). Using daily closes (v4/data/d2_close.parquet, Cboe/CNBC cross-checked):
- **Announcement day (2026-06-01):** MGM +16.1% ($43.67→$50.69) vs. LVS +5.6%, WYNN +5.5%, CZR +0.3%, SPY +0.3% — an idiosyncratic, deal-driven gain of roughly +10-13pts. Note MGM traded *above* the $48.30 offer, implying the market priced a real chance of a bump or competing bid.
- The stock then drifted from $50.69 down to ~$37-40 through the summer *before* the formal withdrawal — the market was already pricing out completion odds.
- **Withdrawal day (2026-09-24):** MGM -11.0% ($37.85→$33.69) vs. LVS -1.4%, WYNN -1.5%, CZR ~flat, SPY ~flat — an idiosyncratic, deal-driven loss of roughly -10pts, an almost-exact round trip of the announcement-day gain.
- **Cumulative 2026-05-29→2026-09-25:** MGM -25.4% vs. LVS -22.9%, WYNN -19.9%, CZR **+1.9%**, SPY +1.7%.
**Read-through:** the deal itself is roughly a wash cumulatively (gained then gave back ~10-13pts). The bulk of MGM's four-month decline (~20-23pts) is shared with Macau-exposed peers LVS/WYNN, consistent with the MGM China EBITDAR miss in §6 — a sector/Macau re-rating, not an MGM-only story. Against CZR (Vegas/regional, no Macau exposure, **up** 1.9% over the same window), MGM's underperformance (~27pts) is stark and points to Macau as the dominant shared driver, with the withdrawn deal a secondary, largely self-cancelling contributor.

## 9. Bull case
1. Las Vegas Strip Resorts — the largest, highest-quality segment — delivered a second consecutive quarter of YoY revenue *and* EBITDAR growth (+3%/+3%), with continued high-ROI luxury-room reinvestment.
2. Valuation: reverse-DCF-implied shrinkage (-6.9%/10y) is more pessimistic than the 7-10y delivered track record; FCF yield ~10.7%; buybacks ($1.4bn remaining) are shrinking the float into weakness.
3. BetMGM is durably profitable and MGM Osaka (2030) is a call option on a new, high-barrier Asian gaming market not yet in most near-term models.

## 10. Bear case
1. The "modest" ~1.5x conventional net-debt/EBITDA is misleading: ~$23.8bn of triple-net lease liabilities against ~$2.4bn of annualized Adjusted EBITDA implies rent coverage of only ~2.1x, a REIT-tenant credit profile with a fixed obligation that does not flex down in a downturn.
2. Two of three core segments are shrinking on a profit basis: MGM China Segment Adjusted EBITDAR -15% YoY despite flat revenue, and Regional Operations -9% reported; Vegas Strip alone is carrying the growth story.
3. GAAP net income has been flattered by one-off gains for two of the last four quarters while Consolidated Adjusted EBITDA has now declined YoY for two straight quarters — the "record" GAAP headlines mask a shrinking operating base, and the failed takeover removes a speculative floor that had been supporting the stock.

## 11. Key risks & kill criteria
1. Consolidated Adjusted EBITDA declines YoY for a third consecutive quarter (Q3 FY26).
2. MGM China Segment Adjusted EBITDAR declines further or Macau GGR trends turn negative for two more quarters.
3. Rent coverage (EBITDAR/triple-net rent) falls below ~1.8x.
4. Las Vegas Strip YoY growth breaks (the one clearly improving segment rolls over).
5. Any further goodwill/asset impairment in Regional Operations following the Northfield Park disposition precedent.

## 12. Catalysts & calendar
Next earnings ~2026-10-28 (Q3 FY26, per D4 snapshot). Watch for: MGM China monthly Macau GGR data, any revived acquisition interest (from People Incorporated or another party) following the 2026-09-24 withdrawal, and MGM Osaka construction milestones.

## 13. Red-flag scan
No auditor change, restatement or going-concern language identified in the documents reviewed. Two GAAP-distorting one-offs in the last five quarters (Q3 FY25 goodwill impairment driving a GAAP loss; Q2 FY26 disposition gain flattering GAAP net income against a declining Adjusted EBITDA) — both disclosed, not concealed, but material to interpretation (§6). Unsolicited-proposal handling: MGM does not appear to have filed a standalone 8-K on either the receipt or the withdrawal of the People Incorporated proposal (only referenced inside the routine Q2 FY26 earnings 8-K's boilerplate) — consistent with a non-binding, board-rejected approach that did not trigger Item 8.01/14D-9 disclosure obligations, but it also means there is no primary document detailing the board's rationale. Insider Form 4 pattern and litigation docket **not reviewed in this pass** (time-boxed) — flagged as open, not asserted clean.

## 14. Data conflicts vs quant screen
(1) b1's Quality family score for MGM rests on incomplete inputs (`gp_a` blank, n_Q=6) — logged as a data gap, not a clean read. (2) V1's EV/valuation snapshot excludes ~$23.8bn of operating lease liabilities, overstating cheapness on a lease-adjusted basis. (3) V1's "attractive vs. Street" framing (target range $40-57) is very likely stale — pre-dating the 2026-09-24 deal withdrawal and the Q2 FY26 Macau/regional EBITDAR miss — and should not be read as a live margin of safety. (4) GAAP EPS trend (improving) directly contradicts the Adjusted-EBITDA trend (declining for two quarters) — flagged per the lead's standing instruction never to let a GAAP headline stand in for the operating trend.

## Data quality note
All financial figures are GAAP unless labelled "Adj." (non-GAAP, company-defined); sourced from SEC EDGAR (10-Q/10-K XBRL and 8-K Ex-99.1 press releases, cited below) with quant cross-checks from v4/data and v4/outputs (as_of 2026-09-25), plus an independent event-study on v4/data/d2_close.parquet (§8). Two figures are model-derived (marked¹) rather than directly disclosed; a handful of blank table cells reflect metrics the company does not disclose for that period rather than dropped data. Insider Form 4 pattern, full litigation docket and a formal auditor's-report read were not completed in this pass (time-boxed) and are logged as open items, not asserted clean. This dossier is research output for an internal, non-advisory process; it is not personalised investment advice, and no trade is recommended or has been placed.

## Sources
1. SEC EDGAR submissions, CIK 0000789570: https://data.sec.gov/submissions/CIK0000789570.json
2. XBRL company facts: https://data.sec.gov/api/xbrl/companyfacts/CIK0000789570.json
3. 10-Q, period 2026-06-30, filed 2026-07-29: https://www.sec.gov/Archives/edgar/data/789570/000078957026000076/mgm-20260630.htm
4. 8-K Ex-99.1, Q2 FY26 (2026-07-29): https://www.sec.gov/Archives/edgar/data/789570/000078957026000075/mgmex991q22026earningrelea.htm
5. 8-K Ex-99.1, Q1 FY26 (2026-04-29): https://www.sec.gov/Archives/edgar/data/789570/000078957026000034/mgmex991q12026earningrelea.htm
6. 8-K Ex-99.1, Q4/FY25 (2026-02-05): https://www.sec.gov/Archives/edgar/data/789570/000078957026000013/mgmexhibit991q42025er.htm
7. 8-K Ex-99.1, Q3 FY25 (2025-10-29): https://www.sec.gov/Archives/edgar/data/789570/000078957025000073/mgmex991q32025earningrelea.htm
8. 8-K Ex-99.1, Q2 FY25 (2025-07-30): https://www.sec.gov/Archives/edgar/data/789570/000078957025000032/mgmex991q22025earningrelea.htm
9. v4/data/d4_corporate_events.csv (People Incorporated proposal/withdrawal headlines, 2026-06-01 / 2026-09-24).
10. v4/data/d2_close.parquet — MGM/LVS/WYNN/CZR/SPY daily closes, 2026-05-15 to 2026-09-25 (event-study computation, §8).
11. v4/data/b1_live_scores.csv; v4/data/d4_live_snapshot.parquet; v4/outputs/v1_valuation_table.csv, v1_valuation.json (as_of 2026-09-25).
