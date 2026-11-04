import json
from osgeo import ogr
ogr.UseExceptions()
d=json.load(open('build-native/territorial-recipe/korea-lsib-rollback-stage.json',encoding='utf-8-sig'))
def geometry(x):return ogr.CreateGeometryFromJson(json.dumps(x))
def selected(country,date,which):
 vs=d['sources'][country][which]['geometryVersions']
 return geometry(next(v['geometry'] for v in vs if (v['validFrom'] is None or v['validFrom']<=date) and (v['validTo'] is None or v['validTo']>=date)))
rows=[]
for r in d['rows']:
 assert r['inverseExact'];b=d['sources'][r['id']]['before'];a=d['sources'][r['id']]['after'];v=next(v for v in a['geometryVersions'] if v['versionId']==r['versionId']);g=geometry(v['geometry']);assert g.IsValid();rows.append({'id':r['id'],'versionId':r['versionId'],'valid':True,'inverseExact':True})
periods=[]
for date in ['1948-09-09','1953-07-26','1953-07-27','1964-03-19','1964-03-20','2026-11-04']:
 before=[selected(k,date,'before') for k in ['KOR','PRK','CHN']];after=[selected(k,date,'after') for k in ['KOR','PRK','CHN']]
 union=lambda a:a[0].Union(a[1]).Union(a[2])
 diff=union(before).SymDifference(union(after)).GetArea();overlap=[after[0].Intersection(after[1]).GetArea(),after[1].Intersection(after[2]).GetArea()];assert diff<1e-12,(date,diff);assert max(overlap)<1e-12,(date,overlap);periods.append({'date':date,'threeCountryUnionDifferenceSquareDegrees':diff,'KOR_PRKOverlapSquareDegrees':overlap[0],'PRK_CHNOverlapSquareDegrees':overlap[1]})
for kind in ['paektu','mdl']:
 line=geometry({'type':'LineString','coordinates':d[kind]['baseline']});points=['PRK','CHN'] if kind=='paektu' else ['KOR','PRK'];a,b=[selected(k,'2026-11-04','after') for k in points];missing=line.Difference(a.Boundary().Intersection(b.Boundary())).Length();assert missing<1e-12,(kind,missing)
result={'validity':rows,'periods':periods,'sharedBaselineChainsExact':True,'method':'Existing OGR/GEOS runtime; exact baseline chain containment, validity, paired overlap and three-country union. Technical square degrees, not event area or historical accuracy.'};json.dump(result,open('build-native/territorial-recipe/korea-lsib-rollback-qa.json','w'),indent=2);print(json.dumps(result))
