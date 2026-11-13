import json,math
from pathlib import Path
import numpy as np
B=Path('build-native/territorial-recipe');O=B/'boundary-semantic-review-2026-11-05';D=json.loads((B/'historical-detail-line-2.geojson').read_text(encoding='utf-8-sig'));samples=json.loads((B/'historical-detail-final-metric-input.json').read_text(encoding='utf-8-sig'))['samples']
def dp(p,t,locks):
 p=np.asarray(p);keep={0,len(p)-1,*locks};a=sorted(keep);stack=list(zip(a,a[1:]))
 while stack:
  l,r=stack.pop()
  if r-l<2:continue
  v=p[r]-p[l];q=p[l+1:r]-p[l];den=v@v;u=np.clip(q@v/den,0,1)if den else np.zeros(len(q));d=np.sum((q-u[:,None]*v)**2,axis=1);j=int(np.argmax(d))+l+1
  if d[j-l-1]>t*t:keep.add(j);stack.extend([(l,j),(j,r)])
 return sorted(keep)
def intervals(s):
 runs=[]
 for i in sorted(s):
  if runs and i==runs[-1][-1]+1:runs[-1].append(i)
  else:runs.append([i])
 return runs
rows=[]
for fi in [25,27]:
 p=D['features'][fi]['properties'];x=p['display_simplification_20261028'];mask=x['terrain_mask'];coords=D['features'][fi]['geometry']['coordinates'];metric=next(s['historical']for s in samples if s.get('featureIndex')==fi);reasons={0:{'feature endpoint'},len(coords)-1:{'feature endpoint'}}
 if fi==25:
  rawmap=[205-i for i in x['retained_input_indices']];water=set(i for a,b in mask['possibleWaterCrossingsVertexIntervalsInclusive']for i in range(a,b+1));major=set(mask['majorBendAndNamedAnchorIndices']);uncertain=[list(range(a,b+1))for a,b in mask['overlapAndEndpointVertexIntervalsInclusive']];rawlocked=set(x['protected_input_indices'])
 else:
  r=p['remaining_display_simplification_20261028'];rawmap=[89-x['retained_input_indices'][i]for i in r['retained_input_indices']];water={v for i in mask['waterOrPossibleWaterCrossingSegmentIndices']for v in [i,i+1]};major=set(mask['fixedMajorBendIndices']);uncertain=intervals(set(mask['lockedVertexIndices']));rawlocked=set(mask['lockedVertexIndices'])
 for j,k in enumerate(rawmap):
  if k in water:reasons.setdefault(j,set()).add('recorded uncertain water/ice/channel span: preserve all current points')
  if k in major:reasons.setdefault(j,set()).add('recorded major bend/named anchor or pixel context: preserve conservatively')
 for run in uncertain:
  js=[j for j,k in enumerate(rawmap)if k in run]
  if js:
   for j in [min(js),max(js)]:reasons.setdefault(j,set()).add('uncertainty interval boundary among current retained points')
 # The old raw blanket lock is not treated as a legal-point certificate. No known water, named/macro or interval-end safeguard is relaxed.
 trial=[]
 for tol in [250,500]:
  keep=dp(metric,tol,reasons);assert set(reasons).issubset(keep);trial.append({'tolerance_m':tol,'points':len(keep),'keep':keep,'coordinates':[coords[i]for i in keep],'released_current_indices':[i for i in range(len(coords))if i not in keep],'all_known_water_and_major_indices_preserved':True,'status':'provisional display-only uncertainty-interval-interior trial; source pixels not newly verified'})
 rows.append({'feature':fi,'original_points':len(coords),'fixed_count':len(reasons),'fixed_reasons':{str(k):sorted(v)for k,v in reasons.items()},'raw_index_mapping':rawmap,'trials':trial,'source':{'image_sha256':'823c6377cfebe6fdb7effcd60d913ef9986a1d180746053e17fce97b33cfe482','mask_path':x['terrain_mask_source'],'mask_sha256':x['terrain_mask_sha256'],'pixels_seen_locally':False},'decision':'research-only; preserving specified water/major/interval boundaries does not certify unknown historical semantics'})
(O/'uncertainty-interior-trials.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps([{'feature':r['feature'],'old':r['original_points'],'fixed':r['fixed_count'],'trials':[(t['tolerance_m'],t['points'])for t in r['trials']]}for r in rows]))
