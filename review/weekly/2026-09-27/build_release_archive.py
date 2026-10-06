from pathlib import Path
import zipfile,json,hashlib,datetime
R=Path(__file__).resolve().parents[3];W=Path(__file__).resolve().parent
parents=['v005_2026-09-26_codex','v011_2026-09-27_claude']
archives={k:zipfile.ZipFile(R/'versions'/k/'package.zip') for k in parents}
entries={}
for parent,z in archives.items():
 for info in z.infolist():
  if not info.is_dir():entries[info.filename]=('archive',parent,info.filename)
for p in (R/'review').rglob('*'):
 if p.is_file() and '__pycache__' not in p.parts:
  entries[p.relative_to(R).as_posix()]=('local',p)
for rel in ['AGENTS.md','RESEARCH_VERSIONING.md','README.md','tools/publish_research_release.py']:
 p=R/rel
 if p.exists():entries[rel]=('local',p)
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
package=R/f'Investment_Trading_Weekly_2026-09-27_Codex_{stamp}.zip'
records=[]
with zipfile.ZipFile(package,'x',zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as out:
 for name,source in sorted(entries.items()):
  sha=hashlib.sha256();count=0
  inp=archives[source[1]].open(source[2]) if source[0]=='archive' else source[1].open('rb')
  with inp,out.open(name,'w',force_zip64=True) as dst:
   while True:
    data=inp.read(1024*1024)
    if not data:break
    dst.write(data);sha.update(data);count+=len(data)
  records.append({'file':name,'bytes':count,'sha256':sha.hexdigest(),'origin':source[1] if source[0]=='archive' else 'current weekly workspace'})
 out.writestr('PACKAGE_CONTENTS.json',json.dumps({'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parents':parents,'files':records},indent=2))
for z in archives.values():z.close()
with zipfile.ZipFile(package) as check: assert check.testzip() is None
result={'package':package.relative_to(R).as_posix(),'entries':len(records)+1,'bytes':package.stat().st_size,'sha256':hashlib.sha256(package.read_bytes()).hexdigest()}
(W/'package_build_receipt.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
