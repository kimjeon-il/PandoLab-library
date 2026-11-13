import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const {probeNgaBatch03}=await import(pathToFileURL(resolve('tools/gis/probe-nga-streams.mjs')));
const {screenHydroPoints}=await import(pathToFileURL(resolve('tools/gis/hydro-point-screen-native.mjs')));
const {buildBatch03Screen}=await import(pathToFileURL(resolve('tools/gis/verify-osm-hydro-batch03-points.mjs')));
const root='build-native/hydro-point-screen/real-proof-92B7wp/';
const raw=execFileSync('git',['show','HEAD:tests/fixtures/hydro-osm-batch03-nga-response.json']);
const receipts=await probeNgaBatch03({fetcher:async()=>new Response(raw,{status:200})});
const decoded=JSON.parse(readFileSync(root+'decoded.json','utf8'));
const result=await buildBatch03Screen(decoded,{receipts,screen:input=>screenHydroPoints(input,{
  directory:resolve('build-native/hydro-point-screen/candidate-tree'),runtimeRoot:'D:/dev/tools/osgeo4w'})});
const baseline=readFileSync(root+'batch03-python.json');assert.deepEqual(result,JSON.parse(baseline));
writeFileSync(root+'batch03-windows.json',JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({systems:result.systemsReviewed,points:result.comparedIndependentPoints,queries:result.governmentQueryCount,
  baselineBytes:baseline.length,baselineSha256:createHash('sha256').update(baseline).digest('hex')}));
