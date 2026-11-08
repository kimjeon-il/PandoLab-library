import {chromium} from '@playwright/test';
import {performance} from 'node:perf_hooks';
import fs from 'node:fs';
import config from '../../../playwright.config.js';
import {startDevelopmentServer} from '../../../scripts/frontend-dev-server.mjs';
const server=await startDevelopmentServer({repository:process.cwd(),port:4189,observe:false});
const browser=await chromium.launch({headless:true,...config.use.launchOptions});
try{
 const runs=[];
 for(const repeat of [false,true]){
  const context=await browser.newContext({viewport:{width:1280,height:800}}),page=await context.newPage();
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  const cdp=await context.newCDPSession(page);await cdp.send('Performance.enable');await cdp.send('Network.enable');
  let requests=0,transfer=0;cdp.on('Network.requestWillBeSent',()=>requests++);cdp.on('Network.loadingFinished',e=>transfer+=e.encodedDataLength);
  if(repeat){await page.goto('http://127.0.0.1:4189/?debug=1');await page.locator('#viewerStatus[data-ready="true"]').waitFor({timeout:120000});requests=0;transfer=0;}
  const start=performance.now();await page.goto('http://127.0.0.1:4189/?debug=1');await page.locator('#viewerStatus[data-ready="true"]').waitFor({timeout:120000});
  const elapsedMs=performance.now()-start;
  const metrics=await cdp.send('Performance.getMetrics');
  const resources=await page.evaluate(()=>performance.getEntriesByType('resource').filter(r=>r.name.includes('/builtin-world/')).map(r=>({url:r.name.split('/builtin-world/')[1],encoded:r.encodedBodySize,transfer:r.transferSize,decoded:r.decodedBodySize})));
  runs.push({repeat,elapsedMs,requests,encodedNetworkBytes:transfer,metrics:Object.fromEntries(metrics.metrics.filter(m=>['JSHeapUsedSize','JSHeapTotalSize','TaskDuration','ScriptDuration'].includes(m.name)).map(m=>[m.name,m.value])),builtinRequests:resources.length,builtinEncodedBytes:resources.reduce((s,e)=>s+e.encoded,0),errors});
  await context.close();
 }
 fs.writeFileSync('.superpowers/sdd/domain-data-restructure/loading-after.json',JSON.stringify({code:server.evidence.sourceCommit,data:server.evidence.dataCommit,runs},null,2));
 console.log(JSON.stringify(runs));
}finally{await browser.close();await server.close();}
