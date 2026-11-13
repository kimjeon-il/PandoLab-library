import ast,base64,json,math,struct,subprocess
from pathlib import Path
from PIL import Image
src=subprocess.check_output(['git','show','bffbabb6:tools/build-physical-data.py']).decode('utf8');fn=next(n for n in ast.parse(src).body if isinstance(n,ast.FunctionDef) and n.name=='crop_with_gutter')
m=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),fn],type_ignores=[]);scope={'Image':Image};exec(compile(ast.fix_missing_locations(m),'oracle','exec'),scope);crop=scope['crop_with_gutter']
r=json.loads(Path('tests/fixtures/physical-composite-oracle.json').read_text(encoding='utf8'));w,h=r['width'],r['height'];im=lambda k,mode:Image.frombytes(mode,(w,h),base64.b64decode(r[k]));images=[im('land','RGB'),im('ocean','RGB'),im('mask','L'),im('relief','L')];bands=[]
for img,mode in zip(images,['RGB','RGB','L','L']):
 for b in [(0,0,w,h),(w-1,0,w,h),(0,0,1,h)]:bands.append(img.crop(b).convert(mode).tobytes())
frame=struct.pack('<8sIIII',b'PDPCMP03',w,h,0,0)+b''.join(bands)
a,b,m,s=[crop(img,(0,0,w,h)) for img in images];red,green,blue=Image.composite(a,b,m).split();out=Image.merge('RGBA',(red,green,blue,s)).tobytes()
f={'frame':base64.b64encode(frame).decode(),'expected':base64.b64encode(out).decode()}
Path('tests/fixtures/physical-gutter-alpha-oracle.json').write_text(json.dumps(f,separators=(',',':')),encoding='utf8');print('bytes',len(out))


