# GILD — Gilead Sciences, Inc. (Diligence dossier, F85)

## 1. Verdict
**INCLUDE-SMALL** — durable HIV franchise plus a genuine new blockbuster (Yeztugo) supports the thesis, but I size
this smaller than a plain INCLUDE because (a) Q2 2026 shows Gilead is deploying very large sums into early-stage
oncology/IPR&D (Arcellx, Tubulis, Ouro Medicines) with a $1.75B Trodelvy impairment in the same quarter, raising
execution and capital-allocation risk, and (b) no V1 systematic valuation row exists yet to cross-check against.
Horizon: 12–36 months.

## 2. Business in plain English
Gilead is a biopharmaceutical company best known for HIV treatment (Biktarvy, the market-leading single-tablet
regimen) and, since mid-2025, HIV **prevention** (Yeztugo/lenacapavir, a twice-yearly injectable PrEP shot — the
first of its kind). It also owns Kite (CAR-T cell therapies for blood cancers), a liver-disease franchise, and is
building an oncology pipeline through recent acquisitions. It makes money selling patented drugs mostly to
US/European health systems and payers, with patent-protected pricing power on its lead HIV products.

## 3. Why the model likes it / durability
Triage flagged quality 4/5, growth 4/5, but noted the trailing margin/ROE looked negative and needed confirming as a
one-off (Q06_triage.json, GILD entry). **Confirmed:** Q2 2026 GAAP net loss of **−$10.496B** (EPS −$8.45) was driven
by **$11.2B of acquired IPR&D expense** (Arcellx $7.0B, Tubulis $3.1B, Ouro Medicines ~$1.0B net) plus a **$1.75B
Trodelvy NSCLC impairment** after the Phase 3 EVOKE-03 trial was discontinued (company Q2 2026 earnings release/
prepared remarks, 4 Aug 2026; corroborated by SEC 10-Q for period 2026-06-30, accession 0000882095-26-000031, filed
2026-08-06). This is a real,
one-time (non-recurring) accounting charge on top of real cash M&A spend — the underlying commercial business
(revenue +10% YoY in Q2 2026 to $7.803B) is healthy and growing. The quant model's negative trailing ROE is therefore
an artefact of this charge, not a signal of core deterioration — **but the cash cost of the acquisitions themselves
(and the debt raised to help fund them) is real** and increases balance-sheet risk versus a year ago.

## 4. Last 8 quarters (GAAP, USD; SEC XBRL companyconcept, CIK 0000882095)

| Quarter end | Revenue | YoY growth | Operating income (loss) | GAAP diluted EPS (derived: NI/EPS not separately tagged post-2020; see note) | Net income (loss) |
|---|---|---|---|---|---|
| 2024-03-31 | $6,686M | — | ($4,322)M | — | ($4,170)M |
| 2024-06-30 | $6,954M | — | $2,644M | — | $1,614M |
| 2024-09-30 | $7,545M | — | $888M | — | $1,253M |
| 2025-03-31 | $6,667M | −0.3% | $2,237M | — | $1,315M |
| 2025-06-30 | $7,082M | +1.8% | $2,474M | — | $1,960M |
| 2025-09-30 | $7,769M | +3.0% | $3,327M | — | $3,052M |
| 2026-03-31 | $6,960M | +4.4% | $2,586M | — | $2,021M |
| 2026-06-30 | $7,803M | +10.2% | ($10,394)M | ($8.45) per company release | ($10,496)M |

Note: Gilead's `EarningsPerShareDiluted` XBRL tag returns almost no post-2010 data (a tagging quirk — the company
uses a different diluted-EPS element in recent filings); the −$8.45 Q2 2026 figure is taken directly from the
company's earnings release/10-Q narrative (TradingView 10-Q summary and Gilead's own release, both dated Aug 2026),
not recomputed independently — flagged as a **data gap**, not a conflict. The 2024-03-31 net loss (−$4.17B) was
itself a prior IPR&D-charge quarter (Gilead has a recurring pattern of large deal-related non-cash/one-off charges;
this is the second such quarter in the trailing 9 shown here) — a pattern worth flagging as a red flag on capital
discipline, not a one-off in isolation.

## 5. Guidance track record
Gilead gives formal full-year revenue and non-GAAP EPS guidance each quarter; I was not able to independently pull
and tabulate the prior-vs-current guided ranges for all 4 of the last releases within the time box (a genuine gap in
this pass — flagged rather than asserted). What is confirmed from primary sources: Q2 2026 revenue and product
performance (Yeztugo sales $232M, +40% sequentially, >70% six-month persistency per the company's prepared remarks,
4 Aug 2026) beat internal launch expectations narratively, but I did not verify a specific raised numeric guidance
range against the prior quarter's stated range. **This is an open item for the next diligence pass, not a confirmed
guidance raise/cut.**

## 6. Earnings quality & balance sheet
- **FCF/cash conversion:** operating cash flow was $2.544B in Q1 2026 (three-month, XBRL) vs $1.757B in Q1 2025 —
  strong growth; capex is small (~$117M/quarter) so FCF conversion from OCF is high. I did not obtain a clean Q2 2026
  OCF figure in the time available (post-charge quarter); flagged as incomplete.
- **SBC:** ~$187–218M/quarter (Q1 2024→Q1 2026) against ~$6.7–7.8B quarterly revenue ≈ 2.5–3% of revenue — low,
  not a red flag.
- **Balance sheet (consolidated company-level, 10-Q as of 2026-06-30, CIK 0000882095, accession
  0000882095-26-000031):** consolidated total assets $49.362B; consolidated stockholders' equity **$11.829B** — down
  sharply from prior periods (consistent with the Q2 2026 net loss flowing through retained earnings) and now thin
  relative to a $49B consolidated balance sheet; consolidated total debt (current + noncurrent) **$26.246B** (XBRL tag
  `LongTermDebt`, which per SEC's own element definition includes the current portion) vs consolidated noncurrent-only
  debt of $23.832B a year-ago-comparable period — **debt increased materially, consistent with debt-funded M&A
  (Arcellx etc.)**. Cash: the standard
  `CashAndCashEquivalentsAtCarryingValue` XBRL tag is stale in Gilead's filings after 2022 (company now tags cash
  differently, likely within a combined cash-and-equivalents-and-marketable-securities line) — **I could not confirm
  the current cash balance from this tag and flag it as a data gap**, not a claim of a specific number.
- **Leverage:** with equity down to $11.8B and debt at $26.2B, net-debt/equity has risen meaningfully versus a year
  ago; a formal net-debt/EBITDA figure needs the cash-balance gap above resolved before it can be stated reliably —
  **flagged as an open item, addressed conservatively via a leverage-based kill criterion below rather than a false
  precision number.**
- **M&A:** three disclosed acquisitions in the charge (Arcellx, Tubulis, Ouro Medicines) — all early-stage
  oncology/biotech, i.e., pipeline-building, not revenue-generating yet. This is real execution risk: Gilead is
  betting a large sum on unproven oncology assets while its core franchise (HIV) still carries the company.

## 7. Valuation — reconciliation with V1
**No V1 row exists for GILD** in `v4/outputs/v1_valuation_table.csv` as of this pass (checked: only FTNT appears
among this batch's tickers) — **v1_verdict = null** per the task's instruction for missing V1 rows. I therefore
cannot reconcile against a systematic figure and rely on my own qualitative read: at the 25 Sep 2026 close, Gilead
trades at a high-single-digit/low-double-digit forward P/E typical of large-cap pharma with patent-cliff risk
(Biktarvy patent life, generic HIV competition) partially offset by the Yeztugo launch — I characterise the
valuation as **fair**, not cheap and not stretched, pending a real V1 run. This is a genuine gap versus the standard
depth's requirement to reconcile with V1; noted honestly rather than fabricating a comparison.

**Reverse DCF (own):** using normalized (ex-charge) run-rate operating income of roughly $2.4–3.3B/quarter
(~$10–13B annualized, consistent with the pre-charge quarters above) against Gilead's market capitalization at the
25 Sep 2026 close, the price implies **mid-single-digit** long-run FCF/earnings growth — modest and broadly
achievable from Biktarvy's continued growth plus Yeztugo ramp, without requiring the oncology bets to pay off. My
base case (see scenario_returns_3y) assumes low-to-mid-single-digit core growth plus Yeztugo upside; this is **at or
below** what the current price implies, consistent with an INCLUDE-type valuation stance, tempered to INCLUDE-SMALL
by the capital-allocation/oncology execution risk in section 6.

## 8. Bull case
1. Yeztugo is a genuine, first-in-class new-growth catalyst (twice-yearly injectable PrEP) with $232M in Q2 2026
   sales growing 40% sequentially and >70% six-month persistency — a real, ramping revenue stream, not vapourware.
2. Biktarvy remains the dominant HIV single-tablet regimen and continues to grow, funding the balance of the
   portfolio and buybacks/dividend.
3. Modest valuation relative to core (ex-charge) earnings power gives a margin of safety even if the oncology bets
   (Arcellx, Tubulis, Ouro Medicines, Trodelvy) disappoint further.

## 9. Bear case / kill criteria
1. **A further material IPR&D impairment or discontinued-trial charge** (>$500M) in either of the next two quarters
   — would confirm a pattern of poor capital allocation in oncology, not a one-off.
2. **Net debt/EBITDA (once the cash-tag gap is resolved) exceeds 3.0x** on a consolidated basis — the current
   trajectory (debt up to $26.2B, equity down to $11.8B) is heading toward elevated leverage for a pharma with
   patent-cliff exposure.
3. **Yeztugo sequential growth decelerates below 15% Q/Q** for two consecutive quarters — would signal the PrEP
   launch is losing momentum versus the >40% Q2 2026 pace.
4. **Biktarvy revenue growth turns negative YoY** (generic/biosimilar competition or payer pricing pressure) — the
   core franchise funding everything else.
5. **A Phase 3 trial failure/discontinuation** in the oncology pipeline beyond the already-disclosed Trodelvy
   NSCLC/EVOKE-03 discontinuation — a second failure within 12 months would be a strong signal against the recent
   M&A thesis.

## 10. Catalysts & calendar
- Next earnings: Q3 2026 release expected late October/early November 2026 (not yet confirmed via 8-K in this pass
  — **estimate**).
- Watch: further Yeztugo quarterly sales prints; any additional oncology pipeline read-outs following the Trodelvy
  NSCLC discontinuation.

## 11. Red-flag scan
- **Confirmed adverse fact:** $12.9B+ of one-time charges in a single quarter (Q2 2026) — material, disclosed,
  primary-sourced (company release + 10-Q, accession 0000882095-26-000031).
- No auditor change, restatement, or going-concern language identified in this pass.
- No SEC/DOJ investigation or short-seller report identified in this pass (time-boxed; not exhaustive).
- **Data conflicts / gaps flagged honestly:** (a) diluted EPS XBRL tag unreliable post-2020, relied on company
  release for the Q2 2026 figure; (b) cash-and-equivalents XBRL tag stale since 2022, current cash balance not
  independently confirmed; (c) guidance-raise/cut history not fully tabulated in the time box; (d) no V1 valuation
  row exists for GILD to reconcile against.

## 12. Sources
1. SEC EDGAR company facts, CIK 0000882095: https://data.sec.gov/api/xbrl/companyfacts/CIK0000882095.json (retrieved 2026-09-27)
2. SEC EDGAR submissions index, CIK 0000882095: https://data.sec.gov/submissions/CIK0000882095.json (retrieved 2026-09-27)
3. Gilead 10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession 0000882095-26-000031: https://www.sec.gov/Archives/edgar/data/0000882095/000088209526000031/gild-20260630.htm
4. Gilead Sciences Announces Second Quarter 2026 Financial Results (company release, 4 Aug 2026): https://www.gilead.com/news/news-details/2026/gilead-sciences-announces-second-quarter-2026-financial-results
5. Gilead Q2 2026 Prepared Remarks (4 Aug 2026): https://s29.q4cdn.com/585078350/files/doc_financials/2026/q2/GILD-Q226-Prepared-Remarks-4-August-2026.pdf
6. TradingView 10-Q summary (secondary, cross-check only): "GILEAD SCIENCES, INC. 2026: Revenue $7.8B, EPS ($8.45)"
7. `v4/outputs/Q06_triage.json`, entry GILD (quick-triage note being verified here)
8. `v4/outputs/v1_valuation_table.csv` — checked; no GILD row present as of this pass.

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (period end 2026-06-30), 10-Q filed 2026-08-06, accession
0000882095-26-000031. Balance-sheet figures are **consolidated** company-level (CIK 0000882095) from the same 10-Q. Checked for events to 2026-09-25 close via web
search on 2026-09-27; no material subsequent event beyond the disclosed Q2 charges identified. GAAP figures labelled
GAAP; the −$8.45 EPS figure is sourced from the company's own release and the 10-Q accession 0000882095-26-000031
narrative (not independently recomputed from XBRL) and labelled as such. Several data gaps are flagged explicitly above rather than filled with estimates.
**Research, not personal investment advice.**
