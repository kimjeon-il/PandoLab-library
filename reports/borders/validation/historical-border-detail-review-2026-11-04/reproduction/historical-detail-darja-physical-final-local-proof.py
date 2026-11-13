from historical_detail_membership import *
from pathlib import Path
BASE=Path(base);load0=lambda name:load(str(BASE/name));geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));before=load0('historical-detail-darja-joint-baseline-request.json');exact=load0('historical-detail-darja-physical-exact-splice.json');native=load0('historical-detail-darja-joint-candidate-result.json');oldLand,newLand=geo(before['modernLand']),geo(exact['land']);oldWater,newWater=geo(before['historicalWater']),geo(exact['water']);arc=load0('historical-detail-west-darja-arcs.json')['arcs'][-1];oldArc=geo({'type':'LineString','coordinates':load0('historical-detail-darja-physical-old-exact-arc.json')});newArc=geo({'type':'LineString','coordinates':arc['new']})
def surface(g):
 if g.IsEmpty():return 0.0
 name=g.GetGeometryName()
 if name=='POLYGON':return g.GetArea()
 if name in ['MULTIPOLYGON','GEOMETRYCOLLECTION']:return sum(surface(g.GetGeometryRef(i)) for i in range(g.GetGeometryCount()))
 return 0.0
def counts(g):
 name=g.GetGeometryName()
 if name=='POLYGON':return [1,max(0,g.GetGeometryCount()-1)]
 if name=='MULTIPOLYGON':return [g.GetGeometryCount(),sum(max(0,g.GetGeometryRef(i).GetGeometryCount()-1) for i in range(g.GetGeometryCount()))]
 raise ValueError(name)
def box(a,b,c,d):return geo({'type':'Polygon','coordinates':[[[a,b],[c,b],[c,d],[a,d],[a,b]]]})
def local(g,w):
 out=None
 for i in range(g.GetGeometryCount()):
  p=g.GetGeometryRef(i)
  if p.Intersects(w):
   q=p.Intersection(w);out=q if out is None else out.Union(q)
 return out
w=box(53.2,38.7,54.3,40.1);a,b=local(oldLand,w),local(newLand,w);c,d=oldWater.Intersection(w),newWater.Intersection(w);oldContact,newContact=a.Intersection(c),b.Intersection(d);contactDiff=oldContact.SymDifference(newContact);support=oldArc.Union(newArc).Buffer(1e-10);contactOutside=contactDiff.Difference(support).Length();aral=box(54.5,42.5,62,48);fullRegion=box(45,35,57,48);protoDifference=local(newLand,fullRegion).SymDifference(local(geo(native['land']),fullRegion));metrics={'surfaceAreaMethod':'Only Polygon.GetArea; recurse MultiPolygon/GeometryCollection, all 0D/1D components contribute zero.','waterHolesBefore':counts(oldWater)[1],'waterHolesAfter':counts(newWater)[1],'waterHoleCoordinatesExactlyEqual':before['historicalWater']['coordinates'][1:]==exact['water']['coordinates'][1:],'physicalStructureBefore':counts(oldLand),'physicalStructureAfter':counts(newLand),'modifiedPhysicalPolygonValid':newLand.GetGeometryRef(4318).IsValid(),'globalLandValidityBefore':oldLand.IsValid(),'globalLandValidityAfter':newLand.IsValid(),'old2dOverlapDegree2':surface(oldContact),'new2dOverlapDegree2':surface(newContact),'overlap2dSymDifferenceDegree2':surface(oldContact.SymDifference(newContact)),'physicalUnion2dDifferenceDegree2':surface(a.Union(c).SymDifference(b.Union(d))),'landWaterDelta2dDifferenceDegree2':surface(a.SymDifference(b).SymDifference(c.SymDifference(d))),'water2dDifferenceOutsideDarjaDegree2':surface(oldWater.SymDifference(newWater).Difference(w)),'AralLand2dDifferenceDegree2':surface(local(oldLand,aral).SymDifference(local(newLand,aral))),'nativeOwnerVsExactSplice2dDifferenceDegree2':surface(protoDifference),'oldContactType':oldContact.GetGeometryName(),'newContactType':newContact.GetGeometryName(),'contactDiffType':contactDiff.GetGeometryName(),'contactDiffDimension':contactDiff.GetDimension(),'contactDifferenceOutsideIntendedOldNewDarjaSupportLengthDegrees':contactOutside,'contactSupportNumericEpsilonDegrees':1e-10,'contactSupportEpsilonMeaning':'Numerical collinear support test only; not an editing/generalization tolerance. Exact outside arrays independently checked without rounding.'}
assert metrics['waterHoleCoordinatesExactlyEqual'] and metrics['waterHolesAfter']==68
assert metrics['physicalStructureBefore']==metrics['physicalStructureAfter'] and metrics['modifiedPhysicalPolygonValid']
assert metrics['globalLandValidityBefore']==metrics['globalLandValidityAfter']
for k in ['old2dOverlapDegree2','new2dOverlapDegree2','overlap2dSymDifferenceDegree2','physicalUnion2dDifferenceDegree2','landWaterDelta2dDifferenceDegree2','water2dDifferenceOutsideDarjaDegree2','AralLand2dDifferenceDegree2','nativeOwnerVsExactSplice2dDifferenceDegree2']:assert metrics[k]<=1e-12,(k,metrics[k])
assert contactOutside<=1e-8,contactOutside
master=Path('tools/historical-library/sources/ussr-1922-approved/caspian-shoreline-completed-candidate-20261024.zip');metrics['originalMasterZipSha256']=hashlib.sha256(master.read_bytes()).hexdigest();assert metrics['originalMasterZipSha256']=='3df45ab6e7d3a4b1dfac42b29f28cc1c932c3b1be9f866ccd7df6bb769b9a5b4'
with (BASE/'historical-detail-darja-physical-final-local-proof.json').open('x',encoding='utf-8') as f:json.dump(metrics,f,indent=2)
print(metrics,flush=True)
