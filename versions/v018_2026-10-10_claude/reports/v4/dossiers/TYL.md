# TYL (Tyler Technologies, Inc.) — Diligence Dossier

Agent: F37 · Standard depth · Prepared 2026-09-26 · Prices/market data as of 2026-09-25 close ($325.57; mkt cap ≈$13.33B)

**Data quality note:** all figures are consolidated (Tyler has no separately-reported standalone entity), in US dollars ($ = USD; m/mn = millions, bn = billions unless a per-share $ figure), sourced primarily from SEC EDGAR XBRL and company earnings releases as cited in Section 13; GAAP vs. non-GAAP figures are labelled throughout; approximated (derived) figures are flagged where used.

## 1. Verdict

**INCLUDE-SMALL** — 24–36 month horizon. Dominant public-sector (courts, property tax/appraisal, ERP, courts
recording) software vendor with 22 consecutive quarters of 20%+ SaaS growth and 86.7% recurring revenue; the
reverse DCF shows the market pricing in only ~1.9%/yr FCF growth for 10 years, far below the growth actually
being delivered. Held at half weight, not full, for three specific, named reasons: (i) leverage went from
near-zero to a new $1.4375bn convertible note issued mid-2026, used mostly to fund buybacks and a bolt-on deal
rather than organic growth; (ii) non-GAAP operating margin *contracted* 80bp YoY in the most recent quarter even
as revenue and FCF hit records; (iii) Tyler's courts/justice software has a documented, recurring history of
implementation failures tied to wrongful arrests/detentions — a sector-specific tail risk with no clean analog
in most SaaS names. No V1 row exists for TYL, so `v1_verdict` is null.

## 2. Business in plain English

Tyler sells mission-critical software to US state and local governments: court case management (Odyssey/Enterprise
Justice), property tax and appraisal systems, municipal/county ERP and financial systems, public-safety records
management, and (since April 2026) digital court recording (For The Record). It earns subscription/SaaS fees,
maintenance on legacy on-premise licenses being migrated to the cloud, and services revenue from implementation.
The moat is multi-decade government contracts and extreme switching costs — a county does not re-platform its
court system or property-tax rolls lightly — reinforced by data-residency and public-record requirements that
favor an incumbent with an existing certified footprint in most US counties.

**Sector routing note:** the stock-analysis skill router maps this to `it-saas.md`. That playbook's central
warning applies directly here: GAAP P/E (39.2x trailing) and non-GAAP P/E (~21–22x NTM) tell very different
stories because SBC (~6.4% of TTM revenue) and acquired-intangible amortization are excluded from non-GAAP.
Neither multiple alone is "the" valuation; Section 7 uses FCF, which nets SBC out as a real cash cost.

## 3. Why the model likes it / durability

`data/b1_live_scores.csv`: live_rank 307, composite 0.382 (decile 4) — the lower composite versus PAYX/VLTO is
driven almost entirely by weak raw Momentum (fam_M 0.043, mom_12_1 -0.289: the stock has lagged over the past
year despite strong fundamentals) even though SUE (earnings-surprise momentum) is very strong at 1.207 and
Value (fam_V 0.753) is good. This is a case where quant momentum and fundamentals disagree — the stock has been
a fundamentals story that the market has been slow to re-rate, which is consistent with (not contradicted by)
the cheap reverse-DCF read in Section 7. Durability check: SaaS revenue growth of 20%+ has now held for 22
straight quarters (a genuinely long, hard-to-fake streak), and recurring revenue is 86.7% of the total — this
is a real, structural annuity, not a cyclical or one-off beat.

## 4. Last two years of results (calendar quarters, FYE 31-Dec; GAAP unless marked)

| Qtr (end) | Revenue | Op. margin (GAAP) | GAAP diluted EPS | Non-GAAP diluted EPS |
|---|---|---|---|---|
| Q3 2024 (Sep-24) | $543.3M | 15.2% | $1.74 | — |
| Q4 2024 (Dec-24) | $541.1M | 13.2% | ~$1.48 (derived) | $2.14* |
| Q1 2025 (Mar-25) | $565.2M | 15.8% | $1.84 | — |
| Q2 2025 (Jun-25) | $596.1M | 16.0% | $1.93 | — |
| Q3 2025 (Sep-25) | $595.9M | 16.4% | $1.93 | $2.79* |
| Q4 2025 (Dec-25) | $575.2M | 13.0% | ~$1.50 (derived) | $2.64 |
| Q1 2026 (Mar-26) | $613.5M (+8.6%) | 16.3% | $1.88 | $3.09 (+9.3%) |
| **Q2 2026 (Jun-26)** | **$645.1M (+8.2%)** | **14.7%** | **$2.23 (+10.5%)** | **$3.08 (+0.9%)** |

*Approximate, sourced from Zacks/Alphastreet secondary summaries, not independently confirmed against the
primary release for those two older quarters — flagged, not treated as certain.

FY2025: revenue $2,300M, **[Corrected 2026-10-08: $2,332.3M]** non-GAAP diluted EPS $11.31. Q2 2026 detail: recurring revenue $559.5M (86.7% of
total); subscription revenue $453.7M (+12.0%); **SaaS revenue $230.6M (+21.7%), the 22nd straight quarter of
20%+ SaaS growth**; free cash flow $118.5M (+34.7%, a Q2 record). Q4/Q1-derived GAAP EPS figures are FY-total
minus reported Q1–Q3 (Tyler does not separately XBRL-tag a discrete Q4 GAAP EPS), disclosed as an
approximation. TTM (Sep-25–Jun-26) net income $324.6M; TTM free cash flow $705.9M (Q3'25 $247.6M + Q4'25
$237.0M + Q1'26 $102.8M + Q2'26 $118.5M, company-reported figures) → **FCF/NI ≈217%**, and even FCF-less-SBC/NI
≈169% — very strong, though the gap itself is a flag to read (Section 6).

## 5. Guidance track record (last 3 releases, FY2026 outlook)

| Release | Total revenue | Non-GAAP diluted EPS | FCF margin | vs prior guide |
|---|---|---|---|---|
| FY26 initial (19-Feb-26, w/ Q4'25) | $2.50–2.55B | $12.40–12.65 | 26–28% | New-year guide |
| Q1 2026 (29-Apr-26) | $2.535–2.575B | $12.50–12.75 | 26–28% | **Raised** (both revenue and EPS lifted) |
| **Q2 2026 (29-Jul-26)** | **$2.535–2.575B** | **$12.95–13.20** | **26–28%** | **Raised again** (EPS midpoint +$0.40 vs. Q1 guide) |

Two consecutive raises, no cuts, and the FY2026 top-line range was never widened downward — a clean track
record. FY2026 guided non-GAAP EPS growth (vs. FY2025's $11.31 actual) is ~14–17% at the current range.

## 6. Earnings quality & balance sheet

- **SBC:** TTM (Sep-25 through Jun-26) ≈$155.8M / TTM revenue $2,429.7M ≈ **6.4% of revenue** — moderate for
  enterprise software, worth tracking (per-quarter SBC has risen from ~$27M in late 2023 to ~$44M in Q2 2026,
  slightly faster than revenue growth).
- **GAAP vs non-GAAP:** Q2 2026 GAAP EPS $2.23 (+10.5% YoY) vs non-GAAP EPS $3.08 (+0.9% YoY) — the growth-rate
  *direction* flipped between the two measures this quarter, which is unusual and worth watching next quarter;
  driven mainly by SBC/acquired-intangible add-backs and, this quarter specifically, by a **non-GAAP operating
  margin decline (25.7% vs 26.5% a year earlier)** even as revenue grew 8.2% — a genuine margin-quality nuance,
  not merely an SBC-timing artefact, plausibly tied to SaaS-transition costs and the newly-closed For The Record
  integration.
- **Leverage — the central new fact this quarter:** Tyler closed a **$1.4375bn 0.50% convertible senior notes
  offering due 2031 on 14-May-2026** (upsized from a planned $1.0bn). Net proceeds ≈$1,408.1M were used:
  ~$187.2M to fund capped-call transactions, ~$320.7M to repurchase ~1.03M shares, and the remainder for
  "general corporate purposes" — which included funding the **$212.5M "For The Record" acquisition** (closed
  Apr-2026, a court-recording/AI-transcription bolt-on). This is a genuine shift from a near-zero-leverage
  balance sheet **[Corrected 2026-10-08: the convert partly refinanced a $600M convertible due 2026 repaid in Q1; the move was from net cash ~$0.5bn to net debt ~$0.44bn]**: LT debt (mostly the new convert) ≈$1,455.0M, cash+ST investments ≈$970.0M → net debt ≈$485.0M
  vs TTM EBITDA $458.5M → **net debt/EBITDA ≈1.06x** **[Corrected 2026-10-08: net debt $438.7M on carrying debt $1,408.7M; TTM EBITDA $505.6M; ratio 0.87x]** — still low in absolute terms, but a real change in kind
  (debt-funded buybacks/M&A vs. the prior organically-funded model) that should be tracked, not waved through.
- **Litigation pattern (sector-specific, recurring):** courts/justice software implementation failures have
  repeatedly resulted in real-world harm attributed to Tyler's products: wrongfully-arrested/jailed individuals
  in Alameda County, CA after switching to Tyler's Odyssey Case Manager (2016); Lubbock County, TX software
  problems (2021 report); a June-2023 North Carolina class action (with two sheriffs as co-defendants) alleging
  hundreds wrongly detained during the state's paper-to-digital court-system migration; a 2021 $3M settlement of
  a federal wage-and-hour class action. This is not a one-off — it recurs roughly every 2–3 years and is a
  structural feature of selling case-management software to under-resourced court systems, not a solved
  historical problem.

## 7. Valuation snapshot and reverse DCF

No V1 row exists for TYL; `v1_verdict = null`. Analyst-derived reverse DCF (`stock-analysis/scripts/valuation.py`,
10-year fade to 4% terminal growth):

- EV bridge: market cap $13,332.8M + debt $1,455.0M − cash $970.0M = **EV ≈$13,817.8M** (Yahoo EV $13,870.2M,
  consistent)
- WACC 8.5% (beta 0.835, moderate; software moat but newly leveraged)
- Base FCF (TTM, company-reported): $705.9M
- **Implied 10-year FCF growth priced in: ~1.9%/yr**, fading to 4% terminal. **[Corrected 2026-10-08: company FCF adds back SBC; programme basis (Ke 8.85%, FCF after SBC $550M, 3.0% terminal) gives ~7.2%/yr, implied vs base in line]**

That is dramatically below what Tyler has actually delivered (22 straight quarters of 20%+ SaaS growth,
guided FY26 non-GAAP EPS growth ~14–17%, Rule-of-40-style composition of ~8% revenue growth + ~29% TTM FCF
margin ≈ 37). Trailing P/E 39.2x looks rich in isolation but FCF yield is 5.3% and EV/EBITDA (30.1x) is inflated
by SBC/amortization exclusions from EBITDA that the FCF-based read already nets out. **valuation_view_vs_v1.
implied_vs_base = "below"** — the price embeds far less growth than the evidenced base case, satisfying the
INCLUDE-SMALL/INCLUDE growth-priced-in test; held to half weight for the balance-sheet-change and
litigation-pattern reasons above, not for valuation reasons.

Scenario table (analyst-constructed; 3-year forward EPS × exit P/E, no dividend): **Bear** EPS $11.50 @ 25x →
**-4.1%/yr**; **Base** EPS $14.80 @ 30x → **+10.9%/yr**; **Bull** EPS $17.50 @ 35x → **+23.5%/yr**.

**scenario_returns_3y (annualised, price only, no dividend): bear -4.1%/yr, base +10.9%/yr, bull +23.5%/yr.**

## 8. Bull case / bear case

**Bull (3):**
1. 22 consecutive quarters of 20%+ SaaS growth on an 86.7%-recurring revenue base is a genuinely long,
   hard-to-manufacture streak — the moat (multi-decade government contracts, extreme switching costs) is
   evidenced, not asserted.
2. Reverse DCF shows the market pricing in ~1.9%/yr FCF growth against a company that has guided (and twice
   raised guidance to) mid-teens non-GAAP EPS growth this year alone.
3. For The Record extends Tyler's Courts & Justice footprint into digital court recording/AI transcription —
   a logical, moat-reinforcing bolt-on, not a diversifying distraction.

**Bear (3):**
1. The shift from near-zero leverage to a $1.4bn convert used mainly to fund buybacks (not organic growth)
   changes the risk profile; if SaaS growth or margins disappoint, Tyler now carries balance-sheet risk it did
   not have a year ago.
2. Non-GAAP operating margin contracted 80bp YoY in the most recent quarter despite record revenue and FCF — a
   real margin-quality question, not yet resolved, that bears directly on whether the "Rule of 40" profile is
   improving or eroding.
3. Courts/justice software implementation failures tied to wrongful arrests/detentions have recurred roughly
   every 2–3 years historically; a repeat event carries real reputational and contract-renewal risk that is
   structurally different from a typical enterprise-SaaS churn risk.

## 9. Key risks & kill criteria (measurable)

1. SaaS revenue growth falls below 15% YoY for two consecutive quarters (vs. 20%+ sustained for 22 straight
   quarters through Q2 2026).
2. FY2026 non-GAAP diluted EPS finishes below the guided $12.95–13.20 range at year-end.
3. Net debt/EBITDA rises above 2.5x (currently ≈1.06x) without a corresponding FCF acceleration.
4. A material software-failure incident tied to Tyler's Odyssey/Enterprise Justice or related courts products
   (e.g., another wrongful-detention/arrest event) results in a contract termination, new material litigation,
   or regulatory action.
5. Non-GAAP operating margin contracts more than 100bp YoY for two consecutive quarters (it contracted 80bp in
   Q2 2026).

## 10. Catalysts & calendar

- Next earnings: **Q3 2026, ~28-Oct-2026** (per quant snapshot; not independently re-confirmed against a fresh
  IR calendar posting in this pass).
- New $1.5bn share-repurchase authorization announced with Q2 2026 results (29-Jul-2026) — a capital-allocation
  signal to track against the new leverage.

## 11. Red-flag scan

- **Litigation:** recurring, sector-specific pattern described in Section 6 (Alameda County 2016, Lubbock
  County 2021, North Carolina class action 2023); a case captioned "White v. Tyler Technologies, Inc." was
  noted in search results dated 27-Jul-2026 but its substance was not independently confirmed in this pass —
  flagged as an open item, not a resolved finding. A long-running dispute with a state-government client over
  ~$15M in contractually owed fees (litigation reinitiated 20-Mar-2024) remains a smaller, contained item.
- No auditor changes, restatements, or going-concern language found in this review.
- No SEC investigation found in the sources checked.
- Convertible-note capped-call structure and the $1.5bn buyback authorization are disclosed capital-markets
  activity, not concealment.

## 12. Data basis, recency and disclaimer

Most recent period incorporated: **Q2 2026 10-Q (quarter ended 30-Jun-2026), filed 29-Jul-2026**, plus the
Q2 2026 earnings release (29-Jul-2026) and the FY2025 10-K (filed 18-Feb-2026). Checked for events to
2026-09-25. GAAP figures are labelled GAAP; non-GAAP figures are management's own measures as disclosed in
earnings releases, not independently reconciled line-by-line. Q4 2024/Q4 2025 GAAP EPS are disclosed
approximations (FY total minus reported Q1–Q3). **This is research, not personalized investment advice; consult a licensed financial advisor before acting on it.**

## 13. Sources

1. SEC EDGAR submissions/companyfacts, CIK 0000860731 (data.sec.gov), retrieved 2026-09-26.
2. Tyler Technologies Q2 2026 earnings release (29-Jul-2026): sec.gov/Archives/edgar/data/0000860731/000086073126000048/a991earningsrelease-6302026.htm
3. Tyler Technologies Q1 2026 earnings release (29-Apr-2026): sec.gov/Archives/edgar/data/860731/000086073126000031/a991earningsrelease-3312026.htm
4. Tyler Technologies Q4/FY2025 earnings release (19-Feb-2026): sec.gov/Archives/edgar/data/860731/000086073126000013/a991earningsrelease12312025.htm
5. Tyler Technologies convertible notes closing press release (14-May-2026): sec.gov/Archives/edgar/data/0000860731/000086073126000040/tylexhibit991closingpr51426.htm
6. "Tyler Technologies to Acquire For The Record" (businesswire.com, Feb-2026) and completion release (Apr-2026).
7. Wikipedia "Tyler Technologies" (litigation history summary, cross-checked against Yale Law Journal essay
   "Enterprise Justice: Tyler Technologies and the Privatizing Court" and classaction.org news index) — secondary
   sources used to identify the litigation pattern; primary court filings not individually pulled given the
   time-box, flagged as a limitation.
8. v4/data/b1_live_scores.csv, v4/data/d4_live_snapshot.parquet (quant context, retrieved this session).
9. finance-skills stock-analysis skill (`references/sectors/it-saas.md`) and `scripts/valuation.py`.

## Correction (verification DV41, 2026-10-08)

Research only; not personal advice. Original text above is unchanged. Verification by auditor DV41 against SEC EDGAR primary sources (8-K Ex-99.1 releases, 10-Q/10-K, XBRL companyfacts). Items not listed here were checked and tied (see v4/outputs/dv/DV41_factcheck.json).

1. **Wrong:** Debt ~$1,455.0M, net debt ~$485.0M, TTM EBITDA $458.5M, net debt/EBITDA ~1.06x
   **Correct:** Convertible notes due 2031 carrying $1,408.7M (face $1,437.5M); cash + ST investments $970.0M; net debt $438.7M; TTM EBITDA $505.6M (adjusted $672.7M); ratio 0.87x (0.65x adjusted)
   **Source:** Ex-99.1 acc 0000860731-26-000048 balance sheet and EBITDA reconciliation; acc -26-000013 (FY25 EBITDA $495.2M); acc -26-000031 (Q1)
   **Verdict effect:** no

2. **Wrong:** 'Leverage went from near-zero to a new $1.4375bn convertible'; Q2 buybacks implied ~$320.7M
   **Correct:** The convert partly refinanced a $599.7M convertible due 2026 repaid in Q1 2026 ($600.0M); Q2 2026 repurchases were $505M; the company moved from net cash (~$497M) to net debt ~$439M
   **Source:** Ex-99.1 acc 0000860731-26-000048 (balance sheet, cash flow, CFO quote)
   **Verdict effect:** no

3. **Wrong:** Reverse DCF ~1.9%/yr: WACC 8.5% on EV, FCF $705.9M described as SBC-net, 4% terminal
   **Correct:** Company FCF adds back SBC. On the programme basis (Ke 8.85% = 5.17% + Blume beta 0.889 x 4.14%; equity $13.33B; FCF after SBC $550.1M; 10 years then 3.0%) implied growth is 7.2%/yr (6.3% at Ke 8.5%). Implied vs base restated below -> in line
   **Source:** Release SBC lines acc 0000860731-26-000048; programme parameters (10-yr 5.17% on 25 Sep 2026)
   **Verdict effect:** implied_vs_base below -> in_line; verdict INCLUDE-SMALL unchanged

4. **Wrong:** FY2025: revenue $2,300M
   **Correct:** FY2025 revenue $2,332.3M
   **Source:** 10-K acc 0000860731-26-000016 XBRL
   **Verdict effect:** no

**Verdict:** unchanged.
