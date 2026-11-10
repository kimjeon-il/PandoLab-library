import sys,json,math,base64,io,zipfile
from pathlib import Path
from shapely.geometry import shape,Polygon,MultiPolygon,box
from shapely.ops import unary_union,transform
from shapely.validation import explain_validity
from pyproj import Transformer,Geod
from PIL import Image,ImageDraw
x=json.load(sys.stdin);out=Path(x['out']);write=lambda n,v:(out/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
r=box(*x['scope']);don=shape(x['donorGeometry']);indices=x['donorIndices'];group=MultiPolygon([don.geoms[i] for i in indices]);ug=unary_union(group)
actual=[i for i,p in enumerate(don.geoms) if r.intersects(p)]
assert actual==indices and all(r.covers(don.geoms[i]) for i in actual)
assert group.is_valid and len(group.geoms)==18
proof=[];oldgroups=[]
for row in x['selected']:
 before=shape(row['geometry']);after=shape(row['candidate']);old=MultiPolygon([before.geoms[i] for i in row['oldIndices']]);oldgroups.append(old)
 rest=unary_union([p for i,p in enumerate(before.geoms) if i not in row['oldIndices']]);expected=unary_union([rest,ug])
 assert after.is_valid,explain_validity(after)
 assert not ug.intersects(rest)
 assert after.symmetric_difference(expected).is_empty
 oldcoords=row['geometry']['coordinates'];candidatecoords=row['candidate']['coordinates']
 assert candidatecoords==[p for i,p in enumerate(oldcoords) if i not in row['oldIndices']]+[x['donorGeometry']['coordinates'][i] for i in indices]
 assert [i for i,p in enumerate(before.geoms) if r.intersects(p)]==row['oldIndices']
 proof.append({'entityId':row['entityId'],'versionId':row['versionId'],'validFrom':row['validFrom'],'validTo':row['validTo'],'beforeValid':before.is_valid,'candidateValid':after.is_valid,'oldIndices':row['oldIndices'],'donorCount':18,'retainedCoordinateArraysExact':True,'all18WholeDonorPolygonsAndAllRingsExact':True,'scopeCrossingPolygons':0,'newVsRetainedIntersectionAreaDegrees2':ug.intersection(rest).area,'newVsRetainedTouches':ug.intersects(rest),'candidateEqualsRetainedUnionCompleteDonorGroup':True,'parentConstituentSelectedGroupIdentical':True,'unchangedMainlandAndOtherIslands':True,'oldComponents':len(old.geoms),'newComponents':len(group.geoms),'oldHoles':sum(len(p.interiors) for p in old.geoms),'newHoles':sum(len(p.interiors) for p in group.geoms)})
assert all(old.equals(oldgroups[0]) for old in oldgroups)
ziplineage=[]
if x.get('originalZipBase64'):
 z=zipfile.ZipFile(io.BytesIO(base64.b64decode(x['originalZipBase64'])))
 for name in ['geometry-v2/assembly/ussr-four-founders.normalized-provisional.geojson','geometry-v2/assembly/ussr-four-founders.display-10m-provisional.geojson']:
  fc=json.loads(z.read(name))
  for f in fc['features']:
   if f.get('id') not in ['state:soviet-union','state:soviet-union-russian-sfsr']:continue
   ps=[p for p in shape(f['geometry']).geoms if r.intersects(p)];g=MultiPolygon(ps);assert g.equals(oldgroups[0]);ziplineage.append({'entry':name,'entityId':f['id'],'components':len(ps),'equalsCurrentOldGroup':True})
proj='+proj=laea +lat_0=69.1 +lon_0=49.2 +datum=WGS84 +units=m +no_defs'
t=Transformer.from_crs('EPSG:4326',proj,always_xy=True);aa=transform(t.transform,oldgroups[0]);bb=transform(t.transform,group);delta=aa.symmetric_difference(bb)
projection={'definition':proj,'units':'metre','scaleDenominator':10000000,'dpi':300,'metresPerPixel':10000000*.0254/300,'actualExecution':'pyproj Transformer.from_crs(EPSG:4326, definition, always_xy=True); shapely.ops.transform','oldProjectedAreaKm2':aa.area/1e6,'donorProjectedAreaKm2':bb.area/1e6,'symmetricDifferenceAreaKm2':delta.area/1e6,'screenPhysicalScaleCalibrated':False,'purpose':'Nominal source-scale comparison. Modern display-coast update, not measured historical positional accuracy.'}
write('projection-evidence.json',projection)
write('topology-proof.json',{'schemaVersion':1,'sourceRevision':x['sourceRevision'],'status':'passed-for-three-source-candidates-only','donorGroupValid':True,'scopeContainsAllIntersectingDonorComponents':True,'donorIndices':indices,'sizeThreshold':None,'omittedDonorComponents':0,'sameOldGroupAll3Versions':True,'sameNewGroupAll3Versions':True,'originalApproved1922MasterAndDisplayLineage':ziplineage,'targets':proof,'limits':['This does not certify the entire historical USSR reconstruction or runtime.','Original Caspian, Aral, Arctic claim exceptions and mainland coordinates are untouched.','Modern physical coast is reused at display scope; exact coast location in 1922 is not established.','Inherited small-island title caveat remains; state-level membership of the named Kolguyev group is independently supported by documentary administration evidence.']})
mpp=projection['metresPerPixel'];extent=unary_union([aa,bb]).bounds;cx=(extent[0]+extent[2])/2;cy=(extent[1]+extent[3])/2
im=Image.new('RGB',(930,330),'white');dr=ImageDraw.Draw(im)
for n,(label,geoms) in enumerate([('Historical: all 5 components',[(aa,'#1565a9')]),('Approved modern: all 18 components',[(bb,'#dc6b13')]),('Overlay: old blue / donor orange',[(aa,'#1565a9'),(bb,'#dc6b13')])]):
 ox=155+n*310;oy=155;dr.text((n*310+12,25),label,fill='black')
 for g,color in geoms:
  for p in g.geoms:
   for ring in [p.exterior,*p.interiors]:
    dr.line([(ox+(px-cx)/mpp,oy-(py-cy)/mpp) for px,py in ring.coords],fill=color,width=1)
 dr.line([(n*310+55,270),(n*310+55+50000/mpp,270)],fill='black',width=2);dr.text((n*310+55,275),'50 km',fill='black')
dr.text((12,5),'Kolguyev: identical group in RSFSR 1922, USSR 1922 and USSR 1925-1929; candidates only',fill='black')
dr.text((12,305),'Nominal 1:10M at 300 dpi. No island-size cutoff. Tiny components verified by exact coordinate ledger.',fill='black');im.save(out/'kolguyev-source-scale.png')
# Vaygach is only a held candidate: preserve every modern component, do not hide coastal conflicts.
vr=box(58.1,69.5,60.9,70.65);vix=[i for i,p in enumerate(don.geoms) if vr.covers(p)];first=x['selected'][0];b=shape(first['geometry']);oldix=[i for i,p in enumerate(b.geoms) if vr.covers(p)];rest=unary_union([p for i,p in enumerate(b.geoms) if i not in oldix]);conflicts=[]
for i in vix:
 q=don.geoms[i].intersection(rest)
 if not q.is_empty:conflicts.append({'donorIndex':i,'intersectionAreaDegrees2':q.area,'bbox':list(q.bounds)})
write('held-candidates.json',{'sourceRevision':x['sourceRevision'],'vaygach':{'status':'hold-for-linked-mainland-contact-review','allWholeModernIndices':vix,'count':len(vix),'conflictsWithUnchangedHistoricalGeometry':conflicts,'doNotOmitConflictingComponents':True,'reason':'Complete island-region donor group intersects retained historical mainland geometry. Detached-only independent replacement is not yet valid.'},'novayaZemlya':{'status':'not-prepared','reason':'Named archipelago has supporting administration history, but complete modern component membership and nonintersection ledger were not completed. Do not substitute only the two large islands.'}})
print(json.dumps({'status':'passed','targets':len(proof),'donorComponents':18,'projection':projection,'vaygachConflicts':conflicts}))
