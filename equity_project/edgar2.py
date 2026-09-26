# EARNINGS-RELEASE READER AGENT: pulls every 8-K Item 2.02 press release (last ~2 years) from SEC EDGAR and reads it
import requests, json, re, time, pickle, os, pandas as pd, numpy as np
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Independent equity research (personal, non-commercial) research-bot@proton.me','Accept-Encoding':'gzip, deflate'}
import sys
pool=sys.argv[1].split(',')
tk=requests.get('https://www.sec.gov/files/company_tickers.json',headers=H,timeout=30).json()
cik={v['ticker'].replace('.','-'):str(v['cik_str']).zfill(10) for v in tk.values()}
OUT=pickle.load(open('edgar.pkl','rb')) if os.path.exists('edgar.pkl') else {}
def get(u):
    for k in range(3):
        try:
            time.sleep(0.15); r=requests.get(u,headers=H,timeout=30)
            if r.status_code==200: return r
        except Exception: pass
        time.sleep(1)
    return None
def txt(html):
    html=re.sub(r'(?is)<(script|style).*?</\1>',' ',html); t=re.sub(r'(?s)<[^>]+>',' ',html)
    t=re.sub(r'&nbsp;|&#160;',' ',t); t=re.sub(r'&amp;','&',t); t=re.sub(r'&#8217;|&rsquo;',"'",t); t=re.sub(r'&#\d+;|&\w+;',' ',t)
    return re.sub(r'\s+',' ',t)
def one(t):
    if t in OUT or t not in cik: return t,OUT.get(t)
    c=cik[t]; r=get(f'https://data.sec.gov/submissions/CIK{c}.json')
    if r is None: return t,None
    rec=r.json()['filings']['recent']; docs=[]
    for i,f in enumerate(rec['form']):
        if f=='8-K' and '2.02' in (rec['items'][i] or '') and rec['filingDate'][i]>='2024-07-01':
            acc=rec['accessionNumber'][i].replace('-','')
            ix=get(f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/index.json')
            if ix is None: continue
            items=[x['name'] for x in ix.json()['directory']['item'] if x['name'].lower().endswith(('.htm','.html'))]
            ex=[x for x in items if re.search(r'ex-?99|exh?99|ex99|pressrel|earningsrel|q\d.*release|pr\.htm',x.lower()) and 'cfo' not in x.lower()] or [x for x in items if x!=rec['primaryDocument'][i] and 'index' not in x.lower()]
            if not ex: continue
            d=get(f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/{ex[0]}')
            if d is None: continue
            docs.append(dict(date=rec['filingDate'][i],url=f'https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc}/{ex[0]}',text=txt(d.text)[:60000]))
        if len(docs)>=9: break
    return t,docs
with ThreadPoolExecutor(4) as ex:
    for t,d in ex.map(one,pool): OUT[t]=d
pickle.dump(OUT,open('edgar.pkl','wb'))
print('companies',len([t for t in pool if OUT.get(t)]),'of',len(pool),'releases',sum(len(OUT[t]) for t in pool if OUT.get(t)))
