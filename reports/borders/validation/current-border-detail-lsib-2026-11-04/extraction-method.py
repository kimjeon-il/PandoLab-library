import json,math,os,sys
from osgeo import ogr
from pyproj import Transformer
ogr.UseExceptions()
base='build-native/territorial-recipe/'
i=json.load(open(base+'border-detail-input.json',encoding='utf-8-sig'))
def geom(g): return ogr.CreateGeometryFromJson(json.dumps(g))
def lineparts(g):
 if g is None:return []
 if ogr.GT_Flatten(g.GetGeometryType())==ogr.wkbLineString:return [[[p[0],p[1]] for p in g.GetPoints()]] if g.Length()>0 else []
 return [a for n in range(g.GetGeometryCount()) for a in lineparts(g.GetGeometryRef(n))]
def chain(parts):
 parts=[p[:] for p in parts]
 merged=[]
 while parts:
  p=parts.pop(0);again=True
  while again:
   again=False
   for n,q in enumerate(parts):
    if p[-1]==q[0]:p+=q[1:]
    elif p[-1]==q[-1]:p+=list(reversed(q))[1:]
    elif p[0]==q[-1]:p=q[:-1]+p
    elif p[0]==q[0]:p=list(reversed(q))[:-1]+p
    else:continue
    parts.pop(n);again=True;break
  merged.append(p)
 return merged
samples=[]
plans=[('lsib-paektu','CHN','PRK',[127.98,41.93,128.15,42.08]),('lsib-river','CHN','PRK',[125.5,40.7,126.0,41.1]),('straight','USA','CAN',[-115,48.8,-112,49.2]),('mountain','AUT','LIE',[9.48,47.06,9.68,47.27]),('river','DEU','POL',[14.1,52.70,14.5,53.0]),('lake','USA','CAN',[-89.5,47.8,-88.3,48.5])]
for name,a,b,box in plans:
 x0,y0,x1,y1=box;clip=geom({'type':'Polygon','coordinates':[[[x0,y0],[x1,y0],[x1,y1],[x0,y1],[x0,y0]]]})
 public=[];work=[]
 for group,out in [('source',public),('work',work)]:
  gs=[]
  for k in [a,b]:
   v=i[group][k]['geometryVersions'][-1];c=i.get('publicCompiled' if group=='source' else 'compiled',{}).get(k)
   binding=next((b for b in c.get('sourceBindings',[]) if b.get('sourceVersionId')==v['versionId']),None) if c else None
   g=next((g for g in c['geometries'] if g['id']==binding['geometryRef']['id'] and g['version']==binding['geometryRef']['version']),None) if binding else None
   gs.append(geom(g['geojson'] if g else v['geometry']))
  parts=chain(lineparts(gs[0].Boundary().Intersection(clip).Intersection(gs[1].Boundary().Intersection(clip))))
  out.extend(parts)
 refs=[f for f in i['lsib']['features'] if set([f['properties']['CC1_GENC3'],f['properties']['CC2_GENC3']])==set([a,b])]
 reference=chain([p for f in refs for p in lineparts(geom(f['geometry']).Intersection(clip))])
 crs=f'+proj=aeqd +lat_0={(y0+y1)/2} +lon_0={(x0+x1)/2} +datum=WGS84 +units=m +type=crs';t=Transformer.from_crs('EPSG:4326',crs,always_xy=True)
 project=lambda p:[list(t.transform(*q)) for q in p]
 longest=lambda ps:max(ps,key=lambda p:sum(math.dist(u,v) for u,v in zip(project(p),project(p)[1:])))
 if not public or not reference:
  samples.append({'id':name,'excluded':'No common shared line in selected window','publicParts':len(public),'lsibParts':len(reference)});continue
 p,r,w=longest(public),longest(reference),longest(work)
 if math.dist(project(p)[0],project(r)[-1])<math.dist(project(p)[0],project(r)[0]):r=r[::-1]
 legacy=lineparts(geom({'type':'LineString','coordinates':r}).SimplifyPreserveTopology(.0004))[0]
 samples.append({'legacyDerivative':project(legacy),'legacyParameterDegrees':.0004,'id':name,'type':name,'countries':[a,b],'box':box,'metricCrs':crs,'public':project(p),'work':project(w),'reference':project(r),'geographic':{'public':p,'work':w,'reference':r},'componentCounts':{'public':len(public),'work':len(work),'reference':len(reference)},'lsibIds':[f['properties']['ID'] for f in refs],'sourceVersions':[i['source'][k]['geometryVersions'][-1]['versionId'] for k in [a,b]],'runtimeBasis':'actual selected compiled geometry where registered; source fallback explicitly marked only for unregistered candidates','applicationStatus':'applied current runtime','sourceSupplement':[i['source'][k]['geometryVersions'][-1].get('modernBoundarySupplement',{}).get('sourceId') for k in [a,b]]})
# Historical samples are detail comparators, not positional comparisons against a modern political boundary.
h=i['work']['deutsche-demokratische-republik'];v=h['geometryVersions'][-1]
for name,box,typ in [('gdr-berlin',[13.1,52.39,13.28,52.57],'built urban historical boundary'),('gdr-elbe',[10.6,53.1,11.05,53.4],'historical river boundary')]:
 x0,y0,x1,y1=box;clip=geom({'type':'Polygon','coordinates':[[[x0,y0],[x1,y0],[x1,y1],[x0,y1],[x0,y0]]]});parts=chain(lineparts(geom(v['geometry']).Boundary().Intersection(clip)));crs=f'+proj=aeqd +lat_0={(y0+y1)/2} +lon_0={(x0+x1)/2} +datum=WGS84 +units=m +type=crs';t=Transformer.from_crs(4326,crs,always_xy=True)
 projected=[[[*t.transform(*q)] for q in p] for p in parts]
 if not projected:samples.append({'id':name,'excluded':'No selected historical boundary'});continue
 n=max(range(len(parts)),key=lambda n:sum(math.dist(a,b) for a,b in zip(projected[n],projected[n][1:])));samples.append({'id':name,'type':typ,'box':box,'metricCrs':crs,'historical':projected[n],'geographic':{'historical':parts[n]},'componentCounts':{'historical':len(parts)},'version':v['versionId'],'applicationStatus':'source candidate, absent from active compiled catalog','positionalComparisonExcluded':'Modern LSIB has no corresponding internal German historical boundary.'})
# An actually applied 1922 historical international/shared counterpart.
name='ussr-atrek';box=[54.3,37.3,55.2,38.3];x0,y0,x1,y1=box
clip=geom({'type':'Polygon','coordinates':[[[x0,y0],[x1,y0],[x1,y1],[x0,y1],[x0,y0]]]});gs=[];versions=[]
for k in ['soviet-union','IRN']:
 c=i['compiled'][k];binding=next(b for b in c['sourceBindings'] if b['sourceVersionId'].endswith('1922-12-30-reviewed-v2') or b['sourceVersionId'].endswith('caspian-1922-12-30'));versions.append(binding['sourceVersionId']);g=next(g for g in c['geometries'] if g['id']==binding['geometryRef']['id'] and g['version']==binding['geometryRef']['version']);gs.append(geom(g['geojson']))
parts=chain(lineparts(gs[0].Boundary().Intersection(clip).Intersection(gs[1].Boundary().Intersection(clip))));crs=f'+proj=aeqd +lat_0={(y0+y1)/2} +lon_0={(x0+x1)/2} +datum=WGS84 +units=m +type=crs';t=Transformer.from_crs(4326,crs,always_xy=True);projected=[[[*t.transform(*q)] for q in p] for p in parts]
if projected:
 n=max(range(len(parts)),key=lambda n:sum(math.dist(a,b) for a,b in zip(projected[n],projected[n][1:])));samples.append({'id':name,'type':'applied historical river boundary','box':box,'metricCrs':crs,'historical':projected[n],'geographic':{'historical':parts[n]},'componentCounts':{'historical':len(parts)},'versions':versions,'applicationStatus':'applied compiled USSR/IRN shared border, 1922-12-30 through 1925-05-12','positionalComparisonExcluded':'Modern political route is not a period reference; compare detail only, not historical accuracy.'})
else:samples.append({'id':name,'excluded':'No shared historical line in selected window'})
# Applied 1948 38th-parallel straight border; not a modern ownership comparison.
box=[126.5,37.98,127.5,38.02];x0,y0,x1,y1=box;clip=geom({'type':'Polygon','coordinates':[[[x0,y0],[x1,y0],[x1,y1],[x0,y1],[x0,y0]]]});c=i['compiled']['PRK'];binding=next(b for b in c['sourceBindings'] if b['sourceVersionId']=='state:PRK:38th-parallel-1948');g=next(g for g in c['geometries'] if g['id']==binding['geometryRef']['id'] and g['version']==binding['geometryRef']['version']);parts=chain(lineparts(geom(g['geojson']).Boundary().Intersection(clip)));crs='+proj=aeqd +lat_0=38 +lon_0=127 +datum=WGS84 +units=m +type=crs';t=Transformer.from_crs(4326,crs,always_xy=True);projected=[[[*t.transform(*q)] for q in p] for p in parts]
if projected:
 n=max(range(len(parts)),key=lambda n:sum(math.dist(a,b) for a,b in zip(projected[n],projected[n][1:])));samples.append({'id':'prk-1948-straight','type':'applied historical straight border','box':box,'metricCrs':crs,'historical':projected[n],'geographic':{'historical':parts[n]},'componentCounts':{'historical':len(parts)},'version':binding['sourceVersionId'],'applicationStatus':'applied compiled historical geometry','positionalComparisonExcluded':'38th parallel is historical ownership, not a current LSIB boundary.'})
json.dump({'schema':'pando-border-detail-samples-v1','publicRevision':i['publicRevision'],'workRevision':i['workRevision'],'lsibProvenance':i['lsibProvenance'],'samples':samples},open(base+'border-detail-samples.json','w'),indent=2)
print(json.dumps([{'id':s['id'],'points':{k:len(s[k]) for k in ['public','work','reference','historical'] if k in s},'parts':s.get('componentCounts'),'excluded':s.get('excluded')}for s in samples]))



