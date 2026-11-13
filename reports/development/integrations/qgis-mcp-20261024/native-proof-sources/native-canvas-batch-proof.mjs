import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {runNativeBridge} from '../../tools/qgis/native-bridge.mjs';
const config=resolve('build-native/qgis/migration-current/qgis-config.json');
const input=resolve('build-native/qgis/migration-current/delete-proof.geojson');
const digest=()=>createHash('sha256').update(readFileSync(input)).digest('hex');
const before=digest(),call=(...args)=>runNativeBridge(['--config',config,...args]);
const opened=await call('open',input),id=opened.id;assert.equal(opened.crs,'EPSG:4326');
const initial=await call('edit-status','--layer',id);assert.equal(initial.editable,false);assert.equal(initial.owned,false);
const extent=await call('canvas-extent','--bounds','[14000000,4000000,14500000,4500000]','--source-crs','EPSG:3857');
assert.equal(extent.crs,'EPSG:4326');assert(extent.extent[0]>125&&extent.extent[2]<131);assert(extent.extent[1]>30&&extent.extent[3]<40);
const scale=await call('canvas-scale','--scale','2000000','--rotation','15');assert(Math.abs(scale.scale-2000000)<1);assert.equal(scale.rotation,15);
const canvas=await call('canvas');assert.equal(canvas.crs,'EPSG:4326');assert.equal(canvas.rotation,15);assert(Math.abs(canvas.scale-2000000)<1);
const page=await call('features','--layer',id,'--limit','2');assert.equal(page.features.length,2);
await call('begin-edit','--layer',id);
try{
  await call('set-attribute','--layer',id,'--fid',page.features[0].fid,'--field','name','--json','"trial"');
  const modified=await call('edit-status','--layer',id);assert.equal(modified.editable,true);assert.equal(modified.owned,true);assert.equal(modified.modified,true);
  assert.equal(modified.canUndo,true);assert.equal(modified.pending.changedAttributes,1);
  await call('undo-edit','--layer',id);const undone=await call('edit-status','--layer',id);assert.equal(undone.canRedo,true);
}finally{await call('rollback-edit','--layer',id);}
const closed=await call('edit-status','--layer',id);assert.equal(closed.editable,false);assert.equal(closed.owned,false);assert.equal(digest(),before);
await assert.rejects(call('canvas-extent','--bounds','[1,2,3,4]','--source-crs','NOT_A_CRS'),/CRS/i);
console.log(JSON.stringify({id,extent:extent.extent,scale:scale.scale,rotation:scale.rotation,sourceSha256:before,editing:'undo-and-rollback-verified'}));
