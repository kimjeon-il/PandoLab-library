import ast,base64,io,json,math,subprocess,tempfile
from pathlib import Path
from PIL import Image,ImageDraw
source=subprocess.check_output(['git','show','bffbabb6:tools/build-physical-data.py']).decode('utf8')
tree=ast.parse(source);names={'crop_with_gutter','build_outer_land_mask','combine_land_without_drainages'}
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),*[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]],type_ignores=[])
scope={'Image':Image,'ImageDraw':ImageDraw,'json':json,'math':math};exec(compile(ast.fix_missing_locations(module),'gray-original','exec'),scope)
o=json.loads(Path('tests/fixtures/physical-build-mini-oracle.json').read_text(encoding='utf8'));w,h=o['width'],o['height']
images={k:Image.frombytes('RGB',(w,h),base64.b64decode(v)) for k,v in o['inputs'].items()};images['gray']=images['gray'].convert('L')
tiff=io.BytesIO();images['gray'].save(tiff,format='TIFF',compression='raw')
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp);(p/'countries.json').write_text(json.dumps(o['countries']));(p/'lakes.json').write_text(json.dumps(o['lakes']))
 mask=scope['build_outer_land_mask'](p/'countries.json',p/'lakes.json',(w,h));tiles=[]
 for level,width in enumerate((2,4)):
  height=width//2;scaled={name:(image if width==w else image.resize((width,height),Image.Resampling.LANCZOS)) for name,image in images.items()}
  scaled_mask=mask if width==w else mask.resize((width,height),Image.Resampling.NEAREST)
  for col in range((width+1)//2):
   box=(col*2,0,min(width,(col+1)*2),height);crop=scope['crop_with_gutter'];land=crop(scaled['land'],box);ocean=crop(scaled['ocean'],box);m=crop(scaled_mask,box);gray=crop(scaled['gray'],box).convert('L')
   rgb=scope['combine_land_without_drainages'](land,ocean,m);r,g,b=rgb.split();rgba=Image.merge('RGBA',(r,g,b,gray))
   tiles.append(dict(level=level,column=col,width=rgba.width,height=rgba.height,rgba=base64.b64encode(rgba.tobytes()).decode()))
 Path('tests/fixtures/physical-build-mini-gray-oracle.json').write_text(json.dumps(dict(tiff=base64.b64encode(tiff.getvalue()).decode(),tiles=tiles),separators=(',',':')),encoding='utf8')
