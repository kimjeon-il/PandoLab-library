import json,pathlib
from osgeo import ogr
p=pathlib.Path(__file__).parent
a=ogr.CreateGeometryFromJson(json.dumps(json.loads((p/'CUB-raw-candidate.geojson').read_text())['geometry']));b=ogr.CreateGeometryFromJson(json.dumps(json.loads((p/'USG-raw-candidate.geojson').read_text())['geometry']))
x=a.Boundary().Intersection(b.Boundary());assert a.Intersection(b).GetArea()==0 and x.Length()>0
u=a.Union(b);assert u.IsValid()
r={'entities':['state:CUB','state:USG'],'sourceCoordinatesUnmodified':True,'pairedMigration':True,'intersectionArea':0,'sharedBoundaryLengthDegrees':x.Length(),'unionValid':True,'unionPolygonCount':u.GetGeometryCount(),'unionUsedAsSource':False,'note':'Raw original feature pair adopted together; union only checks topology; no generated coordinates written.'}
(p/'cuba-paired-topology-check.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
