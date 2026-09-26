import json, pathlib, datetime, hashlib
p=pathlib.Path('source_bundle/equity_project')
for fn in ['dash.json','dash2.json','info.json']:
 d=json.loads((p/fn).read_text()); print(fn,type(d).__name__,list(d)[:30]);
 if fn=='dash.json': print('asof',d.get('asof')); print('C sample',str(next(iter(d['C'].items())))[:2300])
 if fn=='dash2.json': print('CV keys',d.get('CV',{}).keys());print('CV sample',str(d.get('CV'))[:1700])
i=json.loads((p/'info.json').read_text())
for t in ['NVDA','MSFT','CPAY','AMP','RL','AME','SNA','ABNB','NTAP','PAYX','IBKR','HIG','ALLE','AIZ']:
 o=i[t]; print(t,{k:o.get(k) for k in ['regularMarketPrice','currentPrice','regularMarketTime','forwardPE','forwardEps','trailingPE','lastFiscalYearEnd','mostRecentQuarter']}); print('time',datetime.datetime.fromtimestamp(o.get('regularMarketTime',0),datetime.timezone.utc).isoformat())
a=pathlib.Path('HANDOFF_v3_US_Equity_Conviction_Research.md').read_bytes();b=pathlib.Path('C:/Users/user/.codex/attachments/6e6168e1-7a37-4cd5-80e3-4b6ed817db08/Pasted text.txt').read_bytes();print('handoff comparison',len(a),len(b),a==b)
