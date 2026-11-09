# ARG / CHL exact-edge review, 2026-11-09

## Result

This exact-edge audit found **0 residual ordinary ARG–CHL shared-country edges** and **35 retained SPI-boundary edges: ARG 7, CHL 28**. This does not mean no Natural Earth coordinates remain. Every one of the 35 residual edges is exactly shared with the existing **state:SPI** polygon, not between Argentina and Chile.

No source patch or replacement-completion receipt was created. Operational sources, attribution, periods, names and relationships remain unchanged. Applying the single LSIB Argentina–Chile line to these two separate SPI interfaces would change the territorial allocation; that is not authorized by geometry-only reuse.

## Evidence

- `arg-chl-spi-evidence.png` and `.svg`: small scoped map, visually inspected after rendering. Blue: ARG/SPI residuals. Orange: CHL/SPI residuals. Green: existing exact ARG/CHL border. Red: original LSIB comparison line. The map is not a legal determination.
- `ne-edge-audit.json`: all 35 residual segment endpoints and exact array positions. The direction-independent six-decimal equality test is a lower bound, not proof of origin or political equivalence. The original ARG 7 count includes one edge matched through the neighboring NE SPI feature; comparison to NE ARG alone finds only 6.
- `focused-topology-proof.json`: all three current geometries are valid. ARG/SPI, CHL/SPI and the affected ARG/CHL mainlands have zero areal overlap. The separate SPI polygon covers about 1,408.91 km² in a local equal-area projection. The raw LSIB line crosses its interior for about 74.42 km.
- `exact-existing-modern-shared-arcs.geojson`: 4 existing ARG/CHL shared chains, 3,440 edges and 3,444 distinct coordinates, copied exactly from current source and verified on both country sides. This is **already-adopted evidence**, not a new candidate or simplification. Of these points, 3,438 match raw LSIB coordinates exactly; 3,439 match at ten decimal places. The unmatched points are not silently normalized or claimed to be LSIB originals.
- `raw-lsib-icefield-excerpt.geojson`: consecutive unmodified raw LSIB array coordinates around SPI, with source indices and feature ID. It is comparison-only, not an approved replacement or completed display simplification.
- `source-and-preservation-evidence.json`: current source descriptors, geometry preimage digests, final official-decoder readback, exact source hashes, historical policy quotes and reproduction commands.
- `artifact-hashes.json`: hashes and sizes of retained evidence. The 20.96 MB reconstructible input intermediate is removed after checking; the immutable source originals stay in the existing shared archive.

## Fixed inputs and protection conditions

Library source commit: `2d65ccfe2fa57a42bfbe26f8952af2a416b45159`. Inputs were decoded with the current application main's official `decodeArchiveEntry(fetch:false)`, `decodeTerritorialSource`, and `normalizeTerritorialLibraryEntity`. Generated country chunks/current-world were not used as authoritative inputs.

ARG and CHL current geometries exactly equal the approved prepared donor `da1fbbf46e7a1e4cf41ec891133cf150f59e8a5f36c0fd990d1ed7c29d51956e`. SPI still has a separate Natural Earth source geometry and identity.

Original LSIB local archival logical path: `tools/historical-library/sources/lsib-11.4/boundaries.geojson.gz`, SHA256 `de87a3d317b7c18c07a8d16d1299778aaa19fd43a8d7b06a1217ac397cbd4194`. Selected source feature `4fa5f249-3c16-4dc2-961f-73fa5bfb0211` has 117,257 original vertices, country pair ARG/CHL and status “International Boundary”. No corresponding ARG/SPI or CHL/SPI line exists in this source.

The stored `reports/borders/data/country-files-lsib-2026-10-21.md` explicitly withheld ARG/SPI (line 76) and CHL/SPI (line 99) due to country-pair mismatch, and preserved the existing allocation (line 31). The current three-source geometry confirms this is still a separate SPI boundary. This historical record is corroborating evidence, not an independent grant of permission.

The separately recorded world GeoPackage SHA `903802ac3af29e071a608f27a3c1ca67372d38dba2125f8325b9569f454f519d` was not locally verified, and no ARG/CHL retained-index artifact was found. These are explicit provenance limits, not permission to invent a new simplification. Korean retained-index files do not establish an ARG/CHL method.

To revisit these 35 edges, first establish an explicitly approved treatment of the separate SPI object and a source with matching political scope. A changed country-pair or SPI allocation requires a new reviewed decision. Keep all three preimage hashes and the stored shared-border topology bound to any future work. Do not delete SPI, choose a side, snap, invent connectors, or substitute a newly calculated simplification automatically.

All work ran on the user's Windows PC. Only this evidence folder was written. No runtime source, active generator input, mount, code, process, pin or compiler artifact was modified. No fetch, download, publication, installation, full-project validation, worktree, branch or portable package was performed.
