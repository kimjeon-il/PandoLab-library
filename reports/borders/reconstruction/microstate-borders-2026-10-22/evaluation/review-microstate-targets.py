"""One focused review of the normalized candidate, not a world-wide validator."""
import copy
import gzip
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import shapely
from shapely.geometry import LineString, Point, shape
from shapely.ops import substring
from pyproj import Geod

root = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('screen', root / 'tools/verify-lsib-screen-delta.py')
screen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)
generator_spec = importlib.util.spec_from_file_location('generator', root / 'tools/supplement-lsib-boundaries.py')
generator = importlib.util.module_from_spec(generator_spec)
generator_spec.loader.exec_module(generator)
candidate_name = sys.argv[1] if len(sys.argv) > 1 else 'microstate-candidate.json'
candidate = json.loads((root / 'build-native/lsib-supplement' / candidate_name).read_text())
source = root / 'assets/data/territorial-entities/source/countries'
staged = root / 'build-native/lsib-supplement/microstate-staged-source/countries'
before, after, areas = {}, {}, {}
geod = Geod(ellps='WGS84')
for change in candidate['changes']:
    code = change['entityId'].split(':')[1]
    raw = (source / f'state-{code}.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == change['inputFileSha256'], code
    old = json.loads(raw)
    new = json.loads((staged / f'state-{code}.json').read_text(encoding='utf-8'))
    version_id = change['geometryVersionId']
    old_version = next(v for v in old['geometryVersions'] if v['versionId'] == version_id)
    new_version = next(v for v in new['geometryVersions'] if v['versionId'] == version_id)
    before[code], after[code] = shape(old_version['geometry']), shape(new_version['geometry'])
    assert after[code].is_valid, (code, shapely.is_valid_reason(after[code]))
    expected_attributions = {a['sourceId']: a for a in old['sourceInfo'].get('sourceAttributions', [])}
    expected_attributions.update({a['sourceId']: a for a in change.get('sourceAttributions', [])})
    actual_attributions = {a['sourceId']: a for a in new['sourceInfo'].get('sourceAttributions', [])}
    assert expected_attributions == actual_attributions, f'Source attribution mismatch: {code}'
    for value in (old, new):
        version = next(v for v in value['geometryVersions'] if v['versionId'] == version_id)
        for field in ('geometry', 'sourceId', 'modernBoundarySupplement'):
            version.pop(field, None)
        for field in ('sourceId', 'title', 'geometrySha256', 'sourceAttributions'):
            value['sourceInfo'].pop(field, None)
    assert old == new, f'Metadata or historical version changed: {code}'
    areas[code] = {'beforeKm2': abs(geod.geometry_area_perimeter(before[code])[0]) / 1e6,
                   'afterKm2': abs(geod.geometry_area_perimeter(after[code])[0]) / 1e6}

groups = []
for codes in [('AND', 'FRA', 'ESP'), ('ITA', 'SMR', 'VAT'), ('LSO', 'ZAF')]:
    codes = tuple(code for code in codes if code in before)
    if len(codes) < 2:
        continue
    diff = shapely.union_all([before[c] for c in codes]).symmetric_difference(
        shapely.union_all([after[c] for c in codes])).area
    overlap = max(after[a].intersection(after[b]).area for i, a in enumerate(codes) for b in codes[i + 1:])
    assert diff <= 1e-9 and overlap <= 1e-10, (codes, diff, overlap)
    for code in codes:
        parts = lambda g: list(g.geoms) if g.geom_type == 'MultiPolygon' else [g]
        assert len(parts(before[code])) == len(parts(after[code])), code
        assert sum(len(p.interiors) for p in parts(before[code])) == sum(len(p.interiors) for p in parts(after[code])), code
    groups.append({'countries': codes, 'unionDifferenceSquareDegrees': diff, 'overlapSquareDegrees': overlap})

master = json.loads(gzip.decompress((root / 'tools/historical-library/sources/lsib-11.4/boundaries.geojson.gz').read_bytes()))
by_id = {f['properties']['ID']: shape(f['geometry']) for f in master['features']}
results = []
for entry in candidate['boundaries']:
    if 'referenceManifest' in entry:
        source_line, _ = generator.reviewed_reference(root, entry['referenceManifest'])
    else:
        source_line = shapely.line_merge(shapely.union_all([by_id[line_id] for line_id in entry['sourceLineIds']]))
    parts = list(source_line.geoms) if source_line.geom_type == 'MultiLineString' else [source_line]
    for segment in entry['segments']:
        closed = segment.get('closedRing', False)
        code = segment['enclave'] if closed else entry['countries'][0]
        anchors = segment.get('anchors', [])
        if closed:
            assert len(parts) == 1 and parts[0].is_ring
            reference = parts[0]
        else:
            reference = min(parts, key=lambda line: sum(line.distance(Point(p)) for p in anchors))
            reference = substring(reference, reference.project(Point(anchors[0])), reference.project(Point(anchors[1])))
        final_entity = json.loads((staged / f'state-{code}.json').read_text(encoding='utf-8'))
        geometry = next(v['geometry'] for v in final_entity['geometryVersions'] if v['datePrecision'] == 'current')
        display = screen.display_section(geometry, anchors, reference)
        counterpart = after[entry['countries'][0]].boundary.intersection(after[entry['countries'][1]].boundary)
        assert counterpart.covers(display), entry['countries']
        forward, n1 = screen.sampled_distance(reference, display)
        reverse, n2 = screen.sampled_distance(display, reference)
        upper = max(forward, reverse) + screen.STEP * screen.SCALE / 2
        assert upper <= .5, (entry['countries'], upper)
        results.append({'countries': entry['countries'], 'closedRing': closed, 'samples': n1 + n2,
            'sampledMaximumCssPx': max(forward, reverse), 'continuousUpperBoundCssPx': upper})

comparison = None
if 'SMR' in after:
    screen.STEP = .0001
    official = shape(json.loads((root / 'tools/historical-library/sources/reviewed-boundaries-2026-10-22/smr-state-boundary.geojson').read_text())['features'][0]['geometry'])
    display = LineString(after['SMR'].exterior.coords)
    f, n1 = screen.sampled_distance(official, display)
    r, n2 = screen.sampled_distance(display, official)
    comparison = {'source': 'San Marino SIT Limite_stato_li; source survey date and datum-operation accuracy unestablished',
        'samples': n1 + n2, 'sampledMaximumCssPx': max(f, r),
        'continuousUpperBoundCssPx': max(f, r) + screen.STEP * screen.SCALE / 2}
report = {'scope': f'{len(after)} normalized current-country geometries; selected LSIB targets only',
    'historicalAccuracyVerified': False, 'widthCssPx': 2560, 'flatZoom': 64,
    'metadataAndDatedVersionsPreserved': True, 'groups': groups, 'areas': areas,
    'lsibDerivative': results, 'maximumLsibDerivativeUpperBoundCssPx': max(r['continuousUpperBoundCssPx'] for r in results),
    'sanMarinoIndependentComparison': comparison}
out = root / 'build-native/lsib-supplement' / candidate_name.replace('-candidate.json', '-staged-review.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k not in ('areas', 'lsibDerivative')}))
