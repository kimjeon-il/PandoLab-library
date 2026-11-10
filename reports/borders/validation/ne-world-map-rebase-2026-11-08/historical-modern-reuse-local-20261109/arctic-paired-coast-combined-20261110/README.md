# Combined Arctic coastal source preparation

Status: **prepared and independently read back; source not written**. Parent review and a separate serialized writer release are required. No source writer, store, commit, fetch, push, runtime generation, build or deployment was run for this combined scope.

## Exact scope

Two existing entities, three existing versions:

- RSFSR reviewed 1922-12-30 through 1925-05-12: 231→1033 polygons.
- USSR reviewed the same dates: 235→1037 polygons.
- USSR Caspian 1925-05-13 through 1929-12-31: 299→1101 polygons.

All six old Novaya Zemlya components become all 757 approved modern components. The old Vaygach component becomes the complete 51-component initial window plus linked-shore island1562, **52 total**, together with the matching Yugorsky mainland coast arc. The two donor groups are disjoint: **809 whole components**, no omissions. Donor1552/1554 retain their original point contact; neither is attached to modern mainland. No physical isthmus or individual islet name is newly inferred.

Only the exact 42-coordinate historical mainland arc is replaced, using two actual old/modern coast intersections and all 75 intervening donor vertices. Endpoint segments are split at the intersections. No old-land clipping, arbitrary bridge, simplification, rounding or component size filter is used. The old arc occurs exactly in reversed orientation in the original approved 1922 master/display.

All18 Kolguyev donor components and every other original polygon/ring remain exact. The previous Kolguyev historical-membership report and source reference remain unchanged. A new nested clarification reference explicitly distinguishes the 1920/1922 provincial drafts from the June1924 final VTsIK approval. This wording clarification changes neither geometry nor political membership/date.

## Composition and verification

The fixed assembly rule is original retained polygon order, then all809 donor components sorted by original donor index. Independent Nova→Vay and Vay→Nova operations produce byte-identical geometry under that explicit rule. Merely appending in raw operation order is not claimed byte-identical.

Three full candidates are valid, with no donor/retained land contact or overlap, and candidate union equals retained geometry plus the full donor group. Within-donor point contacts are retained exactly. Source gate count3, full codec roundtrips for both entities, all3 replacement version hashes, unchanged nonselected versions and inherited provenance have passed.

Review base is 2af6c0834ac2987a7ffdfe3cde0db1827b04d4e1. The latest 44fcddf4140cf49b72238da86575a95de9ef2876 archive and main pin were checked: RUS, USSR and RSFSR whole source preimages are unchanged. No historical dates, certainty, source identifiers, Arctic claims, Sakhalin/Kuril interpretation, Caspian/Aral changes or nonselected version changed. No new RSFSR version is invented for the1925–1929 gap. Full dated-counterpart closure is not asserted.

## Review files

- canonical-paired-source-patch.json: the single paired2-entity/3-version patch. Do not apply separate standalone Nova/Vay replacements.
- preparation-readback.json: latest full-source preimages, expected version/entity/descriptor hashes and exact5 planned source paths.
- source-gate-proof.json: gate and codec results.
- combined-operation-ledger.json: all809 donor hashes, old groups, changed arc offsets, both-order replay and Kolguyev preservation.
- geometry-proof.json: full candidate validity, no new overlap/contact, union proof.
- temporal-review.json: exact unchanged intervals and existing version coverage.
- source-provenance.json and comparison-scope.json: input lineage, preserved old review/notes, scope and evidence receipts.
- visual-review.json, projection-evidence.json, combined-source-scale.png: actual opened three-panel comparison, same executed LAEA projection and nominal1:10M/300dpi.

Supporting sibling folders are novaya-zemlya-candidate-20261110, vaygach-mainland-contact-review-20261110, and kolguyev-provenance-clarification-20261110. Their saved manifests and the combined manifest form the local review bundle.

## Limits and next step

Named-group/regional state membership is documented independently. Tiny-islet historic title, glacier fronts and coast positions are not newly surveyed or adjudicated; inherited limitations remain. The approved modern composite is copied exactly, not newly licensed as unrestricted or represented as a wholly revalidated raw upstream GPKG. The comparison establishes nominal display detail and preservation, not uniform positional accuracy.

After parent review, reread current HEAD/pin and entire target preimages before any canonical write. If another source edit changes these entities, reconstruct from current entities and replay operations instead of overwriting it with this old full-version bundle. Only two descriptors and three new geometry resources belong to the eventual source store. Report-only storage is separate and must not alter runtime pins.
