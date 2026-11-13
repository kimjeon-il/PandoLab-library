from historical_detail_membership import *
d=load(base+'historical-detail-east-candidate.json');old=d['originalChain'];new=d['candidateChain'];active=load(base+'historical-detail-active-composites.json');outputs=[]
for c in active['countries']:
 if c['entityId'] not in ['state:soviet-union','state:soviet-union-russian-sfsr']:continue
 for record in c['records']:
  before=record['geometry'];after=json.loads(json.dumps(before));matches=[]
  for pi,p in enumerate([after['coordinates']] if after['type']=='Polygon' else after['coordinates']):
   for ri,r in enumerate(p):
    for i,point in enumerate(r):
     if point==old[0] and r[i:i+len(old)]==old:p[ri]=r[:i]+new+r[i+len(old):];matches.append([pi,ri,i])
  print(c['entityId'],'compiled chain matches',matches,flush=True)
  if len(matches)!=1:raise RuntimeError('Compiled chain must match once')
  a=ogr.CreateGeometryFromJson(json.dumps(before));b=ogr.CreateGeometryFromJson(json.dumps(after));print('valid',a.IsValid(),b.IsValid(),'xor deg2',a.SymDifference(b).GetArea(),flush=True)
  outputs.append({'entityId':c['entityId'],'sourceVersionId':record['coverage'][0]['sourceVersionId'],'beforeCompiledRef':record['geometryRef'],'before':before,'after':after,'coverage':record['coverage'],'match':matches})
json.dump({'status':'Candidate not written to source/native/compiled','dataRevision':active['dataRevision'],'rows':outputs},open(base+'historical-detail-east-compiled-candidate.json','w'),indent=2)
