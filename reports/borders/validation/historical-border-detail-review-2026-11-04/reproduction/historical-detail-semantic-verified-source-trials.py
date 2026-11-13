import json
from pathlib import Path
import numpy as np
B=Path('build-native/territorial-recipe');O=B/'boundary-semantic-review-2026-11-05';review=json.loads((B/'east-mask-review-2026-11-05/feature-review.json').read_text(encoding='utf-8-sig'));samples=json.loads((B/'historical-detail-final-metric-input.json').read_text(encoding='utf-8-sig'))['samples'];proof=json.loads((B/'strong-independent-2026-11-05/anchor-proofs.json').read_text(encoding='utf-8-sig'))['east'];rows=json.loads((O/'named-anchor-constrained-trials.json').read_text(encoding='utf-8-sig'))
def dp(a,t,anchors):
 a=np.asarray(a);keep={0,len(a)-1,*anchors};k=sorted(keep);stack=list(zip(k,k[1:]))
 while stack:
  l,r=stack.pop()
  if r-l<2:continue
  v=a[r]-a[l];q=a[l+1:r]-a[l];den=v@v;u=np.clip(q@v/den,0,1)if den else np.zeros(len(q));d=np.sum((q-u[:,None]*v)**2,axis=1);j=int(np.argmax(d))+l+1
  if d[j-l-1]>t*t:keep.add(j);stack.extend([(l,j),(j,r)])
 return sorted(keep)
for fi in [18,20]:
 s=next(x for x in samples if x.get('featureIndex')==fi);ref=next(x for x in review if x['feature']==fi);anchors=set(ref['categories_overlapping']['source_mask_anchor_reason_unspecified']['current_indices'])|set(next(x for x in proof if x['feature']==fi)['macro'])|{0,len(s['historical'])-1};cs=s['geographic']['historical']['coordinates'];trials=[]
 for tol in [250,500]:
  keep=dp(s['historical'],tol,anchors);trials.append({'tolerance_m':tol,'keep':keep,'points':len(keep),'coordinates':[cs[i]for i in keep]})
 rows.append({'feature':fi,'original_points':len(cs),'anchor_indices':sorted(anchors),'anchor_count':len(anchors),'policy':'Hold all mapped original source-mask anchors, named/technical endpoints, feature endpoints and algorithmic2km macro bends; prior shortcut/40degree checks are not independent meaning points.','sourceEvidence':'Upstream exact ZIP map/mask/master hashes and current coordinate subset confirmed; local original pixel review only forJ43-028.','trials':trials})
rows.sort(key=lambda x:x['feature']);(O/'verified-source-constrained-trials.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps([{'feature':r['feature'],'anchors':r['anchor_count'],'trials':[(t['tolerance_m'],t['points'])for t in r['trials']]}for r in rows]))
