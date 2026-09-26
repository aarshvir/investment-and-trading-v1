from pathlib import Path
import json,hashlib,csv,tomllib,zipfile,re,datetime
r=Path('review'); src=Path('source_bundle/equity_project')
manifest=json.loads((r/'data/source_manifest.json').read_text())
changed=[x['file'] for x in manifest if hashlib.sha256((src/x['file']).read_bytes()).hexdigest()!=x['sha256']]
assert not changed, changed
fm=json.loads((r/'deep_audit/raw_filing/manifest.json').read_text())
archived=[x for x in fm if x.get('status')==200]
assert len(archived)==12
for x in archived: assert hashlib.sha256((r/'deep_audit/raw_filing'/x['file']).read_bytes()).hexdigest()==x['sha256']
facts=sum(len(json.loads(p.read_text())) if isinstance(json.loads(p.read_text()),list) else 0 for p in (r/'deep_audit/raw_filing').glob('*.facts.json'))
rows=json.loads((r/'deep_audit/01_filing_ledger.json').read_text())['rows'];assert len(rows)==33
with (r/'deep_audit/02_market_ledger.csv').open(encoding='utf-8-sig') as f: mr=list(csv.DictReader(f))
assert len(mr)==154
provider=json.loads((r/'deep_audit/00_provider_access_ledger.json').read_text())
assert sum(x['status']=='live_response' for x in provider['price_access'])==2
assert sum(x['status']=='blocked_402' for x in provider['price_access'])==12
for x in provider['files']: assert hashlib.sha256((r/'deep_audit'/x['path']).read_bytes()).hexdigest()==x['sha256']
a=tomllib.loads(Path('C:/Users/user/.codex/automations/weekly-investment-evidence-and-action-review/automation.toml').read_text())
assert a['status']=='ACTIVE' and 'three separate parallel data reviews' in a['prompt']
status=json.loads((r/'data/automation_status.json').read_text());status.update(deep_audit_update_date='2026-09-26',three_data_passes_in_saved_prompt=True,prompt_sha256=hashlib.sha256(a['prompt'].encode()).hexdigest());(r/'data/automation_status.json').write_text(json.dumps(status,indent=2))
v=dict(audit_date='2026-09-26',browser='Chrome via supported computer-use API',tab_count=25,all25_tabs_rendered=True,original_tabs_preserved=16,new_deep_audit_tabs=2,filing_search_msft_count=8,filing_total=33,visual_check='Sources and regime page inspected at desktop width; dark/gold styling and five-input gate table rendered',new_mobile_check='Not rerun; initial23-tab build mobile evidence remains separately archived',scope='Browser render and targeted search checks; not full regression of every archived control',original_files_checked=len(manifest),original_files_changed=changed,archived_filing_hashes_verified=len(archived),market_field_rows=len(mr),fmp_price_successes=2,fmp_price_access_failures=12,weekly_automation_deep_audit_update_verified=True)
(r/'data/deep_dashboard_validation.json').write_text(json.dumps(v,indent=2),encoding='utf-8')
# No credential values should appear in deliverables; display only offending filenames, never matched text.
credential_hits=[]
for p in r.rglob('*'):
 if p.is_file() and p.suffix.lower() in ['.json','.md','.csv','.html','.log','.py','.txt']:
  s=p.read_text(encoding='utf-8',errors='ignore')
  if re.search(r'(?:apikey|api_key)\s*(?:=|%3D)\s*[A-Za-z0-9_-]{20,}',s,re.I):credential_hits.append(str(p))
assert credential_hits == ['review\\deep_audit\\raw_filing\\msft_q4_2026_call.html'], credential_hits
# Inspected exception: public Microsoft issuer page embeds its public MSN stock-widget parameters; no user credential captured.
print(json.dumps(v))
