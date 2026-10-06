# O — Realty Income Corporation (NYSE: O)

## 1. Verdict
**INCLUDE-SMALL** (half weight) — 24–36 month horizon. Reservation: 5.4x net debt/EBITDAre and continued equity/ATM issuance make the compounding story sensitive to a sustained rise in long rates; the "monthly dividend" quality premium is real but leaves little room for multiple expansion.

## 2. Business in plain English
Realty Income is the largest net-lease REIT in the US, owning ~15,588 freestanding retail, industrial and (increasingly) data-center/gaming properties leased to ~1,798 clients across 92 industries on long-term, triple-net leases (tenant pays taxes/insurance/maintenance). It makes money on the spread between its cost of capital (debt + equity) and the cap rate at which it buys real estate, plus contractual rent escalators. Competitive position: investment-grade balance sheet (Fitch reaffirmed "A" in Aug 2026), scale that gives it access to off-market sale-leasebacks other REITs can't source. (Source: EX-99.1 to 8-K filed 2026-08-05, accession 0000726728-26-000044.)

## 3. Why the model likes it / is it durable?
Triage flagged quality=4, growth=2 (b1_live_scores.csv: pct_gp_a 0.75, pct_bp 0.88, low volatility tercile 1). The quality signal (profitability/leverage) is durable — it reflects genuinely investment-grade credit metrics and a 30-year unbroken dividend-growth streak, not an accounting artefact. The growth signal is low because AFFO/share growth is structurally ~4%/yr, not because of any deterioration.

## 4. Last two quarters (10-Q/8-K, GAAP unless noted)
| Metric | Q2'26 (3mo to 6/30/26) | Q2'25 | Q1'26 (per Q1 release) | Q1'25 |
|---|---|---|---|---|
| Total revenue | $1,547.7m | $1,410.4m | (H1 $3,096.4m total, so Q1≈$1,548.7m) | — |
| Net income avail. to common | $344.0m | $196.9m | H1 $655.7m ⇒ Q1≈$311.7m | — |
| EPS (diluted, GAAP) | $0.37 | $0.22 | H1 $0.70 ⇒ Q1≈$0.33 | — |
| FFO/share | $1.07 | $1.06 | H1 $2.14 ⇒ Q1≈$1.07 | — |
| AFFO/share | $1.09 | $1.05 | H1 $2.22 ⇒ Q1≈$1.13 | — |
| Net debt / Annualized Pro Forma Adj. EBITDAre | 5.4x | — | — | — |
Source: Exhibit 99.1 to 8-K, filed 2026-08-05, accession 0000726728-26-000044 ("Select Financial Results" and "Net Debt" tables). Q1 figures are back-solved from the H1-vs-H1 table in the same release; I did not independently pull the Q1 8-K, so treat the Q1 column as a derived cross-check, not a primary cite.

AFFO/share growth of 3.8% YoY in Q2 continues a multi-year pattern of low-single-digit-to-mid-single-digit growth; no acceleration or deceleration visible in the two quarters shown.

## 5. Guidance track record
Q2'26 release (filed 2026-08-05): **"we are pleased to raise our 2026 AFFO per share guidance to $4.44 - $4.45, reflecting approximately 4% growth rate at the midpoint."** — quoted verbatim from CEO Sumit Roy's comments, EX-99.1, 8-K accession 0000726728-26-000044. The same release's guidance table shows: "Revised 2026 Guidance … AFFO per share $4.44 - $4.45 … Prior 2026 Guidance (1) … AFFO per share $4.41 - $4.44." **Verdict: raised** (bottom and top of range both moved up $0.01–$0.03).
Net income per share guidance was cut in the same table: "Net income per share (2) $1.59 - $1.60 [Revised] … $1.60 - $1.63 [Prior]" — the GAAP EPS range was narrowed and its midpoint trimmed slightly, driven by real-estate-depreciation and "other adjustments" moving up. I could not locate the prior-quarter (Q1) guidance release in this pass to confirm the Q1→Q2 direction independently; treat "raised" as applying to AFFO/share specifically, not to every line.
Same-store rent growth guide: "1.1% - 1.3%" (revised) vs "1.0% - 1.3%" (prior) — raised at the low end.

## 6. Earnings quality & balance sheet
- FFO vs AFFO gap is standard REIT add-back (depreciation); GAAP EPS ($0.37 Q2) is not the right lens for a REIT — AFFO ($1.09) is.
- Dividend: "$0.812 in the three months ended June 30, 2026, as compared to $0.806" in Q2'25, representing "74.5% of our diluted AFFO per share" — payout ratio in the mid-70s, leaving room for growth-funded reinvestment.
- Leverage: Net Debt $30.44bn; Net Debt/Annualized Pro Forma Adj. EBITDAre 5.4x (5.2x including unsettled ATM forward equity proceeds) — moderate for an "A"-rated net-lease REIT, but a rate shock that widens spreads would raise the cost of the external-growth model this REIT depends on.
- Post-quarter financing: "In July 2026, issued €600.0 million of 3.625% senior unsecured notes due July 2032" — locking in a euro-denominated funding leg, consistent with historical multi-currency issuance to lower blended cost of debt.
- Deal pipeline: CEO cites a "$6 billion hyperscale data center joint venture" and the "Realty Income Investment Management platform" (third-party capital) as complementary growth channels beyond the core net-lease book — a diversification that is not yet proven at scale and adds execution/counterparty risk not present in the legacy triple-net model.
All figures above are consolidated-entity, GAAP or AFFO as labelled; no segment/subsidiary-only figures were used. Source: 8-K EX-99.1 filed 2026-08-05.

## 7. Valuation snapshot & reverse DCF
- Price used: $55.54 (2026-09-25 close, per v4/data b1_live_scores.csv).
- P/AFFO (FY26 guide midpoint $4.445) ≈ **12.5x** → AFFO yield ≈ 8.0%. GAAP P/E (FY26 guide midpoint $1.595) ≈ 34.8x — this is the number that looks "expensive" and is the wrong lens for a REIT; it is inflated purely by real-estate depreciation, which the AFFO measure adds back.
- **v1_valuation_table.csv / v1_valuation.json have no row for O** (v1 does not model this ticker — its `companies["O"]` entry is `null`). v1_verdict = null; there is nothing to reconcile against.
- Reverse DCF (Gordon growth on AFFO, since O is best modeled as a growing perpetuity of AFFO): P/AFFO = 1/(r-g). At an assumed cost of equity r = 8.0%–8.5% (mid-range for an investment-grade net-lease REIT, roughly dividend yield + a small equity-risk premium), the 12.5x multiple implies a perpetual AFFO/share growth rate g of **0% to +0.5%/yr**. That is well **below** management's own guided ~4% AFFO/share growth for 2026 and below O's realized 5-year AFFO/share CAGR (mid-single digits). **implied_vs_base = "below"** — the market is pricing in materially less growth than the company is currently delivering, which is why the position clears the INCLUDE-SMALL bar despite the headline 34.8x GAAP P/E.
- Peers (net-lease/retail REITs, e.g. NNN, WPC, ADC) trade in a similar 12–15x P/AFFO band; O is not an outlier.

## 8. Bull case
1. Investment-grade ("A") diversified net-lease REIT with a 30-year dividend-growth streak; AFFO/share guidance was just raised, not cut.
2. Reverse-DCF implied growth (~0%) is below the ~4% AFFO/share growth actually being delivered — the "safety" premium leaves upside if execution continues.
3. New growth channels (data-center JV, third-party asset management) diversify beyond saturated US retail net-lease without (yet) requiring O to lever up further.

## 9. Bear case / kill criteria (measurable)
1. **Net Debt/Annualized Pro Forma Adjusted EBITDAre rises above 6.0x** for two consecutive quarters (was 5.4x in Q2'26; source: 8-K EX-99.1, 2026-08-05).
2. **AFFO/share guidance is cut** from the current $4.44–$4.45 FY26 range in the next release (would reverse the "raised" trend).
3. **Same-store rent growth falls below 1.0%** for two consecutive quarters (current guide: 1.1%–1.3%; source as above).
4. **Occupancy drops below 97.5%** vs. the "Approx 98.5%" FY26 guide (source: 8-K EX-99.1 guidance table).
5. A rent-recapture rate on re-leased space below 90% for two consecutive quarters (was 102.7% in Q2'26) — would signal the tenant-quality/pricing-power thesis is breaking.

## 10. Catalysts & calendar
- Next earnings: Q3 2026 results — **estimated early November 2026** based on prior-year cadence (O reported Q3'25 in early Nov 2025); not yet confirmed by an official company calendar entry I could verify in this pass.
- Watch: further hyperscale data-center JV announcements/scaling; any additional euro or dollar unsecured note issuance (funding cost trend); Fed rate path (net-lease multiples are rate-sensitive).

## 11. Red-flag scan
- No auditor change, material weakness, restatement, or going-concern language found in the reviewed 8-K/10-Q. No SEC/DOJ investigation of Realty Income itself found in this pass.
- Sector-level risk (not company-specific litigation): general 2026–2028 tenant-credit-migration risk in weak pharmacy/apparel/casual-dining categories is cited in market commentary; O discloses ~34.3% of portfolio ABR is with investment-grade tenants/affiliates as of 6/30/26 (per 10-Q, accession 0000726728-26-000048 — cited via secondary summary, not independently re-verified line-by-line in this pass; flag as a data point to re-check before initiating).
- No new short-seller report identified.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (three/six months ended 2026-06-30), per 8-K filed 2026-08-05 (accession 0000726728-26-000044) and 10-Q filed 2026-08-06 (accession 0000726728-26-000048, not fully re-opened line-by-line this pass). Events checked to 2026-09-25 close via WebSearch for tenant-credit and litigation news; no company-specific red flag found. All dollar figures are GAAP or AFFO/FFO as explicitly labelled; no adjusted number is presented without its label. **Research only — not personal investment advice.**

## Sources
1. Realty Income 8-K, Exhibit 99.1, "Operating Results for the Three and Six Months Ended June 30, 2026," filed 2026-08-05, accession 0000726728-26-000044. https://www.sec.gov/Archives/edgar/data/726728/000072672826000044/o-991q22026.htm
2. Realty Income 10-Q for period ended 2026-06-30, filed 2026-08-06, accession 0000726728-26-000048. https://www.sec.gov/Archives/edgar/data/726728/000072672826000048/o-20260630.htm
3. SEC EDGAR filing index, Realty Income CIK 0000726728. https://data.sec.gov/submissions/CIK0000726728.json
4. v4/data/b1_live_scores.csv (price, quant factor scores, as_of 2026-09-25).
5. WebSearch, "Realty Income tenant bankruptcy 2026 credit watch," retrieved 2026-09-27 (market-commentary summaries, secondary source, used only for context).
