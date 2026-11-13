import ast,json
from pathlib import Path
source=Path('tools/build-physical-data.py').read_text(encoding='utf8');tree=ast.parse(source)
nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('scalar','hydro_properties')]
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),*nodes],type_ignores=[])
scope={};exec(compile(ast.fix_missing_locations(module),'physical-oracle','exec'),scope)
records=[{}, {'ne_id':123,'name_ko':'한강','name_en':'Han River','scalerank':2,'min_zoom':3.5,'strokeweig':1.2,'wikidataid':'Q1'},
 {'ne_id':0,'id':'name-17','name':'Example','scalerank':'4','min_zoom':'bad','strokeweig':None},
 {'objectid':42,'name_ko':'','name_en':'','name':'Lake','scalerank':None,'min_zoom':-1.25,'strokeweig':'3.125'},
 {'id':-2,'name':'No rank','scalerank':20,'min_zoom':None,'strokeweig':'bad'}]
rows=[{'record':v,'layer':'rivers_base','category':'river','index':i,'expected':scope['hydro_properties'](v,'rivers_base','river',i)} for i,v in enumerate(records)]
Path('tests/fixtures/physical-hydro-properties-oracle.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('cases',len(rows))
