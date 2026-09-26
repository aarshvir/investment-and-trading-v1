"""Append-only local research releases; standard library only."""
from pathlib import Path, PurePosixPath
import argparse, datetime, hashlib, html, json, os, re, shutil, zipfile

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=ROOT/'versions'
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()
def atomic(path,text):
    tmp=path.with_name(path.name+'.new')
    with tmp.open('x',encoding='utf-8') as f:f.write(text)
    os.replace(tmp,path)
def rel(path):return path.relative_to(ROOT).as_posix()

def navigation(catalog):
    entries=sorted(catalog['releases'],key=lambda x:x['number'],reverse=True)
    md=['# Research versions','', 'Completed releases are preserved. Publication order is not an investment-quality score.','', '| Version | Author / prepared UTC | What changed | Reports | Complete archive |','|---|---|---|---|---|']
    cards=[]
    for r in entries:
        folder=r['id']; docs=r['convenient_reports']
        selected=[]
        for suffix,label in [('Investment_Decision_Memo.pdf','Memo PDF'),('Investment_Decision_Model.xlsx','Model'),('WEEKLY_POLICY_V2.md','Weekly policy')]:
            match=next((d for d in docs if d.endswith(suffix)),None)
            if match:selected.append((label,match))
        selected.append(('Release notes',folder+'/RELEASE_NOTES.md'))
        links=' · '.join(f'[{label}]({path})' for label,path in selected)
        md.append(f"| {folder} | {r['author']} / {r['prepared_utc']} | {r['summary'].replace('|','/')} | {links} | [ZIP]({folder}/package.zip) |")
        buttons=' '.join(f'<a href="{html.escape(path)}">{html.escape(label)}</a>' for label,path in selected)
        cards.append(f'<article><p class="eyebrow">{html.escape(folder)} · {html.escape(r["author"])}</p><h2>{html.escape(r["summary"])}</h2><p>Prepared {html.escape(r["prepared_utc"])} · Data: {html.escape(r["data_cutoff"])}</p><p>Parents: {html.escape(", ".join(r["parents"]) or "None recorded")}</p><div>{buttons} <a href="{folder}/package.zip">Complete version ZIP</a></div><p class="small">Published snapshot · SHA-256 manifest retained · Read release notes for scope and disagreements.</p></article>')
    md+=['','## Earlier and active workstreams','','These references retain their original labels; a working branch is not a completed release.','']
    legacy=[]
    for r in catalog.get('legacy_references',[]):
        md.append(f"- [{r['label']}](../{r['path']}) — {r['status']}")
        legacy.append(f'<li><a href="../{html.escape(r["path"])}">{html.escape(r["label"])}</a> — {html.escape(r["status"])}</li>')
    atomic(VERSIONS/'INDEX.md','\n'.join(md)+'\n')
    doc='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Investment research · Version library</title><style>body{margin:0;background:#0b1220;color:#e5eaf1;font:16px/1.65 system-ui}main{max-width:1080px;margin:auto;padding:45px 24px}h1{font-size:38px;line-height:1.2}h2{font-size:23px}article{margin:24px 0;padding:25px;background:#131f30;border:1px solid #314158;border-radius:12px}a{color:#bddcff}article a{display:inline-block;margin:5px 12px 5px 0}.eyebrow{color:#dec58a;font-size:13px;letter-spacing:.06em}.small{font-size:13px;color:#aab9cc}li{margin:12px 0}</style><main><p class="eyebrow">SHARED CLAUDE + CODEX RESEARCH</p><h1>Every version. Its evidence. What changed.</h1><p>Published reports stay available. A newer version is a new contribution—not automatic proof that an older investment judgment was wrong. Read the release notes and parent versions.</p>'+''.join(cards)+'<h2>Earlier reports and active work</h2><ul>'+''.join(legacy)+'</ul><p class="small">The complete archive contains the version-specific dashboard and supporting evidence. Extract it to use all local links. External chats must be given the handoff or package; this library does not synchronize chats automatically.</p></main></html>'
    atomic(VERSIONS/'index.html',doc)
    latest=entries[0]
    handoff=f'''# Latest shared research handoff

Latest completed publication: **{latest['id']}**, by {latest['author']}.

Summary: {latest['summary']}

Prepared UTC: {latest['prepared_utc']}. Data cutoff: {latest['data_cutoff']}.

Parents: {', '.join(latest['parents'])}.

Start with [version library](versions/index.html), [release notes](versions/{latest['id']}/RELEASE_NOTES.md), [full archive](versions/{latest['id']}/package.zip) and [machine-readable catalog](versions/catalog.json).

Read the latest completed releases from both authors before continuing. Verify inherited claims; record adopted, rejected and unresolved findings. Preserve all previous versions. A new publication does not automatically authorize trades or supersede the investment policy.

Claude's existing v4/ folder is a separately observed working branch; check its own STATE.md and later published releases. Do not claim this completed package incorporates unfinished parallel work. External Claude chats require these files to be supplied explicitly.

Follow RESEARCH_VERSIONING.md and publish the next delivered revision through tools/publish_research_release.py. Use the release IDs as explicit parents, not just the label "latest".
'''
    atomic(ROOT/'LATEST_HANDOFF.md',handoff)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--author',required=True,choices=['Codex','Claude']);ap.add_argument('--package',required=True);ap.add_argument('--notes',required=True);ap.add_argument('--summary',required=True);ap.add_argument('--parents',nargs='+',required=True);ap.add_argument('--data-cutoff',required=True);a=ap.parse_args()
    package=(ROOT/a.package).resolve();notes=(ROOT/a.notes).resolve()
    for f in [package,notes]:
        if not f.is_relative_to(ROOT) or not f.is_file():raise SystemExit('Input must be an existing workspace file: '+str(f))
    with zipfile.ZipFile(package) as z:
        if z.testzip():raise SystemExit('Package failed integrity check')
    VERSIONS.mkdir(exist_ok=True);lock=VERSIONS/'.publish.lock'
    fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    try:
        with os.fdopen(fd,'w') as f:f.write(f'pid={os.getpid()}\n')
        catalog_path=VERSIONS/'catalog.json'
        catalog=json.loads(catalog_path.read_text(encoding='utf-8')) if catalog_path.exists() else {'schema_version':1,'releases':[],'legacy_references':[]}
        numbers=[int(m[1]) for p in VERSIONS.iterdir() if (m:=re.match(r'^v(\d+)_',p.name))]
        number=max([4]+numbers)+1;now=datetime.datetime.now(datetime.timezone.utc);dubai=now.astimezone(datetime.timezone(datetime.timedelta(hours=4))).date().isoformat()
        rid=f'v{number:03d}_{dubai}_{a.author.lower()}';dest=VERSIONS/rid;dest.mkdir(exist_ok=False)
        initial_hash=sha(package);shutil.copyfile(package,dest/'package.zip')
        if sha(dest/'package.zip')!=initial_hash or sha(package)!=initial_hash:raise RuntimeError('Package changed during publication; incomplete release retained for inspection')
        shutil.copyfile(notes,dest/'RELEASE_NOTES.md')
        docs=[]
        with zipfile.ZipFile(dest/'package.zip') as z:
            for info in z.infolist():
                p=PurePosixPath(info.filename)
                # Convenient report copies only; full package remains authoritative.
                if info.is_dir() or '..' in p.parts or p.is_absolute():continue
                if p.suffix.lower() not in ['.pdf','.xlsx','.csv','.md','.json']:continue
                if any(part.startswith('raw_') or part in ['source_bundle','sources','data'] for part in p.parts):continue
                if not (info.filename.startswith('review/ready/') or info.filename.startswith('v4/outputs/') or info.filename.startswith('v4/dossiers/') or info.filename.startswith('review/weekly/')):continue
                out=dest/'reports'/Path(*p.parts);out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(z.read(info));docs.append(out.relative_to(VERSIONS).as_posix())
        release={'id':rid,'number':number,'author':a.author,'status':'completed','prepared_utc':now.isoformat(),'data_cutoff':a.data_cutoff,'parents':a.parents,'summary':a.summary,'original_package':rel(package),'package_sha256':initial_hash,'convenient_reports':docs,'policy':'Immutable historical publication. See notes for whether findings supersede or supplement earlier decisions.'}
        (dest/'release.json').write_text(json.dumps(release,indent=2),encoding='utf-8')
        manifest=[{'file':f.relative_to(dest).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(dest.rglob('*')) if f.is_file()]
        (dest/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
        assert all(sha(dest/r['file'])==r['sha256'] for r in manifest)
        catalog['releases'].append(release);catalog['latest_completed']=rid
        catalog.setdefault('latest_by_author',{})[a.author]=rid
        atomic(catalog_path,json.dumps(catalog,indent=2));navigation(catalog)
        print(json.dumps({'release':rid,'package_sha256':initial_hash,'report_copies':len(docs),'manifest_files_verified':len(manifest),'index':str(VERSIONS/'index.html')}))
    finally:lock.unlink()

if __name__=='__main__':main()
