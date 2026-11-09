# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: rendering/country-prepared-scene.spec.mjs >> Soviet 1922 extra stays ready without fabricated raster draws across reload and date return
- Location: tests/browser/rendering/country-prepared-scene.spec.mjs:153:1

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false

Call Log:
- Timeout 30000ms exceeded while waiting on the predicate
```

# Page snapshot

```yaml
- generic [ref=e2]:
  - banner [ref=e3]:
    - navigation "지도 메뉴" [ref=e4]:
      - button "파일 메뉴 열기" [ref=e6] [cursor=pointer]: 파일
      - button "보기" [ref=e7] [cursor=pointer]
      - button "점검" [ref=e8] [cursor=pointer]
      - button "설정" [ref=e9] [cursor=pointer]
  - main "지도 작업 공간" [ref=e11]:
    - generic "지도 자료 출처" [ref=e12]:
      - link "© OpenStreetMap" [ref=e13] [cursor=pointer]:
        - /url: https://www.openstreetmap.org/copyright
      - link "바이코누르 원본·파생 데이터 (ODbL)" [ref=e14] [cursor=pointer]:
        - /url: https://github.com/kimjeon-il/PandoLab-library-data/blob/0b080946cda3c9150ac07693b6c5b03951313027/reports/geography/ne-selected-20261023/odbl-source-and-derivative.zip
        - text: 원본·파생 데이터
    - generic "지도" [ref=e15]:
      - img:
        - generic:
          - generic:
            - generic [ref=e17]: 불가리아
            - generic [ref=e19]: 독일
            - generic [ref=e21]: 덴마크
            - generic [ref=e23]: 이집트
            - generic [ref=e25]: 에스파냐
            - generic [ref=e27]: 에티오피아
            - generic [ref=e29]: 핀란드
            - generic [ref=e31]: 영국
            - generic [ref=e33]: 아이티
            - generic [ref=e35]: 이라크
            - generic [ref=e37]: 아이슬란드
            - generic [ref=e39]: 일본
            - generic [ref=e41]: 모로코
            - generic [ref=e43]: 부탄
            - generic [ref=e45]: 스위스
            - generic [ref=e47]: 쿠바
            - generic [ref=e49]: 그린란드
            - generic [ref=e51]: 호주령 인도양 지역
            - generic [ref=e53]: 세인트헬레나
            - generic [ref=e55]: 헝가리
            - generic [ref=e57]: 캄보디아
            - generic [ref=e59]: 라이베리아
            - generic [ref=e61]: 노르웨이
            - generic [ref=e63]: 오만
            - generic [ref=e65]: 폴란드
            - generic [ref=e67]: 튀니지
            - generic [ref=e69]: 터키
            - generic [ref=e71]: 중화민국
            - generic [ref=e73]: 미국
            - generic [ref=e75]: 베네수엘라
            - generic [ref=e77]: 아프가니스탄
            - generic [ref=e79]: 이란
            - generic [ref=e81]: 몽골
            - generic [ref=e83]: 소련
          - generic:
            - generic: (현)이슬라마바드
            - generic: 다카
            - generic: (현)시우다드데라파스
            - generic: 코테
            - generic: 마드라스
            - generic: 니코시아
            - generic: 예카테린부르크
            - generic: 셰글롭스크
            - generic: 타슈켄트
            - generic: 사이공
            - generic: 하노이
            - generic: 도도마
            - generic: 바타비아
            - generic: 다이호쿠
            - generic: 톈진
            - generic: 광저우
            - generic: 대전
            - generic: 요코하마
            - generic: 지부티
            - generic: 다카르
            - generic: 브라자빌
            - generic: 리스본
            - generic: 몬로비아
            - generic: 아비장
            - generic: 캄팔라
            - generic: (현)아부자
            - generic: 빅토리아
            - generic: 코나크리
            - generic: 알제
            - generic: 발레타
            - generic: 코펜하겐
            - generic: 베른
            - generic: 빈
            - generic: 산마리노
            - generic: 티라나
            - generic: 앙카라
            - generic: 조지타운
            - generic: 레이캬비크
            - generic: 산토도밍고
            - generic: 카이로
            - generic: 하르툼
            - generic: 차리친
            - generic: 심비르스크
            - generic: 뉴욕
            - generic: 무르만스크
            - generic: 크라스노다르
            - generic: 예레반
            - generic: 포트루이스
            - generic: 쾰른
            - generic: 더블린
            - generic: 헬싱키
            - generic: 키예프
    - generic:
      - generic "지도 명령" [ref=e85]:
        - button "검색" [ref=e87] [cursor=pointer]
        - button "전체 지도 보기" [ref=e90] [cursor=pointer]
      - group "시점 이동" [ref=e93]:
        - button "10년 이전" [ref=e94] [cursor=pointer]
        - button "1년 이전" [ref=e97] [cursor=pointer]
        - button "1922년 12월, 월말 기준, 시점 직접 입력" [active] [ref=e100] [cursor=pointer]:
          - generic [ref=e103]:
            - generic [ref=e104]: 1922년 12월
            - generic [ref=e105]: 월말 기준
        - button "1년 이후" [ref=e106] [cursor=pointer]
        - button "10년 이후" [ref=e109] [cursor=pointer]
    - generic:
      - status: 지도 준비 완료.
    - status [ref=e112]
```

# Test source

```ts
  87  |       for (const [name, observe] of Object.entries(methods)) {
  88  |         const method = original[name];
  89  |         if (typeof method !== 'function') throw Error('Missing observed method: ' + name);
  90  |         descriptors[name] = { enumerable: true, configurable: false, writable: false,
  91  |           value(...args) {
  92  |             const before = { ...original.stats?.(), drawCallCount: original.drawCallCount };
  93  |             const result = method.apply(original, args);
  94  |             observe(result, args, original, before);
  95  |             return result;
  96  |           } };
  97  |       }
  98  |       return Object.freeze(Object.defineProperties({}, descriptors));
  99  |     };
  100 |     const OriginalWorker = globalThis.Worker;
  101 |     globalThis.Worker = class extends OriginalWorker {
  102 |       constructor(...args) {
  103 |         super(...args);
  104 |         this.addEventListener('message', ({ data }) => {
  105 |           if (data?.rpc !== 'pandolab-worker-rpc' || data.operation !== 'geometry.prepare' || !data.ok) return;
  106 |           for (const { cacheKey, packet } of data.result?.packets || []) if (probe.matches(packet)) {
  107 |             probe.record({ stage: 'worker', cacheKey, rasterState: packet.rasterState,
  108 |               triangleCount: packet.triangleCount, segmentCount: packet.segmentCount,
  109 |               coordinates: [...packet.ringCoordinates], ringOffsets: [...packet.ringOffsets], polygonOffsets: [...packet.polygonOffsets], stats: data.result.stats });
  110 |           }
  111 |         });
  112 |       }
  113 |     };
  114 |   }, SOVIET_EXTRA);
  115 | 
  116 |   // Only main-thread factory exports are observed. Worker bytes, return values,
  117 |   // typed arrays, GPU calls, clock, readiness and draw counters are never changed.
  118 |   const wrappers = {
  119 |     'render-scene.js': ['createRenderSceneBuilder', `
  120 |       return p.wrap(original, { build: value => p.scene(value), patch: value => p.scene(value) });`],
  121 |     'gpu-polygon-overlay-pass.js': ['createGpuPolygonOverlayPass', `
  122 |       const draw = (value) => {
  123 |         const keys = [...p.keys].filter(key => value.gridCollapsedKeys?.includes(key));
  124 |         if (keys.length) p.record({ stage: 'gpu-draw', keys, succeeded: value.succeeded,
  125 |           renderedKeys: [...value.renderedKeys], missingKeys: [...value.missingKeys] });
  126 |       };
  127 |       return p.wrap(original, {
  128 |         hasPreparedResource: (value, [packet]) => {
  129 |           if (value === true && p.matches(packet)) { p.keys.add(packet.key); p.record({ stage: 'gpu-ready', key: packet.key, ready: value }); }
  130 |         },
  131 |         ensureResource: (value, [packet], pass, before) => {
  132 |           if (!p.matches(packet)) return;
  133 |           p.keys.add(packet.key);
  134 |           const after = pass.stats();
  135 |           p.record({ stage: 'gpu-resource', key: packet.key, ready: pass.hasPreparedResource(packet),
  136 |             rasterState: value.resource?.rasterState, byteLength: value.resource?.byteLength,
  137 |             uploadDelta: after.uploadBytes - before.uploadBytes,
  138 |             drawDelta: pass.drawCallCount - before.drawCallCount });
  139 |         }, drawPackets: draw, drawResourceItems: draw });`],
  140 |   };
  141 |   await page.route(/\/modules\/(render-scene|gpu-polygon-overlay-pass)\.js(?:\?|$)/, async route => {
  142 |     const file = new URL(route.request().url()).pathname.split('/').at(-1);
  143 |     const [name, body] = wrappers[file], response = await route.fetch();
  144 |     const source = await response.text(), signature = 'export function ' + name + '(';
  145 |     if (!source.includes(signature)) throw Error('Observed factory moved: ' + file);
  146 |     const observed = source.replace(signature, 'function __observed_' + name + '(')
  147 |       + '\nexport function ' + name + '(...args) { const original = __observed_' + name
  148 |       + '(...args), p = globalThis.__gridCollapsedAcceptance; ' + body + '\n}\n';
  149 |     await route.fulfill({ response, body: observed });
  150 |   });
  151 | }
  152 | 
  153 | test('Soviet 1922 extra stays ready without fabricated raster draws across reload and date return', async ({ page }, info) => {
  154 |   test.setTimeout(360_000);
  155 |   const ring = Array.from({ length: SOVIET_EXTRA.coordinates.length / 2 }, (_, i) => SOVIET_EXTRA.coordinates.slice(i * 2, i * 2 + 2));
  156 |   expect(createHash('sha256').update(JSON.stringify(['Polygon', [ring]])).digest('hex')).toBe(SOVIET_EXTRA.digest);
  157 |   const errors = [], consoleErrors = [], observations = [];
  158 |   page.on('pageerror', error => errors.push(String(error)));
  159 |   page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); });
  160 |   await observeGridCollapsedPipeline(page);
  161 |   const ready = async month => {
  162 |     await expect.poll(() => page.evaluate(expected => {
  163 |       const viewer = globalThis.__PANDOLAB_VIEWER__, stats = viewer?.rendererStats();
  164 |       return !!(viewer && (!expected || viewer.builtinMonth().month === expected)
  165 |         && document.querySelector('#viewerStatus')?.dataset.ready === 'true'
  166 |         && viewer.initialMapPresented() && stats.canonicalMeshReady && !stats.projectRenderBlocked
  167 |         && stats.countriesPublishedGeneration === stats.projectGeneration
  168 |         && stats.pendingCountryCount === 0 && stats.surfaceDraw?.countryIndexCount > 0
  169 |         && stats.countrySharedBoundaryReady);
  170 |     }, month), { timeout: 90_000 }).toBe(true);
  171 |   };
  172 |   const year = async value => {
  173 |     await page.locator('#timelineDateButton').click();
  174 |     await page.locator('#timelineViewUnit').selectOption('month');
  175 |     await page.locator('#timelineYearInput').fill(String(value));
  176 |     await page.locator('#timelineMonthInput').selectOption('12');
  177 |     await page.locator('#timelineGoBtn').click();
  178 |     await ready(value + '-12');
  179 |   };
  180 |   const check = async (label, reuseScene = false) => {
  181 |     await expect.poll(() => page.evaluate(reuse => {
  182 |       const p = globalThis.__gridCollapsedAcceptance;
  183 |       const rows = p.events.filter(row => row.round === p.round);
  184 |       return (rows.some(row => row.stage === 'scene') || reuse && p.events.some(row => row.stage === 'scene'))
  185 |         && rows.some(row => row.stage === 'gpu-resource' || !reuse && row.stage === 'gpu-ready' && row.ready)
  186 |         && rows.some(row => row.stage === 'gpu-draw');
> 187 |     }, reuseScene), { timeout: 30_000 }).toBe(true);
      |                                          ^ Error: expect(received).toBe(expected) // Object.is equality
  188 |     const evidence = await page.evaluate(() => {
  189 |       const p = globalThis.__gridCollapsedAcceptance;
  190 |       return { rows: p.events.filter(row => row.round === p.round),
  191 |         workers: p.events.filter(row => row.stage === 'worker'), stats: __PANDOLAB_VIEWER__.rendererStats() };
  192 |     });
  193 |     expect(evidence.workers.length).toBeGreaterThan(0);
  194 |     for (const row of evidence.workers) {
  195 |       expect(row.rasterState).toBe('grid-collapsed');
  196 |       expect(row.triangleCount).toBe(0); expect(row.segmentCount).toBe(0);
  197 |       expect(row.coordinates).toEqual(SOVIET_EXTRA.coordinates);
  198 |       expect(row.ringOffsets).toEqual([0, 4]); expect(row.polygonOffsets).toEqual([0, 1]);
  199 |       expect(row.stats.builds).toBe(0); expect(row.stats.assetHits).toBeGreaterThan(0);
  200 |     }
  201 |     for (const row of evidence.rows) {
  202 |       if (row.stage === 'scene') {
  203 |         expect(row.coordinates).toEqual(SOVIET_EXTRA.coordinates);
  204 |         expect(row.rasterState).toBe('grid-collapsed'); expect(row.triangleCount).toBe(0); expect(row.segmentCount).toBe(0);
  205 |       }
  206 |       if (row.stage === 'gpu-resource') {
  207 |         expect(row.ready).toBe(true); expect(row.rasterState).toBe('grid-collapsed');
  208 |         expect(row.byteLength).toBe(0); expect(row.uploadDelta).toBe(0); expect(row.drawDelta).toBe(0);
  209 |       }
  210 |       if (row.stage === 'gpu-draw') {
  211 |         expect(row.succeeded).toBe(true);
  212 |         for (const key of row.keys) { expect(row.renderedKeys).not.toContain(key); expect(row.missingKeys).not.toContain(key); }
  213 |       }
  214 |     }
  215 |     const selected = await page.evaluate(async () => {
  216 |       const meta = globalThis.PANDOLAB_BUILD_META;
  217 |       const { temporalMonthEnd } = await import('./assets/js/modules/temporal.js?v=' + meta.assetRevision);
  218 |       const month = __PANDOLAB_VIEWER__.builtinMonth().month;
  219 |       return { month, effectiveDate: temporalMonthEnd(month).canonical };
  220 |     });
  221 |     expect(selected).toEqual({ month: SOVIET_EXTRA.selectedMonth, effectiveDate: SOVIET_EXTRA.effectiveDate });
  222 |     observations.push({ label, selected, expectedScope: SOVIET_EXTRA.scope, ...evidence });
  223 |   };
  224 |   try {
  225 |     await page.goto('/?debug=1&renderer=webgl2', { waitUntil: 'domcontentloaded' });
  226 |     await ready();
  227 |     const bindings = await page.evaluate(async () => {
  228 |       const response = await fetch(globalThis.PANDOLAB_BUILD_META.builtinWorld.url);
  229 |       if (!response.ok) throw Error('Pinned builtin scope index unavailable');
  230 |       const index = await response.json();
  231 |       return ['state:soviet-union', 'state:soviet-union-ukrainian-ssr'].map(id => {
  232 |         const row = index.readIndex.records.geometryBindings.find(value => value.objectRef.id === id
  233 |           && value.validFrom === '1922-12-30');
  234 |         return { id, validFrom: row?.validFrom, validTo: row?.validTo };
  235 |       });
  236 |     });
  237 |     for (const binding of bindings) {
  238 |       expect(binding.validFrom).toBe(SOVIET_EXTRA.validFrom); expect(binding.validTo).toBe(SOVIET_EXTRA.validTo);
  239 |     }
  240 |     observations.push({ selectedScopeBindings: bindings });
  241 |     for (const mode of ['cold', 'reload-reuse']) {
  242 |       if (mode === 'reload-reuse') { await page.reload({ waitUntil: 'domcontentloaded' }); await ready(); }
  243 |       await year(1922); await check(mode + '-1922');
  244 |       await year(2024);
  245 |       await page.evaluate(() => { globalThis.__gridCollapsedAcceptance.round++; });
  246 |       await year(1922); await check(mode + '-return');
  247 |     }
  248 |     const beforeRestore = await page.evaluate(() => {
  249 |       const { revision, checkpoint, timelineCursor } = __PANDOLAB_VIEWER__.documentState();
  250 |       return { revision, checkpoint, timelineCursor };
  251 |     });
  252 |     await page.evaluate(() => {
  253 |       const gl = document.querySelector('#viewerCanvas').getContext('webgl2');
  254 |       const extension = gl?.getExtension('WEBGL_lose_context');
  255 |       if (!extension) throw Error('Real WebGL context-loss exercise is unavailable');
  256 |       globalThis.__gridCollapsedAcceptance.round++;
  257 |       globalThis.__gridAcceptanceContext = extension;
  258 |       extension.loseContext();
  259 |     });
  260 |     await expect.poll(() => page.evaluate(() => __PANDOLAB_VIEWER__.rendererStats().webglContextLost)).toBe(true);
  261 |     await page.evaluate(() => globalThis.__gridAcceptanceContext.restoreContext());
  262 |     await ready('1922-12');
  263 |     await check('real-context-restored', true);
  264 |     expect(await page.evaluate(() => {
  265 |       const { revision, checkpoint, timelineCursor } = __PANDOLAB_VIEWER__.documentState();
  266 |       return { revision, checkpoint, timelineCursor };
  267 |     })).toEqual(beforeRestore);
  268 |     expect(errors).toEqual([]); expect(consoleErrors).toEqual([]);
  269 |     await page.screenshot({ path: info.outputPath('soviet-1922-grid-collapse.png') });
  270 |   } finally {
  271 |     await writeFile(info.outputPath('soviet-1922-grid-collapse.json'), JSON.stringify({
  272 |       target: SOVIET_EXTRA, observations, errors, consoleErrors,
  273 |       limits: ['Main-thread observation wrappers are test-only; routing disables HTTP cache, so reload-reuse is not an HTTP-cache claim.', 'Canvas-specific fallback delivery is a separate acceptance case.'],
  274 |     }, null, 2));
  275 |   }
  276 | });
  277 | 
```