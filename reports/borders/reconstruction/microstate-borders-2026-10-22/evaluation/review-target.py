import copy
import gzip
import importlib.util
import io
import json
from pathlib import Path
import zipfile

import shapefile
import shapely
from shapely.geometry import LineString, Point, shape, mapping
from shapely.ops import substring, transform
from pyproj import Transformer

root = Path.cwd()
work = root / 'build-native/lsib-supplement'
spec = importlib.util.spec_from_file_location('delta', root / 'tools/verify-lsib-screen-delta.py')
delta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(delta)
candidate = json.loads((work / 'aut-lie-candidate.json').read_text())
before, after = {}, {}
preserved = []
for change in candidate['changes']:
    name = change['entityId'].replace(':', '-') + '.json'
    a = json.loads((root / 'assets/data/territorial-entities/source/countries' / name).read_text(encoding='utf-8'))
    b = json.loads((work / 'staged-source/countries' / name).read_text(encoding='utf-8'))
    av = next(v for v in a['geometryVersions'] if v['versionId'] == change['geometryVersionId'])
    bv = next(v for v in b['geometryVersions'] if v['versionId'] == change['geometryVersionId'])
    code = a['sourceInfo']['featureId']
    before[code], after[code] = shape(av['geometry']), shape(bv['geometry'])
    expected = copy.deepcopy(a)
    ev = next(v for v in expected['geometryVersions'] if v['versionId'] == change['geometryVersionId'])
    ev['geometry'], ev['sourceId'], ev['modernBoundarySupplement'] = bv['geometry'], bv['sourceId'], bv['modernBoundarySupplement']
    expected['sourceInfo'] = {**expected['sourceInfo'], **{k: b['sourceInfo'][k] for k in ('sourceId', 'title', 'geometrySha256')}}
    assert expected == b, f'Unexpected model metadata change: {code}'
    assert after[code].is_valid, (code, shapely.is_valid_reason(after[code]))
    old_parts = list(before[code].geoms) if before[code].geom_type == 'MultiPolygon' else [before[code]]
    new_parts = list(after[code].geoms) if after[code].geom_type == 'MultiPolygon' else [after[code]]
    assert len(old_parts) == len(new_parts)
    assert sum(len(p.interiors) for p in old_parts) == sum(len(p.interiors) for p in new_parts)
    preserved.append(code)
overlaps = {a + '/' + b: after[a].intersection(after[b]).area for a, b in [('AUT', 'LIE'), ('AUT', 'CHE'), ('CHE', 'LIE')]}
assert max(overlaps.values()) <= 1e-10, overlaps
union_delta = shapely.union_all(list(before.values())).symmetric_difference(shapely.union_all(list(after.values()))).area
assert union_delta <= 1e-9, union_delta

z = zipfile.ZipFile(work / 'swissboundaries3d_2025-01_2056_5728.shp.zip')
stem = next(n[:-4] for n in z.namelist() if n.endswith('TLM_LANDESGEBIET.shp'))
reader = shapefile.Reader(shp=io.BytesIO(z.read(stem + '.shp')), dbf=io.BytesIO(z.read(stem + '.dbf')))
official = {r.record.as_dict()['ICC']: shape(r.shape.__geo_interface__) for r in reader.shapeRecords()}
project = Transformer.from_crs(2056, 4326, always_xy=True)
official_lines = {
    ('AUT', 'LIE'): transform(project.transform, shapely.line_merge(official['LI'].boundary.difference(official['CH'].boundary))),
    ('CHE', 'LIE'): transform(project.transform, shapely.line_merge(official['LI'].boundary.intersection(official['CH'].boundary))),
    ('AUT', 'CHE'): transform(project.transform, official['CH'].boundary),
}
with gzip.open(root / 'tools/historical-library/sources/lsib-11.4/boundaries.geojson.gz', 'rt') as f:
    records = json.load(f)['features']
by_id = {f['properties']['ID']: shape(f['geometry']) for f in records}

def official_section(line, anchors, witness):
    if not line.is_ring and line.geom_type == 'LineString':
        return substring(line, line.project(Point(anchors[0])), line.project(Point(anchors[1])))
    choices = []
    for part in list(line.geoms) if line.geom_type == 'MultiLineString' else [line]:
        a, b = sorted(part.project(Point(p)) for p in anchors)
        if b - a < 1e-12:
            continue
        choices.append(substring(part, a, b))
        if part.is_ring:
            tail, head = substring(part, b, part.length), substring(part, 0, a)
            coords = list(tail.coords) + list(head.coords)[1:]
            if len(coords) > 1:
                choices.append(LineString(coords))
    points = [witness.interpolate(v, normalized=True) for v in (.2, .4, .6, .8)]
    return min(choices, key=lambda c: sum(c.distance(p) for p in points))

results = []
for entry in candidate['boundaries']:
    pair = tuple(entry['countries'])
    source = shapely.line_merge(shapely.union_all([by_id[v] for v in entry['sourceLineIds']]))
    parts = list(source.geoms) if source.geom_type == 'MultiLineString' else [source]
    segment = entry['segments'][0]
    anchors = segment['anchors']
    witness = min(parts, key=lambda p: sum(p.distance(Point(a)) for a in anchors))
    witness = substring(witness, witness.project(Point(anchors[0])), witness.project(Point(anchors[1])))
    reference = official_lines[pair] if pair == ('AUT', 'LIE') else official_section(official_lines[pair], anchors, witness)
    staged = json.loads((work / 'staged-source/countries' / ('state-' + pair[0] + '.json')).read_text(encoding='utf-8'))
    geometry = staged['geometryVersions'][0]['geometry']
    display = delta.display_section(geometry, anchors, reference)
    assert after[pair[1]].boundary.covers(display), f'Counterpart shared line differs: {pair}'
    forward, n1 = delta.sampled_distance(reference, display)
    reverse, n2 = delta.sampled_distance(display, reference)
    upper = max(forward, reverse) + delta.STEP * delta.SCALE / 2
    assert upper <= .5, (pair, upper)
    results.append({'pair': list(pair), 'anchors': anchors, 'samples': n1+n2,
        'sampledMaximumCssPx': max(forward, reverse), 'continuousUpperBoundCssPx': upper})
report = {'widthCssPx': 2560, 'flatZoom': 64, 'source': 'swissBOUNDARIES3D 2025-01 independent official vectors',
    'sourceCrs': 'EPSG:2056', 'comparisonCrs': 'EPSG:4326, equirectangular display coordinates',
    'transform': project.description, 'publishedTransformAccuracyMetres': project.accuracy,
    'scope': 'entire AUT/LIE boundary and four adjacent tripoint branches, C++ normalized staged geometry',
    'historicalGroundTruthVerified': False, 'preservedIdsDatesAndOtherMetadata': preserved,
    'counterpartOverlapDegreesSquared': overlaps, 'threeCountryUnionDeltaDegreesSquared': union_delta,
    'sections': results, 'maximumContinuousUpperBoundCssPx': max(v['continuousUpperBoundCssPx'] for v in results)}
(work / 'staged-review.json').write_text(json.dumps(report, indent=2))
print(json.dumps(report))
