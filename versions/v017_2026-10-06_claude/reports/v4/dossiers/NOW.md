# ServiceNow, Inc. (NYSE: NOW) — Diligence Dossier (Agent F30, standard depth)

## 1. Verdict
**INCLUDE-SMALL** (half weight), horizon 12–36 months. Reason: best-in-class enterprise SaaS franchise trading at a
reverse-DCF-implied growth rate below a reasonable base case (cheap-to-fair), but with two live, unresolved legal/
regulatory overhangs (a DOJ investigation tied to a former executive's government-contract conduct, and a DOJ
antitrust "second request" on the pending Moveworks deal) plus heavy share-based compensation that keeps GAAP margins
thin — reservation named explicitly in §9. **[Corrected 2026-10-06: the 'cheap-to-fair' label came from a reverse DCF that added back stock compensation, used a FCF figure that does not match the filings and overstated FY26 revenue; corrected, price implies about 17% annual free-cash-flow-after-SBC growth for 10 years versus a 14-17% base, so there is no margin of safety. Verdict lowered to WATCH, see Re-assessment RA9 below]]**

## 2. Business in plain English
ServiceNow sells a single cloud platform ("Now Platform") that automates IT, HR, customer-service and other back-office
workflows for large enterprises and governments, increasingly wrapped in generative-AI agents ("Now Assist"/AI Agents).
Customers pay multi-year subscriptions; renewal rates and net expansion are among the highest in enterprise software.
It competes with point solutions (Atlassian, Salesforce Service Cloud, BMC) but increasingly positions itself as the
"AI control tower" that orchestrates other vendors' AI agents across a company's tech stack.

## 3. Why the model likes it — durable or artefact?
Quant snapshot (`b1_live_scores.csv`): composite percentile is weak (decile 1, live_rank 474) — the pre-registered
factor model does **not** like NOW (it is a growth/quality name the value- and momentum-tilted model structurally
underweights; ep=0.012, mom_12_1=-19.6%, i.e. the stock has fallen over the past year). NOW is in this wave only via
the triage/quality-growth process, not the live-rank gate. That is consistent with the facts: subscription growth has
been resilient (24.5% YoY in Q2 FY26) while the share price has been flat-to-down, i.e. a valuation reset, not a
business deterioration — durable, not an artefact, based on the filings below.

## 4. Last eight quarters (GAAP, USD millions except EPS; source: SEC XBRL companyfacts, 10-Q/10-K)
| Quarter end | Revenue | YoY growth | GAAP op. margin | GAAP dil. EPS | Non-GAAP dil. EPS¹ |
|---|---|---|---|---|---|
| 2024-09-30 | 2,796 | — | 15.9% (418/2,632³) | 2.07 | n/a |
| 2024-12-31 | 2,957 (Q4 rev per release) | — | — | — | — |
| 2025-03-31 | 3,088² | — | 13.5% (est.) | 0.44 | 0.97 (Q1'26 was $0.97; Q1'25 n/a here) |
| 2025-06-30 | 3,215² | — | 358/3,215=11.1% | 0.37 | n/a |
| 2025-09-30 | 3,347² | — | 572/3,347=17.1% | 2.40 (incl. one-off tax benefit) | n/a |
| 2025-12-31 | 3,568 | 20.5% | 12.5% (GAAP) | 0.38 | 0.92 |
| 2026-03-31 | 3,770 | 22% | 13.5% (GAAP) | 0.45 | 0.97 |
| 2026-06-30 | 3,987 | 24% | 4.0% (GAAP)⁴ | 0.29 | 0.90 |

¹ Non-GAAP figures for 2026 quarters from company earnings releases (8-K Ex-99.1); non-GAAP for 2024/2025 quarters
not independently re-derived here (data gap, disclosed). ² Total revenue for these older quarters is the XBRL
`Revenues`/`RevenueFromContractWithCustomerExcludingAssessedTax` figure (SEC companyfacts), not re-confirmed against a
press release; treat as approximate. ³ GAAP operating income from XBRL `OperatingIncomeLoss`. ⁴ The Q2 FY26 4.0% GAAP
operating margin (vs 29.5% non-GAAP) is the widest GAAP/non-GAAP gap of the eight quarters shown — driven by SBC and
acquisition-related charges (Armis/Veza/Moveworks integration), not a core-margin problem; confirm the exact bridge in
the 10-Q before treating GAAP margin trend as a standalone red flag.
**Acceleration/deceleration:** subscription revenue growth has been in a narrow 21–24.5% YoY band for the last five
quarters — remarkably steady, not decelerating, for a company at a >$15B revenue run-rate.

## 5. Guidance track record (last 3 releases; source: 8-K Ex-99.1 exhibits, SEC EDGAR)
- At **Q4 FY25** (28 Jan 2026): initial FY26 subscription-revenue guide **$15,530–15,570M** (20.5–21% YoY), non-GAAP
  op margin 32%, non-GAAP FCF margin 36%.
- At **Q1 FY26** (22 Apr 2026): **raised** FY26 subscription guide to **$15,735–15,775M** (22–22.5%); non-GAAP op
  margin **cut** to 31.5%, FCF margin cut to 35% — explicitly attributed to the Armis acquisition (~125 bps rev
  contribution, near-term margin headwind).
- At **Q2 FY26** (22 Jul 2026): **raised again** to **$15,760–15,780M** (22.5%); margin guide held at 31.5% non-GAAP
  op margin / 35% FCF margin. Q2 itself beat the high end of its own prior guidance by ~150 bps.
- **Q3 FY26 guide** (given with Q2 print): subscription revenue $3,975–3,980M (20.5% YoY).
**Pattern: revenue guidance raised in back-to-back quarters (beat-and-raise); margin guidance was cut once (M&A
dilution), then held** — a real, disclosed, verifiable trade-off, not a hidden one.

## 6. Earnings quality & balance sheet (10-Q, 30 Jun 2026, filed 23 Jul 2026)
- **FCF conversion:** Q2 FY26 FCF $634M on GAAP net income of ~$300M (FCF>>NI most quarters; FCF is structurally
  much cleaner than GAAP EPS because SBC and deferred-revenue timing dominate GAAP earnings). FY26 guided FCF margin
  35% on ~$18.5B total revenue ≈ **~$6.5B FY26 FCF**. **[Corrected 2026-10-06: FY26 total revenue is about $16.1-16.3bn (H1 $7,757m plus Q3 subscription guide $3,975-3,980m and Q4), not $18.5bn, so 35% gives about $5.7bn, not $6.5bn; and the $5.15bn trailing FCF used in section 7 is not in the filings (OCF $5,308m less capex $728m = $4,580m); SBC of about $2.2bn trailing is not deducted from either]]**
- **SBC:** $547M in Q1 FY26 alone (XBRL `ShareBasedCompensation`, six-month/quarterly cumulative — treat as
  approximate scale) versus ~$3.77B Q1 revenue — **mid-teens % of revenue**, high even for large-cap SaaS; this is
  the main GAAP-vs-adjusted-EPS driver (GAAP EPS $0.29–$0.45/qtr vs non-GAAP $0.90–$0.97/qtr).
- **Balance sheet:** cash & investments ~$8.78B; total debt $7.6B carrying value, including **$4.0B of new senior
  notes issued in May 2026** (4.25–6.30% coupons, 2028–2056 maturities) — a real leverage increase used partly to
  fund the buyback below. Still net-cash-light positive (~$1.2B) but the direction (new debt + buybacks) should be
  watched. **[Corrected 2026-10-06: cash and investments are $6,707m (cash $2,503m, marketable securities $2,161m, long-term marketable securities $2,043m), not $8.78bn (that number is the H1 acquisition outflow of $8,776m); debt is $7,517m (short-term $2,082m commercial paper/term debt plus long-term $5,435m), so net debt is about $0.8bn, not net cash of $1.2bn]]**
- **Buybacks:** 20.2M shares repurchased for $2.23B in H1 2026; shares outstanding fell from 1,047.3M (Dec-25) to
  1,033.9M (Jun-26).
- **M&A:** Armis (cybersecurity) closed and integrating; Moveworks ($2.85B, AI) signed but **under DOJ second-request
  antitrust review** — not yet closed, timing/closure uncertain (see §11).

## 7. Valuation snapshot and reconciliation with V1
NOW has **no row in `v4/outputs/v1_valuation_table.csv`** (v1_verdict = null; not covered by the systematic valuation
agent in this cycle). NTM P/E (d4, 25 Sep 2026 close $135.62, split-adjusted 5:1 Dec-2025): **28.5x**; FCF yield
**3.7%**; EV/EBITDA not meaningful given SBC distortion of GAAP EBITDA.
**My own reverse DCF** (FCFF proxy, TTM FCF $5.15B, EV $146.2B, WACC 9.2% [beta 0.97, rf 5.17%, ERP 4.14%, per the
same CAPM inputs V1 used for SNDK], 10-year fade to 3% terminal growth): the price implies **~10.1%/yr FCF growth for
10 years**. **[Corrected 2026-10-06: corrected: on free cash flow after SBC the price implies ~17%/yr for 10 years at 9.8%, not 10.1%; see Re-assessment RA9]]** My evidence-based base case (subscription growth decelerating from the current 22–24% toward
high-single-digits by year 10, with FCF margin expanding from 35% toward ~40% on operating leverage) is **~14–16%/yr**
— **implied growth is below my base case → view = "below/cheap"**. **[Corrected 2026-10-06: after the corrections, implied growth is at or above the top of a re-based 14-17% after-SBC base case: implied_vs_base = above]]** This is a genuine analyst judgment call (no V1
row to disagree with), flagged as such.

## 8. Bull case / bear case
**Bull:** (1) Now Assist/AI Agents crossed $1B ACV in one quarter — a real, disclosed monetization proof point, not
just a roadmap slide. (2) cRPO growth (21% YoY) is tracking subscription growth, so the revenue guide is not being
propped up by one-time deals. (3) FCF margin guide (35%) is high and durable given the asset-light subscription
model. **Bear:** (1) SBC dilution (~15% of revenue) means GAAP profitability is a mirage until buybacks structurally
offset it — they currently do (share count falling) but at the cost of rising leverage. (2) The Moveworks deal's DOJ
antitrust review could force a break fee, divestiture, or abandonment, muddying the AI-agent narrative. (3) The DOJ
investigation into the 2023 Army-CIO hiring (below) is open-ended; a finding of a compliance failure at the company
level (not just the departed COO) could bring fines or debarment risk in the public-sector business, a meaningful
customer segment.

## 9. Key risks & kill criteria (verbatim, copied into summary JSON)
1. "Subscription revenue growth decelerates below 18% YoY for two consecutive quarters."
2. "DOJ investigation into the 2023 Army-CIO hiring results in a formal finding against the company (not just the
   departed executive) or any debarment/suspension action against ServiceNow's federal business."
3. "The Moveworks acquisition is blocked, abandoned, or requires a material divestiture after the DOJ second
   request."
4. "Non-GAAP FCF margin falls below 30% for two consecutive quarters (guide is 35%)."
5. "Net debt/EBITDA (GAAP) exceeds 2.0x following further debt-funded buybacks or M&A."

## 10. Catalysts & calendar
Next earnings: **28 Oct 2026** (Q3 FY26, per company IR calendar/8-K schedule). Watch for: Moveworks DOJ
resolution timing (open as of this writing), FY27 initial guidance (typically given with Q4 print, Jan 2027).

## 11. Red-flag scan
- **DOJ / DoD-IG / Army Suspension & Debarment Office investigation**: a complaint alleged a conflict of interest in
  ServiceNow's March 2023 hiring of the outgoing U.S. Army CIO as head of its Global Public Sector business. The
  board found the company's President/COO and the hired executive violated company policy; the COO resigned 24 Jul
  2024. The company has referred the matter to DOJ/DoD-IG/Army SDO and DOJ has opened its own investigation — still
  open as of the most recent disclosures found (source: SEC filing text via news search, not independently re-read
  in the primary 10-Q Legal Proceedings section — **data gap: the Item 1 Legal Proceedings text itself could not be
  retrieved verbatim from the Q2 FY26 10-Q in this session; the summary above is drawn from secondary reporting of
  company disclosures and should be verified against the primary Legal Proceedings section before sizing**). **[Corrected 2026-10-06: the primary text is now read: 10-Q (0001373715-26-000076) Note 17 says the Company 'is continuing to cooperate with the Department of Justice, which has commenced its own investigation and required the Company to deliver certain documents' and 'cannot predict the timing, outcome or possible impact'; still open, nothing quantified]]**
- **Moveworks $2.85B acquisition** under active DOJ antitrust "second request" (in-depth review), not yet closed.
- Shareholder law-firm "investigation" solicitations (e.g., Schall Law Firm) were found in search results; these are
  routine plaintiff's-bar advertisements following any stock volatility and are **not evidence of a filed securities
  class action** — noted for completeness, not treated as a red flag.
- No auditor change, material weakness, or going-concern language found in the reviewed portions of the FY25 10-K /
  Q2 FY26 10-Q.
- Insider selling: not separately checked for NOW in this session (time-boxed; disclosed gap).

## 12. Sources
1. SEC EDGAR companyfacts API, CIK 0001373715 (retrieved 2026-09-26).
2. ServiceNow 8-K Ex-99.1, Q2 FY2026 results, https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm
3. ServiceNow 8-K Ex-99.1, Q1 FY2026 results, https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000054/erq1fy26.htm
4. ServiceNow 8-K Ex-99.1, Q4 FY2025 results, https://www.sec.gov/Archives/edgar/data/1373715/000137371526000005/erq4fy25.htm
5. ServiceNow 10-Q, period 2026-06-30, https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm
6. Web search on DOJ/Army-CIO investigation and Moveworks antitrust review (secondary reporting; see §11 caveat), retrieved 2026-09-26.
7. `v4/data/b1_live_scores.csv`, `v4/data/d4_live_snapshot.parquet` (quant context, 2026-09-25).
8. `v4/outputs/Q12_triage.json` (prior triage note on NOW).

## Data basis, recency and disclaimer
**Data Quality Note:** all figures are **consolidated GAAP** unless explicitly labelled "non-GAAP"/adjusted (company's
own reconciliation); all dollar figures are USD; most figures trace to SEC filings/8-K exhibits cited in §12, a
minority (marked with a data-gap note in §4/§11) come from secondary reporting of company disclosures and are flagged
as such. Most recent period incorporated: **Q2 FY2026, quarter ended 30 June 2026** (10-Q filed 23 Jul 2026; earnings
release 22 Jul 2026). Events checked to 2026-09-25. This dossier is **research, not personalized investment advice**
and not a recommendation to buy or sell any security.

## Correction (2026-09-26, added by the lead after auditor A3, Loop 3)

This dossier (§1, §6, §9 kill criterion 3, §11) describes the $2.85B Moveworks acquisition as "signed but under a DOJ second request, not yet closed". That is out of date. ServiceNow's investor-relations release and its Form 8-K filed on 15 December 2025 show the deal **closed in December 2025**, about nine months before this dossier's data cutoff. Data audit DA6 is re-confirming the accession number (`v4/outputs/da6_factcheck.md`).

- **Kill criterion 3 is withdrawn.** It concerned the deal being blocked or abandoned, so it can no longer fire. The other four kill criteria stand.
- **One DOJ matter remains open,** not two: the Army-CIO hiring investigation.
- **Verdict unchanged: INCLUDE-SMALL (half conviction).** The reservation is now the open DOJ hiring matter plus heavy share-based compensation.

---
## Re-assessment (RA9, 2026-10-06)
Scope: independent re-test of the valuation behind "implied vs base". Data cutoff: EDGAR to 2026-10-06; nothing after the 23 Jul 2026 10-Q except Forms 4/144 and S-8s (no 8-K since 22 Jul). Price $135.62 (25 Sep 2026), 1.040bn diluted shares (market cap $141.0bn). Original text above is unchanged (including the 26 Sep Moveworks correction). Research only, not personal advice.

| # | Wrong or stale text | Corrected value | Source | Effect |
|---|---|---|---|---|
| 1 | TTM FCF $5.15bn | Filed: operating cash flow $5,444m (FY25) - $2,393m (H1 25) + $2,257m (H1 26) = $5,308m; capex $868m - $395m + $255m = $728m; FCF $4,580m (company non-GAAP, which adds back business-combination costs, is higher: H1 26 $2,299m versus $2,012m) | XBRL companyfacts CIK 1373715; Q2 release 0001373715-26-000072 | The $5.15bn figure came from the d4 snapshot and does not reconcile to the filings |
| 2 | SBC not deducted from FCF in the reverse DCF | SBC $652m in Q2 2026 (16.4% of revenue) and $1,199m in H1; trailing $2,185m (about 14.9% of $14.7bn revenue); about $2.6bn for FY26. FCF after SBC: trailing $2.40bn; FY26 guided about $3.1bn ($5.7bn less $2.6bn). Net share settlement taxes ($281m in H1) and buybacks ($2,225m in H1) are the cash cost of that dilution | Q2 release cash-flow statement | After-SBC yield is 2.2% of market cap, not 3.7% |
| 3 | FY26 FCF "about $6.5bn on $18.5bn revenue" | FY26 revenue is about $16.2bn: H1 $7,757m (Q1 $3,770m, Q2 $3,987m) + Q3 about $4.09bn + Q4 about $4.3bn. Guidance quoted verbatim: subscription revenues $15,760-$15,780m (22.5% growth), non-GAAP operating margin 31.5%, free cash flow margin 35%. 35% x $16.2bn = $5.7bn. H1 non-GAAP FCF margin was 29.5% versus 32% a year earlier, so H2 must reach about 43% | Q2 release outlook table | Anchor lowered by about 12% |
| 4 | Cash and investments about $8.78bn; net cash about $1.2bn | Cash and investments $6,707m; debt $7,517m (short-term $2,082m, long-term $5,435m); net debt about $0.8bn before $0.94bn of operating lease liabilities. Strategic investments ($2,073m) not counted as cash | Q2 release balance sheet | Net debt, not net cash; leverage trend (term loan, $4.0bn notes, commercial paper) is the real flag |
| 5 | WACC 9.2% using ERP 4.14% | 5.17% + 0.98 (Blume-adjusted beta; raw 0.972) x 4.75% = 9.8%; range 9.2-10.5%; terminal growth 3.5% (dossier used 3.0%, shown as a sensitivity) | FRED DGS10 25 Sep 2026; d4 beta | Higher discount rate than the dossier's |
| 6 | Implied ~10.1%/yr for 10 years versus base 14-16% (below, cheap) | Implied 10-year growth in FCF per share after SBC, base $2.98 per share: 15.5% at 9.2%, 17.0% at 9.8%, 18.7% at 10.5% (terminal 3.5%; 16.3% / 17.8% / 19.4% with 3.0%). Base re-set on the same after-SBC basis: revenue CAGR about 14% (22% fading to 9%) plus after-SBC margin from about 19% to 25-27% gives 14-17% | RA9 arithmetic | Price implies the top of the base range or more: implied_vs_base = above. Fair value at 16% growth and 9.8% is $126 (-7%); at 17% $135 (the price) |
| 7 | Scenarios -5.3% / +16.3% / +29% | Scenario fair values with 10-year growth and discount rate (bear 11%, 10.5%; base 16%, 9.8%; bull 21%, 9.2%), price converging to scenario value in 3 years: $77 / $126 / $206 per share, or -8.6% / +7.0% / +25.5% a year | arithmetic by RA9 | Base return is under the 9.8% hurdle |
| 8 | DOJ Legal Proceedings text "could not be retrieved" | Retrieved and quoted in the correction above; matter open, no accrual | 10-Q Note 17 | Gap closed; reservation unchanged |
| 9 | Moveworks "$2.85B" | Purchase consideration $2,407m (stock $1,467m, cash $905m); closed December 2025 (already corrected 26 Sep) | 10-Q Note on acquisitions | Immaterial |

Verdict: **INCLUDE-SMALL reduced to WATCH.** The business facts hold (subscription revenue +24.5%, cRPO +21%, guidance raised) but after counting stock compensation as a cost the price already discounts roughly the top of the growth range, base-case value is about 7% below the price, the net-cash balance sheet is now a net-debt one, and a DOJ investigation remains open. Revisit below about $110 (value at 14% growth and 9.8%) or after the 28 Oct 2026 print if free cash flow after SBC tracks the $3.1bn guide.
