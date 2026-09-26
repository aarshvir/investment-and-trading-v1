"""Reconcile frozen source fields to explicitly observed external facts; never fill missing evidence."""
import json,csv,pathlib,pickle,hashlib,datetime
P=pathlib.Path('source_bundle/equity_project'); O=pathlib.Path('review/deep_audit')
I=json.loads((P/'info.json').read_text()); E=pickle.load(open(P/'est_all.pkl','rb')); D=pickle.load(open(P/'deep.pkl','rb'))
C=pickle.load(open(P/'close10.pkl','rb'))
T=json.loads((P/'conv_port.json').read_text())['pick']
# Observed public forecast display, accessed 26 Sep Dubai, not historical-vintage API data.
# tuple: FY0, FY1, current low, current high, page table analyst count (not guaranteed EPS count), page update
obs={
'NVDA':(9.31,15.68,9.01,10.10,53,'2026-09-21'),
'CPAY':(27.39,31.45,27.23,27.90,16,'2026-09-02'),
'AMP':(46.53,51.67,45.89,47.65,8,'2026-09-22'),
'RL':(18.90,20.91,18.60,20.02,17,'2026-09-24'),
'AME':(8.34,9.59,8.25,8.44,20,'2026-09-25'),
'SNA':(19.82,21.34,19.60,20.03,8,'2026-08-20'),
'ABNB':(5.30,6.19,5.00,5.91,43,'2026-09-22'),
'NTAP':(10.01,11.12,9.84,11.00,17,'2026-09-18'),
'PAYX':(5.96,6.39,5.92,6.00,18,'2026-09-25'),
'MSFT':(19.76,23.68,19.21,20.70,50,'2026-09-25'),
'IBKR':(2.71,3.20,2.59,2.82,9,'2026-09-22'),
'HIG':(12.76,13.68,12.14,13.19,6,'2026-09-16'),
'ALLE':(8.96,9.77,8.86,9.08,11,'2026-09-22'),
'AIZ':(22.27,23.43,21.75,23.06,4,'2026-09-08')}
fymonth={'NVDA':(2027,'January'),'RL':(2027,'March'),'NTAP':(2027,'April'),'PAYX':(2027,'May'),'MSFT':(2027,'June')}
quotes={'NVDA':(224.58,'https://sogotrade2.websol.barchart.com/?1_selected=stockQuote&module=stockDetail&region=US&symbol=NVDA','Barchart hosted dated quote','second_vendor_corroborated'),
'MSFT':(497.93,'https://sogotrade2.websol.barchart.com/?1_selected=stockQuote&module=stockDetail&region=US&symbol=MSFT','Barchart hosted dated quote','second_vendor_corroborated'),
'AME':(247.74,'https://www.cboe.com/delayed_quotes/AME/quote_table/','Cboe delayed last 2026-09-24 16:00 ET','exchange_website_last_corroborated'),
'CPAY':(400.32,'https://stockscan.io/stocks/CPAY/price-history','StockScan dated close; upstream not established','external_display_corroborated'),
'AMP':(485.15,'https://stockanalysis.com/stocks/amp/','StockAnalysis dated close; site documents UTP/Cboe','external_display_corroborated'),
'RL':(351.86,'https://nl.investing.com/equities/polo-ralph-laur-historical-data','Investing.com historical table; upstream not established','external_display_corroborated'),
'SNA':(None,'https://www.cboe.com/delayed_quotes/SNA/quote_table/','Retrieved stale historical crawl; rejected','unverified'),
'ABNB':(151.39,'https://www.financecharts.com/stocks/ABNB/summary/price','FinanceCharts adjusted close; upstream not established','external_display_corroborated'),
'NTAP':(197.24,'https://www.financecharts.com/stocks/NTAP/summary/price','FinanceCharts adjusted close; upstream not established','external_display_corroborated'),
'PAYX':(101.59,'https://www.financecharts.com/stocks/PAYX/summary/price','FinanceCharts adjusted close; upstream not established','external_display_corroborated'),
'IBKR':(89.82,'https://www.financecharts.com/stocks/IBKR/summary/price','FinanceCharts adjusted close; upstream not established','external_display_corroborated')}
for z in json.loads((O/'raw/02_sep22_price_observations.json').read_text())['rows']:
 t=z['ticker'];quotes[t]=(z['sep24_close'],f'https://stockanalysis.com/stocks/{t.lower()}/history/','StockAnalysis dated raw close; site documents UTP/Cboe pricing; raw exchange payload not acquired','external_display_corroborated')
rows=[];fields=[]
for t in T:
 i=I[t]; tr=E[t]['trend']; eps0=float(tr.loc['0y','current']);eps1=float(tr.loc['+1y','current']);p=i['currentPrice'];o=obs[t];fy,month=fymonth.get(t,(2026,'December'))
 ee=D.get(t,{}).get('ee');disp=ee.loc['+1y'].to_dict() if ee is not None and '+1y' in ee.index else None
 q=quotes.get(t,(None,None,'No qualifying dated independent close recovered in this pass','unverified'))
 r=dict(ticker=t,company=i.get('longName'),currency=i.get('currency'),exchange=i.get('exchange'),quote_utc=datetime.datetime.fromtimestamp(i['regularMarketTime'],datetime.timezone.utc).isoformat(),price_original=p,price_external=q[0],price_external_url=q[1],price_external_basis=q[2],price_status=q[3],price_delta=None if q[0] is None else round(q[0]-p,8),fiscal_year_current=fy,fiscal_year_next=fy+1,fiscal_end_month=month,fiscal_date_precision='Forecast page month-end labels; exact issuer week-ending calendar must be retained separately',eps_current_original=eps0,eps_next_original=eps1,eps_info_forward=i.get('forwardEps'),pe_original=i.get('forwardPE'),pe_current_recomputed=p/eps0,pe_next_recomputed=p/eps1,ntm_eps=None,ntm_status='not_computable_from_only_two_annual_estimates_without_seasonality_assumption',eps_external_current=o[0],eps_external_next=o[1],eps_external_current_low=o[2],eps_external_current_high=o[3],external_table_analyst_count=o[4],external_page_last_updated=o[5],external_url=f'https://stockanalysis.com/stocks/{t.lower()}/forecast/',external_eps_basis='non-GAAP adjusted; exact company adjustments not independently bridged',external_provider='S&P Global via StockAnalysis public display',estimate_independence='Second distributor; original Yahoo upstream not documented, independent collection not certified',estimate_vintage_status='post_cutoff_page_update' if o[5]>'2026-09-24' else 'page_date_at_or_before_cutoff_but_field_vintage_unproven',eps_next_external_minus_cache=o[1]-eps1,eps_next_within_display_rounding=abs(o[1]-eps1)<=.0050001,cached_next_fy_dispersion=disp,dispersion_status='cache_only_not_independently_reconciled' if disp else 'missing_original_next_fy_dispersion',audit_date='2026-09-26 Asia/Dubai',decision_status='research_only_pending_point_in_time_estimates_and_underwriting')
 r['market_session_date']='2026-09-24'
 rows.append(r)
 def add(field,value,period,basis,source,status):fields.append(dict(ticker=t,field=field,value=value,units='USD/share' if 'eps' in field or 'price' in field else 'multiple',period=period,basis=basis,source=source,retrieved='2026-09-26 Asia/Dubai',status=status,quote_utc=r['quote_utc'],market_session_date=r['market_session_date']))
 add('price_original',p,'2026-09-24 regular session','vendor regularMarketPrice','source_bundle/equity_project/info.json','reproduced_cache')
 add('price_external',q[0],'2026-09-24',q[2],q[1],q[3])
 for n,v,period in [('eps_current_original',eps0,fy),('eps_next_original',eps1,fy+1)]:add(n,v,'FY'+str(period),'Yahoo trend; exact adjustment definition missing','source_bundle/equity_project/est_all.pkl','cache_only')
 for n,v,period in [('eps_external_current',o[0],fy),('eps_external_next',o[1],fy+1),('eps_external_current_low',o[2],fy),('eps_external_current_high',o[3],fy)]:add(n,v,'FY'+str(period),r['external_eps_basis'],r['external_url'],r['estimate_vintage_status'])
 add('pe_current_recomputed',p/eps0,'FY'+str(fy),'price_original / eps_current_original','local arithmetic','recomputed_not_forecast_verified')
 add('pe_next_recomputed',p/eps1,'FY'+str(fy+1),'price_original / eps_next_original','local arithmetic','recomputed_not_forecast_verified')
 add('ntm_eps',None,'next12months','quarterly estimates with fiscal mapping required','not available','blocked')
out=dict(cutoff='2026-09-24T20:00:00Z',retrieved_date='2026-09-26 Asia/Dubai',holdings=rows,notes=['No source count is an accuracy score.','External displays are not archived as-of vintages.','No independent analyst estimate vintage was acquired.','Consult raw/fmp_prices_2026-09-24.json for lead agent authenticated FMP results; not inferred by this script.'])
(O/'02_market_ledger.json').write_text(json.dumps(out,indent=2,default=str),encoding='utf-8')
with (O/'02_market_ledger.csv').open('w',newline='',encoding='utf-8-sig') as f:w=csv.DictWriter(f,fieldnames=list(fields[0]));w.writeheader();w.writerows(fields)
observations={t:dict(zip(['eps_current','eps_next','current_low','current_high','table_analyst_count','page_last_updated'],o),url=f'https://stockanalysis.com/stocks/{t.lower()}/forecast/') for t,o in obs.items()}
(O/'raw/02_public_forecast_observations.json').write_text(json.dumps(dict(type='manual_numeric_observations_from_web_tool_not_raw_api_response',observed_at='2026-09-26 Asia/Dubai',observations=observations),indent=2),encoding='utf-8')
manifest=[]
for f in [P/'info.json',P/'est_all.pkl',P/'deep.pkl',P/'close10.pkl',O/'raw/02_public_forecast_observations.json',O/'raw/02_sep22_price_observations.json',O/'raw/02_sep22_sp500_observation.json',O/'02_market_ledger.json',O/'02_market_ledger.csv',O/'02_market_audit.md',O/'build_market_ledger.py']:
 manifest.append(dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest(),type='original_supplied_file' if f.is_relative_to(P) else 'audit_observation_record' if f.parent.name=='raw' else 'audit_derived_artifact'))
(O/'02_market_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(dict(holdings=len(rows),field_rows=len(fields),next_eps_rounding_mismatches=[r['ticker'] for r in rows if not r['eps_next_within_display_rounding']],missing_dispersion=[r['ticker'] for r in rows if not r['cached_next_fy_dispersion']]),indent=2))
