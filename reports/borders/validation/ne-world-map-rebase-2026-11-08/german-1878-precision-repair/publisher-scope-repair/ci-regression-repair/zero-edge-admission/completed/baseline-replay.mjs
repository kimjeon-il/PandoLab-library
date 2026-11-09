import fs from 'node:fs';import {gunzipSync} from 'node:zlib';import crypto from 'node:crypto';import {pathToFileURL} from 'node:url';import assert from 'node:assert/strict';
const root='D:/dev/worktrees/gis/build-native/wasm';
const {sphericalCore:core}=await import(pathToFileURL(root+'/tools/build/load-spherical-core.mjs'));
await import(pathToFileURL(root+'/src/rendering/workers/gpu-mesh-core.js'));
const {createCanonicalGeometryVersionStore:createStore}=await import(pathToFileURL(root+'/src/geometry/geometry-version-store.js'));
assert.equal(core.coreSourceSha256,'f4138927ea2044814f11cf60daadfb7a0a7b8ef11860ddaab57f081ed365a16c');
const {encodePolygonMesh}=await import(pathToFileURL(root+'/src/rendering/polygon-mesh-codec.js'));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const file=root+'/assets/data/builtin-world/generated/v1/geometries/sha256-c9d645236d9c51df74464ebe3bcefaef79a5f2b022ca501a1bfc47b9f8a2fccc.json.gz';
const stored=fs.readFileSync(file),bytes=gunzipSync(stored),g=JSON.parse(bytes),before=JSON.stringify(g),copy=structuredClone(g),duplicates=[];
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],edge=r=>r.slice(1).flatMap((b,i)=>eq(r[i],b)?[]:[[r[i],b]]);
copy.coordinates=copy.coordinates.map((p,pi)=>p.map((r,ri)=>r.filter((v,i)=>{if(i&&eq(r[i-1],v)){duplicates.push({polygon:pi,ring:ri,index:i,point:v});return false;}return true;})));
const result={input:{file,compressedSha:sha(stored),bytes:stored.length,decodedSha:sha(bytes),decodedBytes:bytes.length},duplicates,ringCounts:g.coordinates.map(p=>p.map(r=>r.length)),nonzeroEdgesPreserved:g.coordinates.every((p,pi)=>p.every((r,ri)=>JSON.stringify(edge(r))===JSON.stringify(edge(copy.coordinates[pi][ri])))),sourceIssues:core.validateTerritorialRing(g.coordinates[0][0]),clippedIssues:core.validateClippedTerritorialRing(g.coordinates[0][0]),exactDuplicateOnlyIssues:copy.coordinates.map(p=>p.map(r=>core.validateClippedTerritorialRing(r)))};
for(const [name,fn]of [['rawGeneratedNormalizer',()=>core.normalizePolygonGeometry(g,true)],['rawCanonicalStore',()=>createStore([{id:'test',version:1,geojson:g}])]])try{fn();result[name]={passed:true};}catch(e){result[name]={passed:false,error:e.message};}
const normalized=core.normalizePolygonGeometry(copy,true);result.exactDuplicateOnlyNormalization={equal:JSON.stringify(normalized)===JSON.stringify(copy),counts:normalized.coordinates.map(p=>p.map(r=>r.length)),uniquePointRetained:normalized.coordinates[0][0].some(p=>eq(p,[26.23715307091098,48.82603901853353]))};
const engine=globalThis.PandoLabGpuMeshCore;engine.setSharedCore(core);
const a=engine.buildPolygonGeometryPacket(g),b=engine.buildPolygonGeometryPacket(copy);result.mesh={keys:Object.keys(a),sameNonRingFields:Object.keys(a).filter(k=>!['ringCoordinates','ringOffsets','polygonOffsets'].includes(k)).map(k=>({key:k,equal:JSON.stringify(a[k])===JSON.stringify(b[k])})),ringCoordinatesPreserved:JSON.stringify(Array.from(a.ringCoordinates))===JSON.stringify(g.coordinates.flat(2).flat()),rawRingCount:a.ringCoordinates.length/2};
result.mesh.packetSha256=sha(Buffer.from(encodePolygonMesh(a)));
result.mesh.ordinaryPacketSha256=sha(Buffer.from(encodePolygonMesh(engine.buildPolygonGeometryPacket({type:'Polygon',coordinates:[[[0,0],[0,2],[2,2],[2,0],[0,0]]]}))));
result.inputUnchanged=JSON.stringify(g)===before;
fs.writeFileSync(root+'/zero-edge-baseline-proof.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
assert.deepEqual(core.validateClippedTerritorialRing(g.coordinates[0][0]),[],'RED: exact zero-length edge must not invalidate unchanged generated boundary');

