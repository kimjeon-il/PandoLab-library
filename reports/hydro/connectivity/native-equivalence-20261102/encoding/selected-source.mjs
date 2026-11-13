import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {openSync,closeSync,readFileSync,readSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {gunzipSync} from 'node:zlib';
import vm from 'node:vm';
import {buildFrontendIndex,frontendAsset} from '../../scripts/lib/frontend-layout.mjs';

const root=process.cwd(),base=resolve(root,'assets/data/hydro/v0.13.2');
const manifest=JSON.parse(readFileSync(resolve(base,'manifest.json'))),fd=openSync(resolve(base,manifest.container.url),'r');
const digest=data=>createHash('sha256').update(data).digest('hex');
function asset(spec){
  assert.equal(spec.url,manifest.container.url);assert(Number.isSafeInteger(spec.offset)&&spec.offset>=0&&spec.offset+spec.bytes<=manifest.container.bytes);
  const bytes=Buffer.alloc(spec.bytes);let at=0;while(at<bytes.length){const n=readSync(fd,bytes,at,bytes.length-at,spec.offset+at);if(!n)throw Error('Truncated Hydro subresource');at+=n;}
  assert.equal(digest(bytes),spec.sha256);return bytes;
}
try{
  const context=vm.createContext({TextDecoder,URL,performance,structuredClone,inputManifest:manifest});context.self=context;context.onmessage=null;context.importScripts=()=>{};
  const index=buildFrontendIndex(root);for(const file of ['vendor/earcut.min.js','workers/geographic-boundary-core.js','workers/hydro-tile-worker.js']){
    const item=frontendAsset(root,'assets/js/'+file,{index});vm.runInContext(item.bytes.toString('utf8'),context,{filename:item.sourcePath});}
  vm.runInContext('manifest = inputManifest',context);
  const decoder=vm.runInContext('({readGlobalIndex,readFeatureMetadata,readPack,logicalPacks,packSpecs,featureMetadata})',context);
  decoder.readGlobalIndex(gunzipSync(asset(manifest.index)));decoder.readFeatureMetadata(gunzipSync(asset(manifest.metadata.core)));
  const fid=7504,meta=decoder.featureMetadata.get(fid);assert(meta);
  const detail=JSON.parse(gunzipSync(asset(manifest.metadata.detail))).features.find(row=>row.fid===fid);assert(detail);Object.assign(meta,detail);
  let selected=null;for(const pack of decoder.logicalPacks.get(meta.logicalFid)||[]){const spec=decoder.packSpecs.get(pack),shardSpec=manifest.shards.find(row=>row.id===spec.shard);
    const shard=asset(shardSpec),bytes=gunzipSync(shard.subarray(spec.offset,spec.offset+spec.length));
    selected=decoder.readPack(bytes,pack).features.find(row=>row.properties.__fid===fid);if(selected)break;}
  assert(selected);const feature={fid:meta.fid,logical_fid:meta.logicalFid,pandolab_id:meta.awId,category:meta.category,stage:meta.stage,flags:meta.flags,
    fragment_index:meta.fragmentIndex,fragment_count:meta.fragmentCount,width:meta.width,geometry:selected.geometry,bounds:meta.bounds.map(value=>value/1000000),
    width_profile:selected.properties.stroke_widths,source_id:meta.sourceId||''};
  writeFileSync('build-native/hydro-encoding/selected-decoded.json',JSON.stringify({metadata:meta,geometry:selected.geometry,widths:selected.properties.stroke_widths})+'\n',{flag:'wx'});
  console.log(JSON.stringify({fid,sourceId:feature.source_id,geometry:feature.geometry.type,featureSha256:digest(Buffer.from(JSON.stringify(feature)))}));
}finally{closeSync(fd);}
