import fs from 'node:fs';
import {pathToFileURL} from 'node:url';
import {isDeepStrictEqual as eq} from 'node:util';
import {entity,h,gh,sha} from '../deu-c1-c2-c3-combined/source-review/review-inputs.mjs';
const O=new URL('.',import.meta.url),ledger=JSON.parse(fs.readFileSync(new URL('candidate-ledger.json',O)));
export const sourceRevision=ledger.sourceRevision;
export const donorIndices=ledger.donorComponents.map(c=>c.index);
const donor=entity('RUS',sourceRevision).entity.geometryVersions.find(v=>v.versionId===ledger.donor.versionId);
if(gh(donor.geometry)!==ledger.donor.geometrySha256)throw Error('Novaya donor preimage changed');
export const donorCoordinates=donorIndices.map((i,j)=>{const p=donor.geometry.coordinates[i];if(h(p)!==ledger.donorComponents[j].sha256)throw Error('Novaya donor component changed');return p});
export function removeLegacyGroup(geometry,versionId){
 const target=ledger.targets.find(t=>t.versionId===versionId);if(!target)throw Error('Unapproved Novaya target');
 const hashes=geometry.coordinates.map(h),remove=new Set();
 for(const old of target.oldComponents){const hits=hashes.flatMap((x,i)=>x===old.sha256?[i]:[]);if(hits.length!==1)throw Error('Novaya original component missing or ambiguous '+old.index);remove.add(hits[0]);}
 return {...geometry,coordinates:geometry.coordinates.filter((_,i)=>!remove.has(i))};
}
export function replayNovayaZemlya(geometry,versionId){const retained=removeLegacyGroup(geometry,versionId);return {...retained,coordinates:[...retained.coordinates,...donorCoordinates]};}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const proofs=[];
 for(const t of ledger.targets){const rec=entity(t.entityId.replace('state:',''),sourceRevision),v=rec.entity.geometryVersions.find(v=>v.versionId===t.versionId);if(rec.descriptorSha256!==t.sourceDescriptorSha256||h(v)!==t.versionSha256)throw Error('Novaya target preimage changed');const result=replayNovayaZemlya(v.geometry,t.versionId);if(gh(result)!==t.candidateGeometrySha256||!eq(result.coordinates.slice(-757),donorCoordinates))throw Error('Novaya replay differs');proofs.push({entityId:t.entityId,versionId:t.versionId,oldIndices:t.oldComponents.map(c=>c.index),candidateGeometrySha256:gh(result),exactReplay:true});}
 const vb=fs.readFileSync(new URL('../vaygach-mainland-contact-review-20261110/paired-coast-operation.json',O)),v=JSON.parse(vb),intersection=donorIndices.filter(i=>v.donorComponentIndices.includes(i));
 if(v.sourceRevision!==sourceRevision||intersection.length||new Set(v.donorComponentIndices).size!==52)throw Error('Vaygach donor conflict or revision mismatch');
 const operation={schemaVersion:1,status:'stable-geometry-operation-for-combined-preparation-only',sourceRevision,scope:ledger.scope,donor:ledger.donor,donorComponentIndices:donorIndices,donorComponentLedger:{reference:'candidate-ledger.json',sha256:sha(fs.readFileSync(new URL('candidate-ledger.json',O)))},targets:ledger.targets.map(t=>({entityId:t.entityId,versionId:t.versionId,validFrom:t.validFrom,validTo:t.validTo,sourceDescriptorPreimageSha256:t.sourceDescriptorSha256,versionPreimageSha256:t.versionSha256,geometryPreimageSha256:t.geometrySha256,oldComponents:t.oldComponents,standaloneCandidateGeometrySha256:t.candidateGeometrySha256})),replay:'Match each of the six complete old component coordinate hashes exactly once, remove those complete polygons, preserve every remaining coordinate array; append all 757 full donor polygons. For a combined patch choose one fixed merged donor ordering after independent operation selection.',combinedOrderingCaution:'Sequential append orders differ in MultiPolygon array order. Use retained original order plus combined donor index order, or compare independent replay component multisets before deterministic final assembly. Do not silently reuse stale full replacement versions.',sourceWritten:false,gateOrCodecClaimed:false};
 const proof={schemaVersion:1,status:'passed-for-novaya-operation-and-donor-disjointness-only',sourceRevision,proofs,donor757Count:donorIndices.length,vaygach52Count:v.donorComponentIndices.length,donorIndexIntersection:intersection,combinedDistinctDonors:new Set([...donorIndices,...v.donorComponentIndices]).size,vaygachOperationSha256:sha(vb),combinedGeometryValidated:false,sourceWritten:false};
 for(const [name,data] of [['whole-group-operation.json',operation],['operation-replay-proof.json',proof]]){fs.writeFileSync(new URL(name,O),JSON.stringify(data,null,2)+'\n');JSON.parse(fs.readFileSync(new URL(name,O)));}
 console.log(JSON.stringify(proof));
}
