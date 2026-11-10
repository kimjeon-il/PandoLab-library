import json
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from pyproj import Transformer
P=Path(__file__).parent;x=json.loads((P/'inputs.json').read_text(encoding='utf-8'));c=json.loads((P/'safe-coast-candidates.geojson').read_text(encoding='utf-8'));cert=json.loads((P/'intersection-certificates.json').read_text(encoding='utf-8'));proj='+proj=laea +lat_0=32 +lon_0=54 +datum=WGS84 +units=m +no_defs';tr=Transformer.from_crs('EPSG:4326',proj,always_xy=True);font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17);small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',14)
def rings(g):return[r for p in (g['coordinates'] if g['type']=='MultiPolygon' else[g['coordinates']]) for r in p]
def render(name,center,mpp,size,title,notes,neighbors=False):
 im=Image.new('RGB',size,'white');dr=ImageDraw.Draw(im);cx,cy=tr.transform(*center)
 def px(p):
  X,Y=tr.transform(*p);return(size[0]/2+(X-cx)/mpp,(size[1]-220)/2+80-(Y-cy)/mpp)
 def draw(g,col,w=1):
  for r in rings(g):dr.line([px(p) for p in r],fill=col,width=w)
 if neighbors:
  for p in x['peers']:
   if p['id'] in ['IRQ','PAK']:draw(p['entity']['geometryVersions'][-1]['geometry'],'#b9c0c8')
 draw(x['donor']['geometry'],'#bcc3cc');draw(x['irn']['entity']['geometryVersions'][2]['geometry'],'#d76a61',2 if neighbors else 1);draw(c['features'][1]['geometry'],'#176db2',2 if neighbors else 1)
 dr.text((20,15),title,font=font,fill='#202d3b');dr.text((20,45),'Blue: safe candidate | Red: original source | Gray: modern donor context',font=small,fill='#303f4d')
 if neighbors:
  for q in cert['intersections']:
   X,Y=px(q['computedIntersection']);dr.ellipse((X-5,Y-5,X+5,Y+5),fill='black')
 dr.rectangle((10,size[1]-170,size[0]-10,size[1]-10),fill='#f2f4f7')
 for i,n in enumerate(notes):dr.text((20,size[1]-160+i*25),n,font=small,fill='#303f4d')
 im.save(P/name,dpi=(100,100))
render('IRN-safe-coast-10m.png',(54,32),2540,(1100,1200),'IRN 1922-12-30: source-preserving coast candidate',['1:10,000,000 at 100 dpi; same LAEA projection for all three layers.','184 entire donor components plus original Abu Musa and two Caspian components.','Farsi and both Tunbs remain absent. No political ownership change.','Caspian, Atrek, original land boundaries and political coastal contacts are preserved.','Two calculated in-segment intersections; no arbitrary straight connectors.'])
render('IRN-west-join-diagnostic.png',(48.57,29.96),100,(1000,800),'Western intersection and retained original political endpoint',['Diagnostic enlargement only; not a new historical scale requirement.','Black point: calculated intersection, not a political boundary relocation.','Original endpoint and coastal run remain red/blue coincident to that point.','Current IRQ outline is date-effective stored context; pre-existing mismatch is unchanged.'],True)
render('IRN-east-join-diagnostic.png',(61.58,25.21),50,(1000,800),'Eastern intersection and retained original political endpoint',['Diagnostic enlargement only; not a new historical scale requirement.','Black point: calculated intersection. Source political/coastal contact remains unchanged.','PAK is modern donor-only context, not an asserted 1922 counterpart.','No local British India/Raj source found; no substitute historical geometry invented.'],True)
(P/'projection-execution.json').write_text(json.dumps({'projection':proj,'units':'metre','nominalSourceScale':10000000,'outputDpi':100,'metresPerPixelAtSourceScale':2540,'sourceScaleImage':'IRN-safe-coast-10m.png','diagnostics':{'IRN-west-join-diagnostic.png':100,'IRN-east-join-diagnostic.png':50},'sameInputsInAllPanels':True,'threeVersionsShareIdenticalCoastalOperation':True}),encoding='utf-8')
print('Rendered source scale and two splice diagnostics')
