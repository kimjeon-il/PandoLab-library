# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: project-common-lod.spec.mjs >> project-common-lod world canvas: accepted meshes, camera, selection and recovery
- Location: tests\browser\rendering\project-common-lod.spec.mjs:90:3

# Error details

```
Error: expect(locator).toHaveAttribute(expected) failed

Locator:  locator('#viewerStatus')
Expected: "true"
Received: "false"
Timeout:  120000ms

Call log:
  - Expect "toHaveAttribute" with timeout 120000ms
  - waiting for locator('#viewerStatus')
    5 × locator resolved to <span role="status" id="viewerStatus" aria-live="polite" aria-atomic="true" data-ready="false" class="ui-visually-hidden">지도 불러오는 중…</span>
      - unexpected value "false"
    232 × locator resolved to <span role="status" id="viewerStatus" aria-live="polite" aria-atomic="true" data-ready="false" class="ui-visually-hidden" data-loading-kind="initial">지도 불러오는 중…</span>
        - unexpected value "false"

```

```yaml
- status: 지도 불러오는 중…
```

# Test source

```ts
  1  | import { expect } from '@playwright/test';
  2  | 
  3  | // Shared acceptance boundaries for the shipped Viewer. Clock and renderer selection
  4  | // always stay with the caller, so a test can still hold external data or GPU work.
  5  | export async function openReadyViewer(page,{url='/?debug=1',timeout=90_000}={}){
  6  |   await page.goto(url,{waitUntil:'domcontentloaded'});
> 7  |   await expect(page.locator('#viewerStatus')).toHaveAttribute('data-ready','true',{timeout});
     |                                               ^ Error: expect(locator).toHaveAttribute(expected) failed
  8  | }
  9  | export async function waitForCommittedMonth(page,month,{timeout=90_000}={}){
  10 |   await expect.poll(()=>page.evaluate(()=>{
  11 |     const api=window.__PANDOLAB_VIEWER__;
  12 |     return {month:api?.builtinMonth?.()?.month,cursor:api?.documentState?.()?.timelineCursor,
  13 |       ready:document.getElementById('viewerStatus')?.dataset.ready};
  14 |   }),{timeout}).toEqual({month,cursor:month,ready:'true'});
  15 | }
  16 | export async function waitForCanonicalMap(page,{timeout=90_000}={}){
  17 |   await expect.poll(()=>page.evaluate(()=>{
  18 |     const r=window.__PANDOLAB_VIEWER__?.rendererStats?.();
  19 |     return Boolean(r?.canonicalMeshReady && !r.projectRenderBlocked && r.surfacePresentation?.quality==='canonical'
  20 |       && r.countriesPublishedGeneration===r.projectGeneration && r.mapReadiness?.mapReady);
  21 |   }),{timeout}).toBe(true);
  22 | }
  23 | 
```