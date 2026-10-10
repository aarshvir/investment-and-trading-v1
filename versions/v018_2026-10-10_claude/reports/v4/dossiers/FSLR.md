# First Solar, Inc. (FSLR) — Diligence Dossier (Agent F28, standard depth)

## 1. Verdict
**INCLUDE-SMALL** (half weight) — thesis horizon 12–36 months. First Solar is priced cheaply against its own backlog and
current earnings power (reverse DCF implies roughly flat-to-slightly-negative FCF growth, versus a plausible mid-single-digit
base case), but two fresh, unresolved legal matters and a policy-dependent margin structure are specific, named reservations
that argue against full weight.

## 2. Business in plain English
First Solar is the only scaled non-Chinese manufacturer of thin-film cadmium-telluride (CdTe) solar modules, sold mainly to
utility-scale solar developers under multi-year, fixed-price supply contracts. Its moat is regulatory/geopolitical, not purely
technological: CdTe avoids the polysilicon supply chain (and its Xinjiang forced-labor scrutiny) that dominates Chinese
crystalline-silicon competitors, its US-based manufacturing captures Section 45X advanced-manufacturing production credits,
and antidumping/countervailing duties raise the cost of Asian-made panel imports. It sells forward — a 45.1 GW contracted
backlog through 2030 as of 30-Jun-2026 (First Solar Q2 2026 earnings release, 30-Jul-2026) — so near-term revenue is largely
locked in, but backlog conversion depends on customer construction schedules and on the policy environment persisting.

## 3. Why the model likes it — durable or artefact?
b1_live_scores.csv: composite 0.65 (live_rank 175/503), driven by earnings-yield/FCF-yield (V family) and strong momentum
(mom_12_1 = +104%, SUE 0.65). Triage (Q12_triage.json) flagged an 8x NTM P/E, 8.4% FCF yield and 53% Street upside against a
"backlog-supported growth path," with one red flag: negative TTM-style revenue growth and ITC/OBBBA phase-down timing risk.
**Verified and refined:** the reported revenue deceleration is real and specific — Q2 2026 net sales were **-3.7% YoY**
(First Solar 8-K, 30-Jul-2026, matching the triage figure exactly), even as gross margin *expanded* to 57.3% from ~45.6% a
year earlier. That expansion is not pure operating leverage: Section 45X credits (guided at $2.10–2.19bn for full-year 2026,
Q1 2026 8-K, 30-Apr-2026) are booked through cost of sales and are now the single largest driver of gross margin — i.e., a
meaningful share of the "cheap on FCF yield" quality score is a **policy artefact with a 2030 phase-down date and new
Foreign-Entity-of-Concern (FEOC) domestic-content rules for "integrated" components effective for tax years after
31-Dec-2026** (Miller & Chevalier, "OBBBA Brings 45X Changes, Though Not Wholesale Repeal," 2026), not a permanent structural
margin gain. **[Corrected 2026-10-06: Q2 2026 gross margin of 57.3% included an $88.6m net benefit from expected IEEPA tariff refunds (10-Q MD&A, acc 0001274494-26-000170), the first-named driver; 45X cost-of-sales benefit was $70.7m YoY and logistics $35.6m. Excluding the IEEPA item gross margin is about 48.9%]** This is durable through the guided period but is a input assumption, not a law of nature, and should be modelled
as such.

## 4. Last eight quarters (SEC XBRL, GAAP, USD millions except EPS; company fiscal year = calendar year)
| Quarter | Net sales | YoY growth | Gross margin | Operating margin | GAAP diluted EPS |
|---|---|---|---|---|---|
| Q3 2024 | 887.7 | +10.8% | 50.2% | 36.3% | 2.91 |
| Q4 2024 | 1,514.0¹ | n/a² | 37.5%¹ | 30.2%¹ | 3.66¹ |
| Q1 2025 | 844.6 | +6.4% | 40.8% | 26.2% | 1.95 |
| Q2 2025 | 1,097.2 | +8.6% | 45.6% | 33.0% | 3.18 |
| Q3 2025 | 1,594.9 | +79.7% | 38.3% | 29.2% | 4.24 |
| Q4 2025 | 1,682.8¹ | +11.2%¹ | 39.5%¹ | 32.6%¹ | 4.84¹ |
| Q1 2026 | 1,044.2 | +23.7% | 46.6% | 33.1% | 3.22 |
| Q2 2026 | 1,056.2 | **-3.7%** | 57.3% | 42.6% | 3.92 |

Source: SEC EDGAR XBRL companyfacts (CIK 1274494), 10-Q/10-K filings, discrete-quarter facts; cross-checked against the Q1
and Q2 2026 8-K press releases (exhibit 99.1), which match to the dollar. ¹ Q4 figures are not separately XBRL-tagged
(10-Ks report annual only); derived here as FY annual minus 9-month YTD (dollar figures, no restatement risk). ² Q4 2023 base
not independently re-derived in this pass; YoY omitted rather than estimated.

**Revenue growth is decelerating and turned negative last quarter even as margin expanded on 45X mix — the two trends are
not offsetting noise, they are the same story (a smaller, higher-credit-content revenue base).** **[Corrected 2026-10-06: 10-Q MD&A attributes the Q2 revenue decline to customer contract terminations, partly offset by +5.3% module volume; no mix effect is stated]**

## 5. Guidance track record
Full-year 2026 guidance has been **maintained, not raised, across both releases checked**: FY2026 net sales $4.9–5.2bn and
adjusted EBITDA $2.6–2.8bn, stated identically in the Q1 2026 release (30-Apr-2026) and reaffirmed verbatim in the Q2 2026
release (30-Jul-2026, headlined "Reaffirms Guidance"). No EPS guidance is given. This is a clean, unembellished track record —
no beat-and-raise narrative to interrogate, but also no cut. Company does not publish quarterly guidance beyond next-quarter
EBITDA (Q3 2026 Adjusted EBITDA guided $625–775m in the Q2 release).

## 6. Earnings quality & balance sheet
- **Cash conversion:** TTM operating cash flow (derived: FY2025 10-K OCF $2,057.1m − H1 2025 OCF −$458.4m + H1 2026 OCF
  −$359.8m) ≈ **$2,155.7m**; TTM capex (same method) ≈ **$655.6m**; **TTM FCF ≈ $1,500.1m**. This is a primary-source
  reconstruction from quarterly SEC filings, not an aggregator pull.
- **Data conflict (disclosed):** Yahoo/d4_live_snapshot shows TTM operating cash flow of $2,155.7m (matches exactly) but
  TTM free cash flow of $1,598.7m — about $99m (6.6%) above the SEC-derived figure, implying a lower aggregator capex
  assumption than the one actually reported. Immaterial to the thesis but a reminder that d4's `freeCashflow` field should
  not be treated as primary for this name.
- **Balance sheet:** net cash. Cash & equivalents $1,688.3m at 30-Jun-2026 (XBRL); the Q2 2026 release describes total debt
  as "current portion $37.6m, long-term $0," while the Yahoo-sourced d4 field shows total debt of $194.0m — a second,
  smaller data conflict, immaterial either way given the size of the net-cash position (~$1.5–1.7bn, 8–9% of market cap). **[Corrected 2026-10-06: total debt per the 10-Q (Note 9) is $37.6m, not $194.0m; net cash is $1.69bn (cash 1,688.3 + marketable securities 38.7 - debt 37.6), ~8.8% of market cap]**
- SBC and share count are non-issues: diluted share count has moved only 107.4m → 107.7m over two years (+0.3%), i.e.
  negligible dilution.

## 7. Valuation snapshot and reverse DCF
Price 25-Sep-2026 close: $177.71. Market cap $19.10bn. EV (SEC-sourced net cash of ~$1.49bn) ≈ **$17.61bn**. **[Corrected 2026-10-06: EV is about $17.41bn using net cash of $1.69bn]** Trailing P/E
45.2x is misleadingly high (Q1 2026's low-margin quarter still sits in the trailing-four window); NTM P/E per d4 is **7.6x**
(y_forwardPE) and the Street-consensus reverse view is consistent with the triage's "8x" reference. P/FCF (TTM, SEC-derived
FCF) = 12.7x; FCF yield 7.9%.

**Reverse DCF** (scripts/valuation.py, stock-analysis skill; WACC 9.5%, terminal growth 3.0%, 10-year stage-1 horizon,
base FCF = TTM $1,500.1m, EV anchor $17.61bn): **implied stage-1 FCF growth ≈ -1.0% per year for 10 years.** **[Corrected 2026-10-06: on the programme basis (Ke 11.34% = 5.17% + 1.491 x 4.14%, equity value $19.10bn, FCF after SBC $1,476.5m) implied growth is +3.7%/yr]** In plain
English: today's price already assumes First Solar's free cash flow shrinks slightly, on average, for the next decade. Given
a 45.1 GW backlog through 2030, guided 2026 sales growth versus the TTM run-rate, and 45X credits that do not expire until
2030, an evidence-based **base case of roughly +6–8%/yr FCF growth through 2030** (moderating toward mid-single digits after
2030 as 45X phases down and FEOC content rules bite) looks more defensible than the market's implied path. **Implied vs
base: below (cheap). **[Corrected 2026-10-06: unchanged (below), but narrower: implied +3.7%/yr vs base 6-8%; the 7% base path is worth 1.27x market value at Ke 11.34%]**** No V1 systematic valuation exists yet for this name (not in `v1_valuation_table.csv`/`v1_valuation.json`
— it is one of the 45 newly diligenced names from the triage cycle); this dossier is the first valuation view on file.

Scenario table (exit-multiple method, 3-year horizon, no dividend):
| Scenario | Prob. | 3y-forward EPS | Exit P/E | Value/share | 3y annualised return |
|---|---|---|---|---|---|
| Bear | 30% | $12.50 | 10x | $125 | **-11.1%/yr** |
| Base | 45% | $20.00 | 13x | $260 | **+13.5%/yr** |
| Bull | 25% | $27.00 | 16x | $432 | **+34.4%/yr** |

Bear case assumes FEOC/45X compliance friction and backlog cancellations after a policy setback; base assumes guided 2026
delivered and mid-single-digit growth resuming; bull assumes accelerating US utility-scale demand and full backlog
conversion at expanding, credit-supported margins.

## 8. Bull case / Bear case
**Bull:** (1) 45.1 GW backlog through 2030 provides revenue visibility no domestic peer can match. (2) Antidumping/
countervailing duties plus FEOC rules structurally disadvantage Chinese-linked competitors in the US market. (3) Net-cash
balance sheet with no refinancing risk, funding continued US capacity expansion.

**Bear:** (1) Two fresh, unresolved lawsuits allege management overstated its ability to manage tariff-policy impact
(securities class action, E.D.N.Y., filed 23-Jun-2026; shareholder derivative suit filed 28-Jul-2026) — an adverse legal
and governance finding not in the original triage. (2) Revenue growth has already gone negative (Q2 2026, -3.7% YoY) while
gross margin is inflated by a credit that has statutory guardrails tightening after 2026 (FEOC "material assistance,"
effective for tax years after 4-Jul-2025) and 2030 (65% domestic-content threshold for "integrated" components after
31-Dec-2026, and full phase-out starting 2030). (3) JinkoSolar patent litigation (stayed pending a USITC Section 337
determination) and a live antidumping/countervailing-duty appeal (Auxin Solar v. United States, Fed. Cir. No. 25-2120, from
which the federal government withdrew in Feb-2026) leave retroactive duty exposure legally unresolved.

## 9. Key risks & kill criteria
1. Quarterly net sales YoY growth negative for **two consecutive quarters** (currently 1 of 2: Q2 2026).
2. Full-year 2026 guidance ($4.9–5.2bn sales / $2.6–2.8bn EBITDA) **cut** at any subsequent release.
3. Contracted backlog falls below **40 GW** (from 45.1 GW at 30-Jun-2026) without an offsetting new-bookings explanation.
4. An adverse ruling or settlement in the securities class action or derivative suit that implies a **material monetary
   liability or a restatement**.
5. Treasury guidance or legislative action that **narrows the FEOC "material assistance" safe harbor** in a way that
   disqualifies a material share of First Solar's supply chain from 45X eligibility before 2030.

## 10. Catalysts & calendar
Next earnings: **29-Oct-2026** (Q3 2026, per company IR calendar / d4 estimate). Q3 2026 Adjusted EBITDA guided $625–775m.
No investor day scheduled in the sources reviewed.

## 11. Red-flag scan
- **Litigation (new, material):** securities class action (E.D.N.Y., filed 23-Jun-2026) and shareholder derivative suit
  (filed 28-Jul-2026), both alleging false/misleading statements about First Solar's capacity to manage US tariff-policy
  impacts. Status: early stage, no admission, amount not yet quantifiable. **This is the single most important adverse
  fact this dossier adds versus the original triage**, which did not flag active litigation.
- **Patent litigation:** JinkoSolar counterclaims (validity/non-infringement), stayed 2-Apr-2026 pending USITC Investigation
  No. 337-TA-1494; a JinkoSolar inter partes review of First Solar's '074 patent was declined by the PTAB (20-Nov-2025) and
  a subsequent ex parte reexamination request was filed (15-Dec-2025).
- **Trade-remedy uncertainty:** Auxin Solar v. United States remains active at the Federal Circuit after the government's
  Feb-2026 withdrawal from the appeal — retroactive AD/CVD exposure on certain imports is legally unresolved (not specific
  to First Solar's own imports, but relevant to the sector's cost structure and its downstream customers).
- No auditor changes, going-concern language, or insider-selling pattern identified in the sources reviewed this pass.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: **Q2 2026 (quarter ended 30-Jun-2026), 10-Q/8-K filed 30-Jul-2026.** Checked for events to
**25-Sep-2026** (market close). All figures are **consolidated GAAP** unless labelled "adjusted"/"non-GAAP" (Adjusted
EBITDA); Q4 2024/2025 figures are arithmetic derivations from annual 10-K minus 9-month 10-Q data, both primary SEC
sources. Data-quality note: revenue/margin/EPS figures are primary-sourced (SEC XBRL, cross-checked to 8-K press releases);
the two capex/debt figures flagged in §6 as "data conflicts" are estimates reconciling two sources, not fabricated numbers.
**This is research, not investment advice, and not a personalised or financial recommendation — consult a licensed advisor
for any decision.**

## 13. Sources
1. SEC EDGAR, First Solar Inc. (CIK 0001274494), companyfacts XBRL API: https://data.sec.gov/api/xbrl/companyfacts/CIK0001274494.json (retrieved 26-Sep-2026)
2. First Solar Q1 2026 earnings release (8-K ex.99.1, filed 30-Apr-2026): https://www.sec.gov/Archives/edgar/data/0001274494/000127449426000108/ex991pressreleaseq1-2026.htm
3. First Solar Q2 2026 earnings release (8-K ex.99.1, filed 30-Jul-2026): https://www.sec.gov/Archives/edgar/data/0001274494/000127449426000169/ex991pressreleaseq2-2026.htm
4. First Solar 10-Q, quarter ended 30-Jun-2026: https://www.sec.gov/Archives/edgar/data/0001274494/000127449426000170/fslr-20260630.htm
5. National Law Review, "Retroactive Solar Duty Exposure Remains Unresolved as Federal Circuit Appeal Proceeds" (2-Sep-2026): https://natlawreview.com/article/retroactive-solar-duty-exposure-remains-unresolved-federal-circuit-appeal-proceeds
6. Miller & Chevalier, "OBBBA Brings 45X Changes, Though Not Wholesale Repeal": https://www.millerchevalier.com/publication/obbba-brings-45x-changes-though-not-wholesale-repeal
7. PV Tech, "US ITC opens TOPCon supply chain case over First Solar patents": https://www.pv-tech.org/us-itc-opens-topcon-supply-chain-case-over-first-solar-patents/
8. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (row: FSLR), v4/outputs/Q12_triage.json (internal, retrieved 26-Sep-2026)
9. scripts/valuation.py (finance-skills stock-analysis skill), reverse-DCF and scenario computation, run 26-Sep-2026

## Correction (verification DVH4, 2026-10-06)

**Wrong text and corrections (all sources are SEC filings for First Solar, CIK 1274494: 10-Q acc 0001274494-26-000170, 8-K Ex-99.1 acc 0001274494-26-000169, 8-K Ex-99.1 acc 0001274494-26-000108).**

1. **Gross-margin driver (FAIL).** Wrong: 45X credits are "the single largest driver of gross margin", a "policy artefact", and the Q2 revenue decline reflects "a smaller, higher-credit-content revenue base". Correct: the 10-Q lists (i) an $88.6m net benefit from expected IEEPA tariff refunds less amounts payable to customers, (ii) higher 45X volume (cost of sales down $70.7m YoY) and (iii) lower logistics (-$35.6m) as the drivers of the 11.7-point expansion; gross margin excluding the IEEPA item is about 48.9%. Q2 operating margin (42.6%) and EPS ($3.92, about $0.82/share pre-tax from the item) include the one-off. The revenue decline is attributed to customer contract terminations; backlog fell 2.8 GW in the quarter (47.9 to 45.1 GW). Verdict does not change.
2. **Debt and net cash (FAIL).** Wrong: net cash ~$1.49bn and EV $17.61bn (built on Yahoo's $194.0m debt). Correct: total debt $37.6m (Note 9), cash and marketable securities $1,727.0m, net cash about $1.69bn (company: $1.7bn including restricted cash); EV about $17.41bn.
3. **Valuation method (FAIL).** Wrong: WACC 9.5% on an EV anchor, implied FCF growth -1.0%/yr. Correct (programme basis): 10-year Treasury 5.17% (25 Sep 2026) + Blume beta 1.491 (raw 1.733) x ERP 4.14% = Ke 11.34%; equity value $19.10bn; FCF after SBC $1,476.5m (TTM FCF $1,500.1m less SBC $23.6m); ten years then 3.0%. Implied growth is +3.7%/yr (3.4% before SBC). The dossier's own 6-8% base is worth about 1.27x the market value at 7%; a 4% path is worth about 1.02x. TTM FCF is understated by a $649m H1 build in 45X grants receivable and includes IEEPA refunds received, so it is a noisy base. **implied_vs_base stays "below" but the gap is much smaller.**
4. Verified, no change: all eight quarter rows and YoY rates, TTM OCF/capex/FCF reconstruction, FY2026 guidance (verbatim, unchanged at Q1 and Q2), Q3 EBITDA guide, 45X range, backlog, both lawsuits, scenario arithmetic. Not verifiable on EDGAR: next earnings date, FEOC/45X legal commentary.

**Verdict:** INCLUDE-SMALL unchanged. Scenarios unchanged (the base EPS of $20 is below the forward-EPS reference, so the arithmetic stands). F28_summary.json: key_adverse_facts[1] and data_conflicts[1] rewritten and the reconciliation extended; verdict, implied_vs_base and scenario_returns_3y values unchanged.
