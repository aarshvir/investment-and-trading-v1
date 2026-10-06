from pathlib import Path
import json,csv,datetime,zipfile,hashlib
R=Path(__file__).resolve().parents[3]; W=Path(__file__).resolve().parent; P=R/'review/ready'
M=json.loads((P/'decision_model.json').read_text()); A=json.loads((W/'market_audit.json').read_text()); by={x['ticker']:x for x in A['rows']}
with zipfile.ZipFile(W/'baseline/delivered_v005_convenience_state.zip') as z: old=json.loads(z.read('review/ready/decision_model.json'))
prior={s['ticker']:s for s in old['stocks']}
def money(x): return f'${x:,.2f}'
def pct(x): return f'{100*x:.2f}%'
def table(h,rs): return '| '+' | '.join(h)+' |\n|'+'|'.join(['---']*len(h))+'|\n'+'\n'.join('| '+' | '.join(str(v).replace('|','/') for v in row)+' |' for row in rs)+'\n'
changes={
'AMP':'Price refresh; normalized EPS44 and13x terminal multiple retained. Reject repurchase/book-value double count in competing model.',
'PAYX':'Rechecked Q1FY27 cash-flow decline already incorporated in v005. Keep recurring integration allowance and cash-recovery trigger.',
'MSFT':'Correct v005 Sep25 close516.05 to516.17. No scenario or limit change.',
'HIG':'Sep25 post-close commutation: expected393m GAAP gain, no core EPS effect; exhausted reinsurance limit. Settlement/capital bridge required before entry.',
'AME':'Price refresh; post-Indicor financing bridge still required before purchase.',
'NTAP':'Adopt dated history201.15; Cboe201.145 precision difference retained. Sep25 PEAK:AIO acquisition intent: terms and earnings effect unquantified; no value added.'}
actions=[]
for s in M['stocks']:
    q=by[s['ticker']]; b=next(x for x in s['scenarios'] if x['name']=='base'); event=q['inherited_forecast'].get('next_earnings_date')
    actions.append(dict(ticker=s['ticker'],action=s['decision'],prior_action=prior[s['ticker']]['decision'],prior_limit=prior[s['ticker']]['limit_price'],revised_limit=s['limit_price'],close=s['reference_price'],price_date=s['reference_date'],changed_fact=changes.get(s['ticker'],'Refreshed close; unchanged archived normalized earnings and valuation assumptions after filing-index sweep.'),source=q['new_cboe_url'],financial_source='; '.join(str(x.get('url','')) for x in s['sources']),period=s['terminal_period'],thesis_impact=s['condition'],next_catalyst=f'{event or "Date unconfirmed"}: vendor earnings calendar only unless confirmed in filing audit; refresh issuer calendar before entry',allocation_effect=f'Up to {100*s["slot_weight"]:g}% funded slot' if s['slot_weight'] else '0% funded allocation; replacement requires explicit comparison',uncertainty='Scenario growth/multiples are judgments; live executable price, actual holdings and personal taxes unknown.',net_base_IRR_reference=b['irr_reference_after_30pct_withholding_25bp_costs']))
for q in A['rows']:
    if q['ticker'] in prior: continue
    reason={'RSG':'Do not adopt reverse DCF until cash-flow/discount-rate and total-versus-per-share growth definitions reconcile. Peer premium does not fix this.', 'LH':'Do not compare perpetual reverse growth directly with finite-horizon EPS growth. Need consistent duration and after-cost entry model.', 'PGR':'Hard-reject malformed FY1EPS1012 and derivedNTM747.864; dossier itself uses trailing underwriting instead.'}.get(q['ticker'],'Retain Claude dossier as candidate evidence; no matched after-tax/cost entry ceiling or funded replacement approved in this review.')
    actions.append(dict(ticker=q['ticker'],action='WAIT',prior_action='Claude v011 all-stock selection; no Codex funded slot',prior_limit=None,revised_limit=None,close=q['accepted_close'],price_date=q['market_session_date'],changed_fact='Friday close newly corroborated; Claude v011 candidate evidence reconciled.',source=q['new_cboe_url'],financial_source='v011 immutable dossier; deep fresh filing audit restricted to RSG/LH among new candidates',period='Inherited dossier fiscal periods; no new Codex terminal scenario adopted',thesis_impact=reason,next_catalyst=str(q['inherited_forecast'].get('next_earnings_date') or 'Unconfirmed')+' (inherited vendor calendar; not cleared for entry)',allocation_effect='0%; no addition beyond10% direct sleeve',uncertainty='Not rejected as a business. No claim that original14 outrank every new candidate.',net_base_IRR_reference=None))
for action in actions:
    if action['ticker']=='AMP': action['next_catalyst']='October29 results08:15ET /call09:00ET: search-indexed issuer release; direct source unavailable. Overall event clearance UNKNOWN.'
    if action['ticker']=='PAYX': action['next_catalyst']='Q1FY27 reportedSeptember23. Next earnings date not primary-confirmed; next-quarter/cumulative cash recovery is critical.'
    if action['ticker']=='HIG': action['next_catalyst']='Next Q3 filing and settlement/capital bridge; earnings calendar not independently cleared.'
    if action['ticker']=='NTAP': action['next_catalyst']='PEAK:AIO definitive terms/funding/closing update; earnings calendar unconfirmed.'
with (W/'ACTION_TABLE.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(actions[0]));w.writeheader();w.writerows(actions)
(W/'action_journal.json').write_text(json.dumps(actions,indent=2))
refresh={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parent':'v005_2026-09-26_codex','operating_scenarios_retained':42,'holding_horizon':'Three annual periods ending September2029; fiscal terminal conventions retained per stock','company_models':[{'ticker':s['ticker'],'reference_price':s['reference_price'],'reference_date':s['reference_date'],'baseline':s['baseline'],'terminal_period':s['terminal_period'],'scenarios':s['scenarios'],'change':changes.get(s['ticker'],'Price and reference IRRs refreshed; normalized operating cases unchanged.'),'limit':s['limit_price'],'condition':s['condition']} for s in M['stocks']]}
(W/'company_model_refresh.json').write_text(json.dumps(refresh,indent=2));(P/'company_model_refresh.json').write_text(json.dumps(refresh,indent=2))
text='''# Weekly investment decision review — 27 September 2026

Prepared by Codex for USD $50,000–$100,000. Status: completed conditional new-money research; no trades or holdings inferred. Prices are the completed US regular session of Friday 25 September. Public information was checked on Sunday 27 September; disclosures after Friday's close are separately identified. Holding periods remain thesis-dependent; valuation scenarios use a three-year horizon to September 2029.

## This week's decision

**Retain AMP at $500 or less and PAYX at $101.80 or less, each up to 2% of total capital.** Friday closes were $493.00 and $101.37. Both remain valuation-qualified; obtain a live executable quote, confirm the event/thesis checks and available capacity before buying. A Friday close is not a Monday order price. Do not add another 2% if an existing holding already fills that slot.

**No change to entry ceilings or allocation.** Initial planning remains 15% broad US index, up to4% AMP/PAYX and81% short Treasury exposure/cash. Maximum equity remains25%:15% index plus10% direct, with at least75% reserve. MSFT500, NVDA215, ALLE145 and HIG120 remain conditional funded levels. All four Friday closes exceed their limits. HIG also requires the settlement/capital reconciliation described below before entry. No weekly turnover is required.

These are my retained recommendations, not an endorsement of Claude's entire stock list. Claude's latest336-company research expands the candidate pool; its100% stock portfolio is a separate, much riskier proposal. The stated15–20% tolerable drawdown governs this review. Actual holdings, tax status and cash needs have not been provided, so there is no personalized HOLD/REDUCE/SELL list or realized performance claim.

## Action table: original fourteen

BUY means a modest new-money purchase is conditional on all gates, not a standing order. WAIT includes waiting for valuation, evidence or funded replacement capacity. Earlier labels BUY BELOW and AVOID CURRENT PRICE are consolidated to WAIT; this is a label change, not an upgrade. All prior and revised limits are identical this week. The detailed34-name CSV records prior action/limit, changed fact, source, fiscal period, thesis effect, catalyst, allocation effect and uncertainty.

'''
text+=table(['Stock','Action','Sep25 close','Prior → revised ceiling','Base IRR at close, net','Full direct slot'],[[s['ticker'],s['decision'],money(s['reference_price']),money(s['limit_price'])+' → same',pct(next(x for x in s['scenarios'] if x['name']=='base')['irr_reference_after_30pct_withholding_25bp_costs']),pct(s['slot_weight']) if s['slot_weight'] else 'Unfunded'] for s in M['stocks']])
text+='''
The IRRs above assume30% dividend withholding and25bp of purchase cost plus25bp of sale cost, excluding personal capital-gains tax, FX and fixed fees. They are conditional scenario calculations, not expected returns. The cash-flow model retains stock compensation and recurring expenses; it adds neither buyback yield nor a separate cash balance to EPS valuation.

[Full action journal](ACTION_TABLE.csv) · [Market reconciliation](market_audit.md) · [Filing audit](filing_audit.md) · [Transformation and risk audit](lineage_risk_audit.md).

## What changed, and what did not

**AMP — keep the $500 ceiling.** The normalized annual earning-power anchor stays$44 after removing the Comerica benefit; base growth remains7% for three years, terminal P/E13x, with dividends modeled separately. Claude's alternative justified-book-value model grows book using dividend-only retention while shrinking shares for buybacks without deducting their cost from book. That is a cash-use inconsistency, not merely a different investment opinion. A thin equity base and disparate financial peers further weaken a mechanical P/B comparison. We retain the segment/earnings approach; this does not prove7% growth or13x is correct. Lower markets, fee pressure, net outflows and regulated capital remain the main downside channels. No multiple or limit is raised to follow the share price. [AMP Q2 primary release](https://www.sec.gov/Archives/edgar/data/820027/000082002726000038/q22026er.htm).

**PAYX — keep $101.80, with a narrow valuation cushion.** The Q1FY2027 10-Q was accepted24 September at20:06:01UTC, just after that day's close. It was already incorporated in the26 September model, so this review corrects the availability label rather than claiming newly discovered cash weakness. Operating cash fell to$413.5m from$718.4m; conventional CFO less capex fell to$357.4m from$662.5m. The previous model already usesTTM CFO less capex$2,016.7m and a stricter owner-cash diagnostic$1,711.5m. Operating settlement movements must be distinguished from client-fund financing; the timing explanation is not proof of recovery. Keep the recurring integration charge and existing recovery/thesis triggers. Require demonstrated cash recovery before adding beyond the starter allocation; the owner-cash measure sits only$11.5m above the$1.7bn failure threshold. The model's after-withholding/25bp-each-side ceiling is only about$101.85; higher actual costs require a lower price, not relaxation of the hurdle. [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/723531/000072353126000006/payx-20260831.htm).

**HIG — WAIT, retain $120 as a conditional ceiling.** A25 September8-K accepted20:18:34UTC came18 minutes after the price cutoff. A commutation with National Indemnity brings$1.12bn cash and an expected$497m pretax/$393m net GAAP gain; the company excludes it from core earnings. The earlier10-Q shows the$1.5bn adverse-development cover limit was already fully ceded, with no remaining limit at31 December2025. It would be wrong to describe the settlement as surrendering$1.5bn of unused protection. It resolves disputed recoveries on exhausted cover. Do not add the gain to normalized EPS or treat all proceeds as surplus capital. Require the receivable/deferred-gain/equity/capital reconciliation before an entry; normalized catastrophe and reserve assumptions stay in the model. Exact8-K/10-Q links, locators and hashes are in the filing audit.

**MSFT — correct a small price error.** The corroborated25 September close is$516.17; the previous memo incorrectly called$516.05 reconciled. The$0.12 correction changes reference IRRs slightly and does not cross the$500 ceiling. **NTAP** uses the dated$201.15 history close; Cboe's$201.145 fractional-cent observation is retained, not silently averaged. NetApp also announced an intent to acquire PEAK:AIO on25 September; no purchase price or quantified earnings contribution was established. Preserve the$150 ceiling and require a financing/earnings bridge before entry. [Issuer announcement](https://investors.netapp.com/news/news-details/2026/NetApp-Announces-Intent-to-Acquire-PEAKAIO-to-Advance-Scalable-AI-Infrastructure-Architecture/default.aspx). No normalized EPS, terminal multiple or stock dividend path changes in any of the42 scenarios this week.

## Adjudicating Claude v011

Exact parents: **v005_2026-09-26_codex** and **v011_2026-09-27_claude**. This review updates the Codex decision pack and supplements/challenges Claude v011. It does not overwrite it or claim synchronization with an external Claude chat.

Adopt the expanded336 dossiers/214 eligible candidates as archived research coverage, the latest dated price evidence, explicit zero-alpha assumptions and reproducible risk arithmetic. Do not equate dossier counts, audit grades or a higher version number with an investment edge. The three agents are separate reviewers, not three independent economic sources.

Reject the following as bases for increasing risk or replacing funded names:

- The100% stock allocation does not fit this review's drawdown mandate. Its GFC replay loses about47.35%, excludes/renormalizes6.21% of original portfolio weight without GFC history, and applies today's selection to past crises. It is a stress replay, not a strategy track record. A separate15%index/10%Claude-sleeve/75%reserve historical replay loses12.70%; it assumes a constant4% reserve return and that sleeve is not our six-stock sleeve.
- Selection order matters: the number of names appearing in every tested ordering fell to6 in the latest wave. This is not evidence of a uniquely best20. Conditional simulation profit/outperformance percentages are not calibrated probabilities for your account.
- The quarterly-label detector's zero flags cover only a subset of financial rows. The lineage audit records13 checkable December-year-end holdings and7 others, versus12/8 in the release notes; only34 matched target-revenue rows among110 recognized labels. Skips and unmatched values cannot be counted as verified facts.
- PGR's inherited FY1EPS$1,012 and derivedNTM$747.864 are hard-invalid for valuation. Claude's dossier already discloses the problem and uses trailing underwriting metrics; agreement between vendors does not repair the erroneous field.
- RSG's reverse DCF needs consistent cash-flow, enterprise/equity and discount-rate definitions; comparing company-wide cash growth with EPS growth aided by repurchases is unsound. LH's perpetual reverse-growth result cannot be directly compared with a finite-horizon growth assumption. Its dossier also mislabels a six-month long-term debt increase as one quarter and overlooks the current-debt offset; total borrowings rose$273.8m, not$773m. Model the newly disclosed reimbursement-cut risk before a switch. Peer multiples alone do not repair these issues.

These limitations do not make RSG, LH or the other18 names bad businesses. They mean the published evidence does not establish a superior, cost-aware replacement for a funded slot this week. No fabricated entry ceilings or quota-driven additions are introduced. All20 receive a dated WAIT in the journal with zero new allocation; later evidence can change that decision.

'''
claude=[a for a in actions if a['ticker'] not in prior]
text+=table(['Additional candidates','Decision / funding','Further work before a switch'],[['RSG, LH','WAIT /0%','Repair valuation definitions, then compare after-cost downside and returns.'],['PGR','WAIT /0%','Discard malformed forward estimates; underwrite reserve and underwriting economics.'],[', '.join(x['ticker'] for x in claude if x['ticker'] not in ['RSG','LH','PGR']),'WAIT /0%','Reconcile an absolute entry valuation and funded replacement; retain archived research.']])
text+='''
## Sizing and portfolio risk

No leverage. Direct-name maximum2%; direct-sector maximum5%; known-issuer look-through planning cap3.5%. These are proposed model constraints. The initial eligible4% is not an instruction to infer prior purchases. If live prices fail, those budgets stay in reserve. For$50,000 the target stock budgets are$1,000 each; for$100,000,$2,000 each. Whole-share illustrations below use stock ceilings and issuer NAVs, not executable fund prices; fees come from residual cash.

'''
for p in M['portfolios']:
    text+='### '+money(p['capital'])+' illustration\n\n'+table(['Instrument','Illustrative units','Cost before fees','Capital weight'],[[r['ticker'],r['whole_shares'] if r['whole_shares'] is not None else 'Cash',money(r['cost']),pct(r['weight'])] for r in p['rows']])+'\n'
text+='''
For eligible non-US investors, the illustrated USD London lines remain VUAA (ISINIE00BFMXXD54) and IB01 (IE00BGSF1X88). Tax eligibility is unresolved; US-person status can make the Irish-fund illustration unsuitable. Economic exposure can instead use an eligible domestic index fund and short Treasury bills/cash. No broker access is needed for this research.

Issuer25 September NAVs areVUAA$149.7632 andIB01$121.89; both published fees are0.07% annually. IB01's4.16% yield-to-maturity and0.31-year duration remain dated24 September, not25 September. Yield is not locked for three years. The displayed£112.80 Vanguard market price is a different currency listing and is not theUSDVUAA quote. August31 holdings weights remainNVDA8.07902% andMSFT5.69335%; no claim is made that they are live. At full modeled targets those imply2.712% and2.854% total issuer exposure. Recheck current holdings before adding. [Vanguard issuer](https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-) · [iShares issuer](https://www.ishares.com/uk/individual/en/products/307243/ishares-treasury-bond-0-1yr-ucits-etf-fund).

'''
text+=table(['Simultaneous stress','Index /direct /reserve','Initial loss','Full25%equity loss','$100k full loss'],[[x['name'],f"{pct(x['core_shock'])} / {pct(x['direct_shock'])} / {pct(x['reserve_shock'])}",pct(x['initial_loss']),pct(x['full_loss']),money(x['dollars_100k'])] for x in M['stresses']])
text+='''
The severe full-allocation loss is14.25%; the constructed tail loss18.00%. Neither is a maximum-loss bound. An equity wipeout alone can lose25% at full deployment, and reserve or currency losses can worsen it. Weekly reviews can miss intraweek gaps. No stop or allocation can guarantee the15–20% tolerance.

'''
text+=table(['Three-year planning case','Index annual assumption','Reserve annual assumption','Initial wealth CAGR','All slots filled CAGR'],[[x['name'],pct(x['index_annual_assumption']),pct(x['reserve_annual_assumption']),pct(x['initial_wealth_cagr']),pct(x['full_wealth_cagr'])] for x in M['portfolio_scenarios']])
text+='''
The portfolio table retains the prior endpoint method: stock terminal proceeds plus 30%-withheld dividends held as cash; index and reserve compound. It excludes dealing costs, personal capital-gains tax andFX, unlike the stock IRR column above. Full deployment assumes every conditional slot fills immediately at its ceiling, which may never happen. The base4.26% initial/4.93% full figures are scenario outcomes, not promised returns. Compounding each stock's IRR is not the same calculation.

## Data coverage, validation and next review

The weekly price sweep newly corroborated34/34 stocks, with7 additional dated public history checks. The unchanged, immutable25 September universe contains503 USD price rows; archived raw Cboe payloads were reconciled to all503 rows, and both archived validation feeds were within0.5%. **469 universe prices were reused, not newly fetched.** The inherited forecast labels are366 ok,92 caution and45 unreliable; those are provider-quality tags, not permission to use them automatically. Annual time-weighted EPS approximations are not verified four-quarterNTM. No point-in-time consensus revision history is claimed.

The fresh filing sweep covers the original14 plus new RSG/LH. The other18 Claude-selected names receive fresh quote checks and archived research reuse, not a new comprehensive filing audit. New and material facts receive three bounded reviews: exact accounting/filing/availability; price/forecast identity and vintage; transformation and risk. Raw captures carry hashes. None of these checks validates future earnings or a stock-selection edge.

Finance-skills' financial-analyst workflow is applied for source reconciliation, scenario consistency and valuation sensitivity. The requested Druckenmiller synthesizer requires five fresh upstream reports; the requisite complete set is unavailable. No composite conviction score or allocation override is fabricated. This does not prevent conditional company-level decisions within the risk budget.

Before any buy: check the current ask and costs against the ceiling, the issuer event calendar (wait within five trading days of earnings unless gap risk is explicitly underwritten), thesis changes, actual funded capacity and fund overlap. The filing audit did not establish a confirmed earnings event in the next five sessions, but incomplete calendars are unknown, not cleared. PAYX reported23 September; its next primary date is unconfirmed. AMP29 October results/09:00 ET call are observed in search-indexed issuer syndication; direct source pages remain unavailable. This is not a complete event clearance. Confirm the applicable issuer calendar before execution. For HIG, do not count the post-close gain as recurring earning power. For AME, obtain the post-acquisition funding bridge. Each limit expires at a material event or the next weekly review, whichever comes first.

For actual holdings, HOLD depends on an intact thesis and switching costs, not whether price exceeds a buy ceiling. REDUCE/SELL review follows a thesis break, capital need or cap breach; also reassess a base forward return below8%. At a measured portfolio drawdown of8%, freeze additions for review; at12%, consider reducing weaker exposure toward15% total equity; at15%, prioritize reduction toward10% unless the mandate is explicitly revised. These are discretionary responses, not automated stops. Actual holdings and cash flows are needed to calculate account drawdown or performance.

Next scheduled weekly review: Sunday4 October2026,18:00 Dubai. This is weekly research, not daily monitoring. The action this week is **NO CHANGE to ceilings/weights**, with two retained conditional BUY candidates, refreshed prices, a corrected quote, stricter data exclusions and a new Hartford event gate.

## Package and audit trail

Current memo, model, scenario CSV, workbook and dashboard are updated together. All29 existing dashboard tabs remain; the first four carry the weekly decisions and the other25 preserve historical evidence. The previous delivered state is saved before modification, and the complete release ZIP preserves dated sources, audits and this journal. The original company underwriting remains archived; company_model_refresh.json records all42 refreshed calculations with unchanged operating assumptions.

The numerical verification recomputes1,422 model/workbook checks,1,262 cached workbook formulas and all14 purchase-ceiling cost gates. These are arithmetic checks, not investment guarantees. See consolidated_financials_audit.json and the separate final weekly check for the final file hashes and results.
'''
# Keep prose readable without changing URLs, filenames or version identifiers.
import re
parts=re.split(r'(\[[^\]]*\]\([^)]*\)|`[^`]*`)',text)
for idx,part in enumerate(parts):
    if idx%2: continue
    part=re.sub(r'(?<!\bv)(?<=[a-z])(?=\d)', ' ', part)
    part=re.sub(r'(?<=%)(?=[A-Za-z\d])', ' ', part)
    part=re.sub(r'(?<=[A-Za-z])(?=\$)', ' ', part)
    for ticker in ['MSFT','NVDA','ALLE','HIG','AMP','PAYX','NTAP']:
        part=re.sub(r'\b'+ticker+r'(?=\d)',ticker+' $',part)
    parts[idx]=part
text=''.join(parts)

(W/'WEEKLY_REVIEW.md').write_text(text,encoding='utf-8')
# Current convenience memo uses relative links back to the dated weekly audit.
current=text.replace('(ACTION_TABLE.csv)','(../weekly/2026-09-27/ACTION_TABLE.csv)')
for name in ['market_audit.md','filing_audit.md','lineage_risk_audit.md']:
    current=current.replace('('+name+')','(../weekly/2026-09-27/'+name+')')
(P/'INVESTMENT_DECISION_MEMO.md').write_text(current,encoding='utf-8')
print('Created34-row journal,42 refreshed company cases and current/dated weekly memo.')
