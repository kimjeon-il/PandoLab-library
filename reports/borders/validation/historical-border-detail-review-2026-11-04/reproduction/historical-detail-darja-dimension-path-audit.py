from historical_detail_membership import *
from pathlib import Path
BASE=Path(base)
paths=['historical-detail-darja-joint-baseline-request.json','historical-detail-darja-joint-candidate-request.json','historical-detail-darja-joint-candidate-result.json','historical-detail-darja-overlap-diagnostic.json','historical-detail-darja-joint-independent-observation.json','historical-detail-darja-overlay-stability.json','historical-detail-darja-dimension-audit.json']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();hashes={p:sha(BASE/p) for p in paths}
baseline=load(str(BASE/paths[0]));request=load(str(BASE/paths[1]));result=load(str(BASE/paths[2]));geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));oldWater,newWater=geo(baseline['historicalWater']),geo(request['historicalWater']);oldLand,newLand=geo(baseline['modernLand']),geo(result['land']);window=geo({'type':'Polygon','coordinates':[[[53.2,38.7],[54.3,38.7],[54.3,40.1],[53.2,40.1],[53.2,38.7]]]})
def local(g):
 out=None
 for i in range(g.GetGeometryCount()):
  p=g.GetGeometryRef(i)
  if p.Intersects(window):
   q=p.Intersection(window);out=q if out is None else out.Union(q)
 return out
A,B=local(oldLand),local(newLand);C,D=oldWater.Intersection(window),newWater.Intersection(window);O,P=A.Intersection(C),B.Intersection(D);difference=O.SymDifference(P)
def surface_area(x):
 name=x.GetGeometryName()
 if x.IsEmpty():return 0.0
 if name=='POLYGON':return x.GetArea()
 if name in ['MULTIPOLYGON','GEOMETRYCOLLECTION']:return sum(surface_area(x.GetGeometryRef(i)) for i in range(x.GetGeometryCount()))
 return 0.0
positive_lines=[];nodes=[]
def record(x,path):
 name=x.GetGeometryName();nodes.append({'path':path,'geometryName':name,'dimension':x.GetDimension(),'empty':x.IsEmpty(),'polygonOnlySurfaceAreaDegree2':surface_area(x)})
 if name in ['LINESTRING','LINEARRING']:
  raw=x.GetArea()
  if raw>0:positive_lines.append({'path':path,'pointCount':x.GetPointCount(),'IsRing':bool(x.IsRing()),'envelope':list(x.GetEnvelope()),'rawGetAreaDegree2_NotSurfaceArea':raw,'dimension':x.GetDimension(),'correctSurfaceAreaDegree2':0.0})
  return
 if name=='POLYGON':return
 for i in range(x.GetGeometryCount()):record(x.GetGeometryRef(i),path+'/geometries/'+str(i))
for key,x in [('A_oldLand',A),('B_newLand',B),('C_oldWater',C),('D_newWater',D),('O_oldIntersection',O),('P_newIntersection',P),('intersectionSymDifference',difference)]:record(x,key)
holes=[]
for i,coords in enumerate(baseline['historicalWater']['coordinates'][1:],1):
 polygon=geo({'type':'Polygon','coordinates':[coords]})
 if window.Contains(polygon):holes.append({'holeIndex':i,'pointCount':len(coords),'envelope':list(polygon.GetEnvelope()),'polygonAreaDegree2':surface_area(polygon),'coordinatesUnchanged':coords==request['historicalWater']['coordinates'][i]})
hole_sum=sum(p['polygonAreaDegree2'] for p in holes);old_raw=O.GetArea();new_raw=P.GetArea();old_positive=[p for p in positive_lines if p['path'].startswith('O_oldIntersection/')];new_positive=[p for p in positive_lines if p['path'].startswith('P_newIntersection/')]
metrics={'fullyContainedHoleCount':len(holes),'fullyContainedHolePolygonAreaSumDegree2':hole_sum,'oldRawIntersectionGetArea_NotSurfaceArea':old_raw,'newRawIntersectionGetArea_NotSurfaceArea':new_raw,'differenceHoleSumVsOldRawDegree2':hole_sum-old_raw,'differenceHoleSumVsNewRawDegree2':hole_sum-new_raw,'oldPositiveLineRawAreaSumDegree2':sum(p['rawGetAreaDegree2_NotSurfaceArea'] for p in old_positive),'newPositiveLineRawAreaSumDegree2':sum(p['rawGetAreaDegree2_NotSurfaceArea'] for p in new_positive),'oldTrueOverlapSurfaceAreaDegree2':surface_area(O),'newTrueOverlapSurfaceAreaDegree2':surface_area(P),'trueOverlapSymDifferenceSurfaceAreaDegree2':surface_area(difference)}
assert hashes=={p:sha(BASE/p) for p in paths},'Original inputs or prior diagnostics changed'
output={'scope':'Additional read-only dimensional/path audit of the same four actual inputs. GetArea used as surface area only on Polygon members; positive line raw values retained only to explain prior erroneous totals. No production/remote edit.','originalInputAndDiagnosticSha256':hashes,'originalInputsAndDiagnosticsUnchanged':True,'geometryNodes':nodes,'positiveRawAreaLineComponents':positive_lines,'unchangedFullyContainedWaterHoles':holes,'metrics':metrics}
with (BASE/'historical-detail-darja-dimension-path-audit.json').open('x',encoding='utf-8') as f:json.dump(output,f,indent=2)
print(json.dumps({'topLevel':nodes[:1]+[n for n in nodes if '/' not in n['path'] and n['path']!='A_oldLand'],'positiveLineComponentCounts':{'oldIntersection':len(old_positive),'newIntersection':len(new_positive),'allResults':len(positive_lines)},'metrics':metrics,'originalInputsAndDiagnosticsUnchanged':True}),flush=True)
