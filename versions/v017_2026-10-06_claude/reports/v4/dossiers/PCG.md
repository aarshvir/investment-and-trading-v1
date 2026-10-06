# PG&E Corporation (PCG) — Fundamental Diligence Dossier (F124, wave 8, standard depth)

**Verdict: INCLUDE-SMALL** (half weight at most) — 12–36 month horizon. One-sentence reason: a regulated wires-and-gas utility with visible ~8–9% EPS growth is priced at ~7.5x 2026 guided EPS, which implies far less growth than management targets, but the stock carries an unbounded wildfire-liability tail, the highest debt load in this batch and negative free cash flow, so it must be sized as a special-situation holding, not a core utility. Named reservation: a single catastrophic wildfire caused by utility equipment after the Wildfire Fund / Continuation Account capacity is exhausted could impair equity (2019 precedent).

Triage reconciliation: `Q15_triage.json` shows PCG as "no" (not advanced; note "unresolved, potentially unbounded wildfire liability exposure"). I partly overturn: the exposure is real and stays as a sizing cap, but the filings show the post-AB 1054 / SB 254 framework, three years of reaffirmed/tightened guidance and no planned equity issuance through 2030, so the price already discounts more than the evidence supports. No V1 row exists for PCG in `v1_valuation_table.csv`, so v1_verdict = null.

## 1. Business in plain English
PG&E Corporation is a holding company whose main subsidiary, Pacific Gas and Electric Company (the Utility), sells electricity and gas to about 16 million Californians in Northern and Central California ("parent company of Pacific Gas and Electric Company ... serves 16 million Californians across a 70,000-square-mile service area", Q2 2026 release, Form 8-K 0001004980-26-000047). Earnings come from regulated rate base growth: the CPUC sets revenues to recover costs plus an authorized return on a 52% equity / 47.5% debt / 0.5% preferred capital structure (Form 10-Q 0001004980-26-000048, Liquidity section). Moat is a legal monopoly franchise; the risk is that wildfires caused by its equipment can create liabilities under California's inverse-condemnation doctrine.

## 2. Why the model likes it (b1 scores) and durability
b1 composite percentile 0.78 (composite_qvm 0.62), driven by Value (fam_V 0.80: earnings-yield percentile 0.92, book-to-price 0.98, EBIT/EV 0.82) and Surprise (fam_S 0.82), with Quality 0.71 and Momentum weak (fam_M 0.11; 12-1 month momentum percentile 0.11). Free-cash-flow yield percentile is only 0.09, consistent with the capex-driven negative FCF. This is a Value-family pick: cheap because of the wildfire discount, not a cyclical earnings peak, and the discount is a risk premium that persists or widens if liability reform stalls or a new fire occurs. Conflict: d4 shows `impliedSharesOutstanding` 3.0B and market cap $37.0B, but the 10-Q cover shows 2,202,366,726 shares (Form 10-Q 0001004980-26-000048, balance sheet) and diluted weighted shares of 2,285M including 78M from the mandatory convertible preferred; I use 2,285M x $12.34 = ~$28.2B.

## 3. Last 8 quarters (consolidated PG&E Corporation; $M; GAAP unless labelled; source XBRL companyfacts copy of 10-Q/10-K filings)
| Quarter | Revenue | YoY | Operating income | Op margin | GAAP EPS | Non-GAAP core EPS (company-defined, adjusted) |
|---|---|---|---|---|---|---|
| Q3 2024 | 5,941 | | 1,029 | 17.3% | 0.27 | 0.37 |
| Q4 2024 | 6,631 (FY 24,419 less 9M 17,788) | | 1,020 | 15.4% | 0.30 | 0.31 |
| Q1 2025 | 5,983 | | 1,220 | 20.4% | 0.28 | 0.33 |
| Q2 2025 | 5,898 | | 1,096 | 18.6% | 0.24 | 0.31 |
| Q3 2025 | 6,250 | +5.2% | 1,209 | 19.3% | 0.37 | 0.50 |
| Q4 2025 | 6,804 (FY 24,935 less 9M 18,131) | +2.6% | 1,224 | 18.0% | 0.29 | 0.36 |
| Q1 2026 | 6,881 | +15.0% | 1,470 | 21.4% | 0.39 | 0.43 |
| Q2 2026 | 5,902 | +0.1% | 1,263 | 21.4% | 0.33 | 0.40 |

Variance note (Q2 2026 vs Q2 2025): operating income +15% ($1,263M vs $1,096M), GAAP EPS $0.33 vs $0.24; release attributes the increase to "customer capital investment due to the earnings impact of higher rate base and net O&M savings, partially offset by a lower CPUC return on equity in effect during 2026 as compared to 2025 and increased Wildfire Fund expense" (8-K 0001004980-26-000047). Wildfire Fund expense rose to $126M from $109M in the quarter, mostly accelerated amortization. Revenue is largely pass-through (electric procurement +$201M in Q2), so revenue growth is not the driver; margin and rate base are. Earnings rhythm is stable; no acceleration or deceleration beyond the ROE step-down.

## 4. Guidance track record (non-GAAP core EPS; company gives no GAAP guidance)
- Q3 2025 (8-K 0001004980-25-000147, 23 Oct 2025): "Narrowing 2025 non-GAAP core EPS guidance to $1.49 to $1.51 per share", "from the prior range of $1.48 to $1.52 per share"; "Initiating 2026 non-GAAP core EPS guidance in the range of $1.62 to $1.66"; "Reaffirming at least 9% annual non-GAAP core EPS growth guidance for 2027-2030." Narrowed, midpoint unchanged.
- Q4 2025 (8-K 0001004980-26-000008, 12 Feb 2026): "Tightening 2026 non-GAAP core EPS guidance to $1.64 to $1.66 per share versus $1.62 to $1.66 per share previously." Low end raised 2 cents. FY2025 core EPS delivered $1.50, at the top half of the $1.49-$1.51 range.
- Q1 2026 (8-K 0001004980-26-000032, 23 Apr 2026): "Full year 2026 non-GAAP core EPS guidance reaffirmed at $1.64 to $1.66 per share."
- Q2 2026 (8-K 0001004980-26-000047, 23 Jul 2026): "Full year 2026 non-GAAP core EPS guidance reaffirmed at $1.64 to $1.66 per share."
Result: no cuts in four releases; one narrowing, one low-end raise, two reaffirmations. The 2027-2030 "at least 9%" growth statement is quoted only from the Q3 2025 release; I did not find it repeated in the 2026 releases I opened, so treat it as last explicitly stated on 23 Oct 2025.

## 5. Moat and growth drivers
Rate base growth from ~$11.8B of 2025 capex (consolidated cash flow statement, FY2025 Form 10-K 0001004980-26-000009), undergrounding ("more than 1,900 total miles of undergrounding" by end 2027, Q2 2026 release), 2-4% non-fuel O&M reduction target ("On track to meet 2-4% non-fuel operating and maintenance (O&M) cost reduction target"), and data-center load ("overall pipeline of over 12 gigawatts (GWs)" per Q2 2026 release, a pipeline not a commitment). Counter-weights: ROE reduced in 2026, customer-affordability politics, and California regulatory risk.

## 6. Earnings quality, balance sheet and cash conversion (entity labelled)
- Consolidated PG&E Corporation (Form 10-Q 0001004980-26-000048, Condensed Consolidated Balance Sheet, 30 Jun 2026): short-term borrowings $1,375M; long-term debt classified as current $1,075M (current portion only; carrying value, includes $226M VIE); long-term debt $61,768M (carrying); cash and cash equivalents $972M; total shareholders' equity $33,901M (XBRL StockholdersEquity; includes $1,579M mandatory convertible preferred). Total consolidated debt ~$64.2B; net of cash ~$63.2B. Of this, the statement notes the $61,768M long-term debt "includes $11.6 billion ... related to VIEs" (a subset of that line, not additional) (PG&E Recovery Funding LLC $3.0B and PG&E Wildfire Recovery Funding LLC $7.0B securitisation bonds serviced from customer charges). Ex-VIE consolidated debt ~$52.6B. Consolidated net debt / Yahoo-labelled EBITDA ($10.45B, aggregator cross-check) ~6.0x total, ~5.0x ex-VIE; utility-style metrics (FFO/debt) not disclosed in the filing I opened.
- Entity split of cash: PG&E Corporation standalone $716M; Utility $256M (10-Q Liquidity). Liquidity ~$6.5B including $5.5B undrawn revolvers (Utility $6.25B facility to June 2031 with $4,891M availability; Corporation $650M to June 2029, undrawn; 10-Q credit-facility table).
- Parent holdco debt includes $2.15B 4.25% Convertible Senior Secured Notes due 1 Dec 2027 and $1.0B 6.850% junior subordinated notes due 2056 issued 19 Feb 2026 (10-Q Note on debt). The Dec 2027 convertible is the nearest parent-level maturity.
- Cash conversion (consolidated): TTM operating cash flow ~$8.15B (FY25 $8,716M less H1 25 $3,905M plus H1 26 $3,336M) versus TTM capex ~$12.4B (FY25 $11,787M less H1 25 $5,700M plus H1 26 $6,323M) = free cash flow about -$4.3B. Aggregator d4 shows -$6.15B; the filing-derived figure is used. A regulated utility in a heavy capex cycle normally has negative FCF; it is financed by debt (Utility bond issuance $4.4B YTD per Q2 release) and retained earnings. The 10-Q states that "PG&E Corporation does not expect to undertake any equity issuances through 2030", which is a key condition of the EPS growth case.
- Credit: Utility's "unsecured credit rating remains below investment grade with one of the major credit rating agencies" (10-Q). GAAP vs core gap ~$0.07 per quarter (Q2 2026 non-core $164M after tax), mostly Wildfire Fund amortization and wildfire claims; it recurs every quarter, so GAAP EPS is the more honest figure ($1.18 FY25 GAAP vs $1.50 core).
- Dividend: Yahoo shows $0.20 annual rate (payout ~12% of core EPS); share count 2,202M basic; diluted includes convertible preferred conversion (78M).

## 7. Valuation and reverse DCF (price at 25 Sep 2026 close: $12.34, d4 snapshot)
- Multiples: ~7.5x 2026 guided core EPS midpoint $1.65; 8.9x trailing GAAP; P/B 0.84; dividend yield ~1.6%; Yahoo forward EPS $1.80.
- V1 reconciliation: no V1 row for PCG (`v1_valuation_table.csv` has 93 lines; none for PCG); v1_verdict = null, v1_base_3y = null.
- Reverse DCF (earnings-based; assumptions mine: 9.5% cost of equity reflecting wildfire risk, dividend payout held at 12%, exit multiple 9-11x, 10 years, EPS start $1.65): the price implies core EPS compounding at about 4.0% (exit 11x) to 5.9% (exit 9x) per year. Management's "at least 9%" (Q3 2025 release) is far above the implied; my base is 7% (guidance haircut for ROE reset, O&M and execution); bear 0% with 5.5x; bull 10% with 11x. Implied < base, so INCLUDE-SMALL is permitted. **[Corrected 2026-10-06: the reverse DCF starts from core EPS $1.65 although recurring non-core costs (about $0.22 a year in H1 2026, $0.32 in FY25) are real and the Ke 9.5% is not tied to the 5.17% 10-year Treasury; from a GAAP-adjusted $1.43 the price implies 5.6%-7.6% a year versus base 7%, i.e. in line, not below; INCLUDE-SMALL unchanged (DVH5)]**
- 3-year scenario returns (annualised total return incl. dividends, from $12.34): bear -7.6%, base +13.1%, bull +26.2%. Base return is driven roughly half by EPS growth (7%) and half by re-rating from 7.5x to 8.5x; it is not a "steady-state" estimate. The bear is not the tail: a new catastrophic fire is a separate scenario with loss of well over 50% possible and is not probability-weighted here.

## 8. Bull case and bear case
Bull: (1) rate base and O&M savings deliver guided 9%+ core EPS growth with no equity issuance through 2030; (2) California liability reform (SB 254 report issued 7 Apr 2026) narrows the tail and the multiple re-rates toward 12-14x; (3) data-center load adds rate base without customer bill pressure.
Bear: (1) a new wildfire ignition from Utility equipment once the Wildfire Fund is depleted; the Fund asset is being amortised faster (accelerated amortization in Q2 2026) and the Dixie/Kincade reimbursement application of $1.59B is under CPUC review with $674M already drawn; (2) CPUC ROE and affordability pressure compress earnings growth below 5%; (3) consolidated leverage (~$64B debt) and negative FCF make the equity sensitive to rates and to a credit downgrade.

## 9. Key risks and kill criteria (measurable)
1. A wildfire attributed to PG&E equipment with estimated claims above $1.0B (the Wildfire Fund threshold per 10-Q) in any coverage year, or any Cal Fire report naming Utility equipment for a fire exceeding 100,000 acres.
2. Annual non-GAAP core EPS guidance cut below the low end of the prior range in any release (2026 range $1.64-$1.66), or 2027 guidance implying less than 7% growth.
3. Any announced PG&E Corporation common equity issuance before 2030 (contradicts the 10-Q statement) or dilution above 5% of diluted shares.
4. Any downgrade of the Utility to below its current unsecured rating by the agency that rates it below investment grade, or loss of investment grade at the other agencies.
5. CPUC decision disallowing more than $500M of the $1.59B Kincade/Dixie AB 1054 cost-recovery application (filed 14 Nov 2025).

## 10. Catalysts and calendar
Next earnings: Q3 2026 around 22 Oct 2026 (estimate from prior-year pattern, 23 Oct 2025; company date not checked) **[Corrected 2026-10-06: still not confirmed on EDGAR as of 6 Oct 2026]**. Also: CPUC decision on Kincade/Dixie recovery; SB 254 policy follow-up in the 2027 legislative session; Dec 2027 convertible note maturity; 2027 GRC cycle; fire season through October.

## 11. Red-flag scan
No auditor change or restatement found in the 10-Q/8-K list to 25 Sep 2026; Forms 4 (25 Sep, 9 Sep, 24 Aug, 4 Aug 2026), Form 144 (4 Sep) and Schedule 13G and 13G/A were present in the submissions index but were not opened; insider pattern not assessed. Litigation: Dixie fire, approx 190 complaints on behalf of at least 9,062 plaintiffs (10-Q); cumulative Dixie/Mosquito claim payments $2,344M; Dixie loss accrual balance $202M at 30 Jun 2026; Dixie liability insurance $521M; Wildfire Fund receivable $1.25B of which $1.01B received. Wildfire-related securities claims in the bankruptcy process remain open, with possible additional share issuance to the Fire Victim Trust (10-Q note). An 8-K of 31 Aug 2026 (Item 7.01, furnished) was opened; it only furnishes information and contains no quantified event. The 8-K of 4 Aug 2026 (Items 8.01, 9.01) was opened but I did not read its substantive section; treat as unreviewed.

## 12. Sources
1. PG&E Corp Q2 2026 results, 8-K accession 0001004980-26-000047 (23 Jul 2026) and Q1, Q4, Q3 releases 0001004980-26-000032, -26-000008, -25-000147.
2. Form 10-Q for period ended 30 Jun 2026, accession 0001004980-26-000048, filed 2026-07-23; Form 10-K FY2025 0001004980-26-000009 filed 2026-02-12.
3. SEC companyfacts XBRL: https://data.sec.gov/api/xbrl/companyfacts/CIK0001004980.json (machine copy of filings).
4. `v4\data\d4_live_snapshot.parquet` (retrieved 2026-09-25) as labelled cross-check only.

## Data basis, recency and disclaimer
Most recent period incorporated: quarter ended 30 June 2026 (10-Q filed 23 Jul 2026); filings index checked to 25 Sep 2026 (latest filings: Forms 4 on 25 Sep 2026). GAAP figures are labelled GAAP; "non-GAAP core" is company-defined adjusted and is always labelled. Reverse DCF and scenarios are my own assumptions, stated above. Research, not personal investment advice.

## Correction (verification DVH5, 2026-10-06)

Sources: 10-Q acc 0001004980-26-000048; 8-K Ex-99.1 accs 0001004980-26-000047, -26-000032, -26-000008, -25-000147; XBRL companyfacts. All reported quarterly figures, guidance quotes, balance-sheet lines, wildfire items and liquidity pass. The two mechanical debt flags (1,075 and 11,600 vs 60,146) are false positives.

1. Valuation method (FAIL, moderate). Wrong text: "Implied < base, so INCLUDE-SMALL is permitted" (implied 4.0%-5.9% core EPS growth vs base 7%). Issue: the reverse DCF starts from non-GAAP core EPS $1.65 although section 6 says recurring non-core costs make GAAP the more honest figure (non-core $0.32 in FY25; H1 2026 core 0.83 vs GAAP 0.72, i.e. about $0.22 a year), and the 9.5% cost of equity is not tied to the 5.17% 10-year Treasury (25 Sep 2026; it equals 5.17% plus a 4.33% premium). Correct value: from a GAAP-adjusted $1.43 the price implies 5.6% (11x exit) to 7.6% (9x exit) a year; at Ke 8.67% to 10% the range is 4.8% to 8.1%; base is 7%. implied_vs_base: below -> in line. Verdict stays INCLUDE-SMALL (half weight); the cheapness case rests on the unbounded wildfire tail being priced, not on a growth gap.
2. Unverified: Q3 2026 earnings date (22 Oct) is still an estimate; the 4 Aug 2026 8-K (Items 8.01, 9.01) was not read by this audit.

Verdict change: none. implied_vs_base changed (below -> in line). `F124_summary.json` PCG entry updated (implied_vs_base and reconciliation only).
