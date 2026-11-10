import json,pathlib,sqlite3,subprocess,hashlib
from osgeo import ogr,gdal
ogr.UseExceptions();gdal.PushErrorHandler('CPLQuietErrorHandler');p=pathlib.Path(__file__).parent;meta=json.loads((p/'source-metadata.json').read_text());codes=['IOT','SGS','FLK','TWN']
source=pathlib.Path('D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg');c=sqlite3.connect(source.as_uri()+'?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
def geom(b):return ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:])
def boxes(a,b):return not(a[1]<b[0] or a[0]>b[1] or a[3]<b[2] or a[2]>b[3])
def parts(g):return [g.GetGeometryRef(i) for i in range(g.GetGeometryCount())]
def intersect(a,b):
 if not boxes(a.GetEnvelope(),b.GetEnvelope()):return 0.0
 return a.Intersection(b).GetArea() if a.Intersects(b) else 0.0
donorPath=pathlib.Path('D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/display-review-final-authorized-candidate.geojson');donor=ogr.Open(str(donorPath));dl=donor.GetLayer();out=[]
for code in codes:
 mr=next(r for r in meta['rows'] if r['code']==code);desc=mr['descriptor'];v=desc['geometryVersions'][0];data=subprocess.check_output(['C:/Program Files/nodejs/node.exe',str(p/'emit-current-geometry.mjs'),code]);old=ogr.CreateGeometryFromJson(data.decode());row=c.execute('select * from DoS_WP_11_4 where GENC_3=?',(code,)).fetchone();blob=row['geom'];base=geom(blob);g=base.Clone();spratly=None;selection=[]
 if code=='TWN':
  sr=c.execute("select * from DoS_WP_11_4 where WP_ID='4ac4f563-db48-4b0a-a528-e45d1dc047d4'").fetchone();spratly=geom(sr['geom'])
  for i,sp in enumerate(parts(spratly)):
   matching=[j for j,op in enumerate(parts(old)) if intersect(sp,op)>0]
   if matching:
    selection.append({'rawComponentIndex':i,'rawComponentWkbSha256':hashlib.sha256(bytes(sp.ExportToWkb())).hexdigest(),'rawBounds':sp.GetEnvelope(),'rawAreaDegrees2':sp.GetArea(),'oldComponentIndices':matching,'oldContainsRawInteriorPoint':bool(old.Contains(sp.PointOnSurface())),'intersectionRawFraction':intersect(sp,old)/sp.GetArea()});g.AddGeometry(sp)
  (p/'TWN-spratly-mapping.json').write_text(json.dumps({'sourceWP_ID':sr['WP_ID'],'rawBlobSha256':hashlib.sha256(sr['geom']).hexdigest(),'approvedPreparedIndices':v['modernBoundarySupplement']['spratlyEffectiveControl']['componentIndices'],'selectedOriginalComponents':selection},indent=2)+'\n')
 oldmiss=[]
 for i,op in enumerate(parts(old)):
  matches=[j for j,rp in enumerate(parts(g)) if intersect(op,rp)>0]
  if not matches:oldmiss.append({'oldComponentIndex':i,'bounds':op.GetEnvelope(),'area':op.GetArea(),'point':json.loads(op.PointOnSurface().ExportToJson())})
 extras=[]
 for i,rp in enumerate(parts(g)):
  if not any(intersect(rp,op)>0 for op in parts(old)):
   extras.append({'rawComponentIndex':i,'bounds':rp.GetEnvelope(),'area':rp.GetArea(),'distanceToExistingDegrees':rp.Distance(old),'point':json.loads(rp.PointOnSurface().ExportToJson())})
 rec={'code':code,'descriptorSha256':mr['descriptorSha256'],'currentGeometryPayloadSha256':hashlib.sha256(data).hexdigest(),'sourceRevision':meta['pinRevision'],'descriptorParent':desc['parentEntityId'],'dates':[v['validFrom'],v['validTo']],'rawProperties':{k:row[k] for k in row.keys() if k!='geom'},'rawBlobSha256':hashlib.sha256(blob).hexdigest(),'rawWkbSha256':hashlib.sha256(bytes(base.ExportToWkb())).hexdigest(),'rawValid':bool(base.IsValid()),'composedValid':bool(g.IsValid()),'rawBounds':g.GetEnvelope(),'oldBounds':old.GetEnvelope(),'oldComponents':old.GetGeometryCount(),'rawBaseComponents':base.GetGeometryCount(),'candidateComponents':g.GetGeometryCount(),'oldComponentsUnmatched':oldmiss,'rawExtraComponents':extras,'rawOverlapOldFraction':g.Intersection(old).GetArea()/g.GetArea(),'selectedSpratlyComponents':selection,'rawPeerContacts':[],'approvedDonorOutsidePeerContacts':[]}
 box=g.GetEnvelope()
 for rr in c.execute('select t.* from DoS_WP_11_4 t join rtree_DoS_WP_11_4_geom r on t.fid=r.id where r.maxx>=? and r.minx<=? and r.maxy>=? and r.miny<=?',(box[0],box[1],box[2],box[3])):
  if rr['WP_ID']==row['WP_ID']:continue
  other=geom(rr['geom'])
  if code=='TWN' and rr['WP_ID']==sr['WP_ID']:
   remaining=ogr.Geometry(ogr.wkbMultiPolygon);selected={r['rawComponentIndex'] for r in selection}
   for i,z in enumerate(parts(other)):
    if i not in selected:remaining.AddGeometry(z)
   other=remaining
  if g.Intersects(other):
   z=g.Intersection(other);rec['rawPeerContacts'].append({'WP_ID':rr['WP_ID'],'code':rr['GENC_3'],'name':rr['WP_Name'],'area':z.GetArea(),'length':z.Length()})
 dl.SetSpatialFilterRect(box[0],box[2],box[1],box[3]);dl.ResetReading()
 for f in dl:
  if f.GetField('id')==code:continue
  other=f.GetGeometryRef()
  if g.Intersects(other):
   z=g.Intersection(other);rec['approvedDonorOutsidePeerContacts'].append({'id':f.GetField('id'),'area':z.GetArea(),'length':z.Length()})
 out.append(rec);(p/'flagged-islands-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:rec[k] for k in ['code','rawValid','composedValid','oldComponents','rawBaseComponents','candidateComponents','oldComponentsUnmatched','rawPeerContacts','approvedDonorOutsidePeerContacts']}));print('extras',code,len(extras),sorted(extras,key=lambda r:r['distanceToExistingDegrees'],reverse=True)[:5],flush=True)
