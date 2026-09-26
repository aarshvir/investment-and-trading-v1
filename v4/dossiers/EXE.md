# Expand Energy Corporation (NASDAQ: EXE) — Diligence Dossier (Agent F65, Wave 4)

## 1. Verdict
**INCLUDE-SMALL** (half weight) — reason: North America's largest natural gas producer with a genuinely strong, de-levered
balance sheet and a market price that (on a reverse DCF) is not even asking for flat free cash flow from an already-elevated
2025 base, but the company has had a CEO terminated without cause, a new CFO, a controller resignation and a $1.25bn
acquisition all inside the last eight months, with the CEO seat still filled on an interim basis as of this writing — a
named, specific governance/execution reservation that keeps this out of full-weight INCLUDE. Thesis horizon: 12–24 months.

## 2. Business in plain English
Expand Energy (formerly Chesapeake Energy, renamed after its 2024 merger with Southwestern Energy) is the largest natural
gas producer in the United States, operating in the Marcellus (Appalachia) and Haynesville (Louisiana/Texas) shale basins,
producing ~7.4–7.6 Bcfe/day (92% natural gas). It sells gas to utilities, industrials and (its stated strategic focus) LNG
exporters and power generators along the Gulf Coast, and — following the September 2026 close of its acquisition of Twin
Eagle Holdings — now also runs an integrated physical natural gas marketing and optimization business, positioning itself as
both the largest producer and, pro forma, a leading marketer of natural gas in North America.

## 3. Why the model likes it — durable or artefact?
Gates checked: not a pass/fail screen — `exclude_pending_deal=False`, `coverage_flag="full"` (no data-coverage gate tripped);
this composite is descriptive context, not a disqualifying gate, and the verdict in §1 is set from the primary-source
evidence in §4–§11, not from this score. b1 factor file (`v4/data/b1_live_scores.csv`, as_of 2026-09-25): composite score 0.478 (decile 5, quintile 3, live_rank 260).
Family scores: Quality (fam_Q) 0.858 — high, driven by low leverage (0.5x net debt/EBITDAX per the company's own Q2 2026
release) and strong operating-cash-flow/assets; Value (fam_V) 0.989 — the highest of any of the three F65 names, driven by
FCF/price (fcfp 0.133), EBIT/EV (0.158) and book/price (0.965, i.e., trading near book value); Momentum (fam_M) 0.025 —
very weak; Earnings-surprise (fam_S) 0.128 — weak, driven by **sue = -0.39** (a smaller negative than EQT's -1.08 but still
a real, model-visible earnings-surprise penalty). **Data conflict noted:** as with EQT, the negative SUE score reflects
GAAP EPS volatility mechanically driven by unrealized hedge/derivative marks (e.g., Q1 2025 GAAP EPS -$1.06 vs Q1 2026
GAAP EPS +$4.81, both heavily influenced by mark-to-market swings on an unsettled hedge book), not by a deteriorating
underlying business — the underlying production and cash-cost trends are stable-to-improving. The triage read (Q04:
quality 4/growth 3/price_vs_growth 4, flagging "post-merger integration and hedge-book complexity" as the named red flag)
is directionally right, though the single biggest concrete risk this diligence pass surfaced (leadership turnover, §6/§11)
was not specifically named in the triage.

## 4. Last two years of results (GAAP unless marked; $ millions except per-share)
| Quarter (calendar) | Revenue | Net income (GAAP) | Diluted EPS (GAAP) | Adjusted net income (non-GAAP) | Adjusted diluted EPS (non-GAAP) |
|---|---|---|---|---|---|
| Q1 2024 | 1,081 | 26 | 0.18 | n/a | n/a |
| Q2 2024 | 505 | (227) | (1.73) | n/a | n/a |
| Q3 2024 | 648 | (114) | (0.85) | n/a | n/a |
| Q4 2024 | n/a | n/a | n/a | 73 | n/a |
| Q1 2025 | 2,196 | (249) | (1.06) | n/a | n/a |
| Q2 2025 | 3,690 | 968 | 4.02 | n/a | n/a |
| Q3 2025 | 2,966 | 547 | 2.28 | n/a | n/a |
| Q4 2025 | n/a | n/a | n/a | 218 | n/a |
| **FY2025 total** | n/a | n/a | n/a | **1,910 (adj. FCF, not net income)** | n/a |
| Q1 2026 | 4,397 | 1,159 | 4.81 | n/a | n/a |
| Q2 2026 | 2,960 | 522 | 2.19 | 317 | 1.33 |

Source: SEC XBRL companyfacts (CIK 0000895126, concepts `Revenues`/`NetIncomeLoss`/`EarningsPerShareDiluted`) for Q1
2024–Q2 2026, cross-checked against the Q2 2026 8-K Ex-99.1 (filed 2026-07-28), which independently confirms Q2 2026 net
income $522M / $2.19 diluted EPS / adjusted net income $317M / adjusted diluted EPS $1.33 — matches exactly. **As with EQT,
revenue and GAAP net income swing heavily quarter to quarter on unrealized derivative marks; this is not organic
revenue/volume change.** Net production was ~7.48 Bcfe/d in Q2 2026 (92% natural gas), within the reaffirmed FY2026 range.

## 5. Guidance track record (last 3 releases with a stated FY2026 range)
| Release (filed) | FY2026 production guidance | FY2026 capex guidance | Action |
|---|---|---|---|
| Q4/FY2025 (2026-02-17, Ex-99.1) | ~7.5 Bcfe/d | ~$2.85bn | **Introduced** ("Expect to produce ~7.5 Bcfe/d for ~$2.85 billion of capital") |
| Q1 2026 (2026-04-28, Ex-99.1) | ~7.5 Bcfe/d | ~$2.85bn | **Maintained/reaffirmed** ("reaffirming full-year 2026 guidance of ~7.5 Bcfe/d") |
| Q2 2026 (2026-07-28, Ex-99.1) | 7.4 – 7.6 Bcfe/d | $2.75 – $2.95bn | **Maintained** (single-point estimate converted to a range around the same midpoint; "reaffirmed full-year 2026 guidance of 7.4 – 7.6 Bcfe/d") |

All figures quoted verbatim from the respective 8-K Exhibit 99.1 earnings releases. No guidance cut or raise across the
three releases reviewed — a stable, on-track production/capex program through three quarters of primary-source evidence.

## 6. Earnings quality & balance sheet
- **Entity scope:** all figures are **Expand Energy Corporation consolidated** (CIK 0000895126 XBRL/10-Q), the successor
  entity to Chesapeake Energy Corporation following its 2024 merger with Southwestern Energy.
- **FCF conversion:** FY2025 GAAP operating cash flow $4,575M less capex $2,736M = free cash flow (non-GAAP) $1,839M;
  adjusted free cash flow (which also excludes merger-related cash costs) **$1,910M** vs FY2024 adjusted FCF of only $202M
  — an ~9.5x increase, driven by (a) a full year of post-merger scale/synergies and (b) materially higher realized gas
  prices in 2025 vs 2024. This base year is elevated by both factors simultaneously and should not be treated as a "normal"
  run-rate (see §7).
- **Leverage:** total debt fell from ~$5.0bn (2025-12-31) to **$3.7bn** (2026-06-30), driven by an April 2026 senior-note
  redemption (~$1.3bn), taking reported net debt to $3.1bn and a **~0.5x net-debt/adjusted-EBITDAX leverage ratio**
  (company-stated, Q2 2026 release) — a genuinely strong, primary-source-confirmed balance sheet for a commodity producer.
  Note the XBRL `LongTermDebt` vs `LongTermDebtNoncurrent` figures at 2026-03-31 ($5,008M total vs $4,133M noncurrent)
  imply an ~$875M current portion of long-term debt at that date — consistent with the subsequently-disclosed April 2026
  redemption of that maturity.
- **Shareholder returns:** ~$530M of buybacks in Q2 2026 alone; ~$850M (≈4% of shares outstanding) year-to-date through
  Q2 2026; a further ~$1bn buyback authorization announced alongside Q2 2026 results; quarterly base dividend of $0.575/
  share (20th consecutive quarter paying a dividend, per the Q4/FY2025 release) — an aggressive, executing capital-return
  program, not just an announced target.
- **M&A:** the Twin Eagle Holdings, N.A., LLC acquisition — entered into via a definitive merger agreement dated **July 27,
  2026**, for **$1.25 billion cash from Five Point Infrastructure**, funded via cash on hand and revolver borrowings,
  closed **September 16, 2026** (both dates from the respective primary-source 8-Ks, not a news summary). Company-stated
  expectations: >$200M of incremental annual EBITDA initially, $150M/year of run-rate synergies by year-end 2028, and an
  increase in the company's total targeted marketing/commercial incremental free cash flow to $750M/year (up 50% from a
  prior $500M/year target). These are management projections, not yet realized results — flagged as such.
- **Leadership turnover (the central finding of this diligence pass):**
  - **2026-02-06:** CEO Domenic "Nick" Dell'Osso, Jr. was replaced, "effective immediately," by Board Chairman Michael
    Wichterich as **Interim** President and CEO; Dell'Osso also resigned from the Board effective immediately and will
    serve only "as an external advisor for a period of time." The 8-K states this was a termination "without cause" (which
    entitles Dell'Osso to severance per his existing agreement) — the filing gives no reason beyond the personnel change
    itself. Same 8-K/press release also announced the corporate HQ will relocate from Oklahoma City, OK to Spring, TX
    (Houston area) in mid-2026.
  - **2026-04-06:** Marcel Teunissen (previously President, North America and CFO 2020–2024 at Parkland Corporation) was
    appointed EVP and CFO, replacing **Brittany Raiford**, who had been serving as **Interim CFO** — meaning the actual
    permanent CFO who preceded Raiford is not identified in the filings reviewed in this pass (a further, earlier,
    unexplained CFO-level departure — **data gap, disclosed**).
  - **2026-06-23:** VP – Accounting & Controller Gregory M. Larson resigned (company states "not the result of any
    disagreement... on any matter relating to its operations, policies or practices"); new CFO Teunissen assumed the
    principal-accounting-officer role on an interim basis while a permanent Controller search continues.
  - **2026-09-16:** concurrent with the Twin Eagle close, EVP–Marketing and Commercial Dan Turco moved to a different EVP
    role (not a departure, but a title/scope change tied to the acquisition).
  - As of this dossier's data cutoff (2026-09-25), **no permanent CEO has been named** — more than seven months after the
    February 2026 departure. This is the single most significant, evidence-based (not speculative) reservation in this
    dossier.

## 7. Valuation snapshot and reverse DCF
- Price used: **2026-09-25 close, $86.84**; market cap $20.77bn; shares 239.2M. NTM P/E 10.1x (`pe_ntm`) vs 11.1x
  (`pe_ntm_qaware`), flagged `ntm_quality="caution"` / `fy1_dispersion_extreme` — analyst estimates for this name disagree
  materially, consistent with the same hedge-driven EPS volatility noted in §3/§4. Consensus rating `buy` (27 analysts),
  mean target $125.52 — **~45% above the current price** (matches the triage's "largest street upside in the batch").
- **No V1 systematic valuation row exists for EXE** (not present in `v1_valuation_table.csv`/`v1_valuation.json`) — this
  dossier's valuation view is the analyst's own reverse DCF.
- **Reverse DCF (two-stage, adjusted-FCF basis):** Base-year FCF = FY2025 adjusted FCF $1,910M (as with EQT, this base is
  itself elevated by a strong 2025 gas-price year *plus* a full year of merger synergy ramp, so it is a genuinely aggressive
  starting point, not a conservative one). WACC assumption 9.5% (E&P sector convention, with a modest premium to EQT's 9.0%
  reflecting the leadership-turnover and integration risk in §6 — not embedded via a lower base-case growth number so the
  valuation math and the qualitative risk discussion stay separate and auditable). Terminal growth 2.5%. Solving for the
  constant 10-year FCF growth rate that equates the two-stage DCF value to the $20.77bn market cap: **implied 10-year FCF
  growth ≈ -1.6%** (sensitivity: -2.5% at WACC 9.0%, -0.7% at WACC 10.0%, +0.2% at WACC 10.5%). In plain English: even
  starting from an unusually strong 2025 base, the market is pricing in a mild multi-year *decline* in free cash flow, not
  growth — a conservative embedded expectation.
- **Analyst base case:** modest positive FCF/share growth (~0–2%/yr) from continued share buybacks (shrinking the
  denominator ~4%/yr at the current pace) roughly offsetting gas-price normalization off the 2025 high, before any Twin
  Eagle contribution is even credited. This is **above** the reverse-DCF implied growth of ~-1.6% → **implied_vs_base =
  "below."** This is the valuation-side case for inclusion; it is the governance/leadership finding in §6, not the
  valuation, that caps this at INCLUDE-SMALL rather than full INCLUDE.

## 8. Bull case / bear case
**Bull (3 points):**
1. Leverage is genuinely low (~0.5x net debt/adjusted EBITDAX, company-stated) after an active 2026 debt-paydown program,
   giving real balance-sheet flexibility that most of the E&P sector lacks.
2. Capital return is not just promised but executing: ~4% of shares repurchased year-to-date through Q2 2026 plus a new
   ~$1bn authorization, on top of an uninterrupted quarterly dividend (20 consecutive quarters).
3. Twin Eagle (closed September 2026) is a real, closed transaction (not a pending/at-risk announcement) that management
   states is "immediately accretive" at >$200M of initial annual EBITDA for a $1.25bn purchase price (~6.25x EV/EBITDA on
   the stated initial contribution) — a reasonable multiple if the EBITDA contribution materializes as described.

**Bear (3 points):**
1. Leadership instability is real and recent: a CEO terminated without cause, a CFO who replaced another CFO who was
   already "interim," and a controller resignation, all within an eight-month window, with the CEO seat still interim as
   of this writing — a demonstrated pattern, not a single isolated event, occurring simultaneously with a $1.25bn
   acquisition integration.
2. FY2025's FCF base ($1,910M) is a genuinely difficult comparison: it embeds both a strong gas-price year and the peak
   of post-merger synergy capture, so period-over-period FCF growth from here is arithmetically likely to be harder to
   sustain even before considering Twin Eagle integration risk.
3. As with EQT, GAAP EPS is not a clean quarter-to-quarter signal (Q1 2026 $4.81 vs Q2 2026 $2.19, both influenced by
   hedge mark-to-market), which raises real execution/communication risk for a company simultaneously managing a CEO
   transition and a major acquisition close.

## 9. Key risks & kill criteria (measurable)
1. No permanent CEO is named within 12 months of the February 6, 2026 departure (i.e., by February 6, 2027) — a direct,
   dated, measurable governance trigger.
2. A third C-suite or principal-officer-level departure (beyond the CEO and CFO changes already disclosed) within the
   next 12 months — would confirm a pattern rather than a one-off transition.
3. Consolidated net debt/adjusted EBITDAX rises above 1.5x for two consecutive quarters (vs. the current ~0.5x).
4. FY2026 production guidance is cut below the current 7.4–7.6 Bcfe/d range.
5. The Twin Eagle-linked $750M/year incremental marketing/commercial free-cash-flow target is not on a credible trajectory
   (management commentary walks it back or delays it) within 18 months of the September 16, 2026 close (i.e., by March 2028).

## 10. Catalysts & calendar
- Next earnings date: **2026-10-27** (Q3 2026, per d4 snapshot; `next_earnings_is_estimate = True`, treat as approximate).
- Permanent CEO appointment (unscheduled — a real catalyst/risk event whenever it occurs).
- Twin Eagle integration updates expected on the Q3 2026 and subsequent earnings calls.

## 11. Red-flag scan
- **Legal proceedings:** the Q2 2026 10-Q (Item 1, Part II) discloses ordinary-course litigation plus ongoing claims
  reconciliation tied to the 2021 Chesapeake Energy Chapter 11 emergence (Effective Date 2021-02-09) — management states no
  pending/threatened matter is expected to have a material adverse effect; no new material litigation surfaced.
- **Leadership/governance:** see §6 — this is the dossier's primary red flag, evidence-based and dated from the company's
  own 8-K filings (2026-02-06, 2026-04-06, 2026-06-23, 2026-09-16), not from news summaries or speculation.
- **Auditor/restatement/going concern:** none disclosed in the sections reviewed.
- **Insider ownership:** d4 snapshot shows `y_heldPercentInsiders` 0.36%, `y_heldPercentInstitutions` 96.4%. No Form 4
  cluster-selling analysis performed in this pass — data gap, disclosed (though notable that no executive departure 8-K
  reviewed mentioned a for-cause or fraud-related trigger).

## 12. Sources
1. SEC EDGAR submissions index, CIK 0000895126: `https://data.sec.gov/submissions/CIK0000895126.json` (retrieved 2026-09-26).
2. SEC EDGAR XBRL companyfacts, CIK 0000895126: `https://data.sec.gov/api/xbrl/companyfacts/CIK0000895126.json` (retrieved 2026-09-26).
3. Expand Energy 8-K Ex-99.1, Q2 2026 results, filed 2026-07-28: `https://www.sec.gov/Archives/edgar/data/895126/000089512626000046/exe-ex_991x20260630x8kxpr.htm`.
4. Expand Energy 8-K Ex-99.1, Q1 2026 results, filed 2026-04-28: `https://www.sec.gov/Archives/edgar/data/895126/000089512626000027/exe-ex_991x20260331x8kxpr.htm`.
5. Expand Energy 8-K Ex-99.1, Q4/FY2025 results & 2026 outlook, filed 2026-02-17: `https://www.sec.gov/Archives/edgar/data/895126/000089512626000008/exe-ex_991x20251231x8kxpr.htm`.
6. Expand Energy 8-K, Twin Eagle acquisition announcement, filed 2026-07-27: `https://www.sec.gov/Archives/edgar/data/895126/000089512626000039/exe-ex_991x20260727x8kxpr.htm`.
7. Expand Energy 8-K, Twin Eagle acquisition closing/officer change, filed 2026-09-16: `https://www.sec.gov/Archives/edgar/data/895126/000089512626000053/exe-20260916.htm`.
8. Expand Energy 8-K, CFO appointment, filed 2026-04-06: `https://www.sec.gov/Archives/edgar/data/895126/000089512626000016/exe-20260406.htm`.
9. Expand Energy 8-K, CEO transition, filed 2026-02-09 (event date 2026-02-06): `https://www.sec.gov/Archives/edgar/data/895126/000089512626000003/exe-20260206.htm`.
10. Expand Energy 8-K, Controller resignation, filed 2026-06-26 (event date 2026-06-23): `https://www.sec.gov/Archives/edgar/data/895126/000089512626000036/exe-20260623.htm`.
11. Expand Energy Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-28: `https://www.sec.gov/Archives/edgar/data/895126/000089512626000047/exe-20260630.htm`.
12. `v4/data/b1_live_scores.csv` and `v4/data/d4_live_snapshot.parquet` (as_of 2026-09-25), and `v4/outputs/Q04_triage.json`.
13. `v4/outputs/v1_valuation_table.csv` (checked; no EXE row as of this writing).

## Data basis, recency and disclaimer
Most recent period incorporated: 10-Q for the quarter ended 2026-06-30 (filed 2026-07-28) and the 8-K earnings release
dated 2026-07-28. Events checked to 2026-09-25 close, including the September 16, 2026 Twin Eagle closing and associated
officer-change 8-K, both inside the review window. GAAP vs adjusted figures are labelled throughout; "adjusted net income,"
"adjusted diluted EPS," "adjusted EBITDAX," "free cash flow" and "adjusted free cash flow" are the company's own defined
non-GAAP measures, reconciled in the source earnings releases. This is research, not personalized investment advice; not personalised investment advice.
