# Weekly lineage, transformation and risk audit — 27 September 2026

**Retain the maximum 25% equity allocation and existing stock entry limits.** The completed Claude v011 package adds substantial company research and reproducible risk calculations. It does not establish a selection advantage or make a fully invested stock portfolio compatible with the user's stated 15–20% temporary-loss tolerance. The most material new finding is a capital-accounting omission in v011's financial-company valuation scenarios: repurchases reduce shares without reducing aggregate book equity.

Parents reviewed: **v011_2026-09-27_claude** and **v005_2026-09-26_codex**, following AGENTS.md, RESEARCH_VERSIONING.md, LATEST_HANDOFF.md and the shared catalog. All published files and Claude's working branch were read-only. Calculations below use the immutable v011 ZIP, rather than assuming its active working branch is identical. The current `review/ready/decision_model.json` was identical to the archived v005 model at this audit's start. Companion JSON records the archive hash, calculations, coverage and limitations.

## What the new evidence establishes

The v011 candidate array contains **350 rows, 336 nonmissing diligence verdicts, and 214 eligible companies**; its final portfolio has **20 holdings**. Those counts reproduce. The 14 other verdict values are JSON NaN, not actual completed assessments; the count must use missing-value semantics rather than merely test for null. Precise portfolio weights sum to 100%; rounded display rows sum to 99.999%, an immaterial rounding difference. Financials are 25%; maximum single holding is WEC at about 8.323%. These are weights of the Claude stock sleeve. At a 10% whole-portfolio sleeve, that maximum becomes about 0.8323% of total capital; at 100% stocks, it remains 8.323%. Mandates must not be mixed.

Expanded diligence is useful for sourcing future candidates. The fact that AMP/PAYX are eligible but outside v011's top twenty is an ordering outcome, not a disproof of their absolute entry valuations. Conversely, v005's fourteen-company scope never established that those were the best opportunities across the whole index.

The new archived price panel has **752 of 759 columns populated on 22 September**, including **all fourteen v005 names and all twenty v011 holdings**. This removes the known date gap for those names in the new dataset; it does not repair or certify the preserved old dataset. Seven absent panel values are not automatically outages; coverage can differ by instrument and listing history.

## Risk recalculations and their limits

I independently recalculated from the archived dividend/split-adjusted daily panel, using fixed target weights for the covariance calculation, sample covariance with 252 trading days per year, and SPY as benchmark:

| Measure | Independently recomputed v011 stock sleeve |
|---|---:|
| Window | 25 September 2023–25 September 2026 |
| Complete daily-return observations | 754 |
| Days lost to missing holding returns in this window | 0 |
| Annualized volatility | 13.5481% |
| Beta to SPY | 0.592906 |
| Annualized tracking error | 11.8352% |
| Inverse concentration of portfolio weights | 18.8746 |
| Inverse concentration of risk contributions | 18.9823 |

These match the archived figures to rounding. The final two numbers are concentration measures, **not proof of nineteen statistically independent bets**. Equal risk contributions can produce a high effective count even when the holdings share common risks. The model itself attributes about 44.8% of sample portfolio variance to its market factor.

For crisis tests, I separately reconstructed the sleeve from 4 January 2005 through 25 September 2026, rebalancing at quarter boundaries and excluding unavailable names with weights renormalized. No held-name missing return needed zero filling in this reconstructed path. Its maximum drawdown is **47.7042%**. Mean missing original target weight over the full history is 3.6088%; maximum is 16.4786%.

| Episode / dates | Today's v011 stock sleeve, episode return | SPY episode return | 15% SPY /10% v011 sleeve /75% reserve: worst drawdown within episode |
|---|---:|---:|---:|
| GFC, 9 Oct 2007–9 Mar 2009 | -47.3495% | -55.1894% | -12.6973% |
| COVID, 19 Feb–23 Mar 2020 | -37.4317% | -33.7173% | -8.5318% |
| 2022, 3 Jan–12 Oct | -17.3427% | -24.4964% | -4.1054% |

All six archived crisis episode calculations reproduce. In the GFC and 2011 episodes, **GDDY and VEEV had no history: 6.2094% of original target weight was excluded and the available holdings renormalized**. This is a selected-survivor replay of today's portfolio, not a point-in-time investment strategy backtest. The 15/10/75 column uses v011's twenty stocks and an assumed constant **4% annual reserve return**, not v005's six direct-stock slots or the actual historical Treasury path. It therefore supports defensive allocation in principle; it does not validate v005's portfolio track record.

Corporate-action coverage is explicit: the panel is Yahoo's retrospective split/dividend-adjusted total-return proxy, with five listed historical spin-off double-count corrections. It is not a full independent certification of every corporate action. The new data and visible adjustment ledger improve lineage, but the former Sep22 patch's pending basis questions cannot be declared globally settled from the presence of a newer panel alone.

The v011 bootstrap uses twenty thousand stationary-bootstrap paths, a 21-day mean block, seed 7, a 2005–2026 source window, assigned market drifts and zero stock-picking alpha. Its probabilities are conditional simulation outputs. The audit grades **85/89/86** are reviewer rubric scores, not investment odds. Neither the grades, the recent beta, nor a simulated zero frequency of a particular loss event warrants raising the equity cap.

Recomputing v005's simultaneous stress arithmetic leaves initial/full losses unchanged: **-6.10%/-8.50%** for the selloff, **-10.71%/-14.25%** for severe stress, and **-13.62%/-18.00%** for the tail. These are instantaneous scenario losses, with reserve marks stressed separately; they are not maximum losses or probabilities. The 25% cap remains a defensible design choice under the expressed tolerance, not a guarantee.

## Quarter-label controls: adopt the tripwire, correct its coverage claim

The release notes say twelve December-year-end holdings are mechanically checked and eight are excluded. The archived `quarter_label_check.json` actually marks **thirteen checkable and seven not checkable**.

More importantly, I traced the archived detector against the actual dossier text and the available local SEC companyfacts cache. It recognizes **110 quarter-labelled rows** across twenty holdings. Its parsing produces:

| Outcome | Rows |
|---|---:|
| Revenue matches the target calendar-quarter frame | 34 |
| No matching SEC revenue value; no flag generated | 11 |
| Target quarter unavailable; no flag generated | 2 |
| Non-December year end, skipped | 28 |
| No parsable revenue field | 11 |
| Numeric value below 50, skipped | 21 |
| Explicit correction marker, skipped | 3 |

Only **seven holdings have at least one matched target-revenue row** under this mechanism. LVS, DOV and HBAN have no recognized quarter-row labels; AXP/BALL values are skipped by the less-than-50 filter; PGR's selected figures do not match one of the detector's revenue concepts. Some unmatched Q4 amounts require annual-minus-nine-month derivation. These are coverage limitations, **not eleven newly proven bad figures**.

The check only flags a revenue value when it matches a different SEC quarter and the purported quarter also has a contradictory value available. A wholly unrecognized number does not flag. It does not verify EPS, operating income, fiscal-quarter mappings, every unit, or all other table cells. Corrected rows are deliberately skipped. The companyfacts cache used for this detailed reproduction is external to the release package; the script has no filing-availability cutoff filter. Therefore “zero flags” cannot mean all quarterly data is validated.

Adopt the detector as an additional control. A stronger successor should report matched/unmatched/skipped denominators, normalize million/billion units, derive fiscal periods from explicit start/end dates, reconcile Q4, test every load-bearing column and preserve the filing/accession used. Do not remove a valid manual check merely because automation is silent.

## AMP: the disagreement is not entirely a harmless choice of method

X1 correctly reproduced v005's AMP EPS normalization and cash-flow arithmetic. Its broad statement that the v011 and v005 valuation gap is solely a methodology choice is incomplete.

In archived `v4/code/v1_valuation.py`, line 615 defines payout as **dividends / net income**. Lines 627–629 then increase total equity by retained earnings while independently decreasing shares using historical share-count growth. **Repurchase cash is not deducted from total book equity.** A share repurchase reduces cash/equity as well as shares; otherwise future book value per share is overstated. This affects financial-company scenarios using that routine, particularly a heavy repurchaser such as AMP. Historical ROE assumptions do not repair the missing capital roll-forward.

At AMP's archived $493 reference, its V1 base scenario uses historical exit P/B **3.595x**, not the peer median 2.746x. It forecasts $575.82 terminal price and 6.48% three-year terminal-wealth CAGR. Simply holding shares constant while retaining the same aggregate-book forecast reduces terminal price to **$486.27** and the CAGR to **0.85%**. The bull version changes from **67.65% to 53.86%**. This is a **no-repurchase sensitivity**, not a repaired realistic buyback forecast; it isolates the contribution of free share shrinkage. A proper repair needs the repurchase expenditure/price path and corresponding equity, retained earnings, dividends and regulatory capital.

The AMP dossier itself flags the spectacular bull outcome as an artifact. It also cites an unverified 2023 dividend of $1.35 despite X1 later validating the current $1.70, and describes about $6bn net cash as parent-level from a consolidated Yahoo debt/cash field without a parent-entity bridge. Neither stale dividend information nor that capital attribution should enter a fresh valuation.

**Keep v005's normalized operating-EPS model, crosschecked by segment valuation, as the main decision basis.** Wealth/asset management and legacy insurance have different earnings and capital economics; historical P/B and heterogeneous financial peers are supplementary checks. The $44 normalized baseline removes the Comerica benefit, 7% EPS growth is far below the latest reported quarterly growth, and the $500 limit remains below the tax/cost-adjusted base-case ceiling. Buybacks are reflected once in per-share growth, with no separate buyback yield or unverified surplus-cash addition. This is still an analyst forecast, not a finding that v005's growth or terminal multiple is certain.

## Cross-version corrections, fund dates and entry decisions

Adopt newly corroborated dated price references in the new weekly model, without overwriting old observations. The MSFT $516.05 versus $516.17 discrepancy should be recorded as a correction to the earlier reference claim once root's independent source check completes; it does not change a $500 entry limit. AMP's archived Sep25 $493 similarly supersedes the earlier unresolved display conflict for the weekly snapshot, not retrospectively rewriting the evidence log.

X1's claimed exact replication of the v005 portfolio return table is only approximate: it compounded stock IRRs, whereas the delivered model adds terminal stock value and **non-reinvested dividends**, then computes portfolio wealth CAGR. The correct formulas were independently verified previously. For the new release, retain the actual model convention rather than inheriting the verifier's reverse-engineered explanation.

X1's PAYX “not confirmed” historical-multiple item is chiefly a requested disclosure, not a demonstrated error in a claim v005 actually made. Its quoted v005 wording describes 20x as a 5% earnings yield; it does not claim 20x is inside a ten-year trading range. Also, historical GAAP P/E observations and an adjusted forward-earnings exit multiple need aligned definitions before comparison. A conservative exit multiple should be justified economically, not lifted merely to match historical valuation peaks.

All fourteen existing limits remain below their recomputed base-case maximum after **30% dividend withholding plus 25bp entry and exit cost stress**. PAYX's mathematical maximum is about $101.846, leaving only a small margin above the practical $101.80 limit; additional fixed fees can matter. Only AMP/PAYX meet their old limits at v011's archived Sep25 price observations. Fresh prices alone do not justify changing normalized earnings or raising a limit.

Root separately supplied fresh issuer fund observations for arithmetic checking: **VUAA NAV $149.7632 and IB01 NAV $121.89 on Sep25**; IB01 **4.16% YTM and 0.31-year duration remain dated Sep24**; Vanguard company weights remain dated Aug31. These different dates must remain visible. NAV is not an executable exchange quote; YTM is not a guaranteed three-year cash return. The issuer-source archive/validation is root's workstream, not claimed as a second independent retrieval here.

At those NAVs and unchanged stock limits, the $50,000 illustration remains 50 VUAA /2 AMP /9 PAYX /328 IB01 shares, with **$615.72 cash** and **18.80872% equity**. The $100,000 illustration is 100 /4 /19 /656, with **$1,129.64 cash** and **18.91052% equity**. Thus the NAV refresh changes amounts, not the allocation policy. Full NVIDIA/Microsoft look-through remains **2.711853% /2.8540025%**, below the 3.5% planning cap, based on the disclosed Aug31 issuer weights.

## Druckenmiller readiness and final disposition

The requested synthesizer requires five genuine upstream reports less than 72 hours old. The workspace still contains only two valid report families: breadth and uptrend, generated Sep26 from Sep24 data. Market-top, macro-regime and FTD reports are missing; the environment check shows no FMP key available to this process. The v011 archive does not supply these missing report families. **No synthesized conviction score is issued.** The two breadth inputs share provenance and are not independent provider confirmations. Generic skill allocation bands cannot override the user's loss-tolerance mandate.

**Adopt:** expanded source coverage, visible primary corrections, current price/fund observations after their independent checks, the limited quarter tripwire, zero-alpha framing, and reproducible risk arithmetic.

**Reject:** changing to 100% stocks on the strength of audit grades, treating zero flags as complete validation, calling risk-concentration counts independent bets, importing defective buyback/book scenarios, or interpreting v011's hypothetical defensive replay as the historical performance of v005's selected stocks.

**Leave explicit:** mandate differences, selection-order sensitivity, unvalidated growth/multiple assumptions, unresolved corporate-action completeness and the absence of a demonstrated stock-selection edge. No new evidence reviewed here warrants changing the 25% equity cap, 2% direct-name cap, 3.5% look-through planning cap, or existing entry limits. The final updated weekly model will receive a separate numerical reconciliation before publication.

## Final weekly model and workbook reconciliation

The final weekly JSON and workbook passed **2,981 numerical, formula-link and metadata checks, with zero failures; all 1,262 formula caches are present and no Excel errors were found.** All forty-two operating cases retain their terminal earnings, multiples and dividends; all fourteen limits, required returns and stock weights remain unchanged. All fourteen price references are dated September 25, and workbook actions, dates and terminal periods match the final model. After-withholding-and-cost IRRs/PVs independently reconcile, including 25bp entry and exit costs. Every published limit passes that modeled cost gate. Exact final model/workbook hashes are retained in the companion JSON.

The final HIG condition correctly states **WAIT**, identifies the **$393m expected GAAP gain as excluded from core EPS**, says the **$1.5bn reinsurance limit was already exhausted**, and requires settlement/capital reconciliation before entry. HIG retains no initial allocation and its $12 normalized core-EPS anchor is unchanged. This review verifies faithful representation of the filing-audit finding; the disclosure does not create an automatic earnings upgrade or purchase merely because the stock touches $120.

PAYX is explicitly a conditional starter BUY within the 2% cap; **no subsequent ADD is allowed before demonstrated cumulative cash recovery**. NTAP remains WAIT with zero allocation; its September 25 PEAK:AIO acquisition requires a consideration, financing, dilution and integration bridge, with no unverified synergy value. These metadata changes do not alter scenario arithmetic or increase exposure.

The prior static-output issue is resolved: **After costs now contains 504 linked formulas across all 42 cases**, using the editable Scenarios reference price, limit, hurdle, tax, dividends and terminal value. Exact formula links, all 336 helper cashflow caches and 168 displayed output caches were independently verified; the tax label now correctly says it follows the Scenarios input. Editing those inputs is therefore reflected through spreadsheet formulas on recalculation. This audit checked formula structures and current cached values; it did not launch a spreadsheet calculation engine. Published decision limits remain recommendations and should not be automatically raised merely because a user changes assumptions.
