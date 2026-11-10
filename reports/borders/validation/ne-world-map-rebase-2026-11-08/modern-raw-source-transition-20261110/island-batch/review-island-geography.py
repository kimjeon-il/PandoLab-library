import pathlib,json,sqlite3
from osgeo import ogr
p=pathlib.Path(__file__).parent
raw=pathlib.Path(r'D:\dev\PandoLab-library-data\reports\.edits\gis\borders\validation\ne-world-map-rebase-2026-11-08\historical-modern-reuse-local-20261109\c-raw-versus-prepared-audit\official-original-preserved\WorldPolygons11_4.gpkg')
c=sqlite3.connect(raw.as_uri()+'?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
out=[]
for code in ['JAM','MDG']:
 f=json.loads((p/(code+'-raw-candidate.geojson')).read_text(encoding='utf8'));g=ogr.CreateGeometryFromJson(json.dumps(f['geometry']));old=ogr.CreateGeometryFromJson((p/(code+'-before.geojson')).read_text());box=g.GetEnvelope();checks=[]
 for row in c.execute('select t.WP_ID,t.WP_Name,t.GENC_3,t.geom from DoS_WP_11_4 t join rtree_DoS_WP_11_4_geom r on t.fid=r.id where r.maxx>=? and r.minx<=? and r.maxy>=? and r.miny<=?',(box[0],box[1],box[2],box[3])):
  if row['WP_ID']==f['properties']['WP_ID']:continue
  b=row['geom'];other=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);checks.append({'id':row['WP_ID'],'name':row['WP_Name'],'code':row['GENC_3'],'intersects':bool(g.Intersects(other))})
 out.append({'code':code,'rawBounds':box,'previousBounds':old.GetEnvelope(),'rawPolygonCount':g.GetGeometryCount(),'previousPolygonCount':old.GetGeometryCount(),'rawAreaSquareDegrees':g.GetArea(),'previousAreaSquareDegrees':old.GetArea(),'rawNeighbours':checks,'scope':'No geopolitical repartition; one independent LSIB feature with unchanged parent, all original polygons retained. Bounds/area are geographic degrees, not metric accuracy estimates.'})
(p/'island-batch-geographic-review.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

