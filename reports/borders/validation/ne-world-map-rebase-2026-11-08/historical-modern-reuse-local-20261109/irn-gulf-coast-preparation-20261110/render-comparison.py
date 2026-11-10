import json,math
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from pyproj import Transformer
P=Path(__file__).parent;x=json.loads((P/'inputs.json').read_text(encoding='utf-8'));can=json.loads((P/'gulf-coast-historical-scope-candidates.geojson').read_text(encoding='utf-8'));q=Transformer.from_crs('EPSG:4326','+proj=laea +lat_0=32 +lon_0=54 +datum=WGS84 +units=m +no_defs',always_xy=True)
im=Image.new('RGB',(1100,1200),'white');dr=ImageDraw.Draw(im);font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17);small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',14)
mpp=2540.0;center=q.transform(54,32)
def px(a):
 X,Y=q.transform(*a);return(550+(X-center[0])/mpp,500-(Y-center[1])/mpp)
def poly(g,color,w=1):
 for p in g['coordinates']:
  for r in p:dr.line([px(a) for a in r],fill=color,width=w)
poly(x['donor']['geometry'],'#c5cbd2');poly(x['irn']['entity']['geometryVersions'][2]['geometry'],'#dc665b');poly(can['features'][1]['geometry'],'#1b75b9')
for i,name in {85:'85 Farsi: ownership unresolved',114:'114 Abu Musa: political difference',117:'117 Little Tunb',118:'118 Greater Tunb'}.items():
 r=x['donor']['geometry']['coordinates'][i][0];pt=px(r[0]);dr.ellipse((pt[0]-5,pt[1]-5,pt[0]+5,pt[1]+5),outline='#c07800',width=2)
for text,y in [('IRN 1922-12-30: preparatory southern-coast candidate',20),('Blue: candidate | Red: existing source | Gray: full modern donor | Orange: political holds',50),('LAEA 54E 32N, 1:10,000,000 at 100 dpi; all polygons retained without a size cutoff',80)]:dr.text((25,y),text,fill='#20232a',font=font)
dr.rectangle((20,910,1080,1180),fill='#f4f6f9')
notes=['All three 1922-1929 candidates keep the original mainland land-border coordinates.','Caspian shoreline, Atrek and both separate Caspian components remain coordinate-exact.','184 entire detached modern components included; 4 islands isolated on political evidence.','Candidate is not a full mainland-border rebase and is not ready for source adoption.','849 m western and 174 m eastern geometric splice joins need paired endpoint review.','Existing NE political boundaries are not certified as historical. Full rebase remains a paired task.','1932 Turkey changes and compiled-only western exception must remain distinct from coast detail.']
for n,t in enumerate(notes):dr.text((35,930+n*30),t,fill='#303945',font=small)
im.save(P/'IRN-preparatory-coast-comparison.png',dpi=(100,100));print('Saved comparison PNG')
