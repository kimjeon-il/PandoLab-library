from historical_detail_membership import *
d=load(base+'historical-detail-konotop-tc-current-chains.json');out=[]
for family in d['rows']:
 for i,ch in enumerate(family['chunks']):
  if ch['role']!='nonmodern-unreviewed':continue
  ps=ch['coordinates'];xs=[p[0] for p in ps];ys=[p[1] for p in ps];lat=(min(ys)+max(ys))/2;lon=(min(xs)+max(xs))/2;definition=f'+proj=aeqd +lat_0={lat} +lon_0={lon} +datum=WGS84 +units=m +type=crs';src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);dst=osr.SpatialReference();dst.SetFromUserInput(definition);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);tr=osr.CoordinateTransformation(src,dst);coords=[list(tr.TransformPoint(*p)[:2]) for p in ps];out.append({'id':family['id']+'-'+str(i),'metricCrs':definition,'projectionEvidence':'OSGeo GDAL/PROJ transform executed, traditional XY','historical':coords,'extent':[min(xs),min(ys),max(xs),max(ys)],'geographic':{'historical':{'type':'LineString','coordinates':ps}},'scope':'Actual adopted nonmodern shared component, not recovered source master'});print(out[-1]['id'],len(ps),out[-1]['extent'],ps[0],ps[-1],flush=True)
json.dump({'schema':'pando-border-detail-samples-v1','samples':out},open(base+'historical-detail-konotop-tc-metric-input.json','w'),indent=2)
