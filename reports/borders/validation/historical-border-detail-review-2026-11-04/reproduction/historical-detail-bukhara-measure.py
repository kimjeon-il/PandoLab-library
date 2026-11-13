from historical_detail_membership import *
from historical_detail_line_merge import merged
sp=load(base+'historical-detail-central-arc-patch-spec.json');coords=sp['bukhara']['replacement_coordinates_preserved_reference_only'];geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));h=geo({'type':'LineString','coordinates':coords});ne=load('assets/data/countries-ne-5.1.1.geojson');ng={f['id']:f['geometry'] for f in ne['features']};samples=[]
for name,extent,left,right in [('bukhara-west',[61.8,38.8,65.8,41.6],'UZB','TKM'),('bukhara-central',[65.5,38.8,68.2,41.1],'UZB','TJK'),('bukhara-east',[67.8,37.2,73.1,39.9],'TJK','KGZ')]:
 x0,y0,x1,y1=extent;box=geo({'type':'Polygon','coordinates':[[[x0,y0],[x1,y0],[x1,y1],[x0,y1],[x0,y0]]]});hs=merged(h.Intersection(box));ms=merged(geo(ng[left]).Boundary().Intersection(geo(ng[right]).Boundary()).Intersection(box));
 if not hs or not ms:print(name,'not comparable',len(hs),len(ms));continue
 historical=max(hs,key=lambda l:l.Length());modern=max(ms,key=lambda l:l.Length());definition=f'+proj=aeqd +lat_0={(y0+y1)/2} +lon_0={(x0+x1)/2} +datum=WGS84 +units=m +type=crs';src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);dst=osr.SpatialReference();dst.SetFromUserInput(definition);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);tr=osr.CoordinateTransformation(src,dst)
 def metric(g):
  p=g.Clone();p.Transform(tr);return [list(v[:2]) for v in p.GetPoints()]
 samples.append({'id':name,'metricCrs':definition,'projectionEvidence':'Existing OSGeo GDAL/PROJ transform executed; traditional XY','extent':extent,'historical':metric(historical),'work':metric(modern),'historicalParts':len(hs),'modernParts':len(ms),'modernCountries':[left,right],'scope':'Regional NE land-boundary context at same physical scale. Routes/ownership/endpoints differ; not historical accuracy, positional-error calibration or uniformly same landform','geographic':{'historical':json.loads(historical.ExportToJson()),'modern':json.loads(modern.ExportToJson())}})
json.dump({'schema':'pando-border-detail-samples-v1','samples':samples},open(base+'historical-detail-bukhara-metric-input.json','w'),indent=2)
