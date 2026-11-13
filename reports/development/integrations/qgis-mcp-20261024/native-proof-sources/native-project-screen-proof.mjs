import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {runNativeBridge} from '../../tools/qgis/native-bridge.mjs';
import {decodeNativeImageBytes} from '../../tools/map-image/native-resample.mjs';

const config=resolve('build-native/qgis/migration-current/qgis-config.json');
const input=resolve('build-native/qgis/migration-current/delete-proof.geojson');
const digest=()=>createHash('sha256').update(readFileSync(input)).digest('hex');
const before=digest(),call=(...args)=>runNativeBridge(['--config',config,...args]);
const started=await call('start');assert.equal(started.transport,'pando-native-v1');
const project=await call('project');
const opened=project.layers.find(layer=>layer.name==='delete-proof')||await call('open',input);
await call('zoom-to-layer','--layer',opened.id);
try{
  const changed=await call('project-crs','--target-crs','EPSG:3857');assert.equal(changed.crs,'EPSG:3857');
  assert.equal((await call('project')).crs,'EPSG:3857');
  await assert.rejects(call('project-crs','--target-crs','NOT_A_CRS'),/CRS/i);
  assert.equal((await call('project')).crs,'EPSG:3857');
  const shot=await call('canvas-screenshot'),bytes=Buffer.from(shot.data,'base64');
  assert.equal(shot.mimeType,'image/png');assert(bytes.subarray(0,8).equals(Buffer.from('89504e470d0a1a0a','hex')));
  const image=await decodeNativeImageBytes({bytes,format:'png',maxPixels:16777216});
  assert(image.width>1&&image.height>1);
  const colors=new Set();for(let i=0;i<image.data.length;i+=4)colors.add(image.data.subarray(i,i+4).toString('hex'));
  assert(colors.size>1,'QGIS screenshot must contain rendered variation');
  assert.equal(digest(),before);
  console.log(JSON.stringify({crs:changed.crs,pngWidth:image.width,pngHeight:image.height,pngBytes:bytes.length,
    pngSha256:createHash('sha256').update(bytes).digest('hex'),colors:colors.size,pid:started.pid,sourceSha256:before}));
}finally{await call('project-crs','--target-crs','EPSG:4326');}
