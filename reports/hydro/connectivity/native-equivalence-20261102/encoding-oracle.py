import ast
import json
import struct
import types
from pathlib import Path

source = Path('tools/build-hydro-tiles.py').read_text(encoding='utf-8')
tree = ast.parse(source)
names = {'normalize_lon', 'quantize', 'line_parts', 'encode_uvarint', 'encode_svarint',
         'encode_line', 'encode_geometry', 'encode_width_profile', 'encode_source_ids', 'encode_feature'}
definitions = [item for item in tree.body if isinstance(item, ast.FunctionDef) and item.name in names]
module = ast.Module(body=[ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0), *definitions], type_ignores=[])
scope = {'struct': struct, 'MICRO': 1_000_000}
exec(compile(ast.fix_missing_locations(module), '<existing-hydro-encoder>', 'exec'), scope)

def feature(fid, category, geometry, bounds, widths=None, source_id='', **kwargs):
    return dict(fid=fid, logical_fid=fid+100, pandolab_id='fixture:'+str(fid), category=category,
                stage=kwargs.get('stage', 0), flags=kwargs.get('flags', 0), fragment_index=0,
                fragment_count=1, width=kwargs.get('width', 1.25), geometry=geometry, bounds=bounds,
                width_profile=widths, source_id=source_id)

rows = [
    feature(1, 'river', {'type':'LineString','coordinates':[[-180,0],[-179.999999,0.000001],[180,-0.000001]]},
            [-180,-0.000001,180,0.000001], [[0, 1.2345, 70]], '100,110,105', flags=1),
    feature(2, 'river', {'type':'MultiLineString','coordinates':[[[181,91],[0,0]], [[-181,-91],[-1.25,2.5]]]},
            [-181,-91,181,91], [[0.001,0.002],[2.5,2.5]], '1001,1000', stage=2),
    feature(3, 'lake', {'type':'Polygon','coordinates':[[[0,0],[1,0],[1,1],[0,0]], [[.25,.25],[.5,.25],[.25,.25]]]},
            [0,0,1,1], width=0),
    feature(4, 'lake', {'type':'MultiPolygon','coordinates':[[[[179,1],[-179,1],[-179,2],[179,1]]], [[[10,-1],[11,-1],[10,-1]]]]},
            [-179,-1,179,2], stage=3, width=0),
    feature(10, 'river', {'type':'LineString','coordinates':[[0,0],[1.002,0]]},
            [0,0,1.002,0], [[1,1]], '1'),
    feature(11, 'river', {'type':'LineString','coordinates':[[1.002,0],[2,0]]},
            [1.002,0,2,0], [[1,1]], '2', flags=1),
]
result=[]
for row in rows:
    obj=types.SimpleNamespace(**row)
    result.append({'feature':row,'featureHex':scope['encode_feature'](obj).hex(),
                   'sourceIdsHex':scope['encode_source_ids'](obj).hex()})
Path('tests/fixtures/hydro-encoding-oracle.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
