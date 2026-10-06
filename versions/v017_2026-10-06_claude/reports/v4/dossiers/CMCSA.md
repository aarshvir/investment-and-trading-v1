# CMCSA — Comcast Corporation

## 1. Verdict
**INCLUDE-SMALL.** Horizon 12–36 months. Named reservation: Comcast announced on 29-Jun-2026 that it will split into two public companies (a "Comcast" broadband/wireless RemainCo and an independent "NBCUniversal" that also absorbs Sky), targeted to close in ~12 months; the capital structure, dividend policy and exact NBCUniversal stake retained (up to 19.9%, to be sold down) are not yet finalized. The 25-Sep-2026 close ($21.91) already prices in roughly a 16–24%/year *perpetual decline* in free cash flow — far worse than anything in the last 5–10 years of delivered results — so the valuation gap is real, but realizing it depends on a binary corporate event executing cleanly, not just on the underlying cash flows. **[Corrected 2026-10-06: the 16-24% a year range rested on V1's mismatched inputs (levered FCF against enterprise value at a 6.05% WACC, FCF before cash paid for intangible assets, SBC added back). On equity value of $77.75bn, TTM FCF after intangibles and SBC of $16.45bn and a 9.0% cost of equity, the price implies a decline of 14.1% a year for 10 years (12.5% on FY2026E, 9.6% on owner FCF). Still far below any base case, so the conclusion is unchanged. See Re-assessment (RA10).]**

## 2. Business in plain English
Comcast sells broadband internet, video and wireless service to US households and businesses (Connectivity & Platforms, ~64% of Q2 2026 revenue) and, through NBCUniversal, makes and distributes films, TV and news (NBC, Telemundo, Universal Pictures, Peacock) and operates theme parks including the new Epic Universe (Content & Experiences, ~36% of revenue). It earns money from broadband/wireless subscriptions, advertising, content licensing and park admissions/spending. Its moat in cable/broadband is a regulated-adjacent local infrastructure duopoly; in media it is content IP and distribution scale, both now being reorganized into two separately traded companies.

## 3. Why the model likes it — durability check
b1 composite 0.656 (decile 7, quintile 4, live_rank 172). Driven by **Value** (fam_V 0.79) and **Quality** (fam_Q 0.56) — cheap on earnings/FCF yield (pct_fcfp 0.97, pct_ep 0.94) with reasonable ROE/OCF-to-assets — while **Momentum is the weakest family (fam_M 0.42)**, consistent with a stock the market has been reluctant to re-rate. This is a genuine value setup, not an artefact: NTM P/E 6.16x sits at the **6.8th percentile of its own ~15-year history** (own_history_percentile 6.8) — i.e. only 7% of history was cheaper. It is, however, *above* the Cable & Satellite peer median of 4.44x (peer set is now just 2 names, mostly CHTR, after Versant's spin removed a pure-play cable-network comp) — so the cheapness case rests on CMCSA's own history, not on a peer discount.

## 4. Last two years of results (quarterly, GAAP, $mn, 10-Q/10-K, SEC EDGAR CIK 1166691)
| Quarter | Revenue | YoY | Op. income | Net income | Diluted EPS | Note |
|---|---:|---:|---:|---:|---:|---|
| Q3 2024 | 32,070 | — | 5,859 | 3,629 | 0.94 | |
| Q4 2024 | ~31,915* | — | ~4,993* | ~4,777* | ~1.31* | *derived: FY2024 10-K minus 9M 2024 10-Q |
| Q1 2025 | 29,887 | −6.8% qoq seasonal | 5,658 | 3,375 | 0.89 | |
| Q2 2025 | 30,313 | +2.1% | 5,992 | **11,123** | **2.98** | includes **~$9.4bn pre-tax Hulu-stake sale gain** (one-off, GAAP only) |
| Q3 2025 | 31,198 | −2.7% yoy | 5,534 | 3,332 | 0.90 | |
| Q4 2025 | ~32,309* | — | ~3,488* | ~2,168* | ~0.59* | *derived; depressed by Versant separation costs |
| Q1 2026 | 31,457 | +5.3% yoy | 4,135 | 2,174 | 0.60 | first full quarter **ex-Versant** (spun off 2-Jan-2026) |
| Q2 2026 | 29,940 | −1.2% yoy | 5,160 | 3,526 | 0.99 | |

Q2 2026 segment detail (press release, primary): Connectivity & Platforms $19.8bn (−3.0% yoy: Residential −4.0%, Business Services +3.7%); Content & Experiences $10.7bn (+22.9%: Media +25.3%, Studios +25.0%, Theme Parks +2.7%). **Peacock reached its first-ever quarterly profit** ($189mn EBITDA) on 48mn paid subscribers (+2mn qoq); record 448,000 wireless line net adds (10.2mn total lines); residential broadband lost 167,000 customers, an improvement of 34,000 yoy but still a net loss. GAAP net income fell 68% yoy (Q2 2025's figure includes the Hulu gain); **adjusted EPS $1.04, down 16.7% yoy** — the GAAP/adjusted gap in Q2 2025 is entirely the Hulu one-off, not an earnings-quality issue in the current quarter.

## 5. Guidance track record
Comcast does not issue formal forward EPS/revenue guidance in its earnings releases (confirmed: no guidance in the Q2 2026 8-K exhibit). There is therefore no prior-range-versus-delivered comparison to make; the closest equivalent is the 29-Jun-2026 spin-off announcement itself, which set a ~12-month timeline to close — that timeline has not yet been tested against results.

## 6. Earnings quality & balance sheet
- **Net debt/EBITDA ≈ 2.3–2.4x.** Long-term debt + capital leases $84.26bn + current portion $6.12bn = $90.38bn total debt (10-Q, 30-Jun-2026); cash $7.66bn; net debt ≈ $82.7bn against TTM adjusted EBITDA in the mid-$30bns.
- **TTM (Q3'25–Q2'26) FCF ≈ $20.44bn** on TTM CFO $32.52bn − capex $12.07bn (independently re-derived from XBRL; matches v1_valuation.json's D3 TTM figures exactly, cross-check passed). **[Corrected 2026-10-06: this FCF is overstated. Comcast's own definition deducts cash paid for intangible assets as well as capital expenditures (Q2 2026 release: $4.6bn of free cash flow = OCF $8,092m - capex $2,902m - intangibles $587m). TTM cash paid for intangible assets is $2,627m (XBRL: 677 + 724 + 639 + 587), so TTM FCF is $17.82bn, not $20.44bn; after TTM SBC of $1,371m (311 + 274 + 427 + 359; V1 used the FY2025 $1,289m and added it back through OCF) it is $16.45bn. Q3-Q4 2025 also include Versant (spun 2 Jan 2026), so a FY2026E run-rate (H1 2026 OCF $14,983m, capex $5,253m, intangibles $1,226m scaled by the FY2025 seasonal split, less SBC) is about $14.8bn. Net debt of $82.7bn is not needed on the equity-value method used in the re-assessment. See Re-assessment (RA10).]** FCF/NI is not meaningful on a simple TTM basis because TTM NI ($11.2bn) spans quarters distorted by the Hulu gain's absence and Versant separation costs; on an adjusted-earnings basis conversion is healthy.
- **Q4 2025 and Q1 2026 operating income dropped sharply** (to ~$3.49bn and $4.14bn from a normal $5.5–6.6bn run-rate) — this coincides exactly with the **1-Jan/2-Jan-2026 completion of the Versant spin-off** (cable networks USA, MS NOW [renamed from MSNBC], CNBC, Golf Channel, E!, SYFY, Oxygen), which removed a high-margin earnings stream and layered on one-time separation costs. Reported figures from Q1 2026 onward are Comcast **ex-Versant**; the modest yoy revenue growth despite losing that business implies the comparative periods have been restated to a continuing-operations basis.
- Capital return: Q2 2026 buybacks $900mn + dividends $1.2bn; **no share repurchases after 29-Jun-2026 pending the NBCUniversal/Sky separation** — capital return is paused mid-transaction, a real near-term drag on the buyback-driven part of the bull case.
- Minority interest is immaterial (~$0.19bn).

## 7. Valuation — reconciled against V1 (`v1_valuation_table.csv` / `v1_valuation.json`)
**V1 verdict: attractive (score 0.96/1.00).** V1's reverse FCFF DCF (WACC 6.05%, 10-year fade to 3% terminal, EV $154.8bn) finds the price implies **FCF shrinking at −24.2%/year for 10 years** — versus a 5-year delivered CAGR of +2.8% and a 10-year delivered CAGR of +5.1%. **[Corrected 2026-10-06: V1's WACC of 6.05% (beta 0.74, ERP 4.14%, net debt $76.6bn) was applied to a levered FCF (OCF is after interest), which mixes enterprise value with an equity cash flow, and excluded $2.6bn of cash paid for intangible assets and SBC. Recomputed on equity value $77.75bn (3,539.2m Class A + 9.4m Class B shares at 15 Jul 2026 x $21.91), cost of equity 5.17% + 0.8 x 4.8% = 9.0% (beta floored at 0.8), terminal growth 2%: implied FCF growth for 10 years is -14.1% on $16.45bn (-15.3% on $17.82bn before SBC; -12.5% on FY2026E $14.8bn; -9.6% on owner FCF of $12.3bn = net income + D&A - capex - intangibles, which strips a $4.2bn working-capital and deferred-tax inflow), against a base of 0% to +3%. implied_vs_base stays below. V1's +62.1% base return rested on an exit P/E of 17.2x against 6.2x today and is retired in favour of the RA10 scenarios. See Re-assessment (RA10).]** V1's scenarios: **bear +24.2%/yr, base +62.1%/yr, bull +89.5%/yr** (3-yr annualised, including dividends), driven mostly by multiple re-rating (exit P/E 10.0x/17.2x/20.2x vs today's 6.2x) rather than by growth assumptions alone.
**I agree with the direction (cheap; implied growth is far below any reasonable base case) but not the magnitude.** My own base case: low-single-digit FCF growth (0% to +3%/year) — Residential Connectivity is genuinely shrinking (−4.0% yoy) but Business Services (+3.7%), wireless (record adds), and the higher-margin, faster-growing Content & Experiences segment (+22.9%) are real, disclosed offsets. That is still dramatically above the priced-in −24%/year, so **implied_vs_base = below**, supporting inclusion — but V1's base/bull cases require the market to re-rate the P/E to 17–20x, which depends heavily on the NBCUniversal/Sky spin-off actually closing on favorable terms (clean investment-grade balance sheets for both entities, as management has stated as a goal but not yet delivered). A re-rating case is less certain than a pure cash-flow case, which is why I size this INCLUDE-SMALL rather than full INCLUDE.

## 8. Bull case
1. Valuation is priced for a level of FCF decline (−16% to −24%/yr) that is far worse than anything Comcast has delivered even during the worst of cord-cutting (5y CAGR still +2.8%), leaving a large margin of safety if the business merely does not shrink. **[Corrected 2026-10-06: the priced-in decline is 9-14% a year, not 16-24% (see section 7 correction). The margin of safety remains large: base-path value at 9.0% is $54 a share at 0% FCF growth on FY2026E FCF less SBC ($14.8bn), $43 at -4% and $61 at +2%, against $21.91.]**
2. The NBCUniversal/Sky spin-off is a disclosed, dated catalyst that management frames as unlocking two focused, investment-grade companies — sum-of-the-parts is a plausible re-rating path given the conglomerate discount visible in the 6.2x multiple today.
3. Wireless (record 448,000 adds) and Peacock (first profitable quarter) are genuinely inflecting positive at the same time broadband erosion is *decelerating* (−167k vs −201k a year ago), i.e., the offsets are strengthening, not just theoretical.

## Bear case
1. Residential broadband is still losing subscribers every quarter with no evidence of an inflection to growth — this is the core cash-generating asset and the secular decline (fixed wireless, cord-cutting) is real and ongoing.
2. The spin-off is announced but unexecuted: terms for splitting debt, the size/duration of Comcast's retained NBCUniversal stake, and each entity's dividend policy are all undecided as of this writing, and buybacks are already paused — a live example of the process constraining shareholder returns before it delivers any benefit.
3. Q4 2025/Q1 2026 already show what separation costs and losing a profitable segment (Versant) look like in the numbers; the NBCUniversal/Sky separation is a much larger transaction and could produce a similar, or larger, transitional earnings air-pocket.

## 9. Key risks & kill criteria (thesis-invalidation triggers)
1. The NBCUniversal/Sky spin-off is delayed beyond Q4 2027 (18+ months from announcement) or is restructured so either resulting entity is sub-investment-grade.
2. Residential broadband net losses exceed 250,000 in any quarter (vs. −167,000 in Q2 2026), i.e., the recent deceleration reverses.
3. Net debt/EBITDA rises above 3.0x ahead of the spin (from ~2.3–2.4x now), suggesting the balance sheet is being loaded to fund the separation.
4. Wireless net adds fall below 300,000/quarter (from 448,000 record in Q2 2026), removing the main offset to broadband erosion.
5. The dividend is cut or suspended in connection with the spin-off.

## 10. Catalysts & calendar
Next earnings: **22-Oct-2026** (Q3 2026, per company IR release). NBCUniversal/Sky separation: targeted close ~mid-2027 (12 months from 29-Jun-2026 announcement); watch for the Form 10/S-1-type separation filing and capital-structure disclosure, expected before close. **[Corrected 2026-10-06: items missed. (1) 29 Jun 2026 8-K (accession 0000950103-26-009591): Mike Cavanagh will be CEO of NBCUniversal and Comcast's former CFO Michael Angelakis will become CEO of Comcast after the separation (Brian Roberts remains involved in both). (2) June 2026 cash tender offers for 2027-2030 notes, consideration cap raised from $3.75bn to $4.14bn (8-Ks 27 May, 2 Jun, 3 Jun; 0000950103-26-007759, -008329, -008429): debt reduction, total debt $90.4bn at 30 Jun vs $98.9bn at 31 Dec. (3) S-4 of 30 Jul 2026 (0001193125-26-326101; effective 7 Aug, 424B3): a registered exchange of up to $1,172,013,000 of 5.168% Notes due 2037 for the unregistered notes issued in October 2025 exchanges; not a merger. (4) Form 25 on 14 Sep 2026 (0001354457-26-000874, text not read). No guidance, merger agreement or rating action found. See Re-assessment (RA10).]**

## 11. Red-flag scan
No auditor changes, restatements or going-concern language identified in this review window. No SEC/DOJ investigation or short-seller report surfaced in this search window (not exhaustively verified against the full 10-K legal-proceedings note — treat as a scope limitation, not a clean bill of health). **Data/model gap flagged for the lead:** `b1_live_scores.csv`'s `exclude_pending_deal` flag is **False** for CMCSA even though a major, dated corporate separation was announced 29-Jun-2026 and is disclosed in the Q2 2026 10-Q; the pending-deal exclusion in the quant pipeline appears scoped to M&A/buyout situations only, not self-initiated spin-offs — worth confirming with the B1 team.

## Data quality note, recency and disclaimer
All figures are on a **consolidated** basis (Comcast Corporation and subsidiaries; no standalone/parent-only statements used). Most recent period incorporated: Q2 2026 10-Q (quarter ended 30-Jun-2026, filed 23-Jul-2026) and the Q2 2026 earnings release (8-K, same date). Events checked to 2026-09-25 close, including the 29-Jun-2026 spin-off announcement. GAAP figures are labeled GAAP; adjusted EPS is labeled adjusted; Q4 2024/Q4 2025 figures are marked "derived" (annual 10-K total minus 9-month 10-Q YTD) because no company-published quarterly figure for those periods was directly sourced in this review. This is research, not personalised investment advice, and not a recommendation to buy or sell; the reader is responsible for their own decisions.

## 12. Sources
1. CMCSA companyfacts (XBRL) — https://data.sec.gov/api/xbrl/companyfacts/CIK0001166691.json
2. CMCSA Q2 2026 8-K earnings exhibit — https://www.sec.gov/Archives/edgar/data/0001166691/000162828026049274/ex991-6302026.htm
3. CMCSA FY2025 10-K — https://www.sec.gov/Archives/edgar/data/1166691/000162828026004994/cmcsa-20251231.htm
4. CMCSA Q2 2026 10-Q — https://www.sec.gov/Archives/edgar/data/0001166691/000162828026049360/cmcsa-20260630.htm
5. CNBC — "Comcast announces it will spin off NBCUniversal and Sky" (29-Jun-2026) — https://www.cnbc.com/2026/06/29/comcast-announces-it-will-spin-off-media-and-tech-wings-into-separate-public-companies.html
6. Comcast IR press release — spin-off announcement — https://www.cmcsa.com/news-releases/news-release-details/comcast-announces-plans-separate-media-and-technology-businesses
7. NewscastStudio — Versant spin-off completed 2/5-Jan-2026 — https://www.newscaststudio.com/2026/01/05/versant-ipo/
8. Deadline / Yahoo Finance — Q2 2026 earnings coverage (Peacock profitability, wireless adds) — https://deadline.com/2026/07/comcast-q2-earnings-peacock-subscribers-1237000945/
9. Comcast Q3 2026 earnings-date announcement — https://www.stocktitan.net/news/CMCSA/comcast-to-host-third-quarter-2026-earnings-conference-78xtj642sbj7.html
10. v4 systematic valuation — `v4/outputs/v1_valuation_table.csv`, `v4/outputs/v1_valuation.json` (CMCSA row)
11. v4 quant context — `v4/data/b1_live_scores.csv` (CMCSA row)


---
## Re-assessment (RA10, 2026-10-06)
Data cutoff for filings: 2026-10-06 (EDGAR submissions checked for every ticker). Prices and share counts are the 25 Sep 2026 values in the dossier / d4 snapshot unless stated. Discount-rate convention for RA10: 10-year Treasury 5.17% (FRED DGS10, 25 Sep 2026; 5.28% on 2 Oct) plus an equity risk premium of 4.8% (assumption) times beta, where beta is the Blume-adjusted 5-year beta floored at 0.8 (raw betas of 0.15-0.6 understate risk when the 10-year yield is 5.17%). V1 used an ERP of 4.14% and unfloored betas. Research only; not personal advice.

**Result: verdict INCLUDE-SMALL kept; implied_vs_base below -> below (implied FCF decline restated from -24% to -14% a year); scenario returns restated (bear -5.8% / base +8.7% / bull +22.4%, was +24.2% / +62.1% / +89.5%); confidence text corrected.** Original text above is unchanged except for inline **[Corrected 2026-10-06: ...]** markers.

**Recency (EDGAR, 23 Jul to 6 Oct 2026).** No 8-K, 10-Q or 10-K after the Q2 8-K and 10-Q of 23 Jul 2026 (0001628280-26-049274, -049360). Filed since: S-4 30 Jul (0001193125-26-326101) with 424B3 and EFFECT on 7 Aug (registered exchange for $1.172bn of 5.168% Notes due 2037); Form 25 on 14 Sep (0001354457-26-000874); Schedule 13G/A 12 Aug (routine); Forms 4 on 18 Aug, 3 Sep and five on 2 Oct (directors Baltimore, Brady, Breen, Honickman, Smith; transaction detail not tabulated). Earlier 2026 items: 8-K 29 Jun (spin-off announcement and CEO succession, 0000950103-26-009591), debt tender offers 27 May-3 Jun, 8-K 12 Jun (Item 5.07). No merger agreement, rating action or guidance (Comcast gives none). Next report 22 Oct 2026 (company IR release per dossier, not re-verified in a filing).

### Claims verified
| Claim | Status | Source |
|---|---|---|
| Spin-off of NBCUniversal and Sky announced 29 Jun 2026, tax-free, completion in about one year | CONFIRMED | 8-K Ex-99.1 (0000950103-26-009591) |
| Q2 2026: wireless line net adds 448,000 record, residential broadband -167,000, Peacock EBITDA $189m | CONFIRMED as dossier / release values (headline items in Ex-99.1, not re-tabulated) | Q2 release (0001628280-26-049274) |
| TTM CFO $32.52bn; capex $12.07bn; TTM FCF $20.44bn | CFO and capex CONFIRMED; FCF WRONG basis | XBRL OCF 8,693 + 8,841 + 6,891 + 8,092 = 32,517; PaymentsToAcquirePropertyPlantAndEquipment 3,071 + 3,749 + 2,351 + 2,902 = 12,073; omits cash paid for intangible assets 2,627 |
| Q2 FCF per the company $4.6bn | CONFIRMED | release: OCF 8,092 - capex 2,902 - intangibles 587 = 4,603 |
| Total debt $90.38bn at 30 Jun 2026; cash $7.66bn | CONFIRMED | 10-Q debt table ($90.4bn vs $98.9bn at Dec); XBRL cash 7,661 |
| SBC | WRONG year | TTM $1,371m (V1 used FY2025 $1,288m) |
| Quarterly dividends about $1.2bn; buybacks $0.9bn in Q2, none after 29 Jun | CONFIRMED | XBRL PaymentsOfDividends 1,184 (Q2); release 'returned $2.1 billion' |
| V1 WACC 6.05% for a reverse DCF on levered FCF | WRONG method | levered FCF needs equity value and a cost of equity |
| 'Priced-in FCF decline of 16-24% a year' | WRONG magnitude | recomputed -9.6% to -15.3% (see below) |
| No formal guidance | CONFIRMED | release has none |
| 10-year Treasury 5.17% on 25 Sep 2026 | CONFIRMED | FRED DGS10 fetched 6 Oct |

### Valuation recomputed (own arithmetic)
Equity value $77.75bn = 3,548.6m shares (10-Q cover, 15 Jul 2026) x $21.91. Cash flow to equity (OCF is after interest and tax): OCF - capex - cash paid for intangible assets - SBC. Cost of equity 9.0% (Blume beta 0.74, floored at 0.8; stress 8.2% and 10.0%); terminal growth 2%; 10 years.

| Cash flow base | $bn | implied 10-yr FCF growth at COE 8.2% / 9.0% / 10.0% |
|---|---|---|
| V1 as used (before intangibles, SBC added back) | 20.44 | -18.7% / -17.6% / -16.3% |
| TTM OCF - capex - intangibles | 17.82 | -16.5% / -15.3% / -14.0% |
| TTM less SBC (central) | 16.45 | -15.3% / -14.1% / -12.7% |
| FY2026E ex-Versant, less SBC (own estimate) | 14.81 | -13.7% / -12.5% / -11.0% |
| Owner FCF (NI + D&A - capex - intangibles) | 12.26 | -10.9% / -9.6% / -8.1% |

Base case 0% to +3% a year (Residential Connectivity -4%, Business Services +3.7%, wireless record adds, Content & Experiences +22.9%, Peacock profitable), but with the spin-off, a possible earnings air-pocket and no buyback until it closes; even a -4% path is worth $43 a share at 9.0% on $14.8bn, and a 0% path $54, against $21.91. Implied -9.6% to -14.1% is far below the base -> **below**. A cash-flow multiple this low (FCF after SBC yield 21%) also means the market doubts the cash flow itself (cable capex intensity, fiber and fixed-wireless competition, how debt and dividends are split at the spin), which is why the size stays half.

### Scenario arithmetic (3 years, per share)
NTM EPS $3.55 (V1 eps_ntm, 6.2x), dividend about $1.34 a share (Q2 dividends paid $1,184m / 3.55bn shares). Base: EPS -1% a year -> $3.45, exit 7.0x (6.2x now) = $24.1 plus dividends $4.0 -> **+8.7%** a year. Bear: EPS -6% a year (broadband losses accelerate, separation costs and dis-synergies) -> $2.95, 5.0x = $14.8 plus $3.6 (dividend cut in year 3) -> **-5.8%**. Bull: EPS +4% a year -> $4.00, 9.0x = $36.0 plus $4.2 -> **+22.4%**. V1's bear / base / bull of +24.2% / +62.1% / +89.5% needed exit multiples of 10x / 17x / 20x and are retired.

**Verdict: INCLUDE-SMALL (unchanged).** The margin of safety survives the corrected method (priced-in decline of about 10-14% a year against a 0-3% base; base 3-year return +8.7% a year, above the 5.17% Treasury), but the spin-off is unexecuted, buybacks are paused and the cash flow is heavily discounted by the market, so half weight. No kill criterion has fired (wireless adds 448,000, broadband losses 167,000, dividend intact, net debt/EBITDA about 2.3-2.4x).
