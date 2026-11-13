import ast,base64,hashlib,json,math,tempfile
from pathlib import Path
from PIL import Image,ImageDraw
src=Path('tools/build-physical-data.py').read_text(encoding='utf8')
import subprocess
src=subprocess.check_output(['git','show','bffbabb6:tools/build-physical-data.py']).decode('utf8')
fn=next(n for n in ast.parse(src).body if isinstance(n,ast.FunctionDef) and n.name=='build_outer_land_mask')
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),fn],type_ignores=[]);scope={'Image':Image,'ImageDraw':ImageDraw,'json':json,'math':math};exec(compile(ast.fix_missing_locations(module),'edge-oracle','exec'),scope)
g={'type':'Polygon','coordinates':[[[179.5,52],[179.8,52],[179.8,50],[179.5,50],[179.5,52]]]}
fc={'type':'FeatureCollection','features':[{'type':'Feature','properties':{},'geometry':g}]}
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp);(p/'countries.json').write_text(json.dumps(fc));(p/'lakes.json').write_text(json.dumps({'type':'FeatureCollection','features':[]}))
 out=scope['build_outer_land_mask'](p/'countries.json',p/'lakes.json',(720,360)).tobytes()
req={'name':'offscreen-antimeridian-copy','countries':fc,'x':0,'y':0,'width':720,'height':360,'levelWidth':720,'levelHeight':360,'fillHoles':True,'expectedSha256':hashlib.sha256(out).hexdigest()}
Path('tests/fixtures/physical-land-mask-edge-oracle.json').write_text(json.dumps(req,separators=(',',':'))+'\n',encoding='utf8')
print(req['expectedSha256'],sum(x==255 for x in out))
