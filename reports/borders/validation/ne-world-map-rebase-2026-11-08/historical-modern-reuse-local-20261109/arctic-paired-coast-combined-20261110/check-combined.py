import json,sys,math
from pathlib import Path
from shapely.geometry import shape,MultiPolygon,box
from shapely.ops import unary_union,transform
from shapely.validation import explain_validity
from pyproj import Transformer
from PIL import Image,ImageDraw
x=json.load(sys.stdin);O=Path(x['output']);write=lambda n,v:(O/n).write_text(json.dumps(v,indent=2)+'\n',encoding='utf8')
d=shape(x['donorGeometry']);group=MultiPolygon([d.geoms[i] for i in x['donorIndices']]);ng=MultiPolygon([d.geoms[i] for i in x['novaIndices']]);vg=MultiPolygon([d.geoms[i] for i in x['vayIndices']]);assert group.is_valid and not ng.intersects(vg)
proj='+proj=laea +lat_0=74 +lon_0=60 +datum=WGS84 +units=m +no_defs';t=Transformer.from_crs('EPSG:4326',proj,always_xy=True);tr=lambda g:transform(t.transform,g);rows=[]
for r in x['rows']:
 b=shape(r['before']);a=shape(r['after']);assert a.is_valid,explain_validity(a);assert r['after']['coordinates'][-809:]==[x['donorGeometry']['coordinates'][i] for i in x['donorIndices']]
 retained=unary_union(list(a.geoms)[:-809]);assert not group.intersects(retained);expected=unary_union([retained,group]);assert a.symmetric_difference(expected).is_empty
 assert len(a.geoms)==len(b.geoms)-7+809
 oldnova=MultiPolygon([b.geoms[i] for i in r['oldNovaIndices']]);oldvay=MultiPolygon([b.geoms[i] for i in r['oldVayIndices']]);assert not oldnova.intersects(oldvay)
 rows.append({'entityId':r['entityId'],'versionId':r['versionId'],'validFrom':r['validFrom'],'validTo':r['validTo'],'fullBeforeValid':b.is_valid,'fullCandidateValid':True,'fullCandidateValidity':explain_validity(a),'oldComponentsRemoved':7,'allWholeDonorComponents':809,'allRingsAndCoordinateArraysExact':True,'newGroupVsRetainedIntersectionArea':group.intersection(retained).area,'newGroupVsRetainedAnyContact':False,'candidateEqualsRetainedUnionWholeDonorGroup':True,'novaVsVayGroupsAnyContact':False,'modernWithinGroupPointContactsRetained':True,'beforePolygonCount':len(b.geoms),'afterPolygonCount':len(a.geoms)})
projection={'definition':proj,'units':'metre','executedWith':'pyproj Transformer.from_crs EPSG:4326 to LAEA, always_xy=True; shapely transform','geographicExtent':[50,69.45,70,77.4],'scaleDenominator':10000000,'dpi':300,'metresPerPixel':10000000*.0254/300,'physicalScreenScaleCalibrated':False,'purpose':'Nominal NE 1:10M display comparison only, not historical survey accuracy.'};write('projection-evidence.json',projection)
write('geometry-proof.json',{'status':'passed-three-combined-candidates','reviewRevision':x['revision'],'projection':projection,'targets':rows,'novaDonorCount':757,'vayDonorCount':52,'combinedDonorCount':809,'donorIndexOverlap':[],'combinedDonorValid':True,'sourceWritten':False,'limits':['No full catalog or worldwide historical topology validation performed.','Full candidate validity and exact coordinate preservation are checked only for the three selected source versions.','Original historical dates, territorial interpretations and unproven tiny-islet title caveats remain.']})
win=box(50,69.45,70,77.4);pb=tr(win).bounds;mpp=projection['metresPerPixel'];pw=math.ceil((pb[2]-pb[0])/mpp)+60;H=math.ceil((pb[3]-pb[1])/mpp)+130;im=Image.new('RGB',(pw*3,H),'white');draw=ImageDraw.Draw(im);cx=(pb[0]+pb[2])/2;cy=(pb[1]+pb[3])/2
old=shape(x['rows'][0]['before']);new=shape(x['rows'][0]['after'])
for k,(label,geoms) in enumerate([('Before: 7 legacy group components',[(old,'#2566ad')]),('Paired candidate: all 809 modern components',[(new,'#d96e0c')]),('Overlay: old blue / combined orange',[(old,'#2566ad'),(new,'#d96e0c')])]):
 ox=pw*(k+.5);oy=H/2+8;draw.text((pw*k+10,25),label,fill='black')
 def plot(g,c):
  if g.is_empty:return
  if g.geom_type=='Polygon':
   for ring in [g.exterior,*g.interiors]:draw.line([(ox+(a-cx)/mpp,oy-(b-cy)/mpp) for a,b in ring.coords],fill=c,width=1)
  elif hasattr(g,'geoms'):
   for q in g.geoms:plot(q,c)
 for g,c in geoms:plot(tr(g.intersection(win)),c)
 draw.line([(pw*k+20,H-55),(pw*k+20+100000/mpp,H-55)],fill='black',width=2);draw.text((pw*k+20,H-50),'100 km',fill='black')
draw.text((10,5),'Combined Novaya Zemlya + Vaygach/Yugorsky coast, all selected parent/constituent dates; candidate only',fill='black');draw.text((10,H-22),'Nominal 1:10M / 300 dpi, same LAEA projection and viewport. All components checked by ledger, not display visibility.',fill='black');im.save(O/'combined-source-scale.png')
print(json.dumps({'status':'passed-three-combined-candidates','donors':809,'targets':rows,'imageSize':im.size}))
