# Caucasus modern-border reuse: local staging

Targets: only USSR + Transcaucasian SFSR, existing1922-12-30–1925-05-12 slot. Input USSR assembled-four includes the previous four approved patches; TSFSR supplied at e79308f832256c70fd9f2ea6b87bfd807e7c1585. No repository/remote writes. RSFSR and other countries untouched.

## Replacement
The exact Natural Earth GEO/ARM/AZE versus TUR/IRN shared land-border chains (including short Turkey–Nakhchivan) form a single408-vertex line. No contemporary effective-control or disputed-territory attribution is being inferred: this is the specifically approved NE border-model reuse.

Old source coast endpoints lie exactly on the same NE model (Black Sea ~2.5e-15degree, Caspian ~5.5e-16degree). To reach the selected land-border endpoints, reuse only those existing coastal-model sections: Black Sea2points; Caspian3points. Existing old endpoint coordinates are preserved exactly. With duplicate joins removed, replacement is411points. These are country perimeter extensions along the same model, not edits to any lake/coast/water assets. The apparent connector lengths are11.67 and5.54 CSSpx at227.5556px/degree, not hidden snapping.

## Exact splice / preservation
Source152-point local arc and compiled248-point local arc each splice between exact preserved endpoints. Every other coordinate and its order is retained. Inverse splice restores each original geometry exactly. Restoring changed geometry plus the new provenance/content-ref restores the complete original JSON object. Existing earlier patch metadata, periods, names/lifetimes and non-target geometries remain unchanged. All four geometries are valid. Input hashes were rechecked unchanged after assembly.

Compiled content IDs use historical-world:<compact UTF-8 JSON SHA256>, with both sourceBindings and timelineRecords.geometryBindings updated to that same ref. No full source geometry is substituted for compiled data.

## Applied delta vs effective delta
USSR and TSFSR actual add/remove geometries are exactly equal within each source/compiled class.
Source adds0.6359703314853823deg² and removes0.19039868166736032deg². Compiled adds the same area to numerical precision and removes almost zero, because that source overlap was already absent in the compiled representation. Actual source/compiled removal deltas therefore **are not identical**.
Applying the same source add/remove command to the original compiled geometry yields the exact-splice compiled output within1.5571e-15deg² symmetric-difference residue. This distinction is recorded in proof.json; no artificial source/compiled equality flag is used.

## Files
- staging/source and staging/compiled: four staging JSON files only.
- replacement-arc.geojson:411points; original shared408points are unaltered.
- patch-spec.json: old/new arcs and hashes, target period.
- add.geojson / remove.geojson: source delta command, not the compiled effective delta.
- proof.json: input/output hashes, exact preservation and validity, delta semantics.
- assemble.py: reproducible local assembly.

Read-only visual comparison and source provenance are in ../caucasus-application-audit-1522/. The entire pipeline does not reassess historical border legal changes; it implements the parent-confirmed user reuse instruction. Publication must preserve latest concurrent remote changes.
