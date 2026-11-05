import json,copy,math
from pathlib import Path
O=Path('.');R=Path('D:/dev/worktrees/gis/assets/data/territorial-entities/source/countries');m=json.loads((O/'normalized.json').read_text());refs={};pointmap={};box=[5,40,28,57]
for code in ['DEU','DNK','POL','RUS','LTU','HRV','SVN','ITA','AUT','CHE']:
 g=json.loads((R/f'state-{code}.json').read_text())['geometryVersions'][0]['geometry'];ps=g['coordinates']if g['type']=='MultiPolygon'else[g['coordinates']];runs=[]
 for pol in ps:
  for ring in pol:
   r=[]
   for p in ring:
    if box[0]<=p[0]<=box[2]and box[1]<=p[1]<=box[3]:r.append(p);pointmap.setdefault((round(p[0],6),round(p[1],6)),p)
    elif r:
     if len(r)>1:runs.append(r)
     r=[]
   if len(r)>1:runs.append(r)
 refs['reference-'+code]={'type':'MultiLineString','coordinates':runs}
counts={}
for k,g in m.items():
 n=0
 for pol in g['coordinates']:
  for ring in pol:
   for i,p in enumerate(ring):
    q=pointmap.get((round(p[0],6),round(p[1],6)))
    if q is not None and max(abs(q[j]-p[j])for j in range(2))<2e-7:
     if q!=p:n+=1
     ring[i]=q
 counts[k]=n
(O/'normalized-ne-snapped.json').write_text(json.dumps(m));(O/'ne-reference-arcs.json').write_text(json.dumps(refs));(O/'reference-snapping-proof.json').write_text(json.dumps({'method':'Only exact 6-decimal matches to preserved selected NE reference vertices are replaced by those original reference coordinate pairs; no global rounding and no nearest unrelated vertex snapping.','maximumCoordinateDifferenceDegrees':2e-7,'changedVertices':counts,'references':list(refs),'coastArcPolicy':'Arcs shared with these existing NE lines are retained intact, not generalized again.'},indent=2));print(counts)
