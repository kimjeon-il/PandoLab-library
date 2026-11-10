import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';
import {isDeepStrictEqual as eq} from 'node:util';
if(!process.argv.includes('--apply'))throw Error('Explicit --apply required after parent releases this writer slot; preparation alone does not authorize execution.');
const A='D:/dev/PandoLab',GIS='D:/dev/worktrees/gis',O=new URL('.',import.meta.url),root='D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109';
// Process-only stricter guard: no Git transport can be used, including accidental lazy fetch. No repository configuration is changed.
const count=Number(process.env.GIT_CONFIG_COUNT||0);if(!Number.isInteger(count)||count<0||count>1024)throw Error('Unexpected Git environment');process.env.GIT_CONFIG_COUNT=String(count+1);process.env['GIT_CONFIG_KEY_'+count]='protocol.allow';process.env['GIT_CONFIG_VALUE_'+count]='never';process.env.GIT_TERMINAL_PROMPT='0';process.env.GIT_NO_LAZY_FETCH='1';
const m=await import(pathToFileURL(root+'/deu-c1-c2-c3-combined/source-review/review-inputs.mjs'));
const s=await import(pathToFileURL(A+'/tools/data/territorial-entity-sources.mjs')),rt=await import(pathToFileURL(A+'/tools/data/library-runtime.mjs')),ctx=await import(pathToFileURL(A+'/tools/data/library-context.mjs'));
const read=n=>JSON.parse(fs.readFileSync(new URL(n,O))),write=(n,x,flag)=>fs.writeFileSync(new URL(n,O),JSON.stringify(x,null,2)+'\n',flag?{flag}:undefined),bundle=read('canonical-paired-source-patch.json'),ledger=read('candidate-ledger.json');
if(fs.existsSync(new URL('local-source-application.json',O)))throw Error('Existing application journal: inspect actual state before any retry.');
const base=m.git('rev-parse','HEAD').toString().trim(),configBefore=JSON.parse(fs.readFileSync(A+'/config/library-data.json')),gisPinBytes=fs.readFileSync(GIS+'/config/library-data.json'),appHeadBefore=execFileSync('git',['-C',A,'rev-parse','HEAD'],{encoding:'utf8'}).trim();
if(configBefore.revision!==base)throw Error('Main writer pin must equal latest archive HEAD; do not alter GIS pin or auto-repoint main here.');
if(m.git('status','--porcelain').toString().trim())throw Error('Archive checkout contains edits; wait for other writer.');
const view=ctx.libraryMaterializedRoot(A);if(!fs.existsSync(path.join(view,'.complete')))throw Error('Existing complete main materialized view required; no fetch/preparation fallback.');
if(!eq(bundle.patches.map(p=>p.entityId).sort(),['state:soviet-union','state:soviet-union-russian-sfsr']))throw Error('Unexpected entity batch');
const donor=m.entity('RUS',base).entity.geometryVersions.find(v=>v.versionId===ledger.donor.versionId);if(m.gh(donor.geometry)!==ledger.donor.geometrySha256)throw Error('Approved donor changed');
const prepared=[];
for(const p of bundle.patches){
 const archived=m.entity(p.entityId.replace('state:',''),base),before=s.readTerritorialSource(p.entityId);
 if(archived.descriptorSha256!==p.sourceDescriptorPreimageSha256||m.h(archived.entity)!==p.normalizedEntityPreimageSha256||!eq(before,archived.entity)||m.sha(fs.readFileSync(A+'/'+p.sourcePath))!==p.sourceDescriptorPreimageSha256)throw Error('Latest archive/live source preimage changed: '+p.entityId);
 const next=structuredClone(before);for(const v of p.replacementVersions){const at=next.geometryVersions.findIndex(q=>q.versionId===v.versionId);if(at<0)throw Error('Missing version');next.geometryVersions[at]=v;}next.sourceInfo.sourceAttributions??=[];next.sourceInfo.sourceAttributions.push(...p.sourceAttributionsAppend);
 const n=m.normalize(next),enc=m.encodeTerritorialSource(n),count=m.assertHistoricalDisplayChanges(n,before);
 if(count!==p.replacementVersions.length||m.h(n)!==p.expected.entitySha256||m.sha(Buffer.from(JSON.stringify(enc.descriptor,null,2)+'\n'))!==p.expected.descriptorSha256||!eq(m.normalize(m.decodeTerritorialSource(enc.descriptor,f=>enc.geometries.get(f))),n))throw Error('Hash/gate/codec mismatch');
 const selectedIds=new Set(p.replacementVersions.map(v=>v.versionId)),selectedFiles=new Set(enc.descriptor.geometryVersions.filter(v=>selectedIds.has(v.versionId)).map(v=>v.geometryResource.file)),newPaths=[];
 for(const [file,bytes] of enc.geometries){const target=A+'/assets/data/territorial-entities/source/'+file;if(fs.existsSync(target)){if(!fs.readFileSync(target).equals(bytes))throw Error('Existing immutable resource differs');}else{if(!selectedFiles.has(file))throw Error('Unselected geometry unhydrated; stop instead of writing it');newPaths.push('assets/data/territorial-entities/source/'+file);}}
 if(newPaths.length!==p.replacementVersions.length)throw Error('Expected exactly one new geometry resource per selected version; inspect unexpected existing resource before retry.');
 prepared.push({p,before,n,paths:[p.sourcePath,...newPaths],count});
}
const prefixes=[...new Set(prepared.flatMap(q=>q.paths))].sort();if(prefixes.length!==5||prepared.reduce((n,p)=>n+p.count,0)!==3)throw Error('Expected exactly two descriptors and three new geometries');
// Prove storage's unchanged source-index dependency is locally available before any write.
m.archived('assets/data/territorial-entities/generated/v2/index.json',base);
write('fresh-write-preimage.json',{status:'passed',reviewRevision:bundle.sourceRevision,applicationBaseRevision:base,mainRoot:A,gisRuntimePinPreserved:true,gisConfigSha256:m.sha(gisPinBytes),configBefore,appHeadBefore,selectedSourcePreimagesIdenticalToReviewedInputs:true,approvedDonorIdentical:true,prefixes,transportGuard:'protocol.allow=never; process-only',networkUsed:false});
const journal={status:'starting-source-write',reviewRevision:bundle.sourceRevision,sourceRevision:base,applicationBaseRevision:base,root:A,prefixes,configBefore,gisConfigSha256:m.sha(gisPinBytes),appHeadBefore,results:[],sourceOnly:true,compiled:false,push:false,deployed:false};write('local-source-application.json',journal,'wx');
try{
 rt.withLibraryWrite({root:A,prefixes},lease=>{const prior=process.env.PANDOLAB_LIBRARY_WRITE_LEASE;process.env.PANDOLAB_LIBRARY_WRITE_LEASE=lease.id;try{
  if(m.git('rev-parse','HEAD').toString().trim()!==base||!eq(JSON.parse(fs.readFileSync(A+'/config/library-data.json')),configBefore))throw Error('Archive/pin changed before write');
  for(const {p} of prepared){if(m.h(s.readTerritorialSource(p.entityId))!==p.normalizedEntityPreimageSha256||m.sha(fs.readFileSync(A+'/'+p.sourcePath))!==p.sourceDescriptorPreimageSha256)throw Error('Concurrent source change');const relative=path.relative(fs.realpathSync(lease.view),fs.realpathSync(A+'/'+p.sourcePath));if(relative.startsWith('..')||path.isAbsolute(relative))throw Error('Source is outside canonical write view');}
  for(const {p,n} of prepared){journal.currentEntity=p.entityId;write('local-source-application.json',journal);const result=s.writeTerritorialSource(n),reread=s.readTerritorialSource(p.entityId);if(m.h(reread)!==p.expected.entitySha256||m.sha(fs.readFileSync(A+'/'+p.sourcePath))!==p.expected.descriptorSha256)throw Error('Source readback failed '+p.entityId);journal.results.push({entityId:p.entityId,result,expected:p.expected,sourceReadbackPassed:true});delete journal.currentEntity;write('local-source-application.json',journal);}
 }finally{if(prior===undefined)delete process.env.PANDOLAB_LIBRARY_WRITE_LEASE;else process.env.PANDOLAB_LIBRARY_WRITE_LEASE=prior;}});
 if(!fs.readFileSync(GIS+'/config/library-data.json').equals(gisPinBytes))throw Error('GIS runtime pin unexpectedly changed');
 journal.status='both-local-sources-applied-archive-pending';write('local-source-application.json',journal);console.log(JSON.stringify({status:journal.status,applicationBaseRevision:base,prefixes,entities:journal.results.map(r=>r.entityId),sourceVersions:3}));
}catch(error){journal.status='stopped-inspect-journal-and-live-source-before-retry';journal.error=String(error.stack||error);write('local-source-application.json',journal);throw error;}
