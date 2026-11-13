import json,math,hashlib
from collections import defaultdict
from osgeo import ogr,osr
ogr.UseExceptions()
EPS=1e-10;STEP=.1;base='build-native/territorial-recipe/'
load=lambda p:json.load(open(p,encoding='utf-8-sig'))
def rings(g):return [r for p in ([g['coordinates']] if g['type']=='Polygon' else g['coordinates']) for r in p]
def edges(g):return [(a,b) for r in rings(g) for a,b in zip(r,r[1:])]
def bins(a,b):
 for x in range(math.floor((min(a[0],b[0])-EPS)/STEP),math.floor((max(a[0],b[0])+EPS)/STEP)+1):
  for y in range(math.floor((min(a[1],b[1])-EPS)/STEP),math.floor((max(a[1],b[1])+EPS)/STEP)+1):yield x,y
class Cover:
 def __init__(self,g):
  self.edges=edges(g);self.grid=defaultdict(list)
  for i,(a,b) in enumerate(self.edges):
   for k in bins(a,b):self.grid[k].append(i)
 def includes(self,a,b):
  dx=b[0]-a[0];dy=b[1]-a[1];ll=dx*dx+dy*dy
  if ll==0:return False
  length=math.sqrt(ll);slop=EPS/length;intervals=[];ids=set(i for k in bins(a,b) for i in self.grid[k])
  for i in ids:
   c,d=self.edges[i]
   if abs(dx*(c[1]-a[1])-dy*(c[0]-a[0]))>EPS*length or abs(dx*(d[1]-a[1])-dy*(d[0]-a[0]))>EPS*length:continue
   t=[((p[0]-a[0])*dx+(p[1]-a[1])*dy)/ll for p in [c,d]];lo=max(0,min(t));hi=min(1,max(t))
   if hi>=lo-slop:intervals.append((lo,hi))
  end=0
  for lo,hi in sorted(intervals):
   if lo>end+slop:return False
   end=max(end,hi)
   if end>=1-slop:return True
  return False

def chains(g,labels,select):
 result=[];offset=0
 for pi,p in enumerate([g['coordinates']] if g['type']=='Polygon' else g['coordinates']):
  for ri,r in enumerate(p):
   n=len(r)-1;ls=labels[offset:offset+n];offset+=n
   if not n:continue
   cut=next((i for i in range(n) if ls[i]!=ls[(i-1)%n]),0);current=[];role=None
   for k in range(n):
    i=(cut+k)%n
    if ls[i]!=role:
     if len(current)>1 and select(role):result.append({'polygon':pi,'ring':ri,'role':role,'coordinates':current})
     current=[r[i]];role=ls[i]
    current.append(r[(i+1)%n])
   if len(current)>1 and select(role):result.append({'polygon':pi,'ring':ri,'role':role,'coordinates':current})
 return result
ne=load('assets/data/countries-ne-5.1.1.geojson');ng={f['id']:f['geometry'] for f in ne['features']}
modern={k:Cover(ng[k]) for k in ['POL','RUS','LTU']};prussia=load(base+'historical-detail-prussia-all-runtime.json');out=[];inputs=[]
for entity,country in prussia.items():
 source=load('assets/data/territorial-entities/source/countries/'+entity.replace(':','-')+'.json');native=source['geometryVersions'][0];peer=next(v for k,v in prussia.items() if k!=entity)
 for record in country['geometries']:
  g=record['geojson'];coverage=[b for b in country['sourceBindings'] if b['geometryRef']['id']==record['id']];peerRecords=[r['geojson'] for r in peer['geometries']];peerCover=[Cover(p) for p in peerRecords];nativeCover=Cover(native['geometry']);labels=[];counts=defaultdict(int)
  for a,b in edges(g):
   matches=[k for k,v in modern.items() if v.includes(a,b)]
   role='modern-reference' if matches else 'native-residual' if nativeCover.includes(a,b) else 'derived-residual'
   labels.append(role);counts[role]+=1
  residual=chains(g,labels,lambda r:r!='modern-reference')
  for j,ch in enumerate(residual):ch.update({'id':entity+'-'+str(len(out))+'-'+str(j),'nativeSharedWithPeer':all(any(v.includes(a,b) for v in peerCover) for a,b in zip(ch['coordinates'],ch['coordinates'][1:]))})
  out.append({'entityId':entity,'geometryRef':{'id':record['id'],'version':record['version']},'sourceVersionId':native['versionId'],'coverage':coverage,'edgeCounts':dict(counts),'residualChains':residual})
  print(entity+' runtime '+str(len(out))+' '+json.dumps(dict(counts)),flush=True)
# Iran: modern, historical Caspian water, reviewed USSR priority classification.
water=load('assets/data/territorial-entities/source/countries/waterbody-caspian.json');historicalWater=next(v for v in water['geometryVersions'] if v['versionId']=='caspian-near1922-approved')['geometry'];iran=load('assets/data/territorial-entities/source/countries/state-IRN.json');iranModern=next(v for v in iran['geometryVersions'] if v['versionId']=='state:IRN:natural-earth-5.1.1')['geometry'];soviet=load('assets/data/territorial-entities/source/countries/state-soviet-union.json');soviet1922=next(v for v in soviet['geometryVersions'] if v['versionId'].endswith('1922-12-30-reviewed-v2'))['geometry'];refs={'modern':Cover(iranModern),'historical-water':Cover(historicalWater),'reviewed-USSR':Cover(soviet1922)};iranOut=[]
for v in iran['geometryVersions']:
 if ':caspian-19' not in v['versionId']:continue
 labels=[];counts=defaultdict(int)
 for a,b in edges(v['geometry']):
  role=next((k for k,ref in refs.items() if ref.includes(a,b)),'unexplained');labels.append(role);counts[role]+=1
 ira={'versionId':v['versionId'],'edgeCounts':dict(counts),'changedChains':chains(v['geometry'],labels,lambda r:r!='modern')};iranOut.append(ira);print(v['versionId']+' '+json.dumps(dict(counts)),flush=True)
json.dump({'epsilonDegrees':EPS,'epsilonMeaning':'Collinear membership numerical slack only; never a simplification tolerance. Unmodified original coordinates retained in every chain.','prussia':out,'iran':iranOut},open(base+'historical-detail-prussia-iran-chains.json','w'),ensure_ascii=False,indent=2)
