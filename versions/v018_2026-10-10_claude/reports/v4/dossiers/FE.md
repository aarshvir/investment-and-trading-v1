# FirstEnergy Corp. (FE) — Diligence Dossier (Agent F75, Wave 4)

## 1. Verdict
**INCLUDE-SMALL** (half weight). Thesis horizon: 24–36 months. Reservation: free cash flow is structurally negative through the current capital plan, so the dividend and the newly-enlarged capex program depend on continuous debt/equity market access, and a legacy governance overhang (HB6) is not fully closed at the individual level.

## 2. Business in plain English
FirstEnergy is a holding company for ten rate-regulated electric transmission-and-distribution utilities serving roughly 6 million customers across Ohio, Pennsylvania, New Jersey, West Virginia and Maryland. It earns a regulated return on the "wires" it builds and maintains (it largely exited unregulated generation years ago), so revenue and earnings grow mainly through rate-base investment approved by state commissions and FERC, not through selling more electricity. Its main competitive position is as the incumbent, sole regulated distributor in its territories.

## 3. Why the model likes it — durable or artefact?
Per `v4/data/b1_live_scores.csv` (as of 2026-09-25): composite decile 4/10, quintile 2, live_rank 334/~500 — a middling quant score. The model's attraction is concentrated in **momentum** (fam_M 0.69, 12-1m return percentile 0.69) and **earnings surprise** (fam_S 0.53, SUE percentile 0.53), not classic value (fam_V 0.20 — low, because raw earnings-yield and EBIT/EV percentiles are poor for a bond-proxy utility) or quality (fam_Q 0.38, dragged down by a leverage percentile of just 0.05, i.e. FE is among the most levered names in the universe on this raw metric). **Judgement: partly durable.** The re-rating reflects real news (HB6 settlement progress, a materially larger capital plan) rather than a one-off print, but the "quality" flag on leverage is not an artefact — FE really does carry utility-typical but elevated debt, now growing further.

## 4. Last 8 quarters (GAAP; Revenues = us-gaap:Revenues; Q4 figures for FY2024/FY2025 are derived by subtracting the sum of the three reported quarters from the audited annual 10-K total, since FirstEnergy's 10-K does not separately tag a discrete Q4 XBRL fact — flagged where used)
| Quarter | Revenue ($M) | Op. income ($M) | Op. margin | Net income ($M) | GAAP diluted EPS |
|---|---|---|---|---|---|
| Q3'24 | 3,729 | 727 | 19.5% | 419 | $0.73 |
| Q4'24 (derived) | 3,176 | 613 | 19.3% | 261 | ~$0.45 |
| Q1'25 | 3,765 | 754 | 20.0% | 360 | $0.62 |
| Q2'25 | 3,380 | 646 | 19.1% | 268 | $0.46 |
| Q3'25 | 4,148 | 830 | 20.0% | 441 | $0.76 |
| Q4'25 (derived) | 3,797 | **-24** | n.m. | **-49** | **~-$0.08** |
| Q1'26 | 4,202 | 828 | 19.7% | 405 | $0.70 |
| Q2'26 | ~3,700 | n/a* | n/a* | n/a* | $0.50 (GAAP); $0.50 core (non-GAAP) **[Corrected 2026-10-10: 10-Q: Q2'26 revenue $3,678m, operating income $677m, net income $288m (vs $3,380m, $646m, $268m in Q2'25)]** |

*Q2'26 operating income/net income not yet in SEC's XBRL companyfacts cache (data lags the 2026-07-28 10-Q by one refresh cycle); EPS is from the 8-K press release. Note the derived **Q4'25 GAAP operating loss and net loss** — full-year 2025 Core (non-GAAP) EPS was a positive $2.55 vs GAAP diluted $1.76, so a large adjustment sits in Q4; the exact composition (pension/OPEB mark-to-market is the standard driver for utilities booking actuarial remeasurement in Q4, but this is not confirmed from a primary source in this session) should be pulled from the FY2025 10-K non-GAAP reconciliation before increasing conviction. **[Corrected 2026-10-10: 10-Q Note 9: the PUCO order of 7 Jan 2026 required about $275m ($213m after tax) of customer restitution and refunds, recognized in Q4 2025; that is the large Q4 item, not pension/OPEB mark-to-market]** **Data conflict flagged.**

Revenue growth has accelerated: +11.6% YoY in Q1'26, roughly +9% in Q2'26 (vs mid-single-digit in 2024).

## 5. Guidance track record (last 3 releases; FY2026 Core EPS)
| Release | Date | Guidance given | vs prior |
|---|---|---|---|
| Q4/FY2025 | 2026-02-17 | Initial FY2026 Core EPS $2.62–$2.82 | New (2025 Core EPS was $2.55, itself +7.6% vs 2024's $2.37) **[Corrected 2026-10-10: the Q4/FY25 release headline says the company 'Affirms 2026 Core Earnings guidance range of $2.62 to $2.82', so the range pre-dates 17 Feb 2026 and was affirmed, not initiated, here (acc 0001031296-26-000041)]** |
| Q1 2026 | 2026-04-28 | Reaffirmed $2.62–$2.82 | Maintained |
| Q2 2026 | 2026-07-28 | Reaffirmed $2.62–$2.82 | Maintained |

Guidance has not been raised all year despite Q1/Q2 revenue growth of ~10–12% — management is holding the same range through two above-trend quarters. That is conservative/credible, but it also means no guidance-raise catalyst is currently priced for the rest of 2026. Long-term: management reaffirms a **6–8% Core EPS CAGR through 2030, "near the top end,"** underpinned by a **5-year "Energize365" capital plan just raised ~30% to $36bn (2025–2029; $6bn in 2026 alone)** (source: Q2 2026 release).

## 6. Earnings quality & balance sheet
- **Balance sheet (consolidated, per the 10-Q as of 2026-06-30, filed 2026-07-28):** cash $63M; current portion of long-term debt $505M; long-term debt & other long-term obligations $27,102M; total liabilities $43,795M; stockholders' equity $14,426M; total assets $58,221M.
- **Net debt ≈ $27.5bn.** Against TTM EBITDA ≈ $5.42bn (d4 snapshot), **net debt/EBITDA ≈ 5.1x** **[Corrected 2026-10-10: balance sheet also has short-term borrowings of $1,376m; debt = 505 + 1,376 + 27,102 = $28,983m, net debt $28,920m; on the d4 EBITDA of $5.42bn that is 5.3x, not 5.1x (10-Q acc 0001031296-26-000123)]** — high in absolute terms but within the normal range for a rate-regulated wires utility carrying its rate base on the balance sheet; still worth watching as the capital plan grows.
- **Free cash flow is negative:** TTM FCF ≈ **-$2.01bn** (fcf_yield -8.0%, d4 snapshot) — capex is running well ahead of operating cash flow, so the dividend (4.3% yield) and the enlarged capital plan are funded by new debt and/or equity issuance. This is the single biggest thing to monitor: a 30% step-up in the 5-year capital plan raises the odds of dilutive equity issuance.
- **GAAP vs Core (non-GAAP):** FY2025 GAAP diluted EPS $1.76 vs Core EPS $2.55 — a large, utility-typical gap (Core normally excludes mark-to-market pension/OPEB, discontinued items, and legacy-litigation items); the derived Q4'25 GAAP loss above is the concrete manifestation of that gap and needs the reconciliation table to fully explain.
- **Cash items:** the H1 2026 cash-flow statement shows **$266M of "Ohio settlement customer restitution and refunds" paid** — the HB6 settlement clean-up is being executed, not merely promised.

## 7. Valuation snapshot and reverse DCF
NTM P/E ≈ 15.0x (d4 pe_ntm 14.97), FY2026 P/E on guided Core EPS midpoint ($2.72) ≈ 15.9x, dividend yield 4.3%, beta 0.44. This sits within the normal 15–18x band for large regulated utilities and is described in the model as "within Street 12m target range" (per triage data card).

**Reverse DCF (own model; no V1 row exists for FE — it is outside V1's 69-name universe, so `v1_verdict` is null):** solving for the constant 10-year Core-EPS CAGR that, combined with the current dividend payout ratio (~68% of EPS) and a 16x exit P/E, discounted at a 7.8% cost of equity (beta 0.44 utility, but with a small idiosyncratic premium for residual litigation/regulatory risk), reproduces the current $43.30 price: **implied growth ≈ 3.3%/yr** — well **below** management's own guided 6–8% CAGR. `implied_vs_base = "below"`. If FE simply delivers its own guidance, this is a mispriced (cheap) utility; if it merely delivers half its guidance, the stock is still roughly fairly valued.

## 8. Bull case
1. The market is pricing in only ~3.3%/yr EPS growth against a management-guided 6–8%/yr — a real margin of safety if the $36bn Energize365 plan executes as filed.
2. The corporate-level HB6 legal overhang is largely resolved: the 2021 DPA was completed, a $100M SEC penalty was paid (2024), and PUCO approved a settlement in January 2026 that increased customer restitution and closed four investigations — governance-discount compression is plausible.
3. 4.3% current dividend yield plus guided high-single-digit EPS growth is a straightforward ~11%/yr total-return algebra if the multiple simply holds.

## 9. Bear case
1. TTM free cash flow is **-$2.0bn**; the newly enlarged $36bn capital plan will very likely require incremental debt and/or new equity, which could dilute EPS growth below the headline rate-base growth.
2. Guidance was **not raised** at either Q1 or Q2 2026 despite ~10%+ revenue growth — a sign management sees cost inflation, regulatory lag, or interest expense eating into the topline before it reaches Core EPS.
3. A criminal trial of two former FirstEnergy executives (Chuck Jones, Mike Dowling) is now scheduled for jury selection **21 January 2027**, and the 10-Q references an ongoing securities class action without giving its resolution status in the section retrieved — the governance story is improved, not closed.

## 10. Key risks & kill criteria (measurable)
1. FY2026 Core EPS guidance cut below the current $2.62 low end in any quarterly release.
2. Consolidated net debt/EBITDA rises above 5.5x (per the 10-Q debt schedule) without a disclosed, credible deleveraging plan tied to Energize365 financing.
3. An adverse verdict, or new DOJ/SEC action, arising from the January 2027 criminal trial of former executives.
4. A single unplanned equity issuance diluting shares outstanding by more than 5% versus the financing plan disclosed at the time of the $36bn capital-plan announcement.
5. Two additional consecutive quarters of GAAP operating losses (as derived for Q4 2025) without a primary-source explanation in the 10-K/10-Q reconciliation.

## 11. Catalysts & calendar
- Next earnings: **21 October 2026** (Q3 2026, per d4 snapshot).
- Pending state rate-case decisions across OH/PA/NJ/WV/MD (not individually itemized here — follow-up item).
- Criminal trial jury selection: 21 January 2027 (former executives, not the company).

## 12. Red-flag scan
- **Resolved at corporate level:** 2021 DOJ Deferred Prosecution Agreement (SDOH) — completed; $230M 2021 penalty and $100M 2024 SEC securities-fraud penalty paid; PUCO settlement approved 7 Jan 2026 closing four HB6-related investigations, restitution being paid on schedule ($266M in H1 2026).
- **Open:** an ongoing securities class action is referenced in the current 10-Q's forward-looking-statement risk factors without a named case/status in the excerpt reviewed — **follow-up item, not confirmed resolved.**
- **Open:** criminal trial of two former executives set for January 2027 — reputational/discovery risk to the company even though FE itself is not the defendant.
- No auditor change, no material-weakness or going-concern language found in the sections reviewed.

## 13. Sources
1. SEC EDGAR submissions — CIK 0001031296: https://data.sec.gov/submissions/CIK0001031296.json (retrieved 2026-09-26)
2. SEC XBRL company facts — https://data.sec.gov/api/xbrl/companyfacts/CIK0001031296.json (retrieved 2026-09-26; data current through the 10-Q filed 2026-04-28 — see §4 note)
3. Form 10-Q, period 2026-06-30, filed 2026-07-28: https://www.sec.gov/Archives/edgar/data/1031296/000103129626000123/fe-20260630.htm
4. Q2 2026 earnings release (8-K Ex-99.1), filed 2026-07-28: https://www.sec.gov/Archives/edgar/data/1031296/000103129626000122/ex991-q22026newsrelease.htm
5. Q1 2026 earnings release (8-K Ex-99.1), filed 2026-04-28: https://www.sec.gov/Archives/edgar/data/1031296/000103129626000084/ex991-q12026newsrelease.htm
6. Q4/FY2025 earnings release (8-K Ex-99.1), filed 2026-02-17: https://www.sec.gov/Archives/edgar/data/1031296/000103129626000041/ex991-q42025newsrelease.htm
7. WebSearch: FirstEnergy DPA/HB6 status (Columbus Underground, PUCO, OCC.ohio.gov, occ filings) — retrieved 2026-09-26.
8. `v4/data/b1_live_scores.csv`, `v4/data/d4_live_snapshot.parquet` (as of 2026-09-25).

## 14. Data basis, recency and disclaimer
Most recent period incorporated: fiscal Q2 2026 (ended 2026-06-30, 10-Q filed 2026-07-28) for the balance sheet and legal-proceedings excerpt; SEC XBRL companyfacts data used for the multi-quarter table is current only through the 10-Q filed 2026-04-28 (one quarter behind the 10-Q itself — disclosed in §4). Events checked to 2026-09-25. GAAP figures are labelled GAAP; "Core Earnings" is FirstEnergy's own non-GAAP measure and is labelled as such throughout. This is research, not investment advice, and not a recommendation; it is not personalized to any individual's circumstances.

## Correction (verification DV17, 2026-10-10)

**Wrong text and corrections (checked against 10-Q acc 0001031296-26-000123, Q2 release acc 0001031296-26-000122, Q4/FY25 release acc 0001031296-26-000041, Q1 release acc -000084):**
1. Section 6 net debt: omits short-term borrowings of $1,376m. Debt = currently payable LTD $505m + short-term borrowings $1,376m + long-term debt and other long-term obligations $27,102m = $28,983m; cash $63m; net debt $28,920m (not about $27.5bn). On the dossier's own d4 EBITDA of $5.42bn, net debt/EBITDA is 5.3x (not 5.1x), 0.17x below kill criterion 2 (5.5x), not 0.4x. The $5.42bn EBITDA could not be reproduced from the filings: TTM operating income $2,311m (FY25 2,206 + H1'26 1,505 - H1'25 1,400) plus TTM provision for depreciation about $1,683m is about $4.0bn, which would give about 7x; kill criterion 2 should state its EBITDA definition (UNVERIFIABLE, left for the lead).
2. Section 4 and 6: Q4 2025 derived operating loss of $24m and net loss of $49m are arithmetically right (FY25 less nine months). The cause is not pension MTM: Note 9 of the 10-Q states that the PUCO order of 7 Jan 2026 directed about $275m ($213m after tax) of restitution and refunds, recognized in Q4 2025; about $266m had been issued by 30 Jun 2026. Kill criterion 5 premise (unexplained operating losses) is therefore resolved for Q4 2025.
3. Section 4: Q2'26 cells left n/a are revenue $3,678m (+8.8% YoY, consistent with the 'roughly +9%' in the text), operating income $677m, net income $288m, GAAP EPS $0.50 (all 10-Q).
4. Section 5: the 17 Feb 2026 release 'Affirms' the $2.62-2.82 range; the dossier calls it 'Initial / New'. Figures are verbatim; only the characterization is wrong.
5. Minor: stockholders' equity $14,426m includes noncontrolling interest (parent common equity $14,106m); TTM FCF from filings is about -$1.95bn (dossier -$2.01bn from d4). Reverse DCF replicates (3.3% at Ke 7.8%; Ke 7.74% = 5.17% + Blume beta 0.62 x 4.14%).

**Verdict:** INCLUDE-SMALL unchanged (valuation inputs unchanged; leverage headroom to the 5.5x kill line is thinner than stated). F75_summary.json FE entry updated (data_conflicts, key_adverse_facts, kill criterion 2).
