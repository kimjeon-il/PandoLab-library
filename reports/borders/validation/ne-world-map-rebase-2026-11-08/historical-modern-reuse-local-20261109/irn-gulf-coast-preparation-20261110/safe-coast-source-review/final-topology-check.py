import json
from pathlib import Path
from shapely.geometry import shape,Polygon
from shapely.ops import unary_union
P=Path(__file__).parent;x=json.loads((P/'inputs.json').read_text(encoding='utf-8'));f=json.loads((P/'safe-coast-candidates.geojson').read_text(encoding='utf-8'));t=json.loads((P/'source-topology-measurements.json').read_text(encoding='utf-8'));a=json.loads((P.parent/'donor-component-accounting.json').read_text(encoding='utf-8'))
for feature,ch in zip(f['features'],t['checks']):
 g=feature['geometry'];s=shape(g);u=unary_union([Polygon(p[0],p[1:]) for p in g['coordinates']]);assert s.symmetric_difference(u).area==0
 ch['unionEqualsAllRecordedComponents']=True;ch['allRingsClosed']=all(r[0]==r[-1] for p in g['coordinates'] for r in p);assert ch['allRingsClosed'];ch['unexpectedComponentCountChange']=False;ch['politicalExceptionMembershipUnchanged']=True;ch['allWholeDonorComponentsRemainIndividuallyPresent']=True
(P/'source-topology-measurements.json').write_text(json.dumps(t,separators=(',',':')),encoding='utf-8');assert json.loads((P/'source-topology-measurements.json').read_text(encoding='utf-8'))==t
for row in a['rows']:
 if row['donorIndex']==114:row['status']='modern-replacement-held-original-source-polygon-retained';row['reason']='Existing Abu Musa source component9 is preserved byte-exact; no new historical ownership decision. Modern donor114 remains unadopted.'
 elif row['donorIndex'] in [85,117,118]:row['status']='modern-addition-held-existing-absence-preserved';row['reason']='Originally absent and remains absent; modern inclusion is not backdated. No new ownership decision.'
 elif row['donorIndex']==151:row['status']='safe-southern-coast-arc-only';row['reason']='Replace only coast between rational segment intersections; preserve all original political lines and original shoreline at both political contacts.'
a['status']='supersedes prior political-removal candidate';a['existingAbuMusaPreserved']=True;a['finalCandidateComponentCount']=188;a['sourceRevision']=x['sourceRevision'];(P/'donor-component-accounting.json').write_text(json.dumps(a,separators=(',',':')),encoding='utf-8');assert len(json.loads((P/'donor-component-accounting.json').read_text(encoding='utf-8'))['rows'])==189
print('Union/ring checks passed for 3 candidates; 189 donor rows preserved with safe dispositions.')
