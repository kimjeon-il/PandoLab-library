import json,hashlib,itertools
from pathlib import Path
import shapely
from shapely.geometry import shape,box,mapping
B=Path('D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/current-source-adoption-review/adjacency-review')
p=B/'scoped-island-input.json'; x=json.loads(p.read_text(encoding='utf8')); gs={f['id']:shape(f['geometry']) for f in x['features']}; scs=box(105,0,125,25); wake=box(166,19,167,20)
def parts(g):
 if g.is_empty:return []
 if g.geom_type=='Polygon':return [g]
 if hasattr(g,'geoms'):return [p for q in g.geoms for p in parts(q)]
 return []
def stat(g):return {'type':g.geom_type,'empty':g.is_empty,'valid':g.is_valid,'polygonAreaDegrees2':sum(p.area for p in parts(g)),'polygonParts':len(parts(g))}
recipients=['VNM','PHL','CHN','TWN']; pairs=[]
for a,b in itertools.combinations(recipients,2):
 q=gs[a].intersection(gs[b]);pairs.append({'a':a,'b':b,**stat(q)})
wparts=[{'componentIndex':i,'bbox':list(g.bounds),'areaDegrees2':g.area,'geometrySha256':hashlib.sha256(json.dumps(mapping(g),separators=(',',':')).encode()).hexdigest()} for i,g in enumerate(parts(gs['UMI'])) if g.intersects(wake)]
pga=[]
for r in recipients:
 q=gs['PGA'].intersection(gs[r]);pga.append({'recipient':r,**stat(q)})
out={'status':'bounded-canonical-recipient-and-wake-intersections-complete','sourceRevision':x['revision'],'inputSha256':hashlib.sha256(p.read_bytes()).hexdigest(),'engine':{'shapely':shapely.__version__,'geos':shapely.geos_version_string},'recipientPairs':pairs,'actualWakeUMI':{'envelope':[166,19,167,20],'components':wparts,'remainsInRetiredView':True,'basis':'UMI selection and whole canonical geometry exactly rebound in companion canonical-binding proof'},'retiredPGA':{'components':len(parts(gs['PGA'])),'bbox':list(gs['PGA'].bounds),'touchesActualWake':gs['PGA'].intersects(wake),'recipientIntersections':pga},'scopeLimits':['Polygonal intersection area only; line intersections do not contribute polygon area.','No coordinate rounding, simplification, snap, make-valid, ownership change, or source writes.','Approved original10 World Polygons components are distinct from12 old PGA parts. Independent original10 coverage not rerun here.','This is prospective retirement evidence; current authoring and runtime still require coherent retirement.']}
assert len(wparts)==2,wparts
assert [p['componentIndex'] for p in wparts]==[11,12],wparts
assert not gs['PGA'].intersects(wake)
assert all(p['polygonAreaDegrees2']==0 for p in pairs),pairs
(B/'island-intersections.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps(out,indent=2))
