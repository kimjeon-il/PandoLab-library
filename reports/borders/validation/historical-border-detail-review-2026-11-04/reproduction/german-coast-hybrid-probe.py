import json
from pathlib import Path
import shapely
from shapely.geometry import shape
from shapely.ops import transform,unary_union
from pyproj import Transformer
d=json.loads(Path('build-native/territorial-recipe/german-coast-selected-geos313-oracle.json').read_text(encoding='utf8'))['input']
p=Transformer.from_crs('EPSG:4326','EPSG:3035',always_xy=True).transform;q=Transformer.from_crs('EPSG:3035','EPSG:4326',always_xy=True).transform
clean=lambda g:g if g.is_valid else g.buffer(0)
H=transform(p,clean(shape(d['historical'])));T=transform(p,clean(unary_union([clean(shape(x)) for x in d['modern']])))
from shapely.geometry import box
sea=transform(p,unary_union([box(4.5,52.7,11.5,56.7),box(8,52.7,24,56.7)]));z=T.boundary.intersection(sea).buffer(12000);r=clean(H.difference(z).union(T.intersection(z).intersection(H.buffer(12000))))
ih,id=[transform(p,clean(shape(d[x]))) for x in ['helgoland','dune']];r=clean(r.difference(ih.buffer(5000).union(id.buffer(5000))).union(ih).union(id))
w=transform(q,r)
zone_geo=transform(q,z.buffer(1));print('zone inverse',zone_geo.is_valid,shapely.is_valid_reason(zone_geo),flush=True)
if not zone_geo.is_valid:zone_geo=shapely.make_valid(zone_geo)
wg=shapely.make_valid(w)
refined=clean(shape(d["historical"]).difference(zone_geo).union(wg.intersection(zone_geo)))
back=transform(p,refined)
print('refined valid',refined.is_valid,'metric valid',back.is_valid,'type',refined.geom_type,flush=True)
if not back.is_valid:back=shapely.make_valid(back)
print('outside km2',H.symmetric_difference(back).difference(z.buffer(1)).area/1e6,'source delta km2',r.symmetric_difference(back).area/1e6,'hausdorff m',r.boundary.hausdorff_distance(back.boundary),flush=True)

print('geo outside square degrees',shape(d['historical']).symmetric_difference(refined).difference(zone_geo).area,flush=True)
print('geo fixed',refined.is_valid,'types',[g.geom_type for g in refined.geoms] if hasattr(refined,'geoms') else [],flush=True)
polys=[g for g in refined.geoms if g.geom_type=='Polygon'] if refined.geom_type=='GeometryCollection' else [refined]
polygon_only=unary_union(polys)
print('polygon-only',polygon_only.geom_type,polygon_only.is_valid,'outside wgs diff',shape(d['historical']).symmetric_difference(polygon_only).difference(zone_geo).area,flush=True)
back=transform(p,polygon_only)
if not back.is_valid:back=shapely.make_valid(back)
print('polygon-only delta km2',r.symmetric_difference(back).area/1e6,'hausdorff m',r.boundary.hausdorff_distance(back.boundary),flush=True)
