import json,math
from pathlib import Path
from shapely.geometry import shape
from shapely.ops import transform
from pyproj import Transformer
from PIL import Image,ImageDraw
r=Path(__file__).parent;c=json.loads((r/'reviewed-candidate.json').read_text(encoding='utf8'));proj='+proj=laea +lat_0=-2 +lon_0=118 +datum=WGS84 +units=m +no_defs';t=Transformer.from_crs('EPSG:4326',proj,always_xy=True);g=transform(t.transform,shape(c['geometry']));lo,la,hi,ha=g.bounds;mpp=10000000*.0254/96;w=math.ceil((hi-lo)/mpp)+40;h=math.ceil((ha-la)/mpp)+80;im=Image.new('RGB',(w,h),'white');dr=ImageDraw.Draw(im)
for p in g.geoms:
 for rg in[p.exterior,*p.interiors]:dr.line([(20+(x-lo)/mpp,40+(ha-y)/mpp)for x,y in rg.coords],fill='#176ab2',width=1)
dr.text((5,5),'Complete approved IDN + TLS union | 1975-1999 display proxy | No components omitted',fill='black');dr.text((5,h-20),'LAEA 118E/2S; nominal 1:10M at 96dpi; not physical screen calibration.',fill='black');im.save(r/'complete-modern-union-source-scale.png');(r/'projection-evidence.json').write_text(json.dumps({'definition':proj,'units':'metre','scaleDenominator':10000000,'dpi':96,'metresPerPixel':mpp,'width':w,'height':h},indent=2),encoding='utf8');print('Rendered complete union',w,h)
