import assert from 'node:assert/strict';
import {copyFileSync,mkdtempSync,readFileSync} from 'node:fs';
import {join,resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const {runNativeBridge}=await import(pathToFileURL(resolve('tools/qgis/native-bridge.mjs')));
const root=resolve('build-native/qgis/edit-proof-B1h7dA'),config=join(root,'qgis-config.json');
const scratch=mkdtempSync(join(root,'integer-'));
const input=join(scratch,'integer-copy.geojson');copyFileSync(resolve(process.env.TEMP,'pando-qgis-migration-hJqtBq','source.geojson'),input);
const before=readFileSync(input),command=(...args)=>runNativeBridge(['--config',config,...args]);
const layer=(await command('open',input)).id;await command('begin-edit','--layer',layer);
try{
  const update=(field,json)=>command('set-attribute','--layer',layer,'--fid','0','--field',field,`--json=${json}`);
  for(const value of ['2147483648','-2147483649','9007199254740993','18446744073709551616'])
    await assert.rejects(update('schemaVersion',value),/range|large/i);
  await assert.rejects(update('schemaVersion','1.5'),/fractional/i);
  await assert.rejects(update('source','{\"a\":1,\"a\":2}'),/duplicate/i);
  await update('schemaVersion','2147483647');
  await update('source','{\"schemaVersion\":1,\"sourceId\":\"map\",\"sequence\":9223372036854775807}');
  const output=join(scratch,'integer-result.geojson');await command('export','--layer',layer,'--output',output);
  const bytes=readFileSync(output,'utf8');assert.match(bytes,/9223372036854775807/);
  assert.equal(JSON.parse(bytes).features[0].properties.schemaVersion,2147483647);
}finally{await command('rollback-edit','--layer',layer);}
assert.deepEqual(readFileSync(input),before);
console.log(JSON.stringify({int32Bounds:true,nestedInt64:true,duplicateKeysRejected:true,originalPreserved:true}));
