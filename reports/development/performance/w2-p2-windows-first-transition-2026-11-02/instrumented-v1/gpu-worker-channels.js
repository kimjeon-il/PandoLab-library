
globalThis.__w2Mark=(stage,edge,extra={})=>{const m=globalThis.__w2Current||{};performance.mark('W2|'+JSON.stringify({stage,edge,requestId:m.requestId??null,projectGeneration:m.projectGeneration??null,geometryRevision:m.geometryRevision??null,quality:m.quality??null,...extra}));};
// One owner for worker identity, lifetime and delivery. Payloads and transfer lists
// pass through unchanged; domain-specific revision checks remain with consumers.
export function createGpuWorkerChannels({ WorkerClass = globalThis.Worker } = {}) {
  const channels = new Set();
  let disposed = false;
  function create(url, options) {
    if (disposed) throw Object.assign(new Error('Renderer disposed'), { name: 'AbortError' });
    const worker = new WorkerClass(url, options);
    let live = true;
    let onmessage = null;
    let onerror = null;
    const channel = {
      get onmessage() { return onmessage; },
      set onmessage(handler) { onmessage = handler; },
      get onerror() { return onerror; },
      set onerror(handler) { onerror = handler; },
      postMessage(...args) { if(live&&!disposed){const d=args[0];globalThis.__w2Current=d;__w2Mark('main-post','start',{worker:String(url),type:d?.type,featureCount:d?.features?.length});if(String(url).includes('country-shared-boundary')&&globalThis.__W2Delay)d.__w2Delay=globalThis.__W2Delay;worker.postMessage(...args);__w2Mark('main-post','end',{worker:String(url),type:d?.type});} },
      terminate() {
        if (!live) return;
        live = false;
        channels.delete(channel);
        worker.terminate();
        onmessage = null; onerror = null;
      },
    };
    worker.onmessage = event => {
      if (!live || disposed) { event.data?.bitmap?.close?.(); return; }
      globalThis.__w2Current=event.data;__w2Mark('main-receive','start',{worker:String(url),type:event.data?.type});onmessage?.(event);__w2Mark('main-receive','end',{worker:String(url),type:event.data?.type});
    };
    worker.onerror = event => { if (live && !disposed) onerror?.(event); };
    channels.add(channel);
    return channel;
  }
  return Object.freeze({
    create,
    WorkerClass: function OwnedWorker(url, options) { return create(url, options); },
    dispose() { if (disposed) return; disposed = true; for (const channel of channels) channel.terminate(); },
  });
}
// @worker-transport dedicated: channel owner connects GPU worker ports and routes native worker events
