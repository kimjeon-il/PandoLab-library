# Preview retirement and numeric DEM packaging

Implemented in shared work/gis; child performed no application commit/push/deployment.

- Initial SVG land owner, generated initial-land-preview, metadata requirement, loading/reveal CSS/state and reader/controller/composition ports removed.
- data-loader-worker now only loads optional source-verified prepared canonical scenes; removed preview/geometry/canonical bootstrap stages. builtin-mesh-resource uses one worker URL with no legacy mode.
- World bundle normalization/publication, runtime closure, staging and artifact graph select canonical packet/mesh/labels/prepared scene and canonical boundaries only. Archived preview fields are ignored metadata; no original archived assets deleted.
- build-world-preview replaced by build-world-country-packet; preserves canonical packet encoding/classification, does not build preview polygons/meshes. world-preview artifact family and direct auto-publication/check/package callers renamed. Source recipe legacyPreviewManifest remains unchanged stored metadata; no vector source/storage modification.
- project-preview-policy and preview-specific admission tests removed; its sole live geometryFingerprint consumer retains exact hash implementation inside canonical packet producer.
- Native country validator now validates canonical source only. Preview gzip branch and --canonical-only option removed; duplicate registered canonical validation collapsed. Required parent CI check: country-selftest. No local compiler/build run.
- Precolored terrain build/check entrypoints and their builder/source helpers removed; dispatcher refuses terrain-preview. Numeric grid tests/helpers preserved as terrain-tile-grid. Native package-terrain-preview/native utility intentionally retained: tools/gis/build-physical-terrain.mjs uses its physical resize/luminance/compositor functions, and physical-terrain-native tests verify that offline tool. Not an application preview asset path.
- default-world selects assets/data/terrain/v0.13.3/manifest.json. Map catalog coherence validates numeric representation independently of physicalLand lineage. Runtime closure includes tile receipts and excludes tint.

## Existing DEM source/package evidence

Original pin: f26d0896ab393aa351938637571347baa09ebf71
Original tree: 23435d594df2bfe4809e6ada9e9c1013a0af396a
Original manifest SHA256: e63ac5f18188bd55c8eb032ad0a9e1a6bfb14232b617758ca9076e35771391ff
Original assetsSha256 verified using existing terrainAssetDigest: 622a6d272bdda6b507a1f4ba49794fe9ef41aca06f29d8b38e24114caa50d023
1280 numeric tiles = 852,527,664 bytes, transferred without changing pixels/encoding.
Tint 2,433,794 bytes not copied. Source top-level Git tree unchanged.
Runtime manifest SHA256: 51c09ccefc54cf8a58d3571d9c11862f077656474fb2fcc0a9101cc36829fd87
Local scoped storage revision: 5dc14820019f78f1322258a752f4b6e248c30c4c, parent 7435ad1f05a452f08e582ea7896165c15f9eca20; not pushed.
Direct storage diff: 1281 terrain entries only. Compared with original pin, existing data branch ancestors also contain 28 report entries. All other runtime archive entry metadata unchanged. See terrain-archive-evidence.json.
Disk preflight: free 35,764,416,512 B; conservative peak 1,705,055,328 B plus 5 GiB headroom passed. No tar/verification copy created. Materialized numeric tiles remain required by current branch pin/runtime.

## Focused validation

- Initial contract red: preview-free world manifests/build metadata failed as expected; first world/frontend suite then passed 10 tests.
- Composition/closure/product tests passed 23; source-free generator/worker/physical/publication checks passed 16.
- Synthetic staging/artifact/auto-publication batch: 123 tests, 109 passed, 14 initially failed. Fixed directly affected obsolete fixture roles, Windows URL pathname, stale source descriptor fixtures; all 14 rechecked passing in 25-test retry plus one selected P2 ownership test. No real GIS validation/generation performed.
- Final integrated frontend/DEM packaging/world generator/closure/composition: 31 passed (preview-dem-integration.log).
- Final actual synthetic stage proof: 2 passed (preview-staging-final.log); preview descriptor obsolete versions ignored/not staged, canonical asset integrity retained.
- Numeric grid/GIS allowlist: 14 passed (terrain-retirement-tests.log).
- ESLint passed selected 14 changed/new JS modules and tests, including both new packaging producers and runtime loading path.
- Browser/backend pixels, real timing, native country-selftest CI and final application/data/report publication remain parent-owned.

Task evidence logs are retained only for parent report assembly; remove/archive after report completion. No source/GIS or original evidence deletion performed.

## Canvas core closure and focused CI follow-up

- Moved factory dynamic import registration from canvas-render-worker.js to canvas-render-core.js; classic Worker closure includes all seven imports. Inline Canvas gets public core and terrain-manifest without the unhashed Worker entry.
- Product closure/frontend synthetic tests: 18 passed; changed product-assets ESLint passed. Real buildFrontendSnapshot against 5dc1482 succeeded without preparation or tile payload reads; evidence canvas-core-actual-build.json.
- Registered all ten newly introduced tests with focused existing owners; moved GIS group before generic object ownership for project LOD tests and bound core extraction to relevant Canvas/terrain checks. Structural repository/catalog load passed.
- Added manual shared-core geometry-wasm scope: existing pinned CMake/Emscripten and integrity-preserving zlib workaround; only pando-wasm build target, package new source-matched assets, registered wasm-domain-geometry runner (only core-assets prerequisite), immutable trio artifact on success. YAML parsed and exact plan structurally verified. Not dispatched by this agent; parent controls commit/push/CI.

## Explicit residual-cleanup pass (checks deferred by user)

Removed dead startup readiness policy/session fields and ports, preview-only editor boundary payload override, initial SVG browser suites (replaced by gated formal first-frame coverage), stale preview DOM assertions, dead topology-preview generator modules, dead persistence preview ports and unused performance fields. Canonical fixtures no longer generate preview meshes; targeted exclusion cases retain invalid old descriptors to prove no runtime/publication dependency. Benchmark retains canonical/stress only.

Standalone terrain native tool renamed physical-terrain (outside shared WASM source roots). Removed PDTERR01 compose/default dispatch and dead JS API. Live mask, RGB/mask resize, luminance and streaming composite operations remain; source/package/env/workflow consumers updated coherently. Registered command physical-terrain-native uses native-physical-terrain prerequisite; fixed output build-native/physical-terrain/artifact. No local/native/browser/unit checks executed during this pass.

Retained names: immutable world recipe legacyPreviewManifest/world-preview-v*.json are existing canonical packet/mesh/labels descriptor storage names, not generated preview resources; archive fixture source hashes and frozen portability snapshots remain untouched. Deployment/review/editor overlays and Map Toolkit reference-map image preview are separate live operations. Frozen tests/fixtures/terrain-preview-kernel.json remains original reference evidence, with no executable consumer. docs/terrain-preview.md explicitly marked historical/retired.

## Final producer-consumer correction

Further tracing established that the alleged live physical-terrain owner only generated retired NE precolored terrain/v0.12.6, never current numericDEM. Removed it, the build-physical-data wrapper, all standalone compositor/mask sources/package/helper/tests/CI and the temporarily added physical-terrain prerequisite. Removed sole-caller resizePhysicalRgb from map-image; generic resampling/encoding stays. Source dispatcher now calls existing physical-hydro CLI directly. Original oracle fixtures remain preserved. The earlier native physical-terrain CI recommendation is superseded: no such target remains. Focused native-map-image preparation with tests/unit/document/physical-webp-stream.test.mjs is sufficient for affected shared image owner; geometryWASM untouched. No tests executed.

## Frozen oracle regression repair

The failed admitted oracle was not Windows CRLF. Historical app commit b4bec4bce changed only its generated-by comment from tools/build-country-default-colors.mjs to tools/build/build-country-default-colors.mjs (4742 instead of4736bytes); allotheroraclefiles matched original Git objects. Restored country-default-colors.js from verified existing blob6f355d0b06e6f286c457a9c4ad286485ba4e1756, SHA25646e2e18f2fb78058edd7d990ecc99d9a81cb087dc3f0ca2de55f7771d5660730. Verifier and manifest unchanged. Evidence frozen-oracle-repair.json.

Two previously failing oracle-importing tests ran42pass/1fail. Remaining failure was old spatial fixture missing the production store transition callback that increments accepted territorial geometry revision; wired real onEntitiesReplaced and preserved old/new bounds assertions plus unchanged-resource reuse. Only remaining failedcase re-run:1pass. Logs frozen-oracle-retry.log and frozen-oracle-spatial-retry.log.
