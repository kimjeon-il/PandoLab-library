from historical_detail_membership import *
from pathlib import Path
BASE=Path(base);geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));old=load(str(BASE/'historical-detail-darja-joint-baseline-request.json'));new=load(str(BASE/'historical-detail-darja-physical-exact-splice.json'));arc=load(str(BASE/'historical-detail-west-darja-arcs.json'))['arcs'][-1];oldCoords=load(str(BASE/'historical-detail-darja-physical-old-exact-arc.json'));line=lambda cs:{'type':'LineString','coordinates':cs};oldArc,newArc=geo(line(oldCoords)),geo(line(arc['new']));window=geo({'type':'Polygon','coordinates':[[[53.2,38.7],[54.3,38.7],[54.3,40.1],[53.2,40.1],[53.2,38.7]]]})
def local(g):
 out=None
 for i in range(g.GetGeometryCount()):
  p=g.GetGeometryRef(i)
  if p.Intersects(window):
   q=p.Intersection(window);out=q if out is None else out.Union(q)
 return out
oldContact=local(geo(old['modernLand'])).Intersection(geo(old['historicalWater']).Intersection(window));newContact=local(geo(new['land'])).Intersection(geo(new['water']).Intersection(window));diff=oldContact.SymDifference(newContact);support=oldArc.Union(newArc);outside=diff.Difference(support.Buffer(1e-10));cover=Cover({'type':'MultiLineString','coordinates':[oldCoords,arc['new']]});actual=json.loads(diff.ExportToJson());uncovered=[]
for a,b in edges(actual):
 if not cover.includes(a,b):
  seg=geo(line([a,b]));uncovered.append({'a':a,'b':b,'distanceToOldDarjaDegrees':seg.Distance(oldArc),'distanceToNewDarjaDegrees':seg.Distance(newArc),'lengthDegrees':seg.Length()})
expected=oldArc.SymDifference(newArc);actualCover=Cover(actual);expectedUncovered=[]
for a,b in edges(json.loads(expected.ExportToJson())):
 if not actualCover.includes(a,b):expectedUncovered.append({'a':a,'b':b})
summary={'numericEpsilonDegrees':EPS,'actualChangedContactEdges':len(edges(actual)),'actualChangedEdgesOutsideIntendedArcSupport':len(uncovered),'uncoveredActual':uncovered,'expectedChangedEdgesMissingInActualContact':len(expectedUncovered),'uncoveredExpected':expectedUncovered,'thinBufferResidualLengthDegrees':outside.Length(),'thinBufferResidualDistanceToExactSourceSupportDegrees':outside.Distance(support),'thinBufferResidualType':outside.GetGeometryName(),'thinBufferResidualCoordinates':json.loads(outside.ExportToJson()),'originalExpectedDarjaDifferenceLengthDegrees':expected.Length(),'actualContactDifferenceLengthDegrees':diff.Length(),'rawExactContactVsIntendedDifferenceLengthDegrees':diff.SymDifference(expected).Length()};json.dump(summary,open(str(BASE/'historical-detail-darja-contact-support-audit.json'),'x'),indent=2);print({k:v for k,v in summary.items() if k not in ['thinBufferResidualCoordinates','uncoveredExpected','uncoveredActual']},flush=True);print('uncovered actual',uncovered[:4],flush=True)
