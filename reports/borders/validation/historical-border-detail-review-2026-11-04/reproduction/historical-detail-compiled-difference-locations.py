import json
from osgeo import ogr
ogr.UseExceptions();base='build-native/territorial-recipe/';d=json.load(open(base+'historical-detail-active-composites.json',encoding='utf-8-sig'));rows=[]
for c in d['countries']:
 if c['entityId'] not in ['state:soviet-union','state:soviet-union-russian-sfsr','IRN']:continue
 sid=c['entityId'] if ':' in c['entityId'] else 'state:'+c['entityId'];source=json.load(open('assets/data/territorial-entities/source/countries/'+sid.replace(':','-')+'.json',encoding='utf-8-sig'))
 for r in c['records']:
  b=r['coverage'][0];v=next(v for v in source['geometryVersions'] if v['versionId']==b['sourceVersionId']);a=ogr.CreateGeometryFromJson(json.dumps(v['geometry']));p=ogr.CreateGeometryFromJson(json.dumps(r['geometry']));delta=a.SymDifference(p)
  if delta.IsEmpty():continue
  rows.append({'entityId':c['entityId'],'versionId':v['versionId'],'envelope':delta.GetEnvelope(),'geometry':json.loads(delta.ExportToJson())});print(json.dumps({'entity':c['entityId'],'bounds':delta.GetEnvelope(),'components':delta.GetGeometryCount()}),flush=True)
json.dump({'status':'Diagnostic source-versus-compiled differences, not new territorial changes or active candidates','rows':rows},open(base+'historical-detail-compiled-difference-locations.json','w'),indent=2)
