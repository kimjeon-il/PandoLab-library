import fs from'node:fs';import cp from'node:child_process';import path from'node:path';import{pathToFileURL}from'node:url';import{createHash}from'node:crypto';
const app='D:/dev/worktrees/gis',base='d3a241588424afb7fc0dcf5f94c71f3bdd995238',current='ebc525a87e32808c3bf5f3cb008618a95fb58fba',out=path.resolve('ci-baseline-publication');fs.mkdirSync(out,{recursive:true});
const show=(rev,p)=>cp.execFileSync('git',['show',rev+':'+p],{cwd:app,encoding:'utf8',maxBuffer:32e6});
const modules=['tools/build-builtin-world.mjs','tools/builtin-world-compiler.mjs','tools/gis/historical-display-review.mjs'];
const copies=new Map(modules.map(p=>[path.resolve(app,p),path.join(out,path.basename(p))]));
function resolveImports(code,relativeFile,useCopies){return code.replace(/(from\s*['"])(\.[^'"]+)(['"])/g,(_,a,b,c)=>{const resolved=path.resolve(app,path.dirname(relativeFile),b);return a+pathToFileURL(useCopies&&copies.has(resolved)?copies.get(resolved):resolved).href+c;});}
for(const p of modules)fs.writeFileSync(copies.get(path.resolve(app,p)),resolveImports(show(base,p),p,true));
const fixture='tests/unit/historical-world-publication.test.mjs';let results=[];
for(const [name,rev]of [['baseline-d3a',base],['fixed-ebc',current]]){
 let code=resolveImports(show(rev,fixture),fixture,name==='baseline-d3a');
 const cleanup=' t.after(()=>fs.rmSync(folder,{recursive:true,force:true}));';
 if(!code.includes(cleanup))throw Error('Cleanup adapter anchor changed');
 code=code.replace(cleanup," t.after(()=>t.diagnostic('Preserved fresh synthetic fixture folder: '+folder));");
 const file=path.join(out,name+'.test.mjs');fs.writeFileSync(file,code);
 const run=cp.spawnSync(process.execPath,['--test','--test-name-pattern=country publication is deterministic',file],{cwd:app,encoding:'utf8',windowsHide:true,maxBuffer:4e6});
 const log=run.stdout+run.stderr;fs.writeFileSync(path.join(out,name+'.log'),log);
 results.push({name,revision:rev,exit:run.status,sameReviewFailure:/Historical display review required: state:changing\/before: missing or unresolved review/.test(log),logFile:path.basename(file).replace('.test.mjs','.log'),output:log.slice(-3500)});
}
const hash=s=>createHash('sha256').update(s.replaceAll('\r\n','\n')).digest('hex');
const compared=['tests/unit/historical-world-publication.test.mjs','tests/fixtures/historical-world-cases.mjs','tests/helpers/builtin-world.mjs','tools/gis/historical-display-review.mjs'];
const proof={baseline:base,current,comparison:compared.map(p=>({path:p,baselineSha256:hash(show(base,p)),currentSha256:hash(show(current,p)),unchanged:hash(show(base,p))===hash(show(current,p))})),adapter:'Only import paths point at the existing application or three extracted baseline modules; fresh fixture cleanup is replaced with a retention diagnostic in both copies. Test assertions, synthetic data and production gate are unchanged. No test folder is removed.',results};
if(results.some(r=>r.exit!==1||!r.sameReviewFailure))throw Error('Unexpected baseline comparison result: '+JSON.stringify(proof));
fs.writeFileSync('publication-baseline-reproduction.json',JSON.stringify(proof,null,2)+'\n');console.log(JSON.stringify(proof,null,2));
