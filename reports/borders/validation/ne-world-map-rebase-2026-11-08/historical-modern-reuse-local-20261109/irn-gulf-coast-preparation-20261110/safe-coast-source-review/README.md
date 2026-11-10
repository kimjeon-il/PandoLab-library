# Safe Iran Gulf/Oman coast source update

## Outcome and scope

Local source commit: **46e6d5c9451fb137717987483428c441051c19a5**, parent **7a307819c680fdb221d19cf18d49e12daebefdfa**, data branch main. The canonical write lease wrote one descriptor and two new immutable geometry resources. Canonical exact-prefix --store committed those three logical paths only. A separate independent archive read-back passed, including gate count 3, unique-arc replay count 3 and codec roundtrip.

- Descriptor: assets/data/territorial-entities/source/countries/state-IRN.json
- New resource: geometries/sha256-982d1a5a90f6174d713ecf37783d20e31d98ce9c54c3052cf9f009da62807464.json
- New resource: geometries/sha256-f46d52834f5d1c710dcd84b69333a97544180e2a37bbee1844400eb79855ef1e.json
- Descriptor SHA-256: b732efa94b164e83d17f88b7dd47de36655ddd70ad987d05469735cbca2c96aa
- Normalized entity SHA-256: 92f39f664b39033506b4aa1dc9e753d0466f196afc93f8e659c8dc9829500fb4

Only the existing 1922-01-01..1922-12-29, 1922-12-30..1925-05-12 and 1925-05-13..1929-12-31 versions changed. Their dates, IDs, certainty and prior provenance are preserved; source-only review evidence is appended. The two other IRN versions are unchanged.

## Geometry and complete component accounting

Approved donor: display-review-final-authorized-candidate.geojson, IRN feature, 189 polygons. Whole-file SHA-256 da1fbbf46e7a1e4cf41ec891133cf150f59e8a5f36c0fd990d1ed7c29d51956e.

Every donor component has an explicit row in donor-component-accounting.json:
- 184 detached components reused with exact coordinates, no area, pixel, vertex-count or distance cutoff.
- Mainland component 151 contributes only the safe southern coastal arc.
- Modern Farsi 85 and Tunbs 117/118 are held; existing absence is retained.
- Modern Abu Musa 114 is held; original source polygon 9 remains present and coordinate-exact. Area remains 11.72349577352035 square kilometres in all three versions. No political reassignment is made.
- Original Caspian components 5 and 6 remain coordinate-exact, as do all mainland holes.

Final count is 188 polygons in each version. The 958 original NE-only edges become 33: 17 protected northern, 13 original Abu Musa and 3 original coastal-contact edges. Southern NE-only edges change 941 to 16, so 925 southern edges are replaced. This is not a failure to include small donor components.

## Coastal joins and neighbors

The provisional 849 m / 174 m straight connectors were rejected. The accepted operation joins at actual original-source / approved-donor segment intersections, computed from exact binary inputs with rational arithmetic before one final conversion to doubles:
- West: 48.56736271884503, 29.960584658535165.
- East: 61.586142441783736, 25.206890979587786.

Original political contact coordinates remain 48.531016, 29.96133 and 61.588227, 25.202094. The old coastal runs from those political contacts to the intersection points are retained. No artificial connecting segment is added. Tiny floating-point point-on-line residuals are documented in intersection-certificates.json, not mislabeled mathematically exact zero.

The actual date-effective locally stored counterpart versions were used where available. Ten distinct counterpart/context versions were rebound against current archive inputs. All tested peer-intersection geometry and shared-boundary deltas are zero, as is the historical Caspian-water-intersection delta. These checks preserve pre-existing nonzero overlaps; they do not certify that all original overlaps were zero.

No local historical British India/British Raj source was found. PAK and IND begin 1947-08-15 and are explicitly donor-only comparators, not 1922 neighbors. GBR is active but its source geometry is the British Isles. Therefore the east-side safety claim is limited to preserving original political arc, contact and adjacent original coastline, rather than inventing a historical counterpart.

## Evidence and limits

The 1928 India Office memoranda distinguish Persian-held islands from disputed or uncertain claims:
- B397: https://www.qdl.qa/en/archive/81055/vdc_100029521333.0x000008
- B399: https://www.qdl.qa/en/archive/81055/vdc_100063253984.0x0000c6
- B399 continuation: https://www.qdl.qa/en/archive/81055/vdc_100063253984.0x0000c7

These are contemporary British official positions, not neutral adjudication of present-day sovereignty. They justify holding the four modern exceptions while preserving existing source membership; this change does not implement the earlier proposed political correction. The dated memorandum, rather than a later archival file date, is the historical evidence.

Existing Caspian and interval-specific Atrek changes, Sarakhs retirement, original land political arcs and prior uncertainty are preserved. A wholesale modern Iran replacement is not supported: the Turkey boundary changed in 1932/1937 and the Shatt al-Arab arrangement also differed historically. References: https://www.iranicaonline.org/articles/boundaries-v/ and https://www.iranicaonline.org/articles/boundaries-i/ . Existing NE proxy lines are retained as this operation's boundary, not certified as historically exact or permanently exempted from future paired modernization.

The October report warned of an older compiled-only western Iran/Turkey adjustment. The later read-only investigation in compiled-continuation-plan.md does not find a current western discrepancy in the selected three versions; it identifies an actual Atrek/Caspian compiled difference that must be preserved. Do not reapply an unverified stale western mask. No compiled chunk, generated index, runtime world or live app was regenerated. This source-only review is not compiled/runtime approval.

## Executed checks and saved artifacts

- prepare-safe-coast.py, reviewed-operations.json, intersection-certificates.json: exact source/donor operation and join certificates.
- political-exception-preservation.json: all four exceptions in all three versions, inclusion, component IDs, area and symmetric difference.
- source-topology-measurements.json: valid multipolygons, 188 components, closed rings, union equality, exact donor inclusion, protected edges, peer deltas and explicit limits.
- IRN-safe-coast-10m.png plus west/east diagnostic PNGs: viewed 1:10M common-projection comparison and both joins; projection-execution.json and visual-review.json bind the review.
- canonical-source-patch.json, source-gate-proof.json and codec/: frozen reviewed source patch, gate 3 and exact codec bytes.
- independent-patch-replay-proof.json: independent pre-write replay, 30 immutable terminal input checks, 24 structured evidence checks, 10 counterpart-version checks, all successful.
- local-source-application.json: canonical write and immediate materialized read-back.
- store-command-result.json: successful exact-prefix store with Git network protocols disabled for that command.
- local-archive-commit.json: independent committed archive read-back, gate/codec/replay and strict changed-path accounting.
- pre-store-pin-compatibility.json: 0e49 pin and 7a307 source/runtime entries were identical; only 84 report entries differed. No unnecessary pre-store pin adjustment was made.

The store preserved all 11,034 existing report entries, all unselected runtime/source archive entries and every report-owner protection ref. The app config changed only its revision to the source commit. Data checkout was clean after storage. No network Git, process inspection, full-catalog validation, package creation, push or deployment occurred.

## Read-only continuation investigation

See compiled-continuation-plan.md and its two JSON inspection receipts before any later compilation. Actual current compiled differences are Atrek/Caspian, not a verified surviving western Turkey patch. Two outside-period raw source versions also remain uncompiled; a whole-entity input hash must not falsely mark them complete.

## Remaining archival step

This report bundle is locally saved and read back, not yet separately archived/published. The coordinator will handle its authorized report scope after the source commit. Frozen preparation receipts retain their original not-applied state as timestamped evidence; local-source-application.json and local-archive-commit.json establish the later successful application. Do not rerun apply-source.mjs or store-source.mjs blindly.
