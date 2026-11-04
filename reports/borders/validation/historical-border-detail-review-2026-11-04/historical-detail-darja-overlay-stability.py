from historical_detail_membership import *
request=load(base+'historical-detail-darja-joint-candidate-request.json');result=load(base+'historical-detail-darja-joint-candidate-result.json');baseline=load(base+'historical-detail-darja-joint-baseline-request.json');geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));oldWater,newWater=geo(baseline['historicalWater']),geo(request['historicalWater']);oldLand,newLand=geo(baseline['modernLand']),geo(result['land']);window=geo({'type':'Polygon','coordinates':[[[53.2,38.7],[54.3,38.7],[54.3,40.1],[53.2,40.1],[53.2,38.7]]]})
def local(g):
 out=None
 for i in range(g.GetGeometryCount()):
  p=g.GetGeometryRef(i)
  if p.Intersects(window):
   q=p.Intersection(window);out=q if out is None else out.Union(q)
 return out
raw=[local(oldLand),local(newLand),oldWater.Intersection(window),newWater.Intersection(window)];rows=[]
for grid in [1e-8,1e-9,1e-10]:
 A,B,C,D=[g.SetPrecision(grid) for g in raw];old=A.Intersection(C);new=B.Intersection(D);rows.append({'measurementGridDegrees':grid,'oldOverlapDeg2':old.GetArea(),'newOverlapDeg2':new.GetArea(),'overlapGeometryDifferenceDeg2':old.SymDifference(new).GetArea(),'unionDifferenceDeg2':A.Union(C).SymDifference(B.Union(D)).GetArea(),'deltaDifferenceDeg2':A.SymDifference(B).SymDifference(C.SymDifference(D)).GetArea()});print(rows[-1],flush=True)
json.dump({'purpose':'Numerical stability diagnostic on four clipped in-memory measurement copies only; never quantizes or overwrites source/native/compiled/physical candidates; raw preservation assertion remains recorded independently. Grid is sub-mm overlay arithmetic support, not display tolerance.','rows':rows},open(base+'historical-detail-darja-overlay-stability.json','w'),indent=2)
