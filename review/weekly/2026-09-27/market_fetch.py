import json,csv,pathlib,datetime,time,requests,zipfile,hashlib
O=pathlib.Path('review/weekly/2026-09-27'); R=O/'raw_market';R.mkdir(parents=True,exist_ok=True)
old=json.loads(pathlib.Path('review/ready/decision_model.json').read_text())['stocks']
cl=json.loads(pathlib.Path('versions/v011_2026-09-27_claude/reports/v4/outputs/lead_portfolio.json').read_text())['rows']
T=list(dict.fromkeys([x['ticker'] for x in old]+[x['t'] for x in cl]))
Z=zipfile.ZipFile('versions/v011_2026-09-27_claude/package.zip')
for name in ['d4_validation_prices.csv','d4_indep_prices.csv','d4_changelog_v3.csv','d4_live_snapshot.meta.json','d4_live_snapshot.parquet','d4_anomalies.csv']:
 hits=[n for n in Z.namelist() if n.endswith('/'+name)]
 if hits:
  raw=Z.read(hits[0]);(R/('inherited_'+name)).write_bytes(raw)
  local=pathlib.Path('v4/data')/name
  print('archive',name,'same_as_working',local.exists() and local.read_bytes()==raw,flush=True)
S=requests.Session();S.headers['User-Agent']='PersonalEquityResearch/1.0'
res=[]
for t in T:
 url=f'https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/{t}.json'
 stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 rec={'ticker':t,'url':url,'retrieved_utc':stamp}
 try:
  r=S.get(url,timeout=15);rec['http_status']=r.status_code
  if r.status_code==200:
   raw=r.json(); rec['response']=raw;d=raw.get('data',{});rec['close']=d.get('close');rec['last_trade_time']=d.get('last_trade_time');rec['provider_timestamp']=raw.get('timestamp')
  else:rec['body_excerpt']=r.text[:200]
 except Exception as e:rec['error']=str(e)
 (R/f'new_cboe_{t}.json').write_text(json.dumps(rec,indent=2));res.append(rec)
 print(t,rec.get('http_status'),rec.get('close'),rec.get('last_trade_time'),flush=True)
 if rec.get('http_status') in [403,429]:
  print('Stopping this provider after access/rate restriction',flush=True);break
 time.sleep(2.6)
(R/'new_cboe_summary.json').write_text(json.dumps(res,indent=2))
(R/'scope.json').write_text(json.dumps({'tickers':T,'original14':[x['ticker'] for x in old],'claude20':[x['t'] for x in cl]},indent=2))
