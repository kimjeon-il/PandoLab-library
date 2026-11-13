import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
let seed=159;const random=n=>((seed=(seed*1664525+1013904223)>>>0)%n);
const py=`import sys,numpy as np
from PIL import Image,ImageFilter
kind,w,h,r=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
a=np.frombuffer(sys.stdin.buffer.read(),dtype=np.uint8).reshape(h,w)
if kind=='dilate':
 p=np.asarray(Image.fromarray(a).filter(ImageFilter.MaxFilter(2*r+1)));print(''.join(str(int(x)) for x in p.flat))
else:
 n=np.zeros_like(a);i=np.zeros_like(a,dtype=bool)
 for v in np.unique(a):
  if v:
   m=Image.fromarray((a==v).astype(np.uint8));n+=np.asarray(m.filter(ImageFilter.MaxFilter(2*r+1)));i|=np.asarray(m.filter(ImageFilter.MinFilter(2*r+1))).astype(bool)
 p=(n>=2)&(a==0);k=p|i;print(''.join(str(int(x)) for x in p.flat)+' '+''.join(str(int(x)) for x in k.flat))`;
for(let n=0;n<40;n++){
  const kind=n%2?'dilate':'adjacency',w=1+random(12),h=1+random(12),r=1+random(kind==='dilate'?32:4),input=Buffer.alloc(w*h);
  for(let i=0;i<input.length;i++)input[i]=random(kind==='dilate'?2:5);
  const args=[kind,String(w),String(h),String(r)];
  const old=spawnSync('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',['-c',py,...args],{input,encoding:'utf8'});
  assert.equal(old.status,0,old.stderr);
  const native=spawnSync(process.execPath,['build-native/map-image/macro-mask-dev.cjs',...args],{input,encoding:'utf8'});
  assert.equal(native.status,0,native.stderr);assert.equal(native.stdout.trim(),old.stdout.trim(),`case ${n}: ${args}`);
}
console.log('40 macro mask cases matched Pillow');
