import copy,hashlib,json,math
from pathlib import Path
from shapely.geometry import shape,Polygon,LineString,Point,mapping
from shapely.ops import transform,unary_union
from shapely.validation import explain_validity
from pyproj import Transformer,Geod
P=Path(__file__).parent
x=json.loads((P/'inputs.json').read_text(encoding='utf-8'));d=x['donor']['geometry'];historical=x['irn']['entity']['geometryVersions'][1:4];ne=next(f for f in x['ne'] if f['id']=='IRN')['geometry'];geod=Geod(ellps='WGS84')
def save(n,o):
 (P/n).write_text(json.dumps(o,ensure_ascii=False,separators=(',',':')),encoding='utf-8');assert json.loads((P/n).read_text(encoding='utf-8'))==o

def h(o):return hashlib.sha256(json.dumps(o,separators=(',',':')).encode()).hexdigest()
def edge_set(g):return {tuple(sorted([tuple(a),tuple(b)])) for q in g['coordinates'] for r in q for a,b in zip(r,r[1:])}
names={77:'Lavan / Sheikh Shuaib',85:'Farsi',108:'Kharg',110:'Khargu',114:'Abu Musa',115:'Sirri',116:'Little Farur / Bani Farur',117:'Little Tunb',118:'Greater Tunb',119:'Farur',122:'Kish / Kais',126:'Hindurabi',155:'Hengam',156:'Qeshm / Kishm',174:'Larak',182:'Hormuz'}
held={85:'1928 India Office memorandum says ownership undetermined; no affirmative 1920s Iranian attribution established.',114:'1928 official record distinguishes contested Persian claim from Sharjah administration. Existing NE proxy inclusion is not proof of historical ownership.',117:'1928 official record distinguishes Persian claim from Trucial/Qawasim attribution; do not backdate modern Iranian administration.',118:'1928 official record distinguishes Persian claim from Trucial/Qawasim attribution; do not backdate modern Iranian administration.'}
sources={
 'B397':{'date':'1928-08-24','title':'India Office B397, Status of the Islands of Tamb, Little Tamb, Abu Musa, and Sirri','url':'https://www.qdl.qa/en/archive/81055/vdc_100029521333.0x000008','meaning':'Contemporary British governmental evidence: Sirri effectively occupied by Persia since 1887; Persian claims to Tamb and Abu Musa remained contested. Not a modern sovereignty adjudication.'},
 'B399-1':{'date':'1928','title':'India Office B399, Status of certain Groups of Islands in the Persian Gulf, folio 197r','url':'https://www.qdl.qa/en/archive/81055/vdc_100063253984.0x0000c6','meaning':'Lists Qeshm, Hengam, Hormuz, Larak, Lavan, Hindurabi, Kish and Farur as Persian. Begins discussion of Little Farur uncertainty.'},
 'B399-2':{'date':'1928','title':'India Office B399, folio 197v','url':'https://www.qdl.qa/en/archive/81055/vdc_100063253984.0x0000c7','meaning':'Concludes Little Farur should be considered Persian with a slight doubt about Qawasim claim. Farsi/Arabi/Harqus ownership described as undetermined.'},
 'Turkey':{'date':'2017-02-15 update','title':'Richard N. Schofield, Encyclopaedia Iranica, Boundaries v. With Turkey','url':'https://www.iranicaonline.org/articles/boundaries-v/','meaning':'1932 treaty changed the 1914 line, with another small 1937 rectification. Modern/NE proxy coordinates cannot be recertified as universally identical to 1922.'},
 'Shatt':{'date':'encyclopedia historical account','title':'Encyclopaedia Iranica, Boundaries i. With the Ottoman Empire','url':'https://www.iranicaonline.org/articles/boundaries-i/','meaning':'1913 river delimitation differed from later Shatt al-Arab thalweg arrangements. Modern and NE lines are proxies, not historical legal evidence.'}}
rows=[];f=[]
for i,c in enumerate(d['coordinates']):
 p=Polygon(c[0],c[1:]);area=abs(geod.geometry_area_perimeter(p)[0])/1e6
 nr=shape(ne); status='protected-mainland-splice-needed' if i==151 else 'political-hold' if i in held else 'reuse-whole-donor-component'
 reason=held.get(i,'Existing Persian mainland/littoral display-scope refinement; no component-size filter, no assertion of exact historical shore position.')
 if i in [77,119,122,126,155,156,174,182]:reason='1928 B399 explicitly places the named island in the Persian group. Complete donor polygon retained.'
 if i==115:reason='1928 B397 reports Persian effective occupation since 1887; underlying rival claim remains documented.'
 if i==116:reason='1928 B399 concludes Persian attribution with slight Qawasim claim uncertainty, not a reason to delete this approved donor component.'
 row={'donorIndex':i,'name':names.get(i,'Iranian littoral component '+str(i)),'status':status,'reason':reason,'bounds':list(p.bounds),'areaKm2ForDescriptionOnly':area,'ringCount':len(c),'coordinateCount':sum(len(r) for r in c),'coordinatesDigest':h(c),'overlapsOldNE':bool(p.intersection(nr).area>0),'distanceToOldNEInDegreesDescriptiveOnly':p.distance(nr)}
 rows.append(row);f.append({'type':'Feature','id':'IRN-donor-'+str(i),'properties':row,'geometry':{'type':'Polygon','coordinates':c}})
save('donor-component-accounting.json',{'schemaVersion':1,'sourceRevision':x['revision'],'total':189,'mainland':151,'wholeReusableCount':184,'politicalHolds':[85,114,117,118],'sizeCutoff':None,'rows':rows,'sources':sources})
save('complete-donor-accounted.geojson',{'type':'FeatureCollection','features':f})
# Source-bound southern coast candidate only. Exact old political endpoints are retained.
oldW=[48.531016,29.96133];oldE=[61.588227,25.202094];dr=d['coordinates'][151][0]
coast=list(reversed(dr[6281:-1]+dr[:3218]));assert coast[0]==dr[3217] and coast[-1]==dr[6281]
connectors=[LineString([oldW,coast[0]]),LineString([coast[-1],oldE])]
nonheld=[i for i in range(189) if i!=151 and i not in held];assert len(nonheld)==184
checks=[];features=[];protected=[];neEdges=edge_set(ne)
for v in historical:
 g=v['geometry'];r=g['coordinates'][0][0];a=r.index(oldW);b=r.index(oldE);assert a<b
 ring=r[:a+1]+coast+r[b:]; polys=[[ring,*copy.deepcopy(g['coordinates'][0][1:])]]+[copy.deepcopy(d['coordinates'][i]) for i in nonheld]+[copy.deepcopy(g['coordinates'][i]) for i in [5,6]]
 cg={'type':'MultiPolygon','coordinates':polys};s=shape(cg);old=shape(g)
 assert s.is_valid,explain_validity(s)
 assert polys[0][0][:a+1]==r[:a+1] and polys[0][0][-len(r[b:]):]==r[b:]
 assert all(polys[j+1]==d['coordinates'][idx] for j,idx in enumerate(nonheld));assert polys[-2:]==[g['coordinates'][5],g['coordinates'][6]]
 oldOutside=LineString(r[b:]+r[1:a+1]); outsideAfter=LineString(ring[a+len(coast)+1:]+ring[1:a+1]);assert oldOutside.equals_exact(outsideAfter,0)
 nonNE=edge_set(g)-neEdges;assert nonNE.issubset(edge_set(cg))
 changes=old.symmetric_difference(s); residual=edge_set(cg)&neEdges
 overlap=[]
 for peer in x['peers'][:7]:
  if not peer.get('entity'):continue
  ps=shape(peer['entity']['geometryVersions'][-1]['geometry']); before=old.intersection(ps).area;after=s.intersection(ps).area
  overlap.append({'id':peer['id'],'beforeSquareDegrees':before,'afterSquareDegrees':after,'deltaSquareDegrees':after-before})
 check={'versionId':v['versionId'],'validFrom':v['validFrom'],'validTo':v['validTo'],'status':'valid-preparatory-coast-candidate-not-adoption-ready','beforePolygons':len(g['coordinates']),'afterPolygons':len(polys),'valid':s.is_valid,'protectedNonNEEdges':len(nonNE),'protectedNonNEEdgesPreserved':True,'allNonGulfMainlandCoordinatesExact':True,'bothCaspianComponentsExact':True,'all184AcceptedDetachedDonorsExact':True,'oldGulfMainlandVerticesReplaced':b-a-1,'retainedNEEdgesAllRoles':len(residual),'changesBounds':list(changes.bounds),'modernNeighborOverlapDiagnostic':overlap,'geometryDigest':h(cg),'coordinatesDigest':h(cg['coordinates'])}
 checks.append(check);features.append({'type':'Feature','id':v['versionId'],'properties':{'validFrom':v['validFrom'],'validTo':v['validTo'],'status':check['status'],'politicalHolds':[85,114,117,118],'meaning':'Southern coast candidate only; NE political coordinates remain only because this isolated operation changes no land borders. Not the final full-border rebase.'},'geometry':cg})
 protected.append({'type':'Feature','id':v['versionId']+':protected-nonNE','properties':{'role':'All current non-NE source edges, protected; undirected edge ordering only'},'geometry':{'type':'MultiLineString','coordinates':[[list(a),list(b)] for a,b in sorted(nonNE)]}})
save('gulf-coast-historical-scope-candidates.geojson',{'type':'FeatureCollection','features':features})
save('protected-northern-edges.geojson',{'type':'FeatureCollection','features':protected})
save('candidate-checks.json',{'schemaVersion':1,'sourceRevision':x['revision'],'checks':checks,'wholeDonorGeometryValid':shape(d).is_valid,'all189DonorComponentsAccounted':len(rows)==189,'omittedForSize':[],'historicalPoliticalHolds':{str(k):v for k,v in held.items()},'connectors':[{'coordinates':list(map(list,c.coords)),'lengthMetres':geod.geometry_length(c),'role':'Explicit source-to-donor geometric splice; no legal endpoint relocation claimed'} for c in connectors],'visualReview':'not-yet-performed','compiledMigration':'not-performed','fullMainlandRebase':'not-performed','sourceWrites':False})
print(json.dumps({'versions':[(c['versionId'],c['afterPolygons'],c['protectedNonNEEdges']) for c in checks],'connectorsMetres':[geod.geometry_length(c) for c in connectors],'all189Accounted':True,'wholeReusable':184,'holds':list(held)},indent=2))

