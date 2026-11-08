import fs from 'node:fs';
import {chromium,expect} from '@playwright/test';
import config from '../../../playwright.config.js';
import {startDevelopmentServer} from '../../../scripts/frontend-dev-server.mjs';
const server=await startDevelopmentServer({port:4189,observe:false});
const browser=await chromium.launch({headless:true,...config.use.launchOptions});
const result={code:server.evidence.sourceCommit,data:server.evidence.dataCommit,errors:[]};
try{
 const page=await browser.newPage({viewport:{width:1280,height:800}});page.on('pageerror',error=>result.errors.push(error.message));
 await page.goto('http://127.0.0.1:4189/?debug=1');await expect(page.locator('#viewerStatus')).toHaveAttribute('data-ready','true',{timeout:90000});
 result.before=await page.evaluate(()=>({state:window.__PANDOLAB_VIEWER__.documentState(),view:window.__PANDOLAB_MAP_HOST__.getViewState()}));
 await page.mouse.move(640,420);await page.mouse.down();await page.mouse.move(720,450,{steps:5});await page.mouse.up();await page.mouse.wheel(0,-120);
 await expect.poll(()=>page.evaluate(()=>window.__PANDOLAB_MAP_HOST__.getViewState().globeZoom)).toBeGreaterThan(result.before.view.globeZoom);
 result.afterInput=await page.evaluate(()=>window.__PANDOLAB_MAP_HOST__.getViewState());
 expect(result.afterInput.globeRotation).not.toEqual(result.before.view.globeRotation);
 await page.evaluate(()=>{const h=window.__PANDOLAB_MAP_HOST__;h.setViewState({projection:'globe',view:{...h.getViewState(),globeRotation:[-2.3,-48.8,0],globeZoom:4}});h.requestRepaint('final-body-pick');});
 await expect.poll(()=>page.evaluate(()=>window.__PANDOLAB_VIEWER__.rendererStats().mapReadiness.mapReady),{timeout:20000}).toBe(true);
 await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
 const point=await page.evaluate(()=>window.__PANDOLAB_MAP_HOST__.project([2.3,48.8]));
 const bounds=await page.locator('#map').boundingBox();await page.mouse.click(bounds.x+point[0],bounds.y+point[1]);
 await expect.poll(()=>page.evaluate(()=>window.__PANDOLAB_VIEWER__.selectionSnapshot().items.map(row=>row.id)),{timeout:15000}).toContain('FRA');
 result.selection=await page.evaluate(()=>window.__PANDOLAB_VIEWER__.selectionSnapshot());
 result.after=await page.evaluate(()=>window.__PANDOLAB_VIEWER__.documentState());
 for(const key of ['revision','checkpoint','documentDirty'])expect(result.after[key]).toEqual(result.before.state[key]);
 expect(result.errors).toEqual([]);result.passed=true;
}catch(error){result.passed=false;result.error=error.message;process.exitCode=1;}
finally{fs.writeFileSync('.superpowers/sdd/domain-data-restructure/viewer-input-flow.json',JSON.stringify(result,null,2));await browser.close();await server.close();}
console.log(JSON.stringify({passed:result.passed,error:result.error,errors:result.errors}));
