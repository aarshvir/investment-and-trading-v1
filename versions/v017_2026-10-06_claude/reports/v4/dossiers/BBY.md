# Best Buy Co., Inc. (NYSE: BBY, CIK 0000764478)

**Recency:** most recent reported period incorporated: Q2 FY27 (13 weeks ended 2026-08-01), published 2026-08-27 (8-K earnings release) / 10-Q filed 2026-09-04; checked for events to 2026-09-25. Also incorporates the FY26 10-K (fiscal year ended 2026-01-31, filed 2026-03-18) and 8-K/press-release history back to Q3 FY25 (November 2024).

**Reporting basis:** consolidated, USD millions unless stated. Fiscal year ends the Saturday closest to January 31 (FY26 = year ended 2026-01-31).

---

## 1. Verdict line

**INCLUDE-SMALL (half weight).** BBY is a genuine, primary-sourced turnaround — comparable sales have gone from -6.8% (FY24) to +0.5% (FY26) to +4.1% (Q2 FY27), and guidance has been raised twice this year — but a scenario-weighted DCF (run via `valuation.py`) puts fair value at ~$86/share against a $90.51 price, the CEO and CFO are both departing within the same six months, and the market is already pricing in slightly negative long-run FCF growth, leaving little margin of safety for a concentrated position. Thesis horizon: 12–24 months (through the CEO/CFO transition and FY27 guidance delivery). **[Corrected 2026-10-06: wrong/incomplete: FY27 guidance was raised once (2026-08-27; Q1 FY27 only reiterated) - the earlier raise was FY26 (2025-11-25); and the CFO vacancy was filled on 2026-08-03 (8-K 0000764478-26-000034: Anne Bramman, ex-CFO of Nordstrom, Avery Dennison and Carnival, effective 2026-08-19); only the CEO handover (Bonfig, 2026-11-01) remains]**

## 2. Business in plain English

Best Buy is the largest specialty consumer-electronics retailer in North America, selling computing devices, mobile phones, consumer electronics, appliances, gaming and entertainment products through ~1,068 stores (926 Domestic, 142 Canada) and e-commerce (bestbuy.com / bestbuy.ca), plus services (Geek Squad support/installation, memberships, Best Buy Health) (10-K filed 2026-03-18, Item 1). It makes money on product gross margin (~22-24%), high-margin services/membership and, increasingly, two capital-light "profit streams" it is scaling — Best Buy Marketplace (third-party seller commissions) and Best Buy Ads (retail media) (10-K, Item 7). Competitively it sits between mass-market generalists (Walmart, Amazon, Costco) that also sell electronics at thin margins and it competes on staffed expertise, in-home delivery/installation, and vendor partnerships (Apple, Samsung) that de-prioritize pure price competition.

## 3. Why the model likes it — durable or artefact?

The pre-registered QVM model gives BBY Quality 0.753, Value 0.866, Momentum 0.65 (composite 0.756, the lowest of the three retail names under review). Momentum is well-supported: four consecutive comp-sales beats and two guidance raises in the last four earnings releases (Section 5) are real, dated, primary-sourced events, not noise. Value is directionally real — NTM P/E (~12.8-14.0x depending on source/date; see Section 7), FCF yield 9.3%, EV/EBITDA 8.3x are all below BBY's own 10-year average (P/E ~14.35x, EV/EBITDA ~7.4x median per MacroTrends/GuruFocus, cross-check only) — but the model's own reverse-DCF (Section 7) shows the market is pricing in *negative* trailing FCF growth, i.e. the "cheapness" is compensation for real, disclosed risk, not free money.

**Quality is the one to interrogate, and the orchestrator's hypothesis is partly correct.** The very low leverage input (0.073) is genuinely structural, not a shrinking-asset artefact: funded net debt is trivial and has been for years — BBY has actually run a **net cash position excluding leases** every year in this sample (net debt ex-leases is *negative* $1,086M at Q2 FY27: $1,169M gross debt less $2,255M cash), and gross debt has been flat at $1.14-1.17B since FY24 (10-K, Note 8; 8-K balance sheets). That part of Quality is durable.

But the **gross-profit/assets (0.594) and other asset-efficiency inputs are partly an artefact**, for two documented reasons, not one:
1. **Non-cash impairments have shrunk the denominator.** Best Buy Health (the healthcare/aging-in-place unit built around the Current Health and Lively/GreatCall acquisitions) took a $475M goodwill impairment in Q4 FY25 and another $171M goodwill/intangible impairment in Q3 FY26 — $646M cumulative in two years, explicitly tied to "downward revisions in the long-term financial projections for Best Buy Health" and "pressures in the Medicaid and Medicare Advantage markets" (8-K filed 2025-03-04; 10-K filed 2026-03-18, Item 7 & Note 3). Goodwill fell from $1,383M (FY24) to $790M (FY26/TTM) on write-offs, not monetization.
2. **The store fleet is genuinely shrinking and undercapitalized.** `ratios.py` flags, as a MEDIUM-severity quality warning, that capex has run below depreciation in all four periods sampled (0.81x-0.89x) — net PP&E fell from $2,260M (FY24) to $1,986M (FY26). Total store count fell from 1,125 (FY24) to 1,068 (FY26), and management guided 10-15 further closures in FY27 (Retail Dive, Feb-2026 earnings call coverage) while planning only ~+4 net Best Buy-banner stores.

Net: the underlying retail operation is genuinely improving (ROIC ex-goodwill 21.9%→28.9% FY24→TTM per `ratios.py`, comp sales inflecting positive, adjusted operating margin expanding), which is durable. But part of the *asset-efficiency* half of the Quality score is flattered by writing off a failed diversification bet and running the store base leaner rather than by compounding capital at a high rate — a meaningfully different, less repeatable story than the headline score suggests.

## 4. Last two years of results

All figures GAAP unless labeled Adjusted (company-defined non-GAAP; reconciling items in Section 6). FCF = operating cash flow − capex, derived from cumulative 8-K cash-flow statements (each quarter is the difference between consecutive YTD figures; TTM through Q2 FY27 sums to $1,768M CFO−capex, which exactly matches the orchestrator-supplied quant snapshot).

| Quarter (ended) | Revenue $M | YoY | QoQ | Op. margin (GAAP) | GAAP dil. EPS | Adj. dil. EPS | FCF $M |
|---|---|---|---|---|---|---|---|
| Q3 FY25 (2024-11-02) | 9,445 | -3.2% | -4.1% | 3.7% | $1.26 | $1.26 | -449 |
| Q4 FY25 (2025-02-01)¹ | 13,948 | -4.8% | +47.7% | 1.6% | $0.54² | $2.58 | 1,359 |
| Q1 FY26 (2025-05-03) | 8,767 | -0.9% | -37.1% | 2.5% | $0.95 | $1.15 | -132 |
| Q2 FY26 (2025-08-02) | 9,438 | +1.6% | +7.7% | 2.7%³ | $0.87 | $1.28 | 574 |
| Q3 FY26 (2025-11-01) | 9,672 | +2.4% | +2.5% | 2.0%⁴ | $0.66⁴ | $1.40 | -287 |
| Q4 FY26 (2026-01-31) | 13,814 | -1.0% | +42.8% | 5.2% | $2.56 | $2.61 | 1,103 |
| Q1 FY27 (2026-05-02) | 8,936 | +1.9% | -35.3% | 4.1% | $1.31 | $1.28 | 215 |
| Q2 FY27 (2026-08-01) | 9,779 | +3.6% | +9.4% | 4.3% | $1.48 | $1.47 | 737 |

Sources: 8-K earnings-release exhibits, filed 2024-11-26, 2025-03-04, 2025-05-29, 2025-08-28, 2025-11-25, 2026-03-03, 2026-05-28, 2026-08-27 (each with condensed statements of earnings and cash flows). ¹ 13-week quarter vs. a 14-week Q4 FY24 comp (extra week added ~$735M revenue in the prior year per the 8-K). ² Includes a $475M ($2.02/share) pre-tax non-cash Best Buy Health goodwill impairment. ³ Includes a $114M restructuring charge (labor/store-optimization initiative). ⁴ Includes a $171M ($0.74/share after-tax) Best Buy Health goodwill/intangible impairment.

**Trend:** revenue troughed in FY24 (comp -6.8% for the year) and has re-accelerated every quarter since Q1 FY26, with the last two quarters (+1.9%, +3.6% YoY) the strongest of the set. Operating margin is also inflecting, though Q4 FY26's 5.2% and Q3 FY26's 2.0% are both distorted by, respectively, a lapped impairment and a new one — the **adjusted** operating-margin trend (not shown in this GAAP table; see Section 6) is a cleaner read: 3.9%→4.0%→4.1%→4.3% domestic adjusted OI margin, Q1 FY26→Q2 FY27, a genuinely steady four-quarter improvement.

**Latest-quarter (Q2 FY27) variance decomposition:**
- **Revenue** $9,779M vs. PY $9,438M (+3.6%, +$341M) and vs. Q1 FY27 $8,936M (+9.4%, +$843M, largely seasonal — Q2 is a stronger calendar quarter and comps accelerated from +2.0% to +4.1% enterprise). Neither breaches the 10% YoY threshold; the QoQ move is essentially in line with normal seasonality plus the comp acceleration itself, which is the real news (Section 5).
- **Gross margin** 23.9% vs. PY 23.2% (**+70bps**), driven by growth in Best Buy Marketplace/Ads and a **$34M IEEPA tariff refund** (see Section on tariffs below), partly offset by lower product margin rates (8-K filed 2026-08-27). This is below the 200bps decomposition trigger but is explicitly tariff-driven and non-recurring in the same size next quarter (Q3 FY27 refund is separately disclosed at $41M — see Section 5).
- **Opex** (Q2 FY27 8-K): SG&A $1,923M (19.7% of revenue) vs. PY (Q2 FY26) $1,829M (19.4%), +30bps, from higher incentive compensation and Marketplace/Ads/advertising investment.
- **Operating margin** 4.3% (GAAP) vs. PY 2.7%, **+160bps** — but this GAAP delta is mechanically inflated by lapping a $114M one-off restructuring charge in Q2 FY26 against a $6M *credit* in Q2 FY27. On the **adjusted** basis both quarters actually disclose (which strips restructuring and intangible amortization), the comparison is 4.3% vs. 3.9%, **+40bps** — the more representative figure.
- **Net income** (Q2 FY27) $315M vs. PY (Q2 FY26) $186M (+69%) and **diluted EPS** $1.48 vs. $0.87 (**+70%**) — both breach the 10% trigger, but the decomposition is the same restructuring-charge lap described above, not a fundamental step-change in profitability. The company's own **adjusted diluted EPS** growth of +15% ($1.47 vs. $1.28) is the cleaner read on underlying momentum.

## 5. Guidance track record (last four releases, each with the prior range quoted)

| Release (date) | OLD guidance | NEW guidance | Verdict |
|---|---|---|---|
| Q3 FY26 (2025-11-25) | FY26 revenue $41.1-41.9B; comp (1.0%)-1.0%; adj. OI rate ~4.2%; adj. tax rate ~25.0%; adj. dil. EPS $6.15-6.30 (set 2025-05-29) | FY26 revenue $41.65-41.95B; comp 0.5-1.2%; adj. OI rate ~4.2% (unchanged); adj. tax rate ~25.4%; adj. dil. EPS **$6.25-6.35** | **RAISED** |
| Q4/FY26 results (2026-03-03) | *(no prior FY27 guidance existed)* | FY27 revenue $41.2-42.1B; comp (1.0%)-1.0%; adj. OI rate 4.3-4.4%; adj. tax rate ~25.5%; adj. dil. EPS **$6.30-6.60**; capex ~$750M | **Initial guide** — not comparable to a prior range; FY26 actual ($6.43 adj. EPS) beat the just-raised $6.25-6.35 FY26 range |
| Q1 FY27 (2026-05-28) | FY27 adj. dil. EPS $6.30-6.60 (set 2026-03-03) | "Reiterating" — FY27 revenue/comp/OI-rate/tax-rate/EPS/capex **all unchanged** at $6.30-6.60 adj. EPS | **MAINTAINED** |
| Q2 FY27 (2026-08-27) | FY27 revenue $41.2-42.1B; comp (1.0%)-1.0%; adj. OI rate 4.3-4.4%; adj. dil. EPS $6.30-6.60 | FY27 revenue **$42.3-42.8B**; comp **1.9-3.0%**; adj. OI rate **4.4-4.5%**; adj. tax rate ~25.5% (unchanged); adj. dil. EPS **$6.70-6.90**; capex ~$750M (unchanged) | **RAISED** (large — comp range moved from a possible decline to solid growth) |

Notably, the **Q1 FY26 release (2025-05-29) was a guidance CUT explicitly tied to tariffs**: FY26 adjusted diluted EPS was cut to $6.15-6.30 from the $6.20-6.60 set on 2025-03-04, comp guidance cut to (1.0%)-1.0% from 0.0%-2.0%, with CFO Matt Bilunas stating on the release: *"Today we are updating our full year guidance to incorporate the impact of tariffs... Our underlying working assumptions are that tariffs stay at the current levels for the rest of the year."* This is the one cut in the eight-quarter window; every subsequent release has raised or maintained.

## 6. Earnings quality & balance sheet

**FCF conversion:** TTM FCF/NI = $1,768M / $1,272M = **139%** (`ratios.py`); FY24 54%, FY25 151%, FY26 118% — lumpy because non-cash impairments depress NI more than CFO in the impairment years, but the **Sloan accrual ratio is negative in all four periods (-1.5% to -7.9%)**, meaning CFO consistently exceeds net income — a genuine positive earnings-quality signal, not one inflated by receivables/revenue-recognition aggression.

**SBC:** $139M (FY26), $139M (FY25), $145M (FY24) — a stable **0.33% of revenue**, immaterial as a dilution or non-GAAP-add-back concern.

**GAAP vs. Adjusted gap:** FY26 GAAP diluted EPS $5.04 vs. Adjusted $6.43 (gap $1.39/share: restructuring $0.48, Best Buy Health goodwill/intangible impairment $0.74, long-lived asset impairment $0.07, intangible amortization $0.05, disposal/investment losses $0.05). FY25's gap was larger still — GAAP $4.28 vs. Adjusted $6.37 ($2.09/share, ~49% of GAAP EPS), almost entirely the $475M Best Buy Health impairment. **Two years running, the single largest GAAP-adjusted reconciling item has been the same failed Best Buy Health initiative** — each exclusion is legitimate and clearly itemized, but the repetition is itself a data point on historical capital allocation, not a one-off to wave away.

**Leverage:** Funded net debt is negative $1,086M ex-leases (net cash) at Q2 FY27; net debt/EBITDA (incl. lease liabilities as debt) is **0.72x TTM** (1.02x-1.16x FY24-FY26; `ratios.py`). **Lease-adjusted leverage** — (net debt + operating lease liabilities)/(EBITDA+rent), per the required sector convention — is (−1,086 + 2,964) / (2,508 + 1,017 TTM operating lease cost) = **0.53x**, and gross debt-incl-leases/EBITDAR is 1.17x. Both are low in absolute and peer terms. Note explicitly: **BBY reports under US GAAP (ASC 842)**, which keeps lease expense as a single opex line rather than splitting it into depreciation+interest as IFRS 16 does — so BBY's EBITDA was **not** mechanically inflated by the 2019 lease-accounting change the way an IFRS 16 reporter's would be; the $2,964M-$2,957M of recognized lease liability is real, debt-like, off-EBITDA obligation layered on top of the funded-debt figures above.

**Debt maturities:** $500M 2028 notes + $650M 2030 notes (10-K, Note 8), plus an undrawn **$1.25B revolving credit facility** refinanced 2025-04-18 (5-year, matures April 2030, replacing an identical-sized facility; 8-K filed 2025-04-23) — no amounts drawn. No near-term refinancing wall.

**M&A/financing:** No material acquisitions in the window; the company *exited* a component of Best Buy Health (finalized Q2 FY26) and disposed of a Mexico subsidiary (Q4 FY26) — both divestitures, not deals.

**Share count / buybacks:** Diluted shares fell from 218.5M (FY24) to 212.7M (TTM), but buyback *pace has decelerated sharply*: FY25 buybacks $500M → FY26 $273M → FY27 guided ~$300M, and **H1 FY27 buybacks were just $36M** vs. $165M in H1 FY26 (8-K filed 2026-08-27). Per-share metrics are getting progressively less buyback assistance than in FY24-25.

**Dividend:** Raised to $0.96/quarter ($3.84 annualized) on 2026-08-27, a **1% increase** — the third straight 1% raise (from $0.95 in March 2025 and March 2026), a sharp deceleration from the 2% raise in February 2024 and BBY's historical double-digit dividend-growth years. Current yield ≈ **4.2%** at $90.51 (FMP quote, cross-checked against the $18,982.5M quant-snapshot market cap and 209.7M shares outstanding per the 10-Q cover page as of 2026-09-02). Payout ratio ≈ **64% of TTM GAAP diluted EPS** ($6.01) or **~57% of TTM Adjusted diluted EPS** ($6.76); FY25's 87% payout (GAAP) reflected the impairment-suppressed denominator, not a coverage problem. BBY has paid an uninterrupted quarterly dividend since fiscal 2004 (10-K, Item 5).

## 7. Valuation snapshot

All multiples below are from `valuation.py`, run on TTM financials (period ended 2026-08-01) and the 2026-09-25 price of $90.51 (209.7M diluted shares, market cap $18,982M).

| Metric | Value | vs. BBY 10-yr history (cross-check only, aggregator) | vs. peers (cross-check only, aggregator, Aug-Sep 2026) |
|---|---|---|---|
| P/E (trailing GAAP, TTM) | 14.96x | 10-yr avg ~14.35x, range 9.82x-26.93x (macrotrends/gurufocus) | — |
| NTM P/E | ~12.8-14.0x (12.78x per orchestrator quant snapshot; 12.99-13.99x per aggregator search, both consistent) | mid-of-range | TGT ~16x fwd; WMT ~39x fwd; COST ~37-39x fwd |
| EV/EBITDA (**lease-inclusive EV**, ASC 842 EBITDA — see Section 6 caveat) | 8.29x | 10-yr median ~7.44x, range 4.32x-11.47x | TGT ~9.8x; WMT ~20.7x; COST ~30-38x |
| EV/EBITDA excl. lease liability from EV | ~7.1x | — | — |
| EV/EBIT | 12.16x | — | — |
| FCF yield | 9.3% | — | — |
| Dividend yield | 4.2% | — | — |

BBY trades at a large discount to WMT and COST on every multiple shown, but those are structurally different businesses (membership/grocery-anchored, secularly growing, minimal cyclicality) — **TGT is the more relevant comp**, and BBY trades roughly in line with or slightly above it, both well below WMT/COST. All peer multiples are aggregator cross-checks (Tier 4), not filings, and should be treated as directional only.

**What growth is priced in:** the reverse-DCF (`valuation.py`, WACC 9.5%, terminal growth 3.0%, 10-year stage-1) finds the current enterprise value of $20,860M implies **-1.0% per year FCF decline for 10 years**, fading to 3% terminal growth. That is a pessimistic embedded expectation — the stock is not priced for the recovery in Sections 4-5 to continue, which is exactly the disconnect a value investor would want to see, PROVIDED the recovery is durable (Section 3's caveats apply). A forward DCF using a more constructive 4%/yr FCF-growth assumption implies $136.5/share (+51%) — probably too optimistic given the flat 3-year revenue CAGR (-1.0%, `ratios.py`) — so the **probability-weighted scenario value of $86.4/share (Bear $58 @ 25%, Base $88.4 @ 50%, Bull $111 @ 25%)** is the more defensible single number, and it sits **~4.5% below** the current price. **[Corrected 2026-10-06: method: lease liabilities are deducted in the equity bridge (and added to EV) although FCF is already after lease expense, SBC ($139M) is added back, and WACC 9.5% is only 4.3 pts over the 5.17% Treasury for beta 1.305; consistent restatement gives a scenario-weighted value of $78–86 (central ~$82 at 10.6%), i.e. 5–17% below the $90.51 price, and an implied FCF growth of +0.8% to +1.6% (not -1.0%), above the dossier's own base-case path of about -1.3%/yr]** The 52-week range is $55.10-$96.53 (FMP profile); at $90.51 the stock is close to its highs, not its lows.

## 8. Bull case and bear case

**Bull case:**
1. Comp sales have inflected from -6.8% (FY24) to +4.1% (Q2 FY27, the strongest quarter in the 8-quarter window), with broad-based category strength (computing +6.8%, home theater +5.6% in Q2 FY27) and guidance raised twice this fiscal year on the strength of it (Section 5). **[Corrected 2026-10-06: wrong: one raise in FY27 (2026-08-27); the Nov-2025 raise belongs to FY26]**
2. Two new, capital-light profit streams — Best Buy Marketplace (US launch, FY26) and Best Buy Ads — are explicitly cited as the primary driver of the domestic gross-margin improvement in three of the last four quarters, and management (incoming CEO Jason Bonfig) has made expanding them a named FY27 priority.
3. Balance sheet is genuinely conservative: net cash position ex-leases, an undrawn $1.25B revolver through 2030, interest coverage of 38x EBIT/interest (TTM, `ratios.py`), and a 4.2% dividend yield backed by ~57-64% payout — a shareholder-yield floor while the turnaround plays out.

**Bear case:**
1. **Leadership discontinuity at the worst possible time.** CEO Corie Barry (7 years in the role) departs 2026-10-31 and CFO Matt Bilunas departs 2026-07-31 with an *external* CFO search still ongoing as of the 2026-09-25 cutoff — both transitions land inside the next two quarters, with a new, first-time CEO (Jason Bonfig) and possibly a new external CFO simultaneously executing a strategy pivot (Marketplace/Ads/Retail-media) neither has run before. **[Corrected 2026-10-06: wrong as of the cutoff: a new CFO with prior CFO experience (Anne Bramman) was appointed on 2026-08-03, effective 2026-08-19 (8-K 0000764478-26-000034)]**
2. **Two years of impairments from the same failed bet.** $646M cumulative Best Buy Health goodwill/intangible write-offs (FY25 + FY26) plus a near-total wind-down of the Yardbird store format (21 stores → 2, per the FY26 10-K store table) show a real, recent history of value-destructive diversification — a portfolio manager should ask what Marketplace/Ads/Best Buy Health-next-act risk looks like under new leadership.
3. **Margin and revenue exposed to two live, quantifiable external cost shocks**: (a) IEEPA tariffs were ruled unauthorized by the Supreme Court (2026-02-20) and BBY has booked $75M of refunds (Q2+Q3 FY27) that will **not repeat**, while the government has "initiated further actions under existing trade authorities" that could reimpose tariffs under different legal cover (10-Q filed 2026-09-04); (b) a DRAM/NAND ("memory") cost spike is pushing computing ASPs up mid-teens% with unit volumes *down* high-single-digits in Q2 FY27 (Q2 FY27 earnings call, 2026-08-27) — i.e., a meaningful share of the headline comp-sales beat is price/mix from a memory shortage passing through to consumers, not pure volume strength.

## 9. Key risks & kill criteria (thesis-invalidation triggers)

1. **Comp sales turn negative for two consecutive quarters** (baseline: Q2 FY27 +4.1% enterprise; FY27 guidance assumes 1.9-3.0% for the year) — would signal the recovery was a comp-driven sugar high, not durable share gain.
2. **CFO hire is delayed past Q3 FY27 earnings (expected ~late Nov 2026) or is an internal/interim appointment without prior public-company CFO experience** — the company itself said it "expects to name a successor with previous CFO experience" (8-K filed 2026-06-22); failure to do so raises succession-planning-quality concerns during a CEO transition. **[Corrected 2026-10-06: moot: Anne Bramman, a former CFO of Nordstrom, Avery Dennison and Carnival, was named CFO on 2026-08-03 (8-K 0000764478-26-000034), effective 2026-08-19]**
3. **Gross margin down >150bps YoY in any quarter once the ~$75M of one-off IEEPA tariff refunds fully laps** (by Q4 FY27) — would show the tariff/memory cost pressure is structural, not transitory.
4. **Another Best Buy Health-scale impairment or a third consecutive year of goodwill write-offs from the same unit** — would confirm the capital-allocation risk flagged in Section 8 is systemic, not resolved.
5. **Lease-adjusted leverage (net debt + operating leases)/(EBITDA+rent) rises above ~1.5x** (baseline 0.53x TTM) — would indicate the conservative balance sheet BBY is relying on as a floor is eroding, e.g. from a large debt-funded buyback restart or a sustained FCF decline.

## 10. Catalysts & calendar

- **Next earnings (Q3 FY27):** not yet announced as of 2026-09-25 cutoff; the prior three Q3 releases fell 2023-11-21, 2024-11-26, 2025-11-25, so **~late November 2026** is the reasonable estimate (not available: exact date).
- **CFO departure:** 2026-07-31 (already occurred by the cutoff); external CFO successor announcement — timing unconfirmed, is itself a near-term catalyst/risk event. **[Corrected 2026-10-06: superseded: the CFO successor was announced 2026-08-03]**
- **CEO transition:** Jason Bonfig becomes CEO 2026-11-01; Corie Barry remains as a paid Strategic Advisor through ~2027-05-01 (Transition Letter Agreement, 8-K Exhibit 10.2 filed 2026-04-23).
- **Dividend dates:** Q2 FY27 dividend ($0.96/share) payable 2026-10-08 to holders of record 2026-09-17.
- **FY27 year-end / Q4 earnings:** based on history, expected early March 2027.

## 11. Red-flag scan

- **Auditor:** Deloitte & Touche LLP; no auditor change disclosed (10-K, Item 9: "None").
- **Material weakness:** none — management and Deloitte concluded disclosure controls and internal control over financial reporting were effective as of 2026-01-31 (10-K, Item 9A).
- **Restatements:** none found in the filings reviewed.
- **SEC/DOJ investigation, going-concern language:** none found.
- **Litigation:** no matters flagged as probable/material beyond ordinary course (10-K, Note 12, Contingencies and Commitments); $76M of outstanding letters of credit. "Price-fixing settlements" appear as a recurring, small non-GAAP reconciling *credit* line item across releases (BBY as an indirect-purchaser plaintiff beneficiary in industry antitrust settlements, not a defendant) — immaterial and not a red flag.
- **Insider selling pattern:** **not independently verified this session** — FMP's insiderTrades tool was access-denied at the current subscription tier. A small manual sample of recent Form 4 filings (SEC EDGAR) showed a cluster of 9 filings on 2026-06-16 (consistent with routine annual equity-vesting/tax-withholding transactions across multiple executives, transaction code patterns consistent with option exercises, e.g. CHRO Kathleen Scarlett's 2026-09-23 Form 4, code "M") and scattered Form 4s through September 2026; this is **not** a systematic 12-month buy/sell-ratio analysis and should not be read as clearing or confirming an insider-selling concern either way.
- **Short-seller reports:** none identified in this session's searches.
- **Governance:** two new independent directors added in the window — Meghan Frank (lululemon CFO, appointed 2025-09-12) and Dylan Jadeja (Riot Games CEO, appointed 2025-12-01) — both routine, not adverse.

## 12. Sources

1. SEC EDGAR submissions index, CIK 0000764478 — `https://data.sec.gov/submissions/CIK0000764478.json`
2. SEC EDGAR XBRL company facts, CIK 0000764478 — `https://data.sec.gov/api/xbrl/companyfacts/CIK0000764478.json`
3. 10-K, fiscal year ended 2026-01-31, filed 2026-03-18 — accession 0000764478-26-000009 (`bby-20260131.htm`)
4. 10-Q, quarter ended 2026-08-01, filed 2026-09-04 — accession 0000764478-26-000042 (`bby-20260801.htm`)
5. 8-K + Ex-99, Q2 FY27 earnings, filed 2026-08-27 — accession 0000764478-26-000037
6. 8-K + Ex-99.1/99.2, Q1 FY27 earnings, filed 2026-05-28 — accession 0000764478-26-000018
7. 8-K + Ex-99, Q4 FY26 / FY26 full-year earnings, filed 2026-03-03 — accession 0000764478-26-000005
8. 8-K + Ex-99, Q3 FY26 earnings, filed 2025-11-25 — accession 0000764478-25-000050
9. 8-K + Ex-99, Q2 FY26 earnings, filed 2025-08-28 — accession 0000764478-25-000035
10. 8-K + Ex-99, Q1 FY26 earnings, filed 2025-05-29 — accession 0000764478-25-000014
11. 8-K + Ex-99, Q4 FY25 / FY25 full-year earnings, filed 2025-03-04 — accession 0000764478-25-000003
12. 8-K + Ex-99, Q3 FY25 earnings, filed 2024-11-26 — accession 0000764478-24-000038
13. 8-K, CEO succession announcement, filed 2026-04-22 — accession 0000764478-26-000012 (Ex-99.1 press release; Ex-10.1 employment letter; Ex-10.2 transition letter)
14. 8-K, CFO transition announcement, filed 2026-06-22 — accession 0000764478-26-000027
15. 8-K, $1.25B revolving credit facility, filed 2025-04-23 — accession 0000764478-25-000011
16. 8-K, board appointment (Dylan Jadeja), filed 2025-12-01 — accession 0000764478-25-000052
17. 8-K, board appointment (Meghan Frank), filed 2025-09-12 — accession 0000764478-25-000045
18. SEC Form 4 sample, CHRO Kathleen Scarlett, filed 2026-09-24 — accession 0001225208-26-007910
19. FMP `company` profile-symbol and `peers` endpoints (accessed 2026-09-26) — price $90.51, market cap ~$19.08B, beta 1.305, 52-week range $55.10-$96.53
20. V4 `d4_live_snapshot.parquet` quant snapshot (orchestrator-supplied, 2026-09-25) — cross-checked; see Data Quality Note for the one material discrepancy found
21. Best Buy Q2 FY27 earnings call transcript coverage — The Motley Fool, 2026-08-31 (`fool.com/earnings/call-transcripts/2026/08/31/best-buy-bby-q2-2027-earnings-call-transcript/`) — membership-count and memory-cost commentary
22. Retail Dive, "Best Buy to close as many as 30 stores this year" (Feb-2026 earnings call coverage) — store-closure guidance cross-check
23. MacroTrends (`macrotrends.net/stocks/charts/BBY/best-buy/pe-ratio`) and GuruFocus (`gurufocus.com/term/enterprise-value-to-ebitda/BBY`) — 10-year P/E and EV/EBITDA range, aggregator cross-check only
24. Peer multiples (WMT, TGT, COST), various aggregators accessed 2026-09-26 — aggregator cross-check only, not primary
25. `ratios.py` and `valuation.py` outputs (this session, 2026-09-26), computed from inputs sourced to items 3-11 above; input JSON and script stdout cached at `C:\Users\user\eqv4\cache\f3\BBY\`

---

### Data Quality Note

**Primary-sourced:** all quarterly and annual GAAP/Adjusted income-statement, balance-sheet and cash-flow figures (Sections 4, 6, and the `ratios.py`/`valuation.py` inputs) trace to 8-K earnings-release exhibits and the FY26 10-K/Q2 FY27 10-Q (Sources 3-12). `verify_data.py` ran PASS-WITH-WARNINGS on a 29-datapoint intake sample: 100% of sampled figures traced to a Tier 1-3 source, with the single warning being an expected TTM-vs-fiscal-year period-alignment note (disclosed, not a defect).

**One material data conflict found and resolved:** the orchestrator-supplied quant snapshot's TTM figures are **internally inconsistent in exactly the way flagged** — its "TTM revenue" of $41,691.0M is not actually a trailing-twelve-month figure at all; it is **FY2026 full-year revenue** (year ended 2026-01-31, per the 10-K) carried over unchanged. Independently summing the four most recent quarters (Q3 FY26 + Q4 FY26 + Q1 FY27 + Q2 FY27, from the 8-K releases) gives true TTM revenue of **$42,201M**. By contrast, the snapshot's COGS ($32,631M), gross profit ($9,570M), operating income ($1,710M), net income ($1,272M), operating cash flow ($2,475M) and capex ($707M) all match my independently-derived true-TTM sums for those same four quarters **exactly**. So the snapshot mixed a stale (FY26 year-end) revenue figure with true-TTM figures for every other line — the "~$510M / 1.2%-of-revenue" gap the orchestrator flagged is fully explained by this, not by an XBRL tagging quirk. Practical effect: the snapshot's implied gross margin (23.0%) and operating margin (4.10%) are both overstated by roughly 30-40bps versus the true TTM figures used throughout this dossier (22.7% gross margin, 4.05% operating margin) — small, but worth the correction for anyone chaining this snapshot into further screens.

**Estimated / lower-confidence:** the WACC (9.5%) and growth assumptions feeding the forward DCF and reverse-DCF are analyst judgment, not sourced; NTM P/E is cross-checked across the orchestrator snapshot (12.78x) and two aggregator reads (12.99x, 13.99x) that agree only loosely, reflecting different pull dates/estimate bases; peer multiples (WMT/TGT/COST) are aggregator-sourced (Tier 4) and dated to their own August-September 2026 pulls, not verified against those companies' own filings.

**Not available (explicitly, not silently assumed):** a quantified shrink/inventory-shrinkage rate or trend (BBY discloses only boilerplate "physical inventory losses (resulting from, for example, theft)" language with no figure); a full 12-month statistical insider Form-4 pattern analysis (FMP `insiderTrades` tool was access-denied at the current plan tier); exact My Best Buy Plus vs. My Best Buy Total membership split or any membership count before February 2026; the exact Q3 FY27 earnings date.

*This is independent research for the v4 program, not personalised investment advice.*

## Correction (verification DV05, 2026-10-06)
Scope: BBY re-checked against 10-Q 0000764478-26-000042 (quarter ended 2026-08-01), 10-K 0000764478-26-000009, 8-K Ex-99 0000764478-26-000037/-000018/-000005/-25-000050/-25-000014, 8-Ks -26-000012 (CEO succession), -26-000027 (CFO departure), -26-000034 (CFO appointment) and XBRL companyfacts CIK0000764478. The eight-quarter table, TTM sums (revenue $42,201M, operating income $1,710M, OCF $2,475M, capex $707M, FCF $1,768M; the mechanical xbrl flag compares a TTM sum with a single quarter), every guidance range in s5, net cash $1,086M, lease liabilities $2,964M, buybacks and the $0.96 dividend tie.
1. **CFO status (s1, s8 bear 1, s9(2), s10) — FAIL.** Wrong: "external CFO search still ongoing as of the 2026-09-25 cutoff". On 2026-08-03 Best Buy appointed Anne Bramman (former CFO of Nordstrom, Avery Dennison and Carnival; most recently Circana) as CFO effective 2026-08-19 (8-K 0000764478-26-000034). Kill criterion 2 is already satisfied; the leadership-discontinuity risk is the CEO handover only (Barry departs 2026-10-31, Bonfig CEO 2026-11-01; 8-K -26-000012).
2. **Guidance "raised twice this fiscal year" (s1, s8 bull 1).** FY27 was raised once (2026-08-27); Q1 FY27 reiterated; the Nov-2025 raise was FY26.
3. **Valuation method (s7, rule e) — FAIL.** (a) Operating-lease liabilities ($2,964M) are included in EV for the reverse DCF and deducted in the equity bridge of the forward DCF although FCF is already after operating-lease expense (ASC 842): double count of about $14 per share. (b) SBC ($139M in FY26) is added back inside FCF. (c) WACC 9.5% is only 4.3 pts over the 5.17% Treasury (25 Sep 2026) for beta 1.305; CAPM gives 10.1% (Blume beta 1.2, ERP 4.14%), 10.6% (raw beta, ERP 4.14%) or 11.0% (ERP 4.5%). Restated using the dossier's own back-solved scenario growth paths (-6.4% / -1.3% / +1.6%) on SBC-burdened FCF $1,629M and an equity bridge without lease liabilities: scenario-weighted value $85.9 (10.1%), $81.6 (10.6%), $77.6 (11.0%) vs $86.4 stated; bear/base/bull at 10.6% = $59.8 / $83.2 / $100.4. Price $90.51 is therefore 5–17% (central ~11%) above scenario value, not 4.5%. Equity-basis implied FCF growth at the CAPM rate is +0.8% (10.6%) to +1.6% (11.0%) against the stated -1.0%; relative to the base-case path (about -1.3%/yr) implied_vs_base = above. The claim that "the market is pricing negative long-run FCF growth" does not survive.
4. **Verdict logic (s1).** Operating evidence is strong (comparable sales +4.1%, FY27 guide raised to $6.70–$6.90 adjusted EPS, net cash, CFO named, 4.2% yield) and the leadership risk is smaller than stated; the valuation leg is weaker than stated (price above scenario value). INCLUDE-SMALL is retained; if the lead requires price at or below scenario value for any INCLUDE-SMALL the name would fall to WATCH. No F*_summary.json contains BBY (its verdict is parsed from this dossier's text by lead_build_portfolio.py), so no summary field was edited.
Verdict changes: none made here (INCLUDE-SMALL retained, marginal on valuation).
