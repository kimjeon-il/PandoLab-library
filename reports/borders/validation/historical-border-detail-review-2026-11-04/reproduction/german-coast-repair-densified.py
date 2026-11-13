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
for name,fixed in [('buffer0',w.buffer(0)),('make_valid',shapely.make_valid(w))]:
 back=transform(p,fixed)
 print(name,'wgs valid',fixed.is_valid,'reprojected valid',back.is_valid,flush=True)
 if not back.is_valid:back=shapely.make_valid(back)
 print(name,'diff area km2',r.symmetric_difference(back).area/1e6,'boundary hausdorff meters',r.boundary.hausdorff_distance(back.boundary),'densified hausdorff meters',shapely.hausdorff_distance(r.boundary,back.boundary,densify=.1),'source areas',r.area/1e6,back.area/1e6,flush=True)

