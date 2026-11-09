# German 1878 Core repair milestone

Status: source and matching Core published on work/gis; selected CI and saved-operand replay verified. Runtime activation and Viewer verification are not completed.

- Source commit: 6dd607962173cce251aef13c40b38028490f72d9.
- Paired commit: 5eb58c250ef68b1236b154643410e8d986169152.
- Core source fingerprint: f4138927ea2044814f11cf60daadfb7a0a7b8ef11860ddaab57f081ed365a16c, the same 160 canonical input paths.
- [Official P2 build/publication](https://github.com/kimjeon-il/Pando/actions/runs/42569328420): attempt 1 failed on CMake HTTP504 before compilation; the unchanged failed-job rerun succeeded.
- [Final registered checks](https://github.com/kimjeon-il/Pando/actions/runs/42570344615): three native targets passed; WASM-domain13/13, plain JS76/76 and WASM-bound units210/210 passed. The selection contains13 unit files, no browser or full matrix.
- Original saved1878-04-01..1878-12-17 operands22/604 and isolated pair normalize to185/124 components, discard0, with two canonical store round trips. Their output bytes equal the preceding verified Core97 result. Exact vertices and undirected edges are preserved through normalization;14 components per case still fail ordinary source admission.
- The five additional corrections change tests only: source admission rather than a winding proxy, canonical persisted provenance, a genuinely historical compiler fixture with current/current control, moved worker root, and the current bounded ARG runtime reader.
- The old current-world file is absent from mounted/Git-tree runtime but remains as a12.44MB archive-index entry. ARG verification reads only current index metadata plus its691B descriptor and39,446B geometry; source/projection/runtime geometry values match. No world restoration or generation was used.
- Live work/gis70, application main, library pins, source and runtime data were not advanced. Mesh5 runtime is not relabelled or accepted as revision6.

## Evidence and limits

[Final handoff](final-handoff.json), [explicit replay comparison](final-1878-comparison-proof.json), [pair verification](final-pair-verification.json), [independent final check](review/independent-final-pair-and-replay-check.json), and [official selected-check result](final-checks-evidence/application-checks-non-browser.json). The completed-core-proof-manifest.json lists exact archived proof files and hashes. Raw source operands, generated coordinate payloads, duplicate WASM, and unfinished report folders are excluded.

This is not a full interval peer-selection compile, connected publication, Viewer check, app main deployment or runtime6 activation. The mathematical exactness of every native Boolean output edge is unproved. Source admission, original coordinates, historical metadata and precision budgets remain unchanged.

The existing224-file verification location (5,686,693bytes) is retained for the parent's next bounded1878 interval preflight. First compare relevant canonical source versions against the saved fixture inputs; no broader runtime generation has started.
