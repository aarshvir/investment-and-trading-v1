# DA11 — Adversarial data audit: dossier facts (EXC, STE, BALL)

**As of:** 2026-09-27 · **Scope:** three current-holding dossiers — **EXC, STE, BALL**. 21 load-bearing facts checked (7/7/7 by ticker), selected for the claims most likely to break a thesis or a kill criterion if wrong: headline quarterly/annual figures, guidance track records, debt and leverage, rate-case/regulatory decisions, litigation/settlement terms, and balance-sheet items. `dossier_precheck.json` entries for EXC, STE and BALL were read and their flagged lines (balance-sheet figures without explicit entity scope, possible period mislabels, citations without accession numbers) were checked among the facts below where load-bearing. Special attention paid to EXC's multi-registrant filing structure (Exelon Corp consolidated vs. ComEd/PECO/BGE/PHI subsidiary registrants in the same combined 10-Q) and STE's non-calendar fiscal year (FYE 31-March). **Method:** primary sources only — SEC EDGAR 8-K Ex-99.1 earnings-release exhibits, 10-Q/10-K text, and data.sec.gov XBRL companyconcept pulls — fetched directly from `www.sec.gov`/`data.sec.gov` and cited below. Each dossier was read to its end; no appended "Correction" sections were found on any of the three. Each ticker's one-line thesis and first kill criterion were also checked for consistency with the underlying filings.

## Top-line result

**21 facts checked: 17 PASS, 2 MINOR, 0 FAIL, 0 UNVERIFIABLE.** Strict pass rate = 17/21 = **81.0%**; including MINORs as effectively-correct = 19/21 = **90.5%**. EXC and BALL's kill-criterion and thesis-consistency facts all held up exactly. Both MINOR findings are small (<0.5%) numeric overstatements in supporting detail (a segment-revenue figure for STE, an EBITDA figure for BALL) that do not change any guidance figure, leverage-ratio conclusion, or kill-criterion status.

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | EXC | Q2 2026: GAAP EPS $0.39; adj. operating EPS $0.43; FY26 guide affirmed $2.81-$2.91 | 8-K Ex-99.1, Q2 2026, filed 2026-07-30 | PASS |
| 2 | EXC | Guidance track record: introduced $2.81-$2.91 (Q4/FY25) → affirmed Q1 2026 → affirmed Q2 2026 | 8-K Ex-99.1, Q4/FY25, Q1/Q2 2026 | PASS |
| 3 | EXC | FY2025 actual: GAAP EPS $2.73; adj. operating EPS $2.77 | 8-K Ex-99.1, Q4/FY25, filed 2026-02-12 | PASS |
| 4 | EXC | LT debt $41.3bn→44.7bn→49.4bn(FY23-25)→$47.9bn noncurrent(Q1'26); equity $26.9bn→$29.3bn | XBRL companyconcept, CIK0001109357 | PASS |
| 5 | EXC | BGE MD rate case filed 2026-07-02: $156M ask, 10.40% ROE ask, decision Q1 2027 | 8-K Ex-99.1, Q2 2026 | PASS |
| 6 | EXC | Q2'26 debt issuances: ComEd $1,425M, BGE $925M, Pepco $130M; 86% of 2026 plan executed | 8-K Ex-99.1, Q2 2026 | PASS |
| 7 | EXC | Kill criterion 1 / thesis consistency: no guidance cut at any checkpoint | 8-K Ex-99.1 releases, Q4/FY25-Q2'26 | PASS |
| 8 | STE | FY2026: revenue $5,935.9m(+8.7%/+9% headline); GAAP EPS $7.93; adj. EPS $10.17 | 8-K Ex-99.1, Q4/FY26, filed 2026-05-11 | PASS |
| 9 | STE | Q1 FY27: P&L guidance reiterated ($11.10-$11.30); capex $375m→$450m; FCF $850m→$800m | 8-K Ex-99.1, Q1 FY27, filed 2026-08-05 | PASS |
| 10 | STE | Q1 FY27 segment detail: Healthcare $1,051.4m(+8%)/AST $297.6m(+6%)/Life Sci $146.7m(+9%) | 8-K Ex-99.1, Q1 FY27, segment table | **MINOR** |
| 11 | STE | Leverage: LT debt (noncurrent) $1,812.8m(FY26-end)→$1,650.2m(Q1FY27-end); cash $482.3m | XBRL companyconcept, CIK0001757898 | PASS |
| 12 | STE | EO litigation: term sheets 3-Mar-2025, settlement agreements 29-Oct-2025 | STERIS 8-Ks (Item 8.01), Mar-2025/Oct-2025 | PASS |
| 13 | STE | Restructuring: Consolidation Plan $55-70m pretax ($40-50m cash/$15-20m noncash) thru FY2030 | 8-K (Item 2.05), filed 2026-08-05 | PASS |
| 14 | STE | Kill criterion 1 / thesis consistency: FY27 EPS guide $11.10 floor reiterated, not cut | 8-K Ex-99.1, FY26 Q4 and Q1 FY27 | PASS |
| 15 | BALL | FY2025: comparable EPS $3.57(~14% growth, guided 12-15%); record FCF $956m | 8-K Ex-99.1, Q4/FY25, filed 2026-02-03 | PASS |
| 16 | BALL | FY2026 guide "10-plus percent"/FCF>$900m; reaffirmed Q1'26 and Q2'26 | 8-K Ex-99.1, Q4/FY25 and Q2 2026 | PASS |
| 17 | BALL | Leverage Dec-2025: total debt $7,012m; cash $1,212m; net debt $5,800m; EBITDA $2,044m; ~2.8x | 8-K Ex-99.1, Q4/FY25, leverage table | **MINOR** |
| 18 | BALL | Balance sheet 6/30/26: assets $20,110m; liabilities $14,344m; equity $5,746m; curr. LTD $649m | XBRL companyconcept, CIK0000009389 | PASS |
| 19 | BALL | CBP aluminum tariff-classification contingency (Sept-2025), unreserved, unquantified | FY2025 10-K, Note 22 | PASS |
| 20 | BALL | FY2025 capital returns $1.54bn ($1,321m buybacks + $220m dividends); H1'26 $222m | 8-K Ex-99.1, Q4/FY25 and Q2 2026 | PASS |
| 21 | BALL | Kill criterion 2 consistency: net debt/EBITDA 3.5x threshold vs. ~2.8x/~3.2x currently | Facts 17/18 above | PASS |

## 2. The MINORs, in full

### STE — Q1 FY2027 segment table: Healthcare-segment current-quarter revenue overstated

**Claim in dossier (STE.md §4):** "Healthcare revenue +8% ($1,051.4m vs $974.7m)."

**What the primary source says:** the 8-K Ex-99.1 segment-data table (three months ended 30-Jun-2026 vs 30-Jun-2025) reports Healthcare segment total revenue of **$1,048.3 million** for the current quarter (prior-year quarter $974.7m confirmed exact). The dossier's figure is $3.1 million (0.3%) too high. Implied YoY growth is actually ~7.6%, not the ~7.9% the stated figures would produce (both round to a similar "+8%" headline). Operating income for Healthcare ($260.2m vs $235.5m) and every AST/Life Sciences figure in the same table are exact.

**Why this matters little:** this is a small, immaterial dollar-figure slip in supporting segment detail, not a guidance, leverage, or kill-criterion number; it does not change the "all three segments grew both revenue and operating income" conclusion the dossier draws from it. This is the specific line `dossier_precheck.json` flagged for STE (line 52) as load-bearing, so it was checked directly against the earnings-release table rather than accepted on trust.

### BALL — FY2025 comparable EBITDA overstated by $3m in the leverage summary

**Claim in dossier (BALL.md §6):** "comparable EBITDA (TTM) $2,044m."

**What the primary source says:** Ball's own Q4/FY2025 leverage summary table states comparable EBITDA of **$2,041 million** for FY2025 — $3m (0.15%) lower than the dossier's figure. Total debt ($7,012m), cash ($1,212m) and net debt ($5,800m) in the same table all match the dossier exactly. The net debt/EBITDA ratio is unaffected at the precision reported (2.84x per the company's own table vs. the dossier's stated "≈2.8x"), and kill criterion 2's 3.5x threshold comparison is not impacted either way.

## 3. The FAILs, in full

None. No FAIL-severity discrepancies were found in this batch.

## 4. Thesis / kill-criterion-1 consistency check

- **EXC:** kill criterion 1 ("FY2026 adjusted operating EPS guidance is cut below the current $2.81-$2.91 range") is consistent with a confirmed introduce-then-affirm track record across all three releases checked (Q4/FY2025, Q1 2026, Q2 2026); no cut occurred. The one-line thesis (guided 5-7% near-top-end EPS growth through 2029, priced below management's own guidance even on a conservative cost-of-equity assumption) is directly supported by the primary sources, including the BGE rate-case terms and Q2 2026 debt-issuance detail, both confirmed exact.
- **STE:** kill criterion 1 ("any subsequent quarterly update that lowers FY2027 adjusted EPS guidance below the current $11.10 floor") remains consistent — the Q1 FY27 release explicitly reiterates the $11.10-$11.30 range even while revising capex/FCF guidance for a disclosed, growth-oriented reason (the new NC Center of Excellence), exactly as the dossier describes. The one MINOR finding (segment-revenue overstatement) does not touch this kill criterion or the thesis.
- **BALL:** kill criterion 2 ("net debt/comparable EBITDA exceeding 3.5x") and the underlying leverage claims are internally consistent with the filings at both the Dec-2025 company-disclosed figure (~2.8x) and the dossier's own clearly-flagged June-2026 approximation (~3.2x), both comfortably below the threshold. The one MINOR finding (EBITDA off by $3m) does not change this conclusion. FY2026 guidance ("10-plus percent" EPS growth, FCF >$900m) was independently confirmed reaffirmed at both Q1 and Q2 2026 with no cut.

## 5. One-line judgement on dossier reliability

This batch is clean at the level that matters: every guidance figure, debt/leverage headline number, rate-case term, litigation settlement date, and kill-criterion threshold checked across all three dossiers matched the primary source exactly, including entity-scope-sensitive figures flagged by the mechanical pre-check (EXC's Exelon-consolidated vs. subsidiary-registrant debt figures, BALL's consolidated balance-sheet lines) and a litigation-date claim STE's own author had explicitly flagged as unverified (EO settlement dates, now independently confirmed against STERIS's primary 8-Ks). The two MINOR findings are both small (<0.5%) overstatements in supporting detail — a segment-revenue figure and an EBITDA figure — that a diligent reader would not catch without re-pulling the exact table, and neither survives into a guidance range, leverage ratio, or kill-criterion comparison. As in prior batches, the general lesson holds: **segment-level and derived-metric tables are the cells most worth re-verifying against the filing's own printed table, even when the surrounding narrative and headline figures are exact.**
