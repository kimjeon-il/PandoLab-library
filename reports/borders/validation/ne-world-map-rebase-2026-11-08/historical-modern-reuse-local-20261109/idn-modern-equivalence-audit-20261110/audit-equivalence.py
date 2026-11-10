import json,math
from pathlib import Path
from shapely.geometry import Polygon,shape,mapping
from shapely.ops import unary_union
from shapely.strtree import STRtree
from pyproj import Geod
r=Path(__file__).parent;root=r.parent;read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));x=read(r/'source-inputs.json');vs=x['rec']['entity']['geometryVersions'];modern=vs[-1];tls=x['neighbors'][0]['entity']['geometryVersions'][0];dm=[Polygon(p[0],p[1:])for p in modern['geometry']['coordinates']];dt=[Polygon(p[0],p[1:])for p in tls['geometry']['coordinates']];gd=Geod(ellps='WGS84')
def km(g):
 if g.is_empty:return 0
 if g.geom_type=='Polygon':return abs(gd.geometry_area_perimeter(g)[0])/1e6
 if hasattr(g,'geoms'):return sum(km(p)for p in g.geoms)
 return 0
legacy=read(root/'idn-independent-islands-20261110/source-inputs.json')['rec']['entity']['geometryVersions'][0]['geometry'];leg=[Polygon(p[0],p[1:])for p in legacy['coordinates']];lt=STRtree(leg);ne=next(f for f in x['ne']['features']if f['id']=='IDN');nes=[Polygon(p[0],p[1:])for p in ne['geometry']['coordinates']];excluded=[]
for i,g in enumerate(nes):
 if not any(g.equals(leg[int(j)])for j in lt.query(g)):excluded.append(i)
assert len(excluded)==25,len(excluded);ex=unary_union([nes[i]for i in excluded]);kept=unary_union(leg);classes={'papua_only':[],'retained_only':[],'mixed':[],'no_NE_overlap':[]}
for i,g in enumerate(dm):
 a=g.intersection(ex).area>0;b=g.intersection(kept).area>0;classes['mixed'if a and b else'papua_only'if a else'retained_only'if b else'no_NE_overlap'].append(i)
# Provisional comparison excludes only source-supported modern Papua components. Unmatched new pieces are NOT silently excluded.
papua=unary_union([dm[i]for i in classes['papua_only']]);current=shape(modern['geometry']);base1945=current.difference(papua);base1975=unary_union([current,shape(tls['geometry'])]);ledger={vs[0]['versionId']:[],vs[2]['versionId']:[]};receipts=[]
for folder in root.glob('idn-*'):
 if not(folder/'local-archive-commit.json').exists()or not(folder/'reviewed-candidate.json').exists():continue
 receipt=read(folder/'local-archive-commit.json');c=read(folder/'reviewed-candidate.json');vids=[q['versionId']for q in c['results']]if 'results'in c else[c['versionId']];items=[]
 if 'operation'in c:
  items=[{'entityId':'IDN','index':q['index']}for q in c['operation'].get('omittedDetached',[])]
 elif 'operations'in c:
  items=[{'entityId':'IDN','index':q['index']}for o in c['operations']for q in o.get('omittedComponents',[])]
 elif 'omittedDetached'in c:items=[{'entityId':q['entityId'],'index':q['index']}for q in c['omittedDetached']]
 if folder.name=='idn-west-timor-coast-20261110':items=[{'entityId':'IDN','index':q['index']}for q in read(folder/'topology-and-projection.json')['detachedComponentLossAudit']]
 for vid in vids:
  if vid in ledger:ledger[vid]+=[{**q,'scope':folder.name,'revision':receipt['revision']}for q in items]
 receipts.append({'scope':folder.name,'revision':receipt['revision'],'omissionsPerEditedVersion':len(items),'versions':vids})
rows=[];features=[];detail={}
for vi,baseline,label in[(0,base1945,'modern IDN minus definitely source-matched Papua components; unmatched modern islands remain unresolved'),(2,base1975,'exact union of complete approved current IDN and TLS')]:
 v=vs[vi];a=shape(v['geometry']);missing=baseline.difference(a);excess=a.difference(baseline);exact=[];tree=STRtree(dm)
 for i,p in enumerate(v['geometry']['coordinates']):
  g=Polygon(p[0],p[1:]);matches=[int(j)for j in tree.query(g)if g.equals(dm[int(j)])]
  if matches:exact.append({'historicalPolygonIndex':i,'donorIndices':matches})
 ld=[];seen=set()
 for q in ledger[v['versionId']]:
  key=(q['entityId'],q['index'])
  if key in seen:continue
  seen.add(key);g=(dm if key[0]=='IDN'else dt)[key[1]];absent=g.difference(a);ld.append({**q,'donorAreaKm2':km(g),'actuallyAbsentKm2':km(absent),'fullyAbsent':g.intersection(a).area==0,'bounds':g.bounds})
 row={'versionId':v['versionId'],'validFrom':v['validFrom'],'validTo':v['validTo'],'baseline':label,'exactModernEquivalent':a.equals(baseline),'historicalPolygonCount':len(v['geometry']['coordinates']),'exactCurrentIDNPolygonMatches':len(exact),'missingFromHistoricalKm2':km(missing),'extraInHistoricalKm2':km(excess),'symmetricDifferenceKm2':km(missing)+km(excess),'explicitOmissionUniqueComponents':len(ld),'explicitOmissionFullyAbsentComponents':sum(q['fullyAbsent']for q in ld),'explicitOmissionActuallyAbsentKm2':sum(q['actuallyAbsentKm2']for q in ld)};rows.append(row);detail[v['versionId']]={'exactMatches':exact,'explicitOmissions':ld}
 features +=[{'type':'Feature','properties':{'versionId':v['versionId'],'kind':'missing from historical','baseline':label},'geometry':mapping(missing)},{'type':'Feature','properties':{'versionId':v['versionId'],'kind':'extra in historical','baseline':label},'geometry':mapping(excess)}]
summary={'sourceRevision':x['sourceRevision'],'status':'read-only discrepancy audit; no changes applied','rows':rows,'papuaClassification':{k:len(v)for k,v in classes.items()},'excludedNEPapuaPolygonIndices':excluded,'modernPapuaMatchedAreaKm2':km(papua),'unmatchedModernComponentsAreaKm2':sum(km(dm[i])for i in classes['no_NE_overlap']),'omissionPolicyFinding':'Prior omissions were based on a display-scale pixel criterion, not a verified simplification error. No new omissions are authorized or performed during this audit.','knownDifferenceClasses':['Remaining unchanged old NE island/coast polygons','Protected old NE political boundary and junction connectors, even where their display differs from modern','Explicit prior display-scale omissions of approved modern components','1945 Papua exclusion and 1975 East Timor inclusion are period-specific ownership/display scope, not shape errors'],'limits':['1945 exact target still needs authoritative classification of modern components without any old NE overlap. The provisional baseline includes them rather than treating them as approved exclusions.','Numbers are ellipsoidal areas of planar-overlay differences, not evidence of historical territorial entitlement.'],'committedScopes':receipts};(r/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8');(r/'detailed-components.json').write_text(json.dumps({'papuaClasses':classes,'versions':detail},indent=2),encoding='utf8');(r/'differences.geojson').write_text(json.dumps({'type':'FeatureCollection','features':features}),encoding='utf8');print(json.dumps(summary))
