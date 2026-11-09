# Independent review: five CI fixture corrections

Date: 2026-11-09.
Base: 45e64efaa706cb4085cfd4fe305b123bf5d1c793, failed run 42565978097.
Frozen candidate.patch: ef940fc59ee0c40e588310f0685a359d6cba96ababd5c0060eebd0fcfbd70e90, 7,748 bytes, five test files.

## Disposition

No blocking findings in the frozen five-file patch. Approved for the reviewed test-source correction and subsequent official verification. This is not native executable approval, a new matching Core/WASM publication result, a full selected-CI pass, or deployment approval. No further candidate change is required by this review.

The patch changes only existing tests. Production geometry, source admission, canonical storage, precision budgets, raw coordinates, compiler selection behavior, publisher guards, assets, library pin, recipes and workflow policy remain unchanged.

## Reviewed invariants

1. tools/cpp/spherical-polygon-tests.cpp:38-53 replaces the invalid inference from source-mode winding inspection with actual strict source admission. Existing rejected(source), exact positive/simple predicates, unchanged vertex set and size, clipped winding, idempotence and input preservation remain. New rejected(normalized) calls the existing source-default normalizer through the same rejecting helper at lines 19-23. A winding predicate is not an admission predicate.

   Independently exercised all 25 numeric rings from the exact native fixture header through existing official source-matched Core97 WASM: 25/25 raw source rejections, 25/25 clipped-normalized source rejections, 25/25 clipped-winding acceptances, 25/25 inputs unchanged. Eight normalized rings have source-mode winding=true, disproving the old assertion without relaxing admission. This evidence covers both the old 11 and current 14 fixtures, not only the currently failing examples.

2. tests/native/document/document-session-tests.cpp:245-248 replaces the invalid persisted drawn/license fixture with the public canonical provenance normalizer on {kind:user}. normalizeWebSourceProvenance is declared in src/data/native/include/pandoeditor/projectcodec.h:32 and used by normal web content creation. Existing includes expose the namespace/API. Stored-source decoding remains strict. The mixed archive, reversed inline geometry, exact restore/save/reopen and invalid-input assertions are retained. The helper's actual DocumentSession WASM reproduction confirms the old /source/license failure and valid canonical provenance roundtrip; it does not execute this changed C++ test or prove its compilation.

3. tests/unit/document/historical-world-territories.test.mjs:469 expects the actual exact-predicate error for the retraced collinear injected shell: INVALID_POLYGON_RING: self-intersection. The diagnostic bounds, component index, area and repeated-vertex assertions remain. Independently reproduced that error using the existing source-matched Core. This changes the expected failure classification, not acceptance.

4. tests/unit/geometry/polygon-canonical-storage.test.mjs:85-108 retains a both-current control and changes only BBB's view selection for the historical case. Actual compiler membership establishes currentSnapshot status; the current: prefix does not. Both-current overlap is intentionally bypassed. Independent real default-clipper comparison confirmed original AAA archive has two unchanged components and no target/adjustments, while the minimally mixed selection yields five components including the original exact target and ordinary island. The corrected test retains exact target vertices, canonical JSON roundtrip, no precision discard and unchanged input, and additionally requires the historical adjustment and strict-source archive rejection. No fake clipper, altered operand, tolerance or weakened fragment assertion is introduced.

5. tests/unit/geometry/gpu-mesh-country-strokes.test.mjs:22 and 165-189 corrects the moved test's root and replaces the unmounted whole-world projection with readBuiltinCountry, the canonical runtime owner. It reads index metadata and only ARG's descriptor plus its single geometry payload. Existing sliver removal, surviving-fill edge, >0.62-degree border coverage and input-preservation assertions are byte-for-byte unchanged. Independently verified the compressed payload hashes and that decoded geometry bytes equal the canonical ARG source resource, SHA-256 3042caf5d55bc6ce2776bf32214f7b82f8962a01fd8db2645e57aa7404c7282f. No new coordinate fixture, hydration requirement or whole-world generation enters the patch. The old projection remains in archive metadata but is excluded from the mounted viewer closure; its payload was not read during this review.

## Independent verification

- Verified all five manifest preimage hashes against exact base Git blobs and all five candidate hashes.
- Reconstructed every patched file in memory; all five results equal frozen candidate bytes exactly.
- git apply --cached --check --whitespace=error passed using a separate review-only index populated from the base commit. No working-tree or operational-index write.
- Three candidate JavaScript syntax checks passed.
- Focused corrected compiler/historical tests passed 2/2 through a read-only candidate overlay.
- Final ARG test passed independently 1/1 with the frozen candidate, exact production dependencies and existing official matching WASM. The read-only resolver performs no dependency materialization or source substitution.
- Reviewed helper's final entire GPU test log/result: 14/14, three suites, zero failures/skips. This is separately attributed evidence, not an independent full-file rerun.
- Operational checkout remained clean at 70bffe76dba3b060c85d6dfcfe157ab046ec5e98.

## Evidence

Paths below are relative to this ci-regression-repair directory unless stated otherwise.

- review/final-independent-checks.json: 2302cbf5b99f4d4344adc21b1182d42cbc8f48a8d559cef991e39d286d99ff2a. Frozen hashes, applicability, exact reconstruction, syntax and independent ARG result.
- review/independent-source-admission-proof.json: 2aad293a936c52cddffa4a2bb365f140c85cb31ddbc9da20341c73c1716ebfda. All 25 raw/normalized source-negative checks and exact fixture/header/Core identities.
- review/independent-arg-test.stdout.txt: 4cdd95d4a8a2da54502b4514fa9c3225a8b849d5872730b1ac5e136655024807.
- gpu-fixture-diagnosis/arg-provenance.json: b6686c8dbfdb7b2d39c2f08240130f0dc631f9b3cc1ff51f3aad8e300eb3c558.
- gpu-fixture-diagnosis/arg-metrics.json: 00da16bc0e4533d873099dbe3c786189d6598d0c186b2f042a80299b624c8f3e. Two payloads, 8 polygons/4,674 points, 2 removed triangles, 21,124 survivors, 4,666 outline segments, border coverage 0.6289529999999957.
- gpu-fixture-diagnosis/final-gpu-test-result.json: e3db4a9b317b91931daa7ba9b94299b15d1c259eb970c0ec23ad630551a1e646, helper's full-file 14/14 result.
- Under current-clipped-contract-candidate/store-contract-extension/ci42565978097-independent-compiler-review: actual-archive-comparison.json SHA-256 347c164340d41f160f2308beed19b790d9ce953fbd0048e466641799b1c0721a and independent-compiler-fixture-diagnosis.md SHA-256 23f87039e302f6fd4be9c196686cfec74b0fe07eb4aefd63899d9dbad2af16d2.

## Remaining gate

The changed native test sources affect the native source fingerprint. Their executable compilation/execution and the source-matched final WASM pair still require the official route and selected CI. Existing Core97 observations cannot substitute for that gate. No native build, SDK/package installation, network action, CI dispatch, full catalog generation, source/candidate modification, staging, commit or push was performed by this reviewer. Only review-local reports, loaders, logs and a temporary read-only-check index were written.
