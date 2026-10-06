from pathlib import Path
import json, csv, math, hashlib
import xlsxwriter

P=Path(__file__).resolve().parent
WEEKLY=json.loads((P/'weekly_override.json').read_text(encoding='utf-8')) if (P/'weekly_override.json').exists() else {}
def read(name): return json.loads((P/name).read_text(encoding='utf-8-sig'))
def pv(terminal,divs,r,tax=0): return sum(d*(1-tax)/(1+r)**(i+1) for i,d in enumerate(divs))+terminal/(1+r)**3
def irr(price,terminal,divs,tax=0):
    lo,hi=-.999,10
    for _ in range(180):
        mid=(lo+hi)/2
        if pv(terminal,divs,mid,tax)>price: lo=mid
        else: hi=mid
    return (lo+hi)/2

DESCRIPTIONS={
'AMP':('Ameriprise Financial','Financials','Recurring advice fees and high operating leverage support compounding; the price leaves room for moderate growth. Normalize market-sensitive earnings rather than extrapolating record markets.','Equity markets, client cash yields and fund outflows can weaken together; regulated capital is not spare cash.','Two quarters of wealth net outflows, normalized annual earning power below $40, or an unexplained regulatory-capital deterioration: suspend additions and revalue.'),
'PAYX':('Paychex','Industrials','Payroll and compliance workflows are sticky. Modest growth, integration improvements and dividends can justify the entry without a return to historic premium valuations.','Paycor integration, borrowing and cash-conversion weakness can erode the apparent yield advantage.','Normalized FY2027 EPS below $5.50, persistent owner cash below $1.7bn without documented reversible timing, or debt-funded dividends: suspend additions and revalue.'),
'MSFT':('Microsoft','Information Technology','Azure, Microsoft 365 and enterprise distribution support durable earnings; remove investment gains and retain stock compensation.','Heavy AI spending, finance leases and competition can weaken cash returns despite strong accounting earnings.','Two quarters of weakening cloud growth with continued capital-intensity increases, or a material cut to operating-margin earning power: rebuild the valuation.'),
'NVDA':('NVIDIA','Information Technology','Accelerated computing demand and platform economics support growth, but the base case already requires a very large revenue expansion.','Customer concentration, export restrictions and extraordinary supply, cloud and investment commitments make the downside highly nonlinear.','Material customer financing stress, cancelled demand, sustained gross margin below 65%, or commitments rising while orders slow: suspend additions and rebuild bear/base cases.'),
'ALLE':('Allegion','Industrials','Installed security hardware and specification relationships support pricing and recurring replacement demand. A lower entry compensates for construction cyclicality.','Acquisitions, international disruption and construction weakness can impair margins and cash conversion.','Two quarters of negative Americas organic growth with over 200bp margin deterioration, or weak cash conversion without a documented bridge: cancel entry and revalue.'),
'HIG':('The Hartford','Financials','Core underwriting and disciplined insurance pricing can compound book value. Strip favorable prior-year reserve development and normalize partnership income.','Catastrophes, reserve deficiencies, social inflation and credit losses can arrive together.','Underlying accident-year underwriting deteriorates persistently, adverse development reverses the reserve thesis, or capital weakens: stop additions and review reduction.'),
'CPAY':('Corpay','Financials','Corporate payments can support high-single-digit earnings growth; explicitly charge stock compensation and recurring integration costs.','Leverage, regulatory expenses and recurring acquisition costs can consume cash. Client funds are not distributable corporate cash.','Two quarters of organic growth below 5%, leverage above 3.5x with weak debt repayment, or a material customer-funds/compliance failure: cancel entry and revalue.'),
'AIZ':('Assurant','Financials','Connected-living services and housing insurance have useful recurring economics; valuation must include a normal catastrophe allowance.','A benign catastrophe year and reserve releases can flatter run-rate earnings. Distribution concentration and claims inflation remain important.','Repeated catastrophe/claims experience above the normalized allowance or weakening program economics: increase the loss allowance and reduce the entry value.'),
'SNA':('Snap-on','Industrials','Professional tools, diagnostic information and franchise distribution are durable, but current pricing asks too much of a modest-growth business.','Financed purchases link tool demand and credit quality; a slowdown can hit both.','Financing past-due rates above 5%, rising provisions with declining tool sales, or two quarters of margin compression over 200bp: re-underwrite.'),
'NTAP':('NetApp','Information Technology','Storage growth can support earnings; use GAAP guidance so stock compensation stays charged.','Recent sales growth exceeds cash conversion; inventory turns and competition weaken the case for paying a premium.','Inventory turns remain below 8 while growth falls below 10%, cash conversion continues to weaken, or operating-margin guidance falls over 200bp: cancel entry.'),
'IBKR':('Interactive Brokers','Financials','Account growth and scalable brokerage economics remain attractive, but the quoted price demands strong growth and a rich terminal multiple.','Falling rates, trading activity, operational incidents and regulation can compress earnings and valuation simultaneously.','Account/client-asset growth slows materially while net interest income declines, or a material regulatory/operational capital event occurs: reset growth and multiple.'),
'ABNB':('Airbnb','Consumer Discretionary','An asset-light marketplace can compound, but stock compensation and ordinary taxes absorb much of headline cash-flow appeal.','Regulation, travel cyclicality, competition and dilution can prevent revenue growth from reaching owners.','Material deterioration in nights/bookings and take rate, sustained stock compensation dilution, or broad regulatory restrictions: lower normalized margins and valuation.'),
'AME':('AMETEK','Industrials','Specialized instrumentation and operating discipline are attractive, but the price and the large Indicor acquisition leave insufficient room for error.','A $5bn transaction changes financing and integration risk; June cash/debt cannot represent the post-close balance sheet.','Obtain the post-close debt, interest and integration bridge before any purchase; weak organic growth or acquisition returns below capital cost require a lower multiple.'),
'RL':('Ralph Lauren','Consumer Discretionary','Premiumization is working, but the current price capitalizes a strong margin and growth outcome.','Fashion cycles, leases, inventory and discretionary spending make recent growth an unsafe straight-line forecast.','Inventory growth exceeds sales by 10 points for two quarters with markdown pressure, or normalized margin falls below 14%: cancel entry and revalue.')}
ORDER=['AMP','PAYX','MSFT','NVDA','ALLE','HIG','CPAY','AIZ','SNA','NTAP','IBKR','ABNB','AME','RL']
LIMITS={'PAYX':101.80,'SNA':310,'RL':265}
SLOTS={'AMP':.02,'PAYX':.02,'MSFT':.02,'NVDA':.015,'ALLE':.015,'HIG':.01}
S=[]
def add(s,kind,root):
    t=s['ticker']; name,sector,thesis,bear,trigger=DESCRIPTIONS[t]
    ref=s.get('reference_price',s.get('price')); date=s.get('reference_date',s.get('price_date','2026-09-24'))
    # Use a later reconciled close when actually obtained, not an inconsistent header.
    if t=='MSFT': ref=516.05;date='2026-09-25'
    update=WEEKLY.get('stocks',{}).get(t,{})
    ref=update.get('reference_price',ref);date=update.get('reference_date',date)
    limit=LIMITS.get(t,s.get('limit_price',s.get('limit')))
    raw=s['scenarios']; raw=[dict(v,name=k) for k,v in raw.items()] if isinstance(raw,dict) else raw
    scenarios=[]
    for x in raw:
        pe=x.get('terminal_PE',x.get('terminal_pe',x.get('terminal_pe_assumption')))
        div=x.get('annual_dividends_per_share',x.get('dividends_by_holding_year',x.get('year_1_2_3_dividends')))
        tp=x['terminal_eps']*pe
        assert abs(tp-x['terminal_price'])<1e-6
        scenarios.append(dict(name=x['name'],terminal_eps=x['terminal_eps'],terminal_pe=pe,terminal_price=tp,dividends=div,
          irr_reference=irr(ref,tp,div),irr_limit=irr(limit,tp,div),irr_reference_withholding30=irr(ref,tp,div,.30),irr_limit_withholding30=irr(limit,tp,div,.30),
          pv_hurdle=pv(tp,div,s['hurdle']),pv_hurdle_withholding30=pv(tp,div,s['hurdle'],.30),total_return_reference=(tp+sum(div))/ref-1,total_return_limit=(tp+sum(div))/limit-1))
    base=next(x for x in scenarios if x['name']=='base')
    decision='BUY NOW' if t in ['AMP','PAYX'] else ('AVOID CURRENT PRICE' if t in ['ABNB','AME','RL'] else 'BUY BELOW')
    decision=update.get('decision',decision)
    sources=s.get('sources',[])
    if kind=='financials':sources=[v for k,v in root['source_urls'].items() if k.startswith(t+'_')]
    if kind=='technology': sources={k:v for k,v in root['sources'].items() if k.startswith(t.lower()+'_')}
    if isinstance(sources,dict): sources=[dict(id=k,**v) if isinstance(v,dict) else dict(id=k,url=v) for k,v in sources.items()]
    sources=[dict(url=v) if isinstance(v,str) else v for v in sources]
    horizon=s.get('terminal_earnings_period',s.get('terminal_period','FY2029-equivalent annual earning power; three growth steps from normalized FY2026'))
    horizon={'NVDA':'FY2030 ending January 2030; four months forward at September 2029 exit','MSFT':'FY2029 ending June 2029; completed fiscal year at September 2029 exit','PAYX':'FY2029 ending May 2029; completed fiscal year at September 2029 exit','ALLE':'FY2029 ending December 2029; three months forward at September 2029 exit','SNA':'FY2029 ending around December 2029; approximately three months forward at September 2029 exit','RL':'FY2029 ending around March 2029; completed fiscal year at September 2029 exit','CPAY':'FY2029 ending December 2029; three months forward at September 2029 exit','AME':'FY2029 ending December 2029; three months forward at September 2029 exit','NTAP':'FY2030 ending April 2030; seven months forward at September 2029 exit','ABNB':'FY2029 ending December 2029; three months forward at September 2029 exit'}.get(t,horizon)
    baseline=s.get('baseline_definition',s.get('definition',s.get('earnings_baseline',root.get('normalization_bridges',{}).get(t,{}))))
    S.append(dict(ticker=t,name=name,sector=sector,rank=ORDER.index(t)+1,decision=decision,reference_price=ref,reference_date=date,
        limit_price=limit,hurdle=s['hurdle'],slot_weight=SLOTS.get(t,0),initial_weight=SLOTS.get(t,0) if decision in ['BUY NOW','BUY'] else 0,
        thesis=thesis,countercase=bear,failure_rule=trigger,baseline=baseline,terminal_period=horizon,sources=sources,scenarios=scenarios,
        base_ceiling=base['pv_hurdle'],base_ceiling_withholding30=base['pv_hurdle_withholding30'],detail_file=kind+'.md',
        condition='Price alone is insufficient: recheck thesis, event risk and portfolio capacity. '+('Post-close financing bridge is also required.' if t=='AME' else ''),
        slot_note='Funded slot in the model portfolio' if t in SLOTS else 'Reserve candidate only; replacement requires an explicit switch within the 10% direct-stock cap'))

for kind,file,key in [('technology','technology.json','stocks'),('quality_compounders','quality_compounders.json','companies'),('industrials_payments','industrials_payments.json','stocks'),('financials','financials.json','stocks')]:
    d=read(file);ss=d[key]
    if isinstance(ss,dict):ss=[dict(v,ticker=k) for k,v in ss.items()]
    for s in ss:add(s,kind,d)
add(read('airbnb.json'),'airbnb',read('airbnb.json'))
for stock in S:
    update=WEEKLY.get('stocks',{}).get(stock['ticker'],{})
    if update.get('condition'): stock['condition']=update['condition']
    stock['price_source']=update.get('price_source')
    stock['price_conflict']=update.get('price_conflict')
    for case in stock['scenarios']:
        case['irr_reference_after_30pct_withholding_25bp_costs']=irr(stock['reference_price']*1.0025,case['terminal_price']*.9975,case['dividends'],.30)
        case['irr_limit_after_30pct_withholding_25bp_costs']=irr(stock['limit_price']*1.0025,case['terminal_price']*.9975,case['dividends'],.30)
        case['pv_hurdle_after_30pct_withholding_25bp_costs']=pv(case['terminal_price']*.9975,case['dividends'],stock['hurdle'],.30)/1.0025
    stock['base_ceiling_after_costs']=next(c['pv_hurdle_after_30pct_withholding_25bp_costs'] for c in stock['scenarios'] if c['name']=='base')
S.sort(key=lambda x:x['rank']); assert len(S)==14 and len(set(x['ticker'] for x in S))==14
for s in S:
    assert s['limit_price']<=s['base_ceiling_withholding30']+1e-6,(s['ticker'],s['limit_price'],s['base_ceiling_withholding30'])
assert abs(sum(SLOTS.values())-.10)<1e-9

funds=[dict(ticker='VUAA',name='Vanguard S&P 500 UCITS ETF USD Accumulating',isin='IE00BFMXXD54',exchange='London Stock Exchange, USD trading line',domicile='Ireland',nav=149.0017,nav_date='2026-09-24',fee=.0007,weight=.15,source='https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-',note='NAV is a sizing illustration, not an executable quote. Do not use the VUAG GBP market price. Equity risk remains.'),
dict(ticker='IB01',name='iShares $ Treasury Bond 0-1yr UCITS ETF USD Accumulating',isin='IE00BGSF1X88',exchange='London Stock Exchange, USD trading line',domicile='Ireland',nav=121.86,nav_date='2026-09-24',fee=.0007,weight=.75,ytm=.0416,duration=.31,source='https://www.ishares.com/uk/individual/en/products/307243/ishares-treasury-bond-0-1yr-ucits-etf-fund',note='Short-duration Treasury fund, not guaranteed cash. Yield to maturity is not a locked three-year return. Reserve can instead be eligible short Treasury bills held to maturity or insured cash, after checking access and terms.')]

for fund in funds:
    fund.update(WEEKLY.get('funds',{}).get(fund['ticker'],{}))

portfolios=[]
for capital in [50000,100000]:
    rows=[]
    for ticker,w,price,basis in [('VUAA',.15,funds[0]['nav'],'NAV illustration'),('AMP',.02,500,'maximum stock purchase limit'),('PAYX',.02,101.80,'maximum stock purchase limit'),('IB01',.80,funds[1]['nav'],'NAV illustration')]:
        qty=math.floor(capital*w/price);cost=qty*price
        rows.append(dict(ticker=ticker,budget=capital*w,illustrative_price=price,price_basis=basis,whole_shares=qty,cost=cost,weight=cost/capital))
    residual=capital-sum(r['cost'] for r in rows)
    rows.append(dict(ticker='USD cash',budget=capital*.01,illustrative_price=1,price_basis='cash after share rounding, before fees',whole_shares=None,cost=residual,weight=residual/capital))
    portfolios.append(dict(capital=capital,rows=rows,equity_weight=sum(r['weight'] for r in rows if r['ticker'] in ['VUAA','AMP','PAYX']),reserve_weight=sum(r['weight'] for r in rows if r['ticker'] in ['IB01','USD cash']),total=sum(r['cost'] for r in rows)))
stress=[]
for label,c,d,r in [('Equity selloff',-.30,-.40,0),('Severe correlated shock',-.50,-.60,-.01),('Tail shock',-.60,-.75,-.02)]:
    stress.append(dict(name=label,core_shock=c,direct_shock=d,reserve_shock=r,initial_loss=.15*c+.04*d+.81*r,full_loss=.15*c+.10*d+.75*r,dollars_50k=(.15*c+.10*d+.75*r)*50000,dollars_100k=(.15*c+.10*d+.75*r)*100000))

# No-reinvestment terminal-wealth comparison: different from cash-flow IRR.
portfolio_scenarios=[]
for scenario,index_r,reserve_r in [('bear',-.08,.025),('base',.06,.035),('bull',.12,.045)]:
    row=dict(name=scenario,index_annual_assumption=index_r,reserve_annual_assumption=reserve_r)
    for state in ['initial','full']:
        weights={x['ticker']:x['initial_weight'] if state=='initial' else x['slot_weight'] for x in S}
        reserve_w=1-.15-sum(weights.values())
        terminal=.15*(1+index_r)**3+reserve_w*(1+reserve_r)**3
        for s in S:
            x=next(z for z in s['scenarios'] if z['name']==scenario)
            # All slots filled immediately at limits is a hypothetical, not a timing forecast.
            entry=s['limit_price']
            terminal+=weights[s['ticker']]*(x['terminal_price']+sum(x['dividends'])*.70)/entry
        row[state+'_terminal_wealth_multiple']=terminal;row[state+'_wealth_cagr']=terminal**(1/3)-1
    portfolio_scenarios.append(row)

model=dict(prepared='2026-09-26 Dubai',decision_cutoff='Late September 2026; individual price dates shown',holding_years=3,exit='September 2029',stocks=S,funds=funds,portfolios=portfolios,stresses=stress,portfolio_scenarios=portfolio_scenarios,
    core_weight=.15,direct_initial=.04,direct_cap=.10,reserve_initial=.81,reserve_min_full=.75,
    overlap=dict(date='2026-08-31 issuer holdings',NVDA_index_weight=.0807902,MSFT_index_weight=.0569335,NVDA_total_full=.15*.0807902+.015,MSFT_total_full=.15*.0569335+.02),
    limitations=['Analyst scenarios, not calibrated forecasts or probabilities.','The new portfolio has no validated historical track record.','Bear terminal values are not maximum drawdowns.','Tax residency, US-person status, holdings, access, commissions and liabilities are unknown. Model is new-money USD capital with no leverage.','Conditional stock slots are not simultaneous instructions; cash stays in reserve until limits and thesis tests both pass.','ETF expense ratios are fund expenses; scenarios are after assumed fund expenses, before personal tax and trading costs.'])
model.update({k:WEEKLY[k] for k in ['prepared','decision_cutoff','parents','weekly_report','coverage'] if k in WEEKLY})
(P/'decision_model.json').write_text(json.dumps(model,indent=2,ensure_ascii=False),encoding='utf-8')
with (P/'decision_table.csv').open('w',newline='',encoding='utf-8-sig') as f:
    fields=['rank','ticker','decision','reference_price','reference_date','limit_price','hurdle','base_ceiling','base_ceiling_withholding30','slot_weight','initial_weight','terminal_period']
    wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader();wr.writerows({k:s[k] for k in fields} for s in S)
with (P/'scenarios.csv').open('w',newline='',encoding='utf-8-sig') as f:
    rows=[dict(ticker=s['ticker'],**{k:v for k,v in x.items() if k!='dividends'},dividend_y1=x['dividends'][0],dividend_y2=x['dividends'][1],dividend_y3=x['dividends'][2]) for s in S for x in s['scenarios']]
    wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)

# Excel workbook with editable inputs, formulas and cached numerical results.
wb=xlsxwriter.Workbook(P/'Investment_Decision_Model.xlsx')
head=wb.add_format({'bold':True,'bg_color':'#17344D','font_color':'white','text_wrap':True});money=wb.add_format({'num_format':'$0.00'});pct=wb.add_format({'num_format':'0.00%'});wrap=wb.add_format({'text_wrap':True,'valign':'top'})
ws=wb.add_worksheet('Read me');ws.set_column('A:A',30);ws.set_column('B:B',115)
notes=[('Purpose','Prospective investment decisions, dated 27 September 2026 Dubai. Use live quotes and verify thesis before placing any order.'),('Model','Three annual dividend cashflows; year-three terminal EPS times analyst P/E. IRR differs from terminal-wealth CAGR. All future values are analyst assumptions.'),('Editable scenario inputs','Scenario sheet columns C:K are inputs. Formulas recompute terminal value, IRR and maximum entry. Tax rate starts at 30% dividend withholding as a sensitivity, not a tax-status determination.'),('Authoritative limits','Decision sheet contains the committee limits. Changing a scenario does not automatically change the published recommendation or portfolio budgets.'),('Risk','No loss guarantee, return probability, strategy backtest or trade authorization. Full allocation 25% equity /75% reserve; initial 19% equity /81% reserve before rounding.'),('Funds','VUAA/IB01 USD London trading lines for an eligible non-US investor. Confirm personal tax eligibility; Irish funds can be unsuitable for US persons. NAVs are sizing illustrations, not quotes.'),('Source archive','See companion decision_model.json, company memoranda, original three deep audits and hashed source captures. Source dates and periods differ and are explicit.'),('Costs','Personal capital-gains tax, commissions and FX excluded. Stress 25bp entry plus 25bp exit on direct stocks; 10bp per side on funds. At full target this is about 0.23% of capital once, before fixed fees and turnover.')]
for i,(a,b) in enumerate(notes):ws.write(i,0,a,head);ws.write(i,1,b,wrap);ws.set_row(i,48)
ws=wb.add_worksheet('Decisions');fields=['Rank','Ticker','Action','Reference price','Price date','Buy/reconsider limit','Hurdle','Base PV gross','Base PV 30% withholding','Initial weight','Full slot','Terminal earnings period'];ws.write_row(0,0,fields,head);ws.freeze_panes(1,2);ws.autofilter(0,0,14,len(fields)-1);ws.set_column('A:C',20);ws.set_column('D:K',20);ws.set_column('L:L',85)
for i,s in enumerate(S,1):ws.write_row(i,0,[s['rank'],s['ticker'],s['decision'],s['reference_price'],s['reference_date'],s['limit_price'],s['hurdle'],s['base_ceiling'],s['base_ceiling_withholding30'],s['initial_weight'],s['slot_weight'],s['terminal_period']]);[ws.write_number(i,j,v,pct) for j,v in [(6,s['hurdle']),(9,s['initial_weight']),(10,s['slot_weight'])]]
ws=wb.add_worksheet('Scenarios');headers=['Ticker','Case','Reference','Limit','Hurdle','Dividend tax','Terminal EPS','Terminal PE','Dividend Y1','Dividend Y2','Dividend Y3','Terminal price','IRR reference gross','IRR limit gross','IRR limit after withholding','PV gross','PV after withholding'];ws.write_row(0,0,headers,head);ws.freeze_panes(1,2);ws.set_column('A:Q',19);ws.autofilter(0,0,42,16)
r=1
for s in S:
 for x in s['scenarios']:
    n=r+1;ws.write_row(r,0,[s['ticker'],x['name'],s['reference_price'],s['limit_price'],s['hurdle'],.30,x['terminal_eps'],x['terminal_pe'],*x['dividends']])
    ws.write_formula(r,11,f'=G{n}*H{n}',money,x['terminal_price'])
    # RATE equivalent is invalid with varying dividends; use IRR on explicit hidden cashflows.
    for offset,entry,tax in [(18,s['reference_price'],0),(22,s['limit_price'],0),(26,s['limit_price'],.30)]:
        ws.write_formula(r,offset,f'=-{"C" if offset==18 else "D"}{n}',None,-entry)
        for j,d in enumerate(x['dividends']):
            col=['I','J','K'][j];form=f'={col}{n}'+(f'*(1-F{n})' if tax else '')+(f'+L{n}' if j==2 else '')
            ws.write_formula(r,offset+j+1,form,None,d*(1-tax)+(x['terminal_price'] if j==2 else 0))
    for col,form,value,fmt in [(12,f'=IRR(S{n}:V{n})',x['irr_reference'],pct),(13,f'=IRR(W{n}:Z{n})',x['irr_limit'],pct),(14,f'=IRR(AA{n}:AD{n})',x['irr_limit_withholding30'],pct),(15,f'=I{n}/(1+E{n})+J{n}/(1+E{n})^2+(K{n}+L{n})/(1+E{n})^3',x['pv_hurdle'],money),(16,f'=I{n}*(1-F{n})/(1+E{n})+J{n}*(1-F{n})/(1+E{n})^2+(K{n}*(1-F{n})+L{n})/(1+E{n})^3',x['pv_hurdle_withholding30'],money)]:ws.write_formula(r,col,form,fmt,value)
    r+=1
ws.set_column('S:AD',None,None,{'hidden':True})
for portfolio in portfolios:
 ws=wb.add_worksheet(str(portfolio['capital'])+' initial');ws.write_row(0,0,['Instrument','Budget','Sizing price','Price basis','Whole shares','Illustrative cost','Capital weight'],head);ws.set_column('A:G',23);ws.set_column('D:D',48)
 for i,row in enumerate(portfolio['rows'],1):ws.write_row(i,0,[row[k] for k in ['ticker','budget','illustrative_price','price_basis','whole_shares','cost','weight']])
 ws.write(8,0,'Total');ws.write_formula(8,5,'=SUM(F2:F6)',money,portfolio['capital']);ws.write(10,0,'Refresh prices and recompute shares before execution. Reserve includes unfilled conditional slots. Fees come from residual cash.')
ws=wb.add_worksheet('Stress');ws.set_column('A:A',35);ws.set_column('B:H',22);ws.write_row(0,0,['Scenario','Index shock','Direct shock','Reserve shock','Initial portfolio','Full portfolio','Full loss $50k','Full loss $100k'],head)
for i,x in enumerate(stress,1):ws.write_row(i,0,list(x.values()))
ws=wb.add_worksheet('Sources');ws.set_column('A:A',15);ws.set_column('B:B',125);ws.write_row(0,0,['Ticker','Primary documents / price source'],head);r=1
for s in S:
 for src in s['sources']:
    u=src.get('url',src.get('source_url',''))
    if isinstance(u,str) and u.startswith('http'):ws.write(r,0,s['ticker']);ws.write_url(r,1,u);r+=1
for f in funds:ws.write(r,0,f['ticker']);ws.write_url(r,1,f['source']);r+=1
ws=wb.add_worksheet('Weekly audit');ws.set_column('A:A',30);ws.set_column('B:B',115);ws.write_row(0,0,['Field','Weekly evidence / scope'],head)
for row,(key,value) in enumerate([('Prepared',model['prepared']),('Cutoff',model['decision_cutoff']),('Parents','; '.join(WEEKLY.get('parents',[]))),('Coverage',json.dumps(WEEKLY.get('coverage',{}))),('Actions','BUY AMP <=500 and PAYX <=101.80, up to2% each, only if live price/thesis/capacity pass; WAIT on other names. No actual holdings supplied.'),('HIG event',WEEKLY.get('stocks',{}).get('HIG',{}).get('condition','')),('Valuation facts','42 operating scenarios retained; 34 prices freshly corroborated. 469 other universe prices reused from dated immutable archive.'),('Limit cost gate','Ceilings tested with30% dividend withholding plus25bp entry and25bp exit. Personal capital-gains tax and fixed dealing fees are unknown.'),('Report',WEEKLY.get('weekly_report',''))],1):
 ws.write(row,0,key,head);ws.write(row,1,value,wrap);ws.set_row(row,60)
ws=wb.add_worksheet('After costs');ws.set_column('A:G',24);ws.write_row(0,0,['Ticker','Case','IRR reference net','IRR limit net','PV at hurdle net','Published limit','Cost assumptions'],head)
r=1
for stock in S:
 for case in stock['scenarios']:
  n=r+1
  ws.write_row(r,0,[stock['ticker'],case['name']])
  ws.write_formula(r,5,f'=Scenarios!D{n}',money,stock['limit_price'])
  ws.write(r,6,'Scenarios tax input;25bp entry/exit')
  for offset,entrycol,entry in [(7,'C',stock['reference_price']),(11,'D',stock['limit_price'])]:
   ws.write_formula(r,offset,f'=-Scenarios!{entrycol}{n}*1.0025',money,-entry*1.0025)
   for i,div in enumerate(case['dividends']):
    col=['I','J','K'][i]; form=f'=Scenarios!{col}{n}*(1-Scenarios!F{n})'+(f'+Scenarios!L{n}*0.9975' if i==2 else '')
    ws.write_formula(r,offset+i+1,form,money,div*.7+(case['terminal_price']*.9975 if i==2 else 0))
  ws.write_formula(r,2,f'=IRR(H{n}:K{n})',pct,case['irr_reference_after_30pct_withholding_25bp_costs'])
  ws.write_formula(r,3,f'=IRR(L{n}:O{n})',pct,case['irr_limit_after_30pct_withholding_25bp_costs'])
  ws.write_formula(r,4,f'=(Scenarios!I{n}*(1-Scenarios!F{n})/(1+Scenarios!E{n})+Scenarios!J{n}*(1-Scenarios!F{n})/(1+Scenarios!E{n})^2+(Scenarios!K{n}*(1-Scenarios!F{n})+Scenarios!L{n}*0.9975)/(1+Scenarios!E{n})^3)/1.0025',money,case['pv_hurdle_after_30pct_withholding_25bp_costs'])
  r+=1
ws.set_column('H:O',None,None,{'hidden':True})
wb.close()
print(json.dumps({'stocks':len(S),'scenarios':sum(len(s['scenarios']) for s in S),'portfolio_totals':[p['total'] for p in portfolios],'limits_below_afterwithholding_pv':True,'base_portfolio_wealth_cagr':portfolio_scenarios[1]},indent=2))

