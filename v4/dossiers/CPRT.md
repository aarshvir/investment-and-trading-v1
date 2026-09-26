# CPRT (Copart, Inc.) — Diligence Dossier

Agent: F36 · Standard depth · Prepared 2026-09-26 · Prices/market data as of 2026-09-25 close ($27.59; mkt cap ≈$25.5B)

## 1. Verdict

**WATCH** — overturns the triage advance. Thesis horizon if resolved favourably: 12–24 months. The triage read
CPRT as "near-monopoly economics intact" with growth merely decelerating; primary-source work through the
just-reported Q4 FY2026 (filed 10-Sep-2026) and the 10-Sep-2026 M&A announcement finds a materially different,
more adverse picture: gross margin compressed ~350bps YoY in the quarter, operating cash flow is down
year-to-date, the CEO abruptly departed with the founder returning mid-cycle, plaintiff law firms have opened
securities-related "investigations," and the company has just committed $1.9B of cash to an antitrust-gated
acquisition (ACV Auctions) that management itself says is EPS-neutral in year one. None of this is disqualifying
on its own, but together it removes the margin of safety the triage assumed. Condition to move to INCLUDE: a
quarter of stabilised-or-improving gross margin, HSR clearance and a credible integration update on ACV, and no
material finding from the ongoing securities-law-firm inquiries. No V1 systematic valuation row exists for CPRT;
`v1_verdict = null`.

## 2. Business in plain English

Copart runs the largest online salvage- and used-vehicle auction network in the US (with UK/international
operations), taking vehicles on consignment mostly from insurance companies after a total-loss determination
(and, on a smaller "purchase agreement" basis, buying some vehicles outright) and selling them via its own
online auction (VB3/VB Advantage) to dismantlers, rebuilders, dealers and exporters. Revenue is mainly per-unit
service/auction fees plus, on purchased units, the sale margin itself. The moat is largely a real-asset one — a
nationwide land bank of storage/processing yards that is genuinely hard to replicate (permitting, capital,
insurer-relationship lock-in) — layered under a software/marketplace business.

**Sector routing note:** GICS files CPRT under "Diversified Support Services" / "Auto & Truck Dealerships" adjacency,
neither of which is a clean fit. Per the stock-analysis skill's routing rules, this is nearest to the
`retail-ecommerce.md` marketplace framework (fee/margin on transaction volume — "GMV × take rate" analog), with
the land-bank/permitted-yard asset base treated as a moat feature (analogous to the waste-environmental
"permitted disposal asset" logic) rather than the primary profit driver. Explicitly rejected: `auto.md` (Copart
does not manufacture, retail, or finance vehicles) and `people-businesses.md` (this is not a pure labour/fee
brokerage — the yard network is a real capital asset).

## 3. Why the model likes it / is the reason still durable?

`data/b1_live_scores.csv`: live_rank 380, composite factor score driven by Quality (fam_Q, high gross-profit/
assets and OCF/assets — both computed on **stale** data: `max_filed_used` 2026-05-29, i.e. the Q3 FY26 10-Q,
predating the Q4 FY26 results and the ACV deal). The triage's "32% margins remain intact" framing is now
contradicted by the just-reported quarter (Section 4) — this is a live example of the quant/triage layer running
ahead of primary sources, exactly the scenario this diligence pass exists to catch.

## 4. Last two years of results (fiscal quarters, FYE 31-Jul)

| Qtr (end) | Revenue | YoY | Gross profit | Gross margin | Diluted EPS | Net income |
|---|---|---|---|---|---|---|
| Q1 FY25 (Oct-24) | — | — | — | — | $0.37 | $362.1M |
| Q2 FY25 (Jan-25) | — | — | — | — | $0.40 | $387.4M |
| Q3 FY25 (Apr-25) | — | — | — | — | $0.42 | $406.6M |
| Q4 FY25 (Jul-25) | $1.13B | +5.2% | — | 45.3%* | $0.41 | ~$396M |
| **FY25 total** | **$4.65B** | +9.7% | — | 45.2% | $1.59 | $1,552.4M |
| Q1 FY26 (Oct-25) | — | — | — | — | $0.41 | $403.7M |
| Q2 FY26 (Jan-26) | — | — | — | — | $0.36 | $350.7M |
| Q3 FY26 (Apr-26) | $1.24B | +2.1% | $572.6M | — | $0.43 | $402.4M |
| Q4 FY26 (Jul-26) | $1.2B | +2.4% | $481.4M | **41.8%** | $0.35 | $327.4M |
| **FY26 total** | **$4.7B** | +0.4% | ~$2.1B | 44.6% | **$1.55** | **$1,485M (~ -4.4% YoY)** |

*Q4 FY25 gross margin of 45.3% is the prior-year comparator quoted directly in the Q4 FY26 release.

Revenue growth decelerated from +9.7% (FY25) to +0.4% (FY26); global units sold fell in both years (FY25 units
−5.5%, largely catastrophe-volume driven; FY26 volumes described by management as pressured by "record total
loss frequency" — the language is ambiguous on whether volumes were up or down and needs a primary 10-K read
this dossier did not complete in the time-box). **Full-year diluted EPS fell 2.5% YoY (FY26 $1.55 vs FY25
$1.59)** — the first EPS decline in the multi-year record checked here.

Gross margin decline driver (per the Q4 FY26 earnings call, cited via secondary transcript sources — flagged as
such): operating cost per car +12.7% in Q4, driven by investment in new products/services (long-haul delivery,
TitleExpress, dedicated wholesale facilities) plus US facility costs +7.7% (+14.2% per unit) against softer
core-segment volumes. This is management's own explanation of the margin compression, not this analyst's
inference — cited to the earnings call, not yet cross-checked against the 10-K MD&A line-by-line.

## 5. Guidance track record

Copart does **not** issue formal quarterly or annual financial guidance (consistent with prior periods) — no
guidance-versus-prior-range table to build for this name.

## 6. Earnings quality & balance sheet

- **FCF conversion:** FY25 (last full audited year) OCF $1,799.75M − capex $568.99M = FCF ≈$1,230.8M vs net
  income $1,552.4M → FCF/NI ≈79%. **9-month FY26 OCF was $1,246.95M vs $1,361.27M in the same 9 months of FY25
  (−8.4% YoY)** — cash generation is declining even before the ACV cash outlay. This is a genuine
  deterioration, not a data artefact (both figures from primary 10-Q filings).
- **SBC:** modest, ~$29M for 9-month FY26 vs ~$3.5B revenue base — under 1% of revenue.
- **Balance sheet:** essentially debt-free historically (last confirmed long-term debt figure in this pull, from
  FY23 10-Qs, was under $25M); cash-and-investments ≈$4.49B (Yahoo/D4, cross-checked directionally against the
  9-month FY26 cash decline from $2.78B to $1.91B reported in the Q4 release net of buybacks — the two cash
  figures are not on the same basis (D4's totalCash appears to include short/long-term investments beyond just
  "cash," a **data conflict** not fully resolved in this pass).
- **Capital returns:** FY26 share repurchases **$1,632.5M** vs **zero** in FY25 — a sharp change in capital-
  allocation policy in the same year cash generation weakened and immediately before committing $1.9B cash to
  the ACV acquisition. No dividend.
- Net debt (post-buybacks, pre-ACV-close): materially net-cash positive.

## 7. Valuation snapshot and reverse DCF

No V1 row exists for CPRT; `v1_verdict = null`. Analyst reverse DCF (`valuation.py`, 10y fade to 3% terminal):

- EV bridge: market cap $25.54B + debt ~$0.1B (immaterial, estimated) − cash/investments $4.49B ≈ **EV $21.15B**
- WACC 9.4% (rf 5.17%, ERP 4.14%, Blume-adjusted beta 1.02 from raw beta 1.03 in `d4_live_snapshot`; debt
  weight negligible)
- Base FCF: FY2025 actual (primary-sourced, most recent complete fiscal year) $1,230.8M
- **Implied 10-year FCF growth priced in: ~3.9%/yr**, fading to 3% terminal.

On its face this looks cheap relative to a base case of, say, 4%/yr EPS growth (roughly "in line," not clearly
below) — but given the **FY26 EPS decline** and the **9-month OCF decline** just reported, this analyst's own
base case is **not** the double-digit growth the triage assumed; it is closer to 3–4%/yr, i.e. **in line with**
what the market is already pricing, not clearly below it. Trailing P/E 16.5x is not table-pounding cheap once
the deteriorating trend is taken into account. **valuation_view_vs_v1.implied_vs_base = "in_line."**

**Scenario 3-yr annualised total return (illustrative, no dividend):** Bear −12.2%/yr (EPS −5%/yr, exit 14x
P/E), Base +4.0%/yr (EPS +4%/yr, exit P/E flat at 17.8x), Bull +14.4%/yr (EPS +10%/yr, exit 20x P/E) — not
consensus, an analyst estimate built to be checkable against the assumptions stated.

## 8. Bull case / bear case

**Bull (3):**
1. The land-bank moat (permitted yard capacity, insurer relationships) has not gone away; margin pressure this
   quarter is explicitly framed by management as *investment* spend (new products, wholesale facilities), which
   could reverse once those investments mature.
2. Net-cash balance sheet funds the ACV deal without leverage; if antitrust clearance is obtained and
   integration goes to plan, management's own framing (accretive from FY28) implies a longer-run earnings step-up.
3. Founder Jay Adair's return as CEO could be read as a stabilising, execution-focused signal after a rocky
   stretch, by someone who built the business the first time.

**Bear (3):**
1. Margin compression (−350bps YoY in the reported quarter) plus a YoY EPS decline is a real earnings-quality
   deterioration, not merely a deceleration in an otherwise-strong story, and the stated causes (new-service
   investment, facility cost inflation) are exactly the kind of "temporary" explanation that deserves scepticism
   until at least one more quarter confirms the trend reverses.
2. An abrupt CEO exit (announced 29-Jun-2026, effective 31-Jul-2026, stock −8% same day) alongside multiple
   plaintiff-firm "securities fraud investigation" press releases is a governance yellow flag that should be
   tracked to resolution (these law-firm releases are frequently opportunistic and non-predictive of any
   finding, but the pattern coincided with a real, disclosed earnings deterioration and a leadership change,
   which raises the bar for dismissing it outright).
3. The $1.9B all-cash ACV acquisition is: (a) subject to HSR antitrust clearance in a space where Copart is
   already the dominant salvage-auction player, so clearance is not guaranteed on current terms; (b)
   management's own guidance is EPS-**neutral** in year one, i.e. no near-term financial benefit is being
   offered to offset the integration and execution risk; and (c) it follows, rather than precedes, a quarter of
   margin and cash-flow deterioration — a moment of demonstrated operating softness is an unusual time to
   deploy the balance sheet's full net-cash cushion.

## 9. Key risks & kill criteria (measurable)

1. Gross margin below 43% (i.e., not recovering meaningfully from the reported 44.6% FY26 full-year level) for
   two consecutive quarters.
2. Operating cash flow (trailing nine/twelve months) below the prior-year comparable period for a third
   consecutive reporting period.
3. HSR review of the ACV acquisition extended past a second request, or the deal terminated/repriced.
4. Any securities-class-action complaint actually filed (as opposed to a law-firm "investigation" solicitation)
   naming Copart or its officers.
5. Diluted EPS down year-over-year for two consecutive quarters.

## 10. Catalysts & calendar

- Next earnings: **Q1 FY2027 (quarter ending 31-Oct-2026), expected early December 2026** (estimated from
  Copart's historical reporting cadence; not yet confirmed by the company at time of writing).
- ACV Auctions tender offer/HSR process: deal announced 10-Sep-2026, expected to close by year-end 2026.
- Antitrust settlement with Auto Auction Services Corp already resolved (Copart obtained a data-access licence)
  — a closed item, not an open risk.

## 11. Red-flag scan

- **Leadership:** CEO Jeffrey Liaw stepping down effective 31-Jul-2026 (announced 29-Jun-2026); founder/Executive
  Chairman A. Jayson Adair resumed the CEO role. Stock fell 8.0% (to $28.10) on the announcement day. No
  company-stated reason for the change was identified in this pass beyond "CEO transition."
  Liaw sold 27,745 shares on 28-Jul-2026 under a pre-existing Rule 10b5-1 plan (adopted earlier — not
  opportunistic on its face, but noted).
- **Litigation/investigations:** Multiple plaintiff law firms (Pomerantz, Kessler Topaz Meltzer & Check, Bragar
  Eagel & Squire) issued "investigation" solicitations in Jun–Jul 2026 following the CEO transition and stock
  decline; no complaint or SEC enforcement action was identified in this pass, so this is disclosed as a
  monitoring item, not a confirmed adverse finding. A California PAGA wage-and-hour class/representative action
  (Mejia v. Copart, C.D. Cal.) is pending — a routine-scale employment-law risk for a large hourly workforce,
  not obviously outsized.
- **Insider selling:** director Daniel J. Englander sold 80,000 shares 13-Jul-2026 ($27.50–27.66); routine option
  exercises by other officers/directors also on file. No pattern of unusual pre-earnings selling identified in
  this time-boxed pass.
- No auditor changes, restatements, or going-concern language identified.

## 12. Data basis, recency and disclaimer

Most recent period incorporated: **Q4 and full-year FY2026 results (fiscal year ended 31-Jul-2026), reported via
8-K Ex-99.1 filed 10-Sep-2026**; the FY2026 10-K itself was not located/read in this pass (only the earnings
release and the FY2025 10-K/prior 10-Qs were used for balance-sheet and cash-flow detail) — this is a
**limitation**, not a completed document review, and should be revisited once the FY2026 10-K's MD&A and risk
factors are available. Checked for events to 2026-09-25, including the 10-Sep-2026 ACV acquisition announcement.
All figures are on a **consolidated** basis. GAAP figures throughout; Copart does not report a material
non-GAAP adjusted-EPS series. **This is research, not personalized investment advice; it is not a
recommendation to buy or sell any security, and it is not financial advice.**

## 13. Sources

1. SEC EDGAR submissions/companyfacts, CIK 0000900075 (data.sec.gov), retrieved 2026-09-26.
2. Copart Q4 & FY2026 earnings release (8-K Ex-99.1, filed 10-Sep-2026): sec.gov/Archives/edgar/data/0000900075/000119312526387902/cprt-ex99_1.htm
3. Copart Q3 FY2026 earnings release (8-K Ex-99.1, filed ~21-May-2026): sec.gov/Archives/edgar/data/0000900075/000119312526234447/cprt-ex99_1.htm
4. Copart FY2025 10-K (filed 26-Sep-2025): sec.gov/Archives/edgar/data/900075/000162828025042946/cprt-20250731.htm
5. Copart 8-K, ACV Auctions merger agreement (filed 10-Sep-2026): sec.gov/Archives/edgar/data/0000900075/000119312526388064/
6. "Copart to Acquire ACV Auctions for $1.9 Billion in All-Cash Deal," Yahoo Finance/Reuters wire, 10-Sep-2026.
7. "Copart Announces CEO Transition," BusinessWire, 29-Jun-2026: businesswire.com/news/home/20260629970802/en/Copart-Announces-CEO-Transition
8. Kessler Topaz Meltzer & Check / Bragar Eagel & Squire / Pomerantz investigation press releases, Jun–Jul 2026 (plaintiff-firm solicitations — treated as a monitoring item, not an adverse finding).
9. Copart Form 4 filings, Jun–Aug 2026 (sec.gov/Archives/edgar/data/0000900075/...) for insider transactions.
10. Copart Q4 FY2026 earnings call commentary on margin drivers, via secondary transcript aggregation (Motley Fool/Investing.com/GuruFocus summaries) — flagged as secondary, not yet cross-checked against the 10-K MD&A.
11. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (quant context, retrieved this session — noted as stale relative to the Q4 FY26 release and the ACV deal).
