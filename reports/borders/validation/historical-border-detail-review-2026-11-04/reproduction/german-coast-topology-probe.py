import json,shapely
from pathlib import Path
from shapely.geometry import shape,box
from shapely.ops import unary_union,transform
from pyproj import Transformer
d=json.loads(Path('build-native/territorial-recipe/german-coast-selected-geos313-oracle.json').read_text(encoding='utf8'))['input']
p=Transformer.from_crs('EPSG:4326','EPSG:3035',always_xy=True).transform;q=Transformer.from_crs('EPSG:3035','EPSG:4326',always_xy=True).transform
clean=lambda g:g if g.is_valid else g.buffer(0)
h=clean(shape(d['historical']));t=clean(unary_union([clean(shape(x)) for x in d['modern']]))
H=transform(p,h);T=transform(p,t)
sea=transform(p,unary_union([box(4.5,52.7,11.5,56.7),box(8,52.7,24,56.7)]));z=T.boundary.intersection(sea).buffer(12000)
patch=T.intersection(z).intersection(H.buffer(12000)); result=clean(H.difference(z).union(patch))
for name,g in [('historical',h),('historical roundtrip',transform(q,H)),('metric',result),('after coast inverse',transform(q,result))]: print(name,g.is_valid,shapely.is_valid_reason(g),flush=True)
islands=[transform(p,clean(shape(d[x]))) for x in ['helgoland','dune']]
result=clean(result.difference(islands[0].buffer(5000).union(islands[1].buffer(5000))).union(islands[0]).union(islands[1]));w=transform(q,result)
print('after islands inverse',w.is_valid,shapely.is_valid_reason(w))
