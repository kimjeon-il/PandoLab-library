import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {spawnSync} from 'node:child_process';
import {normalizeHydronym} from '../../tools/gis/hydronym-normalize.mjs';

const bridge=readFileSync('tests/unit/hydro-name-python-bridge.test.mjs','utf8');
const marker='const script=String.raw`',start=bridge.indexOf(marker)+marker.length,end=bridge.indexOf('`;',start);
if(start<marker.length||end<start)throw Error('Python naming oracle not found');
const python=bridge.slice(start,end);
const rows=JSON.parse(readFileSync('tests/fixtures/hydro-name-oracle.json','utf8')).map(({name,category,overrides})=>({name,category,overrides}));
const whitespace=[' ','\t','\n','\r','\u001c','\u0085','\u00a0','\u2003','\u2028'];
for(const space of whitespace)for(const name of ['한 강강','예시 호수','Example River','강','Lake','미명명 수계 4','한강\n','강\r'])
  for(const category of ['river','lake','other'])rows.push({name:space+name+space,category,overrides:{}});
for(const name of ['A','예시 호수','미명명 강'])for(const alias of ['북아랄해','예시 호수','Example River','미명명 강\n'])
  rows.push({name,category:'river',overrides:{[name]:alias}});
const run=spawnSync('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',['-X','utf8','-B','-c',python],
  {input:JSON.stringify(rows),encoding:'utf8',windowsHide:true,timeout:30000});
assert.equal(run.status,0,run.stderr);
const expected=JSON.parse(run.stdout),differences=[];
for(let i=0;i<rows.length;i++){
  const actual=normalizeHydronym(rows[i].name,rows[i].category,rows[i].overrides);
  if(actual!==expected[i])differences.push({input:rows[i],expected:expected[i],actual});
}
console.log(JSON.stringify({cases:rows.length,differences:differences.slice(0,10),differenceCount:differences.length}));
if(differences.length)process.exitCode=1;
