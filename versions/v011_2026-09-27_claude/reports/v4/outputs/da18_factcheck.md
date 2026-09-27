# DA18 — Adversarial data audit: dossier facts (WEC, RMD, MCK, PTC)

**As of:** 2026-09-27 · **Scope:** four current dossiers — **WEC, RMD, MCK, PTC**. 24 load-bearing facts checked (6/6 by ticker), selected for the claims most likely to break a thesis or a kill criterion if wrong: latest-quarter revenue/GAAP net income/diluted EPS with correct period labels, guidance changes, debt/leverage, litigation/regulatory items, and thesis/kill-criterion-1 consistency. Special attention paid to the three known error patterns named in the task: (1) latest-quarter figures actually being the prior-year column or another quarter — tested explicitly for RMD (FY ends June), MCK (FY ends March) and PTC (FY ends September); (2) consolidated vs segment/subsidiary figures — tested for WEC as a multi-subsidiary utility holding company; (3) debt figures on the wrong basis/date — tested for all four. `v4/outputs/dossier_precheck.json` and `v4/outputs/xbrl_crosstie.json` were read in full for all four tickers; the numeric flags they carried (RMD total-debt sum-of-two-tags, gap 62.8%; PTC net income, gap up to 699.8%) were independently re-derived from `data.sec.gov` XBRL companyfacts — the RMD flag resolved as a benign false positive, while the **PTC flag resolved as a genuine, severe fact error** (see below). **Method:** primary sources only — SEC EDGAR 8-K Ex-99.1 earnings-release exhibits, 10-Q/10-K XBRL structured data via `data.sec.gov/api/xbrl/companyfacts`, and an FDA device-recall record — fetched directly with a compliant User-Agent header at ≤2 requests/second and cached locally under `C:\Users\user\eqv4\cache\DA18\`. All four dossiers were read to their end (no appended "Correction" sections found on any). Each ticker's one-line thesis and first kill criterion were checked for consistency with the underlying filings.

## Top-line result

**24 facts checked: 20 PASS, 1 MINOR, 3 FAIL, 0 UNVERIFIABLE.** Strict pass rate = 20/24 = **83.3%**. MCK was clean across all six facts checked (this dossier's own math and sourcing are excellent, including a subtle GAAP-vs-adjusted reconciliation that checked out to the dollar). WEC had one trivial arithmetic slip and otherwise passed cleanly, including resolving its own self-flagged "data gap" on the data-center pipeline via a primary-source 8-K the dossier hadn't located. RMD and PTC each had one severe, load-bearing FAIL: RMD's cited FY2027 guidance figures do not exist in the primary source it names (and the dossier misses a material MatrixCare divestiture disclosed in that same release); PTC's results table has its two most recent quarters shifted one fiscal quarter out of place — exactly the non-calendar-fiscal-year trap the task asked to stress-test.

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | WEC | Q2 2026: revenue $2,062.1M(+2.6%); GAAP EPS $0.91(+$0.15 YoY); 2026 guidance $5.51-$5.61 reaffirmed | 8-K Ex-99.1, accn 0000783325-26-000080 | PASS |
| 2 | WEC | FY2025 diluted EPS $4.81 (vs FY2024 $4.83) | XBRL companyfacts CIK0000783325 | PASS |
| 3 | WEC | Total debt $22,564M at 6/30/26 (3-tag sum) | XBRL companyfacts CIK0000783325 | PASS |
| 4 | WEC | Data-center pipeline (Microsoft $20.3B/2.6GW; Vantage 1.3GW/3.5GW; $37.5B capital plan; 7-8% EPS growth) | 8-K Ex-99.1 investor deck, accn 0000783325-26-000099 | PASS |
| 5 | WEC | Q4 2025 revenue derived = 2,536.6 (=9,800.1-7,263.0) | XBRL companyfacts CIK0000783325 | **MINOR** |
| 6 | WEC | Kill-crit-1 consistency: guidance reaffirmed, not cut | 8-K Ex-99.1, accn 0000783325-26-000080 | PASS |
| 7 | RMD | Quarterly table Q3FY25-FY2026 + derived Q4 figures | XBRL companyfacts CIK0000943819 | PASS |
| 8 | RMD | FY2027 guidance $5.75-5.85B rev / $12.00-12.25 non-GAAP EPS | 8-K Ex-99.1, accn 0001193125-26-337962 | **FAIL** |
| 9 | RMD | Total debt $659.4M (sum of two XBRL tags) | XBRL companyfacts CIK0000943819 | PASS |
| 10 | RMD | "9-month" buybacks $700.0M / dividends $2.40/sh, cited to Q3 FY26 10-Q | XBRL companyfacts CIK0000943819 | **FAIL** |
| 11 | RMD | Astral ventilator FDA Class I recall details | FDA record id 221232 | PASS |
| 12 | RMD | Kill-crit-3 gross margin 61.1% | XBRL companyfacts CIK0000943819 | PASS |
| 13 | MCK | FY2026/Q3FY26/Q1FY27 revenue, NI, EPS (incl. -17.6% GAAP EPS YoY) | XBRL companyfacts CIK0000927653 | PASS |
| 14 | MCK | GAAP-vs-adjusted reconciliation ($3.85 txn costs, $293M/$81M NCI, $136M restructuring, $0.41 amort.) | 8-K Ex-99.1, accn 0000927653-26-000232 | PASS |
| 15 | MCK | FY2027 guidance raised $44.20-45.00 (from $43.80-44.60) | 8-K Ex-99.1, accn 0000927653-26-000232 | PASS |
| 16 | MCK | Balance sheet 6/30/26: cash $5.164B, LT debt+leases $8.432B, equity -$4.240B | XBRL companyfacts CIK0000927653 | PASS |
| 17 | MCK | Opioid liability $5.692B ($601M current + $5.091B LT) | FY2026 10-K, accn 0000927653-26-000069 | PASS |
| 18 | MCK | Gross debt/EBITDA 1.4x / 0.65x cash-adjusted | XBRL companyfacts CIK0000927653 | PASS |
| 19 | PTC | Results table: "Q1'26" row ($774.3M/$4.98 EPS) and "Q2'26" row ($600.0M/$1.03 EPS) | XBRL companyfacts CIK0000857005; 8-K Ex-99.1 accn 0001193125-26-323617 | **FAIL** |
| 20 | PTC | ARR: cc +9.1% ($2,448M vs $2,245M); as-reported +7% ($2,412M vs $2,256M) | 8-K Ex-99.1, accn 0001193125-26-323617 | PASS |
| 21 | PTC | FY'26 guidance raises (ARR, revenue, GAAP/non-GAAP EPS) | 8-K Ex-99.1, accn 0001193125-26-323617 | PASS |
| 22 | PTC | Balance sheet 6/30/26: cash $351.5M, LT debt $1,398.2M, equity $3,469.7M | XBRL companyfacts CIK0000857005 | PASS |
| 23 | PTC | ~$525M buybacks in Q3'26 | 8-K Ex-99.1, accn 0001193125-26-323617 | PASS |
| 24 | PTC | Bear case 3: FY'26 as-reported revenue guide -2% to 0% | 8-K Ex-99.1, accn 0001193125-26-323617 | PASS |

## 2. The three FAILs, in full

### RMD — §5: fabricated/misattributed FY2027 guidance figures, and a missed material divestiture

**Dossier claim (RMD.md §5):** "company issued FY2027 guidance of $5.75–$5.85B revenue and $12.00–$12.25 non-GAAP diluted EPS," sourced to the 6 Aug 2026 Q4 FY2026 earnings release.

**Primary source (ResMed Q4/FY2026 earnings release, 8-K Ex-99.1, accession 0001193125-26-337962, filed 2026-08-06 — the same document the dossier itself cites):** contains **no FY2027 revenue or EPS guidance range at all**. The only FY2027 guidance given is a capital-return target: "Guiding to more than $1.85 billion in capital to be returned to shareholders through share repurchases and dividends during FY 2027." A full-text search of the release for "5.75", "5.85", "12.00" and "12.25" returns zero matches.

**A second, related miss in the same document:** the release discloses "Announced agreement to sell MatrixCare business; transaction expected to close during the first quarter of Resmed's fiscal year 2027" — a material divestiture of exactly the care-management/SaaS business the dossier's bull case #2 cites as a continuing growth driver ("Software/SaaS (care-management)... growth continue to outgrow the core"). This is not mentioned anywhere in the dossier.

**Why it matters:** this is a load-bearing guidance line feeding directly into kill criterion 5 ("FY2027 guidance... is cut at any subsequent quarterly update") and the valuation section's forward growth assumptions. As currently written, the dossier is checking a kill criterion against numbers that do not appear in its own cited source. Recommend re-verifying against RMD's Q1 FY2027 release (expected ~29 Oct 2026) and correcting the bull case for the MatrixCare divestiture before this dossier is relied on further.

### RMD — §6: nine-month vs full-year mislabeling on buybacks and dividends

**Dossier claim (RMD.md §6):** "FY2026 9-month repurchases $700.0M (10-Q, accession 0000943819-26-000025, filed 2026-05-01)" and "$2.40/share declared over 9 months of FY2026 (10-Q, accession 0000943819-26-000025, filed 2026-05-01)."

**Primary source (SEC XBRL companyfacts, CIK0000943819):** the nine-month period actually covered by the cited 10-Q (2025-07-01 through 2026-03-31) shows repurchases of **$500.0M** and dividends declared of **$1.80/share**. The **$700.0M** and **$2.40/share** figures the dossier attributes to that 10-Q are in fact the **full twelve-month FY2026** totals, reported in a different filing (the FY2026 10-K, accession 0000943819-26-000047).

**Why it matters:** a $200M (40%) overstatement on the buyback figure and a $0.60/share (33%) overstatement on the dividend figure, both mislabeled as nine-month numbers when they are annual numbers. This does not trip any specific kill criterion, but it is exactly the wrong-period error pattern the task asked to hunt for, applied to a capital-returns line rather than revenue/EPS.

### PTC — §4: results table shifted one fiscal quarter, exactly the non-calendar-year trap flagged for this ticker

**Dossier claim (PTC.md §4):** table row "Q1'26 (Oct–Dec'24)" [sic] reports revenue $774.3M, GAAP operating income $295.8M, GAAP diluted EPS $4.98 (including a $463M divestiture gain); the next row "Q2'26 (Jan–Mar'26)" reports revenue $600.0M (down 7% YoY), GAAP operating income $166.5M, GAAP diluted EPS $1.03, non-GAAP EPS $1.58.

**Primary source (SEC XBRL companyfacts, CIK0000857005, cross-checked against PTC's own Q3 FY2026 earnings release, 8-K Ex-99.1, accession 0001193125-26-323617, filed 2026-07-29 — headlined "Three Months Ended June 30, 2026" and "Full Fiscal Year 2026 and Fourth Fiscal Quarter Guidance"):**
- **True Q1 FY2026** (Oct 1–Dec 31, 2025): revenue $685.8M, operating income $221.1M, diluted EPS $1.39 — **entirely absent from the dossier's table.**
- **True Q2 FY2026** (Jan 1–Mar 31, 2026): revenue $774.3M, operating income $295.8M, net income $590.7M, diluted EPS $4.98 — **this is the data the dossier's table mislabels "Q1'26."**
- **True Q3 FY2026** (Apr 1–Jun 30, 2026 — the actual subject of the earnings release the dossier itself cites as the "Q3'26 press release"): revenue $600.0M, operating income $166.5M, net income $118.8M, diluted EPS $1.03, non-GAAP EPS $1.58 — **this is the data the dossier's table mislabels "Q2'26."**

This also explains the `xbrl_crosstie.json` auto-flag (net income: dossier $590.7M vs "nearest_xbrl" $118.8M, gap 397.3%) — both figures are real, correctly-reported XBRL values; they are simply attached to the wrong quarter labels in the dossier's table, one quarter apart.

**Why it happened / why it matters:** PTC's fiscal year ends in September, so "Q1" is Oct–Dec and the current-year column can easily be misread against an adjacent quarter when working from a multi-quarter press release. The dossier's own narrative *correctly* states the Kepware/ThingWorx divestiture closed "March 13, 2026 (fiscal Q2'26)" (§4, note), which is internally inconsistent with placing the associated $463M gain in a row the table calls "Q1'26" — the dossier contradicts itself. This does **not** undermine the ARR-based bull thesis (independently verified correct — the constant-currency ARR growth of 9.1% and the FY'26 guidance raises are both confirmed exactly against the primary source) but the quarterly results table and its "Q1'26"/"Q2'26" narrative discussion should be relabelled one fiscal quarter forward before reuse, and the missing true Q1 FY2026 quarter should be added.

## 3. Thesis / kill-criterion-1 consistency checks

- **WEC:** thesis (data-center large-load pipeline layered on rate-base growth) and kill criterion 1 (guidance cut) are consistent with the primary source — guidance was reaffirmed, not cut, and the data-center pipeline figures the dossier flagged as an unconfirmed secondary-source data gap are in fact confirmed by WEC's own September 2026 investor-materials 8-K. No contradiction found.
- **RMD:** thesis (priced for less growth than delivered; Astral recall is a sized, quantified item) holds up on the recall side (confirmed via FDA record) but is undermined on the guidance side by FAIL #1 above — the specific FY2027 guidance range cited to test kill criterion 5 does not exist in the cited source.
- **MCK:** thesis (reverse-DCF implies growth below guide, even after pricing in the separation and opioid liability) and every underlying figure checked (GAAP/adjusted reconciliation, guidance raise, balance sheet, opioid liability, leverage) are all confirmed exactly. No contradiction found; this is the strongest dossier of the four on data accuracy.
- **PTC:** thesis (FY26 "revenue decline" is a divestiture-accounting artifact, not organic decay; ARR growth is healthy) is independently confirmed correct via the primary source, but the supporting quarterly table used to illustrate it (FAIL #3 above) has a one-quarter labeling shift that should be fixed.

## 4. Scope notes and limitations

- `dossier_precheck.json` carried only citation-type flags (not numeric-value flags) for WEC, RMD and MCK, and an empty array for PTC; all citation-flagged lines were read and are addressed in the facts above. `xbrl_crosstie.json` carried one numeric flag each for RMD and PTC (both addressed above) and empty flag arrays for WEC and MCK.
- WEC's rating-agency figures (A-/Baa1, FFO/debt targets) and D&A/EBITDA approximation, already self-flagged by the dossier as unconfirmed secondary-sourced data gaps, were not independently re-verified this pass (time-boxed to the six selected facts per ticker); they remain open items.
- RMD's SBC line and insider Form 4 pattern, both self-flagged gaps, were not re-derived this pass.
- MCK's TTM EBITDA figure (used in the 1.4x/0.65x leverage ratios) is sourced internally (d4) rather than independently re-derived from the income statement this pass; the ratios reconcile exactly given that EBITDA figure, but the EBITDA figure itself was not independently rebuilt line-by-line.
- PTC's SBC line and insider-selling pattern, both self-flagged gaps, were not re-derived this pass.
- This is research support, not investment advice, and is not personalized for any individual's circumstances.
