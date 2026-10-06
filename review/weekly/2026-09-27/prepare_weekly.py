from pathlib import Path
import json, hashlib, zipfile, datetime, urllib.request

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
READY = ROOT / 'review/ready'
baseline = OUT / 'baseline'
baseline.mkdir(exist_ok=True)
archive = baseline / 'delivered_v005_convenience_state.zip'
if not archive.exists():
    files = sorted(p for p in READY.rglob('*') if p.is_file()) + [ROOT/'review/Investment_Review.html']
    with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, p.relative_to(ROOT).as_posix())
    (baseline/'manifest.json').write_text(json.dumps({
        'parent': 'v005_2026-09-26_codex',
        'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
        'files': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    }, indent=2))
raw = OUT/'raw_funds'
raw.mkdir(exist_ok=True)
sources = {
    'vuaa': 'https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-',
    'ib01': 'https://www.ishares.com/uk/individual/en/products/307243/ishares-treasury-bond-0-1yr-ucits-etf-fund'
}
manifest = []
for name, url in sources.items():
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    response = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=40)
    data = response.read()
    (raw/(name+'.html')).write_bytes(data)
    manifest.append(dict(name=name, url=url, retrieved_utc=stamp, status=response.status, sha256=hashlib.sha256(data).hexdigest()))
(raw/'manifest.json').write_text(json.dumps(manifest, indent=2))
print(json.dumps({'baseline_preserved': str(archive), 'fund_sources': manifest}, indent=2))

