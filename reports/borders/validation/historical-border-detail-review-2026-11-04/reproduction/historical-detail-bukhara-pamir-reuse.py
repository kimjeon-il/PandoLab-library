from historical_detail_membership import *
sp=load(base+'historical-detail-central-arc-patch-spec.json');endpoint=sp['bukhara']['replacement_coordinates_preserved_reference_only'][-1];ne=load('assets/data/countries-ne-5.1.1.geojson');afg=Cover(next(f['geometry'] for f in ne['features'] if f['id']=='AFG'));s=load('assets/data/territorial-entities/source/countries/state-soviet-union.json');v=next(v for v in s['geometryVersions'] if v['versionId'].endswith('1922-12-30-reviewed-v2'));out=[]
for ri,r in enumerate(rings(v['geometry'])):
 for i,p in enumerate(r):
  if p!=endpoint:continue
  for direction in [-1,1]:
   chain=[p];j=i
   while 0<=j+direction<len(r) and afg.includes(r[j],r[j+direction]):j+=direction;chain.append(r[j])
   out.append({'ring':ri,'startIndex':i,'direction':direction,'points':len(chain),'lastIndex':j,'last':chain[-1],'coordinates':chain});print({k:v for k,v in out[-1].items() if k!='coordinates'},flush=True)
json.dump({'endpoint':endpoint,'status':'Current native modern-AFG collinear containment at Bukhara endpoint; geometry unchanged','runs':out},open(base+'historical-detail-bukhara-pamir-reuse.json','w'),indent=2)
