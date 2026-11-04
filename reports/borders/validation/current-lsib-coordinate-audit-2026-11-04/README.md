# Current LSIB coordinate audit — 2026-11-04

Read-only snapshot audit preceding the separately authorized Korean rollback. Monaco is explicitly excluded and is not classified as untouched original LSIB detail. Source-ID text was not used as coordinate evidence.

At each immutable pin, public observation 0388abf78dff4ea4835e36b01de67d10703ac596 and then-work/gis 89bff9a4c9ed42a7bca5325a3449fbe8055012e8, inspected 257/257 active non-water native objects and 253/253 current compiled countries after Monaco exclusion. Unexamined: zero. The complete 1,020 model instances reduce to 264 unique geometries. 258 native vs 254 compiled (before exclusion) reflects SCR merged into CHN, BRI into BRA, BJN/SER into COL; no native-only current country was omitted. Date: 2026-11-04.

Strict numerical XY equality, direction-normalized consecutive segments and ordered retained subsequences were compared against the preserved LSIB 11.4 source (395 features; one Monaco-pair feature excluded; 4,316,092 reference vertices). At least three ordered anchors are required; point contacts/two-point edges do not count. A separate six-decimal comparison does not conflate rounding with exact numeric identity. Re-run using the final helper also covers ordered original anchors separated by inserted target points. No additional retained subsequences or rounded-only chains were found outside the following exact chains:

| Boundary | Countries / current source phase | LSIB feature | Original vertices retained | Geodesic length |
| --- | --- | --- | ---: | ---: |
| Korean mainland MDL | KOR armistice-1953 / PRK sino-korean-protocol-1964 | 121eb8f6-5a86-46be-beb2-451c9a558382 | 4,448 of 4,448 | 243.386338 km |
| Paektu | CHN / PRK sino-korean-protocol-1964 | 8ea0154a-8bae-42a1-abdc-af310aeca0cc | 1,953 of 19,341 feature vertices (indices 7052–9004) | 92.113601 km |

These chains occur on both counterpart polygons, in native and compiled geometry, at both pins. Source-coordinate chain hashes respectively: 9cd96dacd66fe0b3d68c35d795097f7c2f1f9e338d250328f6285478a963bc8d and bb7c953206dca68916dd8b62a553e90f5a8a32d08bd35f9b4da2aaa7843dace7. Duplicate counterpart/pin instances are not additional border segments. Contact-only matches are separately retained in the result JSON. No other current country, including Vatican, contributes an original-detail chain under these definitions.

The public pin's native CHN object contained the later G input, while its selected compiled runtime used the earlier CHN version; the work pin had retired G. This is a native/compiled difference, not a claim that G was displayed or newly published. Seventeen missing native object paths per pin were read through the existing paired chunk's canonical compact-JSON/newline serialization only when its SHA256 exactly matched the requested native object ID. No repaired object was written. The per-model readBasis records this evidence.

The direct Korean insertion was introduced by app b39f1a362787d21ff4cddff392ae7e716e783170, 2026-10-21 03:09:43 UTC, in tools/build-korean-boundaries.mjs. Existing LSIB targeted supplementation elsewhere often preserved only selected generalized positions; isolated retained vertices do not mean raw original detail. Numeric coordinate correspondence is not legal-boundary verification or proof of source exclusivity. Runtime here means selected compiled geographic inputs, before GPU Float32/mesh handling; preview geometry is a different layer.

The archive includes exact pinned model identities, coordinate indices/hashes, chain coordinates, coverage and reproduction script. Copy the script to the existing build-native/territorial-recipe directory and run from app work/gis; it only reads the two immutable pins and writes its task-local JSON. Original LSIB master SHA256: de87a3d317b7c18c07a8d16d1299778aaa19fd43a8d7b06a1217ac397cbd4194.

## Subsequent authorized change

The two direct Korean insertions were subsequently rolled back at work/gis app 9f9058f79997be56e0a72f47078d935f9e438363 / data 30ce140bdd55b45cbe40d75346719a4b140e1342. That separate scoped verification found no remaining original or retained LSIB chains in the six affected source versions and three current compiled geometries. See reports/borders/validation/korean-lsib-baseline-rollback-2026-11-04. The two earlier snapshot audits above remain historical evidence and are not relabelled as the current post-rollback state. No fresh public deployment is claimed.
