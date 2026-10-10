# Equinix, Inc. (EQIX) — Diligence Dossier (F32, standard depth)

## 1. Verdict
**INCLUDE-SMALL** (half weight). Thesis horizon 24–36 months. One-sentence reason: the dominant interconnection-density data-center REIT is compounding AFFO/share faster than the price implies, but a capex program that is about to roughly double annual spend (funded partly by more debt/equity issuance) and a residual, if now-resolved, accounting-scrutiny history argue for a starter position rather than full weight.

**Thesis (≤25 words):** The world's most interconnected data-center network, benefiting from AI/hyperscaler demand, growing AFFO faster than its rich-looking headline P/E suggests.

## 2. Business in plain English
Equinix owns and operates 270+ carrier-neutral data centers (International Business Exchanges, "IBX") where enterprises, cloud providers (hyperscalers) and network carriers colocate equipment and interconnect directly with each other. It earns recurring rent for cabinet/space ("colocation") plus per-connection interconnection fees — the interconnection business is the moat, since the value of being in an Equinix facility rises with the number of other networks already there (a network effect that is very hard for a new entrant to replicate). It also earns development fees and equity income from xScale, a joint-venture vehicle built specifically to fund hyperscale (large single-tenant) capacity without putting all of that capex on Equinix's own balance sheet.

## 3. Why the model likes it / durability
Triage (Q13_triage.json) scored EQIX quality 5, growth 4, price_vs_growth 4, flagging net debt/EBITDA of "4.9x amid a $4–5bn/year capex plan to double capacity through 2029" as the key diligence item, and noting the required growth under a simple FCF-yield heuristic (~5.2%) is "well below Equinix's actual mid-teens-to-20% growth trajectory." The pre-registered quant composite agrees and ranks it strongly: decile 8, live_rank 106 of 503, composite 0.79 (b1_live_scores.csv). Quality percentiles are genuinely high (ROE pct 0.71, OCF/assets pct 0.81) and reflect a durable, structurally growing business (AI/hyperscaler demand for interconnected capacity, not a one-off). **One caveat on the "value" family score:** EQIX's book/price percentile is very high (0.95, i.e. screens "cheap" on book value) — this is a REIT-accounting artefact (real estate carried at depreciated historical cost, not fair value) rather than genuine cheapness, and should not be read as the stock being statistically undervalued on that basis; the momentum score (pct 0.71) and the AFFO-based valuation work in §7 are the more trustworthy reads.

## 4. Last two years of results (GAAP; source: SEC XBRL companyfacts CIK0001101239, cross-checked to 8-K press releases)
| Quarter | Revenue ($M) | YoY | GAAP diluted EPS | GAAP net income ($M) | Diluted AFFO/share |
|---|---|---|---|---|---|
| Q3'23 | 2,061 | — | 2.93 | 276 | n/a |
| Q1'24 | 2,127 | — | 2.43 | 231 | n/a |
| Q2'24 | 2,159 | — | 3.16 | 301 | n/a |
| Q3'24 | 2,201 | +6.8% | 3.10 | 297 | n/a |
| Q1'25 | 2,225 | +4.6% | 3.50 | 343 | n/a |
| Q2'25 | 2,256 | +4.5% | 3.75 | 368 | $9.91 |
| Q3'25 | 2,316 | +5.2% | 3.81 | 374 | $9.83 |
| Q1'26 | 2,444 | +9.9% | 4.20 | 415 | n/a |
| **Q2'26** | **2,625** | **+16.4%** | **4.83** | **479** | **$11.78 (+19% YoY)** |
Revenue growth clearly accelerated through 2026 (from mid-single-digit in 2024–25 to double-digit in 2026), driven by record bookings and AI-infrastructure demand. Recurring revenue was $2.377bn of Q2'26's $2.625bn (11% YoY growth); FFO/share (diluted) was $8.61 in Q2'26 vs $7.03 in Q2'25. GAAP EPS growth (29% YoY in Q2'26) and AFFO/share growth (19% YoY) both accelerated together — this is not a case of GAAP/adjusted divergence distorting the picture.

## 5. Guidance track record (last four releases; FY revenue and AFFO)
| Release | New FY range | Prior range | Verdict |
|---|---|---|---|
| Q3'25 (2025-10-29, 8-K ex-99.1) | FY2025 revenue $9.208–$9.328bn; AFFO/share $37.95–$38.77 | Revenue $9.233–$9.333bn; AFFO/share $37.67–$38.48 | **Raised** (AFFO +$0.32/sh underlying, revenue flat/FX-offset) |
| Q4/FY'25 (~Feb 2026, 8-K) | FY2025 actual AFFO/share ~$38.5 (per range, actual not independently re-pulled); initial FY2026 guide: revenue $10.123–$10.223bn, AFFO/share $41.93–$42.74 | n/a (first FY2026 guide) | Initiated |
| Q1'26 (2026-04-29, 8-K ex-99.1) | FY2026 revenue $10.144–$10.244bn; AFFO $4.198–$4.278bn | $10.123–$10.223bn; AFFO $4.158–$4.238bn | **Raised** |
| Q2'26 (2026-07-29, 8-K ex-99.1) | FY2026 revenue $10.205–$10.285bn; AFFO/share $42.69–$43.29 | $10.144–$10.244bn; AFFO $4.198–$4.278bn | **Raised** — management called it "the largest single guidance raise in the history of our company" |
Long-term guidance was also raised at Q2'26: 2027–2029 annual revenue growth to 10–13% (from 7–10%) and AFFO/share growth to 9–12% (from 5–9%) — a structural upgrade to the multi-year algorithm, not just an in-quarter beat. Four consecutive releases, all raises, no cuts. **[Corrected 2026-10-08: three raises (Q3'25, Q1'26, Q2'26) plus one initiation (Q4/FY'25); no cuts]**

## 6. Earnings quality & balance sheet
AFFO is the correct cash-flow lens here (GAAP FCF is structurally negative — 1H'26 free cash flow was **−$560m**, adjusted FCF −$336m — because "free cash flow" as reported nets ~$2.9bn of 1H'26 non-recurring/development capex against $1.78bn of operating cash flow; this is normal for a REIT in a heavy build-out phase and is why AFFO, which separates recurring maintenance capex [~1.6% of revenue] **[Corrected 2026-10-08: recurring capex is guided at ~3% of revenue ($290-310m)]** from growth capex, is the metric management, analysts and this dossier all use). **Key balance-sheet fact validating the triage's own flag:** full-year 2026 total capex guidance is now $5.0–$6.0bn, roughly double the prior ~$3.8bn non-recurring-capex run-rate, and the long-term 2027–2029 capex range was raised to $5.0–$7.0bn/year. Total debt principal was $22.15bn at Q2'26 (senior notes $19.69bn) vs $21.42bn at YE'25, funding this build-out; cash was only $979m. Using Q2'26-guided adjusted EBITDA ($5.21–$5.27bn annualized) and net debt (~$21.2bn), **net debt/EBITDA ≈4.0x** by this dossier's method — lower than triage's cited 4.9x, likely because triage used a trailing (rather than forward-guided) EBITDA base or a gross-debt denominator; both readings agree leverage is moderate-to-elevated for a REIT and will need continued external funding (debt and/or equity) to sustain the capacity-doubling plan, which is dilution risk to per-share AFFO growth if funded disproportionately with equity. Dividend ~$2.04bn expected FY2026 (dividend yield ~1.9%, d4), and management said dividend growth should "approximate AFFO per share growth" going forward.

## 7. Valuation snapshot & reverse DCF
Price (2026-09-25 close) $1,008.08; GAAP trailing P/E 65.0x / NTM P/E 54.7x (d4) — both distorted by heavy real-estate depreciation, the classic reason GAAP P/E is the wrong lens for a REIT. The economically relevant multiple is price/AFFO: $1,008.08 ÷ FY2026-guided AFFO/share midpoint ($42.99) ≈ **23.4x**, versus FCF yield 3.8–4.2% (d4). Peer DLR (Digital Realty, a direct data-center-REIT comparator) trades at an even richer NTM P/E of 62.1x with a lower FCF yield (5.6% — Yahoo methodology differs from AFFO) and dividend yield 2.7% (d4, 2026-09-25); sell-side mean target for EQIX is $1,233.48 (+22%, d4). **No V1 row exists for EQIX** → v1_verdict = null; valuation view is independently derived.

**Reverse DCF (AFFO basis):** EV = market cap $99.47bn + net debt ~$21.17bn = $120.6bn; AFFO₀ = FY2026-guided $4.27bn; WACC 8.3% (cost of equity = rf 4.2% + β0.97×ERP 5% = 9.1%; post-tax cost of debt ≈4.5%; debt weight ≈17.5%) **[Corrected 2026-10-08: rf should be the 5.17% 10-year Treasury (25 Sep 2026); AFFO adds back SBC and excludes growth capex; restated Ke 9.5%, WACC 8.8%]**; terminal growth 3%. Solving for the 10-year AFFO growth rate that reproduces today's EV gives **implied growth ≈7.8% p.a.** **[Corrected 2026-10-08: restated to ~10.7% p.a. on AFFO less SBC at WACC 8.8%]** My evidence-based base case is **~10% p.a.** — the midpoint of management's own just-raised, credible (three-consecutive-raise track record) 2027–2029 AFFO/share growth guide of 9–12%. Implied (7.8%) is **below** base case (10%) → the stock is **not** priced above what the evidence supports; if anything it screens modestly cheap relative to the newly raised long-term algorithm. **[Corrected 2026-10-08: withdrawn: restated implied ~10.7% vs base ~10% is in line]** Bear case 4%/yr (AI-capex demand cools, heavy equity issuance to fund the doubled capex program dilutes per-share AFFO growth well below aggregate growth, exit multiple compresses to 18x): **3-yr annualized return ≈ −3%**. Base case 10%/yr, exit multiple ~23x (roughly stable): **≈ +11%/yr**. Bull case 13%/yr (top of the new long-term range sustained, multiple re-rates to 26x): **≈ +18%/yr**.

## 8. Bull case / Bear case
**Bull:** (1) the interconnection network effect (record 9,700 net interconnections added in Q2'26, third consecutive quarter of double-digit MRR growth) is arguably the hardest-to-replicate moat among data-center REITs — a new entrant cannot buy its way into an existing web of carrier/cloud relationships; (2) management just raised its long-term (2027–2029) growth algorithm across revenue, AFFO/share and EBITDA margin, backed by record bookings, not merely a forecast; (3) xScale JVs let EQIX capture hyperscale demand while keeping a meaningful share of that capex off its own balance sheet, partially mitigating the funding/dilution risk in §6.
**Bear:** (1) the capex step-up is real and large — guided FY2026 total capex of $5–6bn is roughly double the prior non-recurring run-rate, and it must be funded by some mix of debt (pushing leverage higher) and equity (diluting per-share AFFO growth) for years; (2) a March 2024 short-seller report (Hindenburg Research) alleged Equinix was misclassifying maintenance capex as growth capex to inflate AFFO — a direct challenge to the exact metric this dossier's valuation relies on (§11); although the company's own investigation and the SEC/DOJ inquiries have since closed with no restatement and no enforcement action, the underlying capex-classification judgment calls that prompted the allegation still exist and deserve ongoing scrutiny, not blind trust; (3) AI-driven hyperscaler demand for interconnected colocation, while currently accelerating, is a newer and less-tested growth driver than EQIX's historically stable enterprise-colocation base — a slowdown in hyperscaler capex plans (already debated across the sector) would hit the highest-growth, highest-multiple part of the bull case first.

## 9. Key risks & measurable kill criteria
1. AFFO/share guidance cut (a reduction to the low end of the then-current full-year range) at a subsequent quarterly release.
2. Net debt/EBITDA rises above 5.0x (from ~4.0x currently) without a credible funding plan disclosed alongside it.
3. Recurring (monthly recurring revenue) growth decelerates below 8% YoY for two consecutive quarters (from 11% currently).
4. Any restatement of prior AFFO or capex classification, or a new SEC/DOJ enforcement action (distinct from the closed 2024 matter).
5. Annualized gross bookings decline YoY for two consecutive quarters (from +23% YoY currently).

## 10. Catalysts & calendar
Next earnings: **2026-10-28** (Q3'26, per d4 next_earnings_date). Watch for: bookings trend continuation, any update on xScale JV funding/equity stakes, and the pace of the capex step-up (guided $5–6bn FY2026) actually landing within range.

## 11. Red-flag scan
**Material, now-resolved:** on 20 March 2024 short-seller Hindenburg Research published a report alleging Equinix engaged in "accounting manipulation" — specifically, misclassifying capex necessary to sustain existing operations as growth/expansion capex to inflate AFFO. The Audit Committee launched an independent investigation (WilmerHale/AlixPartners); Equinix received subpoenas from the SEC (30 April 2024) and the US Attorney's Office, N.D. California. The investigation "didn't identify any accounting inconsistencies or errors that would require an adjustment to previous financial statements" per the company; on 19 November 2025 the SEC notified Equinix it had concluded its investigation with no enforcement action recommended, and the company said it expects no further NDCA action. A related shareholder securities class action was settled for $41.5m. No auditor change, going-concern language, or restatement was found. **Read-through:** the underlying dispute (recurring vs. non-recurring capex classification) is exactly the judgment call behind the AFFO figure this dossier's valuation depends on — the matter is legally closed but the modeling sensitivity it exposed is not, and warrants continued monitoring each quarter (§9, kill criterion 4).

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q and 8-K ex-99.1, both filed 2026-07-29. Events checked to 2026-09-25 (litigation/regulatory search, guidance history). All figures are consolidated (US GAAP, single-entity reporter, no separate standalone statements filed). GAAP figures are labelled GAAP; AFFO/FFO are Equinix's own non-GAAP measures (industry-standard NAREIT-style definitions) and are labelled as such — never conflated with GAAP net income or EPS. **Research only, not personal investment advice. This is research, not investment advice, and not a recommendation.**

## 13. Sources
1. SEC EDGAR XBRL companyfacts, CIK0001101239: https://data.sec.gov/api/xbrl/companyfacts/CIK0001101239.json
2. Q2'26 8-K ex-99.1 (filed 2026-07-29): https://www.sec.gov/Archives/edgar/data/0001101239/000110123926000145/a991eqix-q226xpr.htm
3. Q1'26 8-K press release (filed 2026-04-29): https://www.sec.gov/Archives/edgar/data/0001101239/000110123926000089/eqix-q126xpr.htm
4. Q3'25 8-K press release (filed 2025-10-29): https://www.sec.gov/Archives/edgar/data/1101239/000110123925000061/october292025pressrelease-.htm
5. Q4/FY2025 press release and financials (Feb 2026): https://d1io3yog0oux5.cloudfront.net/_ba869986ad322fb21537df4eea7e069d/equinix/db/2183/27011/earnings_release/Equinix+Q4+2025+Press+Release+and+Financials+Final.pdf
6. DataCenterDynamics, "SEC drops investigation into Equinix following short-seller accusations of accounting manipulation": https://www.datacenterdynamics.com/en/news/sec-drops-investigation-into-equinix-following-short-seller-accusations-of-accounting-manipulation/
7. Bloomberg Law, "Equinix Leaders Sued by Shareholder Over Accounting Fraud Claims" (class-action settlement reporting)
8. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (as_of 2026-09-25)
9. v4/outputs/Q13_triage.json (EQIX entry)
10. v4/outputs/v1_valuation_table.csv (checked: no EQIX row)


## Correction (verification DV15, 2026-10-08)

1. Guidance count: the releases show a raise at Q3'25, an initiation of FY2026 guidance at Q4/FY'25 (not a raise), then raises at Q1'26 and Q2'26. 'Four consecutive releases, all raises' (s5) and 'four consecutive guidance raises' (F32 confidence_in_thesis) should read three consecutive raises plus one initiation. FY2025 actual diluted AFFO/share was $38.33 (Q4/FY25 release 0001101239-26-000030), not '~$38.5'.
2. Recurring capex is guided at $290-310m, ~3% of revenue (8-K Ex-99.1 0001101239-26-000145), not ~1.6%. Net debt omits $1,245m of short-term investments: carrying debt $21,989m (senior notes $19,689m, finance leases $2,280m, mortgages $20m) less cash $979m and short-term investments $1,245m is ~$19.8bn (about 3.8x guided adjusted EBITDA of $5.21-5.27bn).
3. Reverse DCF restated to programme rules. The dossier's inputs replicate (implied 7.8%) but the risk-free rate of 4.2% is not the 5.17% Treasury, AFFO adds back stock-based compensation ($531m TTM: 498 FY25 - 240 1H25 + 273 1H26) and excludes ~$5bn/yr of non-recurring capex. Using 5.17% + 0.97 x 4.5% = Ke 9.5%, WACC 8.8%, terminal growth 3%, AFFO less SBC (~$3.7bn) and EV net of cash and short-term investments (~$119bn), implied 10-year AFFO growth is ~10.7%, against the base of ~10% (management guide 9-12%). implied_vs_base is therefore in line, not 'below'; on a dividend-only basis ($2.04bn) the implied growth is ~18%, which shows how much the price depends on growth capex earning its return.
4. The conclusion 'screens modestly cheap' (s7) and F32 dossier_view 'cheap' are withdrawn; the stock is fairly priced on the corrected method. The 3-year scenario returns (bear -3%, base +11%, bull +18%) re-compute from the stated growth and exit-multiple assumptions and are unchanged.

Verdict stays **INCLUDE-SMALL**; implied_vs_base changes below -> in_line and dossier_view cheap -> fair (F32_summary.json valuation_view_vs_v1 updated; scenarios unchanged).
