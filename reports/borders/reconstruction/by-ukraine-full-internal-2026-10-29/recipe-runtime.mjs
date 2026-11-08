import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {gzipSync,gunzipSync} from 'node:zlib';
import '../china-apply/app/shared/frontend/js/vendor/polygon-clipping.min.js';
import {applyCompiledSourceDelta,patchCountryWindow} from '../china-apply/app/tools/gis/china-frontier-delta.mjs';
import {territorialIndexEntry} from '../china-apply/app/apps/editor/frontend/js/modules/territorial-index-entry.js';
import {packBuiltinWorldFiles} from '../china-apply/app/tools/build-builtin-world.mjs';
import {storeNativeLibraryObjects} from '../china-apply/app/tools/library-data.mjs';
const root=path.dirname(fileURLToPath(import.meta.url)),read=p=>fs.readFileSync(path.join(root,p)),json=p=>JSON.parse(read(p)),sha=b=>createHash('sha256').update(b).digest('hex');
const output=path.join(root,'staged-runtime'),files=new Map(),put=(p,b)=>{b=Buffer.from(b);files.set(p,b);const full=path.join(output,p);fs.mkdirSync(path.dirname(full),{recursive:true});fs.writeFileSync(full,b);};
const bytes=v=>Buffer.from(JSON.stringify(v)+'\n'),pretty=v=>Buffer.from(JSON.stringify(v,null,2)+'\n');
const ids=['state:soviet-union-byelorussian-ssr','state:soviet-union-ukrainian-ssr','state:soviet-union-russian-sfsr'],FROM='1922-12-30',TO='1925-05-12',stem=id=>id.replace(':','-')+'.json';
const originals=new Map(ids.map(id=>[id,json('source-original/'+stem(id))])),updates=new Map(ids.map(id=>[id,json('source-new/'+stem(id))]));
const selected=e=>{const v=e.geometryVersions.filter(v=>(v.validFrom==null||v.validFrom<=FROM)&&(v.validTo==null||v.validTo>=TO));if(v.length!==1)throw Error('No unique window for '+e.entityId);return v[0];};
const previousIndex=json('materialized/assets/data/territorial-entities/generated/v2/index.json'),index=structuredClone(previousIndex),chunks=new Map();
for(const id of ids){const entity=updates.get(id),source=pretty(entity),stored=gzipSync(source,{level:9,mtime:0});stored[9]=3;const entry=territorialIndexEntry(entity,{sha256:sha(stored),compressedBytes:stored.length,decodedBytes:source.length});
 const at=index.entities.findIndex(e=>e.entityId===id);if(at<0)throw Error('Unknown selected entity');index.entities[at]=entry;chunks.set(id,stored);put('assets/data/territorial-entities/generated/v2/'+entry.file,stored);put('assets/data/territorial-entities/source/countries/'+stem(id),source);}
const indexBytes=bytes(index);put('assets/data/territorial-entities/generated/v2/index.json',indexBytes);
const previousLibrary=json('library-original.json'),native={schemaVersion:1,indexHash:sha(indexBytes),entities:storeNativeLibraryObjects({libraryIndex:index,previousLibrary,previousIndex,readChunk:entry=>{if(!chunks.has(entry.entityId))throw Error('Unexpected native regeneration '+entry.entityId);return chunks.get(entry.entityId);},put})};
put('objects/'+native.indexHash+'.json',indexBytes);put('library.json',bytes(native));
const compiledPath='assets/data/builtin-world/generated/v1/',oldIndex=json('materialized/'+compiledPath+'index.json'),compiledIndex=structuredClone(oldIndex),transport=read('materialized/'+compiledPath+oldIndex.transport.url);
if(sha(transport)!==oldIndex.transport.sha256)throw Error('Transport hash mismatch');
const pc=globalThis.polygonClipping,mp=g=>g.type==='Polygon'?[g.coordinates]:g.coordinates;

const packed=new Map(),proof=[];
for(const entry of compiledIndex.entities){const old=oldIndex.entities.find(x=>x.entityId===entry.entityId),stored=transport.subarray(old.offset,old.offset+old.compressedBytes),source=compiledIndex.sourceIdentities.find(x=>x.projectEntityId===entry.entityId),id=source?.sourceEntityIds.find(x=>ids.includes(x));
 if(!id){packed.set(entry.file,stored);continue;}
 if(sha(stored)!==old.sha256)throw Error('Affected old chunk hash mismatch');
 const country=JSON.parse(gunzipSync(stored)),before=selected(originals.get(id)),after=selected(updates.get(id));
 const transformed=patchCountryWindow(country,{from:FROM,to:TO,sourceVersionId:after.versionId,transform:g=>applyCompiledSourceDelta(before.geometry,after.geometry,g,null,pc)});
 const timeline=transformed.identity?.properties?.metadata?.historicalTimeline;
 if(timeline){timeline.geometryVersions=updates.get(id).geometryVersions.map(({geometry,...v})=>v);timeline.lifetime=structuredClone(updates.get(id).lifetime);if(timeline.sourceInfo)timeline.sourceInfo=structuredClone(updates.get(id).sourceInfo);}
 transformed.identity.properties.metadata.internalBoundaryRefinement={validFrom:FROM,validTo:TO,sourceVersionId:after.versionId,transitionDate:null,scope:'Full reviewed BY/Ukraine internal shared-boundary source-fidelity refinement; retained uncertain segments, no new territorial event',sourceGeometryOnly:false};
 const decoded=bytes(transformed),encoded=gzipSync(decoded,{level:9,mtime:0});encoded[9]=3;
 Object.assign(entry,{file:'countries/'+entry.entityId.replaceAll(':','-')+'-sha256-'+sha(encoded)+'.json.gz',encoding:'gzip',sha256:sha(encoded),compressedBytes:encoded.length,decodedBytes:decoded.length});packed.set(entry.file,encoded);put(compiledPath+entry.file,encoded);
 proof.push({entityId:id,projectEntityId:entry.entityId,sourceVersionId:after.versionId,oldCompiledHash:old.sha256,compiledHash:entry.sha256,bindings:transformed.sourceBindings.filter(r=>r.validFrom<=TO&&(r.validTo==null||r.validTo>=FROM)).map(r=>({from:r.validFrom,to:r.validTo,ref:r.geometryRef.id}))});
 const p=path.join(root,'compiled-new/'+entry.entityId.replace(':','-')+'.json');fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,decoded);
}
for(const id of ids)compiledIndex.inputHashes.sourceRevisions[id]=index.entities.find(x=>x.entityId===id).sha256;
compiledIndex.inputHashes.sourceRevisions=Object.fromEntries(Object.entries(compiledIndex.inputHashes.sourceRevisions).sort(([a],[b])=>a.localeCompare(b,'en')));
compiledIndex.inputHashes.entities=sha(JSON.stringify(compiledIndex.inputHashes.sourceRevisions));
packBuiltinWorldFiles(compiledIndex,packed,{verifyEntityIds:new Set(ids)});
put(compiledPath+compiledIndex.transport.url,packed.get(compiledIndex.transport.url));put(compiledPath+'index.json',packed.get('index.json'));
put('runtime-proof.json',pretty({sourceIds:ids,from:FROM,to:TO,compiled:proof,transport:compiledIndex.transport,sourceIndexHash:sha(indexBytes),nativeIndexHash:native.indexHash}));
fs.writeFileSync(path.join(output,'staging-manifest.json'),pretty({files:[...files].map(([p,b])=>({path:p,size:b.length,sha256:sha(b)}))}));
console.log(JSON.stringify({files:files.size,transport:compiledIndex.transport,proof},null,2));
