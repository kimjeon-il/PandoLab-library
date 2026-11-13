import assert from 'node:assert/strict';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import {readFileSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {createInterface} from 'node:readline';
const root=resolve('build-native/qgis/cli-proof-eLq7rh'),config=join(root,'qgis-config.json');
const child=spawn(process.execPath,[resolve('tools/qgis/native-mcp.mjs')],{windowsHide:true,stdio:['pipe','pipe','pipe'],
  env:{...process.env,PANDO_QGIS_NATIVE_CONFIG:config}});
let stderr='';child.stderr.setEncoding('utf8');child.stderr.on('data',text=>{stderr+=text;});
const pending=new Map(),lines=createInterface({input:child.stdout});
lines.on('line',line=>{const message=JSON.parse(line),callback=pending.get(message.id);if(callback){pending.delete(message.id);callback(message);}});
let number=0;const request=(method,params)=>new Promise((ok,fail)=>{
  const id=++number,timer=setTimeout(()=>fail(Error(`MCP ${method} timed out`)),30000);
  pending.set(id,message=>{clearTimeout(timer);if(message.error)fail(Error(message.error.message));else ok(message.result);});
  child.stdin.write(JSON.stringify({jsonrpc:'2.0',id,method,params})+'\n');
});
try{
  await request('initialize',{protocolVersion:'2025-06-18',capabilities:{},clientInfo:{name:'proof',version:'1'}});
  child.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n');
  const call=async(name,args)=>{const result=await request('tools/call',{name,arguments:args});if(result.isError)throw Error(result.content[0].text);return JSON.parse(result.content[0].text);};
  const status=await call('qgis_native_status',{});assert.equal(status.pid,9712);
  const project=await call('qgis_native_project',{});assert.equal(project.layer_count,1);
  const layers=await call('qgis_native_layers',{offset:0,limit:1});assert.equal(layers.total_count,1);assert.equal(layers.layers[0].feature_count,2);
  const input=resolve(process.env.TEMP,'pando-qgis-migration-hJqtBq','source.geojson');
  const opened=await call('qgis_native_open',{input});assert.equal(opened.feature_count,2);
  const picked=await call('qgis_native_select',{layer:opened.id,fids:['0']});assert.equal(picked.selected,1);const selected=await call('qgis_native_selection',{layer:opened.id});assert.deepEqual(selected.fids,['0']);await call('qgis_native_clear_selection',{layer:opened.id});assert.equal((await call('qgis_native_selection',{layer:opened.id})).count,0);
  const byName=await call('qgis_native_select',{layer:opened.id,expression:`"name" = 'QGIS 연동 검증 영역'`});assert.equal(byName.selected,1);
  await call('qgis_native_clear_selection',{layer:opened.id});
  const schema=await call('qgis_native_schema',{layer:opened.id});assert.equal(schema.crs,'EPSG:4326');assert.ok(schema.fields.some(field=>field.name==='source'));
  const output=join(root,'mcp-result.geojson');await call('qgis_native_export',{layer:opened.id,output});
  const before=JSON.parse(readFileSync(input)),after=JSON.parse(readFileSync(output));
  assert.equal(after.features.length,2);
  for(let i=0;i<2;i++){assert.deepEqual(after.features[i].geometry,before.features[i].geometry);assert.deepEqual(after.features[i].properties.source,before.features[i].properties.source);}
  console.log(JSON.stringify({pid:status.pid,features:2,output}));
}finally{child.stdin.end();if(child.exitCode===null){await once(child,'exit');}}
if(stderr)console.error(stderr);
