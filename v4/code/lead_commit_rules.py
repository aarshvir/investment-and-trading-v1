"""Pre-registration firewall for the selection rules (A2 loop-3/4 must-fix).

`python code/lead_commit_rules.py "reason"` appends {time, sha256 of lead_build_portfolio.py and lead_portfolio.py,
reason} to outputs/rule_commitments.jsonl. lead_build_portfolio.py refuses to run unless the current hash of those two
files matches the latest commitment, so any rule change must be committed (timestamped, with its reason) before the
build that uses it can read any diligence output. The log is append-only; earlier entries are never rewritten.
Rule (j) predates this firewall: it was written after the wave-1 verdicts were known (STATE.md 12:38) and is committed
retroactively in the first entry, which says so."""
import hashlib, json, pathlib, sys, datetime
V4 = pathlib.Path(__file__).resolve().parents[1]
FILES = [V4 / 'code' / 'lead_build_portfolio.py', V4 / 'code' / 'lead_portfolio.py']
LOG = V4 / 'outputs' / 'rule_commitments.jsonl'


def current_hash():
    h = hashlib.sha256()
    for f in FILES:
        h.update(f.read_bytes())
    return h.hexdigest()


def latest():
    if not LOG.exists():
        return None
    lines = [l for l in LOG.read_text(encoding='utf-8').splitlines() if l.strip()]
    return json.loads(lines[-1]) if lines else None


if __name__ == '__main__':
    reason = ' '.join(sys.argv[1:]) or 'no reason given'
    e = {'time': datetime.datetime.now().isoformat(timespec='seconds'), 'sha256': current_hash(), 'files': [f.name for f in FILES], 'reason': reason}
    with LOG.open('a', encoding='utf-8') as fh:
        fh.write(json.dumps(e) + '\n')
    print('committed', e['sha256'][:12], e['time'])
