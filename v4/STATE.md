# v4 program STATE (single source of truth — update after every phase)

Owner: Aarsh (Dubai). Request (2026-09-26): review v3 handoff, improve methodology, validate data, run 5–10 parallel
agents + 2–3 audit agents in loops until an independent audit scores the output/artefacts/strategy 95+.
Capital at stake: $50k–$100k. Per prior Codex review notes (review/WEEKLY_INVESTMENT_POLICY.md, 2026-09-25):
owner said flexible holding periods, weekly buy/hold/sell review, 15–20% tolerable drawdown (not yet re-confirmed).

Owner follow-ups (2026-09-26, mid-run): (1) "Continue improving the score... real money and real life depend on it,
but I'm also ready to take some risks — not very risk-averse, not extremely risk-taking" → MODERATE risk appetite.
(2) "If you don't like the output, give me a better output — don't just say it's not ready. Keep running overnight
until confident; take the score as close to 100 as possible." → deliverable = finished, investable portfolio + plan.

## Environment
- Python libs: C:\Users\user\eqv4\pylib (PYTHONPATH). Raw cache: C:\Users\user\eqv4\cache. Conventions: v4/CONVENTIONS.md
- Data cutoff: US close 2026-09-25 (S&P 500 7,743.41; SPY 771.36; NVDA 225.07).

## Phase plan
- [x] P0 Read handoff v3 + bundle + prior Codex review (review/)
- [ ] P1 Wave-1 agents (parallel): D1 membership/IDs/SIC · D2 prices · D3 SEC XBRL PIT fundamentals ·
      D4 live snapshot + validation · R1 CMAs/market regime · R2 UAE implementation facts · R3 evidence base/base rates
- [ ] P2 Wave-2: B1 PIT backtest engine (pre-registered model; replicate v2/v3; bias quantification) · B2 risk engine
- [ ] P3 Live scoring of ~500 → candidates → finalists; F1–F4 diligence dossiers (primary sources) · V1 valuation
- [ ] P4 Portfolio construction (verified constraints), probability calibration, stress, allocation scenarios
- [ ] P5 Deliverables: dashboard v4 tabs (add to artifact U2RjG3tNLgLfVCF55x6cEf, never remove), HANDOFF_v4.md
- [ ] P6 Audit loop: A1 quant · A2 fundamental/IC · A3 client/mandate/compliance → fix → re-audit until ≥95 or honest ceiling

## Pre-registered primary model (frozen before any v4 backtest is run — 2026-09-26)
Families (sector-neutral percentile ranks → average within family → average across families, equal weights):
- Q Quality: gross profit/assets, ROE (TTM), operating cash flow/assets, accruals (−), leverage (−),
  asset growth (−), net share issuance (−)
- V Value: earnings yield (TTM), free-cash-flow yield, EBIT/EV, book/price
- M Momentum: 12-1 month total return
- S Earnings momentum: SUE (latest quarterly diluted EPS YoY change ÷ std of prior 8 YoY changes)
Composite = mean(Q, V, M, S). Rebalance monthly; signal at month-end t uses only data filed ≤ t; 10 bps one-way costs.
Variants reported (not selected on results): QVM only; each family alone; v3 conviction proxy; v2 composite.
Risk (volatility) is a constraint, not a return driver. Live-only overlays (analyst revisions, NTM valuation) are
tie-breakers/red flags only because no point-in-time history exists for them.

## Log
- 2026-09-26 00:10: env built; v4 folders; conventions; wave-1 launched (D1 D2 D3 D4 R1 R2 R3).
- 00:20 lead verified v3 flaws (v4/outputs/lead_v3_audit.md): momentum look-ahead 29.1%→18.1%; daily DD −36.2%; drift sensitivity; price-vs-TR benchmark −1.8pts.
- 00:50 R1, R2, R3 complete. Scenarios Bear 2% / Base 6% / Bull 9%, cash 4%, vol 16%. Prior alpha for tilt ≈ +1%/yr (0–2%), TE ~7%.
- 00:53 launched B2 risk engine, DA1/DA2/DA3 deep data audits (FMP connector now live), A1–A3 loop-0 baseline audits of v3.
- 00:56 dashboard v4 progress version published (artifact version 4) via v4/code/lead_assemble.py; re-run + republish after every loop.
- Owner (00:50): "keep working till 7am; show audit loops continuously improving"; wants 20–25 parallel agents.
- ~01:10 ALL agents killed by subscription session limit (reset 02:10). LESSON: 12 concurrent Opus agents exhaust the
  5-hour window in ~1h. From 02:12: Opus only for D1/D3 (resumed via SendMessage) + B1 + auditors of v4; Sonnet for
  diligence, data audits, risk engine, baseline audits. Keep ≤15 concurrent.
- 02:15 D2 + D4 complete (reports written before cutoff). D2: 1,172 symbols; PIT member-day price coverage 69% (2010-14),
  79% (2015-19), 93% (2020-26) → disclose residual survivorship. D4: 503/503 prices within 0.5% of Cboe & CNBC; Yahoo
  fwdPE ≠ NTM >10% for 11% of names; pending deals: WBD KVUE TECH AES NSC D (exclude); MGM bid dropped 09-24.
- 02:20 launched F1–F7 diligence (20 names from lead_prelim_rank.csv: TRV ALL GL AIZ SYF TROW DLTR TGT BBY DECK TPR RL
  BMY HST EIX JBHT UPS GD CF MPC PCAR), B2 (sonnet), DA1, DA3 (sonnet), A1–A3 loop-0 baseline (sonnet).
- 02:16 D3 PIT panel written (d3_pit_monthly, d3_eps_quarterly_pit); launched B1 (opus), B1X (sonnet), DA2 (sonnet), V1 (sonnet).
- 02:24 LOOP 0 (v3 baseline) scores: A1 41 · A2 42 · A3 45 → avg 42.7. Dashboard republished (artifact version 5).
- 02:33 B1 Phase A (membership = D2 fja05680 spells, labelled temporary; D1 never delivered): PRE-REGISTERED MODEL HAS NO
  EDGE 2012-01..2026-08: top-30 EW net 12.6% vs SPY TR 15.1% (−2.5%/yr, NW t −0.96); vs PIT EW −1.3% (t −0.63); IC 0.007
  (t 0.97); deciles flat; top-30 daily maxDD −46% vs SPY −34%. Calibration flat: P(12m>0) 65–70%, P(beat SPY) 44–46% all
  deciles. Residual survivorship vs RSP +0.9%/yr. B1X independent replication agrees (top-30 12.68% vs 12.64%; live
  rank corr 0.976); today's-survivors version shows fake +4.65%/yr (t 2.2) → quantifies v3-style hindsight bias.
- 02:45 V1 valuation (69 names): 27 attractive / 18 fair / 7 demanding / 17 excessive vs own history.
- 02:50 DA1 data audit 76/100 (yes-with-fixes; prices/splits excellent; some "no data" historical names are recent
  delistings, e.g. CMA/EA/K). FMP quote endpoints plan-gated (demo whitelist).
- 02:55 STRATEGY DECISION (lead, from evidence): index is the core (UCITS S&P 500); stock sleeve = satellite justified by
  verified quality, valuation discipline and diversification away from the 40% top-10 concentration — NOT by a claimed
  edge (expected alpha ≈ 0, TE ~7–8%); cash/T-bill reserve sized to the drawdown tolerance (SPY: P(DD>20%) within 3y
  45%, 5y 69% empirically since 1995).
- 03:00 SLEEVE SELECTION RULES FIXED BEFORE reading bulk diligence verdicts (v4/code/lead_build_portfolio.py): live_rank
  ≤70; no pending deal; vol ≤45%; V1 verdict attractive/fair; diligence INCLUDE/INCLUDE-SMALL; ≤2 per sub-industry;
  inverse-vol weights ×(1 / 0.5 small), 3–10%, sector ≤25%, sub-industry ≤12%, verified post-solve.
- 03:00 launched F8 (HIG CINF MTB), F9 (CVS DVA EOG), F10 (SWK HAS MGM), F11 (FRT LMT) — no sub-agents allowed.
- ~03:00–07:10 SECOND session-limit stop (reset 07:10). B1 Phase B on D1 membership had completed (02:59). Final B1:
  top-30 12.5% vs SPY 15.1% (−2.6, t −1.12); sleeve rule 10.8% (−4.3, t −1.81); Dirichlet 1.4% positive; bias today
  vs PIT +6.0 pts; momentum (v3 window) +12.5 pts; residual survivorship +1.0 pt vs RSP.
- 07:12 resumed F8/F9/F10/F11/DLTR. Built lead_risk.py, lead_views.py, lead_report_sections.py (report sections generated
  from data). Interim sleeve (13): DLTR HST JBHT ALL MPC GL HIG BMY MTB LMT FRT SYF RL; all caps pass, 100% invested.
  Base-case allocation odds: Moderate 55/15/30 → P(gain 10y) 94%, 5y 87%, P(DD>20% 5y) 51%; Cautious 35/10/55 → 5y 94%,
  DD20 13%; Index only → 5y 80%, 10y 88%, DD20 81%.
- 07:37 LOOP 1 (v4 draft, 15-name sleeve) scores: A1 85 · A2 76 · A3 80 → avg 80.3 (loop 0: 42.7).
- 07:40–08:05 LOOP-1 FIXES (every must-fix of A1/A2/A3 addressed; details in audit/loop_fixes.json "1"). SLEEVE RULE
  AMENDMENTS — each removes an internal inconsistency an auditor found; none uses returns or backtest results:
  (a) missing V1 valuation = ineligible (A2: RL entered because its V1 row arrived after the build);
  (b) negative V1 base case = ineligible (a "fair price" holding cannot have a negative own-valuation base case: MPC, HAS out);
  (c) V1 valuation without a base case = incomplete = ineligible (same logic as (a); DXCM);
  (d) INCLUDE-SMALL also halves the per-name cap (5%); sleeve capacity the caps cannot absorb goes to the S&P 500 index
      fund, not cash (with 12 names in 5 sectors the old rule forced half-conviction BMY/DLTR to the full 10% cap);
  (e) the analyst's reconciled valuation view (dossier §7 / T2 notes) must ALSO be cheap or fair (symmetric to RL:
      T2 found JBHT's own dossier values it ~31% below the price while V1 says "fair" → JBHT out).
  Freshness guard (sha256 manifest; downstream scripts stop on any changed/new input). Crisis replays now rebalance
  quarterly (Loop-1 replay rebalanced daily despite a "buy-and-hold" comment). Added: worst-fall anchor with dates,
  max equity share that kept each crisis within −20%/−15% (GFC: 34%/26%), block-length sensitivity (5/21/63 days),
  sample-covariance risk contributions, 95% CIs in §5, DA1 limitation, estate-tax precondition, per-$10,000 table,
  glossary (§12 + dashboard), run_all.py + requirements.txt.
- 07:50 launched F12 (DG ABNB DRI), F13 (MAS VRSN BKNG), F14 (UDR PSA) — the 8 names that pass every quantitative gate
  but had no dossier (equal diligence coverage; F9 still covers CVS DVA EOG); V1X (independent valuation re-derivation),
  T2 (holding notes), DA4 (53-fact adversarial check), R3 (implementation facts), D2R (re-download of the no-data list).
- 07:55–08:02 R3: UAE clients onboard via Interactive Brokers (U.K.) Ltd DIFC Branch (DFSA Cat 4) → custody IB LLC → SIPC;
  Vested appears PAN/NRI-gated; SCA renamed Capital Market Authority 1-Jan-2026. T2: 12 one-line theses, 5 verbatim kill
  criteria each; valuation conflicts JBHT (dossier expensive), BMY and SYF (dossier fair vs V1 attractive) reconciled in
  the dossiers. DA4: 51/53 facts PASS, 1 MINOR, 1 UNVERIFIABLE, 0 FAIL; flags HST P/FFO 8.5x (V1) vs ~10.4x on the
  company's own AFFO guidance → pending V1X.
- 08:06 F9 (CVS DVA EOG) found hung since 02:50 on an interactive directory-request tool call (never resumed after the
  session-limit stop; wrote nothing). Stopped and replaced by F15 (same names, Loop-2 addendum, directory tools banned).
- 08:17 SHARED-WORKSPACE RULES found (project-root CLAUDE.md / AGENTS.md / RESEARCH_VERSIONING.md, installed 01:15 by the
  parallel Codex workstream). Latest completed release: v005_2026-09-26_codex (25% max equity: 15% index + 10% direct +
  ≥75% reserve; AMP ≤$500 and PAYX ≤$101.80 "buy now"; ranks only v3's 14 candidates). v4 will publish as a new numbered
  Claude release via tools/publish_research_release.py with parents v005_2026-09-26_codex, claude-v3, codex-initial-audit,
  codex-deep-data-audit. Reconciliation: code/lead_reconcile_v005.py → FINAL_REPORT §13 + dashboard tab; agent X1 verifies
  v005's inherited claims. Added the Defensive 15/10/75 mix (v005's budget) to every allocation table. v4 does not
  override v005; the owner decides. F13 done (MAS WATCH; VRSN, BKNG INCLUDE-SMALL); F14 done (UDR INCLUDE-SMALL; PSA WATCH;
  found V1 REIT capex input ~20–40x too low); V1X: 85% of checks pass, no verdict changes, REITs valued with FCFF DCF (flaw).
- 08:21 F12 done (DG, ABNB INCLUDE-SMALL; DRI INCLUDE). V1X final: 185 checks, 86.5% pass, all 8 FAILs traced (net-debt
  tags for banks/insurers/REITs, insurer D&A), no verdict or base-case sign change; DLTR bear NaN = real V1 bug (P/E exit
  on a loss year → negative price; floored = −100%). V1's REIT "FFO" = net income + total D&A (counts property-sale gains):
  HST 8.5x proxy vs ~10.4x on company AFFO guidance; FRT 10.8x vs ~14.7x on Core FFO guidance → launched V2R (NAREIT FFO
  rebuild) and wired amendment (f): V2R's FFO-based verdict replaces V1's for REITs. C1: 216 report numbers checked,
  215 match; fixed "top quintile ~100 names" → ~85 and the stale hard-coded evidence-tab lede (now data-driven).
  Preview build with F12–F14 dossiers: 17 names, 7 sectors, 100% invested (no index fill), all caps pass.
- 08:25 X1 (v005 inherited-claim check): 26 items, 23 CONFIRMED (all reference prices exact vs D2; VUAA/IB01 ISINs, TERs,
  IB01 4.16% YTM, look-through weights; shock and CAGR tables reproduce; AMP/PAYX base cases reproduce from SEC filings),
  1 MINOR (MSFT "reconciled" close $516.05 vs $516.17), 1 NOT CONFIRMED (PAYX 20x exit multiple is BELOW its own 10-yr
  P/E range ~24–34x: conservative but undisclosed), 1 UNVERIFIABLE (IB01 duration). AMP gap (v005 13–14% IRR vs V1 +6.5%/yr)
  = method choice. Folded into lead_v005_reconciliation.json → FINAL_REPORT §13 and the dashboard tab.
- 08:39 F15 done (CVS, DVA, EOG INCLUDE-SMALL; EOG "cheap" inflated by a war-driven oil spike → analyst view fair).
  V2R (NAREIT FFO rebuilt from filings): HST 10.6x TTM (10.4x FY26 AFFO guide), 49th pct 10-yr, peers 11.0x → FAIR
  (V1: attractive); FRT 14.9x (14.7x guide), 37th pct, peers 15.1x → FAIR (V1: attractive; "near cheapest ever" does not
  survive); UDR 13.7x vs peers 15.8x → attractive (low-confidence percentile); PSA 16.7–17.0x → fair. Amendment (f)
  applies V2R's verdicts; all REITs stay eligible. Launched F16 to re-assess FRT and HST verdicts on the corrected
  valuation (dated dossier addenda + F16_summary.json). Pipeline precedence: the most recently written diligence source
  (summary or T2 notes) wins, so re-assessments are never masked. Preview: 20 names, 9 sectors, 100% invested.
- 08:47 F16: FRT INCLUDE → INCLUDE-SMALL (corrected valuation fair, not cheap; net debt rising); HST stays INCLUDE.
  LOOP-2 BUILD (frozen for audit, build 08:44:06): 20 names, 9 sectors, 100% invested, all caps pass; Moderate P(gain 10y)
  94%, Cautious 5y 94%, Defensive 5y 99%; GFC replay: sleeve −55.8% vs SPY −55.2%, Moderate −40.9%, Cautious −26.5%,
  Defensive −13.3%; equity share for −20%/−15% in the GFC: 34%/27%. Probabilities never printed as 100%/0% ("over 99%" /
  "under 1%"). Dashboard republished (artifact v8). Launching Loop-2 auditors A1–A3 (Sonnet, prompts/A_personas.md).
- 08:54 D2R done: root cause of DA1's false-missing defect confirmed in code (d2 phase_retry accepted "no data" after 2
  tries ~2 s apart, no backoff); Yahoo's chart API currently 404s even live names (BK, MMC) from this network and one
  call flipped 404→200 minutes apart (transient block). Two full sweeps of 499 symbols (45 min apart, with backoff)
  recovered 0 of the 408 no-data symbols; coverage unchanged (2010-14 68.7%, 2015-19 79.2%, 2020-26 93.5%). B1 unchanged;
  +1.0 pt/yr residual bias stays disclosed, true size unresolved. To add to FINAL_REPORT §11 after the Loop-2 freeze.
- 08:55 Delisted-price source probe: the connected Shibui market database holds only CURRENTLY listed securities (0 of 18
  acquired/delisted S&P names found — HES, MRO, CTXS, XLNX, TWX, AET, CA, TIF, AGN, RTN, ATVI, PXD, SIVB, CMA, EA, K, WBA,
  IPG; tickers APC and STI now belong to unrelated companies) and caps queries at 200 rows → cannot fill the survivorship
  gap. CMA/EA/K/IPG were acquired or taken private in 2025–26, so D2's "no data" for them reflects Yahoo purging delisted
  histories after the deals (DA1 saw CMA trading to Jan-2026), i.e. survivorship, not only a download bug. Closing the gap
  needs a delisting-aware vendor (CRSP/Norgate). For FINAL_REPORT §11 after the Loop-2 freeze.
- 09:02 LOOP 2: A1 88 (loop 1: 85), A2 89 (loop 1: 76); A3 pending. A1 must-fixes: §11 cited d2r_report.md before it existed
  (now exists: 0 of 408 recovered); CMA status; independent reproduction of risk contributions. CMA RESOLVED with primary
  source: Fifth Third completed its all-stock merger with Comerica on 1 Feb 2026 (1.8663 FITB per CMA; Fifth Third IR
  release 2026-02-02; FITB 10-Q Q1 2026) → CMA delisted; D2's "no data" reflects Yahoo purging the acquired name.
  lead_check_risk_contrib.py (independent numpy re-derivation from D2 prices): vol, avg corr, all 20 risk contributions
  match to ≤5e-7; TE differs by 8e-5 only because lead_risk uses np.std ddof=0 → align to ddof=1 when the freeze lifts.
  A2 must-fixes: UDR dossier lacks the V2R addendum (14-month percentile caveat); 8 holdings never fact-checked (DA5
  launched: ALL DVA GL HIG CVS VRSN UDR DRI); risk contributions "near-tautological" → add risk-per-unit-weight view.
- 09:09 LOOP 2 complete: A1 88 · A2 89 · A3 89 → avg 88.7 (loop 1: 80.3). Correction to the 08:44 entry: the 20-name
  sleeve spans 8 GICS sectors, not 9 (A1 loop-2 finding; the report and dashboard compute it from data and were right).
  Loop-3 fixes in progress: §11 D2R/CMA/Shibui text; UDR V2R addendum + lead correction of its thesis line
  (outputs/f_lead_corrections_summary.json, per-ticker precedence); risk engine: TE ddof=1, one-factor split, effective
  bets by sample-cov risk, risk-to-weight ratios, independent check (lead_check_risk_contrib.py, fails the run on
  mismatch); Appendix A (technical) + plain §5/§7; changes-since-draft note (HAS, RL, MPC, JBHT); excluded list to top 45;
  base-rate column relabelled; §8 open items labelled with workarounds; DA5 fact-checks the 8 unaudited holdings.
- 09:19 DA5: 40 facts in 8 unaudited dossiers → 36 PASS, 1 MINOR, 1 FAIL, 2 UNVERIFIABLE. FAIL fixed (VRSN renewal rate:
  final Q1-26 76.3% up from 75.5%, not "expected 75.2%" — dated correction appended; verdict unchanged); MINOR fixed (HIG
  next earnings date relabelled as an estimate). Every holding now fact-checked by ≥1 independent agent/auditor.
  OWNER (09:2x): wants an all-stock answer (no T-bills/index "right now", age 35) → answered with the 20-stock list as a
  standalone portfolio + honest stress/odds; added an "All-stock option" card to the dashboard summary. V1X extension
  (8 new names) running; then rebuild, freeze, Loop 3.
- 09:20 OWNER challenge: why no NVDA/MSFT; growth and moats must count, not only valuation. Fair point: both were
  excluded only by the model-rank gate (NVDA rank 103, MSFT 152, outside the top 70), never diligenced; the model has no
  proven edge, so that gate is not evidence against them. PRE-COMMITTED RULE (written before any verdict is read):
  "Quality-growth lane" = the 8 largest S&P 500 companies by market cap tied to AI/cloud (NVDA, MSFT, AVGO, GOOGL, AMZN,
  META, AAPL, ORCL) get the same full diligence. A name is eligible if (1) the diligence verdict is INCLUDE or
  INCLUDE-SMALL, and (2) the reverse DCF shows the growth priced in is at or below the analyst's evidence-based base case
  (market not already paying for more than the plausible outcome). Same caps: ≤10% per name, ≤25% per sector,
  ≤2 per sub-industry. Launched F17 (NVDA, AVGO, AAPL, ORCL) and F18 (MSFT, GOOGL, AMZN, META).
- 09:26 OWNER: every S&P 500 company must get at least a quick research pass (model rank must not hide good businesses).
  PRE-COMMITTED (before any triage result): (1) quick triage of all 455 names without a dossier (15 Sonnet agents Q01–Q15,
  sector-grouped, data cards v4/data/triage_cards.csv); each scores quality, growth and price-vs-growth 1–5 and flags red
  flags; ADVANCE = no disqualifying red flag AND price_vs_growth ≥ 3 AND (quality ≥ 4 OR growth ≥ 4). (2) Every ADVANCE name
  gets full diligence (if > 45, the 45 with the highest quality+growth+price_vs_growth first, the rest queued and
  disclosed). (3) Eligibility for triage-advanced names = the quality-growth-lane rule (g): verdict INCLUDE/INCLUDE-SMALL
  AND the growth priced in ≤ the analyst's base case; same caps (≤10% name, ≤25% sector, ≤2 per sub-industry),
  inverse-vol weights. Existing top-70 names keep their original gates.
- 12:12 TRIAGE DONE: 455 scored, 296 ADVANCE (bar too loose; several agents hit search rate limits and relied on general
  knowledge — disclosed; full diligence is where facts get verified). Per the pre-committed rule, the top 45 by
  quality+growth+price_vs_growth go to full diligence now; TIE-BREAK (not specified earlier, fixed now before any diligence
  result): price_vs_growth, then quality, then ticker. 251 advanced names queued for the next cycle (disclosed).
  Big-8 results: F17 NVDA INCLUDE-SMALL (implied above base on trailing FCF, in line on next-FY FCF), AVGO INCLUDE-SMALL
  (in line), AAPL INCLUDE-SMALL (above), ORCL WATCH; F18 MSFT, GOOGL, AMZN, META all WATCH (priced above base case).
  Under rule (g) only AVGO is eligible. Launching F19–F33 (3 names each, standard depth) on the top 45.
- 12:13 AMENDMENT (i): the 1-yr volatility ≤ 45% gate is removed for ALL names (owner is 35, wants an all-stock growth-
  tolerant portfolio; volatility is handled by inverse-vol weights and caps). Made before any affected diligence
  result: no diligenced name had been excluded by volatility alone; all 20 holdings are under 45%; it makes the rule
  identical for top-70, lane and triage names (fixing the asymmetry that would otherwise exclude EXPE/MU/SNDK/LRCX/ALB
  but not lane names). GOOG removed from wave 1 (same company as GOOGL, WATCH) → replaced by UAL.
- 12:38 WAVE-1 DILIGENCE DONE (F19–F33, 45 names). ~29 new names pass rule (g)/(h); with the existing names ~49 would be
  eligible — too many for the owner's 5–20. PRE-COMMITTED FINAL-SIZE RULE (written before running the build): hold at
  most 20 names. Rank eligible names by (1) conviction: INCLUDE before INCLUDE-SMALL; (2) margin of safety: price-implied
  growth below base ("below", or V1 "attractive" for V1-gated names) before in line ("in_line"/V1 "fair"); (3) base-case
  3-yr return (analyst scenario where available, else V1) descending; walk down that order keeping ≤2 per GICS
  sub-industry; stop at 20. Weights unchanged (inverse-vol × conviction; ≤10% full / ≤5% half; sector ≤25%; sub ≤12%).
  Summaries missing implied_vs_base were normalized from the analysts' own report tables (outputs/lead_implied_normalization.json).
- 12:44 LOOP-3 BUILD (frozen for audit): whole-index process. 50 eligible → best 20 by rule (j): full conviction HST DRI BR
  MTB CRH LVS AMP PGR; half UDR BMY CVS CMCSA DG SWK BKNG DVA NOW EG SYF BX. All caps pass. All-stock: GFC −59.7% (S&P
  −55.2%), COVID −38.8% (−33.7%), 2022 −14.8% (−24.5%); base case P(gain 5y) 75%, P(beat S&P) 49%, P(fall>20% in 5y) 92%;
  TE 11.6%, beta 0.73, 15 effective bets. v005 reconciliation updated (AMP now held = confirms v005; HIG dropped; MSFT/NVDA
  both "not at current price"). Launching Loop-3 auditors A1–A3.
- LOOP-3 AUDIT: A1 78, A2 78, A3 76 (avg 77.3; down from 85.7 because the whole-index rebuild added 13 new holdings and
  the verdict still led with the index/T-bill allocation the owner had declined). LOOP-3 FIXES (audit/loop_fixes.json "3"):
  §1 verdict, dashboard hero, tiles and answer cards now lead with the all-stock 20-name portfolio (allocation view kept
  below as the lower-risk option); §5 closing line rewritten; PGR NTM P/E 0.27x (corrupt vendor field) replaced by a
  sanity-bounded P/E (3–150x, else trailing, labelled); display weights by largest-remainder rounding (sum exactly 100.0%);
  NOW dossier corrected (Moveworks closed Dec 2025; kill criterion 3 withdrawn). HONESTY CORRECTION on rule (j): it was
  written after the wave-1 diligence verdicts were known (12:38) but before the ranked list was built; it is a judgement
  call, not a pre-registered test (now said in §6). §6 lists all 30 eligible-but-not-held names in (j) order. The 2007–09
  replay excludes DG (first price 2009-11-13), NOW (2012-06-29) and SYF (2014-07-31), 7.9% of weight, renormalising the
  rest (b2 missing='exclude'; not an S&P stand-in) — now disclosed in §1. Coverage stated: 455 triaged + 40 earlier
  dossiers; 88 names with full diligence verdicts; 251 triage-advanced names lack a full dossier (231 could still qualify
  under rule (h); 20 already fail the model's valuation gates or are pending takeovers). Note: V1's 3-yr scenarios are
  annualised (CMCSA base +62%/yr is V1's re-rating arithmetic from a 6.2x P/E, copied by the analyst), so the (j)
  tie-breaker favours deep-value re-rating names; disclosed in §6. DA6 (fact-check of BR, CMCSA, BKNG, DG, NOW, BX, EG)
  running. Artifact republished (version 10).
- 13:18 WAVE-2 DILIGENCE launched (F34–F48, 45 names = the next 45 queued in the same pre-committed order; data/
  full_diligence_wave2.json; prompt prompts/F_standard_wave2.md). Loop-4 audit waits for wave 2 + DA6 so it judges the
  more complete build. No rule changes: wave-2 names enter through rule (h) and the (j) order exactly as wave 1 did.
- 13:30 DA6 DONE (BR, CMCSA, BKNG, DG, NOW, BX, EG): 28 facts, 24 pass/confirmed, 1 minor (EG BVPS $379.70 vs $379.83),
  2 FAIL (BR: CQG price was disclosed, ~$173m, closed 30 Apr 2026; DG: Washtenaw dismissal was 2025-06-23 not 2026, case
  since amended, motion to dismiss fully briefed 29 May 2026), 1 unverifiable (BX debt path). NOW/Moveworks correction
  confirmed by 8-K. Corrections appended to BR.md, DG.md, EG.md (originals kept). No verdict changes; DG kill criterion 5
  not fired but closer. Folded into the next build (after wave 2).
- WAVE-2 DONE (F34–F48, 45 names): 34 INCLUDE/INCLUDE-SMALL, 11 WATCH (APTV CPRT VLTO CMI GEV MS NUE STLD; BAC is
  INCLUDE-SMALL but top-70 so V1 'excessive' gate excludes it). implied_vs_base missing in 12 summaries: recorded from the
  agents' own report tables (outputs/lead_implied_normalization.json, code/lead_add_implied.py; SCHW takes the
  conservative in_line reading); agents later wrote the same values themselves (F36, F41 — all matched).
  scenario_returns_3y missing for ADP MCD PAYX TYL INTU TMUS UBER: the authoring agents added them from their own §7/§8
  work (basis lines in the summaries; prices checked against the d4 snapshot). ES/SRE (wave 1) still lack scenarios
  (not held). lead_previous_sleeve.json now = the Loop-3 list.
- LOOP-4 BUILD (frozen for audit): 86 eligible (was 50). Held: full HST DOV DRI ADP BR CRH GM MTB LVS RJF AMP PGR HBAN
  (13, 77%); half UDR CVS CMCSA DG BKNG DVA SYF. Out (still eligible, displaced by new full-conviction names): SWK BMY EG
  BX NOW. Financials at the 25% cap. GFC −59.7% (S&P −55.2%), COVID −40.7%, 2022 −16.6%; TE 11.6%, beta 0.75, ENB 16.6.
  2007–09 replay now lists holdings with no price from the data (DG, SYF, GM = 10.5%); GM caveat added (old GM bankrupt
  2009, so the real loss would likely have been worse). DA6 corrections folded in. Launching Loop-4 auditors A1–A3.
- LOOP-4 AUDIT: A1 79, A2 76, A3 84 (avg 79.7). FIXES APPLIED (13:47 build, rules committed f0b33c49 in
  outputs/rule_commitments.jsonl; build now refuses to run on uncommitted rule changes): GM net-cash corrected by its
  author (+$3.67bn auto net cash, not +$8.7bn; verdict/implied/scenarios unchanged); stale Ledoit-Wolf block renamed
  risk_ledoit_wolf_SUPERSEDED; rule-(j) sensitivity (code/lead_j_sensitivity.py: 15–20/20 overlap, 12 names in every
  ordering, GFC −54% to −62%) added to §6; all-stock rows in the per-$10k and estate-tax tables + dashboard impl rows;
  withholding and tracking-error sizing of the "10 points" goal in §1 and the answer card; AUDITED loop-4 entries.
  OPEN (resume here): (1) BUG: §6 lane marker/footnote reads 0 of 20 because lead_portfolio.json rows lack 'lane' —
  carry 'lane' through lead_views.py rows (AMP, BR, CRH, LVS, PGR, GM, ADP, DOV, RJF, HBAN etc. are lane names) before
  publishing; (2) DA7 fact-check (GM, LVS, RJF, HBAN) running → fold into A.5; (3) regenerate c1_consistency against
  the current build (A1); (4) publish artifact v12, run Loop-5 auditors; (5) numbered release via
  tools/publish_research_release.py; (6) wave 3 diligence (189 queued).
- LOOP-4 FIXES COMPLETE (build frozen for Loop-5 audit): DA7 5 FAILs corrected in dossiers (GM net cash; RJF bank
  capital restated to standalone 16.4% vs 15% kill threshold and parent debt ~$4.47bn; LVS Adelson 58.2% per DEF 14A, no
  July-2026 13D/A; HBAN Veritex closed 20 Oct 2025 / Cadence 1 Feb 2026); A.5 marks "(corrected in dossier)". Lane flag
  carried through lead_views (11 of 20 via the analyst route, § marker; † footnote says whose scenarios are shown).
  Analyst-vs-V1 labels now directional (GM "more optimistic than V1"; ‡ only for non-lane names where the analyst is more
  cautious). C1 re-run on the current build: 350 checked, 349 matched, 1 mismatch (dashboard stress used worst-point keys)
  fixed; old C1 archived in outputs/archive/. v005 reconciliation: PAYX now diligenced (INCLUDE-SMALL, bench). loop_fixes
  "4" recorded. Next: artifact v12, Loop-5 auditors, then rewrite release notes and publish the numbered release.
- LOOP-5 AUDIT: A1 82, A2 81, A3 86 (avg 83.0). FIXES (17:45 build, rules e38d4616; content_sha256 ee5f7079 = identical
  to the 17:17/17:35 builds): dashboard loop-score bug (JSON total now authoritative); verification gate
  (code/lead_verify_gate.py) blocks packaging until every holding has a DA check with FAILs corrected and C1 names the
  current content_sha256; build_history.jsonl; A.5 reads auditors' structured fact_checks from Loop 6; estate-tax table
  on the dashboard; wave-3 prompt (entity-scope rule, required-fields self-check) and batches F49–F63
  (data/full_diligence_wave3.json) prepared, NOT launched (would change build inputs before the release).
  SEQUENCE: DA8 (running) → corrections → rebuild → C1 re-run (must record content_sha256) → artifact → package +
  publish release → launch wave 3.
- 18:08 RELEASE CANDIDATE: DA8 (AMP ADP CRH PGR DOV: 33 facts, 1 FAIL ADP litigation, 4 MINOR) corrected in dossiers;
  C1 final: 361 checked, 361 match, content_sha256 ee5f7079 recorded; PAYX wording fixed (guided 7–9%). Verification
  gate PASS. Publishing artifact and the numbered release (notes: release/RELEASE_NOTES_v4.md).
- 18:12 PUBLISHED v006_2026-09-26_claude (package sha256 613fe4df…, 720 files; parents v005_2026-09-26_codex,
  claude-v3, codex-initial-audit, codex-deep-data-audit; notes release/RELEASE_NOTES_v4.md; states it supplements and
  partly challenges v005, does not supersede it). LATEST_HANDOFF.md and versions/ index updated by the tool.
  Artifact v13. NEXT: wave 3 (F49–F63, prompts/F_standard_wave3.md) launched now; then rebuild, DA check of any new
  holdings (gate), C1, Loop-6 audit, next release (parent v006).
- 18:29 RULE (k) V1 input-defect guard (committed 9bba358c before any build using it): F60 found FIX's V1 valuation
  built on a mis-dated duplicate XBRL context (D3 TTM revenue $3.96bn vs $11.23bn true; "excessive, base −52%/yr" is an
  artefact). Scan of all 92 V1 names (D3 vs Yahoo TTM revenue, V1 using D3): only FIX affected; APA already fell back;
  COF/SYF valued without revenue (SYF held, unaffected). Defective-input names go to the analyst route. FIX's own
  diligence (F60) = WATCH, so it stays ineligible, now for the correct reason. The v1_valuation.json row itself is left
  unchanged (upstream artefact) and the defect is documented here and in the build header.
- WAVE 3 progress: F50 XEL IS/NRG IS/VST W; F53 IDXX IS/ISRG IS/LIN W; F54 MA INCLUDE/MCO IS/MRSH IS; F56 SHW W/SPG IS/
  SPGI IS; F60 DASH IS/DELL IS/FIX W; F61 MRVL W/TER W/ACN IS.
- XOM CIK note (F59): b1_live_scores carries CIK 2115436 for XOM while d1_cik_map has 34088 (whose last SEC report is
  2026-08-03, and whose companyfacts lacks the Aug-2026 10-Q). A full scan found XOM is the only one of 503 names whose
  CIKs disagree. The pattern fits a 2026 holding-company re-registration rather than a data error, but it is unresolved.
  XOM is WATCH (F59) and not held, so no portfolio effect; recorded as an open data question in FINAL_REPORT §11 at the
  next build.
- WAVE 3 more: F49 WDC W/WFC INCLUDE/WTW INCLUDE; F51 ABBV IS/AME IS/AXP INCLUDE; F55 MSCI INCLUDE/NEE IS/ORLY IS;
  F59 XOM W/AMD W/AXON W; F62 PNR W/AON IS/AVY IS.
- WAVE 3 DONE (F49–F63, 45 names; all summaries complete, no normalisation needed). Rule (l) committed 73504286 before
  the build: ≤5 names per GICS sector in the (j) walk (disclosed as written after wave-3 verdicts showed many new
  full-conviction Financials). WAVE-3 BUILD (content 31e96bf8): 116 eligible; held 16 full (HST DOV DRI ADP MA CAH BR
  CRH COR GM LVS PGR AXP HBAN VEEV MSCI) + 4 half (CVS CMCSA DG BKNG). Out vs v006: MTB RJF AMP (eligible; sector limit)
  UDR DVA SYF. GFC −56.5% (S&P −55.2%; DG VEEV GM MSCI had no price = 12.7% of weight), COVID −37.0%, 2022 −15.5%;
  TE 11.2%, beta 0.67, ENB 17.2. j-sensitivity now in run_all (12 names in every ordering). v005 row now dynamic (AMP
  eligible, not held). §11 records the FIX data defect and the XOM CIK question. DA9 (MA AXP MSCI) and DA10 (CAH COR
  VEEV) running → corrections → rebuild → C1 last → Loop-6 audit → release (parent v006).
- 18:50 DA9 (MA AXP MSCI: 21 facts, 0 FAIL, 1 MINOR MSCI label) and DA10 (CAH COR VEEV: 21 facts, 1 FAIL COR revenue
  guidance history 5–7%→7–9%→4–6%) corrected in dossiers. All 20 holdings independently fact-checked. Build 18:49:31
  (content 31e96bf8, unchanged). Loop-6 auditors A1–A3 launched on this build; then fixes → C1 last → release v007
  (parent v006).
- LOOP-6 AUDIT: A1 84, A2 82, A3 87 (avg 84.3). FIXES: inline "[Corrected …]" markers on the operative RJF (parent
  debt, consolidated ratios) and MSCI (kill criterion 2) sentences, originals kept; XOM CIK reconciled (2115436 =
  ExxonMobil Holdings Corp, Aug-2026 reorganisation, co-registrant with 34088; §11 and XOM dossier updated); A.4
  register lists every DA check, the Q01–Q15 triage (455 scored / 296 advanced) and each diligence wave; dividend-yield
  source named in §1; j-sensitivity JSON now lists every bench name's position in the (j) order and why it missed;
  stored weights sum exactly; NEW code/lead_dossier_precheck.py (mechanical pre-check before DA checks: missing summary
  fields, balance-sheet figures without entity scope, mislabelled YoY periods, filings cited without accession) — it
  found an MSCI share-count mislabel (clarified in the dossier). PROCESS RULE (written): a new holding must pass the
  pre-check and an independent DA-series fact-check, with FAILs corrected, before any release; the verification gate
  enforces it at packaging.
- 19:20 PUBLISHED v007_2026-09-26_claude (package sha256 398e9363…, 793 files; parents v006, v005, claude-v3,
  codex-initial-audit, codex-deep-data-audit; notes release/RELEASE_NOTES_v4_wave3.md). Build 19:16:27, content
  9bc2eb70, gate PASS (C1 282/282). v006's local zip renamed release/Claude_v4_Research_Release_2026-09-26_v006.zip
  (the published copy is versions/v006_…/package.zip). Artifact v14. NEXT: wave 4 (next 45 of 160 queued in
  data/full_diligence_wave3.json "queued"), run code/lead_dossier_precheck.py on new holdings before DA checks.
- 19:25 WAVE 4 launched (F64–F78, prompts/F_standard_wave4.md, data/full_diligence_wave4.json; FOXA dropped as the same
  company as FOX, replaced by the next queued name APP). 115 triage-passed names queued after wave 4.
- 27 Sep: WAVE 4 DONE (F64–F78, 45 names, all fields complete). WAVE-4 BUILD: 223 researched, 148 eligible; 20 held, all
  full conviction: EXC STE BALL MA DOV USB DRI ADP CAH BR PPG CRH COR PGR AXP HBAN GM LVS VEEV GDDY. Out vs v007: HST
  MSCI CVS CMCSA DG BKNG (all still eligible). GFC −51.2% (S&P −55.2%; GDDY VEEV GM no price = 11% of weight), COVID
  −38.7%, 2022 −18.8%; TE 11.6%, beta 0.64, ENB 18.5; 16 names in every (j) ordering. Pending-deal notes from F66/F69:
  FOX (Roku) and MKC (Unilever Foods) have signed deals but exclude_pending_deal=False; both are WATCH so ineligible
  regardless — to fix in the pending-deal list at the next data refresh. Pre-check run on the 6 new holdings;
  DA11 (EXC STE BALL) and DA12 (USB PPG GDDY) launched.
- 27 Sep 00:56: DA11 (EXC STE BALL: 21 facts, 0 FAIL, 2 MINOR) and DA12 (USB PPG GDDY: 21 facts, 1 FAIL PPG long-term
  debt $6,195m not $6,876m → net debt ~$5.37bn) corrected in dossiers. All 20 holdings independently fact-checked.
  Build 00:56:27 (content d5c7e755). Loop-7 auditors launched; then fixes → C1 last → release v008 (parent v007).
- LOOP-7 AUDIT: A1 85, A2 84, A3 84 (avg 84.3). RULE (m) (written, process; enforced in code by lead_verify_gate.py at
  packaging): no name is released as a holding until (1) code/lead_dossier_precheck.py and code/lead_xbrl_crosstie.py
  have been run on its dossier, and (2) an independent DA-series fact-check has checked ≥6 load-bearing facts with every
  FAIL answered by a dated correction and an inline "[Corrected …]" marker on the operative sentence.
  LOOP-7 FIXES: §6 exit triggers no longer truncated (were cut at 110 characters, mid-sentence, for all 20 holdings);
  bench shown as a table of the next 20 (full list in lead_j_sensitivity.json with places-behind-20th and base-return
  gap); lead_assemble.py fails the run if any dashboard audit score differs from the auditor's JSON total; NEW
  code/lead_xbrl_crosstie.py compares dossier debt/cash/equity figures with SEC XBRL at the two latest balance-sheet
  dates (tested: it flags the pre-correction PPG debt line; it points to lines, it does not prove errors). DA13 sourcing
  BR's $227m digital-asset gain and GDDY's gross-vs-net debt basis.
- Correction to the 27 Sep wave-4 launch entry: 114 (not 115) triage-passed names are queued after wave 4 (C1 count of
  data/full_diligence_wave4.json "queued"). C1 (loop-7 build, content d5c7e755): 297 checked, 296 match, 1 mismatch
  (A.4 lacked a wave-4 row: the wave list was hard-coded) — fixed by globbing every wave file; the A.4 C1 row is now
  generated from the C1 JSON instead of fixed text.
- 27 Sep 01:30 PUBLISHED v008_2026-09-27_claude (package sha256 cc43eedd…, 869 files; parents v007, v006, v005,
  claude-v3, codex-initial-audit, codex-deep-data-audit; notes release/RELEASE_NOTES_v4_wave4.md). Build 01:24:52,
  content d5c7e755, gate PASS. Packager now skips Windows device-name files (a stray v4/nul from a shell redirect broke
  zipping). v007's local zip renamed …_v007.zip. NEXT: wave 5 (next 45 of 114 queued, data/full_diligence_wave4.json).
- 27 Sep 01:35 WAVE 5 launched (F79–F93 via one background workflow, prompts/F_standard_wave5.md; analysts must run
  the pre-check and XBRL cross-tie on their own dossiers before finishing; NWSA dropped as the same company as NWS).
  69 triage-passed names queued after wave 5.
- WAVE 5 workflow done: 13 of 15 batches wrote files; F81 (ODFL PG PLD) and F90 (OXY P=Everpure PANW) misread "research
  only" and wrote nothing → re-launched with explicit file instructions (prompt amended, item 5). F79 lacked
  implied_vs_base → recorded from its report (AMT below, BRK-B in_line, CB above).
- WAVE 5 DONE (F79–F93 incl. F81/F90 re-runs). WAVE-5 BUILD: 268 researched, 172 eligible; 20 full conviction: TJX SO
  MA STE USB EXC BALL DOV ADP CAH BR PPG PGR AXP HBAN CRH COR LVS VEEV GDDY. Out vs v008: GM, DRI (eligible, outranked).
  GFC −48.7% (S&P −55.2%; GDDY VEEV no price = 6.6%), COVID −36.9%, 2022 −16.9%; TE 11.8%, beta 0.59, ENB 18.4; 14
  names in every (j) ordering. New holdings TJX, SO → pre-check, cross-tie, DA14.
- DA14 (TJX SO: 14 facts, 1 FAIL — TJX Q2 FY2027 net income $1,520m, not the prior-year $1,243m; neither mechanical check
  caught a prior-year-column mix-up) corrected. Build 02:10:44 (content 174b2544). Loop-8 auditors launched.
- Cross-tie extended to quarterly net income (latest ~13-week XBRL period). Tested on the uncorrected TJX line: NOT caught,
  because table cells carry no "$" and no adjacent label; the tool reads labelled dollar figures in prose only. Known
  limitation, recorded: prior-year-column mix-ups in results tables still depend on the DA fact-check.
- LOOP-8 AUDIT: A1 86, A2 85, A3 87 (avg 86.0). FIXES: rule (m) text placed in the build script's rule block (commit
  9c2125ac, comment only); §6 states when Financials binds both the five-name and 25% limits and names who is left out;
  dividend yield labelled a snapshot; MSCI marker moved to the end of its criterion. Latest-quarter sweep of all 20
  holdings for prior-period/column mix-ups (DA15–DA17) + GDDY second valuation leg running.
- Latest-quarter sweep DA15–DA17 (69 facts across all 20 holdings): 1 FAIL (ADP Q4 FY26 net earnings $978.6m; the dossier
  repeated the Q1/Q2 figures) corrected; EXC n/a cells filled from the 8-K; no other prior-period swaps. GDDY peer
  EV/EBITDA–EV/FCF cross-check corroborates "below base case".
- 27 Sep 02:40 PUBLISHED v009_2026-09-27_claude (package sha256 10b4e326…, 945 files; parents v008, v007, v005,
  claude-v3, codex-initial-audit, codex-deep-data-audit; notes release/RELEASE_NOTES_v4_wave5.md). Build 02:34:17,
  content 174b2544, gate PASS, C1 312/312 (first zero-mismatch run). NEXT: wave 6 (remaining 68 queued).
- 27 Sep 02:45 WAVE 6 launched (F94–F108, workflow; prompts/F_standard_wave6.md; data/full_diligence_wave6.json). 23 names queued after it.
- WAVE 6 DONE (F94–F108; all files written). WAVE-6 BUILD: 313 researched, 200 eligible; 20 full conviction: TJX WEC STE
  MA USB BALL DOV EXC ADP RMD BR MCK PGR AXP HBAN CRH LVS PTC VEEV GDDY. Out vs v009: SO CAH PPG COR (eligible,
  outranked). GFC −46.4%, COVID −37.1%, 2022 −17.2%; TE 11.7%, beta 0.61, ENB 18.7. Only 8 names in every (j)
  ordering (was 14): the larger eligible pool makes the exact list more order-dependent — to be stated in §6.
  New holdings WEC RMD MCK PTC → pre-check, cross-tie, DA18.
- DA18 (WEC RMD MCK PTC: 24 facts, 3 FAIL, 1 MINOR). PTC table labels one fiscal quarter early (Sept year-end) —
  corrected; WEC arithmetic slip — corrected; MCK clean. RMD: dossier's FY2027 guidance range does not exist in the
  cited 8-K, 9-month buyback/dividend figures were full-year, and a MatrixCare divestiture was omitted → sent back for
  a full re-assessment (verdict may change) before any rebuild.
- RMD re-assessed (FY2027 guidance in the dossier did not exist; 9-month buyback/dividend figures were full-year;
  MatrixCare divestiture omitted): implied_vs_base still "below" on a guidance-free base case, verdict INCLUDE →
  INCLUDE-SMALL. Rebuild: RMD out, CAH back in (CAH already checked by DA10 and DA16). Holdings: TJX WEC STE MA USB BALL
  DOV EXC ADP CAH BR MCK PGR AXP HBAN CRH LVS PTC VEEV GDDY. Build content 7ac48e4d. Loop-9 auditors launched.
- LOOP-9 AUDIT: A1 84, A2 84, A3 80 (avg 82.7; down on a missing WEC thesis line and the undisclosed RMD episode).
  FIXES: thesis extraction handles long verdict paragraphs and skips the bare verdict/horizon sentences; the build now
  fails on any placeholder thesis; §6 lists every diligence error that changed a verdict (outputs/lead_verdict_changes.json)
  and states rising order-dependence (9 vs 14 in v009); A.4 cumulative DA tally (DA4–DA18: 374 facts, 17 fails, all
  corrected); new pre-check "guidance_unquoted" (flags the RMD lines) and the wave prompts now require verbatim quotes for
  guidance. Correction to an earlier log line: 9 (not 8) names are chosen under every ordering in the wave-6 build.
  C1 for v010 launched.
- 27 Sep 03:40 PUBLISHED v010_2026-09-27_claude (package sha256 ccc7360b…, 1016 files; parents v009, v008, v005,
  claude-v3, codex-initial-audit, codex-deep-data-audit; notes release/RELEASE_NOTES_v4_wave6.md). Build 03:34:07,
  content 7ac48e4d, gate PASS (C1 320/319, the one A.4 count mismatch fixed). Artifact v17. NEXT: final wave 7 (last 24
  queued names, data/full_diligence_wave6.json "queued").
- 27 Sep 03:45 WAVE 7 (final) launched: F109–F116, the last 23 queued names (data/full_diligence_wave7.json). After it, every triage-advanced name has full diligence.
- WAVE 7 DONE (F109–F116, last 23 names; all files written). Queue complete: every triage-advanced name has full
  diligence (GOOG, FOXA, NWSA labelled as second share classes, commit e1d06355). WAVE-7 BUILD: 336 researched, 214
  eligible; 20 full conviction: WEC RSG TJX MA USB LH STE BALL DOV ADP BR PGR AXP HBAN MCK CRH LVS PTC VEEV GDDY. Out vs
  v010: EXC, CAH (eligible, outranked). GFC −47.3%, COVID −37.4%, 2022 −17.3%; TE 11.8%, beta 0.59, ENB 19.0; 6 names
  in every (j) ordering (was 9). New holdings RSG, LH → pre-check, cross-tie, DA19. §1 wording for a complete queue and
  an all-full-conviction list.
- DA19 (RSG LH: 14 facts, 1 FAIL — LH table row labelled Q2'25 was Q3'25; 2 MINOR incl. RSG untraceable "+5.2%/+4.4%")
  corrected with inline markers. All 20 holdings independently fact-checked. Loop-10 auditors next.
- LOOP-10 AUDIT: A1 85, A2 89, A3 86 (avg 86.7). FIXES: NEW code/lead_quarter_label_check.py — maps each results-table
  revenue figure to its SEC XBRL calendar-quarter frame and flags a label that disagrees with the labelled quarter's own
  filed figure (catches the uncorrected LH row; 0 flags on all 20 current dossiers; covers the 12 December-year-end
  holdings, the other 8 still rely on DA checks; USB near-duplicate quarters were a false positive before tightening).
  §1 says the queue is complete as of the data cutoff, not for good; §6 shows the full order-dependence history
  (12→12→16→14→9→6, outputs/order_dependence_history.json) and flags holdings above 25x earnings (VEEV, RSG, MA).
  DA20 (second valuation leg for RSG, LH) running.
- 27 Sep 04:55 PUBLISHED v011_2026-09-27_claude (package sha256 9b803425…, 1062 files; parents v010, v009, v005,
  claude-v3, codex-initial-audit, codex-deep-data-audit; notes release/RELEASE_NOTES_v4_wave7.md). Build 04:50:23,
  content cd5f38e0, gate PASS, C1 331/331. Artifact v18. The full-diligence queue is complete as of the 25 Sep 2026
  cutoff. Remaining work is maintenance: weekly review, quarterly earnings refresh, next audit loop on the next change.
