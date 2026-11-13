import {spawn} from 'node:child_process';
import {randomBytes} from 'node:crypto';
import {mkdirSync,mkdtempSync,readFileSync,writeFileSync} from 'node:fs';
import {createServer} from 'node:net';
import {join,resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
const {requestNativeQgis}=await import(pathToFileURL(resolve('tools/qgis/native-client.mjs')));
const {exportNativeQgis}=await import(pathToFileURL(resolve('tools/qgis/native-export.mjs')));
const root=mkdtempSync(resolve('build-native/qgis/native-proof-'));
const profiles=join(root,'profiles'),profile=join(profiles,'profiles','proof','QGIS');
mkdirSync(profile,{recursive:true});
const artifact=resolve(process.env.PANDO_QGIS_TEST_ARTIFACT||'build-native/qgis/artifact');
writeFileSync(join(profile,'QGIS3.ini'),`[Plugins]\npando_qgis_bridge=true\n[plugins]\nsearchPathsForPlugins=${artifact.replaceAll('\\','/')}\n`,{flag:'wx'});
const probe=createServer();await new Promise((ok,fail)=>probe.once('error',fail).listen(0,'127.0.0.1',ok));
const port=probe.address().port;await new Promise((ok,fail)=>probe.close(error=>error?fail(error):ok()));
const config={host:'127.0.0.1',port,token:randomBytes(32).toString('hex')};
const launcher='D:\\dev\\tools\\osgeo4w\\bin\\qgis-ltr.bat';
const child=spawn(process.env.ComSpec||'cmd.exe',['/d','/c',launcher,'--nologo','--noversioncheck','--profiles-path',profiles,'--profile','proof'],{
  env:{...process.env,PANDO_QGIS_NATIVE_TOKEN:config.token,PANDO_QGIS_NATIVE_PORT:String(port)},windowsHide:true,stdio:'ignore'});
child.on('error',error=>{console.error('QGIS launcher failed:',error.message);process.exitCode=1;});
let status;const deadline=Date.now()+120000;
while(Date.now()<deadline){
  try{status=await requestNativeQgis(config,{command:'status'},{timeoutMs:2000});break;}
  catch{await new Promise(ok=>setTimeout(ok,1000));}
}
if(!status)throw Error(`Native QGIS did not start; test profile preserved at ${root}`);
assert.equal(status.transport,'pando-native-v1');assert.match(status.qgis_version,/^3\.44\.15/);
console.log(JSON.stringify({stage:'status',root,status}));
await assert.rejects(requestNativeQgis({...config,token:'incorrect'},{command:'status'},{timeoutMs:90000}),/authentication/i);
console.log(JSON.stringify({stage:'authentication'}));
const input=resolve(process.env.TEMP,'pando-qgis-migration-hJqtBq','source.geojson');
const original=JSON.parse(readFileSync(input,'utf8'));
const layer=await requestNativeQgis(config,{command:'open',path:input},{timeoutMs:90000});
console.log(JSON.stringify({stage:'open',layer}));
assert.equal(layer.feature_count,2);assert.equal(layer.crs,'EPSG:4326');
const output=join(root,'native-result.geojson');
const receipt=await exportNativeQgis(config,{layerId:layer.id,output});
const exported=JSON.parse(readFileSync(output,'utf8'));
assert.equal(exported.features.length,original.features.length);
for(let i=0;i<original.features.length;i++){
  assert.deepEqual(exported.features[i].geometry,original.features[i].geometry);
  assert.deepEqual(exported.features[i].properties.source,original.features[i].properties.source);
}
await assert.rejects(exportNativeQgis(config,{layerId:layer.id,output}),/exists/i);
console.log(JSON.stringify({root,status,layer,receipt,verified:['authentication','geometry','nested provenance','existing output refusal']}));
