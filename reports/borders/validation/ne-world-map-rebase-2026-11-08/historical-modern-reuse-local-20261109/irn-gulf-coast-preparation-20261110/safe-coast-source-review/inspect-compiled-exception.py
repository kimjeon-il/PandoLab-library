import json,subprocess
from pathlib import Path
from shapely.geometry import shape
P=Path(__file__).parent
helper=(P.parent.parent/'deu-c1-c2-c3-combined/source-review/review-inputs.mjs').as_uri()
code="""import * as m from '%s';import {readBuiltinCountry} from 'file:///D:/dev/PandoLab/tools/data/builtin-country-bytes.mjs';const rev='46e6d5c9451fb137717987483428c441051c19a5',prior='7a307819c680fdb221d19cf18d49e12daebefdfa',base='assets/data/builtin-world/generated/v1/',i=JSON.parse(m.archived(base+'index.json',rev)),e=i.entities.find(e=>e.entityId==='IRN'),c=readBuiltinCountry(e,i,f=>m.archived(base+f,rev)),id='state:IRN:natural-earth-5.1.1:caspian-1922-12-30',b=c.sourceBindings.find(b=>b.sourceVersionId===id),g=c.geometries.find(g=>g.id===b.geometryRef.id&&g.version===b.geometryRef.version),old=m.entity('IRN',prior).entity.geometryVersions.find(v=>v.versionId===id).geometry,now=m.entity('IRN',rev).entity.geometryVersions.find(v=>v.versionId===id).geometry;console.log(JSON.stringify({before:old,after:now,compiled:g.geojson}));""" % helper
r=subprocess.run(['node','--input-type=module','-e',code],cwd='D:/dev/PandoLab',capture_output=True,text=True,check=True)
x=json.loads(r.stdout);s,c,n=[shape(x[k]) for k in ['before','compiled','after']]
removed=s.difference(c);added=c.difference(s);exception=s.symmetric_difference(c);coast=s.symmetric_difference(n)
def info(g):
 return {'empty':g.is_empty,'type':g.geom_type,'bounds':list(g.bounds) if not g.is_empty else None,'areaSquareDegrees':g.area,'components':[{'bounds':list(q.bounds),'areaSquareDegrees':q.area} for q in (list(g.geoms) if hasattr(g,'geoms') else ([g] if not g.is_empty else []))]}
out={'status':'read-only-existing-compiled-exception-footprint','dataRevision':'46e6d5c9451fb137717987483428c441051c19a5','sourcePreimageRevision':'7a307819c680fdb221d19cf18d49e12daebefdfa','versionId':'state:IRN:natural-earth-5.1.1:caspian-1922-12-30','sourceMinusCompiled':info(removed),'compiledMinusSource':info(added),'existingException':info(exception),'newSafeCoastDelta':info(coast),'exceptionIntersectionWithNewCoastDeltaSquareDegrees':exception.intersection(coast).area,'geometriesDisjoint':exception.disjoint(coast),'generatedCandidate':False,'canonicalWrites':False}
p=P/'compiled-exception-footprint.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');assert json.loads(p.read_text(encoding='utf-8'))==out
print(json.dumps({k:v for k,v in out.items() if k!='newSafeCoastDelta'},indent=2))
