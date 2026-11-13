from historical_detail_membership import *
d=load(base+'historical-detail-east-candidate.json');raw=load(base+'historical-detail-line-2.geojson');old=[];new=[]
for fi,f in enumerate(raw['features']):
 cs=f['geometry']['coordinates'];ns=[p for i,p in enumerate(cs) if i not in d['spec'].get(str(fi),[])];old+=cs[1:] if old else cs;new+=ns[1:] if new else ns
sha=lambda c:hashlib.sha256(json.dumps(c,separators=(',',':')).encode()).hexdigest()
print('Python original/candidate SHA',sha(old),sha(new),flush=True)
assert old==d['originalChain'] and new==d['candidateChain']
assert sha(old)=='3ac508edf85114dbd6097931282f6affce93042e35978a6a85bfd4e125630fb4' and sha(new)=='c322ca78155c5166dba6de381ddaa9075e215498e88182de93123557b9bd7740'
for sid in ['state:soviet-union','state:soviet-union-russian-sfsr']:
 e=load('assets/data/territorial-entities/source/countries/'+sid.replace(':','-')+'.json')
 for v in e['geometryVersions']:
  matches=[]
  for ri,r in enumerate(rings(v['geometry'])):
   for i,p in enumerate(r):
    if p==old[0] and r[i:i+len(old)]==old:matches.append({'ring':ri,'index':i,'direction':1})
    if p==old[-1] and r[i:i+len(old)]==old[::-1]:matches.append({'ring':ri,'index':i,'direction':-1})
  print(sid,v['versionId'],matches,flush=True)
