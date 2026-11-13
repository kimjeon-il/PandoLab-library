from historical_detail_membership import *
from pathlib import Path
R=Path(base)/'historical-detail-darja-bundle';plan=load(str(R/'staging-plan.json'));whole=load(str(R/'candidate-whole-countries.json'))['rows'];edits=load(base+'historical-detail-darja-integrated-compiled-candidate.json')['rows'];peerInputs=load(base+'historical-detail-final-peer-inputs.json');geo=lambda x:ogr.CreateGeometryFromJson(json.dumps(x))
def surface(g):
 if g.IsEmpty():return 0.0
 if g.GetGeometryName()=='POLYGON':return g.GetArea()
 if g.GetGeometryName() in ['MULTIPOLYGON','GEOMETRYCOLLECTION']:return sum(surface(g.GetGeometryRef(i)) for i in range(g.GetGeometryCount()))
 return 0.0
def actual(row,side):
 country=next(c[side] for c in whole if c['entityId']==row['entityId']);binding=next(b for b in country['sourceBindings'] if b['sourceVersionId']==row['versionId']);return next(g['geojson'] for g in country['geometries'] if g['id']==binding['geometryRef']['id'] and g['version']==binding['geometryRef']['version'])
rows=[]
for p in peerInputs:
 for spec in p['geometries']:
  peer=geo(spec['geojson'])
  for e in edits:
   before,after=geo(actual(e,'before')),geo(actual(e,'after'));oldOverlap,newOverlap=before.Intersection(peer),after.Intersection(peer);oldShared,newShared=before.Boundary().Intersection(peer.Boundary()),after.Boundary().Intersection(peer.Boundary());metric={'entityId':e['entityId'],'versionId':e['versionId'],'foreignPeer':p['entityId'],'old2dOverlapDegree2':surface(oldOverlap),'new2dOverlapDegree2':surface(newOverlap),'overlap2dDifferenceDegree2':surface(oldOverlap.SymDifference(newOverlap)),'sharedContactDifferenceLengthDegrees':oldShared.SymDifference(newShared).Length()};assert metric['overlap2dDifferenceDegree2']<=1e-12 and metric['sharedContactDifferenceLengthDegrees']<=1e-8;rows.append(metric)
retained=[]
for family in load(base+'historical-detail-konotop-tc-current-chains.json')['rows']:
 ids=['soviet-union-transcaucasian-sfsr','soviet-union-russian-sfsr'] if family['id'].startswith('tc') else ['soviet-union-ukrainian-ssr','soviet-union-russian-sfsr']
 for chunk in family['chunks']:
  cs=chunk['coordinates']
  if len(cs) not in [59,833,63,99]:continue
  for id in ids:
   selected=next((e for e in edits if e['entityId']=='state:'+id and e['versionId'].endswith('1922-12-30-reviewed-v2')),None)
   geometry=actual(selected,'after') if selected else load(base+'historical-detail-retain-'+id+'.json')['geometries'][0]['geojson'];cover=Cover(geometry);count=sum(cover.includes(a,b) for a,b in zip(cs,cs[1:]));assert count==len(cs)-1;retained.append({'chain':family['id'],'points':len(cs),'entityId':'state:'+id,'allRetainedEdges':count})
with (R/'foreign-peer-and-retained-proof.json').open('x',encoding='utf-8') as f:json.dump({'scope':'Three stored actual foreign peer geometries x six changed country version bindings, plus eight retained source residual chain copies. No world regeneration. Areas use Polygon members only.','foreignComparisons':rows,'retainedCompiledChains':retained},f,indent=2)
print({'foreignComparisons':len(rows),'retainedChainCopies':len(retained),'status':'passed'},flush=True)
