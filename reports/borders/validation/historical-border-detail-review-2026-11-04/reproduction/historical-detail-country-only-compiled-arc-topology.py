from historical_detail_membership import *
n=load(base+'historical-detail-country-only-native-candidate.json');c=load(base+'historical-detail-country-only-compiled-arc-candidate.json');geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));out=[]
for row in c['rows']:
 source=next(r for r in n['rows'] if r['entityId']==row['entityId']);old=next(v['geometry'] for v in source['before']['geometryVersions'] if v['versionId']==row['versionId']);new=next(v['geometry'] for v in source['after']['geometryVersions'] if v['versionId']==row['versionId']);delta=geo(old).SymDifference(geo(new));a=geo(row['before']);b=geo(row['after']);outside=a.SymDifference(b).Difference(delta.Buffer(1e-10));r={'entityId':row['entityId'],'versionId':row['versionId'],'valid':b.IsValid(),'outsideSourceDeltaDeg2':outside.GetArea(),'compiledDeltaDeg2':a.SymDifference(b).GetArea()};out.append(r);print(r,flush=True)
json.dump(out,open(base+'historical-detail-country-only-compiled-arc-topology.json','w'),indent=2)
