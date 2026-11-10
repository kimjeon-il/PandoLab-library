# Later IRN compilation: read-only continuation plan

Status: investigation only. No source, source chunk, compiled country, generated index, current world, application code or deployment was written. No build or generator was executed. All observations below use immutable data revision 46e6d5c9451fb137717987483428c441051c19a5 and application c9ca35d32c54b1c31bef474683946baa2dc12566. Recheck those inputs before any future execution.

## Current facts, not inherited assumptions

1. The published source-only coast patch has three 1922-1929 versions. All three pre-coast geometries at 7a307819 equal the corresponding current generated source-chunk geometries. Their latest raw source geometries have changed as reviewed.
2. The generated source chunk assets/data/territorial-entities/generated/v2/state-IRN.json.gz remains SHA-256 7e37c37dd6050af65046461df8b810ebe3e5076e25d65979923928c9bb9c7b56. The builtin index inputHashes.sourceRevisions['state:IRN'] equals this hash. This is internally paired, but not the latest raw source.
3. Two other source versions, caspian-before and the unqualified natural-earth-5.1.1 version, already differed between generated source and raw source before this coast patch. Generated/compiled digest is 35a2cbe36881862786edd4d7480bfcf44a6e9a80f130828c847e55c4df70a92d; current raw geometry digest is 269f85adc99c34ddba1aa69ec47e8d5bc63384531ee266bfde4ebbc7ec8e2ac4. They are outside this operation and were not changed or newly reviewed here.
4. Current compiled IRN descriptor is assets/data/builtin-world/generated/v1/countries/IRN-sha256-fdd6227d9a9756eb5e54c34df19b2cff4a8044c13d3ccf88b05e5fc89cc7b510.json.gz. The current codec materializes only IRN and its referenced geometry assets. Exact indexed paths/hashes and five source bindings are in compiled-continuation-inspection.json.
5. Of the three selected historical bindings, only 1922-12-30..1925-05-12 currently differs between compiled and pre-coast source geometry. Compiled digest bc9b10118b8f453df7c432cc70d0b6cff1cf8a3c7ab2b5d26d5126b5ed820629 contrasts with source digest edd0f60799e29f9fd303277666fba7934edb066b70cd8ad2f73cd0ebf59a5168.
6. Crucially, that current difference is not a western Turkey patch. Actual source-minus-compiled main component bounds are [54.787281,37.61693,54.85663,37.761133], area 0.001280702229999055 square degrees, in the Atrek region. Other Caspian difference components are approximately 2e-17 square degrees and are recorded rather than silently removed. The current difference has zero intersection with the new Gulf/Oman coast delta, and the two geometries are disjoint.
7. The 2026-10-28 report says its old delta preserved a previously approved compiled-only western Iran/Turkey adjustment. That is useful historical caution, not proof of a currently surviving western-only discrepancy. No western discrepancy was found in the three selected historical source-versus-compiled bindings at the inspected revision. Its earlier origin or later incorporation has not been established here. Do not invent or reapply a stale western mask merely because that report mentions one.

## Safe geometry method for a later authorized operation

For each dated binding, define S as its verified pre-change source geometry, S' as the reviewed new source geometry, and C as the exact pinned compiled geometry. Use the existing pure helper tools/gis/caspian-territory-delta.mjs, regenerateGeometry(before, after, compiled, pc):

C' = (C minus (S minus S')) union (S' minus S).

For these three coast edits, S is the matching 7a307 source version and S' is the 46e6 source version; the corresponding generated source geometry provides an independent baseline match. Do not replace C wholesale with S'. This retains actual compiled exclusions outside the source delta, including the currently observed Atrek difference. The current exception and coast delta are disjoint, so the method is suitable in principle; no C' was generated or approved by this investigation.

Before accepting a future C':
- Independently compare C' versus C outside the exact S/S' symmetric difference, not an arbitrary broad bounding box. Require no unintended changes, allowing only explicitly quantified polygon-operation numerical residuals.
- Verify original compiled exclusion/addition geometry remains unchanged outside the source delta. Bind the evidence to actual current payload hashes, not the name 'western exception'.
- Preserve all existing Abu Musa coordinates, absent Farsi/Tunbs, complete approved donor components, Caspian/Atrek structure and source dates. Validate each compiled dated binding and its actual date-effective neighbors.
- Compare at the same 1:10M target projection and review the compiled result, not only the source image.
- When overlapping future deltas arise, preservation is no longer established by this disjointness result; resolve the exact source and compiled policy interaction before execution.

## Important entity-level pairing constraint

Do not claim IRN is fully compiled by advancing its whole-entity sourceRevision hash after applying only the three coast deltas. Two outside-period versions already contain pending source-only changes. Current bookkeeping records one source chunk hash per entity, not one hash per geometry version.

The clean publication path is to inventory and review all currently pending IRN source-versus-generated changes, including those two versions, before advancing the entity's generated chunk and compiled input hash. Preserve their original authorization, provenance, historical/modern roles and any existing exclusions. If that additional scope is not ready or authorized, keep this as a pending continuation plan and do not publish a misleading whole-entity completion. Do not create a parallel source or fake source revision to bypass this constraint.

## Current canonical owners and procedure

The old October recipe names packBuiltinWorldFiles and storeNativeLibraryObjects. Those names are not present in current tools; the recipe is historical, not a runnable command sequence. Current storage uses separate immutable descriptor/geometry assets, not the old aggregate transport. The old tests/unit/caspian-territory-delta.test.mjs path is also absent in the current checkout; do not claim it was rerun.

When execution is separately authorized and the complete IRN pending scope is resolved:

1. Freeze exact old/new raw IRN, old generated chunk/index, old compiled IRN/index, coverage report, source view and policy identities. Use local immutable archive reads. Preserve a rollback/replay receipt before any canonical write.
2. Reuse tools/gis/caspian-territory-delta.mjs for source-delta geometry. No current CLI was found that directly performs this particular reviewed delta publication; prepare a narrowly scoped orchestration around existing owners rather than pretending an old command still exists.
3. Use tools/build/build-territorial-entity-chunks.mjs --entities=state:IRN only for the reviewed complete raw entity and its paired generated/v2/index.json. This is one source chunk plus its shared metadata index, not a full catalogue geometry regeneration. Run only under the canonical scoped library write lease when authorized.
4. Materialize the pinned compiled IRN with readBuiltinCountry in tools/data/builtin-country-bytes.mjs. Preserve all identity fields, property/parent/lifetime records, unrelated geometry bindings and unselected country descriptors. Create new immutable geometry identities; never overwrite old (id,version) geometry bytes. Update matching sourceBindings, timeline geometry bindings and historicalTimeline geometry metadata coherently.
5. Generate fresh compiled review receipts for every changed dated compiled binding. assertHistoricalCompiledChanges in tools/gis/historical-display-review.mjs expects builtin entity IRN, actual sourceVersionId, actual binding dates and the compiled geometry hash. It searches displayDetailReview.compiledDerivatives. Existing source-only reviews use state:IRN and cannot automatically approve a different compiled derivative.
6. Reuse encodeBuiltinCountries(index, [updatedIRN], files) and finalizeBuiltinWorldFiles(index, files, {previousIndex}) from tools/data/builtin-country-bytes.mjs. They update immutable geometry resources, the country descriptor, country parts if needed, and readIndex while retaining unchanged references. Advance inputHashes.sourceRevisions['state:IRN'] only to the paired generated chunk that is fully represented by the reviewed compiled result; recordBuiltinWorldInputs is the existing index hash owner.
7. Keep coverage diagnostics honest: preserve unrelated entries and update any selected IRN metrics or adjustments whose geometry changed. Do not label stale coverage counts current. Do not regenerate current-world data merely for the three historical intervals. The two other pending versions may require an explicit separately reviewed current-world projection step.
8. Run the smallest actual geometry, source/chunk, compiled-binding and byte-roundtrip checks. writeBuiltinWorldPublication in tools/build/build-builtin-world.mjs calls the compiled review gate, writes payloads before index and restores changed targets on a write failure. Use this canonical writer with exact scope under the existing lease. No writer was run here.
9. Enumerate only emitted immutable assets, paired indexes, IRN source/chunk and any genuinely changed projection/coverage files for canonical --store. Its territorial pairing guard requires source, chunk and generated index together when that generated source changes. Independently read back those archive entries and confirm all unselected entries and owner refs are preserved. Network/push/deployment remains outside this plan.

## Do not run the generic full rebuild

build-builtin-world.mjs --entities=state:IRN is not guaranteed to be an IRN-only delta. buildBuiltinWorldPartialPublication constructs connected dependency components and calls compileBuiltinWorldCatalog for each whole component. That fresh reconstruction does not invoke regenerateGeometry. The October report observed approximately 170 connected countries; that old count is not certified for the current graph. Even an entity-scoped invocation can therefore be broad and can replace an old compiled-only exclusion. This investigation did not invoke it, including its plan mode. A later metadata-only --plan may reveal current scope, but scope output is not preservation proof and is not permission to execute a broad build.

## Saved read-only evidence

- compiled-continuation-inspection.json: exact source/generated/compiled identities, five dated bindings, eleven immutable IRN-related archive inputs and current owner code hashes.
- compiled-exception-footprint.json: actual existing difference components and disjointness against the reviewed southern coast delta.
- inspect-compiled-continuation.mjs and inspect-compiled-exception.py: reproducible read-only inspection scripts; they write report evidence only.
- ../caspian-territory-delta-2026-10-28-README.md and ../caspian-territory-delta-2026-10-28-recipe.json: preserved historical procedure and explicit old limitations, not current executable instructions.

No additional source or compiled writes were performed after source commit 46e6d5c.
