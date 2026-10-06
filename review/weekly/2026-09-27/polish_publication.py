from pathlib import Path
P=Path('review/ready');W=Path('review/weekly/2026-09-27')
f=P/'publish_dashboard.py';s=f.read_text(encoding='utf-8');s=s.replace('<summary>Detailed normalization, source tables and catalysts</summary>', '<summary>September 26 baseline normalization, source tables and catalysts</summary><p class="sm mute">These preserved company memoranda contain older price references. Use the current table and September 27 weekly memo for prices, actions, events and limits.</p>');s=s.replace('<summary>Weekly buy, hold, reduce and sell policy</summary>','<summary>Weekly policy — effective September 26; reviewed unchanged September 27</summary>');f.write_text(s,encoding='utf-8')
f=W/'build_weekly_report.py';s=f.read_text(encoding='utf-8');marker="(W/'WEEKLY_REVIEW.md').write_text(text,encoding='utf-8')"
insertion=r'''# Keep prose readable without changing URLs, filenames or version identifiers.
import re
parts=re.split(r'(\[[^\]]*\]\([^)]*\)|`[^`]*`)',text)
for idx,part in enumerate(parts):
    if idx%2: continue
    part=re.sub(r'(?<!\bv)(?<=[a-z])(?=\d)', ' ', part)
    part=re.sub(r'(?<=%)(?=[A-Za-z\d])', ' ', part)
    part=re.sub(r'(?<=[A-Za-z])(?=\$)', ' ', part)
    for ticker in ['MSFT','NVDA','ALLE','HIG','AMP','PAYX','NTAP']:
        part=re.sub(r'\b'+ticker+r'(?=\d)',ticker+' $',part)
    parts[idx]=part
text=''.join(parts)
'''
assert marker in s;s=s.replace(marker,insertion+'\n'+marker);f.write_text(s,encoding='utf-8')
print('Publication clarity labels updated.')
