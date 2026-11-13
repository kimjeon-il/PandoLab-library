import {createHash} from 'node:crypto';
import {writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const {fetchBoundedBytes}=await import(pathToFileURL(resolve('tools/gis/bounded-source-json.mjs')));
const base='https://spatial.planning.vic.gov.au/server/rest/services/yarra_river_land/MapServer/0/query';
const params=new URLSearchParams({where:'1=1',outFields:'OBJECTID_1,NAME',returnGeometry:'true',outSR:'4326',f:'geojson'});
const bytes=await fetchBoundedBytes(base+'?'+params,{timeoutMs:90000,limit:24000000,
  headers:{'User-Agent':'PandoLab-independent-geometry-research/1.0',Accept:'application/geo+json,application/json'}});
if(!bytes.length)throw Error('Empty government GeoJSON');
const data=JSON.parse(bytes.toString('utf8'));if(data.error||data.type!=='FeatureCollection')throw Error('Invalid official response');
const hash=createHash('sha256').update(bytes).digest('hex');
const output=resolve('build-native/hydro-point-screen/real-proof-92B7wp/yarra-reference.geojson');writeFileSync(output,bytes,{flag:'wx'});
console.log(JSON.stringify({output,bytes:bytes.length,sha256:hash,matchesPreservedReceipt:hash==='70a2b0c84e9094258c64514d1392f7ef712fbaa7312754a7b80296e3dbb50fb6'}));
