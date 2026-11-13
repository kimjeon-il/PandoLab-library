import ast,base64,json,math,tempfile
from pathlib import Path
from PIL import Image,ImageDraw
source=Path('tools/build-physical-data.py').read_text(encoding='utf8');tree=ast.parse(source)
func=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='build_outer_land_mask')
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),func],type_ignores=[])
scope={'Image':Image,'ImageDraw':ImageDraw,'json':json,'math':math};exec(compile(ast.fix_missing_locations(module),'mask-oracle','exec'),scope)
def fc(geoms):return {'type':'FeatureCollection','features':[{'type':'Feature','properties':{},'geometry':g} for g in geoms]}
def poly(*rings):return {'type':'Polygon','coordinates':list(rings)}
a=[[-100,60],[-20,60],[-20,-50],[-100,-50],[-100,60]]
hole=[[-80,40],[-40,40],[-40,-30],[-80,-30],[-80,40]]
b=[[165,80],[-165,80],[-165,-70],[165,-70],[165,80]]
c=[[30,20],[80,20],[80,-10],[30,-10],[30,20]]
cases=[('outer-fills-hole',fc([poly(a,hole)]),fc([])),('dateline-and-lakes',fc([poly(b)]),fc([poly(c)]))]
rows=[]
with tempfile.TemporaryDirectory(prefix='pando-physical-mask-') as d:
 for name,countries,lakes in cases:
  cp=Path(d)/'countries.json';lp=Path(d)/'lakes.json';cp.write_text(json.dumps(countries),encoding='utf8');lp.write_text(json.dumps(lakes),encoding='utf8')
  image=scope['build_outer_land_mask'](cp,lp,(36,18))
  merged=fc([f['geometry'] for f in countries['features']+lakes['features']]);rows.append({'name':name,'countries':merged,'width':36,'height':18,'x':0,'y':0,'levelWidth':36,'levelHeight':18,'fillHoles':True,'expectedBase64':base64.b64encode(image.tobytes()).decode()})
Path('tests/fixtures/physical-land-mask-oracle.json').write_text(json.dumps(rows,separators=(',',':'))+'\n',encoding='utf8')
print('mask cases',len(rows))
