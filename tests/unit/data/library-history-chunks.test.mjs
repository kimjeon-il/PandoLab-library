import test from 'node:test';
import assert from 'node:assert/strict';
import {buildHistoryRetentionManifest,buildResearchPurgeManifest} from '../../../tools/storage/history/library-history.mjs';
const chunk=(stored,offset)=>({stored,offset,bytes:10,sha256:'a'.repeat(64)});
function entry(){return {stored:'archive/blobs/master.gzip-chunks.json',encoding:'gzip-chunks',bytes:100,sha256:'b'.repeat(64),packedBytes:20,packedSha256:'c'.repeat(64),manifestBytes:500,manifestSha256:'d'.repeat(64),chunks:[chunk('archive/chunks/one.bin',0),chunk('archive/chunks/two.bin',10)]};}
test('chunk history retains every referenced part and preserves shared parts during purge',()=>{
 const source='assets/data/territorial-entities/source/geometries/live.json',retired='reports/borders/test/retired.json',e=entry(),index={files:{[source]:e,[retired]:e}};
 const paths=[e.stored,...e.chunks.map(p=>p.stored)];
 const keep=buildHistoryRetentionManifest({keepPaths:[source],indexes:[index]});
 for(const path of paths)assert.ok(keep.keepPaths.includes(path),path);
 const purge=buildResearchPurgeManifest({retiredPaths:[retired],indexes:[index],currentIndex:{files:{[source]:e}}});
 for(const path of paths)assert.ok(!purge.paths.includes(path),path);
 const exclusive=buildResearchPurgeManifest({retiredPaths:[retired],indexes:[{files:{[retired]:e}}],currentIndex:{files:{}}});
 for(const path of paths)assert.ok(exclusive.paths.includes(path),path);
});
test('history inventories fail closed for missing, malformed and escaping chunk references',()=>{
 for(const mutate of [e=>e.chunks=[],e=>e.chunks[0].stored='../escape',e=>delete e.chunks[0].stored,e=>e.chunks[1].offset=1]){
 const e=entry();mutate(e);
 assert.throws(()=>buildHistoryRetentionManifest({keepPaths:['source'],indexes:[{files:{source:e}}]}));
 assert.throws(()=>buildResearchPurgeManifest({retiredPaths:['reports/borders/test/a.json'],indexes:[{files:{'reports/borders/test/a.json':e}}],currentIndex:{files:{}}}));
 }
});
