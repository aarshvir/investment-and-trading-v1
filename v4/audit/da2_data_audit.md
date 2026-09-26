# DA2 — Deep Data Audit: As-Filed Fundamentals (SEC XBRL → Point-in-Time Panel)

Auditor: da2. Scope: `v4/data/d3_pit_monthly*.parquet`, `d3_eps_quarterly_pit.parquet`, `d3_xbrl_facts.parquet`,
`d3_lineage.csv`, `d3_company_meta.csv` (d3_report.md was not yet written when this audit ran; the meta.json
sidecars and raw fact/lineage files were used instead, per the fallback instruction).
Seed: **20260926**. Supporting evidence tables: `v4/audit/da2_supporting/*.csv|json`.

## 1. Verdict

**YES-WITH-FIXES.** Data-quality score: **83/100**.

Rubric (my own, stated): filing-document fidelity for standard filers (30 pts) 27 · PIT/revision-integrity logic
(20 pts) 19 · independent cross-check agreement (15 pts) 12 · coverage/staleness transparency (10 pts) 9 ·
units/signs/dual-class & extreme-value handling (15 pts) 7 · lineage/documentation clarity (10 pts) 9.

The core engineering is strong: the `filed<=t` point-in-time rule has **zero violations in 114,695 rows**, revision
handling is demonstrably correct, and spot-checked revenue/NI/OCF/cash values match the actual EDGAR filings
exactly. But there is a real, concentrated defect surface — dual/multi-class share structures, one filer-side XBRL
tagging error, and one company whose revenue concept D3's candidate list no longer covers — none of which are
currently caught by a plausibility filter. These are individually severe (up to 1500x) but narrow (a handful of
tickers), and several are mechanically fixable (one is fixed in this audit).

## 2. Tests run, sample sizes, pass rates (95% Wilson CI)

**(1) Filing-document truth test.** Sample: 12 purposive (JPM bank · V payments · AAPL/NVDA/COST 52/53-wk · AME
2026-acquisition name · TRV/ALL/AIZ insurers · DLTR/TGT/BMY diligence-list) × 2 filings (latest 10-Q + latest
10-K) + 20 seeded-random current constituents × 1 filing (latest 10-Q) = **44 filing-checks across 32 companies**,
fetched from EDGAR's own rendered financial-statement pages (`R#.htm`, generated from each filer's inline XBRL —
not FMP/Yahoo), 0 fetch errors. Matched against the exact raw fact for that accession in `d3_xbrl_facts.parquet`:

| Field | Matched / extracted | Pass rate (95% CI) |
|---|---|---|
| Revenue | 31/31 | 100% [89–100%] |
| Net income to common | 29/29 | 100% [88–100%] |
| Operating cash flow | 26/26 | 100% [87–100%] |
| Cash & short-term investments | 30/30 | 100% [89–100%] |
| Capex (sign-corrected*) | 23/28 | 82% [64–92%] |
| Shares outstanding vs. panel | 28/32 | 88% [72–95%] |

\*My extractor read capex as a cash-flow-statement outflow (negative); `PaymentsToAcquirePropertyPlantAndEquipment`
is stored positive in XBRL. After sign correction, 5 residual misses (V, ETR, LNT, REG, VMC) traced to my own
regex grabbing a non-standard capex line (REIT/utility "construction/real-estate" labels) — not confirmed D3
defects. The 4 shares_out misses (AAPL×2, NVDA×2) traced to my script misreading a cover-page scale note; I
independently confirmed both companies' D3 values (14.59B / 24.1B shares) are correct. 13/44, 15/44, 18/44, 14/44
filings respectively had no matching line found by my generic parser (bank/insurer statement layouts) — not
scored either way. **Plus 4 targeted extreme-value checks (below) that found real defects.**

**Q4 = FY − 9M derivation.** Locally recomputed TTM (revenue/NI/OCF/capex) from the *original, first-filed* raw
facts only (fixed a dedup bug in my own harness that first sampled multi-year-stale comparatives) and compared to
the panel's TTM at the first month-end after each 10-K, for a random ~55-company sample per metric:
revenue 87% [76–94%], NI 93% [82–97%], OCF 93% [83–97%], capex 91% [80–96%] within 1%. Residuals are
concept-selection edge cases (see APA below), not derivation-math bugs — the FY−9M arithmetic itself checks out
on 8,700–8,900 recomputable pairs per metric.

**(2) Independent cross-check.** **FMP MCP tool access was denied** (plan-tier gate on the `statements` endpoint) —
substituted **Shibui Finance** (SEC-sourced quarterly financials, 9,500+ tickers), disclosed per instructions.
149/150 seeded-random current constituents resolved (1 gap: CEG). TTM vs. `d3_pit_monthly` at 2026-09:
revenue 82%/90% within 1%/5% [75–87%]/[84–94%], net income 87%/91% within 1%/5%, OCF 89%/91%, capex 51%/64%
(expected weaker — capex most convention-sensitive; sign flipped before comparing). Of 15 names >5% off on
revenue, most trace to known 2025–26 corporate actions (DD/Qnity spin, HON/Solstice spin, OMC/IPG merger) or
bank/finance gross-vs-net revenue conventions (C, CFG, TFC, SYF — confirmed via direct filing check that SYF's
NI/EPS match exactly, isolating the gap to the revenue *definition* only); COST is a TTM-window timing artifact.
**APA (-72%) is a confirmed defect, not a definitional difference — see below.**

**(3) Point-in-time integrity.** `max_filed_used <= month_end`: **0 violations in all 114,695 rows** and in a
2,000-row random sample (100% [99.8–100%]). ≥6 clean revision cases found and verified (after fixing two bugs in
my own test: instant-fact `groupby` silently drops rows when grouped on the NaT `start` column; and needing to
exclude cases where a *newer* period already superseded the "revision" before testing the switch) — VRT, LUV,
KMB, MDT, MAA, MI (`da2_supporting/revision_cases_clean.csv`). VRT's genuine 10-K/A restatement is reflected
exactly (panel shows $668M before the amendment, $512M after, both match to the dollar). MAA/MI show the panel
correctly *ignores* an 8-K's pro-forma figure that isn't a real restatement — good defensive behavior.

**(4) Coverage & staleness.** Feature coverage by year in `coverage_by_year.csv` (builds from ~0% in 2009–11 to
>90% for most core fields by ~2013, matching the disclosed XBRL-adoption caveat). At the 2026-09 snapshot:
staleness median 87 days, 90th pct 178 days, max 268 days (n=626 CIKs). **65 of 500 current constituents (13%)**
have fundamentals >120 days stale — list with `last_form`/`last_period_end` in `stale_gt120_current.csv`; spot
checks show this is mostly non-calendar/slow fiscal-year filers, not a pipeline defect. 3 current constituents
have no row at all in the latest snapshot (likely very recent index adds).

**(5) Units/signs/splits.** Flow signs: capex/buyback/div/issuance stored as **positive magnitudes** (99%/83%/
96%/71% positive; small negative tails, e.g. divestiture-driven negative capex, plausible but worth a spot check).
Splits: confirmed `eps_q0..q12` is retroactively split-adjusted to the *latest known* share basis at each snapshot
(AAPL/NVDA spot-checked) — **downstream users must know this is not as-originally-filed EPS**, while `shares_out`
is a raw point-in-time count that is *not* retroactively adjusted; mixing the two across a split date without also
consulting `n_splits_known`/`n_splits_detected` will misstate per-share ratios.

## 3. Defects found (evidence, severity, fix)

1. **BRK-B diluted EPS overstated ~1,500x for the whole 2,428-row history** (Severity: High, but bounded to one
   ticker). Berkshire's non-dimensional `EarningsPerShareDiluted`/`Basic` facts are Class-A-equivalent only; the
   1/1500 Class-B ratio is disclosed only in an English footnote, never as a structured fact. Confirmed against
   the actual filing: Q3 2013 10-Q shows `$3,074` for a 3-month period
   (https://www.sec.gov/Archives/edgar/data/1067983/000119312513423169/R3.htm, footnote [1]: "Net earnings per
   Class B common share is equal to one-fifteen-hundredth (1/1,500) of such amount"); true BRK-B EPS ≈ $2.05.
   Corrupts BRK-B's SUE / earnings-momentum factor. **Fixed**: `v4/data/da2_fix_eps_quarterly_pit_brkb.parquet`
   (2,428 rows, `eps_diluted_adj` ÷ 1500; meta sidecar has full derivation). Not touched: any BRK-A row.

2. **APA Corporation revenue understated ~75–80% since FY2021** (Severity: High). `d3_xbrl_facts` has no
   `Revenues`/`RevenueFromContractWithCustomerExcludingAssessedTax`/`SalesRevenueNet` fact for APA filed after
   2021-02-26 — APA's post-2020 filings use a custom `OilAndGasRevenue` concept plus a non-standard "Total
   revenues and other" line (bundling in derivative/divestiture gains); D3's candidate list doesn't include
   either. Confirmed against the actual Q2-2026 10-Q
   (https://www.sec.gov/Archives/edgar/data/1841666/000184166626000053/R2.htm): real quarterly revenue ≈$2.0–2.4B
   vs. panel's `rev_ttm` = $2.433B for the whole *year*. Checked: isolated to APA — the other 9 current-universe
   CIKs using `OilAndGasRevenue` still file a standard concept too. **Fix**: add `OilAndGasRevenue` (and/or the
   `apa:` extension for total revenues net of derivative/divestiture gains) to the revenue candidate list for CIK
   6769; generally, add a sanity check that flags any `rev_ttm` implying >50% q/q collapse with no disclosed
   divestiture.

3. **ERIE Class A/B share-count mixup** (Severity: High for affected snapshots). Panel shows `shares_out`=2,542
   for ERIE at 2021-06-30 — that is Erie Indemnity's non-traded **Class B** count; the traded ticker (Class A) had
   46,189,068 shares. Confirmed on the actual 10-Q cover page
   (https://www.sec.gov/Archives/edgar/data/922621/000092262121000036/R1.htm). Would corrupt any per-share/market-
   cap calc for ERIE at affected dates. **Fix**: for dual-class filers, select the `dei:EntityCommonStockShares
   Outstanding` context matching the actually-traded class/ticker, not the first non-dimensional value found;
   audit all ERIE month-ends (only one date-checked here) before trusting the series.

4. **Halliburton EPS off by exactly 10^6 for several 2022–24 quarters, and a broader, bounded EPS-scale problem**
   (Severity: High but a filer-side error, not a D3 bug). HAL's own filed 10-Q shows `Earnings Per Share, Diluted`
   = "$790,000" (Q3-2023) — this is what's rendered from HAL's own inline XBRL
   (https://www.sec.gov/Archives/edgar/data/45012/000004501223000056/R2.htm); true value ≈$0.79 (NI $716M / 902M
   diluted shares). D3 faithfully carried the filer's own tagging error. Sizing the wider problem: **3,940 of
   1,353,303 eps_quarterly_pit rows (0.29%) have |EPS|>1000**, concentrated in BRK-B (2,200, fixed above), HAL
   (503), ICE (432), BBWI (330), DXCM (207), HIG (114), TMO (77), VTRS (62), FTI/MDT/PARA/SWK (≤5 each) — full
   list in `local_audit_summary.json`. **Fix**: add a plausibility clip (e.g. reject |EPS|>$1,000, or >20x the
   trailing-quarter value, with the affected cell left MISSING rather than silently kept) — this single guardrail
   would have caught HAL, and would need per-ticker review for the others before deciding fix vs. flag.

5. **Shares-outstanding placeholder-value glitches, ~14 tickers, 27 month-to-month episodes** (Severity: Medium,
   bounded, self-correcting). `shares_out` occasionally drops to an implausible small constant (1, 100, 786,
   1000...) for one month then recovers next month — AAP, AMCR, ATO, COHR, CTVA, EXE, FOXA, LIN, LUV, MDT, NBR,
   NEE, QRVO, STI and others (`local_audit_summary.json` → shares jump table). Looks like an occasional bad
   `dei:EntityCommonStockSharesOutstanding` cover-page tag getting past D3's "fresh, plausible" filter. **Fix**:
   tighten the plausibility bound (e.g. reject a value that implies >10x single-month change with no confirmed
   split/spinoff).

6. **LUV transient PIT scale-error exposure** (Severity: Low, informational). A LUV 10-Q briefly tagged
   Assets/Equity at 1/1,000,000 scale (filed 2011-10-25, corrected by 10-Q/A 2011-11-08); because a month-end
   (2011-10-31) fell inside that 2-week error window, the *monthly* panel briefly shows the erroneous value before
   snapping to correct on 2011-11-30 (both transitions verified exactly). Not a D3 logic bug — it's a structural
   consequence of "latest filed<=t," faithfully implemented. **Action**: none required for the monthly panel; flag
   for anyone doing daily-granularity PIT from raw facts that the same risk applies without a sanity filter.

## 4. Fix shipped

`v4/data/da2_fix_eps_quarterly_pit_brkb.parquet` + `.meta.json` — corrected BRK-B `eps_diluted_adj` (÷1500), 2,428
rows, all 2,200 previously-implausible (|EPS|>1000) values now in a realistic $-0.66–$2.05 range. Does not
overwrite `d3_eps_quarterly_pit.parquet`; apply by ticker-match join and re-derive `sue` for BRK-B downstream.

## 5. Limitations of this audit

Generic filing-parser missed line items for bank/insurer layouts in 13–18 of 44 checks (not scored, not assumed
passing). ERIE/HAL/shares-glitch defects are dated at only the snapshots checked here — full historical extent
unquantified. FMP substitution (Shibui) reduces independence slightly since both ultimately source SEC filings.
