import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {mkdtempSync,readFileSync,writeFileSync} from 'node:fs';
import {join,resolve} from 'node:path';
import {runNativeBridge} from '../../tools/qgis/native-bridge.mjs';

const base=resolve('build-native/qgis/migration-current'),root=mkdtempSync(join(base,'clip-proof-'));
const config=resolve(base,'qgis-config.json'),args=['--config',config];
const before=await runNativeBridge([...args,'project']);
if(before.filename||before.layer_count!==0)throw Error('Preserve the existing QGIS project; a blank test project is required');
const line=join(root,'line.geojson'),polygon=join(root,'polygon.geojson'),output=join(root,'clip.geojson');
writeFileSync(line,JSON.stringify({type:'FeatureCollection',features:[{type:'Feature',id:'road-1',
  geometry:{type:'LineString',coordinates:[[-2,0],[2,0]]},properties:{name:'road',source:{sourceId:'original'}}}]}),{flag:'wx'});
writeFileSync(polygon,JSON.stringify({type:'FeatureCollection',features:[{type:'Feature',
  geometry:{type:'Polygon',coordinates:[[[-1,-1],[1,-1],[1,1],[-1,1],[-1,-1]]]},properties:{name:'boundary'}}]}),{flag:'wx'});
const sha=path=>createHash('sha256').update(readFileSync(path)).digest('hex'),lineSha=sha(line),polygonSha=sha(polygon);
const layers=[];
try{
  const a=await runNativeBridge([...args,'open',line]);layers.push(a.id);
  const b=await runNativeBridge([...args,'open',polygon]);layers.push(b.id);
  await assert.rejects(runNativeBridge([...args,'clip','--layer',a.id,'--overlay',a.id,'--output',join(root,'invalid.geojson')]),/polygon/i);
  const result=await runNativeBridge([...args,'clip','--layer',a.id,'--overlay',b.id,'--output',output]);
  assert.equal(result.qgis.crs,'EPSG:4326');assert.equal(result.qgis.features,1);
  const saved=JSON.parse(readFileSync(output,'utf8')),feature=saved.features[0];
  const coordinates=feature.geometry.type==='MultiLineString'?feature.geometry.coordinates[0]:feature.geometry.coordinates;
  assert.deepEqual(coordinates,[[-1,0],[1,0]]);assert.equal(feature.properties.name,'road');
  assert.equal(feature.properties.source.sourceId,'original');
  const outputSha=sha(output);await assert.rejects(runNativeBridge([...args,'clip','--layer',a.id,'--overlay',b.id,'--output',output]),/exists/i);
  assert.equal(sha(output),outputSha);assert.equal(sha(line),lineSha);assert.equal(sha(polygon),polygonSha);
  console.log(JSON.stringify({features:1,coordinates,sourcePreserved:true,existingOutputPreserved:true,outputSha256:outputSha}));
}finally{
  for(const layer of layers.reverse())await runNativeBridge([...args,'remove-layer','--layer',layer]);
}
