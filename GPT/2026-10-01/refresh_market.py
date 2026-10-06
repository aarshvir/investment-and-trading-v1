from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
import hashlib,json,math,requests,time,zipfile
R=Path(__file__).resolve().parents[2]; G=Path(__file__).resolve().parent
P=R/'versions/v011_2026-09-27_claude/package.zip'; Q=R/'versions/v012_2026-09-27_codex/reports/review/ready/decision_model.json'
with zipfile.ZipFile(P) as z:
    names=z.namelist(); path=next(x for x in names if x.endswith('/lead_portfolio_build.json')); C=json.loads(z.read(path))['candidates']
    path2=next(x for x in names if x.endswith('/lead_portfolio.json')); H=json.loads(z.read(path2))['rows']
held={x['t'] for x in H}; near=[]
for x in sorted((a for a in C if a.get('eligible') and a['t'] not in held),key=lambda a:(a.get('rank') if a.get('rank')==a.get('rank') else 9999)):
    if x['t'] not in near: near.append(x['t'])
    if len(near)==50:break
old=json.loads(Q.read_text())['stocks']; og=[x['ticker'] for x in old]
mega=['AAPL','AMZN','GOOGL','META','AVGO','COST','GOOG','UNH','TSLA']
tickers=list(dict.fromkeys([x['t'] for x in H]+og+near+mega+['SPY','QQQ']))
assert len(near)==50
scope={'prepared_utc':datetime.now(timezone.utc).isoformat(),'latest_completed_us_session_target':'2026-09-30','parent_releases':['v011_2026-09-27_claude','v012_2026-09-27_codex'],'near_miss_selection':'First 50 eligible nonheld names by archived v011 original rank. Coverage definition only, not evidence of investment merit.','v011_holdings':[x['t'] for x in H],'v012_original14':og,'near_miss50':near,'additional_mega_caps_and_benchmarks':mega+['SPY','QQQ'],'unique_count':len(tickers),'tickers':tickers}
(G/'market_scope.json').write_text(json.dumps(scope,indent=2))
raw=G/'raw_market';raw.mkdir(exist_ok=True)
S=requests.Session();S.headers['User-Agent']='PersonalInvestmentResearch/1.0 public-source audit'
def fetch(t):
    u=f'https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/{t}.json';stamp=datetime.now(timezone.utc).isoformat();rec={'ticker':t,'url':u,'retrieved_utc':stamp}
    try:
        response=S.get(u,timeout=20);rec['http_status']=response.status_code
        if response.status_code==200:
            data=response.json();rec['raw_response']=data;d=data.get('data',{});rec['provider_timestamp']=data.get('timestamp');rec['symbol']=d.get('symbol');rec['close']=d.get('close');rec['last_trade_time']=d.get('last_trade_time');rec['session_match']=str(d.get('last_trade_time','')).startswith('2026-09-30') and d.get('symbol')==t and isinstance(d.get('close'),(int,float)) and d['close']>0
        else:rec['body_excerpt']=response.text[:300]
    except Exception as e:rec['error']=str(e)
    return rec
records=[]
with ThreadPoolExecutor(max_workers=3) as pool:
    futures={pool.submit(fetch,t):t for t in tickers}
    for fut in as_completed(futures):
        r=fut.result();t=r['ticker'];rawbytes=json.dumps(r,indent=2,allow_nan=False).encode();(raw/(t.replace('.','_')+'.json')).write_bytes(rawbytes)
        records.append({k:v for k,v in r.items() if k!='raw_response'} | {'raw_sha256':hashlib.sha256(rawbytes).hexdigest()})
        print(t,r.get('close'),r.get('last_trade_time'),r.get('http_status'),flush=True)
records.sort(key=lambda x:x['ticker']);coverage={'scope':len(tickers),'session_matched':sum(bool(x.get('session_match')) for x in records),'failures':[x['ticker'] for x in records if not x.get('session_match')],'provider':'Cboe public delayed quote endpoint; close and last_trade_time; not broker executable or guaranteed official auction close','records':records}
(G/'market_quotes_2026-09-30.json').write_text(json.dumps(coverage,indent=2));print('SUMMARY',coverage['scope'],coverage['session_matched'],coverage['failures'])
