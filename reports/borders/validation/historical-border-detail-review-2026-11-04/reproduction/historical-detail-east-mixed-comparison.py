import json,hashlib,struct
from pathlib import Path
B=Path('build-native/territorial-recipe');R=B/'east-mask-review-2026-11-05';O=R/'mixed';previous=json.loads((R/'runner-copy-manifest.json').read_text(encoding='utf-8-sig'))
for r in previous:assert hashlib.sha256(Path(r['source']).read_bytes()).hexdigest()==r['sourceSha256']
def fp(g):
 h=hashlib.sha256();h.update(g['type'].encode()+b'\0');ps=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']];h.update(struct.pack('>I',len(ps)))
 for p in ps:
  h.update(struct.pack('>I',len(p)))
  for ring in p:
   h.update(struct.pack('>I',len(ring)))
   for q in ring:h.update(struct.pack('>dd',*q))
 return h.hexdigest()
results=[]
for t in [250,500]:
 mixed=json.loads((O/f'Latvia{t}_Poland250_EastMixed.geojson').read_text(encoding='utf-8-sig'));strong=json.loads((B/f'strong-independent-2026-11-05/Latvia{t}_Poland250_East500.geojson').read_text(encoding='utf-8-sig'));rows=[]
 for a,z in zip(strong['features'],mixed['features']):
  name=a['properties']['entity'];before,after=a['geometry'],z['geometry'];rows.append({'entity':name,'strongFingerprint':fp(before),'mixedFingerprint':fp(after),'identical':before==after});assert (before==after)==(name in ['BY','UA'])
 results.append({'latvia':t,'poland':250,'east':'legacy weak908featurepoints','comparison':rows})
(R/'mixed-comparison.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8');print('mixed geometry fingerprints recorded; BY/UA exact to strong; original five scripts preserved')
