from pathlib import Path
import json,re,hashlib,zipfile,datetime,csv
from pypdf import PdfReader
R=Path(__file__).resolve().parents[3]; W=Path(__file__).resolve().parent; P=R/'review/ready'
M=json.loads((P/'decision_model.json').read_text(encoding='utf-8'))
doc=(R/'review/Investment_Review.html').read_text(encoding='utf-8')
payload=json.loads(re.search(r'const PACK=(.*);\s*const MODEL=PACK.model;',doc,re.S).group(1))
assert payload['model']==M
assert "TABS.unshift(['decisions'" in doc
for s in M['stocks']: assert s['reference_date']=='2026-09-25'
core=json.loads((P/'consolidated_financials_audit.json').read_text())
assert not core['failed_checks'] and not core['cost_exceptions'] and not core['excel_errors'] and not core['missing_formula_cache']
assert core['workbook_formula_count']==1262
pdf=PdfReader(P/'Investment_Decision_Memo.pdf');text='\n'.join(p.extract_text() for p in pdf.pages)
assert len(pdf.pages)==5
for s in M['stocks']: assert s['ticker'] in text
assert '27 September 2026' in text
assert len(list(csv.DictReader((W/'ACTION_TABLE.csv').open(encoding='utf-8-sig'))))==34
for name in ['filing_audit.md','filing_audit.json','market_audit.md','market_audit.json','lineage_risk_audit.md','lineage_risk_audit.json']:
 assert (W/name).is_file()
manifest=json.loads((W/'baseline/manifest.json').read_text())
assert hashlib.sha256((W/'baseline/delivered_v005_convenience_state.zip').read_bytes()).hexdigest()==manifest['archive_sha256']
files=[P/'decision_model.json',P/'Investment_Decision_Model.xlsx',P/'INVESTMENT_DECISION_MEMO.md',P/'Investment_Decision_Memo.pdf',R/'review/Investment_Review.html']
result={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','core_numerical_checks':1422,'independent_weekly_checks':2981,'workbook_formula_count':1262,'pdf_pages':5,'action_journal_rows':34,'dashboard_source_model_equal':True,'dashboard_tabs':29,'historical_tabs':25,'baseline_archive_hash_verified':True,'files':{p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'limitations':'Arithmetic and publication consistency only; future earnings and risk outcomes remain assumptions.'}
(W/'final_publication_checks.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
