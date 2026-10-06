# DA19 — Adversarial data audit: dossier facts (RSG, LH)

**As of:** 2026-09-27 · **Scope:** two current dossiers — **RSG, LH**. 14 load-bearing facts checked (7/7 by ticker), selected for the claims most likely to break a thesis or a kill criterion if wrong: latest-quarter revenue/GAAP net income/diluted EPS with correct period labels, guidance figures verified verbatim against the cited release, consolidated vs segment figures, debt/leverage on the correct basis and date, litigation/regulatory items, and thesis/kill-criterion-1 consistency. Special attention paid to the four known error patterns named in the task: (1) latest-quarter figures actually being a prior-year or different-quarter column; (2) guidance figures verified to appear verbatim in the cited release; (3) consolidated vs segment figures; (4) debt on the wrong basis/date. `v4/outputs/dossier_precheck.json` (RSG: empty array; LH: 8 citation/guidance-unquoted/entity-scope flags, none numeric) and `v4/outputs/xbrl_crosstie.json` (RSG and LH: empty flags array for both) were read in full for both tickers — no numeric crosstie flags existed for either ticker this pass. **Method:** primary sources only — SEC EDGAR 8-K Ex-99.1 earnings-release exhibits, 10-Q/10-K full-text filings, and `data.sec.gov/api/xbrl/companyfacts` structured data — fetched directly with User-Agent `PersonalEquityResearch research-admin@personal-research.org` at ≤2 requests/second and cached locally under `C:\Users\user\eqv4\cache\DA19\`. Both dossiers were read to their end (no appended "Correction" sections found on either). Each ticker's one-line thesis and first kill criterion were checked for consistency with the underlying filings.

## Top-line result

**14 facts checked: 11 PASS, 2 MINOR/UNVERIFIABLE, 1 FAIL, 0 pure UNVERIFIABLE.** Strict pass rate = 11/14 = **78.6%**. RSG's dossier was very strong: every headline revenue/EPS/guidance/debt/litigation figure checked exactly against primary sources, with only one MINOR item (an untraceable parenthetical growth figure inside an otherwise-correct kill-criterion note). LH's dossier had one severe, load-bearing FAIL: the quarterly results table's "2Q'25" row is actually the true Q3 2025 quarter's data (revenue, operating income and GAAP EPS all one quarter out of place), mislabeled with a footnote that itself misdescribes the figure — exactly the wrong-quarter-column error pattern the task asked to stress-test — though every other LH fact checked (headline Q2'26 results, guidance raised twice running, balance sheet, litigation, cash flow, thesis/kill-criterion-1) passed cleanly.

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | RSG | Q2'26: revenue $4,430m(+4.6%); NI $566m; GAAP EPS $1.84 (vs $1.75) | 8-K Ex-99.1, accn 0001060391-26-000273 | PASS |
| 2 | RSG | FY2026 guidance: initial (Q4'25) then raised (Q2'26) on all 4 metrics | 8-K Ex-99.1, accns ...093 and ...273 | PASS |
| 3 | RSG | Net debt $13,962m at 6/30/26; net debt/adj. EBITDA ≈2.5x | XBRL companyfacts CIK0001060391 | PASS |
| 4 | RSG | No Item 103 environmental proceeding ≥$1m disclosed | 10-Q, accn 0001060391-26-000275 | PASS |
| 5 | RSG | Core price 5.7%/5.3% (Q1/Q2'26); dividend +7% to $0.670/qtr | 8-K Ex-99.1, accns ...210 and ...273 | PASS |
| 6 | RSG | Q4'25: revenue $4,136m(+2.2%); op. inc. $800m(19.3%); GAAP EPS $1.76 | 8-K Ex-99.1, accn 0001060391-26-000093 | PASS |
| 7 | RSG | Kill-crit-1: organic growth <2% two quarters — not triggered (1.5%/3.5% total-organic) | 8-K Ex-99.1, accns ...210 and ...273 | **MINOR** |
| 8 | LH | Q2'26: revenue $3,731.1m(+5.8%); GAAP EPS $3.64(+28.5%); adj. EPS $4.99(+14.9%) | 8-K Ex-99.1, accn 0000920148-26-000162 | PASS |
| 9 | LH | FY2026 guidance raised twice running (Q1'26 and Q2'26 releases) | 8-K Ex-99.1, accns 0000920148-26-000135 and -000162 | PASS |
| 10 | LH | Balance sheet 6/30/26: cash $141.8m, equity $8,606.8m, LT debt $5,857.6m (+$773m) | XBRL companyfacts CIK0000920148 | PASS |
| 11 | LH | Qui tam FCA suits + DOJ subpoena (6/27/2022, urine drug testing) | FY2025 10-K, accn 0000920148-26-000111 | PASS |
| 12 | LH | 1H'26 OCF $637.0m vs $639.1m; capex $252.6m vs $203.9m | XBRL companyfacts CIK0000920148 | PASS |
| 13 | LH | Results table "2Q'25" row: revenue $3,563.5m/op.inc $396.6m/EPS $3.12 | XBRL companyfacts CIK0000920148; Q2'25 and Q3'25 10-Qs | **FAIL** |
| 14 | LH | Kill-crit-1 consistency: guidance raised, not cut, at both recent releases | 8-K Ex-99.1, accns ...135 and ...162 | PASS |

## 2. The issues, in full

### LH — §4: results table "2Q'25" row is actually true Q3'25 data, one quarter out of place

**Dossier claim (LH.md §4):** table row "2Q'25" reports revenue $3,563.5m, operating income $396.6m, GAAP diluted EPS $3.12 (footnoted "9mo cum., not isolated"), and adjusted EPS $4.35.

**Primary source (SEC XBRL companyfacts, CIK0000920148, cross-checked against Labcorp's own Q2 2025 10-Q, accession 0000920148-25-000081, and Q3 2025 10-Q, accession 0000920148-25-000096):**
- **True Q2 2025** (Apr–Jun 2025, per the Q2'25 10-Q): revenue $3,527.3m, operating income $394.5m, diluted EPS $2.84 — **entirely absent from the dossier's table**, even though this is exactly the prior-year comparator the dossier's own Q2'26 row and narrative correctly cite elsewhere ("$3.64 vs $2.84, +28.5%").
- **True Q3 2025** (Jul–Sep 2025, per the Q3'25 10-Q, an isolated quarterly figure, not a 9-month cumulative one): revenue $3,563.5m, operating income $396.6m, diluted EPS $3.12 — **this is the data the dossier's table mislabels "2Q'25."**

**Why it matters:** this is exactly the wrong-quarter-column error pattern the task instructions asked to test explicitly. The dossier's own footnote compounds the error by calling the $3.12 EPS figure "9mo cum., not isolated" — it is in fact the true isolated Q3'25 quarterly EPS, not a 9-month cumulative number (the correct 9-month-cumulative EPS through Q3'25 is $8.48, which the dossier does show, correctly, in the adjacent "3Q'25" row). The row's adjusted-EPS entry ($4.35) is, separately, the correct true-Q2'25 figure — so the row as constructed mixes data from two different quarters under a single label. This does not undermine the dossier's headline Q2'26 YoY growth story (independently re-verified correct against the primary press release) but the table and footnote should be corrected before reuse: relabel $3,563.5m/$396.6m/$3.12 as "3Q'25 (isolated)," insert a true "2Q'25" row ($3,527.3m/$394.5m/$2.84), and fix the footnote.

### RSG — §9: kill-criterion-1 parenthetical growth figures not traceable to the cited primary source

**Dossier claim (RSG.md §9):** kill criterion 1 note reads "(was +5.2%/+4.4% related-business growth in Q1/Q2'26 — actually core price; total-business organic was 1.5%/3.5%)."

**Primary source (RSG Q1 2026 and Q2 2026 earnings releases, 8-K Ex-99.1, accessions 0001060391-26-000210 and 0001060391-26-000273):** the "1.5%/3.5% total-business organic" figure is correctly and exactly derivable (total revenue growth 2.6%/4.6% minus the ~1.1pp acquisition contribution disclosed in both releases = 1.5%/3.5%). However, no combination of the figures actually disclosed in either release — core price on related-business revenue (6.8%/6.4%), average yield (4.1%/4.0%), or volume (−1.0%/−1.9%) — produces "5.2%" or "4.4%" for either quarter.

**Why it matters:** the kill-criterion conclusion itself (organic growth comfortably above the 2% floor, not triggered) is correct and independently confirmed, so this does not change the INCLUDE call. But the specific 5.2%/4.4% parenthetical figures are unverifiable against the cited sources and should be re-sourced or dropped before reuse. Graded MINOR rather than FAIL because it is a supplementary aside inside an otherwise-verified kill-criterion line, not a headline revenue/EPS/guidance figure.

## 3. Thesis / kill-criterion-1 consistency checks

- **RSG:** thesis (durable oligopolistic pricing power; price implies 10-year FCF growth modestly below base case) and kill criterion 1 (organic related-business revenue growth <2% for two consecutive quarters) are consistent with the primary sources — organic growth (however measured) is running well above the 2% floor and guidance has been raised, not cut, at the most recent release. No contradiction found; only the MINOR sourcing gap noted above.
- **LH:** thesis (duopoly lab franchise compounding revenue with margin expansion; guidance raised two quarters running) is independently confirmed true — both the Q1'26 and Q2'26 releases are titled "...Raises Full Year 2026 Guidance" with genuine Previous-vs-Updated increases. Kill criterion 1 (full-year adjusted EPS guidance cut at either of the next two releases) is confirmed not triggered. The one FAIL found (§4 results table mislabeling) is a supporting-table data-quality issue, not a thesis or kill-criterion inconsistency.

## 4. Scope notes and limitations

- `dossier_precheck.json` carried an empty flag array for RSG and eight non-numeric flags (citation/guidance-unquoted/entity-scope type) for LH; all LH-flagged lines were read and are addressed by the facts above (the guidance and cash/debt items LH's own precheck flagged as "unquoted" or "entity scope" are independently confirmed correct in facts 9, 10 and 12).
- `xbrl_crosstie.json` carried no numeric flags for either ticker this pass (empty flags arrays for both RSG and LH).
- RSG's SBC line, insider Form 4 pattern, and rating-agency figures, already self-flagged by the dossier as unconfirmed/unverified gaps, were not independently re-verified this pass (time-boxed to the seven selected facts per ticker); they remain open items.
- LH's cash/debt swing explanation (likely a debt-funded acquisition or buyback, per the dossier's own hedge) was not independently traced to a specific named transaction this pass; the balance-sheet figures themselves are confirmed exact, but the underlying cause of the move remains an open item as the dossier itself flags.
- This is research support, not investment advice, and is not personalized for any individual's circumstances.
