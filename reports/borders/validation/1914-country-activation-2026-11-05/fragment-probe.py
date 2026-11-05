exec(open('verify-compiled.py',encoding='utf-8-sig').read().split('rows=[]')[0])
def polys(z):return [z.GetGeometryRef(i).Clone()for i in range(z.GetGeometryCount())]if z.GetGeometryName()=='MULTIPOLYGON'else[z]
frags=[]
for c in after:
 old=next((r for r in before if r['entityId']==c['entityId']),None)
 if old is None:continue
 for day in ['1914-07-28','1914-07-31']:
  if c['entityId']=='DEU' and day=='1914-07-31':continue
  a,b=rowgeom(old,day),rowgeom(c,day)
  if a is None or b is None:continue
  pa,pb=polys(g(a)),polys(g(b));groups={}
  for p in pb:
   pt=p.PointOnSurface();matches=[i for i,q in enumerate(pa)if q.Intersects(pt)];assert matches,(c['entityId'],day);groups.setdefault(matches[0],[]).append(p)
  for i,ps in groups.items():
   if len(ps)<2:continue
   for p in sorted(ps,key=area)[:-1]:frags.append({'entityId':c['entityId'],'date':day,'originalComponent':i,'areaKm2':area(p),'geometry':json.loads(p.ExportToJson())})
Path('compiled-fragments.json').write_text(json.dumps(frags));print([(r['entityId'],r['date'],r['areaKm2'])for r in frags])

