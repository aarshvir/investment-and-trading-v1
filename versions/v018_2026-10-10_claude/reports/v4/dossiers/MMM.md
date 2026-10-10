# MMM — 3M Company (F104, wave 6)

## 1. Verdict
**INCLUDE-SMALL** — a de-risked industrial conglomerate whose litigation overhang (PFAS, Combat Arms earplugs) is
now largely reserved and, for the earplug MDL, dismissed; the reverse DCF implies close-to-zero long-run growth,
below a plausible mid-single-digit base case. Reservation: GAAP results are still noisy from residual litigation
and divestiture charges each quarter, book equity is unusually thin from years of litigation charges and buybacks,
and the ~$7.4bn residual PFAS/environmental liability is not fully extinguished. Thesis horizon: 12–36 months.

## 2. Business in plain English
3M makes industrial, safety and consumer products across three segments: Safety & Industrial (abrasives,
adhesives, personal protective equipment), Transportation & Electronics, and Consumer (Post-it, Scotch, home
care). It sells through both B2B industrial channels and B2C retail, monetizing decades of proprietary materials-
science IP and manufacturing scale. Its competitive position is a broad, sticky industrial-products portfolio with
high switching costs in many niches (e.g., respirators, industrial tapes), though it is not a single-category
leader the way a pure-play competitor might be.

## 3. Why the model likes it / durability
b1_live_scores.csv (25 Sep 2026): composite percentile 47.6th (decile 5, middling — not a standout quant name),
pct_gp_a 49.0th, pct_roe 97.1st (very high, but see §6 caveat on thin equity), pct_ep 48.2th, pct_fcfp 45.5th,
pct_mom_12_1 30.7th (below-median momentum), live_rank 261/1172. MMM entered diligence via triage (Q10: quality
4/5, growth 3/5, price_vs_growth 3/5, ADVANCE=True; red flag noted: "residual PFAS/earplug litigation tail beyond
the roughly $16bn already reserved/settled"). The very high pct_roe (97th percentile) is **not** a clean quality
signal here — 3M's stockholders' equity has been driven down to $2.95bn (30 Jun 2026, consolidated) by years of
litigation charges and buybacks, so ROE is mechanically inflated by a shrunken equity base, not by an unusually
capital-light business model. This is a data-conflict worth flagging explicitly: the model's quality read on ROE
overstates durability here.

## 4. Last quarters' results (consolidated, GAAP; SEC XBRL companyfacts CIK 0000066740, cross-checked against the
Q2 2026 earnings release, filed 2026-07-21)
| Quarter end | Revenue ($mm) | Op. income ($mm) | Op. margin | Net income ($mm) |
|---|---|---|---|---|
| 2024-03-31 | — | 1,149 | — | — |
| 2024-06-30 | 6,255 | 1,272 | 20.3% | 1,145 |
| 2024-09-30 | 6,294 | 1,316 | 20.9% | 1,372 |
| 2024-12-31 (FY10-K qtr) | 6,010 | — | — | 728 |
| 2025-03-31 | 5,954 | 1,246 | 20.9% | 1,116 |
| 2025-06-30 | 6,344 | 1,140 | 18.0% | 723 |
| 2025-09-30 | 6,517 | 1,447 | 22.2% | 834 |
| 2026-03-31 | 6,030 | 1,397 | 23.2% | 653 |
| 2026-06-30 | 6,500 | 984 | 15.1% | 933 (GAAP EPS $1.78) |

**GAAP vs adjusted (Q2 2026)**: GAAP operating margin 15.1% (down 290bps YoY) vs. **adjusted** operating margin
24.9% (up 40bps YoY) — a wide and explicitly disclosed gap. GAAP EPS $1.78 (+33% YoY) vs. adjusted EPS $2.40
(+11% YoY); the GAAP quarter was reduced by $0.44/share of "net costs for significant litigation and PFAS exit"
and $0.61/share of "loss on business divestitures" (3M Q2 2026 earnings release, Ex. 99.1). Organic growth by
segment, Q2 2026: Safety & Industrial +8.2%, Transportation & Electronics +5.9%, Consumer **−2.1%** — the Consumer
segment (Post-it, Scotch, home care) is shrinking organically even as the industrial segments grow; this
divergence is a genuine mixed signal the model's composite score does not see.

## 5. Guidance track record
- **FY2026 adjusted EPS**: raised in the Q2 2026 release (21 Jul 2026) to **$8.80–$8.95**, up from the prior guide
  of **$8.50–$8.70** given after Q1 2026 — an explicit, quoted raise (3M Q2 2026 press release).
- **FY2026 adjusted organic sales growth**: raised to ">3.5%"; adjusted total sales growth ">4.5%".
- **FY2026 adjusted operating margin expansion**: guided 70–80bps, in line with the trend already shown in
  adjusted results (Q2 2026 adjusted margin +40bps YoY, cumulative H1 progress toward the full-year target).
- **FY2026 adjusted free cash flow**: guided to >100% conversion of adjusted net income, supported by adjusted
  operating cash flow guidance of $5.8–$6.0bn (per company commentary reported by TradingView/3M IR, cross-checked
  against the operating-cash-flow trend in companyfacts, which shows Q1 OCF swinging from **−$79mm** in the
  2025 quarter to **+$574mm** in the 2026 quarter — a large favorable swing, partly litigation-payment timing).
- No missed guide identified in the last two years in the sources reviewed; guidance has been raised at both
  Q1 2026 and Q2 2026 releases.

## 6. Earnings quality & balance sheet (consolidated, MMM CIK 0000066740)
- **FCF conversion**: d4 snapshot TTM free cash flow $6.35bn vs. TTM net income (trailing EPS $5.63 × ~516mn
  diluted shares ≈ $2.9bn) — FCF well above reported net income, consistent with management's own >100%
  conversion framing, but this dossier notes the TTM Yahoo figure likely mixes in one-off divestiture cash flows;
  a more conservative, guidance-based FCF proxy (adjusted OCF $5.8–6.0bn less ~$0.9bn TTM capex ≈ **$4.9–5.1bn**)
  is used for the reverse DCF in §7 instead of the raw $6.35bn TTM figure.
- **Leverage (consolidated)**: long-term debt $10.904bn + current debt $1.647bn = ~$12.55bn total debt at 30 Jun
  2026, against cash $5.303bn (consolidated balance sheet, XBRL) → **net debt ≈ $7.25bn**. **[Corrected 2026-10-09: cash was $2.955bn plus $0.375bn marketable securities at 30 Jun 2026 (10-Q 0000066740-26-000246), so net debt is ~$9.6bn, not ~$7.25bn]** S&P's own
  adjusted debt/EBITDA estimate is **~2.5–2.6x**, below its 3x downgrade threshold, with a stable outlook
  (Investing.com, citing S&P; the S&P adjusted figure differs from a simple GAAP-debt/GAAP-EBITDA ratio because
  S&P's own adjustments capitalize leases/pensions and are not independently re-derived here — disclosed
  limitation).
- **PFAS/environmental liability**: "other environmental liabilities" of **$7.4bn** at 30 Jun 2026 ($2.9bn current
  + $4.5bn non-current, consolidated balance sheet, per the Q2 2026 10-Q), down from the prior year, reflecting
  the $10.3bn present-value accrual for the Public Water Suppliers (PWS) PFAS settlement being paid down over its
  13-year schedule. **Combat Arms earplug litigation**: the federal MDL (2873) was **completely dismissed on 28
  April 2026**, closing all 391,283 cases that had been filed in that MDL (per search-aggregated 3M/press
  reporting; not independently verified against the dismissal order itself — disclosed as a secondary-source
  fact, high confidence given consistency across sources, but flagged per the wave-3 lesson on dated filing
  claims).
- **Consolidated stockholders' equity** has fallen sharply — $4.628bn (30 Sep 2025) → $4.702bn (31 Dec 2025) →
  $3.263bn (31 Mar 2026) → **$2.952bn (30 Jun 2026)**, consolidated — driven by continuing litigation charges, buybacks
  ($1.999bn of stock repurchased in Q1 2026 alone, per XBRL) and dividends outrunning net income. This is thin
  relative to $34.9bn total assets, though total liabilities ($31.9bn) are still well covered by cash flow, not a
  going-concern signal, but it does mean a further adverse litigation or environmental charge would show up
  disproportionately in the equity account.
- **Capex** is modest and stable (~$225–236mm/quarter, i.e. ~3.5% of revenue), consistent with a mature industrial
  franchise, not a name requiring heavy reinvestment.

## 7. Valuation — reverse DCF and reconciliation with V1
**No V1 row exists for MMM** in `v4/outputs/v1_valuation_table.csv` (checked directly) → **v1_verdict = null**.

Reverse DCF (two-stage, N=10 years at growth g, terminal growth 2.5%, discount rate 7.9% — an industrial-average **[Corrected 2026-10-09: 7.9% is not Treasury 5.17% plus a stated premium; see Correction section]**
WACC estimate for a mid-2x-levered, BBB/A-range industrial issuer), solving for g against enterprise value
($94.30bn, d4 snapshot):
- Using the **normalized guidance-based FCF** ($4.9–5.1bn, §6), implied growth ≈ **2.2–2.7%/yr** for 10 years. **[Corrected 2026-10-09: restated: ~4.5% (EV incl. $7.4bn environmental liability, WACC 8.6%) to ~5.0% (equity basis, 9.3%); up to ~7.8% if PFAS payments are charged to cash flow]**
- (For context: using the raw, likely one-off-inflated TTM FCF of $6.35bn, implied growth is roughly **flat to
  slightly negative** — an even cheaper reading this dossier does not rely on, since that FCF figure is judged
  unreliable.)

**Base case** (evidence-based): FY2026 adjusted EPS growth is already guided at ~11% at the midpoint of the raised
range, and adjusted operating margin is expanding 70–80bps; but this is recovery-phase growth off a litigation-
depressed base, not a sustainable long-run rate for a mature, ~$26bn-revenue industrial conglomerate. A reasonable
10-year base case is **mid-single-digit (4–6%)** underlying FCF/EPS growth once the recovery phase normalizes
(low-single-digit organic growth + margin recovery + buybacks). **The reverse-DCF implied growth (2.2–2.7%) is
below this base case → supports an INCLUDE-type verdict on valuation grounds.** **[Corrected 2026-10-09: restated implied growth ~4.5-5.0% is IN LINE with the 4-6% base, so the valuation leg does not support INCLUDE on its own]** The reservation (INCLUDE-SMALL,
not INCLUDE) is earnings-quality and balance-sheet related: GAAP results are still routinely hit by litigation/
divestiture charges, book equity is thin, and the ~$7.4bn residual environmental liability, while reserved, is
large enough that a materially adverse development (e.g., a new PFAS claim class outside the current settlement
scope) could still move the stock meaningfully — a risk the reverse DCF's terminal-value math does not capture.

**Scenario basis** (annualised 3-yr total returns): starting point trailing EPS $5.63 (GAAP) / adjusted EPS run-
rate ~$8.85 (FY2026 guide midpoint), dividend yield ~1.8% (dividendRate $3.12), exit multiple assumption 16–19x
adjusted EPS (current forward P/E 17.3x per d4):
- **Bear**: a new, unreserved PFAS or environmental claim emerges, adjusted EPS growth stalls, multiple compresses
  to 14x → ≈ **−6%/yr**.
- **Base**: FY2026 guidance is met, adjusted EPS growth moderates to mid-single-digit in FY2027 as the recovery
  phase completes, multiple holds ~17x → ≈ **+7%/yr**.
- **Bull**: margin recovery runs further than guided, buybacks accelerate as litigation costs roll off, multiple
  re-rates to 19–20x → ≈ **+16%/yr**.

## 8. Bull case
1. FY2026 adjusted EPS guidance has been raised twice this year (Q1 and Q2), and adjusted operating margin is
   expanding toward the 70–80bp full-year target — real, guided-and-delivered operating momentum.
2. The single largest litigation overhang, the Combat Arms earplug MDL, is fully dismissed (391,283 cases
   closed, April 2026); the PFAS PWS settlement is a known, scheduled 13-year cash outflow, not an open-ended
   liability.
3. Reverse DCF implies close to zero real long-run growth priced in on a normalized-FCF basis — a low bar for a **[Corrected 2026-10-09: restated: ~4.5-5.0% a year is priced in, not close to zero]**
   business still guiding double-digit adjusted EPS growth this year.

## 9. Bear case
1. GAAP operating margin (15.1% in Q2 2026, down 290bps YoY) and consolidated stockholders' equity ($2.95bn, down
   from $4.7bn nine months earlier) show the litigation/divestiture drag is still large and recurring in GAAP terms, even as
   adjusted results improve — a name that requires trusting management's non-GAAP add-backs.
2. $7.4bn of residual "other environmental liabilities" remains on the balance sheet; the company itself states it
   "is unable to estimate a possible loss or range of possible loss in excess of the amounts accrued" — i.e. tail
   risk beyond the reserve is explicitly not bounded by the company.
3. The Consumer segment is organically shrinking (−2.1% in Q2 2026) while Safety & Industrial and Transportation &
   Electronics carry the growth — a segment-mix risk if industrial demand softens.

## 10. Key risks & kill criteria (measurable)
1. GAAP operating margin below 15% for two consecutive quarters (current: 15.1% in Q2 2026, near this threshold
   already).
2. Consolidated stockholders' equity falls below $2.0bn (from $2.95bn at 30 Jun 2026), signalling a fresh, large
   litigation or environmental charge beyond current reserves.
3. S&P-adjusted debt/EBITDA rises above 3.0x (vs. ~2.5–2.6x now — S&P's own stated downgrade threshold).
4. FY2026 adjusted EPS guidance ($8.80–$8.95) is cut at either the Q3 2026 (Oct 20) or Q4 2026 release.
5. Consumer segment organic growth remains negative for three consecutive quarters (currently −2.1% in Q2 2026).

## 11. Catalysts & calendar
- Next earnings: **2026-10-20** (Q3 2026, per d4 snapshot next_earnings_date).
- Any new PFAS-related claims filed outside the current PWS settlement scope (state AG suits, international
  claims) — monitor via subsequent 10-Q litigation footnotes.
- Continued paydown schedule of the $10.3bn PWS settlement (13-year schedule) — cash-flow visibility item.

## 12. Red-flag scan
- Litigation: PFAS (Public Water Suppliers settlement, $10.3bn PV accrual, final court approval reported) and
  Combat Arms earplugs (federal MDL fully dismissed 28 Apr 2026) are the two dominant legal matters; both are
  reserved/resolved rather than open-ended, but the company's own 10-Q language states it cannot bound losses
  beyond current accruals (see §9).
- No auditor change, restatement, or going-concern language identified in this pass.
- No new SEC/DOJ investigation identified in the sources reviewed (disclosed as a negative-result check, not
  exhaustive).
- Insider selling patterns and short-seller reports were not separately checked this pass — disclosed limitation
  given the ~40-minute time box.

## 13. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (quarter ended 2026-06-30), per the Q2 2026 earnings release (SEC 8-K
Ex. 99.1, filed 2026-07-21) and SEC XBRL companyfacts (CIK 0000066740, retrieved 2026-09-27). Events checked to
2026-09-25 close. GAAP figures are labelled GAAP; adjusted (non-GAAP) figures are labelled "adjusted" throughout.
S&P's adjusted debt/EBITDA figure is a rating-agency estimate, not independently re-derived from a lease/pension-
adjusted EBITDA calculation — disclosed limitation. **Research, not personal investment advice.**

## Sources
1. SEC XBRL companyfacts, CIK 0000066740, retrieved 2026-09-27: https://data.sec.gov/api/xbrl/companyfacts/CIK0000066740.json
2. 3M Q2 2026 earnings release (8-K Ex. 99.1, filed 2026-07-21): https://www.sec.gov/Archives/edgar/data/66740/000006674026000242/q22026-8kerexx991.htm
3. 3M IR, "3M Reports Second-Quarter 2026 Results; Increases Full-Year Guidance": https://investors.3m.com/news-events/press-releases/detail/1938/3m-reports-second-quarter-2026-results-increases-full-year
4. TradingView News summary of 3M Q2 2026 results (adjusted OCF guidance cross-check): https://www.tradingview.com/news/tradingview:ca6c01ea81b84:0-3m-posts-q2-2026-revenue-6-5b-adjusted-eps-2-40-raises-full-year-guidance/
5. Investing.com, "3M outlook revised to stable due to reduced leverage, S&P affirms ratings": https://www.investing.com/news/stock-market-news/3m-outlook-revised-to-stable-due-to-reduced-leverage-sp-affirms-ratings-93CH-3902939
6. lawsuit-information-center.com, 3M Combat Arms earplug MDL dismissal timeline (secondary source, cross-checked
   against multiple search results for consistency).
7. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (25 Sep 2026 snapshot) — quant context.
8. v4/outputs/Q10_triage.json — MMM triage entry.

## Correction (verification DV28, 2026-10-09)

1. **Cash and net debt (Sec 6).** Wrong text: "cash $5.303bn ... net debt ≈ $7.25bn". Correct: cash and cash equivalents $2,955M (31 Dec 2025: $5,235M) plus marketable securities $375M; short-term borrowings and current portion of long-term debt $1,647M; long-term debt $10,904M; net debt is ~$9.6bn ($9.2bn net of marketable securities). Source: 10-Q 0000066740-26-000246, consolidated balance sheet. The S&P adjusted debt/EBITDA of 2.5-2.6x is from a secondary source and was not verified.
2. **Reverse DCF (Sec 7, Sec 8 bull case 3).** Wrong text: discount rate 7.9% "industrial-average WACC", enterprise value $94.30bn, normalized FCF $4.9-5.1bn, implied growth 2.2-2.7%, "below this base case". The arithmetic reproduces (2.16-2.68%), but: (a) 7.9% is not tied to the 10-year Treasury (5.17% on 25 Sep 2026) plus a stated equity premium; at a cost of equity of 9.3% (5.17% + 4.14% x Blume beta ~1.0, beta assumed) and ~12.6% debt weight the WACC is ~8.6%; (b) the cash flow is the company's ADJUSTED operating cash flow guide ($5.8-6.0bn, in the 21 Jul 2026 release), which excludes litigation and PFAS payments (GAAP operating cash flow was $2.3bn in FY2025 and $1.56bn in H1 2026), while the $7.4bn "other environmental liabilities" ($2.9bn of it current) is not in the enterprise value; (c) SBC ($225M in FY2025) is not deducted. Restated: EV $101.7bn, FCFF ~$5.2bn, WACC 8.6% gives implied 10-year growth of ~4.5%; equity basis (market cap ~$87.05bn, FCF after SBC $4.78bn, 9.3%) gives ~5.0%; charging ~$0.9bn a year of PFAS payments to cash flow gives ~7.8%. Implied growth is therefore in line with or above the dossier's 4-6% base, not below it: implied_vs_base changes from **below** to **in_line** and the "close to zero growth priced in" statement in the bull case is withdrawn. Verdict stays INCLUDE-SMALL in this file but its valuation leg is much weaker than stated; the case now rests on earnings momentum and litigation de-risking, not on cheapness. F104_summary.json updated.
3. **Minor.** The Q2 2026 GAAP-to-adjusted bridge also contains a $0.60 per share gain from the increase in value of the Solventum stake and $0.15 of transformation costs, which Sec 4 omits when it cites only the $0.44 litigation/PFAS and $0.61 divestiture items. The Combat Arms MDL dismissal (28 Apr 2026, 391,283 cases) is not in the 10-Q and remains secondary-sourced. Adjusted operating cash flow guidance of $5.8-6.0bn is in the company's own release (cited in the dossier to TradingView).
