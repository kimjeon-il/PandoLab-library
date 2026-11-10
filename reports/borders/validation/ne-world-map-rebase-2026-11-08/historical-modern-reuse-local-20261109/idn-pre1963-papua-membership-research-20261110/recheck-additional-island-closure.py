from pathlib import Path
import json,hashlib
from shapely.geometry import Polygon,shape
from shapely.strtree import STRtree
r=Path(__file__).parent;out=r/'additional-connected-islands-review';load=lambda p:json.loads(p.read_text(encoding='utf8'));review=load(out/'individual-visual-review.json');fixed=load(r/'fixed-idn-input.json');D=fixed['entity']['geometryVersions'][-1]['geometry']['coordinates'];DP=[Polygon(p[0],p[1:])for p in D];dt=STRtree(DP)
ne=load(r.parent/'idn-modern-equivalence-audit-20261110/source-inputs.json')['ne'];N=next(f['geometry']['coordinates']for f in ne['features']if f['id']=='IDN');NP=[Polygon(p[0],p[1:])for p in N];nt=STRtree(NP)
def xy(c):return c[:2]if isinstance(c[0],(int,float))else[xy(v)for v in c]
sources={};proof=[]
for q in review['accepted']:
 a=q['officialConnectedLandmass'];f=r/'public-sources'/a['sourceFile']
 if f.name not in sources:
  g=load(f)['features'][0]['geometry'];s=shape({'type':g['type'],'coordinates':xy(g['coordinates'])});sources[f.name]=([s]if s.geom_type=='Polygon'else list(s.geoms),hashlib.sha256(f.read_bytes()).hexdigest())
 pieces,digest=sources[f.name];land=pieces[a['sourcePolygonIndex']];di=q['modernIndex'];ni=q['originalNEIndex'];modernContacts=[int(i)for i in dt.query(land)if land.intersects(DP[i])];positive=[i for i in modernContacts if land.intersection(DP[i]).area>0];neContacts=[int(i)for i in nt.query(land)if land.intersection(NP[i]).area>0];donorTouches=[int(i)for i in dt.query(DP[di])if i!=di and DP[di].intersects(DP[int(i)])]
 passed=positive==[di]and modernContacts==[di]and neContacts==[ni]and not donorTouches
 proof.append({'originalNEIndex':ni,'modernIndex':di,'rawOfficialSource':a['sourceFile'],'rawOfficialSourceSha256':digest,'connectedPolygonIndex':a['sourcePolygonIndex'],'rawOfficialXYUnchanged':True,'allModernPositiveAreaIntersections':positive,'allModernContactsIncludingBoundaryOnly':modernContacts,'allOriginalNEPositiveAreaIntersections':neContacts,'otherModernComponentsTouchingSelectedDonor':donorTouches,'closurePassed':passed})
allPassed=all(x['closurePassed']for x in proof);failed=[x for x in proof if not x['closurePassed']]
data={'status':'passed'if allPassed else 'pending groups found; do not apply this candidate','sourceRevision':load(out/'current-source-binding.json')['sourceRevision'],'recomputedFromRawOfficialPolygons':True,'approvedModernUniverseCount':len(DP),'originalNEUniverseCount':len(NP),'selectedGroups':len(proof),'noOtherDonorEvenTouchesOfficialConnectedLand':all(x['allModernContactsIncludingBoundaryOnly']==[x['modernIndex']]for x in proof),'noOtherDonorTouchesSelectedModernComponent':all(not x['otherModernComponentsTouchingSelectedDonor']for x in proof),'groups':proof,'scope':'Physical connected-landmass closure only, not an exclusion rule for offshore or unresolved components. No buffered/proximity or area-size cutoff used.'};f=out/'closure-recheck.json';f.write_text(json.dumps(data,indent=2)+'\n');assert load(f)==data;print(json.dumps({'status':data['status'],'groups':len(proof),'failed':failed}))
