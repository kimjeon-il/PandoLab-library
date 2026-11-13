import fs from'node:fs';const p='build-native/territorial-recipe/historical-detail-measure.py';let s=fs.readFileSync(p,'utf8');s=s.replace('rows=[];sample=[]',`def merged(g):
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
rows=[];sample=[]`);s=s.replace("modern_parts=lines(features[left].Boundary().Intersection(features[right].Boundary()).Intersection(box))","modern_parts=merged(features[left].Boundary().Intersection(features[right].Boundary()))");s=s.replace("modern=max(modern_parts,key=lambda l:l.Length());historic=max(lines(historic.Intersection(box)),key=lambda l:l.Length())",`modern=max(modern_parts,key=lambda l:l.Length());historic=max(lines(historic.Intersection(box)),key=lambda l:l.Length())
 if modern.IsEmpty() or historic.IsEmpty():raise RuntimeError('Empty comparison chain '+name)
 menv=modern.GetEnvelope();extent=[min(extent[0],menv[0]-.15),min(extent[1],menv[2]-.15),max(extent[2],menv[1]+.15),max(extent[3],menv[3]+.15)]`);fs.writeFileSync(p,s);
