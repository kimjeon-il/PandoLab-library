import json,sys,hashlib
from pathlib import Path
from shapely.geometry import shape,box,mapping,Polygon,MultiPolygon,LineString,Point
from shapely.ops import unary_union,nearest_points,transform
from pyproj import Transformer
from PIL import Image,ImageDraw
x=json.load(sys.stdin);O=Path(x['output']);w=lambda n,v:(O/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
D=shape(x['donor']['geometry']);scope=box(58.1,69.5,60.9,70.65);r=box(60.5,69.6,60.9,69.85);groupix=[i for i,p in enumerate(D.geoms) if scope.covers(p)];cross=[i for i,p in enumerate(D.geoms) if scope.intersects(p) and not scope.covers(p)];focus=D.geoms[1554]
t=Transformer.from_crs('EPSG:4326','+proj=laea +lat_0=69.7 +lon_0=60.65 +datum=WGS84 +units=m +no_defs',always_xy=True)
tr=lambda g:transform(t.transform,g)
rows=[]
for v in x['rows']:
 B=shape(v['geometry']);oldix=[i for i,p in enumerate(B.geoms) if scope.covers(p)];conf=[]
 for i in groupix:
  for j,p in enumerate(B.geoms):
   if j in oldix:continue
   a=D.geoms[i].intersection(p)
   if not a.is_empty:conf.append({'donorIndex':i,'historicalIndex':j,'intersectionAreaDegrees2':a.area,'projectedAreaM2':tr(a).area,'intersection':mapping(a),'historicalBounds':list(p.bounds)})
 near=[{'index':j,'rings':len(p.interiors)+1,'vertices':len(p.exterior.coords),'intersectionsWithDonorMainland':None} for j,p in enumerate(B.geoms) if r.intersects(p)]
 rows.append({'entityId':v['entityId'],'versionId':v['versionId'],'validFrom':v['validFrom'],'validTo':v['validTo'],'oldIndices':oldix,'conflicts':conf,'focusHistoricalComponents':near})
B=shape(x['rows'][0]['geometry']);bi=rows[0]['conflicts'][0]['historicalIndex'];bc=B.geoms[bi];mi=[i for i in cross if D.geoms[i].intersects(r)];assert len(mi)==1;mi=mi[0];dc=D.geoms[mi]
inter=bc.boundary.intersection(dc.boundary).intersection(r)
nearnew=[{'index':i,'bbox':list(p.bounds),'distanceTo1554m':tr(p).distance(tr(focus))} for i,p in enumerate(D.geoms) if r.intersects(p)]
oldne=shape(x['ne']['geometry']);neproof={'historicalLocalMainlandBoundaryEqualsNE':bc.boundary.intersection(r).equals(oldne.boundary.intersection(r)),'neLocalSymmetricDifferenceDegrees2':bc.intersection(r).symmetric_difference(oldne.intersection(r)).area}
result={'sourceRevision':x['revision'],'reviewWindow':[58.1,69.5,60.9,70.65],'donorGroupIndices':groupix,'donorGroupCount':len(groupix),'scopeCrossingDonorIndices':cross,'modernMainlandIndex':mi,'modern1554Coordinates':x['donor']['geometry']['coordinates'][1554],'modern1554Bounds':list(focus.bounds),'modern1554AreaM2':tr(focus).area,'modern1554DistanceToModernMainlandM':tr(focus).distance(tr(dc)),'modern1554IntersectsMainland':focus.intersects(dc),'modern1554TouchesAnyOtherComponent':[i for i,p in enumerate(D.geoms) if i!=1554 and focus.intersects(p)],'focusModernComponents':nearnew,'oldModernMainlandBoundaryIntersections':mapping(inter),'oldNELocalProof':neproof,'targets':rows,'sourceWritten':False}
w('contact-geometry-proof.json',result)
# Inspection rendering only; bounds crop is display-only, never a source operation.
im=Image.new('RGB',(1400,680),'white');draw=ImageDraw.Draw(im)
for k,(extent,title) in enumerate([((58.05,69.45,60.95,70.7),'Whole 51-component donor review window'),((60.5,69.63,60.85,69.79),'Diagnostic contact inset, not historical survey proof')]):
 win=box(*extent);pb=tr(win).bounds;sc=min(640/(pb[2]-pb[0]),570/(pb[3]-pb[1]));cx=(pb[0]+pb[2])/2;cy=(pb[1]+pb[3])/2;ox=350+700*k;oy=340
 def render(g,color,width=1):
  g=tr(g.intersection(win))
  def plot(z):
   if z.is_empty:return
   if z.geom_type=='Polygon':
    for ring in [z.exterior,*z.interiors]:draw.line([(ox+(a-cx)*sc,oy-(b-cy)*sc) for a,b in ring.coords],fill=color,width=width)
   elif hasattr(z,'geoms'):
    for q in z.geoms:plot(q)
   elif hasattr(z,'coords'):draw.line([(ox+(a-cx)*sc,oy-(b-cy)*sc) for a,b in z.coords],fill=color,width=width)
  plot(g)
 render(B,'#2468b2',2);render(D,'#de790b',2);render(focus,'#c90000',3)
 p=tr(focus.representative_point());draw.text((ox+(p.x-cx)*sc+5,oy-(p.y-cy)*sc-15),'1554',fill='#c90000');draw.text((700*k+20,30),title,fill='black')
 draw.text((700*k+20,620),'Historical blue; approved modern orange; donor1554 red',fill='black')
im.save(O/'vaygach-contact-inspection.png')
print(json.dumps({'donorCount':len(groupix),'modernMainlandIndex':mi,'focus':result['modern1554Bounds'],'mainlandGapM':result['modern1554DistanceToModernMainlandM'],'contacts':[{'version':z['versionId'],'old':z['oldIndices'],'conflictIndices':[(q['donorIndex'],q['historicalIndex']) for q in z['conflicts']]} for z in rows],'ne':neproof,'intersections':mapping(inter)}))
