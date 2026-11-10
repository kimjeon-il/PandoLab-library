import pathlib,json,sqlite3,subprocess,hashlib
from osgeo import ogr
p=pathlib.Path(__file__).parent;report=json.loads((p/'VNM-supplemental-set-proof.json').read_text());c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);b=c.execute("select geom from DoS_WP_11_4 where WP_ID='4ac4f563-db48-4b0a-a528-e45d1dc047d4'").fetchone()[0];raw=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);checks=[]
for code in ['TWN','PHL','CHN','VNM']:
 data=subprocess.check_output(['C:/Program Files/nodejs/node.exe',str(p/'emit-latest-peer.mjs'),code]);g=ogr.CreateGeometryFromJson(data.decode());hits=[]
 for i in [2,3,6,10]:
  a=raw.GetGeometryRef(i)
  if a.Intersects(g):hits.append({'rawSpratly':i,'area':a.Intersection(g).GetArea()})
 checks.append({'code':code,'currentPayloadSha':hashlib.sha256(data).hexdigest(),'contacts':hits})
report['latestCanonicalPeerCheck']={'revision':'85464e0ba06fe43a0e67c9095807d260e5c5ecef','rows':checks,'outsideRecipientContacts':[r for r in checks if r['code']!='VNM' and r['contacts']]};(p/'VNM-supplemental-set-proof.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report['latestCanonicalPeerCheck']))
