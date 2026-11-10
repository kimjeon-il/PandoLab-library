import json,statistics
from pathlib import Path
r=Path(__file__).parent;x=json.loads((r/'detailed-components.json').read_text(encoding='utf8'));out=[]
for vid,rec in x['versions'].items():
 q=rec['explicitOmissions'];a=sorted(v['donorAreaKm2']for v in q);bins=[(0,.01),(.01,.1),(.1,1),(1,5),(5,float('inf'))];out.append({'versionId':vid,'count':len(a),'minimumKm2':min(a),'maximumKm2':max(a),'medianKm2':statistics.median(a),'totalKm2':sum(a),'distribution':[{'fromKm2':lo,'belowKm2':hi if hi!=float('inf')else None,'count':sum(lo<=v<hi for v in a)}for lo,hi in bins],'largest':sorted(q,key=lambda z:-z['donorAreaKm2'])[:3],'measurement':'pyproj.Geod WGS84 ellipsoidal polygon area on the unchanged approved donor coordinates; sum absolute exterior-minus-hole area, no screen-pixel conversion.'})
(r/'omitted-component-size-statistics.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out))
