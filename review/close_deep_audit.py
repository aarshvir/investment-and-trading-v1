from pathlib import Path
import json
r=Path('review')
p=r/'DEEP_DATA_AUDIT.md';s=p.read_text(encoding='utf-8')
s=s.replace('The separate repair uses the raw observation consistent with the original cutoff\'s adjustment basis.', 'The separate patch uses the observed raw close. Matching the cutoff endpoint alone does not prove every intervening adjustment; the resulting return and risk diagnostics are provisional until corporate actions through the cutoff are fully reconciled.')
s=s.replace('The skill requires five fresh inputs.', 'The requested skill explicitly says: “Run the required skills first.” Its input requirements list five fresh reports. Source: C:/Users/user/.agents/skills/stanley-druckenmiller-investment/stanley-druckenmiller-investment/SKILL.md, lines 33–59.')
p.write_text(s,encoding='utf-8')
p=r/'INVESTMENT_COMMITTEE_REVIEW.md';s=p.read_text(encoding='utf-8').replace('the original adversarial reviewer is checking this extension','the original adversarial reviewer completed a closing challenge of this extension').replace('weekly endpoint volatility is unchanged.', 'weekly endpoint volatility is unchanged. These repaired-series diagnostics remain provisional pending complete intervening corporate-action alignment.')
p.write_text(s,encoding='utf-8')
p=r/'build_dashboard.py';s=p.read_text(encoding='utf-8')
s=s.replace("${safe(x.skill)}</td><td>${x.score", "${safe(({market_breadth:'Market breadth',uptrend_analysis:'Uptrend participation',market_top:'Market-top risk',macro_regime:'Macro regime',ftd_detector:'Follow-through day'})[x.skill]||x.skill)}</td><td>${x.score")
s=s.replace("${safe(x.status)}</td></tr>`).join('')}</tbody></table></div>\n <div class=\"callout\"><b>Combined", "${x.status==='GENERATED_REAL_DATA'?'Generated; source not independently rebuilt':'Missing required data access'}</td></tr>`).join('')}</tbody></table></div>\n <div class=\"callout\"><b>Combined")
s=s.replace('Missing-day observations repaired', 'Missing-day observations recovered').replace('Twelve finalists plus benchmark; 426 stock gaps remain.', 'Twelve finalists plus benchmark; risk patch provisional for corporate actions.')
p.write_text(s,encoding='utf-8')
p=r/'README.md';s=p.read_text(encoding='utf-8').replace('23 tabs','25 tabs').replace('all23 tabs rendered','First version: all23 tabs rendered')
s += '''

Deep-data extension, 26 September 2026:
- DEEP_DATA_AUDIT.md: integrated three-audit synthesis and source-access boundaries.
- deep_audit/01_filing_audit.md: six-company filings, footnotes, 33 field checks; raw source hashes and selected XBRL contexts.
- deep_audit/02_market_audit.md:14 finalists,154 field observations, explicit fiscal/adjustment/vintage distinctions.
- deep_audit/03_lineage_audit.md:497-stock and593-document data audit; separate provisional missing-day patch; actual regime-skill run evidence.
- deep_audit/04_closure_review.md: independent closing challenge and corrections.
- deep_audit/00_provider_access_ledger.json:actual FMP access outcomes; full download versus transcription distinctions; no credentials.
- data/deep_dashboard_validation.json: additional browser checks and explicit limits.
- data/deep_package_manifest.json: hashes of the extended deliverables.

The first-six-report price-verification statements and Airbnb ambiguity are superseded by the deeper extension. No original source bundle file was changed. Old report/diagnostic inputs remain historical evidence; they must not be presented as freshly validated investment rankings.
'''
p.write_text(s,encoding='utf-8')
print('Closing qualifications and reader-friendly labels added.')
