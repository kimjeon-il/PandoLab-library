import json,pathlib,math
from PIL import Image,ImageDraw
from shapely.geometry import shape,Polygon
from shapely.ops import transform
from pyproj import Transformer
D=pathlib.Path('D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/europe-explicit-omission-audit-20261110')
fc=json.loads((D/'restoration-candidates.geojson').read_text(encoding='utf8'));manifest=json.loads((D/'restoration-manifest.json').read_text(encoding='utf8'));audit=json.loads((D/'audit-report.json').read_text(encoding='utf8'));ne=json.loads((D/'ne-comparison.geojson').read_text(encoding='utf8'));f=Transformer.from_crs('EPSG:4326','EPSG:3035',always_xy=True).transform
mpp=10000000*0.0254/96;rows=[]
for row in manifest['groups']:
 cand=next(x for x in fc['features']if x['id']==row['entityId'])['geometry'];before={'type':'MultiPolygon','coordinates':cand['coordinates'][:row['currentPolygonCount']]};a,b=transform(f,shape(before)),transform(f,shape(cand));restored=[transform(f,Polygon(x['coordinates'][0],x['coordinates'][1:]))for x in audit['components']if x['entityId']==row['entityId']]
 xmin,ymin,xmax,ymax=b.bounds;pad=50000;xmin-=pad;ymin-=pad;xmax+=pad;ymax+=pad;w=math.ceil((xmax-xmin)/mpp);h=math.ceil((ymax-ymin)/mpp);margin=30;top=70
 image=Image.new('RGB',(w*2+margin*3,h+top+margin),'white');draw=ImageDraw.Draw(image)
 draw.text((margin,12),row['entityId']+' | EPSG:3035 | nominal 1:10M at 96dpi',fill='black')
 draw.text((margin,30),'Gray: NE donor-country reference. Blue: historical display. Red: exact restored components.',fill='black')
 for i,(geom,title)in enumerate([(a,'Before'),(b,'Restored exact donor components')]):
  off=margin+i*(w+margin)
  point=lambda p:(off+(p[0]-xmin)/mpp,top+(ymax-p[1])/mpp)
  def paint(g,color,filled=False):
   for p in ([g] if g.geom_type=='Polygon' else g.geoms):
    xy=[point(z)for z in p.exterior.coords]
    if filled:draw.polygon(xy,fill=color)
    draw.line(xy,fill=color,width=1)
  donor=next(x for x in ne['features']if x['id']==row['donorEntityId'].replace('state:',''));paint(transform(f,shape(donor['geometry'])),'#bbbbbb');paint(geom,'#1e4e78')
  if i:
   for p in restored:paint(p,'#df3030',True)
  draw.text((off,top-20),title,fill='black');draw.rectangle([off,top,off+w,top+h],outline='#dddddd')
 name=('AH' if row['entityId']!='state:DEU' else 'DEU')+'-restoration-source-scale.png';image.save(D/name);rows.append({'entityId':row['entityId'],'image':name,'extentProjectedMetres':[xmin,ymin,xmax,ymax],'panelPixels':[w,h],'scaleDenominator':10000000,'dpi':96,'metresPerPixel':mpp,'restoredCount':len(restored)})
(D/'projection-execution.json').write_text(json.dumps({'definition':'EPSG:3035; always_xy longitude,latitude','units':'metre','rows':rows,'physicalDisplayScaleCalibrated':False,'limits':['Tiny restored polygons are subpixel in this nominal-scale image; coordinate identity and inclusion are verified geometrically, not certified by visual discernibility.']},indent=2)+'\n');print(json.dumps(rows))

