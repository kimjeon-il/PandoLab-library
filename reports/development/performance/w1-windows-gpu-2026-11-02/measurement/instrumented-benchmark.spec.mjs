import {chromium,test,expect} from '@playwright/test';
import {createHash} from 'node:crypto';
import {mkdir,writeFile} from 'node:fs/promises';
import {gzipSync} from 'node:zlib';
import {reportPath} from '../../tools/report-paths.mjs';
const evidence=reportPath('reports/development/performance/w1-windows-gpu-2026-11-02/measurement',{access:'write'});

test.use({timezoneId:'Asia/Seoul',locale:'ko-KR',viewport:{width:1280,height:800},trace:'off'});

function replaceExactlyOnce(source,anchor,replacement){
  const first=source.indexOf(anchor);
  if(first<0||source.indexOf(anchor,first+anchor.length)!==-1)
    throw new Error('GPU cross benchmark source contract changed: '+anchor.slice(0,100));
  return source.slice(0,first)+replacement+source.slice(first+anchor.length);
}
function classifyBackend(value){
  const raw=[value?.unmaskedRenderer,value?.unmaskedVendor,value?.renderer,value?.vendor].filter(Boolean).join(' ');
  if(!raw)return 'unverified';
  if(/swiftshader/i.test(raw))return 'swiftshader-software';
  if(/llvmpipe|lavapipe|software rasterizer|microsoft basic render|warp\b|softpipe/i.test(raw))return 'other-software';
  if(/paravirtual|virtualbox|vmware|virgl|virtio|virtual gpu/i.test(raw))return 'virtual-gpu-unverified';
  if(/apple\s+m[1-9]|metal renderer:\s*apple\s+m[1-9]|nvidia|geforce|radeon|intel.*(graphics|iris|arc|uhd)|adreno|mali-/i.test(raw))
    return 'hardware-reported';
  return 'unverified';
}
function percentile(values,p){
  if(!values.length)return null;
  const data=[...values].sort((a,b)=>a-b);
  const index=(data.length-1)*p,lo=Math.floor(index),hi=Math.ceil(index);
  return Math.round((data[lo]+(data[hi]-data[lo])*(index-lo))*10)/10;
}
const time=()=>performance.now();

async function installInstrumentation(page){
  await page.addInitScript(()=>{
    globalThis.__gpuCrossProbe={
      marks:[],longTasks:[],
      mark(stage,month='',extra={}){this.marks.push({stage,month,at:performance.now(),...extra});performance.mark('W1:'+stage+':'+month);}
    };
    try{
      new PerformanceObserver(list=>{
        for(const entry of list.getEntries())
          globalThis.__gpuCrossProbe.longTasks.push({at:entry.startTime,ms:entry.duration});
      }).observe({type:'longtask',buffered:true});
    }catch(_){/* Chrome version may not implement this observation */ }
  });
  await page.route('**/modules/viewer-composition.js*',async route=>{
    const response=await route.fetch();let source=await response.text();
    source=replaceExactlyOnce(source,
      'applyMonth:async(month,{isCurrent,commit})=>{',
      "applyMonth:async(month,{isCurrent,commit})=>{globalThis.__gpuCrossProbe?.mark('requested',month);");
    source=replaceExactlyOnce(source,
      "onPresented:()=>{commit();window.dispatchEvent(new CustomEvent('pandolab:project-changed'));}",
      "onPresented:()=>{commit();globalThis.__gpuCrossProbe?.mark('presented',month);window.dispatchEvent(new CustomEvent('pandolab:project-changed'));}");
    source=replaceExactlyOnce(source,
      "status.dataset.ready='true';",
      "status.dataset.ready='true';globalThis.__gpuCrossProbe?.mark('ready');");
    await route.fulfill({response,body:source});
  });
  await page.route('**/modules/core-document-client.js*',async route=>{
    const response=await route.fetch();let source=await response.text();
    source=replaceExactlyOnce(source,
      '      const { result } = await rpc.request(operation, request, atomic || speculative',
      "      if(operation==='core.document-replacement-release')globalThis.__gpuCrossProbe?.mark('release-start');"+
      '      const { result, timing: __gpuCrossWorkerTiming } = await rpc.request(operation, request, atomic || speculative');
    source=replaceExactlyOnce(source,
      '        ? { timeoutMs: 0 } : { signal: options.signal });',
      "        ? { timeoutMs: 0 } : { signal: options.signal });"+
      "if(operation==='core.document-replacement-release')globalThis.__gpuCrossProbe?.mark('release-end','',{workerMs:__gpuCrossWorkerTiming?.durationMs??null});");
    await route.fulfill({response,body:source});
  });
}
async function runOne(mode,baseURL){
  const report={mode:mode.name,flags:mode.flags,platform:process.platform,status:'pending',samples:[],errors:[]};
  let browser,context,page,cdp;const traceEvents=[];
  try{
    await mkdir(evidence,{recursive:true});
    browser=await chromium.launch({headless:true,args:mode.flags,timeout:90000});
    report.browserVersion=browser.version();
    cdp=await browser.newBrowserCDPSession();
    report.systemInfo=await cdp.send('SystemInfo.getInfo');
    cdp.on('Tracing.dataCollected',e=>traceEvents.push(...e.value));
    await cdp.send('Tracing.start',{categories:'devtools.timeline,blink.user_timing,cc,gpu',options:'record-as-much-as-possible',transferMode:'ReportEvents'});
    context=await browser.newContext({viewport:{width:1280,height:800},
      deviceScaleFactor:1,timezoneId:'Asia/Seoul',locale:'ko-KR',reducedMotion:'reduce'});
    page=await context.newPage();
    page.on('pageerror',error=>report.errors.push(String(error)));
    await installInstrumentation(page);
    await page.goto(new URL('/?debug=1&renderer=webgl2',baseURL).href,{waitUntil:'domcontentloaded',timeout:60000});
    await expect(page.locator('#viewerStatus')).toHaveAttribute('data-ready','true',{timeout:110000});
    report.gpu=await page.evaluate(()=>{
      const canvas=document.querySelector('#viewerCanvas');
      const gl=canvas?.getContext('webgl2');
      const extension=gl?.getExtension('WEBGL_debug_renderer_info');
      return {webglVersion:gl?.getParameter(gl.VERSION)??null,
        vendor:gl?.getParameter(gl.VENDOR)??null,
        renderer:gl?.getParameter(gl.RENDERER)??null,
        unmaskedVendor:extension?gl.getParameter(extension.UNMASKED_VENDOR_WEBGL):null,
        unmaskedRenderer:extension?gl.getParameter(extension.UNMASKED_RENDERER_WEBGL):null,
        attributes:gl?.getContextAttributes?.()??null,
        width:canvas?.width??null,height:canvas?.height??null,
        devicePixelRatio:devicePixelRatio,
        actualRenderer:globalThis.__PANDOLAB_GPU_METRICS__?.renderer??null,
        sourceCommit:globalThis.PANDOLAB_BUILD_META?.sourceCommit??null,
        dataRevision:globalThis.PANDOLAB_BUILD_META?.dataRevision??null};
    });
    report.category=classifyBackend(report.gpu);
    console.log('W1_DRIVER '+JSON.stringify({mode:mode.name,category:report.category,gpu:report.gpu}));
    report.initialMonth=await page.evaluate(()=>globalThis.__PANDOLAB_VIEWER__?.builtinMonth()?.month);
    if(!/^\d{4}-\d{2}$/.test(report.initialMonth||''))
      throw new Error('Viewer did not expose the current month after first frame');
    if(!report.gpu?.unmaskedRenderer)
      throw new Error('WebGL GPU driver identity unavailable. Hardware cannot be verified.');
    if(!report.gpu?.webglVersion?.includes('WebGL 2.0'))
      throw new Error('Actual Viewer is not running WebGL2');
    if(!report.initialMonth.startsWith('2026-'))throw Error('Expected 2026 initial year');
    const previous='2025-12';
    const hashes=new Map();
    const rounds=Number(process.env.PANDOLAB_W1_ROUNDS||8),warmups=2;
    for(let i=0;i<warmups+rounds;i++){
      const target=i%2===0?previous:report.initialMonth;
      const button=i%2===0?'#timelinePreviousYear':'#timelineNextYear';
      await page.evaluate(()=>{globalThis.__gpuCrossProbe.marks=[];globalThis.__gpuCrossProbe.longTasks=[];});
      await page.locator(button).click({timeout:70000});
      await expect.poll(()=>page.evaluate(()=>({
        month:globalThis.__PANDOLAB_VIEWER__?.builtinMonth()?.month,
        cursor:globalThis.__PANDOLAB_VIEWER__?.documentState()?.timelineCursor,
        ready:document.getElementById('viewerStatus')?.dataset.ready
      })),{timeout:100000}).toEqual({month:target,cursor:target,ready:'true'});
      await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
      const record=await page.evaluate(()=>{
        const events=globalThis.__gpuCrossProbe.marks;
        const at=stage=>events.find(e=>e.stage===stage)?.at??null;
        const releaseEnd=events.find(e=>e.stage==='release-end');
        const requested=at('requested'),presented=at('presented'),ready=at('ready');
        const releaseStart=at('release-start'),releaseFinish=at('release-end');
        const filtered=globalThis.__gpuCrossProbe.longTasks.filter(e=>
          requested!=null&&ready!=null&&e.at<ready && e.at+e.ms>requested);
        const document=globalThis.__PANDOLAB_VIEWER__.documentSnapshot();
        const semantic={
          setupMonth:document.projectSetup?.initialMonth,
          geometries:document.geometries,
          places:document.places,
          labels:[...globalThis.document.querySelectorAll('#viewerLabels text')].map(e=>({text:e.textContent,x:e.getAttribute('x'),y:e.getAttribute('y')})).sort((a,b)=>JSON.stringify(a).localeCompare(JSON.stringify(b))),
          svgPaths:[...globalThis.document.querySelectorAll('#viewerLabels path')].map(e=>e.getAttribute('d')).sort(),
          entities:document.territorialEntities?.map(e=>[e.id,e.properties?.name,
            e.properties?.parentId,e.geometryRef?.id,e.geometryRef?.version]),
          geometryVersions:document.geometries?.map(g=>[g.id,g.version]),
          timelineCounts:Object.fromEntries(Object.entries(document.timelineRecords??{})
            .filter(([,v])=>Array.isArray(v)).map(([k,v])=>[k,v.length]))
        };
        return {requested,presented,ready,releaseStart,releaseFinish,
          workerReleaseMs:releaseEnd?.workerMs??null,
          longTaskMaxMs:Math.max(0,...filtered.map(e=>e.ms)),
          longTasks:filtered.filter(e=>e.ms>=100).slice(0,8),
          visible:globalThis.__PANDOLAB_VIEWER__.visibleTerritorialCount(),semantic};
      });
      for(const k of ['requested','presented','ready','releaseStart','releaseFinish']){
        if(!Number.isFinite(record[k]))throw new Error('Missing actual transition marker '+k+' in mode '+mode.name);
      }
      if(record.visible<=0)throw new Error('No countries visible after accepted map in '+mode.name);
      const semanticHash=createHash('sha256').update(JSON.stringify(record.semantic)).digest('hex');
      const known=hashes.get(target);
      if(known && known!==semanticHash)throw new Error('Repeated year changed semantic world data for '+target);
      hashes.set(target,semanticHash);
      const sample={requestedAt:record.requested,presentedAt:record.presented,readyAt:record.ready,target,kind:i<warmups?'warmup':'measured',
        requestedToPresentedMs:record.presented-record.requested,
        requestedToReadyMs:record.ready-record.requested,
        presentedToReadyMs:record.ready-record.presented,
        releaseRoundtripMs:record.releaseFinish-record.releaseStart,
        workerReleaseMs:record.workerReleaseMs,longTaskMaxMs:record.longTaskMaxMs,
        longTasks:record.longTasks,semanticHash,visible:record.visible};
      if(i>=warmups)report.samples.push(sample);
      if(i===warmups||i===warmups+1)await page.screenshot({path:evidence+'/'+mode.name+'-'+target+'.png'});
      console.log('GPU_CROSS_SAMPLE '+JSON.stringify({mode:mode.name,category:report.category,round:i,...sample}).slice(0,6000));
    }
    report.hashes=Object.fromEntries(hashes);
    const numeric=key=>report.samples.map(s=>s[key]).filter(Number.isFinite);
    report.stats=Object.fromEntries(['requestedToPresentedMs','requestedToReadyMs','presentedToReadyMs','releaseRoundtripMs','longTaskMaxMs']
      .map(key=>[key,{p50:percentile(numeric(key),.5),p95Exploratory:percentile(numeric(key),.95),
        max:Math.max(...numeric(key))}]));
    if(report.errors.length)throw new Error('Unexpected page errors: '+report.errors.slice(0,5).join('; '));
    report.status='passed';
  }catch(error){
    report.status='failed';
    report.failure=String(error?.stack||error);
    console.log('GPU_CROSS_ERROR '+JSON.stringify({mode:mode.name,category:report.category,error:report.failure}).slice(0,2400));
  }finally{
    try{if(cdp){const completed=new Promise(resolve=>cdp.once('Tracing.tracingComplete',resolve));await cdp.send('Tracing.end');await completed;await writeFile(evidence+'/'+mode.name+'-trace.json.gz',gzipSync(JSON.stringify({traceEvents})));report.traceEventCount=traceEvents.length;}}catch(e){report.traceError=String(e);}
    try{await context?.close();}catch(e){report.closeError=String(e);}
    try{await browser?.close();}catch(e){report.browserCloseError=String(e);}
  }
  console.log('GPU_CROSS_BACKEND '+JSON.stringify({mode:report.mode,category:report.category,backend:report.gpu?.unmaskedRenderer,
    platform:report.platform,status:report.status,stats:report.stats}).slice(0,7000));
  return report;
}
test('same-host GPU/backend comparison without presuming hardware acceleration',async({baseURL},testInfo)=>{
  test.setTimeout(1100000);
  if(!baseURL)throw new Error('Base URL is required for Pando GPU cross benchmark');
  // A-B-A controls for warm driver caches and first-browser ordering.
  // Re-run the first backend on the SAME runner after forcing SwiftShader.
  const modes=process.platform==='darwin'
    ?[{name:'metal',flags:['--use-angle=metal']},
      {name:'swiftshader',flags:['--use-angle=swiftshader']},
      {name:'metal-retest',flags:['--use-angle=metal']}]
    :[{name:'default',flags:process.platform==='win32'?['--use-angle=d3d11']:[]},
      {name:'swiftshader',flags:['--use-angle=swiftshader']},
      {name:'default-retest',flags:process.platform==='win32'?['--use-angle=d3d11']:[]}];
  const report={schema:'pando-gpu-cross-v1',sourceCommit:process.env.GITHUB_SHA??null,
    host:{platform:process.platform,arch:process.arch,cpus:process.env.RUNNER_OS??null},
    measuredAt:new Date().toISOString(),modes:[],comparison:null};
  try{
    for(const mode of modes)report.modes.push(await runOne(mode,baseURL));
    const hardware=report.modes.find(m=>m.status==='passed'&&m.category==='hardware-reported');
    const software=report.modes.find(m=>m.status==='passed'&&m.category==='swiftshader-software');
    if(hardware&&software){
      report.comparison={
        status:'paired-hardware-reported-vs-swiftshader',
        note:'Same-host software-vs-reported-hardware backend; browser version and source pin must match. Small n, not universal.',
        hardwareMode:hardware.mode,softwareMode:software.mode,
        hardwareBackend:hardware.gpu.unmaskedRenderer,softwareBackend:software.gpu.unmaskedRenderer,
        hardwarePresentedP50Ms:hardware.stats.requestedToPresentedMs.p50,
        softwarePresentedP50Ms:software.stats.requestedToPresentedMs.p50,
        hardwareReadyP50Ms:hardware.stats.requestedToReadyMs.p50,
        softwareReadyP50Ms:software.stats.requestedToReadyMs.p50,
        hardwareReleaseP50Ms:hardware.stats.releaseRoundtripMs.p50,
        softwareReleaseP50Ms:software.stats.releaseRoundtripMs.p50,
        compatibleSource:hardware.gpu.sourceCommit===software.gpu.sourceCommit
          &&hardware.gpu.dataRevision===software.gpu.dataRevision,
      };
      if(!report.comparison.compatibleSource)
        throw new Error('Cross-backend project source pin mismatch');
    }else{
      report.comparison={
        status:'inconclusive-hardware-not-confirmed',
        reason:'No completed pair with both a verified reported hardware GPU and SwiftShader on the same host.',
        available:report.modes.map(m=>({mode:m.mode,status:m.status,category:m.category,renderer:m.gpu?.unmaskedRenderer})),
      };
    }
    const first=report.modes[0],retest=report.modes.at(-1);
    report.orderControl={
      firstMode:first.mode,retestMode:retest.mode,
      sameDriver:first.gpu?.unmaskedRenderer===retest.gpu?.unmaskedRenderer,
      firstReleaseP50Ms:first.stats?.releaseRoundtripMs?.p50??null,
      retestReleaseP50Ms:retest.stats?.releaseRoundtripMs?.p50??null,
      firstReadyP50Ms:first.stats?.requestedToReadyMs?.p50??null,
      retestReadyP50Ms:retest.stats?.requestedToReadyMs?.p50??null,
      firstPresentedP50Ms:first.stats?.requestedToPresentedMs?.p50??null,
      retestPresentedP50Ms:retest.stats?.requestedToPresentedMs?.p50??null
    };
    console.log('GPU_CROSS_ORDER_CONTROL '+JSON.stringify(report.orderControl));
    console.log('GPU_CROSS_COMPARISON '+JSON.stringify(report.comparison));
  }finally{
    await mkdir('test-results/viewer-gpu-backend-cross',{recursive:true});
    const file=evidence+'/report-'+process.platform+'.json';
    await writeFile(file,JSON.stringify(report,null,2));
    await testInfo.attach('viewer-gpu-backend-cross',{path:file,contentType:'application/json'});
  }
  if(report.modes.some(m=>m.status!=='passed')||report.modes[0].category!=='hardware-reported'||report.modes[2].category!=='hardware-reported'||report.modes[1].category!=='swiftshader-software')
    throw new Error('Neither GPU backend ran the actual Viewer, cannot claim cross measurement');
});
test('W1 unforced backend diagnostic',async({baseURL})=>{
  test.setTimeout(300000);
  const report=await runOne({name:'unforced',flags:[]},baseURL);
  await writeFile(evidence+'/unforced.json',JSON.stringify(report,null,2));
  expect(report.status).toBe('passed');
});
