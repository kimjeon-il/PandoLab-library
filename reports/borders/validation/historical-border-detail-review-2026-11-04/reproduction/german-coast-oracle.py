import json,sys
from pathlib import Path
from shapely.geometry import shape,mapping,box,Point,MultiPolygon
from shapely.ops import unary_union,transform
from pyproj import Transformer
r=Path.cwd()
def clean(g): return g if g.is_valid else g.buffer(0)
def run(d):
    p=Transformer.from_crs('EPSG:4326','EPSG:3035',always_xy=True).transform
    q=Transformer.from_crs('EPSG:3035','EPSG:4326',always_xy=True).transform
    H=transform(p,clean(shape(d['historical'])))
    T=transform(p,clean(unary_union([clean(shape(x)) for x in d['modern']])))
    sea=unary_union([box(4.5,52.7,11.5,56.7),box(8,52.7,24,56.7)])
    zone=T.boundary.intersection(transform(p,sea)).buffer(12000)
    patch=T.intersection(zone).intersection(H.buffer(12000))
    result=clean(H.difference(zone).union(patch))
    IH,ID=[transform(p,clean(shape(d[x]))) for x in ['helgoland','dune']]
    result=clean(result.difference(IH.buffer(5000).union(ID.buffer(5000))).union(IH).union(ID))
    if result.geom_type=='Polygon': result=MultiPolygon([result])
    elif result.geom_type!='MultiPolygon': result=MultiPolygon([g for g in result.geoms if g.geom_type=='Polygon'])
    result=clean(result); W=transform(q,result); changed=H.symmetric_difference(result)
    outside=changed.difference(zone.buffer(1)).area/1e6
    return {'geometry':mapping(W),'valid':result.is_valid,'outsideKm2':outside,'areaKm2':result.area/1e6,'historicalAreaKm2':H.area/1e6,'changedKm2':changed.area/1e6,'helgolandKm2':IH.area/1e6,'duneKm2':ID.area/1e6,'controls':[W.covers(Point(*v['point'])) for v in d['controls']]}
def rect(w,s,e,n):return mapping(box(w,s,e,n))
input={'historical':rect(8,53,12,55),'modern':[rect(8,53,12.08,55)],'helgoland':rect(9,54.985,9.012,54.99),'dune':rect(9.04,54.985,9.052,54.99),'controls':[{'name':'inside','point':[10,54],'expected':True},{'name':'outside','point':[13,54],'expected':False}]}
p=Path('tests/fixtures/german-modern-coast-oracle.json');p.write_text(json.dumps({'input':input,'expected':run(input)},separators=(',',':'))+'\n',encoding='utf-8')
print('fixture', {k:v for k,v in run(input).items() if k!='geometry'})
