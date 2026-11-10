import sqlite3,json,pathlib
from osgeo import ogr
p=pathlib.Path(__file__).parent;raw=pathlib.Path(r'D:\dev\PandoLab-library-data\reports\.edits\gis\borders\validation\ne-world-map-rebase-2026-11-08\historical-modern-reuse-local-20261109\c-raw-versus-prepared-audit\official-original-preserved\WorldPolygons11_4.gpkg');c=sqlite3.connect(raw.as_uri()+'?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row;out=[]
for code,names in [('JPN',['Senkaku Islands','Liancourt Rocks']),('PHL',['Spratly Islands'])]:
 old=ogr.CreateGeometryFromJson((p/(code+'-before.geojson')).read_text());new=ogr.CreateGeometryFromJson(json.dumps(json.loads((p/(code+'-raw-candidate.geojson')).read_text())['geometry']))
 for name in names:
  r=c.execute('select WP_ID,geom from DoS_WP_11_4 where WP_Name=?',(name,)).fetchone();b=r['geom'];g=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);parts=[]
  for i in range(g.GetGeometryCount()):
   part=g.GetGeometryRef(i);pt=part.PointOnSurface();parts.append({'component':i,'point':json.loads(pt.ExportToJson()),'beforeCoversInterior':bool(old.Intersects(pt)),'rawCountryCoversInterior':bool(new.Intersects(pt))})
  out.append({'entity':code,'name':name,'sourceWP_ID':r['WP_ID'],'components':parts})
(p/'sensitive-island-coverage.json').write_text(json.dumps(out,indent=2));print(json.dumps([{'entity':x['entity'],'name':x['name'],'beforeCovered':sum(y['beforeCoversInterior']for y in x['components']),'rawCountryCovered':sum(y['rawCountryCoversInterior']for y in x['components']),'components':len(x['components'])}for x in out]))
