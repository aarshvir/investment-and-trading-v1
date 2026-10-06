from pathlib import Path
import re, html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

P=Path(__file__).resolve().parent
pdfmetrics.registerFont(TTFont('Report','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ReportBold','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('Report',normal='Report',bold='ReportBold',italic='Report',boldItalic='ReportBold')
styles=getSampleStyleSheet()
for k in ['Normal','BodyText','Title','Heading1','Heading2','Heading3']:styles[k].fontName='Report';styles[k].textColor=colors.HexColor('#163047')
styles['BodyText'].fontSize=9;styles['BodyText'].leading=13;styles['BodyText'].spaceAfter=8
styles['Title'].fontSize=24;styles['Title'].leading=28;styles['Title'].spaceAfter=18
styles['Heading1'].fontSize=16;styles['Heading1'].leading=20;styles['Heading1'].spaceBefore=16
styles['Heading2'].fontSize=12;styles['Heading2'].leading=16;styles['Heading2'].spaceBefore=12;styles['Heading2'].keepWithNext=True;styles['Heading1'].keepWithNext=True
small=ParagraphStyle('TableCell',parent=styles['BodyText'],fontSize=7,leading=9,spaceAfter=0,wordWrap='CJK')
def inline(s):
    s=html.escape(s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',r'<a href="\2" color="#276C9E">\1</a>',s)
    s=re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)',r'\1',s)
    return s
story=[];lines=(P/'INVESTMENT_DECISION_MEMO.md').read_text(encoding='utf-8').splitlines();i=0
while i<len(lines):
    l=lines[i].strip()
    if not l:i+=1;continue
    if l.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            cells=lines[i].strip().strip('|').split('|')
            if not all(re.fullmatch(r'[\s:\-]+',c) for c in cells):rows.append([Paragraph(inline(c.strip()),small) for c in cells])
            i+=1
        n=len(rows[0]);widths=[510/n]*n
        if n==9:
            story.append(PageBreak())
            rows=[[Paragraph('Rank / stock',small),Paragraph('Action',small),rows[0][3],rows[0][5],rows[0][6],rows[0][7],rows[0][8]]]+[[Paragraph(r[0].text+' · '+r[1].text,small),Paragraph(r[2].text.replace('AVOID CURRENT PRICE','AVOID'),small),r[3],r[5],r[6],r[7],r[8]] for r in rows[1:]]
            n=7;widths=[48,60,57,63,91,103,50];widths=[w*510/sum(widths) for w in widths]
        if n==9:widths=[25,33,61,56,42,65,77,94,57];widths=[w*510/sum(widths) for w in widths]
        t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E4EDF3')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.8,colors.HexColor('#667F92')),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#CFD8DF')),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
        story.extend([t,Spacer(1,10)]);continue
    heading=re.match(r'^(#{1,3}) (.*)',l)
    if heading:
        style=['Title','Heading1','Heading2'][len(heading[1])-1];story.append(Paragraph(inline(heading[2]),styles[style]));i+=1;continue
    para=[l];i+=1
    while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|')):para.append(lines[i].strip());i+=1
    story.append(Paragraph(inline(' '.join(para)),styles['BodyText']))
def footer(c,d):
    c.setFont('Report',8);c.setFillColor(colors.HexColor('#677B8A'));c.drawString(42,25,'Investment decision memorandum · 27 September 2026 · Conditional research');c.drawRightString(552,25,str(d.page))
doc=SimpleDocTemplate(str(P/'Investment_Decision_Memo.pdf'),pagesize=(594,842),rightMargin=42,leftMargin=42,topMargin=38,bottomMargin=42,title='Investment decision memorandum — 27 September 2026',author='Independent multi-agent research')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print('PDF created', (P/'Investment_Decision_Memo.pdf').stat().st_size)
