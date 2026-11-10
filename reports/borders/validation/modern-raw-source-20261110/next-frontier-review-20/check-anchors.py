import pathlib,json,sqlite3,subprocess,hashlib
from osgeo import ogr,gdal
gdal.PushErrorHandler('CPLQuietErrorHandler');p=pathlib.Path(__file__).parent
c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
raw={};old={};proof=[]
for code in ['MMR','BGD']:
 row=c.execute('select * from DoS_WP_11_4 where GENC_3=?',(code,)).fetchone();b=row['geom'];raw[code]=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);data=subprocess.check_output(['C:/Program Files/nodejs/node.exe',str(p/'emit-current-geometry.mjs'),code]);payload=json.loads(data);old[code]=ogr.CreateGeometryFromJson(data.decode());proof.append({'code':code,'rawBlobSha256':hashlib.sha256(b).hexdigest(),'oldPayloadSha256':hashlib.sha256(data).hexdigest(),'rawValid':bool(raw[code].IsValid()),'rawComponents':raw[code].GetGeometryCount(),'oldComponents':old[code].GetGeometryCount()});print('loaded',code,flush=True)
(p/'anchor-input-proofs.json').write_text(json.dumps(proof,indent=2)+'\n')
def clip(g,region):
 out=ogr.Geometry(ogr.wkbMultiPolygon);env=region.GetEnvelope()
 for a in ([g] if g.GetGeometryName()=='POLYGON' else [g.GetGeometryRef(i) for i in range(g.GetGeometryCount())]):
  b=a.GetEnvelope()
  if b[1]<env[0] or b[0]>env[1] or b[3]<env[2] or b[2]>env[3]:continue
  z=a.Intersection(region)
  if z is None:raise RuntimeError('Intersection failed: '+gdal.GetLastErrorMsg())
  if z.IsEmpty():continue
  if z.GetGeometryName()=='POLYGON':out.AddGeometry(z)
  else:
   for j in range(z.GetGeometryCount()):
    t=z.GetGeometryRef(j)
    if t.GetGeometryName()=='POLYGON':out.AddGeometry(t)
 return out
box=ogr.CreateGeometryFromWkt('POLYGON ((91 20,94 20,94 23,91 23,91 20))');ra,rb,oa,ob=[clip(g,box) for g in [raw['MMR'],raw['BGD'],old['MMR'],old['BGD']]];inset=box.Buffer(-0.00001);rline=ra.Boundary().Intersection(rb.Boundary()).Intersection(inset);oline=oa.Boundary().Intersection(ob.Boundary()).Intersection(inset);common=rline.Intersection(oline);segments=[]
def lines(g):
 if g.GetGeometryName()=='LINESTRING':
  if g.Length()>0:segments.append({'length':g.Length(),'start':g.GetPoint_2D(0),'end':g.GetPoint_2D(g.GetPointCount()-1),'vertexCount':g.GetPointCount()})
 else:
  for i in range(g.GetGeometryCount()):lines(g.GetGeometryRef(i))
lines(common);report={'pair':['MMR','BGD'],'rawSharedLength':rline.Length(),'currentSharedLength':oline.Length(),'exactCommonLength':common.Length(),'exactCommonSegments':segments,'status':'anchor-feasibility-only-not-a-candidate','method':'Exact intersection of the two shared boundary line sets. No snap or tolerance. Endpoints are potential cut anchors, not permission to modify or proof of a valid ring splice.','next':'Choose two exact common vertices bracketing one changed connected arc; verify one-to-one path order on all four rings. Splice raw arc into both current rings with reverse orientations. Keep all nonselected coordinates/components unchanged and validate before any application.'};(p/'MMR-BGD-exact-anchor-feasibility.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'exactCommonLength':common.Length(),'segments':len(segments),'sample':segments[:6]}))
anchors={tuple(s[k]) for s in segments for k in ['start','end']};observations={str(x):{} for x in sorted(anchors)}
for label,g in [('rawMMR',raw['MMR']),('rawBGD',raw['BGD']),('currentMMR',old['MMR']),('currentBGD',old['BGD'])]:
 polys=[g] if g.GetGeometryName()=='POLYGON' else [g.GetGeometryRef(i) for i in range(g.GetGeometryCount())]
 for pi,poly in enumerate(polys):
  for ri in range(poly.GetGeometryCount()):
   ring=poly.GetGeometryRef(ri)
   for vi in range(ring.GetPointCount()):
    point=ring.GetPoint_2D(vi)
    if point in anchors:observations[str(point)].setdefault(label,[]).append({'polygon':pi,'ring':ri,'vertex':vi})
report['exactEndpointVertexMembership']=observations;report['anchorsPresentInAllFour']=sum(len(v)==4 for v in observations.values());(p/'MMR-BGD-exact-anchor-feasibility.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'anchorsPresentInAllFour':report['anchorsPresentInAllFour'],'observations':observations}))
