import json
from pathlib import Path
P=Path(__file__).parent;x=json.loads((P/'inputs.json').read_text(encoding='utf-8'));c=json.loads((P/'gulf-coast-historical-scope-candidates.geojson').read_text(encoding='utf-8'));checks=json.loads((P/'candidate-checks.json').read_text(encoding='utf-8'))
def edges(g):return {tuple(sorted([tuple(a),tuple(b)])) for p in (g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]) for r in p for a,b in zip(r,r[1:])}
ne=next(f['geometry'] for f in x['ne'] if f['id']=='IRN');neE=edges(ne);peerE=set().union(*(edges(f['geometry']) for f in x['ne'] if f['id']!='IRN'));coast=neE-peerE;south={e for e in coast if max(a[1] for a in e)<32}
for v,f,ch in zip(x['irn']['entity']['geometryVersions'][1:4],c['features'],checks['checks']):ch['oldNEOnlySouthernEdgesBefore']=len(south&edges(v['geometry']));ch['oldNEOnlySouthernEdgesAfter']=len(south&edges(f['geometry']));ch['allNEOnlyEdgesBefore']=len(coast&edges(v['geometry']));ch['allNEOnlyEdgesAfter']=len(coast&edges(f['geometry']));print(ch['oldNEOnlySouthernEdgesBefore'],ch['oldNEOnlySouthernEdgesAfter'],ch['allNEOnlyEdgesBefore'],ch['allNEOnlyEdgesAfter']);assert ch['oldNEOnlySouthernEdgesAfter']==0
checks['visualReview']={'image':'IRN-preparatory-coast-comparison.png','projection':'+proj=laea +lat_0=32 +lon_0=54 +datum=WGS84 +units=m +no_defs','scaleDenominator':10000000,'outputDpi':100,'viewed':True,'finding':'Recognizable national outline; southern coastline modernized and historical northern source retained. No independent historical-position measurement or legal certification.'}
(P/'candidate-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8');assert json.loads((P/'candidate-checks.json').read_text(encoding='utf-8'))==checks
print([(ch['oldNEOnlySouthernEdgesBefore'],ch['oldNEOnlySouthernEdgesAfter']) for ch in checks['checks']])



