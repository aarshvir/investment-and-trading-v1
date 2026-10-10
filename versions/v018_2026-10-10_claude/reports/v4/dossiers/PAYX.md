# PAYX (Paychex, Inc.) — Diligence Dossier

Agent: F37 · Standard depth · Prepared 2026-09-26 · Prices/market data as of 2026-09-25 close ($101.37; mkt cap ≈$36.09B)

**Data quality note:** all figures are consolidated (Paychex has no separately-reported standalone entity),
in US dollars ($ = USD; m/mn = millions, bn = billions unless a per-share $ figure), sourced primarily from SEC
EDGAR XBRL and company earnings releases as cited in Section 13; GAAP vs. non-GAAP/adjusted figures are labelled
throughout; approximated (derived) figures are flagged where used.

## 1. Verdict

**INCLUDE-SMALL** — 24–36 month horizon. High-quality, high-margin payroll/HR/PEO franchise, recently
enlarged by the $4.1bn Paycor acquisition, trading at a valuation that prices in almost no growth (reverse DCF:
~0.7%/yr FCF growth for 10 years vs. management's own guided 7–9% adjusted EPS growth). Held at half weight
because the core Management Solutions segment (≈75% of revenue) has decelerated and, on the company's own Q1
FY27 commentary, needs to reaccelerate to hit even the low end of FY27 guidance — a real, named reservation, not
a strawman. No V1 systematic valuation row exists for PAYX (`v1_valuation_table.csv`), so `v1_verdict` is null;
the valuation view below is the analyst's own (Section 7).

## 2. Business in plain English

Paychex sells payroll processing, tax filing, HR administration, benefits and retirement-plan services to
~745,000 clients (after the 2025 Paycor acquisition added ~2,900 HCM clients and ~57,000 payroll clients),
mostly small and mid-sized US employers. It earns per-client/per-transaction fees (Management Solutions, ~75%
of revenue) plus PEO/co-employment and insurance brokerage fees (PEO & Insurance Solutions, ~24%), and a
secondary, rate-sensitive stream from short-term investment of client payroll funds held briefly before
remittance. The moat is switching costs (payroll/tax compliance is high-stakes, low-visibility infrastructure)
and compliance scale (all-50-state tax tables, PEO co-employment risk pooling).

**Sector routing note:** GICS labels PAYX "Human Resource & Employment Services" → the stock-analysis skill
router maps this to `people-businesses.md`. That fits Management Solutions' payroll-service economics, but PEO
is closer to an insurance/risk-pooling business and client-funds float income is bank-like; both are read
separately below rather than blended into a single people-business ratio set.

## 3. Why the model likes it / durability

`data/b1_live_scores.csv`: live_rank 95, composite 0.810 (decile 9 of 10) — driven mainly by Quality (fam_Q
0.852: gp/assets 0.314, ROE 48.7%, OCF/assets 14.4%, low accruals) and strong earnings momentum (fam_S 0.539,
SUE 0.855 — recent EPS surprises have been positive). Value and Momentum are unremarkable (fam_V 0.688, fam_M
0.420) — this reads as a quality/earnings-momentum name, not a re-rating story. Durable, not an artefact: the
28%+ operating margin and ~47% ROE predate Paycor by a decade, and Paycor integration is running *ahead* of
plan (expense synergies raised from an original $80–90m target to ~$100m; revenue synergies at the high end of
a 30–50bp contribution), so the quality read is not propped up by a fresh, unproven deal.

## 4. Last two years of results (fiscal quarters, FYE 31-May; GAAP unless marked)

| Qtr (end) | Revenue | Op. margin | GAAP diluted EPS | Adj. diluted EPS |
|---|---|---|---|---|
| Q2 FY25 (Nov-24) | $1,316.9M | 40.9% | $1.14 | — |
| Q3 FY25 (Feb-25) | $1,509.0M | 45.8% | $1.43 | — |
| Q4 FY25 (May-25) | $1,427.3M | 30.2% | ~$0.83 (derived) | — |
| Q1 FY26 (Aug-25) | $1,540.0M | 35.2% | $1.06 | — |
| Q2 FY26 (Nov-25) | $1,557.6M | 36.7% | $1.10 | — |
| Q3 FY26 (Feb-26) | $1,808.9M | 43.8% | $1.56 | — |
| Q4 FY26 (May-26) | $1,605.5M | 37.7% | ~$1.17 (derived) | — |
| **Q1 FY27 (Aug-26)** | **$1,630.5M (+5.9% YoY)** | **38.0%** | **$1.21 (+14.2%)** | **$1.34 (+10%)** |

FY26 total: revenue $6,512M (+17%; ~12pp from the Paycor consolidation, ~5% organic); GAAP diluted EPS $4.89
(+7%); adjusted diluted EPS $5.51 (+11%, above the initial 8.5–10.5% guided range); adjusted operating margin
43.2% (vs. 42.5% FY25). Q4/Q1-derived EPS figures use FY-total minus reported Q1–Q3 (a standard, disclosed
approximation since Paychex does not separately tag discrete Q4 EPS in XBRL). TTM (Nov-25–Aug-26) net income
$1,805.9M ties to Yahoo's trailing net income to the dollar — a clean cross-check that the derived series is
right. Q1 FY27's GAAP-vs-adjusted gap ($1.21 vs $1.34) is mainly Paycor integration and acquisition-related
amortization, disclosed as such — not a red flag on its own, but must never be quoted as one figure.

Sources: SEC EDGAR XBRL companyfacts (CIK 0000723531); Paychex Q1 FY2027 earnings release/call (24-Sep-2026);
Q4/FY2026 earnings release (24-Jun-2026, globenewswire).

## 5. Guidance track record (last 4 releases)

| Release | Total revenue growth | Mgmt Solutions | PEO & Insurance | Adj. diluted EPS growth | vs prior guide |
|---|---|---|---|---|---|
| FY26 initial (24-Jun-25) | 16.5–18.5% | 20–22% | 6–8% | 8.5–10.5% | New guide (Paycor consolidation) |
| **FY26 actual (24-Jun-26)** | **delivered 17%** | — | — | **delivered 11%** | **Beat** the top of the EPS range |
| FY27 initial (24-Jun-26) | 5–6% | 5–6% | 6–7% | 7–9% | New-year guide |
| FY27 Q1 update (24-Sep-26) | maintained 5–6% | *not reaffirmed explicitly* | **raised to 7–8%** | not reiterated numerically | **Raised** (PEO segment only) | **[Corrected 2026-10-08: the Q1 release (8-K 0000723531-26-000004, 23-Sep-2026) explicitly marks Management Solutions 5-6% 'No change', adjusted EPS growth 7-9% 'No change' and adjusted operating margin ~44% 'No change', and also raised interest on funds held for clients to $200-210M]**

Never cut across these four data points, and FY26 EPS growth beat even the top of the initial range. The Q1
FY27 update is a genuine mixed signal, not a clean raise, however: **[Corrected 2026-10-08: Management Solutions and EPS guidance were reaffirmed, not omitted; the concern that Management Solutions grew 4% in Q1 against a 5-6% full-year guide stands]** PEO strength (worksite-employee growth,
record retention, ASO-to-PEO conversions) was the only segment explicitly raised, while Management Solutions —
75% of revenue — was flagged by sell-side (Stifel, 24-Sep-26 note, Hold, PT cut to $112 from $130) as requiring
"more than 100bp" of second-half acceleration in both Management Solutions and PEO to hit the full-year revenue
midpoint. The stock fell ~9% on the Q1 FY27 print. This is the single most important adverse fact in this
dossier and the reason for INCLUDE-SMALL rather than INCLUDE.

## 6. Earnings quality & balance sheet

- **FCF conversion:** derived quarterly OCF-minus-capex (SEC XBRL, cross-checked against Yahoo's TTM FCF of
  $1,887.1M — the two differ ~7%, likely definitional; disclosed rather than silently picking one). TTM
  (Nov-25–Aug-26) FCF ≈$2,016.7M vs TTM net income $1,805.9M → **FCF/NI ≈112%** — strong cash conversion typical
  of a negative-working-capital services model.
- **Dividend & payout:** $4.76/share annualized declared, yield 4.7%; **payout ratio ≈90% of GAAP EPS** **[Corrected 2026-10-08: on TTM GAAP EPS of $5.04 the payout is about 94%]** (Yahoo:
  0.9008) — high, and it limits capital-return flexibility if EPS growth disappoints; FY26 buybacks were still
  $611.0M, so the company is running both a near-full payout and a buyback program simultaneously.
- **Leverage:** Paycor was funded with ~$4.2bn of new fixed-rate corporate bonds (closed with the deal,
  14-Apr-2025, $4.1bn total consideration). As of 31-Aug-2026: long-term debt $4,558.0M, cash $600.9M → net debt
  $3,957.1M vs TTM EBITDA ~$3,078.0M → **net debt/EBITDA ≈1.29x** — manageable, not stretched.
- **Goodwill:** $4,534.1M (Aug-26), essentially all Paycor-related — a large intangible balance that would be
  the first thing tested for impairment if the Management Solutions deceleration proves structural.

## 7. Valuation snapshot and reverse DCF

No V1 row exists for PAYX; `v1_verdict = null`. Analyst-derived reverse DCF
(`stock-analysis/scripts/valuation.py`, 10-year fade to 4% terminal growth):

- EV bridge: market cap $36,085.7M + debt $4,558.0M − cash $600.9M = **EV ≈$40,042.8M** (Yahoo EV $39,852.7M,
  consistent)
- WACC 8.0% (low-beta, 0.808, stable-cash-flow name)
- Base FCF (TTM, primary-sourced): $2,016.7M
- **Implied 10-year FCF growth priced in: ~0.7%/yr** **[Corrected 2026-10-08: restated on the programme basis (equity basis, FCF after SBC $1,928M, Ke 8.5-9.3% = 5.17% + beta x 4.14%, 3.0% terminal): 3.0% to 4.8%, still below a total-FCF base of about 5-6%, but a far smaller margin than 0.7% implies]**, fading to 4% terminal — i.e. the market is pricing in
  essentially *no* growth beyond inflation.

Trailing P/E 20.1x is below PAYX's own 10-year historical range (~24–34x per a prior-run cross-check in this
program's v005 reconciliation — noted as a data point, not re-verified independently here), FCF yield 5.6%,
dividend yield 4.7%. That is *well below* even a conservative base case (mid-single-digit organic revenue
growth + operating leverage + buybacks ≈ high-single-digit FCF/EPS growth, well short of what would be needed
to call this "priced for perfection"). **valuation_view_vs_v1.implied_vs_base = "below"** — satisfies the
INCLUDE-SMALL/INCLUDE growth-priced-in test with a wide margin.

Scenario table (analyst-constructed; 3-year forward EPS × exit P/E, annualized incl. ~4.7% average dividend
yield): **Bear** EPS $4.90 @ 15x → **-5.5%/yr**; **Base** EPS $6.20 @ 19x → **+9.8%/yr**; **Bull** EPS $7.00 @
23x → **+21.5%/yr**.

**scenario_returns_3y (annualised, price + dividends): bear -5.5%/yr, base +9.8%/yr, bull +21.4%/yr.**

## 8. Bull case / bear case

**Bull (3):**
1. Reverse DCF shows the market pricing almost no growth into a business still guiding mid-single-digit revenue
   growth and high-single-digit adjusted EPS growth — a real margin of safety if Management Solutions merely
   stabilizes rather than reaccelerates.
2. Paycor integration is ahead of plan on cost synergies ($100m vs. an original $80–90m target) with revenue
   synergies still building — a multi-year tailwind not yet fully reflected in trailing numbers.
3. PEO & Insurance Solutions (record retention, accelerating ASO-to-PEO conversions) is growing well above the
   company average and was the only segment raised at Q1 FY27.

**Bear (3):**
1. Management Solutions (75% of revenue) has decelerated to the point that management's own FY27 guidance
   requires >100bp of second-half reacceleration in both major segments — this is a company-specific, evidenced
   concern, not macro noise, and the stock already sold off ~9% on it.
2. A ~90% GAAP-EPS dividend payout ratio leaves little room to keep raising the dividend if EPS growth
   disappoints, without either cutting buybacks or letting payout run above 100%.
3. An April-2026 data breach (workers' names and SSNs exposed; company reportedly waited ~a month to begin
   notifications) drew a negligence class action (W.D.N.Y., filed 11-Jul-2026) — a real, if likely containable,
   litigation and reputational risk for a company whose entire business is trusted handling of payroll/PII data.

## 9. Key risks & kill criteria (measurable)

1. Management Solutions organic (ex-Paycor) revenue growth stays below 4% for two consecutive quarters (vs. the
   >100bp H2 FY27 acceleration management's own guidance requires).
2. FY27 adjusted diluted EPS growth finishes below the guided 7–9% range at year-end (24-Jun-2027 release).
3. Net debt/EBITDA rises above 2.0x (currently ≈1.29x) without a clear deleveraging path.
4. The 2026 data-breach litigation, or a further cybersecurity incident, results in a material fine/judgment or
   documented client attrition.
5. Dividend payout ratio is forced above 100% of GAAP EPS for two consecutive quarters (currently ≈90%).

## 10. Catalysts & calendar

- Next earnings: **Q2 FY27, ~18-Dec-2026** (Yahoo calendar estimate; not yet formally confirmed by Paychex).
- FY27 guidance in force: total revenue +5–6%, Management Solutions +5–6%, PEO & Insurance +7–8% (raised
  24-Sep-26), adjusted operating margin ~44%, adjusted diluted EPS +7–9%.

## 11. Red-flag scan

- **Litigation:** Data-breach negligence class action (W.D.N.Y., filed 11-Jul-2026) following an April-2026
  breach exposing employee names/SSNs — open, not yet resolved or quantified in filings reviewed.
- No auditor changes, restatements, or going-concern language found in this review.
- No SEC investigation found in the sources checked (only routine "pending/future litigation" risk-factor
  boilerplate in the 10-K/10-Q).
- No pending M&A affecting Paychex itself (Paycor already closed 14-Apr-2025).
- Insider Form-4 pattern and detailed related-party review not exhaustively completed given the time-box;
  flagged as a limitation, not a finding.

## 12. Data basis, recency and disclaimer

Most recent period incorporated: **Q1 FY2027 10-Q (quarter ended 31-Aug-2026), filed 24-Sep-2026**, plus the
FY2026 10-K (filed 17-Jul-2026) and the Q1 FY27 earnings release/call (24-Sep-2026). Checked for events to
2026-09-25. GAAP figures are labelled GAAP; "adjusted"/non-GAAP figures are management's own measures as
disclosed in earnings releases, not independently reconciled line-by-line in this pass. Q4 FY25/FY26 EPS are
disclosed approximations (FY total minus reported Q1–Q3, since Paychex does not separately XBRL-tag discrete Q4
EPS) — flagged, not hidden. **This is research, not personalized investment advice; consult a licensed financial advisor before acting on it.**

## 13. Sources

1. SEC EDGAR submissions/companyfacts, CIK 0000723531 (data.sec.gov), retrieved 2026-09-26.
2. Paychex FY2026 10-K, filed 2026-07-17: sec.gov/Archives/edgar/data/723531/000119312526307785/payx-20260531.htm
3. Paychex Q1 FY2027 10-Q, filed 2026-09-24: sec.gov/Archives/edgar/data/0000723531/000072353126000006/payx-20260831.htm
4. Paychex Reports Fourth Quarter and Full-Year 2026 Results (24-Jun-2026): globenewswire.com/news-release/2026/06/24/3316844
5. Paychex Q1 FY2027 earnings call transcripts (24-Sep-2026): Motley Fool, Benzinga, Seeking Alpha (cross-checked, not sole source).
6. Paychex FY2025 Q4/FY guidance release (25-Jun-2025): sec.gov/Archives/edgar/data/723531/000095017025089743/payx-ex99_1.htm
7. Stifel PAYX note (24-Sep-2026), reported via Investing.com: "Stifel cuts Paychex stock price target to $112 on growth concerns."
8. HR Dive, "Paychex sued for negligence after data breach exposes workers' names and Social Security numbers" (2026).
9. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (quant context, retrieved this session).
10. finance-skills stock-analysis skill (`references/sectors/people-businesses.md`) and `scripts/valuation.py`.

## Correction (verification DV32, 2026-10-08)
**Wrong text and corrections (sources: 8-K Ex-99.1 0000723531-26-000004 (Q1 FY27, dated 23-Sep-2026) and 0001193125-26-280314 (Q4 FY26), 10-Q 0000723531-26-000006, 10-K 0001193125-26-307785):**
1. Section 5 guidance table and prose: the Q1 FY27 release's Fiscal Year 2027 Outlook table shows total revenue 5-6% "No change", Management Solutions 5-6% "No change", PEO and Insurance 7-8% (previously 6-7%), interest on funds held for clients $200-210M (previously $195-205M), adjusted operating margin ~44% "No change", adjusted diluted EPS growth 7-9% "No change". The dossier says Management Solutions was "not reaffirmed explicitly" and EPS growth "not reiterated numerically"; both were reaffirmed, so the update was a small clean raise rather than a "mixed signal". The Management Solutions concern (Q1 revenue +4% against a 5-6% full-year guide) is genuine. The release is dated 23-Sep-2026 (the 10-Q is 24-Sep).
2. Section 6: payout is about 94% of TTM GAAP EPS ($5.04), not 90%.
3. Section 7 valuation method: the 0.7% reproduces (EV $40.0bn, WACC 8.0%, 4.0% terminal growth) but the terminal growth is within 1.2 points of the 5.17% Treasury, levered FCF (after interest) is set against an EV, and SBC ($89M TTM) is not deducted. Restated (equity basis, market cap $36.09bn, FCF after SBC $1,928M, Ke 8.5% at the stated beta 0.808, 8.9% at a Blume beta of 0.89, 9.3% at beta 1.0, ten years then 3.0%): implied 10-year FCF growth 3.0%, 3.8% and 4.8%. The dossier's base ("high-single-digit FCF/EPS growth") includes buyback accretion; in total FCF the base is about 5-6%, so the price is below the base but not by a wide margin.
Checked and correct: every cell of the section 4 table, FY26 revenue $6,512M (+17%), GAAP EPS $4.89, adjusted $5.51, TTM net income $1,805.9M and TTM FCF $2,016.7M, debt $4,558.0M, cash $600.9M (marketable securities of $333.3M are not netted).

**Verdict:** INCLUDE-SMALL unchanged; implied_vs_base = below unchanged but narrower. F37_summary.json PAYX valuation_view_vs_v1.reconciliation and key_adverse_facts (guidance wording) updated.
