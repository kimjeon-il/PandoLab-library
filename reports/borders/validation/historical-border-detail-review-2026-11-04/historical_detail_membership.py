import json,math,hashlib
from collections import defaultdict
from osgeo import ogr,osr
ogr.UseExceptions()
EPS=1e-10;STEP=.1;base='build-native/territorial-recipe/'
load=lambda p:json.load(open(p,encoding='utf-8-sig'))
def rings(g):
 if g['type']=='LineString':return [g['coordinates']]
 if g['type']=='MultiLineString':return g['coordinates']
 return [r for p in ([g['coordinates']] if g['type']=='Polygon' else g['coordinates']) for r in p]
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
  if ll<=EPS*EPS:
   ids=set(i for k in bins(a,b) for i in self.grid[k])
   def point_distance(p,c,d):
    ux=d[0]-c[0];uy=d[1]-c[1];length=ux*ux+uy*uy;t=max(0,min(1,((p[0]-c[0])*ux+(p[1]-c[1])*uy)/length)) if length else 0
    return math.hypot(p[0]-c[0]-t*ux,p[1]-c[1]-t*uy)
   return any(max(point_distance(a,*self.edges[i]),point_distance(b,*self.edges[i]))<=EPS for i in ids)
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
