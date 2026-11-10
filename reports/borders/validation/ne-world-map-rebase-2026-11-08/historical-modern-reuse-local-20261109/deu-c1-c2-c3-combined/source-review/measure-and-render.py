import json,hashlib,math,sys
from pathlib import Path
from fractions import Fraction as F
from shapely.geometry import shape,Polygon,LineString,MultiLineString,Point,box
from shapely.ops import transform,unary_union
from shapely.validation import explain_validity
import shapely,pyproj
from PIL import Image,ImageDraw
D=Path(__file__).parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,x:(D/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
x=read(D/'review-inputs.tmp.json');patch=read(D.parent/'DEU-c1-c2-c3-combined-patch.json');old=x['before']['geometry'];new=x['after'];ops=patch['operations'];a,b=shape(old),shape(new);delta=a.symmetric_difference(b)
t=pyproj.Transformer.from_crs('EPSG:4326','EPSG:3035',always_xy=True);project=lambda g:transform(t.transform,g)
key=lambda a,b:tuple(sorted((tuple(a),tuple(b))))
polys=lambda g:g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
ne=[f for f in x['ne']['features'] if f['id'] in ['DEU','DNK','POL','RUS','LTU']]
neEdges={key(a,b) for f in ne for po in polys(f['geometry']) for ring in po for a,b in zip(ring,ring[1:])}
master=x['master']['features'][0]['geometry'];protected=[(p,q) for po in polys(master) for ring in po for p,q in zip(ring,ring[1:]) if key(p,q) not in neEdges]
newEdges={key(p,q) for po in polys(new) for ring in po for p,q in zip(ring,ring[1:])};oldEdges={key(p,q) for po in polys(old) for ring in po for p,q in zip(ring,ring[1:])}
currentProtected=oldEdges-neEdges;assert currentProtected<=newEdges
protectedPresent=[(p,q) for p,q in protected if key(p,q) in oldEdges];protectedNotPresent=[(p,q) for p,q in protected if key(p,q) not in oldEdges]
assert all(key(p,q) in newEdges for p,q in protectedPresent)
protectedLine=MultiLineString(protectedPresent);assert not delta.intersects(protectedLine)
remaining=[p for p in old['coordinates'][1:] if not any(p==o['oldWholeIsland'] for o in ops)];detached=[p for op in ops for p in op['newDetachedWholePolygons']]
assert remaining+detached==new['coordinates'][1:];assert old['coordinates'][0][1:]==new['coordinates'][0][1:]
prior=next(v for v in x['priorOps']['targets'] if v['entityId']=='state:DEU');priorChecks=[]
for op in prior['operations']:
 c=op['replacementCoordinates'];nr=new['coordinates'][0][0];n=sum(nr[i:i+len(c)]==c for i in range(len(nr)-len(c)+1));assert n==1;priorChecks.append({'operationId':op.get('id'), 'exactOccurrences':n,'vertices':len(c)})
intersection=[];local=[]
for op in ops:
 for p,q in zip(op['oldCoordinates'],op['oldCoordinates'][1:]):assert key(p,q) in neEdges
 assert all(key(p,q) in neEdges for ring in op['oldWholeIsland'] for p,q in zip(ring,ring[1:]))
 donor=x['donor']['geometry']['coordinates'][0][0];s,e=op['donor']['vertexSpan'];assert donor[s:e+1]==op['exactDonorCoordinates']
 for k,(p,ab,cd) in enumerate(zip(op['computedIntersectionCoordinates'],[op['oldCoordinates'][:2],op['oldCoordinates'][-2:]],[donor[s-1:s+1],donor[e:e+2]])):
  A,B,C,E=[[F(v) for v in q] for q in ab+cd];u=[B[i]-A[i] for i in range(2)];v=[E[i]-C[i] for i in range(2)];w=[C[i]-A[i] for i in range(2)];cross=lambda q,r:q[0]*r[1]-q[1]*r[0];den=cross(u,v);st=cross(w,v)/den;dt=cross(w,u)/den;r=[A[i]+st*u[i] for i in range(2)];cert=op['computedIntersectionCertificates'][k]
  assert 0<=st<=1 and 0<=dt<=1 and [str(z) for z in r]==cert['rationalCoordinate'] and str(st)==cert['oldParameter'] and str(dt)==cert['donorParameter'] and [float(z) for z in r]==p
  intersection.append({'oldIslandIndexHint':op['oldIslandIndexHint'],'endpoint':k,'point':p,'oldSegment':ab,'donorSegment':cd,'rationalCertificateRecomputed':True,'oldParameter':str(st),'donorParameter':str(dt),'oldLineResidualDegrees':Point(p).distance(LineString(ab)),'donorLineResidualDegrees':Point(p).distance(LineString(cd)),'representation':'Exact rational intersection of stored binary floating inputs, converted once to double. Nonzero floating residuals retained; not snap/accuracy tolerances.'})
 pts=op['replacementCoordinates']+op['oldCoordinates']+[p for r in op['oldWholeIsland'] for p in r];bounds=[min(p[0] for p in pts),min(p[1] for p in pts),max(p[0] for p in pts),max(p[1] for p in pts)];region=box(bounds[0]-.001,bounds[1]-.001,bounds[2]+.001,bounds[3]+.001)
 local.append({'oldIslandIndexHint':op['oldIslandIndexHint'],'bbox':bounds,'oldWholeIslandExactNE':True,'oldArcEveryEdgeExactNE':True,'exactCopiedDonorVertices':len(op['exactDonorCoordinates']),'beforeLocalLandKm2':project(a.intersection(region)).area/1e6,'afterLocalLandKm2':project(b.intersection(region)).area/1e6,'addedKm2':project(b.difference(a).intersection(region)).area/1e6,'removedKm2':project(a.difference(b).intersection(region)).area/1e6,'arbitraryConnectors':0})
peers=[];selected='1914-07-31'
for rec in x['peers']:
 for v in rec['entity']['geometryVersions']:
  g=shape(v['geometry']);lo=max(x['before']['validFrom'],v.get('validFrom') or x['before']['validFrom']);hi=min(x['before']['validTo'],v.get('validTo') or x['before']['validTo']);dated=v.get('validFrom') is not None or v.get('validTo') is not None
  role='selected-date bounded source counterpart' if dated and (v.get('validFrom') or '0000')<=selected<=(v.get('validTo') or '9999') else 'bounded source at different historical date' if dated and lo<=hi else 'modern technical comparator only'
  q={'entityId':rec['entity']['entityId'],'versionId':v['versionId'],'validFrom':v.get('validFrom'),'validTo':v.get('validTo'),'role':role,'overlappingStoredInterval':[lo,hi] if lo<=hi else None,'geometrySha256':hashlib.sha256(json.dumps([v['geometry']['type'],v['geometry']['coordinates']],separators=(',',':')).encode()).hexdigest(),'deltaTouchesPeer':delta.intersects(g),'sharedBoundaryUnchanged':a.boundary.intersection(g.boundary).equals(b.boundary.intersection(g.boundary)),'overlapUnchanged':a.intersection(g).equals(b.intersection(g)),'beforeOverlapKm2':project(a.intersection(g)).area/1e6,'afterOverlapKm2':project(b.intersection(g)).area/1e6,'beforeSharedLengthDegrees':a.boundary.intersection(g.boundary).length,'afterSharedLengthDegrees':b.boundary.intersection(g.boundary).length}
  # JavaScript geometry digests are supplied later by the canonical writer, not Python float serialization.
  q.pop('geometrySha256');assert not q['deltaTouchesPeer'] and q['sharedBoundaryUnchanged'] and q['overlapUnchanged'];peers.append(q)
assert a.is_valid and b.is_valid
polyOverlaps=[]
for i,p in enumerate(b.geoms):
 for j,q in enumerate(b.geoms):
  if j<=i or not p.envelope.intersects(q.envelope):continue
  area=p.intersection(q).area
  if area:polyOverlaps.append([i,j,area])
assert not polyOverlaps
measures={'schemaVersion':1,'status':'passed-scoped-source-topology-only','sourceRevision':x['sourceRevision'],'candidateGeometrySha256':patch['resultGeometryDigest'],'validity':{'before':explain_validity(a),'after':explain_validity(b),'wholeBeforeValid':a.is_valid,'wholeAfterValid':b.is_valid},'union':{'afterEqualsUnionOfOwnComponents':b.equals(unary_union(list(b.geoms))),'addedKm2':project(b.difference(a)).area/1e6,'removedKm2':project(a.difference(b)).area/1e6,'totalDeltaKm2':project(delta).area/1e6},'connectivity':{'beforePolygonCount':len(old['coordinates']),'afterPolygonCount':len(new['coordinates']),'removedWholeIslandCount':3,'newDetachedCount':1,'meaning':'Three old display-proxy island components are replaced by current mainland routes and exact detached polygon145. This is not evidence of historical land connection or ownership.'},'holesIslands':{'remainingPolygonsExactAndOrdered':remaining+detached==new['coordinates'][1:],'mainlandHolesExact':old['coordinates'][0][1:]==new['coordinates'][0][1:],'exactWholeDonor145Preserved':detached==[x['donor']['geometry']['coordinates'][145]],'beforeHoleCount':sum(len(p)-1 for p in old['coordinates']),'afterHoleCount':sum(len(p)-1 for p in new['coordinates']),'newComponentInteriorOverlaps':polyOverlaps},'protectedMasterEdges':{'currentPreimageExactNEMismatchEdges':len(currentProtected),'allCurrentMismatchedEdgesExactlyRetained':True,'exactNEMismatchInMaster':len(protected),'presentInCurrentPreimage':len(protectedPresent),'absentBeforeThisChange':len(protectedNotPresent),'allPresentEdgesRetained':True,'deltaIntersectsProtectedEdges':False,'classificationLimit':'Exact-NE mismatch is only a conservative preservation classification, NOT proof that the edge is historically sourced. Some mismatches may be generalized NE. No historical provenance is inferred from mismatch.'},'priorThreeCoastOperations':priorChecks,'localOperations':local,'computedIntersections':intersection,'counterparts':peers,'dateReview':{'unchangedVersionPeriod':[x['before']['validFrom'],x['before']['validTo']],'representativeDate':selected,'certainty':x['before']['certainty'],'sourceId':x['before']['sourceId'],'modernLTUNot1871Counterpart':True,'undatedDNKPOLAreTechnicalComparatorsOnly':True,'fullPeriodDatedCounterpartClosureVerified':False},'notClaimed':['Independent historical positional accuracy','Historical land connection/ownership from modern donor extent','Revalidated historical ownership throughout 1871-1918','Compiled/runtime/producer approval']}
write('source-topology-measurements.json',measures)
# Actual projected render at 1:10M with a separate enlarged diagnostic.
M=10000000*.0254/96;pg=project(b);pold=project(a);pne=project(shape(next(f for f in ne if f['id']=='DEU')['geometry']));pmaster=project(shape(master));bounds=pg.bounds;w=math.ceil((bounds[2]-bounds[0]+140000)/M);hh=math.ceil((bounds[3]-bounds[1]+140000)/M);cx=(bounds[0]+bounds[2])/2;cy=(bounds[1]+bounds[3])/2;extent=[cx-w*M/2,cy-hh*M/2,cx+w*M/2,cy+hh*M/2]
def draw_geom(dr,g,extent,offset=(0,0),scale=M,color=(20,80,200),width=1):
 def xy(p):return (offset[0]+(p[0]-extent[0])/scale,offset[1]+(extent[3]-p[1])/scale)
 def one(p):
  dr.line([xy(q) for q in p.exterior.coords],fill=color,width=width)
  for r in p.interiors:dr.line([xy(q) for q in r.coords],fill=color,width=width)
 if g.is_empty:return
 if g.geom_type=='Polygon':one(g)
 elif g.geom_type in ['MultiPolygon','GeometryCollection']:
  for q in g.geoms:draw_geom(dr,q,extent,offset,scale,color,width)
 elif g.geom_type in ['LineString','LinearRing']:dr.line([xy(q) for q in g.coords],fill=color,width=width)
 elif g.geom_type=='MultiLineString':
  for q in g.geoms:draw_geom(dr,q,extent,offset,scale,color,width)
im=Image.new('RGB',(w*3+40,hh+100),'white');dr=ImageDraw.Draw(im)
for i,title in enumerate(['Preserved working reconstruction + NE','Current preimage + NE','Candidate + NE']):
 off=(10+i*(w+10),55);dr.text((off[0],32),title,fill='black');draw_geom(dr,pne,extent,off,color=(180,180,180));draw_geom(dr,[pmaster,pold,pg][i],extent,off,color=(30,80,180));
 for op in ops:draw_geom(dr,project(LineString(op['oldCoordinates'])),extent,off,color=(210,50,40),width=2)
dr.text((10,8),'DEU C1/C2/C3 source-only | EPSG:3035 | 1:10,000,000 at96dpi | blue shape, gray NE, red old arcs',fill='black');dr.text((10,hh+65),'No historical coastline accuracy claim. Working reconstruction is evidence preimage, not historical truth.',fill='black');im.save(D/'DEU-source-scale-review.png',dpi=(96,96))
im=Image.new('RGB',(1800,640),'white');dr=ImageDraw.Draw(im);diagnostics=[]
for i,(op,row) in enumerate(zip(ops,local)):
 pts=project(shape({'type':'MultiPoint','coordinates':op['replacementCoordinates']+[q for r in op['oldWholeIsland'] for q in r]})).bounds;scale=max((pts[2]-pts[0])/520,(pts[3]-pts[1])/500);ex=[(pts[0]+pts[2])/2-280*scale,(pts[1]+pts[3])/2-260*scale,(pts[0]+pts[2])/2+280*scale,(pts[1]+pts[3])/2+260*scale];off=(20+i*600,75)
 clip=box(*ex);draw_geom(dr,pold.intersection(clip),ex,off,scale,color=(220,70,50),width=2);draw_geom(dr,pg.intersection(clip),ex,off,scale,color=(10,90,190),width=2);draw_geom(dr,project(shape(x['donor']['geometry'])).intersection(clip),ex,off,scale,color=(50,150,100),width=1)
 for p in op['computedIntersectionCoordinates']:
  px,py=t.transform(*p);u=off[0]+(px-ex[0])/scale;v=off[1]+(ex[3]-py)/scale;dr.ellipse((u-4,v-4,u+4,v+4),fill='black')
 dr.text((off[0],40),f"Original island {op['oldIslandIndexHint']} | red preimage, blue candidate, green donor",fill='black');diagnostics.append({'oldIslandIndexHint':op['oldIslandIndexHint'],'extentMetres':ex,'metresPerPixel':scale,'scaleDenominator':scale*96/.0254})
dr.text((20,12),'Enlarged scoped diagnostic only. Black points: computed segment intersections, not copied donor vertices.',fill='black');im.save(D/'DEU-scoped-diagnostic.png')
write('projection-execution.json',{'schemaVersion':1,'status':'executed','inputCrs':'EPSG:4326','crs':'EPSG:3035','definition':t.definition,'axisOrder':'always_xy longitude,latitude','units':'metre','python':sys.version,'pyproj':pyproj.__version__,'proj':pyproj.proj_version_str,'shapely':shapely.__version__,'geos':shapely.geos_version_string,'renderScaleDenominator':10000000,'dpi':96,'metresPerPixel':M,'framePixels':[w,hh],'sameExtentForEachPanelMetres':extent,'candidateProjectedBoundsMetres':bounds,'candidateGeometrySha256':patch['resultGeometryDigest'],'finite':all(math.isfinite(v) for v in bounds),'sourceScaleImage':'DEU-source-scale-review.png','diagnosticImage':'DEU-scoped-diagnostic.png','diagnostics':diagnostics,'historicalAccuracyMeasured':False})
print(json.dumps({'status':measures['status'],'protectedMasterEdges':measures['protectedMasterEdges'],'union':measures['union'],'local':local,'peerCount':len(peers),'images':2}))
