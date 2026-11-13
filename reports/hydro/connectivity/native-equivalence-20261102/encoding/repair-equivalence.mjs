import assert from 'node:assert/strict';
import {execFile} from 'node:child_process';
import {readFile} from 'node:fs/promises';
import {join,resolve,delimiter} from 'node:path';
import {promisify} from 'node:util';
import test from 'node:test';
import {hydroSourceFixture} from '../../tests/helpers/hydro-source-fixture.mjs';

const exec=promisify(execFile);
test('new Hydro repair matches original Python output on the same nine synthetic regions',async t=>{
  const {root,input}=await hydroSourceFixture(t),oldOutput=join(root,'old-pack'),newOutput=join(root,'new-pack');
  const oldReport=join(root,'old-report.json'),newReport=join(root,'new-report.json');
  const args=(output,report)=>['--baseline',input,'--sources',root,'--output',output,'--report',report];
  await exec('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',[resolve('tools/repair-hydro-connectivity.py'),...args(oldOutput,oldReport)],{
    windowsHide:true,env:{...process.env,PYTHONPATH:resolve('build-native/hydro-connectivity/oracle-deps')+delimiter+(process.env.PYTHONPATH||''),
      PANDO_HYDRO_CONNECTIVITY_BINARY:resolve('build-native/hydro-connectivity/artifact/pando-hydro-connectivity.exe')}});
  await exec(process.execPath,[resolve('tools/repair-hydro-connectivity.mjs'),...args(newOutput,newReport)],{windowsHide:true});
  for(const file of ['index.bin.gz','metadata-core.json.gz','metadata-detail.json.gz','shards/s0.bin'])
    assert.deepEqual(await readFile(join(newOutput,file)),await readFile(join(oldOutput,file)),file);
  const old=JSON.parse(await readFile(oldReport)),next=JSON.parse(await readFile(newReport));
  for(const field of ['baselineRegions','regions','changes','remaining','changedFeatureIds','unchangedFeatureCount','baselineManifestFingerprint'])
    assert.deepEqual(next[field],old[field],field);
  console.log(JSON.stringify({features:3,artifacts:4,reportFields:7,match:true}));
});
