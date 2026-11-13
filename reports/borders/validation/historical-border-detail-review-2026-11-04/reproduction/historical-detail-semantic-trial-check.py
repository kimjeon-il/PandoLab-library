import json
from pathlib import Path
from osgeo import ogr
ogr.UseExceptions();B=Path('build-native/territorial-recipe');O=B/'boundary-semantic-review-2026-11-05';T=O/'trial250';route=json.loads((B/'historical-detail-line-2.geojson').read_text(encoding='utf-8-sig'));editable={tuple(p)for i in [25,27]for p in route['features'][i]['geometry']['coordinates']}
def g(x):return ogr.CreateGeometryFromJson(json.dumps(x))
def area(x):
 if x.GetGeometryName()=='POLYGON':return x.GetArea()
 return sum(area(x.GetGeometryRef(i))for i in range(x.GetGeometryCount()))
def ps(x):return x['coordinates']if x['type']=='MultiPolygon'else[x['coordinates']]
def cyclic(a,b):return len(a)==len(b)and(not a or any(a==b[i:]+b[:i]for i,q in enumerate(b)if q==a[0]))
result=[];changes={}
for layer in ['native','compiled']:
 d=json.loads((T/f'integrated-250-{layer}.json').read_text(encoding='utf-8-sig'))['rows'];changes[layer]={}
 for r in d:
  a,z=g(r['before']),g(r['after']);assert a.IsValid()and z.IsValid();aa,zz=ps(r['before']),ps(r['after']);assert len(aa)==len(zz);outside=True
  for p,q in zip(aa,zz):
   assert len(p)==len(q)
   for old,new in zip(p,q):outside=outside and cyclic([x for x in old[:-1]if tuple(x)not in editable],[x for x in new[:-1]if tuple(x)not in editable])
  assert outside;delta=a.SymDifference(z);changes[layer][r['entityId']]=delta;result.append({'layer':layer,'entity':r['entityId'],'valid_before_after':True,'components':len(aa),'holes':sum(len(p)-1 for p in aa),'exact_ordered_outside':True,'delta_area_degree2':area(delta)})
 for a in changes[layer]:
  for b in changes[layer]:assert area(changes[layer][a].SymDifference(changes[layer][b]))<1e-12
parity={k:area(changes['native'][k].SymDifference(changes['compiled'][k]))for k in changes['native']};assert all(v<1e-12 for v in parity.values())
(T/'topology-checks.json').write_text(json.dumps({'rows':result,'paired_changes_same':True,'source_compiled_delta_mismatch_degree2':parity,'status':'local trial topology; source semantics not fully certified'},indent=2)+'\n',encoding='utf-8');print('trial4geometries valid/outside exact, paired changes and source/compiled delta agree')
