"""Reproduce domain-year aggregate counts from a private QC01-QC08 Excel workbook.
Uses Python standard library only; does not export licensed Scopus record-level content.
Usage: python reproduce_domain_trends.py /path/to/Quantum_Review_Master.xlsx
"""
import csv, sys, zipfile, xml.etree.ElementTree as ET, re
from pathlib import Path
NS='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
DOMAINS={2:'QC01',3:'QC02',4:'QC03',5:'QC04',6:'QC05',7:'QC06',8:'QC07',9:'QC08'}
def extract(path):
    with zipfile.ZipFile(path) as z:
        strings=[]
        with z.open('xl/sharedStrings.xml') as f:
            for _,el in ET.iterparse(f,events=('end',)):
                if el.tag==NS+'si':
                    strings.append(''.join(t.text or '' for t in el.iter(NS+'t')))
                    el.clear()
        out=[]
        for sheet,domain in DOMAINS.items():
            counts={}; header=None
            with z.open(f'xl/worksheets/sheet{sheet}.xml') as f:
                for _,el in ET.iterparse(f,events=('end',)):
                    if el.tag!=NS+'row':continue
                    cells={}
                    for cell in el.findall(NS+'c'):
                        v=cell.find(NS+'v'); val=v.text if v is not None else ''
                        if cell.get('t')=='s' and val:val=strings[int(val)]
                        cells[re.match(r'[A-Z]+',cell.get('r')).group()]=val
                    if header is None:
                        header=cells
                        if header.get('E')!='Year':raise ValueError(f'Unexpected Year column in sheet {sheet}')
                    else:
                        yr=cells.get('E','').strip()
                        if yr.isdigit():counts[yr]=counts.get(yr,0)+1
                    el.clear()
            for yr,c in sorted(counts.items()):out.append((domain,yr,c))
        return out
if __name__=='__main__':
    if len(sys.argv)!=2:sys.exit('Usage: python reproduce_domain_trends.py INPUT.xlsx')
    data=extract(sys.argv[1]);dest=Path(__file__).with_name('domain_year_counts.csv')
    with dest.open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['domain','publication_year','record_occurrences']);w.writerows(data)
    print(f'Wrote {len(data)} domain-year rows, {sum(row[2] for row in data)} occurrences to {dest}')
