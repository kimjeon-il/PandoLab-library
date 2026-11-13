import json
from pathlib import Path
from osgeo import ogr
ogr.UseExceptions();B=Path('build-native/territorial-recipe');O=B/'east-followup-final-2026-11-05';R=O/'selected';load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));trials=load(O/'trials.json')['rows'];source=load(R/'integrated-250-native.json')['rows'];compiled=load(R/'integrated-250-compiled.json')['rows'];features=load(B/'historical-detail-line-2.geojson')['features'];editable={tuple(p)for r in trials if not r['hold']for p in features[r['feature']]['geometry']['coordinates']}
def ps(g):return g['coordinates']if g['type']=='MultiPolygon'else[g['coordinates']]
def geom(g):return ogr.CreateGeometryFromJson(json.dumps(g))
def area(g):return g.GetArea()if g.GetGeometryName()=='POLYGON'else sum(area(g.GetGeometryRef(i))for i in range(g.GetGeometryCount()))
def cyclic(a,b):return len(a)==len(b)and(not a or any(a==b[i:]+b[:i]for i,q in enumerate(b)if q==a[0]))
rows=[];changes={};G={};oldG={};protected=[]
for layer,edits in [('native',source),('compiled',compiled)]:
 changes[layer]={};G[layer]={};oldG[layer]={}
 for e in edits:
  a,z=geom(e['before']),geom(e['after']);assert a.IsValid()and z.IsValid();pa,pz=ps(e['before']),ps(e['after']);assert len(pa)==len(pz)
  for p,q in zip(pa,pz):
   assert len(p)==len(q)
   for ra,rz in zip(p,q):assert cyclic([p for p in ra[:-1]if tuple(p)not in editable],[p for p in rz[:-1]if tuple(p)not in editable])
  present={tuple(p)for p in ps(e['after'])for r in p for p in r};prior={tuple(p)for p in ps(e['before'])for r in p for p in r}
  for t in trials:
   sel=next(v for v in t['variants']if v['name']=='compact');cs=features[t['feature']]['geometry']['coordinates'];required=set(sel['fixed_route_indices'])
   for k in required:
    if tuple(cs[k])in prior:assert tuple(cs[k])in present,(layer,e['entityId'],t['feature'],k)
   protected.append(dict(layer=layer,entity=e['entityId'],feature=t['feature'],fixed_surviving_points_preserved=len(required),previously_absent=t['hard_constraints_absent_in764']))
  id=e['entityId'];changes[layer][id]=a.SymDifference(z);G[layer][id]=z;oldG[layer][id]=a;rows.append(dict(layer=layer,entity=id,valid_before_after=True,components=len(pa),holes=sum(len(p)-1 for p in pa),outside_exact_cyclic=True,change_area_degree2=area(changes[layer][id])))
U='state:soviet-union';RS=U+'-russian-sfsr';parity={i:area(changes['native'][i].SymDifference(changes['compiled'][i]))for i in changes['native']};assert all(v<1e-12 for v in parity.values());delta=area(changes['native'][U].SymDifference(changes['native'][RS]));assert delta<1e-12
# All new shared arcs occur in both owners, and their entire differential regions are identical.
others=[]
for ent,rel in [(U+'-byelorussian-ssr','boundary-semantic-review-2026-11-05/selected/integrated-250-native.json'),(U+'-ukrainian-ssr','east-mask-review-2026-11-05/mixed/integrated-250-native.json')]:
 other=geom(next(x for x in load(B/rel)['rows']if x['entityId']==ent)['after']);old=oldG['native'][RS].Intersection(other);new=G['native'][RS].Intersection(other);d=area(old.SymDifference(new));assert d<1e-12;others.append(dict(peer=ent,overlap_change_degree2=d))
peers=load(B/'historical-detail-final-peer-inputs.json');foreign=[]
for p in peers:
 for spec in p['geometries']:
  peer=geom(spec['geojson'])
  for e in compiled:
   a,z=oldG['compiled'][e['entityId']],G['compiled'][e['entityId']];diff=changes['compiled'][e['entityId']];xmin,xmax,ymin,ymax=diff.GetEnvelope();box=ogr.CreateGeometryFromWkt(f'POLYGON(({xmin-0.01} {ymin-0.01},{xmax+0.01} {ymin-0.01},{xmax+0.01} {ymax+0.01},{xmin-0.01} {ymax+0.01},{xmin-0.01} {ymin-0.01}))');pclip=peer.Intersection(box)
   if pclip.IsEmpty():foreign.append(dict(entity=e['entityId'],peer=p['entityId'],overlap_delta_degree2=0,contact_delta_degrees=0,disjoint_change_window=True));continue
   old=a.Intersection(pclip);new=z.Intersection(pclip);d=area(old.SymDifference(new));contact=a.Boundary().Intersection(peer.Boundary()).SymDifference(z.Boundary().Intersection(peer.Boundary())).Length();assert d<=1e-12 and contact<=1e-8,(e['entityId'],p['entityId'],d,contact);foreign.append(dict(entity=e['entityId'],peer=p['entityId'],overlap_delta_degree2=d,contact_delta_degrees=contact))
result=dict(status='local geometry checks passed; source semantics remain bounded/provisional',rows=rows,protected=protected,source_compiled_delta_mismatch=parity,shared_owner_delta_mismatch=delta,constituent_overlap_checks=others,foreign=foreign)
(R/'topology-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(wholeGeometries=len(rows),protectedCopies=len(protected),foreignComparisons=len(foreign),parity=parity,sharedDeltaMismatch=delta)),flush=True)