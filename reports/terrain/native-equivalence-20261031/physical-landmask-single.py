import ast,json,math,subprocess
from pathlib import Path
from PIL import Image,ImageDraw
source=subprocess.check_output(['git','show','bffbabb6:tools/build-physical-data.py']).decode('utf8');tree=ast.parse(source);fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='build_outer_land_mask')
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),fn],type_ignores=[])
scope={'Image':Image,'ImageDraw':ImageDraw,'json':json,'math':math};exec(compile(ast.fix_missing_locations(module),'single-mask-oracle','exec'),scope)
r=Path('build-native/terrain-preview/physical-landmask-selected');a=json.loads((r/'countries.json').read_text(encoding='utf8'));b=json.loads((r/'lakes.json').read_text(encoding='utf8'));rows=[*a['features'],*b['features']]
(r/'empty.json').write_text(json.dumps({'type':'FeatureCollection','features':[]}),encoding='utf8')
for i,row in enumerate(rows):
 country={'type':'FeatureCollection','features':[row]};p=r/('single-'+str(i)+'.json');p.write_text(json.dumps(country),encoding='utf8')
 expected=scope['build_outer_land_mask'](p,r/'empty.json',(720,360)).tobytes();(r/('single-'+str(i)+'.bin')).write_bytes(expected)
 print(i,row['id'])
