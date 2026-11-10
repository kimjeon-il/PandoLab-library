# Pre-1963 Indonesia: Papua membership and six-island update

## Latest checkpoint: 26 replacements applied in two reviewed steps

The six named islands below were followed by 20 individually verified connected islands. Current local source commit is `44fcddf4140cf49b72238da86575a95de9ef2876`. The 817-component pre-1963 version now contains 644 exact modern components, 171 original NE components and two unchanged modified shared mainlands. All restored 450 are preserved. See `additional-connected-islands-review/local-archive.json`. Two point-connected groups and four identity cases remain unchanged; the full 2,962-component membership problem remains unresolved. The section below preserves the earlier six-island checkpoint.

## Applied result: first six-island checkpoint

Six independently identified retained islands were updated locally after parent review and approval: Kelang, Obilatu, Saparua, Makian, Tidore and Tufure. Complete modern-minus-West-New-Guinea scope is **not certified**.

- Local source commit: `9f59df3a2144d2e76b5d8bbad8df7f7ebe8ab8f6`.
- Previous archive: `2af6c0834ac2987a7ffdfe3cde0db1827b04d4e1`; IDN preimage was exactly unchanged from `ebae7be60b7b40a00627028ee16841701c3511a6`.
- Only the IDN descriptor and one new geometry resource changed. Other logical paths, including existing reports, are identical.
- Period remains 1945-08-17 through 1963-04-30; polygon count remains 817. All 811 untouched components, including existing 618 exact modern components and restored 450, are preserved exactly. Result: 624 exact modern components, 191 original NE components and two unchanged modified shared-mainland components.
- Source gate (one changed version), codec roundtrip, archive readback and exact preservation of the other three IDN versions passed. No fetch, push, compilation, deployment or BIG upload.

Final application proof: `six-island-local-archive-commit.json`. Preparation-time source evidence retains its original hashes/status. This later record establishes application. Do not rerun the writer against the changed preimage.

## Why only six

Each island has one original retained NE component, one complete connected official BIG land polygon, and one whole approved modern donor. An official island-name point lies inside all three. Every modern component intersecting the entire connected BIG polygon was enumerated and yielded exactly the selected donor. All six were visually inspected against the full official land polygon.

| Island | NE index | Modern index |
| --- | ---: | ---: |
| Kelang | 35 | 2789 |
| Obilatu | 42 | 2808 |
| Saparua | 163 | 2990 |
| Makian | 209 | 2891 |
| Tidore | 211 | 2903 |
| Tufure | 247 | 2696 |

Current official data verifies physical island identity, not historical political membership. The historical retained-side anchor is the existing approved NE period source. Complete modern coordinates were copied without clipping, snapping, rounding, buffering, simplification or size-based omissions.

The earlier 194-group/331-component proposal is **diagnostic only and must not be applied**. NE53/modern2163 illustrates why positive-area correspondence alone is insufficient for whole-island replacement. Other 188 groups remain unchanged. Shared Sebatik, Timor and Borneo are unchanged. Original NE241 and NE249 remain unchanged because they have no positive-area modern correspondence. All 191 remaining NE components and two modified mainlands are listed in `six-island-residual-scope.json`; indices refer to the fixed preimage.

## Still unresolved

Approved modern donor: 4,128 components, geometry SHA256 `ac23d0aacbf6ba6b72c4797b40122fb22508cf37c513792c77df7ed9f05a9623`.

- 214 overlap only the original 25 excluded NE Papua components; 952 overlap only retained NE; none overlap both.
- 2,962 have no positive-area NE correspondence, about 7,009.242421 km². They must not be silently omitted. Missing correspondence does not mean all are politically disputed.
- BIG current provinces match 539 previously unmatched components to current Papua. Fourteen also share an entire connected BIG land polygon with an old excluded NE anchor. Both are research findings, not applied historical exclusions.
- Sain/Sayang/Sajan (modern3126 candidate) and Piyai (modern3127 candidate) require separate historical investigation. Kiyas representation remains unlocated. Current official reports and BIG journal record competing provincial claims.
- Geometry dossiers 3227, 3275, 3624, 3696, 3987 and 3991 are research leads, not a deletion list. Triangular/quadrilateral geometry is not an omission reason. These six plus Sain are **not a certified minimum unresolved set**.

Keeping only 952, or taking 4,128 minus 214, does not establish complete historical scope. This application makes no new decision about the 2,962 unmatched components.

## Public sources

- UN 1962 New York Agreement: https://treaties.un.org/doc/Publication/UNTS/Volume%20437/volume-437-I-6311-English.pdf . Existing territory and transfer framework, no complete island inventory.
- GATT L/2072 (1963): https://www.wto.org/gatt_docs/English/SULPDF/90760390.pdf . Contemporary western New Guinea/offshore-islands description and 1963-05-01 transfer, no fine boundary.
- Bakker 1965 map: https://www.papuaerfgoed.org/sites/default/files/collectie/files/2003-10/Bakker_1965_Strategie.pdf . Broad Raja Ampat/Biak/Yapen/mainland context, postperiod and too coarse for all islands.
- BIG current province service: https://geoservices.big.go.id/gis/rest/services/STIG/Batas_Provinsi/MapServer/0 . Connected-landmass evidence; not historical political authority. Extra Z/M values were ignored only in analytical copies; XY unchanged.
- BIG public island names: https://geoservices.big.go.id/rbi/rest/services/BASEMAP/Rupabumi_Indonesia/MapServer/10 . Exact point containment for selected identities; nearby names are leads only.
- BIG Geomatika 23(1), 2017: https://www.big.go.id/uploads/content/produk/Geomatika/Vol23.1/JIGVol23.1.pdf . Sain/Piyai/Kiyas dispute and hypothetical marine lines, not membership rules. Author opinions are not publisher positions.

Additional official party reports, archival leads and access limitations are in `public-evidence-notes.json`. Denials were respected; prior GitHub fetch was not retried or bypassed. SIPULAU login/NDA bulk export was not used. Public RBI is a separate documented service.

Raw downloads remain in `public-sources/`; `retrieval-manifest.json` contains URLs, sizes and hashes. All 27 saved source records were reread and SHA256 verified. **BIG redistribution rights are not established. Do not blanket-publish raw BIG originals.** These files are retained for current reproducible membership research and independent review.

## Evidence

- `canonical-source-patch.json`, `six-island-source-gate-proof.json`: exact prepared patch and gate/codec.
- `six-island-component-ledger.json`, `six-island-independent-replay-proof.json`: six anchors, full donors and 618/450/811 exact preservation.
- `six-island-topology-proof.json`, `six-island-projection-evidence.json`: full candidate validity, executed metre projection, unchanged dates, neighboring spatial screens.
- `six-island-visual-review.json`, `visual-evidence/six-island-all-groups.png`: every changed group visually inspected.
- `six-island-local-archive-commit.json`: final local commit and exact two-path diff.
- `six-island-residual-scope.json`: unfinished original-source scope.
- `component-correspondence.json`, `public-component-correspondence.jsonl`, `official-landmass-anchors.json`: correspondence research, not blanket political assignment.
- `research-findings.json`, `local-source-discovery.json`, `read-only-verification.json`: initial local-only phase; its no-network/no-edit statements describe that earlier phase.
- `research-checkpoint-verification.json`: current local reread/hash checkpoint.

Inherited low-certainty effective-administration proxy remains unchanged; actual 1945-1949 control was not reconstructed. Modern undated neighbor references and post-2002 TLS are spatial screens, not full-period historical counterparts. No changed island touches those reference polygons. Original responses, intermediate mappings and unique visual evidence remain local for continuing review.
