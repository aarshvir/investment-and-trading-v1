# HIG — The Hartford Insurance Group — Fundamental Diligence Dossier

**1. Verdict: INCLUDE-SMALL (half weight).** Thesis horizon 12–24 months. Top-decile quality/earnings-momentum quant score and a genuinely strong core-underwriting franchise, but recent GAAP earnings are inflated by one-off items (tax benefit, reinsurance commutation gain), the Business Insurance underlying combined ratio is drifting up off a cyclical low, general-liability/commercial-auto/legacy-A&E reserves are adding back unfavorable development, and sell-side FY1 EPS estimates are being cut hard (17 down vs. 2 up in 30 days) as the pending Hartford Funds divestiture removes an earnings stream from models. **HIG was a v3 "Supporting"-tier holding (4.0% weight in the final 14-name portfolio; 12.0% in the earlier 10-name v1 cut) — v4 would keep it, but at reduced conviction/size versus v3's treatment, not as a core position.**

## 2. Business in plain English
The Hartford is a US commercial-focused property & casualty insurer with three segments: **Business Insurance** (workers' comp, commercial property/liability, small/middle-market/large accounts, Global Specialty), **Personal Insurance** (auto/home, sold mainly through the AARP affinity program and independent agents), and **Employee Benefits** (group life/disability). It earns money from underwriting profit (premiums minus claims and expenses) plus investment income on the "float" between collecting premiums and paying claims. It is a top-5 US commercial-lines writer with a strong small-commercial franchise and a differentiated AARP-branded personal-lines niche. In June 2026 it agreed to sell its **Hartford Funds** asset-management arm to Wellington Management, refocusing the company purely on insurance underwriting.

## 3. Why the model likes it — durable or artefact?
b1 composite score 0.886 (decile 10/10, live_rank 20, inside the live top-30). Driven mainly by **Quality** (fam_Q top quartile: pct_roe 76th pctile, pct_ocf_a 85th) and **earnings momentum/SUE** (pct_sue 89th pctile; beats 6 of last 8 quarters, avg surprise +9.3%). Price momentum is a *weak* spot, not a strength (pct_mom_12_1 only 33rd pctile), and book-to-price is low (17th pctile — HIG is not statistically cheap). **Partly artefact:** GAAP ROE and recent EPS growth are flattered by non-recurring items (see §6). Management's own stated **trailing-12-month core-earnings ROE of 20.3%** (Q1 2026 release) is the more durable underlying number, but even that sits atop several years of below-average catastrophe experience and favorable-leaning reserve development — a full-cycle test has not occurred recently.

## 4. Last two years of results (GAAP, from 8-K press releases; core/operating EPS is company non-GAAP, labeled)
| Quarter | Revenue | Net earned prem. | GAAP EPS (dil.) | Core EPS | Combined ratio BI / PI | Underlying CR BI / PI |
|---|---|---|---|---|---|---|
| Q3'24 | n/a* | n/a* | n/a* | $2.53 | 92.2 / 102.5 | n/a |
| Q4'24 | n/a* | n/a* | $2.88 | $2.94 | 87.4 / 85.8 | 87.1 / 90.2 |
| Q1'25 | n/a* | n/a* | $2.15 | $2.20 | 94.4 / 106.1 | 88.4 / 89.7 |
| Q2'25 | $6,716M | $5,961M | $3.44 | $3.24 | 87.0 / 94.1 | 88.0 / 88.0 |
| Q3'25 | n/a* | n/a* | $3.77 | $3.78 | 88.8 / 88.7 | 89.4 / 90.0 |
| Q4'25 | n/a* | n/a* | $3.98 | $4.06 | 83.6 / 79.6 | 88.1 / 84.3 |
| Q1'26 | $7,226M | $6,145M | $3.04 | $3.09 | 94.8 / 87.7 | 89.2 / 85.0 |
| Q2'26 | $7,263M | $6,279M | **$4.68** | $3.42 | 91.4 / 90.1 | 89.3 / 86.3 |

\* Not requested/returned from the specific press-release extracts pulled; not fabricated. FY2025 GAAP EPS $13.32 (FY2024 $10.35); FY2025 core EPS $13.42 (FY2024 $10.30). **Note the Q2'26 GAAP/core gap ($4.68 vs $3.42)** — driven by one-offs in §6, not operating performance. **BI underlying combined ratio has drifted from 88.0 (Q2'25) → 89.2 (Q1'26) → 89.3 (Q2'26)** — a modest but real deterioration off the cycle low, consistent with sell-side commentary on softer P&C pricing.

**Data conflict (flag for the lead):** DA2 found a filer-side EPS scale error in HIG's XBRL EPS series. This dossier deliberately sources every EPS figure from the primary 8-K/press-release text (above), **not** from XBRL — do not reconcile this table against `d3`/XBRL EPS without applying DA2's correction.

## 5. Guidance track record
HIG **does not issue quantitative forward EPS, combined-ratio, or revenue guidance** in any of the last four earnings releases (Q2'26, Q1'26, Q4'25, Q3'25) — standard for P&C underwriters given catastrophe unpredictability. Each release closes with a generic safe-harbor statement and qualitative CEO commentary only (e.g., Q4'25: "enters 2026 with momentum," no numbers). **No raise/maintain/cut can be assessed because no numerical guidance exists to compare** — stated per instructions rather than inferred.

## 6. Earnings quality & balance sheet
- **One-off items distorting recent GAAP results:** (a) **$251M income-tax benefit** in Q2'26 tied to the Hartford Funds sale (tax basis vs. GAAP carrying value); (b) **$318M pre-tax discontinued-operations income** in Q2'26 (Hartford Funds, up from $57M in Q2'25); (c) **$497M pre-tax gain / $393M net-income increase** expected in **Q3 2026** from commuting a legacy asbestos & environmental reinsurance treaty with **National Indemnity Company (Berkshire Hathaway)** — the treaty (in place since Dec-2016) was terminated Sept 25, 2026 alongside settlement of a confidential arbitration; Hartford received **$1.12bn cash**. This is a real cash gain but it also **removes A&E reinsurance cover HIG has relied on since 2016** — future adverse A&E development now falls more directly on HIG's own balance sheet. (d) **$165M A&E reserve increase** in Q4'25 and a further **$70M** increase in Q1'26 for legacy sexual-molestation/abuse exposures (1970s–80s policies, incl. one religious-institution bankruptcy settlement) — a recurring, not one-time, category of adverse surprise.
- **Reserve development is genuinely mixed, not uniformly favorable:** Q1'26 Business Insurance PYD was **$30M net *unfavorable*** (vs. $51M favorable in Q1'25); both Q1'26 and Q2'26 releases cite **"increase in general liability and commercial automobile reserves"** partially offsetting favorable workers'-comp/personal-lines releases — the classic social-inflation pattern the insurance sector playbook flags.
- **Net investment income** rising on both higher yields and a large limited-partnership swing (Q2'26 LP income $114M @ 7.6% annualized yield vs. $13M @ 1.0% in Q2'25 — welcome but lumpy/non-repeatable at that rate).
- **Capital:** Book value/share ex-AOCI $78.91 (Jun-26) vs. $73.62 (Dec-25), +7.2%. Returned $615M to shareholders in Q2'26 ($450M buybacks + $165M dividends); **new $4.2bn buyback authorized Aug 1 2026 through 2028 (+27% vs. prior program)**, explicitly part-funded by Hartford Funds sale proceeds.
- **Governance:** New independent director **Priscilla Almodovar** (ex-CEO, Fannie Mae) appointed to the board effective Sept 1, 2026, joining Audit and Finance/Investment/Risk committees — routine strengthening, no departure disclosed alongside it.

## 7. Valuation snapshot (from v1 pipeline, 2026-09-25 close)
P/B 1.75x vs. peer median 1.79x (P&C peer set) — **77th percentile of HIG's own 14-year P/B history: fair, not cheap.** Justified-P/B math implies the market is pricing an **11.8% sustainable ROE**, vs. actual TTM ROE 22.2% (GAAP, one-off-boosted) / 20.3% core — i.e., the price already assumes today's elevated profitability will not persist at face value. V1 base-case 3-year annualized return +2.7% (bear −15.1%, bull +24.6%); V1 verdict **"fair."**

## 8. Bull case
1. Core-earnings ROE of ~20% is genuinely strong for a diversified P&C/EB insurer, with Business Insurance still growing written premium +5–9% with positive (if moderating) renewal pricing.
2. Hartford Funds sale + National Indemnity commutation simplify the balance sheet, bring in ~$1.1bn+ cash, and fund an enlarged, multi-year buyback — a credible capital-return runway.
3. Personal Insurance has swung from a 106.1 combined ratio (Q1'25, CA-wildfire-affected) to consistently sub-90 through 2025–26 — a real underwriting turnaround in a historically weaker segment.

## 9. Bear case
1. Business Insurance underlying combined ratio is drifting up (88.0→89.3 YoY) exactly as sell-side analysts describe a softening commercial pricing cycle — the tailwind that drove the last two years of beats may be fading.
2. General liability, commercial auto and legacy A&E/molestation reserves are adding *unfavorable* development in the two most recent quarters — a first-order, evidenced risk (not hypothetical) for a company with long-tail casualty exposure, and one that will bite harder now that a chunk of A&E reinsurance cover was just commuted away.
3. Reported GAAP EPS growth is substantially a function of one-off tax/reinsurance/discontinued-ops items; 17 of 19 sell-side FY1 EPS revisions in the last 30 days were cuts, chiefly because the Funds-sale removes a profitable, capital-light earnings stream from forward models.

## 10. Key risks & kill criteria
1. BI underlying combined ratio >91% for two consecutive quarters (cycle-turn confirmation).
2. Adverse general-liability/commercial-auto/A&E reserve development >$150M in any single quarter.
3. Hartford Funds sale is delayed, renegotiated, or terminated (watch for another Item 1.02/1.01 8-K).
4. Core-earnings ROE <15% for two consecutive quarters (vs. 20.3% TTM stated by management).
5. Net FY1 sell-side EPS revisions stay negative for two more months without a corresponding guidance/fundamental offset.

## 11. Catalysts & calendar
- **Next earnings: about 2026-10-29** (Q3 2026; an estimate from the data snapshot, not yet confirmed by the company. Corrected 2026-09-26 after data audit DA5; one third-party calendar shows 2026-10-26) — will show the first full-quarter impact of the $497M National Indemnity commutation gain.
- Hartford Funds/Wellington deal closing — timing not disclosed in materials reviewed; monitor for a closing 8-K.
- $4.2bn buyback program runs through 2028.

## 12. Red-flag scan
No auditor change, material weakness, restatement, or going-concern language surfaced in the materials reviewed (full 10-K risk-factor diff and Form 4 insider-trading pattern were **not** exhaustively pulled given the time budget — scope limitation, not a clean bill of health). The Item 1.02 8-K (Sept 25, 2026) is a **negotiated resolution** of a legacy reinsurance arbitration dispute with Berkshire's National Indemnity — cash-positive for HIG, but confirms the company carried, and now bears more directly, real legacy A&E tail risk. No SEC/DOJ investigation, short-seller report, or litigation beyond routine/legacy claims found in the sources reviewed.

## Sources
1. HIG 8-K/EX-99.1, Q2 2026 (filed 2026-07-23): sec.gov/Archives/edgar/data/874766/000087476626000059/ex991earningsnewsrelease63.htm
2. HIG 8-K/EX-99.1, Q1 2026 (filed 2026-04-23): sec.gov/Archives/edgar/data/874766/000087476626000036/ex991earningsnewsrelease33.htm
3. HIG 8-K/EX-99.1, Q4 2025 (filed 2026-01-29): sec.gov/Archives/edgar/data/874766/000087476626000006/ex991earningsnewsrelease12.htm
4. HIG 8-K/EX-99.1, Q3 2025 (filed 2025-10-27): sec.gov/Archives/edgar/data/874766/000087476625000106/ex991earningsnewsrelease93.htm
5. HIG 8-K Item 1.02/7.01 (filed 2026-09-25, event 2026-09-23), National Indemnity commutation: sec.gov/Archives/edgar/data/874766/000087476626000064/hig-20260923.htm
6. HIG 8-K Item 5.02 (filed 2026-08-11), board appointment: sec.gov/Archives/edgar/data/874766/000087476626000062/a08112026-newsreleasexboar.htm
7. SEC EDGAR submissions feed, CIK 0000874766 (filing calendar/next-earnings cross-check), retrieved 2026-09-26.
8. Investing.com, "Keefe Bruyette cuts Hartford Financial stock price target on fund sale"; "Wells Fargo cuts Hartford Financial stock price target on valuation update" (analyst FY1 EPS cut context, ~Sept 2026).
9. Internal v4 quant pipeline: `data/b1_live_scores.csv`, `data/d4_live_snapshot.parquet`, `outputs/v1_valuation.json`/`v1_valuation_table.csv` (as of 2026-09-25 close).
10. `HANDOFF_v3_US_Equity_Conviction_Research.md` (v3 legacy handoff — HIG's prior weight/tier).
11. `v4/outputs/lead_v3_audit.md` (prior finding on HIG's $251M one-off tax benefit, re-verified above with exact source).

## Data basis, recency and disclaimer

- Most recent reported period incorporated: Q2 2026 (quarter ended 2026-06-30), from the 10-Q and 8-K Exhibit 99.1 cited above; events checked through 2026-09-25 (US close).
- Reporting basis: consolidated US GAAP figures in USD millions unless explicitly labelled adjusted/operating (company non-GAAP) or per share.
- Research, not personalised investment advice; the author is not a licensed adviser.
