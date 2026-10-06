import urllib.request,json,pathlib,hashlib,datetime,time
root=pathlib.Path(__file__).parent
ciks={'NVDA':1045810,'CPAY':1175454,'AMP':820027,'RL':1037038,'AME':1037868,'SNA':91440,'ABNB':1559720,'NTAP':1002047,'PAYX':723531,'MSFT':789019,'IBKR':1381197,'HIG':874766,'ALLE':1579241,'AIZ':1267238,'RSG':1060391,'LH':920148}
manifest=[];summary=[]
for ticker,cik in ciks.items():
 url=f'https://data.sec.gov/submissions/CIK{cik:010}.json';row={'ticker':ticker,'url':url,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Research source verification research@example.com'})
  with urllib.request.urlopen(req,timeout=20) as r:raw=r.read()
  obj=json.loads(raw);p=root/f'{ticker}_submissions.json';p.write_bytes(raw);row.update(sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),file=p.name)
  recent=obj['filings']['recent'];items=[]
  for i,date in enumerate(recent['filingDate']):
   if date>='2026-09-20':items.append({k:recent[k][i] for k in ['filingDate','acceptanceDateTime','form','accessionNumber','primaryDocument','reportDate']})
  summary.append({'ticker':ticker,'recent_since_sep20':items,'latest_filing':recent['filingDate'][0] if recent['filingDate'] else None})
 except Exception as e:row['error']=str(e);summary.append({'ticker':ticker,'error':str(e)})
 manifest.append(row);time.sleep(.12)
(root/'submissions_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(root/'submissions_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
