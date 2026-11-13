import json
from shapely.geometry import shape
from shapely.validation import explain_validity
from pathlib import Path
r=json.loads(Path('build-native/territorial-recipe/german-coast-selected-compare.json').read_text(encoding='utf8'))
a,b=[shape(r[x]) for x in ['approved','published']]
print('approved',a.is_valid,explain_validity(a))
print('published',b.is_valid,explain_validity(b))
a,b=[x if x.is_valid else x.buffer(0) for x in [a,b]]
print('cleaned equal',a.equals(b),'symdiff degree2',a.symmetric_difference(b).area,'hausdorff degree',a.boundary.hausdorff_distance(b.boundary))
