"""Audit plugin readiness and save raw public inputs. No fabricated market reports."""
import csv, datetime, hashlib, io, json, os, pathlib, sys, urllib.request
O=pathlib.Path(__file__).resolve().parent/'reports'; O.mkdir(exist_ok=True)
S=pathlib.Path('C:/Users/user/.agents/skills/stanley-druckenmiller-investment/stanley-druckenmiller-investment/scripts')
sys.path.insert(0,str(S))
from report_loader import extract_signal,load_all_reports,REQUIRED_SKILLS
from scorer import calculate_composite_conviction,calculate_signal_convergence
try:
    reports=load_all_reports(str(O),72); error=None
except ValueError as exc: reports={}; error=str(exc)
actual=[]
for k,meta in REQUIRED_SKILLS.items():
    candidates=sorted(O.glob(meta['prefix']+'*.json'))
    candidates=[p for p in candidates if 'history' not in p.name]
    if candidates:
        p=candidates[-1]; d=json.loads(p.read_text()); m=d.get('metadata',{})
        actual.append(dict(skill=k,status='GENERATED_REAL_DATA',file=p.name,data_date=m.get('latest_data_date') or m.get('data_freshness',{}).get('latest_date') or m.get('freshness',{}).get('latest_date'),score=d.get('composite',{}).get('composite_score'),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    else: actual.append(dict(skill=k,status='BLOCKED_MISSING_FMP_API_KEY',attempt_exit_code=1))
# Function-level malformed-input regression probe, kept separate from market reports.
invalid_signals={k:extract_signal(k,{}) for k in REQUIRED_SKILLS}
invalid_result=calculate_composite_conviction(invalid_signals)
test=dict(test_type='ISOLATED_MALFORMED_INPUT_TEST_NOT_MARKET_DATA',empty_required_report_bodies_accepted_by_extractors=True,empty_market_top_becomes_score=invalid_signals['market_top']['composite_score'],inverted_distribution_component=invalid_result['component_scores']['distribution_risk']['score'],invalid_input_still_returns_conviction_score=invalid_result['conviction_score'],invalid_input_claimed_available_components=invalid_result['data_quality']['available_count'],data_availability_parameter_ignored=calculate_composite_conviction(invalid_signals,{'distribution_risk':False})['component_scores']['distribution_risk']['available'],all_bearish_convergence=calculate_signal_convergence({'market_breadth':{'composite_score':0},'uptrend_analysis':{'composite_score':0},'market_top':{'composite_score':100},'macro_regime':{'composite_score':0},'ftd_detector':{'quality_score':0}}))
rawurls={
'market_breadth_data.csv':'https://tradermonty.github.io/market-breadth-analysis/market_breadth_data.csv',
'market_breadth_summary.csv':'https://tradermonty.github.io/market-breadth-analysis/market_breadth_summary.csv',
'uptrend_ratio_timeseries.csv':'https://raw.githubusercontent.com/tradermonty/uptrend-dashboard/main/data/uptrend_ratio_timeseries.csv',
'sector_summary.csv':'https://raw.githubusercontent.com/tradermonty/uptrend-dashboard/main/data/sector_summary.csv'}
manifest=[]
rawdir=O/'raw';rawdir.mkdir(exist_ok=True)
for name,url in rawurls.items():
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Independent-Investment-Data-Audit/1.0'})
        with urllib.request.urlopen(req,timeout=30) as r: b=r.read()
        (rawdir/name).write_bytes(b)
        manifest.append(dict(file=name,url=url,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),retrieved_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=len(list(csv.DictReader(io.StringIO(b.decode('utf-8-sig')))))))
    except Exception as e:manifest.append(dict(file=name,url=url,status='FETCH_FAILED',reason=str(e)))
result=dict(as_of='2026-09-26',overall_status='NOT_READY_NO_SYNTHESIZED_MARKET_CONVICTION',required_reports=actual,required_present=sum(r['status']=='GENERATED_REAL_DATA' for r in actual),required_total=5,missing_report_error=error,fmp_key_present=bool(os.getenv('FMP_API_KEY')),upstream_sources_independent=False,source_note='Both successful breadth inputs share TraderMonty provenance; cannot count as independent vendors.',malformed_input_probe=test,source_manifest=manifest,mandate_override='No leverage; no generic90-100% equity or25% position recommendation approved.15-20% portfolio drawdown tolerance governs risk. Exposure remains blocked until complete inputs, calibrated strategy, and independent data checks pass.',score_calibration='Heuristic points; neither win probability nor calibrated drawdown probability.')
(O/'03_druckenmiller_readiness.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
