import ast,json,re
from pathlib import Path
source=Path('tools/build-hydro-tiles.py').read_text(encoding='utf8')
tree=ast.parse(source)
names={'HYDRONYM_SUFFIX_RE','HYDRONYM_DUPLICATE_SUFFIX_RE','HYDRONYM_ENGLISH_SUFFIX_RE'}
nodes=[n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in names for t in n.targets)]
nodes += [n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='normalize_hydronym']
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),*nodes],type_ignores=[])
namespace={'re':re};exec(compile(ast.fix_missing_locations(module),'hydro-oracle','exec'),namespace)
aliases=json.loads(Path('assets/data/hydro/hydronym-ko-overrides.json').read_text(encoding='utf8'))['aliases']
names=['사우스아랄씨','노스아랄씨','사우스아랄씨호','노스아랄씨호','세인트 폴 강','레이크 위니페고시스','조지아 만','비스툴라 석호','브라마푸트라강 / 얄룽창포강','Example River','미명명 수계 4']
rows=[{'name':name,'category':category,'overrides':{k:aliases[k] for k in names if k in aliases},'expected':namespace['normalize_hydronym'](name,category,aliases)} for name in names for category in ['river','lake']]
Path('build-native/hydro-connectivity/hydronym-selected-python-oracle.json').write_text(json.dumps(rows,ensure_ascii=False),encoding='utf8')
print('selected cases',len(rows))
