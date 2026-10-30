# Map Toolkit 0.5 quality iteration (0.5.1 workflow patch)

> Report ID: MAP-TOOLKIT-QUALITY-V2-20261029 · Status: completed-scoped-verification; phone-check-pending · Map data: not-applied · Indexed: 2026-10-29  
> Last edited: 2026-10-30  
> Installed source: work/ui d0bca5aa37e7c66da8d9a01e9b7c39d942e853b1  
> Scope: projection/georeference, global gazetteer, truthful model evaluation and private Work analysis

## Target and evidence

The current private plugin is Map Toolkit 0.5.1, using immutable source d0bca5aa37e7c66da8d9a01e9b7c39d942e853b1 and independent analysis-data revision 8d668a6c9ffb7844849fb63af5b02ebc8a496b70. Earlier 0.5.0 evidence below uses source 44c68f7726c6e83b367ad3fee3d01aa98b39dbcc. Application runtime pins and unrelated native/icon/rendering work were preserved. This task did not integrate application main, build installers or deploy an application.

The eighteen-original macro cohort has six training, six validation and six test sheets; each contains four modern/two historical and three colour/three monochrome sheets. Production families and duplicate editions remain within a fold. Source/rights/date distinctions, raw hashes and explicit derivatives are recorded in reports/map-analysis/corpus/quality-v2/selected. All labels have two agent source-only overlay review passes and explicitly PARTIAL coverage. They are not human-reviewed or whole-map gold. Freeze revisions and reversible contract corrections are retained.

## Implementation and actual checks

- The shared C++ projection owner composes geographic coordinates, projected metres, warps, inverse transforms and boundary export. Supported-domain and fold checks remain required. Four final-review regressions reproduced wrong metre export, a geographic-RANSAC veto on valid projected registration, and duplicated-observation leakage; all now pass.
- Fixed projection recommendation requires six distinct observations, at least 20 percent hull coverage and original-pixel CV P95 at most eight. Unknown projection search uses disjoint 6/6/6 fit/selection/confirmation observations and rejects duplicates before splitting. Affine-equivalent automatic hypotheses are not counted as separate evidence.
- Analysis-only global search uses 236,849 cities500 records and evidenced historical aliases, independently of the displayed map. Signed manifests bind the data revision and lazy shards; missing coverage or an ambiguous match does not prove a location.
- Focused checks passed: 44 Node projection/gazetteer/plugin/package/import cases, 14 runtime/probe cases, two inspection Python regressions, and 18 projection cases repeated against the actual packaged CI WASM. These groups overlap; they are not a claim of 78 unique tests.
- One fresh final reviewer rechecked the three original Important findings after the fix pass, independently ran the four regressions and found no remaining Important direct risk.
- CI push run 40879253036 rebuilt only affected WASM successfully. A preceding manual workflow dispatch failed before compilation because its shallow checkout lacked the comparison base; no signature or prerequisite was bypassed.
- Private installation readback confirmed version 0.5.0 in both metadata files, 210 installed files including the generated overlay, exact engine/georeference/data-binding bytes and removal of eleven retired files. Private reference IDs, authentication links and package contents are excluded from this public report.

## Actual training and rejected candidate

Fresh official MobileNetV3-Large initialization has SHA256 5c1a416349c4cf298f2a6a5e2600ed0ee55e604713578f5e74e6bc8bcaef7997. The old macro-v6 ancestral lineage could not establish independence, so it was not inherited. Six new training sheets and six source-disjoint older auxiliary sheets used batch one, learning rate 1e-4, encoder freeze two epochs, maximum twenty and validation patience five. Training completed twelve epochs: 1,584 attempted batches, 1,578 updates, six AMP skips. Best epoch index six has validation loss 1.0641453393868037. The checkpoint and 0.55 threshold were frozen before final-test inference.

The checkpoint SHA256 is 253b488859afad07e978a1a23b96bf65b646234fe961fbc3d0e1658d032d594c. ONNX SHA256 is c3894f5f12fb4973f5be92e74b04f5c8fdb6c4e0bd1e23edac3eebcdf4d2bd84. Weights remain private and are NOT published to the public data repository.

Known-patch per-map-macro results (not whole-map accuracy):

| Channel | Precision | Recall | Positive test maps |
| --- | ---: | ---: | ---: |
| International | 0.5834775647 | 1.0 | 3 |
| Administrative | 1.0 | 0.5846153846 | 1 |
| Coast | 0.4051724138 | 1.0 | 1 |

The candidate fails precision/recall floors, confounder nonregression and whole-map review coverage. Text/frame false positives regressed in fourteen of fifteen measured class/confounder comparisons. Its complete new lineage passes independence, but partial labels cannot qualify whole-map performance. The final test is now exposed; do not retune this iteration against its results.

The candidate remains pending, trainingOnly:true, releaseApproved:false. Hydro/transport/frame are unobserved. The private default remains macro-v6, also pending and review-required; this is not a validated-model release.

Actual ORT WASM CPU inference produced finite 1x7x512x512 output, maximum absolute difference 0.0006875991821289062 and mean 0.00001958671989642621 against the fixed diagnostic tensor, below the 0.005 execution-parity threshold. This verifies execution parity, not extraction or historical accuracy.

## Work cloud and user flow

A fresh ordinary Work cloud session loaded the managed private installation without PC Remote or ZIP reattachment. Actual versions: Node 24.22.1, Tesseract.js 7.0.0 and ONNX Runtime Web 1.30.0. It downloaded the official NRCan Africa monochrome continental PDF, 932,213 bytes, SHA256 6dd3c89b159bd8d6ab09bb75cf261ad04b678f3ca56e9c58b1e25cb09f4f0780, at 1224x1584 pixels/144 dpi. Source URL: https://ftp.maps.canada.ca/pub/nrcan_rncan/Geographical-maps_Carte-geographique/SmallScaleReferenceMaps/english_continental/b%26w/Africab%26w.pdf . Its 2024 copyright/file-creation date is not a confirmed depicted-boundary date.

Default English OCR found 58 detections; actual macro-v6 inference completed 12/12 tiles. The provisional graph has 292 chains and six faces. Country labels matched unrelated settlements; duplicate observations were refused. Status stayed needs-georeference, review:null, with no export. Source/legend inspection shows substantial pale inland-border omissions and coastline/graticule/text/frame false positives. Six provisional faces are not six verified countries; macro-v6 does not claim its unobserved coast/hydro/transport/text/frame channels.

The actual downloaded provisional preview has 454,686 bytes and SHA256 896460b5e9a39fd8cd875fd4e6c8a81150541ec8fcf4b1054e20379d6ee3b8c6, matching the cloud receipt. Registration-only revision completed in the next Work turn: revision 0 to 2, affine selected by auto, 38.37 percent hull coverage, CV P95 0.74480961 pixels and reserved-five maximum 0.24465641 pixels. No folds or domain errors occurred. Source, OCR, raw/current pixel graphs, segmentation signature and model/producer/core identities were unchanged. Those points are not independent cartographic or historical truth. No existing chain could be confirmed as an international border; chain 77 was correctly rejected as the 30-degree-N graticule. The source-reviewed short pale vertical border segment subsequently exercised the manual-add patch described below; no unreviewed chain was approved.

The actual 0.5.0 workflow exposed a missing manual-add command: moving an unrelated chain with replace correctly failed the shared-endpoint guard, leaving revision 2 unchanged. No raw job was patched or re-signed and no unapplied proposal was exported. The canonical job revision owner now accepts explicit manual add with one boundary class and a source-review reason; existing C++ pixel validation/topology rebuild handles the inserted path without relaxing endpoints or duplicating vectorization. Two regression tests observed Unknown graph revision before the fix, then passed with unchanged inference, invalidated review, preserved existing endpoints, valid T-junctions/no false face and invalid-input refusal. Thirty-eight affected Node cases and scoped ESLint pass.

Private patch 0.5.1 uses pushed immutable source d0bca5aa37e7c66da8d9a01e9b7c39d942e853b1. Both metadata files, 210-file inventory, unchanged analysis/model binding and metadata equality apart from version were read back. The package has 209 source files, 30,767,535 raw bytes and a 23,978,272-byte ZIP, SHA256 b4cf76fd4b08b3cb1c63d14edf85899e18920a64a3bee0b642d79910ca4057f5. A fresh Work session verified source identity and all 174 pinned runtime files, then completed actual default analysis and manual addition. Old signed jobs were not resumed under changed producer signatures.

The previously local compiled core and CI variant have identical complete input hashes, compiler 4.0.20 and source SHA256 05e684d9c847b8e820e81048dec74a513ab6a3f631a70f009301adc66ff56ed3. The already-tested local artifact was committed without changing its bytes. Normal origin merge had only two generated-artifact conflicts, explicitly resolved to retain that verified artifact; all unrelated WIP remained unstaged. No C++ algorithm change or full app rebuild was needed for manual addition.

Actual 0.5.1 default OCR and all twelve inference tiles completed. The explicit add and 3px refine-line commands produced the source-reviewed manual line:87 at revision 3. Original source, OCR, segmentation, rawGraph and model/producer/core identities remained unchanged. Whole-graph reconstruction can change other candidate vertices/semantics/confidence and moved one selected endpoint by one original pixel. All review is invalidated by edits; current IDs were re-read. Agent visual review compared the original and the selected short stroke at fivefold magnification; it did not approve the remaining graph.

The existing review command selected only line:87 and export at revision 4 returned one LineString, with name/ownership/validity unspecified. Individual links for the five standard files were provided. Both optional five-file ZIPs were actually downloaded and their members verified; the first GeoJSON was also downloaded directly through its individual file link. Its 10,074 bytes and SHA256 d9ab06dd083a29ee0a0ce0ad7b8d92aebcde7f8e9ca7bb45bf8cad0534d1d227 match the first ZIP member. Root-side CRC, entry-name, source hash and complete-manifest checks passed. The next-turn export in the same active Work environment preserved analysis/preview/report bytes, geometry/properties/source/review and job signatures; the sole GeoJSON content difference is a newly generated feature UUID, explicitly reported rather than hidden. First local files remained intact. See cloud-flow.json for exact hashes.

The exact first GeoJSON SHA256 d9ab06dd083a29ee0a0ce0ad7b8d92aebcde7f8e9ca7bb45bf8cad0534d1d227 passed the ordinary Pando browser editor import, batch Undo/Redo, existing vector-editor conversion, vertex edit, edit Undo/Redo and GeoPackage save/reopen. The saved 57,344-byte SQLite file has SHA256 8613b3baab38751c767406071a0a18f8038e704950c9d52200bdf56a84e82b04. Full geometry registry, timeline records, edited resolved geometry and provenance matched after reopen. See pando-flow.json, pando-flow.png and pando-test-project.gpkg (TEST DOCUMENT ONLY). No native Windows/Android dialog or physical phone result is claimed. The physical-phone 0.5.1 check is pending direct user observation; prior-version proof is not reused.

## Storage and limitations

No new environment, full repository/data copy, GIS program or server was introduced. Original maps and labels remain protected. Retained generated files have current named uses: the private candidate model directory (46,631,136 bytes) contains the best checkpoint, ONNX and parity tensors designated as evaluation evidence; the existing public encoder (22,132,113 bytes) remains the pinned training dependency; the failed browser trace (11,358,858 bytes) is the actual reproduced RED workflow evidence. The two downloaded output ZIPs (998,722 bytes together) and extracted first output support download, persistence and import verification, rather than installation caching.

Automatic approval review rejected deletion of two reproducible inspection PNGs (99,464 logical bytes), an empty failed diagnostics directory (zero bytes), and the two ended 0.5.0 package/ZIP pairs (109,484,306 logical bytes); no detailed reason was supplied and no alternate deletion mechanism was used. The user then executed the exact scoped PowerShell command for the four 0.5.0 targets. Fresh checks confirmed all four absent: 109,484,306 logical bytes removed (104.4 MiB). D: free space was 58,413,703,168 before the handoff and 58,518,110,208 after it, an observed increase of 104,407,040 bytes (99.6 MiB). This interval is reported separately from logical file size because allocation and concurrent writes affect free space.

The 0.5.1 transfer package is now ended, as is the previous 0.4.2 transfer package whose deletion was previously blocked. Their four remaining targets total 106,517,102 logical bytes (101.6 MiB). Fresh checks found no command-line consumers or symlinks; pinned code/data Git objects and the original macro-v6 bytes remain available. A one-line forward-slash PowerShell handoff requests their removal without bypassing the earlier deletion rejection. The two inspection PNGs and empty diagnostics directory also remain blocked. See cleanup.json for exact accounting and outstanding targets. The latest measured D: free space before this handoff was 57,399,828,480 bytes; differences outside the measured cleanup interval are not attributed to this task.

Historical reconstruction accuracy, native Windows/Android save/reopen and actual 0.5.1 phone use are separate from engine/contract success. No historical territory ownership, name or validity period was automatically assigned.



## Source delivery and remaining integration limits

The source-reviewed manual-add fix and installed runtime are pinned to d0bca5aa37e7c66da8d9a01e9b7c39d942e853b1. The current-model browser regression updates were committed as ee44b97d5a16bce04d22d823086032a81cb1339a and pushed in a committed-tree merge 74a76c93ffec98ab913c978d30f973d2077fa25f. Relative to the then-current remote, this merge changes only the two tested files. Local checkout/index icon work was untouched: ordinary fast-forward was refused for two protected icon files, so the local branch remains behind the remote merge until that independent WIP is resolved. No force push, stash, workspace/branch creation or main integration was used. P1/P3 runs 40894021589 and 40894021480 passed for the pushed test merge.

A concurrent source-branch P2 run 40888901902 failed in unrelated builtin-world generation (undefined domain in builtin-world-compiler.mjs); it is not represented as a plugin check pass. Its predecessor for the plugin source was cancelled by normal concurrency. The source-matched core, packaged loader, focused engine cases and actual Work/Pando workflow passed independently.
