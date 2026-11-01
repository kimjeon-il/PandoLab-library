# 기존 Core·frozen Web 계약 실패 읽기 전용 분류

## 결론 및 상태

**담당 실패군에서 후보에 새로 생긴 제품 회귀를 가리키는 증거를 찾지 못했다.** 관찰한 실패는 기존 main에도 존재하는 테스트 입력, frozen oracle, 예상 DTO 및 필수 테스트 의존성 불일치로 설명된다.

**기존 문제는 해결하지 않았으며 미해결 debt로 유지한다. 전체 baseline을 재실행하지 않았다. 이 문서는 CI 통과 확인이 아니며 통과 건수에 계상하지 않는다.** 릴리스 승인이나 검사 면제 문서도 아니다. 최초 실패 이후 테스트가 도달하지 못한 동작은 검증되지 않았다.

- 저장소: `kimjeon-il/Pando`
- 고정 main: [`2b460e40dbc51de2d13b0fe40e11bd4af9e49b75`](https://github.com/kimjeon-il/Pando/commit/2b460e40dbc51de2d13b0fe40e11bd4af9e49b75)
- 고정 후보: [`e53f067ef37cafc4bd5d4d50e323f8866e7c9833`](https://github.com/kimjeon-il/Pando/commit/e53f067ef37cafc4bd5d4d50e323f8866e7c9833)
- 원본 로그: `p6-2-release-evidence/p3-contracts-before.log`
- Actions run / job: `41265483904` / `124727574107`
- 실행 상태: job 완료 전 취소. 성공한 전체 기준선 결과가 아님.
- 상위 release triage가 전달한 전체 실패 수: **66건**. 이 하위 작업은 전체 다영역 job의 66건을 독립 재집계하지 않았다.
- 이 하위 작업이 로그의 `tests/unit/core-*`·`web-*` 실패 항목에서 분류한 수: **54건**. 아래 서명별 합계는 54이며, 나머지 범위는 별도 release triage 담당이다.

이 문서와 같은 이름의 JSON에 40개 고정 경로의 main/candidate 전체 Git blob SHA, 대표 로그 위치, 세부 원인과 제한을 보존했다. 37개 경로는 blob이 정확히 같고 3개는 전체 파일이 달라 관련 부분을 따로 비교했다.

## 대표 실패군

| 실패 서명 | 담당 로그 항목 수 | 확인한 원인 | 분류 |
|---|---:|---|---|
| 현재 schema 14를 frozen schema 10에 전달 | 22 | `web-full-document-fixture.mjs` 등이 v14 seed를 frozen v10 `prepareProjectForStorage`에 전달한다. Unicode IDs/name/notes, field, generic conversion, label gesture, Web flag 군에서 실제 Core 비교 전 오라클 준비가 실패한다. | 기존 harness |
| 현재 C++ v14에 schema 13 golden load | 1 | `core-document-flag-wasm`이 `web-opaque-flag-contract.json`의 schema 13 project를 직접 load한다. | 기존 golden 입력 |
| 형상 archive 배열 순서 | 15 | `fixture-water:…0005` 행이 seed 마지막에서 canonical ID/version 정렬 첫 번째로 이동한다. 보인 diff는 같은 좌표를 가진 행의 이동이며 좌표 삭제가 아니다. | 비정규 fixture 순서 |
| world typed DTO 추가 필드 | 1 | 실제 `objectRef`, `rendering:{}` 필드가 golden에 없다. main의 serializer도 같은 필드를 출력한다. | 오래된 예상 DTO |
| `TIMELINE_ENTITY` 수계 참조 | 1 | 테스트가 `hydroEdits=[]`만 만들고 해당 수계의 lifetime·geometry binding은 남긴다. | dangling fixture 참조 |
| 기타 아래 세부 원인 | 14 | 불완전한 stub, frozen schema, 오래된 경로 및 범위 밖 packaging assertion | 기존 harness 또는 별도 미해결 |

### 14건의 기타 원인

1. **candidate rollback teardown 1건:** persistence stub에 `queueProject`만 있다. production `dispose()`는 `cancelPending()`도 요구하며 이 요구는 main에도 동일하다.
2. **frozen generic deletion 1건:** 원본 graph에 `markLayerTreeDirty` 제공 의존성이 없어 `original()` 준비 중 실패한다.
3. **draft snapshot 1건:** 실제 결과의 `selectedVertex:null`, `vertexPlacement:false`, `objectVertexEditing:null`을 golden이 누락한다. `activeTool`은 실제·예상 모두 `polygon`이므로 “activate the polygon tool” assertion 문구를 제품 활성화 실패로 해석하면 안 된다.
4. **view-selection 1건:** current schema 3/`objectRef` complex fixture를 frozen schema 1/`entityId` store에 전달해 `TIMELINE_SCHEMA`가 발생한다.
5. **Core prerequisites 3건:** fixture는 `assets/wasm`에 쓰고 canonical loader는 `shared/frontend/static/wasm`을 읽는다. integrity/capability 분기 전에 manifest missing으로 실패한다.
6. **fixed Worker entry 1건:** Node `file:` URL과 mocked Worker를 쓰면서 immutable Worker build metadata를 준비하지 않아 `workerAssetUrl()`이 거부한다.
7. **frozen history/content/selection/writer-clock 3건:** `editable-history-fixture.mjs`가 `layerTree.normalizeLayerFolderState`를 연결하지 않는다. Undo restore가 실패하여 writer-clock token도 예상대로 이전 값으로 돌아가지 않는다.
8. **web-core trace 1건:** frozen 원본 trace는 timeline schema 1/`entityId`, golden은 schema 3/`objectRef`/`propertyBindings`를 기대한다. 두 파일 모두 main에 이미 같은 상태로 있었다.
9. **frozen map presentation 1건:** 현재 저장 seed에는 device viewing 필드인 `layerVisibility`가 없지만 frozen runtime settings는 그 객체에 쓴다.
10. **Windows packaging 1건:** `web-shell-packaged-build`의 custom-protocol assertion은 이 frozen Core/oracle 작업 범위 밖이다. 제품 문제인지 harness 문제인지 확정하지 않았으며 미해결로 남긴다.

## main에도 있었음을 확인한 blob 근거

아래 경로는 두 고정 commit에서 Git blob SHA가 정확히 일치했다. 전체 40개 경로 비교는 JSON의 `file_identities`에 있다.

| 경로 | main·candidate 공통 Git blob SHA |
|---|---|
| `tests/fixtures/portability/web-document-seed.json` | `020a84294bb06afc91bb487e4900abc41a887e9b` |
| `tests/helpers/web-full-document-fixture.mjs` | `66c761fb8c738e209f2ad89b88dd8360f2ca1db6` |
| `tests/fixtures/portability/web-9300609-oracle/assets/js/modules/project-state.js` | `a13a94f3ab320a87520cb6309653adcf44e989e8` |
| `tests/fixtures/portability/web-9300609-oracle/assets/js/modules/timeline-records.js` | `f1353d9fb7d5f0a8d323452d63126d887577cc3f` |
| `tests/fixtures/portability/web-core-contract.json` | `5bd0fa8b48a8041784b0566fb91d1c111b395560` |
| `tests/fixtures/portability/web-opaque-flag-contract.json` | `dcfe8a2a648240199fec7da92e2b7a2e71f6383a` |
| `tests/fixtures/portability/web-timeline-read-model.json` | `c9f67b9ec02269cf580db3c35ee875061e0469ba` |
| `tests/helpers/core-project.mjs` | `02c03f7dee5f39b5540a22e670a82a5a564b2ff1` |
| `tests/helpers/editable-history-fixture.mjs` | `48a33fb0679503254083ddb8f0e083070ec0e59e` |
| `shared/core/src/projectcodec.cpp` | `1864b074a61de665d8a60a45be5871cad84ef6a5` |
| `shared/core/src/timeline-records.cpp` | `95c0366a7c3ff8aaf1f4a1a1483dbb082b890720` |
| `shared/core/src/timeline-resolver.cpp` | `637991f37071d18c6cca4fedffc97b367e0034a7` |
| `shared/core/include/pandoeditor/geometry-types.h` | `073e5cf1288458bdb75a3f2be5bf4184465cb9b8` |
| `shared/frontend/js/modules/geometry-version-store.js` | `ddc53dc60df91d92ce5bd040e5eb41e488876f02` |
| `shared/frontend/js/modules/project-state.js` | `65c6527927ee67b4949647a1565565fc368dfce7` |
| `apps/editor/frontend/js/modules/editing-domain.js` | `bfe8f78433cf91ad4eeb82a8d67f6d4e182cbe1c` |
| `tools/load-node-core.mjs` | `aae7fc7e84c51b67acac83d02358e8a4851736a9` |
| `shared/frontend/js/modules/worker-asset-url.js` | `ebec37f8866564278baf4a608d240a6c4d9614ec` |

검토한 candidate projection, world, flag, service-clock, view-selection, draft, product-mode, prerequisite 테스트도 main과 동일했다.

### 전체 파일이 달랐던 세 경로의 확인 범위

- `shared/frontend/js/modules/core-document-read-model.js`: 차이는 accepted replacement operation 목록에 `core.document-temporal-candidate-adopt`를 추가한 부분뿐이다. 기존 world DTO 투영의 `objectRef`·`rendering`은 main에도 존재한다.
- `shared/wasm/session-bindings.cpp`: `world(const ResolvedWorld&)` serializer 본문은 main·candidate에서 정확히 같았다.
- `shared/frontend/js/modules/project-domain.js`: 전체 파일은 달랐으나 `dispose()`의 `persistence.cancelPending()` 요구는 main에도 동일했다.

형상 정렬은 새 동작이 아니다. C++ `GeometryStore`는 `std::map<GeometryRef,…>`를 보관하며 JS `geometry-version-store.snapshot()`도 ID/version으로 정렬한다. 두 구현과 codec은 main·candidate에서 동일하다. seed가 `fixture-water` 행을 마지막에 둔 것이 raw 배열 deep equality의 직접 원인이다.

## 로그상의 대표 위치

위치는 원본 로그의 1-based 줄 번호이며 새 실행 결과가 아니다.

- 1955, 3837, 5706: 형상 배열 순서 diff
- 2084: persistence stub teardown
- 2098, 2194, 3111, 3678, 3789, 5837, 5891: v14 입력을 frozen v10에서 거부
- 2290: frozen deletion 의존성 누락
- 3078: draft DTO 추가 기본 필드
- 3175: schema 13 flag golden을 현재 C++ v14에서 거부
- 3325: frozen timeline schema 불일치
- 3599: typed world DTO 필드
- 3901, 3923, 3958: prerequisite fixture 경로 불일치
- 3993: immutable Worker metadata 미준비
- 4144: 수계 dangling timeline
- 5307, 5852, 5939: frozen history restore/clock 의존성
- 5333: frozen schema 1 trace와 schema 3 golden
- 5878: frozen map state의 `layerVisibility` 누락
- 5923: 별도 미분류 Windows packaging assertion

## 릴리스 보고에 적용할 제한

- **기존 문제를 수정하거나 무시하지 않았다. 미해결 debt로 공개해야 한다.**
- **전체 baseline 재실행 아님. CI 통과로 계상하지 않음.**
- 취소된 job과 첫 실패 이후 미실행 assertion을 성공한 검증으로 표현하지 않는다.
- 현재 증거는 이 담당 실패 서명을 설명한다. 모든 제품 동작이 올바르거나 다른 릴리스 실패가 없다는 증명은 아니다.
- 제품에 v10/v13 호환 분기나 옛 `entityId` 모델을 되살릴 근거가 아니다.
- 후속으로 허용된다면 current fixture·의존성·예상 DTO를 정렬하고 좁은 관련 검사를 실행할 대상이다. frozen 오라클 원본을 무단으로 현재 스키마에 맞추거나 검증 없이 golden을 덮어쓰는 방식은 피한다.
- 배포 승인·main 통합 여부는 상위 릴리스 작업의 결정이며 이 문서는 별도 승인 또는 gate 면제가 아니다.

## 수행·비수행

기존 로그 읽기와 명시된 두 immutable commit의 GitHub 읽기만 수행했다. 소스 수정, 테스트 실행, WASM/native/data 빌드, workflow 실행, commit/push 등 원격 변경은 하지 않았다. 보류 중인 1953년 7월 및 failure-year 브라우저 사례를 재실행하거나 삭제하지 않았다.

이번 저장 단계에서는 이미 확보한 내용만 Markdown/JSON으로 보존했다. 새로운 소스 조회·수정·테스트는 하지 않았다.

