import fs from 'node:fs';import {chromium,expect} from '@playwright/test';
import config from '../../../playwright.config.js';import {startDevelopmentServer} from '../../../scripts/frontend-dev-server.mjs';
import {waitForCommittedMonth} from '../../../tests/browser/helpers/viewer-acceptance.mjs';
const server=await startDevelopmentServer({port:4189,observe:false}),browser=await chromium.launch({headless:true,...config.use.launchOptions});
const result={data:server.evidence.dataCommit,states:[],requests:[],errors:[]};
try{const page=await browser.newPage({viewport:{width:1280,height:800}});page.on('pageerror',error=>result.errors.push(error.message));page.on('request',request=>{if(request.url().includes('/physical-land/')||request.url().includes('/builtin-world/'))result.requests.push(request.url().split('/assets/data/')[1]);});
 await page.goto('http://127.0.0.1:4189/?debug=1');await expect(page.locator('#viewerStatus')).toHaveAttribute('data-ready','true',{timeout:90000});
 result.renderer=await page.evaluate(()=>{const gl=document.querySelector('.gpu-map-canvas').getContext('webgl2');const ext=gl?.getExtension('WEBGL_debug_renderer_info');return gl&&{renderer:ext?gl.getParameter(ext.UNMASKED_RENDERER_WEBGL):gl.getParameter(gl.RENDERER)};});
 result.initial=await page.evaluate(()=>{const a=window.__PANDOLAB_VIEWER__,d=a.documentSnapshot();return {entities:d.territorialEntities.length,geometries:d.geometries.length,bindings:d.timelineRecords.geometryBindings.length};});
 const initial=await page.evaluate(()=>window.__PANDOLAB_VIEWER__.builtinMonth().month);
 for(const month of ['1922-12',initial,'1922-12']){
  await page.locator('#timelineDateButton').click();await page.locator('#timelineViewUnit').selectOption('month');await page.locator('#timelineYearInput').fill(month.slice(0,4));await page.locator('#timelineMonthInput').selectOption(String(Number(month.slice(5))));await page.locator('#timelineGoBtn').click();
  await waitForCommittedMonth(page,month,{timeout:45000});result.states.push(await page.evaluate(()=>{const api=window.__PANDOLAB_VIEWER__,s=api.rendererStats();return {month:api.builtinMonth().month,cursor:api.documentState().timelineCursor,ready:s.mapReadiness,quality:s.activeMeshQuality,temporal:s.temporalPresentation};}));
 }
 result.passed=true;console.log(JSON.stringify(result));
}catch(error){result.passed=false;result.error=error.message;const page=browser.contexts()[0]?.pages()[0];if(page)result.failure=await page.evaluate(()=>{const api=window.__PANDOLAB_VIEWER__,s=api?.rendererStats();return {month:api?.builtinMonth().month,cursor:api?.documentState().timelineCursor,ready:s?.mapReadiness,quality:s?.activeMeshQuality,temporal:s?.temporalPresentation};}).catch(()=>null);console.log(JSON.stringify(result));process.exitCode=1;
}finally{fs.writeFileSync('.superpowers/sdd/domain-data-restructure/lazy-viewer-flow.json',JSON.stringify(result,null,2));await browser.close();await server.close();}
