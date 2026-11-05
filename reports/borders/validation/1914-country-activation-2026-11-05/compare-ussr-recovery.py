import json
from osgeo import ogr,osr
with open('p2-ussr-gate-input.json',encoding='utf-8-sig') as f:old=json.load(f)['country']
with open('ussr-scoped-country-diagnostic.json',encoding='utf-8-sig') as f:new=json.load(f)
vid='state:soviet-union:1922-12-30-reviewed-v2'
def shape(c):
 b=next(b for b in c['sourceBindings'] if b['sourceVersionId']==vid)
 return ogr.CreateGeometryFromJson(json.dumps(next(g['geojson'] for g in c['geometries'] if g['id']==b['geometryRef']['id'] and g['version']==b['geometryRef']['version'])))
a,b=shape(old),shape(new)
s=a.SymmetricDifference(b)
src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
dst=osr.SpatialReference();dst.ImportFromEPSG(6933);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
t=osr.CoordinateTransformation(src,dst);projected=s.Clone();projected.Transform(t)
result={'scope':'Read-only comparison of the pinned reviewed compiled USSR geometry and one bounded interval diagnostic; no normalization or publication','oldValid':bool(a.IsValid()),'diagnosticValid':bool(b.IsValid()),'topologicallyEqual':bool(a.Equals(b)),'symmetricDifferenceEmpty':bool(s.IsEmpty()),'symmetricDifferenceKm2':projected.GetArea()/1e6,'symmetricDifferenceComponents':s.GetGeometryCount(),'differenceEnvelope':list(s.GetEnvelope()),'projection':'EPSG:6933; traditional GIS longitude/latitude input','oldDigest':'8ce55c0f889fe402d3e5e7e30f0a3d5076363c2ca4cdbd79ab596ff4992e7ca6','diagnosticDigest':'22e0f3ef5cead6169325705b136ac1627957f87b1425de6902d0f741f682ea37'}
with open('ussr-recovery-geometry-comparison.json','w',encoding='utf-8') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
