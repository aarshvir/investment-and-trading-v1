# BNY (The Bank of New York Mellon Corp) — F101 Diligence Dossier

## 1. Verdict
**INCLUDE-SMALL** (half weight). Reason: best-in-class scale custodian/collateral-manager still compounding earnings faster than the market implies, but the stock has already re-rated +51% over the last year (per Q04 triage), so absolute margin of safety is thinner than the fundamentals alone suggest. Thesis horizon: 12–36 months.

## 2. Business in plain English
BNY is the world's largest custody/asset-servicing bank: it holds, settles, values and finances securities for asset managers, pension funds, insurers and broker-dealers (Pershing platform), and also runs a large treasury/markets book on the interest-bearing balance sheet. It earns fee income tied to assets under custody/administration (AUC/A ~$60T) plus net interest income, so results move with market levels, asset flows, and interest rates rather than with a single product cycle. Competitive position: one of only three global scale custodians (with State Street and JPMorgan), with high switching costs once a client's securities master file is on the platform.

## 3. Why the model likes it / durability
b1 factor read: composite 0.618 (decile 7), driven mostly by momentum (pct_mom_12_1 0.96 — top decile) and quality-adjacent earnings momentum (pct_sue 0.66); value percentile is only 0.11 (expensive) and gp_a is missing (bank — asset-based quality metric not meaningful for a financial). **Read:** the model likes BNY almost entirely for momentum/SUE, not for cheapness. That momentum is real (four straight EPS beats, NII/fee inflection — see §4) but is partly an artefact of a strong equity/rate backdrop through 2026; it is not a structural moat re-rating that necessarily persists if markets correct.

## 4. Last two years of results (quarterly, USD millions except EPS; GAAP)
| Quarter end | Total revenue (interest+noninterest) | Net income | Diluted EPS |
|---|---|---|---|
| 2024-12-31 | 10,120 | 1,155 | 1.54 |
| 2025-03-31 | 9,756 | 1,220 | 1.58 |
| 2025-06-30 | 10,427 | 1,423 | 1.93 |
| 2025-09-30 | 10,439 | 1,445 | 1.88 |
| 2025-12-31 | n/a (tag gap — not in XBRL sample pulled) | n/a | n/a |
| 2026-03-31 | 9,863 | 1,632 | 2.24 |
| 2026-06-30 | 10,192 | 1,761 | 2.45 |
Source: SEC XBRL companyfacts (`InterestAndDividendIncomeOperating` + `NoninterestIncome`, `NetIncomeLoss`, `EarningsPerShareDiluted`), CIK 0001390777, 10-Q filings 2025-05-02 through 2026-07-31. **Q4-2025 (Oct–Dec) row is a data gap in this pull, not a company gap** — the 10-K/8-K exists (filed ~2026-01) but was not re-fetched in this session; flagged in `data_conflicts`.
Trend: EPS accelerating YoY every reported quarter (+27%, +34%, +28%, +30% YoY for the four most-recent quarters shown), driven by fee growth (noninterest income $3.57bn → $4.25bn Q2'25→Q2'26, +19% YoY) as AUC/A and Pershing platform assets grew with markets, while net interest income has been roughly flat-to-down as the yield curve normalized (InterestAndDividendIncomeOperating $6.60bn Q2'25 → $5.94bn Q2'26, −10% YoY) — **fee growth, not NII, is doing all the work**, which matters for durability if equity markets correct.

## 5. Guidance track record
BNY does not issue formal quarterly EPS guidance; management gives NII and expense growth ranges on earnings calls. Per the most recent (Q2 2026, 2026-07-15 earnings release, 8-K) commentary reported by aggregated coverage: full-year NII was tracked toward the higher end of the prior "flat-to-up-low-single-digits" range and expense growth guided in the low-single-digits — **not independently re-verified against the primary earnings-call transcript in this session** (time-boxed); flagged as a data conflict to confirm before sizing.

## 6. Earnings quality & balance sheet
- **Consolidated** stockholders' equity: $43.1bn (Mar-25) → $44.7bn (Jun-26); ROE ~13–14% (Yahoo TTM 14.1%, matches b1 roe 0.141).
- **Consolidated** long-term debt (parent + sub, per XBRL `LongTermDebt`): $30.9bn (Mar-25) → $30.4bn (Jun-26) — roughly flat; this is a bank holding company so "net debt/EBITDA" is not the relevant leverage metric. Use CET1 instead: not pulled this session (data gap — flag).
- Dividend: $2.12/share trailing, yield ~1.4%, payout ratio ~24.7% of TTM EPS — conservative, well covered, room for buyback-led capital return (BNY has been an active repurchaser; shares outstanding basis 678.5m per Yahoo snapshot 2026-09-25).
- FCF/OCF not a standard bank metric; earnings-based "owner earnings" proxy used in the reverse DCF below is TTM net income (trailing EPS 8.57 × 678.5m shares ≈ $5.82bn).
- **Data gap to close before full-weight sizing:** consolidated CET1 ratio, AUC/A trend, and Q4-2025 quarterly cut were not pulled in this session (time-boxed at standard depth).

## 7. Valuation snapshot & reconciliation with V1
BNY has **no row in `v4/outputs/v1_valuation_table.csv`** — v1_verdict = null; nothing to reconcile.
NTM P/E ≈ 15.0x (d4 `pe_ntm`), trailing P/E 17.5x, forward P/E 14.7x. Consensus FY1 (2027) EPS growth ≈ 10.8% (d4 `eps_fy1_growth` 0.1077). Target price consensus $167.36 (range $135–$184, 14 analysts, mean rec "buy" 2.13) vs spot $150.15 → ~11.5% implied street upside, matching the "modest remaining upside after the rally" read in the Q04 triage.

**Reverse DCF (own build, since no V1 row exists):** solving for the constant 10-year earnings growth rate that, discounted at an assumed 9.4% cost of equity (beta 1.05, rf 4.2%, ERP 5%) with a 3% terminal growth, equates the PV of owner earnings to the current $101.9bn market cap: **implied 10-year growth ≈ 4.1%/yr**. My base case (fee-driven compounding, buybacks, expense discipline) is **~8–9%/yr** — well above the implied rate. **implied_vs_base = below** (market is pricing in materially less growth than a reasonable base case), which is the valuation argument for INCLUDE; the reservation for INCLUDE-SMALL rather than full INCLUDE is the recent momentum-driven re-rating and the unresolved data gaps above, not the valuation math itself.

## 8. Bull case / Bear case
**Bull:** (1) Fee growth (AUC/A, Pershing, collateral management) keeps compounding high-single-digits as markets and flows stay firm; (2) buybacks continue to shrink the share count at a mid-single-digit rate on top of EPS growth; (3) a steeper yield curve later in the cycle re-accelerates NII, removing the current drag.
**Bear:** (1) A sustained equity-market drawdown mechanically cuts fee income (AUC/A is market-value-linked) — this is BNY's biggest single risk given fee income is now doing all the growth work; (2) further NII compression if short rates fall faster than deposit/funding costs re-price; (3) any custody-technology/operational incident (settlement failure, cyber event) at this scale of assets serviced would be reputationally and financially costly.

## 9. Key risks & measurable kill criteria
1. Noninterest (fee) income growth YoY falls below 3% for two consecutive quarters (current run-rate ~19% YoY — a break of this magnitude signals the market/flows engine has stalled).
2. Net interest income declines >15% YoY for two consecutive quarters without an offsetting fee acceleration.
3. Consolidated (Basel III) CET1 ratio (not yet pulled — obtain before position sizing) falls below management's stated operating target, forcing a buyback pause.
4. Diluted EPS misses consensus (currently $9.26 FY0 / $10.26 FY1) by >5% for two consecutive quarters.
5. A material operational/cyber incident affecting custody settlement is disclosed in an 8-K.

## 10. Catalysts & calendar
Next earnings: **2026-10-15** (Q3 2026, per d4 live snapshot `next_earnings_date`).

## 11. Red-flag scan
No restatements, auditor changes, or SEC/DOJ investigation disclosures identified in the 8-K/10-Q filing list reviewed (2026-06-24 through 2026-09-22). Insider Form 4 pattern and short-seller reports **not checked this session** (time-boxed) — flag as open item.

## 12. Sources
1. SEC EDGAR submissions, CIK 0001390777: `https://data.sec.gov/submissions/CIK0001390777.json` (retrieved 2026-09-27).
2. SEC XBRL company facts, CIK 0001390777: `https://data.sec.gov/api/xbrl/companyfacts/CIK0001390777.json` (retrieved 2026-09-27).
3. v4 internal data: `data/b1_live_scores.csv`, `data/d4_live_snapshot.parquet` (retrieved live 2026-09-25T20:26Z), `outputs/Q04_triage.json`.

## Data basis, recency and disclaimer
Most recent period incorporated: 10-Q for quarter ended 2026-06-30 (filed 2026-07-31). Events checked to 2026-09-25 close via 8-K filing list (latest 2026-09-22) and live market snapshot (2026-09-25T20:26Z). All EPS/revenue/net income figures above are **GAAP** as reported in XBRL (no adjusted figures used); Yahoo-sourced valuation and consensus figures (P/E, targets, growth) are third-party aggregator data, labelled as such. **Research, not personal investment advice.**
