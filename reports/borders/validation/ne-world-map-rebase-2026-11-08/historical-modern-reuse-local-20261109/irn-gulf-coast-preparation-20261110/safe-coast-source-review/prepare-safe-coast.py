import json,hashlib,copy
from pathlib import Path
from fractions import Fraction as F
from shapely.geometry import shape,Polygon,LineString,Point,mapping
from shapely.ops import transform,unary_union
from shapely.validation import explain_validity
from pyproj import Geod,Transformer
P=Path(__file__).parent;x=json.loads((P/'inputs.json').read_text(encoding='utf-8'));versions=x['irn']['entity']['geometryVersions'][1:4];d=x['donor']['geometry'];ne=next(f['geometry'] for f in x['ne'] if f['id']=='IRN');geod=Geod(ellps='WGS84')
def save(n,o):
 text=json.dumps(o,ensure_ascii=False,separators=(',',':'));(P/n).write_text(text,encoding='utf-8');assert json.loads((P/n).read_text(encoding='utf-8'))==json.loads(text)
def digest(x):return hashlib.sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()
def edges(g):return {tuple(sorted([tuple(a),tuple(b)])) for p in (g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]) for r in p for a,b in zip(r,r[1:])}
def deltaArea(g):return abs(geod.geometry_area_perimeter(g)[0])/1e6
neE=edges(ne);peerNE=set().union(*(edges(f['geometry']) for f in x['ne'] if f['id']!='IRN'));coastNE=neE-peerNE;southNE={e for e in coastNE if max(p[1] for p in e)<32}
# Derive true intersections; no tolerance-based snapping or connecting line.
dr=d['coordinates'][151][0]; donorArc=list(reversed(dr[6281:-1]+dr[:3218]));base=versions[0]['geometry']['coordinates'][0][0];oldArc=base[669:1383];ol=LineString(oldArc);dl=LineString(donorArc);pts=list(ol.intersection(dl).geoms);pts.sort(key=ol.project);ends=[pts[0],pts[-1]]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def exact_intersection(a,b,c,e):
 A=list(map(F,a));B=list(map(F,b));C=list(map(F,c));E=list(map(F,e));r=[B[i]-A[i] for i in range(2)];s=[E[i]-C[i] for i in range(2)];ca=[C[i]-A[i] for i in range(2)];den=cross(r,s);t=cross(ca,s)/den;u=cross(ca,r)/den;assert 0<=t<=1 and 0<=u<=1
 z=[A[i]+t*r[i] for i in range(2)];return [float(f) for f in z],{'sourceParameter':str(t),'donorParameter':str(u),'exactCoordinateFractions':[str(f) for f in z],'sourceSegment':[a,b],'donorSegment':[c,e]}
certs=[]
for p in ends:
 oi=min(range(len(oldArc)-1),key=lambda i:LineString(oldArc[i:i+2]).distance(p));di=min(range(len(donorArc)-1),key=lambda i:LineString(donorArc[i:i+2]).distance(p));z,cert=exact_intersection(*oldArc[oi:oi+2],*donorArc[di:di+2]);cert.update({'sourceMainlandSegmentIndex':oi+669,'donorArcSegmentIndex':di,'computedIntersection':z,'oldLineResidualDegrees':LineString(oldArc[oi:oi+2]).distance(Point(z)),'donorLineResidualDegrees':LineString(donorArc[di:di+2]).distance(Point(z))});certs.append(cert)
a,b=certs[0]['sourceMainlandSegmentIndex'],certs[1]['sourceMainlandSegmentIndex'];c,e=certs[0]['donorArcSegmentIndex'],certs[1]['donorArcSegmentIndex'];cutW,cutE=[q['computedIntersection'] for q in certs];replacement=[base[a],cutW]+donorArc[c+1:e+1]+[cutE,base[b+1]]
accepted=[i for i in range(189) if i not in [85,114,117,118,151]];assert len(accepted)==184
political=[];candidates=[];checks=[];operations=[];paired=[]
water=shape(x['water']['geometryVersions'][0]['geometry'])
def beginning(s):return (s+'-01-01')[:10] if s else '0000-01-01'
def enddate(s):return s+'-12-31' if s and len(s)==4 else s or '9999-12-31'
def active(entity,date):return beginning(entity['lifetime']['validFrom'])<=date<=enddate(entity['lifetime']['validTo'])
for v in versions:
 g=v['geometry'];ring=g['coordinates'][0][0];assert ring[a:b+2]==base[a:b+2];newring=ring[:a]+replacement+ring[b+2:]
 # Existing political-exception geometry is retained verbatim. Unincluded exceptions stay absent.
 Abu=copy.deepcopy(g['coordinates'][9]);assert Polygon(Abu[0],Abu[1:]).intersects(Polygon(d['coordinates'][114][0]))
 polys=[[newring,*copy.deepcopy(g['coordinates'][0][1:])]]+[copy.deepcopy(d['coordinates'][i]) for i in accepted]+[copy.deepcopy(g['coordinates'][5]),copy.deepcopy(g['coordinates'][6]),Abu]
 cg={'type':'MultiPolygon','coordinates':polys};s=shape(cg);old=shape(g);assert s.is_valid,explain_validity(s);changes=old.symmetric_difference(s)
 # Full old non-coastal mainland remains byte-exact and the two original political contacts are untouched.
 assert newring[:a]==ring[:a] and newring[-len(ring[b+2:]):]==ring[b+2:];assert all(polys[j+1]==d['coordinates'][i] for j,i in enumerate(accepted));assert polys[-3:]==[g['coordinates'][5],g['coordinates'][6],g['coordinates'][9]]
 nonNE=edges(g)-neE;assert nonNE.issubset(edges(cg))
 for di,name in [(85,'Farsi'),(114,'Abu Musa'),(117,'Little Tunb'),(118,'Greater Tunb')]:
  dp=Polygon(d['coordinates'][di][0],d['coordinates'][di][1:]);oldmatches=[i for i,q in enumerate(g['coordinates']) if Polygon(q[0],q[1:]).intersection(dp).area>0];newmatches=[i for i,q in enumerate(polys) if Polygon(q[0],q[1:]).intersection(dp).area>0]
  assert bool(oldmatches)==bool(newmatches)
  if di==114:
   assert oldmatches==[9] and polys[newmatches[0]]==g['coordinates'][9];op=Polygon(Abu[0],Abu[1:]);np=Polygon(polys[newmatches[0]][0],polys[newmatches[0]][1:]);unchangedArea=op.symmetric_difference(np).area;assert unchangedArea==0
  else:assert oldmatches==newmatches==[];op=old.intersection(dp);np=s.intersection(dp);unchangedArea=op.symmetric_difference(np).area
  political.append({'versionId':v['versionId'],'name':name,'donorIndex':di,'oldIncluded':bool(oldmatches),'candidateIncluded':bool(newmatches),'oldPolygonIndices':oldmatches,'candidatePolygonIndices':newmatches,'oldFullComponentAreaKm2':deltaArea(op),'candidateFullComponentAreaKm2':deltaArea(np),'symmetricDifferenceSquareDegrees':unchangedArea,'originalCoordinatesPreserved':di==114,'modernDonorNotSubstituted':True,'decision':'Preserve existing source inclusion and geometry; no new attribution judgment.'})
 peers=[]
 for peer in x['peers']:
  en=peer['entity'];dates=[v['validFrom'],v['validTo']];app=[]
  for date in dates:
   if not active(en,date):continue
   vs=[z for z in en['geometryVersions'] if beginning(z['validFrom'])<=date<=enddate(z['validTo'])]
   for pv in vs:
    if pv['versionId'] not in [r['versionId'] for r in app]:app.append(pv)
  if peer['id'] in ['PAK','IND']:
   app=en['geometryVersions'];role='modern donor-only comparator; entity is outside its lifetime at every selected historical date'
  elif peer['id']=='GBR':role='date-active entity; geometry is British Isles, not British India; does not furnish an eastern counterpart'
  else:role='date-effective stored source counterpart/context'
  for pv in app:
   pg=shape(pv['geometry']);oi=old.intersection(pg);ni=s.intersection(pg);overlap=oi.symmetric_difference(ni).area;sharedBefore=old.boundary.intersection(pg.boundary);sharedAfter=s.boundary.intersection(pg.boundary);sharedDelta=sharedBefore.symmetric_difference(sharedAfter).length;deltaForeign=changes.intersection(pg).area
   assert overlap<=1e-14 and sharedDelta<=1e-12 and deltaForeign<=1e-14,(peer['id'],overlap,sharedDelta,deltaForeign)
   row={'entityId':en['entityId'],'versionId':pv['versionId'],'lifetime':en['lifetime'],'validFrom':pv['validFrom'],'validTo':pv['validTo'],'role':role,'sourceGeometryDigest':digest(pv['geometry']),'intersectionBeforeSquareDegrees':oi.area,'intersectionAfterSquareDegrees':ni.area,'intersectionSymmetricDifferenceSquareDegrees':overlap,'sharedBoundaryChangeDegrees':sharedDelta,'changedAreaInsidePeerSquareDegrees':deltaForeign}
   peers.append(row)
 # Candidate changes never enter historical Caspian water; existing relation remains unchanged.
 assert changes.intersection(water).area==0
 chk={'versionId':v['versionId'],'validFrom':v['validFrom'],'validTo':v['validTo'],'valid':s.is_valid,'componentCount':len(polys),'wholeDonorsExact':184,'preservedOriginalComponents':[5,6,9],'protectedNonNEEdges':len(nonNE),'allProtectedNonNEEdgesExact':True,'mainlandHolesPreserved':True,'unchangedPoliticalContactCoordinates':[[48.531016,29.96133],[61.588227,25.202094]],'arbitraryStraightConnectors':0,'oldNEOnlySouthernEdgesBefore':len(southNE&edges(g)),'oldNEOnlySouthernEdgesAfter':len(southNE&edges(cg)),'allNEOnlyEdgesAfter':len(coastNE&edges(cg)),'changedBounds':list(changes.bounds),'changedHistoricalCaspianWaterIntersectionSquareDegrees':0.0,'neighbors':peers,'sourceCoastPrefixUntouched':True,'sourceCoastSuffixUntouched':True}
 checks.append(chk);candidates.append({'type':'Feature','id':v['versionId'],'properties':{'validFrom':v['validFrom'],'validTo':v['validTo'],'status':'source-only-safe-coast-candidate','politicalExceptionPolicy':'Abu Musa original polygon exact; Farsi and both Tunbs remain absent; no new ownership conclusions'},'geometry':cg});operations.append({'versionId':v['versionId'],'oldMainlandVertexSpan':[a,b+1],'oldCoordinates':ring[a:b+2],'replacementCoordinates':replacement,'acceptedWholeDonorIndices':accepted,'preservedOldPolygonIndices':[5,6,9],'newPolygonOrder':'mainland, whole donors in original-index order, old5, old6, old9','intersections':certs})
save('safe-coast-candidates.geojson',{'type':'FeatureCollection','features':candidates});save('reviewed-operations.json',{'sourceRevision':x['sourceRevision'],'operations':operations,'historicalPoliticalSourceUnchanged':True,'sizeCutoff':None});save('political-exception-preservation.json',{'rows':political,'anyPoliticalMembershipChange':False,'modernExceptions':[85,114,117,118]});save('source-topology-measurements.json',{'checks':checks,'status':'passed-source-only-coast-delta-preservation','explicitLimits':['No historical British India/British Raj source entity found in local country source index. PAK and IND begin 1947 and are donor-only comparators.','GBR is active but its geometry is the British Isles, not an eastern counterpart.','Original eastern political arc, endpoint and endpoint coastal run are retained; no missing historical neighbor geometry is inferred.','Current neighbor intersections may be pre-existing nonzero; this change preserves their actual geometry rather than asserting they were originally zero.','No compiled/runtime or historical legal-accuracy validation.']});save('intersection-certificates.json',{'method':'Exact rational intersection of input binary-double coordinates, rounded once to binary double for GeoJSON. No snap tolerance or artificial connector.','intersections':certs,'supersededOldConnectorsMetres':[849.2741155742951,173.526953701885],'originalPoliticalAnchorsPreserved':[[48.531016,29.96133],[61.588227,25.202094]],'sourceCoastRetainedNearWestEndpointMetres':geod.geometry_length(LineString(base[669:a+1]+[cutW])),'sourceCoastRetainedNearEastEndpointMetres':geod.geometry_length(LineString([cutE]+base[b+1:1383]))})
print(json.dumps({'validCandidates':len(checks),'componentCounts':[q['componentCount'] for q in checks],'remainingSouthernNE':[q['oldNEOnlySouthernEdgesAfter'] for q in checks],'oldNewAbuMusa':[[r['oldFullComponentAreaKm2'],r['candidateFullComponentAreaKm2']] for r in political if r['name']=='Abu Musa'],'intersections':[q['computedIntersection'] for q in certs],'oldSpliceSpan':[a,b+1],'newStraightConnectors':0},indent=2))
