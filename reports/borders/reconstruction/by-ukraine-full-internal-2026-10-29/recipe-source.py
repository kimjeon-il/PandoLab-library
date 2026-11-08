import json,pathlib,copy,hashlib,itertools,subprocess,gzip
from osgeo import ogr
R=pathlib.Path(__file__).parent;B=R.parent/'belarus-ukraine-review';F='1922-12-30';T='1925-05-12'
load=lambda p:json.loads(p.read_bytes())
base=load(B/'full-coverage/baseline-four-arcs.geojson');arcs={f['properties']['arc_id']:f['geometry']['coordinates'] for f in base['features']}
names=['byelorussian-ssr','ukrainian-ssr','russian-sfsr'];changes={'BY-RU':('by-ru-display.geojson',[names[0],names[2]]),'BY-UA':('by-ua-display.geojson',[names[0],names[1]]),'UA-RU-MAIN':('ua-ru-main-display.geojson',[names[1],names[2]])}
def shape(g):return ogr.CreateGeometryFromJson(json.dumps(g))
def replace(g,seq,repl):
 out=copy.deepcopy(g);polys=[out['coordinates']] if out['type']=='Polygon' else out['coordinates'];hits=[]
 for pi,p in enumerate(polys):
  for ri,ring in enumerate(p):
   for s,r in [(seq,repl),(seq[::-1],repl[::-1])]:
    for i in range(len(ring)-len(s)+1):
     if ring[i:i+len(s)]==s:p[ri]=ring[:i]+r+ring[i+len(s):];hits.append([pi,ri,i]);break
 assert len(hits)==1,hits
 return out,hits
old=[];new=[];proof=[]
for name in names:
 a=load(B/'baseline'/f'{name}-source.json');b=copy.deepcopy(a);versions=[(i,v) for i,v in enumerate(b['geometryVersions']) if v.get('validFrom')==F and v.get('validTo')==T];assert len(versions)==1;i,v=versions[0];old.append(shape(v['geometry']));hits={};hashes={}
 for arc,(file,owners) in changes.items():
  if name in owners:
   p=R/'evidence'/file;repl=load(p)['geometry']['coordinates'];assert repl[0]==arcs[arc][0] and repl[-1]==arcs[arc][-1];v['geometry'],hits[arc]=replace(v['geometry'],arcs[arc],repl);hashes[arc]=hashlib.sha256(p.read_bytes()).hexdigest()
 v['internalBoundaryRefinement']={'status':'provisional-source-fidelity-refinement','scope':'Full BY/Ukraine internal shared arcs reviewed; source-unreadable sections and all Crimea99 vertices retained','candidateSha256':hashes,'displayToleranceMetres':100,'historicalAccuracyMetres':None,'sourceDates':{'Belarus':'1924 publication with explicit 1920–1924 old-border symbol','Ukraine':'1922-01 depicted; month precision, not proof unchanged through December'},'validFrom':F,'validTo':T,'transitionDate':None,'temporalHold':'Existing coverage retained, not newly established historical validity; Belarus 1924 expansion and Jan-to-Dec Ukraine validity unresolved. 1925-05-12 is not inferred event date.','report':'reports/borders/reconstruction/by-ukraine-full-internal-2026-10-29/README.md'}
 new.append(shape(v['geometry']));assert new[-1].IsValid();stem=a['entityId'].replace(':','-')+'.json'
 for folder,e in [('source-original',a),('source-new',b)]:(R/folder/stem).write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')
 assert all(a[k]==b[k] for k in a if k!='geometryVersions');assert all(x==b['geometryVersions'][j] for j,x in enumerate(a['geometryVersions']) if j!=i)
 proof.append({'entityId':a['entityId'],'versionId':v['versionId'],'ringHits':hits,'outsideVersionsUnchanged':True,'lifetimeUnchanged':True,'valid':True})
union=lambda gs:gs[0].Union(gs[1]).Union(gs[2])
r={'base':'cbf25b306d9b58b2febc3c69bc8f3e4c14a80e43','from':F,'to':T,'source':proof,'unionSymdiff':union(old).SymDifference(union(new)).Area(),'pairOverlap':[a.Intersection(b).Area() for a,b in itertools.combinations(new,2)],'points':{'BY-RU':164,'BY-UA':47,'UA-RU-MAIN':369,'CRIMEA-retained':99}}
assert r['unionSymdiff']==0 and max(r['pairOverlap'])==0
(R/'source-proof.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
