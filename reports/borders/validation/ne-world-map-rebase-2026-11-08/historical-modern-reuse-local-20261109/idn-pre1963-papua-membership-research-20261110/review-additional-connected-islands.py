from pathlib import Path
import json,hashlib,math
from collections import defaultdict
from shapely.geometry import Polygon,shape,box
from shapely.ops import transform
from shapely.strtree import STRtree
from pyproj import Transformer
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).parent;out=r/'additional-connected-islands-review';out.mkdir(exist_ok=True)
load=lambda p:json.loads(p.read_text(encoding='utf8'))
fixed=load(r/'fixed-idn-input.json');C=load(r/'reviewed-candidate.json')['geometry']['coordinates'];oldC=fixed['entity']['geometryVersions'][0]['geometry']['coordinates'];D=fixed['entity']['geometryVersions'][-1]['geometry']['coordinates'];DP=[Polygon(p[0],p[1:])for p in D];tree=STRtree(DP)
pyh=lambda p:hashlib.sha256(json.dumps(p,separators=(',',':')).encode()).hexdigest();byHash={pyh(p):i for i,p in enumerate(C)}
groups=[q['group']for q in load(r/'named-landmass-subset.json')['pending']if q['reasons']==['no-official-island-name-point-in-all-three']];assert len(groups)==26
byNE=defaultdict(list)
for b in load(r/'official-landmass-anchors.json'):
 for i in {x['NEIndex']for x in b['anchorHits']}:byNE[i].append(b)
bySource=defaultdict(set)
for line in(r/'public-component-correspondence.jsonl').read_text().splitlines():
 q=json.loads(line)
 for h in q['sourceHits']:bySource[(h['sourceFile'],h['polygonIndex'])].add(q['modernIndex'])
def xy(c):return c[:2]if isinstance(c[0],(int,float))else[xy(v)for v in c]
sources={}
for f in(r/'public-sources').glob('big-province-*.geojson'):
 g=load(f)['features'][0]['geometry'];s=shape({'type':g['type'],'coordinates':xy(g['coordinates'])});sources[f.name]=[s]if s.geom_type=='Polygon'else list(s.geoms)
definition='+proj=laea +lat_0=-2 +lon_0=118 +datum=WGS84 +units=m +no_defs';tf=Transformer.from_crs('EPSG:4326',definition,always_xy=True).transform
records=[];render=[]
for q in groups:
 ni=q['originalNEIndices'][0];di=q['modernDonorIndices'][0];oldi=q['currentIndices'][0];ci=byHash[pyh(oldC[oldi])];a=byNE[ni];assert len(a)==1;b=a[0];key=(b['sourceFile'],b['sourcePolygonIndex']);official=sources[key[0]][key[1]]
 assert {x['NEIndex']for x in b['anchorHits']}=={ni}and bySource[key]=={di}and b['classification']=='IDN-retained'
 og=Polygon(C[ci][0],C[ci][1:]);dg=DP[di];om=transform(tf,og);dm=transform(tf,dg);bm=transform(tf,official)
 bounds=[min(z.bounds[0]for z in[og,dg,official]),min(z.bounds[1]for z in[og,dg,official]),max(z.bounds[2]for z in[og,dg,official]),max(z.bounds[3]for z in[og,dg,official])]
 padding=max(bounds[2]-bounds[0],bounds[3]-bounds[1])*.12;extent=box(bounds[0]-padding,bounds[1]-padding,bounds[2]+padding,bounds[3]+padding)
 nearby=[int(j)for j in tree.query(extent)if j!=di and DP[j].intersects(extent)]
 record={'originalNEIndex':ni,'preSixCurrentIndex':oldi,'currentIndex':ci,'modernIndex':di,'sourceRevision':load(out/'current-source-binding.json')['sourceRevision'],'oldCoordinateHash':pyh(C[ci]),'donorCoordinateHash':pyh(D[di]),'officialConnectedLandmass':b,'allModernDonorsIntersectingEntireOfficialLandmass':sorted(bySource[key]),'oneToOneClosure':True,'oldBounds':list(og.bounds),'donorBounds':list(dg.bounds),'officialBounds':list(official.bounds),'oldAreaKm2':om.area/1e6,'donorAreaKm2':dm.area/1e6,'officialAreaKm2':bm.area/1e6,'donorCoveredByOfficialFraction':dm.intersection(bm).area/dm.area,'officialCoveredByDonorFraction':dm.intersection(bm).area/bm.area,'oldCoveredByOfficialFraction':om.intersection(bm).area/om.area,'officialCoveredByOldFraction':om.intersection(bm).area/bm.area,'symmetricDifferenceOldModernKm2':om.symmetric_difference(dm).area/1e6,'nearbyModernInDisplayExtentOnly':nearby,'displayPaddingFraction':.12,'displayPaddingIsNotMembershipRule':True,'status':'Awaiting individual visual review; no automatic threshold classifier; source unchanged'}
 records.append(record);render.append((record,om,dm,bm,[transform(tf,DP[j])for j in nearby]))
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',19);small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',15);title=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',25)
files=[]
for page in range(math.ceil(len(render)/4)):
 im=Image.new('RGB',(1500,1400),'white');draw=ImageDraw.Draw(im);draw.text((25,15),'Additional 1:1 connected islands: individual review required',fill='#111827',font=title);draw.text((25,53),'Grey full BIG land | Red old NE | Blue whole modern donor | Orange other nearby modern components',fill='#475569',font=font)
 for slot,(q,o,d,b,near)in enumerate(render[page*4:page*4+4]):
  x0=750*(slot%2);y0=100+640*(slot//2);allg=[o,d,b];xmin=min(z.bounds[0]for z in allg);ymin=min(z.bounds[1]for z in allg);xmax=max(z.bounds[2]for z in allg);ymax=max(z.bounds[3]for z in allg);width=xmax-xmin;height=ymax-ymin;sc=min(650/width,450/height)*.86;cx=(xmin+xmax)/2;cy=(ymin+ymax)/2
  def px(coords):return[(x0+375+(x-cx)*sc,y0+260-(y-cy)*sc)for x,y in coords]
  # Draw on a clipped panel, so neighboring shapes never obscure another group.
  pane=Image.new('RGB',(750,520),'white');pd=ImageDraw.Draw(pane)
  def local(coords):return[(x-x0,y-y0)for x,y in px(coords)]
  pd.polygon(local(b.exterior.coords),fill='#d1d5db')
  for h in b.interiors:pd.polygon(local(h.coords),fill='white')
  for g in near:pd.line(local(g.exterior.coords),fill='#d97706',width=2)
  for g,color in[(o,'#dc2626'),(d,'#0369a1')]:
   pd.line(local(g.exterior.coords),fill=color,width=3)
   for h in g.interiors:pd.line(local(h.coords),fill=color,width=3)
  im.paste(pane,(x0,y0));draw.text((x0+25,y0+530),f"NE {q['originalNEIndex']} / modern {q['modernIndex']} / current {q['currentIndex']}",fill='#111827',font=font)
  draw.text((x0+25,y0+558),f"Old {q['oldAreaKm2']:.2f} | donor {q['donorAreaKm2']:.2f} | official {q['officialAreaKm2']:.2f} km2",fill='#475569',font=small)
  draw.text((x0+25,y0+580),f"Donor/official mutual area coverage: {100*q['donorCoveredByOfficialFraction']:.2f}% / {100*q['officialCoveredByDonorFraction']:.2f}%",fill='#475569',font=small)
  draw.text((x0+25,y0+602),f"Location: {(q['donorBounds'][0]+q['donorBounds'][2])/2:.4f} E, {(q['donorBounds'][1]+q['donorBounds'][3])/2:.4f} N",fill='#475569',font=small)
 f=out/f'connected-islands-{page+1:02}.png';im.save(f);files.append(f.name)
data={'status':'26 individual reviews pending; no source changes','sourceBinding':'current-source-binding.json','projection':{'definition':definition,'units':'metre','executed':True},'areaStatisticsUse':'Diagnostic only. No area or proximity threshold accepts or omits any component.','sheets':files,'groups':records};f=out/'connected-island-review-inputs.json';f.write_text(json.dumps(data,indent=2)+'\n');assert load(f)==data
print(json.dumps({'groups':len(records),'sheets':files,'rows':[{k:q[k]for k in['originalNEIndex','modernIndex','oldAreaKm2','donorAreaKm2','officialAreaKm2','donorCoveredByOfficialFraction','officialCoveredByDonorFraction','nearbyModernInDisplayExtentOnly']}for q in records]}))
