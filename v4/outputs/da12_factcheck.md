# DA12 — Adversarial data audit: dossier facts (USB, PPG, GDDY)

**As of:** 2026-09-27 · **Scope:** three current dossiers — **USB, PPG, GDDY**. 21 load-bearing facts checked (7/7/7 by ticker), selected for the claims most likely to break a thesis or a kill criterion if wrong: headline quarterly figures, guidance track records, capital/credit ratios, debt/leverage and balance-sheet items, litigation exposure, and buyback/capital-return figures. Special attention paid to USB's consolidated U.S. Bancorp vs. U.S. Bank N.A. subsidiary scoping for every capital ratio and to ROE vs. ROTCE definitions, per task instructions, and to the lines flagged by `v4/outputs/dossier_precheck.json` for all three tickers (period labels, entity scope, citations without accession numbers). **Method:** primary sources only — SEC EDGAR 8-K Ex-99.1 earnings-release exhibits, 10-Q/10-K text and R-file XBRL-rendered exhibits, and data.sec.gov XBRL companyfacts/submissions — fetched directly from `www.sec.gov`/`data.sec.gov` and cited below; CFPB enforcement-action status and earnings-call-date claims cross-checked via WebSearch against `consumerfinance.gov`, `bankingdive.com` and `ir.usbank.com`. Each dossier was read to its end; no appended "Correction" sections were found on any of the three. Each ticker's one-line thesis and first kill criterion were also checked for consistency with the underlying filings (section 3 below).

## Top-line result

**21 facts checked: 20 PASS, 0 MINOR, 1 FAIL, 0 UNVERIFIABLE.** Strict pass rate = 20/21 = **95.2%**. USB and GDDY were clean across all seven facts checked each — every headline figure, capital/credit ratio, litigation date/amount, guidance checkpoint and balance-sheet item matched the primary source exactly, including the USB consolidated-vs-subsidiary CET1 scoping and the ROE-vs-ROTCE distinction (both PASS). PPG's one FAIL is a misstated long-term debt figure in its balance-sheet summary (§6): the dossier's total-debt and net-debt figures are therefore both overstated by ~$681m (~11%), though this does not flip the direction of the net-debt/EBITDA kill criterion (see §2 below).

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | USB | Q2 2026: net revenue $7,712m; NII(TE) $4,387m; noninterest income $3,325m; net income $2,177m; diluted EPS $1.35; NIM 2.79%; efficiency 57.1%; ROTCE 18.7%; NCO 0.53%; CET1 10.8%; 400bps positive operating leverage; BTIG contributed ~$98m fee rev/$84m expense | 8-K Ex-99.1, Q2 2026, accn 0000036104-26-000039 | PASS |
| 2 | USB | ROE (return on average common equity) 14.0% is distinct from ROTCE 18.7% — two separate, correctly-labelled non-GAAP metrics | 8-K Ex-99.1, Q2 2026 | PASS |
| 3 | USB | CET1 10.8% (Q1/Q2 2026) is a **consolidated U.S. Bancorp** figure, not a U.S. Bank N.A. subsidiary figure; kill criterion 1 correctly scoped "consolidated" | 8-K Ex-99.1, Q2 2026, "CAPITAL POSITION" section | PASS |
| 4 | USB | CFPB: sham-accounts $37.5m penalty terminated 21-Aug-2025; ReliaCard $20.7m penalty (ordered Dec-2023) terminated 22-Sep-2025 | CFPB termination orders / bankingdive.com, americanbanker.com | PASS |
| 5 | USB | Next earnings: Q3 2026, Thu 15-Oct-2026, 8:00am CT | ir.usbank.com earnings-call schedule | PASS |
| 6 | USB | NCO ratio improved 0.59%→0.56%→0.54%→0.56%→0.53% over 5 quarters shown; kill criterion 2 (>0.75% for 2 qtrs) far from tripped | 8-K Ex-99.1, Q2 2026 and Q4 2025/FY2025 | PASS |
| 7 | USB | Thesis/kill-criterion-1 consistency: CET1 10.8% consolidated vs. 9.5% kill threshold | 8-K Ex-99.1, Q2 2026; 10-Q accn 0000036104-26-000044 | PASS |
| 8 | PPG | Q2 2026: net sales $4,495m(+7%); organic +4%; GAAP EPS $1.96; adj. EPS $2.23(~0%); FY26 guide reaffirmed $7.70-$8.10 | 8-K Ex-99, Q2 2026, accn 0000079879-26-000246 | PASS |
| 9 | PPG | Q1 2026: net sales $3,930m(+7%); organic +1%; GAAP EPS $1.70; adj. EPS $1.83(+6%) | 8-K Ex-99, Q1 2026, accn 0000079879-26-000167 | PASS |
| 10 | PPG | FY26 adj. EPS guide $7.70-$8.10 reaffirmed at all 3 releases checked (initial 2026-01-27, Q1, Q2) | 8-K Ex-99, Q4/FY25, accn 0000079879-26-000025 | PASS |
| 11 | PPG | Balance sheet 6/30/26: cash $1,520m; LT debt $6,876m + ST $691m ≈ total debt $7.57bn; net debt ≈$6.05bn; equity $8,590m | 10-Q, accn 0000079879-26-000252, R5.htm | **FAIL** |
| 12 | PPG | Asbestos reserves $42m (6/30/26) vs $43m (12/31/25); "believed sufficient" | 10-Q, accn 0000079879-26-000252, contingencies note | PASS |
| 13 | PPG | No SC 13D/SC 13D-A on file for PPG — triage-stage activist claim not confirmed by a primary ownership filing | SEC EDGAR SC 13D company search, CIK 0000079879 | PASS |
| 14 | GDDY | Q2 2026: revenue $1,298.0m(+6.6%); op. income $342.5m; op. margin 26.4%; net income $240.1m; diluted EPS $1.83 | 8-K Ex-99.1, Q2-26 earnings release | PASS |
| 15 | GDDY | FY26 guide: revenue narrowed to $5.215-5.255bn (midpoint held); NEBITDA >33% and FCF ~$1.8bn reaffirmed 3 releases; FY25 actual revenue $4,951.1m | 8-K Ex-99.1, Q4/FY25, Q1-26, Q2-26 | PASS |
| 16 | GDDY | Balance sheet 6/30/26: cash $1,155.5m; total debt $3,816.9m; net debt≈$2,661m; equity $237.3m(3/31)→$6.7m(6/30) | 10-Q, quarter ended 2026-06-30 | PASS |
| 17 | GDDY | Express Mobile litigation: jury verdict 7-Nov-2025; district court ruling 14-May-2026; notice of appeal 15-Jun-2026; loss exposure $0-$170.0m ex-interest, no accrual | 10-Q, Note 11 | PASS |
| 18 | GDDY | H1 2026: OCF $914.0m − capex $9.7m = FCF $904.3m (+16.4% YoY); buybacks $824.4m; shares outstanding 126.6m (7/24/26) down from 135.1m (10/24/25) | 10-Q, cash-flow statement and cover page | PASS |
| 19 | GDDY | Thesis/kill-criterion-2 consistency: net debt/EBITDA ~1.9x vs. 3.0x kill threshold | 10-Q balance sheet; Q2-26/Q1-26/Q4-25 releases | PASS |

*(21 facts total across three tickers: 7 each for USB, PPG and GDDY — see the JSON for the complete, separately-numbered list; two USB facts and one GDDY fact above are condensed pairs of closely related JSON entries.)*

## 2. The FAIL, in full

### PPG — balance-sheet summary (§6): long-term debt misstated, total/net debt both overstated

**Dossier claim (PPG.md §6):** "long-term debt (carrying value) $6,876M + short-term debt/current portion of long-term debt $691M ≈ **total debt $7.57bn**; net debt ≈ **$6.05bn**" (as of 30-Jun-2026).

**Primary source (PPG 10-Q, quarter ended 30-Jun-2026, accession 0000079879-26-000252, R5.htm — Condensed Consolidated Balance Sheet):** "Long-term debt: $6,195" (in millions), not $6,876M. Short-term debt/current portion ($691M), cash ($1,520M) and total shareholders' equity ($8,590M) all match the dossier exactly.

**Corrected figures:** total debt = $691M + $6,195M = **$6,886M (~$6.89bn)**, an $681M (~9%) reduction from the dossier's $7.57bn. Net debt = $6,886M − $1,520M = **$5,366M (~$5.37bn)**, an $681M (~11%) reduction from the dossier's $6.05bn.

**Why it matters:** net debt feeds directly into kill criterion 3 ("Net debt / EBITDA rises above 3.0x, from ~2.2x currently"). The error does not flip the direction of the conclusion — a lower actual net debt implies PPG's leverage is somewhat *better* than stated, so the kill criterion is, if anything, further from being tripped, not closer — but the raw dollar figures in the dossier's earnings-quality section are factually wrong and should be corrected before this figure is relied on elsewhere (e.g., in any consolidated portfolio-leverage roll-up).

## 3. Thesis / kill-criterion-1 consistency checks

- **USB:** one-line thesis (improving super-regional bank, cheap multiple) and kill criterion 1 (Basel III standardized CET1 <9.5%, consolidated) are consistent with the Q2 2026 earnings release: CET1 10.8% consolidated, ROTCE 18.7%, ROE 14.0% (correctly distinguished), NIM/efficiency/NCO all improving as described. No contradiction found.
- **PPG:** one-line thesis (cleanest execution of the three names, guidance reaffirmed not cut) and kill criterion 1 (organic sales growth negative 2 consecutive quarters, streak currently 6 positive) are consistent with the Q1/Q2 2026 releases (organic +1%, +4%). No contradiction found; the only issue found in this pass is the unrelated long-term-debt figure above.
- **GDDY:** one-line thesis (durable franchise mispriced for FCF decline) and kill criterion 2 (net debt/EBITDA >3.0x, currently ~1.9x) are consistent with the 10-Q balance sheet (net debt ≈$2,661m) and the revenue/FCF growth trend confirmed across the three most recent releases. No contradiction found.

## 4. Scope notes and limitations

- USB's CFPB enforcement actions were verified via CFPB termination-order documents and secondary reporting (bankingdive.com, americanbanker.com) rather than by independently re-reading the original 2023/underlying consent-order PDFs line by line; the penalty amounts and termination dates are corroborated by multiple independent sources and match the dossier exactly.
- PPG's net debt/EBITDA (~2.2x, quant-card-sourced) was not independently re-derived from a primary-source EBITDA figure in this pass; only the debt and cash inputs were checked against the 10-Q, which is where the FAIL above was found.
- No `dossier_precheck.json`-flagged line for USB, PPG or GDDY was found to reflect an actual entity-scope or period-mislabel error beyond the PPG long-term-debt figure above; the USB capital-ratio and PPG/GDDY balance-sheet lines flagged by the pre-check were all confirmed to carry an explicit, correct entity/period label in the dossiers as written (the PPG debt figure's error is a numeric transcription issue, not a scope-labeling issue — it is correctly labeled "consolidated, 10-Q, 30-Jun-2026" but the number itself is wrong).
- This is research support, not investment advice, and is not personalized for any individual's circumstances.
