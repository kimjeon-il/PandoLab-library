import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
let seed=413;const random=n=>((seed=(seed*1664525+1013904223)>>>0)%n);
for(let example=0;example<60;example++){
  const sx=random(20),sy=random(20),sw=1+random(9),sh=1+random(9),tx=random(20),ty=random(20),tw=1+random(9),th=1+random(9),radius=random(20)/2;
  const source=Buffer.alloc(sw*sh);for(let i=0;i<source.length;i++)source[i]=random(8);
  const header=Buffer.alloc(48);header.write('PXCOR001');let at=8;
  for(const value of [sx,sy,sw,sh,tx,ty,tw,th]){header.writeUInt32BE(value,at);at+=4;}header.writeDoubleBE(radius,at);
  const run=spawnSync(process.execPath,['build-native/map-evaluation/evaluation-dev.cjs'],{input:Buffer.concat([header,source]),encoding:'utf8'});
  assert.equal(run.status,0,run.stderr);const actual=Buffer.from(JSON.parse(run.stdout).data,'base64'),expected=Buffer.alloc(tw*th);
  for(let y=0;y<th;y++)for(let x=0;x<tw;x++)for(let j=0;j<sh;j++)for(let i=0;i<sw;i++)if((tx+x-sx-i)**2+(ty+y-sy-j)**2<=radius*radius)expected[y*tw+x]|=source[j*sw+i];
  assert.deepEqual(actual,expected,`case ${example}`);
}
console.log('60 proximity cases matched direct disk calculation');
