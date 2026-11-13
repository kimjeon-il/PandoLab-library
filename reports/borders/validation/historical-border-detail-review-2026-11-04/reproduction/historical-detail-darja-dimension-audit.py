from historical_detail_membership import *
from pathlib import Path
BASE=Path(base)
paths=['historical-detail-darja-joint-baseline-request.json','historical-detail-darja-joint-candidate-request.json','historical-detail-darja-joint-candidate-result.json','historical-detail-darja-overlap-diagnostic.json','historical-detail-darja-joint-independent-observation.json','historical-detail-darja-overlay-stability.json']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
hashes={p:sha(BASE/p) for p in paths}
baseline=load(str(BASE/paths[0]));request=load(str(BASE/paths[1]));result=load(str(BASE/paths[2]));geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x))
oldWater,newWater=geo(baseline['historicalWater']),geo(request['historicalWater']);oldLand,newLand=geo(baseline['modernLand']),geo(result['land'])
window=geo({'type':'Polygon','coordinates':[[[53.2,38.7],[54.3,38.7],[54.3,40.1],[53.2,40.1],[53.2,38.7]]]})
def local(g):
 out=None
 for i in range(g.GetGeometryCount()):
  p=g.GetGeometryRef(i)
  if p.Intersects(window):
   q=p.Intersection(window);out=q if out is None else out.Union(q)
 return out
A,B=local(oldLand),local(newLand);C,D=oldWater.Intersection(window),newWater.Intersection(window)
oldOverlap,newOverlap=A.Intersection(C),B.Intersection(D);rawDifference=oldOverlap.SymDifference(newOverlap)
def classify(g):
 types=defaultdict(int);dims=defaultdict(int);polygons=[];lines=[];points=[];closed=0;holes=0
 def visit(x):
  nonlocal closed,holes
  name=x.GetGeometryName();types[name]+=1;dims[str(x.GetDimension())]+=1
  if x.IsEmpty():return
  if name=='POLYGON':polygons.append(x.Clone());holes+=max(0,x.GetGeometryCount()-1);return
  if name in ['LINESTRING','LINEARRING']:
   lines.append(x.Clone());pts=x.GetPoints();closed+=int(len(pts)>1 and pts[0]==pts[-1]);return
  if name=='POINT':points.append(x.Clone());return
  for i in range(x.GetGeometryCount()):visit(x.GetGeometryRef(i))
 visit(g)
 summary={'geometryType':g.GetGeometryName(),'dimension':g.GetDimension(),'empty':g.IsEmpty(),'types':dict(types),'nodeDimensions':dict(dims),'polygonComponents':len(polygons),'multiPolygonContainers':types.get('MULTIPOLYGON',0),'polygonHoles':holes,'lineStringComponents':len(lines),'closedLineComponents':closed,'pointComponents':len(points),'rawOgrGetAreaDiagnosticOnly':g.GetArea(),'polygonOnlyAreaDegree2':sum(p.GetArea() for p in polygons),'lineOnlyCoordinateLengthDegrees':sum(p.Length() for p in lines)}
 return summary,polygons,lines
summaries={};parts={}
for key,g in [('oldLocalLand',A),('newLocalLand',B),('oldLocalWater',C),('newLocalWater',D),('oldIntersection',oldOverlap),('newIntersection',newOverlap),('rawIntersectionSymDifference',rawDifference)]:
 summaries[key],polys,lines=classify(g);parts[key]=(polys,lines)
def polygonal_union(polys):
 out=ogr.Geometry(ogr.wkbMultiPolygon)
 for p in polys:out.AddGeometry(p)
 return out.UnionCascaded() if polys else out
def line_collection(lines):
 out=ogr.Geometry(ogr.wkbMultiLineString)
 for line in lines:out.AddGeometry(line)
 return out
old2d=polygonal_union(parts['oldIntersection'][0]);new2d=polygonal_union(parts['newIntersection'][0]);diff2d=old2d.SymDifference(new2d)
old1d=line_collection(parts['oldIntersection'][1]);new1d=line_collection(parts['newIntersection'][1]);diff1d=old1d.SymDifference(new1d)
summaries['polygonOnlySymDifference'],_,_=classify(diff2d);summaries['lineOnlySymDifference'],_,_=classify(diff1d)
src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);dst=osr.SpatialReference();definition='+proj=aeqd +lat_0=39.4 +lon_0=53.7 +datum=WGS84 +units=m';dst.SetFromUserInput(definition);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);tr=osr.CoordinateTransformation(src,dst)
def length_m(g):
 copy=g.Clone();copy.Transform(tr);return copy.Length()
measurements={'old2dOverlapAreaDegree2':old2d.GetArea(),'new2dOverlapAreaDegree2':new2d.GetArea(),'twoDimensionalOverlapSymDifferenceDegree2':summaries['polygonOnlySymDifference']['polygonOnlyAreaDegree2'],'old1dContactLengthMeters':length_m(old1d),'new1dContactLengthMeters':length_m(new1d),'oneDimensionalContactSymDifferenceLengthMeters':length_m(diff1d),'projection':definition,'projectionExecution':'Existing OSGeo OSR transformation with XY axis order; length only, not a simplification tolerance.'}
triangle=ogr.CreateGeometryFromWkt('LINESTRING(0 0,2 0,0 1,0 0)');triangle_summary,_,_=classify(triangle)
output={'scope':'Read-only dimensional diagnosis of the same four original local inputs, original unclipped inputs and prior diagnostic files hash-guarded. No raw assertion removed, no tolerance changed, no data quantization, no production/remote mutation.','inputFilesBeforeSha256':hashes,'syntheticClosedTriangle':triangle_summary,'localWindow':[53.2,38.7,54.3,40.1],'geometryInventory':summaries,'measurements':measurements}
assert {p:sha(BASE/p) for p in paths}==hashes,'Original input/diagnostic bytes changed'
output['originalInputsAndDiagnosticsUnchanged']=True
out=BASE/'historical-detail-darja-dimension-audit.json'
with out.open('x',encoding='utf-8') as f:json.dump(output,f,indent=2)
print(json.dumps({'intersections':{k:summaries[k] for k in ['oldIntersection','newIntersection','rawIntersectionSymDifference']},'measurements':measurements,'originalInputsAndDiagnosticsUnchanged':True}),flush=True)
