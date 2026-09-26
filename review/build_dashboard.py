from pathlib import Path
import json, csv, re, html

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'source_bundle' / 'equity_project'

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def inline(text):
    text = html.escape(text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text

def md(text):
    lines = text.splitlines(); result=[]; i=0
    while i < len(lines):
        line=lines[i].strip()
        if not line: i+=1; continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=lines[i].strip().strip('|').split('|')
                if not all(re.fullmatch(r'[\s:\-]+',c) for c in cells): rows.append(cells)
                i+=1
            result.append('<div class="scroll"><table>'+''.join('<tr>'+''.join(f'<{"th" if k==0 else "td"}>{inline(c.strip())}</{"th" if k==0 else "td"}>' for c in row)+'</tr>' for k,row in enumerate(rows))+'</table></div>'); continue
        heading=re.match(r'^(#{1,6})\s+(.*)',line)
        if heading:
            level=min(len(heading[1])+1,4);result.append(f'<h{level}>{inline(heading[2])}</h{level}>');i+=1;continue
        if line.startswith('- ') or re.match(r'^\d+\. ',line):
            items=[]
            while i<len(lines) and (lines[i].strip().startswith('- ') or re.match(r'^\d+\. ',lines[i].strip())):
                items.append('<li>'+inline(re.sub(r'^(?:- |\d+\. )','',lines[i].strip()))+'</li>');i+=1
            result.append('<ul>'+''.join(items)+'</ul>');continue
        if line.startswith('```'):
            block=[];i+=1
            while i<len(lines) and not lines[i].startswith('```'):block.append(lines[i]);i+=1
            result.append('<pre>'+html.escape('\n'.join(block))+'</pre>');i+=1;continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#|\||- |\d+\. |```)',lines[i].strip()):para.append(lines[i].strip());i+=1
        result.append('<p>'+inline(' '.join(para))+'</p>')
    return '<article class="review-prose">'+''.join(result)+'</article>'

reports=[]
for file in sorted((ROOT/'agents').glob('0[1-6]_*.md')):
    reports.append({'name':file.stem.replace('_',' '),'html':md(file.read_text(encoding='utf-8-sig'))})
with (ROOT/'data/universe_data_ledger_497.csv').open(encoding='utf-8-sig') as f: ledger=list(csv.DictReader(f))
with (ROOT/'agents/01_universe_497_diagnostics.csv').open(encoding='utf-8-sig') as f: diagnostics=list(csv.DictReader(f))
with (ROOT/'data/risk_sensitivity.csv').open(encoding='utf-8-sig') as f: sensitivity=list(csv.DictReader(f))
underwriting_path=ROOT/'agents/04_underwriting.json'
underwriting=read_json(underwriting_path) if underwriting_path.exists() else []
content={
    'memo':md((ROOT/'INVESTMENT_COMMITTEE_REVIEW.md').read_text(encoding='utf-8-sig')),
    'policy':md((ROOT/'WEEKLY_INVESTMENT_POLICY.md').read_text(encoding='utf-8-sig')),
    'reports':reports,'ledger':ledger,'diagnostics':diagnostics,'sensitivity':sensitivity,
    'market':read_json(ROOT/'agents/02_market_data.json'),'risk':read_json(ROOT/'data/risk_audit.json'),
    'diagnosticSummary':read_json(ROOT/'agents/01_diagnostic_summary.json'),
    'underwriting':underwriting,
    'deepMemo':md((ROOT/'DEEP_DATA_AUDIT.md').read_text(encoding='utf-8')),
    'deepReports':[{'name':f.stem.replace('_',' '),'html':md(f.read_text(encoding='utf-8'))} for f in sorted((ROOT/'deep_audit').glob('0[1-4]_*audit.md'))]+[{'name':'04 closure review','html':md((ROOT/'deep_audit/04_closure_review.md').read_text(encoding='utf-8'))}],
    'filingRows':read_json(ROOT/'deep_audit/01_filing_ledger.json')['rows'],
    'regime':read_json(ROOT/'deep_audit/reports/03_druckenmiller_readiness.json'),
}

js=r'''
const REVIEW=__REVIEW_DATA__;
const reviewKeys=new Set(['review','facts','risklab','weekly','ledger','repairs','committee','deepaudit','sourcegate']);
TABS.forEach(t=>t[1]='Archive · '+t[1].replace('★ ',''));
TABS.unshift(['review','Decision brief'],['deepaudit','Three deep data audits'],['sourcegate','Sources & regime gates'],['facts','14 company checks'],['risklab','Risk & capital'],['weekly','Weekly desk'],['ledger','497 evidence rows'],['repairs','Method repairs'],['committee','Original six reviews']);
const safe=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const money=v=>'$'+Math.round(v).toLocaleString('en-US');
const pct4=v=>(100*Number(v)).toFixed(1)+'%';
const badge=(s,c='warn')=>`<span class="tag ${c}">${safe(s)}</span>`;
const title=(eyebrow,h,desc)=>`<p class="eyebrow">${eyebrow}</p><h1>${h}</h1><p class="lede">${desc}</p>`;
const briefFacts=[
 ['36.2%','Daily historical replay drawdown','Compared with your 15–20% tolerance. Retrospective replay, not a track record.'],
 ['95%','Maximum feasible investment','The original selected names cannot absorb 100% under the stated caps.'],
 ['3','Additional deep data audits','Filing tables, market/forecast data, and historical lineage; plus a closing challenge.'],
 ['497','Rows reconciled and reworked','Internal data checks and corrected diagnostics; not 497 external audits.']
];
R.review=()=>{
 $('#app').innerHTML=title('INDEPENDENT REVIEW · 26 SEP 2026 · SNAPSHOT 24 SEP','Useful research. Not ready for capital.','Do not deploy the original 14-stock allocation on its current evidence. Replace the confidence score with verified inputs, coherent valuation and a portfolio risk budget.')+
 `<div class="tally">${briefFacts.map(([v,l,d])=>`<div><b>${v}</b><strong>${l}</strong><p class="sm mute">${d}</p></div>`).join('')}</div>
 <div class="grid"><div class="card hi"><h3>Your revised mandate</h3><p>$50,000–$100,000 · weekly buy/hold/sell review · flexible holding period · 15–20% tolerable decline.</p><p class="sm mute">The holding period follows the thesis. Weekly review is a decision cadence, not a one-week return forecast.</p></div><div class="card"><h3>Current recommendation status</h3><p class="bad"><b>Original allocation: do not implement from this review.</b></p><p>14 candidates: WATCH / re-underwrite. Existing holdings: unknown. No personalized sell instructions or orders.</p></div></div>
 <div class="callout"><b>Deep audit update:</b> 14 closes externally corroborated; 12 missing finalist prices and benchmark repaired; 426 stock gaps remain. Material cash-flow definitions corrected. <a href="#" onclick="go('deepaudit');return false">Read the new evidence</a></div><div class="controls" style="margin-top:18px"><button onclick="go('risklab')">Explore the dollar risk</button><button onclick="go('facts')">Inspect all 14 companies</button><button onclick="go('weekly')">Read the weekly rules</button></div>
 <details open><summary>Read the full investment committee memo</summary>${REVIEW.memo}</details>`;
};
R.facts=()=>{
 const U=REVIEW.underwriting; const ur=Array.isArray(U)?U:(U.rows||U.companies||[]);const lookup=Object.fromEntries(ur.map(x=>[x.ticker,x]));
 $('#app').innerHTML=title('REPORTED FACTS ≠ FORECASTS','The 14 finalists, re-examined','All 14 September 24 closes are externally corroborated; NVDA and MSFT also match authenticated FMP responses. Original forecast vintages and investment values remain unresolved. These are historical snapshots, not order prices.')+
 `<div class="callout"><b>New filing corrections:</b> NVDA TTM conventional FCF $127.006bn; MSFT FY2026 $66.987bn. Airbnb Q2 FCF $1.253bn supports the rounded $1.3bn/35% claim. Detailed source/definition checks are in Three deep data audits.</div><div class="callout">NVIDIA: 14.32× next fiscal year versus 24.13× current fiscal year. Microsoft: 21.03× versus 25.20×. A lower P/E can reflect a more distant earnings forecast.</div>
 <div class="scroll"><table><thead><tr><th>Company</th><th>Saved price</th><th>Vendor fwd P/E</th><th>Current-FY P/E</th><th>Release date</th><th>Evidence status</th></tr></thead><tbody>${REVIEW.market.rows.map(x=>`<tr><td><a href="#co-${x.ticker}"><b>${x.ticker}</b></a></td><td>${usd(x.price_vendor)}</td><td>${n(x.forward_pe_vendor,2)}×</td><td>${n(x.current_fy_pe_computed,2)}×</td><td>${x.latest_cached_sec_date}</td><td>Close corroborated; underwriting incomplete</td></tr>`).join('')}</tbody></table></div>
 <div class="grid">${REVIEW.market.rows.map(x=>{const q=lookup[x.ticker]||{};return `<div class="card" id="co-${x.ticker}"><h3>${x.ticker} ${badge('WATCH')}</h3>${['thesis','bear_case','valuation_method','must_verify','invalidation_trigger'].filter(k=>q[k]).map(k=>`<h4>${({thesis:'Investment case',bear_case:'Countercase',valuation_method:'Valuation approach',must_verify:'Evidence still needed',invalidation_trigger:'Thesis failure to watch'})[k]}</h4><p class="sm">${safe(Array.isArray(q[k])?q[k].join('; '):q[k])}</p>`).join('')}<p class="sm mute">No approved entry price or target weight. Snapshot close corroborated; original consensus vintage unresolved. Earlier dossier accounting ambiguities are superseded by the deep filing audit.</p><p class="sm"><a href="${safe(x.latest_cached_sec_url)}" target="_blank" rel="noopener">Cached SEC document</a></p></div>`}).join('')}</div>
 <details><summary>Full primary-source checks, accounting definitions and sources</summary>${REVIEW.reports.find(x=>x.name.startsWith('02'))?.html||''}</details>
 <details><summary>Company investment cases, countercases and candidates to reconsider</summary>${REVIEW.reports.find(x=>x.name.startsWith('04'))?.html||''}</details>`;
};
R.risklab=()=>{
 $('#app').innerHTML=title('LOSS BUDGET · NOT A LOSS GUARANTEE','What the risk means in dollars','A 50% index / 50% stock blend remains 100% equity. A liquidity reserve changes the amount exposed to an equity shock.')+
 `<div class="grid"><div class="card hi"><h3>Capital and equity stress</h3><label>Capital <input id="capital" type="range" min="50000" max="100000" step="5000" value="100000"></label><p id="capitalValue"></p><label>Equity allocation <input id="equity" type="range" min="0" max="100" step="5" value="30"></label><p id="equityValue"></p><p class="sm mute">Default 30% is a conservative design illustration. No reserve instrument or equity purchase is approved here.</p></div><div class="card"><h3>Deterministic stress results</h3><div id="stressTable"></div><p class="sm mute">Reserve assumed unchanged; excludes fees, tax, currency and reserve losses. Outcomes can be worse. These scenarios have no assigned probabilities.</p></div></div>
 <h2>The original replay understates intramonth pain</h2><div class="grid"><div class="card"><h3>Month-end drawdown</h3><b class="bigbad">26.18%</b><p>Reported month-end observations.</p></div><div class="card"><h3>Daily path, monthly rebalancing</h3><b class="bigbad">36.15%</b><p>20 February–23 March 2020; endpoint wealth reconciles to the original.</p></div></div><p class="mute sm">Today's selected names replayed backward; Airbnb is treated as zero-return cash before listing. This is not historical performance of a strategy selected at the time.</p>
 <h2>How assumed returns produce the profit odds</h2><p class="mute">Same 50/50 blend, 20,000 paths, 3-month blocks, 60 months. Change only the assumed annual blend drift. These reproduce a flawed original model to expose sensitivity.</p><div class="scroll"><table><thead><tr><th>Assumed annual blend return</th><th>Conditional 5-year profit probability</th><th>Meaning</th></tr></thead><tbody>${REVIEW.sensitivity.filter(x=>x.portfolio==='50_50'&&Number(x.block_months)===3).map(x=>`<tr><td>${pct4(x.assumed_annual_return)}</td><td>${pct4(x.p_positive)}</td><td>Model output; not calibrated real-world odds</td></tr>`).join('')}</tbody></table></div>
 <h2>Allocation constraints failed</h2><div class="scroll"><table><thead><tr><th>Sector</th><th>Actual weight</th><th>Stated ceiling</th></tr></thead><tbody>${Object.entries(REVIEW.risk.sector_weights).map(([s,w])=>`<tr><td>${safe(s)}</td><td class="${w>.25?'bad':''}">${pct4(w)}</td><td>25.0%</td></tr>`).join('')}</tbody></table></div><p>Two consumer stocks × 10% + three other sectors × 25% = 95% maximum capacity. A valid construction must allow cash, broaden eligible names, or explicitly change constraints.</p>
 <details><summary>Full independent replication and sensitivity report</summary>${REVIEW.reports.find(x=>x.name.startsWith('03'))?.html||''}</details>`;
 const update=()=>{const cap=Number($('#capital').value),eq=Number($('#equity').value)/100;$('#capitalValue').textContent=money(cap);$('#equityValue').textContent=pct4(eq)+' equities / '+pct4(1-eq)+' reserve';$('#stressTable').innerHTML='<table><tr><th>Equity shock</th><th>Portfolio loss</th><th>Dollar loss</th></tr>'+[.3,.4,.5,.6].map(s=>`<tr><td>−${pct4(s)}</td><td class="${s*eq>.20?'bad':s*eq>.15?'warn':''}">−${pct4(s*eq)}</td><td>−${money(cap*s*eq)}</td></tr>`).join('')+'</table>';};$('#capital').oninput=update;$('#equity').oninput=update;update();
};
R.weekly=()=>{
 $('#app').innerHTML=title('WEEKLY DECISION DESK','Refresh the evidence. Then decide.','Weekly review is scheduled for Sunday 18:00 Dubai. A scheduled research report does not place trades or provide daily risk monitoring.')+
 `<div class="callout"><b>Current action list:</b> all 14 names WATCH / re-underwrite. No verified holdings supplied: personalized HOLD / REDUCE / SELL unavailable.</div><div class="scroll"><table><thead><tr><th>Name</th><th>Action</th><th>Approved entry</th><th>Approved weight</th><th>Reason</th></tr></thead><tbody>${REVIEW.market.rows.map(x=>`<tr><td>${x.ticker}</td><td>WATCH</td><td>None</td><td>None</td><td>Material valuation / evidence gates incomplete</td></tr>`).join('')}</tbody></table></div>
 <div class="grid"><div class="card"><h3>Weekly report</h3><p>Changed facts → thesis impact → valuation → portfolio risk → action. “No trade” is a legitimate result.</p></div><div class="card"><h3>One next step</h3><p>Provide current holdings and cash across accounts. That enables portfolio-specific decisions instead of candidate research alone.</p></div></div>
 ${REVIEW.policy}`;
};
R.ledger=()=>{
 $('#app').innerHTML=title('COVERAGE WITHOUT FALSE CERTAINTY','497 rows, with evidence limits','All saved quote dates are 24 September 2026. Fourteen closing prices now have external corroboration; full exchange-feed history and original consensus vintages remain uncertified.')+
 `<div class="controls"><input id="findStock" type="search" placeholder="Search ticker, company or sector" aria-label="Search 497 companies"><span id="rowCount"></span><a href="data/universe_data_ledger_497.csv" download>Download evidence CSV</a><a href="agents/01_universe_497_diagnostics.csv" download>Download corrected diagnostics</a></div><div class="scroll"><table><thead><tr><th>Stock</th><th>Company</th><th>Sector</th><th>Saved price</th><th>Forward P/E</th><th>Original rank</th><th>Price evidence</th><th>Forecast evidence</th></tr></thead><tbody id="ledgerRows"></tbody></table></div>`;
 const fill=()=>{const q=$('#findStock').value.toLowerCase();const rows=REVIEW.ledger.filter(x=>[x.ticker,x.company,x.sector].join(' ').toLowerCase().includes(q));$('#rowCount').textContent=rows.length+' companies';$('#ledgerRows').innerHTML=rows.map(x=>`<tr><td><b>${safe(x.ticker)}</b></td><td>${safe(x.company)}</td><td>${safe(x.sector)}</td><td>${usd(Number(x.vendor_price))}</td><td>${x.vendor_forward_pe?n(Number(x.vendor_forward_pe),2)+'×':'Unknown'}</td><td>${x.prior_screen_rank} · legacy</td><td>${safe(x.quote_external_status)}</td><td class="warn">${safe(x.consensus_external_status)}</td></tr>`).join('');};$('#findStock').oninput=fill;fill();
};
R.repairs=()=>{
 $('#app').innerHTML=title('REPAIRS AND RELEASE GATES','A score cannot replace an investment case.','The corrected 497-stock computation is a diagnostic, not an approved ranking. It retains unverified input assumptions and earns no stock an automatic buy.')+
 `<div class="grid"><div class="card hi"><h3>11.36% → 9.57%</h3><p>Original-weight illustrative return output after removing repurchase double count, unsupported alpha and flawed scenario averaging, and changing the assumed market prior.</p><p class="bad sm">Neither figure is a validated forecast. Assumed Rf 4%, ERP 4%; inherited growth and rerating assumptions remain.</p></div><div class="card"><h3>Use six gates</h3><p>Source reliability · coherent valuation · company underwriting · unseen-data validation · feasible portfolio controls · implementation suitability.</p><p>A failed material gate prevents deployment even if the aggregate score is high.</p></div></div>${REVIEW.reports.find(x=>x.name.startsWith('01'))?.html||''}`;
};
R.committee=()=>{
 $('#app').innerHTML=title('INDEPENDENT CHALLENGE AND AUDIT TRAIL','Six original reviews, followed by three deeper data audits.','Separate agents reviewed bounded questions in overlapping groups of three. Shared model and sources limit independence; disagreements and unresolved evidence are retained.')+
 `<div class="callout">These first-pass reports are preserved. Their earlier price-verification gaps and Airbnb ambiguity are superseded by the Three deep data audits tab. Nine specialist agents contributed overall; shared data and model family limit independence.</div><p><a href="INVESTMENT_COMMITTEE_REVIEW.md" download>Full memo</a> · <a href="WEEKLY_INVESTMENT_POLICY.md" download>Weekly policy</a> · <a href="data/source_manifest.json" download>Original file hashes</a> · <a href="data/risk_sensitivity.csv" download>Simulation sensitivities</a></p>
 ${REVIEW.reports.map(x=>`<details><summary>${safe(x.name)}</summary>${x.html}</details>`).join('')}
 <div class="callout">Not completed: independent consensus-feed certification; full two-year narrative underwriting for all 30; survivorship-free walk-forward validation; personalized execution. The 16 original tabs are preserved as an archive and carry their original, disputed claims.</div>`;
};

R.deepaudit=()=>{
 $('#app').innerHTML=title('THREE PARALLEL DATA AUDITS · 26 SEP 2026','Trace the number to its source.','Targeted six-company filing audit · 14-name market audit · 497-company historical lineage audit. Evidence depth improved; investment approval remains withheld.')+
 `<div class="tally"><div><b>33</b><strong>Filing / provider field checks</strong><p class="sm mute">Exact periods, formulas, source locators and quarantines.</p></div><div><b>154</b><strong>Market field observations</strong><p class="sm mute">14 candidates; forecast vintage remains unresolved.</p></div><div><b>593</b><strong>Cached documents inspected</strong><p class="sm mute">Coverage and truncation audited across the cache.</p></div><div><b>12 + 1</b><strong>Missing-day observations recovered</strong><p class="sm mute">Twelve finalists plus benchmark; risk patch provisional for corporate actions.</p></div></div>
 <p><a href="DEEP_DATA_AUDIT.md" download>Download synthesis</a> · <a href="deep_audit/01_filing_ledger.csv" download>Filing evidence CSV</a> · <a href="deep_audit/02_market_ledger.csv" download>Market evidence CSV</a> · <a href="deep_audit/03_document_ledger.csv" download>593-document ledger</a> · <a href="deep_audit/03_finalist_repair_impact.json" download>Before / after calculations</a></p>
 ${REVIEW.deepMemo}
 <h2>Exact field evidence</h2><div class="controls"><input id="findFact" type="search" placeholder="Search ticker, field or status" aria-label="Search filing evidence"><span id="factCount"></span></div><div class="scroll"><table><thead><tr><th>Stock / field</th><th>Period / basis</th><th>Reconciled value / unit</th><th>Formula / locator</th><th>Status</th></tr></thead><tbody id="factRows"></tbody></table></div>
 <h2>Read each audit and the closing challenge</h2>${REVIEW.deepReports.map(x=>`<details><summary>${safe(x.name)}</summary>${x.html}</details>`).join('')}`;
 const fill=()=>{const q=$('#findFact').value.toLowerCase();const rows=REVIEW.filingRows.filter(x=>[x.ticker,x.field,x.status].join(' ').toLowerCase().includes(q));$('#factCount').textContent=rows.length+' field checks';$('#factRows').innerHTML=rows.map(x=>`<tr><td><b>${safe(x.ticker)}</b><br>${safe(x.field)}</td><td>${safe(x.period)}<br><span class="sm mute">${safe(x.basis)}</span></td><td>${safe(x.primary_or_derived_value??'Unknown')}<br>${safe(x.units)}</td><td>${safe(x.formula)}<br><span class="sm mute">${safe(x.locator)}</span></td><td class="${x.quarantine?'bad':'mute'}">${safe(x.status)}</td></tr>`).join('');};$('#findFact').oninput=fill;fill();
};
R.sourcegate=()=>{
 $('#app').innerHTML=title('ACTUAL ACCESS · SHARED LINEAGE · MISSING INPUTS','Provider access and regime readiness','Source documentation, actual observations, independent extraction and investment judgment are different evidence layers.')+
 `<div class="grid"><div class="card hi"><h3>FMP: actual responses acquired</h3><p>NVDA / MSFT September 24 closes and three annual cash-flow rows each. The other 12 price requests returned 402. Bundled AAPL samples were rejected by symbol/date checks.</p><p class="sm mute">NVIDIA full JSON retained. Microsoft selected fields transcribed from Raw UI, explicitly labeled. No credential is included.</p></div><div class="card"><h3>Financial Datasets: connected, credits required</h3><p>The connector is now callable. A direct Microsoft annual cash-flow query returned a $0.00 provider-balance error, so no data was acquired. Earlier reports preserve the initial unavailable-connector state. No credits were purchased.</p><p><a href="https://docs.financialdatasets.ai/data-provenance" target="_blank" rel="noopener">Provider provenance</a></p></div></div>
 <p><a href="deep_audit/00_provider_access_ledger.json" download>Provider access and capture ledger</a> · <a href="deep_audit/raw_filing/manifest.json" download>Archived filing hashes</a> · <a href="deep_audit/reports/03_druckenmiller_readiness.json" download>Actual regime runs and readiness</a></p>
 <h2>Requested Druckenmiller framework: incomplete</h2><div class="scroll"><table><thead><tr><th>Required input</th><th>Actual result</th><th>Underlying date</th><th>Status</th></tr></thead><tbody>${REVIEW.regime.required_reports.map(x=>`<tr><td>${safe(({market_breadth:'Market breadth',uptrend_analysis:'Uptrend participation',market_top:'Market-top risk',macro_regime:'Macro regime',ftd_detector:'Follow-through day'})[x.skill]||x.skill)}</td><td>${x.score!=null?safe(x.score)+'/100':'Unavailable'}</td><td>${safe(x.data_date||'None')}</td><td>${x.status==='GENERATED_REAL_DATA'?'Generated; source not independently rebuilt':'Missing required data access'}</td></tr>`).join('')}</tbody></table></div>
 <div class="callout"><b>Combined conviction and allocation withheld.</b> Three required reports could not run. The two generated signals share TraderMonty lineage and are uncalibrated heuristics. The full lineage audit documents unsafe schema defaults, stale-data checks and directional scoring issues. No generic concentration rule overrides your risk tolerance.</div>
 <h2>Weekly release requirements</h2><p>Filing/accounting review → market/forecast review → historical/transformation review. Material failures block new purchases. Require explicit source dates, fiscal definitions, raw hashes and before/after risk effects; preserve conflicts instead of averaging them away.</p><p>Existing holdings require their own thesis and risk assessment. A data outage does not automatically mean sell. Sunday 18:00 Dubai research continues; no daily monitoring or execution is active.</p>`;
};

const previousGo=go;
go=function(k,t){previousGo(k,t);document.getElementById('reviewStatus').textContent=reviewKeys.has(k)?'INDEPENDENT REVIEW · No trade authorization · Source snapshot 24 Sep 2026':'ARCHIVE · Original research contains disputed claims and failed controls. Do not use these legacy weights or probabilities for trading.';};
cur='review';tabs();R[cur]();
'''

extra_css='''
.review-prose{max-width:1120px}.review-prose p{max-width:100ch}.review-prose th,.review-prose td{white-space:normal;min-width:110px;max-width:650px}.review-prose h2{margin-top:36px}.review-prose h3{margin-top:28px}.review-prose h4{margin-top:22px}.review-prose li{margin:8px 0}.review-prose code{overflow-wrap:anywhere;font-size:12px}.review-prose pre{white-space:pre-wrap;overflow-wrap:anywhere}.eyebrow{font-size:11px;letter-spacing:.16em;color:var(--gold);font-weight:600;margin:0 0 14px!important}.tally strong{display:block;font-size:13px;margin-top:8px}.bigbad{font:42px Georgia,serif;color:var(--down)}details{margin:22px 0;border:1px solid var(--line);border-radius:6px;padding:18px;background:var(--panel)}summary{cursor:pointer;color:var(--gold2);font-size:16px;font-weight:600}details[open]>summary{margin-bottom:20px}input[type=range]{width:100%;accent-color:var(--gold);margin-top:12px}#reviewStatus{padding:10px 20px;background:#231d18;color:#e3c98f;border-bottom:1px solid #645039;font-size:12px}#rowCount{align-self:center;color:var(--mute)}#findStock{min-width:290px}#app>.scroll{margin:18px 0}a{overflow-wrap:anywhere}nav .in{max-width:1440px}.wrap{max-width:1360px}.tally{grid-template-columns:repeat(4,1fr)}@media(max-width:760px){.tally{grid-template-columns:repeat(2,1fr)}.grid{grid-template-columns:1fr}details{padding:12px}#findStock{min-width:200px}}@media print{nav,#reviewStatus,.controls{display:none}body{color:#111;background:#fff}.card,details,.scroll,th{background:#fff;color:#111}h1,h2,h3,h4,a{color:#333}.wrap{padding:0}details:not([open]){display:none}}
'''
template=(SOURCE/'dash_tpl_v3.html').read_text(encoding='utf-8')
template=template.replace('<title>The 497-to-10 Equity Audit</title>','<title>Independent investment review · Weekly decision desk</title>')
template=template.replace('__DATA__',json.dumps(read_json(SOURCE/'dash.json'),ensure_ascii=False).replace('</','<\\/'))
template=template.replace('__DATA2__',json.dumps(read_json(SOURCE/'dash2.json'),ensure_ascii=False).replace('</','<\\/'))
template=template.replace('</style>','\n'+extra_css+'\n</style>',1)
template=template.replace('<body>','<body><div id="reviewStatus">INDEPENDENT REVIEW · No trade authorization · Source snapshot 24 Sep 2026</div>',1)
payload=json.dumps(content,ensure_ascii=False,allow_nan=False).replace('</','<\\/')
template=template.replace('</script></body>',js.replace('__REVIEW_DATA__',payload)+'\n</script></body>')
(ROOT/'Investment_Review.html').write_text(template,encoding='utf-8')
print(json.dumps({'output':str(ROOT/'Investment_Review.html'),'bytes':len(template.encode()),'specialist_reports':len(reports),'legacy_tabs':16,'new_tabs':9,'ledger_rows':len(ledger)}))
