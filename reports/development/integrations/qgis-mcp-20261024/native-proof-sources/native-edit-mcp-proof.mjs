import assert from 'node:assert/strict';
import {execFileSync,spawn} from 'node:child_process';
import {once} from 'node:events';
import {copyFileSync,readFileSync} from 'node:fs';
import {join,resolve} from 'node:path';
import {createInterface} from 'node:readline';

const root=resolve('build-native/qgis/edit-proof-nuatYA'),config=join(root,'qgis-config.json');
const original=resolve(process.env.TEMP,'pando-qgis-migration-hJqtBq','source.geojson');
const input=join(root,'mcp-edit-copy.geojson');copyFileSync(original,input);
const before=readFileSync(input),expected=JSON.parse(before);
const child=spawn(process.execPath,[resolve('tools/qgis/native-mcp.mjs')],{windowsHide:true,stdio:['pipe','pipe','pipe'],
  env:{...process.env,PANDO_QGIS_NATIVE_CONFIG:config}});
const pending=new Map(),lines=createInterface({input:child.stdout});
lines.on('line',line=>{const message=JSON.parse(line),callback=pending.get(message.id);if(callback){pending.delete(message.id);callback(message);}});
let number=0;const request=(method,params)=>new Promise((ok,fail)=>{
  const id=++number,timer=setTimeout(()=>fail(Error('MCP request timed out')),30000);
  pending.set(id,message=>{clearTimeout(timer);if(message.error)fail(Error(message.error.message));else ok(message.result);});
  child.stdin.write(JSON.stringify({jsonrpc:'2.0',id,method,params})+'\n');
});
try{
  await request('initialize',{protocolVersion:'2025-06-18',capabilities:{},clientInfo:{name:'proof',version:'1'}});
  child.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n');
  const call=async(name,args)=>{const result=await request('tools/call',{name,arguments:args});if(result.isError)throw Error(result.content[0].text);return JSON.parse(result.content[0].text);};
  const opened=await call('qgis_native_open',{input}),layer=opened.id;
  await call('qgis_native_begin_edit',{layer});
  await call('qgis_native_set_attribute',{layer,fid:'0',field:'name',json:JSON.stringify('-지도 검증')});
  const out=async name=>{const output=join(root,name+'.geojson');await call('qgis_native_export',{layer,output});return JSON.parse(readFileSync(output));};
  const changed=await out('mcp-edit');assert.equal(changed.features[0].properties.name,'-지도 검증');
  assert.deepEqual(changed.features[0].properties.source,expected.features[0].properties.source);
  await call('qgis_native_undo_edit',{layer});assert.equal((await out('mcp-undo')).features[0].properties.name,expected.features[0].properties.name);
  await call('qgis_native_redo_edit',{layer});assert.equal((await out('mcp-redo')).features[0].properties.name,'-지도 검증');
  await call('qgis_native_set_attribute',{layer,fid:'0',field:'source',json:'{\"schemaVersion\":1,\"sourceId\":\"map\",\"sequence\":9007199254740993}'});
  const pageResult=await request('tools/call',{name:'qgis_native_features',arguments:{layer,limit:1,geometry:true}});
  assert.equal(pageResult.isError,undefined);
  const page=JSON.parse(pageResult.content[0].text,(key,value,context)=>key==='sequence'?BigInt(context.source):value);
  assert.equal(page.hasMore,true);assert.equal(page.features[0].fid,'0');
  assert.equal(page.features[0].attributes.source.sequence,9007199254740993n);assert.match(page.features[0].geometryWkt,/^linestring/i);
  const wideOutput=join(root,'mcp-wide.geojson');await call('qgis_native_export',{layer,output:wideOutput});
  assert.match(readFileSync(wideOutput,'utf8'),/9007199254740993/);
  const geometry={type:'LineString',coordinates:[[127,37],[128.5,38.5]]};
  await call('qgis_native_set_geometry',{layer,fid:'0',wkt:'LINESTRING (127 37, 128.5 38.5)'});
  assert.deepEqual((await out('mcp-geometry')).features[0].geometry,geometry);
  await call('qgis_native_undo_edit',{layer});assert.deepEqual((await out('mcp-geometry-undo')).features[0].geometry,expected.features[0].geometry);
  await call('qgis_native_redo_edit',{layer});assert.deepEqual((await out('mcp-geometry-redo')).features[0].geometry,geometry);
  await call('qgis_native_rollback_edit',{layer});const rolled=await out('mcp-rollback');
  assert.equal(rolled.features[0].properties.name,expected.features[0].properties.name);
  assert.deepEqual(rolled.features[0].properties.source,expected.features[0].properties.source);
  const projected=join(root,'mcp-projected.gpkg');
  execFileSync('D:/dev/tools/osgeo4w/bin/ogr2ogr.exe',['-f','GPKG','-s_srs','EPSG:4326','-t_srs','EPSG:3857',projected,input],
    {env:{...process.env,PATH:'D:/dev/tools/osgeo4w/bin;'+process.env.PATH,PROJ_DATA:'D:/dev/tools/osgeo4w/share/proj',GDAL_DATA:'D:/dev/tools/osgeo4w/share/gdal'}});
  const projectedLayer=(await call('qgis_native_open',{input:projected})).id;
  await call('qgis_native_begin_edit',{layer:projectedLayer});
  await call('qgis_native_set_geometry',{layer:projectedLayer,fid:'1',wkt:'LINESTRING (127 37, 128.5 38.5)'});
  const projectedOutput=join(root,'mcp-projected.geojson');await call('qgis_native_export',{layer:projectedLayer,output:projectedOutput});
  const projectedLine=JSON.parse(readFileSync(projectedOutput)).features.find(feature=>feature.geometry.type==='LineString');
  assert.ok(Math.abs(projectedLine.geometry.coordinates[1][0]-128.5)<1e-8);
  assert.ok(Math.abs(projectedLine.geometry.coordinates[1][1]-38.5)<1e-8);
  await call('qgis_native_rollback_edit',{layer:projectedLayer});
  assert.deepEqual(readFileSync(input),before);
  console.log(JSON.stringify({geometry:true,projected:true,undoRedo:true,rollback:true,nestedSourcePreserved:true,inputUnchanged:true}));
}finally{child.stdin.end();if(child.exitCode===null)await once(child,'exit');}
