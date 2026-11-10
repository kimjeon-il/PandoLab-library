import json
from pathlib import Path
from shapely.geometry import shape,Polygon
from shapely.ops import unary_union
r=Path(__file__).parent;x=json.loads((r/'post-correction-archive-inputs.json').read_text(encoding='utf8'));audit=json.loads((r/'detailed-components.json').read_text(encoding='utf8'));vs=x['rec']['entity']['geometryVersions'];don=vs[-1]['geometry'];tls=x['tls']['entity']['geometryVersions'][-1]['geometry'];rows=[]
for vi in[0,2]:
 v=vs[vi];g=shape(v['geometry']);remaining=[]
 for q in audit['versions'][v['versionId']]['explicitOmissions']:
  p=(don if q['entityId']=='IDN'else tls)['coordinates'][q['index']];piece=Polygon(p[0],p[1:])
  if not piece.difference(g).is_empty:remaining.append(q['index'])
 assert not remaining;rows.append({'versionId':v['versionId'],'validFrom':v['validFrom'],'validTo':v['validTo'],'auditedExplicitOmissions':len(audit['versions'][v['versionId']]['explicitOmissions']),'remainingExplicitOmissions':len(remaining),'valid':g.is_valid})
g=shape(vs[2]['geometry']);baseline=unary_union([shape(don),shape(tls)]);assert g.symmetric_difference(baseline).is_empty;rows[1]['completeModernIDNPlusTLSUnionExactlyEqual']=True;rows[1]['symmetricDifferenceArea']=0;rows[0]['completeModernScopeEquivalence']='not yet certified; original West New Guinea exclusion membership research pending';out={'status':'passed post-archive correction verification','sourceRevision':x['sourceRevision'],'rows':rows};(r/'post-correction-verification.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out))
