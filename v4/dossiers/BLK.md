# BlackRock, Inc. (BLK) — Diligence Dossier (F22, standard depth)

## 1. Verdict
**INCLUDE-SMALL** (half weight). Thesis horizon 24–36 months (per this dossier's own §7 reverse DCF and §4 quarterly filings, not a data-provider figure). One-sentence reason: the world's largest, most durable asset-management franchise is compounding fee earnings at a rate the current price does not fully require, but roughly 30% of headline growth is acquisition-driven (GIP/HPS/Preqin, per §3/Q2-26 8-K) and GAAP EPS has been distorted by non-cash contingent-consideration marks (§4, Q1-26 10-Q), so full weight is not warranted until organic, adjusted growth is cleanly separable for another 2–4 quarters.

**Thesis (≤25 words):** As of the 2026-09-25 close, the world's #1 asset manager (iShares, Aladdin, and newly acquired private-markets platforms per Q2-26 8-K) growing AUM 20%+ a year (§4), priced at a market-average multiple (§7).

## 2. Business in plain English
Per its Q2 2026 10-Q (period ended 2026-06-30) and 8-K earnings release, BlackRock manages $15.3tn of client assets (index funds/ETFs via iShares, active strategies, and now private markets) for a fee, plus licenses its Aladdin risk-management/data platform to other institutions. It earns a percentage of assets under management (AUM), so revenue scales with markets and net client inflows; it does not take principal risk on client money. Competitive position (as characterized in the FY2025 10-K and Q2-26 8-K, filed 2026-02-25 and 2026-07-15 respectively): #1 global AUM, #1 ETF platform (iShares), and a quasi-operating-system moat in Aladdin used by hundreds of institutions including some competitors.

## 3. Why the model likes it / durability
b1 factor data (v4/data/b1_live_scores.csv, as_of 2026-09-25): Quality 5, Growth 4, price_vs_growth 4; factor composite driven by quality (gp/assets, ROE, low accruals) and growth (54% forward EPS growth cited in v4/outputs/Q04_triage.json). **Partly an artefact**: a large chunk of both the AUM growth (22% YoY per the Q2-26 8-K, filed 2026-07-15) and the EPS growth is inorganic — the GIP (infrastructure), HPS (private credit) and Preqin (data) acquisitions closed through 2024–2025 and are still being integrated and amortized (Q1-26 intangible amortization $277m). Underlying organic base-fee growth is durable (Aladdin technology services +13–15% YoY per the Q1-26/Q2-26 8-Ks) but slower than the headline.

## 4. Last two years of results (GAAP, USD millions except per-share; source: SEC XBRL companyfacts CIK0002012383, cross-checked to 8-K press releases)
| Quarter | Revenue | YoY | Net income | Diluted EPS (GAAP) | Adjusted diluted EPS |
|---|---|---|---|---|---|
| Q3'24 | 5,197 | — | 1,631 | 10.90 | n/a (not pulled) |
| Q4'24 (derived: FY−9mo) | 7,008 | — | 1,127 | ~7.10 | n/a |
| Q1'25 | 5,276 | — | 1,510 | 9.64 | 11.30 |
| Q2'25 | 5,423 | — | 1,593 | 10.19 | n/a |
| Q3'25 | 6,509 | +25.3% | 1,323 | 8.43 | n/a |
| Q4'25 (derived) | 7,007 | 0.0% | 1,127 | ~7.10 | n/a |
| **Q1'26** | **6,698** | **+27.0%** | **2,212** | **14.06** | **12.53** |
| **Q2'26** | **7,084** | **+30.6%** | **1,914** | **12.19** | **13.91** |
Per the FY2025 10-K (filed 2026-02-25): FY2025 revenue $24,216m (+18.6% YoY); FY2025 GAAP diluted EPS $35.31. Per the Q1-26 and Q2-26 8-Ks (filed 2026-04-14 and 2026-07-15): AUM $13.0tn (Q1-25) → $13.9tn (Q1-26) → $15.3tn (Q2-26), +22% YoY; net inflows $130bn (Q1-26) and $192bn (Q2-26), $321bn YTD.

**Earnings-quality flag (last-loop lesson applied):** per the Q1-26 8-K (filed 2026-04-14, exhibit 99.1), GAAP EPS ($14.06) exceeded as-adjusted EPS ($12.53) that quarter — the reverse of BlackRock's normal pattern — because of a **$549m non-cash positive fair-value mark on contingent consideration** tied to the acquisitions (vs. a $96m expense in Q1-25, same source). Per the Q1-26 8-K, GAAP EPS growth of 46% YoY that quarter is therefore not comparable to the 11% adjusted-EPS growth reported the same filing; Q2-26 (per the Q2-26 8-K, filed 2026-07-15) is cleaner (GAAP +20% vs adjusted +15% YoY, same source). **Always cite GAAP and adjusted separately for BLK; do not average them.**

## 5. Guidance track record
BlackRock gives no formal quantitative EPS/margin guidance. Qualitative commentary (Q2-26 8-K, ex-99.1): management raised quarterly share-repurchase run-rate to $550m (from prior levels) and reiterated no explicit margin target. Sell-side estimate revisions (d4_live_snapshot, 2026-09-25): FY0 EPS +5.1% and FY1 EPS +5.6% over the trailing 90 days (flat over 30 days) — modestly positive momentum, not a guide cut or raise event.

## 6. Balance sheet & cash conversion
Per XBRL `Assets` (companyfacts CIK0002012383): total assets $175.9bn (period end 2026-06-30) vs $123.2bn (period end 2023-12-31); the increase is almost entirely acquisition goodwill/intangibles and consolidated sponsored investment vehicles, not operating leverage. Per the same source: stockholders' equity $57.6bn (2026-06-30), i.e. equity/assets ~33% (2026-06-30). GAAP operating cash flow is not the right cash-conversion metric here (sector playbook: consolidation of sponsored funds distorts it) — per XBRL `NetCashProvidedByUsedInOperatingActivities`, H1-26 GAAP OCF was only $247m (period 2026-01-01 to 2026-06-30) against $4.13bn of H1-26 net income (same period), a large negative swing versus Q1-25/Q1-26 seed-vehicle timing, not a red flag on the actual advisory-fee business but worth monitoring for repeat swings. Per v4/data/d4_live_snapshot.parquet (as_of 2026-09-25): dividend yield ~2.1%, FCF yield 4.3%. No going-concern or leverage stress found in the Q2-26 10-Q; standalone debt load is modest relative to $7bn+ annual adjusted operating income (FY2025 10-K).

## 7. Valuation snapshot & reverse DCF
Price (2026-09-25 close) $1,086.31; NTM P/E 17.5x (calendarised, d4); consensus FY1 EPS growth 14.3%; analyst mean target $1,322.75 (+21.8%). **No V1 row exists for BLK** (`v1_valuation_table.csv` — 93 rows, BLK/BX/EG absent) → v1_verdict = null, no reconciliation possible; this dossier's valuation view is independently derived.

**Reverse DCF:** solving a 10-year explicit-growth + Gordon-terminal model (r = 10.5% cost of equity [rf 4.2% + beta ~1.3 × 5% ERP], terminal growth 3.5%) for the growth rate that reproduces the current price from NTM adjusted EPS ($62.15) gives **implied 10-year EPS growth ≈ 6.7% p.a.** My evidence-based base case for sustainable (ex further large M&A) adjusted EPS/FCF growth is ~8–9% p.a. (mid-single-digit organic base-fee growth + operating leverage + buybacks + full run-rate contribution from HPS/GIP/Preqin), i.e. **above** the implied rate → valuation view = **cheap-to-fair**, not demanding. Bear case 3% (fee compression, weak markets, messy integration); bull case 13% (AI-driven Aladdin/data adoption, private-markets scaling faster than modeled).

## 8. Bull case / Bear case
**Bull:** (1) Aladdin + data (Preqin) creates a recurring, high-margin technology-services annuity growing mid-teens; (2) private-markets AUM (GIP infra, HPS credit) scales into a $600bn+ fee pool with higher yields than traditional index products; (3) buybacks ($550m/quarter) plus a 22% AUM growth rate compound EPS even if markets are flat.
**Bear:** (1) organic (ex-M&A) base-fee growth is genuinely mid-single-digit and the market is paying up for a growth rate propped up by acquisitions; (2) integration of three large deals (GIP, HPS, Preqin) in 18 months raises execution risk, visible in intangible-amortization drag and lumpy GAAP EPS; (3) index-fund antitrust/ESG political risk (see §11) could force costly structural changes to the core iShares business.

## 9. Key risks & measurable kill criteria
1. Organic base-fee (ex-acquisition) net flow growth below 3% for two consecutive quarters.
2. Adjusted operating margin falls below 42% for two consecutive quarters (Q1-26 was 44.5%, Q2-26 was 45.9%).
3. Net outflows (negative total net flows) in any single quarter.
4. A further negative fair-value mark or impairment on GIP/HPS/Preqin contingent consideration/goodwill exceeding $500m in a quarter.
5. Adverse final ruling or consent decree in the 13-state-AG antitrust (coal) suit or the LifePath ERISA litigation that restricts index-voting or fee practices.

## 10. Catalysts & calendar
Next earnings: **2026-10-14** (Q3-26, per d4 next_earnings_date). Integration updates on HPS/GIP/Preqin expected on that call; continued Fed rate path affects fixed-income AUM/flows.

## 11. Red-flag scan
No auditor change, restatement, or going-concern language found. Litigation: (a) 13 state Attorneys General (E.D. Texas) allege BlackRock, State Street and Vanguard conspired via common index-fund ownership to suppress coal-industry output — an antitrust theory novel to asset managers, unresolved; (b) ERISA class actions on BlackRock's LifePath target-date funds have survived motions to dismiss and are in discovery; (c) a securities class action against **BlackRock TCP Capital Corp** (a separate, externally-managed BDC, ticker TCPC) alleges NAV overstatement — BLK is the external manager, not a named defendant in the excerpts found, so direct P&L exposure to BLK looks limited but reputational risk exists. No insider-selling pattern data pulled this cycle (time-boxed).

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q (filed 2026-08-06) and the 2026-07-15 8-K earnings release. Events checked to 2026-09-25 (litigation, BREIT-style items not applicable to BLK). GAAP figures are labelled GAAP; BlackRock's own "as-adjusted" figures are labelled adjusted and are non-GAAP company definitions — see §4 for a case where the two diverged sharply. **Research only, not investment advice; not personalized to any individual’s circumstances.**

## 13. Sources
1. SEC EDGAR submissions/XBRL companyfacts, CIK0002012383: https://data.sec.gov/api/xbrl/companyfacts/CIK0002012383.json
2. Q2-26 8-K earnings release (ex-99.1): https://www.sec.gov/Archives/edgar/data/2012383/000119312526304013/blk-ex99_1.htm
3. Q1-26 8-K earnings release (ex-99.1): https://www.sec.gov/Archives/edgar/data/2012383/000119312526153768/blk-ex99_1.htm
4. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (as_of 2026-09-25)
5. v4/outputs/Q04_triage.json (BLK entry)
6. BlackRock TCP Capital lawsuit reporting (claimdepot.com) and antitrust/ERISA litigation summary (web search, 2026-09-26)
7. v4/outputs/v1_valuation_table.csv (checked: no BLK row)
