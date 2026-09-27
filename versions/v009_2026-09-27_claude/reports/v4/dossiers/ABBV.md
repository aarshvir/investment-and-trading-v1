# AbbVie Inc. (ABBV) — Diligence Dossier

**Agent:** F51 (wave 3) | **As of:** 2026-09-25 close (px $264.34, mktcap $467.14bn per b1_live_scores.csv 2026-09-25)

## 1. Verdict
**INCLUDE-SMALL** (half weight). Thesis horizon 12–36 months. The Humira patent-cliff replacement thesis
(Skyrizi/Rinvoq) has genuinely worked — immunology revenue is still growing double digits — but the named
reservation is specific: AbbVie carries **negative consolidated stockholders' equity** (−$5.9bn at 2026-06-30) on
~$70.8bn of total debt, and its "adjusted" EPS excludes a large, *recurring* (not one-off) acquired-IPR&D/milestone
expense line ($2.76/share in FY2025 alone) that behaves like an ongoing cost of maintaining the pipeline. The
reverse DCF implies growth roughly in line with — not below — a reasonable base case, so there is little margin of
safety on top of those balance-sheet and earnings-quality flags.

## 2. Business in plain English
AbbVie is a global biopharmaceutical company. Its largest franchise is immunology (Skyrizi for psoriasis/psoriatic
arthritis/IBD, Rinvoq for rheumatoid arthritis and related conditions, and the legacy Humira, now in steep
biosimilar-driven decline), plus neuroscience (Vraylar, Botox Therapeutic, migraine drugs Ubrelvy/Qulipta), oncology
(Imbruvica, Venclexta, Elahere) and an aesthetics business (Botox Cosmetic, fillers) inherited from the 2020 Allergan
acquisition. It earns money by selling patented/branded drugs and devices, protected by patents and increasingly by
complex payer-rebate contracting (source: ABBV 10-Q, period 2026-06-30, filed 2026-08-03; ABBV 8-K Ex.99.1 releases).

## 3. Why the model likes it / is this durable — and a genuine data conflict
b1_live_scores.csv (as_of 2026-09-25): composite decile 6, quintile 3, live_rank 243. Quality family (fam_Q=6)
scores well on gross-profit/assets (pct 61.5%) and OCF/assets (pct 71.1%), but **the ROE field is blank/missing for
ABBV in b1_live_scores.csv** — not zero, not low, genuinely absent. This is not a data-pipeline bug in isolation: it
is the direct, explainable consequence of the negative-stockholders'-equity finding in §6 below (ROE is undefined or
economically meaningless when book equity is negative). This is exactly the kind of quant-vs-filing conflict the
wave-3 mandate asks to be surfaced explicitly: **data_conflict — b1's quality composite is silently missing one of
its inputs for ABBV, for a real and identifiable balance-sheet reason, not a data error.**
The growth driver itself (Skyrizi + Rinvoq immunology growth outrunning Humira's decline) is durable in the sense
that it is now visible in two-plus years of reported revenue, not a projection (see §4).

## 4. Last quarters of results (source: ABBV 8-K Ex.99.1 earnings releases, cited; GAAP unless labelled adjusted)
| Quarter | Net revenue ($bn) | YoY (reported/operational) | GAAP dil. EPS | Adj. dil. EPS | Immunology revenue ($bn) |
|---|---|---|---|---|---|
| Q3 2025 | 15.776 | +9.1% / +8.4% | $0.10 | $1.86 | 7.885 |
| Q4/FY2025 | 16.618 (Q4); 61.160 (FY) | FY +8.6%/+8.5% | FY $2.36 (Q4 not itemized above) | FY $10.00 (−1.2% YoY) | FY 30.406 (+14.0%/+13.9%) |
| Q1 2026 | 15.002 | +12.4% / +10.3% | $0.39 (−45.8% YoY) | $2.65 (+7.7%) | 7.290 (+16.4%/+14.3%) |
| Q2 2026 | 16.990 | +10.2% / +9.5% | $2.03 (+290.4% YoY) | $3.65 (+22.9%) | 8.786 (+15.1%/+14.6%) |
Within immunology (Q2 2026): Skyrizi $5.505bn, Rinvoq $2.525bn, Humira $756m (Humira now a small, declining residual
— down from $993m in Q3 2025 and $4.540bn for all of FY2025 — confirming the patent-cliff erosion is largely
mechanical and already mostly realized). GAAP EPS is extremely volatile quarter to quarter (e.g. Q1 2026 $0.39 vs
Q2 2026 $2.03) almost entirely because of the acquired-IPR&D/milestone expense line (see §5–6), not because of core
operating volatility — a real earnings-quality caveat for anyone reading GAAP EPS alone.

## 5. Guidance track record (last several releases; FY adjusted diluted EPS — AbbVie's own disclosure pattern requires
care here, detailed below)
AbbVie's official guidance **excludes future acquired-IPR&D/milestone expense** because it "does not forecast" that
item; it then pre-announces each quarter's actual IPR&D hit via a standalone Item 2.02 8-K roughly a month before the
full earnings release, and republishes an "updated" guidance range that folds in the now-known charge. Comparing
headline ranges across quarters without tracking this two-step process would misstate whether guidance was raised or
cut — exactly the wave-3 lesson this dossier is required to apply.
1. **Q3 2025 (2025-10-31):** FY2025 raised from $10.38–$10.58 to **$10.61–$10.65** (adjusted EPS, excluding Q4 IPR&D).
2. **2026-01-07 8-K (pre-announcement):** discloses Q4 2025 IPR&D/milestone expense of $1.3bn pretax (−$0.71/share)
   and restates the "including Q4 IPR&D" FY2025 range down to **$9.90–$9.94**.
3. **Q4/FY2025 (2026-02-04):** FY2025 actual adjusted EPS **$10.00** — a beat versus the IPR&D-inclusive $9.90–$9.94
   range, but a −1.2% YoY decline once the year's cumulative $2.76/share of IPR&D charges are counted. FY2026 initial
   guidance issued (excluding 2026 IPR&D): **$14.37–$14.57**.
4. **2026-04-03 8-K:** discloses Q1 2026 IPR&D expense of $744m pretax (−$0.41/share), restates FY2026 (IPR&D-
   inclusive) to **$13.96–$14.16**.
5. **Q1 2026 (2026-04-29):** genuinely **raised** (on an apples-to-apples, IPR&D-inclusive basis) to **$14.08–$14.28**.
6. **Q2 2026 (2026-07-31):** updated to **$13.87–$14.07**, explicitly to absorb $0.14/share of dilution from the
   pending Apogee Therapeutics acquisition (partially offset by $0.10/share of operating overperformance) — a
   guidance *change driven by a new deal*, not an operating cut, but the headline range is nonetheless lower than
   the prior $14.08–$14.28.
Net: guidance has been raised on an operating basis in every quarter reviewed once IPR&D and M&A dilution are
adjusted for consistently — but the headline ranges alone, read naively, would look like an unexplained miss (FY25)
followed by a cut (Q2'26) or a raise (Q1'26) depending on which two releases are compared. This dossier resolves that
by reading the pre-announcement 8-Ks, per the wave-3 mandate.

## 6. Earnings quality & balance sheet (consolidated, GAAP, entity = AbbVie Inc. and subsidiaries; 10-Q period
2026-06-30, filed 2026-08-03, and 10-Q period 2026-03-31, filed 2026-05-08)
- **Stockholders' equity is NEGATIVE:** total stockholders' equity −$5,935m at 2026-06-30 (−$6,656m at 2026-03-31),
  driven by treasury stock −$10,618m and accumulated deficit in retained earnings −$17,333m against additional
  paid-in capital of only $23,156m. This is a longstanding structural feature (large buybacks/dividends and Allergan-
  deal-related charges over several years, not a new single-quarter event) but it means AbbVie has **no equity
  cushion**: the balance sheet is supported entirely by ~$85bn of goodwill+intangibles ($35.5bn + $49.1bn at
  2026-06-30) against $135.1bn of total assets and $141.0bn of total liabilities.
- **Leverage:** total debt $70.8bn, cash $6.6bn, net debt $64.3bn (both at 2026-06-30). TTM EBITDA (sum of the last
  four quarterly EBITDA figures reconciled in the company's filings, Q3'25–Q2'26) ≈ $21.2bn → **net debt/EBITDA
  ≈ 3.0x**, consolidated. This is a moderate, investment-grade-consistent level for large pharma but leaves no room
  for a leverage surprise given the zero equity cushion above.
- **Recurring "one-off" item:** acquired IPR&D/milestone expense was $2.76/share for FY2025 (~$4.9bn pretax at ~1.77bn
  shares) and continued at $0.41/share (Q1'26) and further amounts in Q2/Q3 2026 — i.e., AbbVie has incurred a large
  IPR&D charge in every recent quarter. Treating it as purely non-recurring in "adjusted EPS" overstates normalized
  earnings power if the company's business-development pace (licensing deals funding the pipeline) continues at a
  similar cadence, which recent history suggests it will.
- **Litigation accrual:** $1.7bn at 2026-06-30 (up from $1.6bn at 2025-12-31) — see red-flag scan.
- **Capital return:** quarterly dividend raised 5.5% (declared 2025-10-31, from $1.64 to $1.73/share effective the
  2026-02-17 payment) — a genuine, well-covered raise (FCF, see below, comfortably exceeds the dividend).
- **FCF:** TTM (Q3'25–Q2'26) FCF ≈ $19.68bn (sum of quarterly OCF-less-capex, SEC XBRL/10-Q cash-flow statements) on
  ~1.771bn diluted shares → FCF/share ≈ $11.11; quarterly FCF is lumpy (Q3'25 $7.53bn included a large working-capital
  swing per the cash-flow statement) so the TTM figure, not any single quarter, should be used.

## 7. Valuation snapshot & reverse DCF (own build; no V1 row exists for ABBV — not previously a top-70/lane name)
Adjusted NTM P/E on FY2026 guidance midpoint ($13.97): 264.34/13.97 = **18.9x**. EV (mktcap $467.1bn + net debt
$64.3bn) / TTM FCF ($19.68bn) ≈ **27.0x**; FCF yield on equity market cap ≈ 4.2%.
Reverse DCF (2-stage, 10-yr + Gordon terminal; terminal growth 3.0%): given AbbVie's low reported beta (0.281, FMP)
understates its true risk (patent-cliff/litigation/negative-equity risk are not well captured by historical beta for
a company mid-transition), I ran two WACC scenarios rather than picking one: **at WACC 7.5%, implied 10-yr FCF/share
growth ≈ 5.0%/yr; at WACC 8.5%, implied growth ≈ 7.7%/yr.** A reasonable evidence-based base case — mid-single-digit
revenue growth (immunology deceleration as Skyrizi/Rinvoq mature, partially offset by neuroscience and an early
obesity pipeline) translating to high-single-digit EPS/FCF growth via margin and buybacks — sits at roughly 6–8%/yr,
i.e., **inside the WACC-sensitivity band, not clearly below it**. Verdict: **implied_vs_base = "in_line."** This is
a fair, not a cheap, price for a business whose two biggest growth drivers (Skyrizi, Rinvoq) are still compounding
but will mechanically decelerate as they scale.

## 8. Bull case
1. The Humira patent-cliff bear case is now largely played out and visible in the numbers: Humira was $756m of
   revenue in Q2 2026, versus $4.54bn for all of FY2025 and far larger before — the worst of the erosion is behind,
   confirmed by four quarters of reported data, not a projection.
2. Immunology ex-Humira (Skyrizi + Rinvoq) grew revenue 14.6% operationally in Q2 2026 on an already-large base
   ($8.0bn combined in the quarter) — genuine, large-scale, currently-realized growth.
3. Dividend raised 5.5% with FCF coverage comfortable (TTM FCF ≈ $19.7bn vs. TTM dividends paid ≈ $11.9bn implied by
   the quarterly cash-flow statements), supporting the income case even if growth decelerates.

## 9. Bear case
1. Zero equity cushion (negative $5.9bn stockholders' equity) plus ~3.0x net debt/EBITDA leaves no room for a
   negative surprise (an adverse litigation judgment, a failed pipeline bet, or a large dilutive deal) without
   raising real balance-sheet-risk questions, unlike most other large-cap pharma peers with positive equity.
2. The recurring, large acquired-IPR&D/milestone expense line ($2.76/share FY2025) is excluded from "adjusted" EPS
   every year; if treated as a normal, recurring cost of maintaining AbbVie's pipeline (which the multi-year pattern
   suggests it is), normalized earnings power is lower than the headlined adjusted EPS implies.
3. Reverse DCF shows the current price already embeds a base-case-level growth assumption — there is little room
   for the Skyrizi/Rinvoq deceleration (both are large, maturing franchises) to arrive faster than modeled without
   the stock re-rating down.

## 10. Key risks & kill criteria (measurable triggers that would invalidate the thesis)
1. Consolidated net debt/EBITDA (per the 10-Q's own reconciliation) exceeds 3.5x in any quarter.
2. Combined Skyrizi + Rinvoq operational revenue growth falls below 8% YoY for two consecutive quarters (vs. 14.6%
   in Q2 2026).
3. Acquired IPR&D/milestone expense exceeds $3.00/share on a trailing-12-month basis (vs. $2.76/share in FY2025),
   signalling an accelerating, not one-off, drag.
4. Adjusted diluted EPS guidance is cut on an IPR&D-and-M&A-adjusted, apples-to-apples basis (i.e., excluding the
   effect of newly disclosed IPR&D charges and disclosed acquisitions, which are not true operating cuts).
5. An adverse final judgment or settlement in the Allergan opioid MDL or Biocell breast-implant litigation materially
   exceeding the current $1.7bn litigation accrual.

## 11. Catalysts & calendar
Next earnings: Q3 2026 results, estimated ~2026-10-30/31 (Q3 2025 was reported 2025-10-31; **estimate, not
confirmed**). Expect a pre-announcement Item 2.02 8-K disclosing the Q3 2026 IPR&D/milestone charge roughly 3–4
weeks before that release, consistent with the pattern in §5. Apogee Therapeutics acquisition expected to close Q3
2026 (per the Q2 2026 release) — watch for the closing 8-K and updated dilution guidance.

## 12. Red-flag scan
- **Litigation (10-Q, period 2026-06-30, "Legal Proceedings and Contingencies"):** litigation accrual $1.7bn
  (2026-06-30) vs $1.6bn (2025-12-31). Opioid: ~215 lawsuits pending against Allergan (opioid marketing/sale
  allegations), consolidated as MDL No. 2804 (N.D. Ohio) plus ~20 state-court cases; ~20 of the ~215 in the process
  of dismissal under a previously announced settlement. Breast implants: Allergan Biocell textured-implant litigation
  — US lawsuits substantially resolved by a June 2026 settlement agreement, but ~1,300 MDL cases (D.N.J., MDL 2921),
  ~475 state-court cases and ~1,080 international cases remain (Netherlands claims dismissed Dec 2025, under appeal
  Mar 2026). Humira pricing: *Camargo v. AbbVie* (list-price class action) dismissed without prejudice Jan 2026,
  appealed Mar 2026 to the Seventh Circuit. Humira antitrust: *Sheet Metal Workers' Health Plan… v. AbbVie* (filed
  Jan 2025, N.D. Ill.) alleges AbbVie's Humira rebating practices impair biosimilar competition, an antitrust theory —
  ongoing, unresolved. Legacy Niaspan patent-settlement antitrust MDL (Kos Pharmaceuticals/Abbott legacy) also still
  pending.
- No auditor change, restatement, or going-concern language found in the sections reviewed. Insider Form 4 pattern
  and short-seller reports were not checked in the time available (limitation, disclosed).
- **Data conflict vs b1:** ROE field missing in b1_live_scores.csv for ABBV — explained by negative equity (§3, §6).
  This is the dossier's headline `data_conflicts` entry.

## 13. Sources
1. ABBV 10-Q, period 2026-06-30, filed 2026-08-03 — sec.gov/Archives/edgar/data/1551152/000155115226000026/abbv-20260630.htm
2. ABBV 8-K Ex.99.1, 2026-07-31 (Q2 2026 results) — .../000155115226000023/abbv-20260630xexhibit991.htm
3. ABBV 8-K Ex.99.1, 2026-04-29 (Q1 2026 results) — .../000155115226000013/abbv-20260331xexhibit991.htm
4. ABBV 8-K Ex.99.1, 2026-02-04 (Q4/FY2025 results) — .../000155115226000004/abbv-20251231xexhibit991.htm
5. ABBV 8-K Ex.99.1, 2025-10-31 (Q3 2025 results) — .../000155115225000047/abbv-20250930xexhibit991.htm
6. ABBV 8-K (Item 2.02), 2026-01-07 (Q4 2025 IPR&D pre-announcement) — .../000155115226000002/abbv-20260107.htm
7. ABBV 8-K (Item 2.02), 2026-04-03 (Q1 2026 IPR&D pre-announcement) — .../000155115226000011/abbv-20260403.htm
8. SEC XBRL companyfacts and quarterly income/balance/cash-flow data, CIK0001551152, retrieved 2026-09-26 (via FMP
   statements tool, which sources from the same filings; primary filing citations above take precedence on any
   conflict)
9. v4/data/b1_live_scores.csv (as_of 2026-09-25); v4/outputs/Q06_triage.json (ABBV triage entry)

## 14. Data Quality Note -- data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (period ended 2026-06-30; 10-Q filed 2026-08-03). Events checked to
2026-09-25 (including the two IPR&D pre-announcement 8-Ks dated 2026-01-07 and 2026-04-03, used to reconcile the
guidance track record in §5); no Q3 2026 filing exists yet. GAAP figures are labelled GAAP; all "adjusted" figures
are the company's own non-GAAP measures, labelled as such, with the IPR&D-exclusion caveat discussed at length in
§5–6 because it materially affects how "guidance raised/cut" claims should be read. Research, not personalized
investment advice.
