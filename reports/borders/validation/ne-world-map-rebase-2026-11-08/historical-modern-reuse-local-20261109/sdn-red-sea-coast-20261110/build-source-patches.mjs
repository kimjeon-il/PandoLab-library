// Preparation only. All writes stay in this research folder, never territorial source.
import fs from 'node:fs';
import {isDeepStrictEqual as eq} from 'node:util';
import {pathToFileURL} from 'node:url';
const dir='D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/sdn-red-sea-coast-20261110';
const can='reports/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/sdn-red-sea-coast-20261110';
const m=await import(pathToFileURL(dir+'/../deu-c1-c2-c3-combined/source-review/review-inputs.mjs'));
const read=n=>JSON.parse(fs.readFileSync(dir+'/'+n));
const write=(n,x)=>fs.writeFileSync(dir+'/'+n,JSON.stringify(x,null,2)+'\n');
const ref=n=>({reference:can+'/'+n,sha256:m.sha(fs.readFileSync(dir+'/'+n))});
const rev=m.git('rev-parse','HEAD').toString().trim();
const archiveRef=p=>({reference:p,revision:rev,sha256:m.index(rev).files[p].sha256});
const snapshot=read('modern-union-inputs.json'),rec=m.entity('SDN',rev),sds=m.entity('SDS',rev),peer=read('scoped-peer-geometries.json');
if(!eq(rec.entity,snapshot.records.SDN.entity)||!eq(sds.entity,snapshot.records.SDS.entity))throw Error('Input sources changed');
for(const p of peer.peers)if(m.entity(p.id,rev).descriptorSha256!==p.sourceSha256)throw Error('Peer changed '+p.id);
const before=rec.entity.geometryVersions[0],donor=rec.entity.geometryVersions[1],oldRing=before.geometry.coordinates[0][0];
const originalPath='reports/borders/validation/ne-world-map-rebase-2026-11-08/display-review-final-authorized-candidate.geojson';
const original=JSON.parse(m.archived(originalPath,rev));
for(const [id,v] of [['SDN',donor],['SDS',sds.entity.geometryVersions[0]]]){
 const f=original.features.find(f=>[id,'state:'+id].includes(f.id)||Object.values(f.properties||{}).includes(id));
 if(!f||!eq(f.geometry,v.geometry))throw Error('Approved donor mismatch '+id);
}
const limits=[
 'The existing historical version is exactly a modern NE SDN+SDS successor union, not an independently reconstructed historical boundary.',
 'An approved-modern source update does not prove historical control or title across 1956-01-01..2011-07-08.',
 'Halaib/Bir Tawil, al-Fashaga, Wadi Halfa and Ilemi limitations remain explicit. Matching inclusion conventions does not establish identical historical boundary routes.',
 'No whole-world or runtime/compiled historical validation was performed. Source application requires a fresh parent review and preimage check.'
];
const results=[];
for(const safe of [true,false]){
 const prefix=safe?'safe-coast':'full-union';
 const file=safe?'safe-coast-all-sdn-components-candidate.geojson':'full-modern-union-candidate.geojson';
 const candidate=read(file),topo=read(prefix+'-topology-and-projection.json');
 if(!topo.candidateValid||!topo.operationReplaySymmetricDifferenceEmpty||!topo.all45SdnDetachedComponentsExact)throw Error('Candidate proof failed');
 if(safe&&(!topo.allOriginalPoliticalEdgesExact||!topo.all45SdnComponentLocation.allStrictlyWithinRedSeaDiagnosticEnvelope||topo.sharedBoundaryAndOverlap.some(x=>!x.sharedBoundaryDifferenceEmpty||!x.exactExpectedOverlapPreserved||x.changedRegionIntersectsPeer)||topo.legacyNEPeerSharedBoundaryChecks.some(x=>!x.sharedDifferenceEmpty||!x.overlapIdentical)))throw Error('Safe preservation proof failed');
 const visual={schemaVersion:1,status:'reviewed-source-display-only',actualImagesOpened:1,images:[ref(prefix+'-source-scale.png')],projection:ref(prefix+'-topology-and-projection.json'),observations:safe?[
  'Original political exterior and its distinctive northern and southern routes coincide in the overlay. Only the Red Sea coast and donor non-mainland components change.',
  'Northern Egypt/Halaib and southern Eritrea coastline junctions remain attached to the original political exterior.',
  'All 45 donor components are in the Red Sea geographic envelope. Tiny components are preserved numerically, not individually certified by nominal-scale pixels.'
 ]:[
  'The whole union keeps the recognizable united Sudan macro outline, including the Wadi Halfa salient and Bir Tawil exclusion.',
  'Exterior coordinate changes exist along several land borders and the coast. This image does not establish their historical meaning.',
  'The CAF raw strict shared-contact diagnostic remains unresolved; nominal-scale visual similarity does not resolve it.'
 ],historicalAccuracyVerified:false,physicalDisplayScaleCalibrated:false,sourceApplied:false};
 write(prefix+'-visual-review.json',visual);
 const provenance={schemaVersion:1,sourceRevision:rev,status:safe?'prepared-safe-partial-source-patch':'held-full-modern-union-alternative',sourceEntity:archiveRef(rec.path),originalVersionSha256:m.h(before),originalGeometrySha256:m.gh(before.geometry),originalGeometry:archiveRef('assets/data/territorial-entities/source/'+rec.descriptor.geometryVersions[0].geometryResource.file),originalSourceInfo:rec.entity.sourceInfo,originalHistoricalProvenance:before.historicalProvenance,approvedDonor:archiveRef(originalPath),donorVersions:[{entityId:rec.entity.entityId,versionId:donor.versionId,geometrySha256:m.gh(donor.geometry)},{entityId:sds.entity.entityId,versionId:sds.entity.geometryVersions[0].versionId,geometrySha256:m.gh(sds.entity.geometryVersions[0].geometry)}],candidate:ref(file),basis:ref('political-model-review.md'),politicalComparison:ref('political-inclusion-comparison.json'),topology:ref(prefix+'-topology-and-projection.json'),limits:[...limits,...topo.limits],scope:safe?'Replace source mainland vertices 222..421 using two source/donor intersections and exact donor vertices 940..1646; replace the single old offshore component with all 45 approved SDN components. All political edges and both coastline junctions remain exact. This is not the full SDN+SDS union.':'Replace the complete inherited NE successor-union display proxy with the exact approved-modern SDN+SDS union, retaining every component. Pending strict CAF shared-contact diagnosis and final policy review; not applied.',sourceApplied:false,rights:rec.entity.sourceInfo.license};
 write(prefix+'-source-provenance.json',provenance);
 const replacement=structuredClone(before);
 replacement.geometry=structuredClone(candidate.geometry);
 replacement.historicalProvenance??={};
 const method='preserved-modern-source';
 replacement.historicalProvenance.displayDetailReview={schemaVersion:1,status:safe?'passed':'pending',entityId:rec.entity.entityId,versionId:before.versionId,validFrom:before.validFrom,validTo:before.validTo,geometrySha256:m.gh(candidate.geometry),master:archiveRef(originalPath),source:ref(prefix+'-source-provenance.json'),comparison:{reference:archiveRef('assets/data/countries-ne-5.1.1.geojson'),arcSha256:ref(prefix+'-projected-candidate-boundary.wkb').sha256,extent:topo.projection.projectedExtent,extentUnits:'metre',scaleDenominator:10000000,projection:{definition:topo.projection.definition,units:'metre',evidence:ref(prefix+'-topology-and-projection.json')}},method,reason:safe?'Adopt the exact common interior modern Red Sea coast and all 45 modern SDN non-mainland components, preserving original political borders, dates, source notes, and historical uncertainty.':'Candidate replacement of the exact inherited modern NE successor-union proxy with its complete approved-modern equivalent; historical accuracy is not upgraded, and strict CAF shared-contact evidence remains unresolved.',parameters:safe?{operation:'intersection-clipped coast subarc plus complete donor component set',oldVertexSpan:[222,421],exactDonorVertexSpan:[940,1646],donorPolygonIndices:Array.from({length:45},(_,i)=>i+1),omittedDonorPolygons:[],additionalSimplification:null,coordinateRounding:null,protectedOriginalPoliticalEdges:true,allModernComponentsClaimed:false}:{operation:'exact unary union of complete approved SDN and SDS geometries',inputComponents:57,outputComponents:49,omittedComponents:[],additionalSimplification:null,coordinateRounding:null,donorUnionSymmetricDifferenceEmpty:true},visual:ref(prefix+'-visual-review.json'),topology:{status:safe?'passed':'pending',evidence:ref(prefix+'-topology-and-projection.json'),checks:['validity','shared-boundary','union','gaps-overlaps','connectivity','holes-islands','dates'],scope:safe?'The selected coast operation replays exactly, all 45 donor components are retained, and every original political edge plus all old/current scoped peer overlaps and shared lines remain unchanged. Existing old-to-current neighbor mismatch is preserved, not repaired. Dates are retained, not newly inferred.':'Complete union equality and all component coverage pass; nine modern shared contacts match strictly, but CAF raw strict contact segmentation remains unresolved. No historical correspondence is established.'},counterpartVersions:peer.peers.flatMap(p=>p.versions.map(v=>({entityId:p.entityId,versionId:v.versionId,geometrySha256:v.geometrySha256}))),fixedAnchors:safe?[oldRing[219],oldRing[222],oldRing[421],oldRing[430]]:[],historicalAccuracyVerified:false,fullPeriodDatedCounterpartClosureVerified:false,compiledDerivatives:[],sourceApplied:false};
 const updateKey=safe?'modernRedSeaCoastAndAllComponentsReuse':'modernSuccessorUnionCandidate';
 replacement.historicalProvenance[updateKey]={sourceReview:ref(prefix+'-source-provenance.json'),originalSourceId:before.sourceId,originalVersionSha256:m.h(before),historicalAccuracyVerified:false,existingNotesAndCertaintyPreserved:true,limitations:limits,scope:provenance.scope};
 if(!safe)replacement.sourceId='approved-current-world-display-20261107-historical-successor-union';
 const attribution={sourceId:safe?'sdn-red-sea-coast-all-components-20261110':'sdn-complete-modern-successor-union-candidate-20261110',geometryVersionId:before.versionId,sourceReview:ref(prefix+'-source-provenance.json'),role:safe?'Partial interior coast and all approved SDN Red Sea components; inherited political boundaries unchanged.':'Prepared full modern proxy replacement only; historical accuracy not established; source application held.',historicalAccuracyVerified:false};
 const next=structuredClone(rec.entity);next.geometryVersions[0]=replacement;next.sourceInfo.sourceAttributions??=[];next.sourceInfo.sourceAttributions.push(attribution);
 const normalized=m.normalize(next),enc=m.encodeTerritorialSource(normalized),round=m.normalize(m.decodeTerritorialSource(enc.descriptor,p=>enc.geometries.get(p)));
 if(!eq(normalized,round))throw Error('Codec roundtrip failed');
 if(!eq(normalized.geometryVersions[1],rec.entity.geometryVersions[1]))throw Error('Modern version changed');
 if(!eq(normalized.lifetime,rec.entity.lifetime)||replacement.validFrom!==before.validFrom||replacement.validTo!==before.validTo||replacement.notes!==before.notes||replacement.certainty!==before.certainty)throw Error('Historical metadata changed');
 const stripVersion=v=>{const x=structuredClone(v);delete x.geometry;delete x.historicalProvenance.displayDetailReview;delete x.historicalProvenance[updateKey];if(!safe)x.sourceId=before.sourceId;return x;};
 if(!eq(stripVersion(replacement),stripVersion(before)))throw Error('Unpermitted pre-existing version metadata changed');
 let checked=0,gateError=null;try{checked=m.assertHistoricalDisplayChanges(normalized,rec.entity);}catch(error){gateError=error.message;}
 if(safe&&(checked!==1||gateError))throw Error('Safe historical display gate failed: '+gateError);
 if(!safe&&!gateError)throw Error('Held full candidate must not pass unresolved review');
 const expected={entitySha256:m.h(normalized),descriptorSha256:m.sha(Buffer.from(JSON.stringify(enc.descriptor,null,2)+'\n')),geometrySha256:m.gh(replacement.geometry),geometryResource:enc.descriptor.geometryVersions[0].geometryResource};
 const patch={schemaVersion:1,status:safe?'ready-for-parent-preapplication-review':'held-unresolved-full-union-review',sourceRevision:rev,entityId:rec.entity.entityId,sourcePath:rec.path,sourceDescriptorPreimageSha256:rec.descriptorSha256,normalizedEntityPreimageSha256:m.h(rec.entity),sourceVersionPreimageSha256:m.h(before),replacementVersions:[replacement],sourceAttributionsAppend:[attribution],expected,sourceApplied:false};
 write(prefix+'-canonical-source-patch.json',patch);
 const proof={schemaVersion:1,status:safe?'passed-for-scoped-source-change':'expected-rejection-for-unresolved-full-review',sourceRevision:rev,sourceGateModuleSha256:m.sha(fs.readFileSync('D:/dev/PandoLab/tools/gis/historical-display-review.mjs')),gateMethod:method,changedHistoricalVersionsChecked:checked,gateError,codecRoundtrip:true,otherVersionExact:true,allExistingVersionMetadataExactExceptDocumentedAdditions:true,datesAndLifetimeExact:true,existingNotesAndCertaintyExact:true,sourceInfoChange:'One explicit attribution appended only',expected,scopeWarning:'The gate checks input-bound review receipt structure and identity. It does not independently prove historical correctness or authorize source application.',sourceApplied:false};
 write(prefix+'-source-gate-proof.json',proof);
 const reread=read(prefix+'-canonical-source-patch.json');if(!eq(reread,patch))throw Error('Patch readback mismatch');
 results.push({prefix,status:proof.status,checked,gateError,codecRoundtrip:true,geometrySha256:expected.geometrySha256,patch:ref(prefix+'-canonical-source-patch.json')});
}
write('prepared-source-patches-summary.json',{createdAt:new Date().toISOString(),sourceRevision:rev,sourceApplied:false,results});
console.log(JSON.stringify(results));
