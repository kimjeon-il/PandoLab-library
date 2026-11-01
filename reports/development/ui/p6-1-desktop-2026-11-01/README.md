# P6-1 — 데스크톱 기능 확인

## 판정

**요청한 데스크톱 기능 범위 통과.** 실제 Viewer와 고정된 지도 자료, 기존 JS·WASM으로 Chromium 통합 시나리오 **1건을 한 번 실행**했다. 최초 표시, 마우스 이동·확대, 이전/다음 연도, 직접 연도 입력, 어두운/밝은 테마 적용의 **7단계 관측**이 모두 통과했다. 실행 중 브라우저 예외와 콘솔 오류는 각각 **0건**이다.

- 검증 코드: [`9bc6856fa2218f758565acb8670f406c6dab8a41`](https://github.com/kimjeon-il/Pando/commit/9bc6856fa2218f758565acb8670f406c6dab8a41), `work/ui`
- 부모 코드: `aacf43ec4c41948e8c610e30cae56532a80d3f92` — P5-7 검증본
- 실제 CI: [Viewer P6-1 · run 41262009537](https://github.com/kimjeon-il/Pando/actions/runs/41262009537), attempt 1, success
- 원시 관측: [p6-1-functional.json](p6-1-functional.json)
- 실행·소스·화면 해시·자동 CI·정리 근거: [verification.json](verification.json)

## 환경과 재현

| 항목 | 실제 조건 |
| --- | --- |
| 실행 환경 | GitHub Actions Ubuntu 24.04 |
| 브라우저 | Chromium 151.0.7922.34 |
| 도구 | Node v24.22.1, Playwright 1.62.1, pnpm 11.19.0 |
| 화면 | 1280 × 800, 실제 레이아웃 `compact`, 지도 Canvas 1280 × 752 |
| 언어 / 시간대 | `ko-KR` / `Asia/Seoul` |
| 고정 시각 | `2026-10-31T00:00:00+09:00` |
| 실행 설정 | 단일 Chromium, worker 1, retry 0, 단일 spec |
| 지도 자료 pin | `139941d8056418547c796068304ba8db3696fe69` |

검증일은 2026-11-01 UTC다. 연도별 보기의 “올해는 현재 월, 과거는 연말” 동작을 재현하기 위해 브라우저 시각을 위 날짜로 고정했다. 따라서 초기 시점은 `2026-10`이다.

```bash
pnpm exec playwright test --config tests/integration/viewer-functional-p6-1.config.mjs
```

전용 config는 기존 `playwright.config.js`와 `tests/browser/server.mjs`를 재사용한다. 서버가 기존 자료 준비 및 프런트엔드 빌드 경로를 사용하며, 요청 가로채기나 애플리케이션 소스 계측, 인위적인 실패·지연 주입은 사용하지 않았다. `?debug=1`의 기존 읽기 전용 상태 조회 API로 UI 결과와 Core 상태를 대조했다.

Playwright의 실행 결과는 `1 passed (1.4m)`였다. 이 수치는 해당 테스트 실행 전체의 시간이며 지도 전환 지연이나 성능 개선의 측정치로 사용하지 않는다.

## 기능별 결과

| 단계 | 실제 조작과 확인 | 확정 시점 / 화면 표시 | 결과 |
| --- | --- | --- | --- |
| 최초 표시 | 새 브라우저 컨텍스트에서 접속. 초기 지도 표시와 준비 완료, 미리보기 숨김, Canvas·지도 객체 표시 | `2026-10` / 2026년 · 현재 월 기준 | 통과 |
| 카메라 | 지도에서 마우스 100px 드래그 후 휠 -200. 회전 변경·확대 증가와 이동 종료 확인 | 시점 유지 | 통과 |
| 이전 연도 | 이전 연도 버튼 클릭 | `2025-12` / 2025년 · 연말 기준 | 통과 |
| 다음 연도 | 다음 연도 버튼 클릭 | `2026-10` / 2026년 · 현재 월 기준 | 통과 |
| 직접 입력 | 날짜 팝오버에서 연도별 보기 선택, 2024 입력 후 이동 | `2024-12` / 2024년 · 연말 기준, 팝오버 닫힘 | 통과 |
| 어두운 테마 | 환경설정에서 어두운 테마 선택 후 적용 | `2024-12` 유지, dark 저장 및 적용 | 통과 |
| 밝은 테마 | 환경설정에서 밝은 테마 선택 후 적용 | `2024-12` 유지, light 저장 및 적용 | 통과 |

각 단계에서 builtin month, Core `timelineCursor`, `viewerStatus.data-ready`가 기대한 값에 함께 도달했는지 확인했다. 단순히 준비 표시만 돌아오는 상황을 성공으로 판단하지 않았다. 날짜 오류 요소의 실제 `hidden` 속성도 확인했다.

모든 관측에서 `initialMapPresented=true`, `visibleTerritorialCount=254`였고 Canvas의 크기가 0보다 컸다. 이 객체 수는 해당 Viewer의 관측값이며 전체 지도 데이터의 내용 정확성 감사 결과를 의미하지 않는다.

### 카메라와 문서 상태

| 값 | 최초 | 드래그·확대 후 |
| --- | --- | --- |
| Globe rotation | `[-28.780322171285178, -46.46433952490341, 0]` | `[-9.102923969287037, -46.051182267981844, 0]` |
| Globe zoom | `1.25` | `1.6211626083322148` |
| Projection | `globe` | `globe` |

조정 후의 다섯 카메라 필드(projection, globeRotation, globeZoom, flatCenter, flatZoom)는 이후 모든 연도 이동과 테마 변경에서 정확히 같았다. 이 검사는 같은 페이지 안에서의 보존을 확인하며 새로고침 후 복원은 포함하지 않는다.

`dirty`, `documentDirty`, `presentationDirty`, `canUndo`, `canRedo`는 7단계 모두 `false`였다. 탐색·화면 설정 조작이 문서 편집 이력을 만들지 않았음을 확인했다.

### 테마 적용

두 테마 모두 실제 환경설정 UI에서 선택하고 **적용**을 눌렀다. 선택 버튼의 상태, 설정 창 닫힘, 루트 `data-theme`, 저장된 `pandolab-user-preferences.appearance.theme`, 실제 `#map` 배경색을 확인했다.

| 테마 | 저장값 / 루트 값 | 실제 배경색 |
| --- | --- | --- |
| 어두움 | `dark` | `rgb(12, 17, 23)` |
| 밝음 | `light` | `rgb(255, 255, 255)` |

## 화면 확인

화면 3장의 원본 바이트를 CI 로그를 통해 회수하고, CI에서 기록한 SHA-256과 일치하는지 확인한 뒤 직접 열어 검토했다. 독립 검토자도 같은 세 화면을 확인했다.

| 화면 | 시각적 확인 |
| --- | --- |
| [initial.jpg](initial.jpg) | 지구본 지형, 국가 경계, 지명·도시 표시, 상단 메뉴와 하단 조작 버튼이 보임. 2026년 · 현재 월 기준 표시 |
| [dark.jpg](dark.jpg) | 최초보다 확대되고 이동한 지도. 2024년 · 연말 기준. 어두운 주변 배경·메뉴·버튼, 경계 스타일과 금색 도시 표식 적용 |
| [light.jpg](light.jpg) | 어두운 화면과 같은 지도 위치·확대·시점. 흰 배경·메뉴·버튼, 밝은 경계와 파란 도시 표식 적용 |

검토한 화면에 빈 지도, 오류 오버레이, 닫히지 않은 환경설정 창은 없었다.

**가독성 관찰:** 베네룩스·중부 유럽 등 밀집 지역에서 국가·도시 라벨이 가까이 붙거나 겹친다. 해당 축척에서 부분적인 읽기 어려움이 보이지만 검사한 버튼·시점·카메라·테마 조작을 가리지 않는다. 새 회귀라고 판단할 근거는 없으며, 이번 작업에서 라벨 배치 수정이나 추가 검사는 수행하지 않았다.

## 변경 및 실행 범위

애플리케이션 커밋은 다음 **검사 파일 3개만 추가**한다. 제품 코드나 지도 자료, JS·WASM 파일은 변경하지 않았다.

- `tests/integration/viewer-functional-p6-1.spec.mjs`
- `tests/integration/viewer-functional-p6-1.config.mjs`
- `.github/workflows/viewer-functional-p6-1.yml`

기존 `tests/browser/` 경로의 변경은 P3 광범위 브라우저 검사를 선택하므로, 실제 Viewer 통합 시나리오를 기존 `tests/integration/`에 배치하고 전용 config로 실행했다. 기존 CI 분류기나 검사 정책은 수정하지 않았다.

독립 소스 검토에서 1280px 화면의 실제 레이아웃 값이 `compact`인 점을 확인하여 최초의 잘못된 `desktop` 기대값을 CI 실행 전에 수정했다. spec/config 문법, workflow YAML과 내장 Node 스크립트 문법도 확인했다.

### 자동 CI의 실제 선택

| 자동 실행 | 완료된 계획 job | 실행하지 않은 후속 job |
| --- | --- | --- |
| [P1 · 41262009492](https://github.com/kimjeon-il/Pando/actions/runs/41262009492) | plan, native-plan | native-artifact, native-core, wasm-compile, gis-cpp-tools, web-smoke |
| [P3 · 41262009497](https://github.com/kimjeon-il/Pando/actions/runs/41262009497) | plan | web-snapshot, browser-regression, web-contracts, calculation-performance |

기존 push 자동 계획 job과 그 고정된 준비·계획 검사들은 실행됐다. 표의 후속 job들은 실제 완료 상태에서 모두 `skipped`로 확인했다. P6-1에 별도 모바일·성능·광범위 회귀 실행을 추가하지 않았다.

### 기존 Core 산출물 확인

C++·WASM은 다시 빌드하지 않았다. 아래 명령으로 기존 JS·WASM과 해당 소스의 일치를 확인했고 통과했다.

```bash
node tools/package-shared-core-assets.mjs --build-dir shared/frontend/static/wasm --check
```

| 대상 | SHA-256 |
| --- | --- |
| Core source manifest | `fb6f8c79c19b0f786632b3a494c700373c2cf5a1d41f0e68c5a23c87475ea043` |
| JS | `008ce95293a0a291fac586e95e6ec3c9d4684a92a0d552ea60eaca421355b895` |
| WASM | `9671907356ac4b00d1f3bbb10a4a4ed85362b57c8c7d34a530d9ce20e32a70d5` |

자료 준비는 고정 pin의 정식 helper를 사용하고 보고서 전체 복원이나 GIS 재생성은 수행하지 않았다. Chromium·의존성 설치 후 자료 준비 직전에 여유 공간 `90,502,475,776` bytes를 확인했다. 보수적인 추가 공간 `2,080,907,017` bytes와 5 GiB 여유분을 합한 요구량 `7,449,616,137` bytes를 충족했다.

## 범위의 한계

- 이 판정은 한 데스크톱 Chromium 세션의 요청된 정상 기능에 적용한다. 다른 브라우저, 모바일, 네이티브 데스크톱 설치 패키지는 검사하지 않았다.
- 사용자가 유예한 1953년 7월 전환 타임아웃과 실패 주입 후 이전 연도 클릭 타임아웃은 재실행하지 않았다.
- P6-2, 성능 벤치마크, 새로고침 복원 검사는 시작하지 않았다.
- 앱 `main`은 `2b460e40dbc51de2d13b0fe40e11bd4af9e49b75` 그대로이며 main 통합과 배포는 하지 않았다.
- 런타임 자료 pin은 그대로 유지한다. 이번 결과의 보고서 revision과 런타임 pin은 독립적이다.

## 결과 보관과 정리

정본 범위는 `reports/development/ui/p6-1-desktop-2026-11-01/`이다. README, 원시 관측 JSON, 검증 JSON 및 화면 3장을 같은 묶음으로 보관한다.

이 실행 환경의 Git/HTTPS 프록시 연결이 불가능하여 지원되는 GitHub connector의 Git-data API로 해당 보고서 범위와 archive index만 반영한다. 현재 branch head를 비교하는 ref 갱신과 독립적인 원격 바이트·index 확인을 사용한다. 로컬 `--publish-reports`나 `--check-reports` 명령을 실행했다고 주장하지 않는다.

화면 전송용 `transfer.json`은 원시 JSON과 화면 원본의 정확한 일치를 검증한 뒤 삭제했다. 제거한 논리 크기는 **480,113 bytes**, 그 시점에 측정한 파일시스템 여유 공간 증가는 **483,328 bytes**였다. 실패한 artifact 다운로드는 파일을 남기지 않았다. 남은 파일은 코드 변경과 이번 검증의 원본 증거이며, 별도 native build나 SDK를 생성하지 않았다.
