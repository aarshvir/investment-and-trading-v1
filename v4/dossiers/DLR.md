# Digital Realty Trust, Inc. (DLR) — Diligence Dossier

**Agent:** F42 (wave-2 standard diligence) | **As of:** 2026-09-25 close ($178.61, mkt cap ≈ $66.8bn per Yahoo/d4 snapshot)

## 1. Verdict
**INCLUDE-SMALL** (12–36 month horizon), reservation: the growth is real and well-evidenced (record backlog, raised guidance three quarters running) but the company is funding an AI-datacenter capex supercycle with **both** rising leverage-adjacent development spend **and** heavy ATM equity dilution, and carries an unresolved SEC inquiry into its cybersecurity-disclosure controls — this is a "pay up for quality growth" REIT, not a cheap one.

Thesis (plain English): the largest data-center REIT by footprint is riding the AI/hyperscale build-out, with $1.9bn of already-signed leases yet to start paying rent — but investors are being asked to fund record development capex through equity issuance, and the accounting P/E (62x) is meaningless; use Core FFO, not GAAP EPS, to judge this stock.

## 2. Business in plain English
All figures below are on a **consolidated** basis (Digital Realty Trust, Inc., the parent REIT, plus its operating partnership and subsidiaries); no standalone-only figures are used. Digital Realty owns and operates data centers (colocation and hyperscale wholesale capacity) that it rents to cloud providers, enterprises, and network/interconnection customers on multi-year leases, plus a fast-growing "0–1MW plus interconnection" retail-colocation business. It earns rent (with contractual escalators), interconnection fees, and (increasingly) revenue from joint-venture stakes in large hyperscale campuses (e.g., a newly acquired 64% stake in three Northern Virginia hyperscale data centers). Its moat is scale, power/land access in constrained markets, and a global interconnected-campus network that is expensive and slow for competitors to replicate — offset by intense capital intensity and a highly cyclical, AI-capex-dependent demand base.

## 3. Why the model likes it — durable or artefact?
Triage (Q13, quality 4/5, growth 4/5, price_vs_growth 4/5) flagged the $1.9bn signed-not-yet-commenced backlog and $20bn under construction, using a cost-of-capital-minus-FCF-yield heuristic (≈9%−5.6%=3.4% required growth) against actual 29.9% revenue growth — a wide margin. The triage separately flagged **net debt/EBITDA "5.7x, high even for a REIT"** as a red flag needing verification; the primary-source Q2 2026 release states **net debt/adjusted EBITDA of 4.7x**, flat vs Q1 2026 and *improved* from 5.1x a year ago — **data conflict, resolved in DLR's favour**: leverage is elevated for a REIT but not rising, and the triage's 5.7x figure does not match the company's own reported ratio (source discrepancy noted, not investigated further this pass). The v4 quant composite (`b1_live_scores.csv`) ranks DLR poorly (composite 0.161, decile 2, live_rank 417/503) with a **very weak Quality family score (fam_Q 0.035)** — this is very likely a REIT-accounting artefact (the Q family uses gross-profit/assets, accruals and asset-growth measures that misread REITs' straight-line depreciation and land/building capitalisation, per the sector playbook) rather than a genuine quality problem, and is flagged as a data_conflict below.

## 4. Last two quarters
GAAP figures from SEC 10-Q/8-K (USD millions except per-share); **GAAP EPS is not a meaningful metric for this REIT** (real-estate depreciation and one-off gains on JV/asset sales swing it wildly — Q2 2025 GAAP diluted EPS was $2.94 on a large one-off gain, versus $0.15–$0.46 in adjacent quarters) — Core FFO per share is the correct earnings measure and is used below.

| Metric | Q1 2026 (end 2026-03-31) | Q2 2026 (end 2026-06-30) |
|---|---|---|
| Total revenue | $1,635.2m (GAAP, XBRL) | $1,924m (press release; +18% sequential, +29% YoY) |
| Core FFO / share (ex. net promote) | $2.04 | **$2.65** (incl. net promote); $2.13 ex-promote |
| GAAP net income (available to common) | $179.3m | not separately extracted this pass |
| Operating cash flow | $532.4m (Q1 discrete) | not separately extracted (YTD only) |

Leasing: Q2 2026 total signed bookings $307m (100% share) / $208m (DLR share); zero-to-1MW-plus-interconnection bookings hit a record $108m, the **third straight quarterly record**; renewal spreads surged to **25%+**; backlog reached a **record $1.9bn** (100% share, $1.4bn DLR share), ~30% of in-place revenue. Additional hyperscale leases were signed after quarter-end.

Source: SEC EDGAR 10-Q Q1 2026 (filed 2026-05-01) and Q2 2026 (filed 2026-07-31); 8-K Ex-99.1 Q2 2026 earnings release (filed 2026-07-23); XBRL cross-check via `data.sec.gov/api/xbrl/companyfacts/CIK0001297996.json` (note: the companyfacts JSON had not yet ingested full Q2 2026 line items as of this pass — Q2 revenue/FFO figures above are sourced to the primary earnings-release exhibit, which is itself an SEC filing).

## 5. Guidance track record (last two releases vs prior range)
- **Q1 2026 release (Apr 2026):** FY26 Core FFO/share (ex. net promote) guided **$8.00–$8.10**.
- **Q2 2026 release (Jul 2026):** FY26 Core FFO/share (ex. net promote) guidance **raised** to **$8.15–$8.20**; constant-currency Core FFO/share raised to $8.10–$8.15 (from $7.95–$8.05); FY26 revenue guidance raised to $6.85–$6.95bn (from $6.65–$6.75bn); same-capital cash NOI growth raised to 4.25–5.25% (from 4.0–5.0%); **renewal cash rental-rate-increase guidance raised sharply to 9.0–11.0%** (from 6.5–8.5%). This is a genuine, broad-based guidance raise across revenue, FFO and leasing-economics metrics — not merely a beat-and-hold.

## 6. Earnings quality & balance sheet (REIT metric set — see sector playbook)
- **Leverage:** net debt / adjusted EBITDA **4.7x** (flat Q1→Q2 2026; down from 5.1x a year ago); debt-plus-preferred / enterprise value 22.3% (down from 22.7% Q1 2026); fixed-charge coverage 5.2x; Q2 interest expense $113.9m. New long-term debt issuance guided at **4.5–5.5%** pricing (raised from 4.0–4.5% — a real, disclosed increase in marginal borrowing cost).
- **Development capex and dilution:** FY26 development capex guidance raised to **$4.25–4.75bn** (net of partner contributions) to hit targeted 10%+ stabilised yields on new capacity. YTD through Q2 2026 the company sold **13.5 million shares at an average $184.94 via its ATM programme, raising $2.5bn** — real, ongoing dilution funding the growth, which is the standard trade-off for this business model (see REIT sector playbook: never judge FCF/dividend coverage without checking the funding source of growth capex).
- **JV concentration:** a $3.5bn, 64%-stake acquisition of three Northern Virginia hyperscale data centers adds anchor-tenant/partner concentration risk typical of the sector.
- **FX:** guidance carries a $0.05/share constant-currency headwind, flagging real international-revenue translation exposure.
- **GAAP vs Core FFO gap:** GAAP EPS is depreciation- and gain-distorted (see §4); the 62x raw trailing P/E the triage flagged is a GAAP artefact, not a valuation signal — Core FFO-based multiples are used throughout §7.

## 7. Valuation snapshot and reverse-multiple check (REIT framework, not FCFF DCF)
No V1 systematic-valuation row exists for DLR (outside V1's original 69-name universe) — **v1_verdict = null**. Per the finance-skills REIT playbook, P/E and generic reverse-FCF-DCF are the wrong tool here (REIT depreciation and gain/loss accounting break both); the correct anchor is **P/Core FFO** and the implied cap rate.

- **P/Core FFO:** $178.61 ÷ ~$8.175 (FY26 guide midpoint, ex-net-promote) ≈ **21.9x** — a premium to the developed-market office-REIT range (12–18x) that the sector playbook flags as normal for a **contracted, hyperscale-demand growth REIT** rather than a stabilised income REIT; comparable data-center peers command similar-to-higher multiples in the current AI-capex cycle (not independently peer-benchmarked this pass — flagged as a limitation).
- **Reverse dividend-discount sanity check:** trailing dividend yield ≈2.7% (Yahoo/d4 snapshot); at an estimated ~8% cost of equity for a REIT running 4.7x leverage, the yield alone implies the market requires only **≈5.3%/yr** perpetual distribution growth — well below the double-digit Core FFO/share growth management is currently guiding to for 2026 (and says the backlog supports "through 2027 and 2028"). This is the basis for calling the valuation **"in_line"** rather than "expensive": the price does not appear to demand the company sustain today's growth rate indefinitely, only that it decelerate toward high-single-digit/low-double-digit — a lower bar than current guidance implies.
- `implied_vs_base`: **in_line**.

Scenario framework (analyst estimate; Core FFO/share compounding + multiple + dividend yield, 3-year horizon):
- **Bear (30%):** hyperscale capex pause, dilution/leverage force multiple compression — Core FFO/share ~3%/yr to $8.93, exit 16x → ~$143 (**≈ −4.3%/yr, 3y annualised** incl. dividend).
- **Base (45%):** backlog converts as guided, ~9%/yr Core FFO/share growth to $10.59, exit ~20x (slight de-rate from 21.9x) → ~$212 (**≈ +8.6%/yr**).
- **Bull (25%):** hyperscale demand stays structurally undersupplied, ~13%/yr growth to $11.80, exit 23x → ~$271 (**≈ +17.8%/yr**).

## 8. Bull case / bear case
**Bull:** (1) A record $1.9bn signed-not-commenced backlog (~30% of in-place revenue) gives multi-year visibility that few REITs can match. (2) Leasing economics are accelerating, not decelerating — renewal spreads jumped to 25%+ and 0–1MW-plus-interconnection bookings hit a third consecutive quarterly record. (3) Leverage (4.7x) is stable-to-improving even through the heaviest development phase, evidence of disciplined balance-sheet management alongside the growth.

**Bear:** (1) Growth is being funded by continuous ATM equity issuance ($2.5bn YTD) — existing holders are diluted every quarter this cycle continues, and per-share metrics (not aggregate FFO) are what matter. (2) An open SEC investigation into the adequacy of DLR's cybersecurity-risk disclosures and disclosure controls is unresolved; the company calls it immaterial but cannot yet prove that. (3) The business is now more exposed to a small number of hyperscale/JV counterparties (the new $3.5bn Northern Virginia stake) — a concentrated bet on AI-capex durability that would re-rate sharply lower if hyperscaler capex plans slow.

## 9. Key risks & kill criteria (measurable)
1. Net debt/adjusted EBITDA rises above 5.5x (vs 4.7x now) without a corresponding acceleration in backlog conversion.
2. FY26 Core FFO/share guidance is cut (vs the current $8.15–$8.20 ex-net-promote range) at the Q3 2026 release (2026-10-22).
3. Same-capital cash NOI growth falls below 4.0% for two consecutive quarters (vs the 4.25–5.25% FY26 guide).
4. ATM share issuance for the full year exceeds ~$4bn (vs $2.5bn through Q2) without matching growth in per-share Core FFO — a sign dilution is outrunning growth.
5. The SEC cybersecurity-disclosure inquiry results in a material enforcement action or restatement.

## 10. Catalysts & calendar
Next earnings: **2026-10-22** (Q3 2026, after market close). Other: continued hyperscale lease signings post-Q2 quarter-end (already flagged by management), development-yield updates on the $4.25–4.75bn FY26 capex programme, any update on the SEC cybersecurity-disclosure inquiry.

## 11. Red-flag scan
- **SEC investigation (unresolved):** the SEC is investigating the adequacy of Digital Realty's cybersecurity-risk disclosures and related disclosure controls and procedures; the company is cooperating, says it is not aware of any cybersecurity event that prompted the inquiry, and does not expect a material cost — but the matter is open, not closed.
- **Data breach:** a law firm (Federman & Sherwood) opened an investigation into a data breach involving unauthorized access to DLR corporate systems around 2025-01-08; status/materiality not independently confirmed this pass.
- **Historical litigation (not current):** Digital Realty Trust, Inc. v. Somers, a 2018 U.S. Supreme Court whistleblower-protection case — resolved, included only for completeness, not a live risk.
- **Dilution:** $2.5bn of YTD ATM equity issuance is disclosed and not concealed, but is a real, ongoing per-share dilution factor (see §6/§8).
- No auditor change, restatement, or going-concern language found this pass.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: **Q2 2026, quarter ended 2026-06-30**, 10-Q filed 2026-07-31 (SEC EDGAR accession 0001104659-26-089296) and 8-K Ex-99.1 earnings release filed 2026-07-23. Checked for events to 2026-09-25: no subsequent results, rating actions, or M&A approvals identified that would change this verdict; the SEC cybersecurity inquiry remains open with no new disclosed developments as of this pass. GAAP figures are labelled GAAP; Core FFO is DLR's own NAREIT-based non-GAAP measure and is labelled as such throughout. **Research only — not personalised investment advice; kill criteria in §9 are the observable signposts that would change this verdict.**

### Sources
1. SEC EDGAR — DLR 10-Q Q1 2026 (filed 2026-05-01): https://www.sec.gov/Archives/edgar/data/1297996/000110465926054255/dlr-20260331x10q.htm
2. SEC EDGAR — DLR 10-Q Q2 2026 (filed 2026-07-31), accession 0001104659-26-089296.
3. SEC EDGAR — 8-K Ex-99.1, Digital Realty Q2 2026 earnings release (filed 2026-07-23): https://www.sec.gov/Archives/edgar/data/0001297996/000110465926086270/dlr-20260723xex99d1.htm
4. SEC data.sec.gov XBRL companyfacts (CIK0001297996), retrieved 2026-09-26.
5. Investing.com, "Digital Realty lifts 2026 outlook after record Q2 2026" earnings-call transcript: https://www.investing.com/news/transcripts/earnings-call-transcript-digital-realty-lifts-2026-outlook-after-record-q2-2026-93CH-4810202
6. SEC EDGAR — DLR 10-Q Q2 2025 (net debt/EBITDA year-ago comparison context): https://www.sec.gov/Archives/edgar/data/1297996/000155837025009991/dlr-20250630x10q.htm
7. Federman & Sherwood, Digital Realty data-breach investigation notice.
8. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (quant context, retrieved 2026-09-25 20:28 UTC per file metadata).
9. v4/outputs/Q13_triage.json (DLR triage entry).
