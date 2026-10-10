# NRG Energy, Inc. (NRG) — Diligence Dossier

**Agent:** F50 · Wave 3 · Standard depth · **As of:** 2026-09-25 close ($100.37/share; mkt cap ≈$21.1bn per `v4/data/b1_live_scores.csv`)

## 1. Verdict
**INCLUDE-SMALL** (half weight). Thesis horizon 24–36 months. Real, primary-source-confirmed earnings growth from the LS Power acquisition and hyperscaler data-center deals, and a clean guidance record — but leverage is genuinely high post-acquisition, quarterly GAAP earnings are extremely volatile (mark-to-market swings of $600m+ quarter to quarter), and the market-implied valuation on the more reliable EV/EBITDA basis is not obviously cheap once leverage is accounted for, contrary to the triage's "sold off to 9.5x, cheap" framing.

## 2. Business in plain English
NRG is a merchant power generator and retail electricity/energy-services provider, with fleets concentrated in Texas (ERCOT) and, since closing the LS Power acquisition on 2026-01-30, a much larger footprint of natural-gas and dual-fuel generation across the eastern U.S. It earns money from wholesale energy sales, capacity payments, and retail electricity/gas supply contracts with residential and business customers; unlike a regulated utility, its prices are set by competitive/auction markets (ERCOT energy prices, PJM/other capacity auctions), not a rate case.

## 3. Why the model likes it / is it durable
Q15 triage scored NRG quality 3, growth 5, price_vs_growth 4, and flagged the leverage issue explicitly: "Net debt/EBITDA ~7.2x is elevated... leverage is the real thing to underwrite in full diligence." b1 factor data shows NRG in the top decile for several quality/value percentiles but with `pct_leverage`=0.017 (very poor leverage percentile — consistent with the triage flag) and elevated `vol_1y` (49%). The 2026 EBITDA growth is real and primary-source-confirmed (LS Power added a 13 GW gas/dual-fuel portfolio plus CPower on 2026-01-30; East-segment Adjusted EBITDA growth of $370m in Q2'26 alone was attributed to it in the earnings release) — this is not an accounting artefact. **However, I partially overturn the triage's specific leverage number**: using the company's own reported consolidated balance sheet (see §6), I compute net debt/EBITDA at ~5.3x trailing and ~4.2x on the FY26 guidance midpoint, not 7.2x. The direction of the triage's concern (leverage is elevated and integration risk is real) is confirmed; the specific magnitude is not, and I flag this as a **data conflict** to be resolved with a full-cycle EBITDA figure once LS Power's first full year is reported.

## 4. Last two years of results (consolidated GAAP; source: XBRL companyfacts CIK0001013871 and 10-Qs/10-K/earnings releases)
| Quarter | Revenue ($m) | Op. income ($m) | GAAP net income ($m) | GAAP diluted EPS | Adjusted EBITDA ($m) | Adjusted EPS |
|---|---|---|---|---|---|---|
| Q3'24 | 7,127 | (812) | (767) | ($3.79) | 1,055 | n/a |
| FY24 total | 27,748 | 2,424 | 1,125 | $4.99 | n/a | n/a |
| Q1'25 | 8,489 | 1,134 | 750 | $3.61 | 1,126 | n/a |
| Q2'25 | 6,673 | 0 | (104) | ($0.62) | 909 | $1.73 |
| Q3'25 | 7,503 | 414 | 152 | $0.69 | 1,205 | n/a |
| FY25 total | 30,347 | 1,845 | 864 | $4.01 | **4,087** | **$8.24** |
| Q1'26 | 10,136 | 328 | 125 | $0.52 | 1,080 | n/a |
| Q2'26 | 7,319 | 976 | 506 | $2.31 | 1,217 | $1.49 |

GAAP net income and EPS swing heavily quarter to quarter (e.g., Q2'25 loss vs Q2'26 $506m profit, a $610m swing) — company attributes this primarily to unrealized, non-cash mark-to-market changes on economic/commodity hedges, which is a genuine sector feature (see the utilities-power playbook: merchant generation earnings are a "strip of spread options"), not obviously an earnings-quality problem, but it makes GAAP EPS a poor quarter-to-quarter signal — adjusted EBITDA and adjusted EPS are the more informative series and are used throughout this dossier, clearly labelled.

## 5. Guidance track record (last 4 releases, exact dates from earnings-release exhibits)
1. **Q3'25 (filed 2025-11-06):** reaffirmed a guidance range that had been **raised on 2025-09-17** — Adj. EBITDA $3,875–4,025m, Adj. EPS $7.55–8.15, FCFbG $2,100–2,250m (FY25 basis, pre-LS Power).
2. **Q4/FY25 (filed 2026-02-24):** FY25 actual Adj. EBITDA $4,087m (above the raised range), Adj. EPS $8.24 (above range), FCFbG $2,210m (within range) — **guidance beaten**. Initial FY26 guidance (reflecting ~11 months of LS Power ownership): Adj. EBITDA $5,325–5,825m, Adj. EPS $7.90–9.90, FCFbG $2,800–3,300m.
3. **Q1'26 (filed 2026-05-06):** reaffirmed FY26 guidance unchanged — **maintained**.
4. **Q2'26 (filed 2026-08-04):** reaffirmed FY26 guidance unchanged — **maintained**.

No cut across four releases; the FY25 raise was delivered. The wide FY26 Adj. EPS range ($7.90–$9.90, ±11% around the midpoint) itself signals real integration/hedging uncertainty that a point verdict should not paper over.

## 6. Earnings quality & balance sheet
- **Entity scope:** all figures are **NRG Energy, Inc. consolidated** (Q2'26 10-Q balance sheet, filed 2026-08-04, accession 0001013871-26-000020). No holdco/subsidiary split was required to be checked because NRG does not present a separately-regulated subsidiary balance sheet in this filing (unlike XEL).
- **Leverage:** consolidated total debt (`LongTermDebt` XBRL tag, includes current portion) = **$23,392m** at 2026-06-30 (up from $9,812m at 2025-06-30 and $16,412m at 2025-12-31 **[Corrected 2026-10-08: comparators mixed: $9,812m and $16,412m are NON-CURRENT debt, while $23,392m is the total-debt XBRL tag; like-for-like total debt (balance sheet, incl. current and finance leases) is $23,256m at 30 Jun 2026 vs $16,443m at 31 Dec 2025]** — the LS Power close on 2026-01-30 drove the step-up); cash = $162m. Net debt ≈ **$23.23bn**. TTM adjusted EBITDA (Q3'25 $1,205m + FY25-implied Q4'25 $1,706m **[Corrected 2026-10-08: arithmetic slip: FY25 $4,087m less $3,240m is $847m (Q4/FY25 release acc 0001013871-26-000002 shows Q4 Adjusted EBITDA $847m); the stated TTM total of about $4,348m already reflects $847m]** [FY25 total $4,087m less Q1–Q3'25 $1,126+909+1,205=$3,240m] + Q1'26 $1,080m + Q2'26 $1,217m) ≈ **$4,348m** (LS Power only partially reflected — it closed mid-quarter). **Net debt/adjusted EBITDA (TTM) ≈ 5.3x**; on the FY26 guidance midpoint ($5,575m, reflecting a fuller year of LS Power) ≈ **4.2x**. Both are materially below the triage's cited 7.2x. Company itself discloses no leverage ratio or target/timeline in the Q2'26 release or 10-Q excerpt reviewed — a genuine information gap on NRG's side, not just this dossier's.
- **LS Power financing:** $4.9bn of debt issued (Oct-2025) ahead of the Jan-2026 close; a further $2.6bn debt refinancing completed late-April 2026 ("more than $10m of annual interest savings," ~$1.0bn shifted from secured to unsecured) — company financed the acquisition almost entirely with new debt, consistent with the leverage jump above.
- Liquidity fell from $9.6bn (year-end 2025) to $3.3bn (Q1'26) to $5.3bn (Q2'26) as acquisition cash was deployed and then partially rebuilt — a real, if temporary, liquidity compression worth watching through the LS Power integration period.
- Share buybacks: $1.0bn planned for 2026, $932m completed through 2026-07-31; dividend ~$407m planned for 2026, Q3'26 dividend $0.475/share declared 2026-07-22 (implies $1.90/yr annualized).
- No material weakness, restatement or auditor change found in the sections of the Q2'26 10-Q reviewed; a Sierra Club v. Midwest Generation LLC (2019) environmental matter and a settled (2026-04-16) New York PSC matter are referenced in the filing's legal-proceedings tags, but the narrative text describing materiality was not fully retrievable in this pass — **disclosed as a limitation**, not asserted as clean.

## 7. Valuation snapshot and reconciliation with V1
No V1 row exists for NRG in `v4/outputs/v1_valuation_table.csv` (checked directly, absent) → **v1_verdict = null**.
- Headline P/E on FY26 guided Adj. EPS midpoint ($8.90): **11.3x** — this is the number that makes NRG look cheap in the triage note ("9.5x NTM," computed off a different, presumably lower, consensus estimate).
- **EV/EBITDA (the more reliable metric for a leveraged merchant generator per the sector playbook):** EV = mkt cap $21.1bn + net debt $23.23bn = **$44.33bn**; FY26 guided Adj. EBITDA midpoint $5,575m → **EV/EBITDA ≈ 7.95x**. The utilities-power playbook's indicative merchant-generation band is 4–7x on **mid-cycle** spreads; NRG at ~8x sits above that band, implying the market is already paying for continued (not mid-cycle-average) capacity prices and successful data-center monetization, not for a distressed sell-off. This is the opposite of "cheap at 9.5x" — **on a leverage-adjusted basis NRG is fully, not cheaply, priced**.
- **Reverse DCF (EPS-based, given no V1 row):** **[Corrected 2026-10-08: not a cash-flow DCF (EPS and an exit P/E are not free cash flow); see Correction section for the programme-method recompute]** solving for the EPS growth rate that justifies $100.37 at an 11x exit P/E (current) over 3 years from the $8.90 FY26 EPS midpoint requires roughly 0% further growth already (11.3x current multiple ≈ 11x assumed exit), i.e., the current price is broadly consistent with EBITDA/EPS growth flattening near-term while integration completes — but management's own stated "Adj. EPS growth rate target of 14%+ through 2030" (Q4/FY25 release) is well above what a flat-multiple 3-year hold requires, suggesting genuine additional upside IF that target is delivered and IF the multiple does not compress further from leverage concerns.
- valuation_view_vs_v1.implied_vs_base = **"in_line"** (not clearly cheap on EV/EBITDA; not clearly expensive relative to management's own long-term growth target; net assessment is that the market is pricing execution risk fairly, not gifting a bargain).

## 8. Bull case / Bear case
**Bull:** (1) LS Power closing (2026-01-30, 13 GW gas/dual-fuel + CPower, primary-source-confirmed) materially diversifies NRG beyond ERCOT and is already contributing (+$370m East Adjusted EBITDA in Q2'26 alone); (2) a "Bring Your Own Power" 1.2 GW combined-cycle gas deal with an unnamed hyperscaler has agreed "principal commercial terms" (Q2'26 release) — real, near-term optionality not yet in guidance; (3) FY25 guidance was raised (Sept-2025) and then beaten, and FY26 guidance has been maintained twice since — a clean recent track record.

**Bear:** (1) Consolidated leverage is genuinely elevated post-LS Power (net debt/EBITDA ≈4.2–5.3x on my own compute, still well above pre-deal levels even if below the triage's 7.2x claim), and the company discloses no explicit deleveraging target or timeline in the materials reviewed — an information gap, not just a risk; (2) FY26 Adjusted EPS guidance spans $7.90–$9.90, an unusually wide ±11% band for a "reaffirmed" outlook, signalling real integration/hedging uncertainty rather than high confidence; (3) GAAP earnings are extremely volatile quarter to quarter on mark-to-market swings (a $610m swing Q2'25→Q2'26), which will make it hard to judge underlying progress until a full post-LS-Power year of adjusted results is reported.

## 9. Key risks & kill criteria (what would break the thesis / thesis-invalidation triggers)
1. FY26 Adjusted EBITDA guidance ($5,325–5,825m) cut at any release (currently reaffirmed twice since being set).
2. Net debt/Adjusted EBITDA (computed on total debt and TTM/guided EBITDA as in §6) rises above 6.0x at any quarter-end (currently ≈4.2–5.3x by this dossier's own compute).
3. Liquidity falls back below $3.0bn (was $3.3bn at Q1'26 trough) without a stated remediation plan.
4. The 1.2 GW hyperscaler "Bring Your Own Power" deal fails to reach final documentation within 12 months of the "principal terms agreed" disclosure (2026-08-04 release).
5. Two consecutive quarters of Adjusted EBITDA below the low end of whatever the then-current guidance range is.

## 10. Catalysts & calendar
Next quarterly earnings: Q3 2026, expected early-November 2026 (2025 pattern: filed 2025-11-06; not yet confirmed for 2026 as of 2026-09-25). Texas Energy Fund projects: two further TEF gas plants targeted for completion by mid-2028 (T.H. Wharton, 415 MW, already achieved commercial operations 2026-05-26). Full-year 2026 will be the first complete year including LS Power — a key data point for the leverage/integration thesis.

## 11. Red-flag scan
- **Leverage:** see §6 — genuinely elevated, data-conflict on the exact multiple vs. the triage's 7.2x figure (this dossier computes 4.2–5.3x from primary filings; recommend the lead reconcile which debt/EBITDA definition the triage used).
- **Litigation:** Sierra Club v. Midwest Generation LLC (2019, environmental) and a New York State PSC matter (settled 2026-04-16) appear in the Q2'26 10-Q's legal-proceedings XBRL tags; narrative detail on materiality was not fully retrievable in this pass — flagged as a limitation, follow up before sizing at full weight.
- No material weakness, restatement, or auditor change found in the sections reviewed.
- No PJM-specific capacity-price-cap discussion found in NRG's own Q2'26 release or the 10-Q sections reviewed (unlike Vistra, which explicitly discloses PJM auction clearing prices) — NRG's East capacity exposure and its sensitivity to the same PJM price-cap dynamics flagged for VST/NRG in the triage was **not independently confirmed for NRG** in the primary sources reviewed; treat the triage's "PJM price-cap fears" framing as unconfirmed for NRG specifically pending a closer read of the risk factors section.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q, period ended 2026-06-30, filed 2026-08-04 (accession 0001013871-26-000020); also FY2025 10-K (filed 2026-02-24) and Q2'26/Q1'26/Q4'25/Q3'25 earnings-release exhibits. Events checked to 2026-09-25. GAAP figures are labelled GAAP; Adjusted EBITDA/Adjusted EPS are the company's own non-GAAP measures, shown alongside GAAP where available. This is research, not personalized investment advice.

## Sources
1. SEC EDGAR submissions/companyfacts, CIK 0001013871, `data.sec.gov`, retrieved 2026-09-26.
2. NRG Q2 2026 10-Q, filed 2026-08-04, accession 0001013871-26-000020, `www.sec.gov/Archives/edgar/data/1013871/000101387126000020/nrg-20260630.htm`.
3. NRG Q2 2026 earnings release, `.../000101387126000018/nrgq22026ex991.htm`, filed 2026-08-04.
4. NRG Q1 2026 earnings release, `.../000101387126000010/nrgq12026ex991.htm`, filed 2026-05-06.
5. NRG Q4/FY2025 earnings release, `.../000101387126000002/ex991-q42025.htm`, filed 2026-02-24.
6. NRG Q3 2025 earnings release, `.../000101387125000023/nrgq32025ex991.htm`, filed 2025-11-06.
7. `v4/outputs/Q15_triage.json` (NRG entry) and `v4/data/b1_live_scores.csv` (row NRG), read 2026-09-26.
8. `v4/outputs/v1_valuation_table.csv` — checked, no NRG row present.

## Correction (verification DV30, 2026-10-08)

**1. Valuation method (s7).** The 'reverse DCF' solves for EPS growth at an 11x exit P/E and the in_line call rests on EV/EBITDA of 7.95x versus a 4-7x playbook band. That is a multiple test, not a free-cash-flow DCF with a stated discount rate (programme basis: 10-year Treasury 5.17% on 25 Sep 2026 plus beta x ERP; FCF after SBC). Recompute: 2026 FCFbG guidance midpoint $3,050m (Ex-99.1 acc 0001013871-26-000018) less SBC about $140m (FY25 $134m, 10-K) = $2.91bn on a $21.1bn market cap (13.8% yield); with cost of equity 9.3-10.6% (beta 1.0-1.3 x 4.14%) and terminal growth 3% the price implies FCF growth of -6% to -8%/yr for ten years, i.e. 'below' any base. But FCFbG is before growth investments, the guide is back-end loaded (H1-26 FCFbG $959m, 31% of the midpoint; H2 needs $1.8-2.3bn), and trailing GAAP cash flow after capex is only about $0.35bn (TTM operating cash flow 1,555 = 1,913 - 1,306 + 948; capex 1,207 = 1,147 - 595 + 655). On a $1.5bn FCF haircut the implied growth is +1% to +3%. Result: the programme-method answer ranges from clearly below to above depending on the cash-flow definition, so implied_vs_base cannot be established from the dossier's evidence and 'in_line' is left as the conservative label; **verdict INCLUDE-SMALL unchanged**, with low confidence in the valuation leg. No summary file changed.

**2. TTM EBITDA arithmetic.** Q4'25 Adjusted EBITDA was $847m, not $1,706m (the dossier's bracket); the TTM total of about $4,348m (net debt/EBITDA 5.3x) is right.

**3. Debt comparatives.** $23,392m is the total-debt XBRL tag; the $9,812m and $16,412m comparators are non-current balances. On the balance sheet: current portion $1,512m plus long-term debt and finance leases $21,744m = $23,256m at 30 Jun 2026 versus $31m + $16,412m = $16,443m at 31 Dec 2025. Net debt about $23.1bn; leverage conclusions unchanged.

**4. Revenue label.** The s4 'Revenue' column is revenue from contracts with customers (Q2-26 $7,319m; Q1-26 $10,136m); total revenue including derivative and other items is $7,481m (Q2-25 $6,740m) and $10,256m (Q1-26) in the release and 10-Q. Adjusted EPS fell to $1.49 from $1.73 in Q2 and to $2.98 from $4.42 in H1 (interest and D&A from LS Power); the FY26 guide midpoint ($8.90) needs H2 adjusted EPS of about $5.9 and Adjusted EBITDA of about $3.3bn against H1 $2.3bn, a back-end loading the dossier does not discuss.
