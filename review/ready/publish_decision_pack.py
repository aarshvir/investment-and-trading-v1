from pathlib import Path
import json, html, re
P=Path(__file__).resolve().parent
M=json.loads((P/'decision_model.json').read_text(encoding='utf-8'))
def usd(x):return f'${x:,.2f}'
def pct(x):return f'{x*100:.1f}%'
def table(headers,rows):return '| '+' | '.join(headers)+' |\n|'+'|'.join(['---']*len(headers))+'|\n'+'\n'.join('| '+' | '.join(str(x).replace('|','/') for x in r)+' |' for r in rows)+'\n'
decision_rows=[]
for s in M['stocks']:
 b=next(x for x in s['scenarios'] if x['name']=='base')
 decision_rows.append([s['rank'],s['ticker'],s['decision'],usd(s['reference_price']),s['reference_date'][5:],usd(s['limit_price']),pct(b['irr_reference']),pct(b['irr_limit_withholding30']),pct(s['slot_weight'])])
memo='''# Investment decision memorandum

26 September 2026 · USD capital $50,000–$100,000 · independent replacement for the original allocation

## Decision

Use a smaller equity allocation and explicit entry prices. **AMP is the first direct-stock purchase candidate at $500 or less; PAYX is the second at $101.80 or less.** Allocate up to 2% of total capital to each. Their verified September 24 closes were $485.15 and $101.59. These are purchase ceilings, not instructions to pay those prices or claims about the next market opening. If the live ask exceeds a ceiling, leave that allocation in reserve.

The new-money model starts with **15% in a broad US equity fund, up to 4% in AMP/PAYX, and approximately 81% in short Treasury exposure and cash**. The completed model allows up to 25% total equity: 15% index plus 10% direct stocks. Six direct-stock slots are funded in the design; the remaining candidates compete to replace a slot, not expand the allocation. The portfolio is intentionally conservative because the stated tolerable decline is 15–20%.

The current reference prices do not justify chasing the other names. MSFT, NVDA, ALLE and HIG are the next funded conditional entries. CPAY, AIZ, SNA, NTAP and IBKR remain reserve candidates at stated limits. Avoid adding ABNB, AME or RL at their reference prices; each has a lower reconsideration level. This ranking is within the original fourteen candidates, not a claim to have found the best fourteen investments in the entire market.

**This memorandum supersedes the earlier all-WATCH conclusion.** The earlier forensic audits remain evidence of what was wrong with the original research. They are not the action list for this replacement. Research is complete enough for these dated, conditional decisions; no trades have been placed.

## Ranked decisions and entry discipline

“Buy now” means valuation-qualified for a modest new-money allocation if the live price and unchanged thesis still satisfy the limit. “Buy below” means wait for price and fundamentals together. “Avoid current price” is a rejection of adding at the reference valuation, not a prediction of an imminent fall or a personalized sell instruction. Entry limits expire at the next material filing/event or the next weekly review, whichever comes first. Do not leave them as unattended standing orders.

All annual returns below are three-year scenario IRRs. They are conditional calculations, not expected returns, probabilities or promises. The final limits also clear the chosen hurdle after the illustrative 30% withholding on direct-stock dividends. Capital-gains tax, fees and FX are additional.

'''
memo+=table(['Rank','Stock','Decision','Reference','Price date','Maximum entry / reconsider','Base IRR at reference, gross','Base IRR at limit, 30% dividend withholding','Full direct slot'],decision_rows)
memo+='''
MSFT uses the reconciled September 25 close of $516.05. Other reference prices are the corroborated September 24 closes; several September 25 public pages conflicted between their header and history table. Conflicting observations were not averaged. Fresh executable quotes must be checked before placing an order. The limits are deliberately below the model present values; they should not rise just because the share price rises.

The rank combines business quality, valuation, model uncertainty and portfolio usefulness. It is an investment judgment, not a numerical certainty score. For example, NVIDIA offers a high base-case return but also the widest and most consequential downside assumptions. It receives a smaller direct slot.

## Model portfolios and dollar implementation

The following is a new-money USD model, assuming these funds are accessible and appropriate for the investor's tax status. It does not presume existing holdings, borrowing, near-term liabilities or a particular citizenship. Capital needed soon should remain outside the equity sleeve. No leverage, short sales or options are required.

The index implementation shown is **VUAA, the London USD trading line, ISIN IE00BFMXXD54**. The reserve illustration is **IB01, the London USD trading line, ISIN IE00BGSF1X88**, together with residual cash. Both are Irish accumulating UCITS funds with a published 0.07% annual expense ratio. The fund choice is conditional on investor eligibility; a US person should not use this Irish-fund illustration without resolving the foreign-fund tax treatment. An eligible domestic S&P 500 fund and direct short Treasury bills/cash can implement the same economic allocation instead. No paid subscription or fund purchase has been made.

Initial planning weights are 15% VUAA, 2% AMP, 2% PAYX, 80% IB01 and 1% cash. Whole-share rounding increases cash. IB01 includes the 6% earmarked for currently unfilled direct-stock slots; that money has not been allocated twice.

'''
for p in M['portfolios']:
 memo+=f"### {usd(p['capital'])} initial illustration\n\n"
 memo+=table(['Instrument','Budget','Sizing price','Whole units','Illustrative cost','Capital weight'],[[r['ticker'],usd(r['budget']),usd(r['illustrative_price']),r['whole_shares'] if r['whole_shares'] is not None else '—',usd(r['cost']),pct(r['weight'])] for r in p['rows']])
 memo+=f"\nTotal {usd(p['total'])}; equity {pct(p['equity_weight'])}, reserve/cash {pct(p['reserve_weight'])}. Costs are before dealing fees.\n\n"
memo+='''
AMP/PAYX unit counts use the maximum entry prices, not the older close. ETF unit counts use September 24 NAVs—VUAA $149.0017 and IB01 $121.86—solely to make the budget concrete. NAV is not an executable exchange quote. Recompute units as floor(budget/live limit price), including the dealing charge in available cash. Vanguard's displayed £112.80 September 25 market value is the GBP VUAG line; it must not be used as a USD VUAA price. [Vanguard product and listings](https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-), [iShares reserve fund](https://www.ishares.com/uk/individual/en/products/307243/ishares-treasury-bond-0-1yr-ucits-etf-fund).

Use limit orders during liquid regular trading hours; for VUAA, prefer London/US market overlap. Obtain a fresh bid/ask, currency and instrument identity. For a fund, compare the live quote to contemporaneous indicative value and spread; do not impose a limit based on a stale NAV. A spread wider than 0.25% for the index fund or 0.15% for the Treasury fund warrants waiting or choosing an equivalent liquid implementation. These are conservative execution rules, not evidence of a current spread.

The funded conditional slots are MSFT 2%, NVDA 1.5%, ALLE 1.5% and HIG 1%. Reaching a price is not enough: refresh the business case, events and total exposure. At full deployment, preserve at least 75% reserve, at most 10% direct stocks and at most 25% equities. Do not add reserve-list names on top. A replacement must have a clearly better after-cost investment case than the displaced holding; tax and realized losses matter.

## What the risk budget does—and what it cannot do

An independent challenge rejected the initial 30% equity ceiling: the constructed tail shock lost 20.9% of capital. Reducing index exposure from 20% to 15% brings that same test to an 18.0% loss at full deployment. This is why the final portfolio differs from the earlier draft.

'''
memo+=table(['Correlated shock','Index / direct / reserve','Initial model loss','Full model loss','$50k full loss','$100k full loss'],[[x['name'].replace(' beyond tolerance',''),f"{pct(x['core_shock'])} / {pct(x['direct_shock'])} / {pct(x['reserve_shock'])}",pct(x['initial_loss']),pct(x['full_loss']),usd(x['dollars_50k']),usd(x['dollars_100k'])] for x in M['stresses']])
memo+='''
These simultaneous shocks have no assigned probabilities. They are not a backtest, VaR calculation or worst-case bound. An equity wipeout alone can still lose 25% at full deployment; worse reserve losses, currency changes and gaps can increase the loss. A stop order cannot guarantee an exit price. The 15–20% tolerance is a risk-design objective, not an insured floor.

IB01 reported September 24 yield to maturity of 4.16% and effective duration of 0.31 years. A simple duration approximation for a sudden 2 percentage-point yield rise is about −0.62% before carry; spread/liquidity effects can differ. The model therefore also stresses reserve losses of 1–2%. Yield is not fixed for three years because short securities mature and reinvest. [Issuer portfolio characteristics](https://www.ishares.com/uk/individual/en/products/307243/ishares-treasury-bond-0-1yr-ucits-etf-fund).

The 2% single-stock cap means direct positions. The additional all-in planning cap is 3.5% for any known single issuer after fund look-through. Vanguard's August 31 holdings put NVIDIA at 8.07902% and Microsoft at 5.69335% of VUAA: at full model weights, total NVIDIA exposure is 2.712% and Microsoft 2.854%. These holdings weights are dated, not live. Financial direct exposure is 3%; the fund adds financial-sector exposure. Direct sector cap is 5%; it is not a whole-portfolio sector cap. Recompute full look-through with current holdings before adding or rebalancing. [Issuer holdings](https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-).

## The return tradeoff

The reserve allocation means the whole portfolio should not be marketed as a 12–15% annual-return strategy. The following planning comparison assumes fund returns after fund expenses, direct-stock dividends reduced by 30%, no dividend reinvestment, and no personal capital-gains taxes, dealing fees or FX costs. Reserve returns are assumed to compound. The fully allocated case hypothetically fills all six stock slots immediately at their limits; in reality they may never fill and reserve returns may be lower.

'''
memo+=table(['Illustrative endpoint case','Index annual assumption','Reserve annual assumption','Initial model wealth CAGR','All slots filled wealth CAGR'],[[x['name'].title(),pct(x['index_annual_assumption']),pct(x['reserve_annual_assumption']),pct(x['initial_wealth_cagr']),pct(x['full_wealth_cagr'])] for x in M['portfolio_scenarios']])
memo+='''
The base calculation is about 4.3% annually initially and 4.9% if all slots fill. These are scenario outputs, not a forecast distribution. The benign three-year endpoint in the bear planning case does not rule out a severe loss along the way. Acute stress tests above answer a different question. Reserve yields falling to 1% would materially reduce these outcomes. Repeated weekly turnover would also reduce returns; weekly review is not a requirement to trade weekly.

For a cost sensitivity, charge 0.25% on both entry and exit for direct stocks and 0.10% each way for the index and reserve funds. At the full target this is approximately 0.23% of total capital for one round trip, before fixed commissions, FX, taxes or repeated turnover. Actual costs depend on the broker. Holding direct US shares can create tax and estate considerations for a non-US investor even where the fund sleeve is Irish; see the preserved implementation audit. Do not infer the user's tax status from the Dubai timezone.

## Why each decision survives the review

'''
for s in M['stocks']:
 base=next(x for x in s['scenarios'] if x['name']=='base')
 memo+=f"### {s['rank']}. {s['ticker']} — {s['name']}\n\n{s['thesis']} {s['countercase']}\n\n"
 memo+=f"**Decision:** {s['decision'].lower()} at a maximum {usd(s['limit_price'])}; {s['slot_note'].lower()}. Base terminal EPS {usd(base['terminal_eps'])} at {base['terminal_pe']:.1f}× gives a September 2029 terminal value of {usd(base['terminal_price'])}. Earnings period: {s['terminal_period']}. The multiple is an analyst assumption, not an observed fair value.\n\n"
 memo+=table(['Case','Terminal EPS','Terminal P/E','Year 1 / 2 / 3 dividends','Terminal price','Annual IRR at entry, gross','Annual IRR at entry, dividend withholding'],[[x['name'].title(),usd(x['terminal_eps']),f"{x['terminal_pe']:.1f}×",' / '.join(usd(d) for d in x['dividends']),usd(x['terminal_price']),pct(x['irr_limit']),pct(x['irr_limit_withholding30'])] for x in s['scenarios']])
 memo+=f"\n**Change the decision if:** {s['failure_rule']} {s['condition']}\n\n"
 memo+=f"[Detailed normalization, operating assumptions, catalysts and source locators]({s['detail_file']}).\n\n"
 links=[]
 for src in s['sources']:
  u=src.get('url',src.get('source_url',''))
  if isinstance(u,str) and u.startswith('http'):links.append(f"[Source document {len(links)+1}]({u})")
 memo+=' · '.join(links[:5])+'\n\n'
memo+='''## Methodology that replaces the original scoring system

1. Define the mandate and feasible risk budget before choosing stocks. Permit cash. Treat a holding period as thesis-dependent while using a common three-year valuation horizon for comparison. A catalyst trade needs its own event case and risk budget; none is approved by this long-horizon model.
2. Build a source ledger with company identity, units, accounting basis, fiscal period, publication date, retrieval date and a source-table locator. Archive raw responses where obtained. A provider's second display of an SEC figure is not an independent economic source.
3. Normalize economic earnings by company type. Retain stock compensation. Remove identifiable investment/tax windfalls. Charge recurring integration costs. Include ordinary catastrophe losses for insurers. Do not treat client cash or regulated capital as distributable net cash. The full company memoranda disclose departures from GAAP.
4. Project operating drivers where available—revenue, margin, tax, interest and diluted shares—or a clearly stated normalized earnings path. Use financial-sector capital/underwriting checks instead of an industrial cash-flow template. AMP has a separate segment-value check; HIG has an excess-return/book-value check. Do not average incomparable valuation methods merely to produce a single number.
5. Value three explicit earnings scenarios with disclosed terminal multiples and annual dividends. Calculate an exact cash-flow IRR and a present-value entry ceiling at an explicit hurdle. The 11.5–15% hurdles are discretionary compensation for business/model risk, not an estimated cost of equity validated by history. Multiples and growth remain judgments; ranges and sensitivities expose them.
6. Keep three-year holding dates separate from fiscal labels. NVDA and NTAP use forward fiscal earnings at the September 2029 exit; MSFT uses the completed June 2029 fiscal year; ABNB uses December 2029 earnings three months forward. These different multiple conventions are explicit. Never describe all of them as NTM.
7. Prevent double counting: do not add buyback yield to per-share growth, add excess cash already earning modeled interest, or treat the management non-GAAP label as a cash-flow definition. No stock-price-derived target growth, unsupported alpha or uncalibrated profit probability is used.
8. Independently challenge inputs, arithmetic and portfolio consequences. Source uncertainty blocks the affected claim or purchase only when material; it does not prevent explicitly labeled prospective scenarios. Missing original consensus vintages are avoided by building new analyst assumptions, not by pretending those vintages were verified.
9. Recheck events and freshness before action. Price limits depend on unchanged fundamentals; a falling price following a thesis break is not a bargain. Use a decision journal and evaluate all accepted and rejected ideas prospectively, after costs, against both the policy benchmark and simpler alternatives.

The policy benchmark is a quarterly rebalanced 25% S&P 500 /75% short Treasury blend, measured in USD after comparable fund expenses. Also show 100% short Treasuries and 100% US equity so the cost of risk reduction is visible. No performance claim is made before this prospective record exists. A valid historical strategy test would need historical membership, point-in-time filings/estimates, delistings, corporate actions and transaction costs. The old replay cannot supply this evidence.

## Three deep data audits and the final challenge

The underlying audit trail includes six first-pass specialty reviews, three additional deep data workstreams and cross-reviews. Work ran in overlapping parallel groups because the environment permits three active specialists alongside the lead. Shared model family and overlapping sources limit independence; a headcount does not turn agreement into accuracy.

The filing/accounting audit reconciled exact tables and periods, including the large NVDA/MSFT cash-flow definition errors, CPAY's mislabeled cash measure and the Airbnb EBITDA/FCF ambiguity. The market audit corroborated all fourteen September 24 closes, caught conflicting later displays, and separated current-year from next-year earnings denominators. The lineage audit found missing sessions, truncated text, poor historical coverage and survivorship/look-ahead problems; limited repairs did not certify the original backtest. These findings are retained in the dashboard and original deep-audit files.

For this replacement, specialist teams rebuilt all fourteen company cases from primary filings/releases. A separate reviewer checked CPAY/NTAP/AME normalization, fiscal periods and limit math. The fund check independently verified USD listing identities and the GBP-price trap. The portfolio challenge changed the actual allocation. The final calculation audit checks 42 scenarios, tax-sensitive ceilings, weights, dollars and spreadsheet formulas. The entry limits for PAYX, SNA and RL were reduced after the withholding sensitivity; PAYX was reduced again to $101.80 after the dealing-cost challenge; AME still needs its post-close funding bridge before a purchase even at the reconsideration price.

Financial Datasets was callable but the actual request returned a zero-credit balance, so it provided no financial data. FMP produced usable NVDA/MSFT observations; other tested requests hit access limits and sample responses were rejected. Primary sources and recorded public price corroboration support this replacement. The requested Druckenmiller composite remains incomplete because three required inputs could not be produced reliably; no synthetic regime score controls this portfolio. These source limitations do not become invented validation claims.

## Weekly operating rules

The Sunday review at 18:00 Dubai is a research refresh, not intraday monitoring or automated execution. Read the companion weekly policy for the decision sequence. Each report must show what changed, whether that change alters normalized earning power or valuation, the revised limit, portfolio capacity, the next catalyst and the resulting buy/add/hold/reduce/sell/no-trade decision. Preserve the old forecast and explain revisions rather than overwriting the record.

For an owned position, reduce or sell when a material thesis failure survives examination, capital must be protected under the agreed risk policy, or the forward return becomes inadequate and a clearly better after-tax alternative exists. A high valuation alone is not an automatic liquidation instruction. There are no current holdings in this record, so this pack supplies the new-money model and explicit future sell rules; it cannot name personal positions to liquidate.

Unknown facts remaining are specific: future operating results and multiples, live execution prices, personal tax/access details, actual positions, the unresolved AME financing bridge, full original historical-data quality and incomplete regime inputs. They are not hidden behind an overall confidence percentage. The recommendations are defensible conditional judgments, not certainty.
'''
(P/'INVESTMENT_DECISION_MEMO.md').write_text(memo,encoding='utf-8')

policy='''# Weekly investment policy — replacement version

Effective 26 September 2026; supersedes audit-only action instructions. Review Sunday 18:00 Dubai. This is scheduled research, not execution or continuous surveillance.

## Mandate and controls

USD $50,000–$100,000 new-money model; flexible thesis-dependent holding periods; 15–20% tolerable drawdown. Initial model 15% index +4% direct stocks +81% reserve. Maximum proposed equity 25%, split15% index/10% direct; at least75% reserve at full deployment. Direct name cap2%, direct sector cap5%, known issuer look-through planning cap3.5%. No leverage. These are analyst-proposed policy constraints, not a guaranteed loss floor.

## Review sequence

1. Establish the latest completed US session and actual portfolio, if supplied. Do not infer fills from a price crossing a limit. Keep hypothetical model holdings separate from actual holdings. Timestamp cash, costs, dividends, corporate actions and flows; calculate a cash-flow-adjusted portfolio high-water mark before reporting drawdown.
2. Refresh primary filings/releases, earnings events, relevant credit/regulatory developments, splits and reliable price observations. Log retrieval failures and material conflicts. Reuse unchanged archived filing facts with an event/freshness check; do not rerun a full forensic exercise for an unchanged fact.
3. For new or materially changed decision-critical data, run three bounded parallel checks: exact filing/accounting reconciliation; quote/estimate/fiscal-period reconciliation; transformation/availability/risk-impact audit. Record raw hashes and locators. Shared source lineage is not independent confirmation.
4. Rebuild affected earnings bridges, three scenarios, dividend cashflows, IRRs and maximum entry prices. No automatic mark-up with the market price. A future EPS assumption is analyst judgment unless a dated management/consensus source proves otherwise.
5. Apply the stock's thesis-failure rule and reassess each material event. Buy below the published limit only while the business case and risk capacity still pass. Entries expire with material news or the next review. Do not leave old limits as standing instructions through an earnings release. Within five trading days of scheduled earnings, wait for the release or explicitly underwrite the gap risk; no automatic purchase.
6. Test proposed fills, fund overlap, sector/name caps and correlated shocks. At full target, the severe test is -14.25% and the tail test -18.0%; use current exposure and assumptions on each run. If the tail test exceeds20%, reduce the proposed equity exposure before recommending an addition. This gate is a scenario constraint, not a forecast guarantee.
7. Publish a decision journal: prior action/limit, new action/limit, changed fact, source and period, thesis impact, risk/return calculation, allocation effect and next catalyst. Report NO TRADE where justified. Never manufacture an action to fill a weekly quota.

## Buy, hold and sell rules

BUY/ADD requires the live executable price at or below the refreshed limit, an intact thesis, event clearance and funded capacity. The initial eligible names are AMP≤500 and PAYX≤101.80; current conditional funded slots are MSFT≤500, NVDA≤215, ALLE≤145 and HIG≤120. All thresholds are superseded by later dated reviews. Reserve-list candidates may replace a slot after comparison; they cannot expand the10% direct sleeve.

HOLD means the original economic case still works and transaction/tax costs outweigh the value of switching. Do not automatically sell because price exceeds the original buy ceiling. Review trimming when prospective base return falls below8% for a direct stock, while checking downside, alternative returns and personal taxes; this is a judgment threshold, not a validated trading signal.

REDUCE/SELL is supported by a material thesis break, capital/liquidity need, cap breach, or inferior forward economics after costs. Ordinary price volatility alone does not prove thesis failure. Write down the reason and the updated value before acting; never relabel a failed short-term trade as a long-term investment to avoid recognizing the failure.

Portfolio drawdown response, once actual holdings are available: at8% below the cash-flow-adjusted high-water mark, freeze additions pending a risk review; at12%, re-underwrite the portfolio and recommend cutting weaker/high-risk equity exposures toward15% total; at15%, treat capital preservation as the priority and recommend reducing equity toward10% unless the user explicitly revises the mandate. These thresholds are discretionary emergency controls, not backtested optimal stops; execution gaps may bypass them. A weekly process can miss an intraweek breach. No daily monitoring or automatic liquidation is provided.

For a material data outage, pause the affected new discretionary purchase. Do not automatically sell an intact existing business because a provider is unavailable. Use primary-source alternatives and retain uncertainty. Do not require repair of unrelated historical price gaps before making a transparent forward valuation.

## Measurement and maintenance

Keep decisions, fills, dividends, costs and cashflows separately. Compare net time-weighted performance with quarterly-rebalanced25%S&P500/75%shortTreasury, all-Treasury and all-equity benchmarks. Track forecast errors, drawdowns, turnover, costs and rejected ideas prospectively. Do not present the original flawed replay as validation.

Update decision_model.json, company models, the memo, workbook and current dashboard views together, preserving prior dated versions and original archive tabs. Reconcile all weights, dollars, corporate actions and tax conventions. Publish actual returns only from actual dated holdings. The model remains research; no brokerage access or order placement is authorized.
'''
(P/'WEEKLY_POLICY_V2.md').write_text(policy,encoding='utf-8')

industrial='''# CPAY, NTAP and AME — normalized operating cases

26 September 2026. Three-year holding period to September2029. Future EPS, multiples and dividends are analyst assumptions. The entry ceiling is the present value of annual dividends and terminal EPS×P/E at the specified hurdle; no buyback yield is added. The final consolidated model supplies exact IRRs and withholding sensitivities.

## Corpay

Q2 revenue was $1,338.809m; management reported10% organic growth and FY2026 adjusted EPS midpoint$27.35 versus GAAP midpoint$19.70. Normalize the adjusted figure by deducting guidance stock compensation of$150m and an annualized integration/deal-cost allowance of$110.106m, both at26% tax and66m diluted shares:27.35−150×0.74/66−110.106×0.74/66=$24.43366. The integration allowance doubles the disclosed H1$55.053m; this annualization is our assumption. Acquisition amortization remains excluded, so this is a cash-earnings proxy, not GAAP or distributable FCF.

Base FY2029 EPS grows9% annually to$31.6423, below the recent10% organic revenue growth comparison but still dependent on margin/financing stability. At16× the terminal value is$506.28; the12.5% hurdle gives$355.57 gross present value. Choose$350. Bear EPS$20×11=$220; bull$35×19=$665; no dividends. The16× multiple reflects recurring payments economics with a discount for leverage and regulatory risk; it is a judgment, not a peer-derived statistical result.

H1 CFO less capex was$1,307.95m, distinct from the$861.554m company adjusted-income figure previously mislabeled as FCF. Client settlement flows can make conventional cash flow volatile. Management leverage2.55× uses a different definition from vendor leverage and should not be silently substituted. Interest guidance$435–465m matters to equity earning power. Watch organic corporate-payments growth, debt repayment and the FTC settlement cash outcome. Suspend the case if organic growth stays below5%, leverage exceeds3.5× with weak repayment, or customer-funds/compliance problems emerge.

[Q2 release and reconciliation](https://www.sec.gov/Archives/edgar/data/1175454/000117545426000045/ex991q2_2026.htm) · [June10-Q, cash flow and contingencies](https://www.sec.gov/Archives/edgar/data/1175454/000117545426000050/cpay-20260630.htm).

## NetApp

Q1 FY2027 revenue was$2,025m, up30%; CFO$503m versus$673m and FCF$401m versus$620m show weaker cash conversion. Inventory turns fell to6 from14. Use the midpoint of GAAP FY2027 guidance$7.35–7.65: $7.50. Non-GAAP guidance$9.73–10.03 includes a$2.19 stock-compensation adjustment, which this model does not add back.

The base grows GAAP EPS10% annually to FY2030$9.9825 and applies21×:terminal$209.63. FY2030 ends April2030, seven months beyond the September2029 exit; this is an explicit forward-fiscal multiple. Bear EPS$6.25×14=$87.50; bull$12×24=$288. Base annual dividends$2.08/$2.16/$2.24. At12% the gross ceiling is$154.39; choose$150, which also clears the dividend-withholding sensitivity. This is well below the$197.24 reference price.

The base assumes storage demand supports double-digit earnings growth while valuation returns to a more ordinary level; the bear reflects declining earning power and a lower multiple. Watch inventory, cash collection and AI-related storage orders. Cancel entry if inventory turns remain below8 while growth falls below10%, cash conversion continues to deteriorate, or operating-margin guidance is cut over200bp without a temporary bridge.

[Q1 results, guidance and GAAP reconciliation](https://investors.netapp.com/news/news-details/2026/NetApp-Reports-First-Quarter-of-Fiscal-Year-2027-Results/default.aspx) · [July10-Q](https://www.sec.gov/Archives/edgar/data/1002047/000119312526380207/ntap-20260731.htm).

## AMETEK

Pre-close FY2026 GAAP guidance was$7.19–7.29 and adjusted guidance$8.20–8.30. Use$8.25 plus an analyst$0.05 tentative acquisition-accretion allowance=$8.30. That$0.05 is not company quantified guidance. Adjusted earnings exclude acquisition amortization and certain integration/financing costs; stock compensation remains charged. This is not GAAP earning power.

Indicor closed August26 for$5bn cash; the issuer expects about$350m of2026 sales and modest earnings accretion. June debt$2,036.174m and cash$495.446m predate the close and cannot establish the new leverage or interest burden. Consequently$185 is a reconsideration level, not purchase approval without a post-close debt/interest/integration bridge.

Base EPS grows9% annually from the tentative$8.30 anchor to FY2029$10.7487 and receives24×. Bear$7.50×20=$150; bull$12×28=$336. Base dividends$1.36/$1.46/$1.56. The12% hurdle gives about$187.11 gross PV. At the$247.74 reference, even the base offers too little compensation for acquisition risk. The premium24× multiple already gives credit to the instrumentation franchise; do not inflate it to justify the current quote. Revisit after the first post-close financing disclosure and evidence of organic growth and integration returns.

[Q2 results and guidance reconciliation](https://investors.ametek.com/news-releases/news-release-details/ametek-announces-record-second-quarter-2026-results-and-raises) · [Indicor closing disclosure](https://investors.ametek.com/news-releases/news-release-details/ametek-completes-acquisition-indicor-instrumentation) · [June10-Q](https://www.sec.gov/Archives/edgar/data/1037868/000103786826000175/ame-20260630.htm).
'''
(P/'industrials_payments.md').write_text(industrial,encoding='utf-8')
print('Published decision memorandum, weekly policy and three company cases.')
