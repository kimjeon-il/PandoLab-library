# Modern raw source transition, 2026-11-10

## Completed pilot

Existing Iceland source version was changed in place to unsimplified DoS_WP_11_4 coordinates. Existing identity, version ID, dates and other non-source metadata were preserved. All 2,393 raw polygons and 432,916 coordinates are retained (previous prepared source: 8,251 coordinates). GPKG WKB to GeoJSON to WKB byte equality, geometry validity, canonical source codec, metadata guards and committed archive readback passed.

Data local work/gis commit: f26d0896ab393aa351938637571347baa09ebf71.
Application local work/gis pin commit: b1ab73152.
No remote publication, main change, LOD algorithm change, runtime regeneration or deployment occurred. The rendered map is not claimed updated. Source commit contains only the existing ISL descriptor and its new content-addressed coordinate resource; all unselected archive entries are preserved and no archive entry was deleted.

## Original material

Use the preserved WorldPolygons11_4.gpkg in ../historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved. Its receipt records SHA256 55fab422ef09e35eb48d68141b9ece0ace86d4276dfe332a04dfd401c0bfc80c. Select DoS_WP_11_4, not G65 or G99_5. Original ZIP/GPKG are unchanged. Iceland raw feature identity, attribute values and WKB SHA are recorded in the committed source and ISL-raw-proof.json.

## Remaining work

The 254 existing modern donor bindings have 223 one-to-one raw attribute candidates and 31 requiring alias/composite/territorial-policy review. A matching code alone is not adoption approval. These are not completion counts. Modern shapes and historical shapes reusing modern remain the priority; unique historical borders are deferred. Indonesia is assigned to a separate worker.

The existing display-review gate binds historical-source geometry to display receipts. Pure modern Iceland required no gate change. Historical reuse must not inherit outdated simplified-display receipts or erase historical provenance to bypass that gate.

## Reproduction and storage

Scripts run from Pando's GIS worktree using existing OSGeo4W only. prepare-isl-raw.py reconstructs the temporary raw candidate from the preserved GPKG; prepare-isl-source.mjs records the fixed baseline source candidate. apply-isl-source.mjs has fixed preimage guards and must not be blindly rerun. Coordinate candidate duplicates were removed only after verifying committed recoverability; cleanup.json records 34,395,281 logical bytes removed, not measured free-space recovery. Keep the raw GPKG/ZIP and the committed source resource.

Existing clean app work/gis was fast-forwarded to locally cached origin/work/gis d783b6a3b; existing clean data work/gis was fast-forwarded from 887f7218 to local latest source base be66061c. Both had zero unique commits before synchronization. The old app data pin 11a5fe61 to be66061c changes only prior source work and reports, with generated runtime unchanged; this avoids overwriting newer source work. No fetch or network retry was made.
