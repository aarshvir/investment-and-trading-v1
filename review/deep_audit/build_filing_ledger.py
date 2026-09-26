import json,csv,pathlib,hashlib
root=pathlib.Path(__file__).parent
manifest=json.loads((root/'raw_filing/manifest.json').read_text(encoding='utf-8'))
sources={x['file']:x for x in manifest}
rows=[]
def add(ticker,field,period,units,basis,saved,primary,formula,files,locator,status,quarantine,note=''):
 rows.append(dict(id=f'F{len(rows)+1:03}',ticker=ticker,field=field,period=period,units=units,basis=basis,saved_value=saved,primary_or_derived_value=primary,formula=formula,source_urls=' | '.join(sources[f]['url'] for f in files),source_files=' | '.join(files),source_sha256=' | '.join(sources[f].get('sha256','NOT_ARCHIVED') for f in files),retrieval_utc=' | '.join(sources[f]['retrieved_at_utc'] for f in files),locator=locator,information_cutoff='2026-09-24 US close',status=status,quarantine=quarantine,notes=note,reviewer='deep_filing_accounting'))
nv=['nvda_fy2026_10k.html','nvda_q2_2027_10q.pdf']
add('NVDA','TTM CFO','TTM ended 2026-07-26','USD million','GAAP-derived',134359.998464,134360,'102718+74421-42779',nv,'FY26 10-K p55; Q2 FY27 10-Q p8','RECONCILED_ROUNDING',False)
add('NVDA','TTM capital cash purchases','TTM ended 2026-07-26','USD million','GAAP-derived',7354,7354,'6042+4434-3122',nv,'Cash-flow investing section, same pages','RECONCILED',False)
add('NVDA','TTM conventional FCF','TTM ended 2026-07-26','USD million','Analyst CFO minus cash PPE/intangibles',127006,127006,'134360-7354',nv,'Cash-flow statements','RECONCILED_AGGREGATE',False,'Saved value is deep.q_cf four-quarter sum; individual vendor quarters retain small differences.')
add('NVDA','TTM related principal','TTM ended 2026-07-26','USD million','GAAP-derived',None,120,'101+92-73',nv,'Cash-flow financing section','RECONCILED',False)
add('NVDA','TTM company FCF','TTM ended 2026-07-26','USD million','Company non-GAAP formula',None,126886,'134360-7354-120',nv+['nvda_q2_2027_release.html'],'Cash-flow statements and non-GAAP FCF definition','RECONCILED',False)
add('NVDA','info.freeCashflow','Vendor period unspecified, presumed TTM is challenged','USD million','Vendor unknown',41809.874944,127006,'Conventional TTM less saved=85196.125056',nv,'Cash-flow statements vs info.json','MATERIAL_UNRESOLVED_VENDOR_DEFINITION',True,'Primary value is explicit conventional FCF comparator, not asserted same-basis replacement.')
ab=['abnb_q2_2026_10q.html']
add('ABNB','Q2 CFO','2026-04-01 to 2026-06-30','USD million','GAAP',None,1270,'Direct',ab,'MD&A p26 FCF reconciliation','VERIFIED_TABLE',False)
add('ABNB','Q2 FCF','2026-04-01 to 2026-06-30','USD million','Company non-GAAP',1300,1253,'1270-17',ab,'MD&A p26 FCF reconciliation','RECONCILED_ROUNDED_CLAIM',False,'$1.3bn rounded claim is supportable.')
add('ABNB','Q2 FCF margin','2026-04-01 to 2026-06-30','percent','Company non-GAAP',35,1253/3608*100,'1253/3608*100',ab,'MD&A pp25-26','RECONCILED_ROUNDING',False)
add('ABNB','Q2 adjusted EBITDA','2026-04-01 to 2026-06-30','USD million','Company adjusted',1300,1261,'816+81+7+37-183+17+487+1-2',ab,'MD&A p26 adjusted EBITDA reconciliation','RECONCILED_ROUNDED_CLAIM',False,'Same rounded headline as FCF; definitions remain distinct.')
add('ABNB','Customer-held funds treatment','Q2 2026','text','Cash-flow classification',None,'Customer-held funds affect FCF only through interest','Direct footnote',ab,'MD&A p26 paragraph following FCF table','VERIFIED_QUALIFICATION',False,'Normalize own service-fee collection timing and RNPL separately.')
nt=['ntap_q1_2027_10q.html','ntap_q1_2027_release.html']
add('NTAP','CFO YoY bridge','Q1 FY27 ended 2026-07-31 vs 2025-07-25','USD million','GAAP-derived',-170,-170,'142-18+0+15-14-61-149-230-224+126+165+80-2',nt,'10-Q p6 cash-flow statement; MD&A pp27-28','RECONCILED',False)
add('NTAP','Q1 FCF','Q1 FY27 ended 2026-07-31','USD million','Company non-GAAP',401,401,'503-102',nt,'Cash-flow p6; release FCF reconciliation','RECONCILED',False)
add('NTAP','FCF YoY change','Q1 FY27 vs Q1 FY26','percent','Derived',-35,(401/620-1)*100,'(401/620-1)*100',nt,'Release FCF reconciliation','RECONCILED_ROUNDING',False)
add('NTAP','Inventory turns','Q1 FY27 vs Q1 FY26','times','Company supplemental',None,'6 versus 14','Annualized COGS / net inventories',nt,'Release supplemental balance-sheet items','VERIFIED_TABLE',False,'Economic recoverability of inventory remains unproven.')
cp=['cpay_q2_2026_10q.html','cpay_q2_2026_ex991.html']
add('CPAY','H1 conventional FCF','2026-01-01 to 2026-06-30','USD million','Analyst CFO minus capex',None,1307.950,'1413.479-105.529',cp,'10-Q p5 cash-flow statement','RECONCILED',False)
add('CPAY','H1 company FCF alias','2026-01-01 to 2026-06-30','USD million','Adjusted net income',None,861.554,'598.373+324.004-104.926+44.103',cp,'Earnings exhibit non-GAAP definition and Exhibit1','RECONCILED_DIFFERENT_DEFINITION',False)
add('CPAY','Company leverage headline','As of 2026-06-30','times','Management ratio',2.7,2.55,'Numerator and denominator not independently rebuilt',cp,'Earnings release CFO commentary; 10-Q pp40-42 credit facilities','MANAGEMENT_REPORTED_ONLY',True,'2.55x verified as management statement; neither 2.7x nor covenant calculation certified.')
add('CPAY','info.freeCashflow','Vendor period unspecified','USD million','Vendor unknown',1946.175872,None,'Saved CFO=1847.283968; FCF>CFO by98.891904',cp,'Source info.json; 10-Q p5 for definitions','UNRESOLVED_PERIOD_AND_DEFINITION',True)
am=['ame_q2_2026_10q.html']
add('AME','June carrying debt','Instant 2026-06-30','USD million','GAAP carrying debt',2310.944,2036.174,'980.633+1055.541',am,'Balance sheet p5','DEFINITION_DIFFERENCE_UNRESOLVED',True,'Vendor total debt may include leases; do not call difference an error without bridge.')
add('AME','June cash','Instant 2026-06-30','USD million','GAAP cash and equivalents',495.446016,495.446,'Direct',am,'Balance sheet p5','RECONCILED_ROUNDING',False)
add('AME','Acquisition term financing capacity','June 2026 commitment','USD million','Committed not drawn',None,4000,'1625+1625+750',am,'Note12 p17','VERIFIED_COMMITMENT_ONLY',False)
add('AME','Indicor purchase price','Completed 2026-08-26','USD million','Cash acquisition',5000,5000,'Direct announcement',['ame_closing_8k.html','ame_closing_release.html'],'8-K Item8.01 and linked closing announcement','VERIFIED_EVENT',False,'Release available in web tool; direct archive timed out.')
add('AME','Illustrative closing net debt','Illustrative after acquisition','USD million','Scenario not actual',None,6540.728,'2036.174-495.446+5000',am+['ame_closing_8k.html'],'Analyst bridge','SCENARIO_ONLY',True,'Excludes intervening operations, fees, acquired cash/debt and other movements; cannot pass actual leverage gate.')
ms=['msft_2026_10k.html']
add('MSFT','FY26 conventional FCF','2025-07-01 to 2026-06-30','USD million','Analyst CFO minus cash capex',66987,66987,'182935-115948',ms,'Cash-flow statement p53; inline-XBRL cash tags','RECONCILED',False,'Saved value is quarterly FCF sum.')
add('MSFT','info.freeCashflow','Vendor period unspecified, presumed FY26/TTM challenged','USD million','Vendor unknown',16545.500160,66987,'66987-16545.500160=50441.499840',ms,'Cash-flow statement p53 vs info.json','MATERIAL_UNRESOLVED_VENDOR_DEFINITION',True)
add('MSFT','Finance-lease principal cash','2025-07-01 to 2026-06-30','USD million','GAAP financing cash',None,3101,'Direct',ms,'Note13 p78 supplemental cash flows','VERIFIED_TABLE_XBRL',False)
add('MSFT','After-finance-principal cash measure','2025-07-01 to 2026-06-30','USD million','Analyst-defined',None,63886,'182935-115948-3101',ms,'Cash-flow p53 and Note13 p78','RECONCILED_DISTINCT_MEASURE',False)
add('MSFT','Operating lease cash','2025-07-01 to 2026-06-30','USD million','GAAP operating cash',None,6443,'Already included in CFO',ms,'Note13 p78','VERIFIED_TABLE_XBRL',False)
add('MSFT','Uncommenced leases','As of 2026-06-30','USD million','Commitments',None,329100,'Direct disclosure',ms,'Note13 p78 paragraph after maturity table','VERIFIED_DISCLOSURE',False,'Some contractual conditions; starts FY27-FY33. Not all current debt.')
add('MSFT','Calendar 2026 capex guidance','Management forward outlook at Q4 FY26 call','USD million','Management forecast including finance leases',175000,175000,'Future classification changes; economic spend not inferred',['msft_q4_2026_call.html'],'CFO commentary immediately before outlook','VERIFIED_FORECAST_NOT_ACTUAL',True,'Quarantine comparability until finance/operating lease bridge is aligned.')
for ticker,expected in [('NVDA',96676),('MSFT',66987)]:
 f=root/'raw'/f'fmp_{ticker.lower()}_cashflow_annual.json'
 if f.exists():
  values=json.loads(f.read_text(encoding='utf-8')); v=next(x for x in values if str(x['fiscalYear'])=='2026')
  assert v['freeCashFlow']/1e6==expected
  rows.append(dict(id=f'F{len(rows)+1:03}',ticker=ticker,field='Annual FCF provider corroboration',period='FY2026 ended '+v['date'],units='USD million',basis='FMP CFO minus capex',saved_value=v['freeCashFlow']/1e6,primary_or_derived_value=expected,formula='FMP operatingCashFlow + signed capitalExpenditure',source_urls='FMP authenticated response; see raw file',source_files=str(f.relative_to(root)),source_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),retrieval_utc='See parent-session retrieval ledger',locator='FiscalYear2026 annual response row',information_cutoff='2026-09-24 US close',status='PROVIDER_AGREES_WITH_FILING_ARITHMETIC',quarantine=False,notes=('Full downloaded JSON. ' if ticker=='NVDA' else 'Selected fields transcribed from actual full Raw UI response; not full raw payload. ')+ 'Capture method and access: 00_provider_access_ledger.json. Separate provider transformation, common issuer origin. Zero optional fields are not established actual zeros. Does not certify TTM or prices.',reviewer='deep_filing_accounting'))
(root/'01_filing_ledger.json').write_text(json.dumps({'cutoff':'2026-09-24 US close','scope':'Six-company targeted field audit; not entire-company sign-off','rows':rows},indent=2),encoding='utf-8')
with (root/'01_filing_ledger.csv').open('w',newline='',encoding='utf-8-sig') as f:
 writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
assert 102718+74421-42779-(6042+4434-3122)==127006
assert 127006-(101+92-73)==126886
assert 142-18+15-14-61-149-230-224+126+165+80-2==-170
assert 816+81+7+37-183+17+487+1-2==1261
assert 182935-115948-3101==63886
print(f'Wrote {len(rows)} field rows; deterministic material bridges checked.')
