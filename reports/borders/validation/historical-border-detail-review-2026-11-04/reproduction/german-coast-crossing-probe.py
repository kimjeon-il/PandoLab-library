import json,re,shapely
from shapely.geometry import shape,Point,LineString
from pathlib import Path
w=shape(json.loads(Path('build-native/territorial-recipe/german-coast-selected-geos313-oracle.json').read_text(encoding='utf8'))['expected']['geometry'])
reason=shapely.is_valid_reason(w); xy=list(map(float,re.search(r'\[([^ ]+) ([^]]+)\]',reason).groups()));p=Point(*xy)
print(reason)
segments=[]
for i,poly in enumerate(w.geoms):
 for j,ring in enumerate([poly.exterior,*poly.interiors]):
  coords=list(ring.coords)
  for k,(a,b) in enumerate(zip(coords,coords[1:])):
   if min(a[0],b[0])-.00001<=p.x<=max(a[0],b[0])+.00001 and min(a[1],b[1])-.00001<=p.y<=max(a[1],b[1])+.00001:
    s=LineString([a,b]);dist=s.distance(p)
    if dist<1e-7:segments.append((i,j,k,a,b,dist,s.length))
print('segments',len(segments))
for row in segments:print(row)
