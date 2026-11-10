import fs from 'node:fs';import {pathToFileURL} from 'node:url';import {spawnSync} from 'node:child_process';
const O=new URL('.',import.meta.url),root='D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109',m=await import(pathToFileURL(root+'/deu-c1-c2-c3-combined/source-review/review-inputs.mjs')),rev='2af6c0834ac2987a7ffdfe3cde0db1827b04d4e1',op=JSON.parse(fs.readFileSync(new URL('paired-coast-operation.json',O)));
const zipPath='tools/historical-library/sources/ussr-1922-approved/ussr-1922-v2-reviewed-master-20261023.zip',zip=m.archived(zipPath,rev),ne=JSON.parse(m.archived('assets/data/countries-ne-5.1.1.geojson',rev)).features.find(f=>f.id==='RUS');
const py=`import json,sys,base64,io,zipfile
x=json.load(sys.stdin);z=zipfile.ZipFile(io.BytesIO(base64.b64decode(x['zip'])));arc=x['arc'];out=[]
for name in ['geometry-v2/assembly/ussr-four-founders.normalized-provisional.geojson','geometry-v2/assembly/ussr-four-founders.display-10m-provisional.geojson']:
 for f in json.loads(z.read(name))['features']:
  if f['id'] not in ['state:soviet-union','state:soviet-union-russian-sfsr']:continue
  hits=[]
  for pi,p in enumerate(f['geometry']['coordinates']):
   for ri,r in enumerate(p):
    for i in range(len(r)-len(arc)+1):
     segment=r[i:i+len(arc)];rounded=[[round(a,6) for a in c] for c in segment]
     if segment==arc:hits.append({'span':[pi,ri,i,i+len(arc)-1],'mode':'exact-forward'})
     elif segment==arc[::-1]:hits.append({'span':[pi,ri,i,i+len(arc)-1],'mode':'exact-reverse'})
     elif rounded==arc:hits.append({'span':[pi,ri,i,i+len(arc)-1],'mode':'six-decimal-normalization-forward'})
     elif rounded==arc[::-1]:hits.append({'span':[pi,ri,i,i+len(arc)-1],'mode':'six-decimal-normalization-reverse'})
  assert len(hits)==1,(name,f['id'],hits)
  out.append({'entry':name,'entityId':f['id'],'uniqueOldArcCorrespondence':True,'match':hits[0]})
keys={tuple(round(a,6) for a in c) for p in x['ne']['coordinates'] for r in p for c in r};matches=[c for c in arc if tuple(c) in keys]
print(json.dumps({'originalMasterAndDisplay':out,'historicalArcVertexCount':len(arc),'verticesMatchingRawNERoundedToSixDecimals':len(matches),'rawNEProofRole':'Coordinate-lineage diagnostic only; not historical title proof or permission to clip old geometry.'}))`;
const r=spawnSync('C:/Users/taeeu/AppData/Local/Programs/Python/Python312/python.exe',['-X','utf8','-c',py],{input:JSON.stringify({zip:zip.toString('base64'),arc:op.oldCoordinates,ne:ne.geometry}),encoding:'utf8',maxBuffer:100000});if(r.status!==0)throw Error(r.stderr);const proof={revision:rev,originalArchivePath:zipPath,originalArchiveSha256:m.sha(zip),...JSON.parse(r.stdout),sourceWritten:false};fs.writeFileSync(new URL('original-source-lineage.json',O),JSON.stringify(proof,null,2)+'\n');console.log(JSON.stringify(proof));

