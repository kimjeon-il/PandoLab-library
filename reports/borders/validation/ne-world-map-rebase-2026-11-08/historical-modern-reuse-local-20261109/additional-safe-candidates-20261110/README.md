# Kolguyev: complete modern island-group candidate

Status: **prepared, not applied; parent review required**. Local evidence and source patch were read back. No source writer, commit, remote Git operation, runtime generation, build or package command was run.

Base library revision: `7a307819c680fdb221d19cf18d49e12daebefdfa`. The original residual inventory at `f155202698569771dde7af626342ade4801b6364` is only a locator. All selected source versions were reread from immutable current local archive bytes using `decodeArchiveEntry(fetch:false)` and are unchanged since that inventory.

## Recommended next scope

Replace the complete five-component historical Kolguyev group with **all 18** exact approved RUS donor polygons, including all rings. Do not replace only the main island and do not apply any area, visibility or exact-NE-correspondence cutoff.

- RSFSR `state:soviet-union-russian-sfsr:1922-12-30-reviewed-v2`, 1922-12-30 through 1925-05-12: old polygon indices `[47,51,54,55,56]`; 218 becomes 231 polygons.
- USSR `state:soviet-union:1922-12-30-reviewed-v2`, same dates: old `[48,52,58,59,60]`; 222 becomes 235.
- USSR `state:soviet-union:1922-1991-baikonur-r1-after-reviewed-day:caspian-1925-05-13`, 1925-05-13 through 1929-12-31: old `[64,68,74,76,77]`; 286 becomes 299.

Approved donor: `state:RUS:natural-earth-5.1.1`, geometry SHA-256 `1be9c12b314121b9f55697886f4d0b84a9dd9d72d0f213a826a5c45797b75297`. Fresh source equals the archived `display-review-final-authorized-candidate.geojson` RUS feature exactly.

All donor indices: `[738,739,740,741,742,744,794,795,796,797,804,806,807,808,809,810,811,812]`.

The full source-bound ledger is `candidate-ledger.json`. The five old polygons are identical in all three versions and also equal the original approved 1922 master/display groups for parent and constituent. The 1991 RSFSR already contains the same donor arrays. The 1930-1991 USSR already contains the complete same 18-component geometry, with normalized/reordered coordinates; its symmetric difference is zero. Those versions are not changed.

## Independent historical basis and limits

`historical-membership-evidence.json` records the State Archive of Arkhangelsk Oblast's published administrative history and its primary archival/law references. Dated 1920, 1922, 1924, 1927 and 1929 records explicitly support Kolguyev's continuing RSFSR/USSR administration. Dartmouth's 1950 Arctic sovereignty study independently distinguishes Kolguyev's established Russian membership from disputed/new Arctic claims.

The geographic window is only a whole-component enumeration aid. It neither assigns sovereignty nor clips geometry. All donor components intersecting that water-separated window are fully contained and retained. Original tiny-Arctic-island title caveats remain. This is modern physical-coast reuse for the documented island group, not certification of surveyed 1922 coast positions or a new legal title decision.

Franz Josef Land/Victoria, Wrangel, Sakhalin/Kurils, Caspian/Aral changes, mainland borders and every unselected polygon remain untouched. Original dates, source IDs, certainty and provenance are preserved. Old notes are retained with a scoped factual addendum; superseded display-review receipts remain in source-provenance evidence.

## Prepared deliverable and checks

- `canonical-paired-source-patch.json`: two entity patches and three replacement versions, source preimage hashes, appended source attributions, expected normalized entity/descriptor/version/geometry hashes.
- `source-gate-proof.json`: three historical source gates passed; codec roundtrip passed; unselected versions and inherited provenance preserved.
- `topology-proof.json`: all three full candidates valid; exact retained-coordinate and complete-donor replay; zero area overlap and no touch with retained geometry; exact candidate union; identical scoped parent/constituent group.
- `projection-evidence.json` and opened `kolguyev-source-scale.png`: executed LAEA projection and nominal 1:10M at 300 dpi visual review. Old/new display symmetric difference is about 504.362 km², not a measured historical territorial change.
- `patch-readback.json`: local artifact sizes and hashes; source not written.

Before applying, reread HEAD and the two target descriptors. If HEAD changes, do not blindly reuse base-revision assertions. Confirm the selected sources and approved donor remain exact, then rebase the candidate receipts as needed. Apply parent and constituent as one serialized batch. This review does not approve runtime compilation or publication.

## Held alternatives

Vaygach has 51 complete modern donor components. Donor component 1554 intersects the untouched old mainland by `0.00004211944222205031` square degrees. Do not omit it. Hold for a linked mainland/contact review; all indices and the conflict extent are in `held-candidates.json`.

Novaya Zemlya has documentary membership support, but a complete donor-group/nonintersection ledger was not prepared. Do not substitute only its two large islands. Prussia and all excluded task scopes were not modified.

## Retention and publication

Retained files are the active review/application deliverable, reproducer scripts, component ledger, proofs and unique membership research. No disposable source-input copies or expanded original ZIP were written. Remote report archival is **not performed** because the inherited remote Git denial is respected; no remote completion is claimed.

## Serialized writer prepared after parent review

Parent approved the exact Kolguyev candidate scope but has not released its writer slot. Iran is first, Sudan second, Kolguyev third. The following scripts were only syntax-checked, not executed:

1. `node apply-source.mjs --apply`: latest archive HEAD must equal the main checkout runtime pin. Rereads both source descriptors, all three selected preimages and the RUS donor. Uses canonical `withLibraryWrite`/`writeTerritorialSource` for exactly two descriptors and three new immutable geometries. Refuses changed preimages, mismatched pins, incomplete views and existing application journals. Keeps partial/uncertain outcomes for inspection without retry or rollback.
2. `node store-source.mjs --store`: requires completed source readback and unchanged application base. Runs existing `D:/dev/PandoLab/tools/data/library-data.mjs --store` with only the five exact prefixes. No push or expected-remote option. A process-only `protocol.allow=never` guard prohibits accidental Git transport, including lazy fetch; repository/network settings are not modified.
3. `verify-archive.mjs --verify` runs after a successful local store. It verifies parent commit, exact five-path logical diff, both archive/live sources, three source gates, codec roundtrips, all 18 donor components, retained coordinates and inherited provenance. Checks that only the main checkout's revision pin advanced and the GIS runtime pin remained untouched.

Writer root is explicitly `D:/dev/PandoLab`, as confirmed by the parent. External library source ownership is unchanged. No application code/main commit is created. The report working directory remains `.edits/gis`; later report-only storage is a separate GIS-owner step and is not part of these source scripts.

Execution must wait for the parent's separate writer-slot release. Changed archive HEAD from Iran/Sudan is acceptable only when the exact Kolguyev target preimages and approved donor remain identical. The fresh application base is recorded separately from the original review revision, preserving the evidence chain without claiming the review was performed later.

## Applied and independently archive-verified, 2026-11-10

This section supersedes the preparation-only status above. The parent released the serialized writer slot after Iran and Sudan completed. Latest archive HEAD and main checkout pin were both e889e5acceb96f8d7180707f1d2d0a2078393d78; the reviewed two-entity preimages and approved donor were unchanged. Canonical source application and exact five-prefix local store produced 7c9425bfbf5ab7326b806505183bffdda0cd6677. All three historical source gates, codec roundtrips, archive/live readbacks, and exact all-18 donor inclusion checks passed. Unselected versions, retained coordinates, dates, inherited provenance, and all existing archived report content remain unchanged. No other logical path changed. Main runtime pin advanced through the canonical store; GIS runtime pin and app code HEAD were untouched.

See `local-archive-commit.json` for archived entity/version checks and `completion-readback.json` for exact source-path SHA-256 values, preserved-report metadata proof, evidence readback hashes, and writer release. This was source-only local preservation: no fetch, push, build, deployment, or report archive store. Vaygach remains held and unchanged.
