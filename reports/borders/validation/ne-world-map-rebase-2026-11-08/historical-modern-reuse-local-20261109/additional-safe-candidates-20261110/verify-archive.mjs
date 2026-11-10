import fs from 'node:fs';
import {pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';
import {isDeepStrictEqual as eq} from 'node:util';
if(!process.argv.includes('--verify'))throw Error('Explicit --verify required');
const A='D:/dev/PandoLab',GIS='D:/dev/worktrees/gis',O=new URL('.',import.meta.url),root='D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109';
const m=await import(pathToFileURL(root+'/deu-c1-c2-c3-combined/source-review/review-inputs.mjs')),s=await import(pathToFileURL(A+'/tools/data/territorial-entity-sources.mjs'));
const read=n=>JSON.parse(fs.readFileSync(new URL(n,O))),write=(n,x)=>fs.writeFileSync(new URL(n,O),JSON.stringify(x,null,2)+'\n');
const bundle=read('canonical-paired-source-patch.json'),application=read('local-source-application.json'),ledger=read('candidate-ledger.json'),base=application.applicationBaseRevision,rev=m.git('rev-parse','HEAD').toString().trim();
if(rev===base)throw Error('No archive commit to verify');if(m.git('rev-parse',rev+'^').toString().trim()!==base)throw Error('Archive parent mismatch; inspect concurrent stores');
const beforeIndex=m.index(base).files,afterIndex=m.index(rev).files,changed=[...new Set([...Object.keys(beforeIndex),...Object.keys(afterIndex)])].filter(p=>beforeIndex[p]?.sha256!==afterIndex[p]?.sha256).sort();
if(!eq(changed,[...application.prefixes].sort())||changed.length!==5)throw Error('Logical diff is not the exact five authorized source paths');
const donor=m.entity('RUS',rev).entity.geometryVersions.find(v=>v.versionId===ledger.donor.versionId);if(m.gh(donor.geometry)!==ledger.donor.geometrySha256)throw Error('Donor changed');
const dps=ledger.donorComponents.map(p=>donor.geometry.coordinates[p.index]),rows=[];
for(const p of bundle.patches){const rec=m.entity(p.entityId.replace('state:',''),rev),before=m.entity(p.entityId.replace('state:',''),base),live=s.readTerritorialSource(p.entityId);if(m.h(before.entity)!==p.normalizedEntityPreimageSha256||m.h(rec.entity)!==p.expected.entitySha256||rec.descriptorSha256!==p.expected.descriptorSha256||!eq(rec.entity,live))throw Error('Archive/source identity mismatch');
 if(m.assertHistoricalDisplayChanges(rec.entity,before.entity)!==p.replacementVersions.length)throw Error('Archived source gate');
 const enc=m.encodeTerritorialSource(rec.entity);if(!eq(m.normalize(m.decodeTerritorialSource(enc.descriptor,f=>enc.geometries.get(f))),rec.entity))throw Error('Archive codec mismatch');
 const ids=new Set(p.replacementVersions.map(v=>v.versionId));for(const old of before.entity.geometryVersions){const now=rec.entity.geometryVersions.find(v=>v.versionId===old.versionId);if(!ids.has(old.versionId)&&!eq(old,now))throw Error('Unselected version changed');}
 for(const exp of p.expected.versions){const now=rec.entity.geometryVersions.find(v=>v.versionId===exp.versionId),old=before.entity.geometryVersions.find(v=>v.versionId===exp.versionId),target=ledger.targets.find(t=>t.entityId===p.entityId&&t.versionId===exp.versionId),omit=new Set(target.oldComponents.map(c=>c.index));
  if(m.h(now)!==exp.versionSha256||m.gh(now.geometry)!==exp.geometrySha256||!eq(now.geometry.coordinates,[...old.geometry.coordinates.filter((p,i)=>!omit.has(i)),...dps]))throw Error('Exact component replay failed');
  for(const key of Object.keys(old))if(!['geometry','notes','historicalProvenance'].includes(key)&&!eq(now[key],old[key]))throw Error('Historical metadata changed');for(const [key,value] of Object.entries(old.historicalProvenance||{}))if(key!=='displayDetailReview'&&!eq(now.historicalProvenance[key],value))throw Error('Inherited provenance changed');if(!now.notes.startsWith(old.notes||''))throw Error('Original notes not preserved');
  rows.push({entityId:p.entityId,versionId:exp.versionId,expected:exp,archiveReadback:true,liveReadback:true,gate:1,codecRoundtrip:true,retainedCoordinatesExact:true,all18DonorPolygonsAndRingsExact:true,originalDatesSourceCertaintyAndInheritedProvenancePreserved:true});
 }
}
const pin=JSON.parse(fs.readFileSync(A+'/config/library-data.json'));if(!eq(pin,{...application.configBefore,revision:rev}))throw Error('Main config changed beyond revision');if(m.sha(fs.readFileSync(GIS+'/config/library-data.json'))!==application.gisConfigSha256)throw Error('GIS runtime pin changed');
const appHead=execFileSync('git',['-C',A,'rev-parse','HEAD'],{encoding:'utf8',env:{...process.env,GIT_NO_LAZY_FETCH:'1'}}).trim();if(appHead!==application.appHeadBefore)throw Error('Application HEAD moved; inspect unrelated concurrent activity');
const result={schemaVersion:1,status:'local-source-archive-verified',reviewRevision:bundle.sourceRevision,previousRevision:base,revision:rev,parent:base,changedLogicalPaths:changed,historicalVersionsChecked:3,rows,mainConfigPin:pin.revision,mainConfigOnlyRevisionChanged:true,gisRuntimePinUnchanged:true,applicationCodeCommitCreated:false,sourceOnly:true,reportsArchivedInThisCommit:false,push:false,fetch:false,compiled:false,deployed:false};
write('local-archive-commit.json',result);const reread=read('local-archive-commit.json');if(!eq(result,reread))throw Error('Report readback mismatch');console.log(JSON.stringify(result));
