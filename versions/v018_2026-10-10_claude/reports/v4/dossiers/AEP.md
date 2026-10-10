# American Electric Power (AEP) — Diligence Dossier (Agent F82, standard depth)

## 1. Verdict
**INCLUDE-SMALL** (half weight), thesis horizon **24–36 months**. Reservation: leverage is the highest of this
batch (5.9x consolidated net debt/EBITDA, ~$52.6bn total consolidated long-term debt+current at Q1 2026) **[Corrected 2026-10-06: at Q1 2026 long-term debt $46.85bn plus current $2.70bn plus short-term $1.56bn was $51.1bn; at 30 Jun 2026 (10-Q acc. 0000004904-26-000059) total debt was $52.8bn]** funding a genuinely large,
real, contracted capex/load-growth program — the growth case is credible and guidance was just raised, but the
balance sheet has less room for a surprise than SO or TJX, and V1's own base case is a small negative 3-year
return despite a "fair" verdict.

## 2. Business in plain English
AEP is a multi-state regulated electric utility holding company (Ohio, Texas, Indiana, Michigan, West
Virginia, Virginia, Kentucky, Oklahoma, Arkansas, Louisiana, Tennessee via various operating subsidiaries) plus
a regulated transmission segment. It earns a state/FERC-approved return on invested rate base; its current
growth story is unusually strong for a utility because of contracted hyperscaler data-center and industrial
load, concentrated in Ohio, Indiana and Texas.

## 3. Why the model likes it / durability
Triage (`outputs/Q14_triage.json`) scored AEP quality 4/5, growth 4/5, price-vs-growth 3/5: "19% forward EPS
growth is well above typical regulated-utility rates ... 18x NTM P/E is fair, not excessive." `b1_live_scores.csv`
composite decile 9/quintile 5 (model rank 68 — near the top of the scored universe), driven by strong quality
(pct_gp_a 0.76, pct_roe 0.56) and reasonable value/momentum. This is a real, filing-confirmed growth
acceleration, not a factor artefact: AEP's own Q2 2026 release confirms **6 GW of newly signed load agreements
in the quarter alone** (bringing contracted load to 69 GW through 2030) and a **$78bn five-year capital plan**,
and management **raised** full-year operating EPS guidance and **reaffirmed** a 7–9% long-term growth rate
(with an internal expectation of >9% CAGR) through 2030 — durable as long as signed load agreements convert to
rate base on schedule.

## 4. Recent results (consolidated AEP, GAAP unless noted)
Source: XBRL companyfacts (SEC tags `Revenues`, `EarningsPerShareDiluted`) through Q1 2026 (10-Q filed 2026-05-05, accession 0000004904-26-000034), plus the Q2 2026 earnings press release (8-K exhibit filed 2026-07-30, accession 0000004904-26-000055) for the most recent quarter, which had not yet propagated into SEC's structured XBRL
frames as of this diligence date.

| Quarter | GAAP diluted EPS | Operating (adj.) EPS |
|---|---|---|
| Q3 2024 | 1.80 | n/a (not re-pulled) |
| FY2024 (10-K) | 5.58 | n/a |
| Q1 2025 | 1.50 | n/a |
| Q2 2025 | **2.29** | 1.43 |
| Q3 2025 | 1.81 | n/a |
| FY2025 (10-K) | 6.66 | n/a |
| Q1 2026 | 1.60 | n/a |
| **Q2 2026** (press release) | **1.31** | **1.36** |

**Data conflict / adverse fact:** GAAP diluted EPS fell from $2.29 (Q2 2025) to $1.31 (Q2 2026), a 43% YoY
decline, while **operating (non-GAAP) EPS fell only modestly**, from $1.43 to $1.36 (−5%), and guidance was
simultaneously **raised**. The $0.86 gap between the GAAP and operating swing implies Q2 2025 GAAP EPS included
a large one-time item (commonly a divestiture gain at AEP, e.g., prior transmission-company stake sales) that
this pass did not identify by name from the primary document — **gap, flag for fact-check**: do not read the
headline GAAP EPS decline as an operating deterioration without confirming the one-time item's identity and
that it is correctly excluded from "operating" EPS.

Revenue: Q2 2026 **$5.45bn**, up from $5.09bn a year earlier (+7.0%), consistent with rate-base growth and
early contracted-load contribution.

## 5. Guidance track record
Q2 2026 release: full-year 2026 operating EPS guidance **raised to $6.25–$6.55** from the prior **$6.15–$6.45**
(both ranges quoted directly from the press release) — a genuine, confirmed raise, not an assertion. Long-term
growth rate **reaffirmed at 7–9% through 2030**, with management explicitly flagging an internal expectation of
**>9% CAGR**. Prior quarters' guidance releases (Q1 2026, Q4 2025) were not independently re-pulled this pass —
**gap, time-boxed at standard depth**; only the most recent raise is confirmed from a primary source.

## 6. Earnings quality & balance sheet (entity: **consolidated American Electric Power Co.**, from 10-Q tables)
- Long-term debt (consolidated, `LongTermDebtNoncurrent`): **$46.85bn** at 2026-03-31 (Q1 2026 10-Q filed 2026-05-05, accession 0000004904-26-000034 — the latest consolidated balance-sheet date with structured
  XBRL available; Q2 2026 10-Q filed 2026-07-30, accession 0000004904-26-000059, was not pulled line-by-line
  this pass), up from $38.8bn a year earlier (+21% YoY) — a large, real leverage
  increase funding the capex ramp, consistent with the $78bn five-year plan.
- Cash and cash equivalents (consolidated): **$306mn** at 2026-03-31 — thin, as is typical for a utility
  running on revolvers/commercial paper, but leaves little cushion against a financing-market disruption.
- Stockholders' equity (consolidated): **$31.8bn** at 2026-03-31, up from $27.3bn a year earlier — equity is
  growing but more slowly (+16.5% YoY) than debt (+21% YoY): **the balance sheet is leveraging up faster on
  the debt side than the equity side to fund growth**, the single biggest fact to watch.
- `net_debt_to_ebitda` per `triage_cards.csv`: **5.9x** — the highest in this batch (SO 5.2x, TJX 0.9x).
- `fcf_yield` is negative (−9.3% per `triage_cards.csv`), expected given the capex program, but combined with
  rising leverage this is the batch's clearest "watch the financing" item.

## 7. Valuation snapshot and reverse DCF, reconciled with V1
AEP **does** have a systematic valuation row (`v1_valuation_table.csv`/`v1_valuation.json`): NTM P/E **17.58x**
(own-history percentile 37.3 — i.e., cheaper than its own recent median, not expensive on that basis), peer
median 16.08x, implied perpetual growth **−0.44%**, delivered 5y ROE 7.28%, consensus FY1 growth 6.7%, WACC/CoE
used **5.42%**, bear/base/bull 3y annualised returns **−16.2% / −1.9% / +13.2%**, street_flag "base 3y value
below Street 12m low target", **verdict: fair**.

**This dossier's reverse-DCF check:** earnings yield = 1/17.58 = 5.69%. Implied growth ≈ WACC (5.42%) −
earnings yield (5.69%) ≈ **−0.27%**, closely matching V1's −0.44% (small difference from rounding/data-vintage,
not a methodology conflict) — **the reverse-DCF arithmetic itself checks out.**

**Where I disagree, with a primary-source number:** V1's 5.42% WACC looks low for a utility carrying 5.9x net
debt/EBITDA and debt growing faster than equity (see §6); a more conventional blended WACC (≈60% debt at ~5%
after-tax cost, ≈40% equity at ~10% cost of equity) is closer to **6.4–7.0%**, which would push implied growth
up toward **~1–2%** — still **well below** AEP's own guided 7–9% long-term growth and the 6.7% consensus FY1
growth V1 itself records. **Net effect: whichever reasonable WACC is used, implied growth stays materially
below both guidance and consensus, so the "fair, not expensive" verdict holds even under my higher-WACC
correction** — I am not overriding V1's verdict, only flagging that the precise implied-growth number is
sensitive to the WACC assumption. `dossier_view`: **fair**; `consistent`: **true**. **[Corrected 2026-10-06: the reverse DCF treated earnings as cash (earnings yield against a 5.42% WACC that rests on a 4.08% cost of debt below the 5.17% Treasury); on a dividend basis the price implies about 6.0%/yr, implied vs base is IN LINE, see Correction section]**

- **Bear (V1):** −16.2%/yr — a leverage-driven de-rating scenario (credit downgrade risk given rising debt/
  equity growth gap) combined with load-growth pipeline slippage.
- **Base (V1):** −1.9%/yr — modest negative even with guidance delivered, because the multiple is assumed to
  compress from today's level toward a more normal utility multiple as growth normalizes post-2030. **[Corrected 2026-10-06: V1's base path has EPS falling from $6.73 to $5.36 in three years, which contradicts the raised guidance; restated base +7.0%/yr, see Correction section]**
- **Bull (V1):** +13.2%/yr — 69 GW of contracted load converts to rate base on schedule, multiple holds or
  re-rates toward growth-utility peers (e.g., a CEG/VST-style premium).

## 8. Bull case
1. 69 GW of contracted load through 2030 (6 GW added just in Q2 2026) is filing-confirmed, not aspirational,
   and concentrated in the fastest-growing US utility demand pockets (Ohio, Indiana, Texas).
2. Guidance was just **raised** (not merely reaffirmed) with a long-term 7–9% (internally >9%) growth target —
   an unusually strong growth rate for a regulated utility.
3. NTM P/E (17.6x) sits below its own 5–10y history (37th percentile) and below the reverse-DCF's implied
   growth relative to guidance — the market has not yet fully re-rated AEP for the load-growth story.

## 9. Bear case
1. Consolidated long-term debt grew 21% YoY vs consolidated equity growth of only 16.5% YoY — the balance
   sheet is leveraging up faster than it is capitalizing, and consolidated net debt/EBITDA (5.9x) is already
   the highest in this batch; a credit-rating
   pressure point if load agreements slip.
2. The GAAP EPS decline (−43% YoY in Q2 2026) is a real headline number that a less careful reader could
   misinterpret; this dossier could not identify the specific one-time 2025 item driving the gap — **that gap
   itself is a diligence risk** until closed.
3. V1's own base-case 3-year return is **negative** (−1.9%/yr) despite a "fair" verdict — the systematic model
   sees more downside risk (bear −16.2%) than upside (bull +13.2%) is worth at the current multiple.

## 10. Key risks & kill criteria (measurable)
1. Consolidated net debt/EBITDA rises above 6.5x (current 5.9x) without a credit-rating-neutral equity raise alongside it.
2. Any of the newly signed 6 GW (Q2 2026) or the broader 69 GW contracted-load pipeline is publicly cancelled
   or downsized by more than 10%.
3. Full-year operating EPS guidance is cut (not raised/reaffirmed) at either of the next two quarterly releases.
4. A credit-rating agency downgrades AEP or a major operating subsidiary by one notch.
5. Operating EPS growth (ex the identified one-time items) falls below 5% for two consecutive quarters against
   the 7–9% long-term target.

## 11. Catalysts & calendar
Next quarterly release: Q3 2026 earnings, expected ~late October 2026 (AEP's Q3 2025 release was 2025-10-29;
specific 2026 date not confirmed from a primary IR calendar this pass — **gap**). A Form 8-K item 5.02
(2026-07-21, board/executive change) was noted in the filing list but not investigated this pass — **gap**.

## 12. Red-flag scan
- **Litigation:** wildfire liability is a disclosed risk factor (standard for US electric utilities post-2018
  Western wildfire litigation precedent) but no confirmed active 2026 wildfire lawsuit against AEP specifically
  was surfaced in this pass; historical class actions against AEP subsidiaries (e.g., climate-nuisance suits
  such as *New York v. AEP Service Corp.*) are long-resolved federal-preemption cases, not live financial risk.
  A full Item 3 (Legal Proceedings) read of the current 10-Q was not completed this pass — **gap**.
- **Leverage/credit:** flagged above as the primary watch item; no rating-agency action was independently
  checked this pass — **gap, priority follow-up**.
- No going-concern language, restatement, or auditor change identified in the documents reviewed this pass.

## 13. Data basis, recency and disclaimer
Most recent period incorporated: **Q2 2026** (quarter ended 2026-06-30) EPS/revenue from the Q2 2026 earnings
press release (SEC 8-K exhibit filed 2026-07-30, accession 0000004904-26-000055); most recent period with
structured, cross-checkable consolidated XBRL balance-sheet data is **Q1 2026** (10-Q filed 2026-05-05, accession 0000004904-26-000034) because SEC's XBRL companyfacts/frames API had not yet incorporated the
Q2 2026 10-Q (accession 0000004904-26-000059) as of this diligence date. Events checked to 2026-09-25 close via WebSearch; no
2026-dated new litigation or investigation was found. GAAP figures are labelled GAAP; "operating" (non-GAAP)
EPS is labelled as such per AEP's own reconciliation. **Research only; not personal investment advice.**

## Sources
1. SEC EDGAR submissions, CIK 0000004904: https://data.sec.gov/submissions/CIK0000004904.json (retrieved 2026-09-27)
2. SEC XBRL companyfacts, CIK 0000004904: https://data.sec.gov/api/xbrl/companyfacts/CIK0000004904.json (retrieved 2026-09-27)
3. AEP Q2 2026 earnings press release (8-K exhibit, filed 2026-07-30, accession 0000004904-26-000055):
   https://www.sec.gov/Archives/edgar/data/4904/000000490426000055/a2q20268kpressreleaseex991.htm
4. `v4/outputs/Q14_triage.json`, `v4/data/b1_live_scores.csv`, `v4/data/triage_cards.csv`,
   `v4/outputs/v1_valuation_table.csv`, `v4/outputs/v1_valuation.json` (internal, 2026-09-25 close)
5. WebSearch, "American Electric Power AEP litigation 2026 wildfire lawsuit Ohio Texas data center rate case", 2026-09-27

---
## Correction (verification DV02, 2026-10-06)
Research only; not personal advice. Original text above is unchanged. Sources: AEP 8-K Ex-99.1 earnings release acc. 0000004904-26-000055 (30 Jul 2026); 10-Q acc. 0000004904-26-000059 (30 Jun 2026) and -26-000034 (31 Mar 2026); XBRL companyfacts CIK 0000004904; v4\outputs1_valuation.json (AEP).

**Verified as stated:** Q2 2026 GAAP EPS $1.31 vs $2.29; operating EPS $1.36 vs $1.43; revenue $5,445M vs $5,087M (+7.0%); guidance raised to $6.25-6.55 from $6.15-6.45; 7-9% growth reaffirmed with a greater-than-9% CAGR expectation off the 2025 guidance midpoint; $78bn plan; 69 GW contracted load, 6 GW added in Q2; Q1 2026 long-term debt $46.85bn (+20.7% on $38.81bn), equity $31.81bn (+16.4%), cash $306M.

**Corrections**
- Section 4 open item (identity of the Q2 2025 one-off): the Q2 2026 release names it: "the 2025 transmission minority interest sale" (CEO statement); GAAP earnings by segment show AEP Transmission Holdco $578M in Q2 2025 vs $225M in Q2 2026. The GAAP decline is therefore a gain comparison, not operating deterioration, and the gap is closed.
- Sections 1 and 6, balance sheet: the 10-Q for 30 Jun 2026 (filed 30 Jul 2026, before the dossier date) shows total debt $52,836M (long-term $50,808M including current $2,821M, plus short-term $2,028M), long-term debt (non-current) $47,987M (+16.2% on $41,313M), AEP common equity $32,079M (+7.4% on $29,871M), cash $375M, debt 61.4% of total capitalisation. The "$52.6bn at Q1 2026" figure matches neither quarter (Q1: $51.1bn). The thesis point strengthens: debt now outgrows equity by 2x year on year, not 1.3x.
- Section 7, valuation method: implied growth = WACC less earnings yield treats EPS as distributable cash, but AEP's free cash flow is -$6.0bn (d4) and about a third of EPS is retained (payout 65.5%); V1's WACC of 5.42% uses a pre-tax cost of debt of 4.08%, below the 5.17% Treasury, and weights debt at 44%. V1's base scenario (revenue +2.2%/yr, margin 12.4% against 24% now, year-3 EPS $5.36 against NTM $6.73) cannot be reconciled with guidance that was just raised, so adopting V1's -16.2%/-1.9%/+13.2% as the scenario set was wrong.

**Recomputed (programme dividend method, as WEC re-assessment).** Price $118.35, annual dividend $3.80 ($0.95 a quarter), ten years constant growth then 3.0% terminal, cost of equity 5.17% + Blume 5-year weekly beta 0.50 x 4.14% = **7.24%** (V1 cost of equity 7.25%, identical). Implied 10-year dividend growth **6.05%** (4.5% at 6.7%, 7.5% at 7.7%). Base: guided 7-9% operating EPS CAGR to 2030 (8% midpoint; shares +1.9% a year are already inside per-share guidance) fading to 4.5% for 2031-35 = 6.25% average (value $121.7); haircut path 6% then 4.5% = 5.25% (value $111.5); 7% then 4.5% (value $116.5). Price divided by value 0.97-1.06. **Implied vs base: IN LINE** (was below).

**Scenarios restated (3-year annualised total return from $118.35; NTM EPS $6.73, dividends $3.80 growing).** Bear: EPS +2%/yr, exit 15.0x, dividend +3% = **+0.3%** (V1: -16.2%). Base: EPS +6%/yr (haircut to the 7-9% guide), exit 16.5x (peer median 16.1x), dividend +5% = **+7.0%** (V1: -1.9%). Bull: EPS +9%/yr, exit 18.5x, dividend +7% = **+13.8%** (V1: +13.2%). Base return is about the cost of equity, consistent with "in line".

**Verdict:** unchanged, INCLUDE-SMALL (in line, not below; leverage and financing remain the reservation). Updated entry in v4\outputs\F82_summary.json: valuation_view_vs_v1.implied_vs_base ("below" -> "in_line") and reconciliation, scenario_returns_3y, scenario_basis, data_conflicts note.
