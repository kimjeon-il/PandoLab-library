import json
from pathlib import Path
import numpy as np
B=Path('build-native/territorial-recipe');O=B/'boundary-semantic-review-2026-11-05';samples=json.loads((B/'historical-detail-final-metric-input.json').read_text(encoding='utf-8-sig'))['samples'];existing=json.loads((B/'strong-independent-2026-11-05/anchor-proofs.json').read_text(encoding='utf-8-sig'))['east'];fixed23=json.loads((O/'pamir-source4-named-anchor.json').read_text(encoding='utf-8-sig'));initial=json.loads((O/'uncertainty-interior-trials.json').read_text(encoding='utf-8-sig'));s25=next(s for s in samples if s.get('featureIndex')==25);s23=next(s for s in samples if s.get('featureIndex')==23)
def dp(a,t,anchors):
 a=np.asarray(a);keep={0,len(a)-1,*anchors};k=sorted(keep);stack=list(zip(k,k[1:]))
 while stack:
  l,r=stack.pop()
  if r-l<2:continue
  v=a[r]-a[l];q=a[l+1:r]-a[l];den=v@v;u=np.clip(q@v/den,0,1)if den else np.zeros(len(q));d=np.sum((q-u[:,None]*v)**2,axis=1);j=int(np.argmax(d))+l+1
  if d[j-l-1]>t*t:keep.add(j);stack.extend([(l,j),(j,r)])
 return sorted(keep)
rows=[]
for fi,s in [(23,s23),(25,s25)]:
 if fi==23:anchors=set(fixed23['proposedFixedIndices']);policy='All declared source-mask anchors plus confirmed Saar5227/local47 and feature endpoints; prior-shortcut/40degree protections are not promoted to semantic authority.'
 else:
  t=next(t for t in initial if t['feature']==25);anchors={int(i)for i,rs in t['fixed_reasons'].items()if any('water/ice/channel' in x for x in rs)}|{0,2,128};policy='All17 current points in possible-water/contact intervals + confirmed printed pass contact local2 + separate technical endpoint0 + northern dash128 + algorithmic2km macro skeleton. Other broad overlap interiors are not individually certified semantic anchors.'
 macro=next(x['macro']for x in existing if x['feature']==fi);anchors.update(macro);cs=s['geographic']['historical']['coordinates'];tr=[]
 for tol in [250,500]:
  keep=dp(s['historical'],tol,anchors);assert anchors.issubset(keep);tr.append({'tolerance_m':tol,'keep':keep,'points':len(keep),'coordinates':[cs[i]for i in keep]})
 rows.append({'feature':fi,'original_points':len(cs),'anchor_indices':sorted(anchors),'anchor_count':len(anchors),'policy':policy,'authorityLimit':'Source pixels/labels confirm specified named contacts; algorithmic skeleton is only a display safeguard; unresolved source meanings are not certified.','trials':tr,'selection':250,'selectionReason':'Evaluate250/500 locally; use weaker250m for initial constrained comparison while preserving all declared anchors and known contact spans.'})
(O/'named-anchor-constrained-trials.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps([{'feature':r['feature'],'fixed':r['anchor_count'],'trials':[(t['tolerance_m'],t['points'])for t in r['trials']]}for r in rows]))
