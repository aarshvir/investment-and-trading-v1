# TJX Companies (TJX) — Diligence Dossier (Agent F82, standard depth)

## 1. Verdict
**INCLUDE** (full weight), thesis horizon **12–36 months**. Exceptional, durable off-price treasure-hunt model
(62% ROE, ~0.9x consolidated net debt/EBITDA), and the current price implies less growth than management's own guided/track
record, not more. **[Corrected 5 Oct 2026: implied 10-year FCF growth is ~8.3% at the dossier's own 8.5% cost of equity and ~10.6% at a 9.5% cost of equity consistent with the 25 Sep 2026 10-year Treasury (5.17%); that is in line with, not below, the 8-10% base case. Verdict restated to INCLUDE-SMALL; see Correction section]** No V1 systematic valuation row exists for TJX, so `v1_verdict = null`; reconciliation below is
this dossier's own reverse-DCF sense-check.

## 2. Business in plain English
TJX runs off-price apparel/home retail banners — T.J. Maxx, Marshalls, HomeGoods/HomeSense in the US, Winners/
HomeSense in Canada, and TK Maxx/HomeSense across Europe and Australia. It buys excess, close-out and
opportunistic inventory from brands at steep discounts and resells at 20–60% below department-store prices,
funding its own growth almost entirely from operating cash flow (buybacks + dividend) rather than debt.

## 3. Why the model likes it / durability
Triage (`outputs/Q01_triage.json`) scored TJX quality 5/5, growth 3/5, price-vs-growth 3/5: "62.2% ROE and
30.6% street upside for a proven, resilient compounder justify paying a full 23x NTM P/E even at only
high-single-digit forward EPS growth." `data/b1_live_scores.csv` composite decile 7/quintile 4 (model rank 185)
— quality factors (gp_a, roe, ocf_a all in the 60–80th percentile) are the main driver; momentum is weak
(pct_mom_12_1 ≈ 0.21, actual 12-1m return −6.2% per `triage_cards.csv`) and value is mediocre (P/E near the top
of its own range), which is consistent with "pay up for quality, don't expect it to be statistically cheap."
This is a durable-quality read, not a one-off: ROE has been consistently 50%+ for years off a low-capex, high
inventory-turn model — no evidence of an accounting artefact was found in this pass.

## 4. Recent results (consolidated TJX, GAAP unless noted; fiscal year ends ~late January)
Source: XBRL companyfacts (SEC tags `Revenues`, `NetIncomeLoss`) — **fully current through Q2 FY2027** (quarter
ended 2026-08-01, 10-Q filed 2026-08-28, accession 0000109198-26-000048) — cross-checked against the Q2 FY2027
earnings press release (8-K exhibit, filed 2026-08-19, accession 0000109198-26-000045).

| Quarter (fiscal) | Net income ($mn) | Comp. sales growth | GAAP diluted EPS |
|---|---|---|---|
| Q3 FY26 (Nov '24 q) | 1,297 | n/a (not pulled) | n/a |
| Q4/FY26 10-K (year to Feb '25) | 4,864 total FY | n/a | n/a |
| Q1 FY27 (May '26 q) | 1,036 | n/a (not pulled) | n/a |
| **Q2 FY27** (Aug '26 q, press release) | **1,243** (NI, XBRL) | **+4% consolidated** | **$1.36 GAAP / $1.22 adj.** | **[Corrected 27 Sep 2026: Q2 FY2027 net income is $1,520m; $1,243m is the prior-year Q2 FY2026 figure. See the Correction section below.]**
| Q3 FY26 (Nov '25 q) | 1,442 | n/a | n/a |
| FY26 (year to Jan '26, 10-K) | 5,494 total FY | n/a | n/a |

Q2 FY2027 (quarter ended 2026-08-01): net sales **$15.2bn**, up 5% YoY; gross margin **33.4%**, up 2.7pts;
adjusted gross margin 31.4% (+0.7pt) after backing out tariff-related items. GAAP diluted EPS **$1.36** (+24%
YoY) vs adjusted **$1.22** (+11% YoY ex a $0.14 one-time tariff-refund benefit) — **the GAAP figure is inflated
by a one-time item; the adjusted $1.22 is the better run-rate number** and this dossier uses adjusted EPS for
growth-rate purposes. Comp sales by segment: Marmaxx (US) +1% (soft — flagged by CEO as "below expectations"),
HomeGoods +7%, TJX Canada +6%, TJX International +7%.

## 5. Guidance track record
Full-year FY2027 guidance was **raised** at the Q2 FY2027 release: adjusted EPS **$5.15–$5.20** (excluding a
$0.16 tariff benefit), GAAP EPS **$5.31–$5.36**. The prior full-year range ahead of this raise was not
independently re-pulled from the Q1 FY2027 release in this pass — **gap, time-boxed at standard depth**; the
press-release framing ("raised full-year guidance") is taken from TJX's own characterization, not verified
against the specific prior numeric range. **[Corrected 5 Oct 2026: the prior FY27 range was $5.08-$5.15 (Q1 FY27 release, accession 0000109198-26-000023); the Q2 release raised GAAP EPS to $5.31-$5.36 and adjusted EPS (ex $0.16 tariff refund) to $5.15-$5.20, i.e. +$0.07 / +$0.05 on the adjusted basis]**

## 6. Earnings quality & balance sheet (entity: **consolidated TJX Companies**, from 10-Q tables)
- Long-term debt (consolidated, `LongTermDebtAndCapitalLeaseObligations`... actually tag used:
  `LongTermDebtNoncurrent`): **$1.87bn** at 2026-08-01 (Q2 FY2027 10-Q) — essentially flat since a 2025 paydown
  from ~$2.87bn (2025Q2) to ~$1.87bn (2025Q3 onward); very light for a company this size.
- Cash and cash equivalents (consolidated): **$6.00bn** at 2026-08-01, up from $4.64bn a year earlier.
- Stockholders' equity (consolidated): **$10.65bn** at 2026-08-01, up from $8.87bn a year earlier — equity is
  compounding despite heavy buybacks because retained earnings growth outpaces repurchases.
- `net_debt_to_ebitda` per `data/triage_cards.csv`: **0.9x** — very low leverage, a real balance-sheet
  strength versus the peer set.
- Q2 FY2027 shareholder returns: **$798mn** of buybacks (5.1mn shares) + **$529mn** of dividends in the
  quarter, funded from operating cash flow, not debt.
- FCF conversion: TJX's `fcf_yield` (triage_cards.csv) is a modest 3.1% against a 23x P/E — expected for a
  high-multiple compounder; SBC as % of revenue was not independently pulled this pass (**gap**). **[Corrected 5 Oct 2026: XBRL: FY26 operating cash flow $6,874m less capex $1,957m = FCF $4,917m, 89.5% of net income ($5,494m); FY25 $4,198m = 86%; trailing four quarters to 1 Aug 2026 FCF $5,876m (P/FCF 24.3x at $130.06). The 3.1% FCF yield in triage_cards.csv understates the trailing yield (4.1%), but trailing FCF is flattered by tariff-refund cash and working capital; a normalised yield is ~3.5%]**

## 7. Valuation snapshot and reverse DCF
Per `data/triage_cards.csv` (2026-09-25 close, $130.06): NTM P/E **23.1x** (trailing 24.1x), dividend yield
**1.4%**, Street 12-month upside **30.6%** (20 analysts), 1-year momentum **−6.2%**. No V1 row exists
(`v1_verdict = null`).

**Reverse DCF (Gordon-growth approximation on NTM earnings yield):** earnings yield = 1/23.1 = 4.33%. Using an
~8.5% cost-of-equity assumption typical for a low-beta, low-leverage large-cap retailer, implied perpetual
growth ≈ 8.5% − 4.33% ≈ **4.2%/yr**. TJX's own recent delivered growth (adjusted EPS +11% YoY in Q2 FY2027,
guided FY2027 adjusted EPS growth high-single-digit off ~$4.80 FY2026 base) is well above this implied rate.
**Implied growth (~4%) is below the evidence-based base case (~8–10% adjusted EPS growth, driven by ~1–2pts
buyback plus mid-single-digit comps plus modest margin gain)** — consistent with an INCLUDE. **[Corrected 5 Oct 2026: the 4.2% was a perpetual-growth earnings-yield shortcut compared with a 10-year growth base, which is not like-for-like; on a 10-year two-stage model the price implies ~8.3% (8.5% CoE) to ~10.6% (9.5% CoE), i.e. IN LINE with the 8-10% base, not below. implied_vs_base restated to in_line; verdict INCLUDE-SMALL. FY2026 adjusted EPS was $4.73 (Q4 FY26 release), not ~$4.80, so FY27 adjusted guidance of $5.15-5.20 is +8.9% to +9.9%]**

- **Bear:** Marmaxx (the largest US banner) stays stuck at ~1% comps, tariff costs are not fully offset once
  the one-time refund/benefit rolls off, margin gives back 100–150bps. **Annualised 3y return ≈ 2–4%**
  (1.4% yield + ~2–3% EPS growth, modest multiple compression toward 20x). **[Corrected 5 Oct 2026: restated 3y annualised bear is about -3%: EPS +4%/yr, exit multiple 19.5x trailing adjusted EPS, plus 1.5% dividend]**
- **Base:** Comps normalize to mid-single-digit across banners, adjusted EPS growth ~9–10% (buyback + margin),
  multiple holds ~23x. **Annualised 3y return ≈ 10–11%.** **[Corrected 5 Oct 2026: restated 3y annualised base is about +7.7%: adjusted EPS +9%/yr, exit 23.5x trailing adjusted EPS (25.4x now) given higher rates, plus 1.5% dividend; the original assumed the multiple holds]**
- **Bull:** HomeGoods/TJX International momentum (+6–7% comps) broadens to Marmaxx, adjusted EPS growth
  reaches low-teens, multiple re-rates to 25–26x on continued market-share gains from struggling department
  stores/mall retail. **Annualised 3y return ≈ 17–19%.** **[Corrected 5 Oct 2026: restated 3y annualised bull is about +14%: EPS +12%/yr, exit 26x trailing adjusted EPS, plus 1.5% dividend]**

## 8. Bull case
1. Balance sheet is nearly net-cash on a consolidated leverage basis (0.9x net debt/EBITDA) with $6.0bn cash — maximum
   optionality for continued buybacks even in a downturn.
2. Off-price format structurally gains share when consumers trade down and when department-store/mall
   competitors shrink footprint — a countercyclical hedge inside a cyclical sector.
3. International and HomeGoods banners (+6–7% comps) show the format still has real runway outside the
   mature, larger Marmaxx banner.

## 9. Bear case
1. Marmaxx, TJX's largest and most mature US banner, posted only +1% comps and was explicitly called out by
   the CEO as "below our expectations" — if this is share loss rather than a soft quarter, the largest banner
   is decelerating.
2. Reported Q2 GAAP EPS growth (+24%) is materially inflated by one-time tariff-refund items ($331mn refund
   received, $112mn of related accruals); investors extrapolating the GAAP growth rate would overstate the
   run-rate.
3. 23x NTM P/E is toward the high end of TJX's own trading range historically (own-history percentile not
   independently re-derived this pass — **gap**); any comp-sales miss likely draws a larger-than-average
   multiple reaction given how little margin for disappointment is priced in at this multiple.

## 10. Key risks & kill criteria (measurable)
1. Marmaxx US comp sales below 2% for two consecutive quarters (current run-rate: +1%). **[Corrected 5 Oct 2026: Q2 FY27 (+1%) is already the first sub-2% quarter (Q1 FY27 was +6%); a Q3 FY27 Marmaxx comp below 2%, reported 18 Nov 2026, fires this criterion]**
2. Consolidated gross margin (ex. one-time tariff items) contracts more than 100bps YoY in any quarter.
3. Full-year adjusted EPS guidance is cut (not just reaffirmed/raised) at any of the next two quarterly releases.
4. Consolidated net debt/EBITDA rises above 2.0x (current 0.9x) without a value-accretive acquisition explaining it.
5. Buybacks are paused or reduced by more than 30% quarter-over-quarter without a stated capital-allocation reason.

## 11. Catalysts & calendar
Next quarterly release: Q3 FY2027 earnings, historically reported mid-to-late November (based on the FY2026
Q3 release having been filed 2025-11-19, accession 0000109198-25-000058, per the 8-K record) — specific 2026
date not confirmed from a primary IR calendar this pass (**gap**). **[Corrected 5 Oct 2026: the TJX reporting calendar (tjx.com/investors) lists Q3 FY2027 results on 18 Nov 2026]** An 8-K item 5.02 filed 2026-09-17 (accession 0000109198-26-000051) indicates a recent executive/board change; not investigated further this
pass (**gap, flag for next review**). **[Corrected 5 Oct 2026: investigated: the 8-K (accession 0000109198-26-000051) reports the election of Craig A. Pintoff (EVP & Chief Administrative Officer, United Rentals) as an independent director and Audit & Finance Committee member on 16 Sep 2026; not an executive departure, benign]**

## 12. Red-flag scan
- **Litigation:** TJX's well-known historical data breach class action (2007, ~45mn cards) was settled >15
  years ago and is not a live issue; no 2026-dated SEC/DOJ investigation or new material litigation was
  surfaced in this pass (WebSearch, 2026-09-27). A full Item 1/Item 3 legal-proceedings read of the current
  10-Q was not completed this pass — **gap**.
- **Insider activity:** an 8-K item 5.02 was filed 2026-09-17, accession 0000109198-26-000051 (executive/
  director change) — not yet reviewed for context; flagged for the next diligence cycle. **[Corrected 5 Oct 2026: reviewed: see the section 11 marker; benign director election]**
- No going-concern language, restatement, or auditor change identified in the documents reviewed this pass.

## 13. Data basis, recency and disclaimer
Most recent period incorporated: **Q2 FY2027** (quarter ended 2026-08-01), both from XBRL companyfacts (which,
unlike SO/AEP, is current for TJX through this quarter) and the Q2 FY2027 earnings press release (8-K exhibit,
filed 2026-08-19). Events checked to 2026-09-25 close via WebSearch; the search surfaced only legacy (pre-2010)
litigation, no new 2026 item. GAAP vs adjusted figures are labelled throughout; the $0.14–$0.16 one-time
tariff-refund benefit is called out explicitly wherever GAAP EPS is cited. **Research only; not personal
investment advice.**

## Sources
1. SEC EDGAR submissions, CIK 0000109198: https://data.sec.gov/submissions/CIK0000109198.json (retrieved 2026-09-27)
2. SEC XBRL companyfacts, CIK 0000109198: https://data.sec.gov/api/xbrl/companyfacts/CIK0000109198.json (retrieved 2026-09-27)
3. TJX Q2 FY2027 earnings press release (8-K exhibit, filed 2026-08-19, accession 0000109198-26-000045):
   https://www.sec.gov/Archives/edgar/data/109198/000010919826000045/tjxq2fy27earningspressrele.htm
4. `v4/outputs/Q01_triage.json`, `v4/data/b1_live_scores.csv`, `v4/data/triage_cards.csv` (internal, 2026-09-25 close)
5. WebSearch, "TJX Companies litigation SEC investigation 2026 data breach lawsuit tariff", 2026-09-27


---
## Correction (lead, 27 Sep 2026, from fact-check DA14; original text above left unchanged)
- §4 results table: **Q2 FY2027 net income was $1,520m** (13 weeks ended 1 Aug 2026; Q2 FY2027 8-K Ex-99.1, accession 0000109198-26-000045, and 10-Q, accession 0000109198-26-000048). The $1,243m shown is the prior-year column (13 weeks ended 2 Aug 2025, Q2 FY2026): a fiscal-year labelling error that understated the latest quarter by about 18%. EPS, guidance, capital returns and the balance sheet were verified correct; no kill criterion uses net income. Verdict unchanged.

---
## Correction (lead re-assessment, 5 Oct 2026, RA2)
Scope: red-team RT1 challenge to TJX (verdict WEAKENED; 'closest to BROKEN'). Every claim re-checked against primary sources (SEC EDGAR, tjx.com, federalreserve.gov, FRED). Original text above is unchanged apart from inline markers.

**Verified facts (primary).**
- Fed: FOMC raised the target range 25bp to 3-3/4 to 4 percent on 16 Sep 2026, 12-0 (federalreserve.gov monetary20260916a). 10-year Treasury (FRED DGS10): 5.01% on 16 Sep, 5.17% on 25 Sep (the data-cutoff day), 5.24% on 1 Oct. The red-team's 5.34% for 1 Oct is not the daily close.
- Q2 FY27 release (8-K Ex-99.1, filed 19 Aug 2026, accession 0000109198-26-000045): Marmaxx comp +1% (Q1: +6%), consolidated comp +4%, HomeGoods +7%, Canada +6%, International +7%; adjusted EPS $1.22 (+11%); Q3 plan comp +2% to +3%, adjusted EPS $1.30-$1.32; FY27 adjusted EPS $5.15-$5.20 (GAAP $5.31-$5.36 incl. $0.16 net tariff-refund benefit; refunds 'may not equal' tariffs paid); stores +4% a year from FY28; $798m Q2 buyback. Management: 'we are seeing improvement at our Marmaxx division to start the quarter'.
- Marmaxx is 60.0% of Q2 sales ($9,109m of $15,180m) and 63.9% of Q2 segment profit ($1,424m of $2,229m; 66.4% in H1); its segment profit rose 13.6% on a +1% comp. The red-team's '~70% of EBIT' is overstated.
- FY26 adjusted EPS was $4.73 (Q4 FY26 release, accession 0000109198-26-000004), so FY27 adjusted guidance implies +8.9% to +9.9% (midpoint +9.4%), not the red-team's '~7-8%'.
- Free cash flow (XBRL, OCF less capex): FY25 $4,198m (86% of net income), FY26 $4,917m (89.5%), trailing four quarters $5,876m. The red-team's '~75-80% conversion, P/FCF ~33x' is not supported: conversion is ~86-90% and trailing P/FCF is ~24x at $130.06 (normalised ~28x).
- EDGAR: no TJX filing after the 17 Sep 8-K (Item 5.02, director election) and Forms 3/4. Q3 FY27 results: 18 Nov 2026 (tjx.com reporting calendar). Jefferies cut to Hold (PT $145 from $180) on 26 Aug and Citi to Neutral on 20 Aug (secondary: Investing.com); stock fell ~15% in August (Motley Fool). Price $135.04 on 5 Oct (stockanalysis.com, intraday, third party).

**Reverse DCF (recomputed).** Equity value = price x 1,099.97m shares (cover of the Q2 10-Q) = $143.1bn at $130.06 (25 Sep close). FCF base = normalised $5,078m (88% of FY27 adjusted EPS $5.175 x 1,115m diluted shares); 10-year growth g, terminal growth 3%. Risk-free 5.17% (FRED, 25 Sep 2026); the dossier's 8.5% cost of equity implied a ~4.3% equity premium over a ~4.2% risk-free rate, so rf-consistent CoE = 5.17% + 4.3% = 9.5%.
- Implied 10-year FCF growth: 8.3% at 8.5% CoE; 9.5% at 9.0%; 10.6% at 9.5% (central); 11.8% at 10%. At the 5 Oct price ($135.04): 8.7% / 10.0% / 11.1% / 12.3%. On trailing (flattered) FCF $5,876m: 6.4% / 7.6% / 8.7% / 9.8% at $130.06.
- The dossier's 4.2% divided the NTM earnings yield into CoE (a perpetual-growth shortcut with 100% payout) and compared it with a 10-year growth base; the two are not like-for-like. The red-team's FCF-based 10.5% / 11.7% / 13% (at 8.5 / 9 / 9.5%) is also not reproduced because it used a ~3.0% FCF yield (conversion 75-80%); the filed numbers give 8.3 / 9.5 / 10.6%.
- Base case (8-10% FCF/EPS growth) unchanged: guided FY27 adjusted EPS +9.4%, plus 4% store growth from FY28 and ~1.9% net buyback. Rule: below if implied < 7%, above if implied > 11%, else in line. Central 10.6% => **in_line** (was below). It becomes 'above' if the price holds at ~$135 (11.1%) or CoE is 10%.
- Price at which implied growth falls to 10% (top of base): ~$124; to 9%: ~$115 (9.5% CoE).

**Kill criteria status.** None fired. Criterion 1 (Marmaxx comp below 2% for two consecutive quarters): Q2 +1% is the first leg; it fires if the 18 Nov print is below 2% (the red-team's 'Marmaxx plan 0-2%' is its own inference; TJX does not disclose division plans; TJX beat its +2-3% Q2 comp plan with +4%). (2) adjusted gross margin +0.7pt: no. (3) adjusted EPS guide raised, not cut. (4) leverage 0.9x: no. (5) buyback $798m in Q2: no.

**Restated view.** Verdict INCLUDE => **INCLUDE-SMALL**; implied_vs_base below => **in_line**. The premise 'price implies less growth than evidence' no longer holds; the business evidence (above-plan Q2, raised adjusted guidance, 0.9x leverage, Marmaxx segment profit +13.6%) is intact, so this is a downgrade in conviction and size, not a rejection. 3-year annualised scenarios (from $130.06, +1.5% dividend): bear -3% (Marmaxx stays sub-2%, EPS +4%/yr, 19.5x), base +7.7% (EPS +9%, 23.5x vs 25.4x trailing adjusted now), bull +14% (EPS +12%, 26x). Re-upgrade to INCLUDE at a price near $115-124 or on a Q3 Marmaxx comp of 3% or more; move to WATCH if the price stays above ~$135 without such a print; REJECT if kill criterion 1 fires.
