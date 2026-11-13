from historical_detail_membership import *
c=load(base+'historical-detail-final-compiled-candidate.json');peers=load(base+'historical-detail-final-peer-inputs.json');geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));out=[]
for peer in peers:
 for p in peer['geometries']:
  g=geo(p['geojson'])
  for ctry in c['rows']:
   a=geo(ctry['before']);b=geo(ctry['after']);old=a.Intersection(g);new=b.Intersection(g);sharedOld=a.Boundary().Intersection(g.Boundary());sharedNew=b.Boundary().Intersection(g.Boundary());r={'entityId':ctry['entityId'],'peer':peer['entityId'],'overlapBeforeDeg2':old.GetArea(),'overlapAfterDeg2':new.GetArea(),'overlapGeometryDifferenceDeg2':old.SymDifference(new).GetArea(),'sharedLineChangeLengthDegrees':sharedOld.SymDifference(sharedNew).Length()};out.append(r);print(r,flush=True);assert r['overlapGeometryDifferenceDeg2']<1e-12 and r['sharedLineChangeLengthDegrees']<1e-8
json.dump({'scope':'Only actual selected foreign peer geometries in target historical interval, compared against four changed compiled polygons; no world validation','rows':out},open(base+'historical-detail-final-peer-preservation.json','w'),indent=2)
