import json,pathlib,hashlib
from osgeo import ogr
b=pathlib.Path('D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/complete-ssr-source-candidates');o=b/'fixed-snapshot-period-20261109';index=json.loads((o/'output-index.json').read_text());results=[]
for row in index['files']:
 p=o/row['name'];raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==row['sha256'];x=json.loads(raw);valid=[]
 for g in x['geometries']:
  geo=g['geojson'];geo=geo['geometry'] if geo.get('type')=='Feature' else geo;valid.append(bool(ogr.CreateGeometryFromJson(json.dumps(geo)).IsValid()))
 results.append({'entityId':row['entityId'],'valid':all(valid),'geometryCount':len(valid),'geometryPeriods':[{'validFrom':r['validFrom'],'validTo':r.get('validTo')} for r in x['timelineRecords']['geometryBindings']]})
proof={'countryCount':len(results),'allValid':all(r['valid'] for r in results),'allOutputHashesMatch':True,'results':results};(o/'independent-validity-proof.json').write_text(json.dumps(proof,indent=2));print(json.dumps({'countryCount':len(results),'allValid':proof['allValid']}))

