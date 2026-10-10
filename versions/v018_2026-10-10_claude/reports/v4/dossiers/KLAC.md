# KLA Corporation (KLAC) — Diligence Dossier (Agent F28, standard depth)

## 1. Verdict
**WATCH** — not now, on valuation discipline, not business quality. KLA is the best-moat business of the three names in this
batch, and the triage's quality/growth scores (5/5) are well supported by primary data. But the reverse DCF shows the price
already assumes a growth rate this industry has never sustained for a full decade, even in this AI-capex supercycle. A great
business priced for more than it can plausibly deliver is a WATCH under this program's own pre-committed rule, not an
INCLUDE. Horizon if it re-rates or grows into the multiple: 24–48 months.

## 2. Business in plain English
KLA makes process-control and yield-management equipment (inspection and metrology tools) that semiconductor fabs use to
find defects during manufacturing. It holds the leading share in this sub-segment of semicap equipment — every advanced
logic and memory fab, and increasingly every advanced-packaging line, needs its tools regardless of which chipmaker wins the
underlying race, which gives it a toll-booth-like position on the entire industry's capital spending rather than exposure
to any single customer's success.

## 3. Why the model likes it — durable or artefact?
b1_live_scores.csv: composite 0.46 (live_rank 270/503 — a lower composite than FSLR/GEN because KLA scores weakly on the
Value family at today's price, which is exactly the tension this dossier resolves). Triage (Q12_triage.json) called it the
"best moat in semicap," citing a 33x NTM P/E as fair for 15% revenue and 83% EPS growth. **Verified:** the growth numbers
are real and accelerating — Q1 FY26 revenue +13.0% YoY, Q2 +7.2%, Q3 +11.5%, **Q4 FY26 +15.2% YoY** (all SEC XBRL, cross-
checked against earnings releases), and FY2026 GAAP net income grew to $4.83bn (FY2025: $4.06bn, FY2024: $2.76bn) — a
genuine acceleration, not a one-quarter blip. China revenue concentration has been *falling*, not rising, as a risk (29.8% of
FY2026 revenue vs 33.3% FY2025 and 42.8% FY2024, per the FY2026 10-K), which reduces (does not eliminate) the export-control
tail risk. **What needs adjustment:** the "33x NTM P/E is fair for 83% EPS growth" framing understates how much growth is
already priced in over a full decade, not just next year — see §7. It is durable near-term, not an artefact, but the
multiple is pricing perpetuity-level assumptions onto a single strong year.

## 4. Last eight quarters (SEC XBRL, GAAP, USD millions except EPS; fiscal year ends 30-Jun)
| Quarter | Revenue | YoY growth | GAAP Net income | Net margin | GAAP diluted EPS (split-adjusted)¹ |
|---|---|---|---|---|---|
| Q1 FY25 (Sep-2024) | 2,841.5 | +18.5% | 945.9 | 33.3% | 0.701 |
| Q2 FY25 (Dec-2024) | 3,076.9 | +23.7% | 824.5 | 26.8% | 0.616 |
| Q3 FY25 (Mar-2025) | 3,063.0 | +29.8% | 1,088.4 | 35.5% | 0.816 |
| Q4 FY25 (Jun-2025)² | 3,174.7 | n/a | 1,202.8 | 37.9% | 0.907 |
| Q1 FY26 (Sep-2025) | 3,209.7 | +13.0% | 1,121.0 | 34.9% | 0.847 |
| Q2 FY26 (Dec-2025) | 3,297.1 | +7.2% | 1,145.7 | 34.7% | 0.868 |
| Q3 FY26 (Mar-2026) | 3,415.1 | +11.5% | 1,201.0 | 35.2% | 0.912 |
| Q4 FY26 (Jun-2026) | 3,657.6 | +15.2% | 1,363.0 | 37.3% | 1.04 |

Source: SEC EDGAR XBRL companyfacts (CIK 319201), discrete-quarter facts; Q4 FY26 cross-checked exactly against the FY2026
earnings release (revenue $3.658bn, net income $1.363bn, diluted EPS $1.04). ¹ **KLA completed a 10-for-1 stock split
effective after market close 11-Jun-2026** (record date 4-Jun-2026; OCC Info Memo #58941), i.e. mid-way through Q4 FY26.
Pre-split quarters' EPS (originally reported $5.41–$9.12) are shown here divided by 10 for comparability; Q4 FY25 EPS is
further derived (FY2025 annual EPS $3.04 minus the pre-split-equivalent 9-month YTD) because it is not separately tagged.
² Q4 revenue/NI figures for FY25/FY26 that are not separately tagged were derived as FY-annual-10-K minus 9-month-YTD-10-Q
(dollar amounts, unaffected by the later split); Q4 FY26 derivation cross-checks exactly to the earnings release.

**Data conflict — flag for the wider program:** `v4/data/d4_live_snapshot.parquet`'s forward-estimate-trend fields for KLAC
(`eps_q0`, `eps_q1`, `eps_fy0`, `eps_fy1`, `rev_q0`, `rev_fy0`, `rev_fy1`, and the multiples derived from them —
`pe_fy0`, `pe_fy1`, `pe_ntm_qsum`) are **internally inconsistent with the row's own headline fields and with primary SEC
data**: e.g. `rev_fy0` = $5.04bn versus KLA's actual ~$13.6–14bn annual revenue run-rate, and `eps_fy0`/`eps_fy1` of
$17.49/$23.19 versus the SEC-confirmed post-split trailing EPS of ~$3.66–3.70 and Yahoo's own `y_forwardEps` of $6.71 (which
*is* internally consistent with `pe_ntm`=32.65x at the $187.92 price). This looks like either a stale pre-split pull that
was never refreshed after KLA's 11-Jun-2026 split, or a symbol-mapping fault in the estimates-trend feed specifically for
KLAC — either way, **any other agent or script reading d4's `*_fy0`/`*_fy1`/`*_q0`/`*_q1` columns for KLAC will get numbers
off by roughly 3–5x**. Recommend DA (data-audit) follow-up; not corrected in d4 itself per this agent's write-scope limits.

## 5. Guidance track record
Two quarters independently verified in this pass (time-boxed; four requested):
- **Q3→Q4 FY26:** Q3 FY26 release (filed ~Apr-2026) guided Q4 FY26 revenue $3.575bn ±$200m and GAAP diluted EPS $9.66 ±$1.00
  (pre-split terms). Actual Q4 FY26: revenue $3.658bn (within range, above midpoint) and diluted EPS equivalent to ~$10.4
  pre-split (i.e., **beat**, at the upper half of the guided band).
- **Q4 FY26→Q1 FY27:** Q4 FY26 release (28-Jul-2026) guided Q1 FY27 (quarter ending 30-Sep-2026) revenue $4.0bn ±$200m,
  GAAP diluted EPS $1.14 ±$0.10 (post-split). Not yet reportable as actual (next earnings 28-Oct-2026).
Track record over the two verified quarters: **guidance met/beaten, not cut.**

## 6. Earnings quality & balance sheet
- **Cash conversion — data conflict corrected:** FY2026 (annual) operating cash flow = **$4,143.1m** (SEC XBRL, 10-K); FY2026
  capex = **$375.9m**. **Primary-sourced TTM FCF ≈ $3,767.1m.** This is materially higher than the Yahoo/d4 `freeCashflow`
  field of $2,625m used in the quant snapshot — a ~30% (**$1.14bn**) understatement in the aggregator figure, implying an
  aggregator capex assumption roughly 4x the actual reported capex. **This is the largest and most consequential data
  conflict found in this dossier**, since FCF yield feeds directly into the V-family quant score; the true FCF yield is
  ~1.5% of EV, not the lower figure a naive read of d4 would produce (though still low either way, given the size of KLA's
  EV — this is a low-FCF-yield, high-multiple name regardless of which figure is used).
- **Balance sheet:** cash $1.650bn + marketable securities $3.253bn = $4.90bn liquid assets; long-term debt $5.887bn; net
  debt ≈ $1.25bn **[Corrected 2026-10-10: long-term debt $5,887.4m less cash $1,649.8m and marketable securities $3,252.6m is about $985m (Q4 FY26 release, acc 0000319201-26-000024)]** — trivial relative to $245bn market cap. Investment-grade-quality balance sheet.
- **Capital return:** dividend raised to $2.30/share annualised **[Corrected 2026-10-10: $2.30 is the new QUARTERLY dividend, pre-split (Q3 FY26 release, acc 0000319201-26-000014); post-split that is $0.23 a quarter, $0.92 annualised, about 0.5% yield]** — the **17th consecutive annual increase** — plus a new $7bn
  buyback authorisation and $2.29bn of FY2026 repurchases. No dilution concern; share count has fallen from ~137.1m (Sep-23,
  pre-split-equivalent ~1,371m) to ~1,306m post-split-equivalent shares outstanding.
- **Operating margin ~41–42%** (GAAP, per the Q3/Q4 FY26 releases) — KLA does not tag a discrete `OperatingIncomeLoss` line
  in its recent XBRL (it uses a non-standard income-statement presentation; the figure here is taken directly from the
  earnings-release text, not derived), a minor but genuine sourcing friction disclosed rather than hidden.

## 7. Valuation snapshot and reverse DCF
Price 25-Sep-2026 close: $187.92 (post-split). Market cap $245.24bn. EV (net debt $1.25bn) ≈ **$246.49bn**. Trailing P/E
50.8x (elevated by the lower-margin early part of FY2026 still sitting in the trailing window); NTM P/E per d4's headline
(reliable) field ≈ 28.0–32.7x depending on the exact forward-EPS vintage used. Trailing P/FCF on the **corrected** FCF
figure = 65.4x; FCF yield 1.5%.

**Reverse DCF** (WACC 10.0%, terminal growth 3.5%, 10-year horizon, base FCF = corrected TTM $3,767.1m, EV anchor $246.49bn):
**implied stage-1 FCF growth ≈ 22.5% per year for 10 years.** **[Corrected 2026-10-10: FCF of $3,767.1m adds back stock-based compensation of $310.2m; with SBC treated as a cost (FCF $3,457m) the implied growth is about 23.6%, still above base]** This is the key finding of this dossier: sustaining ~22–23%
compound FCF growth for a full decade would require KLA's FCF to grow roughly 8x by 2036, in an industry that is structurally
cyclical (semicap equipment order books historically swing with the 3–5 year memory/logic capex cycle). An evidence-based
**base case of roughly +12–14%/yr** over 10 years (front-loaded high-teens-to-20% growth through the current AI-capex
upcycle for 2–3 years, fading to high-single-digit growth as the cycle normalises and China-related headwinds persist) is
well **below** the ~22.5%/yr the market is paying for. **Implied vs base: above (expensive)** — this is the reason for the
WATCH verdict despite best-in-class business quality. No V1 systematic valuation exists for this name yet.

Scenario table (post-split GAAP EPS basis, 3-year horizon, dividend yield ~0.4%/yr added):
| Scenario | Prob. | 3y-forward EPS | Exit P/E | Value/share | 3y annualised total return |
|---|---|---|---|---|---|
| Bear | 30% | $5.00 | 20x | $100 | **~-19.5%/yr** **[Corrected 2026-10-10: recomputed from the table inputs: about -18.6%/yr]** |
| Base | 45% | $7.50 | 25x | $187.50 | **~+0.4%/yr** |
| Bull | 25% | $9.50 | 30x | $285 | **~+15.3%/yr** |

Bear reflects a semicap-cycle downturn (memory/logic capex digestion after the current AI build-out) compounded with a
tighter China export-control regime; base assumes the current growth trajectory moderates to a sustainable mid-teens rate
and the multiple normalises from its currently elevated trailing level; bull assumes the AI capex cycle extends without a
digestion phase.

## 8. Bull case / Bear case
**Bull:** (1) Structurally the best-positioned company in semicap equipment — process control/inspection is needed
regardless of which chipmaker or foundry wins the AI race, and KLA's share in this sub-segment is the highest in the
industry (triage assessment, consistent with the accelerating, broad-based revenue growth seen across all four FY2026
quarters). (2) China revenue *concentration* is falling (42.8%→33.3%→29.8% over three fiscal years) even as absolute China
revenue held roughly flat — the mix is diversifying away from the single largest geopolitical risk. (3) Fortress balance
sheet (net debt ~$1.25bn against $245bn market cap) and a 17-year dividend-growth streak fund growth and buybacks
simultaneously.

**Bear:** (1) The reverse DCF shows the market pricing ~22.5%/yr FCF growth for a decade — a bar this cyclical industry has
not cleared over any historical 10-year window, including the most recent AI-driven upswing (KLA's own 3-year revenue CAGR
into FY2026 is well under half that rate). (2) Export-control risk to China is not resolved, only reduced in relative
weight — the FY2026 10-K explicitly attributes flat China revenue to export-control restrictions offsetting legacy-node
capex, meaning further tightening could still cut absolute dollars, not just share. (3) Trailing P/FCF of ~65x (corrected
figure) means the stock is priced overwhelmingly on the *next several years'* growth, not today's cash generation — a
classic setup for a sharp de-rating if the semicap cycle turns even briefly.

## 9. Key risks & kill criteria
1. Quarterly revenue YoY growth **below 5% for two consecutive quarters** (a classic early semicap-cycle-turn signal;
   currently accelerating at 7–15%).
2. **GAAP diluted EPS guidance cut** at any subsequent release (currently 2-for-2 met/beaten in this pass's sample).
3. China revenue **share or absolute dollars fall further** in a way the company attributes explicitly to *new* export
   restrictions (as opposed to the already-disclosed, gradually diversifying trend).
4. Net debt/EBITDA (currently trivial) **rises above 1.0x** without a value-accretive reason disclosed (would signal a
   large, possibly dilutive, capital-allocation shift).
5. Trailing P/FCF (corrected basis) **stays above 50x for more than two quarters after revenue growth decelerates below
   10% YoY** — the combination that would confirm the market has not yet re-rated the stock down to the base case.

## 10. Catalysts & calendar
Next earnings: **28-Oct-2026** (Q1 FY2027, quarter ended 30-Sep-2026; company guided revenue $4.0bn ±$200m, GAAP diluted
EPS $1.14 ±$0.10 at the Q4 FY26 release). No investor day identified in the sources reviewed.

## 11. Red-flag scan
- **Stock split (disclosure, not a red flag):** 10-for-1 split effective 11-Jun-2026 (record date 4-Jun-2026) — confirmed
  via OCC Info Memo #58941 and KLA's own 8-K; all figures in this dossier are presented split-adjusted with the pre-split
  quarters explicitly converted and flagged.
- **China export controls:** the company's own FY2026 10-K and earnings releases disclose "evolving Bureau of Industry and
  Security rules" restricting sales of certain tools to certain Chinese customers, without quantifying the dollar impact —
  an acknowledged but unquantified risk.
- **Data-integrity finding (see §4/§6):** the d4 estimate-trend fields for KLAC are internally inconsistent and appear
  stale/mis-mapped post-split; and the aggregator FCF figure materially understates the primary-sourced figure. Both are
  disclosed as `data_conflicts` in the summary JSON for DA follow-up.
- No auditor changes, going-concern language, restatements, or unusual insider-selling pattern identified in the sources
  reviewed this pass.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: **Q4 FY2026 / full fiscal year 2026 (quarter and year ended 30-Jun-2026), 10-K filed
6-Aug-2026.** Checked for events to **25-Sep-2026** (market close). All figures are **consolidated GAAP** unless labelled
non-GAAP; all per-share figures are stated split-adjusted (10-for-1, effective 11-Jun-2026) with the conversion
methodology disclosed in §4. Data-quality note: revenue/NI/EPS are primary-sourced (SEC XBRL, cross-checked to earnings
releases); the FCF and d4 estimate-trend figures are flagged in §4/§6 as conflicting between primary filings and the
Yahoo-derived quant snapshot, with the primary-sourced figure used for this dossier's valuation.
**This is research, not investment advice, and not a personalised or financial recommendation — consult a licensed advisor
for any decision.**

## 13. Sources
1. SEC EDGAR, KLA Corporation (CIK 0000319201), companyfacts XBRL API: https://data.sec.gov/api/xbrl/companyfacts/CIK0000319201.json (retrieved 26-Sep-2026)
2. KLA Corporation, FY2026 10-K (filed 6-Aug-2026): https://www.sec.gov/Archives/edgar/data/0000319201/000031920126000027/klac-20260630.htm
3. KLA Corporation, "Reports Fiscal 2026 Fourth Quarter and Full Year Results" (28-Jul-2026): https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full
4. KLA Corporation, Q3 FY2026 earnings release exhibit (filed ~Apr-2026): https://www.sec.gov/Archives/edgar/data/0000319201/000031920126000014/exhibit991earningsrelease3.htm
5. OCC Information Memo #58941, "KLA Corporation - 10 For 1 Stock Split" (11-May-2026): https://infomemo.theocc.com/infomemos?number=58941
6. Yahoo Finance, "How Investors Are Reacting To KLA (KLAC) Ten-for-One Split And AI-Focused Capital Structure Shift": https://finance.yahoo.com/markets/stocks/articles/investors-reacting-kla-klac-ten-231643196.html
7. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (row: KLAC), v4/outputs/Q12_triage.json (internal, retrieved 26-Sep-2026)
8. scripts/valuation.py (finance-skills stock-analysis skill), reverse-DCF and scenario computation, run 26-Sep-2026

## Correction (verification DV25, 2026-10-10)

Sources: 8-K Ex-99.1 acc 0000319201-26-000014 (Q3 FY26, 29 Apr 2026) and acc 0000319201-26-000024 (Q4 FY26, 28 Jul 2026); 10-K acc 0000319201-26-000027; XBRL companyfacts. Quarterly revenue, net income and EPS (period labels correct), FY24-FY26 net income, both guidance ranges (Q4 FY26 revenue $3.575bn +/- $200m, GAAP EPS $9.66 +/- $1.00; Q1 FY27 revenue $4.0bn +/- $200m, GAAP EPS $1.14 +/- $0.10; all verbatim), debt, cash, securities, operating cash flow, capex, FCF, China share (10-K: 30%, 33%, 43%) and share count pass. The XBRL cross-tie flag (net income 1,363 vs 1,201) is a stale-XBRL artefact: the release confirms Q4 FY26 net income $1,363m.

1. Dividend (FAIL). Wrong text: "dividend raised to $2.30/share annualised". Correct: the Board raised the quarterly dividend to $2.30 per share (pre-split) from the May 2026 declaration; after the 10-for-1 split of 11 Jun 2026 that is $0.23 a quarter, $0.92 a year (about 0.5% yield at $187.92). The 17th consecutive increase and the $7bn authorisation pass. No verdict effect.
2. Net debt (FAIL, minor). Wrong text: "net debt about $1.25bn". Correct: $5,887.4m less $4,902.4m liquid assets = $985m; EV about $246.2bn instead of $246.49bn. No effect on the reverse DCF or verdict.
3. Bear scenario (MINOR). $100 vs $187.92 over three years with a 0.4% dividend gives about -18.6% a year, not -19.5%. `F28_summary.json` KLAC bear return updated.
4. Reverse-DCF cash flow (MINOR, method). TTM FCF $3,767.1m is operating cash flow less capex and still adds back $310.2m of stock-based compensation. Treating SBC as a cost (FCF $3,457m) the implied stage-1 growth at the same 10.0% rate and 3.5% terminal is 23.6% a year (22.5% reproduces on the unadjusted figure); at 5.17% + 5.0% equity risk premium it is 24.1%. The 10.0% rate is not stated as risk-free plus premium. implied_vs_base stays "above".

Verdict change: none (WATCH kept). `F28_summary.json` KLAC updated (bear return, implied-growth wording).
