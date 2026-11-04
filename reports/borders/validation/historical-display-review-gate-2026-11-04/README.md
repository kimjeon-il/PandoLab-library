# Historical display review gate

Report ID: GEO-HISTORICAL-DISPLAY-GATE-20261104. Status: completed for gate, metadata inventory and scoped coordinate-audit regressions only. Runtime geometry: not changed by this scope. Date: 2026-11-04.

App work/gis: 3b3339df9c8db7b89210510d1e157b893697ee91. Runtime data pin: a548d5fa6612a97f998b7bdb326a27eb8b8d9717. No app main integration or deployment. Main was merged into work/gis at 014e94532; changes from concurrent data a548d5fa were preserved.

## Scope and behavior

The source update writer, recipe writer, builtin publication and library storage share a pure per-version review validator. New or coordinate-changed dated historical versions require an input-bound receipt. Existing geometry reused unchanged and metadata-only writes remain readable and writable. Whole territorial scope and builtin-only storage do not bypass the gate. The receipt binds identity/date, canonical prepared-polygon coordinate digest, preserved master/source hashes, comparison arc/reference/projection execution evidence and nominal 1:10M scale, actual method/parameters, counterpart versions, anchors and visual/topology evidence. Compiled derivatives use the existing source provenance receipt, explicitly covering each changed compiled geometry and interval.

This is a schema-checked evidence receipt, not an automatic independent proof of historical accuracy, topology, authentic source bytes or visual review. Declaring passed still requires performing the referenced checks. Geometry changes invalidate earlier receipts. The validator does not force whole-catalog validation or alter approved source ZIP hashes.

## Verification

Focused tests and ESLint were run only for the changed gate, authoring, publication, inventory, measurement and coordinate-audit behavior. See final-tests.log. Review found and reproduced two storage failures: equivalent JSON object key order was rejected; a wrong builtin source input identity could skip validation when the source was unchanged. Both now have behavioral regressions. Object contents use Node deep semantic equality, retaining exact coordinate-array order. Input receipts are checked before unchanged-source early return.

Two ring-seam cases were reproduced: a consecutive original chain across the closing seam and an ordered retained subsequence interrupted by an inserted nonmatching pivot. Cyclic runs now preserve both, across all tested rotations and reversals. Existing real contact candidates were rechecked on only the two unique original Korean geometries (three historical versions) and three relevant LSIB features. Each still has one matched vertex per feature and no new retained-original chain. No world audit or rebuild was rerun.

## Metadata coverage and remaining work

The full active compiled metadata inventory covers 286 source entities, 313 source versions, 278 compiled country references, 337 historical/current source bindings and 308 unique geometry references. Unmapped bindings and native-only entities are zero. The inventory distinguishes 228 modern baselines, 4 separate hydro records, 28 period/local adjustments, 37 modern-derived constructions, 4 merged contributors, 7 historical-linework review records, 2 unapplied source candidates, 2 straight partitions and 1 excluded Monaco record. These classifications are inventory coverage, not detailed geometry approval.

Applied historical detail review and candidate generalization remain a separate ongoing task. In particular this scope does not declare all USSR composites, river/uncertain European segments, Central Asia or the Darja coast completed, and it does not publish the staged eastern 151-point candidate. East/West Prussia remain user-confirmed incomplete and held for the later task. Monaco and all prior rollback/retirement data remain unchanged.

## Reproduction

Use node tools/gis/historical-detail-inventory.mjs OUTPUT.json for metadata only, and node tools/gis/historical-display-review.mjs --before BEFORE.json --candidate CANDIDATE.json for a selected change. See tools/historical-library/README.md for receipt requirements. Tests use synthetic inputs; real coordinate recheck evidence is bounded as above.
