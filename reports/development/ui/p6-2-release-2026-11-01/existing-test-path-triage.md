# Existing test / path triage

## Scope and outcome

Read-only diagnosis of the assigned failures in P3 web-contracts run **41265483904**, job **124727574107**. Baseline log: `p3-contracts-before.log`.

- Immutable candidate: `e53f067ef37cafc4bd5d4d50e323f8866e7c9833`.
- Immutable main: `2b460e40dbc51de2d13b0fe40e11bd4af9e49b75`.
- GitHub compare: candidate is 200 commits ahead, 0 behind, with 229 changed files.
- The **seven pre-existing test files have identical Git blob IDs** on candidate and main.
- The **two lint errors are newly introduced test-fixture defects**, not product runtime failures. Root reports its subsequent `globalThis.EventTarget` / `globalThis.CustomEvent` correction and 18 passing map-input unit cases; this triager did not rerun that correction.
- No source file was changed, no test was rerun, and no data/WASM/native environment was prepared in this triage.
- Existing unrelated failed checks remain **failed or unverified**, not passed. The root-reported 66 unrelated failures are not cleared by this report.

## Findings

| Group | Diagnosis | Main comparison and limit |
| --- | --- | --- |
| Lint, 2 errors | New map-input fixture uses bare `EventTarget` and `CustomEvent`, which ESLint rejects as `no-undef`. | New +152-line fixture relative to main. Root reports qualification fix; final lint gate pending. |
| River partition source test | Bare `readFileSync` has no named import; only default `fs` is imported. Two later reads also use old `assets/js` source paths. | Test bytes identical. The observed ReferenceError occurs before reading product modules. Later assertions were not exercised. |
| Startup, 3 regex failures | Source-text expectations no longer follow the current owners/contracts. Two cases are confirmed below; snapshot-symbol ownership remains incompletely traced. | Test identical. Several rendering modules have branch changes; this report does not certify runtime performance. |
| Territorial lifecycle | Fixture omits `reportOperationError`; its Proxy helper returns undefined for that port. | Test/helper/assembly unchanged; presentation's reporter requirement unchanged. Its sole diff is the independent viewer-cancel guard. |
| Country-label input, 6 failures | Fixture supplies only `objectDisplayInfo`, omitting required `objectRefVisible`. | Test, picking consumer, and foundation mapping unchanged. Object commands have other branch edits, not ruled on here. |
| Core prerequisite, 3 failures | Synthetic assets are written to `assets/wasm`, while loader reads `shared/frontend/static/wasm`. | Test, loader, and layout owner unchanged. No prerequisite test/build was executed. |
| Core product mode, Worker entry | A direct source import uses the default Worker factory outside the generated immutable-asset context. | Test/resolver unchanged. Client's new temporal-operation hunks leave the existing Worker factory intact. |
| Current browser contracts | `changedFiles` uses deployed `assets/css` and `assets/js` URL paths instead of repository source paths. | Test and selector unchanged. Inspected catalog changes only add deferred/manual registrations. |

### Startup regex detail

1. **`createResourceSnapshot`** — the immutable-main code search returned only the test reference. The production owner/replacement for that symbol was not confirmed before scope closure. This is evidence of an obsolete source-text oracle, **not a measured rendering regression or a performance pass**. The branch changes `gpu-map-renderer.js`, `gpu-scene.js`, and `map-content-presentation.js`.
2. **`MANIFEST_URL.searchParams.set('v', DATA_REVISION)`** — unchanged `data-loader-worker.js` now requires `buildMeta.worldBundle` and calls `manifestLoader.loadAsset(buildMeta.worldBundle, ..., parseVerifiedWorldBundle)`. Data revision remains part of the stored-asset loader contract; the old literal URL-mutation expectation does not describe the current pinned-manifest workflow.
3. **Inline `canonicalCountryStore` mapping** — the exact mapping exists in unchanged `shared/frontend/js/modules/map-owner-ports.js` under `MAP_READ_PORT_SPECS.builtinCountries`. Foundation imports/delegates through `createReadPorts`; expecting the literal in the foundation file is stale owner coupling.

### Dependency-fixture evidence

- `capabilityPortsForFixture` reads `flatDependencies[property]`. The lifecycle test's overrides do not include `reportOperationError`, yet the real presentation validates it before startup.
- The label test's `objectOperationsA` fixture contains only `objectDisplayInfo`. Real `object-picking.js` calls `objectRefVisible` at line 36 before explicit label selection. Foundation exposes that capability from `objectCommands`, and current object commands acquire it from `createObjectQuery`.
- The Worker test overrides global `Worker` but imports the un-emitted client source. `workerAssetUrl` searches for the deployed `/assets/js/` namespace and requires immutable Worker metadata; its input is instead a `/shared/frontend/js/workers/` file URL. Repair the generated-frontend fixture, not the production resolver.

### Minimal future repair scope

These are recommendations only; none were applied here.

- River: correct the fs access/import and the two source-owner paths; preserve the partition assertions.
- Lifecycle: supply the required reporter in the fixture; keep fail-visible dependency validation.
- Label input: wire the current visibility capability, retaining explicit identity, hidden-object, blocking, modifier and placement coverage.
- Core prerequisite: use the canonical `frontendWasmRoot`; also avoid an `EEXIST` when the nested asset directory creates `shared` before the existing mkdir call.
- Worker entry: use the generated frontend/immutable metadata harness while exercising the real default Worker factory.
- Browser selector: use `shared/frontend/css/features/map-rendering.css` and `shared/frontend/js/workers/canvas-render-worker.js` as changed repository paths.
- Startup: update owner/behavior checks carefully; do not infer runtime correctness from replacement regex matches.

## Direct test-byte comparison

| File | Blob on both candidate and main |
| --- | --- |
| `tests/unit/river-territory-partition-source.test.mjs` | `f40e66ea0ce8c58e5895234a7f27419af73a2579` |
| `tests/unit/startup-performance-contract.test.mjs` | `a54877f80f866a3d58b1fa8b3530b9950d92789f` |
| `tests/unit/territorial-editor-lifecycle.test.mjs` | `3bd675d77f213d3a74f5da4832310e572acc701b` |
| `tests/unit/country-label-input-contract.test.mjs` | `a00d6ce9d2fb4c367a9b156c5b5a16b6eda4b4f7` |
| `tests/unit/core-prerequisite.test.mjs` | `0ff91828ee86dcc2cde3b21e44ce0fd475758abc` |
| `tests/unit/core-product-mode.test.mjs` | `e47bef9a4b69c237bdc026579b71811abe3cf891` |
| `tests/unit/current-browser-contracts.test.mjs` | `8ee19488d7342b75466692b4772ebc74f93a9c70` |

## Production comparison: what is and is not established

The complete 229-file compare establishes that the following inspected owners are unchanged: object picking, Worker asset resolver, lifecycle assembly, capability-fixture helper, foundation mapping, shared map-owner ports, data-loader Worker, Node core loader, frontend layout, application-check selector, and rendering domain. Full per-file main bodies were not fetched separately for every owner; the JSON records whether evidence comes from direct blob equality or the complete compare.

Changed owners relevant to the broader neighborhoods include:

- `map-input-presentation.js`: **+1/-0**, only the viewer cancel guard; required reporter validation unchanged.
- `core-document-client.js`: **+48/-6**, temporal queue/cancellation behavior; its fixed Worker factory is outside the changed hunks.
- `app-object-commands.js`: **+39/-16**; current visibility capability wiring was read, but all object-command changes were not audited.
- `gpu-map-renderer.js`: **+694/-154**; `gpu-scene.js`: **+12/-1**; `map-content-presentation.js`: **+7/-5**. Their broader runtime effects were not validated by this task.
- Application-check catalog: **+19/-2**, inspected deferred/manual registrations; no CSS owner-path repair in that diff.

Identical stale tests do not prove all product behavior is identical. This report classifies the observed failure mechanisms and preserves the unverified areas.

## Other observed/contextual results

The same core-product-mode file also has a later whole-project equality failure involving canonical geometry order. That is distinct from the Worker-asset failure and belongs to the separate Core/oracle investigation.

Root separately reports the boundary-generator fixture's **8 real CI cases passed** in run **41266000828**, job **124728815278**. That result does not clear the failures triaged here.

## Evidence links

- [Immutable comparison](https://github.com/kimjeon-il/Pando/compare/2b460e40dbc51de2d13b0fe40e11bd4af9e49b75...e53f067ef37cafc4bd5d4d50e323f8866e7c9833)
- [Candidate label fixture](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/tests/unit/country-label-input-contract.test.mjs)
- [Candidate lifecycle fixture](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/tests/unit/territorial-editor-lifecycle.test.mjs)
- [Candidate prerequisite fixture](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/tests/unit/core-prerequisite.test.mjs)
- [Candidate startup source oracles](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/tests/unit/startup-performance-contract.test.mjs)
