import json,pathlib,csv,datetime,collections
p=pathlib.Path('source_bundle/equity_project');out=pathlib.Path('review/data');info=json.loads((p/'info.json').read_text());d=json.loads((p/'dash.json').read_text());d2=json.loads((p/'dash2.json').read_text());u3={r['t']:r for r in d2['U3']};included={r['t'] for r in d['U']}
rows=[]
for r in d['U']:
 o=info.get(r['t'],{}); price=o.get('currentPrice'); eps=o.get('forwardEps');pe=o.get('forwardPE'); calc=price/eps if price and eps else None
 row={'ticker':r['t'],'company':r['n'],'sector':r['s'],'snapshot_utc':datetime.datetime.fromtimestamp(o.get('regularMarketTime',0),datetime.timezone.utc).isoformat(),'vendor_price':price,'vendor_forward_eps':eps,'vendor_forward_pe':pe,'recomputed_pe':calc,'pe_relative_error':abs(calc/pe-1) if calc and pe else None,'quote_external_status':'not independently reconciled','consensus_external_status':'not independently reconciled','prior_screen_score':r['sc'],'prior_screen_rank':r['rk'],'prior_shortlist100':r['sl'],'prior_top30':r['t'] in d['top30'],'v3_gate':u3[r['t']]['gate'],'v3_rank':u3[r['t']]['rk']}
 rows.append(row)
with (out/'universe_data_ledger_497.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
errs=[r for r in rows if r['pe_relative_error'] is not None and r['pe_relative_error']>.01]
print('PE differences>1%',len(errs),[(r['ticker'],round(r['pe_relative_error'],4)) for r in errs][:30]); print('missing EPS',sum(r['vendor_forward_eps'] is None for r in rows));print('omitted from info',sorted(set(info)-included))
print('all timestamps',collections.Counter(x['snapshot_utc'][:10] for x in rows));print('top30 type',type(d['top30']),len(d['top30']))
summary={'universe_count':len(rows),'company_info_count':len(info),'omitted_from_info':sorted(set(info)-included),'pe_arithmetic_exceptions_over_1pct':len(errs),'missing_forward_eps':sum(r['vendor_forward_eps'] is None for r in rows),'external_quote_verified_count':0,'external_consensus_verified_count':0,'timestamp_dates':dict(collections.Counter(x['snapshot_utc'][:10] for x in rows))}
(out/'universe_validation_summary.json').write_text(json.dumps(summary,indent=2));print(summary)
