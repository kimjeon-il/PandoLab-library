from historical_detail_membership import *
import copy
spec=load(base+'historical-detail-west-darja-arcs.json')['arcs'];east=load(base+'historical-detail-east-candidate.json');arcs=[{'name':'east-selected-151','old':east['originalChain'],'new':east['candidateChain']},*spec[:2]];sid=['state:soviet-union','state:soviet-union-russian-sfsr','state:soviet-union-byelorussian-ssr'];out=[]
def substitute(g,old,new,subdivision=False):
 hits=[];oldCover=Cover({'type':'LineString','coordinates':old}) if subdivision else None
 for pi,p in enumerate([g['coordinates']] if g['type']=='Polygon' else g['coordinates']):
  for ri,r in enumerate(p):
   for forward in [True,False]:
    first,last=(old[0],old[-1]) if forward else (old[-1],old[0]);replacement=new if forward else new[::-1]
    starts=[i for i,a in enumerate(r[:-1]) if a==first];ends=[i for i,a in enumerate(r[:-1]) if a==last]
    for i in starts:
     for j in ends:
      if j<=i:continue
      piece=r[i:j+1];match=piece==(old if forward else old[::-1])
      if subdivision and not match:match=all(oldCover.includes(a,b) for a,b in zip(piece,piece[1:])) and all(Cover({'type':'LineString','coordinates':piece}).includes(a,b) for a,b in zip(old,old[1:]))
      if match:hits.append((p,ri,i,j,replacement))
 if len(hits)>1:raise RuntimeError('Multiple exact arc matches')
 for p,ri,i,j,new in hits:p[ri]=p[ri][:i]+new+p[ri][j+1:]
 return len(hits)
for id in sid:
 f='assets/data/territorial-entities/source/countries/'+id.replace(':','-')+'.json';before=load(f);after=copy.deepcopy(before);changes=[]
 for v in after['geometryVersions']:
  for arc in arcs:
   count=substitute(v['geometry'],arc['old'],arc['new'],subdivision=id=='waterbody:caspian' and arc['name']=='darja-400m-protected')
   if count:changes.append({'versionId':v['versionId'],'arc':arc['name'],'substitutions':count})
  if any(c['versionId']==v['versionId'] for c in changes):assert ogr.CreateGeometryFromJson(json.dumps(v['geometry'])).IsValid()
 print(id,changes,flush=True);out.append({'entityId':id,'sourceFile':f,'before':before,'after':after,'changes':changes})
assert sum(len(r['changes']) for r in out)==6,[(r['entityId'],len(r['changes'])) for r in out]

json.dump({'status':'Local staged candidate only; canonical writers not yet called','dataRevision':'a548d5fa6612a97f998b7bdb326a27eb8b8d9717','rows':out},open(base+'historical-detail-country-only-native-candidate.json','w'))

