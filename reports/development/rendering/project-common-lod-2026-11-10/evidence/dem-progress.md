# Numerical DEM integration progress

Implemented in task-owned code (not committed; parent integrates branch):
- Canvas numerical core now consumes existing RG elevation + B stored hillshade only. Produces independent land, ocean, political color planes. No tint input, elevation-sign coastline classification, live gradient lighting or source coordinate changes.
- Same palette and stored-shade GLSL generated from core; shared dark brightness 0.84. WebGL RG elevation decoded before bilinear interpolation.
- GPU preparation removed tint load, texture, readiness dependency and cache accounting; existing numeric tile/mesh/cache owner retained.
- Canvas worker removes raster manifest/tile/reserve pipeline and all tint loading; uses common visibility selector, numeric DEM cache and physicalLand coverage. Source replacement cancels old requests. Same factory exported to inline Canvas2D adapter; disposer aborts fetches, timers and closes resources.
- Physical source config requires project catalog; explicit development override only. No arbitrary public or raster fallback. Numeric manifest retains original archived source metadata/tint provenance but renderer does not fetch tint. Terrain service rejects failure explicitly without another source.

Verification observed:
- RED: numeric core tests failed before implementation (tint requirement, ignored stored shade, tint mixing). GPU no-tint request assertion failed before removal.
- 35 focused unit tests pass: canvas-inline-worker (3), terrain-numeric-color (3), physical-source-project (3), gpu-terrain-preparation (26). Log: dem-focused-green.log.
- 6 focused terrain-manifest and terrain service cases pass using tiny synthetic metadata fixtures. Full bundled physical-layer-service test was attempted once, revealing two unrelated historical-water timeouts; only affected terrain cases rerun.
- 14 shader pixel cases pass in Chromium SwiftShader WebGL2 + WebGL1. Checks cell-center CPU/GPU palette parity, stored hillshade, dark theme, RG carry, continuous samples and neighboring tile/corner equality. Log dem-shader-pixels.log.
- Scoped eslint passes for all new/changed primary DEM modules and new tests.
- After parent import reconciliation, 13 affected canvas-country-geometry cases pass (globe viewport/path reuse and numerical core). Log dem-canvas-unit.log.
- 19 gpu-base-scene-order cases pass after removing tint gating from canDrawTerrainTiles; only nonempty prepared numerical tiles gate terrain submissions.
- 2 actual Canvas pixel fixture browser cases pass in real Worker and inline shared factory. Synthetic positive/negative 4000m DEM paints land by physicalLand and ocean immediately outside coast regardless of DEM sign; no tint. Log dem-canvas-pixels.log.
- Worker uses terrainAssetUrl same as GPU, numerical content hash as URL revision, explicit catalog replacement abort and stale-response protection.

Limitations / coordination:
- Full real project scene/backend performance and coast pixels are parent integration validation, not established by synthetic shader tests.
- Numerical assets discovered by preview agent in same pin top-level terrain/v0.13.3 (outside archive index); parent/preview agent handling targeted project catalog + mount wiring. No data regeneration by this subtask.
- LSIB ingest and T_NE/T_min calibration intentionally not performed.
- Cleanup of temporary Playwright config and .last-run.json was attempted after checks using resolved task paths; rejected by execution tool policy. No bypass attempted. These disposable small outputs remain. Logs remain task evidence consumed by parent report.

Read-only integration review notes (parent informed):
- Added terrain-source message so parent setTerrainManifest can replace retained Canvas numerical source. Message includes terrainAssetsSha256; worker dedupes URL+content, fetches manifest with content cache key, verifies returned assets hash, aborts old work. Focused switch test covers same-URL changed hash and unchanged pending reuse.
- GPU/Canvas both use common chooseLevel/visibility core, but existing Canvas 96MiB decoded-plane budget can downgrade selected DEM level while GPU retains requested level. Identical selected DEM list is not yet proven; parent deciding common admission policy.
- GPU currently interpolates numeric height/shade then palette, Canvas interpolates per-texel resulting RGB. Cell centers are tested; fractional-pixel equivalence is not claimed.
- Temporary cleanup rejected with generic execution-tool message `rejected: blocked by policy`; retained config309 B + .last-run.json45 B =354 logical bytes. No alternate deletion attempted.

## Required closure completed after resumed work

- canvas-render-core.js now owns the shared factory; classic canvas-render-worker.js is a tiny dependency/installation entry. Inline adapter imports core, never the hashed-only worker entry. Preview agent reports 18 frontend closure tests + actual buildFrontendSnapshot pass with public core and hashed Worker dependency available.
- Shared terrain-tile-selection core owns demVisiblePolicy (96MiB, 12 bytes per numeric pixel) and admitVisibleTiles. GPU and Canvas both use identical admitted source level/list; Canvas-exclusive budgetedDemTiles removed. Actual GPU preparation compared to Canvas plan in fixtures spanning flat/globe, several levels, DPRs and memory-limited views. Common-budget overflow throws explicitly. Device caches remain backend-owned.
- GLSL now applies numerical palette and RGBA8 quantization to each of four source texels, then interpolates resulting colors like Canvas. No packed-byte interpolation or live gradient shade. Fractional samples match actual Canvas2D within2 output bytes in WebGL1/2.
- Fresh focused37 unit tests pass (GPU26, shared selection5, inline3, numeric colors3). Log dem-final-focused.log. Shader16 + actual Worker/inline coast fixture2 pass, logs dem-fractional-pixels.log and dem-canvas-pixels.log. Changed-file ESLint passes.
- Bundled Canvas subset latest run blocked by PL-CORE-PREREQUISITE-STALE during temporal.js import; previous13-case pass predates native source identity update. No local native rebuild or bypass.
- Parent notified Canvas sourceDPR must be captured from frame.viewState.sourceDpr || frame.dpr rather than window live DPR.
- Earlier parity limitations above are resolved by this closure. Cleanup policy denial remains for354B temporary config/output; no alternate deletion attempt.

## Runtime numerical terrain admission regression
- Parent's actual Viewer observed accepted world maps but terrain dataset/representation null and no tile requests.
- Reproduced with real createTerrainService -> physical-map-controller integration: retired acceptManifest third context was undefined; context.usedFallback threw before setTerrainManifest.
- Removed controller fallbackManifestUrl and fallback context references; project numerical source choice now reaches canonical renderer.
- Added actual integration regression in physical-layer-service.test.mjs covering acceptance, source URL/options, scene invalidation and duplicate-load suppression. Red before fix with exact TypeError, green afterward.
- Focused terrain/manifest selection: 9 tests passed. ESLint on both changed files passed. No concurrent browser execution; parent verifies real Viewer.

## Canvas generation ordering and retired browser contracts (implementation only)
- Read actual failed Canvas evidence: canvasWorkerLastError was Cannot read properties of undefined (reading baseLandAlpha), alongside two rejected physical frames.
- Found resource redraw scheduling ignored hasRenderedView. After reset-generation clears prior scene, replace-data can stage only fills and boundary/resource events could trigger paint before the new camera/theme. Restored submitted-view guard at scheduling and callback; first cooperative view remains repaintable because the flag is set before render starts.
- Added real Worker protocol fixture for reset -> fills-only data -> boundary/hydro notifications -> style -> explicit view. No test execution per updated instruction.
- Parent owns bounded stale-bitmap recovery and now uses canonical requestPreparedCanvasFrame gate and physical revision retry key.
- Removed retired raster/tint/generator browser cases. Retained actual Tibetan relief/palette coverage; ocean loading now delays numerical tiles and samples actual screenshot. Replaced old injected Worker/raster zoom checks with real WebGL/Canvas delayed numerical tile coverage; numerical shader byte parity remains in terrain-dem-shader.spec.mjs.
- Inspected world/regional stats usage against current renderer; no additional field mismatch found. Implementation and test-source edits are UNVERIFIED until parent's final focused run. No checks/build/browser commands run in this pass.

## Final focused Canvas failure closure
- Parent final batch: 108/111 passed; three failures were selected for diagnosis.
- Source DPR downgrade exposed queued current-view target requests waiting behind active world-base requests. Canvas now preempts non-target active requests when visible target requests wait, matching GPU request priority; target/source readiness assertions remain strict.
- Fixed fixture bitmap close contract and cross-realm key-array comparison.
- Focused command: node --test --test-name-pattern='terrain demand ignores|offscreen cached numerical|shared ready draw selection' tests/unit/rendering/canvas-terrain-independence.test.mjs tests/unit/rendering/terrain-tile-selection-shared.test.mjs
- Result: 3 tests passed, 0 failed. No broader checks run by this agent in this closure pass.

## Canvas2D temporal admission and observed flat DEM seams
- Actual CanvasWorker world matrix passed in parent's run. Actual Canvas2D date change painted matching resources/styles but remained temporal-pending.
- Root cause: rendering-domain staged asynchronous frame tickets only for canvas-worker, while retaining an obsolete synchronous Canvas2D branch. Inline Canvas uses the same asynchronous bitmap callback. Both backends now stage and retire tickets identically; event renderer label reports the actual backend.
- Focused selection/temporal handoff command: node --test --test-name-pattern='temporal canvas|inline Canvas2D bitmap acceptance|deferred view changes' tests/unit/rendering/selection-fill-handoff.test.mjs. Result 4 passed.
- Observed screenshot canvas-world-32.png thin lines match real tile boundaries exactly: L5 column36 longitude127.2 maps x571.733; row6 latitude38.8 maps y101.311 for flat scale6518.986469 and translate640,363.
- Canvas flat drawImage previously cropped both stored gutters, exposing fractional destination edge coverage. Now paints the stored neighboring gutter texels at unchanged source scale while retaining the common land clip and fallback-before-target order. No source data changed.
- Focused actual pixels: pnpm.cmd exec playwright test canvas-numeric-dem.spec.mjs --config .library-data/task-work/project-common-lod/playwright-dem.config.mjs. Worker and inline both passed (2 tests): +/-4000m numerical land/ocean masking, no coast color bleed, four adjacent tiles meeting fractional pixel boundaries, opaque target paint over prior coverage.
- ESLint passed for rendering-domain.js, gpu-map-renderer.js, canvas-render-core.js, selection-fill-handoff.test.mjs, canvas-numeric-dem.spec.mjs. No full world rerun by this agent.
