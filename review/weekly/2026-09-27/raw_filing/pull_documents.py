import urllib.request,json,pathlib,hashlib,datetime
from html.parser import HTMLParser
root=pathlib.Path(__file__).parent
sources={
'HIG_20260925_8K.html':'https://www.sec.gov/Archives/edgar/data/874766/000087476626000064/hig-20260923.htm',
'PAYX_Q1FY27_10Q.html':'https://www.sec.gov/Archives/edgar/data/723531/000072353126000006/payx-20260831.htm',
'LH_20260922_8K.html':'https://www.sec.gov/Archives/edgar/data/920148/000092014826000205/lh-20260922.htm',
'LH_Q22026_10Q.html':'https://www.sec.gov/Archives/edgar/data/920148/000092014826000175/lh-20260630.htm',
'RSG_Q22026_release.html':'https://www.sec.gov/Archives/edgar/data/1060391/000106039126000273/exhibit991q22026.htm',
'NTAP_20260924_144.xml':'https://www.sec.gov/Archives/edgar/data/1002047/000195004726009789/primary_doc.xml'}
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[]
 def handle_data(self,d):self.out.append(d)
manifest=[]
for name,url in sources.items():
 row=dict(file=name,url=url,retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research source verification research@example.com'}),timeout=20) as r:raw=r.read()
  (root/name).write_bytes(raw);row.update(sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw));parser=Text();parser.feed(raw.decode('utf-8',errors='replace'));txt=' '.join(' '.join(parser.out).split());(root/name).with_suffix('.txt').write_text(txt,encoding='utf-8')
  if '8K' in name or '144' in name:print(name+'\n'+txt[-18000:])
 except Exception as e:row['error']=str(e)
 manifest.append(row)
(root/'document_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))
