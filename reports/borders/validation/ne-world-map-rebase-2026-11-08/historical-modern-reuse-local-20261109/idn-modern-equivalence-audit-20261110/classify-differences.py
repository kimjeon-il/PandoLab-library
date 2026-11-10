import json
from pathlib import Path
from shapely.geometry import Polygon,shape
from shapely.ops import unary_union
from shapely.strtree import STRtree
from pyproj import Geod
r=Path(__file__).parent;root=r.parent;read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));x=read(r/'source-inputs.json');details=read(r/'detailed-components.json');summary=read(r/'summary.json');vs=x['rec']['entity']['geometryVersions'];dm=[Polygon(p[0],p[1:])for p in vs[-1]['geometry']['coordinates']];dt=[Polygon(p[0],p[1:])for p in x['neighbors'][0]['entity']['geometryVersions'][0]['geometry']['coordinates']];allmodern=dm+dt;mt=STRtree(allmodern);ne=[];neids=[]
for f in x['ne']['features']:
 if f['id']not in['IDN','TLS']:continue
 for i,p in enumerate(f['geometry']['coordinates']):ne.append(Polygon(p[0],p[1:]));neids.append([f['id'],i])
nt=STRtree(ne);gd=Geod(ellps='WGS84')
def km(g):
 if g.is_empty:return 0
 if g.geom_type=='Polygon':return abs(gd.geometry_area_perimeter(g)[0])/1e6
 return sum(km(p)for p in g.geoms)if hasattr(g,'geoms')else 0
hybrids={}
for name,scope in[('Borneo','idn-borneo-coast-20261110'),('West New Guinea','idn-west-new-guinea-coast-20261110')]:
 c=read(root/scope/'candidate.json');p=c['geometry']['coordinates'][c['polygonIndex']];hybrids[name]=Polygon(p[0],p[1:])
c=read(root/'idn-west-timor-coast-20261110/reviewed-candidate.json');p=c['geometry']['coordinates'][c['polygonIndex']];hybrids['West Timor']=Polygon(p[0],p[1:]);timor=shape(read(root/'idn-timor-coast-20261110/timor-modern-union-geometry.json'));allbase=unary_union(allmodern);papuaIndices=set(details['papuaClasses']['papua_only']);base0=shape(vs[-1]['geometry']).difference(unary_union([dm[i]for i in papuaIndices]));output=[]
for vi in[0,2]:
 v=vs[vi];actual=shape(v['geometry']);base=base0 if vi==0 else allbase;polys=[];legacy=[];counts={};extra={}
 for i,p in enumerate(v['geometry']['coordinates']):
  g=Polygon(p[0],p[1:]);modernMatches=[int(j)for j in mt.query(g)if g.equals(allmodern[int(j)])];nmatch=[int(j)for j in nt.query(g)if g.equals(ne[int(j)])];hmatch=[name for name,h in hybrids.items()if g.equals(h)]
  if modernMatches:cat='exact current donor polygon'
  elif g.equals(timor):cat='exact current Timor mainland union'
  elif hmatch:cat='hybrid mainland preserving old political line/junction'
  elif nmatch:cat='unchanged legacy NE polygon';legacy.append(g)
  else:cat='unclassified historical polygon'
  counts[cat]=counts.get(cat,0)+1;ex=km(g.difference(base));extra[cat]=extra.get(cat,0)+ex;polys.append({'historicalPolygonIndex':i,'category':cat,'modernMatches':[{'entityId':'IDN'if j<len(dm)else'TLS','index':j if j<len(dm)else j-len(dm)}for j in modernMatches],'NEPolygonMatches':[neids[j]for j in nmatch],'hybridNames':hmatch,'extraKm2':ex,'bounds':g.bounds})
 lu=unary_union(legacy);omitted={(q['entityId'],q['index'])for q in details['versions'][v['versionId']]['explicitOmissions']};components=[];missingCounts={};missingAreas={}
 for owner,gs in [('IDN',dm)]+([('TLS',dt)]if vi==2 else[]):
  for i,g in enumerate(gs):
   if vi==0 and i in papuaIndices:cat='intentional Papua exclusion supported by old source';area=0
   else:
    missing=g.difference(actual);area=km(missing)
    if missing.is_empty:cat='fully represented'
    elif(owner,i)in omitted:cat='explicit display-scale omission'
    elif owner=='IDN'and i in([1575,2562]if vi==0 else[1575,4026]):cat='retained old political line/junction discrepancy'
    elif g.intersection(lu).area>0:cat='remaining legacy NE island correspondence'
    elif owner=='IDN'and i in details['papuaClasses']['no_NE_overlap']:cat='modern component without old NE area correspondence'
    else:cat='other missing modern component'
   if area>0:missingCounts[cat]=missingCounts.get(cat,0)+1;missingAreas[cat]=missingAreas.get(cat,0)+area
   components.append({'entityId':owner,'index':i,'category':cat,'missingKm2':area,'bounds':g.bounds})
 output.append({'versionId':v['versionId'],'historicalPolygonCategories':counts,'extraAreaByHistoricalCategoryKm2':extra,'missingModernComponentCategories':missingCounts,'missingModernAreaByCategoryKm2':missingAreas,'historicalPolygons':polys,'modernComponents':components})
(r/'classified-differences.json').write_text(json.dumps(output,indent=2),encoding='utf8');print(json.dumps([{k:v for k,v in q.items()if k not in['historicalPolygons','modernComponents']}for q in output]))
