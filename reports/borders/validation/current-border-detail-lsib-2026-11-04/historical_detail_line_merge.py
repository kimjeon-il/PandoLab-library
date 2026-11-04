from osgeo import ogr
def lines(g):
 if g.GetGeometryName() in ['LINESTRING','LINEARRING']:return [g.Clone()]
 return [l for i in range(g.GetGeometryCount()) for l in lines(g.GetGeometryRef(i))]
def merged(g):
 chains=[list(l.GetPoints() or []) for l in lines(g) if not l.IsEmpty()]
 changed=True
 while changed:
  changed=False
  for i in range(len(chains)):
   for j in range(i+1,len(chains)):
    a,b=chains[i],chains[j]
    if a[-1]==b[0]:c=a+b[1:]
    elif a[-1]==b[-1]:c=a+list(reversed(b))[1:]
    elif a[0]==b[-1]:c=b+a[1:]
    elif a[0]==b[0]:c=list(reversed(b))+a[1:]
    else:continue
    chains[i]=c;chains.pop(j);changed=True;break
   if changed:break
 result=[]
 for chain in chains:
  line=ogr.Geometry(ogr.wkbLineString)
  for p in chain:line.AddPoint_2D(p[0],p[1])
  result.append(line)
 return result
