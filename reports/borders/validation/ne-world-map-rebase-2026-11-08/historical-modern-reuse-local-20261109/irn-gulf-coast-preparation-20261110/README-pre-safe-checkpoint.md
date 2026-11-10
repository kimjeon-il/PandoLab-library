# IRN 1922–1929 Gulf/Oman coast preparation

Status: **Local candidates prepared and checked; no territorial source write or adoption.**

Pinned input: `0e49cfeeb54ee83afb7671e9d56f11d5f400f380`. Main advanced concurrently to `7a307819c680fdb221d19cf18d49e12daebefdfa`; Iran descriptor and normalized entity were reread and are unchanged. Inputs use immutable local archive decoding with `fetch:false`. No network Git, process inspection, source commit, deployment, or portable package.

## Result

Three separate candidates cover exactly the existing intervals:
- 1922-01-01 through 1922-12-29.
- 1922-12-30 through 1925-05-12.
- 1925-05-13 through 1929-12-31.

Each candidate replaces the old Gulf/Oman mainland coast and uses **184 entire modern detached components**, plus the unchanged two historical Caspian components, for **187 polygons** including the mainland. The 189 modern components are all explicitly accounted: one mainland, 184 reusable detached polygons, and four political exceptions held outside the candidate. There is **no area, vertex-count, pixel, or distance cutoff**. The tiny donor components are included exactly.

The frozen screen's 958 old NE-only edges are not all Gulf edges. Independent scoped reconstruction finds **941 southern coast/island edges and 17 northern edges**. These candidates remove all 941 southern edges and retain the 17 northern edges as part of the protected Caspian source. Do not report the residual 17 as failed Gulf modernization or erase them automatically.

Files:
- `gulf-coast-historical-scope-candidates.geojson`: three full-country **preparatory coast-only** candidates.
- `complete-donor-accounted.geojson`: every original donor polygon with its original index and status, including all held islands. Nothing is deleted from evidence.
- `donor-component-accounting.json`: 189-row ledger, exact component digests, descriptive bounds/areas, source URLs and reasons.
- `candidate-checks.json`: actual scoped checks and their limitations.
- `protected-northern-edges.geojson`: every source edge absent from original NE, separated by version.
- `IRN-preparatory-coast-comparison.png`: inspected 1:10M comparison using LAEA 54E/32N, 100 dpi output.
- `inputs.json`, `prepare-inputs.mjs`, `prepare-candidates.py`, `final-focused-check.py`: reproducible locally saved checkpoint and preparation. Archive references, hashes and revisions preserve exact input identity.

## Political island scope, not legacy polygon membership

Contemporary official evidence is a British governmental view, not neutral present-day sovereignty adjudication. A modern donor's territorial assignment is not evidence of the same assignment in 1922.

- **114 Abu Musa, 117 Little Tunb, 118 Greater Tunb:** the 24 August 1928 India Office B397 memorandum distinguishes contested Persian claims from Trucial/Qawasim administration. These are excluded from the historical Iranian candidate on that political evidence. Abu Musa happens to exist in legacy NE whereas the Tunbs do not; that incidental fact is not the reason for their treatment. The Abu Musa removal is a political correction to the inherited proxy and must be reviewed explicitly before adoption. Do not silently remove it in a nominal coast-only source patch.
  Source: https://www.qdl.qa/en/archive/81055/vdc_100029521333.0x000008
- **85 Farsi:** the 1928 B399 memorandum describes its ownership as undetermined. Held as unresolved, **not conclusively reassigned to a different owner**. Automatic addition to historical Iran would exceed the evidence.
  Source: https://www.qdl.qa/en/archive/81055/vdc_100063253984.0x0000c7
- **115 Sirri:** B397 supports Persian effective occupation since 1887, while recording the rival claim. Included.
- **116 Little Farur:** B399 concludes Persian attribution, noting slight uncertainty about a Qawasim claim. Included, not discarded because it is small or absent from NE.
- **77 Lavan, 119 Farur, 122 Kish, 126 Hindurabi, 155 Hengam, 156 Qeshm, 174 Larak, 182 Hormuz:** B399 specifically identifies the Persian group. Whole donor polygons are included. Additional attached littoral/mangrove/islet detail is reused within the existing Iranian coastal display scope; this is not an independent 1920s shoreline survey.
  Sources: https://www.qdl.qa/en/archive/81055/vdc_100063253984.0x0000c6 and https://www.qdl.qa/en/archive/81055/vdc_100063253984.0x0000c7

The memorandum is dated 1928 even though the later compiled archival file is catalogued 1936–1947. Publication/file dates must not be substituted for the date of the original evidence.

## Protected history and full-donor answer

**A blanket full-donor copy is not safe.** It would erase the accepted historical Caspian coast/exposed land and the interval-specific Atrek trace, and would introduce unsupported island attribution. A full modern-donor base can be used for the portions explicitly modeled as modern-boundary proxies, but its distinct historical deltas must be reapplied consistently and kept qualified as proxies.

The three source versions derive from modern NE with historical water/exposed-land changes; the middle interval also has the approved Atrek line. Their source IDs alone are not proof that all international boundaries were legally identical to modern ones. The before-1922 source explicitly calls its donor a modern-outline proxy and disclaims new historical accuracy. The 1930-present donor is likewise not a new legal delimitation proof at 1930.

Protect:
1. The complete existing 1922–1929 Caspian shoreline, its two detached Iranian components, and all recorded exposed-land ownership assumptions.
2. The approved Atrek correction only in 1922-12-30..1925-05-12, including the historical-water closure and its original accepted anchors. Do not replace the nonmodern river route with a modern route.
3. The 2026-11-04 Sarakhs small-event retirement. Do not restore the removed UNTS451 patch merely because an older report contains it.
4. The previously approved **compiled-only western Iran/Turkiye correction** called out in the 2026-10-28 delta report. Raw-source replacement must not erase a compiled exclusion/adjustment.
5. Existing version IDs, dates, source evidence, uncertainty and retired evidence.

Modern legal identity is specifically not universal: the 1932 Turkey agreement changed the 1914 line, followed by a small 1937 adjustment. The 1913 Shatt al-Arab arrangement also differed from later thalweg arrangements. These facts prevent an ahistorical certification but do not make the old NE modern coordinates more historical. Do not preserve legacy NE political arcs solely as a precaution; retain real historical exceptions and replace the remaining proxy boundaries using paired donors, while keeping proxy status explicit.

Sources: https://www.iranicaonline.org/articles/boundaries-v/ and https://www.iranicaonline.org/articles/boundaries-i/

## Safe continuation plan and shared counterparts

The saved candidates deliberately isolate the coast. They are **not the final requested complete border rebase**. Their retained NE political boundaries are an operation boundary, not a historical endorsement or recommendation to leave them forever.

1. Use the full modern donor mainland for all source-modern-proxy boundary runs. Resolve the protected historical Caspian/Atrek arcs by exact source provenance and paired endpoints, not a broad bounding-box union of old NE leftovers. Iran's old mainland and donor have no byte-exact common vertex; geometric joins are therefore real operations requiring explicit review.
2. Align IRN–IRQ, IRN–TUR and IRN–AFG with their already-modernized canonical counterpart versions. On the Pakistan side, use the actual historical parent/binding for the chosen date rather than inventing a 1922 Pakistani state. The modern PAK donor is a coordinate source, not historical polity evidence.
3. For the Soviet side, inspect the date-effective USSR parent and Transcaucasian/Russian-SFSR source bindings. Modern ARM/AZE/TKM geometry is only donor context; it must not substitute for a nonexistent 1922 current-state version. Preserve the shared Atrek trace with both USSR and its actual constituent and retain Caspian water/land parity. Check neighboring-day snapshots around all three intervals.
4. Keep the four islands in the accounted side layer. Review the explicit political corrections/uncertainty before source adoption. A historical counterparty for Abu Musa/Tunbs must have valid date coverage; do not backdate the current UAE entity automatically. Farsi remains unresolved unless a separate valid scope decision supplies attribution.
5. Apply the canonical source delta to the pinned compiled Iran result, preserving the existing western correction, rather than a fresh full compiled replacement. Follow the existing delta recipe or migrate that exception explicitly as a separately reviewed source change. No whole-world generator is required.

## Actual checks and limits

Executed on the saved three candidates:
- Raw Shapely validity: all three valid, 187 components each.
- Every accepted detached donor polygon is byte-equivalent in coordinates: 184/184 for each candidate.
- Every non-Gulf mainland coordinate, all mainland holes, and both historical Caspian components remain exact.
- All source non-NE edges preserved: 167, 186, 167 across the three versions.
- Exact NE-only edge check: southern 941 to 0; overall 958 to 17 for each version.
- Intersections against seven current neighboring donors are unchanged, not zero. These are existing proxy mismatches, not a passed full shared-boundary certificate.
- Two explicit old-source-to-donor coastal endpoint joins measure approximately **849 m (Shatt side)** and **174 m (eastern coastal end)**. They are geometric connections, not surveyed/legal boundary corrections. Review them with counterpart endpoints before adoption.
- Source inputs/candidates/ledgers/checks were saved and reread. The final source identity recheck confirms Iran is unchanged despite concurrent main advancement.
- The PNG was viewed at the documented common extent/projection. Recognizable country outline and preserved northern reconstruction were confirmed visually. No independent historical positional-accuracy measurement is claimed.

Not executed: territorial source adoption, compiled regeneration/parity, full paired political-boundary replacement, live application rendering, deployment, commits, or whole-catalog validation. No permission/access denial occurred during this read-only preparation. The unresolved items are source/history/integration decisions, not an unavailable-tool claim.
