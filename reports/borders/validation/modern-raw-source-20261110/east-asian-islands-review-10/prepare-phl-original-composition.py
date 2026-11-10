import sqlite3,json,pathlib,hashlib
from osgeo import ogr
ogr.UseExceptions()
p=pathlib.Path(__file__).parent
source=pathlib.Path(json.loads((p/'PHL-raw-proof.json').read_text())['sourceFile'])
c=sqlite3.connect(source.as_uri()+'?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
def read(wp):
 r=dict(c.execute('select * from DoS_WP_11_4 where WP_ID=?',(wp,)).fetchone());b=r.pop('geom');g=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);return r,b,g
country,cb,cg=read('4a73e5db-5386-42a6-81c9-f94f46d3fad3')
islands,ib,ig=read('4ac4f563-db48-4b0a-a528-e45d1dc047d4');c.close()
indices=[9,11,12,21]
result=ogr.Geometry(ogr.wkbMultiPolygon)
for i in range(cg.GetGeometryCount()):result.AddGeometry(cg.GetGeometryRef(i))
selected=[]
for i in indices:
 g=ig.GetGeometryRef(i);assert g.IsValid() and cg.Intersection(g).Area()==0
 result.AddGeometry(g);selected.append({'rawComponentIndex':i,'wkbSha256':hashlib.sha256(bytes(g.ExportToWkb())).hexdigest()})
assert result.IsValid()
geom=json.loads(result.ExportToJson(options=['COORDINATE_PRECISION=30','SIGNIFICANT_FIGURES=17']))
assert bytes(ogr.CreateGeometryFromJson(json.dumps(geom)).ExportToWkb())==bytes(result.ExportToWkb())
for i in range(cg.GetGeometryCount()):assert bytes(result.GetGeometryRef(i).ExportToWkb())==bytes(cg.GetGeometryRef(i).ExportToWkb())
for j,i in enumerate(indices):assert bytes(result.GetGeometryRef(cg.GetGeometryCount()+j).ExportToWkb())==bytes(ig.GetGeometryRef(i).ExportToWkb())
out=p/'PHL-original-with-approved-islands.geojson';out.write_text(json.dumps({'type':'Feature','id':'state:PHL','properties':country,'geometry':geom},separators=(',',':'))+'\n',encoding='utf8')
proof={'status':'candidate-only-not-applied','sourceFile':str(source),'rawLayer':'DoS_WP_11_4','countryWP_ID':country['WP_ID'],'countryBlobSha256':hashlib.sha256(cb).hexdigest(),'spratlyWP_ID':islands['WP_ID'],'spratlyBlobSha256':hashlib.sha256(ib).hexdigest(),'selectedComponents':selected,'countryProperties':country,'spratlyProperties':islands,'originalCountryComponentsPreserved':True,'originalSelectedIslandComponentsPreserved':True,'rawCoordinateRoundtrip':True,'simplification':False,'polygonCount':result.GetGeometryCount(),'geometryValid':True,'candidateSha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'requiresBeforeApply':'Confirm selected original components map unambiguously to approved PHL donor and not other recipients.'}
(p/'PHL-original-composition-proof.json').write_text(json.dumps(proof,indent=2)+'\n',encoding='utf8');print(json.dumps(proof))
