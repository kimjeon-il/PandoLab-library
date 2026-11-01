# Existing packaging contract triage

## Conclusion

The Windows custom-protocol failure is a pre-existing assertion against the artifact-fetch wrapper command. It is not evidence that the actual native compiler has lost its embedded asset protocol. The inspected native producer explicitly passes `--features custom-protocol` for Windows offline builds. The failing test and the package script it reads are byte-identical Git blobs on both compared commits.

This conclusion is limited to this assertion. Other current Core, editing and fixture contract failures remain unresolved failures. This report does not mark an existing red gate as passed or authorize disabling it.

- Current commit: `e53f067ef37cafc4bd5d4d50e323f8866e7c9833`
- Main baseline: `2b460e40dbc51de2d13b0fe40e11bd4af9e49b75`
- Last source/log observation: 2026-11-01 02:42:31 UTC.
- Method: immutable GitHub file reads and existing CI logs; no code changes, builds, test execution or remote mutations.
- Report save: uses the already retrieved evidence only; no further query.

## Exact observed failure

The existing [P3 log](p3-contracts-before.log), run 41265483904 / job 124727574107, reports:

```text
Test: the Windows executable explicitly enables its embedded asset protocol
Location: tests/unit/web-shell-packaged-build.test.mjs:8
Actual: node packaged-artifacts.mjs --fetch --platform=windows --mode=offline
Expected: /--features(?:=|\s+)custom-protocol(?:\s|$)/
```

The [test](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/tests/unit/web-shell-packaged-build.test.mjs) reads `apps/editor/package.json` and applies that regex directly to `scripts['build:windows']`. It neither runs an EXE nor checks an embedded asset request. Because the test and its exact input are unchanged on main, the same string assertion is already inconsistent with main's wrapper command by source inspection.

## Actual native production path

1. [packaged-artifacts.mjs](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/apps/editor/packaged-artifacts.mjs) uses `--fetch` to request a source-matched CI artifact.
2. [P1 workflow](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/.github/workflows/remote-development-p1.yml) runs `node apps/editor/packaged-artifacts.mjs --ci-build --platform="$NATIVE_PLATFORM" --mode="$NATIVE_MODE" $NATIVE_TEST`.
3. [native-producer.mjs](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/apps/editor/native-producer.mjs) constructs the following Windows offline arguments:

```json
["build","--debug","--bundles","nsis","--target","x86_64-pc-windows-msvc","--features","custom-protocol"]
```

The producer then appends its config overlay. Offline Windows configuration enables the NSIS bundle and uses the staged frontend directory. [Cargo.toml](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/apps/editor/src-tauri/Cargo.toml) maps `custom-protocol` to `tauri/custom-protocol`. The producer requires a setup executable, and the native bundle verifier requires that installer for an offline Windows artifact.

The existing [native-build.test.mjs](https://github.com/kimjeon-il/Pando/blob/e53f067ef37cafc4bd5d4d50e323f8866e7c9833/apps/editor/tests/native-build.test.mjs) tests the real argument function for offline `custom-protocol` and `nsis`. That test's source was inspected; it was not rerun here. The arguments above are derived from source, not from a new native build.

## Exact Git blob identity comparison

All 15 files below have the same blob SHA at both commits. The SHAs are Git blob object identities, not SHA-256 content digests.

| File | Blob SHA on both commits |
|---|---|
| `tests/unit/web-shell-packaged-build.test.mjs` | `fd9244c360943dcc4743fde0e146e073d9d29cf6` |
| `package.json` | `12f427c5f11e3731a37f1f1c89b97aac3dade59d` |
| `apps/editor/package.json` | `229970c135c740d57ea7de16980fd112aafadb3f` |
| `apps/editor/packaged-artifacts.mjs` | `e4884a455f87b0303b46445a79e04dd89df709b0` |
| `apps/editor/native-producer.mjs` | `55b8908c04b969534cd8200d9eb7dbed17ce7f91` |
| `apps/editor/native-contract.mjs` | `c28ca70496f8b95e9b3dd586b8b2fbe3460e5b3c` |
| `config/native-artifacts.json` | `7487c5ee5b00bf62300f67608280d4d44b2f5958` |
| `.github/workflows/remote-development-p1.yml` | `f4a19e098935b30077b38e9746f45197cedbe4ef` |
| `apps/editor/src-tauri/Cargo.toml` | `15792e89d031caffc67ae8686bb2576d074b9836` |
| `apps/editor/src-tauri/tauri.conf.json` | `f36021c8a71ad1ccae0a67a85d2d19fa9eb46333` |
| `apps/editor/src-tauri/build.rs` | `fc7fc33fa87b5402460022e5f6e76850213651fc` |
| `apps/editor/tests/native-build.test.mjs` | `bb0ab9d2f948b1455c9c70d66b74fda62cbcef79` |
| `apps/editor/stage.mjs` | `1388b5e6739f6eda244dd8de200c110d52bdbac4` |
| `apps/editor/check-stage.mjs` | `27a663848113b6eef0aff53876d9ee74e3689ec0` |
| `.github/workflows/web-pages.yml` | `befde61924e1f8751b564fc2604730142bebf49c` |

The transitive frontend asset builders are **not** identical:

| File | Main blob | Current blob | Observed change |
|---|---|---|---|
| `scripts/lib/frontend-build.mjs` | `2b3f478079a42cee6ff498f72026912c8a57620e` | `d4dd2a3feebab650110331d17a355924659c09b8` | Adds createInitialLandPreviewAsset, generated viewer preview bytes and initialLandPreview build metadata. |
| `scripts/lib/product-assets.mjs` | `f8b1ab83914413c31e1761b7418f8b8d29a5e6b1` | `bd18960a21b34632cb8fc2f471dcfa5522d7dfd8` | Reads immutable viewer build metadata, requires initialLandPreview.url and includes its data asset. |

Therefore this report does not claim that every packaging input is unchanged. The previously completed [P6 log](narrow-final.log) records Web staging of 1,822 files / 238,139,589 bytes / 0 native files, App test-fixture verification of 1,131 files, and App map-data verification of 1,829 files. These are stage/check-stage results and do not prove native EXE or installer execution.

## Existing CI baseline evidence and limits

### Main Architecture stopped before unit execution

- [Run 41088220785 / job 124174906618](https://github.com/kimjeon-il/Pando/actions/runs/41088220785/job/124174906618), main `2b460e40dbc51de2d13b0fe40e11bd4af9e49b75`: failed during planning with `Unregistered test: tests/browser/post-2000-world-timeline.spec.mjs`.
- [Run 41082088455 / job 124153552959](https://github.com/kimjeon-il/Pando/actions/runs/41082088455/job/124153552959), preceding main `0a87cabc5c04fe954f54b934f55f5f43b6f71ffb`: same failure.

Neither job executed the unit contracts, so neither establishes that the current numerous unit contract failures were already present.

### An older Architecture run proves one matching CSS failure

[Run 40895207190 / job 123523625956](https://github.com/kimjeon-il/Pando/actions/runs/40895207190/job/123523625956), main `2c41bf5fca8ccdcb69a5485d7bceddd347647ac7`, reports 148 tests, 137 pass, 2 fail and 9 skip:

- `CSS selects relevant UI checks without C++/GIS build or data generation commands`: `Unclassified product change: assets/css/features/map-rendering.css`. The current P3 log contains this same test failure.
- `Python files only decrease within the reviewed inventory and two integrated tests`: original Python inventory exceeded its ceiling of 44.

This confirms the older CSS classification failure, not the origin of unrelated current failures.

### Earlier SharedCore had three concrete C++ failures

[Run 41082088447 / job 124153552678](https://github.com/kimjeon-il/Pando/actions/runs/41082088447/job/124153552678), main `0a87cabc5c04fe954f54b934f55f5f43b6f71ffb`, completed compilation, then CTest reported 3 failures out of 9 with exit code 8:

| Test | Existing failure |
|---|---|
| `web_content_codec_tests` | `shared/tests/web-content-codec-tests.cpp:50`: DTO encode/decode round-trip equality assertion. |
| `web_content_command_tests` | `shared/tests/web-content-command-tests.cpp:144`: raw hydro/label annotation equality assertion. |
| `web_object_command_tests` | `shared/tests/web-object-command-tests.cpp:54`: `INVALID_DATE: format`, then assertion. |

These establish earlier Core contract failures. They do not establish that the current many JavaScript failures share the same cause.

### Main P3 success did not include contract execution

[Run 41142687544](https://github.com/kimjeon-il/Pando/actions/runs/41142687544) and [run 41087970887](https://github.com/kimjeon-il/Pando/actions/runs/41087970887), both at main `2b460e40dbc51de2d13b0fe40e11bd4af9e49b75`, had successful planning but skipped `web-contracts`, `browser-regression`, `web-snapshot` and `calculation-performance`. Their overall success must not be presented as a passing contract baseline.

## Release scope and unresolved coverage

The inspected Windows assertion is existing test debt rather than evidence of a newly missing compiler feature. It does not by itself justify adding a native installer build to the P6/Web Pages task. The native installer has **not** been built or launched for this triage.

The current unrelated Core/editing/fixture contract failures must remain disclosed separately. This report does not relabel them as passes or infer blanket prior-debt status. Existing mandatory gate policy remains unchanged.

## Actions performed

Only repository file reads, existing log reads and the requested evidence save were performed. No source code was edited, no tests or builds ran, and no remote state changed. No additional query was performed while saving these two reports.
