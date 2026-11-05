import json
from pathlib import Path
from osgeo import ogr
ogr.UseExceptions();R=Path('D:/dev/worktrees/gis');d=json.loads(Path('display-250.json').read_text());rows=[]
for key,p in [('DEU','tools/historical-library/working/german-empire-1914-base.geojson'),('AH','tools/historical-library/working/austro-hungarian-empire-1914-base.geojson')]:
 j=json.loads((R/p).read_text());g=(j.get('features')or[j])[0]['geometry'];a=ogr.CreateGeometryFromJson(json.dumps(g));b=ogr.CreateGeometryFromJson(json.dumps(d[key]));retained=[]
 for i in range(1,a.GetGeometryCount()):
  part=a.GetGeometryRef(i);pt=part.PointOnSurface();assert b.Intersects(pt),(key,i);retained.append({'component':i,'interiorPoint':list(pt.GetPoint()[:2]),'retained':True,'sourceDerivedProbe':True})
 rows.append({'entity':key,'originalNonMainComponents':len(retained),'retainedInteriorProbes':retained})
Path('important-islands-proof.json').write_text(json.dumps({'method':'Source-derived interior probes verify original island/component presence; these are preservation checks, not independent historical positional controls. German duplicate component 1 remains covered by main component 0; removing its duplicate does not remove its land.', 'rows':rows},indent=2));print('All original non-main component interior probes remain in final display derivatives.')
