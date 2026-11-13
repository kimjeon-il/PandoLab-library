import json,math
from pathlib import Path
import numpy as np
B=Path('build-native/territorial-recipe');O=B/'boundary-semantic-review-2026-11-05';samples=json.loads((B/'historical-detail-final-metric-input.json').read_text(encoding='utf-8-sig'))['samples'];trials=json.loads((O/'verified-source-constrained-trials.json').read_text(encoding='utf-8-sig'));existing=json.loads((O/'east14-ne-detail.json').read_text(encoding='utf-8-sig'));caps={18:250,20:500,23:500,25:500}
def metric(a):
 n=len(a);a=np.asarray(a);ds=np.linalg.norm(np.diff(a,axis=0),axis=1);good=np.r_[True,ds>0];a=a[good];ds=np.linalg.norm(np.diff(a,axis=0),axis=1);ar=np.r_[0,np.cumsum(ds)];L=ar[-1];turn={}
 for step in [1000,5000]:
  vals=[]
  for phase in range(8):
   t=np.unique(np.r_[0,np.arange(phase*step/8,L,step),L]);p=np.column_stack([np.interp(t,ar,a[:,i])for i in range(2)]);v=np.diff(p,axis=0);h=np.arctan2(v[:,1],v[:,0]);d=np.arctan2(np.sin(np.diff(h)),np.cos(np.diff(h)));vals.append(float(np.abs(np.degrees(d)).sum()/L*100000))
  turn[str(step)]=float(np.mean(vals))
 return {'points':n,'km':float(L/1000),'points_per_km':float(n/L*1000),'median_spacing_m':float(np.median(ds)),'turn_deg_per100km':turn}
def certificate(a,keep):
 a=np.asarray(a);m=0
 for l,r in zip(keep,keep[1:]):
  v=a[r]-a[l];q=a[l:r+1]-a[l];den=v@v;u=np.clip(q@v/den,0,1)if den else np.zeros(len(q));m=max(m,float(np.sqrt(np.sum((q-u[:,None]*v)**2,axis=1)).max()))
 return m
rows=[]
for r in existing:
 fi=r['feature'];s=next(s for s in samples if s.get('featureIndex')==fi);p=np.asarray(s['historical']);m=metric(s['work']);entry={'feature':fi,'status':'prior weak candidate retained; source-classification missing or no new reviewed replacement','selected':m,'modern':metric(s['reference'])}
 if fi in caps:
  t=next(x for x in trials if x['feature']==fi);q=next(x for x in t['trials']if x['tolerance_m']==caps[fi]);entry.update({'status':'new source-constrained research candidate; named/contact safeguards checked, not blanket historical certification','cap':caps[fi],'selected':metric(p[q['keep']]),'original_vertex_to_corresponding_chord_max_m':certificate(p,q['keep']),'anchors':t['anchor_indices'],'fixed_count':len(t['anchor_indices']),'referenceToSourcePolicy':t['policy']})
 entry['detail_ratios']={'density':entry['selected']['points_per_km']/entry['modern']['points_per_km'],**{'turn'+k:entry['selected']['turn_deg_per100km'][k]/entry['modern']['turn_deg_per100km'][k]for k in ['1000','5000']}};rows.append(entry)
assert sum(r['selected']['points']for r in rows)==764
(O/'selected-east-ne-metrics.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print(json.dumps([r for r in rows if r['feature']in caps]),flush=True)
