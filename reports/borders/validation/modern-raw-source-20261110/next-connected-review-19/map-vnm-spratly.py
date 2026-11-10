import json,pathlib,sqlite3,subprocess,hashlib
from osgeo import ogr
p=pathlib.Path(__file__).parent;c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
r=c.execute("select * from DoS_WP_11_4 where WP_ID='4ac4f563-db48-4b0a-a528-e45d1dc047d4'").fetchone();b=r['geom'];raw=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);data=subprocess.check_output(['C:/Program Files/nodejs/node.exe',str(p/'emit-current-geometry.mjs'),'VNM']);old=ogr.CreateGeometryFromJson(data.decode());matches=[]
def overlaps(a,b):
 x=a.GetEnvelope();y=b.GetEnvelope()
 if x[1]<y[0] or x[0]>y[1] or x[3]<y[2] or x[2]>y[3]:return 0
 return a.Intersection(b).GetArea()
for i in range(raw.GetGeometryCount()):
 a=raw.GetGeometryRef(i);hit=[]
 for j in range(old.GetGeometryCount()):
  z=old.GetGeometryRef(j);area=overlaps(a,z)
  if area>0:hit.append({'currentComponent':j,'overlapArea':area,'rawFraction':area/a.GetArea(),'currentBounds':z.GetEnvelope(),'currentContainsRawInterior':bool(z.Contains(a.PointOnSurface()))})
 if hit:matches.append({'rawComponent':i,'rawWkbSha256':hashlib.sha256(bytes(a.ExportToWkb())).hexdigest(),'rawBounds':a.GetEnvelope(),'rawArea':a.GetArea(),'currentMatches':hit})
 report={'status':'raw-to-current-mapping-only-prepared-index-verification-pending','rawBlobSha256':hashlib.sha256(b).hexdigest(),'rawWP_ID':r['WP_ID'],'approvedPreparedIndices':[0,1,2,4],'originalComponents':raw.GetGeometryCount(),'currentComponents':old.GetGeometryCount(),'rawComponentsChecked':i+1,'matches':matches};(p/'VNM-spratly-mapping-progress.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
