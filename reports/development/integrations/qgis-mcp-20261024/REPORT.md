# QGIS MCP / Pando integration

> Report ID: `DEV-QGIS-MCP-001` · status: `verified-development-integration` · map application: `not-applied` · indexed: 2026-10-24  
> Last revised: 2026-10-24  
> App/Web base: `151b5eec6a03728ae01915f9fe7fafd1fd952ce3` plus task working changes on `work/ui`  
> Sources: [QGIS MCP](https://github.com/nkarasiak/qgis-mcp/tree/dae432367fcb2873a151b94c4faaadef2033cf9f), [official OSGeo4W](https://download.osgeo.org/osgeo4w/v2/), local integration evidence below.

## Scope and versions

Installed QGIS LTR 3.44.15-Solothurn at `D:/dev/tools/osgeo4w` and upstream
QGIS MCP 0.15.2, pinned commit `dae432367fcb2873a151b94c4faaadef2033cf9f`.
MCP uses the existing UI Python3.12 runtime; no new training environment or model
copy was created. Codex configuration adds one authenticated loopback server in
compound mode. No token or complete user configuration is included in evidence.

Automatic approval review rejected the native installer, without a specific
reason. The user ran the exact official installer command. The installed runtime
was then verified through the upstream client and MCP stdio protocol. QGIS tool
definitions subsequently appeared in this chat. Native QGIS had exited before
the first direct invocation; restarting the managed session restored it. Codex
direct tool calls then succeeded: system information, layer list, Pando-export
layer add, two-feature query and removal. No cause of the native exit is claimed.

## Method and checks actually run

- Python bridge tests: **8 passed**. Includes CRS/coordinate rejection,
  provenance restoration, output collisions, failed execution/temporary cleanup,
  upstream false-return connection handling and Korean-console UTF-8 output.
- Import-service and Core exchange tests: **12 passed**. The actual editor
  exposed an existing bug: generic lines were passed to a Polygon-only
  validator. The canonical import service now filters Polygon/MultiPolygon,
  matching the committer; regression verifies mixed geometry succeeds while an
  open Polygon is still rejected.
- Scoped ESLint: passed on changed JS/test files.
- MCP stdio initialization: **27 tools**; `system/get_qgis_info` returned QGIS
  3.44.15 through authenticated loopback.
- Actual QGIS loaded the synthetic two-feature input. The first OGR export
  failed on the source QVariantMap; a source-only field converter fixed it.
  Repeating the same export succeeded with nested provenance restored.
- Chromium editor test with the **actual QGIS export**: **1 passed**. File menu,
  GIS wizard, source/new IDs, line coordinates, Polygon XOR/vertex coverage,
  one Undo/Redo, and production GeoJSON bundle export were exercised. Canonical
  Polygon winding/starting vertex can change while shape remains identical.
- Pando's production GeoJSON export reopened in QGIS: **2 features** in WGS84.
- Existing torch **2.14.1+cu126**, CUDA available; `pip check` found no broken
  requirements. No full app rebuild, unrelated full test suite or new hook.

## Results and limits

File exchange is operational. The bridge uses upstream MCP framing/client and
PyQGIS projection/export, and Pando's existing importer/Core commands. Reimport
creates new objects; no implicit live synchronization or replacement by foreign
IDs was introduced. GeoPackage attribute round trips were not tested. Native
QGIS first launch took several minutes during concurrent data-repository work;
an already-running managed session is reused by `start`.

The fixture has synthetic geometry and CC0 software-test provenance. No historical
attribution, border-model accuracy, map reconstruction, Android behavior or model
release is claimed. No pending model was promoted. No main merge/deploy occurred.

## Storage and evidence

`integration-evidence.zip` contains the input, actual QGIS export, actual Pando
export, sanitized verification metadata with SHA256 hashes and the installed
native-package list. It is the retained original integration evidence; task
temporary layers/files are disposable after archival.

The native runtime measured **1,484,933,192 bytes**, upstream source **658,306
bytes**, managed profile **1,016,068 bytes** at measurement. These support current
execution and are retained. Existing Python/Qt native dependencies supplied by
QGIS are its own required runtime; no second model/venv was created.

All **101** downloaded package archives matched setup-manifest sizes/hashes.
After native health verification, the user deleted the download cache,
installer and help logs because automatic approval review blocked deletion.
Removed logical bytes: **409,886,215** (about391MiB). Confirmed all four target
paths absent afterward. D: free was **31,425,691,648 bytes** (about29.3GiB).
Other concurrent cleanup changed free space too, so that total physical change
cannot be attributed to this task. Originals, models and active runtime remain.

Remaining task temporaries: **30,679 bytes** across three ignored exchange files
and two Python bytecode files. The retained archive was CRC/byte/SHA256 verified
against all three originals. Automatic execution review also blocked their scoped
deletion without a specific reason; no other deletion tool was used to bypass it.
These small remnants remain solely because deletion was blocked, not for future
speculative use. They are excluded from the app commit.

## Implementation and edition

Task code: `tools/qgis/`, focused bridge/Core/editor tests and the import-service
Polygon-only validation fix. Reuses the permanent `work/ui` checkout. One fresh
review found the connection false-return bug; it was reproduced, fixed and
retested. No unresolved review finding remained after the converter review.

App implementation commit: `c1efa658cedbf35c0f5d7f65c8e0847f393afc76` on `work/ui`.
Runtime data pin remains `d401965fdbbcb53b54602b1d8736554b8ebc7dda`.

First edition. Subsequent reports must retain this original evidence and state
which additional platform/format checks were actually run.

## 보관된 native 검증 원문

[당시 native 검증 source](native-proof-sources/)는 기존 단위·통합 검사와 별개로 당시 실행 조건과 단언을 보존한 원문이다. 현재 실행 진입점이나 새로 통과한 검사로 해석하지 않는다. 현재 QGIS 설정·프로젝트·SDK와 서비스 자원은 별도로 유지한다.
