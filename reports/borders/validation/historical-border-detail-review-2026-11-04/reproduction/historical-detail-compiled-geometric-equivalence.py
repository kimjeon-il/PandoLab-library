import json
from osgeo import ogr
ogr.UseExceptions();base='build-native/territorial-recipe/'
d=json.load(open(base+'historical-detail-active-composites.json',encoding='utf-8-sig'));rows=[]
for c in d['countries']:
 if c['entityId'] not in ['state:soviet-union','state:soviet-union-russian-sfsr','IRN']:continue
 sid=c['entityId'] if ':' in c['entityId'] else 'state:'+c['entityId'];source=json.load(open('assets/data/territorial-entities/source/countries/'+sid.replace(':','-')+'.json',encoding='utf-8-sig'))
 for r in c['records']:
  for b in r['coverage']:
   v=next(v for v in source['geometryVersions'] if v['versionId']==b['sourceVersionId']);a=ogr.CreateGeometryFromJson(json.dumps(v['geometry']));p=ogr.CreateGeometryFromJson(json.dumps(r['geometry']));delta=a.SymDifference(p)
   row={'entityId':c['entityId'],'versionId':v['versionId'],'compiledGeometryRef':r['geometryRef'],'symmetricDifferenceSquareDegrees':delta.GetArea(),'nativeBoundaryMissingFromCompiledLengthDegrees':a.Boundary().Difference(p.Boundary()).Length(),'compiledBoundaryOutsideNativeLengthDegrees':p.Boundary().Difference(a.Boundary()).Length()};rows.append(row);print(json.dumps(row),flush=True)
json.dump({'scope':'Only selected composite versions with different canonical digests; technical geometric equivalence, not historical accuracy','rows':rows},open(base+'historical-detail-compiled-geometric-equivalence.json','w'),indent=2)
