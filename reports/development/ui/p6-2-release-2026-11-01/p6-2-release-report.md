# P6-2 · main 통합 · Pages 배포 결과

작성일: 2026-11-01. 시간은 별도 표시가 없으면 UTC다.

## 1. 판정

**P6-2 좁은 화면 기능 검증은 통과했고, 검증한 코드 `35bce38a3444c57bcaf60a9a12d30421e6602740`을 `main`에 fast-forward 통합한 뒤 GitHub Pages에 배포했다.** 배포 후 공개 응답 10개의 실제 바이트와 코드·자료 revision 일치도 확인했다.

다만 **저장소 전체 CI가 통과한 상태는 아니다.** 최종 P3 계약 검사에 1개 실패가 남아 있고, 통합 후 Shared C++ Core 네이티브 CTest에서는 9개 중 3개가 실패했다. 앞선 넓은 계약 실행에서 관찰된 66개 실패도 해결 또는 통과로 처리하지 않았다. Architecture 자동 실행은 아래 시각 기준 상태를 별도로 기록한다.

독립 공개 브라우저 확인에서는 동적 모듈 요청이 `ERR_BLOCKED_BY_CLIENT`로 차단되어 지도 UI의 정상 기동을 확인하지 못했다. 이 관찰은 HTTP 404 또는 제품 회귀를 확정하는 근거가 아니며, CI의 P6-2 기능 통과 및 공개 응답 10개 일치와 구분한다.

- 서비스: [판도연구소](https://kimjeon-il.github.io/Pando/)
- 코드: [35bce38a](https://github.com/kimjeon-il/Pando/commit/35bce38a3444c57bcaf60a9a12d30421e6602740)
- P6-2: [Actions 41266380067](https://github.com/kimjeon-il/Pando/actions/runs/41266380067)
- 배포: [Actions 41266675990](https://github.com/kimjeon-il/Pando/actions/runs/41266675990)

## 2. 통합 및 배포 식별자

| 항목 | 결과 |
|---|---|
| 이전 main | `2b460e40dbc51de2d13b0fe40e11bd4af9e49b75` |
| 최종 main / work/ui | `35bce38a3444c57bcaf60a9a12d30421e6602740` |
| 최종 코드 tree | `d251ffa02c3026b7cdb65dc7e0cd30538a81e357` |
| 통합 방식 | 기존 main을 expected SHA로 확인한 fast-forward, force=false |
| 통합 시각 | 2026-11-01 02:48:28 UTC / 11:48:28 KST |
| 통합 범위 | 이전 main 대비 201 commits ahead, 0 behind, 229 changed files |
| 런타임 자료 저장소 | `kimjeon-il/PandoLab-library-data` |
| 유지한 자료 pin | `139941d8056418547c796068304ba8db3696fe69` |
| Pages 배포 성공 보고 | 2026-11-01 02:50:11.2031132 UTC |
| 공개 응답 검증 완료 | 2026-11-01 02:50:12.0424663 UTC |
| 원격 branch/pin 최종 재조회 | 2026-11-01 02:57:01 UTC |

`main`과 `work/ui`의 원격 ref를 다시 읽어 같은 최종 commit임을 확인했다. 최종 commit의 `config/library-data.json`도 직접 읽어 자료 pin이 유지됨을 확인했다. 자료 저장소의 `work/ui`는 `67e54b893d754b58e58544d24ad3b2c0eed58e02`로 유지됐다. 영구 브랜치는 삭제하지 않았다. 근거: [main-integration.json](main-integration.json), [release-identity.json](release-identity.json).

## 3. P6-2에서 실제로 확인한 기능

환경은 Chromium `151.0.7922.34`, Node `v24.22.1`, 390×844 viewport, `hasTouch=true`, `isMobile=true`, 한국어 locale, Asia/Seoul 시간대다. 시계는 `2026-10-31T00:00:00+09:00`로 고정했다.

최종 코드에서 **하나의 연속 시나리오, 네 단계가 통과**했다. 실행 시간은 약 1.1분이며 retry 없이 완료했다. 페이지 예외 0개, console error 0개다.

| 단계 | 확인한 결과 |
|---|---|
| 첫 지도 표시 | 2026-10 / 2026년 / 현재 월 기준, 초기 로딩 종료, 지도가 표시됐다는 상태와 visible territorial count 254 확인 |
| 한 손가락 이동·두 손가락 확대 | 지구 회전 변화와 globeZoom 증가, dragging 해제, 문서 배율은 1로 유지 |
| 연도 직접 입력 | 좁은 화면의 입력창에 2024를 입력하고 이동 버튼을 터치해 2024-12 / 2024년 / 연말 기준으로 전환 |
| 모바일 환경설정 | 메뉴·설정창 열기, dark 선택과 적용, 실제 지도 배경색·설정 저장·modal 종료 확인 |

이동·확대로 조정한 카메라는 연도 전환과 테마 변경 후 그대로 유지됐다. 각 관찰 지점에서 document/presentation dirty와 Undo/Redo 상태는 모두 false였다.

페이지 가로 넘침이 없고, 검사한 메뉴·타임라인·연도 입력창·설정창은 viewport 안에 있었다. 타임라인 버튼 다섯 개는 각각 최소 40×40px이고, 조작 대상 중앙의 hit test를 통과했다. 지도 도구와 타임라인의 세로 간격도 검사했다. 이 크기 검증을 모든 색상 선택 요소에 확대 적용한 것은 아니다.

최종 screenshot 세 장의 SHA-256을 CI 기록과 대조하고 시각적으로 확인했다. 조작 UI와 폼의 잘림은 발견하지 않았다. 조밀한 지도 라벨의 겹침과 지도 가장자리 라벨의 일부 잘림은 남아 있으며, 라벨 배치 개선이나 지도 문자 전체의 가독성을 인증한 결과로 해석하지 않는다.

근거: [narrow-release.json](narrow-release.json), [narrow-release.log](narrow-release.log), [screenshots-release/manifest.json](screenshots-release/manifest.json).

### 이번에 수정한 실제 기능 결함

첫 실행은 네 기능 단계를 마쳤지만 console error 검증에서 실패했다. 두 번째 터치가 들어와 pinch로 전환할 때 공통 입력 controller가 기존 stroke 취소를 요청했고, Viewer에는 없는 `editingDomain.cancelActiveGesture`를 presentation이 호출하면서 `PL-DRAFT-CANCEL-001`이 발생했다.

`shared/frontend/js/modules/map-input-presentation.js`의 `cancelStroke` 시작에 Viewer guard `if(!editing)return false;`를 추가했다. Editor의 비동기 취소 대기, dispatch, 오류 보고 동작은 유지했다. 이전 presentation으로 실제 실패를 재현한 뒤 기존 14개와 추가 4개를 합친 **18개 입력 계약 테스트**를 통과시켰다. 마지막에는 새 fixture의 EventTarget/CustomEvent를 `globalThis`로 한정해 lint 오류도 수정했다.

근거: [map-input-pinch-red.json](map-input-pinch-red.json), [map-input-pinch-result.json](map-input-pinch-result.json), [map-input-pinch-tests.patch](map-input-pinch-tests.patch), 최종 P6-2 CI.

## 4. 검증 결과와 범위

| 검사 | 결과 | 실행 근거 |
|---|---|---|
| 최종 P6-2 기능 | 1 test / 4 steps 통과, 예외·console error 0 | 35bce38a, run 41266380067 / job 124729942675 |
| 최종 입력 계약 | 18/18 통과, fail/skip 0 | 같은 P6-2 실행 |
| 변경 대상 lint | 통과 | 같은 P6-2 실행 |
| read model | 14/14 통과 | e53f067e, run 41266000828 / job 124728815176 |
| registry / runner | 26/26 통과 | 같은 fixture job |
| 실제 자료의 shared boundary | 8/8 통과, 18 assertions 유지 | e53f067e, run 41266000828 / job 124728815278 |
| P2 source / selection / graph | 49/49 통과 | 84bf8312, run 41265483853 / job 124727448843 |
| 최종 P2 선택 | plan 성공, generate 의도적으로 미선택 | 35bce38a, run 41266380044 |
| Web staging closure | 통과 | 최종 P6-2 및 Pages build |
| App test-fixture staging | 1,131 files / 67,149,412 bytes / 3 entities, verify 통과 | 최종 P6-2 실행 |
| App map-data staging | 1,829 files / 263,395,493 bytes / 258 entities, verify 통과 | 최종 P6-2 실행 |

Read model 변경은 canonical geometry 순서 및 objectRef fixture 정합성 수정이다. Shared-boundary 변경은 archive 입력을 실제 `assets/data` mount에서 읽도록 한 test fixture 경로 수정이며, 해당 8개 테스트나 18개 assertion을 줄이지 않았다.

통합 검사 목록은 최종 코드에서 **unit 파일 432개, browser spec 159개, command 30개**로 해석됐다. 이는 **list-only 계획 결과이며 실행·통과 개수가 아니다**. 계획 단계는 자료를 준비한 P6 job에서 실행하도록 정리하고, merge-base 계산에 필요한 `fetch-depth: 0`을 적용했다.

App 결과는 두 profile의 staging/verify 범위다. 네이티브 설치 파일의 생성·설치·실행 또는 WebView의 실제 UI 동작을 검증한 결과가 아니다.

근거: [read-model-release.log](read-model-release.log), [shared-boundary-final.log](shared-boundary-final.log), [p2-ci-checks.log](p2-ci-checks.log), [integration-plan-release.json](integration-plan-release.json).

## 5. 자료 생성 선택의 수정과 보존

기존 P2 자동 실행 `41264286651`은 unit fixture 변경만으로 입력 변경과 무관한 기존 stale 자료 family 9개를 선택했다. 실제 수정 push가 기존 concurrency 정책으로 이 실행을 02:31:08 UTC에 취소했으며, 해당 실행의 런타임 자료 publication은 없었다.

자동 push이고, 명시 family 선택이나 필요한 WASM 작업이 없으며, 변경이 검증·표현 범위에만 있고 generator/validator closure·입력·출력·외부 원자료 소유 경로와 교차하지 않을 때만 자동 자료 생성을 보류하도록 범위를 제한했다. 수동 실행, 실제 생성 입력 변경, 자료 pin 변경, 필요한 WASM 작업의 선택 동작은 유지했다.

실제 CI에서 무관한 family 선택이 9개에서 0개가 됐다. `needed`, `reasons`, fingerprints, blocked 진단을 지우지 않았고, `--check`가 stale을 발견하는 동작도 유지했다. 총 11개 family의 stale 진단은 남아 있다. **모든 자료가 최신이라고 판정한 것은 아니다.**

코드/WASM의 기록된 source SHA-256은 `fb6f8c79c19b0f786632b3a494c700373c2cf5a1d41f0e68c5a23c87475ea043`이고 자료 pin은 유지했다. 이 identity 관찰과 최신 네이티브/WASM 행동 동등성 검증의 통과는 별개의 주장이다.

근거: [p2-ci-selection.json](p2-ci-selection.json), [p2-cancelled-runtime-audit.json](p2-cancelled-runtime-audit.json), [p2-selection-boundaries.json](p2-selection-boundaries.json), [p2-selection-actual-graph-intersection.json](p2-selection-actual-graph-intersection.json).

## 6. 해결되지 않은 검사

### 최종 P3 계약 검사

최종 코드의 [run 41266380046](https://github.com/kimjeon-il/Pando/actions/runs/41266380046), job `124730140093`은 **85 tests / 84 pass / 1 fail / 0 skip**이다.

남은 실패는 `tests/unit/current-browser-contracts.test.mjs`의 “CSS selects relevant UI checks without C++/GIS build or data generation commands”이다. 오류는 `Unclassified product change: assets/css/features/map-rendering.css`이며, 테스트가 현재 source 경로 대신 예전 public-output 경로를 changed-path fixture로 넘긴다. 해당 test와 selector는 이전 main과 동일하고, 과거 main run `40895207190`에도 같은 오류가 기록돼 있다. 이 사실은 실패 원인의 분류 근거이며, 통과로 바꾸는 근거가 아니다.

### 앞선 넓은 계약 실행

앞선 [run 41265483904](https://github.com/kimjeon-il/Pando/actions/runs/41265483904), job `124727574107`은 다음 수정 push로 cancelled됐다. 취소 전 완료된 네 unit batch에서 **399 tests / 333 pass / 66 fail / 0 skip**이 관찰됐다. workflow cancelled와 내부 테스트 실패를 그대로 남긴다. 최종 P3의 1개 실패와 단순 합산하지 않는다.

읽기전용 source 대조에서 과거 fixture·경로·frozen oracle·mock port 불일치가 확인됐다. 그러나 전체 이전 main을 다시 실행한 baseline은 없고, 일부 주변 product 코드에는 실제 branch 변경이 있다. 따라서 66개 모두의 제품 회귀 가능성이 배제됐다고 주장하지 않는다. 실패 테스트를 삭제하거나 임의로 skip 처리하지 않았다.

근거: [p3-release-contracts.log](p3-release-contracts.log), [p3-contracts-before.log](p3-contracts-before.log), [existing-core-contract-triage.md](existing-core-contract-triage.md), [existing-test-path-triage.md](existing-test-path-triage.md), [existing-packaging-contract-triage.md](existing-packaging-contract-triage.md).

### main 통합 후 자동 검사

[Shared C++ Core run 41266676029](https://github.com/kimjeon-il/Pando/actions/runs/41266676029), job `124730803184`는 failure다. **현재 job의 실제 로그에서 CTest 9개 중 6개 통과, 3개 실패**를 확인했다.

- `web_content_codec_tests`
- `web_content_command_tests`
- `web_object_command_tests` — INVALID_DATE assertion

이 실패 이후 Emscripten/WASM build, 실제 native/WASM month 계약, Worker lifecycle 등 후속 단계는 skipped됐다. **이번 릴리스에서 최신 네이티브·WASM 동등성 및 실패·복구 전체 통과를 주장하지 않는다.**

[Application Architecture run 41266676100](https://github.com/kimjeon-il/Pando/actions/runs/41266676100)의 changes job은 성공했다. checks job `124730992689`는 02:57:32 UTC 조회 당시 진행 중이었다. 진행 중 로그는 아직 제공되지 않아 테스트 실패 수를 추정하지 않았다. 조회 시각과 상세 상태는 [main-automatic-checks.json](main-automatic-checks.json)에 기록한다.

## 7. 사용자가 보류한 두 사례

다음 두 사례는 미해결 상태를 유지했고, 이번 작업에서 재실행하지 않았다.

1. 1953년 7월 전환 완료 대기.
2. 주입한 실패 후 이전 연도 클릭 timeout.

기존 helper와 두 test 본문을 `tests/browser/deferred-builtin-timeline.spec.mjs`로 그대로 옮겨 명시적인 수동 catalog group에 등록했다. immutable `9bc6856f` 기준으로 본문 동일성을 비교했다. 일반 floating-date-controls 테스트는 자동 검사에 남겼다. 이 둘을 삭제하거나 통과로 표시하지 않았고, 자동 통합 계획에서 제외된 것을 list-only로 확인했다.

## 8. Pages 배포와 공개 응답 검증

Pages build job `124730803083`과 deploy job `124731040846`가 모두 성공했다. 배포 전에는 더 최신 main이 존재하면 배포를 거부하는 기존 검사를 통과했다.

배포 artifact는 222,547,646 bytes다. 배포 검증기는 deployment SHA로 cache busting하며 `index.html`, `build-meta.js`, 선택한 current/index/manifest 런타임 JSON을 포함한 **10개 공개 응답의 실제 bytes/SHA-256**을 staged manifest와 비교했다. 출력은 다음과 같다.

```json
{
  "sourceCommit": "35bce38a3444c57bcaf60a9a12d30421e6602740",
  "dataCommit": "139941d8056418547c796068304ba8db3696fe69",
  "checkedFiles": 10
}
```

이 검사는 모든 JavaScript 모듈의 공개 응답이나 실제 브라우저 초기화를 전부 검사하지 않는다. 상세 live.json은 [CI artifact 13068025779](https://github.com/kimjeon-il/Pando/actions/runs/41266675990/artifacts/13068025779)에 있다. 여기의 [pages-live-summary.json](pages-live-summary.json)은 verifier가 출력한 정확한 요약이며, 내려받지 않은 전체 live.json을 재구성한 파일이 아니다.

독립 브라우저에서 페이지 제목·메뉴·canvas element·타임라인은 로딩됐으나 “연결이 복구되면 지도를 다시 불러옵니다.”가 표시됐다. 한 차례 재시도 후에도 같았다. console은 아래 모듈의 dynamic import 실패를 보고했다.

`https://kimjeon-il.github.io/Pando/assets/js/modules/viewer-composition.js?v=0.36.0-build-35bce38a3444`

관찰한 정확한 URL을 직접 열었을 때 브라우저는 `net::ERR_BLOCKED_BY_CLIENT`를 보고했다. 보호 설정이나 네트워크 경로는 변경하지 않았다. 이 환경의 공개 UI 기동 확인은 미완료다. 보고서의 screenshot은 앞의 CI Chromium 에뮬레이션에서 얻은 것이며 공개 Pages 기동 screenshot이 아니다.

근거: [pages-build.log](pages-build.log), [pages-deploy.log](pages-deploy.log), [live-browser-observation.json](live-browser-observation.json).

## 9. 변경 이력과 결과물 보관

| Commit | 내용 |
|---|---|
| fb4f5df5 | P6-2 집중 시나리오·config·workflow와 read-model 검증 workflow |
| e0baee5c | read-model fixture 정합성, 보류 사례의 수동 분리, 누락된 spec 소유 등록 |
| 84bf8312 | Viewer pinch guard, 18개 입력 계약, P2 자동 생성 선택 범위, 통합 계획 위치·history 수정 |
| e53f067e | 실제 data mount를 사용하는 boundary fixture와 고정 자료 CI 검사 |
| 35bce38a | 새 fixture global 한정과 변경 대상 lint gate |

원문 로그, 성공·실패 JSON, patch, 최종 screenshot 및 이 보고서의 보관 범위는 자료 저장소 `reports/development/ui/p6-2-release-2026-11-01/`다. 자료 저장소에서는 runtime generation이나 테스트를 실행하지 않는다. 게시 시 기존 원격 main과 archive index를 다시 읽고, 이 보고서 범위 및 해당 index entry만 추가하며, 다른 runtime tree와 보고서 범위는 보존한다. Git-data API의 blob/tree/commit 및 expected SHA 확인을 사용하며, 네트워크 제약으로 실행하지 못한 repository helper를 실행했다고 기록하지 않는다.

명시적으로 제거한 task-owned 임시 source/test copy 6개와 screenshot bridge 2개는 합계 449,124 logical bytes다. 고유한 근거 파일·부분 source workspace·영구 branch는 보존했다. 파일시스템의 실제 회수량이나 전체 캐시 정리를 이 수치로 주장하지 않는다.

실기기, Safari, WebView, 소프트웨어 키보드·IME, 새 성능 측정, native installer 및 사용자 보류 두 사례는 이번 결과의 인증 범위에 포함되지 않는다.

