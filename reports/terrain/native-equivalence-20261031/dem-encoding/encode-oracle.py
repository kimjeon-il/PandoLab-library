import ast
import base64
import json
import math
from pathlib import Path
import numpy as np

tree=ast.parse(Path('tools/build-terrain-dem.py').read_text(encoding='utf-8'))
names={'shade','quantize_shade','encode'}
module=ast.Module(body=[item for item in tree.body if isinstance(item,ast.FunctionDef) and item.name in names],type_ignores=[])
scope={'np':np,'math':math,'RADIUS_METERS':6371008.8,'LIGHT_AZIMUTH':315.,'LIGHT_ALTITUDE':45.,
       'AMBIENT':.42,'DIFFUSE':.58,'SHADE_QUANTIZATION_STEP':4,'BIAS':12000}
exec(compile(ast.fix_missing_locations(module),'<original-dem-encode>','exec'),scope)
rows=[]
def case(name,elevation,width,height,north):
    elevation=np.asarray(elevation,dtype=np.float32)
    rows.append(dict(name=name,width=elevation.shape[1],height=elevation.shape[0],levelWidth=width,levelHeight=height,north=north,
                     elevation=base64.b64encode(elevation.astype('<f4').tobytes()).decode(),
                     shade=base64.b64encode(scope['shade'](elevation,width,height,north).tobytes()).decode(),
                     rgba=base64.b64encode(scope['encode'](elevation,width,height,north).tobytes()).decode()))
case('zero-and-range',[[-12000,-11745,-11744,0,53535]],5,1,0)
case('coarse-polar',[[100,200,300,400],[200,300,400,500],[300,400,500,600],[400,500,600,700]],4,2,-1)
case('fine-polar',[[100,200,300],[250,1000,350],[20,-100,500]],43200,21600,-1)
case('southern-polar',[[20,-50,80],[900,300,1000],[-120,12,111]],43200,21600,21599)
case('rounding',[[-1.5,-.5,.5,1.5,2.5,3.5]],6,3,1)
rng=np.random.default_rng(8251)
for i in range(4):
    values=rng.uniform(-11000,25000,size=(7,9)).astype(np.float32)
    case('random-'+str(i),values,43200,21600,[0,7000,10800,21593][i])
Path('tests/fixtures/terrain-dem-encoding-oracle.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
