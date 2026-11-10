# Novaya Zemlya complete-group candidate, 2026-11-10

## Result and scope

Candidate supported for the three selected source versions, not applied. All reads are pinned to library revision `2af6c0834ac2987a7ffdfe3cde0db1827b04d4e1` and use local immutable archive bytes with `fetch:false`. No source, configuration, runtime pin, commit, push, package or build was changed or produced. These are local research artifacts; remote report publication was not attempted under the task's no-remote instruction.

Replace all **6** old Novaya Zemlya components with all **757** whole approved modern donor components, including every ring and coordinate. The 757 components contain 14,024 vertices. No size filter, clipping, snapping, rounding, resimplification or two-large-islands-only substitution is used. Membership comes from documentary attribution of the named archipelago, not from geometry proximity or equality.

Donor: `state:RUS:natural-earth-5.1.1`; full geometry digest `1be9c12b314121b9f55697886f4d0b84a9dd9d72d0f213a826a5c45797b75297`. Its entire geometry is exactly equal to the pinned approved-original RUS feature. Complete group digest: `49b3a7259dbdaf99fac100e3717999c2530f472a9988800b3addfff1108127fb`.

The complete donor indices form these inclusive ranges: **813–987, 1016–1248, 1308–1479, 1623–1754, 1979–2023**. `candidate-ledger.json` records every component's exact index, coordinate-array digest, ring digests, bounds and vertex count.

## Targets and reconstruction

- RSFSR `state:soviet-union-russian-sfsr:1922-12-30-reviewed-v2`, 1922-12-30 through 1925-05-12: remove indices 61, 62, 70, 77, 97, 99. Polygon count 231 → 982. Candidate geometry digest `befefd5fc72251a257f377ff849a34e1f6359751013147e1a7581c7bdef47d84`.
- USSR `state:soviet-union:1922-12-30-reviewed-v2`, 1922-12-30 through 1925-05-12: remove 65, 66, 74, 81, 101, 103. Count 235 → 986. Digest `8ae323f7c6adb38e849295b59f6f1594b22d7f878952b13e045256a4aa2697b4`.
- USSR `state:soviet-union:1922-1991-baikonur-r1-after-reviewed-day:caspian-1925-05-13`, 1925-05-13 through 1929-12-31: remove 84, 86, 90, 97, 130, 140. Count 299 → 1050. Digest `55e587ec4e02481f3fba4c93e6e2f41e75c0bff9a358594a6b296b02b604a640`.

Replay leaves the unselected polygons in their original order and appends the 757 donor polygons in donor order. All three old groups are exactly identical. Source-descriptor, normalized-entity, version, metadata and geometry preimages are in the ledger. Never replay these indices against another revision without checking the preimages.

## Actual checks

- All three complete candidates and the modern island group are Shapely-valid. Donor/retained intersection is **empty**, including zero-dimensional contacts; area is exactly 0 square degrees. No retained polygon intersects the replacement group. Minimum donor-to-retained separation is 0.917657948004287 coordinate degrees, used only as a separation diagnostic, not as an accuracy or selection threshold.
- All unselected complete polygons and all donor coordinate arrays/rings are byte-exact in JSON. All eighteen modern Kolguyev polygons occur once before and once afterward. All other inherited historical exceptions remain in untouched components.
- The retrieval perimeter lies entirely in water relative to all modern RUS and each selected historical target. No polygon crosses it or touches it. Modern minimum perimeter clearance is 0.19486000000006243 coordinate degrees. The selected group bounds are [51.43276590000005, 70.44486000000006, 69.08941930000003, 77.04674150000005].
- The overview overlay and nominal 1:10M, 300 dpi three-panel comparison use common Lambert azimuthal equal-area projection/extent within each image. Both images were opened. Visual inspection confirms the complete North/South island chain and accompanying islands, separated from Vaigach, mainland/Yamal and other groups. The nominal comparison includes the actual pinned raw Natural Earth RUS reference. Neither view is physical-screen calibrated or a historical positional measurement.
- Original 1922 master/display zip SHA-256 is `53d5889738d995e76c0f8da7f00fcc36fdb0baaa98f471bfdad41384061ceb8a`. All six old component occupied geometries equal the original USSR and RSFSR master/display groups exactly: Hausdorff and symmetric-difference area both 0. Their serialized coordinate arrays are **not** byte-identical because of earlier ring rotation/orientation and normalization; one South Island vertex differs in redundancy. Failed stricter serialization comparisons are retained in `geometry-evidence.json`, rather than reported as passes. No source was modified to obtain this result.

## Historical meaning and cautions

`historical-membership-evidence.json` links independently read historical sources and separates administrative evidence from modern geographic scope. Established pre-1916 Russian title and 1920, 1922, 1924, 1927 and 1929 administration support group-level membership across both selected intervals. The **25 March 1922 provincial draft was not final VTsIK approval**. A consolidated 1959 statute text includes a **1933 revision**, so it is not silently treated as an unamended 1929 original.

This updates an already-modern physical-coast approximation. It does not establish period-exact glacier fronts, each small modern fragment's historical existence or every tiny Arctic island's title. The original macro-baseline limitation and mixed historical-source rights remain. Franz Josef Land/Victoria, Wrangel, Sakhalin/Kurils, mainland historical borders, coverage dates and metadata are untouched. The paired 1922 parent/constituent group is identical; no complete later RSFSR period closure or worldwide topology certification is claimed.

## Artifacts and reproduction

Run `node <this-directory>/research-candidate.mjs` from the existing Pando GIS worktree. It reads archives in memory, invokes the scoped Python script and writes only these research artifacts. It does not materialize duplicate full source files. The current Python executable and dependencies are reused.

- `candidate-ledger.json`: exact operation preimages, all 757 new and all 18 old target component entries, candidate hashes and preservation checks.
- `geometry-evidence.json`: actual selection, topology, original-master comparisons and visual metadata.
- `historical-membership-evidence.json`: sources, dated assessment and retained limitations.
- `archive-inputs.json`: 12 verified archive reads with paths, immutable revision and byte digests.
- `whole-group-overlay.png`: inspected matched-projection overview.
- `nominal-source-scale.png`, `projection-evidence.json`, `visual-review.json`: inspected nominal 1:10M comparison and factual review record.
- `topology-proof.json`: three-candidate scoped preservation proof, including actual retained-union equality.
- `whole-group-operation.json`, `replay-novaya-zemlya.mjs`, `operation-replay-proof.json`: stable operation and executable in-memory replay for parent-owned combined preparation.
- Small scripts: executable reproducibility evidence and handoff preparation for this candidate.

All retained files have an immediate review/replay consumer. No disposable source copies, downloads or build outputs were created. These local candidate files are not a historical-display approval receipt, source application, runtime approval or remote archival confirmation.

## Combined handoff decision

The parent chose a combined Novaya Zemlya + Vaygach/mainland + Kolguyev clarification patch. No standalone source patch was generated and no source gate/codec pass is claimed here. `build-source-patch.mjs` is an **unexecuted, explicitly disabled scaffold** retained only to supply structured-provenance preparation patterns to the parent. It cannot run as a standalone writer or overwrite later work.

The Novaya 757 donor indices and the Vaygach 52 indices are independently confirmed disjoint: **809 distinct indices**, intersection empty. The Vaygach operation read had SHA-256 `ddf26ebf37eddaef7f2b161cfd00c03e4449884f541ea8027a7aa7cc3bc09ad1`. This checks index disjointness only, not combined geometry validity.

The replay module exports `removeLegacyGroup`, `replayNovayaZemlya`, `donorIndices`, `donorCoordinates` and the pinned `sourceRevision`. Removal matches each complete old component hash exactly once, so it remains usable after another disjoint island operation shifts numeric indices. Sequential appends can differ solely in array order: the combined author should preserve original retained order and use one fixed combined donor ordering before computing the final digest. All combined geometry, both-order replay, dates, canonical gate and codec checks belong to the parent-owned combined patch. Fresh source preimages must be checked before any later authorized write; unrelated concurrent library HEAD movement is not permission to apply stale replacements.
