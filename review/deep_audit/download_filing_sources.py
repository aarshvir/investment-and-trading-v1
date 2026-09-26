import urllib.request, hashlib, json, pathlib, datetime, concurrent.futures
root=pathlib.Path(__file__).parent/'raw_filing'
root.mkdir(exist_ok=True,parents=True)
sources={
'ntap_q1_2027_10q.html':'https://www.sec.gov/Archives/edgar/data/1002047/000119312526380207/ntap-20260731.htm',
'cpay_q2_2026_10q.html':'https://www.sec.gov/Archives/edgar/data/1175454/000117545426000050/cpay-20260630.htm',
'nvda_q2_2027_10q.pdf':'https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf',
'nvda_fy2026_10k.html':'https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm',
'nvda_q2_2027_release.html':'https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/',
'abnb_q2_2026_10q.html':'https://www.sec.gov/Archives/edgar/data/1559720/000155972026000027/abnb-20260630.htm',
'ntap_q1_2027_release.html':'https://investors.netapp.com/news/news-details/2026/NetApp-Reports-First-Quarter-of-Fiscal-Year-2027-Results/default.aspx',
'cpay_q2_2026_ex991.html':'https://www.sec.gov/Archives/edgar/data/1175454/000117545426000045/ex991q2_2026.htm',
'ame_q2_2026_10q.html':'https://www.sec.gov/Archives/edgar/data/1037868/000103786826000175/ame-20260630.htm',
'ame_closing_8k.html':'https://www.sec.gov/Archives/edgar/data/1037868/000103786826000191/ame-20260826.htm',
'ame_closing_release.html':'https://investors.ametek.com/news-releases/news-release-details/ametek-completes-acquisition-indicor-instrumentation',
'msft_2026_10k.html':'https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm',
'msft_q4_2026_call.html':'https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4'}
def fetch(item):
 name,url=item; out={'file':name,'url':url,'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 if (root/name).exists():
  previous=json.loads((root/'manifest.json').read_text(encoding='utf-8')) if (root/'manifest.json').exists() else []
  found=next((x for x in previous if x['file']==name and 'sha256' in x),None)
  if found:return found
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'InvestmentResearch source verification contact research@example.com'})
  with urllib.request.urlopen(req,timeout=25) as response:
   raw=response.read();out.update(status=response.status,content_type=response.headers.get('content-type'),bytes=len(raw))
  (root/name).write_bytes(raw);out['sha256']=hashlib.sha256(raw).hexdigest()
 except Exception as e: out['error']=str(e)
 return out
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(fetch,sources.items()))
(root/'manifest.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
