from historical_detail_membership import *
import copy
sp=load(base+'historical-detail-west-darja-spec.json');sha=lambda c:hashlib.sha256(json.dumps(c,separators=(',',':')).encode()).hexdigest();raw=load('assets/data/territorial-entities/source/countries/state-soviet-union.json');v=next(v for v in raw['geometryVersions'] if v['versionId'].endswith('1922-12-30-reviewed-v2'));arcs=[]
for s in sp['west']+[sp['darja']]:
 matches=[]
 for r in rings(v['geometry']):
  for i,p in enumerate(r):
   if p==s['start'] and i+s['oldPoints']<=len(r) and r[i+s['oldPoints']-1]==s['end']:matches.append(r[i:i+s['oldPoints']])
 assert len(matches)==1,(s['name'],'anchor lookup',len(matches));old=matches[0];new=[old[i] for i in s['retained']];print(s['name'],len(old),len(new),sha(old),sha(new),flush=True);assert sha(old)==s['oldSha'] and sha(new)==s['newSha'],('Hash mismatch',s['name']);arcs.append({**s,'old':old,'new':new})
json.dump({'status':'Verified coordinate instructions, no production writes','arcs':arcs},open(base+'historical-detail-west-darja-arcs.json','w'),indent=2)
