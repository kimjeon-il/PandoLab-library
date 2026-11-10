import sqlite3,json,pathlib
from osgeo import ogr,gdal
gdal.PushErrorHandler('CPLQuietErrorHandler'); p=pathlib.Path(__file__).parent
inv=json.loads((p.parent/'modern-source-progress.json').read_text());byid={c['WP_ID']:r for r in inv['rows'] for c in r['rawCandidates']}
c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
codes=['BLZ','PAN','VEN','PNG','EGY','YEM','MRT','GNQ','GMB','VAT'];out=[]
def geom(b):return ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:])
for code in codes:
 r=next(r for r in inv['rows'] if r['entityId']=='state:'+code);key=r['rawCandidates'][0]['WP_ID'];a=c.execute('select * from DoS_WP_11_4 where WP_ID=?',(key,)).fetchone();g=geom(a['geom']);box=g.GetEnvelope();ns=[]
 for b in c.execute('select t.* from DoS_WP_11_4 t join rtree_DoS_WP_11_4_geom r on t.fid=r.id where r.maxx>=? and r.minx<=? and r.maxy>=? and r.miny<=?',(box[0],box[1],box[2],box[3])):
  if b['WP_ID']==key:continue
  h=geom(b['geom'])
  if not g.Intersects(h):continue
  z=g.Intersection(h);br=byid.get(b['WP_ID'],{});ns.append({'code':b['GENC_3'],'name':b['WP_Name'],'id':b['WP_ID'],'entityId':br.get('entityId'),'class':br.get('classification','unmapped'),'area':z.GetArea(),'length':z.Length()})
 out.append({'entityId':r['entityId'],'neighbors':ns});(p/'tail-adjacency-checkpoint.json').write_text(json.dumps(out,indent=2)+'\n');print(code,[(n['name'],n['area']) for n in ns],flush=True)
