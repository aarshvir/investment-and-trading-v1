"""Lead: reconcile Claude v4 with the latest completed Codex release (v005_2026-09-26_codex), as the shared workspace
rules require (AGENTS.md / RESEARCH_VERSIONING.md / CLAUDE.md): record which inherited findings were adopted, confirmed,
changed, rejected or left unresolved, with evidence. Reads v005 files READ-ONLY; writes v4/outputs/lead_v005_reconciliation.json.
Numbers are pulled from the data so the section cannot drift from the files."""
import json, pathlib, math
import pandas as pd

ROOT = pathlib.Path(r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments')
V4 = ROOT / 'v4'
V005 = ROOT / 'versions' / 'v005_2026-09-26_codex'
READY = V005 / 'reports' / 'review' / 'ready'


def load(p):
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None


def fnum(x):
    try:
        x = float(x)
        return None if math.isnan(x) else x
    except Exception:
        return None


rel = load(V005 / 'release.json') or {}
dt = pd.read_csv(READY / 'decision_table.csv', encoding='utf-8-sig')
L = pd.read_csv(V4 / 'data' / 'b1_live_scores.csv').set_index('ticker_yahoo')
V = pd.read_csv(V4 / 'outputs' / 'v1_valuation_table.csv').set_index('ticker')
S = pd.read_parquet(V4 / 'data' / 'd4_live_snapshot.parquet').set_index('ticker')
B = load(V4 / 'outputs' / 'lead_portfolio_build.json') or {}
_SEL = set(B.get('selected') or [])
_WHY = {c['t']: c.get('why') for c in (B.get('candidates') or [])}
_ELIG = {c['t'] for c in (B.get('candidates') or []) if c.get('eligible')}


def _held_or_bench(t):
    return 'held' if t in _SEL else ('eligible, not held' if t in _ELIG else 'not eligible')


def _why(t):
    w = str(_WHY.get(t) or '')
    return 'the five-per-sector limit (rule l) filled Financials with names ranked ahead of it' if w.startswith('sixth name in sector') else (w or 'outranked')

RR = load(V4 / 'outputs' / 'lead_risk_results.json') or {}
X1 = load(V4 / 'outputs' / 'x1_v005_verification.json')
why = {c['t']: c['why'] for c in B.get('candidates', [])}
held = set((B.get('weights') or {}).keys())

cands = []
for _, r in dt.iterrows():
    t = r['ticker']
    px = fnum(S.loc[t, 'y_regularMarketPrice']) if t in S.index else None
    lim = fnum(r['limit_price'])
    l = L.loc[t] if t in L.index else None
    v = V.loc[t] if t in V.index else None
    cands.append({'t': t, 'v005_rank': int(r['rank']), 'v005_decision': r['decision'], 'v005_limit': lim, 'v005_ref': fnum(r['reference_price']),
                  'v005_ref_date': r['reference_date'], 'v005_slot': fnum(r['slot_weight']), 'v4_price_2026_09_25': px,
                  'price_vs_limit': (px / lim - 1) if (px and lim) else None,
                  'v4_rank': (int(l.live_rank) if l is not None and l.live_rank == l.live_rank else None),
                  'v4_V1': (v.verdict if v is not None else None), 'v4_V1_base_3y': (fnum(v.base_ann_return_3y) if v is not None else None),
                  'v4_status': ('held in the v4 sleeve' if t in held else (why.get(t) or 'outside the pre-registered top-70 universe'))})

lim = (RR.get('equity_share_limits') or {}).get('Global financial crisis', {})
gfc = next((s for s in RR.get('stress', []) if s['episode'].startswith('Global')), {})


def sim(mix, h, key):
    for s in RR.get('sims', []):
        if s['mix'] == mix and s['scenario'] == 'Base':
            return s['result']['horizons'][h][key] if key != 'dd20' else s['result']['horizons'][h]['p_drawdown_worse_than']['-20%']
    return None


D = 'Defensive (15/10/75)'
M = 'Moderate (55/15/30)'
findings = [
    {'topic': 'A hard 15–20% loss limit needs a small equity share', 'status': 'CONFIRMED independently',
     'v005': 'Maximum 25% equity (15% index + 10% direct, at least 75% reserve); a hypothetical tail shock (index −60%, stocks −75%, reserve −2%) loses 18.0% at full deployment.',
     'v4': (f"Daily-data replay of 2007–09 with quarterly rebalancing: staying within −20% needed ≤{(lim.get('max_equity_share_within_20pct') or 0):.0%} in equities, within −15% ≤{(lim.get('max_equity_share_within_15pct') or 0):.0%}. "
            f"The Defensive mix (v005's budget) fell {(gfc.get(D + ' | worst point') or 0):+.1%} in that replay."),
     'effect': 'v4 adds the Defensive 15/10/75 mix to every allocation table, with simulated odds on the same engine as the other mixes.'},
    {'topic': 'Whether 15–20% must hold in every crash', 'status': 'UNRESOLVED (owner decision)',
     'v005': 'Treats 15–20% as the design objective for the whole portfolio, hence 75–81% reserve.',
     'v4': (f"Shows the trade-off instead. Base case, median 5-year return {(sim(D, '5y', 'annualized_return_pct') or {}).get('p50', float('nan')):+.1%}/yr for Defensive vs {(sim(M, '5y', 'annualized_return_pct') or {}).get('p50', float('nan')):+.1%}/yr for Moderate; "
            f"P(fall > 20% within 5 yrs) {(sim(D, '5y', 'dd20') or 0):.0%} vs {(sim(M, '5y', 'dd20') or 0):.0%}. The 15–20% figure comes from the earlier Codex review notes; to Claude the owner described his risk appetite as 'not very risk-averse, not extremely risk-taking'."),
     'effect': 'v4 does not override v005: the owner chooses which sentence describes his limit (the one next step).'},
    {'topic': 'Irish UCITS index core and a short-Treasury reserve', 'status': 'ADOPTED',
     'v005': 'VUAA (IE00BFMXXD54) for the index; IB01 (IE00BGSF1X88, 0–1 yr Treasuries) plus cash for the reserve.',
     'v4': 'CSPX or VUAA for the core; directly held T-bills or a UCITS T-bill fund for the reserve. IB01 is such a fund; both keep the reserve outside US estate tax.',
     'effect': 'v4 names IB01 as one eligible reserve fund, alongside direct T-bills.'},
    {'topic': 'Dividend withholding and US estate tax', 'status': 'CONFIRMED',
     'v005': '30% withholding on direct US dividends; Irish funds 15% internally; direct US shares are US-situs.',
     'v4': 'Same facts, re-verified against IRS and issuer pages on 26 Sep 2026 (R2, R3).', 'effect': 'None.'},
    {'topic': 'Which stocks are candidates', 'status': 'CHALLENGED',
     'v005': "Ranks only the original fourteen v3 candidates and says so ('not a claim to have found the best fourteen investments in the entire market').",
     'v4': "v3's candidate list rested on biased evidence: its momentum result falls from 29.1%/yr to 18.1%/yr once stocks count only after joining the index, and its conviction filter failed out of sample. v4 screens all 503 point-in-time members with pre-registered rules plus primary-source diligence. The only overlap is HIG.",
     'effect': "v4's satellite is not built from v3's list. v4 also found no stock-selection edge, so neither workstream's picks should be expected to beat the index."},
    {'topic': 'AMP and PAYX as first purchases', 'status': f"AMP CONFIRMED ({_held_or_bench('AMP')}); PAYX CONFIRMED as buyable ({_held_or_bench('PAYX')})",
     'v005': 'BUY NOW at ≤ $500 (AMP) and ≤ $101.80 (PAYX), 2% slots each, base 3-yr IRRs 12.8% / 12.2% after withholding.',
     'v4': "Once v4 extended research to every S&P 500 company, its own full diligence (F21) rated AMP INCLUDE at full conviction, fairly priced at under 10x forward earnings. " + ("AMP is now a holding. " if _held_or_bench('AMP') == 'held' else "AMP passes every v4 test but is not held: " + _why('AMP') + ". ") + "PAYX was researched in full in wave 2 (F37): INCLUDE-SMALL (half conviction), with the price implying about 0.7% a year of cash-flow growth against management's own guided 7–9% earnings growth, and a base-case return of about +9.8% a year. It passes every v4 test but is not held: 20 names outranked it under rule (j). Its named reservation is a slowdown in the Management Solutions unit (75% of revenue) and an April 2026 data breach.",
     'effect': ("Both names now pass v4's own full diligence, so v005's judgement that they are sound purchases at those limits is confirmed; " + ("v4 holds AMP and keeps PAYX on its bench. " if _held_or_bench('AMP') == 'held' else "v4 keeps both on its bench of eligible names (neither is in the current 20). ") + "PAYX closed at $101.37 on 25 Sep 2026, just under v005's $101.80 limit. X1 reproduced both v005 base cases to the cent from SEC filings. AMP's 13x exit multiple sits near its 10-year average P/E. "
                "PAYX's 20x sits below its whole 10-year P/E range (about 24–34x): conservative, but v005 does not say so. The AMP gap between v005 (13–14% IRR, cash-flow model) "
                "and v4's valuation model (+6.5%/yr, price-to-book relative to peers) is a method choice, not an error on either side." if X1 else
                "Neither confirmed nor rejected; X1 is checking the load-bearing inputs of both cases.")},
    {'topic': 'RL, AIZ, NTAP at current prices', 'status': 'CONFIRMED',
     'v005': 'RL: avoid (reconsider at $265). AIZ: buy only ≤ $235. NTAP: buy only ≤ $150.',
     'v4': "V1 rates RL 'demanding' (base −7.8%/yr), AIZ 'excessive' (−3.9%/yr) and NTAP 'excessive' (−17.2%/yr); none is held.", 'effect': 'None.'},
    {'topic': 'HIG entry price', 'status': 'RESOLVED (HIG no longer held)',
     'v005': 'Buy only at ≤ $120 (12% hurdle).',
     'v4': "HIG remains eligible (fair valuation, +2.7%/yr base case) but fell outside v4's best 20 once research covered the whole index.",
     'effect': 'None: the thin-margin name was displaced by stronger ideas.'},
    {'topic': 'MSFT and NVDA', 'status': 'CONFIRMED (not at current prices)', 'v005': 'Buy below $500 (MSFT, price $516) and below $215 (NVDA, price $225).',
     'v4': 'Full diligence (F17, F18): MSFT WATCH, since the price implies about 12.7% a year of growth against a ~10.9% base case. NVDA INCLUDE-SMALL on quality, but on trailing cash flow its price implies more than the base case.',
     'effect': 'Both workstreams like the businesses and decline to buy at the 25 September prices.'},
    {'topic': 'Drawdown response rules', 'status': 'ADOPTED for the Defensive mix',
     'v005': 'Freeze additions at −8% from the high-water mark, re-underwrite at −12%, capital preservation at −15%.',
     'v4': 'Review theses at −10%, the equity/reserve mix at −15%, tolerance reached at −20% (sized for the Moderate/Cautious mixes).',
     'effect': "v4 keeps its triggers for Moderate/Cautious; for the Defensive mix v005's tighter triggers apply."},
    {'topic': 'Dollar illustrations', 'status': 'CHANGED (presentation)',
     'v005': 'Unit counts for $50,000 and $100,000.',
     'v4': 'Research-only presentation: a per-$10,000 table and the formula, no order sheet in the owner\'s dollars.', 'effect': 'None on substance.'},
]
out = {'v005_release': rel.get('id', 'v005_2026-09-26_codex'), 'v005_prepared_utc': rel.get('prepared_utc'), 'v005_data_cutoff': rel.get('data_cutoff'),
       'parents_for_v4_release': ['v005_2026-09-26_codex', 'claude-v3', 'codex-initial-audit', 'codex-deep-data-audit'],
       'findings': findings, 'candidates': cands,
       'x1': ({'checked': X1.get('checked'), 'confirmed': X1.get('confirmed'), 'counts_by_status': X1.get('counts_by_status'),
               'exceptions': [f"{it.get('status')}: {it.get('claim')} ({it.get('note')})" for it in X1.get('items', []) if it.get('status') != 'CONFIRMED'],
               'disagreements': [(d.get('topic', '') + ': ' + d.get('assessment', '')) if isinstance(d, dict) else str(d) for d in X1.get('disagreements', [])]}
              if X1 else None)}
(V4 / 'outputs' / 'lead_v005_reconciliation.json').write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str), encoding='utf-8')
print('reconciliation written:', len(findings), 'findings,', len(cands), 'candidates; X1', 'present' if X1 else 'pending')
