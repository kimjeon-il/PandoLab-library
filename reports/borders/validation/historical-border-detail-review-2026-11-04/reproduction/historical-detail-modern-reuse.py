import json
from osgeo import ogr
ogr.UseExceptions()
ne=json.load(open('assets/data/countries-ne-5.1.1.geojson',encoding='utf-8-sig'));shapes={f['id']:ogr.CreateGeometryFromJson(json.dumps(f['geometry'])) for f in ne['features']}
codes=['ARM','AZE','BLR','EST','GEO','KGZ','LTU','LVA','MDA','TJK','TKM','TLS','UZB','CHN','KOR','PRK','IRN','MNG','RUS']
rows=[]
for code in codes:
 source=json.load(open('assets/data/territorial-entities/source/countries/state-'+code+'.json',encoding='utf-8-sig'))
 for v in source['geometryVersions']:
  if code in ['KOR','PRK'] and '38th' in v['versionId']:continue
  if code=='MNG' and 'reviewed' in v['versionId']:continue
  if code=='RUS' and 'post-soviet' in v['versionId']:continue
  g=ogr.CreateGeometryFromJson(json.dumps(v['geometry']));d=g.SymDifference(shapes[code]);rows.append({'entityId':source['entityId'],'versionId':v['versionId'],'neFeature':code,'topologicallyEqualToNE':bool(g.Equals(shapes[code])),'symmetricDifferenceSquareDegrees':d.GetArea(),'scope':'Selected modern-reuse candidates only; planar technical equivalence, not political/historical verification'})
json.dump(rows,open('build-native/territorial-recipe/historical-detail-modern-reuse.json','w'),ensure_ascii=False,indent=2)
print(json.dumps({'reviewed':len(rows),'zeroDifference':sum(r['symmetricDifferenceSquareDegrees']==0 for r in rows),'different':[r for r in rows if r['symmetricDifferenceSquareDegrees']!=0]}))
