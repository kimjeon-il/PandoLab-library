import json,re,shapely
from shapely.geometry import shape,Point,LineString
from pathlib import Path
req=json.loads(Path('build-native/territorial-recipe/german-coast-selected-geos313-oracle.json').read_text(encoding='utf8'))
source=Path('build-native/territorial-recipe/german-coast-oracle.py').read_text(encoding='utf8').split('def rect')[0].replace('W=transform(q,result)','W=transform(q,result.segmentize(100))')
scope={};exec(compile(source,'oracle','exec'),scope);w=shape(scope['run'](req['input'])['geometry']);reason=shapely.is_valid_reason(w);xy=list(map(float,re.search(r'\[([^ ]+) ([^]]+)\]',reason).groups()));p=Point(*xy)
print(reason,flush=True);segments=[]
for i,poly in enumerate(w.geoms):
 for j,ring in enumerate([poly.exterior,*poly.interiors]):
  coords=list(ring.coords)
  for k,(a,b) in enumerate(zip(coords,coords[1:])):
   if min(a[0],b[0])-1e-7<=p.x<=max(a[0],b[0])+1e-7 and min(a[1],b[1])-1e-7<=p.y<=max(a[1],b[1])+1e-7:
    s=LineString([a,b]);dist=s.distance(p)
    if dist<1e-9:segments.append((i,j,k,a,b,dist,s.length))
for row in segments:print(row)
