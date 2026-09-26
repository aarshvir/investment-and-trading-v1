import json,pathlib,collections,csv,hashlib,difflib
p=pathlib.Path('source_bundle/equity_project'); out=pathlib.Path('review/data')
i=json.loads((p/'info.json').read_text()); d=json.loads((p/'dash.json').read_text()); d2=json.loads((p/'dash2.json').read_text())
print('universe',len(i),len(d['U']),len(d['C']),len(d2['U3']))
print('U row',d['U'][0]);print('U3 row',d2['U3'][0]);print('C2 sample',str(next(iter(d2['C2'].items())))[:4000]);print('NC',str(d2['CV']['NC'])[:8000]);print('grade',d2['grade3']);print('tail',pathlib.Path(p/'dash_tpl_v3.html').read_text()[-2200:])
manifest=[{'file':str(x.relative_to(p)),'bytes':x.stat().st_size,'sha256':hashlib.sha256(x.read_bytes()).hexdigest()} for x in p.iterdir() if x.is_file()]
(out/'source_manifest.json').write_text(json.dumps(manifest,indent=2))
a=pathlib.Path('HANDOFF_v3_US_Equity_Conviction_Research.md').read_text(encoding='utf-8-sig').splitlines(); b=pathlib.Path('C:/Users/user/.codex/attachments/6e6168e1-7a37-4cd5-80e3-4b6ed817db08/Pasted text.txt').read_text(encoding='utf-8-sig').splitlines();delta=list(difflib.unified_diff(a,b));(out/'pasted_vs_handoff.diff').write_text('\n'.join(delta),encoding='utf-8');print('delta lines',len(delta));print('\n'.join(delta[:60]))
