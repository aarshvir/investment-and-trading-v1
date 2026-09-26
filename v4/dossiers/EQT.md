# EQT Corporation (NYSE: EQT) — Diligence Dossier (Agent F65, Wave 4)

## 1. Verdict
**INCLUDE-SMALL** (half weight) — reason: a genuinely low-cost, structurally advantaged Appalachian gas producer with real
LNG/power-demand tailwinds and a market price that is not paying up for growth, but only 25% of 2026 volumes are hedged and
GAAP earnings are dominated by unrealized derivative marks, so the near-term P&L (and any single-quarter re-rating) can be
noisy and commodity-price cyclicality is real. Thesis horizon: 12–36 months.

## 2. Business in plain English
EQT is the largest natural gas producer in Appalachia (Marcellus shale, Pennsylvania/West Virginia/Ohio), producing ~2.4
Tcfe/year, with an integrated gathering/transmission midstream system (including stakes in the Mountain Valley Pipeline and
Eureka Midstream) that it uses to control its own costs and market access rather than paying third parties. It sells natural
gas, NGLs and a small amount of oil to utilities, industrial buyers, marketers and (increasingly) LNG exporters and gas-fired
power generators, earning a spread between a low production/transport cost base (~$1.00–1.10/Mcfe operating cost) and the
sale price, which is levered directly to Henry Hub/Appalachian basis gas prices.

## 3. Why the model likes it — durable or artefact?
Gates checked: not a pass/fail screen — `exclude_pending_deal=False`, `coverage_flag="full"` (no data-coverage gate tripped);
this composite is descriptive context, not a disqualifying gate, and the verdict in §1 is set from the primary-source
evidence in §4–§11, not from this score. b1 factor file (`v4/data/b1_live_scores.csv`, as_of 2026-09-25): composite score 0.224 (decile 3, quintile 2, live_rank 386 —
**not** in live_top30; `exclude_pending_deal=False`). Family scores: Quality (fam_Q) 0.502 — decent, driven by gross
profit/assets (gp_a 0.193, ~high percentile) and low leverage; Value (fam_V) 0.918 — very high, driven by earnings yield,
FCF/price (fcfp 0.118) and EBIT/EV (0.108); Momentum (fam_M) 0.073 — weak (mom_12_1 only +0.7%); Earnings-surprise (fam_S)
0.075 — very weak, driven by **sue = -1.08**, the worst of the three F65 names. **Data conflict:** the SUE (standardized
unexpected earnings) factor penalizes EQT for volatile/negative *reported* EPS surprises, but those swings are mechanically
driven by unrealized mark-to-market gains/losses on EQT's gas hedge book (see §6), not by operating deterioration — Q3 2025
GAAP EPS was -$0.54 while adjusted EPS was positive; the quant model cannot see that distinction. The genuine, durable part
of the "why the model likes it" story is the Value signal (real: FCF yield 7.7%, EV/EBIT 10.9%, cheap on cash generation)
plus the underlying Quality (real: low leverage 0.8x, high gross margins). The triage read (Q04, quality 4/growth 3/
price_vs_growth 4) called the "negative near-term growth" a gas-price/comp lap rather than volume decline — confirmed below.

## 4. Last two years of results (GAAP unless marked; $ millions except per-share)
| Quarter (calendar) | Revenue | YoY | Net income (GAAP) | Diluted EPS (GAAP) | Adjusted EPS (non-GAAP) |
|---|---|---|---|---|---|
| Q1 2024 | 1,412 | — | 103 | 0.23 | n/a (not pulled) |
| Q2 2024 | 953 | — | 10 | 0.02 | n/a |
| Q3 2024 | 1,284 | — | (301) | (0.54) | n/a |
| Q4 2024 (derived: FY24 − 9mo24) | 1,625 | — | 418 | ~0.74 | n/a |
| Q1 2025 | 1,740 | +23.2% | 242 | 0.40 | n/a |
| Q2 2025 | 2,558 | +168.4% | 784 | 1.30 | 0.45 |
| Q3 2025 | 1,959 | +52.6% | 336 | 0.53 | n/a |
| Q4 2025 (derived: FY25 − 9mo25) | 2,388 | +47.0% | 677 | ~1.08 | n/a |
| Q1 2026 | 3,379 | +94.2% | 1,487 | 2.36 | n/a |
| Q2 2026 | 1,810 | −29.2% | 211 | 0.34 | 0.39 |

Source: SEC XBRL companyfacts (CIK 0000033213), `Revenues`/`NetIncomeLoss`/`EarningsPerShareDiluted`, cross-checked against
the Q2 2026 8-K Ex-99.1 (filed 2026-07-22) and Q1 2026 8-K Ex-99.1 (filed 2026-04-22) tables, which show GAAP diluted EPS of
$0.34 (Q2'26) and $2.36 (Q1'26) matching XBRL exactly. **Revenue and GAAP net income swing violently quarter to quarter
because "Revenues" and "Net income" include unrealized gains/losses on EQT's natural gas derivative (hedge) book, which move
with the forward gas curve — this is not organic revenue growth/decline.** FY2025 total sales volume was 2,382 Bcfe vs 2,228
Bcfe in FY2024 (+6.9%, the real organic growth number), average realized price $3.19/Mcfe vs $2.74/Mcfe (+16.4%, the price
effect that dominates the GAAP swings). Full-year: FY2025 net income attributable to EQT $2,039M (EPS $3.31) vs FY2024 $231M
(EPS $0.45); adjusted EPS $3.05 (FY25) vs $1.60 (FY24) (2025 8-K Ex-99.1, filed 2026-02-18).

## 5. Guidance track record (last 3 releases with a stated FY2026 range; the Sep-2025 release predates FY2026 guidance)
| Release (filed) | FY2026 total sales-volume guidance | FY2026 capex guidance | Action |
|---|---|---|---|
| Q4/FY2025 (2026-02-17, Ex-99.1) | 2,275 – 2,375 Bcfe | Maintenance $2,070–2,210M + growth $580–640M | Initial guidance |
| Q1 2026 (2026-04-21, Ex-99.1) | 2,275 – 2,375 Bcfe | (unchanged detail in release) | **Maintained** |
| Q2 2026 (2026-07-21, Ex-99.1) | **2,375 – 2,450 Bcfe** (quote: "Raising 2026 production guidance by ~90 Bcfe") | Maintenance capex cut $25M (quote: "full-year capital spending guidance reduced by $25 million") | **Raised** volume, **cut** capex |

All three numbers quoted verbatim from the respective 8-K Exhibit 99.1 earnings releases (primary source, not a news
summary). The Q2 2026 raise was explicitly attributed to "better-than-expected benefits from compression investments...
shallowing decline rates" — i.e., well performance, not a price assumption change.

## 6. Earnings quality & balance sheet
- **Entity scope:** all figures below are **EQT Corporation consolidated** (CIK 0000033213 10-Q/10-K XBRL) unless marked
  "attributable to EQT," which is the company's own non-GAAP measure that nets out the ~47–51% third-party (Blackstone
  Credit & Insurance, "BXCI") noncontrolling interest in the PipeBox LLC Midstream JV that began December 30, 2024.
- **FCF conversion:** FY2025 free cash flow attributable to EQT $2,503M vs FY2024 $684M (2025 8-K Ex-99.1, p.2 table) — a
  3.7x increase driven almost entirely by the +16.4% realized-price move above, not cost structure change. Net income
  attributable to EQT FY2025 $2,039M vs FCF-attributable $2,503M ⇒ FCF/NI ≈ 1.23x (healthy, cash generation exceeds GAAP
  earnings, consistent with high D&A and working-capital timing).
- **GAAP vs adjusted gap:** driven almost entirely by unrealized (non-cash) gains/losses on the commodity derivative book,
  which the company explicitly labels as removed in its "adjusted" EPS/EBITDA. Q2 2026 GAAP EPS $0.34 vs adjusted $0.39
  (narrow gap, hedges roughly settled); Q2 2025 GAAP EPS $1.30 vs adjusted $0.45 (wide gap, large unrealized hedge gain).
- **Hedging:** per the Q4/FY2025 release, EQT "increased 2026 hedge percentage from 7% to 25%," with collars floor
  $3.94/ceiling $5.70 per MMBtu — meaning **75% of 2026 volumes remain unhedged and exposed to spot Appalachian gas prices**;
  this is the single biggest swing factor in both earnings and the reverse-DCF below.
- **Balance sheet / leverage:** total debt fell from $7.8bn (2025-12-31) to $5.7bn (2026-06-30); net debt from ~$7.7bn to
  $5.5bn over the same period (Q2 2026 8-K Ex-99.1, "Liquidity" section) — a genuine, primary-source-verified deleveraging of
  ~$2.1–2.2bn in two quarters, aided by the strong FY2025 cash generation. Fitch upgraded EQT to BBB in Q1 2026 (Q1 2026
  8-K Ex-99.1, "Credit Ratings" bullet). Total liquidity ~$3.6bn (Q2 2026, revolver + cash, ex-Eureka Midstream facility).
- **M&A / capital deployed:** (1) Blackline Midstream (two New England propane terminals) acquired for $77M, closed
  2026-07-21, ~20% projected FCF yield (2027–2031 average) — small, accretive bolt-on. (2) MVP Mainline/MVP Boost ownership
  increased from ~49% to ~53% for ~$115M (EQT's share), implying 9x adjusted EBITDA / 12% IRR, exercised 2026-01-02 per the
  Q4/FY2025 8-K — a related-party-adjacent transaction with the Blackstone-affiliated Midstream JV partner, priced at an
  option struck when the JV was formed; disclosed, not flagged as a governance concern. (3) MVP Southgate: EQT accelerated
  $85M of capital contributions to complete construction by year-end 2026 (Q2 2026 8-K).
- **Share count:** diluted shares ~625.5M (Q2 2026 10-Q), essentially flat — no material buyback or issuance program
  disclosed in the reviewed releases; capital return is currently debt paydown + a small dividend (yield ~1.3%), not buybacks.

## 7. Valuation snapshot and reverse DCF
- Price used: **2026-09-25 close, $50.81** (matches `d4_live_snapshot.parquet`, retrieved 2026-09-25 20:29 UTC).
  Market cap $31.78bn; EV $41.59bn; shares 625.5M.
- NTM P/E from d4: 12.4x (`pe_ntm`) vs 15.2x (`pe_ntm_qaware`) — d4 itself flags this pair `ntm_quality="caution"` with
  flags `fy0_vs_quarterly_rows_-9%`, `fy1_thin_coverage`, `ntm_timeweighted_vs_quarteraware_-18%`. **Data conflict noted:**
  the NTM P/E is unreliable for EQT because consensus quarterly EPS estimates disagree by double digits depending on
  aggregation method — a direct consequence of the same hedge-driven EPS volatility flagged in §6. FCF yield (b1) 7.74%.
- **No V1 systematic valuation row exists for EQT** (not present in `v1_valuation_table.csv`/`v1_valuation.json`) — this
  dossier's valuation view is the analyst's own reverse DCF, built independently below.
- **Reverse DCF (two-stage, FCF-attributable-to-EQT basis):** Base-year FCF = FY2025 actual $2,503M (attributable to EQT,
  per §6 — this is itself an elevated, strong-gas-price year, so the reverse DCF answers "how much *further* growth from an
  already-good year does the price need"). WACC assumption 9.0% (E&P sector convention; d4's trailing beta of 0.576 is not
  used directly — a hedge-smoothed regression beta understates a commodity producer's true cost of capital). Terminal
  growth 2.5%. Solving for the constant 10-year FCF growth rate that equates the two-stage DCF value to the $31.78bn market
  cap: **implied 10-year FCF growth ≈ -0.4%** (sensitivity: -1.4% at WACC 8.5%, +1.5% at WACC 10.0%). In plain English: at
  the current price, the market is not asking EQT to grow free cash flow at all from its already-strong 2025 level over the
  next decade — it only has to hold roughly flat (in a business with real production growth, LNG-linked demand, and capex
  discipline) to justify today's price.
- **Analyst base/bear/bull cases** (see scenario_basis in the summary JSON for the full numeric basis): Base case assumes
  FCF/share grows ~6%/yr for three years (mid-single-digit production growth plus incremental LNG/power-demand contracts,
  partially offset by gas-price normalization off the 2025 high) with the exit FCF yield roughly unchanged at 8% — well
  **above** the reverse-DCF implied growth of ~0%. **implied_vs_base = "below"** — consistent with the program's INCLUDE
  eligibility test (price is not paying for more growth than the evidence-based base case delivers).

## 8. Bull case / bear case
**Bull (3 points):**
1. Structural Appalachian gas demand from Gulf Coast LNG exports and new gas-fired power/data-center load is real and
   contracted, not speculative: the CPV Shay Energy Center 10-year supply deal (325,000 Dth/d, PJM-power-linked pricing) and
   the 5-year, 0.5 Mtpa LNG offtake SPA (signed with an Asian buyer, expected +$45M of 2028 FCF at strip pricing) are both
   dated, primary-source-confirmed contracts (Q2 2026 8-K), not aspirational targets.
2. Balance sheet has genuinely de-levered ($2.1–2.2bn of net debt reduction in two quarters of 2026) with a credit-rating
   upgrade (Fitch to BBB, Q1 2026) — reduces refinancing/rate risk relative to prior years.
3. Reserve base growth: proved reserves +7% YoY to 28.0 Tcfe (including Olympus assets), PV-10 $26bn at the SEC price deck
   ($3.39/MMBtu) and $31bn at recent strip (FY2025 10-K/8-K, reviewed by independent engineer Netherland, Sewell &
   Associates) — a real, third-party-audited asset base, not management's own estimate.

**Bear (3 points):**
1. 75% of 2026 production is unhedged; a reversion to 2024-like realized prices ($2.74/Mcfe vs $3.19 in 2025) would cut FCF
   sharply — FY2024 FCF-attributable was only $684M vs FY2025's $2,503M, a 3.7x difference driven almost entirely by price.
2. GAAP earnings are not a clean signal quarter to quarter (derivative mark-to-market swings of $500M+ per quarter are
   common), which raises the risk of the market (or a less careful analyst) mis-reading a single quarter's headline EPS.
3. Capital is being deployed into pipeline joint-venture ownership increases (MVP) and midstream bolt-ons with related
   parties (Blackstone Credit & Insurance co-invests in the Midstream JV) — reasonable so far, but a pattern to watch for
   related-party pricing discipline as the JV structure grows.

## 9. Key risks & kill criteria (measurable)
1. FY2026 total sales-volume guidance is cut below the current 2,375–2,450 Bcfe range (a reversal of the Q2 2026 raise).
2. Realized price differential widens beyond the guided ($0.55)–($0.35)/Mcf full-year range for two consecutive quarters
   (signals a basis/egress problem, not just a price-level issue).
3. Consolidated net debt rises back above $7.0bn (i.e., gives back more than half of the 2026 deleveraging) without a
   specific, disclosed growth-capex reason.
4. Hedged percentage of the following year's production falls below 15% by the Q4 earnings release (i.e., EQT becomes
   *less* hedged than the 25% level disclosed for 2026, raising cash-flow-at-risk into an unhedged down-cycle).
5. MVP Southgate or the LNG offtake SPA volumes are delayed past their disclosed 2026 (Southgate) / 2028 (LNG) start dates
   by more than two quarters, without a replacement demand contract.

## 10. Catalysts & calendar
- Next earnings date: **2026-10-20** (Q3 2026, per d4 snapshot `next_earnings_date`, not flagged as an estimate).
- MVP Southgate targeted completion: year-end 2026 (company-disclosed acceleration).
- LNG offtake SPA volumes begin 2028.
- 2026 debentures ($115M) already repaid subsequent to Q2 2026 quarter-end (per the Q2 2026 release).

## 11. Red-flag scan
- **Legal proceedings:** the Q2 2026 10-Q (Item 1, Part II) states "there are no material updates to the matters
  previously disclosed" in the FY2025 10-K and prior 10-Q Legal Proceedings sections — no new material litigation surfaced
  in the filing itself.
- **Auditor/restatement/going concern:** none disclosed in the reviewed filings; no material-weakness language found.
- **Insider ownership/selling:** `y_heldPercentInsiders` in the d4 snapshot is 0.9% — low insider ownership is itself worth
  noting (limited skin in the game at the individual level), though this is common for a company of EQT's size and history
  (it was not founder-led through this cycle). No Form 4 cluster-selling analysis was performed in this pass (time-boxed
  standard-depth diligence) — **data gap**, disclosed rather than silently omitted.
- **Related-party-adjacent transactions:** MVP JV ownership increase from/to the Blackstone-affiliated partner (§6/§8) —
  disclosed and priced at a pre-agreed option, not flagged as improper, but worth continued monitoring.

## 12. Sources
1. SEC EDGAR submissions index, CIK 0000033213: `https://data.sec.gov/submissions/CIK0000033213.json` (retrieved 2026-09-26).
2. SEC EDGAR XBRL companyfacts, CIK 0000033213: `https://data.sec.gov/api/xbrl/companyfacts/CIK0000033213.json` (retrieved 2026-09-26).
3. EQT 8-K Ex-99.1, Q2 2026 results, filed 2026-07-22: `https://www.sec.gov/Archives/edgar/data/33213/000003321326000041/ex9916302026earningsrelease.htm`.
4. EQT 8-K Ex-99.1, Q1 2026 results, filed 2026-04-22: `https://www.sec.gov/Archives/edgar/data/33213/000003321326000028/ex9913312026earningsrelease.htm`.
5. EQT 8-K Ex-99.1, Q4/FY2025 results & 2026 guidance, filed 2026-02-18: `https://www.sec.gov/Archives/edgar/data/33213/000003321326000012/ex99112312025earningsrelea.htm`.
6. EQT 8-K Ex-99.1, Q3 2025 results, filed 2025-10-22: `https://www.sec.gov/Archives/edgar/data/33213/000003321325000047/ex9919302025earningsrelease.htm`.
7. EQT Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-22: `https://www.sec.gov/Archives/edgar/data/33213/000003321326000043/eqt-20260630.htm`.
8. `v4/data/b1_live_scores.csv` and `v4/data/d4_live_snapshot.parquet` (as_of 2026-09-25), and `v4/outputs/Q04_triage.json`.
9. `v4/outputs/v1_valuation_table.csv` (checked; no EQT row as of this writing).

## Data basis, recency and disclaimer
Most recent period incorporated: 10-Q for the quarter ended 2026-06-30 (filed 2026-07-22) and the 8-K earnings release
dated 2026-07-21. Events checked to 2026-09-25 close (no EQT-specific 8-Ks filed between 2026-07-22 and 2026-09-25 in the
reviewed submissions feed). GAAP vs adjusted figures are labelled throughout; all non-GAAP figures ("adjusted," "FCF
attributable to EQT," "adjusted EBITDA") are the company's own defined non-GAAP measures, reconciled in the source
earnings releases. This is research, not personalized investment advice; not personalised investment advice.
