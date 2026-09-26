"""Sensitivity only. Stored inputs are unverified; outputs are not recommendations."""
from pathlib import Path
import pandas as pd, numpy as np, json
p=Path('source_bundle/equity_project'); out=Path('review/agents')
x=pd.read_pickle(p/'conv.pkl').set_index('t'); info=json.loads((p/'info.json').read_text())
port=json.loads((p/'conv_port.json').read_text()); w=pd.Series(port['w'])
x['beta_adjusted_assumed']=np.clip(.67*x.beta3+.33,.6,1.6)
x['prior_assumed_rf4_erp4']=.04+.04*x.beta_adjusted_assumed
# Preserve original analyst-growth haircut and 3-year rerating, solely to isolate accounting defects.
x['bb_ex_buyback_diagnostic']=(x.dy+x.bb_growth+x.bb_rerate).clip(-.3,.4)
# Uniform method count; scenario removed because flawed and available only for 100/497.
x['return_diagnostic']=.25*x.bb_ex_buyback_diagnostic+.75*x.prior_assumed_rf4_erp4
x['change_vs_original_pp']=100*(x.return_diagnostic-x.E_cons)
x['scenario_coverage_original']=x.E_scen.notna()
def route(r):
    if r.sector=='Real Estate': return 'Real estate: AFFO, LTV, debt maturities required'
    if r.sector!='Financials': return 'Operating company'
    if r['sub']=='Transaction & Payment Processing Services': return 'Operating company'
    if 'Insurance' in r['sub'] and 'Brokers' not in r['sub']: return 'Insurance: capital, reserves, underwriting required'
    if 'Banks' in r['sub'] and 'Asset Management' not in r['sub']: return 'Bank: CET1, liquidity, credit losses required'
    return 'Financial services: business-specific capital and liquidity review required'
x['balance_route']=x.apply(route,axis=1)
def nd(t):
    d=info.get(t,{})
    debt,cash,eb=[d.get(n) for n in ['totalDebt','totalCash','ebitda']]
    if any(v is None for v in [debt,cash,eb]) or eb<=0: return np.nan
    return (debt-cash)/eb
x['nd_ebitda_missing_not_zero']=[nd(t) for t in x.index]
x['balance_status']='UNKNOWN: specialist balance-sheet verification required'
oper=x.balance_route.eq('Operating company'); has=x.nd_ebitda_missing_not_zero.notna()
x.loc[oper&has,'balance_status']=np.where(x.loc[oper&has,'nd_ebitda_missing_not_zero']<=2.5,'PASS provisional 2.5x screen','FAIL provisional 2.5x screen')
x.loc[oper&~has,'balance_status']='UNKNOWN: missing leverage inputs'
x['guidance_status']=np.where(x.cuts4.isna(),'UNKNOWN: no machine-read record',np.where(x.cuts4>0,'FLAG: machine-read cut','PROVISIONAL: no machine-read cut; not verified'))
x['original_stability']=x.stab
x['valuation_sanity_diagnostic']=(x.fpe>0)&((x.pe_rel<=1.35)|((x.fpe/(x.g.clip(lower=.01)*100))<=1.5))&(x.bb_ex_buyback_diagnostic>=.06)
x['diagnostic_quality_gate']=x['L_Quality (Buffett)']
x['diagnostic_risk_gate']=x['L_Risk']
x['diagnostic_complete_operating_candidate']=oper&x.balance_status.eq('PASS provisional 2.5x screen')&x.diagnostic_quality_gate&x.diagnostic_risk_gate&x.valuation_sanity_diagnostic&~x.vetoed
x['evidence_status']='UNVERIFIED STORED DATA: sensitivity only; not an investable ranking'
cols=['name','sector','sub','price','fpe','beta_adjusted_assumed','prior_assumed_rf4_erp4','dy','nby','g','bb_growth','bb_rerate','E_bb','bb_ex_buyback_diagnostic','E_cons','return_diagnostic','change_vs_original_pp','scenario_coverage_original','nd_ebitda','nd_ebitda_missing_not_zero','balance_route','balance_status','guidance_status','original_stability','passes','valuation_sanity_diagnostic','diagnostic_quality_gate','diagnostic_risk_gate','diagnostic_complete_operating_candidate','evidence_status']
x[cols].sort_index().to_csv(out/'01_universe_497_diagnostics.csv',index_label='ticker')
y=x.loc[w.index,cols].copy(); y.insert(0,'original_weight',w); y.to_csv(out/'01_original_14_comparison.csv',index_label='ticker')
summary={'original14_weighted_return':float(w@x.loc[w.index,'E_cons']/w.sum()),'diagnostic_original14_weighted_return':float(w@x.loc[w.index,'return_diagnostic']/w.sum()),'rf_assumption':.04,'erp_assumption':.04,'qualified_operating_candidates_before_primary_verification':int(x.diagnostic_complete_operating_candidate.sum()),'notes':['No current prices or filings validated by this script.','Growth, fair multiple and rerating remain unvalidated original assumptions.','Original scenarios removed; zero alpha assumed; no missing beta imputation.','No robustness resimulation or portfolio selection performed.','Bank/insurance/broker capital adequacy is unknown, not passed based on ROE.']}
(out/'01_diagnostic_summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2));print(y[['E_cons','return_diagnostic','balance_status']].to_string())
