from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor,as_completed
import hashlib,json,requests,time,zoneinfo
G=Path(__file__).resolve().parent;raw=G/'raw_market';scope=json.loads((G/'market_scope.json').read_text());tickers=scope['tickers'];S=requests.Session();S.headers['User-Agent']='Mozilla/5.0 PersonalInvestmentResearch/1.0'
def fetch(t):
    u=f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d';stamp=datetime.now(timezone.utc).isoformat();r={'ticker':t,'url':u,'retrieved_utc':stamp}
    try:
        response=S.get(u,timeout=20);r['http_status']=response.status_code
        if response.status_code==200:
            j=response.json();r['raw_response']=j;x=j['chart']['result'][0];q=x['indicators']['quote'][0];a=x.get('indicators',{}).get('adjclose',[{}])[0].get('adjclose',[]);ts=x['timestamp'];rows=[]
            for i,v in enumerate(ts):
                rows.append({'date_et':datetime.fromtimestamp(v,zoneinfo.ZoneInfo('America/New_York')).date().isoformat(),'timestamp_utc':datetime.fromtimestamp(v,timezone.utc).isoformat(),'close':q['close'][i],'adjclose':a[i] if i<len(a) else None,'open':q['open'][i],'high':q['high'][i],'low':q['low'][i],'volume':q['volume'][i]})
            r['rows']=rows;r['currency']=x['meta'].get('currency');r['symbol']=x['meta'].get('symbol');r['regular_market_time']=x['meta'].get('regularMarketTime')
        else:r['body_excerpt']=response.text[:300]
    except Exception as e:r['error']=str(e)
    return r
records=[]
with ThreadPoolExecutor(max_workers=2) as pool:
    for fut in as_completed({pool.submit(fetch,t):t for t in tickers}):
        r=fut.result();t=r['ticker'];last=next((x for x in r.get('rows',[]) if x['date_et']=='2026-09-30'),None);r['close_sep30']=last['close'] if last else None;r['session_match']=bool(last and r['symbol']==t and r['currency']=='USD' and isinstance(last['close'],(int,float)) and last['close']>0)
        data=json.dumps(r,indent=2,allow_nan=False).encode();(raw/('yahoo_'+t.replace('.','_')+'.json')).write_bytes(data)
        records.append({k:v for k,v in r.items() if k!='raw_response'}|{'raw_sha256':hashlib.sha256(data).hexdigest()});print(t,r.get('close_sep30'),r.get('http_status'),flush=True)
records.sort(key=lambda x:x['ticker']);out={'scope':len(tickers),'session_matched':sum(x.get('session_match',False) for x in records),'failures':[x['ticker'] for x in records if not x.get('session_match')],'source':'Yahoo public chart, 1d regular OHLC; no paid feed; dated full payload archived','records':records}
(G/'market_yahoo_2026-09-30.json').write_text(json.dumps(out,indent=2));print('SUMMARY',out['scope'],out['session_matched'],out['failures'])
