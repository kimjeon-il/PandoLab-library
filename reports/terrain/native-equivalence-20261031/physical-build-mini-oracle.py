import ast,base64,json,math,subprocess,tempfile
from pathlib import Path
from PIL import Image,ImageDraw
source=subprocess.check_output(['git','show','bffbabb6:tools/build-physical-data.py']).decode('utf8');tree=ast.parse(source)
names={'crop_with_gutter','build_outer_land_mask','combine_land_without_drainages'}
nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),*nodes],type_ignores=[])
scope={'Image':Image,'ImageDraw':ImageDraw,'json':json,'math':math};exec(compile(ast.fix_missing_locations(module),'mini-original','exec'),scope)
w,h=4,2;images={}
for name,step,start in [('land',31,7),('ocean',17,211),('gray',11,25)]:images[name]=Image.frombytes('RGB',(w,h),bytes((i*step+start)%256 for i in range(w*h*3)))
countries={'type':'FeatureCollection','features':[{'type':'Feature','properties':{},'geometry':{'type':'Polygon','coordinates':[[[-180,-90],[0,-90],[0,90],[-180,90],[-180,-90]]]}}]}
lakes={'type':'FeatureCollection','features':[]}
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp);(p/'countries.json').write_text(json.dumps(countries));(p/'lakes.json').write_text(json.dumps(lakes))
 mask=scope['build_outer_land_mask'](p/'countries.json',p/'lakes.json',(w,h));tiles=[]
 for level,width in enumerate((2,4)):
  height=width//2
  scaled={name:(image if width==w else image.resize((width,height),Image.Resampling.LANCZOS)) for name,image in images.items()}
  scaled_mask=mask if width==w else mask.resize((width,height),Image.Resampling.NEAREST)
  for col in range((width+1)//2):
   box=(col*2,0,min(width,(col+1)*2),height);crop=scope['crop_with_gutter'];land=crop(scaled['land'],box);ocean=crop(scaled['ocean'],box);m=crop(scaled_mask,box);gray=crop(scaled['gray'],box).convert('L')
   rgb=scope['combine_land_without_drainages'](land,ocean,m);r,g,b=rgb.split();rgba=Image.merge('RGBA',(r,g,b,gray))
   tiles.append({'level':level,'column':col,'width':rgba.width,'height':rgba.height,'rgba':base64.b64encode(rgba.tobytes()).decode('ascii')})
 doc={'width':w,'height':h,'inputs':{k:base64.b64encode(v.tobytes()).decode('ascii') for k,v in images.items()},'countries':countries,'lakes':lakes,'tiles':tiles}
 Path('tests/fixtures/physical-build-mini-oracle.json').write_text(json.dumps(doc,separators=(',',':')),encoding='utf8')
 print('tiles',len(tiles),'mask',list(mask.tobytes()))
