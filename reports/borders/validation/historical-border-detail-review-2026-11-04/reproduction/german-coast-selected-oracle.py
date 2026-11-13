import json
from pathlib import Path
scope={}
source=Path('build-native/territorial-recipe/german-coast-oracle.py').read_text(encoding='utf8').split('def rect')[0]
exec(compile(source,'oracle','exec'),scope)
world=json.loads(Path('assets/data/countries-ne-5.1.1.geojson').read_text(encoding='utf8'))
modern=[x['geometry'] for x in world['features'] if x['id'] in ['DEU','DNK','POL','RUS','LTU']]
assert len(modern)==5
root=Path('tools/historical-library/sources/german-empire-1914')
read=lambda name:json.loads((root/name).read_text(encoding='utf8'))['geometry']
controls=[('Berlin',(13.405,52.52),True),('Strasbourg',(7.7521,48.5734),True),('Poznan',(16.9252,52.4064),True),('Danzig',(18.6466,54.352),True),('Memel',(21.1443,55.7033),True),('Warsaw',(21.0122,52.2297),False),('Copenhagen',(12.5683,55.6761),False),('Prague',(14.4378,50.0755),False)]
input={'historical':read('histogis-deutsches-reich-1871-1919.geojson'),'modern':modern,'helgoland':read('helgoland-osm-preserved.geojson'),'dune':read('dune-osm-way-273992076.geojson'),'controls':[{'name':n,'point':p,'expected':e} for n,p,e in controls]}
expected=scope['run'](input)
out=Path('build-native/territorial-recipe/german-coast-selected-oracle.json')
with out.open('x',encoding='utf8') as stream:json.dump({'input':input,'expected':expected},stream,separators=(',',':'))
print(json.dumps({k:v for k,v in expected.items() if k!='geometry'}))
