import json,copy,math
from pathlib import Path
from osgeo import ogr,osr
O=Path('.');t=json.loads((O/'topology.json').read_text());src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);dst=osr.SpatialReference();dst.ImportFromEPSG(3035);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);tx=osr.CoordinateTransformation(src,dst)
def simplified(a,tol):
 cuts=[i for i,p in enumerate(a)if p==[10.452726,46.530948]and 0<i<len(a)-1]
 if cuts:
  indices=[0]+cuts+[len(a)-1];v=[]
  for i,j in zip(indices,indices[1:]):
   q=simplified(a[i:j+1],tol);v+=q if not v else q[1:]
  return v
 g=ogr.Geometry(ogr.wkbLineString);lookup={}
 for p in a:
  x,y,_=tx.TransformPoint(*p);g.AddPoint_2D(x,y);lookup[(x,y)]=p
 if a[0]==a[-1] and g.Length()<100000: return a
 z=g.Simplify(tol);r=[lookup[tuple(z.GetPoint(i)[:2])]for i in range(z.GetPointCount())]
 # Closed rings retain every component and at least a triangle; never delete islands.
 return a if a[0]==a[-1]and len(r)<4 else r
protected=set()
for k,o in t['objects'].items():
 if k.startswith('reference-'):
  for r in o['arcs']:
   for i in r:protected.add(i if i>=0 else ~i)
def rebuild(arcs):
 def ring(r):
  v=[]
  for i in r:
   a=arcs[i]if i>=0 else arcs[~i][::-1];v+=a if not v else a[1:]
  assert v[0]==v[-1];return v
 return {k:{'type':v['type'],'coordinates':[[ring(r)for r in p]for p in v['arcs']]}for k,v in t['objects'].items()if not k.startswith('reference-')}
def count(g):return sum(len(r)for p in g['coordinates']for r in p)
for tol in [100,250]:
 arcs=[a if i in protected else simplified(a,tol)for i,a in enumerate(t['arcs'])];rows=rebuild(arcs);valid={k:bool(ogr.CreateGeometryFromJson(json.dumps(g)).IsValid())for k,g in rows.items()};print(tol,{k:count(g)for k,g in rows.items()},valid);assert all(valid.values());(O/('display-'+str(tol)+'.json')).write_text(json.dumps(rows),encoding='utf8')


