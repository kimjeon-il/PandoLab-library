import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
import shapely
from shapely.geometry import shape, LineString, Point
from shapely.ops import substring
from pyproj import Geod

root=Path.cwd();cache=root/'build-native/lsib-supplement';stage=cache/'monaco-review'
def load_module(name,file):
    spec=importlib.util.spec_from_file_location(name,file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
module=load_module('supplement',root/'tools/supplement-lsib-boundaries.py')
screen=load_module('screen',root/'tools/verify-lsib-screen-delta.py');screen.STEP=.0001
candidate=json.loads((cache/'monaco-candidate.json').read_text(encoding='utf-8'))
before,after,identities={},{},[]
for change in candidate['changes']:
    code=change['entityId'].split(':')[1];filename=f'state-{code}.json'
    old=json.loads((stage/'before/countries'/filename).read_text(encoding='utf-8'))
    new=json.loads((stage/'staged/countries'/filename).read_text(encoding='utf-8'))
    a,b=copy.deepcopy(old),copy.deepcopy(new);a.pop('sourceInfo');b.pop('sourceInfo')
    for entity in [a,b]:
        for version in entity['geometryVersions']:
            if version['versionId']==change['geometryVersionId']:
                for key in ['geometry','sourceId','modernBoundarySupplement']:version.pop(key,None)
    assert a==b,(code,'identity or historical metadata changed')
    old_v=next(v for v in old['geometryVersions'] if v['versionId']==change['geometryVersionId'])
    new_v=next(v for v in new['geometryVersions'] if v['versionId']==change['geometryVersionId'])
    before[code],after[code]=old_v['geometry'],new_v['geometry']
    assert new_v['sourceId']==change['sourceId']
    if code=='FRA':
        retained=[v for v in old_v['modernBoundarySupplement']['boundaries'] if v['countries']!=['FRA','MCO']]
        assert all(v in new_v['modernBoundarySupplement']['boundaries'] for v in retained)
    identities.append({'entityId':new['entityId'],'lifetime':new['lifetime'],'versionId':new_v['versionId'],
        'sourceId':new_v['sourceId'],'sha256':hashlib.sha256((stage/'staged/countries'/filename).read_bytes()).hexdigest()})
module.validate_coastal_repair(before,after,candidate['coastReviews']['FRA/MCO'])
shared=shapely.line_merge(shape(after['FRA']).boundary.intersection(shape(after['MCO']).boundary))
assert shared.geom_type=='LineString'
coasts,metadata=module.reviewed_coast_reference(root,'tools/historical-library/sources/monaco-reviewed-2026-10-22/coast-reference.json')
records=json.loads(gzip.decompress((root/'tools/historical-library/sources/lsib-11.4/boundaries.geojson.gz').read_bytes()))['features']
land=next(shape(f['geometry']) for f in records if f['properties']['ID']==candidate['boundaries'][0]['sourceLineIds'][0])
results=[]
for entry in candidate['boundaries']:
    section=entry['segments'][0];anchors=section['anchors'];code=entry['countries'][0]
    reference=land if entry.get('kind')!='coastline' else coasts[entry['referenceRole']]
    if entry.get('kind')=='coastline' and entry['referenceRole']!='monaco':
        reference=substring(reference,reference.project(Point(anchors[0])),reference.project(Point(anchors[1])))
    display=screen.display_section(after[code],anchors,reference)
    f,n1=screen.sampled_distance(reference,display);b,n2=screen.sampled_distance(display,reference)
    upper=max(f,b)+screen.STEP*screen.SCALE/2
    assert upper<=.5,(entry['countries'],upper)
    results.append({'countries':entry['countries'],'role':entry.get('referenceRole','land'),
        'sourceId':entry['sourceId'],'sampleMaximumCssPx':max(f,b),'continuousUpperBoundCssPx':upper,'samples':n1+n2})
geod=Geod(ellps='WGS84');old_union=shapely.union_all([shape(g) for g in before.values()]);new_union=shapely.union_all([shape(g) for g in after.values()])
area=lambda g:abs(geod.geometry_area_perimeter(g)[0])/1e6 if not g.is_empty else 0
review={'status':'focused-normalized-review','historicalGroundTruthVerified':False,
    'baseline':{'mapContentWidthCssPx':2560,'flatZoom':64},'identities':identities,'sourceDerivative':results,
    'overlapSquareDegrees':shape(after['FRA']).intersection(shape(after['MCO'])).area,
    'coastReview':candidate['coastReviews']['FRA/MCO'],
    'monacoAreaKm2Before':area(shape(before['MCO'])),'monacoAreaKm2After':area(shape(after['MCO'])),
    'landAddedKm2':area(new_union.difference(old_union)),'landRemovedKm2':area(old_union.difference(new_union))}
(cache/'monaco-normalized-review.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in review.items() if k not in ['coastReview','identities']},ensure_ascii=True))
