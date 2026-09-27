# Aon plc (NYSE: AON) — Fundamental Diligence Dossier

**Prepared by:** F62 (fundamental diligence analyst, wave 3) | **Data cutoff:** 2026-09-25 close | **Most recent period incorporated:** Q2 2026 10-Q (filed 2026-07-29, period ended 2026-06-30); 8-K announcing the USI acquisition (filed 2026-08-31, dated 2026-08-30) also incorporated as a subsequent, not-yet-closed event. Checked for events to 2026-09-25. Next scheduled report: 2026-10-30 (Q3 2026 results, per `d4_live_snapshot`). **Basis:** consolidated Aon plc GAAP unless labeled "adjusted" (the company's own non-GAAP reconciliation, quoted from its Ex-99.1 releases). **Entity scope:** all balance-sheet and debt figures are from Aon plc's Condensed Consolidated Statements of Financial Position (10-Q, filed 2026-07-29) — fully consolidated; fiduciary assets/liabilities ($20,698M each at 2026-06-30, client/insurer pass-through funds) are excluded from the net-debt calculation below as they are not Aon's own leverage.

**Data-quality note:** every number is sourced to SEC EDGAR primary filings (10-Q, 8-K Ex-99.1 earnings and M&A press releases) or SEC XBRL company facts (`data.sec.gov/api/xbrl/companyfacts/CIK0000315293.json`, current through the Q2 2026 10-Q), cited in §12 with filing dates. Quant context is from `v4/data/b1_live_scores.csv` and `v4/data/d4_live_snapshot.parquet`; no V1 valuation row exists for AON (`v1_valuation_table.csv` — 92 names, AON not among them), so `v1_verdict` is null. Research output for internal process use, not personalized investment advice.

## 1. Verdict: INCLUDE-SMALL — thesis horizon: 24–36 months
Aon is one of three global mega-brokers (with Marsh McLennan and, since Aon's own abandoned 2021 bid, Willis Towers Watson) — a durable, recurring-commission business with genuine scale advantages, expanding margins, and a management team that has reaffirmed the same full-year framework (mid-single-digit-or-better organic growth, 70–80bps adjusted-margin expansion, strong adjusted EPS growth, double-digit FCF growth) at every one of the last three quarterly releases without a cut. The reverse DCF below shows the market pricing in only ~4% 10-year FCF growth against a company that has delivered mid-teens FCF growth in FY2025 — a reasonably attractive entry point for the quality on offer. The **specific, named reservation** for INCLUDE-SMALL rather than full INCLUDE: on 2026-08-30, Aon signed a **$17.0 billion, all-debt-financed agreement to acquire USI** (closing expected Q4 2026), which this dossier estimates will push pro forma net debt/EBITDA from ~2.3x today toward the low-4x range at close before any synergy ramp or deleveraging, and management has explicitly said **share buybacks are paused near-term** to prioritize debt paydown — a real, dated change to the capital-return profile that the market may not yet have fully digested, layered on top of a first-half 2026 free-cash-flow growth deceleration (+4% YoY, versus 14–16% in FY2025) that itself deserves watching.

## 2. Business in plain English
Aon is a global professional-services firm operating through four segments: **Commercial Risk Solutions** (property & casualty insurance brokerage for corporations), **Reinsurance Solutions** (treaty/facultative reinsurance placement for insurers), **Health Solutions** (employee health & benefits brokerage/consulting) and **Wealth Solutions** (retirement/investment advisory, following the 2025–26 divestitures of the NFP Wealth business and Stroz Friedberg). It earns commissions and fees for advising and placing risk/insurance/benefits programs on behalf of corporate and institutional clients, competing on scale, proprietary data/analytics ("context advantage"), and global reach against Marsh McLennan and Willis Towers Watson.

## 3. Why the model likes it — durable or artefact?
Quant snapshot (`b1_live_scores.csv`, 2026-09-25): composite **0.163** (decile 2, live_rank 416/503 — outside the model's own top tier; AON reached this diligence batch via the triage route, per the triage note's 44.7% ROE / 14–15x forward P/E flag). Family scores: Q 0.935 (very high — pct_roe 0.962), V 0.219 (low — pct_ep 0.454, pct_fcfp 0.385, both below median; **pct_leverage 0.085**, i.e., in the bottom ~9% of the index on leverage, consistent with the debt-funded acquisition history discussed below), M 0.142 (weak recent momentum), S 0.138 (weak earnings-surprise score).
- **The Quality score is genuine and durable**: 44.7% trailing ROE and the mid-single-digit-plus organic growth are recurring, commission-based economics, confirmed every quarter in the primary-source releases (§4–5), not a one-off.
- **The low Value score is real, not an artefact**: AON trades at 14.8x adjusted NTM P/E and only a ~4.4% TTM FCF yield on EV (this dossier's own calculation, §7) — not "cheap" on an absolute basis; the triage's "44.7% ROE at only 14–15x" framing is a reasonable characterization of quality-at-a-fair-price, not of statistical cheapness.
- **The bottom-decile leverage percentile is the one place the model and this diligence agree most strongly**: AON already carries ~$15.0bn of consolidated debt against ~$9.7bn of equity, and is about to add a fully debt-financed $17bn acquisition — this is a real, structural characteristic of AON's serial-acquirer strategy (NFP in 2024, now USI), not a data error.

## 4. Last 8 quarters (GAAP; sourced to 10-Q/10-K XBRL and Ex-99.1 releases, §12)
| Quarter | Revenue ($M) | YoY growth | Operating margin (GAAP/adj.) | GAAP diluted EPS | Adj. EPS (non-GAAP) |
|---|---|---|---|---|---|
| Q3 2024 | 3,721 | — | 16.7%/n/a | $1.57 | — |
| Q4 2024 | 4,147 | — | 26.3%/33.3% | $3.28 | $4.42 |
| **FY2024** | **15,698** | — | 24.4%/31.5% | $12.49 | $15.60 |
| Q1 2025 | 4,729 | +14%* | 30.9%/38.4% | $4.43 | $5.67 |
| Q2 2025 | 4,155 | +11%* | 20.7%/28.2% | $2.66 | $3.49 |
| Q3 2025 | 3,997 | +7%* | — | $2.11 | — |
| Q4 2025 | 4,300 | +4% | 28.1%/35.5% | $7.82 | $4.85 |
| **FY2025** | **17,181** | **+9%** | **25.3%/32.4%** | **$17.02** | **$17.07** |
| Q1 2026 | 5,034 | +6% | 34.1%/39.1% | $5.63 | $6.48 |
| **Q2 2026** | **4,246** | **+2%** | **21.5%/28.9%** | **$2.58** | **$3.81** |

\*Growth figures marked with an asterisk are this dossier's own YoY calculation from the underlying XBRL quarterly series (companyfacts), not separately cross-checked against the original 2025 press-release text this pass. **Q2 2026 organic revenue growth was +5%** despite only +2% reported growth — the 3-point gap is a **4% unfavorable divestiture drag** (mainly the sales of the NFP Wealth business and Stroz Friedberg) partly offset by +1% FX, per the company's own reconciliation table. Segment detail, Q2 2026: Commercial Risk Solutions +5% organic (EMEA/North America net new business, double-digit construction growth), Reinsurance Solutions +5% organic, Health Solutions +5% organic, **Wealth Solutions −18% reported / +5% organic** (the −24% "acquisitions/divestitures" column is almost entirely the NFP Wealth/Stroz sales) — the headline segment decline is a portfolio-reshaping artefact, not an organic deceleration.

## 5. Guidance track record (last three releases — AON gives a qualitative full-year framework, not point EPS guidance, reaffirmed or changed each time)
| Release date | Guidance given | vs. prior guidance | Result |
|---|---|---|---|
| 2026-01-30 (Q4/FY25 release) | **Introduces** 2026 guidance: mid-single-digit-or-greater organic revenue growth, 70–80bps adjusted-margin expansion, strong adjusted EPS growth, double-digit FCF growth | — (initial) | — |
| 2026-05-01 (Q1'26 release) | **Reaffirms** the identical framework | No change | Consistent |
| 2026-07-29 (Q2'26 release) | **Reaffirms** the identical framework | No change | Consistent |

**Unlike PNR, AON has not cut or materially changed its full-year framework in three consecutive quarters** — a genuine positive signal on forecast discipline. The one item worth flagging for the next review: **H1 2026 free cash flow grew only +4% YoY** ($846M vs $816M), a sharp deceleration from FY2025's +14% (full year) / Q4 2025's +16% (quarter), attributed by the company to "NFP Wealth [divestiture] and impact of working capital" (Q2 2026 release) rather than to a change in the underlying double-digit FCF growth guidance — plausible, but not yet independently verified beyond the company's own one-line explanation; flagged as a **data conflict watch-item**, not a confirmed problem.

## 6. Earnings quality & balance sheet
**Entity scope: consolidated Aon plc, per the 10-Q's Condensed Consolidated Statement of Financial Position and Debt note (filed 2026-07-29, period 2026-06-30).**
- **FCF conversion:** FY2025 FCF $3,218M vs. GAAP net income attributable to Aon shareholders of $3,650M (approx., per FY2025 EPS × diluted shares) — a reasonably strong conversion; H1 2026 FCF $846M vs H1 2026 net income ~$1,763M reflects normal H1 seasonality (Aon's Q1 is seasonally its strongest cash quarter for commission timing) plus the divestiture/working-capital drag noted above.
- **SBC:** not separately quantified this pass from the H1 2026 cash-flow statement — flagged as a gap; Aon's compensation-and-benefits line ($2,271M in Q2 2026, down 4% YoY on lower incentive accruals) is the relevant expense category but SBC alone was not isolated.
- **GAAP vs. adjusted gap:** Q2 2026 GAAP EPS $2.58 vs adjusted $3.81 (a 32% gap) — driven mainly by amortization of intangibles ($174M in Q2 2026, down from $201M) and the "Accelerating Aon United" restructuring program ($96M in Q2 2026) per the company's own reconciliation; this is a normal, recurring gap for a serial acquirer and is consistently labeled in every release reviewed.
- **Balance sheet (2026-06-30 vs 2025-12-31):** cash $1,062M (down from $1,195M) + short-term investments $205M (down sharply from $1,603M — a large planned reduction, consistent with debt paydown and buybacks); total debt (current + long-term) **$14,967M** (down from $15,249M) — **$2,020M of this is now current**, including three senior-note tranches (2.850% due May 2027, 5.125% due March 2027, 8.205% Junior Subordinated due January 2027, aggregate ~$1.72bn) reclassified to current as their maturities fell inside 12 months, which the company says it will repay from operating cash flow and cash on hand (i.e., not a distress signal, a normal maturity-ladder mechanic). Total equity $9,686M (up from $9,459M). **Net debt (excluding fiduciary assets/liabilities) ≈ $13,700M**; using this dossier's own TTM EBITDA estimate (~$5.9bn, cross-checked against `d4_live_snapshot`'s y_ebitda), **net debt/EBITDA ≈ 2.3x today**.
- **Pending M&A and its financing — the dominant forward-looking item:** on 2026-08-30 (after the Q2 10-Q, so not yet on the balance sheet above), Aon signed a definitive agreement to acquire **USI (from KKR and other shareholders) for $17.0 billion** ($16.7bn net of ~$278M of tax attributes; ~14.5x trailing synergized adjusted EBITDA), expected to close **Q4 2026**, to be funded entirely with **new debt across a range of maturities**. Aon states it expects to maintain its current Baa2/A− ratings and explicitly says **it does not expect to repurchase shares in the near term**, prioritizing debt repayment instead. This dossier's own pro forma estimate (purchase price ÷ disclosed multiple ⇒ USI EBITDA ≈ $1.15bn; combining with Aon's own ~$5.9bn TTM EBITDA and the announced $395M run-rate synergy target, before phase-in) implies **day-one pro forma net debt/EBITDA in the low-4x range**, versus 2.3x today — a real, material leverage step-up not yet reflected in the Q2 2026 balance sheet reviewed above.
- **Capital return:** $775M returned to shareholders in Q2 2026 ($600M buybacks + $175M dividends), already exceeding the full-year "at least $1 billion" buyback objective as of Q2 — but per the USI announcement, this pace is expected to slow sharply once the deal closes.

## 7. Valuation snapshot and reverse DCF (no V1 row exists for AON — this dossier's own build)
At the 2026-09-25 close of $277.99 (market cap ≈ $58.97bn; EV ≈ **$73.45bn**, `d4_live_snapshot`, consistent with this dossier's own net-debt figure), trailing GAAP P/E ≈13.7x, adjusted NTM P/E ≈14.8x. TTM FCF (this dossier's own build: FY2025 FCF $3,218M − H1 2025 FCF $816M + H1 2026 FCF $846M) ≈ **$3,248M**, a 4.4% EV/FCF yield.
**Reverse DCF (two-stage, 10-year explicit FCF growth at rate g + Gordon-growth terminal value at 3.0%, WACC sensitivity shown):** at WACC 8.0%, implied g ≈ **+4.2%/year**; at WACC 7.5%, implied g ≈ +2.9%; at WACC 8.5%, implied g ≈ +5.4%. **This dossier's base case is that AON can plausibly compound FCF at a high-single-digit to low-double-digit rate over 10 years** (mid-single-digit organic growth + margin expansion + bolt-on/large M&A, consistent with FY2025's 14% delivered FCF growth and the reaffirmed "double-digit FCF growth" guidance), i.e., **implied growth is below this dossier's base case ("below")** — a reasonably attractive entry point for the quality on offer, though the USI-driven leverage step-up and the H1 2026 FCF deceleration are real reasons for caution on the pace of that compounding over the next 1–2 years specifically (hence INCLUDE-SMALL, not INCLUDE).

## 8. Bull case and bear case
**Bull (3 points):**
1. Full-year guidance framework reaffirmed unchanged for three consecutive quarters (Jan/May/Jul 2026) — genuine forecast discipline, unlike several peers in this diligence batch.
2. Reverse DCF implies the market is pricing in only ~4% 10-year FCF growth against FY2025's delivered 14% FCF growth and a reaffirmed double-digit FCF-growth guide — a real gap between price and demonstrated execution.
3. USI (like NFP before it) extends Aon's already-strong position in the large, growing US middle-market segment, with disclosed $395M of run-rate synergies expected — a credible, not speculative, growth lever if integration goes to plan.

**Bear (3 points):**
1. The $17.0bn USI acquisition is entirely debt-financed; this dossier's own pro forma estimate puts net debt/EBITDA in the low-4x range at close (from 2.3x today), with buybacks explicitly paused near-term — a real, dated deterioration in balance-sheet flexibility and capital return, not yet reflected in Q2 2026 reported figures.
2. H1 2026 free cash flow grew only +4% YoY (vs. 14–16% in FY2025), attributed by the company to divestiture/working-capital effects but not yet independently verified beyond that one-line explanation — worth confirming does not represent a genuine deceleration before USI integration adds complexity.
3. AON already carries bottom-decile leverage on the model's own sector-relative measure (pct_leverage 0.085) even before USI; a fully debt-funded $17bn deal on top of that is a large bet that synergies and deleveraging execute on schedule (Q4 2026 close, multi-year synergy ramp).

## 9. Key risks & kill criteria (measurable) — what would break this thesis
1. **USI acquisition fails to close** (regulatory or other block) or closes with materially worse financing terms (e.g., a ratings downgrade below Baa2/A−) than disclosed on 2026-08-30.
2. **Pro forma net debt/EBITDA (consolidated, post-USI close) exceeds 4.5x** without a credible, dated deleveraging path disclosed within two quarters of close.
3. **Organic revenue growth falls below the "mid-single-digit or greater" guided floor for two consecutive quarters** (i.e., a guidance cut, not just a reaffirmation) — would break the "consistent execution" thesis this INCLUDE-SMALL relies on.
4. **H2 2026 free cash flow growth (H2 2026 vs H2 2025) remains below +10% YoY**, confirming the H1 2026 deceleration is structural rather than a one-off working-capital/divestiture timing effect.
5. **Share buybacks are not resumed within 12 months of the USI close**, signaling the leverage/deleveraging path is slower than management's own framing suggests.

## 10. Catalysts & calendar
- **Q3 2026 earnings: 2026-10-30** (`d4_live_snapshot` next_earnings_date).
- **USI acquisition expected to close Q4 2026** — watch for the permanent-debt financing terms (the "range of maturities" is not yet priced/disclosed) and the first pro forma balance sheet.
- Ongoing integration of the 2024 NFP acquisition and the 2025–26 NFP Wealth/Stroz Friedberg divestitures (portfolio-reshaping still in progress).

## 11. Red-flag scan
- **Litigation:** the 2021 DOJ suit to block Aon's proposed acquisition of Willis Towers Watson (abandoned in 2021) is historical, not current, and not relevant to the pending USI deal (a different, smaller target with a different competitive overlap — USI is the 10th-largest US broker, not a "Big Three" peer); no current DOJ/antitrust action against the USI deal was identified in this pass (searched 2026-09-26), though the deal is recent (announced 2026-08-30) and regulatory review is still pending per the company's own closing-conditions language.
- **Auditor/material weakness/going concern:** none identified in the filings reviewed this pass.
- **Insider selling / short-seller reports:** not independently pulled this pass — flagged as a gap.
- **Other litigation:** none material identified beyond routine E&O/professional-liability matters typical of the brokerage industry, not separately quantified this pass.

## 12. Sources (numbered, all retrieved 2026-09-26 unless noted)
1. Aon plc 10-Q, period 2026-06-30, filed 2026-07-29 (SEC EDGAR accession 0001628280-26-050610) — balance sheet, debt note.
2. Aon plc Q2 2026 earnings press release (Ex-99.1 to 8-K filed 2026-07-29, accession 0001628280-26-050367).
3. Aon plc Q1 2026 earnings press release (Ex-99.1 to 8-K filed 2026-05-01, accession 0001628280-26-029093).
4. Aon plc Q4/FY2025 earnings press release (Ex-99.1 to 8-K filed 2026-01-30, accession 0001628280-26-004273).
5. Aon plc 8-K announcing the USI acquisition agreement (filed 2026-08-31, dated 2026-08-30, accession 0001193125-26-375328), Ex-99.1 press release.
6. SEC XBRL companyfacts, CIK 0000315293 (`data.sec.gov/api/xbrl/companyfacts/CIK0000315293.json`) — current through the Q2 2026 10-Q; quarterly revenue/operating income/net income/EPS series.
7. `v4/data/b1_live_scores.csv`, `v4/data/d4_live_snapshot.parquet` (as of 2026-09-25) — quant composite/factor context, EV, EBITDA, next-earnings-date.
8. `v4/outputs/Q05_triage.json` (agent Q05, triage note for AON) and `v4/outputs/v1_valuation_table.csv` (confirmed: no AON row).

## 13. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (quarter ended 2026-06-30), per the 10-Q filed 2026-07-29, plus the 8-K announcing the USI acquisition (filed 2026-08-31, dated 2026-08-30) as a subsequent, not-yet-closed event. Events checked to 2026-09-25 close. All figures are GAAP/consolidated (Aon plc parent, excluding fiduciary pass-through assets/liabilities from net-debt) unless explicitly labeled "adjusted" (the company's own non-GAAP reconciliation). This is research for an internal, multi-agent process — not personal investment advice.
