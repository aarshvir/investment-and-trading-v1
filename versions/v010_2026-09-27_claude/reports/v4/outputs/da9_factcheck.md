# DA9 — Adversarial data audit: dossier facts (MA, AXP, MSCI)

**As of:** 2026-09-26 · **Scope:** three current-holding dossiers — **MA, AXP, MSCI** — not previously checked by this auditor. 21 load-bearing facts checked (7/7/7 by ticker), selected for the claims most likely to break a thesis or a kill criterion if wrong: headline quarterly figures, guidance track records, capital/credit ratios, deal terms/dates, litigation status, and capital-return figures. **Method:** primary sources only — SEC EDGAR 10-Q/10-K text and notes, 8-K Ex-99.1/Ex-99.2 earnings-release exhibits, and data.sec.gov XBRL companyconcept pulls — fetched directly from `www.sec.gov`/`data.sec.gov` (User-Agent `PersonalEquityResearch research-admin@personal-research.org`) and cited below. Each dossier was read to its end; no appended "Correction" sections were found on any of the three. Each ticker's one-line thesis and first kill criterion were also checked for consistency with the underlying filings (section 4 below).

## Top-line result

**21 facts checked: 20 PASS, 1 MINOR, 0 FAIL, 0 UNVERIFIABLE.** Strict pass rate (PASS only) = 20/21 = **95.2%** (100% counting the MINOR as acceptable). This is the cleanest batch of the DA6–DA9 series to date: MA and AXP had zero discrepancies across all seven facts checked each — every headline figure, balance-sheet number, guidance range, litigation detail, and deal term matched the primary source exactly, several to the dollar or the exact percentage point. MSCI had six exact matches and one MINOR — a temporal-labeling slip (calling a two-quarters-ago figure "a year ago"), not a wrong number.

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | MA | Q2'26: revenue $9,277m(+14.1%); op. income $5,587m; op. margin 60.2%; GAAP EPS $4.97; adj. EPS $5.04 | 10-Q + 8-K Ex-99.1, filed 2026-07-30 | PASS |
| 2 | MA | Balance sheet: cash $11,291m(was $10,566m); LT debt $22,184m(was $18,251m), +$3.9bn | 10-Q, Consolidated Balance Sheet | PASS |
| 3 | MA | BVNK acquisition: $1.5bn + up to $300m contingent, close before end Q3'26 | 10-Q, Note 2 Acquisitions | PASS |
| 4 | MA | Accrued litigation reserve $800m(FY25)→$296m(2Q26) | 10-Q, Balance Sheet | PASS |
| 5 | MA | Litigation: Apr-2026 US merchant suit re Damages Class Settlement release (claims since Jan-2019); Portugal ≈€0.4bn(≈$0.5bn) | 10-Q, Legal Proceedings note | PASS |
| 6 | MA | Capital return 2Q26: 9.8M sh./$4.9bn buyback; $771m dividends; $7.8bn remaining auth. (as of 7/27/26) | 8-K Ex-99.1 + 10-Q | PASS |
| 7 | MA | Diluted shares 925M(3Q24)→883M(2Q26), ≈−4.5% | XBRL, WeightedAvgDilutedShares | PASS |
| 8 | AXP | Q2'26: revenue $19,637m(+10%); NI $3,110m; diluted EPS $4.53 | 10-Q, filed 2026-07-24 | PASS |
| 9 | AXP | FY25: revenue $72,229m(+10%); NI $10,833m(+7%); diluted EPS $15.38(+10%/+15% ex-Accertify) | 10-K + 8-K Ex-99.1, FY2025 | PASS |
| 10 | AXP | Guidance: Q3'25 raise→Q4/FY25 initiate FY26 ($17.30-$17.90)→Q1'26 reaffirm→Q2'26 raise revenue only, EPS held | 4x 8-K Ex-99.1 releases | PASS |
| 11 | AXP | Credit: net write-off rate 2.2%(2Q26) vs 2.3/2.3/2.2/2.2 trailing 4Q | 8-K Ex-99.2 stat. supplement | PASS |
| 12 | AXP | Capital: CET1/RWA 10.4%(2Q26) vs 10.5/10.5/10.5/10.6; Tier1 11.0%; Total 13.1% | 8-K Ex-99.2 stat. supplement | PASS |
| 13 | AXP | Litigation: Pizza Hazel(D.Mass, 9/30/24) & 5-Star General Store(D.R.I., 3/21/24) — arbitration compelled-motion denied both, appealed to 1st Cir. | 10-Q, Note 7 Contingencies | PASS |
| 14 | AXP | Diluted shares 699m(2Q25)→679m(2Q26), ≈−2.9% | XBRL, WeightedAvgDilutedShares | PASS |
| 15 | MSCI | Q2'26: revenue $867.0m(+12.2%); op. margin 56.2%(vs 55.0%); GAAP EPS $4.69 | 8-K Ex-99.1, filed 2026-07-21 | PASS |
| 16 | MSCI | Q4'25: op. margin 56.4%; GAAP EPS $3.81(-2.3%); Adj. EPS $4.66(+11.5%); FY25 FCF $1,458.6m vs FY24 $1,386.5m(+5.2%) | 8-K Ex-99.1, filed 2026-01-28 | PASS |
| 17 | MSCI | Q1'26 GAAP EPS $5.53 incl. $88m one-off tax benefit (legal-entity restructuring), excluded from adjusted metrics | 8-K Ex-99.1, filed 2026-04-21 | PASS |
| 18 | MSCI | FY26 guidance raised at Q2'26: opex $1,535-1,575m; FCF $1,485-1,545m; OCF $1,655-1,705m (all up from initial/prior ranges) | 8-K Ex-99.1, Q2'26 | PASS |
| 19 | MSCI | Debt 30-Jun-26: $6.0bn Senior Notes + $475m revolver = $6.475bn; cash $352.7m; net debt ≈$6.12bn | 10-Q, Note 7 Debt + Balance Sheet | PASS |
| 20 | MSCI | Retention Rate 95.3%(2Q26) vs 93.4% "a year ago in Q4'25" | 8-K Ex-99.1 releases, Q2'26 & Q4'25 | **MINOR** |
| 21 | MSCI | First Street acquisition: $120m cash at closing + earn-outs, close Q3'26 (guidance conditioned on it) | 8-K Ex-99.1, Q2'26 + 10-Q | PASS |

*(21 facts total across three tickers: 7 each for MA, AXP and MSCI — see the JSON for the complete, separately-numbered list.)*

## 2. The MINOR, in full

### MSCI — Retention Rate comparator mislabeled as "a year ago"

**Claim in dossier (MSCI.md §9, kill criterion 2):** *"Company-wide Retention Rate falls below 92% for two consecutive quarters (currently 95.3%, Q2 2026; 93.4% a year ago in Q4 2025 — the metric itself has some seasonal/measurement noise, so two-quarter persistence is the trigger)."*

**What the primary sources actually say:** MSCI's Q2 2026 earnings release states *"Retention Rate in second quarter 2026 was 95.3%, compared to 94.4% in second quarter 2025."* MSCI's Q4/FY2025 earnings release states *"Retention Rate in fourth quarter 2025 was 93.4%, compared to 93.1% in fourth quarter 2024."* Both of the dossier's numbers (95.3% and 93.4%) are individually correct and exactly sourced — but Q4 2025 is two quarters (six months) before Q2 2026, not "a year ago." The genuine year-ago comparator for Q2 2026 is Q2 2025's Retention Rate of 94.4% (itself confirmed above), which is closer to today's 95.3% than the 93.4% figure the dossier cites as the year-ago baseline.

**Why this matters:** the substance of the claim (Retention Rate is currently well above the 92% kill-criterion threshold, with no adverse trend) is not overturned by this — if anything, correcting the comparator to the true year-ago figure (94.4%) makes the trend look slightly *more* stable, not less. This is a labeling/temporal-reference slip, not a fabricated or wrong number, in the same class as the mischaracterizations DA7/DA8 flagged elsewhere (a correct figure attached to an incorrect description of what it represents).

## 3. Thesis / kill-criterion-1 consistency check

- **MA:** thesis ("structural double-digit revenue growth, 46%+ operating margins") and kill criterion 1 ("net revenue growth falls below 8% YoY for two consecutive quarters") are both consistent with the confirmed Q2 2026 figures (+14.1% revenue growth, 60.2% operating margin — comfortably above both the thesis's stated floor and the kill-criterion trigger).
- **AXP:** thesis ("consistent double-digit EPS growth") and kill criterion 1 ("net write-off rate rises above 3.0% for two consecutive quarters, vs. 2.2–2.3% today") are both confirmed — Q2 2026 diluted EPS grew 11.0% YoY ($4.53 vs $4.08), and the write-off rate figures match exactly as cited above.
- **MSCI:** thesis ("56%+ operating margin, 95.3% Retention Rate") and kill criterion 1 ("organic recurring subscription Run Rate growth falls below 6% for two consecutive quarters, currently 8.1%") are both confirmed exactly against the Q2 2026 earnings release ("Operating income margin... was 56.2%"; "recurring subscription Run Rate growth was 8.1%"; "Retention Rate... was 95.3%").

## 4. One-line judgement on dossier reliability

This is the cleanest batch of the audit series to date: MA and AXP had zero discrepancies across all seven facts checked each, including several multi-decimal and dollar-exact figures (MA's litigation reserve to the million, AXP's four-release guidance track record verbatim, both companies' capital-return share counts to the million). MSCI was equally clean on every quantitative claim but carried one labeling slip — a correct Retention Rate figure attached to an incorrect "a year ago" description of the period it represents. Unlike the derivation-artefact pattern flagged in DA6/DA7/DA8 (recomputing a figure from balance-sheet components instead of citing the company's own reported line), this batch's only finding is a narrative/temporal-reference error with correct underlying numbers on both sides of the comparison — a materially lower-risk failure mode than a numeric error, and one that does not affect any kill-criterion threshold or verdict in any of the three dossiers.
