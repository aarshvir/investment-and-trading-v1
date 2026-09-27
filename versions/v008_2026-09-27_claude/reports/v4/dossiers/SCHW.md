# SCHW — The Charles Schwab Corporation (F47, wave-2 diligence)

## 1. Verdict
**INCLUDE-SMALL** (half weight), thesis horizon 24–36 months. Reason: the largest US discount brokerage/custodian is compounding revenue and EPS at an unusually high rate (Q2 2026 revenue +21% YoY, adjusted EPS +42% YoY) with net interest margin still guided to expand further into Q4 2026 — but the named reservation is that a large share of this growth is **NIM mean-reversion and post-TD-Ameritrade deleveraging**, not a repeatable annual rate, plus an unresolved cash-sweep class action.

## 2. Business in plain English
Charles Schwab is the largest US retail brokerage/custodian by client assets, serving self-directed investors, registered investment advisors (RIA custody) and workplace-plan participants. It earns money three ways: net interest revenue on client cash swept into its affiliated bank and on securities-based/margin lending; asset-management and administration fees (proprietary funds, advisory programs); and trading revenue (commissions are largely zero for stock/ETF trades, so this is mostly options/futures and order-flow-related revenue). It completed its ~$26B acquisition of TD Ameritrade in 2020, and the last several years have been about realizing the scale/cost synergies from that integration while normalizing net interest margin after the 2022–23 rate shock.

## 3. Why the model liked it — durable or artefact?
Triage (Q05, quality 4/5, growth 4/5, price_vs_growth 4/5): "43% eps growth and 38.8% margins as integration synergies flow through, at only 13.3x forward earnings." b1 quant: composite **0.760** (decile 8, live_rank 120 — comfortably in the model's better tier), fam_S (earnings momentum) **0.883**, fam_Q 0.597, fam_M 0.599, fam_V only 0.322 (weakest family — SCHW does not screen as statistically "cheap" on the model's value factors, consistent with its ~18x trailing GAAP multiple). **Durability check:** the EPS growth is a blend of (a) durable organic growth — net new client assets, RIA custody share gains, buyback-driven share count reduction — and (b) a large, partly mechanical NIM-recovery/deleveraging effect: management's own Q2 2026 commentary attributes the 12bp sequential NIM expansion to "growth in margin and bank lending... reduced aggregate use of wholesale funding and lower rates paid on most funding sources" — i.e., paying down the expensive wholesale/supplemental funding taken on to bridge TD Ameritrade integration and cash-sorting outflows. That tailwind is finite; once wholesale funding is fully unwound and NIM reaches its guided ~3.25–3.30% Q4 2026 exit rate, the growth rate should decelerate toward the durable organic component.

## 4. Last two years of results (GAAP, USD millions except EPS; SEC 10-Q/10-K, XBRL companyfacts)
| Quarter | Revenue | YoY | Net income | GAAP diluted EPS |
|---|---|---|---|---|
| Q3'23 | 4,606 | — | 1,125 | 0.56 |
| Q1'24 | 4,740 | — | 1,362 | 0.68 |
| Q2'24 | 4,690 | — | 1,332 | 0.66 |
| Q3'24 | 4,847 | +5.2% | 1,408 | 0.71 |
| Q4'24* | 5,329 | — | 1,840 | n/a (derived) |
| Q1'25 | 5,599 | +18.1% | 1,909 | 0.99 |
| Q2'25 | 5,851 | +24.8% | 2,126 | 1.08 |
| Q3'25 | 6,135 | +26.6% | 2,358 | 1.26 |
| Q4'25* | 6,336 | +18.9% | 2,459 | n/a (derived) |
| Q1'26 | 6,482 | +15.8% | 2,479 | 1.37 |
| Q2'26 | 7,072 | +20.9% | 2,800 | 1.54 |

\*Q4'24/Q4'25 figures are derived (annual 10-K total minus the three reported 10-Q quarters) — shown as an estimate, not a separately filed discrete-quarter tag.

Q2 2026 (10-Q/8-K, filed 2026-08-07): total revenue $7.1B (+21% YoY, a record); adjusted EPS $1.62 (+42% YoY); GAAP diluted EPS $1.54. **Net interest margin 3.00%, up 12bp QoQ**, "primarily due to the growth in margin and bank lending... and reduced aggregate use of wholesale funding" (company's own attribution, quoted). Client transactional sweep cash ended June at $485.7B, +$24.2B QoQ (tax-season seasonality + organic growth + client allocation decisions).

## 5. Guidance track record (quote the numbers; versus prior)
Schwab has **raised guidance twice in 2026** on both revenue and NIM — a genuine "beat and raise," quoted rather than asserted:
- At its **May 2026 Investor Day**, management guided full-year 2026 revenue growth of **14%–15%**.
- By the **Q2 2026 release (2026-07-21)**, that was **raised to 17.5%–18.5%** full-year revenue growth.
- Full-year 2026 **net interest margin guidance was raised to a range of 3%–3.10%**, with an **average Q4 2026 NIM expected at 3.25%–3.30%** (i.e., management is explicitly guiding to a rising exit rate, not a plateau).
This is a clean, quotable, verifiable raise (source: company earnings-call commentary and release, cross-checked across two independent summaries) — but note it also means the market has already been told to expect the acceleration seen in Q1–Q2 2026; the open question for the reverse DCF (§7) is what happens once the Q4 2026 exit NIM is reached and the "reduced wholesale funding" tailwind is exhausted.

## 6. Earnings quality & balance sheet
- **Cash conversion / FCF:** per the sector playbook, operating cash flow for a bank/broker is dominated by client deposit and loan-book movements and is **not a meaningful FCF signal** — not used as a primary valuation input here.
- **Balance sheet (2026-06-30, 10-Q):** total assets $517.3B, total liabilities $467.1B, stockholders' equity $50.1B (~9.7% equity/assets). Cash & equivalents $40.6B (elevated, consistent with the seasonal sweep-cash inflow noted above). Long-term debt + capital leases (including current maturities) **$22.7B**, up from $20.2B a year earlier — debt has grown, not shrunk, even as "wholesale funding" language suggests deleveraging elsewhere in the funding stack; this is a mild internal tension worth flagging as a data point to watch, not yet a red flag.
- **AFS securities unrealized losses (the SVB-era legacy issue):** the accumulated unrealized loss on available-for-sale debt securities was **$4.385B at 2025-09-30, improving to $3.869B (Dec'25), $3.862B (Mar'26) and $3.850B (Jun'26)** — a steadily shrinking mark, now ≈7.7% of stockholders' equity (down from a materially larger share in the 2022–23 rate-shock period). This is the single most important bank-sector-specific metric per the playbook (duration mismatch risk), and the trend is favorable and improving, not deteriorating.
- **Regulatory capital:** CET1 ratio 26.3% (2026-03-31) — "well in excess of the regulatory minimum of 4.5% combined with the [stress capital buffer] of 2.5%"; consolidated Tier 1 leverage ratio 8.9% (Q1'26, down from 9.3% at year-end 2025) and 8.7% (Q2'26, preliminary), well above regulatory minimums. Schwab disclosed its 2026 CCAR/stress-test results without a capital-distribution constraint noted in the sources reviewed.
- **Capital return:** dividend $1.28/share annualized (1.19% yield at 2026-09-25 close); active buyback programme (not separately quantified this pass).
- **SBC:** ~$126–138M/quarter in Q1 2025/Q1 2026, small relative to revenue (~2%).

## 7. Valuation snapshot and reverse DCF
V1 systematic valuation table (`v4/outputs/v1_valuation_table.csv`) and `v1_valuation.json` **have no SCHW row** — SCHW was not in the 69-name V1 universe, so **v1_verdict = null**; nothing to reconcile against.

- Price 2026-09-25 close: **$99.03**; market cap **$171.26B**; shares out 1,729.3M.
- Trailing GAAP P/E ≈ 17.7x on TTM diluted EPS (Q3'25 1.26 + Q4'25 ~1.42 derived + Q1'26 1.37 + Q2'26 1.54 ≈ $5.59), close to the quant snapshot's 18.04x trailing figure. NTM P/E per the quant snapshot ≈ 12.6–13.3x — a large trailing-to-forward gap consistent with the market already expecting the EPS growth to continue near-term.
- Per the sector playbook, a bank/broker-custodian is properly benchmarked on ROE-vs-COE and P/TBV rather than FCFF DCF; a full P/B build was not completed this pass (time-boxed).
- **Reverse DCF** (own build, earnings-based two-stage): assuming a **10.5% cost of equity** (CAPM: rf ≈4.2%, ERP 5.5%, beta ≈1.15 for a scaled, diversified brokerage/bank) and a 3% terminal growth rate after year 10, the **$171.3B market cap implies roughly 5.9%/yr (TTM-NI-based) to 7.7%/yr (FY2025-NI-based) sustained 10-year net-income growth.** My evidence-based base case — durable organic net-new-asset growth plus buybacks giving mid-single-digit underlying EPS growth, *plus* a genuine but temporary NIM-recovery tailwind through the guided Q4 2026 exit rate that then flattens — nets to **~9–11%/yr** over 10 years if the near-term NIM tailwind is given even partial credit, but only **~5–7%/yr** if it is excluded as non-repeatable. **This straddles the implied range rather than clearing it cleanly**, which is exactly why the verdict is INCLUDE-SMALL rather than INCLUDE: on the more optimistic base case the stock is cheap (implied below base), but on the more conservative "normalize away the funding-cost tailwind" base case it is roughly fairly priced (implied in line). **valuation_view_vs_v1.implied_vs_base = "below"** (using the mid-point base case of ~9%, above the ~6–8% implied range), with the reservation stated explicitly rather than averaged away.
- Peers (directional only, not independently re-pulled this pass): Interactive Brokers (IBKR), LPL Financial (LPLA), Morgan Stanley's wealth-management segment — SCHW's mid-to-high-teens trailing multiple sits broadly in line with this peer set for a business of its scale and franchise quality.

## 8. Bull case / bear case
**Bull (3):**
1. Two consecutive guidance raises in 2026 (revenue growth 14–15% → 17.5–18.5%; full-year NIM raised, with a guided Q4 2026 exit NIM of 3.25–3.30%, still rising) show genuine, quoted operating momentum, not a one-off beat.
2. The AFS unrealized-loss overhang from the 2022–23 rate shock is steadily shrinking (~$4.4B → ~$3.85B over four quarters, now ~7.7% of equity) — the balance-sheet risk that dogged the stock in 2023 is measurably resolving, not worsening.
3. Regulatory capital is strong and improving in absolute dollar terms (CET1 $36.5B, Tier 1 capital $42.8B at 2026-06-30) — no capital-raise or dividend-cut risk visible in the disclosures reviewed.

**Bear (3):**
1. A material share of the recent EPS acceleration is attributable to NIM recovery and reduced wholesale-funding cost — management's own words — which is a mean-reversion effect with a visible end point (the guided Q4 2026 exit NIM), not a structurally repeatable growth driver; the reverse DCF is genuinely ambiguous once this is excluded.
2. Long-term debt + capital leases actually **grew** YoY ($20.2B → $22.7B) even as management describes "reduced wholesale funding" — worth reconciling in a deeper pass rather than treating as fully resolved.
3. An active cash-sweep class action alleges Schwab used client sweep cash economics to help finance the TD Ameritrade acquisition and takes an "outsized" share of the spread; early related cases against Schwab were dismissed, but litigation continues, and the SEC has broadened scrutiny of cash-sweep programs industry-wide (Morgan Stanley and Wells Fargo have disclosed their own SEC investigations) — an unresolved legal/regulatory overhang with an uncertain financial outcome.

## 9. Key risks & kill criteria — thesis-invalidation triggers (measurable, would break the thesis; verbatim into summary JSON)
1. "Full-year net interest margin fails to reach the guided 3.00%–3.10% range for FY2026, or the guided Q4 2026 exit NIM of 3.25%–3.30% is not achieved" (a miss here would confirm the NIM-recovery bull case was over-extrapolated).
2. "Accumulated AFS unrealized loss position rises back above $5B or above 10% of stockholders' equity" (currently ~$3.85B / ~7.7%, trending down; a reversal would be a genuine balance-sheet red flag per the sector playbook).
3. "Long-term debt + capital lease obligations rise above $28B without a disclosed, NIM-accretive rationale" (currently $22.7B, already up YoY — this is the metric to watch for the debt/wholesale-funding tension noted in §8).
4. "The cash-sweep litigation results in a certified class and/or a disclosed reserve/settlement exceeding $500M" (scaled to SCHW's larger size versus the RJF equivalent trigger).
5. "Consolidated Tier 1 leverage ratio falls below 7.5%" (currently 8.7–8.9%, trending down slightly QoQ — worth monitoring, not yet a breach).

## 10. Catalysts & calendar
- Next earnings: **2026-10-15** (Q3 2026, per the quant snapshot's Yahoo calendar field).
- Q4 2026: the guided NIM exit rate of 3.25%–3.30% is the single most falsifiable near-term test of the bull case.
- Ongoing: cash-sweep litigation docket; any further SEC scrutiny of sweep-cash programs industry-wide.

## 11. Red-flag scan
- **Litigation:** active putative class action(s) alleging fiduciary breach and "outsized benefits" from the cash-sweep program, including a claim that sweep-cash economics helped fund the TD Ameritrade deal; some earlier related claims against Schwab were dismissed, but litigation continues as of 2026 (source: Bloomberg Law, ThinkAdvisor, Law360, Top Class Actions, Citywire coverage, cross-checked against multiple independent outlets — not yet independently verified against SCHW's own 10-Q litigation note text in this pass, flagged as a gap).
- **Regulatory:** the SEC has broadened scrutiny of cash-sweep programs industry-wide (peer disclosures at Morgan Stanley, Wells Fargo); no SCHW-specific enforcement action or investigation was identified in the sources reviewed, but the sector-wide scrutiny itself is a disclosed risk.
- **Balance sheet:** AFS unrealized-loss trend is improving (see §6/§8) — the opposite of a red flag, but the level (~$3.85B) is still large in absolute terms and worth tracking against future rate moves.
- **Accounting:** no restatement, auditor change or going-concern language identified in this pass.
- **Insider activity:** not reviewed this pass (time-boxed) — flagged as a gap for a deeper dive.

## 12. Sources
1. SEC EDGAR companyfacts XBRL, CIK 0000316709 (retrieved 2026-09-26): `https://data.sec.gov/api/xbrl/companyfacts/CIK0000316709.json`
2. SEC EDGAR submissions, CIK 0000316709: `https://data.sec.gov/submissions/CIK0000316709.json`
3. Schwab Q2 2026 earnings release and 10-Q (filed 2026-07-21 / 2026-08-07): `https://www.businesswire.com/news/home/20260721955369/en/Schwab-Reports-Record-Quarterly-Revenue-and-Earnings`, `https://www.sec.gov/Archives/edgar/data/0000316709/000031670926000031/schw-20260630.htm`
4. Schwab 2026 CCAR/Comprehensive Capital Analysis and Review disclosure (2026-06-23): `https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Discloses-Results-of-the-Federal-Reserves-2026-Comprehensive-Capital-Analysis-and-Review/default.aspx`
5. TIKR / Motley Fool Q1–Q2 2026 earnings-call transcript coverage (NIM guidance history, cross-check only): `https://www.tikr.com/blog/schwabs-q2-earnings-crushed-estimates-lending-growth-is-why`, `https://www.fool.com/earnings/call-transcripts/2026/07/21/schwab-schw-q2-2026-earnings-call-transcript/`
6. Bloomberg Law, ThinkAdvisor, Law360, Top Class Actions, Citywire — Schwab cash-sweep litigation coverage: `https://news.bloomberglaw.com/litigation/charles-schwab-faces-fiduciary-duty-suit-over-cash-sweep-program`, `https://www.law360.com/articles/1874579/schwab-s-cash-sweep-paid-for-td-ameritrade-buy-suit-says`
7. v4 internal: `data/b1_live_scores.csv`, `data/d4_live_snapshot.parquet` (quant context, retrieved 2026-09-25 close), `outputs/Q05_triage.json` (prior triage note), `outputs/v1_valuation_table.csv` and `outputs/v1_valuation.json` (confirmed: no SCHW row).

## Data basis, recency and disclaimer
Most recent period incorporated: **Q2 2026 (three months ended 2026-06-30), 10-Q filed 2026-08-07, consolidated basis** (Schwab reports on a consolidated basis, including Charles Schwab Bank and all broker-dealer subsidiaries; no separate standalone filing exists). Checked for events to **2026-09-25** (market close used for valuation). GAAP figures are primary; adjusted/non-GAAP figures (adjusted EPS) are labelled explicitly wherever cited. This is research, not personalized investment advice; the reader is responsible for their own decisions.
