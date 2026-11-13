import os,json,hashlib
from osgeo import ogr,osr
ogr.UseExceptions()
base='build-native/territorial-recipe/'
inputs=json.load(open(base+'historical-detail-line-inputs.json',encoding='utf-8-sig'))
ne=json.load(open('assets/data/countries-ne-5.1.1.geojson',encoding='utf-8-sig'))
geo=lambda x: ogr.CreateGeometryFromJson(json.dumps(x))
features={f['id']:geo(f['geometry']) for f in ne['features'] if f['id'] in ['BLR','UKR','RUS']}
version=lambda code: next(v for v in json.load(open('assets/data/territorial-entities/source/countries/state-soviet-union-'+code+'.json',encoding='utf-8-sig'))['geometryVersions'] if v['versionId'].endswith('1922-12-30-reviewed-v2'))
versions={k:version(v) for k,v in [('BLR','byelorussian-ssr'),('UKR','ukrainian-ssr'),('RUS','russian-sfsr')]}
polygons={k:geo(v['geometry']) for k,v in versions.items()}
def lines(g):
 if g.GetGeometryName() in ['LINESTRING','LINEARRING']:return [g.Clone()]
 return [l for i in range(g.GetGeometryCount()) for l in lines(g.GetGeometryRef(i))]
def merged(g):
 chains=[list(l.GetPoints() or []) for l in lines(g) if not l.IsEmpty()]
 changed=True
 while changed:
  changed=False
  for i in range(len(chains)):
   for j in range(i+1,len(chains)):
    a,b=chains[i],chains[j]
    if a[-1]==b[0]:c=a+b[1:]
    elif a[-1]==b[-1]:c=a+list(reversed(b))[1:]
    elif a[0]==b[-1]:c=b+a[1:]
    elif a[0]==b[0]:c=list(reversed(b))+a[1:]
    else:continue
    chains[i]=c;chains.pop(j);changed=True;break
   if changed:break
 result=[]
 for chain in chains:
  line=ogr.Geometry(ogr.wkbLineString)
  for p in chain:line.AddPoint_2D(p[0],p[1])
  result.append(line)
 return result
rows=[];sample=[]
for name,left,right in [('by-ru','BLR','RUS'),('by-ua','BLR','UKR'),('ua-ru-main','UKR','RUS')]:
 entry=next(e for e in inputs if e['logical'].endswith('/'+name+'-display.geojson'))
 document=json.load(open(entry['file'],encoding='utf-8-sig'));historic=geo(document['geometry']);envelope=historic.GetEnvelope();extent=[envelope[0]-.15,envelope[2]-.15,envelope[1]+.15,envelope[3]+.15]
 box=geo({'type':'Polygon','coordinates':[[[extent[0],extent[1]],[extent[2],extent[1]],[extent[2],extent[3]],[extent[0],extent[3]],[extent[0],extent[1]]]]})
 modern_parts=merged(features[left].Boundary().Intersection(features[right].Boundary()))
 if not modern_parts:raise RuntimeError('No comparable modern line '+name)
 modern=max(modern_parts,key=lambda l:l.Length());historic=max(lines(historic.Intersection(box)),key=lambda l:l.Length())
 if modern.IsEmpty() or historic.IsEmpty():raise RuntimeError('Empty comparison chain '+name)
 menv=modern.GetEnvelope();extent=[min(extent[0],menv[0]-.15),min(extent[1],menv[2]-.15),max(extent[2],menv[1]+.15),max(extent[3],menv[3]+.15)]
 definition='+proj=aeqd +lat_0='+str((extent[1]+extent[3])/2)+' +lon_0='+str((extent[0]+extent[2])/2)+' +datum=WGS84 +units=m +type=crs'
 src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
 dst=osr.SpatialReference();dst.SetFromUserInput(definition);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);transform=osr.CoordinateTransformation(src,dst)
 def metric(g):
  p=g.Clone();p.Transform(transform);return [[x[0],x[1]] for x in p.GetPoints()]
 coverage={k:{'missingLengthDegrees':historic.Difference(polygons[k].Boundary()).Length(),'intersectionLengthDegrees':historic.Intersection(polygons[k].Boundary()).Length()} for k in [left,right]}
 if any(v['missingLengthDegrees']>0 for v in coverage.values()):
  retained=historic.Intersection(polygons[left].Boundary()).Intersection(polygons[right].Boundary())
  historic=max(merged(retained),key=lambda l:l.Length())
 sample.append({'id':name,'scope':'Same geographic window and local projection; historical route differs politically. Detail comparison only; no positional-error or tolerance inference. Longest modern connected component, not the full modern border.','metricCrs':definition,'projectionEvidence':'Existing GDAL/PROJ OSR.CoordinateTransformation actually executed; traditional GIS XY axis order. PROJ '+str(osr.GetPROJVersionMajor()),'extent':extent,'historical':metric(historic),'work':metric(modern),'geographic':{'historical':json.loads(historic.ExportToJson()),'modern':json.loads(modern.ExportToJson())},'candidateSha256':entry['receipt']['sha256'],'sourceCandidate':entry['logical'],'originalCandidateCounterpartCoverage':coverage,'measurementScope':'Longest exact both-counterpart applied component if original candidate was partly superseded; otherwise full candidate' })
 rows.append({'id':name,'historicVertices':historic.GetPointCount(),'modernVertices':modern.GetPointCount(),'coverage':coverage,'measuredComponentFullyApplied':all(historic.Difference(polygons[k].Boundary()).Length()==0 for k in [left,right])})
json.dump({'schema':'pando-border-detail-samples-v1','samples':sample,'scope':'Three explicitly selected BY/UA/RU applied-candidate shared arcs; no world validation'},open(base+'historical-detail-metric-input.json','w'),ensure_ascii=False,indent=2)
print(json.dumps(rows))
