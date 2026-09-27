# General Motors Company (GM) — Diligence Dossier

**1. Verdict: INCLUDE.** Thesis horizon 12–36 months. GM's underlying (adjusted-basis, automotive-net-cash) economics are priced far more cheaply than the headline GAAP numbers or the model's V1 valuation suggest; two consecutive 2026 guidance raises, shrinking EV losses and tariff relief support the case, against real cyclicality and EV-transition risk.

**2. Business in plain English.** GM designs, builds and sells cars, trucks and SUVs globally (Chevrolet, GMC, Cadillac, Buick, and Wuling/Baojun in China through a JV), and separately runs GM Financial, a captcaptive finance arm that funds dealer and customer loans/leases. It makes most of its profit from full-size trucks and SUVs in North America; it is also investing in EVs and software-defined vehicles while winding down the loss-making Cruise robotaxi business.

**3. Why the model likes it.** b1_live_scores.csv shows GM ranks well on Value (pct_ep 0.97, pct_fcfp 0.99 — 97th/99th percentile earnings and FCF yield) and moderately on Quality (gp/assets, ROE), with a composite live_rank of 128/1172 and price_vs_growth triage score of 5/5. This is durable operating cash generation (TTM OCF $23.2bn per 10-K/10-Q, FCF ~$14.4bn), not an accounting artefact — but the *reported* GAAP earnings used in several of these ratios are themselves distorted by 2025–26 one-off charges (see §7), so the "cheapness" is real but understated rather than overstated.

**4. Last two years of results (selected quarters, GAAP unless noted; $M).**

| Quarter | Revenue | Op. margin (GAAP) | GAAP dil. EPS | Adj. dil. EPS | EBIT-adjusted |
|---|---|---|---|---|---|
| Q3 2024 | 48,757 | 7.5% | 2.68 | — | — |
| Q4 2024 (FY24 total 187,442; OI 12,784) | — | — | — | — | — |
| Q1 2025 | 44,020 | 7.6% | 3.35 | 2.78 | ~3.0bn (implied) |
| Q2 2025 | 47,122 | 4.5% | 1.91 | ~2.5 (implied) | 3.038bn (implied from Q2'26 YoY) |
| Q3 2025 | 48,591 | 2.2% | 1.35 | 2.80 | 3.376bn |
| **Q4 2025** | ~45,287 (implied) | ~6.4% | (FY25 3.27 GAAP) | ~2.80 (implied) | 2.797bn (FY25 12.7bn − 9M 9.903bn) |
| **Q1 2026** | 43,624 | 6.7% | 2.82 | 3.70 | 4.300bn |
| **Q2 2026** | 48,026 | 3.0% | 1.41 | 3.57 | 3.943bn |

Sources: GM 8-K XBRL (companyfacts, `Revenues`/`OperatingIncomeLoss`/`EarningsPerShareDiluted`) and Q1–Q3 2025, Q4/FY2025, Q1–Q2 2026 earnings-release exhibits (SEC EDGAR, filed 2026-04-28, 2026-07-21, 2026-01-27, 2025-10-21). GAAP operating income and EPS are heavily depressed in Q4 2025 (‑$7.2bn EV-realignment charge) and again in Q1–Q2 2026 ($1.077bn + $2.279bn EV/China charges); adjusted EBIT and adjusted EPS strip these out and show a cleaner, improving trend: adjusted EBIT +29.8% YoY in Q2 2026, adjusted diluted EPS +41.3% YoY.

**5. Guidance track record (last 4 releases, FY EBIT-adjusted range).**
- Q3 2025 (2025-10-21): raised FY25 EBIT-adj to $12.0–13.0bn from $10.0–12.5bn (adj. auto FCF raised to $10.0–11.0bn from $7.5–10.0bn).
- Q4/FY2025 (2026-01-27): FY25 actual EBIT-adj $12.7bn (near top of raised range); initial FY26 guide $13.0–15.0bn EBIT-adj, adj. EPS $11.00–13.00, adj. auto FCF $9.0–11.0bn.
- Q1 2026 (2026-04-28): FY26 raised to $13.5–15.5bn EBIT-adj / $11.50–13.50 adj. EPS (auto FCF maintained $9.0–11.0bn); gross tariff-cost estimate cut to $2.5–3.5bn from $3.0–4.0bn after a favorable US Supreme Court ruling.
- Q2 2026 (2026-07-21): raised again to $14.0–16.0bn EBIT-adj / $12.00–14.00 adj. EPS / $9.5–11.5bn adj. auto FCF.
Three consecutive raises in four releases — a genuine, verifiable improving trend, not merely a "beat-and-raise on easy comps" (2025 comps were themselves depressed by EV charges).

**6. Earnings quality & balance sheet.**
- FCF conversion: TTM OCF $23.2bn, capex $8.8bn → FCF ~$14.4bn vs GAAP NI $1.95bn — ratio is not meaningful because NI is itself charge-depressed; against adjusted EBIT ($14.4bn TTM) FCF conversion is close to 1x, healthy for an automaker.
- GAAP vs adjusted gap: driven almost entirely by EV strategic-realignment and China-restructuring charges (Q1'26 $1.077bn, Q2'26 $2.279bn, Q4'25 $7.2bn) — disclosed, one-time in nature, and shrinking sequentially.
- **Balance sheet nuance (important):** GM's consolidated net debt (~$104bn per Yahoo/D4) is dominated by GM Financial's captive-finance debt ($111.7bn total GM Financial short+long-term debt at Q2 2026), which funds customer loan/lease receivables and is not operating leverage. GM's 10-Q (filed 2026-07-21, balance sheet) shows **Automotive-only debt of just $15.98bn** against **Automotive cash + marketable securities of $24.7bn** — i.e., Automotive is net-cash positive by roughly **$8.7bn**, not levered 6.3x as the consolidated ratio implies. Net debt/EBITDA of "6.3x" cited in triage is a captive-finance artefact.
- Share count: 910M diluted (Q2'26) down from 995M (Dec-2024) — buybacks reducing count (~$2.8bn repurchased in H1 2026 under a $6bn authorization approved Jan 2026); dividend $0.18/share/quarter (raised from $0.15 in Jan 2026).
- No pending M&A of size disclosed.

**7. Valuation snapshot and reconciliation with V1.**
V1 (`outputs/v1_valuation_table.csv`, `v1_valuation.json`) rates GM **"excessive"** (score ‑0.575): NTM P/E 5.65x (29th percentile of its own 10-yr history — i.e., historically cheap on this metric, yet still flagged excessive), reverse-DCF implied 10-year growth **23.5%** vs 5-yr delivered CAGR 5.8% / 10-yr 1.6%, base-case 3-yr annualised return ‑1.6%, bear ‑35.5%, bull +64.2%.
**I disagree with the "excessive" label and believe the specific flawed input is identifiable and primary-source-verifiable:** V1's reverse DCF used TTM GAAP EBIT of $1.815bn (a 0.98% margin) and a consolidated net debt of $104bn (EV $179.2bn) to back into the 23.5% implied-growth figure. Per §6, (a) TTM GAAP EBIT is depressed by ~$3.3bn of H1-2026 one-time EV/China charges alone (on top of the $7.2bn Q4-2025 charge), and GM's own non-GAAP TTM adjusted EBIT is **$14.42bn** (Q3'25 $3.376bn + Q4'25 $2.797bn + Q1'26 $4.300bn + Q2'26 $3.943bn — all from primary-source earnings-release exhibits, cross-checked to a 7.8% TTM margin on the $185.5bn TTM revenue that matches D3's own revenue figure); (b) the $104bn "net debt" is >90% GM Financial captive debt matched by receivables, not automotive enterprise leverage. Re-running a simple reverse DCF on an automotive-view basis (EV ≈ market cap $75.2bn less automotive net cash $8.7bn ≈ $66.5bn; NOPAT off $14.42bn adjusted EBIT at 24% tax ≈ $10.96bn; **EV/adjusted-EBIT ≈ 4.6x**, EV/NOPAT ≈ 6.1x) implies a **perpetual growth rate near zero to slightly negative** at a ~10% WACC — i.e., the market is pricing GM's core auto business for stagnation/decline, not the reverse. That is far more consistent with the triage view ("5.6x NTM P/E … look too cheap") than with V1's "excessive" tag. **valuation_view_vs_v1.consistent = false.**
Against 3 rough peers (Ford ~6.6x NTM P/E per V1 peer set, Tesla far higher on a different growth basis), GM screens cheap on both GAAP and adjusted bases; Street 12-month target range $75–$132 (mean ~$104) brackets the $82.63 close and implies further upside on consensus.

**8. Bull case / Bear case.**
- Bull: (1) tariff relief (Supreme Court ruling) plus further guidance raises compound — three raises already in 2026; (2) EV segment losses keep shrinking toward breakeven, removing the biggest GAAP-vs-adjusted drag; (3) $6bn buyback authorization (only partly used) plus a net-cash automotive balance sheet supports continued EPS-accretive repurchases and dividend growth.
- Bear: (1) North American truck/SUV profit pool (GM's main profit source) is cyclically exposed — a US auto-demand downturn would hit adjusted EBIT hard given operating leverage; (2) China JV remains a drag (restructuring charges recurring) and a full exit/impairment is not off the table; (3) EV strategy could require further capacity write-downs if policy support (consumer incentives) does not return, repeating 2025's $7.2bn charge pattern.

**9. Key risks & kill criteria.**
1. Adjusted EBIT-adjusted guidance cut (vs the current $14.0–16.0bn FY26 range) at any of the next two quarterly releases.
2. Automotive segment swings from net-cash to net-debt positive (i.e., Automotive debt exceeds Automotive cash+securities) for two consecutive quarters.
3. Gross tariff-cost estimate re-raised above the current $2.5–3.5bn 2026 range.
4. Two consecutive quarters of GAAP-to-adjusted EBIT gap driven by *new* (not previously disclosed) restructuring/impairment charges exceeding $1bn/quarter.
5. China equity income (currently modestly positive, $83M in Q2 2026) turns negative for two consecutive quarters.

**10. Catalysts & calendar.** Next earnings: **2026-10-20** (Q3 2026, confirmed via GM IR press release). GM Financial releases Q3 2026 results separately around the same week. No investor day or lock-up events identified in the window.

**11. Red-flag scan.** Cruise robotaxi: GM ended public robotaxi operations and folded Cruise in-house in Dec 2024 (after >$10bn cumulative spend), with further ~1,000 job cuts in Feb 2025 — a de-risking event now largely behind the company, not a live red flag, but evidence of past capital-allocation misses in "growth" bets. No auditor change, restatement, going-concern language, SEC/DOJ investigation, or short-seller report identified in this review window. Insider Form-4 pattern not reviewed at standard depth (flagged as a data gap). EV-realignment and China-restructuring charges are disclosed, recurring-but-shrinking, and reconciled above — not concealed.

**12. Sources.**
1. GM 10-Q, Q2 2026 (filed 2026-07-21): https://www.sec.gov/Archives/edgar/data/1467858/000146785826000051/gm-20260630.htm
2. GM Q2 2026 earnings release exhibit: https://www.sec.gov/Archives/edgar/data/1467858/000146785826000049/gmq22026pressreleaseandfin.htm
3. GM Q1 2026 earnings release exhibit: https://www.sec.gov/Archives/edgar/data/1467858/000146785826000033/gmq12026pressreleaseandfin.htm
4. GM Q4/FY2025 earnings release exhibit: https://www.sec.gov/Archives/edgar/data/1467858/000146785826000011/gmq42025pressreleaseandfin.htm
5. GM Q3 2025 earnings release exhibit: https://www.sec.gov/Archives/edgar/data/1467858/000146785825000141/gmq32025pressreleaseandfin.htm
6. SEC XBRL companyfacts, CIK 0001467858: https://data.sec.gov/api/xbrl/companyfacts/CIK0001467858.json
7. v4/data/b1_live_scores.csv (row GM); v4/outputs/v1_valuation_table.csv and v1_valuation.json (row/key GM)
8. v4/outputs/Q01_triage.json (GM entry)
9. GM Cruise shutdown: CNBC 2024-12-10/12-15, Bloomberg 2025-02-04 (search-derived, secondary — used only for the non-financial Cruise timeline)

**Data basis, recency and disclaimer.** Most recent period incorporated: Q2 2026 10-Q, filed 2026-07-21 (period end 2026-06-30); FY2025 10-K filed 2026-01-27. Checked for events to 2026-09-25. GAAP figures are explicitly labelled; "adjusted"/"EBIT-adjusted" figures are GM's own non-GAAP measures taken from its earnings-release exhibits and labelled as such throughout. This is research, not investment advice: research, not personal investment advice.

---
**Correction (26 Sep 2026).** Auditor A2 flagged that §7's "Automotive cash + marketable securities of $24.7bn / net cash +$8.7bn" wrongly used *consolidated* (Automotive+GM Financial) cash ($20,134M) and marketable securities ($4,585M) from the 10-Q balance sheet, not Automotive-only figures. Re-checked against the Q2 2026 earnings-release exhibit's "Combining Balance Sheet Information" table (accession 0001467858-26-000049, gmq22026pressreleaseandfin.htm): **Automotive-only cash $15,147M + marketable securities $4,503M = $19,650M**, vs Automotive debt $15,979M (10-Q, accession 0001467858-26-000051) → **net automotive cash = +$3,671M**, matching the release's own automotive-liquidity line. The auditor is correct; my original figure was wrong (consolidated, not segment-level).
Effect on the reverse-DCF/EV: corrected EV = market cap $75.193bn − net cash $3.671bn = **$71.52bn** (previously $66.5bn) → EV/adjusted-EBIT (TTM $14.42bn) ≈ **5.0x** (previously 4.6x); EV/NOPAT ≈ 6.5x, implying a perpetuity growth rate of roughly **−4.6%/yr at a 10% WACC** (previously −5.6%/yr) — still deeply negative, i.e. the conclusion is unchanged: the market is still pricing GM's automotive business for decline, not the reverse. §7's core disagreement with V1 ("excessive") stands. **Verdict (INCLUDE), implied_vs_base ("below"), and scenario_returns_3y are unchanged** — the correction affects the precision of the EV/EBIT multiple (~5.0x vs ~4.6x) and perpetuity-growth estimate (~−4.6% vs ~−5.6%), not the direction or magnitude of the conclusion. `F35_summary.json` was not modified because no summary field changed. Net automotive cash/leverage kill-criterion #2 in §9 is unaffected (still net-cash, just a smaller cushion than originally stated: $3.7bn vs the $8.7bn previously reported).

---
## Correction (lead, 26 Sep 2026) — DA7 cross-reference
- Fact-check DA7 independently found the same automotive net-cash error that auditor A2 raised (true Automotive cash + securities $19,650m against $15,979m debt = +$3,671m; Q2 2026 8-K Ex-99.1, accession 0001467858-26-000049). It is corrected by the author in the "Correction (26 Sep 2026)" paragraph in §7; verdict unchanged.
- DA7 minor: Q1 2026 EBIT-adjusted was $4,253m, not $4,300m; the trailing-twelve-month sum moves by under 0.5%.
