from pathlib import Path
from html.parser import HTMLParser
import re, json, html
root=Path(__file__).parent/'raw_filing'
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.out=[]
 def handle_data(self,d): self.out.append(d)
for p in root.glob('*.html'):
 raw=p.read_text(encoding='utf-8');parser=Text();parser.feed(raw)
 text=' '.join(' '.join(parser.out).split());p.with_suffix('.txt').write_text(text,encoding='utf-8')
 facts=[]
 for m in re.finditer(r'<ix:nonFraction\b([^>]*)>(.*?)</ix:nonFraction>',raw,re.I|re.S):
  attrs=dict(re.findall(r'([\w:]+)="([^"]*)"',m.group(1)))
  if any(s in attrs.get('name','') for s in ['NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','FinanceLeasePrincipalPayments','PaymentsOfFinanceLeasePrincipal','OperatingLeasePayments','FinanceLeaseInterestExpense','LongTermDebtCurrent','LongTermDebtNoncurrent']):
   facts.append({'attributes':attrs,'text':html.unescape(re.sub('<[^>]+>','',m.group(2)))})
 contexts={}
 for m in re.finditer(r'<(?:xbrli:)?context\b[^>]*id="([^"]+)"[^>]*>(.*?)</(?:xbrli:)?context>',raw,re.I|re.S):
  contexts[m.group(1)]=re.sub('<[^>]+>',' ',m.group(2))
 for f in facts: f['context']=contexts.get(f['attributes'].get('contextRef'),'CONTEXT_NOT_EXTRACTED')
 if facts:p.with_suffix('.facts.json').write_text(json.dumps(facts,indent=2),encoding='utf-8')
p=root/'msft_2026_10k.txt';t=p.read_text(encoding='utf-8')
for phrase in ['NOTE 13','Operating cash flows from operating leases','Net cash from operations','Additions to property and equipment','329.1']:
 pos=t.find(phrase);print('\n'+phrase+'\n'+t[max(0,pos-150):pos+3500])
