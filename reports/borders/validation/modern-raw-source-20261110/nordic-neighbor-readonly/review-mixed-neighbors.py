import pathlib,json,sqlite3,subprocess,hashlib
from osgeo import ogr,gdal
gdal.PushErrorHandler('CPLQuietErrorHandler');p=pathlib.Path(__file__).parent
c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
box=ogr.CreateGeometryFromWkt('POLYGON ((20 59,34 59,34 72,20 72,20 59))')
def clip(g,region=box):
 env=region.GetEnvelope();out=ogr.Geometry(ogr.wkbMultiPolygon)
 for i in range(g.GetGeometryCount()):
  a=g.GetGeometryRef(i);b=a.GetEnvelope()
  if b[1]<env[0] or b[0]>env[1] or b[3]<env[2] or b[2]>env[3]:continue
  z=a.Intersection(region)
  if z is None or z.IsEmpty():continue
  if z.GetGeometryName()=='POLYGON':out.AddGeometry(z)
  else:
   for j in range(z.GetGeometryCount()):
    t=z.GetGeometryRef(j)
    if t.GetGeometryName()=='POLYGON':out.AddGeometry(t)
 return out
raw={};old={};proof=[]
for code in ['RUS','FIN','NOR']:
 row=c.execute('select * from DoS_WP_11_4 where GENC_3=?',(code,)).fetchone();b=row['geom'];g=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);raw[code]=clip(g);proof.append({'code':code,'WP_ID':row['WP_ID'],'gpkgBlobSha256':hashlib.sha256(b).hexdigest(),'rawComponentCount':g.GetGeometryCount(),'rawAreaDegrees2':g.GetArea()});del g,b
 current=subprocess.check_output(['C:/Program Files/nodejs/node.exe',str(p/'emit-current-geometry.mjs'),code]);old[code]=clip(ogr.CreateGeometryFromJson(current.decode('utf-8')));proof[-1]['currentPayloadSha256']=hashlib.sha256(current).hexdigest();print('loaded',code,flush=True)
(p/'nordic-input-proofs.json').write_text(json.dumps(proof,indent=2)+'\n')
results=[]
for code in ['FIN','NOR']:
 boundary=raw[code].Boundary().Intersection(raw['RUS'].Boundary())
 # Remove clipping-box edges; retain only shared real border inside an inset.
 inset=ogr.CreateGeometryFromWkt('POLYGON ((20.001 59.001,33.999 59.001,33.999 71.999,20.001 71.999,20.001 59.001))');boundary=boundary.Intersection(inset)
 corridor=boundary.Buffer(0.01,8)
 baseline=raw[code].Union(raw['RUS']);mixed=raw[code].Union(old['RUS'])
 gap=baseline.Difference(mixed).Intersection(corridor);overlap=raw[code].Intersection(old['RUS']).Intersection(corridor)
 rec={'code':code,'scope':'Raw shared land-border corridor 0.01 geographic degree buffer; external clipping edges excluded','rawSharedBoundaryLengthDegrees':boundary.Length(),'rawPairOverlapDegrees2':raw[code].Intersection(raw['RUS']).GetArea(),'existingPairOverlapDegrees2':old[code].Intersection(old['RUS']).GetArea(),'mixedPairCorridorOverlapDegrees2':overlap.GetArea(),'mixedPairCorridorGapVersusRawUnionDegrees2':gap.GetArea(),'rawBoundaryNotCoincidentWithExistingRussiaBoundaryDegrees':boundary.Difference(old['RUS'].Boundary()).Length()}
 results.append(rec);(p/'nordic-mixed-neighbor-review.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(rec),flush=True)

