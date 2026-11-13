import json,shapely
from pathlib import Path
from shapely.geometry import shape
req=json.loads(Path('build-native/territorial-recipe/german-coast-selected-geos313-oracle.json').read_text(encoding='utf8'))
source=Path('build-native/territorial-recipe/german-coast-oracle.py').read_text(encoding='utf8').split('def rect')[0]
old=shape(req['expected']['geometry'])
for distance in [2000,500,100]:
    scope={}
    exec(compile(source.replace('W=transform(q,result)',f'W=transform(q,result.segmentize({distance}))'),'oracle','exec'),scope)
    out=scope['run'](req['input']); new=shape(out['geometry'])
    print(distance,'valid',new.is_valid,shapely.is_valid_reason(new),'hausdorff degrees',old.boundary.hausdorff_distance(new.boundary),flush=True)
    if new.is_valid:
        with Path('build-native/territorial-recipe/german-coast-densified-oracle.json').open('x',encoding='utf8') as f:json.dump(out,f,separators=(',',':'))
        break
