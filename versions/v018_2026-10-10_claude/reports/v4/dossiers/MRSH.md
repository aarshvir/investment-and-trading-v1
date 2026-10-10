# Marsh & McLennan Companies, Inc. (MRSH) — Diligence Dossier

**Agent:** F54 | **As of:** 2026-09-25 close ($171.12) | **Depth:** Standard

**Note on naming:** the SEC registrant remains "Marsh & McLennan Companies, Inc." (ticker recently changed
from MMC to MRSH); the company brands itself "Marsh" in current press releases. This dossier uses "MRSH" or
"the Company" throughout. One of its four operating segments is also internally called "Marsh," distinct
from the parent brand — this dossier always says "Risk and Insurance Services segment" for that unit to keep
segment-level figures separate from consolidated ones (the wave-3 entity-scope requirement).

## 1. Verdict
**INCLUDE-SMALL** (24–36 month horizon), reservation: a real, unresolved legal exposure (Credit Suisse's
~$2bn Greensill-related claim against two subsidiaries) could add materially to the $425M already charged,
and GAAP diluted EPS actually **fell** 5% YoY in H1 2026 on that one-off — this is a genuine adverse fact,
not merely a headline scare, so this is a half-weight position pending the next 1–2 quarters of clarity.
Underneath that, the underlying franchise (world's largest insurance broker, plus Mercer and Oliver Wyman) is
high-quality, growing, and — on a reverse DCF — priced for very little forward growth, i.e. cheap if the
litigation resolves within the reserved range.

## 2. Business in plain English
MRSH is the world's largest insurance broker and professional-services group, organized in two segments:
**Risk and Insurance Services** (Marsh — commercial insurance broking; Guy Carpenter — reinsurance broking)
and **Consulting** (Mercer — retirement, health and workforce consulting; Oliver Wyman — management
consulting). It earns commissions and fees for placing insurance/reinsurance and advising clients, plus fee
income on consulting engagements — an asset-light, recurring-revenue model with high client-retention
economics, growing both organically and through bolt-on and larger (e.g., McGriff) acquisitions.

## 3. Why the model likes it — durable or artefact?
Triage (Q05) cited 25.9% ROE, "durable recurring commissions," and 39% EPS growth, calling 15.3x forward P/E
fair. Confirmed with primary data and refined: `b1_live_scores.csv` (2026-09-25) shows ROE (pct_roe) in the
86th percentile and gross-profit/assets in the 91st percentile — genuinely strong, durable broker economics,
not an artefact. However, the "39% EPS growth" and the 15.3x forward P/E in `d4_live_snapshot.parquet` carry
an explicit **`ntm_quality`="caution" flag from the vendor data itself** — this dossier does not rely on that
NTM P/E; it is very likely distorted by the $425M Greensill charge booked in Q1 2026 depressing the trailing
GAAP EPS base that a naive forward-growth calculation would use. The reverse DCF in §7 uses FCF, not that
EPS growth figure, to avoid propagating the distortion.

## 4. Last eight quarters, GAAP (SEC 10-Q/10-K, XBRL `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` / `OperatingIncomeLoss` / `NetIncomeLoss` / `EarningsPerShareDiluted`, consolidated MRSH)

| Quarter | Revenue ($M) | YoY | Operating income ($M) | Op. margin | Net income ($M) | Diluted EPS (GAAP) |
|---|---|---|---|---|---|---|
| 3Q24 | 5,697 | — | 1,108 | 19.4% | 747 | $1.51 |
| 4Q24 | 6,067* | — | 1,142* | 18.8% | 788* | $1.59 |
| 1Q25 | 7,061 | — | 2,005 | 28.4% | 1,381 | $2.79 |
| 2Q25 | 6,974 | — | 1,829 | 26.2% | 1,211 | $2.45 |
| 3Q25 | 6,351 | +11.5% | 1,170 | 18.4% | 747 | $1.51 |
| 4Q25 | 6,595* | +8.7%* | 1,219* | 18.5% | 821* | $1.68 |
| 1Q26 | 7,597 | +7.6% | 1,754 | 23.1% | 1,146 | $2.36 |
| 2Q26 | 7,404 | +6.2% | 1,899 | 25.7% | 1,266 | $2.63 |

\* 4Q figures = FY 10-K total minus the 9-month 10-Q figure. **1Q26 GAAP operating income and net income are
depressed** relative to what underlying growth would suggest: the Company recorded a **$425 million gross
liability in Q1 2026** for the Greensill litigation (§6/§11), booked in "other operating expenses" —
excluding that item, adjusted operating income rose 7% YTD through 2Q26 vs the prior-year period (Q2 2026
earnings release) even as GAAP operating income fell 5% YTD. Six-months GAAP diluted EPS was **$4.99 in H1
2026 vs $5.23 in H1 2025 (−5% YoY)**; six-months **adjusted** diluted EPS rose to $6.25 (+8% YoY). The GAAP
decline is real and disclosed by management itself as being "driven by a decrease in operating income" (10-Q
MD&A) — this is the headline adverse fact for this name.

## 5. Guidance track record
MRSH does **not** publish formal quarterly or full-year numeric revenue/EPS guidance in its earnings releases
(confirmed: no "guidance" or "outlook" language with numeric targets in the Q1 2026 or Q2 2026 8-K Exhibit
99.1 releases, filed 2026-04-16 and 2026-07-21). Management instead discusses qualitative margin-expansion
priorities and its "Thrive" efficiency program (launched Q3 2025) without numeric full-year targets.

## 6. Earnings quality & balance sheet (consolidated MRSH, per the 10-Q filed 2026-07-21, period 2026-06-30,
vs 2025-12-31 10-K balance sheet, unless stated; entity scope noted explicitly per the wave-3 mandate)
- **FCF conversion:** TTM (`d4_live_snapshot.parquet`, 2026-09-25) operating cash flow $5.078bn, FCF
  $4.785bn, TTM net income implied by trailing EPS ~$3.92bn (8.20 trailing EPS × ~477.9M shares) → FCF/NI ≈
  1.22x — strong conversion, though the numerator benefits from the Greensill charge being an *accrual*
  (booked to accounts payable/accrued liabilities, not yet a cash outflow as of 2026-06-30 per the 10-Q), so
  TTM operating cash flow has **not yet** absorbed the eventual cash cost of that liability.
- **SBC:** not separately quantified in the extracts reviewed; flagged as an open item (not a red flag, an
  information gap).
- **The Greensill litigation — entity scope is critical here.** The $425M charge and the underlying claims
  sit at the **subsidiary** level: **Marsh Ltd.** (U.K.) and **Marsh Pty Ltd.** (Australia), insurance-broking
  subsidiaries, not the MRSH parent directly, though the liability is consolidated onto the group balance
  sheet (10-Q Note 17, "Claims, Lawsuits and Other Contingencies"). Marsh Ltd. placed trade-credit insurance
  for Greensill Capital (UK) Limited from 2014; Greensill collapsed into insolvency from March 2021. Of the
  Australian proceedings (36 applicants, ~$5bn originally claimed): (a) White Oak's claim was **settled in
  May 2025**, recovered through the Company's own E&O insurance (no net cost); (b) **Greensill Bank AG (in
  insolvency) and its administrator, which had claimed ~$3bn, reached a settlement with Marsh Ltd./Marsh Pty
  Ltd. in June 2026** — this settlement is inside the $425M charge; (c) **Credit Suisse (two funds), which
  added Marsh Ltd. as a party in November 2023 and has claimed ~$2bn plus interest and costs, is
  UNRESOLVED** as of the 2026-06-30 10-Q. The Company states explicitly: "there can be no assurance that the
  Company's current estimate will prove to be accurate... the Company may record additional charges in future
  periods as discussions progress" (10-Q Note 17). This is the single biggest identifiable tail risk in this
  dossier.
- **Balance sheet, consolidated:** own cash and cash equivalents **$1,700M** (down from $2,687M at YE2025) —
  this explicitly **excludes** "cash and cash equivalents held in a fiduciary capacity" of **$12,203M**
  (client premium/claims money the Company holds temporarily, offset by an equal fiduciary-liability balance;
  not the Company's own liquidity — entity-scope distinction per the wave-3 mandate). Long-term debt $18,891M
  + current portion $646M + commercial paper $1,024M = **≈$20,561M gross debt, consolidated**; total equity
  $15,433M; total assets $59,682M (of which fiduciary assets are a large, offsetting component). Net debt
  (gross debt less **own** cash only) ≈ $18,861M; TTM EBITDA $7.758bn (`d4_live_snapshot.parquet`) → net
  debt/EBITDA ≈ **2.43x** — moderate leverage, but the Greensill overhang is a call on future cash/earnings
  that is not fully captured by a backward-looking leverage ratio.
- **Capital return:** Q2 2026 repurchased 4.5M shares for $750M; H1 2026 repurchased 8.7M shares for $1.5bn;
  Board raised the quarterly dividend **10% to $0.990/share** on 2026-07-08 — a genuine vote of confidence
  from management alongside the litigation charge, worth weighing against the adverse fact above.
- **M&A:** completed 5 acquisitions in 2026 YTD for $181M total consideration (small, bolt-on scale); McGriff
  integration/retention costs ($89M YTD) continue as a noteworthy item, consistent with the 2024 McGriff
  acquisition still being integrated.

## 7. Valuation snapshot
Trailing P/E 20.9x, forward P/E 15.0x, **NTM P/E 15.3x flagged "caution" by the vendor's own data-quality
check** (`d4_live_snapshot.parquet`, `ntm_quality`="caution") — this dossier does **not** use that figure as
primary evidence, consistent with the wave-3 lesson on not trusting an un-sanity-checked vendor NTM field.
FCF yield 3.4%, EV/Sales (NTM) 3.4x, dividend yield (trailing) 2.17%. No V1 systematic valuation row exists
for MRSH (not covered in this V1 run); v1_verdict is null. **Own reverse DCF** (two-stage FCF/share basis,
$10.03 TTM FCF/share from `d4` FCF $4.785bn ÷ ~477.2M shares; cost of equity 7.1% from CAPM, beta 0.577 — a
genuinely low beta for the sector, consistent with insurance broking's non-cyclical, recurring-commission
model; 10-year explicit growth then an 18x terminal FCF multiple, below MRSH's own ~20x historical average)
implies the market is pricing in **≈0.8%/yr** FCF-per-share growth for 10 years — a very low bar, well below
both MRSH's realized organic growth (mid-single-digit underlying, high-single-digit reported revenue growth
even in the softer 2H25/1H26 quarters, §4) and its historical ~8–10%/yr adjusted-EPS growth. **This is priced
below a reasonable base case** — the market appears to be discounting for the Greensill overhang and the
GAAP-EPS optics, which is exactly the risk this dossier flags rather than dismisses. Sensitivity check: this
result is highly sensitive to the WACC/terminal-growth spread in a pure Gordon-growth form (flipping to
negative implied growth for WACC below ~7.5% with a 3% terminal rate) — the exit-multiple form used here is
more stable and is the basis for the "below" call, but the honest range spans roughly 0–3%/yr across
reasonable assumption sets, all still below the ~8% base case. **[Corrected 2026-10-09: SBC ($419M TTM) was not deducted and 7.1% is not tied to the 5.17% Treasury plus a stated risk premium; restated implied growth is 2.0% at 7.1% and 3.0% at 8.14% (5.17% + Blume beta 0.717 x 4.14%), still below the base]**

## 8. Bull case / Bear case
**Bull:** (1) the Board's 10% dividend increase alongside the Greensill charge signals management does not
see the residual Credit Suisse exposure as solvency-relevant; (2) organic growth, while decelerating YoY
(underlying growth ~3–5% in recent quarters vs high-single-digit two years ago), remains positive across a
diversified four-brand (Marsh/Guy Carpenter/Mercer/Oliver Wyman) platform through a softening commercial-
insurance pricing cycle — a resilience test many pure-play brokers do not face as well; (3) at a reverse-DCF
implied growth near zero, almost any resolution of the Credit Suisse claim inside the currently-implied
range should not re-rate the stock lower purely on that basis — the bad news looks largely priced.
**Bear:** (1) Credit Suisse's ~$2bn claim is unresolved and management's own language ("no assurance,"
"may record additional charges") is not boilerplate — a materially adverse outcome could mean a second large
charge on top of the $425M already taken; (2) GAAP EPS declining YoY in H1 2026 is a real earnings-quality
blemish that a "just look at adjusted EPS" framing understates for a research process built to distrust
adjusted-vs-GAAP gaps; (3) underlying/organic revenue growth has decelerated across the last several
quarters (§4) as commercial P&C insurance pricing has softened industry-wide — a genuine cyclical headwind
to the core Risk & Insurance Services segment, separate from the litigation issue.

## 9. Key risks & kill criteria (measurable)
1. The Credit Suisse Greensill claim (or any related Australian-proceedings claim) results in an incremental
   charge exceeding $500M in any single quarter, beyond the $425M already reserved.
2. GAAP diluted EPS declines YoY for a third consecutive quarter (it already has in 1Q26 and, on a six-month
   basis, through 2Q26) while adjusted diluted EPS growth also decelerates below 5% YoY.
3. Risk and Insurance Services segment underlying (organic) revenue growth turns negative for two
   consecutive quarters.
4. Consolidated net debt (excluding fiduciary funds and fiduciary liabilities)/TTM EBITDA exceeds 3.0x
   (from ≈2.43x currently).
5. The quarterly dividend is cut or held flat for four consecutive quarters after the 2026-07-08 increase
   (a reversal of the current capital-return signal).

## 10. Catalysts & calendar
Next earnings: **2026-10-15** (Q3 2026, per `d4_live_snapshot.parquet`). No investor day date found in the
documents reviewed; the Credit Suisse Greensill claim's next procedural milestone was not dated in the 10-Q
text extracted (open item). **[Corrected 2026-10-09: the 10-Q (Note 17) states 'Trial is currently scheduled for September 2026' for the Australian proceedings including the Credit Suisse claim; outcome not disclosed in any SEC filing to 9 Oct 2026]**

## 11. Red-flag scan
- **Greensill litigation** (§6): the single largest identified item, entity-scoped to Marsh Ltd./Marsh Pty
  Ltd., with $425M already charged and the Credit Suisse portion of the claim (~$2bn) unresolved as of the
  filing date.
- **Aviation/reinsurance information-sharing investigation:** the 10-Q's legal-proceedings note also
  references an investigation into an alleged "sharing of sensitive commercial and competitive confidential
  information" among aviation insurers/reinsurers; details and quantum were not further specified in the text
  extracted (open item, flagged not dismissed). **[Corrected 2026-10-09: this and the Brazil item below are one matter: the January 2019 CADE proceeding about alleged information-sharing in aviation insurance and reinsurance]**
- **Brazil antitrust matter:** a long-running (since January 2019) administrative proceeding before Brazil's
  competition authority against a number of insurance brokers, including the Company; no update on status
  found in the extract reviewed (open item).
- Ordinary-course subpoenas and government information requests are disclosed as standard practice (10-Q);
  not treated as a red flag on their own.
- No material weakness, going-concern language, restatement, or auditor-change language found in the
  documents reviewed.

## 12. Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 (period ended 2026-06-30), Form 10-Q filed 2026-07-21 (accession
0000062709-26-000195), plus the Q1 2026 10-Q (filed 2026-04-16) and FY2025 10-K (filed 2026-02-09) for the
two-year quarterly history. Events checked to 2026-09-25 close. All figures above are **GAAP unless labelled
"adjusted"**; adjusted figures are management's own non-GAAP reconciliation as disclosed in the cited 8-K
exhibits. Research, not personalized investment advice; not a recommendation.

## 13. Sources
1. SEC EDGAR, Marsh & McLennan Companies Form 10-Q, period 2026-06-30, filed 2026-07-21 (accession
   0000062709-26-000195): `https://www.sec.gov/Archives/edgar/data/62709/000006270926000195/mrsh-20260630.htm`
2. 8-K Exhibit 99.1, Q2 2026 news release, filed 2026-07-21:
   `https://www.sec.gov/Archives/edgar/data/62709/000006270926000193/mmc2q2026ex991newsrelease.htm`
3. 8-K Exhibit 99.1, Q1 2026 news release, filed 2026-04-16:
   `https://www.sec.gov/Archives/edgar/data/62709/000006270926000096/mmc1q2026ex991newsrelease.htm`
4. SEC EDGAR, Form 10-K, FY2025, filed 2026-02-09: `https://data.sec.gov/submissions/CIK0000062709.json`
5. SEC EDGAR XBRL company facts API: `https://data.sec.gov/api/xbrl/companyfacts/CIK0000062709.json`
6. `v4/data/b1_live_scores.csv` and `v4/data/d4_live_snapshot.parquet` (2026-09-25 snapshot).
7. `v4/outputs/Q05_triage.json` (triage entry for MRSH).

## Correction (verification DV29, 2026-10-09)

**Wrong text 1 (section 10):** "the Credit Suisse Greensill claim's next procedural milestone was not dated in the 10-Q text extracted". **Correct:** 10-Q Note 17 (acc. 0000062709-26-000195): "Trial is currently scheduled for September 2026." The trial window therefore opened before the 25 Sep 2026 price cutoff; no SEC filing through 9 Oct 2026 reports an outcome. The $425M liability reflects the Greensill Bank settlement plus management's best estimate for the remaining Credit Suisse claims, with an explicit no-assurance caveat. This is the dominant near-term binary event for the name and should be tracked as a dated catalyst. Verdict effect: none (INCLUDE-SMALL already reserves for this claim); re-check any 8-K or 10-Q (Q3 results expected 15 Oct 2026) before adding.

**Wrong text 2 (section 11 and F54 key_adverse_facts):** the "aviation/reinsurance information-sharing investigation" and the "Brazil antitrust matter" are listed as two open items. **Correct:** one matter. 10-Q legal proceedings: in January 2019 Brazil's Administrative Council for Economic Defense commenced a proceeding against brokers and insurers "to investigate an alleged sharing of sensitive commercial and competitive confidential information" in the aviation insurance and reinsurance sector. Not a second risk.

**Wrong text 3 (section 7 reverse DCF):** FCF per share $10.03 with SBC not deducted ("not separately quantified"; it is $419M TTM = 394 - 210 + 235 from the FY25 10-K and the H1 cash-flow statements), cost of equity 7.1% (implied risk premium 3.35% over the 5.17% Treasury of 25 Sep 2026). **Correct:** FCF after SBC about $9.11 per share (TTM OCF 5,078 less capex 311 less SBC 419, over 477.2M shares); programme cost of equity 5.17% + Blume beta 0.717 (d4 beta 0.577) x 4.14% = 8.14%. Restated implied 10-year FCF-per-share growth (18x terminal multiple, price $171.12): 2.0% at 7.1%, 3.0% at 8.14%; 3.3% to 4.3% if the unpaid $425M accrual is also deducted from the starting cash flow. The original 0.8% reproduces only on the uncorrected inputs.

**Verdict effect:** none. Implied remains below the ~8% base, so "below" and INCLUDE-SMALL stand. The F54 reconciliation text was updated to the restated figures; scenario returns (-3.5% / +6.8% / +13.2%) reproduce and are unchanged. Minor: the header note's "four operating segments" should read four businesses within two reportable segments.
