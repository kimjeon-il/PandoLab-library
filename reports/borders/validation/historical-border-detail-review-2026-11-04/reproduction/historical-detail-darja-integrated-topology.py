from historical_detail_membership import *
n=load(base+'historical-detail-darja-integrated-native-candidate.json');c=load(base+'historical-detail-darja-integrated-compiled-candidate.json');geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));rows=[]
def structure(g):
 if g.GetGeometryName()=='MULTIPOLYGON':return [g.GetGeometryCount(),sum(g.GetGeometryRef(i).GetGeometryCount()-1 for i in range(g.GetGeometryCount()))]
 return [1,g.GetGeometryCount()-1]
for r in c['rows']:
 s=next(v for v in n['rows'] if v['entityId']==r.get('sourceEntityId',r['entityId']));v=lambda side:next(v for v in s[side]['geometryVersions'] if v['versionId']==r['versionId']);a,b,old,new=geo(r['before']),geo(r['after']),geo(v('before')['geometry']),geo(v('after')['geometry']);outside=a.SymDifference(b).Difference(old.SymDifference(new).Buffer(1e-10));row={'entityId':r['entityId'],'nativeValid':new.IsValid(),'compiledValid':b.IsValid(),'nativeBefore':structure(old),'nativeAfter':structure(new),'compiledBefore':structure(a),'compiledAfter':structure(b),'outsideSourceDeltaDeg2':outside.GetArea(),'datesIdentityUnchanged':[(v['versionId'],v['validFrom'],v['validTo']) for v in s['before']['geometryVersions']]==[(v['versionId'],v['validFrom'],v['validTo']) for v in s['after']['geometryVersions']] and s['before']['lifetime']==s['after']['lifetime'],'editedArcs':len(r['receipts'])};assert row['nativeValid'] and row['compiledValid'] and row['nativeBefore']==row['nativeAfter'] and row['compiledBefore']==row['compiledAfter'] and row['datesIdentityUnchanged'] and row['outsideSourceDeltaDeg2']<1e-12;rows.append(row);print(row,flush=True)
shared=[]
for r in c['rows']:
 cover=Cover(r['after'])
 for receipt in r['receipts']:
  expected=[(a,b) for a,b in zip(receipt['afterArc'],receipt['afterArc'][1:]) if a!=b];count=sum(cover.includes(a,b) for a,b in expected);assert count==len(expected);shared.append({'patch':receipt['id'],'entity':r['entityId'],'nonzeroEdges':count})
family=[r for r in c['rows'] if r['entityId'].startswith('state:soviet-union') and r['versionId'].endswith('1922-12-30-reviewed-v2')];union=lambda side:__import__('functools').reduce(lambda a,b:a.Union(b),[geo(r[side]) for r in family[1:]]);parent=family[0];beforeResidual=geo(parent['before']).SymDifference(union('before'));afterResidual=geo(parent['after']).SymDifference(union('after'));residual=beforeResidual.SymDifference(afterResidual).GetArea();assert residual<1e-12
json.dump({'scope':'Five changed historical versions only; no catalog regeneration','rows':rows,'sharedCopies':shared,'founderPartitionResidualChangeDeg2':residual},open(base+'historical-detail-darja-integrated-topology.json','w'),indent=2);print('PASS integrated topology, founder residual change',residual,flush=True)
