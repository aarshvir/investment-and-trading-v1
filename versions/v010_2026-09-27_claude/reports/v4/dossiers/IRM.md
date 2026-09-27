# IRM — Iron Mountain — Diligence Dossier (Agent F87, Wave 5)

## 1. Verdict
**WATCH.** The legacy records-storage annuity is genuinely excellent and still growing; the data-center pivot is
real but is currently consuming more cash than it returns, and the 25-Sep-2026 price appears to require that pivot
to keep compounding at close to management's own aspirational rate for a decade. Horizon: 12–36 months (revisit
as data-center segment margin/ROIC disclosure matures).

## 2. Business in plain English
Iron Mountain stores physical records, media and other assets for corporations and governments — a sticky,
contractual, high-retention business (customers rarely move boxes once stored) generating steady, annuity-like
cash flow. On top of that legacy base, it is building a second growth engine in data centers and IT/asset
lifecycle management (ALM), funded by heavy capex, targeting roughly a third of company revenue over time
(per its own stated ambition, cited in the triage reason).

## 3. Why the model likes it — durable or artefact?
b1 factor file (composite decile 4, quintile 2): momentum (pct_mom_12_1 0.84) and SUE (pct_sue 0.84) both very
strong, consistent with 18.5% revenue growth; quality metrics (gp_a/roe) show blank/NA in the b1 extract for this
name — a **data gap in the quant file itself**, worth flagging as a `data_conflict`: the model is scoring IRM
partly on momentum/SUE without a clean quality read, which understates how capital-intensive the growth actually
is. The growth is real (confirmed in filings below) but its **durability depends on data-center segment margins
inflecting from cash-burning to cash-generative**, which is not yet demonstrated in the cash-flow statement.

## 4. Last several quarters (source: 10-Qs/10-K, SEC EDGAR, XBRL companyfacts CIK0001020569, e.g. accession 0001020569-26-000071; GAAP throughout)
| Quarter | Period | Revenue | YoY growth | Diluted EPS |
|---|---|---|---|---|
| Q2 2025 | Apr–Jun 2025 | $1,711.9M | — | $(0.15) |
| Q3 2025 | Jul–Sep 2025 | $1,754.1M | — | $0.28 |
| Q4 2025 (derived: FY25 total − 9mo) | Oct–Dec 2025 | $1,843.2M | — | $0.30 (derived) |
| Q1 2026 | Jan–Mar 2026 | $1,936.1M | — | $0.48 |
| Q2 2026 | Apr–Jun 2026 | **$2,029.1M** | **+18.5%** vs Q2 2025 | **$0.34** |

TTM diluted EPS (Q3'25–Q2'26): $0.28+$0.30+$0.48+$0.34 = **$1.40**. TTM revenue ≈ **$7,562M** (FY25 $6,901.7M +
H1'26 $3,965.2M − H1'25 $3,304.5M). The +18.5% Q2 growth figure matches the triage's stated number exactly.

## 5. Guidance track record
Not independently re-verified against prior-quarter guidance letters this round — the 8-K accompanying the
2026-08-05 10-Q (accession 0001020569-26-000068) is a cover-page-only filing in this dataset with no press-
release exhibit attached, so I could not confirm the exact guided range vs. delivered numbers from a primary
source. **Data gap, flagged rather than asserted.**

## 6. Earnings quality & balance sheet
- 6-month 2026 operating cash flow: **$887.8M**; capex (property/equipment): **$1,106.2M** → **FCF ≈ −$218.4M**,
  i.e., genuinely negative, consistent with the triage's own red flag ("negative FCF yield from data-center
  capex ramp"). This is not an accounting artefact — it is a real, large, ongoing cash outflow.
- Consolidated (company-wide, entity scope: consolidated) total debt (LongTermDebt tag, includes current
  portion), per the 10-Q balance sheet, at 2026-06-30: **$17,349.6M** (noncurrent portion $17,128.8M).
  Consolidated cash at 2026-03-31: $250.7M (June-30 figure not captured this round — data gap). Consolidated net
  debt therefore roughly **$17.0–17.1B**, up from a consolidated $16.2B at 2025-09-30 — leverage is rising as
  capex outpaces internally generated cash, funded by debt issuance.
- Weighted average diluted shares rising modestly (297.8M FY25 → 299.8M Q2'26) — mild dilution from equity/ATM
  issuance is plausible but not confirmed as the cause this round.
- REIT-standard AFFO figure was not extracted from a primary-source press release this pass (custom non-XBRL
  tag) — **data gap**; GAAP EPS materially understates cash generation for any REIT because of heavy real-estate
  depreciation, so the P/E-style multiple below should be read with that caveat.

## 7. Valuation: reverse DCF and reconciliation with V1
**No V1 row exists for IRM in `v1_valuation_table.csv`** → v1_verdict = null.

Given FCF is currently negative from the growth-capex cycle, a literal FCF reverse-DCF is not meaningful this
year. Instead: enterprise value ≈ market cap $33.16B (b1 file, 2026-09-25) + consolidated net debt ~$17.1B ≈
**$50.3B**.
Using an estimated (not filed — flagged as an estimate) blended EBITDA margin of ~34% on TTM revenue $7.56B gives
EBITDA ≈ $2.57B, i.e., **EV/EBITDA ≈ 19.6x**. For a REIT-like business with cost of capital around 7.5%, a
multiple this high typically requires roughly **13–15%/year EBITDA growth sustained for a decade** before fading
to a low terminal rate — which is close to, but a bit above, management's own stated ambition (data centers
reaching ~1/3 of revenue) and well above the legacy storage business's own low-single-digit organic growth.
**Implied growth is above my base case** (which discounts execution risk on the still-unprofitable-on-FCF data-
center build and assumes growth decelerates toward high-single digits as the buildout matures) — so per the
mandate, this leans away from INCLUDE despite being a quality legacy business.

## 8. Bull case / Bear case
**Bull:** (1) Legacy records-storage cash flow is genuinely annuity-like — very low churn, pricing power.
(2) Data-center backlog and revenue are scaling fast (+18.5% company-wide) and could inflect to FCF-positive as
built capacity leases up. (3) Diversification reduces reliance on a structurally declining physical-records
market long-term.

**Bear:** (1) FCF has been negative for at least two consecutive quarters funded by rising debt — if data-center
leasing or pricing disappoints, leverage keeps climbing with no offset. (2) GAAP EPS ($1.40 TTM) implies an ~80x
P/E, and even adjusting for REIT depreciation add-backs the multiple is not obviously cheap once the capex is
counted. (3) Data-center capex is a highly competitive, capital-intensive business against much larger dedicated
players (Digital Realty, Equinix) with more established scale.

## 9. Kill criteria (measurable)
1. FCF (OCF − capex) remains negative for **four consecutive quarters** with no improving trend in the
   quarterly deficit.
2. Consolidated net debt exceeds **$19B** without a corresponding step-up in disclosed data-center run-rate revenue.
3. Data-center segment revenue growth decelerates below **+15% YoY** for two consecutive quarters.
4. Weighted-average diluted share count grows **>3% YoY** (signals equity-funded capex diluting the legacy
   annuity holders).
5. Any dividend cut or dividend-coverage disclosure showing AFFO payout ratio above 100% for two consecutive
   quarters.

## 10. Catalysts & calendar
Next earnings: Q3 2026, expected early November 2026 (pattern: Q3 2025 10-Q, accession 0001020569-25-000206,
filed 2025-11-05).

## 11. Red-flag scan
No auditor changes, restatements, going-concern language or SEC/DOJ investigation disclosures identified in the
sections reviewed. No short-seller report identified this round. Insider Form 4 pattern not reviewed this round
(data gap, time-boxed).

## 12. Sources
1. SEC EDGAR submissions, CIK0001020569, https://data.sec.gov/submissions/CIK0001020569.json (accessed 2026-09-27).
2. SEC EDGAR XBRL companyfacts, CIK0001020569, https://data.sec.gov/api/xbrl/companyfacts/CIK0001020569.json
   (accessed 2026-09-27; latest quarter incorporated: 10-Q accession 0001020569-26-000071, filed 2026-08-05,
   period ended 2026-06-30).
3. v4/data/b1_live_scores.csv (IRM row, as_of 2026-09-25).
4. v4/outputs/Q14_triage.json (IRM entry).
5. v4/outputs/v1_valuation_table.csv (checked — no IRM row present).

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q (accession 0001020569-26-000071), period ended 2026-06-30, filed
2026-08-05. Events checked to
2026-09-25 via SEC EDGAR submission list (no later 10-Q/10-K found; the one subsequent 8-K on the list,
2026-08-05, is a cover-page-only filing with no press-release exhibit in this dataset). All figures above are
**GAAP** unless explicitly marked as an estimate (the EBITDA-margin and EV/EBITDA figures in Section 7 are my own
estimates, not filed numbers). AFFO, exact guidance-letter wording and Form 4 insider pattern were **not
independently re-verified this round** and are flagged as data gaps rather than asserted. Research, not personal
investment advice.
