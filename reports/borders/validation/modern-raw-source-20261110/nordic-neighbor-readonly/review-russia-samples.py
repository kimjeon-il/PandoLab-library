import json,pathlib,subprocess,sqlite3,hashlib
from osgeo import ogr
p=pathlib.Path(__file__).parent;current=ogr.CreateGeometryFromJson(subprocess.check_output(['C:/Program Files/nodejs/node.exe',str(p/'emit-current-geometry.mjs'),'RUS']).decode())
c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
points=[('Simferopol Crimea interior',34.1,44.95),('Kunashir interior',145.85,44.05),('Iturup interior',147.85,45.2)]
out=[]
for label,x,y in points:
 pt=ogr.Geometry(ogr.wkbPoint);pt.AddPoint_2D(x,y);owners=[]
 for row in c.execute('select t.WP_ID,t.WP_Name,t.GENC_3,t.WP_PAR_ID,t.Map_Disp,t.Show_Disp,t.geom from DoS_WP_11_4 t join rtree_DoS_WP_11_4_geom r on t.fid=r.id where r.minx<=? and r.maxx>=? and r.miny<=? and r.maxy>=?',(x,x,y,y)):
  b=row['geom'];g=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:])
  if g.Contains(pt):owners.append({k:row[k] for k in ['WP_ID','WP_Name','GENC_3','WP_PAR_ID','Map_Disp','Show_Disp']})
 out.append({'sample':label,'longitude':x,'latitude':y,'existingCurrentRussiaContains':bool(current.Contains(pt)),'rawContainingFeatures':owners});print(json.dumps(out[-1]),flush=True)
(p/'russia-political-scope-samples.json').write_text(json.dumps({'scope':'Interior-point geometry attribution evidence only; no sovereignty determination and not an exhaustive disputed-territory survey','samples':out},indent=2)+'\n')

