import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {mkdtempSync,readFileSync,writeFileSync} from 'node:fs';
import {join,resolve} from 'node:path';
import {pathToFileURL} from 'node:url';

const {runNativeBridge}=await import(pathToFileURL(resolve('tools/qgis/native-bridge.mjs')));
const root=resolve(process.env.PANDO_QGIS_PROOF_ROOT),config=join(root,'qgis-config.json');
const scratch=mkdtempSync(join(root,'projection-'));
const input=resolve(process.env.TEMP,'pando-qgis-migration-hJqtBq','source.geojson');
const projected=join(scratch,'projected.gpkg');
execFileSync('D:/dev/tools/osgeo4w/bin/ogr2ogr.exe',['-f','GPKG','-s_srs','EPSG:4326','-t_srs','EPSG:3857',projected,input],
  {env:{...process.env,PATH:'D:/dev/tools/osgeo4w/bin;'+process.env.PATH,PROJ_DATA:'D:/dev/tools/osgeo4w/share/proj',GDAL_DATA:'D:/dev/tools/osgeo4w/share/gdal'}});
const command=(...args)=>runNativeBridge(['--config',config,...args]);
const opened=await command('open',projected);assert.equal(opened.crs,'EPSG:3857');
await command('begin-edit','--layer',opened.id);
try{
const original=join(scratch,'projected-original.geojson');await command('export','--layer',opened.id,'--output',original);
await command('set-geometry','--layer',opened.id,'--fid','1','--wkt','LINESTRING (127 37, 128.5 38.5)');
const changed=join(scratch,'projected-changed.geojson');await command('export','--layer',opened.id,'--output',changed);
const originalValue=JSON.parse(readFileSync(original)),changedValue=JSON.parse(readFileSync(changed));
const geometry=changedValue.features.find(feature=>feature.geometry.type==='LineString').geometry;
assert.ok(Math.abs(geometry.coordinates[1][0]-128.5)<1e-8);
assert.ok(Math.abs(geometry.coordinates[1][1]-38.5)<1e-8);
await command('undo-edit','--layer',opened.id);
const undo=join(scratch,'projected-undo.geojson');await command('export','--layer',opened.id,'--output',undo);
assert.deepEqual(JSON.parse(readFileSync(undo)).features,originalValue.features);
}finally{await command('rollback-edit','--layer',opened.id);}
const pointSource=join(scratch,'point.geojson'),utm=join(scratch,'utm.gpkg');
writeFileSync(pointSource,JSON.stringify({type:'FeatureCollection',features:[{type:'Feature',properties:{name:'point'},geometry:{type:'Point',coordinates:[3,40]}}]}),{flag:'wx'});
execFileSync('D:/dev/tools/osgeo4w/bin/ogr2ogr.exe',['-f','GPKG','-s_srs','EPSG:4326','-t_srs','EPSG:32631',utm,pointSource],
  {env:{...process.env,PATH:'D:/dev/tools/osgeo4w/bin;'+process.env.PATH,PROJ_DATA:'D:/dev/tools/osgeo4w/share/proj',GDAL_DATA:'D:/dev/tools/osgeo4w/share/gdal'}});
const point=await command('open',utm);await command('begin-edit','--layer',point.id);
try{
  await assert.rejects(command('set-geometry','--layer',point.id,'--fid','1','--wkt','POINT (93 0)'),/transform|coordinate|proj/i);
  assert.equal((await command('status')).transport,'pando-native-v1');
}finally{await command('rollback-edit','--layer',point.id);}
console.log(JSON.stringify({projected:true,undo:true,failedTransformContained:true,source:'synthetic'}));
