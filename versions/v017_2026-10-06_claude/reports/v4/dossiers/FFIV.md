# F5, Inc. (FFIV) — Fundamental Diligence Dossier (F124, wave 8, standard depth)

**Verdict: WATCH** — 12–36 month thesis horizon. One-sentence reason: F5 is a cash-generative, debt-free application-delivery and security franchise executing well (guidance raised three times in a row, eight straight quarters of double-digit product growth), but at $443.06 the price implies ~14% annual growth in SBC-adjusted free cash flow per share for ten years while a hardware refresh cycle, a fresh security-incident overhang and ~7.5% SBC make my base case 8%; a great business priced for more than I can underwrite. Condition that changes it: a price near ~$340 (about 20x FY26 non-GAAP EPS), or evidence that software/subscription revenue is re-accelerating beyond the systems cycle.

Triage reconciliation: `Q11_triage.json` shows FFIV as "no" (application-delivery and security appliances/software for enterprise data centers). I confirm the exclusion on price, not on quality. No V1 row exists for FFIV in `v1_valuation_table.csv`; v1_verdict = null.

## 1. Business in plain English
F5 sells the gear and software that sit in front of a company's applications to balance traffic, speed them up and defend them (BIG-IP load balancers and firewalls as appliances and software, NGINX, and Distributed Cloud security services). Customers are large enterprises and service providers; revenue is products (systems and software, about half) plus maintenance and services (about 47%). The moat is installed base and switching cost: replacing the traffic layer of a production application is risky, which keeps renewals and upgrade cycles predictable. Threats: cloud-native alternatives, pricing, and the company's own security incident.

## 2. Why the model likes it (b1) and durability
b1 composite percentile 0.78 (composite_qvm 0.82, the highest of my three names): Quality 0.67 (gross-profit-to-assets percentile 0.72), Value 0.66 (FCF yield percentile 0.62, earnings yield 0.57) and Momentum 0.60 (12-1 month percentile 0.60). The quality and valuation percentiles are relative to the whole S&P 500, not F5's own history. Durability question: systems revenue (+32% in Q3 FY26) reflects a multi-quarter refresh cycle and is the cyclical part; inventories rose to $126.9M from $77.2M at 30 Sep 2025 (Form 10-Q 0001048695-26-000067), a sign of a supply build that can reverse. Data conflict: d4 shows free cash flow of $717M, but the filings give TTM operating cash flow ~$1,049M and capex ~$80M (FCF ~$970M, derived below).

## 3. Last 8 quarters (consolidated F5, Inc.; $M except EPS; fiscal year ends 30 Sep; GAAP unless labelled)
| Quarter | Revenue | YoY | GAAP op income | GAAP op margin | GAAP EPS | Non-GAAP EPS (adjusted, excludes SBC and amortisation) |
|---|---|---|---|---|---|---|
| Q4 FY24 | 747 | | n/c | | 2.80 | 3.67 |
| Q1 FY25 | 766 | | 205.1 | 26.8% | 2.82 | 3.84 |
| Q2 FY25 | 731 | | 158.9 | 21.7% | 2.48 | 3.42 |
| Q3 FY25 | 780 | | 196.3 | 25.2% | 3.25 | 4.16 |
| Q4 FY25 | 810 | +8% | 205.6 (FY 765.9 less 9M 560.3) | 25.4% | 3.26 | 4.39 |
| Q1 FY26 | 822 | +7% | 214.2 | 26.0% | 3.10 | 4.45 |
| Q2 FY26 | 812 | +11% | 179.0 | 22.1% | 2.58 | 3.90 |
| Q3 FY26 | 865 | +11% | 213.3 | 24.7% | 3.62 | 4.73 |
Sources: earnings-release exhibits 99.1 to 8-Ks 0001048695-25-000153, -26-000018, -26-000042, -26-000063 and XBRL facts from 10-Q/10-K. Variance, Q3 FY26 vs Q3 FY25: revenue +11% ($865M vs $780M); systems $240M (+32%), software $223M (+7%), services $402M (+3%); GAAP gross margin 82.2% vs 81.0% (+120 bps); GAAP operating margin 24.7% vs 25.2% (-50 bps; opex grew with cyber-incident costs of $3.0M in the quarter and $26.5M in nine months); GAAP EPS $3.62 vs $3.25 (+11%), helped by an 8.0% effective tax rate in Q3 (16.0% for nine months; 10-Q). Momentum: growth accelerated from 7% (Q1) to 11% (Q2, Q3), led by systems; software was -8% in Q1 and +17% in Q2 then +7%, which is lumpy and not yet a steady engine. Non-GAAP operating margin 35.0% vs 34.3%; the gap to GAAP (about 10 points) is mostly SBC and amortisation.

## 4. Guidance track record (fiscal 2026; non-GAAP EPS and revenue growth; company gives explicit ranges)
- Q4 FY25 (8-K 0001048695-25-000153, 27 Oct 2025, issued after the security incident): "for fiscal year 2026, F5 is guiding to total revenue growth of 0% to 4%"; "FY26 non-GAAP operating margin in a range of 33.5% to 34.5%"; "FY26 non-GAAP earnings per share in a range of $14.50 to $15.50." It also warned of "some near-term disruption to sales cycles".
- Q1 FY26 (8-K 0001048695-26-000018, 27 Jan 2026): "F5 raised its outlook for its fiscal year 2026, guiding for revenue growth in a range of 5% to 6%, up from 0% to 4% previously"; "non-GAAP earnings per share in a range of $15.65 to $16.05, up from $14.50 to $15.50 previously."
- Q2 FY26 (8-K 0001048695-26-000042, 28 Apr 2026): "F5 raised its outlook for its fiscal year 2026, guiding for revenue growth in a range of 7% to 8%, up from 5% to 6% previously. F5 expects non-GAAP earnings per share in a range of $16.25 to $16.55, up from $15.65 to $16.05 previously."
- Q3 FY26 (8-K 0001048695-26-000063, 27 Jul 2026): "F5 raised its outlook for its fiscal year 2026, guiding for revenue growth of approximately 9% to 10%, up from 7% to 8% previously. F5 expects non-GAAP earnings per share in a range of $17.21 to $17.33, up from $16.25 to $16.55 previously." Q4 FY26 guide: "revenue in the range of $870 million to $890 million, with non-GAAP earnings in the range of $4.14 to $4.26 per diluted share."
Result: three consecutive raises, cumulatively +$2.71 at the midpoint vs the initial $15.00 midpoint (from a deliberately low start after the incident). The initial range was set deliberately low after the incident, so part of the raise is recovery from a cautious start. Implied Q4 FY26 non-GAAP EPS $4.20 midpoint is below Q3's $4.73, consistent with a cautious tone.

## 5. Moat and growth drivers
Drivers: hardware refresh of BIG-IP (systems +26% to +37% each quarter this fiscal year), security and AI-gateway products (SurePath AI bought for $50.1M on 15 Jun 2026; CalypsoAI also acquired, 10-Q), and cross-selling Distributed Cloud. Moat: entrenched installed base with mission-critical function; deferred revenue $2.2B (current $1,289.6M plus long-term $903.1M) and remaining performance obligations of $2.2B (10-Q) give revenue visibility. Weakness: services grows only 2-4%; geographic softness in Asia-Pacific is cited in third-party commentary (not verified in a filing).

## 6. Earnings quality and balance sheet (consolidated F5, Inc.; single-entity reporting, no segment split of the balance sheet)
- Consolidated balance sheet (Form 10-Q 0001048695-26-000067, 30 Jun 2026): cash and cash equivalents $1,605.8M; long-term investments $22.0M; no borrowings (the $350M revolving credit facility expired 31 Jan 2025 with no borrowings; 10-Q note). Yahoo's $252M "total debt" matches operating lease liabilities (aggregator item, not financial debt). Net cash ~$1.6B; total shareholders' equity $3,855.7M; goodwill $2,482.5M.
- Cash conversion: nine months FY26 operating cash flow $841.4M and capex $63.7M (FCF $777.7M); Q4 FY25 implied OCF $208.1M (FY25 $949.7M less nine-month $741.6M) and capex $16.1M (FY25 $43.3M less $27.1M). TTM OCF ~$1,049M, capex ~$80M, FCF ~$970M versus TTM GAAP net income ~$726M (Q4 FY25 190 + 180 + 148 + 208), so FCF/NI ~1.34x; helped by deferred-revenue growth of $192.3M in nine months.
- SBC: nine months FY26 $193.5M (about 7.6% of nine-month revenue of $2,499M); TTM ~ $251M. FCF after SBC ~ $719M. SBC-adjusted FCF yield at the $25.5B market cap (57.55M diluted shares x $443.06) ~2.8%; unadjusted FCF yield ~3.8%. Adjusted (non-GAAP) EPS excludes this SBC, so "P/E 25.7x on non-GAAP" understates the cost; GAAP TTM EPS $12.56 implies 35x.
- Capital return: nine-month buybacks $501.1M; $422.4M authorisation remaining at 30 Jun 2026 (10-Q); diluted shares 57.55M vs 58.49M a year earlier (-1.6%). Buybacks roughly offset SBC dilution and then some.
- Quality flags: effective tax rate 8% in Q3 (vs 10.8% a year ago); inventory +64% since 30 Sep 2025; GAAP-to-non-GAAP operating margin gap ~10 points.

## 7. Valuation and reverse DCF (price at 25 Sep 2026 close: $443.06, d4 snapshot)
- Multiples: 25.7x FY26 non-GAAP EPS midpoint $17.27; 35x trailing GAAP EPS $12.56 (d4 shows 35.3x); EV ~$23.9B (market cap $25.5B less $1.6B cash); EV/TTM operating income (GAAP ~$812M, sum of the last four quarters) ~29x; P/B 6.5x; no dividend. Street mean target $436 (Yahoo aggregator) implies no upside and a "hold" rating; third-party commentary shows the stock up ~75% year to date (not primary, directional only).
- V1 reconciliation: no V1 row exists; v1_verdict null.
- Reverse DCF (my assumptions: 9% discount rate, SBC treated as a cash cost, starting SBC-adjusted FCF per diluted share $12.49 = ($970M - $251M) / 57.55M, exit multiple 22x FCF after ten years, no dividends; buybacks are inside the per-share figure): the price implies ~14.3% per year growth in SBC-adjusted FCF per share for ten years (15.4% at a 20x exit; 12.3% with an 8% rate and 24x exit). On non-GAAP EPS ($17.27 start, same 9% and 22x exit) the implied is ~10.7%. My base is 8% (FY26 +9-10% revenue growth is cycle-boosted; software and services are growing in single digits; SBC drag), bear 0% (refresh cycle reverses, exit 16x), bull 13% (AI-security attach lifts software, exit 26x). Implied is above base, so the verdict cannot be INCLUDE or INCLUDE-SMALL.
- 3-year scenario returns (annualised total return from $443.06, no dividend; on non-GAAP EPS start $17.27): bear -14.6% (EPS flat, 16x), base +2.6% (EPS +8%, 22x), bull +13.5% (EPS +13%, 26x). The base assumes a multiple fall from 25.7x to 22x; if the multiple holds the base return is ~+8%.

## 8. Bull and bear
Bull: (1) eight consecutive quarters of double-digit product growth plus three guidance raises suggest the refresh cycle is broad and long (customers upgrading for AI-era traffic and security); (2) software bookings re-accelerate with AI gateway and security attach (software +17% in Q2 FY26); (3) net cash $1.6B and ~$970M FCF fund continued buybacks; margin expansion beyond 35% non-GAAP.
Bear: (1) the price assumes ~14% SBC-adjusted FCF growth against a cyclical systems bump (inventory +64%); any guidance miss could take the multiple to 20x or lower; (2) the October 2025 security incident: "a threat actor maintained long-term, persistent access to F5 systems, and certain files were exfiltrated", with a securities class action (Smith v. F5, filed 19 Dec 2025, class period 28 Oct 2024 to 27 Oct 2025), two derivative suits and "a small number of inquiries from governmental authorities" (10-Q); (3) 35x GAAP earnings on an 8% tax rate and large SBC add-back.

## 9. Key risks and kill criteria (measurable)
1. Fiscal-year guidance cut: any release lowering FY non-GAAP EPS or revenue growth below the prior range (current FY26 range $17.21-$17.33, revenue +9% to +10%).
2. Product revenue growth below 5% year on year in two consecutive quarters (Q3 FY26 +19%).
3. Non-GAAP operating margin below 33% in any quarter (Q3 FY26 35.0%).
4. A quantified loss or regulatory action from the Cyber Incident above $100M, or a customer-notified BIG-IP vulnerability causing named enterprise churn disclosed in a 10-Q/8-K.
5. Inventory above $200M without corresponding product revenue growth above 15%, or consolidated cash below $1.0B.

## 10. Catalysts and calendar
Q4 FY26 earnings around 26 Oct 2026 (estimate from 27 Oct 2025 date; company date not checked); FY27 guidance then (first guide after the cyber-incident year); securities-class-action lead-plaintiff proceedings (Stichting Bedrijfspensioenfonds voor het Bakkersbedrijf appointed 13 Mar 2026 per 10-Q); remaining $422.4M buyback authorisation; Rambler/Lynwood NGINX ownership suit (filed 8 Jun 2020, N.D. Cal., 10-Q note).

## 11. Red-flag scan
Cyber Incident (disclosed 15 Oct 2025): costs $26.5M nine months FY26, insurance recoveries $5.3M; class and derivative suits; "small number of inquiries from governmental authorities" (10-Q). No auditor change, restatement or going-concern language found in the filings opened. Form 4 and Form 144 filings appear in the submissions index for Aug-Sep 2026 (144s on 3, 5 and 14 Sep; several Forms 4 on 4 Aug and 15 Sep); I did not open them, so insider-selling quantity is unverified (a third-party report cited $27.3M sold in 12 months with no buys, not checked to filings). Schedule 13G/A filed 12 Aug 2026 unopened.

## 12. Sources
1. F5 earnings-release exhibits 99.1 to 8-Ks: 0001048695-25-000153 (27 Oct 2025), 0001048695-26-000018 (27 Jan 2026), 0001048695-26-000042 (28 Apr 2026), 0001048695-26-000063 (27 Jul 2026).
2. Form 10-Q for quarter ended 30 Jun 2026, accession 0001048695-26-000067, filed 2026-08-06; Form 10-K FY2025, accession 0001048695-25-000157 (filed 2025-11-25) via XBRL companyfacts https://data.sec.gov/api/xbrl/companyfacts/CIK0001048695.json.
3. `v4\data\d4_live_snapshot.parquet`, `b1_live_scores.csv` (cross-check only).

## Data basis, recency and disclaimer
Most recent period incorporated: quarter ended 30 June 2026 (10-Q filed 6 Aug 2026); filings checked to 25 Sep 2026. GAAP and non-GAAP (company-defined; excludes SBC and amortisation) figures are labelled. The reverse DCF and scenario returns are my assumptions as stated. Research, not personal investment advice.
