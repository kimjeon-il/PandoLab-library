import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {isDeepStrictEqual as eq} from 'node:util';
import {entity,archived,index,h,gh,sha,archiveEntries} from '../deu-c1-c2-c3-combined/source-review/review-inputs.mjs';
const REV='2af6c0834ac2987a7ffdfe3cde0db1827b04d4e1',O=new URL('.',import.meta.url);
const write=(n,x)=>fs.writeFileSync(new URL(n,O),JSON.stringify(x,null,2)+'\n');
const window=[[50,70.25],[57.5,70.25],[63,73.5],[70,75],[70,77.4],[50,77.4],[50,70.25]];
const donorRecord=entity('RUS',REV),donor=donorRecord.entity.geometryVersions.find(v=>v.versionId==='state:RUS:natural-earth-5.1.1');
const ref='reports/borders/validation/ne-world-map-rebase-2026-11-08/display-review-final-authorized-candidate.geojson';
const approvedBytes=archived(ref,REV),approved=JSON.parse(approvedBytes).features.find(f=>['RUS','state:RUS'].includes(f.id)||['RUS','state:RUS'].some(x=>Object.values(f.properties||{}).includes(x)));
if(!approved||!eq(approved.geometry,donor.geometry))throw Error('Current RUS donor differs from approved original');
const a=entity('soviet-union-russian-sfsr',REV),b=entity('soviet-union',REV);
const wanted=['state:soviet-union-russian-sfsr:1922-12-30-reviewed-v2','state:soviet-union:1922-12-30-reviewed-v2','state:soviet-union:1922-1991-baikonur-r1-after-reviewed-day:caspian-1925-05-13'];
const targets=wanted.map(id=>{const rec=id.includes('russian-sfsr')?a:b;return {rec,v:rec.entity.geometryVersions.find(v=>v.versionId===id)}});
const zipPath='tools/historical-library/sources/ussr-1922-approved/ussr-1922-v2-reviewed-master-20261023.zip',zip=archived(zipPath,REV);
const ne=JSON.parse(archived('assets/data/countries-ne-5.1.1.geojson',REV)).features.find(f=>f.id==='RUS');if(!ne)throw Error('Raw Natural Earth RUS missing');
const p=spawnSync('C:/Users/taeeu/AppData/Local/Programs/Python/Python312/python.exe',['-X','utf8',fileURLToPath(new URL('check-geometry.py',O))],{input:JSON.stringify({window,donor:donor.geometry,ne:ne.geometry,targets:targets.map(({v})=>({id:v.versionId,geometry:v.geometry})),originalZipBase64:zip.toString('base64')}),encoding:'utf8',maxBuffer:120e6});
if(p.status!==0)throw Error(p.stderr||`Python exited ${p.status}`);
const qa=JSON.parse(p.stdout),newCoords=qa.donorIndices.map(i=>donor.geometry.coordinates[i]);
function component(p,i){let b=[180,90,-180,-90];for(const r of p)for(const [x,y] of r)b=[Math.min(b[0],x),Math.min(b[1],y),Math.max(b[2],x),Math.max(b[3],y)];return {index:i,sha256:h(p),bbox:b,rings:p.length,ringSha256:p.map(h),vertices:p.reduce((n,r)=>n+r.length,0)}}
const kg=JSON.parse(fs.readFileSync(new URL('../additional-safe-candidates-20261110/candidate-ledger.json',O))).donorComponents.map(c=>c.sha256);
const ledger={schemaVersion:1,status:'candidate-not-applied',sourceRevision:REV,scope:{name:'Novaya Zemlya entire named archipelago and all approved modern coastal components',selectionPerimeter:window,selectionRole:'Water-separated retrieval only; not a political boundary, clipping operation, ownership proof, or size filter.',oldComponentsPerTarget:6,newComponents:qa.donorIndices.length,discardedModernComponents:0,areaThreshold:null},donor:{entityId:'state:RUS',versionId:donor.versionId,sourceId:donor.sourceId,geometrySha256:gh(donor.geometry),groupGeometrySha256:gh({type:'MultiPolygon',coordinates:newCoords}),sourceDescriptorSha256:donorRecord.descriptorSha256,approvedOriginal:{reference:ref,sha256:sha(approvedBytes)},allCoordinatesAndRingsExactlyEqualApprovedOriginal:true},donorComponents:qa.donorIndices.map(i=>component(donor.geometry.coordinates[i],i)),targets:[],sourceOnly:true,runtimeApproval:false,historicalAccuracyUpgrade:false};
for(const [n,{rec,v}] of targets.entries()){
 const q=qa.targets[n],oldSet=new Set(q.oldIndices),retained=v.geometry.coordinates.filter((_,i)=>!oldSet.has(i)),candidate={...v.geometry,coordinates:[...retained,...newCoords]};
 const beforeHashes=v.geometry.coordinates.map(h),afterHashes=candidate.coordinates.map(h),kgCounts=kg.map(x=>({hash:x,before:beforeHashes.filter(y=>y===x).length,after:afterHashes.filter(y=>y===x).length}));
 ledger.targets.push({entityId:rec.entity.id||('state:'+rec.path.split('state-')[1].replace('.json','')),versionId:v.versionId,validFrom:v.validFrom,validTo:v.validTo,sourcePath:rec.path,sourceDescriptorSha256:rec.descriptorSha256,normalizedEntitySha256:rec.normalizedEntitySha256,versionSha256:h(v),sourceInfoSha256:h(rec.entity.sourceInfo),versionMetadataSha256:h(Object.fromEntries(Object.entries(v).filter(([k])=>k!=='geometry'))),geometrySha256:gh(v.geometry),candidateGeometrySha256:gh(candidate),oldComponents:q.oldIndices.map(i=>component(v.geometry.coordinates[i],i)),retainedComponentsSha256:h(retained),beforePolygonCount:v.geometry.coordinates.length,afterPolygonCount:candidate.coordinates.length,retainedAllRingsByteExact:eq(candidate.coordinates.slice(0,retained.length),retained),donorAllRingsByteExact:eq(candidate.coordinates.slice(retained.length),newCoords),kolguyevAll18RetainedExactly:kgCounts.every(x=>x.before===1&&x.after===1),kolguyevGroupHashes:kg,geometryChecks:q});
}
// Original master serialization is not a preservation preimage: rotation and historical normalization differ.
// Compare its occupied geometry exactly, retaining the unsuccessful byte/normalization comparisons as evidence.
const passes=ledger.targets.every(t=>t.retainedAllRingsByteExact&&t.donorAllRingsByteExact&&t.kolguyevAll18RetainedExactly&&t.geometryChecks.candidateValid&&t.geometryChecks.retainedIntersectionEmpty&&t.geometryChecks.oldBoundaryCrossers.length===0)&&qa.newGroupValid&&qa.donorBoundaryCrossers.length===0&&qa.donorWindowBoundaryIntersections.length===0&&qa.originalEvidence.matches.every(m=>m.oldGroupTopologicallyEqual);
ledger.status=passes?'complete-group-candidate-supported-not-applied':'blocked-see-geometry-checks';
write('candidate-ledger.json',ledger);write('geometry-evidence.json',qa);write('archive-inputs.json',{sourceRevision:REV,entries:archiveEntries(),originalZip:{reference:zipPath,sha256:sha(zip)}});
for(const n of ['candidate-ledger.json','geometry-evidence.json','archive-inputs.json'])JSON.parse(fs.readFileSync(new URL(n,O)));
console.log(JSON.stringify({status:ledger.status,donorComponents:ledger.donorComponents.length,donorGroupHash:ledger.donor.groupGeometrySha256,targets:ledger.targets.map(t=>({versionId:t.versionId,oldIndices:t.oldComponents.map(c=>c.index),candidateGeometrySha256:t.candidateGeometrySha256,valid:t.geometryChecks.candidateValid,retainedIntersectionEmpty:t.geometryChecks.retainedIntersectionEmpty,kolguyevAll18RetainedExactly:t.kolguyevAll18RetainedExactly})),archiveEntries:archiveEntries().length,originalMatches:qa.originalEvidence.matches,readBack:'passed'}));
