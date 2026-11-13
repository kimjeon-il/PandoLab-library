import json,csv,math
from pathlib import Path
import numpy as np
B=Path('build-native/territorial-recipe');O=B/'boundary-semantic-review-2026-11-05'
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dp(p,t,locks=()):
 p=np.asarray(p);keep={0,len(p)-1,*locks};a=sorted(keep);stack=list(zip(a,a[1:]))
 while stack:
  l,r=stack.pop()
  if r-l<2:continue
  v=p[r]-p[l];q=p[l+1:r]-p[l];den=v@v;u=np.clip(q@v/den,0,1)if den else np.zeros(len(q));d=np.sum((q-u[:,None]*v)**2,axis=1);j=int(np.argmax(d))+l+1
  if d[j-l-1]>t*t:keep.add(j);stack.extend([(l,j),(j,r)])
 return sorted(keep)
def metrics(p):
 input_count=len(p);p=np.asarray(p);ds=np.linalg.norm(np.diff(p,axis=0),axis=1);good=np.r_[True,ds>0];p=p[good];ds=np.linalg.norm(np.diff(p,axis=0),axis=1);arc=np.r_[0,np.cumsum(ds)];length=arc[-1];turns={}
 for step in [1000,5000]:
  vals=[]
  for phase in range(8):
   t=np.unique(np.r_[0,np.arange(phase*step/8,length,step),length]);q=np.column_stack([np.interp(t,arc,p[:,i])for i in range(2)]);v=np.diff(q,axis=0);h=np.arctan2(v[:,1],v[:,0]);d=np.arctan2(np.sin(np.diff(h)),np.cos(np.diff(h)));vals.append(float(np.abs(np.degrees(d)).sum()/length*100000))
  turns[str(step)]={'mean_deg_per_100km':float(np.mean(vals)),'phase_min':min(vals),'phase_max':max(vals)}
 return {'points':input_count,'nonzero_sampling_vertices':len(p),'zero_length_edges':input_count-len(p),'length_km':float(length/1000),'points_per_km':float(input_count*1000/length),'median_spacing_m':float(np.median(ds)),'spacing_p10_m':float(np.quantile(ds,.1)),'spacing_p90_m':float(np.quantile(ds,.9)),'turning':turns}
samples=load(B/'historical-detail-final-metric-input.json')['samples'];proof=load(B/'strong-independent-2026-11-05/anchor-proofs.json');rows=[]
for s in samples:
 if not s['id'].startswith('east-'):continue
 p=np.asarray(s['historical']);macro=dp(p,2000);variants={'original':p,'weak':s['work'],'250':p[dp(p,250,macro)],'500':p[dp(p,500,macro)],'modern':s['reference']};m={k:metrics(v)for k,v in variants.items()};ratios={k:{'density':m[k]['points_per_km']/m['modern']['points_per_km'],'turn1km':m[k]['turning']['1000']['mean_deg_per_100km']/m['modern']['turning']['1000']['mean_deg_per_100km'],'turn5km':m[k]['turning']['5000']['mean_deg_per_100km']/m['modern']['turning']['5000']['mean_deg_per_100km']}for k in ['original','weak','250','500']};rows.append({'feature':s['featureIndex'],'assembly':s['assemblyId'],'metricCrs':s['metricCrs'],'comparisonReference':s['comparisonReference'],'metrics':m,'ratios':ratios,'sourceMeaningVerified':False,'limits':'Regional current CHN arc with documented exact native correspondence, politically different historical route; metric detail context, not legal/positional truth. Same8-phase support for every variant.'})
assert sum(r['metrics']['250']['points']for r in rows)==407
assert sum(r['metrics']['500']['points']for r in rows)==253
assert sum(r['metrics']['weak']['points']for r in rows)==908
(O/'east14-ne-detail.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (O/'east14-ne-detail.csv').open('w',newline='',encoding='utf-8-sig')as f:
 fields=['feature','variant','points','length_km','points_per_km','median_spacing_m','turn1km_deg_per_100km','turn5km_deg_per_100km','density_ratio_to_modern','turn1km_ratio_to_modern','turn5km_ratio_to_modern'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in rows:
  for k,m in r['metrics'].items():
   ratio=r['ratios'].get(k,{});w.writerow({'feature':r['feature'],'variant':k,**{x:m[x]for x in ['points','length_km','points_per_km','median_spacing_m']},'turn1km_deg_per_100km':m['turning']['1000']['mean_deg_per_100km'],'turn5km_deg_per_100km':m['turning']['5000']['mean_deg_per_100km'],'density_ratio_to_modern':ratio.get('density',1),'turn1km_ratio_to_modern':ratio.get('turn1km',1),'turn5km_ratio_to_modern':ratio.get('turn5km',1)})
print(json.dumps([{'feature':r['feature'],'weak_vs_modern':r['ratios']['weak'],'500_vs_modern':r['ratios']['500']}for r in rows]),flush=True)
