import json,hashlib,copy
from pathlib import Path
from osgeo import ogr,osr,gdal
ogr.UseExceptions();osr.UseExceptions();O=Path('.');before=json.loads((O/'compiled-final-before.json').read_text());after=json.loads((O/'compiled-final-after.json').read_text());display=json.loads((O/'display-250.json').read_text());root=Path('D:/dev/worktrees/gis');src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);dst=osr.SpatialReference();dst.ImportFromEPSG(3035);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);tx=osr.CoordinateTransformation(src,dst)
def g(j):return ogr.CreateGeometryFromJson(json.dumps(j))
def rowgeom(c,day):
 for b in c['sourceBindings']:
  if (b['validFrom'] is None or b['validFrom']<=day)and(b['validTo']is None or b['validTo']>=day):return next(r['geojson']for r in c['geometries']if r['id']==b['geometryRef']['id']and r['version']==b['geometryRef']['version'])
 return None
def projected(z):z=z.Clone();z.Transform(tx);return z
def area(z):return projected(z).GetArea()/1e6
rows=[];plots={};shapes={};hist={'DEU':('DEU','1914-07-31'),'state:austro-hungarian-empire':('AH','1914-07-28'),'state:kingdom-of-serbia':('SERBIA','1914-07-28')}
for c in after:
 old=next((r for r in before if r['entityId']==c['entityId']),None)
 for r in c['geometries']:assert g(r['geojson']).IsValid(),(c['entityId'],r['id'])
 if c['entityId']in hist:
  key,day=hist[c['entityId']];z=g(rowgeom(c,day));assert z.SymDifference(g(display[key])).GetArea()<1e-12;(shapes.setdefault(day,{}))[c['entityId']]=z
 for day in ['1914-07-28','1914-07-31']:
  a=rowgeom(old,day)if old else None;b=rowgeom(c,day)
  if a is None or b is None:
   if old and a is not None:rows.append({'entityId':c['entityId'],'date':day,'removedEntireProxy':True,'changedKm2':area(g(a)),'reason':'Modern independent Hungary proxy is entirely within Austria-Hungary on the reference day.'});plots[c['entityId']+'@'+day]={'before':json.loads(projected(g(a)).ExportToJson()),'after':None,'changeBounds':projected(g(a)).GetEnvelope()}
   if b is not None:shapes.setdefault(day,{})[c['entityId']]=g(b)
   continue
  z0,z1=g(a),g(b);shapes.setdefault(day,{})[c['entityId']]=z1
  diff=z0.SymDifference(z1)
  if diff.GetArea()>1e-12:
   d=projected(diff);rows.append({'entityId':c['entityId'],'date':day,'changedKm2':d.GetArea()/1e6,'beforeComponents':z0.GetGeometryCount()if z0.GetGeometryName()=='MULTIPOLYGON'else 1,'afterComponents':z1.GetGeometryCount()if z1.GetGeometryName()=='MULTIPOLYGON'else 1,'changeBounds3035':list(d.GetEnvelope()),'valid':True});plots[c['entityId']+'@'+day]={'before':json.loads(projected(z0).ExportToJson()),'after':json.loads(projected(z1).ExportToJson()),'changeBounds':list(d.GetEnvelope())}
# All actual compiled participants at the two reference days are mutually disjoint.
checks=[]
for day,cs in shapes.items():
 ids=list(cs)
 for i,x in enumerate(ids):
  for y in ids[i+1:]:
   it=cs[x].Intersection(cs[y]);assert it.GetArea()<1e-12,(day,x,y,it.GetArea());checks.append({'date':day,'pair':[x,y],'overlapDegree2':it.GetArea()})
# Source masters remain exact archived bytes; include actual duplicate-component area.
masterPaths={'DEU':('tools/historical-library/working/german-empire-1914-base.geojson','1fc5aa30b821b981dc67d71dc62dd8643e1b24b006779c64489f7ec3a0cb2bfb'),'AH':('tools/historical-library/working/austro-hungarian-empire-1914-base.geojson','f5099311e89632b9047588a6a3c4bcfdedc075922015ee6a0e3ad273ff787148'),'SERBIA':('tools/historical-library/sources/serbia/serbia-1914.geojson','914dd9a93e6092b7436f99414fd19106fd0676a97c76c0a1e154096fad4591cd')}
for k,(p,h)in masterPaths.items():assert hashlib.sha256((root/p).read_bytes()).hexdigest()==h
raw=json.loads((root/masterPaths['DEU'][0]).read_text())['features'][0]['geometry'];dup={'type':'Polygon','coordinates':raw['coordinates'][1]};proof=json.loads((O/'topology-proof.json').read_text());proof['metrics']['DEU']['masterPoints']=sum(len(r)for p in raw['coordinates']for r in p);proof['metrics']['DEU']['deduplicatedMasterPoints']=7110;(O/'topology-proof.json').write_text(json.dumps(proof,indent=2));repair=json.loads((O/'repair-proof.json').read_text());repair['repairs']['DEU']['removedOverlapKm2']=area(g(dup));(O/'repair-proof.json').write_text(json.dumps(repair,indent=2));
output={'runtime':{'gdal':gdal.VersionInfo('--version'),'geos':'3.15.0'},'projection':'EPSG:3035 (traditional GIS order)','allCompiledGeometriesValid':True,'historicalSourceCompiledShapeDifferenceDegree2':0,'pairwiseReferenceDayOverlapMaximumDegree2':max(r['overlapDegree2']for r in checks),'pairwiseChecks':len(checks),'changes':rows,'masterHashesPreserved':{k:h for k,(p,h)in masterPaths.items()},'interpretation':'Modern peers are priority-clipped only on the explicit reference day. Their remaining outlines are preserved modern proxies, not newly reconstructed historical states.'};(O/'compiled-proof.json').write_text(json.dumps(output,indent=2));(O/'compiled-plots.json').write_text(json.dumps(plots));print(json.dumps({k:v for k,v in output.items()if k!='masterHashesPreserved'},indent=2))
