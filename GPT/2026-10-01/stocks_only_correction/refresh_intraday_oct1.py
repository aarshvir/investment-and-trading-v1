"""Timestamped public late-sale check for a 20-stock proposed basket."""
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
import requests

HERE=Path(__file__).resolve().parent
RAW=HERE/'raw_intraday';RAW.mkdir(exist_ok=True)
TICKERS=['MSFT','AMP','NVDA','ADP','TJX','RSG','MA','MCK','STE','BALL','DOV','BR','AXP','USB','CRH','PTC','VEEV','GDDY','ALLE','HIG']
s=requests.Session();s.headers['User-Agent']='PersonalInvestmentResearch/1.0 public-source audit'
records=[]
for t in TICKERS:
    url=f'https://cdn-api.cboe.com/api/global/delayed_quotes/quotes/{t}.json'
    rec={'ticker':t,'url':url,'retrieved_utc':datetime.now(timezone.utc).isoformat()}
    try:
        response=s.get(url,timeout=15);rec['http_status']=response.status_code
        if response.status_code==200:
            source=response.json();d=source.get('data',{})
            rec.update(provider_timestamp=source.get('timestamp'),symbol=d.get('symbol'),last=d.get('last'),close=d.get('close'),last_trade_time=d.get('last_trade_time'),prev_day_close=d.get('prev_day_close'))
            rec['session_match']=str(rec['last_trade_time']).startswith('2026-10-01') and rec['symbol']==t
            payload={'metadata':rec,'raw_response':source}
        else:
            rec['error']=response.text[:200];payload={'metadata':rec,'raw_response_excerpt':response.text[:500]}
    except Exception as exc:
        rec['error']=str(exc);payload={'metadata':rec}
    rawbytes=json.dumps(payload,indent=2,allow_nan=False).encode()
    (RAW/f'{t}.json').write_bytes(rawbytes)
    rec['raw_sha256']=hashlib.sha256(rawbytes).hexdigest();records.append(rec)
    print(t,rec.get('close'),rec.get('last_trade_time'),rec.get('http_status'),flush=True)
    time.sleep(.4)
(HERE/'INTRADAY_OCT1_CBOE.json').write_text(json.dumps({'prepared_utc':datetime.now(timezone.utc).isoformat(),'scope':len(TICKERS),'matched_session':sum(bool(x.get('session_match')) for x in records),'records':records,'warning':'Delayed public late sale during open US session, not completed-session close or executable price.'},indent=2),encoding='utf-8')
