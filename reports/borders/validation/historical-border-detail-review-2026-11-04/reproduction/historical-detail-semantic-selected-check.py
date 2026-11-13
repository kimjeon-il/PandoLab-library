import json
from pathlib import Path
from osgeo import ogr
ogr.UseExceptions();B=Path('build-native/territorial-recipe');O=B/'boundary-semantic-review-2026-11-05';R=O/'selected';load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));source=load(R/'integrated-250-native.json')['rows'];compiled=load(R/'integrated-250-compiled.json')['rows'];features=load(B/'historical-detail-line-2.geojson')['features'];editable={tuple(p)for i in [18,20,23,25]for p in features[i]['geometry']['coordinates']};proof=load(R/'splice-proof.json')
for p in proof:
 for key in ['oldWest','newWest']:
  for q in p.get(key,[]):editable.add(tuple(q))
def ps(g):return g['coordinates']if g['type']=='MultiPolygon'else[g['coordinates']]
def geom(g):return ogr.CreateGeometryFromJson(json.dumps(g))
def area(g):
 if g.GetGeometryName()=='POLYGON':return g.GetArea()
 return sum(area(g.GetGeometryRef(i))for i in range(g.GetGeometryCount()))
def cyclic(a,b):return len(a)==len(b)and(not a or any(a==b[i:]+b[:i]for i,q in enumerate(b)if q==a[0]))
results=[];changes={};geoms={};olds={}
for layer,rows in [('native',source),('compiled',compiled)]:
 changes[layer]={};geoms[layer]={};olds[layer]={}
 for row in rows:
  a,z=geom(row['before']),geom(row['after']);assert a.IsValid()and z.IsValid();pa,pz=ps(row['before']),ps(row['after']);assert len(pa)==len(pz);exact=True
  for p,q in zip(pa,pz):
   assert len(p)==len(q)
   for ra,rz in zip(p,q):exact=exact and cyclic([p for p in ra[:-1]if tuple(p)not in editable],[p for p in rz[:-1]if tuple(p)not in editable])
  assert exact;id=row['entityId'];changes[layer][id]=a.SymDifference(z);geoms[layer][id]=z;olds[layer][id]=a;results.append({'layer':layer,'entity':id,'valid_before_after':True,'components':len(pa),'holes':sum(len(p)-1 for p in pa),'exact_outside':True,'change_area_degree2':area(changes[layer][id])})
U='state:soviet-union';RS=U+'-russian-sfsr';BY=U+'-byelorussian-ssr';UA=U+'-ukrainian-ssr';ua=geom(next(r for r in load(B/'east-mask-review-2026-11-05/mixed/integrated-250-native.json')['rows']if r['entityId']==UA)['after']);deltaMismatch=area(changes['native'][U].SymDifference(changes['native'][RS].Union(changes['native'][BY])));assert deltaMismatch<1e-12;parity={id:area(changes['native'][id].SymDifference(changes['compiled'][id]))for id in changes['native']};assert all(v<1e-12 for v in parity.values());overlap=[]
for x,y in [(RS,BY),(RS,UA),(BY,UA)]:
 a=olds['native'][x].Intersection(ua if y==UA else olds['native'][y]);z=geoms['native'][x].Intersection(ua if y==UA else geoms['native'][y]);change=area(a.SymDifference(z));assert change<1e-12;overlap.append({'pair':[x,y],'before':area(a),'after':area(z),'change':change})
(R/'topology-checks.json').write_text(json.dumps({'rows':results,'constituent_union_change_mismatch_degree2':deltaMismatch,'source_compiled_change_mismatch_degree2':parity,'constituent_overlap_checks':overlap,'source_meaning_status':'specific anchors and contact intervals conserved; no blanket historical certification'},indent=2)+'\n',encoding='utf-8');print('selected6geometries valid; exact outside; union/parity/overlap0')
