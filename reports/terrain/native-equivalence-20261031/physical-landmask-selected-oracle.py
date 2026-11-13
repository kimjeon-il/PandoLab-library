import ast,hashlib,json,math,subprocess
from pathlib import Path
from PIL import Image,ImageDraw
source=subprocess.check_output(['git','show','bffbabb6:tools/build-physical-data.py']).decode('utf8');tree=ast.parse(source)
func=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='build_outer_land_mask')
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),func],type_ignores=[])
scope={'Image':Image,'ImageDraw':ImageDraw,'json':json,'math':math};exec(compile(ast.fix_missing_locations(module),'selected-mask-oracle','exec'),scope)
r=Path('build-native/terrain-preview/physical-landmask-selected');a=scope['build_outer_land_mask'](r/'countries.json',r/'lakes.json',(720,360)).tobytes()
with (r/'expected.bin').open('xb') as f:f.write(a)
print('pixels',len(a),'land',sum(x==255 for x in a),'sha256',hashlib.sha256(a).hexdigest())
