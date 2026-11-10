import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';
import {isDeepStrictEqual as eq} from 'node:util';
if(!process.argv.includes('--store'))throw Error('Explicit --store required, only after successful serialized source application.');
const A='D:/dev/PandoLab',GIS='D:/dev/worktrees/gis',O=new URL('.',import.meta.url),root='D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109';
const count=Number(process.env.GIT_CONFIG_COUNT||0);if(!Number.isInteger(count)||count<0||count>1024)throw Error('Unexpected Git environment');process.env.GIT_CONFIG_COUNT=String(count+1);process.env['GIT_CONFIG_KEY_'+count]='protocol.allow';process.env['GIT_CONFIG_VALUE_'+count]='never';process.env.GIT_TERMINAL_PROMPT='0';process.env.GIT_NO_LAZY_FETCH='1';
const m=await import(pathToFileURL(root+'/deu-c1-c2-c3-combined/source-review/review-inputs.mjs')),ctx=await import(pathToFileURL(A+'/tools/data/library-context.mjs')),s=await import(pathToFileURL(A+'/tools/data/territorial-entity-sources.mjs'));
const read=n=>JSON.parse(fs.readFileSync(new URL(n,O))),write=(n,x)=>fs.writeFileSync(new URL(n,O),JSON.stringify(x,null,2)+'\n');
if(fs.existsSync(new URL('local-store-attempt.json',O)))throw Error('A store attempt is already recorded; inspect its outcome, never blindly repeat.');
const application=read('local-source-application.json'),bundle=read('canonical-paired-source-patch.json'),base=application.applicationBaseRevision;
if(application.status!=='both-local-sources-applied-archive-pending'||application.prefixes.length!==5)throw Error('Source application is not complete');
if(m.git('rev-parse','HEAD').toString().trim()!==base||!eq(JSON.parse(fs.readFileSync(A+'/config/library-data.json')),application.configBefore))throw Error('Archive/pin moved since source application; stop for serialized reconciliation');
if(m.git('status','--porcelain').toString().trim())throw Error('Archive has existing edits');
if(m.sha(fs.readFileSync(GIS+'/config/library-data.json'))!==application.gisConfigSha256)throw Error('GIS pin changed unexpectedly');
const view=ctx.libraryMaterializedRoot(A);if(!fs.existsSync(path.join(view,'.complete')))throw Error('Existing complete materialized view required; no fetch fallback');
for(const p of bundle.patches){const before=m.entity(p.entityId.replace('state:',''),base),live=s.readTerritorialSource(p.entityId);if(m.h(before.entity)!==p.normalizedEntityPreimageSha256||m.h(live)!==p.expected.entitySha256||m.sha(fs.readFileSync(A+'/'+p.sourcePath))!==p.expected.descriptorSha256)throw Error('Source preimage/live mismatch before storage');}
m.archived('assets/data/territorial-entities/generated/v2/index.json',base);
const args=['tools/data/library-data.mjs','--store',...application.prefixes.map(p=>'--include-prefix='+p)];
const attempt={status:'starting',baseRevision:base,args,push:false,fetch:false,transportGuard:'process-only protocol.allow=never',compiled:false,sourceOnly:true};write('local-store-attempt.json',attempt);
try{attempt.stdout=execFileSync(process.execPath,args,{cwd:A,env:{...process.env},encoding:'utf8',maxBuffer:1000000});attempt.status='store-returned-success';attempt.revision=m.git('rev-parse','HEAD').toString().trim();write('local-store-attempt.json',attempt);console.log(attempt.stdout);console.log(execFileSync(process.execPath,[fileURLToPath(new URL('verify-archive.mjs',O)),'--verify'],{cwd:A,env:{...process.env},encoding:'utf8',maxBuffer:1000000}));}
catch(error){attempt.status='store-or-readback-stopped-inspect-before-retry';attempt.error=String(error.stack||error);attempt.headAfterFailure=m.git('rev-parse','HEAD').toString().trim();write('local-store-attempt.json',attempt);throw error;}
