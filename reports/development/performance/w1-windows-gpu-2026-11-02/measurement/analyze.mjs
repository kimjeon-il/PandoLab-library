import {existsSync,readFileSync,writeFileSync} from 'node:fs';
import {gunzipSync} from 'node:zlib';
import {reportPath} from './report-paths.mjs';
const base=reportPath('reports/development/performance/w1-windows-gpu-2026-11-02/measurement',{access:'write'});
const report=JSON.parse(readFileSync(base+'/report-win32.json','utf8'));
const consoleText=readFileSync(base+'/console.log','utf8')+(existsSync(base+'/unforced-console.log')?readFileSync(base+'/unforced-console.log','utf8'):'');
const consoleSamples=consoleText.split(/\r?\n/).filter(line=>line.startsWith('GPU_CROSS_SAMPLE ')).map(line=>JSON.parse(line.slice('GPU_CROSS_SAMPLE '.length)));
const summary={source:report.modes[0]?.gpu?.sourceCommit,data:report.modes[0]?.gpu?.dataRevision,modes:[]};
const modes=[...report.modes,...(existsSync(base+'/unforced.json')?[JSON.parse(readFileSync(base+'/unforced.json','utf8'))]:[])];
for(const mode of modes){
 const events=JSON.parse(gunzipSync(readFileSync(base+'/'+mode.mode+'-trace.json.gz')).toString()).traceEvents;
 const firstSample=consoleSamples.find(s=>s.mode===mode.mode&&s.round===0);
 const requests=events.filter(e=>e.name.startsWith('W1:requested:')&&e.args?.data?.startTime>=firstSample.requestedAt-1).sort((a,b)=>a.ts-b.ts);
 const rows=requests.map((request,i)=>{
  const ready=events.find(e=>e.name==='W1:ready:'&&e.ts>=request.ts);
  if(!ready)throw Error('Missing ready trace mark');
  const overlap=events.filter(e=>e.ph==='X'&&Number.isFinite(e.dur)&&e.ts<ready.ts&&e.ts+e.dur>request.ts);
  const layers=overlap.filter(e=>e.name==='LayerTreeHost::DoUpdateLayers');
  const top=overlap.filter(e=>e.dur>=50000).sort((a,b)=>b.dur-a.dur).slice(0,20).map(e=>({name:e.name,ms:e.dur/1000,pid:e.pid,tid:e.tid,thread:events.find(t=>t.ph==='M'&&t.name==='thread_name'&&t.pid===e.pid&&t.tid===e.tid)?.args?.name,args:e.args}));
  const sample=consoleSamples.find(s=>s.mode===mode.mode&&s.round===i);
  if(!sample)throw Error('Missing raw sample '+mode.mode+' '+i);
  return {...sample,layerCount:layers.length,layerMaxMs:Math.max(0,...layers.map(e=>e.dur/1000)),layerTotalMs:layers.reduce((s,e)=>s+e.dur/1000,0),topTraceSpans:top};
 });
 summary.modes.push({mode:mode.mode,status:mode.status,category:mode.category,driver:mode.gpu?.unmaskedRenderer,stats:mode.stats,rows});
}
summary.sameSource=report.modes.every(m=>m.gpu?.sourceCommit===summary.source&&m.gpu?.dataRevision===summary.data&&m.browserVersion===report.modes[0].browserVersion);
summary.sameSemantics=report.modes.every(m=>JSON.stringify(m.hashes)===JSON.stringify(report.modes[0].hashes));
summary.complete=summary.sameSource&&summary.sameSemantics&&report.modes.every(m=>m.status==='passed'&&!m.traceError&&m.samples.length===8)&&report.modes[0].category==='hardware-reported'&&report.modes[1].category==='swiftshader-software'&&report.modes[2].category==='hardware-reported';
writeFileSync(base+'/analysis.json',JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify({...summary,modes:summary.modes.map(m=>({...m,rows:m.rows.map(r=>({target:r.target,presented:r.requestedToPresentedMs,ready:r.requestedToReadyMs,rpc:r.releaseRoundtripMs,worker:r.workerReleaseMs,longTask:r.longTaskMaxMs,layer:r.layerMaxMs}))}))},null,2));
if(!summary.complete)process.exitCode=1;
