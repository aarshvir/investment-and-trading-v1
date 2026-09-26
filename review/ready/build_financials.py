import json, math
from pathlib import Path

OUT=Path(__file__).parent
S={
'AMP_release':'https://www.sec.gov/Archives/edgar/data/820027/000082002726000038/q22026er.htm',
'AMP_q1':'https://www.sec.gov/Archives/edgar/data/820027/000082002726000020/q12026er.htm',
'AMP_10q':'https://www.sec.gov/Archives/edgar/data/820027/000082002726000043/amp-20260630.htm',
'AMP_dividend':'https://ir.ameriprise.com/news/news-details/2026/Ameriprise-Financial-Declares-Regular-Quarterly-Dividend-81877f055/default.aspx',
'HIG_release':'https://ir.thehartford.com/news/news-details/2026/The-Hartford-Reports-Strong-Second-Quarter-2026-Financial-Results/',
'HIG_q1':'https://ir.thehartford.com/news/news-details/2026/The-Hartford-Reports-First-Quarter-2026-Financial-Results/default.aspx',
'HIG_10q':'https://www.sec.gov/Archives/edgar/data/874766/000087476626000060/hig-20260630.htm',
'HIG_dividend':'https://newsroom.thehartford.com/newsroom-home/news-releases/news-release-details/2026/The-Hartford-Declares-Quarterly-Dividends-Of-0-60-Per-Share-Of-Common-Stock-And-375-Per-Share-Of-Series-G-Preferred-Stock-87687251d/default.aspx',
'AIZ_release':'https://s21.q4cdn.com/997934001/files/doc_financials/2026/q2/AIZ-2026-06-30-Ex-99-1-Press-Release_FINAL.pdf',
'AIZ_10q':'https://www.sec.gov/Archives/edgar/data/1267238/000126723826000041/aiz-20260630.htm',
'AIZ_dividend':'https://www.assurant.com/news-insights/news_releases/quarterly-dividend-3Q26',
'IBKR_release':'https://www.sec.gov/Archives/edgar/data/1381197/000138119726000118/ibkr-ex99_1.htm',
'IBKR_10q':'https://www.sec.gov/Archives/edgar/data/1381197/000138119726000147/ibkr-20260630.htm',
'IBKR_august':'https://www.interactivebrokers.com/mkt/getFileNew.php?file=202608MetricsPressRelease.pdf',
'IBKR_rate_transcript':'https://www.fool.com/earnings/call-transcripts/2026/07/21/interactive-brokers-ibkr-q2-2026-earnings-call-transcript/?referring_guid=89ef2ba2-b035-4492-be80-675868705e31&source=financialcontent'
}
def pv(divs,terminal,r):return sum(d/(1+r)**(i+1) for i,d in enumerate(divs))+terminal/(1+r)**3
def irr(p,divs,terminal):
 lo,hi=-.95,3
 for _ in range(160):
  m=(lo+hi)/2
  if pv(divs,terminal,m)>p:lo=m
  else:hi=m
 return (lo+hi)/2

# All forward inputs below are analyst assumptions, not consensus or management guidance.
config={
'AMP':dict(price=485.15,eps=44.,div=6.8,hurdle=.12,limit=500.,rating='BUY NOW at or below $500',
 cases={'bear':(-.05,9.5,0),'base':(.07,13,.05),'bull':(.12,15,.08)}),
'HIG':dict(price=125.69,eps=12.,div=2.4,hurdle=.115,limit=120.,rating='BUY BELOW $120',
 cases={'bear':(-.04,9,0),'base':(.06,11.5,.05),'bull':(.10,13,.08)}),
'AIZ':dict(price=261.86,eps=21.,div=3.52,hurdle=.12,limit=235.,rating='BUY BELOW $235',
 cases={'bear':(-.07,10,0),'base':(.07,13,.06),'bull':(.11,16,.08)}),
'IBKR':dict(price=89.82,eps=2.6,div=.35,hurdle=.13,limit=65.,rating='BUY BELOW $65; avoid initiating near $90',
 cases={'bear':(0,18,0),'base':(.15,25,.10),'bull':(.23,32,.15)})}
data={'as_of_information_cutoff':'2026-09-25 US close','price_reference_date':'2026-09-24','model_horizon_years':3,
'horizon_definition':'Purchase at reference price in late September 2026; dividends at annual periods ending September 2027, 2028, 2029; terminal EPS is normalized FY2026-equivalent annual earning power grown exactly three times to FY2029-equivalent current-year earning power. Not NTM; no FY2030 extra growth year.',
'method':'Three explicit annual dividends plus year-3 EPS times terminal P/E. Solve cash-flow IRR and discount at stated analyst hurdle. No probability weights, buyback yield, separate excess cash, leverage or trading gains.',
'tax_sensitivity':'30% withholding applies only to dividends as a sensitivity, not a determination of user tax status; capital-gains tax, commissions and FX excluded.',
'source_urls':S,'stocks':{}}
for ticker,c in config.items():
 d={k:v for k,v in c.items() if k!='cases'}
 d['price_source']='https://stockanalysis.com/stocks/'+ticker.lower()+'/history/'
 d['normalized_baseline_period']='FY2026-equivalent annual earning power based on latest disclosed June 2026 actuals; analyst normalization, not reported full-year EPS'
 d['scenarios']={}
 for case,(g,pe,dg) in c['cases'].items():
  eps=[c['eps']*(1+g)**n for n in (1,2,3)];divs=[c['div']*(1+dg)**n for n in (0,1,2)];terminal=eps[2]*pe
  d['scenarios'][case]={'eps_growth_assumption':g,'terminal_pe_assumption':pe,'dividend_growth_assumption':dg,'year_1_2_3_eps':eps,'year_1_2_3_dividends':divs,'terminal_eps':eps[2],'terminal_price':terminal,'annual_cashflow_irr_pretax':irr(c['price'],divs,terminal),'annual_cashflow_irr_30pct_dividend_withholding':irr(c['price'],[x*.7 for x in divs],terminal),'cumulative_total_return_no_reinvestment':(terminal+sum(divs))/c['price']-1,'present_value_at_hurdle':pv(divs,terminal,c['hurdle']),'present_value_at_hurdle_30pct_dividend_withholding':pv([x*.7 for x in divs],terminal,c['hurdle'])}
 b=d['scenarios']['base'];d['maximum_entry_pretax']=b['present_value_at_hurdle'];d['maximum_entry_30pct_dividend_withholding']=b['present_value_at_hurdle_30pct_dividend_withholding']
 d['base_irr_at_recommended_limit_pretax']=irr(c['limit'],b['year_1_2_3_dividends'],b['terminal_price'])
 d['base_pv_sensitivity']={str(r):pv(b['year_1_2_3_dividends'],b['terminal_price'],r) for r in (.10,.12,.14)}
 div_pv=sum(v/(1+c['hurdle'])**(i+1) for i,v in enumerate(b['year_1_2_3_dividends']))
 d['implied_growth_to_earn_hurdle_at_reference_price'] = ((c['price']-div_pv)*(1+c['hurdle'])**3/(c['eps']*b['terminal_pe_assumption']))**(1/3)-1
 data['stocks'][ticker]=d

data['normalization_bridges']={
'AMP':{'reported_H1_adjusted_eps':22.33,'H1_diluted_shares_m':93.7,'Q1_nonrecurring_pretax_earnings_benefit_m':25,'assumed_tax':.21,'annualized_normalized_eps_calculated':22.33*2-25*.79/93.7*2,'selected_eps':44,'notes':'Q1 adjusted earnings benefit is $25m, distinct from $28m gross revenue in 10-Q. Rounded down. No separate capital addition.'},
'HIG':{'reported_Q2_core_eps':3.42,'reported_Q2_core_earnings_m':945,'implied_diluted_shares_m':945/3.42,'Q2_favorable_PYD_m':111,'Q2_LP_income_m':114,'reported_LP_annualized_yield':.076,'assumed_normal_LP_yield':.05,'assumed_tax':.21,'annualized_normalized_eps_calculated':3.42*4-4*(111+114*(1-.05/.076))*.79/(945/3.42),'selected_eps':12,'notes':'Remove all favorable Q2 PYD and LP yield above 5%; retain actual Q2 CAT charge. Do not add Q1 core EPS without removing discontinued Hartford Funds. Annualizing a quarter is a starting point, not annual guidance.'},
'AIZ':{'FY2025_adjusted_exCAT_eps':22.81,'FY2026_management_direction':'mid-single-digit growth in adjusted EPS excluding reportable catastrophes','analyst_midpoint_growth':.05,'FY2026_included_favorable_PYD_m':41.9,'Q2_non_run_rate_benefit_m':10,'assumed_full_year_normal_CAT_m':150,'assumed_tax':.20,'assumed_diluted_shares_m':50.2,'annualized_normalized_eps_calculated':22.81*1.05-(41.9+10+150)*.8/50.2,'selected_eps':21,'notes':'Guidance-based annual anchor, not H1 annualization. Normal CAT charge $150m and share denominator are analyst assumptions. Rounded $20.73 to $21; sensitivity supplied.'},
'IBKR':{'reported_Q2_adjusted_eps':.69,'reported_Q2_effective_tax':.147,'assumed_normal_tax':.19,'annualized_normalized_eps_calculated':.69*4*.81/.853,'selected_eps':2.6,'notes':'Normalize Q2 tax windfall. All EPS and dividends on post-June2025 4-for-1 split basis. EPS already accounts for noncontrolling interest; do not divide consolidated group earnings or customer equity by Class A shares.'}}
data['crosschecks']={
'AMP_sotp':{'description':'Illustrative Q2 run-rate segment valuation, discounted 10% for elevated markets; all multiples analyst assumptions; no capital added.', 'pretax_segment_earnings_m':{'wealth':939,'asset_management':274,'retirement_protection':202,'corporate_closed_blocks':-81},'tax':.21,'shares_m':92.9,'segment_multiples':{'wealth':14,'asset_management':10,'retirement_protection':8,'corporate_closed_blocks':10},'runrate_value':(939*14+274*10+202*8-81*10)*4*.79/92.9,'after_10pct_normalization':(939*14+274*10+202*8-81*10)*4*.79/92.9*.9},
'HIG_residual_income':{'exAOCI_book_value':78.91,'sustainable_ROE_assumption':.16,'cost_of_equity_assumption':.11,'long_run_growth_assumption':.04,'justified_price_to_book':(.16-.04)/(.11-.04),'value':78.91*(.16-.04)/(.11-.04),'limitation':'Steady-state excess-return approximation, not full multi-stage statutory capital model; AOCI excluded, credit losses not excluded.'},
'AIZ_cat_eps_sensitivity':{str(cat):22.81*1.05-(41.9+10+cat)*.8/50.2 for cat in (75,150,250,350)},
'IBKR_minus100bps_linear_sensitivity':{'US_25bps_annual_NII_m':81,'nonUS_25bps_annual_NII_m':38,'linear_annual_pretax_loss_m':476,'annualized_Q2_adjusted_pretax_m':5760,'approx_eps_loss':2.6*476/5760,'limitation':'Illustrative symmetry and proportional attribution; actual downward response nonlinear, balances and interest floors change. Quantitative rate figures checked in earnings-call transcript; related 10-Q identified but complete direct 10-Q fetch unavailable. Not a forecast.'}}
data['price_disagreements_2026_09_25']={'AMP':{'page_header':492.96,'history_row':497.19},'HIG':{'page_header':124.23,'history_row':124.48},'AIZ':{'page_header':265,'history_row':266.67},'IBKR':{'page_header':89.24,'history_row':89.22}}
data['limits']=['Targeted filing-led underwriting, not a complete forensic reserve audit or certified current quote.','Hurdles and multiples are analyst investment judgments, not estimated statistical probabilities.','No bear scenario is a maximum loss; mark-to-market drawdowns can exceed the terminal scenario.','AMP can fall with equity markets; HIG/AIZ retain reserve, credit and catastrophe risk; IBKR carries trading-volume, rates, regulation and operational risks.','Do not infer cash distributability from cash-flow statements of regulated financial companies.','Full original historical model remains unvalidated; these are independent prospective valuations.']
(OUT/'financials.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
for t,d in data['stocks'].items():
 b=d['scenarios']['base'];print(t,d['rating'],'max',round(d['maximum_entry_pretax'],2),'afterwithhold',round(d['maximum_entry_30pct_dividend_withholding'],2),'IRR',round(b['annual_cashflow_irr_pretax']*100,2),'range',[round(d['scenarios'][x]['present_value_at_hurdle'],2) for x in ['bear','base','bull']])
