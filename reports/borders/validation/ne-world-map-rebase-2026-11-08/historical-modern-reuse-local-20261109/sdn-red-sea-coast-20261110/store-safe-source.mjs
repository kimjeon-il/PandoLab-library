import fs from 'node:fs';import {execFileSync} from 'node:child_process';import {pathToFileURL} from 'node:url';
import * as m from '../deu-c1-c2-c3-combined/source-review/review-inputs.mjs';
const O=new URL('./',import.meta.url),read=n=>JSON.parse(fs.readFileSync(new URL(n,O))),a=read('local-source-application.json'),p=read('safe-coast-canonical-source-patch.json');
const s=await import(pathToFileURL(m.A+'/tools/data/territorial-entity-sources.mjs'));
if(!process.argv.includes('--store'))throw Error('Explicit --store required');
if(fs.existsSync(new URL('store-command-result.json',O)))throw Error('Prior store result exists; inspect rather than retry');
if(m.git('rev-parse','HEAD').toString().trim()!==a.headBefore||m.git('status','--porcelain').toString().trim())throw Error('Archive state changed');
if(m.sha(fs.readFileSync(m.A+'/config/library-data.json'))!==a.appConfigBeforeSha256||m.h(s.readTerritorialSource(p.entityId))!==p.expected.entitySha256)throw Error('Pin or applied source changed');
if(m.assertHistoricalDisplayChanges(s.readTerritorialSource(p.entityId),m.entity('SDN',a.headBefore).entity)!==1)throw Error('Pre-store gate');
// Confirm the store's only additional data dependency is already local. No full-country hydration.
m.archived('assets/data/territorial-entities/generated/v2/index.json',a.headBefore);
const args=[m.A+'/tools/data/library-data.mjs','--store',...a.prefixes.map(v=>'--include-prefix='+v)],env={...process.env,GIT_NO_LAZY_FETCH:'1'};
const count=Number(env.GIT_CONFIG_COUNT||0);if(!Number.isInteger(count)||count<0)throw Error('Invalid Git environment count');
env.GIT_CONFIG_COUNT=String(count+1);env['GIT_CONFIG_KEY_'+count]='protocol.allow';env['GIT_CONFIG_VALUE_'+count]='never';
let result;
try{const stdout=execFileSync(process.execPath,args,{cwd:m.A,env,encoding:'utf8',maxBuffer:2e6,stdio:['ignore','pipe','pipe']});result={status:'store-command-succeeded',arguments:args,stdout,headAfter:m.git('rev-parse','HEAD').toString().trim(),checkedAt:new Date().toISOString(),networkProtocolsDisabledForCommand:true};}
catch(e){result={status:'store-command-failed-inspect-outcome-before-retry',arguments:args,exitStatus:e.status,stdout:String(e.stdout||''),stderr:String(e.stderr||''),headAfter:m.git('rev-parse','HEAD').toString().trim(),checkedAt:new Date().toISOString()};}
fs.writeFileSync(new URL('store-command-result.json',O),JSON.stringify(result,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify(result,null,2));if(result.status!=='store-command-succeeded')process.exitCode=1;
