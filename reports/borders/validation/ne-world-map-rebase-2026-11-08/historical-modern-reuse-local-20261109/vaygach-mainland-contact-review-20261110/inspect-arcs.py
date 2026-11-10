import sys,json
from shapely.geometry import shape,box,mapping,LineString,Point
from shapely.ops import nearest_points
x=json.load(sys.stdin);d=shape(x['donor']['geometry']);b=shape(x['rows'][0]['geometry']);r=box(59,69.2,62,70.3);old=b.geoms[6];new=d.geoms[3289]
ints=old.boundary.intersection(new.boundary).intersection(r)
pts=list(ints.geoms) if hasattr(ints,'geoms') else [ints]
f=d.geoms[1554].representative_point();print(json.dumps({'intersections':[list(p.coords)[0] for p in pts if p.geom_type=='Point'],'oldIndices':[(i,list(c)) for i,c in enumerate(old.exterior.coords) if r.covers(Point(c))],'newIndices':[(i,list(c)) for i,c in enumerate(new.exterior.coords) if r.covers(Point(c))]}))
print(json.dumps({'1552':x['donor']['geometry']['coordinates'][1552],'1554':x['donor']['geometry']['coordinates'][1554],'contact':mapping(d.geoms[1552].intersection(d.geoms[1554])),'uniontype':d.geoms[1552].union(d.geoms[1554]).geom_type}))
