from historical_detail_membership import *
d=load(base+'historical-detail-active-composites.json'); iran=load('assets/data/territorial-entities/source/countries/state-IRN.json');water=load('assets/data/territorial-entities/source/countries/waterbody-caspian.json');ussr=load('assets/data/territorial-entities/source/countries/state-soviet-union.json');modern=Cover(next(v for v in iran['geometryVersions'] if v['versionId']=='state:IRN:natural-earth-5.1.1')['geometry']);wc=Cover(next(v for v in water['geometryVersions'] if v['versionId']=='caspian-near1922-approved')['geometry']);sc=Cover(next(v for v in ussr['geometryVersions'] if v['versionId'].endswith('1922-12-30-reviewed-v2'))['geometry']);out=[]
for c in d['countries']:
 if c['entityId']!='IRN':continue
 for r in c['records']:
  cc=Cover(r['geometry'])
  for binding in r['coverage']:
   v=next(v for v in iran['geometryVersions'] if v['versionId']==binding['sourceVersionId']);groups=defaultdict(list)
   for a,b in edges(v['geometry']):
    role='modern' if modern.includes(a,b) else 'historical-water' if wc.includes(a,b) else 'reviewed-USSR' if sc.includes(a,b) else 'unexplained';groups[role].append((a,b))
   counts={role:{'nativeEdges':len(es),'presentInCompiled':sum(cc.includes(a,b) for a,b in es)} for role,es in groups.items()};row={'versionId':v['versionId'],'geometryRef':r['geometryRef'],'coverage':binding,'counts':counts};out.append(row);print(json.dumps(row),flush=True)
json.dump({'dataRevision':d['dataRevision'],'epsilonDegrees':EPS,'epsilonMeaning':'Numerical collinear containment, not display tolerance','rows':out},open(base+'historical-detail-iran-compiled-chains.json','w'),indent=2)
