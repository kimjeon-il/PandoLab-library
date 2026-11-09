import json,hashlib,time
from pathlib import Path
import shapely
from shapely.geometry import shape
from shapely.strtree import STRtree
B=Path('D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/current-source-adoption-review');O=B/'adjacency-review';start=time.time();x=json.loads((B/'source-review-input.json').read_text(encoding='utf8'));binding=json.loads((O/'canonical-binding-1f2f20ae.json').read_text());assert hashlib.sha256((B/'source-review-input.json').read_bytes()).hexdigest()==binding['priorTopologyProof']['inputSha256']
fs=x['neighbors']; gs=[shape(f['geometry']) for f in fs]; tree=STRtree(gs); targets={r['featureId'] for r in x['rows']};pairs=[];bad=[]
for i,g in enumerate(gs):
 if not g.is_valid or g.is_empty:bad.append({'id':fs[i]['id'],'valid':g.is_valid,'empty':g.is_empty})
 for j in tree.query(g,predicate='intersects'):
  j=int(j)
  if j<=i or not(fs[i]['id'] in targets or fs[j]['id'] in targets):continue
  q=g.intersection(gs[j]); a,b=fs[i]['id'],fs[j]['id'];intent=set([a,b]) in [set(['KAZ','KAB']),set(['COL','SER']),set(['COL','BJN'])]
  pairs.append({'a':a,'b':b,'type':q.geom_type,'polygonAreaDegrees2':q.area,'intendedPolicyOverlap':intent,'numericResidualUnderPrior1e12':0<q.area<=1e-12})
out={'status':'fresh-bounded-current257-contact-check','revision':binding['revision'],'canonicalBindingSha256':hashlib.sha256((O/'canonical-binding-1f2f20ae.json').read_bytes()).hexdigest(),'inputSha256':binding['priorTopologyProof']['inputSha256'],'source':'Exact hash-rebound approved257 current geometry input; no stale generated chunks used.','engine':{'shapely':shapely.__version__,'geos':shapely.geos_version_string},'scope':{'changedSelectedVersions':250,'directPolicyOrPairedInputs':7,'unrelatedCatalogValidation':False},'validityFailures':bad,'pairs':pairs,'unexpectedOverlapsAbovePriorTolerance':[p for p in pairs if p['polygonAreaDegrees2']>1e-12 and not p['intendedPolicyOverlap']],'nonzeroResiduals':[p for p in pairs if p['numericResidualUnderPrior1e12']],'elapsedSeconds':time.time()-start,'limits':['Not an independent geographic gap/completeness test.','All nonzero double-precision area residuals retained; no rounding or precision change.','No projected area conversion; line geometry area is zero.','Coherent PGA retirement and compiled/runtime receipt gates remain separate.']}
(O/'fresh-current-contacts.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='pairs'}));print('contacts',len(pairs))
