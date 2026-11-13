import {openSync,readSync,closeSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {gunzipSync} from 'node:zlib';
import {createHydroWorkerDecoder,decodeHydroSelectedPack,verifyHydroRiverGroups,verifyHydroManifestPolicy,verifyHydroSelectedLakes,verifyHydroKoreaCoverage,verifyHydroCoreDelivery} from '../../tools/gis/hydro-pack-decoder.mjs';
import {verifyHydroBorderFragments} from '../../tools/gis/hydro-point-screen-native.mjs';

const root='assets/data/hydro/v0.13.2/',manifestBytes=readFileSync(root+'manifest.json'),manifest=JSON.parse(manifestBytes);
const fd=openSync(root+'hydro.bin','r');
function section(spec){const bytes=Buffer.alloc(spec.bytes);if(readSync(fd,bytes,0,bytes.length,spec.offset)!==bytes.length)throw Error('Short section');
  if(createHash('sha256').update(bytes).digest('hex')!==spec.sha256)throw Error('Section checksum mismatch');return bytes;}
try{
  const decoder=createHydroWorkerDecoder(manifest);decoder.readGlobalIndex(gunzipSync(section(manifest.index)));
  const policy=verifyHydroManifestPolicy({manifest,version:'0.13.2',manifestBytes:manifestBytes.length,packCount:decoder.packSpecs.size,logicalCount:decoder.logicalPacks.size});
  const coreDelivery=await verifyHydroCoreDelivery({data:section(manifest.metadata.core),sha256:manifest.metadata.core.sha256,featureCount:manifest.metadata.featureCount});
  decoder.readFeatureMetadata(gunzipSync(section(manifest.metadata.core)));
  const details=JSON.parse(gunzipSync(section(manifest.metadata.detail)));
  for(const detail of details.features){const row=decoder.featureMetadata.get(detail.fid);if(row)Object.assign(row,detail);}
  const candidate=[...decoder.featureMetadata.values()].find(row=>row.category==='river'&&row.name?.includes('한강')&&row.role==='mainstem');
  if(!candidate)throw Error('Selected Han river not found');
  const packIds=decoder.logicalPacks.get(candidate.logicalFid);if(!packIds?.length)throw Error('Selected river packs not found');
  const needed=new Set(packIds.map(id=>decoder.packSpecs.get(id).shard));
  const specs=[manifest.index,manifest.metadata.core,manifest.metadata.detail,...manifest.shards.filter(row=>needed.has(row.id))];
  const files=new Map(specs.map(spec=>[spec.sha256,section(spec)]));
  const rows=decodeHydroSelectedPack({files,layout:manifest,stages:manifest.stages,logicalFids:[candidate.logicalFid]});
  const lake=[...decoder.featureMetadata.values()].find(row=>row.category==='lake'&&row.name?.includes('바이칼'));
  if(!lake)throw Error('Selected Baikal lake not found');
  const lakePacks=decoder.logicalPacks.get(lake.logicalFid),lakeShards=new Set(lakePacks.map(id=>decoder.packSpecs.get(id).shard));
  for(const shard of manifest.shards.filter(row=>lakeShards.has(row.id)))if(!files.has(shard.sha256))files.set(shard.sha256,section(shard));
  const lakeRows=decodeHydroSelectedPack({files,layout:manifest,stages:manifest.stages,logicalFids:[lake.logicalFid]});
  const lakeResult=verifyHydroSelectedLakes({features:lakeRows,original:readFileSync('assets/data/hydro/lakes_base.geojson'),sha256:manifest.sources.naturalEarthLakes.sha256});
  const river=[...decoder.featureMetadata.values()].find(row=>row.category==='river'&&row.name?.includes('압록')&&row.flags===1&&row.source?.endsWith(' CHN/PRK'));
  if(!river)throw Error('Selected Yalu border fragment not found');
  const borderPacks=decoder.logicalPacks.get(river.logicalFid),borderShards=new Set(borderPacks.map(id=>decoder.packSpecs.get(id).shard));
  for(const shard of manifest.shards.filter(row=>borderShards.has(row.id)))if(!files.has(shard.sha256))files.set(shard.sha256,section(shard));
  const riverRows=decodeHydroSelectedPack({files,layout:manifest,stages:manifest.stages,logicalFids:[river.logicalFid]})
    .filter(row=>row.metadata.flags===1&&row.metadata.source.endsWith(' CHN/PRK'));
  const countries=JSON.parse(readFileSync('assets/data/countries-ne-5.1.1.geojson'));
  const country=id=>{const found=countries.features.filter(row=>row.id===id);if(found.length!==1)throw Error('Country ID mismatch: '+id);return found[0].geometry;};
  const border=await verifyHydroBorderFragments({left:country('CHN'),right:country('PRK'),pair:'CHN/PRK',features:riverRows},
    {directory:'D:/dev/worktrees/gis/build-native/hydro-point-screen/candidate-boundary-20261102',runtimeRoot:'D:/dev/tools/osgeo4w'});
  const koreanIds=[...new Set([...decoder.featureMetadata.values()].filter(row=>{const [w,s,e,n]=row.bounds.map(v=>v/1000000);
    return !(e<124||w>131||n<33||s>43);}).map(row=>row.logicalFid))];
  const koreaPacks=new Set(koreanIds.flatMap(id=>decoder.logicalPacks.get(id))),koreaShards=new Set([...koreaPacks].map(id=>decoder.packSpecs.get(id).shard));
  for(const shard of manifest.shards.filter(row=>koreaShards.has(row.id)))if(!files.has(shard.sha256))files.set(shard.sha256,section(shard));
  const korean=decodeHydroSelectedPack({files,layout:manifest,stages:manifest.stages,logicalFids:koreanIds});
  console.log(JSON.stringify({name:candidate.name,logicalFid:candidate.logicalFid,packs:packIds.length,shards:needed.size,policy,coreDelivery,result:verifyHydroRiverGroups(rows),lake:lake.name,lakeResult,border,korea:verifyHydroKoreaCoverage(korean),koreaSelectedSystems:koreanIds.length}));
}finally{closeSync(fd);}
