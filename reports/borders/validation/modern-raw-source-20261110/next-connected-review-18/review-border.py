import pathlib,json,sqlite3,subprocess,hashlib
from osgeo import ogr,gdal
gdal.PushErrorHandler('CPLQuietErrorHandler');p=pathlib.Path(__file__).parent
c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
raw={};old={};proof=[]
for code in ['PNG','IDN','TLS','MYS','BRN','THA']:
 row=c.execute('select * from DoS_WP_11_4 where GENC_3=?',(code,)).fetchone();b=row['geom'];raw[code]=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);data=subprocess.check_output(['C:/Program Files/nodejs/node.exe',str(p/'emit-current-geometry.mjs'),code]);payload=json.loads(data);old[code]=ogr.CreateGeometryFromJson(data.decode());proof.append({'code':code,'rawBlobSha256':hashlib.sha256(b).hexdigest(),'oldPayloadSha256':hashlib.sha256(data).hexdigest(),'rawValid':bool(raw[code].IsValid()),'rawComponents':raw[code].GetGeometryCount(),'oldComponents':old[code].GetGeometryCount()});print('loaded',code,flush=True)
(p/'input-proofs.json').write_text(json.dumps(proof,indent=2)+'\n')
def clip(g,region):
 out=ogr.Geometry(ogr.wkbMultiPolygon);env=region.GetEnvelope()
 for i in range(g.GetGeometryCount()):
  a=g.GetGeometryRef(i);b=a.GetEnvelope()
  if b[1]<env[0] or b[0]>env[1] or b[3]<env[2] or b[2]>env[3]:continue
  z=a.Intersection(region)
  if z.IsEmpty():continue
  if z.GetGeometryName()=='POLYGON':out.AddGeometry(z)
  else:
   for j in range(z.GetGeometryCount()):
    t=z.GetGeometryRef(j)
    if t.GetGeometryName()=='POLYGON':out.AddGeometry(t)
 return out
results=[]
for a,b,bounds in [('PNG','IDN',(140,-10,142,-2)),('TLS','IDN',(123,-10,128,-7)),('IDN','MYS',(108,-2,120,6)),('BRN','MYS',(113,3,116,6)),('MYS','THA',(99,5,103,8))]:
 x,y,X,Y=bounds;box=ogr.CreateGeometryFromWkt(f'POLYGON (({x} {y},{X} {y},{X} {Y},{x} {Y},{x} {y}))');ra,rb,oa,ob=[clip(z,box) for z in [raw[a],raw[b],old[a],old[b]]];inset=box.Buffer(-0.00001);boundary=ra.Boundary().Intersection(rb.Boundary()).Intersection(inset);corridor=boundary.Buffer(.01,8);baseline=ra.Union(rb);rec={'a':a,'b':b,'rawSharedLength':boundary.Length(),'rawOverlap':ra.Intersection(rb).GetArea(),'oldOverlap':oa.Intersection(ob).GetArea(),'scope':'0.01 degree corridor around shared raw border; regional clip artificial edges excluded','directions':[]}
 for aa,bb,g,h in [(a,b,ra,ob),(b,a,rb,oa)]:
  rec['directions'].append({'raw':aa,'existing':bb,'corridorOverlap':g.Intersection(h).Intersection(corridor).GetArea(),'corridorGapVersusRawUnion':baseline.Difference(g.Union(h)).Intersection(corridor).GetArea(),'rawBorderNotCoincidentWithExisting':boundary.Difference(h.Boundary()).Length()})
 results.append(rec);(p/'mixed-border-results.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(rec),flush=True)
