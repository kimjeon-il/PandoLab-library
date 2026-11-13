from historical_detail_membership import *
from historical_detail_line_merge import merged
geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));get=lambda tail:next(v['geometry'] for v in load('assets/data/territorial-entities/source/countries/state-soviet-union-'+tail+'.json')['geometryVersions'] if v['versionId'].endswith('1922-12-30-reviewed-v2'));russia=get('russian-sfsr');ua=get('ukrainian-ssr');tc=get('transcaucasian-sfsr');ne=load('assets/data/countries-ne-5.1.1.geojson');ng={f['id']:f['geometry'] for f in ne['features']};known=Cover(load(base+'historical-detail-line-5.geojson')['geometry']);modernUa=Cover(json.loads(geo(ng['RUS']).Boundary().Intersection(geo(ng['UKR']).Boundary()).ExportToJson()));modernTc=Cover({'type':'MultiPolygon','coordinates':[p for id in ['RUS','GEO','AZE'] for p in ([ng[id]['coordinates']] if ng[id]['type']=='Polygon' else ng[id]['coordinates'])]});out=[]
for name,g,refs in [('ua-ru-current',ua,{'known-main':known,'modern-shared':modernUa}),('tc-ru-current',tc,{'modern-proxy':modernTc})]:
 parts=merged(geo(g).Boundary().Intersection(geo(russia).Boundary()));chunks=[];counts=defaultdict(int)
 for line in parts:
  ps=[list(p[:2]) for p in line.GetPoints()];current=[];role=None
  for a,b in zip(ps,ps[1:]):
   label=next((k for k,c in refs.items() if c.includes(a,b)),'nonmodern-unreviewed');counts[label]+=1
   if label!=role:
    if len(current)>1:chunks.append({'role':role,'coordinates':current})
    current=[a];role=label
   current.append(b)
  if len(current)>1:chunks.append({'role':role,'coordinates':current})
 out.append({'id':name,'sharedComponents':len(parts),'counts':dict(counts),'chunks':chunks});print(name,dict(counts),'unreviewed',[(len(r['coordinates']),min(p[0] for p in r['coordinates']),max(p[0] for p in r['coordinates'])) for r in chunks if r['role']=='nonmodern-unreviewed'],flush=True)
json.dump({'status':'Bounded current adopted shared-line decomposition only. No master restoration or production mutation. Numerical collinear containment epsilon1e-10deg not a display tolerance.','rows':out},open(base+'historical-detail-konotop-tc-current-chains.json','w'),indent=2)
