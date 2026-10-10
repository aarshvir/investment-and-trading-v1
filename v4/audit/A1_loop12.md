# A1 (quant and data) - Loop 12 audit

**Auditor:** A1, former head of quantitative research. **Build audited:** `outputs/lead_portfolio_build.json`, built 2026-10-10T11:06:44, content_sha256 98c5d007df11 (`lead_guard.py`: "build fresh"). Holdings (20): GD 10.0, ACGL 9.2, BR 7.8, WFC 6.7, CAH 6.4, GDDY 5.8, COR 5.6, WTW 5.6 (8 full conviction = 57.1%), then AMCR, BIIB, OMC, BKNG, ADBE, FDX, ACN, INTU, FSLR, UBER, SYF, FIS (12 half conviction). Rule hash unchanged since 6 Oct: the portfolio moved on verdict changes only.

## 1. Total score and verdict

**73 / 100** (Loop 11: 76). The numerical engine is still sound: every backtest, constraint and risk figure I recomputed ties out. The Loop-11 must-fixes on valuation propagation (SNA, UDR), the tech-share disclosure, the DV series in A.4/A.5 and Codex v012-v016 reconciliation are genuinely fixed, and all 500 dossiers now carry a second-analyst check. The score falls because the rebuilt largest holding (GD, 10%) rests on a valuation call its own dossier does not support and a footnote that is false, the "Read this first" block was not regenerated for the completed state (garbled and contradictory), displayed multiples mix bases (FDX, ADBE), and the C1 gate is open for the tenth loop.

## 2. Criterion table

| # | Criterion | Score | Evidence | Gap(s) |
|---|---|---|---|---|
| 1 | Data integrity and lineage | 8 | Weights sum 1.0; yield 1.563% (report 1.6%); tech 21.87% / IT-only 20.17%; risk and drawdown tie to the data. Build vs register implied/verdict now agree for every eligible name (Loop-11 mismatch fixed). | FDX NTM P/E 14.3x is on pre-spin earnings (guide-based about 16.3x); ADBE 8.7x and OMC 6.7x use forward non-GAAP EPS; the snapshot flags FDX and ADBE "caution" and the report shows no flag. Label bug: 'in line' vs 'in_line' (PCG, HPE, F, KKR wrongly ineligible; pool 211 not 207). |
| 2 | Backtest and validation rigour | 8 | Top-30 CAGR 12.52% vs SPY 15.10%, newey-west t -1.12 to -1.18, sub-period gaps (2012-16 -0.3, 2017-21 -7.6, 2022-26 +0.3 pts) reproduce. Honest "no edge". | The backtested model selects only 3 of 20 holdings; 17 come through the analyst route (no backtest). Selection from about 111 tied "below" names by the analyst's own stated base return is a winner's-curse process that is never calibrated. |
| 3 | Calibration and honesty | 7 | 78% gain / 49% beat / 21% and 4% edge odds reproduce (21.3%, 3.7%). 40% tolerance and beta caveat now stated. | Bottom-up -4/+12/+29 silently excludes GD (10% of weight); footnote "base case exists for every holding" is false; beta 0.56 quoted beside 0.61; bull cases of +50%, +53%, +86% a year (ACN, SYF, BKNG) and bear = base for ACN are scripted artefacts shown as scenarios; order-dependence line again just the 8 INCLUDE names. |
| 4 | Company-level diligence | 8 | Five dossiers sampled (GD, ACN, WFC, OMC, FDX): 12 of 12 load-bearing facts pass against company releases. All 20 holdings have an independent check; all 500 covered. | Check depth is thin for some holdings (BKNG 4 facts, GD 8, SYF 7); the independent series fails 22% of facts (909 of 4,186; ADBE 6 of 17, FDX 6 of 15 in DVH6). GD's valuation section is the weak part, not its facts. |
| 5 | Valuation rigour | 6 | Programme basis (5.17% + beta x ERP, SBC deducted) is applied across the DV series. | GD: dossier scenarios give $324 vs $336.72 (-3.8%), V1 says "demanding", and "below" comes from comparing +1.6% to +3.5% implied FCF growth with 6% guided revenue growth; no 3-year base case. Largest holding therefore has no valid margin of safety. Mixed GAAP / non-GAAP / pre-spin P/E in the holdings table. |
| 6 | Portfolio construction and risk | 8 | All six constraints hold after rounding (max name 10.0%, half-conviction max 4.84%, floor 1.70%, sector 25.00%, sub-industry 12.00%). Worst fall -43.20% reproduced exactly; GFC -40.4% vs -40.5% (plain SPY); COVID -36.4%; 2022 -9.3% vs -9.9% (SPY price vs total return). | Beta 0.61 and 42% market share come from one calm window (beta 0.89 / 0.97 / 0.93 / 1.00 in earlier windows, 0.76 over five years); sub-period table still not in the report. Industrials sit exactly at the 25% cap with GD at its 10% cap. |
| 7 | Strategy coherence and mandate fit | 8 | All-stock request answered; 40% tolerance adopted; tech share stated. | The headline turnover is against v011 not v017. |
| 8 | Implementation and monitoring | 7 | Kill criteria per holding; weekly checklist; estate-tax and withholding facts. | Post-cut-off moves not shown: to 9 Oct ACN +18.7%, INTU +10.3%, CAH +8.1%, GDDY +7.4%; ACN's "next earnings" still future in the table. Report earnings dates WFC 13 Oct, SYF and OMC 20 Oct fall within days of purchase. |
| 9 | Communication for the owner | 6 | Answer-first structure retained. | "only 500 of them ... The other 0 dossiers ... treat any unchecked name's numbers as unverified" contradicts the headline; wrong section cross-references; audit-loop language in an owner document; about 120 re-assessment bullets in section 6. |
| 10 | Reproducibility and auditability | 7 | `run_all.py`, pinned requirements, build_history.jsonl, rule commitments hash unchanged. | Gate OPEN for the tenth loop (C1 names an older build); 103 of 111 scripts hard-code `C:\Users\user` paths; libraries and an F-summary cache outside the repo; F-summary precedence by file mtime; stale docstring. |

**Total: 8+8+7+8+6+8+8+7+6+7 = 73**

## 3. Previous must-fix check (Loop 11)

| Item | Status |
|---|---|
| SNA discount rate | Fixed: re-run at the programme rate gives "above"; SNA no longer eligible (build shows it as ineligible). Per-holding WACC table still missing. |
| UDR / implied propagation (rule p) | Fixed: build equals the register for all eligible names (only ineligible names differ, as nan vs "above"). |
| Rule (o) and tech disclosure | Fixed: 21.9% and 20.2% printed, both match my 21.87% and 20.17%. |
| A.4 / A.5 and DV series | Fixed (500 of 500). Wording of the coverage sentence is broken (see below). |
| Risk by sub-period | Not fixed (only a one-line caveat). |
| Order-dependence by conviction group | Not fixed. |
| Gate and quarter-label control | Not fixed; gate OPEN. |
| Rule amendments (j)-(p) | (p) is justified by internal consistency (it removed an inconsistency, UDR, and was committed before the build). (j) remains a judgement call written after verdicts were known; (l) and (o) are disclosed. None looks like result-chasing, but the tie-break by the analyst's own base return rewards the most optimistic scenario writer. |

## 4. Must-fix to reach 95 (ranked by score impact)

1. **GD valuation and the false footnote (criteria 5, 3, 7).** GD is 10% of the portfolio. Its own dossier gives a probability-weighted value 3.8% below the price; V1 says "demanding"; "below" rests on comparing FCF growth with revenue growth; the build has no base case. Give GD a like-for-like base case or relabel it in_line and rebuild; remove "The base case ... exists for every holding"; show the 90% coverage next to the bottom-up figures (-4/+12/+29 is -3.9/+10.7/+26.4 with GD at zero). Verify: numeric GD scenarios, footnote true, build equals register.
2. **Regenerate "Read this first" (criteria 9, 3).** Replace the garbled coverage sentence (template `lead_report_sections.py` line 168) with: 500 of 500 checked, median facts per name, holdings with 4 or fewer facts, 22% fact-failure rate; use beta 0.61; fix (§3) and (§4) references; compare turnover with v017 (13 kept, 7 new, 7 out). Verify with grep.
3. **Multiples on one basis (criteria 1, 5).** FDX about 16.3x on the CY2026 guide; ADBE 13.1x on trailing GAAP; label each row's basis and show the caution flag.
4. **Fix the 'in line' label bug (criteria 1, 3)** and restate the eligible pool (211); add an assertion on the three allowed labels.
5. **Post-cut-off check (criteria 3, 8).** Add a "move since 25 Sep" column and re-test ACN and INTU at 9 Oct prices.
6. **Risk by sub-period, order-dependence by group, per-holding Ke table (criteria 6, 3).**
7. **Close the gate (criterion 10):** rebuild, C1, freeze, audit once; relative paths; hashes not mtimes.

## 5. Numbers re-computed (report vs mine)

| # | Number | Report | Mine | Result |
|---|---|---|---|---|
| 1 | Top-30 backtest CAGR 2012-01 to 2026-08 | 12.5% | 12.52% | PASS |
| 2 | SPY CAGR same window | 15.1% | 15.10% | PASS |
| 3 | Average gap and t-stat (top 30 vs SPY) | -2.0%, t -1.12 | -2.04%, t -1.12 (lag 3) to -1.18 (lag 6) | PASS |
| 4 | Weights sum; max name; max half-conviction; floor; sector; sub-industry | 1.0; 10%; 4.84%; 1.70%; 25.0%; 12.0% | identical (build checks, my sums) | PASS |
| 5 | Worst fall of the sleeve 2005-2026 | -43.2% (2007-12-10 to 2009-03-09) | -43.20%, trough 2009-03-09 | PASS |
| 6 | GFC replay (sleeve, quarterly rebalanced) | -40.5% (84% real data) | -40.4%; SPY -54.8% vs -55.2% (price vs total return); no-price weight 15.7% | PASS |
| 7 | COVID and 2022 replays | -36.4% / -9.9% | -36.4% / -9.3% | PASS (2022 minor: SPY price vs adjusted) |
| 8 | Vol / TE / beta, last 3 years | 14.4% / 12.5% / 0.61 | 14.39% / 12.55% / 0.606 | PASS |
| 9 | Same measures by window | not reported | beta 0.89 (2005-09), 0.97 (2010-14), 0.93 (2015-19), 1.00 (2020-23), 0.76 (5y); TE 5.5-9.3% earlier | FAIL (omission) |
| 10 | Weighted trailing dividend yield | 1.6% | 1.563% | PASS |
| 11 | Odds of 10-point edge: 1 year / 5-year average | 21% / 4% | 21.3% / 3.7% | PASS |
| 12 | Technology share | 21.9% / 20.2% | 21.87% / 20.17% | PASS |
| 13 | Bottom-up 3-year bear / base / bull | -4% / +12% / +29%, $43,861 / $70,036 / $108,271 on $50k | -4.27% / +11.89% / +29.37% on 90% of weight; GD absent | FAIL (coverage not stated) |
| 14 | Independent fact-fail rate | 909 of 4,186 (22%) | 909 of 4,186 across 51 DV files, 446 tickers | PASS |
| 15 | Eligible pool | 207 | 211 once 'in line' is normalised | FAIL |
| 16 | NTM P/E FDX | 14.3x | about 16.3x on CY2026 guide midpoint | FAIL (basis) |

## 6. Facts checked against primary sources

| Ticker | Claim | Source | Result |
|---|---|---|---|
| GD | Q2 2026 revenue $14.09bn (+8.1%), EPS $4.24, backlog $136.5bn, debt $7.5bn / cash $4.3bn | GD 8-K Ex-99.1 | PASS |
| GD | FY26 EPS guide $16.80-16.90, revenue about $55.7bn | company release | PASS |
| GD | implied_vs_base = below | dossier section 6, DV18 item 4, V1 | FAIL |
| ACN | Q4 FY26 revenue $18.7bn, bookings $22.2bn, FY26 EPS $13.56, FY27 guide $14.39-14.81 | Accenture 8-K | PASS |
| ACN | P/E 12.0x and pending earnings at 25 Sep | stock +18.7% by 9 Oct | MINOR |
| WFC | Q2 2026 NI $6.4bn, EPS $2.00, ROE 15.0%, ROTCE 17.7% | Wells Fargo 8-K | PASS |
| OMC | Q2 2026 revenue $6,562.5M, organic 6.1%, EPS $2.08 / $2.65, Core EBITA margin 17.8% | Omnicom 8-K | PASS |
| FDX | FY26 revenue $94.7bn, adjusted EPS $20.24, CY2026 guide $16.90-18.10, spin 1 Jun 2026 | FedEx Q4 release | PASS |
| FDX | NTM P/E 14.3x | snapshot pre-spin vs guide | FAIL |
| FDX | Q4 EPS column ($6.60 GAAP beside adjusted $6.31) | release | MINOR |
| ADBE | NTM P/E 8.7x (non-GAAP forward) | snapshot | MINOR |
| portfolio | Tech 21.9% / 20.2%; "best of 207" | build; code line 152 | PASS / FAIL |
