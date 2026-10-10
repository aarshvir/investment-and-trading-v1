# KEY — KeyCorp (Diligence dossier, agent F76, standard depth)

## 1. Verdict
**INCLUDE-SMALL** (24–36 month horizon), with a named reservation: the thesis depends on net interest income (NII) continuing to re-price upward and on credit costs staying benign through the rest of the rate cycle — both plausible on the primary-source trend below but not yet fully proven over a full cycle. KeyCorp is a mid-size regional bank (Cleveland, OH) working through the back half of a securities-portfolio repositioning that produced a large one-time GAAP loss in Q3 2024, funded in part by a $2.8bn strategic equity investment from The Bank of Nova Scotia (Scotiabank). Eight straight quarters of primary-source XBRL data show NII rising every single quarter since the repositioning — a durable, filing-confirmed trend, not a one-off. No V1 systematic valuation row exists for KEY (bank valuation methodology differs; not run by V1) — `v1_verdict` = null.

## 2. Business in plain English
KeyCorp is the holding company for KeyBank, National Association, a regional bank operating mainly in the Northeast, Midwest, Mountain West and Pacific Northwest. It gathers consumer and commercial deposits and lends them out (net interest income), and earns fees from investment banking/capital markets, wealth management, and commercial payments (noninterest income). It is a "Category IV" bank under the Fed's tailoring rules (not a global systemically important bank), subject to standardized — not advanced — capital rules.

## 3. Why the model likes it — durable or artefact?
b1 (2026-09-25): composite decile 4/10, quintile 2, live_rank 322 — mid-pack, not a top-decile quant name; the triage-advance reason (`Q06_triage.json`) cited "+25% forward EPS growth and 10x NTM P/E" off a bank "still in the early innings of a margin recovery," flagging that ROE (10.3%) is only middling. Raw factor picture: ep (earnings yield) 0.092 (pct file not re-derived here), bp (book/price) raw 0.900 — high, consistent with trading below book on a P/B basis typical of a bank still normalizing ROE; mom_12_1 raw 0.192 — a real positive twelve-month price move, not a momentum artefact, corroborated below by the primary-source earnings trend. **This is durable, not an artefact**: it is the direct, dated, filing-confirmed consequence of (a) an Aug 12, 2024 Investment Agreement with Scotiabank (primary source: 8-K filed 2024-08-13, accession 0001193125-24-199332) that recapitalized the balance sheet, and (b) a securities-portfolio repositioning that shows up in the XBRL data as eight consecutive quarters of NII growth (§4) — a mechanical, arithmetic re-pricing effect, not sentiment or multiple expansion.

## 4. Last two years of results (calendar quarters; consolidated KeyCorp; source: 10-Q "Condensed Consolidated Statements of Income" and XBRL companyfacts, CIK 0000091576)
| Quarter | Total revenue ($M, `Revenues` tag) | Net interest income ($M) | Provision for credit losses ($M) | Net income (loss) attrib. to KeyCorp ($M) | Diluted EPS |
|---|---|---|---|---|---|
| Q3 2023 | 1,566 | 915 | 81 | 303 | $0.29 |
| Q1 2024 | 1,533 | 875 | 101 | 219 | $0.20 |
| Q2 2024 | 1,526 | 887 | 100 | 274 | $0.25 |
| Q3 2024 | 695* | 952 | 95 | **(410)** | **($0.47)** |
| Q1 2025 | 1,773 | 1,096 | 118 | 405 | $0.33 |
| Q2 2025 | 1,840 | 1,141 | 138 | 425 | $0.35 |
| Q3 2025 | 1,895 | 1,184 | 107 | 489 | $0.41 |
| Q1 2026 | 1,953 | 1,222 | 106 | 522 | $0.44 |
| **Q2 2026** | **1,964** | **1,250** | **92** | **509 (XBRL) / $472 attrib. to common per 8-K)** | **$0.44** |

*Q3 2024's low "Revenues" XBRL figure and the ($410)M net loss reflect a large, deliberate loss realized on selling lower-yielding available-for-sale securities as part of a balance-sheet repositioning, executed alongside the Scotiabank capital raise — confirmed primary-source: KeyCorp's own Q3 2024 disclosures and the subsequent, uninterrupted rise in NII every quarter since (887→952→1,096→1,141→1,184→1,222→1,250) is the expected, mechanical payoff of that trade (higher-yielding reinvestment), not an accounting artefact.
Q2 2026 net interest margin **2.89%**, up 2bps sequentially; net charge-offs **42bps**; allowance coverage ratio **1.56%** (down 4bps sequentially) — source: KeyCorp Q2 2026 earnings release, filed 2026-07-21 (accession 0000091576-26-000017), "KEYCORP REPORTS SECOND QUARTER 2026 NET INCOME OF $472 MILLION."

## 5. Guidance track record
KeyCorp's 8-K earnings-release exhibits (last four: 2026-07-21, 2026-04-16, 2026-01-20, 2025-10-16) contain **no explicit forward point or range guidance for revenue or EPS** in the press-release text itself (only boilerplate forward-looking-statement language) — confirmed by direct text search of all four exhibits. Like several large banks (see WFC dossier, same finding), KeyCorp appears to give qualitative NII/expense trajectory commentary on its earnings call rather than in the release; that call commentary is **not independently verified here at standard depth**. Per the addendum's own instruction, this is disclosed rather than assumed.

## 6. Earnings quality & balance sheet
**Entity scope: unless noted, all capital ratios below are KeyCorp (the consolidated bank holding company); KeyBank, National Association (the subsidiary bank) is confirmed separately, in the same filing, to be "well capitalized" under the Prompt Corrective Action framework, but its own numeric ratios are not separately quoted in the passage reviewed.** Source: KeyCorp 10-Q for the quarter ended 2026-06-30, filed 2026-08-04 (accession 0001628280-26-052671), "Capital adequacy," Figure 1/Figure 2.

- **Capital (KeyCorp, consolidated, fully phased-in Basel III, estimated as of 2026-06-30):** Common Equity Tier 1 **11.17%** (regulatory minimum + stress capital buffer 7.70%); Tier 1 **12.78%** (min+buffer 9.20%); Total Capital **14.82%** (min+buffer 11.20%); Leverage **10.32%** (min 4.00%). All ratios comfortably above requirement, and KeyBank (consolidated) is separately confirmed "well capitalized."
- **Deposits (consolidated, XBRL instant):** $145.7bn (Jun 2024) → $149.8bn (Dec 2024) → $146.9bn (Jun 2025) → **$153.1bn (Jun 2026)** — deposits grew through the repositioning, not away from it.
- **Total assets** $187.5bn (Jun 2024) → **$191.3bn (Jun 2026)**; total liabilities $172.7bn → $171.5bn over the same period while stockholders' equity rose from **$14.8bn to $19.8bn** — the jump from $14.8bn (Jun 2024) to $16.9bn (Sep 2024) to $18.2bn (Dec 2024) is the balance-sheet-level footprint of the Scotiabank capital raise plus retained earnings, confirmed against the 8-K terms below.
- **Scotiabank Investment Agreement (dated 2024-08-12; 8-K filed 2024-08-13, accession 0001193125-24-199332):** Bank of Nova Scotia purchases, in two closings, common shares that together represent **~14.9% (up to 14.99%)** of KeyCorp's outstanding common shares, at a fixed price of **$17.17/share**, for aggregate consideration of **~$2.8bn**. Scotiabank receives **two board seats** upon the second closing and a proportional-representation right down to a 5% ownership floor, subject to a one-year transfer restriction/standstill. Scotiabank also has a pro-rata "true-up" right to participate in KeyCorp's buybacks (confirmed active: $49M of the $341M repurchased in Q2 2026 came from Scotiabank under this right — 10-Q for the quarter ended 2026-06-30).
- **Capital return:** quarterly common dividend **$0.205/share** (Q2 2026; dividend yield ≈ 4.0% on the $20.61 close). Board authorized a new **$3.0bn** share-repurchase program (replacing a $1.0bn authorization); **$341M repurchased in Q2 2026 alone** (~16 million shares) — an aggressive pace (~1.5% of market cap per quarter).
- **Preferred stock outstanding** (Series D/E/F/G/H, $2.5bn aggregate liquidation preference, book value ~$2.45bn net of capital surplus) — a real, senior claim ahead of common dividends; coupons 5.0–6.2%.
- No net-debt/EBITDA metric applies to a bank; leverage is governed by the capital ratios above, all of which sit well above regulatory minimums.
- **Credit quality:** net charge-offs 42bps (Q2 2026) and allowance coverage 1.56% — no deterioration signal in the reviewed data; provision for credit losses has ranged $92–138M over the last five quarters without a clear upward trend.

## 7. Valuation snapshot and reconciliation with V1
- **No V1 row exists for KEY** (`v1_valuation_table.csv` has no KEY entry — bank valuation methodology differs, not run by V1). Per the wave-4 instruction, `v1_verdict` = **null**.
- Market data (b1_live_scores.csv / d4_live_snapshot.parquet, 2026-09-25 close): price $20.61; trailing P/E 12.05x; forward P/E 9.65x; NTM P/E (calendarised) 10.03x; consensus 12-month mean target $25.82 (median $25.00, 19 analysts, "buy" consensus) — ~25–27% implied upside on consensus alone; beta 1.023.
- **My own reverse DCF** (EPS-based two-stage model; EPS0 = NTM consensus non-GAAP EPS ≈ $2.06 [d4 `eps_ntm`]; cost of equity ≈ 10.0% [rf ≈4.2% + beta 1.02 × ~5.5% bank equity premium] **[Corrected 2026-10-08: rf was 5.17% on 25 Sep 2026 and a bank should be valued on P/TBV-ROTCE: P/TBV 1.51x implies sustained ROTCE of ~12-14% vs 12.9% now; in_line still fair, see Correction section]**; 10-year explicit growth, exit multiple 11x [KeyCorp's own pre-2022 historical average forward P/E, a normalized bank multiple]; solved against $20.61 close): **implied 10-year EPS growth ≈ 9%/yr**.
- **My bear/base/bull (10-yr EPS growth), evidence-based:**
  - **Bear** (NIM/rate cycle turns unfavorably before the repricing trade is complete, a credit cycle turn — regional-bank CRE exposure is an industry-wide risk not yet tested here — buyback pace slows): ≈ 2–4%/yr.
  - **Base** (the securities-repricing tailwind (NII up every quarter for 2 years running) continues for another 1–2 years before normalizing, loan growth (C&I +3% QoQ in Q2 2026) continues at a moderate pace, buybacks continue near the current ~5–6%/yr share-count reduction pace): ≈ 7–8%/yr.
  - **Bull** (NIM expansion continues faster than expected, Scotiabank partnership adds fee/capital-markets revenue synergies, credit stays benign, buybacks stay this aggressive): ≈ 10–12%/yr.
  - **The ~9%/yr implied growth sits at the top of my base case / bottom of my bull case** — not obviously cheap, but not paying for more than a credible (if optimistic) continuation of the confirmed recovery trend. `implied_vs_base` = **in_line**.
- valuation_view_vs_v1: no v1 row to reconcile against (null); dossier_view = **fair**.

## 8. Bull case
1. NII has risen for **eight consecutive quarters** **[Corrected 2026-10-08: nine consecutive increases once the omitted Q4-24 ($1,051M) and Q4-25 ($1,215M) are included]** ($875M→$1,250M, Q1 2024 to Q2 2026), a primary-source-confirmed, mechanical payoff of the 2024 securities-portfolio repositioning — not a hoped-for outcome but a trend already in the filings.
2. Capital is unusually strong for the valuation on offer: CET1 11.17% vs. a 7.70% requirement, plus a $2.8bn strategic anchor investor (Scotiabank, 2 board seats) that both de-risks the capital base and creates an active buyback counterparty.
3. Aggressive, funded capital return: a new $3.0bn buyback authorization, $341M repurchased in a single quarter (Q2 2026), plus a ~4.0% current dividend yield.

## 9. Bear case
1. Middling profitability: ROE (b1, 10.3%) is only average for a regional bank; the ~9%/yr implied growth requires the NIM-recovery trend to keep compounding rather than plateau, which is not yet proven over a full rate cycle.
2. The Q3 2024 ($410M) net loss shows KeyCorp is willing to take large, deliberate GAAP losses to reposition its balance sheet — a strategy that worked this time, but a repeat under worse market conditions (e.g., higher rates prevailing longer) could be costlier.
3. Regional-bank commercial real estate exposure is an industry-wide, not yet independently stress-tested (at standard depth) risk; a credit cycle turn would show up first in the net-charge-off and allowance-coverage lines tracked in §10 below.

## 10. Key risks & kill criteria (measurable)
1. Net interest income (consolidated, quarterly) **falls quarter-over-quarter for two consecutive quarters** (vs. eight straight quarters of increases through Q2 2026) — the core repricing thesis breaking.
2. CET1 ratio (KeyCorp, consolidated) **falls below 9.5%** (vs. 11.17% now and a 7.70% regulatory minimum+buffer) — capital being deployed too aggressively into buybacks/growth.
3. Net charge-offs (consolidated, quarterly) **exceed 75bps** for two consecutive quarters (vs. 42bps now) — early credit-cycle-turn signal.
4. Diluted EPS growth YoY **turns negative** for two consecutive quarters (excluding the already-disclosed Q3 2024 repositioning loss) — recovery thesis broken.
5. Scotiabank **reduces its stake below 5%** or the board-representation/standstill terms are renegotiated adversely — would remove the strategic-anchor support the bull case partly relies on.

## 11. Catalysts & calendar
- Next earnings: **Q3 2026, Tuesday 2026-10-20** (b1_live_scores/d4_live_snapshot, confirmed not an estimate).
- Scotiabank's board nominees and any further "true-up" buyback participation are disclosed each quarter in the 10-Q's capital/equity notes.

## 12. Red-flag scan
- **Litigation:** the 10-Q's "Legal Proceedings" note (2026-06-30 10-Q) describes only ordinary-course litigation/investigations; KeyCorp states it does not believe any matter, individually or in aggregate, would have a material adverse effect — **no named material litigation found** in the reviewed filing (contrast with MDT and MCHP dossiers in this batch, both of which do have named material items).
- **Regulatory:** none identified in the reviewed 10-Q beyond routine bank-regulatory-capital disclosure; KeyBank (consolidated) is confirmed "well capitalized."
- **One-off/accounting:** the Q3 2024 ($410M) net loss is a real, disclosed, deliberate securities-repositioning loss, not a restatement or accounting irregularity; no auditor change, material weakness, or going-concern language found.
- **Capital structure:** $2.5bn of preferred stock outstanding (senior to common dividends); Scotiabank's 14.9–14.99% stake and board seats are a governance concentration worth monitoring, though the Investment Agreement's transfer restrictions/standstill are disclosed and were negotiated, not adverse.
- No pending M&A found.

## 13. Sources
1. KeyCorp 10-Q for the quarter ended 2026-06-30, filed 2026-08-04, accession 0001628280-26-052671 ("Capital adequacy" Figures 1–2, Legal Proceedings, Scotiabank repurchase "true-up" disclosure): https://www.sec.gov/Archives/edgar/data/91576/000162828026052671/key-20260630.htm
2. KeyCorp 8-K, event date 2024-08-12, filed 2024-08-13, accession 0001193125-24-199332 (Investment Agreement with The Bank of Nova Scotia, Item 1.01): https://www.sec.gov/Archives/edgar/data/91576/000119312524199332/d750641d8k.htm
3. KeyCorp Q2 2026 earnings release, exhibit 99.1 to 8-K filed 2026-07-21, accession 0000091576-26-000017: https://www.sec.gov/Archives/edgar/data/91576/000009157626000017/a2q26earningsrelease.htm
4. SEC XBRL companyfacts, CIK0000091576: https://data.sec.gov/api/xbrl/companyfacts/CIK0000091576.json
5. SEC submissions, CIK0000091576: https://data.sec.gov/submissions/CIK0000091576.json
6. v4/data/b1_live_scores.csv (row KEY, as_of 2026-09-25); v4/data/d4_live_snapshot.parquet (row KEY); v4/outputs/Q06_triage.json (KEY entry); v4/outputs/v1_valuation_table.csv (no KEY row — confirmed absent).

## 14. Data basis, recency and disclaimer
Most recent period incorporated: 10-Q for the quarter ended **2026-06-30**, filed 2026-08-04. Events checked to 2026-09-25 close. All figures GAAP unless labelled "consensus"/"NTM" (analyst estimates, from d4_live_snapshot, sourced from Yahoo/analyst consensus, cross-check only — not independently re-derived at standard depth). Bank-appropriate capital metrics (CET1, Tier 1, Total Capital, Leverage) are used in place of net-debt/EBITDA per the sector playbook. Research, not investment advice; not personalised financial advice.

## Correction (verification DV24, 2026-10-08)
**Scope:** checked against the 21 Jul 2026 earnings release (Ex-99.1 acc 0000091576-26-000017), 10-Q acc 0001628280-26-052671 and companyfacts. Facts file: `outputs/dv/DV24_factcheck.json`. No verdict or implied_vs_base change.

**1. Valuation method (FAIL, conclusion survives).** Wrong text: reverse DCF with "rf about 4.2% + beta 1.02 x about 5.5% bank equity premium" and an 11x exit multiple on consensus EPS. The program rule is a 10-year Treasury of 5.17% (25 Sep 2026) plus a stated ERP, and banks are valued on P/TBV against ROTCE. From the release: tangible book value per share $13.62, ROTCE 12.89% (Q2), P/TBV at $20.61 = 1.51x. Implied sustained ROTCE = g + P/TBV x (Ke - g): 12.2-12.4% at Ke 9.4% (5.17% + 1.02 x 4.14% ERP; beta from the dossier), 13.1-13.3% at 10.0%, 14.3-14.5% at 10.8%. Against ROTCE of 12.9% now and the company's stated target of more than 15% by year-end 2027 (omitted from the dossier), "in_line" remains a fair call. Verdict INCLUDE-SMALL unchanged.

**2. Minor.** The statement "eight consecutive quarters" of rising NII undercounts: the table omits both Q4 quarters (derived Q4-24 NII $1,051M, Q4-25 $1,215M); NII rose in each of the nine sequential steps from Q1-24 ($875M) to Q2-26 ($1,250M). CET1 fell 20bp sequentially (11.4% to 11.2%). The mechanical flag (472 vs 509) is a correctly labelled preferred-dividend difference, not an error.
