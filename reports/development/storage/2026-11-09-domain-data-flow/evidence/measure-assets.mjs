import fs from 'node:fs';import {execFileSync} from 'node:child_process';import {createHash} from 'node:crypto';
import {buildFrontendSnapshot} from '../../../scripts/lib/frontend-build.mjs';import {libraryCheckout,libraryConfig} from '../../../tools/data/library-context.mjs';
const root=process.cwd(),s=await buildFrontendSnapshot({root}),config=libraryConfig(root);
const archive=JSON.parse(execFileSync('git',['show',config.revision+':archive/index.json'],{cwd:libraryCheckout(root),maxBuffer:16*1024*1024}));
const unique=new Map(),inodes=new Map();let bytes=0,dataBytes=0,dataFiles=0,linkedDataFiles=0;
for(const path of s.viewerPaths){let count,key;
 if(s.assets.has(path)){const b=s.assets.get(path).bytes;count=b.length;key=createHash('sha256').update(b).digest('hex');}
 else{const p=fs.realpathSync(path),st=fs.statSync(p,{bigint:true});count=Number(st.size);key=archive.files[path].sha256;dataFiles++;dataBytes+=count;
  if(st.nlink>1n)linkedDataFiles++;inodes.set(st.dev+':'+st.ino,{path:p,bytes:count});}
 bytes+=count;if(unique.has(key)&&unique.get(key)!==count)throw Error('Conflicting content identity');unique.set(key,count);
}
const r={code:s.sourceCommit,data:config.revision,inputSha256:s.sourceSha256,files:s.viewerPaths.size,logicalBytes:bytes,uniqueContentBytes:[...unique.values()].reduce((a,b)=>a+b,0),dataFiles,dataBytes,hardlinkedDataFiles:linkedDataFiles,dataInodeFiles:inodes.size,dataInodeLogicalBytes:[...inodes.values()].reduce((n,x)=>n+x.bytes,0)};
fs.writeFileSync('.superpowers/sdd/domain-data-restructure/assets-after.json',JSON.stringify(r,null,2));fs.writeFileSync('.superpowers/sdd/domain-data-restructure/physical-runtime-files.json',JSON.stringify([...inodes.values()]));console.log(JSON.stringify(r));
