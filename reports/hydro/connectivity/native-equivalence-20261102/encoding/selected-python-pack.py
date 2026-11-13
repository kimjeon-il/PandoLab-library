import ast
import gzip
import hashlib
import json
import os
import shutil
import stat
import struct
import types
from collections import defaultdict
from pathlib import Path

tree=ast.parse(Path('tools/build-hydro-tiles.py').read_text(encoding='utf-8'))
names={'normalize_lon','quantize','line_parts','encode_uvarint','encode_svarint','encode_line','encode_geometry',
       'encode_width_profile','encode_source_ids','encode_feature','geometry_coord_count','sha256','remove_readonly','PackBuilder'}
definitions=[item for item in tree.body if isinstance(item,(ast.FunctionDef,ast.ClassDef)) and item.name in names]
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),*definitions],type_ignores=[])
scope={'struct':struct,'gzip':gzip,'hashlib':hashlib,'json':json,'os':os,'shutil':shutil,'stat':stat,'Path':Path,'defaultdict':defaultdict,
       'MICRO':1_000_000,'PACK_FORMAT_VERSION':4,'PACK_RAW_LIMIT':512*1024,'SHARD_GZIP_LIMIT':4*1024*1024,
       'MAX_TOTAL_GZIP_MIB':48.,'STAGE_GRIDS':((8,4),(16,8),(32,16),(64,32))}
exec(compile(ast.fix_missing_locations(module),'<existing-hydro-packer>','exec'),scope)
row=json.loads(Path('build-native/hydro-encoding/selected-decoded.json').read_text(encoding='utf-8'));meta=row['metadata']
fields=dict(fid=meta['fid'],logical_fid=meta['logicalFid'],pandolab_id=meta['awId'],layer_id=meta['layerId'],category=meta['category'],
            stage=meta['stage'],name=meta['name'],source_id=meta.get('sourceId',''),source=meta.get('source',''),width=meta['width'],
            geometry=row['geometry'],bounds=tuple(x/1e6 for x in meta['bounds']),width_profile=row.get('widths'),
            fragment_index=meta['fragmentIndex'],fragment_count=meta['fragmentCount'],flags=meta['flags'],terminal=meta.get('terminal'),
            system_id=meta.get('systemId',''),mainstem_name_ko=meta.get('mainstemNameKo',''),role=meta.get('role',''),
            aliases=meta.get('aliases'),tributary_names=meta.get('tributaryNames'),osm_relation_ids=meta.get('osmRelationIds'))
output=Path('build-native/hydro-encoding/selected-python-pack')
if output.exists(): raise ValueError('Oracle output exists; preserve it')
builder=scope['PackBuilder'](output);builder.add(types.SimpleNamespace(**fields));builder.write()
