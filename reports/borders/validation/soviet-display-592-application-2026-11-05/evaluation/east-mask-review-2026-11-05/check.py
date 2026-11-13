import json,copy,hashlib
from pathlib import Path
from osgeo import ogr
ogr.UseExceptions();B=Path('build-native/territorial-recipe');O=Path('build-native/territorial-recipe/east-mask-review-2026-11-05/mixed/')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def geom(g):return ogr.CreateGeometryFromJson(json.dumps(g))
def area(g):
 if g is None:raise RuntimeError('missing geometry')
 if g.GetGeometryName()=='POLYGON':return g.GetArea()
 return sum(area(g.GetGeometryRef(i)) for i in range(g.GetGeometryCount()))
def ps(g):return g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
def counts(g):return [len(ps(g)),sum(len(p)-1 for p in ps(g))]
def cyclic(a,b):
 if len(a)!=len(b):return False
 if not a:return True
 return any(a==b[i:]+b[:i] for i,v in enumerate(b) if v==a[0])
west=read(B/'historical-detail-west-whole-view.json');route=read(B/'historical-detail-east-candidate.json')['originalChain'];edit=set(tuple(p) for chain in [route,*[w['coordinates']['old'] for w in west]] for p in chain)
results=[]
for tol in [250,500]:
 source=read(O/f'integrated-{tol}-native.json')['rows'];compiled=read(O/f'integrated-{tol}-compiled.json')['rows'];rr=[];sourcechanges={};compiledchanges={};sourcegeom={};olds={}
 for label,rows in [('native',source),('compiled',compiled)]:
  for row in rows:
   a,b=row['before'],row['after'];ga,gb=geom(a),geom(b);outside=True
   assert counts(a)==counts(b)
   for pa,pb in zip(ps(a),ps(b)):
    assert len(pa)==len(pb)
    for ra,rb in zip(pa,pb):
     aa=[p for p in ra[:-1] if tuple(p) not in edit];bb=[p for p in rb[:-1] if tuple(p) not in edit];outside=outside and cyclic(aa,bb)
   assert outside and ga.IsValid() and gb.IsValid(),(tol,label,row['entityId'])
   delta=ga.SymDifference(gb);(sourcechanges if label=='native' else compiledchanges)[row['entityId']]=delta
   if label=='native':sourcegeom[row['entityId']]=gb;olds[row['entityId']]=ga
   rr.append({'layer':label,'entity':row['entityId'],'valid_before':True,'valid_after':True,'components_holes':counts(b),'outside_ordered_coordinates_exact':outside,'delta_area_degree2':area(delta)})
 print('valid/outside',tol,len(rr),flush=True)
 U='state:soviet-union';members=[U+'-russian-sfsr',U+'-byelorussian-ssr',U+'-ukrainian-ssr'];union=sourcechanges[members[0]].Union(sourcechanges[members[1]]).Union(sourcechanges[members[2]]);mismatch=area(sourcechanges[U].SymDifference(union));assert mismatch<1e-12
 parity={k:area(sourcechanges[k].SymDifference(compiledchanges[k])) for k in sourcechanges};assert all(x<1e-12 for x in parity.values())
 overlaps=[]
 for i,k in enumerate(members):
  for k2 in members[i+1:]:
   old=olds[k].Intersection(olds[k2]);new=sourcegeom[k].Intersection(sourcegeom[k2]);delta=area(old.SymDifference(new));assert delta<1e-12;overlaps.append({'pair':[k,k2],'before_area':area(old),'after_area':area(new),'change_area':delta})
 results.append({'latvia_m':tol,'rows':rr,'constituent_change_union_mismatch_degree2':mismatch,'source_compiled_change_mismatch_degree2':parity,'constituent_overlaps':overlaps,'status':'local geometric checks only; semantic/hydro review unresolved; not active'})
 print('delta/overlap',tol,mismatch,parity,flush=True)
(O/'integrated-checks.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
