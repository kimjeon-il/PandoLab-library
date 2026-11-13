import ast
import json
from pathlib import Path
import numpy as np

tree=ast.parse(Path('tools/verify-terrain-dem.py').read_text(encoding='utf-8'))
names={'validate_shade_values','compare_reference_tile'}
module=ast.Module(body=[item for item in tree.body if isinstance(item,ast.FunctionDef) and item.name in names],type_ignores=[])
scope={'np':np};exec(compile(ast.fix_missing_locations(module),'<original-terrain-verifier>','exec'),scope)
base=np.tile(np.array([12,34,4,255],dtype=np.uint8),(3,3,1))
cases=[]
for name in ['valid','shade','north-excluded','alpha','reference-close','reference-shade','reference-elevation']:
    value=base.copy();reference=None;north=False
    if name in ('shade','north-excluded'): value[0,0,2]=3;north=name=='north-excluded'
    if name=='alpha': value[0,0,3]=254
    if name.startswith('reference-'):
        reference=base.copy()
        if name=='reference-close': reference[0,0,2]=6
        if name=='reference-shade': reference[0,0,2]=7
        if name=='reference-elevation': reference[0,0,1]=35
    try:
        if np.any(value[:,:,3]!=255): raise ValueError('alpha')
        scope['validate_shade_values'](value[:,:,2],4,(0,) if north else ())
        if reference is not None: scope['compare_reference_tile'](value,reference,'fixture')
        ok=True
    except ValueError: ok=False
    cases.append(dict(name=name,pixels=value.ravel().tolist(),reference=None if reference is None else reference.ravel().tolist(),
                      excludeNorth=north,expected=ok))
Path('tests/fixtures/terrain-dem-check-oracle.json').write_text(json.dumps(cases,indent=2)+'\n',encoding='utf-8')
