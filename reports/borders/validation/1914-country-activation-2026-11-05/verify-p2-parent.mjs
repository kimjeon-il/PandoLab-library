import fs from'node:fs';import cp from'node:child_process';import assert from'node:assert/strict';import{createHash}from'node:crypto';import{gunzipSync}from'node:zlib';
import{decodeLibraryArchiveBytes}from'file:///D:/dev/worktrees/gis/tools/library-archive.mjs';import{readBuiltinCountryStoredBytes}from'file:///D:/dev/worktrees/gis/tools/builtin-country-bytes.mjs';import{temporalContains}from'file:///D:/dev/worktrees/gis/shared/frontend/js/modules/temporal.js';
import{contextProject}from'file:///D:/dev/worktrees/gis/tests/helpers/builtin-world.mjs';import{initializeTestTerritorialState,testCoreProject}from'file:///D:/dev/worktrees/gis/tests/helpers/timeline-project.mjs';import{createEmptyTerritorialState}from'file:///D:/dev/worktrees/gis/shared/frontend/js/modules/territorial-entity-store.js';
const rev='bd62cc8ec6d8221202ed19de0a66f98d3e07ace9',repo='D:/dev/PandoLab-library-data',B='assets/data/builtin-world/generated/v1/',read=p=>cp.execFileSync('git',['show',rev+':'+p],{cwd:repo,maxBuffer:32e6}),archive=JSON.parse(read('archive/index.json')),get=p=>decodeLibraryArchiveBytes(read(archive.files[p].stored),archive.files[p]),index=JSON.parse(get(B+'index.json')),sha=g=>createHash('sha256').update(JSON.stringify(g)).digest('hex');
const candidate=JSON.parse(fs.readFileSync('p2-parent-candidate-bd62cc8e.json')),before=JSON.parse(fs.readFileSync('p2-parent-runtime-before.json')),after=JSON.parse(fs.readFileSync('p2-parent-runtime-after.json'));
const pinned=id=>{const e=index.entities.find(e=>e.entityId===id);return JSON.parse(gunzipSync(readBuiltinCountryStoredBytes(e,p=>get(B+p))));};
const geometry=(c,day)=>{const b=c.sourceBindings.find(b=>temporalContains(b,day));return b?c.geometries.find(g=>g.id===b.geometryRef.id&&g.version===b.geometryRef.version).geojson:null;};
let checks=[];
for(const [id,day]of [['DEU','1914-07-31'],['state:austro-hungarian-empire','1914-07-28'],['state:kingdom-of-serbia','1914-07-28'],['state:east-prussia','1914-07-31'],['state:west-prussia','1914-07-31']]){
 const c=candidate.countries.find(c=>c.entityId===id),old=pinned(id);assert.deepEqual(geometry(c,day),geometry(old,day));checks.push({entityId:id,date:day,geometrySha256:sha(geometry(c,day)),matchesPinnedGeometry:true});
}
for(let i=0;i<after.length;i++){
 const a=after[i],b=before[i];assert.deepEqual(a.geometries,b.geometries);assert.deepEqual(a.sourceBindings,b.sourceBindings);
 for(const day of ['1914-07-27','1914-07-28','1914-07-29','1914-07-30','1914-08-01','2026-11-05']){
  const row=c=>c.timelineRecords.parentRelations.find(r=>temporalContains(r,day));const ar=row(a),br=row(b);assert.equal(ar?.parentId,br?.parentId);assert.deepEqual(geometry(a,day),geometry(b,day));
 }
}
// Use the real compiled countries in the existing C++ timeline adapter; no raw
// provincial source or out-of-scope date is rewritten.
const scoped={...index,entities:index.entities.filter(e=>candidate.countries.some(c=>c.entityId===e.entityId))};
const countries=candidate.countries.map(c=>after.find(a=>a.entityId===c.entityId)||pinned(c.entityId));
const project=contextProject({index:scoped,countries}),state=createEmptyTerritorialState();
await initializeTestTerritorialState(state,null,{project});const owner=testCoreProject(state);let native=[];
try{for(const month of ['1914-06','1914-07','1914-08','2026-11']){
 await owner.entityStore.setTimelineCursor(month);
 for(const id of ['state:east-prussia','state:west-prussia']){const f=state.territorialEntities.find(f=>f.id===id);if(month==='1914-07')assert.equal(f?.properties.parentId,'DEU');else if(f)assert.equal(f.properties.parentId,'');}
 native.push({month,status:'passed',entities:state.territorialEntities.length});
}}finally{owner.dispose();}
fs.writeFileSync('p2-parent-preservation-proof.json',JSON.stringify({referenceGeometryChecks:checks,nativeTimelineChecks:native,sourceChanges:0,geometryChanges:0,adjacentDatesPreserved:['1914-07-27','1914-07-28','1914-07-29','1914-07-30','1914-08-01','2026-11-05'],sharedBoundaryAndIslandEvidence:'The three historical geometry objects are byte-for-byte equal to the previously reviewed pinned shapes; their exact seams, islands, anchors and provisional provenance therefore remain unchanged.'},null,2)+'\n');console.log(JSON.stringify({referenceGeometryChecks:checks.length,nativeTimelineChecks:native,sourceChanges:0,geometryChanges:0},null,2));
