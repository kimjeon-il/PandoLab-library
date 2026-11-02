
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

    const __w5Boundary=String(url).includes('country-shared-boundary');
    let __w5Active=null,__w5Pending=null,__w5Bypass=false;
    const __w5Mark=(stage,extra={})=>performance.mark('W5|'+JSON.stringify({stage,...extra}));
    const __w5Native=args=>{const d=args[0];__w5Mark('native-post-start',{requestId:d?.requestId,projectGeneration:d?.projectGeneration});try{worker.postMessage(...args);}finally{__w5Mark('native-post-end',{requestId:d?.requestId,projectGeneration:d?.projectGeneration});}};
    const __w5AsyncNative=args=>{try{__w5Native(args);}catch(error){__w5Mark('native-post-error',{requestId:args[0]?.requestId,message:String(error)});if(onerror)onerror({error,message:String(error)});else queueMicrotask(()=>{throw error;});}};
    function __w5Proof(data){
      const start=performance.now(),snapshot=structuredClone(data),cloned=performance.now();
      const valid=x=>Array.isArray(x)?x.every(valid):typeof x==='number'&&Number.isFinite(x);
      if(!snapshot.features.every(f=>f.geometry==null||(typeof f.geometry.type==='string'&&valid(f.geometry.coordinates))))throw Error('Unsupported boundary geometry');
      const serialized=JSON.stringify([snapshot.quality,snapshot.includeOutlines!==false,snapshot.features]);const bytes=new TextEncoder().encode(serialized),encoded=performance.now();
      __w5Mark('proof-start',{requestId:data.requestId,projectGeneration:data.projectGeneration,bytes:bytes.byteLength,cloneMs:cloned-start,encodeMs:encoded-cloned});
      const promise=crypto.subtle.digest('SHA-256',bytes).then(buffer=>{const sha=[...new Uint8Array(buffer)].map(x=>x.toString(16).padStart(2,'0')).join('');__w5Mark('proof-end',{requestId:data.requestId,projectGeneration:data.projectGeneration,sha,wallMs:performance.now()-start});return sha;},error=>{__w5Mark('proof-error',{requestId:data.requestId,message:String(error)});return null;});
      return{snapshot,promise};
    }
    function __w5Forward(data){__w5Bypass=true;try{worker.onmessage({data});}finally{__w5Bypass=false;}}
    function __w5Flush(p){
      if(!live||disposed||__w5Pending!==p||!p.matched||!p.reply)return;
      __w5Pending=null;__w5Active=null;const old=p.reply,next=p.next.snapshot;
      __w5Forward(old);
      const current=globalThis.__w2Readiness?.();
      if(!current){__w5Mark('join-fallback',{requestId:next.requestId,reason:'no-readiness-certificate'});__w5AsyncNative([next]);return;}
      if(Number(current.requestId)!==Number(next.requestId)||Number(current.generation)!==Number(next.projectGeneration)||Number(current.geometryRevision)!==Number(next.geometryRevision)||current.quality!==next.quality){__w5Mark('join-stale',{requestId:next.requestId,projectGeneration:next.projectGeneration});return;}
      __w5Mark('join-adopt',{requestId:next.requestId,projectGeneration:next.projectGeneration,oldRequestId:old.requestId,oldGeneration:old.projectGeneration});
      __w5Forward({...old,requestId:next.requestId,projectGeneration:next.projectGeneration,geometryRevision:next.geometryRevision,quality:next.quality,__w5Joined:true});
    }
    function __w5Send(args){
      const data=args[0];if(!__w5Boundary){worker.postMessage(...args);return;}if(data?.type!=='replace'||!Array.isArray(data.features)||!data.features.length||args.length!==1){if(data?.type==='replace'||data?.type==='patch'){const p=__w5Pending;__w5Pending=null;__w5Active=null;if(p?.reply)__w5Forward(p.reply);if(p&&Number(data.projectGeneration)===Number(p.next.snapshot.projectGeneration))__w5Native([p.next.snapshot]);}__w5Native(args);return;}
      let proof;try{proof=__w5Proof(data);}catch(error){const old=__w5Pending?.reply;__w5Pending=null;__w5Active=null;if(old)__w5Forward(old);__w5Mark('proof-error',{requestId:data.requestId,message:String(error)});__w5Native(args);return;}
      if(!__w5Active){__w5Active={requestId:data.requestId,generation:data.projectGeneration,...proof};__w5Native([proof.snapshot]);return;}
      if(Number(__w5Active.generation)===Number(data.projectGeneration)||__w5Pending){const prior=__w5Pending;__w5Pending=null;__w5Active=null;if(prior?.reply)__w5Forward(prior.reply);__w5Mark('join-fallback',{requestId:data.requestId,reason:'same-generation-or-superseded'});__w5Native([proof.snapshot]);return;}
      const previous=__w5Active,p={next:proof,reply:null,matched:false};__w5Pending=p;__w5Mark('join-candidate',{requestId:data.requestId,projectGeneration:data.projectGeneration,oldRequestId:previous.requestId,oldGeneration:previous.generation});
      Promise.all([previous.promise,proof.promise]).then(([a,b])=>{if(!live||disposed||__w5Pending!==p)return;if(a&&a===b){p.matched=true;__w5Mark('join-match',{requestId:data.requestId,projectGeneration:data.projectGeneration,sha:a});__w5Flush(p);}else{const old=p.reply;__w5Pending=null;__w5Active=null;if(old)__w5Forward(old);__w5Mark('join-fallback',{requestId:data.requestId,reason:'identity-mismatch'});__w5AsyncNative([proof.snapshot]);}}).catch(error=>{if(!live||disposed||__w5Pending!==p){if(onerror)onerror({error,message:String(error)});else queueMicrotask(()=>{throw error;});return;}const old=p.reply;__w5Pending=null;__w5Active=null;if(old)__w5Forward(old);__w5Mark('join-fallback',{requestId:data.requestId,reason:String(error)});__w5AsyncNative([proof.snapshot]);});
    }
    function __w5Intercept(event){
      if(__w5Bypass||!__w5Boundary||!__w5Active)return false;const data=event.data;
      if(Number(data?.requestId)!==Number(__w5Active.requestId)||Number(data?.projectGeneration)!==Number(__w5Active.generation))return false;
      if(data.type==='error'&&__w5Pending){const p=__w5Pending;__w5Pending=null;__w5Active=null;__w5Mark('join-fallback',{requestId:p.next.snapshot.requestId,reason:'old-worker-error'});__w5Native([p.next.snapshot]);return false;}
      if(data.type!=='prepared')return false;
      if(!__w5Pending){__w5Active=null;return false;}
      const p=__w5Pending;p.reply=data;__w5Mark('join-result-held',{requestId:p.next.snapshot.requestId,oldRequestId:data.requestId});__w5Flush(p);return true;
    }

    const channel = {
      get onmessage() { return onmessage; },
      set onmessage(handler) { onmessage = handler; },
      get onerror() { return onerror; },
      set onerror(handler) { onerror = handler; },
      postMessage(...args) { if(live&&!disposed){const d=args[0];globalThis.__w2Current=d;__w2Mark('main-post','start',{worker:String(url),type:d?.type,featureCount:d?.features?.length});if(String(url).includes('country-shared-boundary')&&globalThis.__W2Delay)d.__w2Delay=globalThis.__W2Delay;__w5Send(args);__w2Mark('main-post','end',{worker:String(url),type:d?.type});} },
      terminate() {
        if (!live) return;
        live = false;
        channels.delete(channel);
        worker.terminate();
        onmessage = null; onerror = null;
      },
    };
    let __w4Receive=0;worker.onmessage = event => {if(live&&!disposed&&String(url).includes('country-shared-boundary')){const seq=++__w4Receive;performance.mark('W4|'+JSON.stringify({stage:'main-before-data',seq}));const data=event.data;performance.mark('W4|'+JSON.stringify({stage:'main-after-data',seq,requestId:data?.requestId,projectGeneration:data?.projectGeneration,geometryRevision:data?.geometryRevision,quality:data?.quality}));}
      if (!live || disposed) { event.data?.bitmap?.close?.(); return; }
      if(__w5Intercept(event))return;
      if(String(url).includes('country-shared-boundary')&&event.data?.type==='prepared'){const original=event.data;globalThis.__w2ReplayStale=()=>{const c=globalThis.__w2Readiness();const current={...original,requestId:c.requestId,projectGeneration:c.generation,geometryRevision:c.geometryRevision,quality:c.quality};for(const override of [{requestId:current.requestId-1},{projectGeneration:current.projectGeneration-1},{geometryRevision:current.geometryRevision-1},{quality:current.quality==='canonical'?'preview':'canonical'}])onmessage?.({data:{...current,...override}});};}globalThis.__w2Current=event.data;__w2Mark('main-receive','start',{worker:String(url),type:event.data?.type});onmessage?.(event);__w2Mark('main-receive','end',{worker:String(url),type:event.data?.type});
    };
    worker.onerror = event => { __w5Pending=null;__w5Active=null;if (live && !disposed) onerror?.(event); };
    if(String(url).includes('country-shared-boundary'))globalThis.__w2ControlBoundary=delay=>worker.postMessage({type:'__w2Control',delay});channels.add(channel);
    return channel;
  }
  return Object.freeze({
    create,
    WorkerClass: function OwnedWorker(url, options) { return create(url, options); },
    dispose() { if (disposed) return; disposed = true; for (const channel of channels) channel.terminate(); },
  });
}
// @worker-transport dedicated: channel owner connects GPU worker ports and routes native worker events
