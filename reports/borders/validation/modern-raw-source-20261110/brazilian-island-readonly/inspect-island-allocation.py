import pathlib,json,sqlite3,subprocess,hashlib
from osgeo import ogr,gdal
gdal.PushErrorHandler('CPLQuietErrorHandler');p=pathlib.Path(__file__).parent
c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
r=c.execute("select * from DoS_WP_11_4 where WP_ID='78b85cb6-71a1-4548-9dff-03045ef7cc96'").fetchone();b=r['geom'];island=ogr.CreateGeometryFromWkb(b[8+{0:0,1:32,2:48,3:48,4:64}[(b[3]>>1)&7]:]);env=island.GetEnvelope();cent=island.PointOnSurface();a=island.GetArea();out={'rawFeature':{k:r[k] for k in ['WP_ID','WP_Name','GENC_3','WP_PAR_ID','Map_Disp','Show_Disp','US_Recog']},'rawBlobSha256':hashlib.sha256(b).hexdigest(),'rawBounds':env,'rawAreaDegrees2':a,'interiorPoint':json.loads(cent.ExportToJson()),'currentCountryCoverage':[]};union=None
for code in ['BRA','URY','ARG']:
 data=subprocess.check_output(['C:/Program Files/nodejs/node.exe',str(p/'emit-current-geometry.mjs'),code]);g=ogr.CreateGeometryFromJson(data.decode());hits=[];candidate=ogr.Geometry(ogr.wkbMultiPolygon)
 for i in range(g.GetGeometryCount()):
  z=g.GetGeometryRef(i);bb=z.GetEnvelope()
  if bb[1]<env[0] or bb[0]>env[1] or bb[3]<env[2] or bb[2]>env[3]:continue
  v=z.Intersection(island)
  if v and not v.IsEmpty():hits.append({'componentIndex':i,'intersectionAreaDegrees2':v.GetArea(),'countryComponentAreaDegrees2':z.GetArea(),'componentBounds':bb});candidate.AddGeometry(z)
 inter=g.Intersection(island);covered=inter.GetArea();union=inter if union is None else union.Union(inter)
 row={'code':code,'geometryPayloadSha256':hashlib.sha256(data).hexdigest(),'containsIslandInteriorPoint':bool(g.Contains(cent)),'intersectionAreaDegrees2':covered,'fractionRawIslandCovered':covered/a,'intersectingComponents':hits};out['currentCountryCoverage'].append(row);print(json.dumps(row),flush=True);(p/'island-current-allocation.json').write_text(json.dumps(out,indent=2)+'\n')
out['rawIslandAreaNotCoveredByCurrentThreeDegrees2']=island.Difference(union).GetArea();out['scope']='Raw Brazilian Island footprint versus existing approved current BRA/URY/ARG geometry; no ownership determination or source edits.';(p/'island-current-allocation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='currentCountryCoverage'}))
