from historical_detail_membership import *
from pathlib import Path
import gzip
B=Path(base);old=load(str(B/'historical-detail-darja-joint-baseline-request.json'))['historicalWater'];new=load(str(B/'historical-detail-darja-physical-exact-splice.json'))['water'];cs=load(str(B/'historical-detail-darja-physical-old-exact-arc.json'));ns=load(str(B/'historical-detail-west-darja-arcs.json'))['arcs'][-1]['new'];src=osr.SpatialReference();src.ImportFromEPSG(4326);src.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);dst=osr.SpatialReference();definition='+proj=aeqd +lat_0=39.4 +lon_0=53.7 +datum=WGS84 +units=m';dst.SetFromUserInput(definition);dst.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER);tr=osr.CoordinateTransformation(src,dst);project=lambda coords:[tr.TransformPoint(*p)[:2] for p in coords];a,b=project(cs),project(ns);x0,y0=tr.TransformPoint(53.2,38.7)[:2];x1,y1=tr.TransformPoint(54.3,40.1)[:2];parts=[]
for x,scale,title in [(20,10000000,'1:10M target scale'),(335,2000000,'5x diagnostic, not target detail')]:
 mpp=scale*.0254/96;xy=lambda p:(x+15+(p[0]-x0)/mpp,90+(y1-p[1])/mpp)
 def line(c):return ' '.join(('M' if i==0 else 'L')+f'{xy(p)[0]:.3f},{xy(p)[1]:.3f}' for i,p in enumerate(c))
 parts.append(f'<text x="{x}" y="67" font-size="13">{title}</text>')
 for coords in old['coordinates'][1:]:
  if any(53.2<=p[0]<=54.3 and 38.7<=p[1]<=40.1 for p in coords):parts.append(f'<path d="{line(project(coords))}" stroke="#88949e" fill="#eceff1" stroke-width=".6"/>')
 parts.append(f'<path d="{line(a)}" stroke="#b54132" stroke-width="1.3" fill="none"/><path d="{line(b)}" stroke="#174b89" stroke-width=".8" fill="none"/>')
svg='<svg xmlns="http://www.w3.org/2000/svg" width="700" height="490"><rect width="100%" height="100%" fill="white"/><g font-family="Arial" fill="#203043"><text x="20" y="25" font-size="18">Darja shared coast: local candidate verification</text><text x="20" y="45" font-size="12">Red: previous711-point water/land arc; blue: shared387-point candidate. Gray:islands unchanged.</text>'+''.join(parts)+'</g></svg>'
(B/'historical-detail-darja-local-comparison.svg').write_text(svg,encoding='utf-8');json.dump({'projection':definition,'execution':'GDAL OSR XY transform','targetScale':10000000,'diagnosticScale':2000000,'extent':[53.2,38.7,54.3,40.1],'beforeCoordinates':cs,'candidateCoordinates':ns},open(B/'historical-detail-darja-visual-input.json','x'),indent=2)
