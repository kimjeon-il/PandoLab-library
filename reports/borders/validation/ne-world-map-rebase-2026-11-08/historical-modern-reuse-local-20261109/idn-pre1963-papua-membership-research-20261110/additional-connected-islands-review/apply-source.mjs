import fs from 'node:fs';import {pathToFileURL} from 'node:url';import {isDeepStrictEqual as eq} from 'node:util';
const A='D:/dev/PandoLab',root='D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109',dir=root+'/idn-pre1963-papua-membership-research-20261110/additional-connected-islands-review';
if(!process.argv.includes('--apply'))throw Error('Explicit --apply required');
const m=await import(pathToFileURL(root+'/deu-c1-c2-c3-combined/source-review/review-inputs.mjs')),p=JSON.parse(fs.readFileSync(dir+'/canonical-source-patch.json'));
const s=await import(pathToFileURL(A+'/tools/data/territorial-entity-sources.mjs')),rt=await import(pathToFileURL(A+'/tools/data/library-runtime.mjs')),st=await import(pathToFileURL(A+'/tools/data/library-store.mjs'));
if(m.git('rev-parse','HEAD').toString().trim()!==p.sourceRevision||m.git('status','--porcelain').toString().trim())throw Error('Archive changed or dirty');
const pin=JSON.parse(fs.readFileSync(A+'/config/library-data.json')).revision,oldIndex=m.index(p.sourceRevision).files,pinIndex=m.index(pin).files;
const pinNonReportDiff=[...new Set([...Object.keys(oldIndex),...Object.keys(pinIndex)])].filter(f=>!f.startsWith('reports/')&&oldIndex[f]?.sha256!==pinIndex[f]?.sha256);
if(pinNonReportDiff.length)throw Error('Runtime pin differs beyond report checkpoint');
const before=s.readTerritorialSource(p.entityId),archivedBefore=m.entity('IDN',p.sourceRevision);
if(!eq(before,archivedBefore.entity)||m.h(before)!==p.normalizedEntityPreimageSha256||m.sha(fs.readFileSync(A+'/'+p.sourcePath))!==p.sourceDescriptorPreimageSha256)throw Error('Source changed');
const next=structuredClone(before);for(const v of p.replacementVersions)next.geometryVersions[next.geometryVersions.findIndex(x=>x.versionId===v.versionId)]=v;next.sourceInfo.sourceAttributions??=[];next.sourceInfo.sourceAttributions.push(...p.sourceAttributionsAppend);
const n=m.normalize(next);if(m.h(n)!==p.expected.entitySha256||m.assertHistoricalDisplayChanges(n,before)!==1)throw Error('Gate/hash');
const enc=m.encodeTerritorialSource(n),prefixes=[p.sourcePath,...[...enc.geometries.keys()].filter(f=>!fs.existsSync(A+'/assets/data/territorial-entities/source/'+f)).map(f=>'assets/data/territorial-entities/source/'+f)];
if(prefixes.length!==2||prefixes.some(f=>f.startsWith('reports/')))throw Error('Expected exact descriptor and one new geometry only');
let result;rt.withLibraryWrite({root:A,prefixes},lease=>{const prior=process.env.PANDOLAB_LIBRARY_WRITE_LEASE;process.env.PANDOLAB_LIBRARY_WRITE_LEASE=lease.id;try{
 if(m.h(s.readTerritorialSource(p.entityId))!==p.normalizedEntityPreimageSha256||m.sha(fs.readFileSync(A+'/'+p.sourcePath))!==p.sourceDescriptorPreimageSha256)throw Error('Concurrent source change');
 if(!fs.realpathSync(A+'/'+p.sourcePath).toLowerCase().startsWith(lease.view.toLowerCase()))throw Error('View mismatch');
 result=s.writeTerritorialSource(n);
 if(m.h(s.readTerritorialSource(p.entityId))!==p.expected.entitySha256||m.sha(fs.readFileSync(A+'/'+p.sourcePath))!==p.expected.descriptorSha256)throw Error('Local readback');
}finally{if(prior===undefined)delete process.env.PANDOLAB_LIBRARY_WRITE_LEASE;else process.env.PANDOLAB_LIBRARY_WRITE_LEASE=prior;}});
const report={status:'local source applied; archive pending',sourceRevision:p.sourceRevision,previousRuntimePin:pin,pinNonReportDiff,prefixes,result,expected:p.expected,sourceOnly:true,compiled:false,push:false,deployed:false};
fs.writeFileSync(dir+'/local-application.json',JSON.stringify(report,null,2)+'\n',{flag:'wx'});
// Prevent any remote transport even if a lower-level local archive reader encounters a missing object.
const previousAllow=process.env.GIT_ALLOW_PROTOCOL,previousTrace=process.env.GIT_TRACE;process.env.GIT_ALLOW_PROTOCOL='file';process.env.GIT_TRACE=dir+'/storage-git-trace.log';
let revision;try{if(m.git('rev-parse','HEAD').toString().trim()!==p.sourceRevision)throw Error('Archive changed before store');revision=st.storeLibraryData({root:A,push:false,prefixes});}finally{if(previousAllow===undefined)delete process.env.GIT_ALLOW_PROTOCOL;else process.env.GIT_ALLOW_PROTOCOL=previousAllow;if(previousTrace===undefined)delete process.env.GIT_TRACE;else process.env.GIT_TRACE=previousTrace;}
const rec=m.entity('IDN',revision),now=m.index(revision).files,changed=[...new Set([...Object.keys(oldIndex),...Object.keys(now)])].filter(f=>oldIndex[f]?.sha256!==now[f]?.sha256);
if(m.h(rec.entity)!==p.expected.entitySha256||rec.descriptorSha256!==p.expected.descriptorSha256||!eq([...changed].sort(),[...prefixes].sort()))throw Error('Archive readback/diff');
const codec=m.encodeTerritorialSource(rec.entity);if(!eq(m.normalize(m.decodeTerritorialSource(codec.descriptor,f=>codec.geometries.get(f))),rec.entity)||m.assertHistoricalDisplayChanges(rec.entity,before)!==1)throw Error('Archived gate/codec');
for(const v of before.geometryVersions)if(!p.replacementVersions.some(x=>x.versionId===v.versionId)&&!eq(v,rec.entity.geometryVersions.find(x=>x.versionId===v.versionId)))throw Error('Other IDN version changed');
const afterGeometry=rec.entity.geometryVersions.find(v=>v.versionId===p.replacementVersions[0].versionId).geometry,replay=JSON.parse(fs.readFileSync(dir+'/independent-replay-proof.json')),hashes=new Set(afterGeometry.coordinates.map(m.h));
if(!replay.existing624.every(x=>hashes.has(x.coordinateSha256))||!replay.restored450.every(x=>hashes.has(x.coordinateSha256))||!replay.untouched797.every(x=>hashes.has(x.coordinateSha256)))throw Error('Archived coordinate preservation');
const trace=fs.readFileSync(dir+'/storage-git-trace.log','utf8');if(/built-in: git (?:[^\n]* )?(fetch|push|ls-remote)\b/.test(trace)||/run_command:.*(?:remote-https|remote-http|ssh)/.test(trace))throw Error('Unexpected network command in trace');
if(!replay.pendingGroups.every(x=>hashes.has(x.coordinateSha256)))throw Error('Pending six groups changed');
const proof={pendingSixGroupsPreserved:true,earlierSixAppliedDonorsPreserved:true,status:'verified locally archived',previousRevision:p.sourceRevision,revision,previousRuntimePin:pin,currentRuntimePin:JSON.parse(fs.readFileSync(A+'/config/library-data.json')).revision,changedLogicalPaths:changed,otherLogicalDiff:0,reportLogicalDiff:0,allExistingReportsPreserved:true,archiveReadback:true,historicalSourceGate:1,codecRoundtrip:true,allOtherIDNVersionsExact:true,existingModern624Preserved:true,restored450Preserved:true,untouched797Preserved:true,remainingOriginalNE:171,unchangedModifiedSharedMainlands:2,expected:p.expected,storageGitTraceSha256:m.sha(Buffer.from(trace)),remoteGitCommands:0,sourceOnly:true,push:false,compiled:false,deployed:false,completeModernMinusPapuaCertified:false};
fs.writeFileSync(dir+'/local-archive.json',JSON.stringify(proof,null,2)+'\n');if(!eq(JSON.parse(fs.readFileSync(dir+'/local-archive.json')),proof))throw Error('Proof reread');console.log(JSON.stringify(proof,null,2));
