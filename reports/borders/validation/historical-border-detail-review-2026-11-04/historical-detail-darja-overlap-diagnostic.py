from historical_detail_membership import *
request=load(base+'historical-detail-darja-joint-candidate-request.json');result=load(base+'historical-detail-darja-joint-candidate-result.json');baseline=load(base+'historical-detail-darja-joint-baseline-request.json');geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));oldWater,newWater=geo(baseline['historicalWater']),geo(request['historicalWater']);oldLand,newLand=geo(baseline['modernLand']),geo(result['land']);window=geo({'type':'Polygon','coordinates':[[[53.2,38.7],[54.3,38.7],[54.3,40.1],[53.2,40.1],[53.2,38.7]]]})
def local(g):
 out=None
 for i in range(g.GetGeometryCount()):
  p=g.GetGeometryRef(i)
  if p.Intersects(window):
   q=p.Intersection(window);out=q if out is None else out.Union(q)
 return out
A,B=local(oldLand),local(newLand);C,D=oldWater.Intersection(window),newWater.Intersection(window);O=A.Intersection(C);P=B.Intersection(D);diff=O.SymDifference(P);metrics={'valid':{k:g.IsValid() for k,g in {'A':A,'B':B,'C':C,'D':D,'oldOverlap':O,'newOverlap':P,'overlapDiff':diff}.items()},'area':{k:g.GetArea() for k,g in {'A':A,'B':B,'C':C,'D':D,'oldOverlap':O,'newOverlap':P,'overlapDiff':diff,'LandDelta':A.SymDifference(B),'WaterDelta':C.SymDifference(D),'UnionDifference':A.Union(C).SymDifference(B.Union(D))}.items()},'diffBBox':diff.GetEnvelope(),'rawWaterDelta':oldWater.SymDifference(newWater).GetArea()};json.dump(metrics,open(base+'historical-detail-darja-overlap-diagnostic.json','w'),indent=2);print(metrics,flush=True)
