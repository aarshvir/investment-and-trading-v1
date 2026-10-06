# DUK — Duke Energy Corporation — Diligence Dossier (F97, Wave 6)

## 1. Verdict
**INCLUDE** — regulated multi-state utility **[Corrected 2026-10-06: verdict restated to INCLUDE-SMALL because 'below-guidance implied growth' no longer holds, see Correction section DV13]** trading at a below-guidance implied growth rate, with a credible, rate-base-driven earnings algorithm and a growing Carolinas/data-center demand pipeline. Thesis horizon: 24–36 months.

## 2. Business in plain English
Duke Energy owns regulated electric utilities in the Carolinas, Florida, Indiana, Ohio/Kentucky and a regulated gas utility (Piedmont), serving ~8.6M electric and gas customers. It earns a state-regulated return on the capital ("rate base") it invests in poles, wires, plants and gas pipes; revenue and profit grow mainly by (a) investing more capital (data-center and industrial load growth, grid hardening, generation build) and (b) periodically raising rates in commission-approved cases. It is not a commodity-price business — nearly all fuel costs pass through to customers.

## 3. Why the model likes it / is it durable?
Quant score: composite decile 9 (top decile), driven by quality (gp/assets, ROE ~9.4% reported, high leverage percentile reflecting normal utility capital structure) and a strong SUE percentile (0.63) — i.e., recent earnings have been beating trend. This is durable, not an artefact: regulated ROE and rate-base growth are structural, not cyclical, and the SUE beat is corroborated by the Q2 2026 print (adjusted EPS $1.43 vs. $1.25 a year ago, +14%) driven by the same rate-base recovery mechanism, not one-offs. One caution: `leverage` percentile is elevated (0.98) because DUK is intentionally issuing debt to fund the capital program — a normal utility feature but worth tracking (§9).

## 4. Last two quarters (GAAP, consolidated; source: 10-Q filed 2026-08-04, period 2026-06-30)
| | Q2 2026 | Q2 2025 | Δ | H1 2026 | H1 2025 | Δ |
|---|---|---|---|---|---|---|
| Total operating revenues | $7,592M | $7,508M | +1.1% | $16,770M | $15,757M | +6.4% |
| Operating income | $2,049M | $1,830M | +12.0% | $4,774M | $4,173M | +14.4% |
| Net income avail. to common | $1,077M | $971M | +10.9% | $2,613M | $2,336M | +11.9% |
| Diluted EPS (GAAP) | $1.38 | $1.25 | +10.4% | $3.33 | $3.00 | +11.0% |
| Diluted EPS (adjusted, non-GAAP, per press release) | $1.43 | $1.25 | +14.4% | n/a in release | n/a | — |

Q1 2026 (per 10-Q filed 2026-05-05/XBRL): revenue $9,178M, **total** net income $1,550M (pre-NCI/preferred; not directly comparable to the "avail. to common" row above), diluted EPS $1.97 — Q1 is seasonally the strongest quarter (winter heating). No revenue deceleration visible; the reported/adjusted gap in Q2 is regulatory-settlement charges, not aggressive non-GAAP add-backs (10-Q, Note; press release EX-99.1, 2026-08-04).
*(Basis note: the §4 table's "Net income avail. to common" row ($1,077M/$971M Q2; $2,613M/$2,336M H1) is Net Income Available to Duke Energy Corporation Common Stockholders, i.e. after NCI and preferred dividends, per the 10-Q Statement of Operations R2.htm — a different, smaller-by-definition figure than total consolidated Net Income and than the Q1 2026 total-net-income figure above; both are correctly sourced, just different line items/periods.)*

## 5. Guidance track record
Q2 2026 release (filed 2026-08-04): "reaffirming its 2026 adjusted EPS guidance of $6.55 to $6.80 and long-term adjusted EPS growth rate of 5% to 7% through 2030 off the 2025 midpoint of $6.30, with confidence to earn in the top half of the range beginning in 2028." This is a **reaffirmation**, not a raise, of the range set at FY2025 results (10-K, filed 2026-02-26, FY2025 diluted EPS $6.31). **[Corrected 2026-10-06: the range was set with the Q4 2025 earnings release (8-K acc. 0001326160-26-000007, 2026-02-10); the 10-K (2026-02-26) reports FY2025 diluted EPS $6.31]** DUK does not forecast GAAP EPS. No guidance cut has occurred across the two quarters reviewed.

## 6. Earnings quality & balance sheet (consolidated, "the Company" = Duke Energy Corp; source: 10-Q R2/R5/R7 exhibits, period 2026-06-30 vs. 2025-12-31)
- **FCF conversion:** H1 2026 operating cash flow $4,272M vs. capex $8,240M ⇒ **negative free cash flow of ~$3,968M** for the half (H1 2025: OCF $5,040M vs. capex $6,428M, FCF −$1,388M). This is structural for a utility mid-build-out, not a red flag by itself, but it means all growth capex plus dividends ($1,693M paid in H1 2026) is externally financed.
- **Balance sheet (consolidated):** Total assets $201,091M (Jun-26) vs. $195,736M (Dec-25); Long-term debt (incl. VIEs) $82,242M vs. $80,108M; Total equity $56,863M vs. $53,019M; cash $673M.
- **Leverage:** consolidated LT debt/equity ≈ 1.45x (Jun-26). No consolidated net-debt/EBITDA is disclosed in the 10-Q; a full reverse-engineered EBITDA calc was out of scope this cycle — treat as a data gap, not a favorable assumption.
- **Financing:** dividends paid $1,693M (H1'26) vs. $1,610M (H1'25); H1 2026 also shows one-off proceeds of $2,501M from the sale of Piedmont's Tennessee gas business and $2,827M of NCI contributions (minority partner capital, e.g., data-center/generation JVs) that helped offset the capex/FCF gap — these are financing-structure items, not deteriorating quality.
- **Credit:** the 10-Q's risk-factor cross-reference to the FY2025 10-K flags credit ratings and debt-covenant compliance as an explicit risk; no downgrade is disclosed in this filing.

## 7. Valuation snapshot & reverse DCF
- Price (2026-09-25 close, per b1_live_scores.csv): **$113.35**. FY2026 guided adjusted EPS midpoint $6.675 ⇒ NTM P/E ≈ **17.0x** (matches quant snapshot's ~16x tag).
- Annualized dividend (2×H1'26 paid/share, ≈$2.17/share H1 ⇒ ~$4.34/yr) ⇒ dividend yield ≈ **3.8%**.
- **Reverse DCF (Gordon dividend-growth sense-check):** solving P = D₁/(r−g) for g at an assumed cost of equity r = 7.8% (assumption: BBB+ regulated utility, low beta ~0.45–0.5, rf ≈4.2%, ERP ≈6–7%; this r is an analyst estimate, not a filed number) gives **implied perpetual growth g ≈ 4.0%** — **below** the company's own guided 5–7% long-term adjusted-EPS growth range. **implied_vs_base = below.** **[Corrected 2026-10-06: restated 2026-10-06 to **in_line**: with the risk-free rate at 5.17% (not 4.2%) and a two-stage test the price implies about 7.0-7.7%/yr dividend/EPS growth for 10 years vs the guided 5-7%; see Correction section DV13]**
- No V1 systematic valuation row exists for DUK in `v1_valuation_table.csv` (checked; absent) — v1_verdict = null.

## 8. Bull / Bear
**Bull:** (1) Carolinas/Southeast data-center and industrial load growth pulls forward rate-base investment beyond the current plan; (2) constructive regulatory settlements (as flagged in Q2 release) continue, supporting the "top half of range" 2028 ambition; (3) further non-core asset sales (Piedmont TN precedent) fund growth without equity dilution.
**Bear:** (1) capex continues to outrun operating cash flow, forcing more debt/NCI financing and credit-metric pressure; (2) regulatory lag or an adverse rate case slows recovery of the growing asset base; (3) data-center demand growth disappoints (10-Q's own risk factors flag this explicitly) and rate-base growth reverts toward GDP-like trend.

## 9. Kill criteria (measurable)
1. FY adjusted EPS guidance ($6.55–$6.80) is **cut** at any quarterly release (vs. reaffirmed/raised).
2. Consolidated long-term debt grows >8% in a single fiscal year without a matching equity/NCI raise (i.e., leverage build accelerates beyond the current run-rate — Jun-26 LT debt +2.7% in one quarter alone **[Corrected 2026-10-06: wrong period: $82,242M vs $80,108M at 2025-12-31 is +2.7% over six months; over the quarter (vs $80,477M at 2026-03-31) it is +2.2%]**).
3. Two consecutive quarters of YoY adjusted EPS growth below 3% (below the low end of the long-term algorithm).
4. A credit-rating downgrade to BBB or equivalent (from current investment-grade BBB+/A- tier) by S&P or Moody's.
5. A major adverse rate-case order (disallowed capex >$500M in a single jurisdiction) in the Carolinas or Florida.

## 10. Catalysts & calendar
Next quarterly results: estimated ~2026-11-05 (based on the FY2025 cadence: Q3 2025 10-Q filed 2025-11-07); no confirmed date found in filings reviewed. Rate cases in the Carolinas/Florida/Indiana are ongoing per the 10-K/10-Q risk-factor cross-references (docket-level detail not pulled this cycle — data gap).

## 11. Red-flag scan
- **Litigation:** Item 1 of the Q2 2026 10-Q incorporates the FY2025 10-K's legal-proceedings disclosure by reference and states no material developments in the quarter (10-Q, filed 2026-08-04). No new material litigation identified.
- **Accounting:** no restatement, no material weakness, no going-concern language found in a full-text search of the Q2 2026 10-Q.
- **Environmental/regulatory:** coal-ash (CCR) remediation liability remains an explicitly disclosed, ongoing cost/recovery-timing risk (21 mentions in the 10-Q) — not new, but real and worth tracking as a recovery-lag risk, not a going-concern issue.
- **Insider activity:** one Rule 10b5-1 plan disclosed (EVP/Chief Administrative Officer, adopted 2026-05-12, sale of up to 2,900 shares) — immaterial in size.
- No short-seller reports identified in this pass (not exhaustively searched — data gap).

## 12. Sources
1. SEC EDGAR, Duke Energy 10-Q, period 2026-06-30, filed 2026-08-04, accession 0001326160-26-000040 (Statements of Operations R2.htm, Balance Sheets R5.htm, Cash Flows R7.htm, Legal Proceedings/Risk Factors, full text).
2. SEC EDGAR, Duke Energy 8-K Ex-99.1 earnings release, "Duke Energy reports second-quarter 2026 financial results," filed 2026-08-04, accession 0001326160-26-000037.
3. SEC EDGAR, Duke Energy 10-K, FY2025, filed 2026-02-26, accession 0001326160-26-000014 (FY2025 EPS $6.31, guidance baseline).
4. SEC EDGAR, XBRL company facts API, CIK0001326160 (companyfacts JSON), retrieved 2026-09-27.
5. `v4/data/b1_live_scores.csv` (quant factor scores, price $113.35 as of 2026-09-25); `v4/outputs/Q14_triage.json` (prior triage call); `v4/outputs/v1_valuation_table.csv` (checked — no DUK row).

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (period end 2026-06-30), 10-Q filed 2026-08-04. Checked for events to 2026-09-25 via the SEC submissions feed (latest filing on record: an 8-K filed 2026-09-25, not opened this cycle — content not reviewed, flagged as a residual gap). GAAP figures are labelled GAAP; the one adjusted-EPS figure used is labelled "adjusted (non-GAAP)" per the company's own release. Research, not personal investment advice.

## Correction (verification DV13, 2026-10-06)
**Verification scope:** Q2 2026 results and guidance (8-K Ex-99.1 acc. 0001326160-26-000037; 10-Q acc. -000040; XBRL), the debt and cash-flow figures, the reverse DCF and the post-10-Q 8-Ks (2026-08-05, 2026-08-13, 2026-09-25). **Verdict changes from INCLUDE to INCLUDE-SMALL** (item 2); `implied_vs_base` changes from "below" to "in_line". F97_summary.json DUK entry updated.

**FAIL 1 - LT-debt growth period (sections 9, kill criterion 2).** Wrong text: "Jun-26 LT debt +2.7% in one quarter alone". Correct: long-term debt (net of current maturities) was $82,242M at 2026-06-30 vs $80,108M at 2025-12-31 (+2.7% in six months) and $80,477M at 2026-03-31 (+2.2% in the quarter). Total debt is larger than the long-term line used for leverage: add current maturities $6,666M and notes payable/commercial paper $2,330M, giving $91,238M (1.60x total equity of $56,863M, not 1.45x). Verdict effect: none by itself.

**FAIL 2 - Reverse DCF and verdict (sections 1, 7).** The dossier uses a risk-free rate of 4.2% (the 10-year Treasury was 5.17% on 25 Sep 2026 after the 16 Sep hike), an ERP of 6-7% and beta 0.45-0.5 for a 7.8% cost of equity, and solves a perpetuity (g about 4.0%) that it compares with a 5-7% growth range that runs only to 2030. Corrected for the risk-free rate alone the cost of equity is about 8.4%-8.7% (5.17% + the dossier's own 3.0-3.5-point equity premium; 8.3%-9.0% with ERP 4.5% x beta 0.7-0.85). On the dividend basis (declared $1.065 a quarter = $4.26 a year; the dossier's $4.34 uses cash paid including preferred; price $113.35) a two-stage test with 3% terminal growth gives implied 10-year growth of 5.5% at 7.8%, **7.0% at 8.4% and 7.7% at 8.7%**, i.e. at or above the top of the 5-7% guidance (a 6%-growth base case is worth about $104.8 at 8.4% and $99.4 at 8.7% against $113.35). A perpetuity at 8.4%-8.7% needs 4.4%-4.7%, so on the dossier's own method the 'below' margin shrinks to under half a point. The scenario table's base return of +8% a year equals a cost of equity of 8.4%, consistent with in line. Implied is therefore **in line**, not below; full-weight INCLUDE (which the dossier justifies only by 'below-guidance implied growth') is not supported, so the verdict is **INCLUDE-SMALL** (same treatment as DHI/DTE at in_line). Scenarios unchanged.

**MINOR items (no text change required):**
- Post-10-Q events not in the dossier (it states the 2026-09-25 8-K was not opened): 8-K 2026-08-13 (acc. 0001104659-26-095903) records the sale of 40,000,000 equity units ($50 stated amount, $2.0bn) with purchase contracts to buy Duke common stock by 1 Aug 2029, i.e. future equity issuance (bull case 3 'without equity dilution'); 8-K 2026-09-25 (acc. -110588) is the appointment of Joyce Mullen to the board (benign).
- Section 4: the $3.33 H1 2026 diluted EPS is continuing operations ($3.35 including discontinued operations of $0.02); Q1 2026 diluted EPS $1.97 includes discontinued operations ($1.95 continuing).
- Dividend: declared $1.065 per quarter ($2.130 H1 2026 vs $2.090).
- Verified as stated: Q2 revenue $7,592M vs $7,508M, operating income $2,049M vs $1,830M, net income to common $1,077M vs $971M (H1 $2,613M vs $2,336M), GAAP EPS $1.38 vs $1.25 (H1 $3.33 vs $3.00), adjusted EPS $1.43 vs $1.25, guidance quote verbatim, H1 OCF $4,272M vs capex $8,240M (FCF -$3,968M), dividends paid $1,693M, Piedmont Tennessee sale proceeds $2,501M, NCI contributions $2,827M, total assets $201,091M, total equity $56,863M, cash $673M.
- Not in the filings reviewed (unverifiable): ratings tier, 2026-11-05 earnings date, 10b5-1 plan details.
