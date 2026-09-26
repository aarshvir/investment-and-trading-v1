# Weekly investment policy — revised mandate

Status: proposed operating policy for research recommendations, not an execution authorization. User clarified on 25 September 2026: $50,000–$100,000 capital; flexible holding periods; weekly buy/hold/sell review; 15–20% tolerable drawdown. No positions or trading permissions supplied. Do not infer that any recommended stock is already held.

## Portfolio risk budget
- Use 15% as planning loss budget, 20% as escalation boundary, never as guaranteed maximum loss.
- Initial design ceiling: 30% total equity exposure, 70% liquidity reserve, assuming equity stress −50% and reserve unchanged. This is a stress-budget design, not an optimized recommended allocation. At −60% equities it loses 18%; reserve/product risk can worsen either result.
- Within that ceiling: at most 10% of total capital in individual stocks; at most 2% of total mandate capital per directly held stock; at most 5% of total mandate capital per sector in the individual-stock sleeve; residual equity capacity may be diversified fund exposure only after suitability and product checks. The reserve's exact instrument, yield, issuer/counterparty risk and withdrawal timing must be specified before implementation.
- Do not fill allocations to hit a quota. All unapproved risk allocations stay uncommitted. Current original basket is NOT approved for deployment.
- Risk denominator is provisionally the $50,000–$100,000 mandate capital; household suitability is not established. Report mandate-only and aggregate exposure including separate algorithmic trading. The proposed ceiling is not an instruction to liquidate unknown existing holdings.
- Direct-stock caps apply to the direct sleeve; separately report combined issuer/sector exposures through funds. Count overlapping index holdings and existing accounts in aggregate exposure; no margin, leverage, shorting, or options in this policy.
- Hypothetical position risk budget: 0.25% of total capital per thesis; position = min(2% capital, risk budget / stress loss fraction). A 25% single-stock stress therefore implies 1% capital. Stress fraction is not a reliable stop price.

## Data and evidence gate
- Fix an explicit completed-US-session cutoff. Store UTC retrieval time, market close date, publication/filing date, fiscal period, provider, URL, source hash, units, GAAP/adjusted basis, fiscal-year/NTM basis, currency and corporate-action treatment per material field.
- Quotes require a fresh actionable broker/exchange quote at execution; a weekly snapshot is not an order price. Compare two independent sources where available. Price disagreement >0.5% after timing/adjustment alignment requires reconciliation. This threshold is an operating tolerance, not a claim of accuracy.
- Price/forward EPS internally matching a vendor P/E is arithmetic reconciliation only. It does not validate the EPS forecast or its horizon.
- Missing leverage, capital adequacy, guidance, filings, or consensus is UNKNOWN, not PASS and not zero. Company-specific evidence requirements follow the business model, not broad GICS sector.
- Require two years of quarterly and annual filing analysis for investment approval, including cash-flow reconciliation, share dilution, debt maturities, segment economics, capital allocation, and major risk changes. Release keyword counts do not fulfill this gate.

## Fundamental investment decision
- Separate business quality, valuation and expected return, evidence quality, and portfolio fit. Do not turn them into a probability by averaging scores.
- Use FCFF/WACC/net debt or FCFE/cost of equity consistently. Do not replace necessary growth capex with assumed owner earnings without a documented bridge. Normalize earnings symmetrically.
- For per-share EPS growth return decomposition, do not add repurchase yield again. Model terminal valuation separately: price ratio = EPS growth factor × terminal multiple/current multiple, plus dividends. Explicit scenario cases have no probabilities until calibrated.
- Route banks/brokers to regulatory capital, liquidity and stress tests; insurers to reserve adequacy/underwriting/capital; payment processors and asset managers to their actual debt/cash-flow model; REITs to AFFO/NAV and debt maturity analysis.
- State stock thesis horizon (typically quarters/years) separately from weekly review frequency. Short-term technical trade theses require a separate tested strategy and a separately limited risk budget; this policy does not manufacture one-day stock forecasts.
- Entry requires verified material data, documented bear/base/bull cash-flow or earnings models, justified valuation range, evidence of a differentiated thesis, and portfolio risk capacity. No fixed quota of approved stocks.

## Weekly actions
- BUY/ADD: all evidence gates pass, live price below approved entry limit, thesis intact, costs considered, and risk capacity exists.
- HOLD: an actual holding is confirmed, thesis intact, valuation acceptable, portfolio exposure inside limits.
- REDUCE: actual holding breaches position/factor/sector exposure, valuation no longer compensates risk, or fundamentals deteriorate without full invalidation.
- SELL: actual holding has documented thesis invalidation, governance/accounting failure, serious liquidity deterioration, or an approved risk-rule trigger. Prefer rational thesis evidence to weekly rank changes.
- WATCH: promising candidate with incomplete evidence or no entry margin. INSUFFICIENT DATA: material inputs missing/stale/conflicting. No fresh buys on either status.
- Rank changes alone do not force trades. Use hysteresis: ordinary discretionary switch requires two weekly observations and positive net expected benefit after spreads, commissions and applicable taxes; urgent thesis breaks override the wait. 5% of portfolio one-way weekly turnover is a review threshold, not a forced trade target.
- Portfolio drawdown measured daily from a cash-flow-adjusted high-water mark: at −8% review aggregate risk; at −12% suspend adds pending review; at −15% urgent capital-protection review; −20% represents breached tolerance, not an exit guarantee. These are proposed governance thresholds, not backtested optimal rules. No daily monitoring is active unless separately implemented; weekly scheduling alone cannot enforce these alerts.
- Data-provider failure freezes new discretionary buys; it does not automatically require liquidation of existing positions. Report failed/stale inputs explicitly.
- Define one-way weekly turnover as 0.5 × (gross purchases + gross sales) / opening NAV, with contributions and withdrawals separately reported.
- Stop orders can fill worse than their trigger after gaps; stop-limit orders can fail to execute. Do not imply either caps realized loss.

## Weekly review record
- Weekly automation created and ACTIVE: Sunday 18:00 Asia/Dubai, using the latest completed US session. Automation id: weekly-investment-evidence-and-action-review. This schedule is editable. No automatic trading or daily monitoring.
- Refresh all ~500 universe members for dated, available fields, reconcile constituent changes, and explicitly mark unavailable refreshes. Deep re-underwrite holdings and high-priority candidates on material change; do not falsely claim 500 fresh company deep dives weekly.
- An eventual order sheet requires actual shares/cash timestamps, exact contract, current/target weights, dollar/share changes, approved entry limit, spread/fees/FX, funding/settlement constraints, expiry and reviewer. No sheet is executable without current quotes and holdings.
- Report dated BUY/ADD/HOLD/REDUCE/SELL/WATCH/INSUFFICIENT DATA rows, evidence, old/new thesis, entry limit if approved, invalidation condition, target weight only if approved, costs and trade reason.
- If holdings are unknown, deliver candidate research only and mark personalized HOLD/REDUCE/SELL unavailable. Never claim current holdings or execute trades.
- Freeze model version before future outcomes. Track a shadow portfolio, no-trade benchmark, turnover, slippage, drawdown, factor exposure and realized thesis performance. Backtests require historical membership, filing availability and delisting returns; use walk-forward development/validation/test separation and transaction costs.
- Notify weekly with the requested action report, including a brief NO CHANGE when appropriate; report failed/stale input refresh explicitly. No promises of live/daily surveillance.


## Mandatory three-pass data audit, added 26 September 2026

For each new or materially changed decision-critical input use three parallel bounded reviewers: (1) source filings/accounting bridges; (2) instrument, market session, corporate action and estimate definition/vintage; (3) historical availability, transformations and before/after portfolio impact. Preserve disagreement and shared source lineage. Reuse unchanged evidence only after event/freshness checks. Read DEEP_DATA_AUDIT.md and all deep_audit reports before each refresh.

- Archive full responses/documents when available; retain accession, acceptance/publication time, fiscal interval, tag/context/unit, transformation, ingestion time and hash. Label observation extracts and manual transcriptions accurately. A hash proves retained bytes, not source truth.
- Reject error responses, provider bundled samples, wrong symbols, wrong dates and stale last-good data. No access upgrade or paid feed is assumed. Current FMP access verified two names; Financial Datasets documentation alone validates no figures.
- Block affected signals on unexplained session gaps. Keep original and repaired series separately; do not fill daily holes with zeros or splice incompatible dividend-adjustment vintages. Recompute dependent measures and document materiality. The remaining 426-stock September 22 outage is unresolved.
- Use complete numerical GAAP/non-GAAP and cash-flow bridges. Do not confuse company-defined FCF, CFO less cash capex, economic owner earnings and after-finance-lease-principal cash. Keep forecast, management claim and actual separate.
- Require original forecast vintage and accounting definition; FY1 is not NTM. Require contemporaneous membership, genuine prior periods, original filing availability, restatements, delistings and transaction costs for strategy validation.
- Apply the requested Druckenmiller skill only after all five required reports pass strict schema and underlying-observation-date checks. File modification time is insufficient. Do not let absent market-top values imply zero risk or bearish agreement inflate directional conviction. The current two partial inputs cannot produce an allocation score.
- Update source corrections everywhere in the current decision view; retain earlier reports as dated evidence, clearly superseded. The corrected Airbnb quarterly FCF claim is supported. Quarantined vendor headline cash-flow fields are not proof that all saved quarterly statements are wrong.

The Sunday 18:00 Dubai automation was updated to include these requirements. No daily monitoring or brokerage execution was added.
