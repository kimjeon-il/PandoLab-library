from historical_detail_membership import *
c=load(base+'historical-detail-integrated-compiled-candidate.json');peers=load(base+'historical-detail-final-peer-inputs.json');geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x));out=[]
for peer in peers:
 for p in peer['geometries']:
  g=geo(p['geojson'])
  for r in c['rows']:
   a,b=geo(r['before']),geo(r['after']);overlap=a.Intersection(g).SymDifference(b.Intersection(g)).GetArea();shared=a.Boundary().Intersection(g.Boundary()).SymDifference(b.Boundary().Intersection(g.Boundary())).Length();assert overlap<1e-12 and shared<1e-8;out.append({'entity':r['entityId'],'peer':peer['entityId'],'overlapDifferenceDeg2':overlap,'sharedDifferenceDegrees':shared})
retained=[]
for family in load(base+'historical-detail-konotop-tc-current-chains.json')['rows']:
 ids=['soviet-union-transcaucasian-sfsr','soviet-union-russian-sfsr'] if family['id'].startswith('tc') else ['soviet-union-ukrainian-ssr','soviet-union-russian-sfsr']
 for chunk in family['chunks']:
  if len(chunk['coordinates']) not in [59,833,63,99]:continue
  cs=chunk['coordinates']
  for id in ids:
   old=load(base+'historical-detail-retain-'+id+'.json')['geometries'][0]['geojson'];latest=next((r['after'] for r in c['rows'] if r['entityId']=='state:'+id),old);cover=Cover(latest);count=sum(cover.includes(a,b) for a,b in zip(cs,cs[1:]));assert count==len(cs)-1;retained.append({'chain':family['id'],'points':len(cs),'entity':id,'compiledEdgesCovered':count})
json.dump({'foreignPeers':out,'retainedResidualCompiledProof':retained},open(base+'historical-detail-integrated-peer-and-retain.json','w'),indent=2);print('PASS',len(out),'foreign peer comparisons;',len(retained),'retained compiled chain copies',flush=True)
