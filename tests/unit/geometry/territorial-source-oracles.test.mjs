import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {spawnSync} from 'node:child_process';
import test from 'node:test';
const fixture=name=>JSON.parse(readFileSync(new URL('../../fixtures/'+name,import.meta.url),'utf8'));
function run(command,input){
 const binary=process.env.PANDO_TERRITORIAL_RECIPE_BINARY;assert.ok(binary,'Select the registered library native recipe check');
 const result=spawnSync(binary,[command,'-'],{input:JSON.stringify(input),encoding:'utf8'});
 assert.equal(result.status,0,result.stderr||result.error?.message);return JSON.parse(result.stdout);
}
for(const [file,command,prepare,read] of [
 ['lsib-merge-lines-oracle.json','--merge-lsib-lines',row=>({geometries:[row.geometry]}),out=>out.geometries[0]],
 ['lsib-reference-oracle.json','--prepare-lsib-reference',row=>row,out=>out.coordinates],
 ['lsib-display-section-oracle.json','--select-lsib-display',row=>row,out=>out.coordinates],
 ['lsib-union-oracle.json','--union-lsib-lines',row=>row,out=>out.geometry],
]){
 const body=fixture(file),rows=Array.isArray(body)?body:body.cases;
 for(const [index,row] of rows.entries())test(file+' '+(row.name||index),()=>{
  const original=structuredClone(row);assert.deepEqual(read(run(command,prepare(row))),row.expected);assert.deepEqual(row,original);
 });
}
