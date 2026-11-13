import assert from 'node:assert/strict';
import {execFile} from 'node:child_process';
import {readFile} from 'node:fs/promises';
import {join,resolve,delimiter} from 'node:path';
import {promisify} from 'node:util';
import test from 'node:test';
import {hydroSourceFixture} from '../../tests/helpers/hydro-source-fixture.mjs';

const exec=promisify(execFile);
test('Node Hydro audit matches the original Python source and report',async t=>{
  const {root,input}=await hydroSourceFixture(t),old=join(root,'old-audit.json'),next=join(root,'new-audit.json');
  const args=report=>['--baseline',input,'--sources',root,'--report',report];
  await exec('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',[resolve('tools/hydro_connectivity.py'),...args(old)],{
    windowsHide:true,env:{...process.env,PYTHONPATH:resolve('build-native/hydro-connectivity/oracle-deps')+delimiter+(process.env.PYTHONPATH||''),
      PANDO_HYDRO_CONNECTIVITY_BINARY:resolve('build-native/hydro-connectivity/artifact/pando-hydro-connectivity.exe')}});
  await exec(process.execPath,[resolve('tools/audit-hydro-connectivity.mjs'),...args(next)],{windowsHide:true});
  assert.deepEqual(JSON.parse(await readFile(next)),JSON.parse(await readFile(old)));
});
