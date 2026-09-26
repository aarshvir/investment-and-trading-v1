# DA10 — Adversarial data audit: dossier facts (CAH, COR, VEEV)

**As of:** 2026-09-26 · **Scope:** three current-holding dossiers — **CAH, COR, VEEV** — not previously checked by this auditor. 21 load-bearing facts checked (7/7/7 by ticker), selected for the claims most likely to break a thesis or a kill criterion if wrong: headline quarterly/annual figures, guidance track records, leverage and debt, opioid/litigation accruals and status, goodwill impairments, deal/settlement terms, and balance-sheet items. Special attention paid to consolidated vs. segment vs. subsidiary figures, non-calendar fiscal years (CAH FYE Jun-30, COR FYE Sep-30, VEEV FYE Jan-31), and GAAP vs. adjusted/non-GAAP figures. **Method:** primary sources only — SEC EDGAR 8-K Ex-99.1 earnings-release exhibits, 10-Q/10-K text and notes, R-file XBRL viewer exhibits, and data.sec.gov XBRL companyconcept pulls — fetched directly from `www.sec.gov`/`data.sec.gov` and cited below. Each dossier was read to its end; no appended "Correction" sections were found on any of the three. Each ticker's one-line thesis and first kill criterion were also checked for consistency with the underlying filings (section 4 below).

## Top-line result

**21 facts checked: 20 PASS, 0 MINOR, 1 FAIL, 0 UNVERIFIABLE.** Strict pass rate = 20/21 = **95.2%**. CAH and VEEV were clean across all seven facts checked each — every headline figure, segment number, balance-sheet item, guidance checkpoint, and litigation/settlement detail matched the primary source exactly. COR's one FAIL is confined to the revenue-growth column of its guidance-track-record table; the adjusted-EPS guidance column (the metric the thesis and kill criterion 1 actually depend on) is fully correct, and every other COR fact — including the trickier opioid-credit and OneOncology-remeasurement figures — checked out exactly.

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | CAH | FY26: revenue $254.2bn(+14%); non-GAAP op. earnings $3.6bn(+30%); GAAP EPS $7.23(+12%); non-GAAP EPS $11.26(+37%, ex-IEEPA $10.95/+33%) | 8-K Ex-99.1, Q4/FY26, filed 2026-08-11 | PASS |
| 2 | CAH | Segment FY26: Pharma rev $234.8bn(+15%)/profit $2,783m(+23%)/margin 1.19%; GMPD rev $12.7bn(+1%)/profit $258m(+91%)/margin 2.03%; Other rev $6.8bn(+26%)/profit $707m(+37%)/margin 10.41% | 8-K Ex-99.1, Q4/FY26 | PASS |
| 3 | CAH | Q3 FY26: GAAP EPS $1.69(-20%) on $184m Navista & ION goodwill impairment; non-GAAP EPS $3.17(+35%); guide raised to $10.70-$10.80 | 8-K Ex-99.1, Q3 FY26, filed 2026-04-30 | PASS |
| 4 | CAH | Non-GAAP EPS guide raised 4-for-4: $9.30-9.50→$9.65-9.85→$10.15-10.35→$10.70-10.80→actual $11.26; FY27 initial $12.40-12.60 | 8-K Ex-99.1, Q1/Q2/Q3 FY26 and Q4/FY26 | PASS |
| 5 | CAH | Opioid: $4.3bn accrued 6/30/26, paid through 2038; FY26 cash payments $417m incl. $366m NOSA installment | FY2026 10-K, Note 14 (R14.htm) | PASS |
| 6 | CAH | Balance sheet 6/30/26: total debt $8,886m; cash $4,856m; net debt≈$4.0bn; parent shareholders' deficit $(2,883)m | FY2026 10-K, Balance Sheet (R5.htm) | PASS |
| 7 | CAH | DOJ CID (Nov-2023, AKS/FCA, 2022 GPO/rheumatology-MSO deal) open; buybacks $1,358m/$765m FY26/FY25; Elliott agreement expired Q2 FY25 | FY2026 10-K Note 14; XBRL companyconcept | PASS |
| 8 | COR | FY25: revenue $321.3bn(+9.3%); GAAP EPS $7.96; adj. EPS $16.00(+16.3%) | 8-K Ex-99.1, Q4/FY25, filed 2025-11-05 | PASS |
| 9 | COR | Q4 FY25: GAAP EPS $(1.75) on $723.9m PharmaLex + $113.5m equity impairments; adj. EPS $3.84(+15.0%) | 8-K Ex-99.1, Q4/FY25 | PASS |
| 10 | COR | Q2 FY26: GAAP EPS $8.40 on $1.086bn OneOncology remeasurement gain + put-option extinguishment | 8-K Ex-99.1, Q2 FY26, filed 2026-05-06 | PASS |
| 11 | COR | Opioid: $4.2bn accrued 6/30/26 (down from $4.3bn 9/30/25), 13-yr payout, $396.2m next 12mo; Q3 FY26 $88.6m net credit | 10-Q, accn ...-26-000034 | PASS |
| 12 | COR | Leverage 6/30/26: total debt $11.72bn (up from $7.92bn 12/31/25); cash $2.82bn; net debt≈$8.9bn | 10-Q Balance Sheet (R2.htm); XBRL companyconcept | PASS |
| 13 | COR | Guidance table: adj. EPS raised/held every checkpoint; revenue guide "7-9%→reaffirmed→cut to 4-6%" | 8-K Ex-99.1, Q4/FY25, Q1/Q2/Q3 FY26 | **FAIL** |
| 14 | COR | Impairments: $418.0m PharmaLex FY24 + $723.9m FY25 + $249.5m FY26 (9mo, U.S. Consulting Services) | 8-K Ex-99.1, Q4/FY24 and Q3 FY26 | PASS |
| 15 | VEEV | FY26 (FYE 1/31/26): revenue $3,195.3M(+16%); GAAP EPS $5.44; non-GAAP EPS $8.10 | 8-K Ex-99.1, Q4/FY26, filed 2026-03-04 | PASS |
| 16 | VEEV | Guidance 4-for-4 raise: FY26 guide ~$7.93 (beat)→FY27 initial $3,585-3600M/~$8.85→raised $3,635-3645M/~$9.05→raised $3,682-3687M/~$9.21 | 8-K Ex-99.1, Q4/FY26, Q1/Q2 FY27 | PASS |
| 17 | VEEV | FQ2 FY27 (7/31/26): revenue $928.0M(+18%); subscription $766.8M(+16%); services $161.2M(+24%); GAAP EPS $1.66; non-GAAP EPS $2.35; margin 44.8% | 8-K Ex-99.1, Q2 FY27, filed 2026-08-26 | PASS |
| 18 | VEEV | Balance sheet 7/31/26: cash $1,812.0M; ST investments $5,430.9M; equity $7,431.4M; no debt | 10-Q Balance Sheet (R2.htm) | PASS |
| 19 | VEEV | IQVIA settled 13-Aug-2025, no damages either way, dismissed w/ prejudice; $30.6M FY26 charge = Veeva's own legal costs | Public settlement reporting; 8-K Ex-99.1 non-GAAP table | PASS |
| 20 | VEEV | SBC $136.8M in FQ2 FY27 (≈14.7% of revenue) | 8-K Ex-99.1, Q2 FY27 | PASS |
| 21 | VEEV | Kill criterion 1 consistency: revenue growth steady 16-18%, no deceleration (kill: <12% for 2 qtrs) | 8-K Ex-99.1 releases, FQ2 FY26–FQ2 FY27 | PASS |

*(21 facts total across three tickers: 7 each for CAH, COR and VEEV — see the JSON for the complete, separately-numbered list.)*

## 2. The FAIL, in full

### COR — guidance-track-record table: revenue-growth-guidance column is wrong on the initial guide and the Q1 FY26 checkpoint

**Claim in dossier (COR.md §5):** the guidance table states the initial FY2026 revenue-growth guide (Q4/FY2025 release, 2025-11-05) was **"7%–9%"**, and that Q1 FY26 (2026-02-04) **"reaffirmed"** that 7%–9% range unchanged, before it was cut to 4%–6% at Q3 FY26.

**What the primary sources actually say:** the Q4/FY2025 release's own "Fiscal Year 2026 Expectations" table states total-company **"Revenue: 5% to 7% growth"** — not 7%–9%. The Q1 FY26 release's own guidance table then shows **"Revenue: 7% to 9% growth"** — i.e., the revenue guide was *raised* from 5–7% to 7–9% at the Q1 checkpoint, not reaffirmed unchanged. (The adjusted-diluted-EPS column of the same table is correct: Q1 FY26 explicitly says the EPS range was "Reaffirmed at $17.45 to $17.75" while the revenue guide moved.)

**Why this matters:** the dossier's own §3 narrative ("FY2026 revenue-growth guidance was cut, not raised... from '7% to 9%' (Q1 FY26 release) to '4% to 6%' (Q3 FY26 release)") is directionally salvageable using only the Q1-to-Q3 comparison, but the guidance table itself misstates the initial-guide value and mischaracterizes the Q1 action as a hold when it was actually a raise. This does not touch kill criterion 1 (an adjusted-EPS-guidance cut, which never happened and is correctly described), but it is a real error in a table meant to be read literally.

## 3. The MINORs, in full

None. No MINOR-severity discrepancies were found in this batch — every other quantitative and qualitative claim checked across all three dossiers, including several multi-decimal and hard-to-reconcile figures (COR's $88.6m litigation net credit traced to the exact 10-Q income-statement line; CAH's parent-only vs. NCI-inclusive shareholders'-deficit lines; VEEV's $30,627 thousand litigation-settlement charge), matched the primary source exactly.

## 4. Thesis / kill-criterion-1 consistency check

- **CAH:** kill criterion 1 ("Non-GAAP diluted EPS guidance is cut... at any quarterly release") is consistent with the confirmed four-for-four raise streak in FY2026 and the FY2027 initial guide already above the prior year's run rate. The one-line thesis ("four-quarter, no-cuts, beat-and-raise guidance record") is directly supported by the primary sources.
- **COR:** kill criterion 1 ("Adjusted diluted EPS guidance is cut at any quarterly release") remains consistent — adjusted EPS guidance was never cut in any release checked (raised at Q2 and Q3, reaffirmed at Q1), despite the revenue-growth-guidance table error described in section 2 above, which affects a supporting narrative point but not the kill-criterion metric itself.
- **VEEV:** kill criterion 1 ("Total revenue growth falls below 12% YoY for two consecutive quarters, vs. the current steady 16-18%") is confirmed consistent — every quarter checked in this pass (FQ2 FY26 through FQ2 FY27) fell in a 16-18% band, comfortably clear of the threshold. The one-line thesis's "four consecutive quarterly guidance raises" claim is also confirmed exactly (section 1, row 16).

## 5. One-line judgement on dossier reliability

This is the cleanest batch of the audit series to date on a strict-PASS basis: CAH and VEEV had zero discrepancies across all seven facts checked each, including several claims that required cross-referencing multiple filings or resolving apparent inconsistencies between an earnings release's own two different phrasings of the same figure (COR's $88.6m opioid credit vs. a $102.0m sub-component mentioned elsewhere; CAH's parent-only vs. consolidated shareholders'-deficit lines) — in every such case, the dossier's specific cited figure held up once the underlying line item was traced precisely. The one FAIL (COR's revenue-growth-guidance column) is the opposite pattern from prior batches' derivation-artefact failures: rather than a bad recomputation from components, it looks like a same-quarter mix-up between the newly-issued-guide figure and a different comparison point, landing on the correct *shape* of the story (revenue guide down, EPS guide up) while getting two of the four specific numbers in the sequence wrong. As in DA6-DA9, the general lesson holds: **guidance-history tables that chain several releases' numbers together are the highest-risk cells in these dossiers and warrant re-verification against each release's own comparison language, not just its own current-quarter figures.**
