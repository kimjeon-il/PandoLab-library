# Caspian territorial delta and paired Iranian boundary correction

2026-10-28. Original calculation bases (not publication parents). Application base: c55fc510e109c682be3b7af91ae1316dde22e9d1. Data base: c22c85ce9fbff291f8886d8e226b9853a7b821db.

## Applied scope

Four canonical territorial sources: Iran, USSR, Russian SFSR, Transcaucasian SFSR. The historical Caspian water version remains unchanged. Its 1922-01-01 through 1929-12-31 interval is intersected with existing country geometry coverage; no new republic coverage is inferred. Expanded water is removed from actual country geometry. All 107 components of modern-water minus historical-water are added to shore owners: 77 Russian SFSR, 11 Transcaucasian SFSR, 19 Iran. Parent USSR receives the two republic allocations.

Seven eastern delta fragments use existing modern Turkmenistan/later-USSR coastal geography as a limited ownership assumption. Six touch those existing coastal/island geometries; one has an approximately 20 m simplification mismatch. This is not independent verification of historical sovereignty. The already-missing original island bodies in the reviewed 1922 source are NOT restored by this delta-only change.

Iran's Atrek and Sarakhs overlaps are removed only during the approved 1922-12-30 through 1925-05-12 boundary interval, using the already-approved USSR line. Existing endpoint gaps, four eastern research holds, Afghan geometry and unrelated borders are unchanged.

## Reproducible transformation

The source operation is (original territory union assigned exposed land) minus historical water, with the two bounded Iranian overlap masks additionally subtracted in their reviewed interval. Existing versions are split at effective-date boundaries; original outside-period geometry is retained exactly. The implementation and synthetic regression tests are `tools/gis/caspian-territory-delta.mjs` and `tests/unit/caspian-territory-delta.test.mjs`.

Compiled objects are updated from the canonical source delta: C' = (C minus (S minus S')) union (S' minus S). This preserves existing compiled exclusions and the previously approved western Iran/Türkiye correction. The generic partial generator's transitive component plan reached approximately 170 countries and was NOT run. Only four compiled country payloads were regenerated; all unrelated chunks remain stored opaque bytes. Version metadata, source bindings, content-addressed geometry refs, chunk hashes, transport offsets, library index and native objects are synchronized.

The existing compiled-only western adjustment remains a pre-existing full-regeneration limitation. This patch does not perform a broad compiler/source migration.

## Verification

- Five focused geometry/temporal/source-delta tests: observed expected failures before implementation, then passed.
- Four source schemas and 19 effective-date cases: valid raw polygon topology; exact unchanged geometry outside the correction interval; no historical-water overlap; no new republic time coverage.
- Reviewed parent/constituent shoreline agreement, two bounded overlaps removed, approved non-water boundary points retained.
- Independent review accepted the final candidates: 25 compiled bindings, all raw-valid; water exclusion and all assigned additions retained; maximum out-of-scope symmetric difference 5.48e-16 degree²; updated metadata version resolution, chunk hashes and transport offsets verified. No Critical or Important findings remain.

No renderer change, whole-world regeneration, main integration, deployment or portable package is included. Browser visual validation has not been performed in this task.

## Publication state

Publication-status correction, 2026-10-29: the earlier approval-pending statement is superseded by verified repository commits, not by a new geometry validation.

- Data published on work/gis at [65fbc692f47f7936a804e7af0eed546966898828](https://github.com/kimjeon-il/PandoLab-library-data/commit/65fbc692f47f7936a804e7af0eed546966898828), commit timestamp 2026-10-28 13:33:13 UTC; actual publication parent: d4c65479847d12f810f96b2162698dbc96d25ed7.
- Application paired at [22d0b24eb5916f9597f4b0c6ae4625236a6722d9](https://github.com/kimjeon-il/Pando/commit/22d0b24eb5916f9597f4b0c6ae4625236a6722d9), commit timestamp 2026-10-28 13:33:55 UTC; actual publication parent: 69ee27763b75c7aca6ede227a21d1ccb090c0be7. Its config/library-data.json pins the data commit above.

These publication parents differ from the original calculation bases recorded at the top. This correction does not reapply the geometry, revise historical ownership assumptions or claim deployment, main integration, browser validation or new test execution. Later work/gis changes remain preserved.
