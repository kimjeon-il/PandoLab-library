import ast
import json
import struct
import types
from pathlib import Path

tree=ast.parse(Path('tools/build-hydro-tiles.py').read_text(encoding='utf-8'))
names={'normalize_lon','quantize','line_parts','encode_uvarint','encode_svarint','encode_line',
       'encode_geometry','encode_width_profile','encode_source_ids','encode_feature'}
definitions=[item for item in tree.body if isinstance(item,ast.FunctionDef) and item.name in names]
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),*definitions],type_ignores=[])
scope={'struct':struct,'MICRO':1_000_000}
exec(compile(ast.fix_missing_locations(module),'<existing-hydro-encoder>','exec'),scope)
feature=types.SimpleNamespace(**json.loads(Path('build-native/hydro-encoding/selected-feature.json').read_text(encoding='utf-8')))
result={'featureHex':scope['encode_feature'](feature).hex(),'sourceIdsHex':scope['encode_source_ids'](feature).hex()}
Path('build-native/hydro-encoding/selected-oracle.json').write_text(json.dumps(result)+'\n',encoding='utf-8')
