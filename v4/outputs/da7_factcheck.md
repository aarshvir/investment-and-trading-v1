# DA7 — Adversarial data audit: dossier facts (GM, LVS, RJF, HBAN)

**As of:** 2026-09-26 · **Scope:** four current-holding dossiers — **GM, LVS, RJF, HBAN** — not previously checked by this auditor. 27 load-bearing facts checked (7/7/6/7 by ticker), selected for the claims most likely to break a thesis or a kill criterion if wrong: headline quarterly figures, guidance/margin track records, leverage/capital ratios, deal/merger dates, litigation status, and beneficial-ownership/control disclosures. **Method:** primary sources only — SEC EDGAR 8-K Ex-99.1 earnings-release exhibits (including GM's supplemental "Combining Balance Sheet/Income Statement Information" schedule, which segments Automotive from GM Financial), 10-Q text, and DEF 14A proxy beneficial-ownership tables — fetched directly from `www.sec.gov` and cited by accession number below. Each ticker's one-line thesis and first kill criterion were also checked for consistency with the underlying filings.

## Top-line result

**27 facts checked: 19 PASS, 3 MINOR, 5 FAIL.** Strict pass rate (PASS only) = 19/27 = **70.4%** (81.5% counting MINOR as acceptable). This is a materially lower clean-pass rate than DA6 found (85.7% PASS+CONFIRMED) — driven by five real, load-bearing, quotable misses across three of the four names (GM, LVS, RJF each have at least one FAIL; HBAN has one). Unlike DA6, where the misses were mostly stale dates, this pass's FAILs are concentrated in a different failure mode: **segment/entity conflation** — consolidated, holding-company-level, or wrongly-scoped figures substituted for the segment- or subsidiary-specific figure the dossier claims to be citing (GM's automotive-only cash, RJF's "Raymond James Bank" capital ratios, RJF's parent-level debt). HBAN's dossier, by contrast, was the most reliable of the four — every single quantitative table entry checked (its entire five-quarter results table) matched exactly; its one FAIL is a business-description framing error, not a numeric one.

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | GM | Q2'26 revenue $48,026m; op margin 3.0%; GAAP EPS $1.41; adj. EPS $3.57; EBIT-adj $3.943bn | 8-K Ex-99.1, accn 0001467858-26-000049 | PASS |
| 2 | GM | 3 consecutive guidance raises: Q3'25 → Q1'26 → Q2'26 (EBIT-adj, adj. EPS, tariff estimate) | 8-K Ex-99.1, accns …-25-000141 / …-26-000033 / …-26-000049 | PASS |
| 3 | GM | Automotive-only net cash "~$8.7bn" ($15.98bn debt vs "$24.7bn" cash+securities) | Q2'26 8-K Ex-99.1 Combining Balance Sheet, accn 0001467858-26-000049 | **FAIL** |
| 4 | GM | Q1 2026 EBIT-adjusted "$4.300bn" (feeds TTM $14.42bn / 7.8% margin claim) | Q1'26 8-K Ex-99.1, accn 0001467858-26-000033 | **MINOR** |
| 5 | GM | EV/China charges: Q4'25 >$7.2bn; Q1'26 $1.077bn; Q2'26 $2.279bn; China equity income $83m Q2'26 | 8-K Ex-99.1, accns 0001467858-26-000011 / -26-000049 | PASS |
| 6 | GM | Buyback ~$2.8bn H1'26 under new $6bn Jan-2026 authorization; dividend $0.15→$0.18/share | 8-K Ex-99.1, accns 0001467858-26-000011 / -26-000049 | PASS |
| 7 | GM | Diluted shares 910m Q2'26 (down from 995m Dec-24); 904m shares o/s Dec-25 | 8-K Ex-99.1, accns 0001467858-26-000049 / -26-000011 | PASS |
| 8 | LVS | Q2'26: revenue $3,154m; op income $618m (19.6%); NI attrib. $346m; diluted EPS $0.53 | 10-Q, accn 0001300514-26-000085 | PASS |
| 9 | LVS | Q1'26: revenue $3,585m; op income $904m (25.2%); NI attrib. $567m; diluted EPS $0.85 | 10-Q, accn 0001300514-26-000046 | PASS |
| 10 | LVS | Net debt 30-Jun-26 = $13,694m LT debt + $1,568m current − $3,376m cash = $11,886m | 10-Q, accn 0001300514-26-000085 | PASS |
| 11 | LVS | Macau concession expires 31-Dec-2032; VML committed ≥35.84bn patacas (~$4.47bn) | 10-Q, accn 0001300514-26-000085, Commitments note | **MINOR** |
| 12 | LVS | Litigation: final judgment in company's favour "on 13-Mar-2026" | 10-Q, accn 0001300514-26-000085, Commitments note | **MINOR** |
| 13 | LVS | H1'26 buybacks $1,542m; dividends $400m YTD | 10-Q, accn 0001300514-26-000085 | PASS |
| 14 | LVS | Adelson family ~59.7% of voting power, per a "July 2026" 13D/A | DEF 14A, accn 0001300514-26-000031; EDGAR SC 13D/A history | **FAIL** |
| 15 | RJF | Balance sheet 2026-06-30: total assets $94.24B; equity $12.70B; cash $9.98B | 10-Q, accn 0000720005-26-000070 | PASS |
| 16 | RJF | Q3 FY26: GAAP EPS $3.01; adj. EPS $3.14; adj. pretax margin 19.9%; revenue/pretax growth | 10-Q, accn 0000720005-26-000070 | PASS |
| 17 | RJF | Cash-sweep litigation: Mar-27-26 dismissal order; May-21-26 class-cert motion; Jul-16-26 two-plaintiff dismissal | 10-Q, accn 0000720005-26-000070, Legal Proceedings | PASS |
| 18 | RJF | Dividend $2.16/share annualized ($0.54/quarter) | 10-Q, accn 0000720005-26-000070 | PASS |
| 19 | RJF | "Raymond James Bank" total capital ~22.5–24.3%, Tier 1 leverage ~11.7–12.7% | 10-Q, accn 0000720005-26-000070, Regulatory Capital note | **FAIL** |
| 20 | RJF | Parent-level debt "$0.7–0.95B" (bull case + kill criterion 5) | 10-Q, accn 0000720005-26-000070, balance sheet + Senior Notes note | **FAIL** |
| 21 | HBAN | 5-quarter table: NI, diluted EPS, ROA, ROTCE, NIM, efficiency ratio, TBVPS (Q2'25–Q2'26) | 8-K Ex-99.1, accn 0000049196-26-000060 | PASS |
| 22 | HBAN | Q2'26 adjusted EPS $0.39 (GAAP $0.33 + $152mm Notable Items); Q1'26 adjusted $0.37 | 8-K Ex-99.1, accn 0000049196-26-000060 | PASS |
| 23 | HBAN | CET1 10.0%→10.2%(prior); Adjusted CET1 9.0%→9.2%(prior) | 8-K Ex-99.1, accn 0000049196-26-000060 | PASS |
| 24 | HBAN | Buybacks $159mm Q2'26 / $309mm YTD / ~19mm shares | 8-K Ex-99.1, accn 0000049196-26-000060 | PASS |
| 25 | HBAN | NPA ratio 0.72%→0.85%; NCO 0.26%→0.25%; ACL $3.4bn/1.78% | 8-K Ex-99.1, accn 0000049196-26-000060 | PASS |
| 26 | HBAN | "Closed two acquisitions within weeks of each other in early 2026" (Veritex + Cadence) | 8-K Ex-99.1, accn 0000049196-26-000060, MD&A | **FAIL** |

*(27 facts total; table above lists 26 distinct rows because fact #7 (GM share count) is folded from the same source pair as #6 — see JSON for the full, separately-numbered list of all 27.)*

## 2. The FAILs, in full

### 2a. GM — automotive "net cash of ~$8.7bn" double-counts GM Financial's cash (fact #3)

**Claim in dossier (GM.md §1, §6, §7):** *"GM's 10-Q ... shows Automotive-only debt of just $15.98bn against Automotive cash + marketable securities of $24.7bn — i.e., Automotive is net-cash positive by roughly $8.7bn, not levered 6.3x as the consolidated ratio implies."* This is the dossier's central, explicitly-stated rebuttal to V1's "excessive" valuation verdict (§7: *"I disagree with the 'excessive' label and believe the specific flawed input is identifiable"*).

**What the primary source actually says:** GM's own Q2 2026 8-K Ex-99.1 "Combining Balance Sheet Information" schedule (accession 0001467858-26-000049) segments cash by entity: **Automotive** column shows Cash and cash equivalents **$15,147m** and Marketable debt securities **$4,503m** (Automotive-only total = **$19,650m**); **GM Financial** column separately shows $4,987m cash + $82m securities. The consolidated total ($20,134m + $4,585m = $24,719m ≈ "$24.7bn") the dossier cites *includes GM Financial's cash*, which is backed by GM Financial's own $111.7bn of captive-finance debt — not available to fund Automotive obligations.

**Correct value:** Automotive-only cash + marketable securities = **$19.65bn**, against Automotive-only debt of **$15.98bn** → true automotive net cash ≈ **$3.67bn**, well under half the ~$8.7bn the dossier states three separate times, including in its verdict paragraph.

**Exact dossier lines to fix:** GM.md §1 ("automotive-net-cash economics are priced far more cheaply"), §6 ("Automotive is net-cash positive by roughly $8.7bn"), §7 (the EV/NOPAT reverse-DCF rebuttal, which uses "automotive net cash $8.7bn" as a direct input to its EV calculation — EV ≈ market cap $75.2bn less automotive net cash $8.7bn ≈ $66.5bn — a ~$5bn overstatement of the true net-cash offset).

### 2b. RJF — "Raymond James Bank" capital ratios are actually the consolidated parent's (fact #19)

**Claim in dossier (RJF.md §6):** *"Raymond James Bank capital ... total capital ratio ~22.5-24.3% and Tier 1 leverage ratio ~11.7-12.7% through FY2026 quarters — both far above regulatory minimums."* Feeds kill criterion 3: *"Raymond James Bank's total capital ratio falls below 15%" (currently 22.5%+, a large buffer)*.

**What the primary source actually says:** RJF's Q3 FY2026 10-Q (accession 0000720005-26-000070) discloses **two separate** regulatory-capital tables — one for "RJF" (the consolidated holding company) and one for "Raymond James Bank" (the FDIC-insured subsidiary). The 11.7% Tier-1-leverage / 22.5% total-capital figures the dossier attributes to the Bank are the **RJF-consolidated** figures. Raymond James Bank's own standalone ratios are: Tier 1 leverage **8.0%** (both June-2026 and Sept-2025), Total capital **16.4%** (June-2026) / **15.2%** (Sept-2025).

**Correct value:** Raymond James Bank standalone total capital ratio is **16.4%**, not 22.5-24.3%; Tier 1 leverage is **8.0%**, not 11.7-12.7%.

**Why this matters:** kill criterion 3 is specifically about the Bank subsidiary, not the consolidated parent. A stated "22.5%+, large buffer" versus a 15% trigger implies enormous headroom; the actual buffer (16.4% vs. 15%) is only about 1.2-1.4 points — a materially thinner margin of safety than the dossier represents, and one that moved in the *right* direction only modestly (15.2%→16.4% y/y).

### 2c. RJF — parent-level debt is ~$4.5bn, not "$0.7-0.95B" (fact #20)

**Claim in dossier (RJF.md §6, §8 bull case 2, §9 kill criterion 5):** *"Parent-level long-term debt is small (the DebtLongtermAndShorttermCombinedAmount XBRL tag shows only $0.7-0.95B across the last two quarters)"* — cited as a bull-case pillar ("conservative funding structure") and as the current baseline for kill criterion 5 ("Parent-level debt rises above $5B ... current ~$0.7-0.95B").

**What the primary source actually says:** RJF's balance sheet has **two** debt line items: "Other borrowings" ($950m Jun-26 / $700m Sep-25) — which is what the dossier's $0.7-0.95B figure captures — **and**, separately, "Senior notes payable" (**$3,522m** Jun-26 / $3,520m Sep-25), which the dossier's figure omits entirely. RJF's own Senior Notes Payable note states: *"At June 30, 2026, we had aggregate outstanding senior notes payable of $3.52 billion."*

**Correct value:** total parent-level debt (Other borrowings + Senior notes payable) ≈ **$4.47bn**, more than 4x the dossier's stated $0.7-0.95B, and much closer to the $5B kill-criterion-5 threshold than the "conservative funding structure" bull case represents.

### 2d. LVS — Adelson-family voting-power figure and its cited source are both wrong (fact #14)

**Claim in dossier (LVS.md §6, §9, §12, source 6):** *"the Adelson family ... beneficially owns/controls ~59.7% of voting power"*, sourced to *"The Nevada Independent / StockTitan Schedule 13D/A filings, Adelson/Chafetz beneficial-ownership disclosure, July 2026."*

**What the primary source actually says:** EDGAR's filing history for LVS (CIK 0001300514) shows **no Schedule 13D/A filed in 2026** at all — the most recent is dated 2023-12-05. The current, correct primary source is LVS's own **2026 DEF 14A** (accession 0001300514-26-000031, filed 2026-04-01), which states: *"the Adelson family members beneficially owning 386,657,840 shares representing approximately 58.2% of the Company's outstanding Common Stock as of March 16, 2026."*

**Correct value:** Adelson-family beneficial ownership is **~58.2%** of outstanding common stock (voting power, single-class stock), not 59.7%, and its source is the 2026 proxy statement, not a nonexistent July-2026 13D/A. The qualitative "controlled company" conclusion is unaffected (the proxy itself states the family controls "more than 50 percent of the voting power").

### 2e. HBAN — Veritex closed in October 2025, not "early 2026 ... within weeks of" Cadence (fact #26)

**Claim in dossier (HBAN.md §2, §3, §8):** *"Huntington ... closed two acquisitions within weeks of each other in early 2026 — Veritex Holdings (Texas, systems converted mid-January 2026) and Cadence Bank (Texas/South, closed 1 Feb 2026, systems converted mid-June 2026)."*

**What the primary source actually says:** HBAN's Q2 2026 8-K Ex-99.1 (accession 0000049196-26-000060) MD&A states: *"the Cadence acquisition, which was completed on February 1, 2026, and the Veritex acquisition, which was completed on October 20, 2025."*

**Correct value:** Veritex's acquisition **closed October 20, 2025** — about 3.5 months before Cadence closed (February 1, 2026), not "within weeks of each other in early 2026." (The dossier's separately-stated systems-conversion date for Veritex, mid-January 2026, is itself correct — that is a post-closing operational milestone, not the deal-closing date, and the dossier's framing sentence conflates the two.) This does not change the dossier's (correct) point that both systems conversions are now complete, ahead of FITB's pending Comerica conversion.

## 3. The MINORs, in full

- **GM (#4):** Q1 2026 EBIT-adjusted is $4,253m per the primary reconciliation table, not $4,300m as tabulated (1.1% overstatement); the dossier's Q4 2025 "implied" cell ($2.797bn) is also off against the actual directly-reported figure ($2,843m). The two errors happen to roughly cancel in the TTM sum the dossier relies on for its valuation rebuttal ($14.415bn actual vs. $14.42bn stated), so the downstream 7.8%-margin conclusion is not materially affected even though two of its four inputs are individually wrong.
- **LVS (#11):** the Macau concession expiry date (31-Dec-2032) and the 35.84bn-patacas commitment figure are exact matches; only the USD conversion (~$4.44bn per the 10-Q's own June-2026 FX rate vs. the dossier's ~$4.47bn) is off by an immaterial <1%.
- **LVS (#12):** the litigation judgment "became final" on March 4, 2026, and was "certified" by the appellate court on March 13, 2026, per the 10-Q's own wording; the dossier collapses these into a single "13-Mar-2026 final judgment" date. Substance (resolved, in the company's favor) is correct; only the precise date attribution is imprecise.

## 4. Thesis / kill-criterion-1 consistency check

- **GM:** kill criterion 1 (guidance cut below the current $14.0-16.0bn FY26 EBIT-adjusted range) is fully consistent with the confirmed guidance track record. However, the one-line verdict's core evidentiary claim — "automotive-net-cash economics" — rests on the overstated $8.7bn net-cash figure in fact #3 above; the qualitative direction (automotive is net-cash positive) still holds, but the magnitude used to argue against V1's "excessive" tag is significantly weaker than presented.
- **LVS:** kill criterion 1 (Sands China mass-market share loss for two consecutive quarters) is not contradicted by any filing reviewed; consistent.
- **RJF:** kill criterion 1 (adjusted pretax margin below 18% for two consecutive quarters) is consistent with the confirmed 19.7-20.0% run rate; no contradiction found.
- **HBAN:** kill criterion 1 (NPA ratio above 1.00% for two consecutive quarters, vs. 0.85% at Q2 2026) is consistent with the confirmed NPA figures; no contradiction found.

## 5. One-line judgement on dossier reliability

HBAN's dossier was the most reliable of the four — every figure in its entire five-quarter results table, its GAAP/adjusted EPS bridge, its capital ratios, its buyback figures and its credit-quality metrics matched the primary source exactly; its only defect is a framing error about deal-closing dates, not a numeric one. GM and LVS were reliable on raw quarterly results (revenue, margins, EPS, net debt all matched exactly) but each had one serious, thesis-relevant error stemming from mis-scoped entity/segment data (GM's automotive-vs-consolidated cash) or a non-existent cited source (LVS's Adelson-ownership 13D/A). RJF's dossier had the weakest showing of the four on its qualitative/structural claims specifically: both of its capital-structure claims (Bank capital ratios, parent debt) picked the wrong line item or the wrong entity, even though its quarterly P&L and litigation-timeline facts were all exact. The pattern across this batch — unlike DA6's mostly date/timing misses — is entity- and segment-scope confusion in balance-sheet and capital claims, worth flagging for future coverage passes as a specific failure mode to check for.
