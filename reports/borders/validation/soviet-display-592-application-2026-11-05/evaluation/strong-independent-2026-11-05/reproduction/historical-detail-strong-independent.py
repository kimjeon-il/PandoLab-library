import json,hashlib,struct,subprocess,copy,math
from pathlib import Path
from collections import defaultdict
import numpy as np
B=Path('build-native/territorial-recipe');O=B/'strong-independent-2026-11-05';O.mkdir(exist_ok=True)
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(n,x): (O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def rings(g):
 for pi,p in enumerate(g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]):
  for ri,r in enumerate(p):yield pi,ri,r
def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
def digest(g):
 h=hashlib.sha256();h.update(g['type'].encode()+b'\0');ps=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']];h.update(struct.pack('>I',len(ps)))
 for p in ps:
  h.update(struct.pack('>I',len(p)))
  for r in p:
   h.update(struct.pack('>I',len(r)))
   for x,y in r:h.update(struct.pack('>dd',x,y))
 return h.hexdigest()
def dp(a,t,anchors=()):
 a=np.asarray(a);keep=set([0,len(a)-1,*anchors]);locks=sorted(keep);stack=list(zip(locks,locks[1:]))
 while stack:
  l,r=stack.pop()
  if r-l<2:continue
  d=a[r]-a[l];v=a[l+1:r]-a[l];den=float(d@d);u=np.clip(v@d/den,0,1) if den else np.zeros(len(v));dist=np.sum((v-u[:,None]*d)**2,axis=1);j=int(np.argmax(dist))+l+1
  if dist[j-l-1]>t*t:keep.add(j);stack.extend([(l,j),(j,r)])
 return sorted(keep)
assert dp([[0,0],[1,.1],[2,0]],.2)==[0,2]
assert dp([[0,0],[1,.1],[2,0]],.2,[1])==[0,1,2]
H={'USSR':'dab7724ba5c764269c6c56b0d84dca130072cd91d1a11e8cde05fff0b4b7e005','RSFSR':'740aa9e2790c761c60e556ae5081c5a156b63988bc5cb32a045ea269f7e752ce','BY':'4d30e7f72ac91019fef1d920f9c62b21e8b41814c596f82afd75d2873132ac80','UA':'b58447ab1d1c0983c7a05a5d6459201b1cf942afc008884d7a57e0a8e0c4db6c'}
original={};versions={}
for k,h in H.items():
 raw=subprocess.check_output(['git','show','a548d5fa6612a97f998b7bdb326a27eb8b8d9717:objects/'+h+'.json'],cwd=r'D:\dev\PandoLab-library-data\.pando-worktrees\gis');assert hashlib.sha256(raw).hexdigest()==h
 entity=json.loads(raw);v=next(v for v in entity['geometryVersions'] if v['versionId'].endswith('1922-12-30-reviewed-v2'));assert [v['validFrom'],v['validTo']]==['1922-12-30','1925-05-12'];original[k]=v['geometry'];versions[k]=v['versionId']
print('four immutable inputs verified',flush=True)
network=defaultdict(set)
for k,g in original.items():
 for _,_,r in rings(g):
  for a,b in zip(r,r[1:]):
   if a!=b:network[edge(a,b)].add(k)
west=load(B/'historical-detail-west-whole-view.json');westChoices={};anchorProof={}
for w in west:
 c=w['coordinates']['old'];p=np.asarray(w['projected']['old']);es=[edge(a,b) for a,b in zip(c,c[1:])];ee=set(es);owners=[tuple(sorted(network[e])) for e in es];assert all('USSR' in s for s in owners);idx={tuple(q):i for i,q in enumerate(c)};locks={0,len(c)-1};reasons=defaultdict(set)
 for i in locks:reasons[i].add('endpoint')
 for i in range(1,len(c)-1):
  if owners[i-1]!=owners[i]:locks.add(i);reasons[i].add('owner transition')
 for i,owner in enumerate(owners):
  if owner==('USSR',):
   for j in [i,i+1]:locks.add(j);reasons[j].add('unmatched counterpart')
 for g in original.values():
  for _,_,r in rings(g):
   n=len(r)-1
   for j,q in enumerate(r[:-1]):
    i=idx.get(tuple(q))
    if i is None:continue
    prev=r[(j-1)%n];nxt=r[(j+1)%n]
    reason='duplicate representation' if q==prev or q==nxt else ('untouched junction' if edge(q,prev) not in ee or edge(q,nxt) not in ee else None)
    if reason:locks.add(i);reasons[i].add(reason)
 for i in dp(p,2000,locks):locks.add(i);reasons[i].add('algorithmic 2km skeleton')
 anchorProof[w['id']]={str(i):sorted(reasons[i]) for i in sorted(locks)}
 for tol in ([250,500] if w['id']=='Latvia' else [250]):westChoices[w['id'],tol]=dp(p,tol,locks)
 print(w['id'],{str(t):len(k) for (name,t),k in westChoices.items() if name==w['id']},flush=True)
route=load(B/'historical-detail-east-candidate.json')['originalChain'];features=load(B/'historical-detail-line-2.geojson')['features'];samples=load(B/'historical-detail-final-metric-input.json')['samples'];eastSamples=[s for s in samples if s['id'].startswith('east-')];offset=0;featureStarts={}
for i,f in enumerate(features):featureStarts[i]=offset;offset+=len(f['geometry']['coordinates'])-1
assert offset+1==len(route)
removed=set();eastProof=[]
for s in eastSamples:
 i=s['featureIndex'];f=features[i];start=featureStarts[i];c=f['geometry']['coordinates'];assert route[start:start+len(c)]==c==s['geographic']['historical']['coordinates'];p=np.asarray(s['historical']);macro=dp(p,2000);keep=dp(p,500,macro);removed.update(start+j for j in range(1,len(c)-1) if j not in keep);eastProof.append({'feature':i,'old':len(c),'new':len(keep),'keep':keep,'macro':macro})
newroute=[p for j,p in enumerate(route) if j not in removed];print('East',sum(r['old'] for r in eastProof),sum(r['new'] for r in eastProof),len(newroute),flush=True)
p=features[25]['properties']['display_simplification_20261028'];mask=p['terrain_mask'];ret=p['retained_input_indices'];protected=set(p['protected_input_indices']);row=next(x for x in eastProof if x['feature']==25);keep=set(row['keep'])
def expand(rs):return set(i for a,b in rs for i in range(a,b+1))
cats={'possible_water_or_unknown':expand(mask['possibleWaterCrossingsVertexIntervalsInclusive']),'symbol_overlap_or_endpoint':expand(mask['overlapAndEndpointVertexIntervalsInclusive']),'major_bend_or_named_anchor':set(mask['majorBendAndNamedAnchorIndices'])}
proof={'mask_sha256':p['terrain_mask_sha256'],'mask_path':p['terrain_mask_source'],'direction':'raw_index = 205 - display_input_index; retained_input_indices map current position to display input','scope':mask['scope'],'not_claimed':'Each recorded point is not independently certified as a legal, river-following or named geographic landmark. Categories include uncertainty protection.','categories':{},'current_points':len(ret),'recorded_protected':len(protected),'candidate_points':len(keep)}
for label,rawindices in cats.items():
 current=[j for j,src in enumerate(ret) if src in protected and 205-src in rawindices];proof['categories'][label]={'count':len(current),'removed_by_500m':[j for j in current if j not in keep]}
proof['removed_recorded_protected_current_indices']=[j for j,src in enumerate(ret) if src in protected and j not in keep];proof['all_recorded_protected_covered_by_categories']=all(any(205-src in s for s in cats.values()) for src in protected)
write('pamir-exception-audit.json',proof);write('anchor-proofs.json',{'west':anchorProof,'east':eastProof})
expected={250:{'USSR':'115d694a463c32e82dd661861affd08e5649095c8feb0450b7e0d4dc58bb7fb2','RSFSR':'d1ad7f9be4708ec681329820568e80b174f17026c2d5d0f6d6a35e8278f5bd41','BY':'a914f565d93807a0e4f2ed11f94508e44a4b990a1eaf9aff466fdcb2fb3278c2','UA':'58491bf08128f2f6ec830e491446dfb14d97d6d5ad28290a5480719964b2fcae'},500:{'USSR':'7a1a3b83692fc473db1c8f961ba56a8dded5beda50e32e9b54d7628172600e1e','RSFSR':'afd3a06b7793389a65e962ac284225ed6850908abe1ef50308d1b0d3c800ea63','BY':'a914f565d93807a0e4f2ed11f94508e44a4b990a1eaf9aff466fdcb2fb3278c2','UA':'58491bf08128f2f6ec830e491446dfb14d97d6d5ad28290a5480719964b2fcae'}}
results=[]
for tol in [250,500]:
 deletions=set();editable=set()
 for w in west:
  c=w['coordinates']['old'];keep=set(westChoices[w['id'],tol if w['id']=='Latvia' else 250]);deletions.update(tuple(q) for i,q in enumerate(c) if i not in keep);editable.update(edge(a,b) for a,b in zip(c,c[1:]))
 cand=copy.deepcopy(original)
 for name,g in cand.items():
  for pi,ri,r in list(rings(g)):
   n=len(r)-1;nr=[q for j,q in enumerate(r[:-1]) if not(tuple(q) in deletions and edge(r[(j-1)%n],q) in editable and edge(q,r[(j+1)%n]) in editable)];nr.append(nr[0]);ps=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']];ps[pi][ri]=nr
  if name in ['USSR','RSFSR']:
   hits=0
   for pi,ri,r in list(rings(g)):
    for j,q in enumerate(r):
     if q==route[0] and r[j:j+len(route)]==route:
      ps=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']];ps[pi][ri]=r[:j]+newroute+r[j+len(route):];hits+=1;break
   assert hits==1,(name,hits)
 hashes={name:digest(g) for name,g in cand.items()};equal={name:h==expected[tol][name] for name,h in hashes.items()};results.append({'latvia':tol,'hashes':hashes,'matches_expected':equal});write('Latvia'+str(tol)+'_Poland250_East500.geojson',{'type':'FeatureCollection','features':[{'type':'Feature','properties':{'entity':name,'version':versions[name],'research_only':True},'geometry':g}for name,g in cand.items()]});print(json.dumps(results[-1]),flush=True)
write('reproduction-status.json',{'inputs':H,'results':results,'production_changed':False,'compiled_prepared_checked':False,'source_checks_not_repeated':'Original research topology not recertified by fingerprint alone. Expected exact geometry fingerprints bind to previously checked research outputs.','exception_audit':'pamir-exception-audit.json'})
