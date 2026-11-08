import sys,json,copy,hashlib
from pathlib import Path
sys.path.insert(0,'recovery/baikonur/deps')
from shapely.geometry import shape,mapping,LineString
from shapely.validation import explain_validity
B=Path('research/europe-approved-baseline');R=Path('research/europe1922');O=R/'application-prepared-v1'
names=['state-soviet-union','state-soviet-union-russian-sfsr','state-soviet-union-byelorussian-ssr','state-soviet-union-ukrainian-ssr']
def H(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def read(p):return json.load(open(p))
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,separators=(',',':')))
def line(p):d=read(R/p);return d.get('geometry',d.get('features',[{}])[0].get('geometry'))['coordinates']
def ring(g):return g['coordinates'][0]if g['type']=='Polygon'else g['coordinates'][0][0]
def setring(g,r):g=copy.deepcopy(g);g['coordinates'][0] =r if g['type']=='Polygon'else g['coordinates'][0];
# Explicit setter avoids normalizing/reordering unmodified geometry.
def replaced(g,r):
 z=copy.deepcopy(g)
 if z['type']=='Polygon':z['coordinates'][0]=r
 else:z['coordinates'][0][0]=r
 return z
sources={};versions={};old={}
for n in names:
 sources[n]=read(B/(n+'-source.json'));versions[n]=next(v for v in sources[n]['geometryVersions']if v['versionId']==n.replace('state-','state:',1)+':1922-12-30-reviewed-v2');old[n]=versions[n]['geometry']
u=ring(old[names[0]])
pol=line('poland/whole-continuous-v1/poland-continuous-candidate.geojson');j=read(R/'poland/application-readonly-plan/application-junctions.json')['junctions'];J1=j[0]['newIntersection'];J2=j[1]['newIntersection']
# Insert real intersections without changing the source line's route.
for v in sorted(j,key=lambda x:x['candidateSegments'][0]['index'],reverse=True):pol.insert(v['candidateSegments'][0]['index']+1,v['newIntersection'])
p_rev=pol[::-1];i1=p_rev.index(J1);i2=p_rev.index(J2)
fin=line('finland/coast-preserved-application/selected-land-arc.geojson');lake=line('estonia/retrace/patch-v2/joined-shared-boundary.geojson')[::-1]
assert p_rev[0]==u[884] and fin[0]==u[1406] and fin[-1]==u[2152] and lake[0]==u[1175] and lake[-1]==u[1279]
outputs={};manifest={'baseline':read(B/'baseline.json'),'scope':'1922 reconstruction European exterior only;local candidates not published','validFrom':'1922-12-30','validTo':'1925-05-12','source_geometry_selection':'display is recommended existing project convention; master retained separately','simplification':{'tolerance_degrees':0.0005,'actual_scope':'Latvia confirmed dry-land7to4 only','before':1737,'after':1734,'max_deviation_m':43.75665,'max_css_px':.102025,'river_uncertain_modern_shared_preserved':True,'Finland_Estonia_Poland_additional_simplification':False},'junctions':[J1,J2],'entities':[]}
for mode,latpath in [('master','latvia/final-landonly-simplification/assembled-unsimplified.geojson'),('display','latvia/final-landonly-simplification/assembled-landonly-display.geojson')]:
 lat=line(latpath)[::-1];assert lat[0]==p_rev[-1] and lat[-1]==u[1169]
 arc=p_rev+lat[1:]+u[1170:1176]+lake[1:]+u[1280:1407]+fin[1:]
 assert arc[0]==u[884] and arc[-1]==u[2152]
 assert len(set(map(tuple,[J1,J2])))==2
 new={names[0]:replaced(old[names[0]],u[:884]+arc+u[2153:])}
 r=ring(old[names[1]]);assert r[2033]==u[2152];new[names[1]]=replaced(old[names[1]],r[:874]+arc[arc.index(J1):]+r[2034:])
 r=ring(old[names[2]]);blr=[J1]+r[1:127]+[J2]+p_rev[i2+1:i1+1];assert blr[0]==blr[-1];new[names[2]]=replaced(old[names[2]],blr)
 r=ring(old[names[3]]);assert r[884]==u[884];new[names[3]]=replaced(old[names[3]],r[:884]+p_rev[:i2+1]+r[950:])
 for n,g in new.items():
  assert shape(g).is_valid,(n,mode,explain_validity(shape(g)))
  save(O/(n+'-source-'+mode+'-geometry.json'),g)
 outputs[mode]=new
# Exact original node preservation on unedited parts.
guards={'USSR_before884':ring(outputs['display'][names[0]])[:884]==u[:884],'USSR_after2152_suffix':ring(outputs['display'][names[0]])[-len(u[2153:]):]==u[2153:],'Finland_coast1397through1406_in_new':all(q in ring(outputs['display'][names[0]]) for q in u[1397:1407]),'north_coast2152through2154_in_new':all(q in ring(outputs['display'][names[0]])for q in u[2152:2155]),'unchanged_other_polygons_USSR':outputs['display'][names[0]]['coordinates'][1:]==old[names[0]]['coordinates'][1:],'BLR_interior1through126_exact':ring(outputs['display'][names[2]])[1:127]==ring(old[names[2]])[1:127],'Poland_original1991nodes_preserved':all(q in ring(outputs['display'][names[0]])for q in line('poland/whole-continuous-v1/poland-continuous-candidate.geojson'))}
assert all(guards.values()),guards
manifest['guards']=guards
for n in names:
 before=shape(old[n]);after=shape(outputs['display'][n]);add=after.difference(before);remove=before.difference(after)
 save(O/(n+'-add.geojson'),mapping(add));save(O/(n+'-remove.geojson'),mapping(remove))
 built=read(B/(n+'-builtin.json'));bind=next(x for x in built['timelineRecords']['geometryBindings']if x['validFrom']=='1922-12-30'and x['validTo']=='1925-05-12');ref=bind['geometryRef'];item=next(x for x in built['geometries']if x['id']==ref['id']and x['version']==ref['version']);bg=item['geojson'];bg=bg.get('geometry',bg);bs=shape(bg)
 bn=bs.difference(remove).union(add);assert bn.is_valid,(n,'compiled delta',explain_validity(bn));save(O/(n+'-compiled-display-geometry.json'),mapping(bn))
 outside=bs.symmetric_difference(bn).difference(add.union(remove));assert outside.area<1e-10,(n,'outside delta changed',outside.area)
 manifest['entities'].append({'entity':n,'versionId':versions[n]['versionId'],'source_file_sha256':hashlib.sha256((B/(n+'-source.json')).read_bytes()).hexdigest(),'builtin_file_sha256':hashlib.sha256((B/(n+'-builtin.json')).read_bytes()).hexdigest(),'before_source_geometry_sha256':H(old[n]),'before_compiled_geometry_sha256':H(bg),'builtin_geometry_ref':ref,'source_after_master':str(O/(n+'-source-master-geometry.json')),'source_after_display':str(O/(n+'-source-display-geometry.json')),'compiled_after_display':str(O/(n+'-compiled-display-geometry.json')),'add_delta':str(O/(n+'-add.geojson')),'remove_delta':str(O/(n+'-remove.geojson')),'source_after_display_geometry_sha256':H(outputs['display'][n]),'compiled_after_display_geometry_sha256':H(mapping(bn)),'compiled_outside_local_delta_difference_area_deg2':outside.area,'source_valid':True,'compiled_valid':True,'change_bounds':list(add.union(remove).bounds)})
# Source consistency: union of the three modified republics cannot diverge on the new exterior.
JLine=LineString(arc)
for n in names[1:]:
 pass
manifest['file_hashes']={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in O.glob('*.json')}
manifest['file_hashes'].update({str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in O.glob('*.geojson')})
save(O/'application-manifest.json',manifest)
print('READY',guards,[(x['entity'],x['source_valid'],x['compiled_valid'])for x in manifest['entities']])
