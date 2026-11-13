import ast
import json
import re
from pathlib import Path

tree=ast.parse(Path('tools/build-hydro-tiles.py').read_text(encoding='utf8'))
constants={'HYDRONYM_SUFFIX_RE','HYDRONYM_DUPLICATE_SUFFIX_RE','HYDRONYM_ENGLISH_SUFFIX_RE'}
nodes=[node for node in tree.body if (isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in constants for t in node.targets))
       or (isinstance(node,ast.FunctionDef) and node.name=='normalize_hydronym')]
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),*nodes],type_ignores=[])
scope={'re':re};exec(compile(ast.fix_missing_locations(module),'<original-hydronym>','exec'),scope)
aliases=json.loads(Path('assets/data/hydro/hydronym-ko-overrides.json').read_text(encoding='utf8'))['aliases']
cases=[('사우스아랄씨','lake',aliases),('노스아랄씨호','lake',aliases),('세인트 폴 강','river',{}),
       ('레이크 위니페고시스','lake',{}),('조지아 만','lake',{}),('비스툴라 석호','lake',{}),
       ('브라마푸트라강 / 얄룽창포강','river',{}),('Example River','river',{}),('미명명 수계 4','river',{}),
       ('Example','river',{'Example':'산타 마리아강'}),('  한\u0085강  ','river',{}),
       ('ELBE RİVER','river',{}),('A LaKe','lake',{}),('', 'river',{})]
rows=[]
for name,category,overrides in cases:
    # Retain only aliases relevant to this fixed input and its immediate result.
    expected=scope['normalize_hydronym'](name,category,overrides)
    selected={k:v for k,v in overrides.items() if k in (name,expected)}
    if scope['normalize_hydronym'](name,category,selected)!=expected:selected=overrides
    rows.append(dict(name=name,category=category,overrides=selected,expected=expected))
Path('tests/fixtures/hydro-name-oracle.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
