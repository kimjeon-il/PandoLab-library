import struct,hashlib,json
from pathlib import Path
from shapely.geometry import shape
B=Path(__file__).parent
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def canon(p):
 rings=[]
 for ring in p:
  pts=[struct.pack('>dd',float(x),float(y)) for x,y in ring]
  if pts[-1]==pts[0]:pts.pop()
  candidates=[]
  for seq in (pts,list(reversed(pts))):candidates.extend(b''.join(seq[i:]+seq[:i]) for i in range(len(seq)))
  rings.append(struct.pack('>I',len(pts))+min(candidates))
 return b'POLY64v1\0'+struct.pack('>I',len(rings))+rings[0]+b''.join(sorted(rings[1:]))
def digest(p):return hashlib.sha256(canon(p)).hexdigest()
expected=['06fe4cdf5e3c9f6750e645616e2991d91e1ca3007000b347b1d74a0481e9eb6f','b244a5af57b2e37f3d22fb66072f41c36f10b38acd486401712169c88f2b4887','9423117d04581ed45cd1ae4e1aa139cb6d76ca866356e01b2db4a2479fc60279','3853871252d3d781575cce1a0964f533e8a1ca32dbc0dc5d2dc153d4d3149b7a','4481f70bfda3982f24e9ddf4960f7e30950c5f2c2477a2275e89fc11635c2429','4c5308f0608acfdbad7bb80574431e6c3d91b61dd38e1e1d517d4b9744ed44be','c3885c2d4d5f3754b5bfb3e30de4847ee8e33be24bfbec6aff1e9f9889537d64','1ef7a6d62833668fe83c15a84b007a10db7a8201f3cf230f4fa1c22f66f20358','7ca124bdddeef270965377f74dcaf3cbf333dfaaacb7e20b6edefd5cc0e6677f','a3f674f98d519640626b96f6da57b27e1ef24912217067eaf2cac167c3ccf062']
original=json.loads((B/'original-ten-exact.geojson').read_text(encoding='utf-8-sig'));current=json.loads((B/'scoped-island-input.json').read_text(encoding='utf-8'));binding_file='canonical-binding-'+current['revision'][:8]+'.json';binding=json.loads((B/binding_file).read_text(encoding='utf-8'));owners=['VNM','VNM','VNM','PHL','VNM','PHL','PHL','CHN','TWN','PHL'];fs={f['id']:f for f in current['features'] if f['id'] in owners};gs={k:shape(f['geometry']) for k,f in fs.items()};rows=[]
for i,p in enumerate(original['coordinates']):
 h=digest(p);assert h==expected[i],(i,h);matches=[];g=shape({'type':'Polygon','coordinates':p});relations=[]
 for id,f in fs.items():
  for j,q in enumerate(f['geometry']['coordinates']):
   if len(q)==len(p) and sorted(map(len,q))==sorted(map(len,p)) and digest(q)==h:matches.append({'recipient':id,'componentIndex':j})
  relations.append({'recipient':id,'missingAreaDegrees2':g.difference(gs[id]).area,'intersectionAreaDegrees2':g.intersection(gs[id]).area,'covers':bool(gs[id].covers(g))})
 rows.append({'originalComponentIndex':i,'approvedRecipient':owners[i],'originalPOLY64v1Sha256':h,'exactMatches':matches,'assignedExactlyOnceAndNoOtherRecipient':len(matches)==1 and matches[0]['recipient']==owners[i],'geometryRelations':relations})
out={'status':'pass' if all(r['assignedExactlyOnceAndNoOtherRecipient'] for r in rows) else 'blocked-exact-component-mismatch','sourceRevision':current['revision'],'originalSource':{'verifiedBy':'/root/list_historical_ne/verify_original_island_components','libraryFileId':'libfile_2c333ee9a7588191a7e870c5ae42c89a','zipSha256':'8f551d2663bd9466099f4cc86470f7980fd265e6390e40c22b2de4cbf78b9ffd','gpkgSha256':'903802ac3af29e071a608f27a3c1ca67372d38dba2125f8325b9569f454f519d','gpkgBytes':35311616,'fid':270,'WP_ID':'4ac4f563-db48-4b0a-a528-e45d1dc047d4','transfer':'Exact original10 coordinates and independent binary64 hashes delivered from verified cloud source, not successful Windows materialization.'},'inputHashes':{n:H(B/n) for n in ['original-ten-exact.geojson','scoped-island-input.json',binding_file,'check-original-ten.py']},'canonicalSourceRefs':[r for r in binding['rows'] if r['entityId'].split(':')[1] in owners],'algorithm':'POLY64v1: big-endian IEEE754 double XY; rotation/orientation-invariant closed-ring encoding, length framing, sorted holes, SHA256. No rounding, tolerance, snap or geometry repair.','rows':rows,'historicalOrSovereigntyClaimsAdded':False,'currentEffectiveControlOnly':True,'runtimeRetirementApproved':False}
(B/'original-ten-canonical-proof.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'rows':[{'index':r['originalComponentIndex'],'matches':r['exactMatches'],'pass':r['assignedExactlyOnceAndNoOtherRecipient']} for r in rows],'proofSha256':H(B/'original-ten-canonical-proof.json')}))
