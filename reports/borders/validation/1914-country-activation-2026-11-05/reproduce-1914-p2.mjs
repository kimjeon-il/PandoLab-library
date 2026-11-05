import fs from 'node:fs';import cp from 'node:child_process';import path from 'node:path';import{pathToFileURL}from'node:url';import{createHash}from'node:crypto';
const [appRoot,dataCheckout]=process.argv.slice(2);
if(!appRoot||!dataCheckout)throw Error('Usage: node reproduce-1914-p2.mjs <Pando root> <library Git checkout>');
const moduleAt=rel=>pathToFileURL(path.resolve(appRoot,rel)).href;
const{decodeLibraryArchiveBytes}=await import(moduleAt('tools/library-archive.mjs'));
const{compileBuiltinWorldCatalog}=await import(moduleAt('tools/builtin-world-compiler.mjs'));
const{buildCurrentWorld}=await import(moduleAt('tools/territorial-current-world.mjs'));
const{historicalWorldClipper}=await import(moduleAt('tools/historical-world-territories.mjs'));
const ids=['DEU','ALB','BEL','BGR','CHE','DNK','FRA','GRC','HUN','ITA','LUX','NLD','ROU','austro-hungarian-empire','kingdom-of-serbia','east-prussia','west-prussia'];
const cases=[['before','d2c023082b3e10ed0dc6928f629f190e0756933c',true],['registered','bd62cc8ec6d8221202ed19de0a66f98d3e07ace9',false],['fixed','b6c3c85bba690244829bdec93c58682d9342bda8',true]];
const results=[];
for(const[label,revision,expectedPass]of cases){
 const read=p=>cp.execFileSync('git',['show',revision+':'+p],{cwd:dataCheckout,maxBuffer:32e6});
 const archive=JSON.parse(read('archive/index.json'));
 const get=p=>{const e=archive.files[p];return e?JSON.parse(decodeLibraryArchiveBytes(read(e.stored),e)):null;};
 const paths=ids.map(id=>'assets/data/territorial-entities/source/countries/state-'+id+'.json');
 const entities=paths.map(get).filter(Boolean),entityIds=new Set(entities.map(e=>e.entityId));
 const view=get('assets/data/territorial-entities/source/views/world.json'),policy=get('assets/data/historical-world/policy.json');
 view.selections=view.selections.filter(v=>entityIds.has(v.entityId));
 policy.replacements=policy.replacements.filter(r=>entityIds.has(r.targetEntityId)&&entityIds.has(r.priorityEntityId));
 if(policy.parentRelations)policy.parentRelations=policy.parentRelations.filter(r=>entityIds.has(r.entityId)&&entityIds.has(r.parentEntityId));
 const input=JSON.stringify(entities);let operations=0,last=[];
 const clipper=Object.fromEntries(['intersection','difference','union','xor'].map(op=>[op,(...args)=>{operations++;last.push({op,hashes:args.map(v=>createHash('sha256').update(JSON.stringify(v)).digest('hex'))});if(last.length>3)last.shift();return historicalWorldClipper[op](...args);} ]));
 let status='passed',error=null,countries=null;
 try{countries=compileBuiltinWorldCatalog({entities,view,policy,clipper,currentWorld:buildCurrentWorld({entities,view}),availableSourceIds:new Set(get('assets/data/builtin-world/generated/v1/index.json').sourceIdentities.flatMap(r=>r.sourceFeatureIds))}).countries.length;}
 catch(e){status='failed';error=String(e);}
 if(JSON.stringify(entities)!==input)throw Error('Source inputs mutated');
 const result={label,revision,entities:entities.map(e=>e.entityId),sourceSha256:Object.fromEntries(paths.filter(p=>archive.files[p]).map(p=>[p,archive.files[p].sha256])),operations,countries,status,error,last};results.push(result);
 if((status==='passed')!==expectedPass)throw Error('Unexpected '+label+' result: '+JSON.stringify(result));
 if(!expectedPass&&!/Maximum call stack size exceeded/.test(error))throw Error('Registered pin failed differently');
}
console.log(JSON.stringify({applicationHead:cp.execFileSync('git',['rev-parse','HEAD'],{cwd:appRoot,encoding:'utf8'}).trim(),cases:results},null,2));
