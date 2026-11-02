
globalThis.__w2Mark=(stage,edge,extra={})=>{const m=globalThis.__w2Current||{};performance.mark('W2|'+JSON.stringify({stage,edge,requestId:m.requestId??null,projectGeneration:m.projectGeneration??null,geometryRevision:m.geometryRevision??null,quality:m.quality??null,...extra}));};
'use strict';

const revision = new URL(self.location.href).searchParams.get('v') || '';
// This worker used to rely on a pure-JS spherical area integral. The verified
// compiled C++ Core must be ready *before* boundary modules are evaluated.
// Node's file:// test harness can inject the separately verified C++ module;
// browser workers always verify their own pinned JS/WASM pair.
const sourceIsTestFile = new URL(self.location.href).protocol === 'file:';
__w2Mark('core-load','start');const coreReady = sourceIsTestFile && globalThis.PandoLabSphericalCore
  ? Promise.resolve(globalThis.PandoLabSphericalCore)
  : import("../modules/core-wasm-loader.js").then(({ loadVerifiedCore }) => loadVerifiedCore({
    baseUrl: new URL('../../wasm/', self.location.href),
  }));
const modules = coreReady.then(core => {__w2Mark('core-load','end');__w2Mark('module-load','start');
  if (core?.coreAbiVersion !== 1 || typeof core.sphericalRingSignedAreas !== 'function')
    throw Object.assign(new Error('Verified C++ spherical area capability is unavailable.'),
      { code: 'PL-CORE-WASM-CAPABILITY' });
  globalThis.PandoLabSphericalCore = core;
  return Promise.all([
    import(`../modules/country-shared-boundary-packet.js?v=${encodeURIComponent(revision)}`),
    import(`../modules/country-shared-boundary-cache.js?v=${encodeURIComponent(revision)}`),
    import(`../modules/prepared-polygon-mesh.js?v=${encodeURIComponent(revision)}`),
  ]);
});
modules.then(()=>__w2Mark('module-load','end'),e=>__w2Mark('module-load','error',{error:String(e)}));let boundaryState = null;
let loadedCacheUrl = null;
let loadedCacheQuality = null;
let pendingCache = null;
let queued = null;
let draining = false;
let latestSequence = 0;
let latestMessage = null;

let yieldId=0;const yieldToMessages=async()=>{const id=++yieldId;__w2Mark('yield','scheduled',{yieldId:id});await new Promise(resolve=>setTimeout(()=>{__w2Mark('yield','callback',{yieldId:id});resolve();},0));__w2Mark('yield','resumed',{yieldId:id});};
const isLatest = message => message.sequence === latestSequence;

function combine(previous, next) {
  if (!previous || next.type === 'replace' || previous.projectGeneration !== next.projectGeneration) return next;
  const features = new Map((previous.features || []).map(feature => [String(feature.id), feature]));
  const removed = new Set((previous.removedIds || []).map(String));
  for (const value of next.removedIds || []) {
    const id = String(value);
    features.delete(id);
    removed.add(id);
  }
  for (const feature of next.features || []) {
    const id = String(feature.id);
    features.set(id, feature);
    removed.delete(id);
  }
  return { ...previous, ...next, type: previous.type, features: [...features.values()],
    removedIds: previous.type === 'replace' ? [] : [...removed],
    cacheUrl: previous.type === 'replace' ? previous.cacheUrl : next.cacheUrl,
    skipCacheReconcile: false };
}

function deferUnapplied(message) {
  if (isLatest(message)) return false;
  queued = combine(message, queued);
  return true;
}

function postError(message, error) {
  self.postMessage({ type: 'error', requestId: message.requestId,
    projectGeneration: message.projectGeneration, geometryRevision: message.geometryRevision,
    quality: message.quality, message: error?.message || String(error) });
}

async function prepareMessage(message) {
  globalThis.__w2Current=message;__w2Mark('dequeue','start',{featureCount:message.features?.length,type:message.type});let applied = false;
  try {
    const [{ prepareCountrySharedBoundaryPacket, createCountrySharedBoundaryState },
      { changedCountryGeometryIds }, { polygonGeometryDigest }] = await modules;
    if (deferUnapplied(message)) return;
    __w2Mark('modules-awaited','end');if (!boundaryState) boundaryState = createCountrySharedBoundaryState();
    // Every replace still carries the entire authoritative country snapshot.
    // A new Core project may rematerialize identical coordinates as new JS
    // objects, so identity/version-only keys cause needless full topology work.
    // Exact SHA-256 over the actual geometry, not a short display checksum,
    // allows the existing prepared store to reuse only truly identical edges.
    // Hash in this Worker, never on the input/UI thread. The full snapshot
    // also makes late/superseded requests safe without patch-base guesses.
    __w2Mark('digest-all','start');const features = [];
    for (const [index, feature] of (message.features || []).entries()) {
      if (deferUnapplied(message)) return;
      const digest = feature.geometry == null
        ? 'empty' : await polygonGeometryDigest(feature.geometry);
      features.push({ ...feature,
        boundaryRootId: feature.boundaryRootId || (!feature.properties?.parentId ? String(feature.id) : ''),
        boundaryGeometryRevision: `sha256:${digest}` });
      if ((index & 31) === 31) await yieldToMessages();
    }
    if (deferUnapplied(message)) return;
    __w2Mark('digest-all','end',{featureCount:features.length});if (message.type === 'replace') {
      let cached = message.cacheUrl === loadedCacheUrl && message.quality === loadedCacheQuality ? pendingCache : null;
      if (message.cacheUrl && (message.cacheUrl !== loadedCacheUrl || message.quality !== loadedCacheQuality)) {
        try {
          __w2Mark('cache-fetch','start',{url:message.cacheUrl});const response = await fetch(message.cacheUrl);__w2Mark('cache-fetch','end',{status:response.status});
          if (!response.ok) throw new Error(`HTTP ${response.status}`);
          __w2Mark('cache-decompress','start');const stream = response.body.pipeThrough(new DecompressionStream('gzip'));const cacheText=await new Response(stream).text();__w2Mark('cache-decompress','end',{chars:cacheText.length});__w2Mark('cache-parse','start');cached=JSON.parse(cacheText);__w2Mark('cache-parse','end');
          if (cached.version !== 1 || cached.quality !== message.quality
            || !Array.isArray(cached.segments) || !cached.signatures) throw new Error('Invalid boundary cache');
          loadedCacheUrl = message.cacheUrl;
          loadedCacheQuality = message.quality;
          pendingCache = cached;
        } catch (error) {
          cached = null;
          console.warn('[PL-COUNTRY-BOUNDARY-CACHE]', error?.message || String(error));
        }
      }
      if (deferUnapplied(message)) return;
      __w2Mark('state-replace','start',{cacheHit:!!cached,skipReconcile:message.skipCacheReconcile});boundaryState.replace(features, cached ? { cachedSegments: cached.segments,
        changedIds: message.skipCacheReconcile ? new Set() : changedCountryGeometryIds(features, cached.signatures) } : {});
      __w2Mark('state-replace','end',{stats:boundaryState.stats()});if (cached === pendingCache) pendingCache = null;
    } else if (message.type === 'patch') {
      __w2Mark('state-patch','start');boundaryState.patch(features, message.removedIds || []);__w2Mark('state-patch','end',{stats:boundaryState.stats()});
    } else return;
    applied = true;
    // Geometry/index preparation remains available to the next patch, but
    // queued date changes get a chance to supersede this packet before paint.
    await yieldToMessages();
    if (!isLatest(message)) return;
    __w2Mark('packet','start');const packet = prepareCountrySharedBoundaryPacket(boundaryState.segments(), boundaryState.features(),
      { preparedStore: boundaryState.preparedStore, maxEdgeDegrees: message.quality === 'preview' ? 2 : 0.499,
        includeOutlines: message.includeOutlines !== false });
    __w2Mark('packet','end',{bytes:packet.startsEnds.byteLength+packet.preparedGeometry.instances.byteLength+packet.preparedGeometry.nodes.byteLength});await yieldToMessages();if (!isLatest(message)) return;if((message.__w2Delay||globalThis.__w2Control)?.point==='worker'){__w2Mark('control-delay','start');await new Promise(r=>setTimeout(r,(message.__w2Delay||globalThis.__w2Control).ms));__w2Mark('control-delay','end');if(!isLatest(message))return;}__w2Mark('result-post','start');self.postMessage({ type: 'prepared', requestId: message.requestId,
      projectGeneration: message.projectGeneration, geometryRevision: message.geometryRevision,
      quality: message.quality, preparationStats: boundaryState.stats(), packet }, [
      packet.startsEnds.buffer, packet.preparedGeometry.instances.buffer, packet.preparedGeometry.nodes.buffer,
      packet.outlineOverrides.startsEnds.buffer, packet.outlineOverrides.preparedGeometry.instances.buffer,
      packet.outlineOverrides.preparedGeometry.nodes.buffer,
    ]);__w2Mark('result-post','end');
  } catch (error) {
    if (!applied && deferUnapplied(message)) return;
    if (isLatest(message)) postError(message, error);
  }
}

async function drain() {
  draining = true;
  try {
    while (queued) {
      const message = queued;
      queued = null;
      await prepareMessage(message);
    }
  } finally { draining = false; }
}

self.onmessage = ({ data }) => {
  if(data?.type==='__w2Control'){globalThis.__w2Control=data.delay;return;}if (!data || !['replace', 'patch'].includes(data.type)) return;
  __w2Mark('worker-receive','instant',{requestId:data.requestId,projectGeneration:data.projectGeneration,geometryRevision:data.geometryRevision,quality:data.quality});latestMessage = { ...data, sequence: ++latestSequence };
  queued = combine(queued, latestMessage);
  if (!draining) drain().catch(error => postError(latestMessage, error));
};
