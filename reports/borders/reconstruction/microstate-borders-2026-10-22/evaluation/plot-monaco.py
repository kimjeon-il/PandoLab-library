import gzip,json
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,LineString
root=Path.cwd();stage=root/'build-native/lsib-supplement/monaco-review'
def polygon(mode):
 d=json.loads((stage/mode/'countries/state-MCO.json').read_text(encoding='utf-8'))
 return shape(next(v['geometry'] for v in d['geometryVersions'] if v['versionId']==d['metadata']['representativeGeometryVersionId']))
old,new=polygon('before'),polygon('staged')
c=json.loads((root/'build-native/lsib-supplement/monaco-candidate-final.json').read_text(encoding='utf-8'))
records=json.loads(gzip.decompress((root/'tools/historical-library/sources/lsib-11.4/boundaries.geojson.gz').read_bytes()))['features']
land=shape(next(f['geometry'] for f in records if f['properties']['ID']==c['boundaries'][0]['sourceLineIds'][0]))
points=list(new.exterior.coords);start,end=c['boundaries'][0]['segments'][0]['anchors'];a,b=points.index(tuple(start)),points.index(tuple(end))
paths=[points[a:b+1] if a<b else points[a:]+points[1:b+1],points[b:a+1] if b<a else points[b:]+points[1:a+1]]
border=min(paths,key=lambda p:LineString(p).hausdorff_distance(land));coast=max(paths,key=lambda p:LineString(p).hausdorff_distance(land))
image=Image.new('RGB',(1800,900),'white');draw=ImageDraw.Draw(image)
def font(size):return ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',size)
draw.text((45,20),'Monaco: current-reference boundary and coast correction',font=font(30),fill='#203345')
draw.text((45,64),'Normalized geometry comparison | 2026-10-22 | Equirectangular longitude/latitude',font=font(19),fill='#536673')
def panel(box,bounds):
 x0,y0,x1,y1=box;minx,miny,maxx,maxy=bounds;scale=min((x1-x0)/(maxx-minx),(y1-y0)/(maxy-miny))*.88
 cx,cy=(x0+x1)/2,(y0+y1)/2;mx,my=(minx+maxx)/2,(miny+maxy)/2
 draw.rectangle(box,fill='#e3eff4',outline='#b6c8d0',width=2)
 def project(seq):return [(cx+(x-mx)*scale,cy-(y-my)*scale) for x,y in seq]
 draw.text((x0+12,y1-30),f'{minx:.3f} to {maxx:.3f} E | {miny:.3f} to {maxy:.3f} N',font=font(16),fill='#526c79')
 return project
left=panel((45,145,865,750),old.bounds);right=panel((935,145,1755,750),new.bounds)
draw.text((60,110),'Previous and corrected country ownership',font=font(22),fill='#203345')
draw.text((950,110),'Corrected geometry, enlarged',font=font(22),fill='#203345')
draw.polygon(left(old.exterior.coords),fill='#a7b0b3',outline='#59696f')
draw.polygon(left(new.exterior.coords),fill='#f4bc4d',outline='#935f16')
draw.polygon(right(new.exterior.coords),fill='#f5d595')
draw.line(right(border),fill='#ab3b2d',width=4);draw.line(right(coast),fill='#166b9a',width=4)
draw.text((60,770),'Gray: previous Natural Earth polygon, 18.840 km2',font=font(21),fill='#59696f')
draw.text((60,804),'Gold: corrected Monaco polygon, 2.077 km2',font=font(21),fill='#935f16')
draw.text((950,770),'Red: LSIB border with shared coastal endpoints',font=font(21),fill='#ab3b2d')
draw.text((950,804),'Blue: IGN BD TOPO high-water coastline',font=font(21),fill='#166b9a')
draw.text((45,860),'Current-reference correction; not an independent historical-accuracy certification.',font=font(17),fill='#536673')
out=root/'reports/geography/images/monaco-geometry-comparison-2026-10-22.png';out.parent.mkdir(parents=True,exist_ok=True);image.save(out);print(out)
