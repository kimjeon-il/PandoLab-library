"""Scoped in-memory Novaya Zemlya candidate measurements; run from Pando GIS worktree."""
import sys, json, io, base64, zipfile, hashlib
from pathlib import Path
from shapely.geometry import shape, Polygon, MultiPolygon, box
from shapely.ops import unary_union, transform
from shapely.validation import explain_validity
from pyproj import Transformer
from PIL import Image, ImageDraw, ImageFont

d=json.load(sys.stdin)
def canonical_ring(r):
    clean=[]
    for p in r:
        p=tuple(p)
        if not clean or p!=clean[-1]: clean.append(p)
    if clean and clean[0]==clean[-1]: clean.pop()
    forms=[]
    for a in [clean,list(reversed(clean))]:
        k=min(range(len(a)),key=lambda k:a[k]); forms.append(tuple(a[k:]+a[:k]))
    return min(forms)
def canonical_polygon(p): return (canonical_ring(p[0]),tuple(sorted(canonical_ring(r) for r in p[1:])))
window=Polygon(d['window'])
ps=lambda g:[Polygon(p[0],p[1:]) for p in g['coordinates']]
donors=ps(d['donor'])
selected=[i for i,p in enumerate(donors) if p.intersects(window)]
new=[donors[i] for i in selected]
new_union=unary_union(new)
out={'window':d['window'],'donorIndices':selected,'donorGroupBounds':list(new_union.bounds),'donorBoundaryCrossers':[i for i in selected if not window.contains(donors[i])], 'donorWindowBoundaryIntersections':[i for i,p in enumerate(donors) if p.intersects(window.boundary)], 'donorMinimumWindowBoundaryDistanceDegrees':min(p.distance(window.boundary) for p in donors),'newGroupValid':MultiPolygon(new).is_valid,'newGroupValidityReason':explain_validity(MultiPolygon(new)),'targets':[]}
original_group=None
for t in d['targets']:
    old_all=ps(t['geometry'])
    old_indices=[i for i,p in enumerate(old_all) if p.intersects(window)]
    old=[old_all[i] for i in old_indices]
    retained=[p for i,p in enumerate(old_all) if i not in old_indices]
    r_union=unary_union(retained)
    candidate=MultiPolygon(retained+new)
    inter=new_union.intersection(r_union)
    collisions=[i for i,p in enumerate(old_all) if i not in old_indices and p.intersects(new_union)]
    old_coords=[t['geometry']['coordinates'][i] for i in old_indices]
    if original_group is None: original_group=old_coords
    out['targets'].append({'id':t['id'],'oldIndices':old_indices,'sameOldAllRingsAsFirstTarget':old_coords==original_group,'oldBoundaryCrossers':[i for i in old_indices if not window.contains(old_all[i])],'oldWindowBoundaryIntersections':[i for i,p in enumerate(old_all) if p.intersects(window.boundary)],'oldGroupBounds':list(unary_union(old).bounds),'oldValid':MultiPolygon(old_all).is_valid,'candidateValid':candidate.is_valid,'candidateValidityReason':explain_validity(candidate),'retainedIntersectionEmpty':inter.is_empty,'retainedIntersectionAreaDegrees2':inter.area,'retainedIntersectionsIndices':collisions,'minimumNewToRetainedDistanceDegrees':new_union.distance(r_union),'minimumOldToRetainedDistanceDegrees':unary_union(old).distance(r_union),'afterPolygonCount':len(retained)+len(new),'candidateEqualsRetainedUnionCompleteDonorGroup':candidate.equals(unary_union([r_union,new_union])),'oldHoles':sum(len(p.interiors) for p in old),'newHoles':sum(len(p.interiors) for p in new)})

z=zipfile.ZipFile(io.BytesIO(base64.b64decode(d['originalZipBase64'])))
out['originalEvidence']={'entries':[],'matches':[]}
for name in ['geometry-v2/assembly/README.md','qa-v2/final-region-qa.json','geometry-v2/assembly/ussr-four-founders.normalized-provisional.geojson','geometry-v2/assembly/ussr-four-founders.display-10m-provisional.geojson']:
    b=z.read(name)
    out['originalEvidence']['entries'].append({'path':name,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    if name.endswith('.geojson'):
        f=json.loads(b)
        for feature in f['features']:
            if feature['geometry']['type']!='MultiPolygon': continue
            polys=ps(feature['geometry'])
            ii=[i for i,p in enumerate(polys) if p.intersects(window)]
            if ii:
                group=[feature['geometry']['coordinates'][i] for i in ii]
                matches=[[ii[j] for j,p in enumerate(group) if p==old] for old in original_group]
                topology_matches=[[ii[j] for j,p in enumerate(group) if Polygon(p[0],p[1:]).equals(Polygon(old[0],old[1:]))] for old in original_group]
                normalized_matches=[[ii[j] for j,p in enumerate(group) if canonical_polygon(p)==canonical_polygon(old)] for old in original_group]
                diagnostics=[]
                for old in original_group:
                    op=Polygon(old[0],old[1:]); j=min(range(len(group)),key=lambda j:op.hausdorff_distance(Polygon(group[j][0],group[j][1:])))
                    pp=Polygon(group[j][0],group[j][1:])
                    old_points={tuple(p) for r in old for p in r}; original_points={tuple(p) for r in group[j] for p in r}
                    diagnostics.append({'originalIndex':ii[j],'oldVertices':sum(len(r) for r in old),'originalVertices':sum(len(r) for r in group[j]),'oldFirstTwo':old[0][:2],'originalFirstTwo':group[j][0][:2],'onlyOriginalCoordinates':sorted(original_points-old_points),'onlyCurrentCoordinates':sorted(old_points-original_points),'hausdorffDistanceDegrees':op.hausdorff_distance(pp),'symmetricDifferenceAreaDegrees2':op.symmetric_difference(pp).area})
                out['originalEvidence']['matches'].append({'file':name,'id':feature.get('id'),'properties':feature.get('properties'),'indices':ii,'oldGroupSameOrder':original_group==group,'exactOriginalIndicesPerCurrentComponent':matches,'oldGroupAllRingsExact':len(group)==len(original_group) and all(len(m)==1 for m in matches),'topologicallyEqualOriginalIndicesPerCurrentComponent':topology_matches,'oldGroupTopologicallyEqual':len(group)==len(original_group) and all(len(m)==1 for m in topology_matches),'normalizationEquivalentOriginalIndicesPerCurrentComponent':normalized_matches,'oldGroupCoordinatesEqualAfterRingRotationReversalAndConsecutiveDuplicateRemoval':len(group)==len(original_group) and all(len(m)==1 for m in normalized_matches),'diagnostics':diagnostics})

# A single matched extent/projection view, without modifying source coordinates.
proj=Transformer.from_crs('EPSG:4326','+proj=laea +lat_0=74 +lon_0=60 +datum=WGS84 +units=m +no_defs',always_xy=True).transform
wb=transform(proj,window).bounds
W,H=1500,1100; pad=70; sx=(W-2*pad)/(wb[2]-wb[0]); sy=(H-170)/(wb[3]-wb[1]); scale=min(sx,sy)
xy=lambda a:(int(pad+(a[0]-wb[0])*scale),int(100+(wb[3]-a[1])*scale))
im=Image.new('RGB',(W,H),'#eff6fa');draw=ImageDraw.Draw(im)
try: font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',23);small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
except OSError: font=small=ImageFont.load_default()
draw.text((30,20),'Novaya Zemlya: complete group candidate | 1922-1929 source review',fill='#172f46',font=font)
draw.text((30,53),'Approved modern: 757 polygons (blue) | Existing: 6 polygons (orange) | Water-only selection perimeter (gray)',fill='#172f46',font=small)
for p in donors:
    if p.intersects(box(48,69,72,78)):
        for r in [p.exterior]+list(p.interiors):
            pts=[xy(proj(x,y)) for x,y in r.coords]
            draw.line(pts,fill='#a7b8c3',width=1)
for p in new:
    for r in [p.exterior]+list(p.interiors): draw.line([xy(proj(x,y)) for x,y in r.coords],fill='#1668a8',width=2)
for p in [Polygon(p[0],p[1:]) for p in original_group]:
    for r in [p.exterior]+list(p.interiors): draw.line([xy(proj(x,y)) for x,y in r.coords],fill='#d27425',width=1)
draw.line([xy(proj(x,y)) for x,y in window.exterior.coords],fill='#646e7c',width=2)
draw.text((30,H-55),'Same Lambert azimuthal equal-area projection and extent. Visual review is not historical positional validation.',fill='#172f46',font=small)
png=Path(__file__).with_name('whole-group-overlay.png');im.save(png)
out['visual']={'file':png.name,'projection':'LAEA centered 74N 60E','sha256':hashlib.sha256(png.read_bytes()).hexdigest(),'bytes':png.stat().st_size,'purpose':'Matched-extent overview and complete-group retrieval review; not cadastral/historical coast measurement.'}
ne_all=ps(d['ne']); ne_indices=[i for i,p in enumerate(ne_all) if p.intersects(window)]; ne_group=[ne_all[i] for i in ne_indices]
old_group=[Polygon(p[0],p[1:]) for p in original_group]
old_projected=transform(proj,unary_union(old_group));new_projected=transform(proj,new_union);ne_projected=transform(proj,unary_union(ne_group))
definition='+proj=laea +lat_0=74 +lon_0=60 +datum=WGS84 +units=m +no_defs'
projection={'definition':definition,'units':'metre','scaleDenominator':10000000,'dpi':300,'metresPerPixel':10000000*0.0254/300,'geographicComparisonExtent':list(unary_union([unary_union(old_group),new_union,unary_union(ne_group)]).bounds),'actualExecution':'pyproj Transformer.from_crs(EPSG:4326, definition, always_xy=True); shapely.ops.transform','oldProjectedAreaKm2':old_projected.area/1e6,'donorProjectedAreaKm2':new_projected.area/1e6,'rawNaturalEarthGroupIndices':ne_indices,'rawNaturalEarthGroupEqualsOld':ne_projected.equals(old_projected),'screenPhysicalScaleCalibrated':False,'purpose':'Nominal 1:10M display reference comparison, not historical accuracy or territorial change measurement.'}
metres_per_pixel=projection['metresPerPixel']; bb=unary_union([old_projected,new_projected,ne_projected]).bounds; margin=32; pw=int((bb[2]-bb[0])/metres_per_pixel)+2*margin;ph=int((bb[3]-bb[1])/metres_per_pixel)+2*margin
nom=Image.new('RGB',(pw*3,ph+120),'#f4f8fb');dd=ImageDraw.Draw(nom)
for panel,(title,polys,color) in enumerate([('Existing historical display',old_group,'#d27425'),('Approved modern: all 757',new,'#1668a8'),('Raw Natural Earth reference',ne_group,'#597867')]):
    dd.text((panel*pw+20,15),title,fill='#172f46',font=small)
    for poly in polys:
        pp=transform(proj,poly)
        for r in [pp.exterior]+list(pp.interiors):
            pts=[(int(panel*pw+margin+(x-bb[0])/metres_per_pixel),int(50+margin+(bb[3]-y)/metres_per_pixel)) for x,y in r.coords]
            dd.line(pts,fill=color,width=1)
dd.text((20,ph+70),'Nominal 1:10,000,000 at 300 dpi; same LAEA projection and extent. Not physical-screen calibrated.',fill='#172f46',font=small)
sp=Path(__file__).with_name('nominal-source-scale.png');nom.save(sp,dpi=(300,300));projection['image']={'file':sp.name,'sha256':hashlib.sha256(sp.read_bytes()).hexdigest(),'bytes':sp.stat().st_size,'dimensions':[pw*3,ph+120]}
Path(__file__).with_name('projection-evidence.json').write_text(json.dumps(projection,indent=2)+'\n',encoding='utf-8');out['projection']=projection
print(json.dumps(out))
