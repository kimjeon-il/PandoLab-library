import json,sys
from pathlib import Path
sys.path.insert(0,'recovery/baikonur/deps')
from shapely.geometry import shape,LineString,mapping
R=Path('research/europe1922');O=R/'application-prepared-v1';M=json.load(open(O/'application-manifest.json'));N=[x['entity']for x in M['entities']];new={n:json.load(open(O/(n+'-source-display-geometry.json')))for n in N};J1,J2=M['junctions']
p=json.load(open(R/'poland/whole-continuous-v1/poland-continuous-candidate.geojson'))['geometry']['coordinates'];j=json.load(open(R/'poland/application-readonly-plan/application-junctions.json'))['junctions']
for x in sorted(j,key=lambda a:a['candidateSegments'][0]['index'],reverse=True):p.insert(x['candidateSegments'][0]['index']+1,x['newIntersection'])
i1=p.index(J1);i2=p.index(J2);parts=[p[:i1+1],p[i1:i2+1],p[i2:]];proof=[]
for n,q in zip(N[1:],parts):
 l=LineString(q);a=l.difference(shape(new[N[0]]).boundary).length;b=l.difference(shape(new[n]).boundary).length
 assert a<1e-10 and b<1e-10,(n,a,b)
 proof.append({'entity':n,'shared_new_poland_boundary_missing_from_USSR_degree_length':a,'missing_from_republic_degree_length':b,'start':q[0],'end':q[-1]})
modern=json.load(open(R/'finland/modern-reuse/modern-interior-candidates.geojson'))['features'];allp=[q for ft in modern for q in ft['geometry']['coordinates']];u=new[N[0]]['coordinates'][0][0];modernok=all(q in u for q in allp)
print('moderncount',len(allp),'preserved',modernok)
# Exact coast subsequences, not only vertex presence.
old=json.load(open('research/europe-approved-baseline/state-soviet-union-source.json'));v=next(x for x in old['geometryVersions']if x['versionId']=='state:soviet-union:1922-12-30-reviewed-v2');r=v['geometry']['coordinates'][0][0]
def subseq(a,b):return any(a[i:i+len(b)]==b for i in range(len(a)-len(b)+1))
coasts={'south1397_1406_exact_subsequence':subseq(u,r[1397:1407]),'north2152_2154_exact_subsequence':subseq(u,r[2152:2155])};assert all(coasts.values())
json.dump({'shared_poland':proof,'Finland_modern_original_count':len(allp),'Finland_modern_vertices_preserved':modernok,'coasts':coasts,'river_policy':'Poland1991 all exact preserved with2intersections inserted, Estonia10points preserved, Finland380 unchanged, Latviaoutside1631..1637 unchanged by mask proof'},open(O/'shared-and-locked-guards.json','w'),indent=2)
print(proof,coasts)
