import sqlite3,json,pathlib,hashlib
from osgeo import ogr
import sys;code=sys.argv[1];assert code in ["BEL","LUX"];ogr.UseExceptions();p=pathlib.Path(__file__).parent;raw=pathlib.Path(r'D:\dev\PandoLab-library-data\reports\.edits\gis\borders\validation\ne-world-map-rebase-2026-11-08\historical-modern-reuse-local-20261109\c-raw-versus-prepared-audit\official-original-preserved\WorldPolygons11_4.gpkg')
c=sqlite3.connect(raw.as_uri()+'?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
r=dict(c.execute('select * from DoS_WP_11_4 where GENC_3=?',(code,)).fetchone());c.close();b=r.pop('geom');g=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);geom=json.loads(g.ExportToJson(options=["COORDINATE_PRECISION=20","SIGNIFICANT_FIGURES=17"]));valid=g.IsValid(); assert bytes(ogr.CreateGeometryFromJson(json.dumps(geom)).ExportToWkb())==bytes(g.ExportToWkb()), "Raw WKB roundtrip changed coordinates"
def count(g):return g.GetPointCount()+sum(count(g.GetGeometryRef(i)) for i in range(g.GetGeometryCount()))
result={'type':'Feature','id':'state:'+code,'properties':r,'geometry':geom};out=p/(code+'-raw-candidate.geojson');out.write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf8')
proof={'entityId':'state:'+code,'sourceFile':str(raw),'rawLayer':'DoS_WP_11_4','rawWP_ID':r['WP_ID'],'rawBlobSha256':hashlib.sha256(b).hexdigest(),'rawCoordinatesUnmodified':True,'simplification':False,'rounded':False,'geometryValid':valid,'polygonCount':g.GetGeometryCount(),'coordinateCount':count(g),'holes':sum(max(0,g.GetGeometryRef(i).GetGeometryCount()-1) for i in range(g.GetGeometryCount())),'candidateSha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'sourceWrite':False};(p/(code+'-raw-proof.json')).write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))









