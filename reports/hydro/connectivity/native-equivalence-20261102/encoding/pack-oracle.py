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
output=Path('build-native/hydro-encoding/oracle-packs')
if output.exists(): raise ValueError('Oracle output exists; preserve it')
builder=scope['PackBuilder'](output)
rows=json.loads(Path('tests/fixtures/hydro-encoding-oracle.json').read_text(encoding='utf-8'))
for row in rows:
    fields={**dict(layer_id='fixture',name='Test',source='fixture',terminal=None,system_id='',mainstem_name_ko='',role='',
                   aliases=None,tributary_names=None,osm_relation_ids=None),**row['feature']}
    builder.add(types.SimpleNamespace(**fields))
stats=builder.write()
layout=stats['_layout'];packs=[]
for row in layout['packs']:
    shard=(output / layout['shards'][row['shard']]['url']).read_bytes()
    compressed=shard[row['offset']:row['offset']+row['length']]
    packs.append({'id':row['id'],'stage':row['stage'],'owner':row['owner'],'features':row['features'],
                  'rawHex':gzip.decompress(compressed).hex(),'gzipHex':compressed.hex()})
result={'packs':packs,'indexRawHex':gzip.decompress((output/'index.bin.gz').read_bytes()).hex(),
        'indexGzipHex':(output/'index.bin.gz').read_bytes().hex(),
        'metadataCore':json.loads(gzip.decompress((output/'metadata-core.json.gz').read_bytes())),
        'metadataDetail':json.loads(gzip.decompress((output/'metadata-detail.json.gz').read_bytes())),
        'statistics':{key:value for key,value in stats.items() if key!='_layout'}}
Path('tests/fixtures/hydro-pack-oracle.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
