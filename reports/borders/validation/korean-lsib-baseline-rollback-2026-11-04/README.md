# Korean direct-LSIB display rollback — 2026-11-04

Completed scope: remove the direct LSIB replacement only from Paektu and the Korean mainland MDL, retaining Monaco exactly. This is a return to a cartographic Natural Earth baseline, not a surveyed treaty reconstruction or removal of Korean historical events.

App work/gis: 9f9058f79997be56e0a72f47078d935f9e438363. Runtime data: 30ce140bdd55b45cbe40d75346719a4b140e1342; remote data HEAD verified. Both source/native objects and paired runtime outputs are stored. No app main integration or deployment occurred.

## Baseline and affected versions

The app introducing the direct copy was b39f1a362787d21ff4cddff392ae7e716e783170; its parent is 317290e44b10d89e713c275b7444ebf281e0542e. Corresponding data parent: 83f64681f0fe90d965d74ec817c3615ceada1ffc. The still-preserved NE 5.1.1 semantic JSON SHA256, 985c34f55ace12be51580f420c6b691d03f48bf73c84a88aed65b7ae6cfc5d01, matches the original introduction provenance. The original LSIB extraction and global LSIB master remain unchanged in data history/current sources.

- Paektu: restore one identical 24-vertex NE arc to CHN and all three PRK phases (1948, 1953, 1964). The replaced display chain contained 1,953 consecutive original LSIB vertices plus two NE anchors (1,955 total).
- Mainland MDL: restore one identical 44-vertex NE arc to KOR 1953 and PRK 1953/1964. The replaced chain had 4,448 original LSIB vertices plus two NE anchors (4,450 total). Preserve the existing Han-estuary/island allocation.
- KOR 1948 geometry remains byte-identical. All six target version IDs, version dates, identity/lifetime data, names, parent/property intervals and source-binding intervals remain unchanged. Existing opaque CHN version ID is retained; provenance explicitly identifies the restored baseline and retired LSIB source.

Only five geometry versions changed, across three source/native objects and three compiled countries. Five new prepared packets were emitted. All other compiled country descriptors were reused; Monaco and France source/chunk bytes, native IDs and compiled descriptors are exactly unchanged. No country-wide CHN reset occurred. Earlier A–C/G/Sarakhs retirement, Crimea and Baikonur remain protected.

## Verification

- Existing OGR/GEOS: all six target versions valid; exact inverse patch recovers each original coordinate serialization. Same restored chain on both sides. On 1948-09-09, 1953-07-26, 1953-07-27, 1964-03-19, 1964-03-20 and 2026-11-04, three-country union symmetric difference is zero and each adjacent-country overlap is zero. These are technical square-degree checks, not legal accuracy or an event area.
- After canonical storage and preparation: all three native object SHA256 values verified against Git bytes; native objects equal source and decoded chunks. All 14 scoped output hashes verified. Actual three-country runtime selection uses the new compiled geometry references.
- Six source versions and three current compiled geometries contain zero original LSIB consecutive/subsequence chains under the scoped exact-coordinate check.
- Fourteen focused Korean/LSIB tests pass, preserving government establishment dates, 1953 attribution transition, 1964 evidence phase, Baengnyeong island, shared-line checks and idempotence. Five prior sub-500 retirement regressions pass. Synthetic pinned-byte/unclassified-version rejection passes. Changed-file ESLint and generator --check pass. Updated fixture receipts cover only the three changed sources/current geometry references; other receipts are retained. No full suite or world regeneration ran.

The active dated runtime is the per-country builtin-world loader, with source/native and prepared-polygon counterparts. Archived legacy whole-world aggregates were not regenerated; no claim is made that every historic export edition changed. Reproduction: prepare the pinned data, then run node --import ./tools/load-spherical-core.mjs tools/build-korean-boundaries.mjs --check and the three affected test files named above. The attached proof files retain exact version/hash/chain data and scoped geometry QA.

## Storage and remaining work

A temporary shared-library lock caused EEXIST at the canonical global lock path before storage; the lock was neither removed nor bypassed. After normal release, the same selected storage succeeded and its remote revision was verified. No outstanding permission blocker remains for this rollback.

This completes this specific rollback. The broader historical-change inventory and future detail-review gate remain separate unfinished work; this report does not claim global historical simplification completion.
