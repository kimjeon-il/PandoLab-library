import json,math
from pyproj import Geod
p='build-native/territorial-recipe/current-lsib-coordinate-audit.json';d=json.load(open(p,encoding='utf-8-sig'));g=Geod(ellps='WGS84');chains={}
for results in d['geometryResults'].values():
 for mode,r in results.items():
  for c in r['chains']:
   h=c['coordinateHash'];points=c['coordinates'];length=g.line_length([p[0] for p in points],[p[1] for p in points]);chains[h]={'coordinateHash':h,'featureId':c['featureId'],'countries':c['countries'],'kind':c['kind'],'normalization':c['normalization'],'vertices':c['vertices'],'lengthMeters':length,'start':points[0],'end':points[-1],'referenceIndicesFirstLast':[c['referenceIndices'][0],c['referenceIndices'][-1]],'referencePartVertices':c['referencePartVertices'],'bbox':[min(p[0] for p in points),min(p[1] for p in points),max(p[0] for p in points),max(p[1] for p in points)]}
json.dump({'method':'PROJ pyproj.Geod WGS84 ellipsoidal geodesic sum over matched XY chain','chains':list(chains.values())},open('build-native/territorial-recipe/current-lsib-chain-lengths.json','w'),indent=2);print(json.dumps(list(chains.values())))
