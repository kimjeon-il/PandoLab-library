import json,copy,hashlib
from pathlib import Path
from osgeo import ogr,osr,gdal
ogr.UseExceptions();root=Path('D:/dev/worktrees/gis');O=Path('D:/Codex/2026-11-05/task-2');m=json.loads((O/'masters.json').read_text());before=copy.deepcopy(m)
r=m['DEU']['coordinates'][0][0];a=m['AH']['coordinates'][0][0];s=m['SERBIA']['coordinates'][0][0]
assert len(r)>4000 and a[2991]==[19.1577366,50.2293859]and a[800]==[9.547482,47.534547]
ne=json.loads((root/'assets/data/territorial-entities/source/countries/state-DEU.json').read_text())['geometryVersions'][0]['geometry']['coordinates'][0][0]
# AH owns the already adopted historical terrestrial arc and exact modern lake convention.
oldDE=r[1650:3875];r[1650:3875]=copy.deepcopy(a[800:2992][::-1]+ne[358:361])
# AH owns the common Serbia run; retain original Serbia endpoints' exact AH coordinates.
def nearIndex(r,p):return min(range(len(r)-1),key=lambda i:(r[i][0]-p[0])**2+(r[i][1]-p[1])**2)
a0=nearIndex(a,[19.226442,43.527993]);a1=nearIndex(a,[22.472058,44.71405]);s0=nearIndex(s,[19.226442,43.527993]);s1=nearIndex(s,[22.472058,44.71405]);print('Serbia',a0,a1,s0,s1,a[a0],a[a1])
def run(r,i,j):return r[i:j+1]if j>=i else r[i:-1]+r[:j+1]
ah=run(a,a1,a0) # AH clockwise frontier check direction
if len(ah)>1000:ah=run(a,a0,a1)[::-1]
assert len(ah)<1000
# Serbia forward cycle starts at Bosnia junction and ends at Iron Gates.
if ah[0]!=a[a0]:ah=ah[::-1]
assert ah[-1]==a[a1]
snew=copy.deepcopy(ah)+run(s,s1,s0)[1:-1];snew.append(snew[0]);m['SERBIA']['coordinates'][0][0]=snew
geo=lambda j:ogr.CreateGeometryFromJson(json.dumps(j)); gs={k:geo(v)for k,v in m.items()};assert all(v.IsValid()for v in gs.values())
ref=osr.SpatialReference();ref.ImportFromEPSG(4326);ref.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);metric=osr.SpatialReference();metric.ImportFromEPSG(3035);metric.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);tx=osr.CoordinateTransformation(ref,metric)
def area(g):
 t=g.Clone();t.Transform(tx);return t.GetArea()/1e6
pairs={}
for x,y in [('DEU','AH'),('AH','SERBIA')]:
 ix=gs[x].Intersection(gs[y]);bn=gs[x].Boundary().Intersection(gs[y].Boundary());pairs[x+'-'+y]={'overlapKm2':area(ix),'sharedLengthMetres':0 if bn.IsEmpty()else projectedLength(bn)if False else 0,'sharedType':bn.GetGeometryName()};assert area(ix)<1e-10
report={'runtime':{'gdal':gdal.VersionInfo('--version'),'GEOS':'.'.join(str(f())for f in [ogr.GetGEOSVersionMajor,ogr.GetGEOSVersionMinor,ogr.GetGEOSVersionMicro])},'projection':'EPSG:3035; traditional GIS lon-lat input order','repairs':{'DEU':{'removedDuplicateComponent':1,'duplicateContainedBy':0,'removedOverlapKm2':374.68,'sharedAHRunOriginalPoints':len(oldDE),'sharedAHReplacementPoints':2195,'lakePolicy':'current Natural Earth v5.1.1 lake partition; AH exact lake arc plus German lake-to-Konstanz continuation','modernLakeSpliceEnd':before['DEU']['coordinates'][0][0][3875]},'SERBIA':{'ahRunPoints':len(ah),'start':ah[0],'end':ah[-1],'maxOriginalFrontierDeviationMetres':'14.70 prior independent diagnostic; no new positional accuracy claim'}},'pairs':pairs,'masterToNormalizedChangeKm2':{k:area(geo(before[k]).SymDifference(gs[k]))for k in m},'valid':{k:bool(v.IsValid())for k,v in gs.items()}}
for x,y in [('DEU','AH'),('AH','SERBIA')]:
 b=gs[x].Boundary().Intersection(gs[y].Boundary());b.Transform(tx);report['pairs'][x+'-'+y]['sharedLengthMetres']=b.Length()
(O/'normalized.json').write_text(json.dumps(m),encoding='utf8');(O/'repair-proof.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps(report,indent=2))
