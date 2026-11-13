from historical_detail_membership import *
d=load(base+'historical-detail-east-candidate.json');raw=load(base+'historical-detail-line-2.geojson');composites=load(base+'historical-detail-active-composites.json');peers=load(base+'historical-detail-east-peers.json');oldLine=ogr.CreateGeometryFromJson(json.dumps({'type':'LineString','coordinates':d['originalChain']}));newLine=ogr.CreateGeometryFromJson(json.dumps({'type':'LineString','coordinates':d['candidateChain']}));rows=[]
for p in peers:
 for g in p['geometries']:
  gg=ogr.CreateGeometryFromJson(json.dumps(g['geojson']));changedShared=[]
  for fi in d['spec']:
   coords=raw['features'][int(fi)]['geometry']['coordinates'];line=ogr.CreateGeometryFromJson(json.dumps({'type':'LineString','coordinates':coords}));inter=line.Intersection(gg.Boundary());
   if inter.Length()>1e-10:changedShared.append({'feature':int(fi),'oldSharedLengthDegrees':inter.Length(),'geometry':json.loads(inter.ExportToJson())})
  row={'entityId':p['entityId'],'geometryId':g['id'],'changedFeatureSharedLines':changedShared,'oldChainBoundaryIntersectionDegrees':oldLine.Intersection(gg.Boundary()).Length(),'oldChainInsidePolygonDegrees':oldLine.Intersection(gg).Length()};rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='changedFeatureSharedLines'}),'changedShared',[(r['feature'],r['oldSharedLengthDegrees']) for r in changedShared],flush=True)
json.dump(rows,open(base+'historical-detail-east-peer-shared.json','w'),indent=2)
