from historical_detail_membership import *
n=load(base+'historical-detail-country-only-native-candidate.json');c=load(base+'historical-detail-country-only-compiled-candidate.json');geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));rows=[]
for row in c['rows']:
 source=next(r for r in n['rows'] if r['entityId']==row['entityId'])
 for v in row['versions']:
  old=next(x['geometry'] for x in source['before']['geometryVersions'] if x['versionId']==v['versionId']);new=next(x['geometry'] for x in source['after']['geometryVersions'] if x['versionId']==v['versionId']);delta=geo(old).SymDifference(geo(new));a=geo(v['before']);b=geo(v['after']);outside=a.SymDifference(b).Difference(delta.Buffer(1e-10));r={'entityId':row['entityId'],'versionId':v['versionId'],'nativeValid':geo(new).IsValid(),'compiledValid':b.IsValid(),'nativeDeltaDeg2':delta.GetArea(),'compiledDeltaDeg2':a.SymDifference(b).GetArea(),'outsideSourceDeltaDeg2':outside.GetArea(),'outsideEnvelope':outside.GetEnvelope() if not outside.IsEmpty() else None};rows.append(r);print(json.dumps(r),flush=True)
json.dump(rows,open(base+'historical-detail-country-only-topology.json','w'),indent=2)
