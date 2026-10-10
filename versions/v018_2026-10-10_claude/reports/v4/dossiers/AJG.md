# AJG — Arthur J. Gallagher & Co. — Diligence Dossier (Agent F38, Wave-2 Standard)

## 1. Verdict
**INCLUDE-SMALL** (12–36 month horizon). Reservation: reported growth (+13% to +31% YoY across recent quarters)
is now almost entirely acquisition-driven. **Organic** growth in the core Brokerage base commissions/fees has
run only **4%** in both Q1 and Q2 2026 (vs AJG's historical high-single-digit organic pace), and the pace of new
bolt-on M&A has itself slowed (6 deals closed in Q2'26 vs 9 a year earlier; $58M of acquired annualized revenue
vs $291M), consistent with leverage (~2.8-3.0x net debt/EBITDA) constraining the very M&A engine the triage
praised. The business is high-quality and the price is undemanding, but the growth-durability story needs the
next 2-3 quarters to show organic re-acceleration before this is a full-conviction position.

## 2. Business in plain English
Arthur J. Gallagher is an insurance broker and risk-management consultant: it places commercial and personal
insurance for clients with third-party insurance carriers (earning commissions and fees) and separately sells
third-party claims administration and risk-consulting services (Risk Management segment, "Gallagher Bassett").
It underwrites no insurance risk itself — it is a distribution and advisory platform, so its economics are
closer to an asset-light services business (people, client relationships, data) than to an insurer's balance
sheet. Growth comes from two engines: organic (new business, retention, exposure/rate) and an unusually active
tuck-in M&A program (independent agencies acquired and folded onto Gallagher's platform), most recently supercharged
by the ~$13.45bn acquisition of AssuredPartners, financed in December 2024 and reflected in results since.

## 3. Why the model likes it — durable or artefact?
b1_live_scores.csv: composite percentile only 0.009 (live_rank 492/503) — the quant model does **not** like AJG;
it reached diligence through the triage/quality-growth screen only (Q05: quality 4, growth 4, price_vs_growth 4,
citing 31% revenue growth and a "38x trailing P/E [that] looks cheap once one-time integration costs are
stripped out"). This research confirms the triage's own caveat was directionally right — the 38x trailing P/E
is indeed distorted by AssuredPartners integration/amortization costs (§6) — but also finds the triage's growth
read was too generous: **31% reported growth is ~25-27 points of M&A and only ~4-5 points organic** (§4-5), a
distinction the triage's `reason` field did not make. The low quant score is at least partly a real signal
(leverage percentile and net-share-issuance from deal financing would penalize AJG in the Quality family), not
purely an artefact — flagged as a `data_conflict` below.

## 4. Last two years of results (GAAP; $ millions except per-share)
| Quarter | Revenue | YoY | GAAP diluted EPS | Adjusted diluted EPS¹ | Total organic change² |
|---|---|---|---|---|---|
| Q1'24 (Mar-24) | 3,256.7 | — | $2.74 | n/a | n/a |
| Q2'24 (Jun-24) | 2,775.4 | — | $1.27 | n/a | n/a |
| Q3'24 (Sep-24) | 2,806.8 | — | $1.39 | n/a | n/a |
| Q4'24 (Dec-24) | n/a³ | — | n/a | n/a | n/a |
| Q1'25 (Mar-25) | 3,727.0 | +14.5% | $2.72 | $4.21 | n/a |
| Q2'25 (Jun-25) | 3,222.0 | +16.1% | $1.40 | $2.30 | n/a |
| Q3'25 (Sep-25) | 3,365.6 | +19.9% | $1.04 | n/a | n/a |
| Q4'25 (Dec-25) | n/a³ | — | n/a | n/a | n/a |
| Q1'26 (Mar-26) | 4,758.0 | +27.7% | $3.16 | $4.97 | **+5%** |
| Q2'26 (Jun-26) | 4,003.0 | +24.2% | $1.25 | $2.84 | **+4%** |

Sources: SEC XBRL companyfacts (CIK 0000354190) for GAAP revenue/EPS; 8-K Ex-99.1 press releases for adjusted
EPS and organic growth (Q1'26 filed 2026-04-30, Q2'26 filed 2026-07-30). ¹Adjusted (company-defined) excludes
acquisition integration costs, amortization of intangibles, workforce/lease termination, and other specified
items — reconciliation on each release. **[Corrected 2026-10-06: Q1'26 adjusted EPS was $4.47 (Q1'25 $3.72), not $4.97 ($4.21); Q1 release acc. 0000354190-26-000132; the 1H26 total of $7.31 in section 6 is right (4.47 + 2.84)]** ²"Total organic change" = organic change in base commissions + fees +
supplemental + contingent revenues, i.e. AJG's own preferred underlying-growth metric, Brokerage + Risk
Management combined. **[Corrected 2026-10-06: the releases give Brokerage total organic +5% in both Q1 and Q2'26 (base commissions and fees +4%); the combined Brokerage + Risk Management organic growth was +5% in Q1 and +6% in Q2 (CEO statement), not +4% in Q2'26]** ³Q4'24/Q4'25 revenue not independently derived this pass (would require the FY10-K annual
total, not pulled for this table — limitation; the FY-level figures below are separately sourced).

**Key earnings-quality finding:** GAAP diluted EPS *fell* YoY in Q2 2026 ($1.25 vs $1.40) even as revenue grew
24%, purely because of AssuredPartners purchase-accounting and an easy prior-year comp: Q2 2025's adjusted
Brokerage-segment result included **~$144M of incremental interest income (~$0.42/share after-tax)** earned on
cash held in escrow ahead of the AssuredPartners financing (closed December 2024) — a one-off that will not
recur. Meanwhile amortization of intangible assets rose to $218M in Q2'26 from $130M in Q2'25 (Brokerage
segment), and acquisition-integration costs rose to $84M from $30M. On the company's own **adjusted** basis
(which strips out both the amortization step-up and the prior-year interest-income one-off), Q2'26 EPS was
**$2.84 vs $2.30, +23%** — a genuinely strong result masked by the GAAP headline. This is exactly the kind of
distinction `lead_v3_audit.md` flagged as commonly mishandled: the GAAP decline is real and disclosed, but it is
not evidence of a weakening business on its own.

## 5. Guidance track record
AJG does **not issue formal numeric full-year EPS or revenue guidance** in its earnings releases (confirmed:
neither the Q1'26 nor Q2'26 8-K Ex-99.1 contains a guidance table of the kind Abbott or Autodesk publish). It
gives qualitative outlook commentary only — e.g. Q2'26: "In an increasingly complex risk environment, client
demand for our advice, analytics, market access, specialty expertise and claims advocacy remains robust... we
remain confident in our ability to build on our momentum." A "CFO Commentary" document referenced in each
release (posted to ajg.com/IR) may contain more specific outlook language but was not accessed this pass (not
an SEC filing; time-boxed limitation). Per the base template's instruction, this is stated rather than
fabricated: **no formal guidance to track.**

## 6. Earnings quality & balance sheet
- **FCF conversion:** TTM (ended 2026-06-30) ≈ FY2025 10-K OCF $1,930M + 1H'26 OCF $967M − 1H'25 OCF $448M =
  **$2,449M OCF**; capex over the same window ≈$164M → **≈$2,285M FCF**, roughly consistent with Yahoo/d4's TTM
  FCF of $2.08bn (d4 `freeCashflow`; cross-check, minor definitional gap not reconciled).
- **SBC:** not separately quantified this pass (limitation).
- **GAAP vs adjusted gap:** 1H26 GAAP diluted EPS $4.41 vs adjusted $7.31 (a $2.90/share gap), vs 1H25 GAAP
  $4.12 / adjusted $6.04 (a $1.92/share gap) — the gap has widened by ~$1/share YoY, driven by the AssuredPartners
  intangible-amortization step-up ($419M 1H26 vs $282M 1H25) and acquisition-integration costs ($149M vs $63M).
  This is disclosed and reconciled, but the widening gap is itself worth watching — a "serial acquirer" business
  model structurally runs GAAP below adjusted, and the gap has grown alongside the largest deal in the company's
  history.
- **Leverage:** total debt (long-term debt noncurrent $11.955bn + short-term borrowings $1.52bn) ≈ **$13.5bn**
  at 2026-06-30, up from ~$12.7bn at 2025-06-30 shortly after the AssuredPartners financing. Cash (incl.
  restricted/fiduciary cash) $1.386bn same date. Net debt ≈ $12.1bn vs TTM EBITDA (Yahoo/d4) $4.29bn →
  **net debt/EBITDA ≈ 2.8x**, in the same range as the triage's cited 3.0x (methodology differs slightly:
  triage likely used company-reported EBITDAC; this analyst used Yahoo EBITDA as a cross-check — both point to
  elevated, not extreme, leverage for the sector). This level of leverage is consistent with, and likely
  explains, the M&A-pace deceleration noted in §1/§8.
- **M&A:** AssuredPartners — ~$13.45bn, financed December 2024, closed and integrating through 2025-2026; the
  single largest deal in company history and the primary driver of both reported revenue growth and the
  GAAP/adjusted gap. Underlying bolt-on M&A pace has slowed: 6 acquisitions closed in Q2'26 (est. annualized
  revenue acquired $58M) vs 9 in Q2'25 ($291M); 8 in Q1'26 vs 10 in Q1'25 — a real, quantified deceleration in
  the company's second growth engine, plausibly capital/leverage-constrained post-AssuredPartners.
- **Share count:** no shares were issued directly to sellers in tax-free-exchange acquisitions in Q2'26 or
  Q2'25 (per the release) — M&A is being funded with cash/debt, not dilutive stock issuance, which is
  consistent with the leverage increase observed above.

## 7. Valuation snapshot and reverse DCF
d4 (2026-09-25 close, price $231.10): NTM P/E 16.0x, FY1 P/E 15.5x, trailing P/E 38.3x (distorted by the
integration/amortization items above — **use NTM/FY1, not trailing**), FCF yield 3.5%, beta 0.51.
No V1 systematic-valuation row exists for AJG (not in the 92-name `v1_valuation_table.csv`) → `v1_verdict = null`;
this section is this analyst's own reverse DCF (skill script `valuation.py`).

- EV bridge: market cap $59.2bn + total debt $13.5bn − cash $1.4bn = **EV $71.3bn**.
- Reverse DCF (central case): WACC 7.0% (beta 0.51, rf≈4.2%, ERP≈5%), terminal growth 4.0%, base FCF $2.29bn,
  10-year stage-1 horizon → **implied FCF growth ≈2.7%/yr for 10 years**, fading to 4%. **[Corrected 2026-10-06: risk-free rate of 4.2% is wrong (5.17%), WACC 7.0% too low and base FCF includes stock-based compensation; restated to about 7.2%/yr (4.9-9.9% across assumptions), see Correction section]**
- Sensitivity: at WACC 8.5% (reflecting the elevated leverage), implied growth rises to **≈7.7%/yr**.
- My evidence-based base case: even at the *current, slowed* organic pace (4-5%) plus a resumed, deleveraged
  bolt-on M&A program (historically adding several points of inorganic growth annually before AssuredPartners
  absorbed capacity) and modest margin expansion, **8-10%/yr adjusted FCF/EPS growth** over the next decade is
  a reasonable base case — below the >20% currently being delivered, but well above the organic-only run-rate,
  on the assumption M&A capacity is restored as leverage comes down.
- **Implied vs base: BELOW** at the central-case WACC, and roughly **in line** at the top of the sensitivity
  range (8.5% WACC gives ~7.7%/yr implied vs an 8-10%/yr base case). **[Corrected 2026-10-06: restated: implied vs base is IN LINE at the programme WACC of about 7.5%, see Correction section]** This is the least clear-cut of this
  analyst's three names: unlike ABT and ADSK, a modestly higher (and, given the leverage, defensible) WACC
  assumption would flip the reverse-DCF read from "cheap" to "roughly fair" — disclosed explicitly rather than
  picking the WACC that produces the more flattering answer.

## 8. Bull case / bear case
**Bull:** (1) Top-3 global insurance broker with genuinely durable moats (client relationships, specialty
expertise, scale in placement/analytics) and a decades-long track record of successful tuck-in M&A. (2) Even at
a slowed pace, the M&A engine is still adding real revenue (6-8 deals/quarter), and deleveraging from the
AssuredPartners deal should restore capacity for more over the next 2-3 years. (3) Client retention and new
business generation both described as "strong"/"outstanding" by management (Q2'26 release) — a qualitative but
consistent management claim across releases, not new spin introduced this quarter.

**Bear:** (1) The headline growth numbers the triage screen liked (31% revenue growth) are overwhelmingly M&A,
not organic; organic growth of 4-5% is unremarkable for an insurance broker and well below AJG's own
historical high-single-digit organic pace — if this is the new normal (hard commercial insurance-rate cycle
turning soft, or genuine competitive share loss), the re-rating case weakens materially. (2) Leverage (~2.8x net
debt/EBITDA) is the highest in recent company history and is already visibly constraining the bolt-on M&A pace
that is the second growth engine — a negative feedback loop if organic growth doesn't independently reaccelerate.
(3) The GAAP/adjusted EPS gap has widened for two consecutive years running; a persistently widening gap between
"what shareholders can spend" (dividends, buybacks — funded by cash/adjusted earnings) and "what GAAP reports"
is a legitimate long-run earnings-quality concern for a serial acquirer, even when each individual adjustment is
well-disclosed.

## 9. Key risks & kill criteria (measurable)
1. Total organic change (AJG's own combined Brokerage + Risk Management metric) stays below 5% for three
   consecutive quarters (currently 4-5% in Q1-Q2'26; below AJG's historical high-single-digit norm).
2. Net debt/EBITDA rises above 3.5x (from ~2.8x now) without a disclosed deleveraging plan.
3. Quarterly acquired-annualized-revenue run-rate stays below $100M (vs $291-354M a year ago) for three more
   consecutive quarters, signaling the M&A engine has not recovered capacity.
4. The GAAP-vs-adjusted EPS gap widens by more than $0.50/share YoY again in a quarter with no new large
   acquisition to explain it.
5. A state insurance-regulatory or E&O (errors & omissions) matter is disclosed that is not ordinary-course
   (none identified this pass — see §11).

## 10. Catalysts & calendar
Next earnings: **2026-10-29** (Q3 2026, per d4 live snapshot). No formal numeric guidance to reconcile against
(§5); watch for organic-growth trend (re-acceleration vs continued 4-5%) and M&A-pace commentary.

## 11. Red-flag scan
- **Litigation/regulatory:** a targeted web search for AJG securities litigation or SEC/DOJ investigation
  (2026) returned no matches beyond routine SEC filings (8-K/10-Q/DEF 14A) — no material litigation or
  investigation identified this pass. This is not the same as a confirmed clean bill: a full read of the FY2025
  10-K Item 3 (Legal Proceedings) and Item 1A risk-factor diff was **not** completed this pass (time-boxed
  limitation, disclosed rather than silently skipped).
- **Auditor/accounting:** no auditor change, restatement, or going-concern language identified this pass (not
  exhaustively verified — same limitation as above).
- **Leverage/M&A-pace deceleration:** treated as the primary, quantified red flag in this dossier (§6, §8) —
  not a governance or accounting problem, but a real change in the shape of the growth story that the triage's
  quick pass did not capture.
- **Data conflict:** b1_live_scores.csv ranks AJG at live_rank 492/503 (bottom 2% of the composite), in tension
  with the triage's quality=4/growth=4 read and this dossier's own INCLUDE-SMALL verdict. Both are plausibly
  correct simultaneously: the pre-registered quant model penalizes recent net share/debt issuance and leverage
  (Quality family) and rewards raw statistical value/momentum signals that a debt-funded serial acquirer with a
  38x trailing P/E will score poorly on, while the qualitative/fundamental read (this dossier) can see through
  the GAAP distortion to a business growing adjusted EPS >20%. Flagged explicitly as a `data_conflict` rather
  than silently favoring one view.

## 12. Data basis, recency and disclaimer
All figures are **consolidated** GAAP as reported in the company's SEC filings unless labelled adjusted/non-GAAP. Most recent period incorporated: **Q2 2026 (period ended 2026-06-30), 10-Q filed 2026-08-05**; earnings press
release (8-K Ex-99.1) filed 2026-07-30. Checked for events to **2026-09-25** (no material 8-Ks beyond routine
items 5.02/5.07/7.01/8.01 identified between the Q2 release and 2026-09-25). GAAP figures are labelled GAAP;
adjusted figures are labelled adjusted and reconciled per the company's own release tables. **Research, not personalized investment advice; this is not investment advice.**

## 13. Sources
1. SEC EDGAR CIK 0000354190, XBRL companyfacts API (`https://data.sec.gov/api/xbrl/companyfacts/CIK0000354190.json`), retrieved 2026-09-26.
2. AJG 8-K Ex-99.1, Q2 2026 results, filed 2026-07-30 (`https://www.sec.gov/Archives/edgar/data/354190/000162828026051070/a2ndquarter2026earningsrel.htm`).
3. AJG 8-K Ex-99.1, Q1 2026 results, filed 2026-04-30 (`https://www.sec.gov/Archives/edgar/data/354190/000035419026000132/lab_exhibit991q1.htm`).
4. AJG 8-K filings list, SEC EDGAR browse-edgar atom feed, retrieved 2026-09-26 (used to confirm no undisclosed material 8-Ks between 2026-07-30 and 2026-09-25).
5. Web search, "Arthur J Gallagher AJG securities litigation SEC investigation 2026" (no material findings; see §11 limitation).
6. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (program quant context, as_of 2026-09-25/2026-08-05).
7. v4/outputs/Q05_triage.json (prior triage entry for AJG, incl. AssuredPartners deal size and initial leverage flag).
8. Company Q1'2025 earnings release (referenced within the Q1'2026 release for the AssuredPartners financing interest-income comparison), filed 2025-05-01 (footnote cross-check only, not separately fetched this pass).

---
## Correction (verification DV02, 2026-10-06)
Research only; not personal advice. Original text above is unchanged. Sources: AJG 8-K Ex-99.1 releases acc. 0000354190-26-000132 (Q1 2026, filed 30 Apr 2026) and 0001628280-26-051070 (Q2 2026, filed 30 Jul 2026); 10-Q acc. 0001628280-26-053489; XBRL companyfacts CIK 0000354190.

**Wrong figures corrected**
- Section 4 table, Q1'26 adjusted EPS: **$4.47** (not $4.97) and Q1'25 **$3.72** (not $4.21): Q1 release, "Total Company, as adjusted" $4.47 vs $3.72 (+20%). GAAP $3.16 vs $2.72 and the Q2 figures ($1.25 vs $1.40 GAAP; $2.84 vs $2.30 adjusted) are right. The 1H26 adjusted $7.31 (4.47 + 2.84) and 1H25 about $6.02 (3.72 + 2.30; dossier $6.04) in section 6 are consistent with the corrected values, so the table, not section 6, was wrong.
- Section 4 table and footnote 2, "Total organic change": the Q2'26 release reports Brokerage total organic change +5% (base commissions and fees +4%, supplemental +20%, contingent -8%) and Risk Management organic fees +12%; the CEO states combined organic growth of 6% for Q2 and 5% for Q1 (Q1 Brokerage +5%, RM +10%). The table's "+4%" for Q2'26 is the base-commissions-and-fees rate. The verdict sentence about base commissions and fees at 4% in both quarters is correct. Kill criterion 1 ("currently 4-5%") should read 5-6% on the combined metric; the conclusion (below AJG's historical high-single-digit pace) stands but is less severe.
- Section 7 valuation: stated risk-free rate 4.2% is wrong (10-year Treasury 5.17% on 25 Sep 2026); with beta 0.51 and ERP 5% the dossier's own inputs give 6.8%, not 7.0%; the base free cash flow ($2.29bn) adds back stock-based compensation (about $65M over the last twelve months: FY25 $49M plus 1H26 $41M less 1H25 $25M).

**Recomputed reverse DCF** (programme parameters: rf 5.17%, ERP 4.14%, Blume-adjusted 5-year weekly beta 0.74, cost of equity 8.2%; after-tax cost of debt about 4.2%, debt 18% of capital, so WACC about **7.5%**): EV $71.3bn; free cash flow after stock-based compensation about $2.22bn; ten years constant growth then 3.0% terminal. Implied growth **7.2%/yr** (4.9% with the dossier's 4.0% terminal; 9.2% at the 8.2% cost of equity; 9.9% at 8.5%). The dossier's 2.7% and 7.7% reproduce only from the flawed inputs. Against the 8-10%/yr base case the gap is 0.8-2.8 points at the central WACC: **implied vs base IN LINE** (was "below"; it was never robust, as the dossier itself said). One further caution: the base 8-10% includes growth bought with bolt-on acquisitions, whose cash cost is not deducted from FCF; netting it would lower the base.

**Verdict:** unchanged, INCLUDE-SMALL (in line is within the rule; organic growth, leverage and M&A-pace reservations stand). Updated entry in v4\outputs\F38_summary.json (AJG): valuation_view_vs_v1.implied_vs_base ("below" -> "in_line") and reconciliation; scenario returns unchanged (basis not stated; not re-derived).

**Not errors:** the XBRL cross-tie flags on debt were false leads (the nearest-value tag $12,873M is total long-term debt at 31 Dec 2025). Debt: long-term $11,955M plus short-term borrowings $1,520M = $13.5bn and cash $1,386M at 30 Jun 2026 are correct (10-Q).
