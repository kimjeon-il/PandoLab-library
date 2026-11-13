from historical_detail_membership import *
from pathlib import Path
O=Path(base)/'strong-independent-2026-11-05';peers=load(base+'historical-detail-final-peer-inputs.json');families=load(base+'historical-detail-konotop-tc-current-chains.json')['rows'];out=[]
def area(g):
 if g.GetGeometryName()=='POLYGON':return g.GetArea()
 return sum(area(g.GetGeometryRef(i)) for i in range(g.GetGeometryCount()))
for tol in [250,500]:
 edits=load(str(O/f'integrated-{tol}-compiled.json'))['rows'];rows=[];retained=[]
 for p in peers:
  for spec in p['geometries']:
   peer=ogr.CreateGeometryFromJson(json.dumps(spec['geojson']))
   for e in edits:
    a=ogr.CreateGeometryFromJson(json.dumps(e['before']));z=ogr.CreateGeometryFromJson(json.dumps(e['after']));old=a.Intersection(peer);new=z.Intersection(peer);delta=area(old.SymDifference(new));contact=a.Boundary().Intersection(peer.Boundary()).SymDifference(z.Boundary().Intersection(peer.Boundary())).Length();assert delta<=1e-12 and contact<=1e-8,(tol,e['entityId'],p['entityId'],delta,contact);rows.append({'entity':e['entityId'],'peer':p['entityId'],'overlap_delta_degree2':delta,'contact_delta_degrees':contact})
 print('foreign peers',tol,len(rows),flush=True)
 for family in families:
  ids=['soviet-union-transcaucasian-sfsr','soviet-union-russian-sfsr'] if family['id'].startswith('tc') else ['soviet-union-ukrainian-ssr','soviet-union-russian-sfsr']
  for chunk in family['chunks']:
   cs=chunk['coordinates']
   if len(cs) not in [59,833,63,99]:continue
   for id in ids:
    selected=next((r for r in edits if r['entityId']=='state:'+id),None);g=selected['after'] if selected else load(base+'historical-detail-retain-'+id+'.json')['geometries'][0]['geojson'];cover=Cover(g);count=sum(cover.includes(a,b) for a,b in zip(cs,cs[1:]));assert count==len(cs)-1;retained.append({'chain':family['id'],'entity':'state:'+id,'points':len(cs),'allEdgesPreserved':count})
 out.append({'tol':tol,'foreignComparisons':rows,'retainedChains':retained});print('retained copies',tol,len(retained),flush=True)
(O/'foreign-and-retained-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
