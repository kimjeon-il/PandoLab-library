# LOD / camera implementation progress

Owned work complete at 2026-11-10; parent integrates renderer and browser evidence. No commit/push by child.

- `render-lod.js` retains exact source coordinate identities and explicit per-ring source indices. It prepares a shared, monotone contraction hierarchy across all owners before filtering visibility. Replacement chords cannot create crossings, new contacts, winding flips, island engulfing, collapsed rings or unequal shared arcs. Holes, date-line/polar rings and small rings remain protected. Selection no longer restores whole-source detail.
- Calibrated source policy inputs use the approved max(T_ref*S_ref/S,T_min) formula. Invalid metadata/source hash rejects. No real calibration values added. Capped preparation failures propagate; numerical mesh error remains separate at existing 0.5 CSS px.
- Worker retains one combined country/physical source topology index across pans. Jobs transport source only once. `extraPhysicalFeatures` is appended to country source; `countryFeatureCount` partitions output without adding masks to country slots. Country and physical derivatives share exact edge protection.
- Worker result fields: `displayFeatures`, `displaySourceIndices`, `displayPhysicalFeatures`, `displayPhysicalSourceIndices`, `displayPhysicalPackets: [{id,packet}]`. Physical typed packets reuse the existing prepared polygon store and transfer their buffers. `physicalPreparation` carries that store's counters. `lod` includes topologyReused, topologyFeatureCount and algorithmVersion.
- Project base scale uses fixed initialMapBounds, both camera projections clamp relative zoom 1..32 with fractional values. Flat world reference fits both axes and centers [0,0]. Date refresh keeps view; resize updates base scale without changing relative zoom or center. Projection conversion keeps the center and meridional local screen scale within limits.
- MapVisualFrame fields: baseScale, relativeZoom, scalePixelsPerMeter, lodPolicyKey, lodSelectionKey, lodSelection. Optional `lodSelection` input is the shared resolved bucket; default is the common stateless screen policy.
- Temporary topology contraction graphs are released after preparation. Density-adaptive candidate grid reduced a synthetic 4,000-point coast from 1451ms to 224ms on this machine; 1,000-point sample148ms to76ms. Both kept17 vertices at cssScale1000. These are synthetic CPU measurements, not browser/world performance certification.

## Verification

Final command: `node --test tests/unit/rendering/screen-geometry-lod.test.mjs tests/unit/rendering/project-lod-worker.test.mjs tests/unit/rendering/project-lod-frame.test.mjs tests/unit/rendering/gpu-mesh-transfer.test.mjs tests/unit/map/project-relative-zoom.test.mjs tests/unit/document/project-setup.test.mjs tests/unit/map/map-input-controller.test.mjs tests/unit/rendering/map-presentation-readiness.test.mjs`.

94 passed, 0 failed. Output: `lod-camera-final-tests.log`. Targeted ESLint of all owned changed source/tests passed. No full project/GIS validation or local native build performed. Existing actual Worker test transport was corrected to resolve source-relative dynamic imports against the canonical Worker source URL; browser importScripts still uses public source transport.

Red/green logs retained in this task directory for parent evidence selection: topology, Worker/frame, camera, physical Worker/packet. Parent owns archival and temporary-output cleanup.

## Findings reported to parent for integration

1. Parent `prepareCountrySharedBoundary({features,replace:true})` originally ignored passed LOD features and reused canonical border cache. Requires effective display source + LOD dependency and no canonical baseline cache on LOD.
2. Parent capped policy needed renderer-side paint gating: Worker refusal alone does not prevent canonical fallback during startup/error/recovery. All backends need pending/previous certified same-project frame handling.
3. Reset must clear screenLodPhysical. Selection boundary revision must include LOD/source identity, not only line count. Frame policy identity must use the same selected bucket if future calibration is activated.
4. Existing compiled mesh validation rejects a valid synthetic hole at both maxEdgeDegrees8 and0.499: outer [[10,10],[10,8],[10.1,6],[10,4],[10.1,2],[10,0],[20,0],[20,10],[10,10]], hole [[12,2],[12,4],[14,4],[14,2],[12,2]], error PL-MESH-BOUNDARY at14,2 ->12,2. No weakened validation or whole-source capped fallback added. Parent must resolve or accurately report this native/mesh issue.

No LSIB input, measured T_NE/T_min, actual GPU pixels, world render time, or deployment has been verified by this child.

## Later scoped preparation optimization (final verification deferred)

Parent's actual world browser request timed out preparing approximately1m combined country/physical source points. Scoped physicalLand input inspection found548,454points in4,274polygons. Measured before hot-loop optimization: source graph1694ms, DP importance1363ms, topology28103ms, total31164ms; derive115ms. This is the physicalLand input alone, not a whole-catalog validation.

Implemented protected immutable-ring separation: protected source rings remain exact spatial obstacles using the existing packed BoundarySpatialIndex; matching mutable source nodes inherit fixed protection. Protected rings no longer allocate mutable adjacency graphs. Synthetic100,000-point protected input measured1141ms/249MiB before to119ms/28MiB after. Existing22 focused tests passed at that intermediate state.

User then directed all checks to run after implementation. Stopped the running diagnostic Node process20220 and ran no further checks. A0.05degree candidate grid experiment caused long-edge overflow scans and was reverted to0.25degrees. Final unverified changes reduce transient Set/flatMap allocations, remove contracted points from spatial postings, release obsolete source adjacency Sets, cache source unit vectors, and use scalar3D point/segment arithmetic. Topology conditions and source coordinates remain unchanged.

New optional createSharedPolygonLodIndex(features,{onProgress}) callback emits source-graph/importance/topology timings and actual topology-progress {completed,total} every4096processed candidates. stats add preparationMs/preparationPhases/graphVertexCount/immutableProtectedVertexCount. Parent wired these to finite monotone Worker progress. Added dense protected-ring structural regression; not run yet.

Final affected check plan: screen-geometry-lod.test.mjs, project-lod-worker.test.mjs, gpu-mesh-transfer.test.mjs, targeted ESLint on render-lod.js and changed tests; then parent actual world rendering phase evidence. Task-owned render-lod-before-protected.mjs retained only as baseline comparator for final preparation measurement; remove after evidence capture. No native changes were made during interrupted hole investigation.
