import ast,json,math,pathlib,random,subprocess,types
source=pathlib.Path('tools/calibrate-hydro.py')
tree=ast.parse(subprocess.check_output(['git','show','HEAD:tools/calibrate-hydro.py'],encoding='utf-8'))
names={'screen_line_length','screen_polygon_area'}
body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),*body],type_ignores=[])
ast.fix_missing_locations(module);scope={'math':math};exec(compile(module,str(source),'exec'),scope)
rng=random.Random(20261102);cases=[]
for name,bbox,width,height,groups,areas in [
    ('empty',[0,0,10,10],1200,720,[[],[[]]],[]),
    ('corners',[-180,-90,180,90],1200,720,[[[[-180,-90],[180,90]]],[[[0,0],[0,0],[1,0],[1,1]]]], [0,1,123.5]),
    ('small',[124,33,132,43],1200,720,[[[[124.0,33.0],[124.000000001,33.000000002],[131.9,42.9]]],
       [[[128,35],[129,36]],[[129,36],[130,35]]]], [0.0000001,0.3,8]),
    ('random',[-11,35,31,72],800,600,[[[[rng.uniform(-11,31),rng.uniform(35,72)] for _ in range(101)] for _ in range(3)] for _ in range(5)],
       [rng.random()*10 for _ in range(5)])]:
    region=types.SimpleNamespace(bbox=bbox)
    lengths=[scope['screen_line_length']([types.SimpleNamespace(coords=line) for line in group],region,width,height) for group in groups]
    scaled=[scope['screen_polygon_area']([types.SimpleNamespace(area=area)],region,width,height) for area in areas]
    cases.append(dict(name=name,request=dict(bbox=bbox,width=width,height=height,lines=groups,areas=areas),expected=dict(lineLengths=lengths,polygonAreas=scaled)))
pathlib.Path('tests/fixtures/hydro-calibration-screen-oracle.json').write_text('[\n'+',\n'.join(json.dumps(x,separators=(',',':')) for x in cases)+'\n]\n',encoding='utf-8')
print('Frozen original screen metric cases:',len(cases))
