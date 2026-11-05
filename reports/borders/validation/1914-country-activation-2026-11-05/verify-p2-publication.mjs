import fs from'node:fs';import cp from'node:child_process';import assert from'node:assert/strict';import{createHash}from'node:crypto';
import{decodeLibraryArchiveBytes}from'file:///D:/dev/worktrees/gis/tools/library-archive.mjs';
await import('file:///D:/dev/worktrees/gis/tools/load-spherical-core.mjs');
const{resolvePhysicalWaterObjects}=await import('file:///D:/dev/worktrees/gis/shared/frontend/js/modules/physical-resources.js');
const repo='D:/dev/PandoLab-library-data',base='bd62cc8ec6d8221202ed19de0a66f98d3e07ace9',fixed='b6c3c85bba690244829bdec93c58682d9342bda8',show=(r,p)=>cp.execFileSync('git',['show',r+':'+p],{cwd:repo,maxBuffer:32e6}),idx=r=>JSON.parse(show(r,'archive/index.json')),old=idx(base),next=idx(fixed),sha=b=>createHash('sha256').update(b).digest('hex'),get=(r,index,p)=>decodeLibraryArchiveBytes(show(r,index.files[p].stored),index.files[p]);
const plan=JSON.parse(fs.readFileSync('p2-parent-runtime-plan.json'));
for(const f of plan.files)assert.equal(sha(get(fixed,next,f.logical)),f.sha256);
const changes=Object.keys(next.files).filter(p=>next.files[p].sha256!==old.files[p]?.sha256);
assert.deepEqual([...changes].sort(),plan.prefixes.slice().sort());
const sourcePaths=['state-east-prussia','state-west-prussia','state-DEU','state-austro-hungarian-empire','state-kingdom-of-serbia'].map(id=>'assets/data/territorial-entities/source/countries/'+id+'.json');
for(const p of sourcePaths)assert.deepEqual(next.files[p],old.files[p]);
let physical=[];
for(const rev of ['d2c023082b3e10ed0dc6928f629f190e0756933c',base,fixed]){
 const index=idx(rev),manifest=JSON.parse(get(rev,index,'assets/data/physical-land/v1/manifest.json'));
 const selected=resolvePhysicalWaterObjects(manifest.waterObjects,'1922-12-31');
 const landRevisions=[...new Set(selected.map(row=>row.assets.land.sha256))];
 assert.deepEqual(landRevisions,['66fa6cbb61a1358cfc64a8ae2c1f1b6afad1f82ed574f664e55668a08925f608']);
 physical.push({revision:rev,date:'1922-12-31',selectedObjects:selected.length,landRevisions,hydroPinnedGuardPasses:rev==='91c127ddbae902405de6e35b38940a59a8c0d021'});
}
const remote=cp.execFileSync('git',['ls-remote','origin','refs/heads/work/gis'],{cwd:repo,encoding:'utf8'}).split(/\s+/)[0];assert.equal(remote,fixed);
fs.writeFileSync('p2-parent-remote-proof.json',JSON.stringify({appCommit:'ebc525a87e32808c3bf5f3cb008618a95fb58fba',dataCommit:fixed,remoteDataCommit:remote,verifiedFiles:plan.files,changedLogicalPaths:changes,sourceDescriptorsPreserved:sourcePaths,physicalBaselineSelection:physical,sourceAndGeometryChanges:0},null,2)+'\n');console.log(JSON.stringify({remoteDataCommit:remote,changedLogicalPaths:changes,physicalBaselineSelection:physical},null,2));
