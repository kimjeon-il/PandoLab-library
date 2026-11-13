import json,hashlib
from pathlib import Path
import numpy as np
B=Path('build-native/territorial-recipe'); O=B/'east-followup-context-2026-11-05'
O.mkdir(exist_ok=False)
load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
route=B/'historical-detail-line-2.geojson'; assert hashlib.sha256(route.read_bytes()).hexdigest()=='b6f76fa266bde7421a328ceebcd654a57b896103aad3908a89ff5ef16bbb733d'
features=load(route)['features']; samples=load(B/'historical-detail-final-metric-input.json')['samples']; weak=load(B/'historical-detail-east-candidate.json')['spec']; proofs=load(B/'strong-independent-2026-11-05/anchor-proofs.json')['east']
# Reuse the already executed fixed-distance metric and finite-chord certificate functions without executing its output stage.
metric_source=(B/'historical-detail-semantic-selected-measure.py').read_text(encoding='utf-8-sig'); exec(metric_source[metric_source.index('def metric('):metric_source.index('rows=[]')],globals())
def ran(a,b):return list(range(a,b+1))
def flatten(v):return set(x for z in v for x in (z if isinstance(z,list)else[z]))
def dp(a,t,anchors):
 a=np.asarray(a);keep={0,len(a)-1,*anchors};stack=list(zip(sorted(keep),sorted(keep)[1:]))
 while stack:
  l,r=stack.pop()
  if r-l<2:continue
  v=a[r]-a[l];q=a[l+1:r]-a[l];den=v@v;u=np.clip(q@v/den,0,1)if den else np.zeros(len(q));d=np.sum((q-u[:,None]*v)**2,axis=1);j=int(np.argmax(d))+l+1
  if d[j-l-1]>t*t:keep.add(j);stack.extend([(l,j),(j,r)])
 return sorted(keep)
def ends(indices):
 a=sorted(indices);return {i for j,i in enumerate(a)if j==0 or j==len(a)-1 or i-a[j-1]>1 or a[j+1]-i>1}
# All index lists below are registered route local, except explicitly tagged weak-local lists converted below.
C={
2:dict(direct=[],hydro=[ran(1,9),ran(53,58),ran(61,73)],contact=[ran(40,43),ran(48,52)],broad=[ran(14,25),ran(27,37)],technical=[]),
4:dict(direct=[11,25,26],hydro=[ran(13,23),ran(43,49),ran(53,59)],contact=[],broad=[ran(0,8),ran(29,40),ran(61,65)],technical=[]),
8:dict(direct=[34,35],hydro=[ran(5,14),ran(15,22),ran(28,32),[24,37]],contact=[],broad=[ran(0,6),ran(38,43)],technical=[]),
12:dict(direct=[12,42],hydro=[],contact=[ran(109,124),ran(89,94),ran(52,76),ran(33,43),ran(14,26),ran(5,13)],broad=[],technical=[],limit='New upstream bounded original-pixel review windows, not replacement authoritative hydro mask; outside windows not certified dry land.'),
27:dict(direct=[0,1,3,8,10,12],hydro=[[17]],contact=[],broad=[ran(0,1),ran(2,4),ran(6,8),ran(9,11),ran(13,14),[16],ran(18,20)],technical=[]),
35:dict(direct=[],hydro=[],contact=[],broad=[ran(0,1),ran(7,8),ran(15,16),ran(31,34),[39],ran(58,59)],technical=[2,6,9,14,17,30,35,38,40,57]),
37:dict(direct=[],hydro=[ran(39,42)],contact=[],broad=[ran(0,3),ran(7,11),ran(17,19),ran(32,33),ran(45,50),ran(57,58),ran(67,78),[82]],technical=[37,39,42,43],limit='Registered39/42 retained;40/41 already absent in764 and not reinserted in remove-only mode.'),
39:dict(direct=[2,10,16],hydro=[],contact=[],broad=[[6,7,8,14]],technical=[1,2,3,4,5,9,10,11,12,13,15,16,17]),
44:dict(direct=[],hydro=[],contact=[],broad=[ran(0,11),ran(15,52)],technical=[4,15,20,21],hold='Supplementary ridge ranges identified; broader unclassified spans await bounded source-context conclusion.'),
48:dict(direct=[],hydro=[ran(13,42)],contact=[],broad=[ran(1,7),ran(47,81)],technical=[48],hold='Chagan08 broad lock remains unclassified; source-context conclusion pending.')}
q25={2:270.401525725,4:110.666678199,8:167.875088712,12:171.785738517,27:312.793797343,35:183.3171849,37:197.469608413,39:410.242734047,44:303.05946205,48:268.41011308}
rows=[]
for fi,c in C.items():
 s=next(x for x in samples if x.get('featureIndex')==fi); raw=features[fi]['geometry']['coordinates']; assert raw==s['geographic']['historical']['coordinates']; indices=[i for i in range(len(raw))if i not in weak[str(fi)]]; p=np.asarray(s['historical']);a=p[indices]; geographic=[raw[i]for i in indices]; orig_to_weak={i:j for j,i in enumerate(indices)}
 groups={}
 for k in ['direct','hydro','contact','broad','technical']:
  z=flatten(c[k]);groups[k]=sorted(indices[i]for i in z)if c.get('weak_local')else sorted(z)
 endpoints={0,len(raw)-1};hard=endpoints|set(groups['direct'])|set(groups['hydro'])|set(groups['contact']);present_hard=hard&set(indices)
 # Constraints already absent from the 764-point baseline are reported, never silently reinserted.
 missing=sorted(hard-set(indices));macro=set(next(x for x in proofs if x['feature']==fi)['macro'])&set(indices)
 variants=[]
 for variant in ['conservative','compact']:
  broad=set(groups['broad'])&set(indices);technical=set(groups['technical'])&set(indices)
  locks=present_hard|(broad|technical|macro if variant=='conservative'else ends(broad)|(macro&broad))
  local_locks={orig_to_weak[i]for i in locks};trials=[]; caps=sorted(set([125,250,375,500,round(q25[fi],6)]));oldm=metric(a)
  for cap in caps:
   keep=dp(a,cap,local_locks)if not c.get('hold')else list(range(len(a)));z=a[keep];m=metric(z);ratio=m['km']/oldm['km'];change=abs(m['turn_deg_per100km']['5000']/oldm['turn_deg_per100km']['5000']-1)if oldm['turn_deg_per100km']['5000']else 0
   trials.append(dict(cap_m=cap,keep_weak=keep,keep_route=[indices[i]for i in keep],points=len(keep),coordinates=[geographic[i]for i in keep],metrics=m,length_ratio=ratio,turn5km_change=change,max_from_764_vertices_m=certificate(a,keep),max_from_registered_vertices_m=certificate(p,[indices[i]for i in keep]),shape_guard_pass=ratio>=.975 and change<=.12,all_present_hard_locks_preserved=local_locks.issubset(keep)))
  # Local current-model omission sagitta supplies a contextual search cap (not a claim of geographic accuracy).
  allowed=[t for t in trials if t['cap_m']<=min(500,2*q25[fi])and t['shape_guard_pass']]
  chosen=min(allowed,key=lambda t:(t['points'],t['cap_m']))if allowed else dict(cap_m=0,keep_weak=list(range(len(a))),keep_route=indices,points=len(a),coordinates=geographic,metrics=oldm,max_from_764_vertices_m=0,max_from_registered_vertices_m=certificate(p,indices),shape_guard_pass=True)
  variants.append(dict(name=variant,fixed_route_indices=sorted(locks),fixed_weak_indices=sorted(local_locks),trials=trials,selected=chosen))
 rows.append(dict(feature=fi,original_points=len(raw),baseline764_points=len(a),groups_route=groups,hard_constraints_absent_in764=missing,algorithmic_macro_route=sorted(macro),hold=c.get('hold'),limits=c.get('limit'),metricCrs=s['metricCrs'],projectionEvidence=s['projectionEvidence'],modern=metric(s['reference']),baseline764_metrics=metric(a),localModernOmissionQ25_m=q25[fi],variants=variants))
result=dict(status='local provisional research, not semantic approval',sourceRouteSha256=hashlib.sha256(route.read_bytes()).hexdigest(),policy='Masters and existing 764 baseline preserved. Hard meaning/contact constraints retained. Broad nonhydro glyph ranges may generalize with endpoints and calculated macro bends. Technical seams are not surveyed anchors. No production writes.',rows=rows)
(O/'trials.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([dict(feature=r['feature'],registered=r['original_points'],baseline=r['baseline764_points'],hold=r['hold'],variants=[dict(name=v['name'],points=v['selected']['points'],cap=v['selected']['cap_m'],max_m=v['selected']['max_from_764_vertices_m'])for v in r['variants']])for r in rows],ensure_ascii=False))