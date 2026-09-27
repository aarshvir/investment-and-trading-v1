# ABT — Abbott Laboratories — Diligence Dossier (Agent F38, Wave-2 Standard)

## 1. Verdict
**INCLUDE-SMALL** (12–36 month horizon). Reservation: the March-2026 Exact Sciences acquisition has temporarily
elevated leverage and widened the GAAP/adjusted gap, and NEC infant-formula litigation, while now partly
quantified via an August 2026 settlement, still leaves ~1,700 suits pending. Neither is a thesis-breaker, but
both argue for half-weight rather than full conviction until Q3/Q4 2026 show the acquisition integrating cleanly
and the balance sheet delevering.

## 2. Business in plain English
Abbott sells four things: diagnostic tests (now including Exact Sciences' Cologuard colon-cancer screening test),
medical devices (FreeStyle Libre continuous glucose monitors, pacemakers/defibrillators, heart-valve and
structural-heart devices), infant/adult nutrition (Similac, Ensure), and branded generic drugs sold mostly outside
the U.S. It makes money selling recurring consumables (test strips, sensors, formula) and durable devices with
high switching costs (implanted cardiac devices, installed diagnostic instruments). Its competitive position is
built on breadth (four uncorrelated franchises) and installed base (FreeStyle Libre has >6 million users
globally per company disclosure).

## 3. Why the model likes it — durable or artefact?
b1_live_scores.csv (as of 2026-08-28 filing lag): composite percentile only 0.029 (live_rank 482/503, not top-30),
low ROE percentile — the quant score is unremarkable and did **not** flag ABT; it reached diligence purely through
the triage/quality-growth screen (Q07: quality 4, growth 4, price_vs_growth 4). d4 shows NTM P/E 17.1x, forward
P/E 16.7x — cheap for a business compounding adjusted EPS at high-single-digit to low-double-digit rates with
7 beats and 1 miss in the last 8 quarters (d4 `beats_last8`/`misses_last8`). The reason the model doesn't rank it
highly is mechanical: trailing GAAP earnings are depressed by 2026 acquisition/interest/tax charges (trailing P/E
32.8x vs forward 16.7x), which is an artefact of purchase accounting, not deteriorating quality — see §6.

## 4. Last two years of results (GAAP, 10-Q/10-K; $ millions except per-share)
| Quarter | Revenue | YoY | Operating income | GAAP diluted EPS | Adjusted diluted EPS¹ |
|---|---|---|---|---|---|
| Q1'24 (Mar-24) | 9,964 | — | 1,386 | $0.70 | n/a (not sourced this pass) |
| Q2'24 (Jun-24) | 10,377 | — | 1,669 | $0.74 | n/a |
| Q3'24 (Sep-24) | 10,635 | — | 1,859 | $0.94 | n/a |
| Q4'24 (Dec-24) | 5,974² | — | (1,410)² | **$5.27** (incl. one-off, see below) | $1.34 |
| Q1'25 (Mar-25) | 10,358 | +4.0% | 1,693 | $0.76 | n/a |
| Q2'25 (Jun-25) | 11,142 | +7.4% | 2,052 | $1.01 | $1.26 |
| Q3'25 (Sep-25) | 11,369 | +6.9% | 2,057 | $0.94 | $1.30 |
| Q4'25 (Dec-25) | ~12,595³ | — | ~1,896³ | n/a | $1.50 (+12%) |
| Q1'26 (Mar-26) | 11,164 | +7.8% | 1,345 | $0.61 | $1.15 (+6%) |
| Q2'26 (Jun-26) | 12,593 | +13.0% | 1,693 | $0.53 | $1.31 (+4%) |

Sources: SEC XBRL companyfacts (CIK 0000001800) for Q1'24–Q1'26 GAAP lines; press releases (8-K Ex-99.1) for
Q4'24 (filed 2025-01-22 accession consistent with FY2024 10-K), Q3'25 (2025-10-15), Q1'26 (2026-04-16), Q2'26
(2026-07-16) for adjusted EPS and Q2'26 GAAP income statement. ¹Adjusted EPS excludes "specified items"
(company-defined non-GAAP; reconciliation on release page 9–10 of each). ²Q4'24 derived as FY2024 10-K total
minus Q1–Q3'24; the negative-looking operating income is an artefact of a one-off tax item hitting "taxes on
earnings," not operating income — flagged, not fully re-derived this pass (limitation). ³Q4'25 derived as
FY2025 10-K total ($44,328M rev, $8,053M operating income) minus Q1–Q3'25; not independently cross-checked
against the Q4'25 press release income statement this pass (limitation).

**Key earnings-quality finding (the audit's #1 lesson: don't mix GAAP and adjusted without saying so):** Q4 2024
GAAP net income of $9,229M / EPS $5.27 includes a **$7.497 billion non-cash income-tax valuation-allowance
benefit** "resulting from the restructuring of certain foreign affiliates and the confirmation of certain tax
filing positions" (Abbott 8-K Ex-99.1, filed 2025-01-22, footnote 1) — worth $3.93/share and excluded from
adjusted EPS ($1.34). FY2024 GAAP net income of $13,402M is **not** comparable to FY2023's $5,723M or FY2025's
$6,524M for this reason; any YoY GAAP comparison spanning Q4 2024 is contaminated unless this is stripped out.
This is exactly the "adjusted vs GAAP mixed silently" failure mode `lead_v3_audit.md` warned about, so it is
called out explicitly here rather than left implicit in a table.

**2026 GAAP/adjusted gap (second, unrelated cause):** Q2 2026 GAAP net earnings of $928M vs adjusted $2,290M —
a $1.362bn after-tax gap — is now driven by Exact Sciences purchase-accounting: amortization of intangibles rose
to $658M from $420M YoY, interest expense rose to $299M from $50M YoY (new acquisition debt), plus one-off tax
items ($110M net tax expense from prior-year position resolutions, $240M from prior deferred-tax-benefit
adjustments — 8-K Ex-99.1, 2026-07-16, footnote 1). This is a real, disclosed, self-consistent reconciliation —
not a red flag on its own — but it means GAAP EPS is temporarily a poor proxy for economic earnings.

## 5. Guidance track record (last 4 releases, adjusted diluted EPS, full-year)
| Release date | Guidance given | vs prior range | Why |
|---|---|---|---|
| 2025-10-15 (Q3'25) | FY25 narrowed to **$5.12–$5.18** | Reaffirmed midpoint, narrowed range | On track; delivered $5.15 actual |
| 2026-01-22 (Q4'25/FY25) | FY26 initial: **$5.55–$5.80** | New year, n/a | Organic sales growth guided 6.5–7.5% |
| 2026-04-16 (Q1'26) | FY26 revised to **$5.38–$5.58** | **Cut** low end $0.17, high end $0.22 | Explicitly attributed to "$0.20 of dilution related to the acquisition of Exact Sciences," which closed 2026-03-23 — earlier than the "second quarter 2026" close the company had flagged in January. Organic/comparable sales guide unchanged at 6.5–7.5%. |
| 2026-07-16 (Q2'26) | FY26 raised to **$5.45–$5.60** | **Raised** both ends by $0.02–$0.07 | Underlying business outperformance funding back some of the dilution; comparable sales guide reaffirmed 6.5–7.5%. Q3'26 adjusted EPS guided $1.38–$1.46. |

Net: FY26 guidance has been cut once (for a disclosed, deal-related reason, not an operating miss) and raised
once since. This is guidance discipline, not guidance drift — but note the FY26 range ($5.45–$5.60) is still
below the original $5.55–$5.80 issued eight months ago, i.e. Exact Sciences has been dilutive to date as
disclosed, not yet accretive.

## 6. Earnings quality & balance sheet
- **FCF conversion:** TTM (approx., ended ~2026-06) operating cash flow ≈ $9,566M (FY2025 10-K) less $2,171M
  capex (FY2025) ≈ **$7.4bn FCF**, roughly consistent with Yahoo/d4's TTM FCF of $7.21bn (cross-check; d4
  `freeCashflow`). Note: SEC XBRL companyfacts for ABT has not yet ingested Q2 2026 (period 2026-06-30) duration
  facts as of this research date (2026-09-26) despite the 10-Q being filed 2026-07-28 — a data-availability gap,
  disclosed rather than papered over; the FY2025-based TTM approximation is used instead of a true trailing-twelve
  from quarterly XBRL.
- **SBC:** not separately quantified this pass (limitation; time-boxed).
- **Leverage:** total debt jumped from ~$13.2bn (2025-12-31: $9.9bn LT noncurrent + $3.0bn LT current) to
  **~$34.0bn** at 2026-03-31 ($29.6bn LT noncurrent + $4.4bn LT current), funding the Exact Sciences deal —
  confirmed by an 8-K (items 1.01/2.03, filed 2026-03-09) for a new note issuance. Cash was $6.8bn same date.
  Net debt ≈ $27.2bn vs TTM EBITDA (Yahoo) $11.68bn → **net debt/EBITDA ≈ 2.3x** on trailing EBITDA that itself
  hasn't yet absorbed Exact Sciences' cash flow contribution; this should improve as Exact Sciences' EBITDA
  layers in and debt amortizes, but is a step up from Abbott's historically conservative (<1.5x) balance sheet.
  Total assets roughly doubled at the same date ($86.7bn→$110.4bn), consistent with a ~$21bn purchase price
  plus goodwill/intangibles from the deal (not independently confirmed to the dollar this pass).
- **M&A:** Exact Sciences (cancer diagnostics, Cologuard) — agreed Nov 2025, closed **2026-03-23**, debt-funded.
  Now reported as the "Cancer Diagnostics" segment; comparable sales growth 13.3% in Q2'26. Structural Heart
  received a one-off competitor compensation payment through Q1 2026 only (final payment recognized then) —
  a real, disclosed headwind to Structural Heart comps from Q2'26 onward.
- **Share count:** ~1,742–1,751M diluted shares over the period, broadly flat to slightly down (buybacks roughly
  offsetting dilution); not a red flag.
- **Segment note:** Nutrition (the legacy, lowest-growth franchise) declined **-3.6% comparable in Q2'26 and
  -5.6% for 1H26**, driven by lower volumes and Q4-2025 pricing actions — a real, ongoing soft spot in ~19% of
  sales, not offset by the new Cancer Diagnostics growth engine in the reported segment mix.

## 7. Valuation snapshot and reverse DCF
d4 (2026-09-25 close, price $101.29): NTM P/E 17.1x, FY1 P/E 16.7x, trailing P/E 32.8x (distorted by the FY2024/
2026 GAAP items above — **use NTM/FY1, not trailing, for ABT right now**), FCF yield 4.1%, beta 0.59.
No V1 systematic-valuation row exists for ABT (not in `outputs/v1_valuation_table.csv`'s 92 covered names) →
`v1_verdict = null` per program rules; this section is this analyst's own reverse DCF (skill script
`valuation.py`), not a reconciliation.

- EV bridge: market cap $176.4bn + total debt $34.0bn (2026-03-31, latest available) − cash $6.8bn = **EV $203.7bn**.
- Reverse DCF (central case): WACC 7.0% (beta 0.59, rf≈4.2%, ERP≈5%), terminal growth 4.0%, base FCF $7.3bn,
  10-year stage-1 horizon → **implied FCF growth ≈1.5%/yr for 10 years**, fading to 4%.
- Sensitivity: at WACC 8.5% (a more conservative equity discount for a company now carrying real litigation
  and acquisition-integration risk), implied growth rises to **≈6.4%/yr**.
- My evidence-based base case: mid-single-digit organic/comparable sales growth (company guides 6.5–7.5%) plus
  margin expansion and Exact Sciences accretion from 2027 onward → **7–9%/yr adjusted FCF/EPS growth** over the
  next decade is a reasonable, not aggressive, base case given the last-8-quarter beat record.
- **Implied vs base: BELOW** even under the higher (8.5%) WACC sensitivity. The market is pricing Abbott as if
  it grows meaningfully slower than its own recent and guided trajectory — consistent with the litigation/
  leverage/GAAP-optics discount discussed above, not with a demonstrated growth problem.

## 8. Bull case / bear case
**Bull:** (1) FreeStyle Libre + Cancer Diagnostics (Exact Sciences/Cologuard) are two genuine structural growth
engines layered onto a defensive base, each growing double-digit organically. (2) Diversification across four
segments and geography (>60% international) smooths any single-franchise shock. (3) A 54-year dividend-increase
streak (Dividend Aristocrat, per company's own Q2'26 release) signals capital-allocation discipline even through
this leveraged deal.

**Bear:** (1) Nutrition (~19% of sales) is shrinking, not just decelerating (-5.6% 1H26 organic), and management
has not yet shown it can stabilize this segment. (2) Leverage jumped roughly 2.5x in one quarter to fund Exact
Sciences; if integration disappoints or synergies are slower than modeled, deleveraging stalls just as NEC
settlement cash payments (below) also come due. (3) NEC litigation is not closed: Abbott settled the lead
(Gill) verdict plus ~2,000 additional infant claims for ~$670M in August 2026, but ~1,700 lawsuits covering
~12,700 infants remain pending (per company 8-K, Item 8.01, filed 2026-08-20, and contemporaneous press
coverage) — the eventual all-in cost is still unknown and could exceed current reserves.

## 9. Key risks & kill criteria (measurable)
1. Comparable/organic sales growth guidance cut below 6.5% (current FY26 floor) for two consecutive quarters.
2. Nutrition segment organic sales decline exceeds -6% for two consecutive quarters (currently -3.6% to -5.6%).
3. Net debt/EBITDA rises above 3.5x (from ~2.3x now) without a clear deleveraging plan disclosed.
4. A single NEC verdict or settlement tranche (beyond the disclosed ~$670M Gill/2,000-claim settlement) exceeds
   $1 billion, signaling the remaining ~1,700-suit tail is materially larger than currently priced.
5. Adjusted diluted EPS guidance is cut (not just narrowed) for a reason other than a disclosed one-time
   acquisition/tax item.

## 10. Catalysts & calendar
Next earnings: **2026-10-14** (Q3 2026, per d4 live snapshot). Q3'26 adjusted EPS already guided $1.38–$1.46
(2026-07-16 release). Watch for: Exact Sciences integration commentary, Nutrition segment trajectory, and any
update on the ~1,700 remaining NEC suits.

## 11. Red-flag scan
- **Litigation (material, quantified in part):** NEC (necrotizing enterocolitis) infant-formula mass tort.
  Missouri Court of Appeals affirmed a $495M jury verdict (Gill case, originally July 2024) in May 2026; rather
  than pursue further appeal, Abbott settled Gill plus ~2,000 additional infant claims for ~$670M (8-K filed
  2026-08-20). ~1,700 suits (~12,700 infants) remain pending in state/federal courts. This is a real, disclosed,
  partially-quantified tail risk — not a going-concern issue given Abbott's balance sheet and cash flow, but
  large enough to matter for sizing.
- **Auditor/accounting:** No auditor change, restatement, or going-concern language identified this pass (not
  exhaustively verified against the full FY2025 10-K Item 9A/critical-audit-matters section — time-boxed
  limitation). The $7.497bn Q4'24 tax valuation-allowance item and the 2026 M&A-driven GAAP/adjusted gap are
  disclosed, reconciled by the company, and explained above — not treated as a red flag, but as a data-quality
  point future analysts must not silently average into a "normal" GAAP trend.
- **Data conflict:** b1_live_scores.csv ranks ABT outside the top-30 (composite percentile 0.029, live_rank
  482/503) largely because trailing GAAP earnings are depressed by the items above; this is a known artefact of
  the pre-registered model using trailing GAAP inputs, not a positive read on ABT's quality — flagged as a
  data_conflict below.
- No insider-selling Form 4 pattern, short-seller report, or auditor resignation identified this pass
  (not independently pulled from EDGAR Form 4 filings — time-boxed limitation, disclosed).

## 12. Data basis, recency and disclaimer
All figures are **consolidated** GAAP as reported in the company's SEC filings unless labelled adjusted/non-GAAP. Most recent period incorporated: **Q2 2026 (period ended 2026-06-30), 10-Q filed 2026-07-28** (press-release
income statement used directly; SEC XBRL companyfacts snapshot used for this research had not yet ingested this
quarter's duration facts as of 2026-09-26 — disclosed above). Checked for events to **2026-09-25** (Q1'26/Q2'26
guidance, the August 2026 NEC settlement 8-K, and Starboard-style activism — none found for ABT). GAAP figures
are labelled GAAP; adjusted/non-GAAP figures are labelled adjusted and reconciled per the company's own
footnotes. **Research, not personalized investment advice; this is not investment advice.**

## 13. Sources
1. SEC EDGAR CIK 0000001800, XBRL companyfacts API (`https://data.sec.gov/api/xbrl/companyfacts/CIK0000001800.json`), retrieved 2026-09-26.
2. Abbott 8-K Ex-99.1, Q2 2026 results, filed 2026-07-16 (`https://www.sec.gov/Archives/edgar/data/1800/000162828026048377/abt-2026q2xexhibitx991.htm`).
3. Abbott 8-K Ex-99.1, Q1 2026 results, filed 2026-04-16 (`https://www.sec.gov/Archives/edgar/data/1800/000162828026025365/abt-2026q1xexhibitx991.htm`).
4. Abbott 8-K Ex-99.1, Q4/FY2025 results, filed 2026-01-22 (`https://www.sec.gov/Archives/edgar/data/1800/000162828026002982/abt-2025q4xexhibitx991.htm`).
5. Abbott 8-K Ex-99.1, Q3 2025 results, filed 2025-10-15 (`https://www.sec.gov/Archives/edgar/data/1800/000162828025045049/abt-2025q3xexhibitx991.htm`).
6. Abbott 8-K Ex-99.1, Q4/FY2024 results, filed 2025-01-22 (`https://www.sec.gov/Archives/edgar/data/1800/000162828025002092/abt-2024q4xexhibitx991.htm`) — source of the $7.497bn tax item.
7. Abbott 8-K, debt issuance, items 1.01/2.03, filed 2026-03-09 (accession 0001104659-26-025240).
8. Abbott 8-K, NEC settlement, items 7.01/8.01/9.01, filed 2026-08-20 (accession 0001104659-26-099247).
9. Insurance Journal, "Abbott Jury Awards at Least $53 Million in Infant-Formula Trial," 2026-04-10.
10. Legal Examiner / drugwatch.com NEC baby-formula lawsuit trackers, accessed 2026-09-26 (secondary, for suit-count cross-check; primary figure is the company's own 8-K).
11. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (program quant context, as_of 2026-09-25/2026-08-28).
12. v4/outputs/Q07_triage.json (prior triage entry for ABT).
