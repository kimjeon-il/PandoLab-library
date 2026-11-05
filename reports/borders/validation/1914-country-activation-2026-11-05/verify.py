import json,hashlib,math
from pathlib import Path
from osgeo import ogr,osr,gdal
ogr.UseExceptions();osr.UseExceptions();O=Path('.');root=Path('D:/dev/worktrees/gis');masters=json.loads((O/'masters.json').read_text());norm=json.loads((O/'normalized.json').read_text());display=json.loads((O/'display-250.json').read_text())
src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);dst=osr.SpatialReference();dst.ImportFromEPSG(3035);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);tx=osr.CoordinateTransformation(src,dst)
def g(v):return ogr.CreateGeometryFromJson(json.dumps(v))
def project(v):
 z=g(v);z.Transform(tx);return z
def area(v):return project(v).GetArea()/1e6
def count(v):return sum(len(r)for p in v['coordinates']for r in p)
def components(v):return len(v['coordinates'])
metrics={}; projected={}
controls={'DEU':{'Berlin':[13.405,52.52,True],'Strasbourg':[7.7521,48.5734,True],'Metz':[6.18,49.12,True],'Poznan':[16.925,52.406,True],'Danzig':[18.646,54.352,True],'Konigsberg':[20.51,54.71,True],'Memel':[21.14,55.7,True],'Haderslev':[9.49,55.25,True],'Eupen':[6.04,50.63,True],'Helgoland-component-presence-source-derived':[7.885362101180695,54.18004525,True],'Dune-component-presence-source-derived':[7.910270327356747,54.1856332,True],'Warsaw':[21.012,52.229,False],'Prague':[14.437,50.075,False],'Luxembourg':[6.13,49.61,False]},'AH':{'Vienna':[16.3738,48.2082,True],'Prague':[14.4378,50.0755,True],'Budapest':[19.0402,47.4979,True],'Sarajevo':[18.4131,43.8563,True],'Zagreb':[15.9819,45.815,True],'Trento':[11.1217,46.0679,True],'Trieste':[13.7768,45.6495,True],'Lviv':[24.0316,49.8429,True],'Belgrade':[20.4489,44.7866,False],'Venice':[12.3155,45.4408,False]},'SERBIA':{'Belgrade':[20.4489,44.7866,True],'Nis':[21.8958,43.3209,True],'Skopje':[21.4314,41.9981,True],'Pristina':[21.1662,42.6629,True],'Bitola':[21.3347,41.0314,True],'Pljevlja':[19.3589,43.3567,False],'Tirana':[19.8187,41.3275,False]}}
for k,v in display.items():
 z=g(v);assert z.IsValid();p=project(v);n=project(norm[k]);d=n.SymDifference(p);tests=[]
 for name,(x,y,expected)in controls[k].items():
  pt=ogr.Geometry(ogr.wkbPoint);pt.AddPoint_2D(x,y);actual=bool(z.Intersects(pt));tests.append({'name':name,'point':[x,y],'expected':expected,'actual':actual});assert actual==expected,(k,name)
 metrics[k]={'valid':True,'components':components(v),'holes':sum(len(p)-1 for p in v['coordinates']),'masterPoints':count(masters[k]),'normalizedPoints':count(norm[k]),'displayPoints':count(v),'areaKm2':p.GetArea()/1e6,'generalizationSymDifferenceKm2':d.GetArea()/1e6,'controls':tests};assert components(v)==components(norm[k]);projected[k]={'normalized':json.loads(n.ExportToJson()),'display':json.loads(p.ExportToJson())}
# GEOS operations on exact shared runs; no independently simplified counterpart.
pairs={}
for x,y in [('DEU','AH'),('AH','SERBIA')]:
 a,b=g(display[x]),g(display[y]);inter=a.Intersection(b);line=a.Boundary().Intersection(b.Boundary());met=line.Clone();met.Transform(tx)
 old=g(norm[x]).Union(g(norm[y]));new=a.Union(b);assert new.IsValid();assert inter.GetArea()==0;assert line.GetGeometryName()=='LINESTRING';pairs[x+'-'+y]={'overlapKm2':area(json.loads(inter.ExportToJson())),'sharedPathContinuous':True,'sharedLengthMetres3035':met.Length(),'unionValid':True,'sharedPoints':line.GetPointCount(),'sharedEndpoints':[list(line.GetPoint(0)[:2]),list(line.GetPoint(line.GetPointCount()-1)[:2])]}
# NE donor comparison is cartographic, not evidence of historical ownership.
for code in ['DEU','AUT','SRB','CZE','CHE','HUN']:
 e=json.loads((root/f'assets/data/territorial-entities/source/countries/state-{code}.json').read_text());v=e['geometryVersions'][0]['geometry'];projected['NE-'+code]={'display':json.loads(project(v).ExportToJson())}
proof={'runtime':{'gdal':gdal.VersionInfo('--version'),'GEOS':'3.15.0'},'projection':{'definition':'EPSG:3035','units':'metre','axisOrder':'traditional GIS longitude,latitude','operation':tx.GetInverse()is not None},'scaleDenominator':10000000,'method':'DP on each exact shared TopoJSON arc in EPSG:3035, retaining original coordinate pairs. Existing NE reference arcs and short closed island arcs preserved intact; ten named overlay remnants closed by common Boolean operations (see display-closure-ledger.json).','parameters':{'toleranceMetres':250,'smallClosedArcPreservationLengthMetres':100000,'quantization':False,'coordinateRounding':None},'metrics':metrics,'pairs':pairs,'fixedAnchors':{'DEU':[[19.1577366,50.2293859],[9.547482,47.534547]],'AH':[[10.452726,46.530948],[19.226442,43.527993],[22.472058,44.71405]],'SERBIA':[[19.226442,43.527993],[22.472058,44.71405]]},'limitations':['Technical topology and generalization only; not independent historical positional accuracy.','1914-07-31 DEU and 1914-07-28 AH/Serbia snapshots; no inferred geometry period.','Modern coastal/lake proxies retained under policy; detailed historical shoreline not verified.','Serbia-Montenegro treaty/gross route checked in archived report; detailed map overlays remain unverified and are not a current mandatory research gate.']}
# A fixed anchor must be present after simplification. Ensure required tripoint retained.
for k,anchors in proof['fixedAnchors'].items():
 pts={tuple(p)for pol in display[k]['coordinates']for ring in pol for p in ring}
 for p in anchors:assert tuple(p)in pts,(k,p)
(O/'topology-proof.json').write_text(json.dumps(proof,indent=2),encoding='utf8');(O/'projected.json').write_text(json.dumps(projected),encoding='utf8');print(json.dumps({'metrics':{k:{a:b for a,b in v.items()if a!='controls'}for k,v in metrics.items()},'pairs':pairs},indent=2))


