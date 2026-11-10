# Jamaica and Madagascar raw-source handoff

Status: lossless candidates locally prepared and checked, NOT applied to active source, NOT rendered, NOT pushed.

Base data source revision: f26d0896ab393aa351938637571347baa09ebf71. Data work/gis HEAD:60ca5b506b7b9166635c4a254f0cf843f9052d0b. App work/gis HEAD observed:aa49654795363a52d5ef45a0132ac554ee94394e. App has concurrent uncommitted LOD changes. Pin and mount unchanged.

JAM: 677 -> 27,715 raw coordinates; 8 -> 45 polygons. Additional original offshore components extend south/east beyond the prepared predecessor. No raw feature bounding-box neighbour intersects. MDG:12,205 -> 80,801 coordinates;322 ->680 polygons. Raw nearby Comoros, Mayotte, Geyser Reef and dateline-wide Fiji do not intersect. These checks do not certify every legacy neighbouring object.

All raw components retained, no simplification or coordinate rounding. Raw -> GeoJSON -> WKB bytes are identical. Both geometries valid. Existing entity identity, dates, parent metadata and version ID unchanged. Territorial source codec roundtrip passed; no historic-display gate affected. Files and their hashes are recorded in JAM-source-candidate-check.json and MDG-source-candidate-check.json.

Next step: coordinate the active GIS LOD worker before expanding current ISL-only scoped materialization. Prepare only JAM/MDG descriptors at the existing pin using prepareOwnedLibraryData(fetch:false); verify source preimage hashes again. Use withLibraryWrite and writeTerritorialSource for each candidate and matching immutable resource, then storeLibraryData with exact descriptor/resource scopes and push:false. Preserve other archive entries. Read back committed descriptors/resources and confirm hashes. Change app pin only after concurrency coordination. Do not rerun the old Iceland apply script.

Retained candidate descriptor and two geometry resources (4,334,317 geometry bytes) are immediate source-adoption inputs, not runtime previews or LOD. Existing original GPKG remains the sole raw baseline. Temporary duplicate GeoJSON and prior geometry exports can be reproduced from scripts and have been removed after equality checks. No main, rendering or algorithm change.
