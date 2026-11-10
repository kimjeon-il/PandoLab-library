import json,sys,copy,hashlib,base64,zipfile,io
from pathlib import Path
from shapely.geometry import shape,box,Polygon,MultiPolygon,LineString,Point,mapping
from shapely.ops import unary_union,transform
from shapely.validation import explain_validity
from pyproj import Transformer
from PIL import Image,ImageDraw
x=json.load(sys.stdin);O=Path(x['output']);w=lambda n,v:(O/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
D=shape(x['donor']['geometry']);dc=x['donor']['geometry']['coordinates'];mi=3289;dr=dc[mi][0];B=shape(x['rows'][0]['geometry']);old=x['rows'][0]['geometry']['coordinates'][6][0]
outer=old[22928:22970];assert outer[0]==[61.770518,69.76203] and outer[-1]==[60.195649,69.561265]
north=LineString(outer[:2]).intersection(LineString(dr[9375:9377]));south=LineString(outer[-2:]).intersection(LineString(dr[9300:9302]));assert north.geom_type==south.geom_type=='Point'
anchors=[list(north.coords)[0],list(south.coords)[0]];replacement=[outer[0],list(anchors[0]),*list(reversed(dr[9301:9376])),list(anchors[1]),outer[-1]]
scope=box(58.1,69.5,60.9,70.65);indices=[i for i,p in enumerate(D.geoms) if scope.covers(p)];assert len(indices)==51
baseIndices=indices.copy()
# Full adjacent mainland shore from actual line intersections, with no area difference/clip used to create source coordinates.
shorewin=box(60.13,69.55,61.8,69.88);extra=[i for i,p in enumerate(D.geoms) if shorewin.intersects(p) and i not in indices and i!=mi]
assert extra==[1562],extra
indices=sorted(indices+extra);group=MultiPolygon([D.geoms[i] for i in indices]);assert group.is_valid
proj='+proj=laea +lat_0=69.7 +lon_0=60.65 +datum=WGS84 +units=m +no_defs';trf=Transformer.from_crs('EPSG:4326',proj,always_xy=True);tr=lambda p:transform(trf.transform,p)
rows=[];newshapes=[];candidates=[];newlocal=[]
for v in x['rows']:
 coords=v['geometry']['coordinates'];b=shape(v['geometry']);ring=coords[6][0];matches=[i for i in range(len(ring)-len(outer)+1) if ring[i:i+len(outer)]==outer];assert len(matches)==1,matches;j=matches[0]
 wholeOld=[i for i,p in enumerate(b.geoms) if scope.covers(p) or shorewin.covers(p)];assert wholeOld
 newring=ring[:j]+replacement+ring[j+len(outer):];main=Polygon(newring,coords[6][1:]);assert main.is_valid,explain_validity(main)
 arr=copy.deepcopy(coords);arr[6][0]=newring;arr=[p for i,p in enumerate(arr) if i not in wholeOld]+[dc[i] for i in indices];candidate={'type':'MultiPolygon','coordinates':arr};after=shape(candidate);assert after.is_valid,explain_validity(after)
 assert not group.intersects(main)
 keep=[p for i,p in enumerate(b.geoms) if i not in wholeOld and i!=6];rest=unary_union(keep);assert not group.intersects(rest)
 assert all(arr[i]==coords[i] for i in range(6))
 assert newring[:j]==ring[:j] and newring[j+len(replacement):]==ring[j+len(outer):]
 assert arr[-len(indices):]==[dc[i] for i in indices]
 pair1552=arr[-len(indices)+indices.index(1552)];pair1554=arr[-len(indices)+indices.index(1554)];assert shape({'type':'Polygon','coordinates':pair1552}).intersection(shape({'type':'Polygon','coordinates':pair1554})).equals(Point(60.635473200000035,69.69992360000003))
 delta=b.geoms[6].symmetric_difference(main);assert delta.difference(shorewin).is_empty
 # The approved current coast itself has not been moved or re-generalized.
 assert all(Point(p).distance(LineString(dr))==0 for p in replacement[2:-2])
 olddelta=group.intersection(b.geoms[6]);rows.append({'entityId':v['entityId'],'versionId':v['versionId'],'validFrom':v['validFrom'],'validTo':v['validTo'],'oldIslandIndices':wholeOld,'oldMainlandIndex':6,'oldVertexSpanInclusive':[j,j+len(outer)-1],'candidateValid':True,'candidateValidity':explain_validity(after),'retainedCoordinatesAndAllOtherPolygonRingsExact':True,'all52DonorComponentsAndRingsExact':True,'donor1552And1554PointContactPreserved':True,'newDonorVsMainlandIntersectionArea':group.intersection(main).area,'newDonorVsRestIntersects':False,'prior1554MainlandOverlapM2':tr(olddelta).area,'new1554MainlandGapM':tr(D.geoms[1554]).distance(tr(main)),'newMainlandSymmetricDifferenceKm2':tr(delta).area/1e6,'beforePolygonCount':len(coords),'afterPolygonCount':len(arr)})
 candidates.append({'entityId':v['entityId'],'versionId':v['versionId'],'geometry':candidate});newshapes.append(after);newlocal.append(main)
# Shared coast coordinates are identical; their vertex offsets may differ with distant source edits.
assert len(rows)==3
# No source files written. A compact replay operation is retained, not full entity copies.
operation={'schemaVersion':1,'status':'geometrically-valid-candidate-not-applied-parent-review-required','sourceRevision':x['revision'],'scope':'Vaygach and Yugorsky Shar complete 51-component Vaygach-window group plus one linked-shore whole island, 52 total donor group plus matching mainland shoreline arc','oldMainlandPolygonIndex':6,'oldCoordinates':outer,'replacementCoordinates':replacement,'donorMainlandPolygonIndex':mi,'donorMainlandRingIndex':0,'donorExactInteriorSpanInclusive':[9301,9375],'donorInteriorDirection':'reverse','joinCoordinates':anchors,'joinMethod':'Two actual intersections of original historical and approved modern coast segments. Retain every donor vertex between the two intersections and all original coast vertices outside. No clipping of original land polygons, no difference/union repair, no invented bridging segment. Only the two intersected endpoint segments are split.','donorComponentIndices':indices,'newDetachedWholePolygons':[dc[i] for i in indices],'omittedApprovedComponents':0,'additionalWholeModernComponentsInLinkedShoreWindow':extra,'omittedAdditionalModernComponentsInLinkedShoreWindow':[],'shoreWindow':list(shorewin.bounds),'targets':rows,'sourceWritten':False}
w('paired-coast-operation.json',operation)
w('candidate-topology-proof.json',{'status':'passed-for-three-geometry-candidates-only','projection':proj,'targets':rows,'sameMainlandArcAcrossAllThree':True,'sameCompleteDonorGroupAcrossAllThree':True,'all52WholeDonorsValid':True,'donor1552And1554PointContact':mapping(D.geoms[1552].intersection(D.geoms[1554])),'modernGroupValidity':explain_validity(group),'exactHistoricalEffectiveDatesUnchanged':True,'historicalMetadataNotModified':True,'sourceGateAndCodecPendingStructuredProvenance':True,'noSourceWrite':True})
# Visuals: nominal 1:10M 300dpi with explicit whole-group/linked-coast viewport.
mpp=10000000*.0254/300;extent=tr(box(58.05,69.45,61.8,70.7)).bounds;cx=(extent[0]+extent[2])/2;cy=(extent[1]+extent[3])/2;W=1150;H=400;im=Image.new('RGB',(W,H),'white');z=ImageDraw.Draw(im)
for k,(label,geoms) in enumerate([('Original historical',[(B,'#2468b2')]),('Paired candidate, all 52 donor components',[(newshapes[0],'#de790b')]),('Overlay; unchanged political border outside view',[(B,'#2468b2'),(newshapes[0],'#de790b')])]):
 ox=190+380*k;oy=205;z.text((380*k+8,25),label,fill='black')
 for g,c in geoms:
  # Cropping is visualization only, never candidate generation.
  p=tr(g.intersection(box(58.05,69.45,61.8,70.7)))
  def draw(q):
   if q.geom_type=='Polygon':
    for r in [q.exterior,*q.interiors]:z.line([(ox+(a-cx)/mpp,oy-(b-cy)/mpp) for a,b in r.coords],fill=c,width=1)
   elif hasattr(q,'geoms'):
    for a in q.geoms:draw(a)
  draw(p)
 for a in anchors:
  p=tr(Point(a));px=ox+(p.x-cx)/mpp;py=oy-(p.y-cy)/mpp;z.ellipse((px-2,py-2,px+2,py+2),fill='red')
 z.line([(380*k+30,350),(380*k+30+50000/mpp,350)],fill='black',width=2);z.text((380*k+30,357),'50 km',fill='black')
z.text((8,5),'Vaygach + linked Yugorsky mainland coast; candidate only. Red dots: actual coast intersections.',fill='black');z.text((8,382),'Nominal 1:10M at 300 dpi. Full component ledger, no area/visibility cutoff. Not a historical survey.',fill='black');im.save(O/'paired-candidate-source-scale.png')
# Return candidate geometry to the Node caller in memory so JS uses canonical hash serialization.
print(json.dumps({'candidates':candidates,'summary':rows},separators=(',',':')))



