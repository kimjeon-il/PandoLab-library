# 프로젝트 공통 LOD 및 수치 DEM 렌더링 통합

> 보고서 ID: DEV-RENDER-LOD-20261110 · 상태: 구현·선정 화면 검증 완료, 검증 범위 축소 후 보고서 확정·원격 보관 대기
> 기준일: 2026-11-10 Asia/Seoul · 작업 브랜치: `work/gis` · `main` 병합·공개 배포 없음

## 현재 판정과 범위

현행 벡터 자료를 사용하는 공통 LOD·카메라·수치 DEM·백엔드 통합과 독립 지도 미리보기 제거를 구현했다. 세계 프로젝트는 WebGL2, WebGL1, Canvas Worker, Canvas2D에서 실제 전체 화면 시나리오를 각각 통과했다. 다만 검사들은 아래에 명시한 서로 다른 수정 단계에서 실행되었다. 독일·한국의 평면·지구본 1·2·4·4.5·8·16·32배와 저장 속성·좌표 해시 보존도 통과했다. 사용자가 검증 확대를 지적한 뒤 추가 검사를 중단했다. 최종 DEM 지연 화면, 동일 자료 핀 전후 성능 비교 및 도구가 차단한 네이티브 3건은 미완료이므로, **구현 반영 완료와 원래 계획의 전체 검증 완료를 구분**한다.

LSIB 입수·등록·교체, 실제 LSIB/NE 대응 구간 비교, `T_NE`·`T_min`의 실측 확정은 이번 범위에서 제외한다. 이번 화면 통과는 현행 자료의 렌더링 검증이며 LSIB 상세도 보정 완료를 뜻하지 않는다. 원본 벡터 좌표·속성·시간 이력·저장 형식을 변경하지 않았다.

## 입력·산출물 식별

| 구분 | 식별값 또는 범위 |
| --- | --- |
| 동기화 후 앱 기준선 | `aa49654795363a52d5ef45a0132ac554ee94394e` |
| 현재 원격 게시 production 커밋 | `afcce77b54117d532de8975ed60dfadcd4c55757` (`work/gis`) |
| 최종 앱 커밋 | `cd2fc6a16` — 저장 정본 identity를 사용하는 지역 fixture 수정 포함, work/gis 게시 |
| 원래 자료 핀 | `f26d0896ab393aa351938637571347baa09ebf71` |
| 기존 수치 DEM Git tree | `23435d594df2bfe4809e6ada9e9c1013a0af396a` |
| 기존 DEM manifest SHA-256 | `e63ac5f18188bd55c8eb032ad0a9e1a6bfb14232b617758ca9076e35771391ff` |
| 기존 DEM assets aggregate SHA-256 | `622a6d272bdda6b507a1f4ba49794fe9ef41aca06f29d8b38e24114caa50d023` |
| 파생 runtime manifest SHA-256 | `51c09ccefc54cf8a58d3571d9c11862f077656474fb2fcc0a9101cc36829fd87` |
| DEM 추가 저장 커밋 | `5dc14820019f78f1322258a752f4b6e248c30c4c` |
| 현행 자료 핀 | `c40af6d237f5db4c8f3688deb4c96e5da00295f4` — 승인받은 원격 역사 보고서 병합을 보존했으며 자료 `work/gis` 원격 일치 확인 |
| 재사용 DEM | 수치 타일 1,280개, 852,527,664바이트. 원문 그대로 재사용, DEM 재생성 없음 |
| 제외된 runtime 자원 | tint 2,433,794바이트. 원본 저장 자료를 삭제하지 않고 runtime 목록·요청·합성에서 제외 |

기존 DEM은 원래 핀의 최상위 `terrain/v0.13.3` Git tree에 있었고 당시 archive index에는 없었다. 기존 자료 저장 도구로 해당 범위만 가져왔다. 직접 저장 차이는 terrain 1,281개 항목이며 다른 runtime 자료 항목은 변경하지 않았다. 원래 핀 이후 자료 브랜치에 이미 있던 보고서 28개 항목은 이 DEM 추가와 구분했다. 디스크 사전 확인은 여유 35,764,416,512바이트, 보수적 추가 사용량 1,705,055,328바이트와 5 GiB 여유 조건을 충족했다. 중간 tar나 전체 자료 복사본은 만들지 않았다.

## 최종 구현과 데이터 흐름

정본 식별·시간 질의 → 유효 원본 콘텐츠와 속성 → `render-lod` 정책 및 공유 위상·중요도 준비 캐시 → 프로젝트 기준 축척 × 상대 확대에 따른 가시 형상 선택 → 공통 표시 메시와 상호작용 경계 → WebGL 또는 공통 Canvas core → 현재 프로젝트·날짜·카메라 프레임 수용으로 연결한다.

- `initialMapBounds`를 고정 프로젝트 범위로 사용하고 최초 화면 맞춤을 상대 1배로 정의한다. 평면·지구본 모두 상대 1~32배와 실수 배율을 사용한다. 날짜 이동과 크기 변경은 카메라의 지리 중심·회전·상대 배율을 유지한다. 투영 전환은 중심과 국소 축척을 최대한 유지한다.
- 공유 원본의 정확한 좌표·연속 변으로 위상 계층을 준비한다. 반올림 키나 자동 스냅으로 경계를 붙이지 않는다. 화면 밖 공유 소유자 관계는 원본 준비 인덱스에 남긴다. 국가·물리 육지·수역은 공통 선택 규칙을 따른다.
- 단순화는 원본 좌표 인덱스를 선택한다. 투영·타일 절단·삼각분할용 계산 정점은 표시 오차로 별도 관리한다. 선택 판정은 정본을 따르고 강조 경계는 화면 LOD에 맞춘다.
- 중요도·위상 준비는 원본 콘텐츠와 알고리즘 버전에 묶어 재사용한다. 확대·날짜 이동마다 원본 전체를 Worker에 다시 보내지 않는다. 측정값과 출처가 제공된 정책에만 `T = max(T_ref × S_ref / S, T_min)`을 활성화한다. 현재 자료에 새 미터 허용치를 임의로 보정하지 않았다.
- 상한이 있는 자료는 실패 시 전체 원본 표시로 우회하지 않는다. 준비 중에는 같은 프로젝트의 이전 수용 프레임을 유지할 수 있으나 새 날짜·배율의 완료로 인정하지 않는다. 프로젝트 교체는 이전 화면을 지운다.
- 원래 Earcut 결과에서 공선 hole bridge의 T-junction을 원본 정점으로 분할하는 네이티브 수정을 추가했다. 취소 checkpoint도 보강했다. 저장 mesh 버전은 유지하고 유효한 기존 사전 계산 자산을 전체 재생성하지 않았다.

DEM은 벡터와 별도로 해상도·가시 타일을 선택한다. 공통 선택 코어가 96 MiB / 수치 픽셀당 12바이트 예산을 적용하여 GPU와 Canvas의 수용 목록을 맞춘다. 원래 고도·수심·저장 음영에서 각 texel의 RGBA8 색상을 계산한 다음 보간한다. `physicalLand` coverage만 육지·바다를 결정하며 DEM 높이 부호나 tint는 해안선을 판정하지 않는다. GPU 텍스처와 CPU 표면은 각 백엔드가 소유한다. Canvas Worker와 Canvas2D는 같은 core와 비동기 프레임 수용 규칙을 사용한다.

## 제거한 경로와 보존한 책임

초기 SVG 육지, 국가 polygon/GPU 미리보기, 사전 채색 지형, Canvas atlas 및 전용 로딩·전환 상태를 제거했다. world bundle 로더·runtime closure·staging·artifact graph는 정본 패킷·메시·라벨·선택적 준비 장면·정본 공유 경계만 소비한다. `build-world-preview`는 정본 패킷만 만드는 `build-world-country-packet`으로 대체했다. 주요 삭제 경로는 [removed-paths.txt](removed-paths.txt)에 기록했다.

잔여 감사에서는 미사용 preview 품질 선택, focus 요청/취소, `qualityPhase`·`desiredCountryMeshQuality`·`countryMeshQuality`, editPreview revision, 초기 준비 API·필드, 저장 미리보기 전달 API, 생산자 없는 성능 지표와 공유 국경 Worker의 preview용 2도 분기도 제거했다. 퇴역 SVG를 전제로 한 검사는 실제 첫 정식 프레임 로딩·게시 검사로 교체했다.

사전 채색 `terrain/v0.12.6` 생성기는 도구끼리 호출할 뿐 현행 수치 DEM 소비자가 없었다. 최종적으로 `build-physical-terrain`, `build-physical-data` wrapper, 독립 C++ 색상 합성·마스크 도구, 전용 검사·CI 및 유일 소비자가 사라진 `resizePhysicalRgb`를 제거했다. 중간에 검토했던 `physical-terrain` 이름 변경과 전용 네이티브 검사 등록은 최종 구현에 남기지 않았다.

보존한 것은 수치 `terrain/v0.13.3`, DEM 고도·음영·gutter·인코딩, 정본 벡터 물리 육지, 수계 생성, 실제 수계 처리에 쓰는 GDAL 원본 읽기, 일반 이미지 리샘플링·WebP 인코딩이다. 편집 작업선, 검수 화면, 배포 검수 preview, Map Toolkit의 참고지도 이미지 기능도 별도 책임으로 유지한다. `legacyPreviewManifest`·`world-preview-v*.json`은 변경하지 않은 자료의 정본 descriptor 저장 이름이며 미리보기 생성·표시 경로가 아니다. 원본 oracle와 역사 스냅샷·자료 바이트는 보존했다.

## 실제 화면·집중 검증 결과

다음 수치는 서로 겹치는 집중 실행의 기록이다. 합산하여 전체 테스트 수나 전체 프로젝트 검증으로 해석하지 않는다.

| 검증 범위 | 관측 결과와 조건 |
| --- | --- |
| 세계 WebGL2 | 전체 시나리오 통과, 약 4.4분. 후속 Canvas 잔여 정리 전의 실행 |
| 세계 WebGL1 | 전체 시나리오 통과, 약 4.3분. 후속 Canvas 잔여 정리 전의 실행 |
| 세계 Canvas Worker | 수정 후 전체 시나리오 통과, 약 5.7분 (`7edb35ec0280357913cf12819798007ff61b4d69` 단계) |
| 세계 Canvas2D | 비동기 수용·gutter 수정 후 전체 시나리오 통과, 약 6.6분 (`afcce77b5` 단계) |
| 세계 공통 시나리오 | 평면·지구본 1·2·4·4.5·8·16·32배, 날짜 왕복, 창 크기 변경, 실제 국가 선택과 동일 LOD 강조. WebGL은 context loss 복구 포함 |
| 최종 Canvas 해안·이음새 픽셀 | Worker·inline 2개 통과. ±4,000m 수치 DEM의 물리 육지 마스크, 해안색 누출 방지, 소수 좌표에서 네 타일 접합, 이전 coverage 위 목표 타일 불투명 색상 확인 |
| 최종 Canvas 날짜·선택 인계 | 비동기 Canvas2D 포함 집중 회귀 4개 통과 |
| 수치 DEM 공통 선택·색상 | 최종 집중 37개 통과. WebGL1/2 실제 shader pixel 16개 통과; 소수 texel 보간은 실제 Canvas2D와 출력 채널 2바이트 이내 차이 확인 |
| GPU base scene | 관련 19개 통과 |
| LOD·카메라 | 초기 집중 94개, 후속 123개 중 122개 통과 후 진행률 사례 수정·해당 11개 재실행 통과. 동일 합성 원본의 인덱스 포함 관계로 정점 단조성 검사 |
| Renderer·Canvas 준비 | 초기 renderer 62개 통과. 후속 111개 중 108개 통과 후 3개 실패를 수정해 해당 3개 재실행 통과 |
| 배포·자산 계약 | frontend closure 18개 및 실제 snapshot 생성 통과. 통합 31개, 합성 실제 staging 2개, 수치 grid/dispatcher 14개 통과 기록 |
| 퇴역 경로 최종 계약 | 114개 중 110개 통과 후 descriptor 오류 기대값·프로젝트 reader 계약·고정 oracle/공간 fixture 실패를 수정해 해당 사례 재실행 통과 |
| WASM | CI `42816087700` 성공. source hash `c7ebf2a5c59a911c1f45ddda9b848b307a45b7baa6c2d4b426919c415f3d9ba3` 일치. 등록 geometry WASM 계약 및 로컬 집중 2개 통과 |
| 독일·한국 | 최초 지역 실행은 표시 이름의 `nameSource`까지 정본 식별과 비교한 fixture 조건에서 실패. 정본 `documentSnapshot` 식별로 수정하고 재검사 중. 지역 완료 판정 없음 |

연속 확대 시 원본 좌표 전송 1회와 이후 `sourceReuses` 증가를 관측했다. 배율마다 가시 국가가 바뀌므로 전체 `keptVertices`의 단순 총합을 단조성의 근거로 쓰지 않았다.

최종 Canvas2D 32배 PNG를 직접 열어 이전 x571/y101의 밝은 가로·세로 이음새가 사라진 것을 확인했다. 한국 주변의 지형·수심·물리 해안선·선택 강조가 실제로 표시된다. 이는 전체 세계 해안과 모든 화면 위치의 무결성을 증명하는 주장은 아니다.

## 실패 원인과 수정 근거

최초 실패 자료도 보존하며 최종 통과 자료로 덮어쓰지 않는다.

| 발견한 문제 | 원인·조치 및 현재 판정 |
| --- | --- |
| Viewer 투영·날짜 카메라 | Viewer 정책의 투영 전환 금지와 날짜 복원의 강제 globe 전환 제거. 세계 실제 시나리오에서 확인 |
| DEM이 로드되지 않음 | 폐기된 `acceptManifest` 세 번째 callback context를 읽어 예외 발생. 실제 서비스→controller 회귀로 재현·수정; 지형/manifest 9개 집중 통과 |
| Canvas core 404 | inline adapter가 해시 경로 전용 Worker 진입점을 import. 공유 factory core로 분리하고 동적 import 자산 목록을 갱신; 실제 frontend snapshot 확인 |
| LOD 준비 30초 초과 | 보호 고리의 불필요한 가변 그래프와 위상 준비 비용. 보호 고리를 불변 공간 장애물로 분리하고 실제 완료 작업량의 유한·단조 진행률 연결 |
| 날짜 이동의 경계 작업 정체 | 이전 pending 작업이 남고 가시 타일 키가 경계 완료 상태에 의존하여 canonical/LOD 선택 반복. 작업 수명 정리와 원본 메시·카메라 기반 키로 수정; 90초 동안 1,662회 경계 요청이 반복된 최초 진단 보존 |
| Canvas 최초 검사 오류 | WebGL 전용 `surfaceDraw`를 Canvas에 요구한 잘못된 검사. 실제 bitmap 스타일·pending/busy·공통 프레임 수용 기준으로 변경 |
| Canvas 초기화 예외 | reset-generation 뒤 국가색만 받은 상태의 자원 알림이 화면 요청 전에 draw를 실행해 `baseLandAlpha` 오류. 해당 세대 화면 요청 이후에만 재그리기; 최초 화면 취소 시 현재 요청 재제출 |
| Canvas culled 슬롯 오류 | 명시적인 `geometry:null`을 누락된 기하로 처리. 화면 밖 LOD 슬롯과 미제공 입력을 구별; 실제 Worker 집중 2개 통과 |
| DEM 목표 타일 정체 | 이전 세계 기본 타일 요청 뒤에서 새 화면 목표 요청이 대기. 목표 밖 활성 요청 선점으로 GPU와 같은 우선순위 적용; 관련 실패 3개 재실행 통과 |
| Canvas 날짜 콘텐츠 불일치 | 객체 참조와 정본 콘텐츠 해시 비교 혼용. `countryMeshContentKey`로 통일; 국가 메시·장면 36개 및 실제 날짜 이동 통과 |
| Canvas2D가 `presenting`에 남음 | 실제 bitmap과 자료는 맞지만 도메인이 Worker만 비동기 ticket으로 등록. 폐기된 동기 Canvas2D 분기 제거; 두 백엔드 ticket 수용 통일 후 전체 Canvas2D 통과 |
| Canvas 소수 픽셀 타일 틈 | 양쪽 저장 gutter를 잘라 `drawImage` 경계 coverage가 배경을 노출. 원래 축척으로 gutter texel까지 그리며 육지 clip·fallback→목표 순서 유지. 실제 픽셀 2개 및 최종 화면 확인 |
| 고정 Web oracle 해시 실패 | CRLF가 아니라 과거 `b4bec4bce` 커밋이 생성기 경로 주석을 6바이트 변경. 기존 Git blob `6f355d0b06e6f286c457a9c4ad286485ba4e1756`을 매니페스트 SHA-256과 대조해 정확히 복구. 검증기·기대 해시 유지 |
| 공간 인덱스 fixture 실패 | 정본 교체 알림→기하 revision 연결이 fixture에 없음. 실제 store callback 계약 연결; 기존 위치 변경 단정 및 불변 자원 재사용 단정 유지. 두 oracle 소비 파일 42개 통과 후 남은 1개만 재실행 통과 |

동경130도 부근의 원자료 특징과 실제 타일 틈은 구별했다. 이후 확인된 틈은 L5 열36의 동경127.2도와 행6의 북위38.8도가 화면 x571.733/y101.311에 투영되는 위치와 정확히 일치했다. 원래 고도·음영 자료를 이동·변경하지 않았다.

초기 합성 배포·artifact batch 123개 중 14개 실패는 fixture 역할·Windows URL 경로·오래된 descriptor 계약에 따른 것이었으며 25개 집중 재시도와 P2 소유권 1개로 해당 실패들을 다시 확인했다. DEM 초기 전체 관련 파일 실행에서 별도 역사 수역 timeout 2개가 나타난 기록도 남긴다. 해당 실행을 전체 통과로 기록하지 않았고 이후 영향받은 지형 사례만 재실행했다.

## 성능·미완료 항목

- 동일 자료 핀·기기·화면의 냉/온 캐시 전후 비교는 **미수행**이다. 초기 globe desktop 기준선은 확보했지만 자료 핀이 달라 그대로 성능 개선 근거로 쓸 수 없다. 첫 정식 표시시간, 프레임 p95/p99, 메시 준비·재사용, 전송량, 캐시 메모리의 최종 비교표가 필요하다. 위 시나리오 실행 시간은 전체 테스트 소요시간이며 렌더링 성능 지표가 아니다.
- 국소 준비 측정은 별도 증거다. physicalLand 548,454점/4,274폴리곤의 수정 전 준비는 source graph 1,694ms, 중요도 1,363ms, 위상 28,103ms, 전체 31,164ms, 파생 115ms였다. 합성 보호 고리 100,000점은 중간 구현에서 1,141ms/249MiB → 119ms/28MiB로 관측했다. 최종 실제 장면의 전후 성능으로 일반화하지 않는다.
- 독일·한국 실제 프로젝트 배율 검사는 최종 통과했다. 최종 DEM 지연·실패 화면의 추가 검사와 모든 요구 장면의 포괄 판정은 미수행이다. 합성 shader·마스크 통과를 이 결과 대신 사용하지 않는다.
- `polygon-mesh-native`, `country-selftest`, 일반 이미지 소스 변경에 필요한 `physical-webp-stream`/`native-map-image` 선택 검사는 명시적 사용자 승인 이후에도 실행 도구의 `PreToolUse CHECK-BUDGET` 정책에 의해 거부되었다. 우회하지 않았으며 미실행 상태다. 이는 사용자의 전체 검사 제한 때문에 생긴 거부가 아니다. geometry WASM CI 성공과 구분한다.
- 관측하지 않은 GPU 수치·세계 전역 픽셀·LSIB 상세도를 통과로 기록하지 않는다. 전체 프로젝트 테스트·전체 GIS 검증·로컬 SDK 설치는 수행하지 않았다.

## 증거 위치와 보관 상태

작업 로그와 JSON은 앱 워크트리의 `.library-data/task-work/project-common-lod/`, 실제 화면 출력은 `test-results/project-common-lod/`와 `test-results/project-common-lod-regions/`에서 생성한다. 후속 실행이 기본 출력 폴더를 재사용하므로 최초 실패와 최종 통과의 별도 보존본을 최종 보관 시 대조해야 한다.

| 근거 | 주요 파일명 |
| --- | --- |
| 자료 원문·저장 | `terrain-archive-evidence.json`, `terrain-package.log`, `terrain-store.log` |
| 공통 LOD·카메라 | `lod-camera-final-tests.log`, `final-lod-camera.log`, `lod-camera-progress.md` |
| DEM 공통 선택·보간·픽셀 | `dem-final-focused.log`, `dem-fractional-pixels.log`, `dem-canvas-pixels.log`, `dem-progress.md` |
| frontend 자산 | `canvas-core-actual-build.json`, `canvas-core-closure-tests.log`, `preview-staging-final.log` |
| 세계 실제 화면 | `final-world-backends.log`, `final-canvas-all.log`, `final-canvas2d-admission.log`; 보존본 `canvas-world-passed.json`, `canvas2d-world-passed.json` 및 1·32배 PNG |
| 날짜·실패 진단 | `date-state-blocked.json`, `date-state-passed.json`, `lod-key-oscillation.json`, `world-webgl2-date-blocked.json`, 보존본 `canvas2d-date-presentation-failure.json` |
| 퇴역 경로·fixture 수정 | `retirement-contracts-final.log`, `frozen-oracle-repair.json`, `frozen-oracle-retry.log`, `frozen-oracle-spatial-retry.log` |
| WASM | `geometry-wasm-ci.log`, CI `42816087700`, 내려받은 불변 artifact |
| 지역 검증 완료 | `regions-final-run.log`, `DEU-regional-lod.json`, `KOR-regional-lod.json`, 지역 CSV와 PNG |

이 README는 외부 라이브러리 `reports/.edits/gis/development/rendering/project-common-lod-2026-11-10`의 **검증 범위를 명시한 확정 보고서**이다. 여기 적은 증거 파일명이 곧 이 보고서 scope의 원격 보관 완료를 뜻하지 않는다. 최종 결과·원본 증거를 정리한 뒤 해당 scope에 대해서만 `--publish-reports`와 `--check-reports`를 완료하고 원격 커밋을 기록해야 한다. 작업 메모에는 공유 라이브러리 main의 별도 미게시 이력이 있어 보고서 게시 전에 처리 상태를 확인해야 한다고 남아 있다. 이를 무단으로 함께 게시하지 않는다.

사용이 끝난 임시 출력은 원본 증거 보관 뒤 정리한다. 작은 Playwright 설정 309바이트와 `.last-run.json` 45바이트, 합계 354논리바이트의 삭제 시도가 실행 도구 정책으로 거부된 기록이 있다. 우회 삭제하지 않았다. 대규모 DEM materialization은 현재 자료 핀·실행 앱이 사용하는 자원이며 폐기용 복사본이 아니다. 최종 정리에서는 남은 출력의 현재 소비자·크기와 실제 삭제·보류 결과를 따로 기록한다.

공통 렌더링의 최종 완료 여부와 LSIB 실측 보정 미수행 상태를 분리하여 보고한다. `main` 및 공개 배포는 변경하지 않는다.


## 검증 범위 최종 결정

사용자의 “검증을 왤케많이해” 지적에 따라 진행 중이던 추가 경계 검사를 중단하고 검증을 더 확장하지 않았다. 추가 독일 경계 32배 1건은 중단 전에 통과했고 한국 추가 경계 사례는 완료 판정하지 않는다. 이 추가 테스트 코드는 커밋하지 않고 제거했다. 기존 전체 지역 배율 2건은 각각 2.7분·2.9분에 통과했다. 추가 DEM 지연 및 최종 성능 비교는 실행하지 않는다. 처음 계획의 미수행 항목을 통과로 바꾸지 않는다. 실제 서버와 진행 검사는 종료했다.

## 보관 경로 승인 및 정리

정식 --publish-reports 명령은 자료 main의 선택 범위 밖 미게시 보고서 커밋 36개 때문에 거부되었다. 사용자는 이번 보고서만 기존 자료 work/gis에 보관·푸시하고 원격 확인하도록 명시 승인했다. 따라서 이번 보고서는 main 정식 게시가 아닌 work/gis 보관으로 완료하며 다른 미게시 이력은 변경하지 않는다. 런타임 자료 핀은 c40af6d237f5db4c8f3688deb4c96e5da00295f4 그대로다.

수정된 앱 최종 커밋은 cd2fc6a169a285a7f9ac711812aa95f15a2ccf8c이며 work/gis에 푸시했다. 추가 검사는 종료했고, 향후 추가 실행을 약속하거나 통과로 기록하지 않는다.

사용 종료된 task scratch 로그·진단자료는 보고서 원본과 해시가 일치한 뒤 중복본을 제거했다. CI WASM 다운로드 3개는 Git에 보존된 assets/wasm 파일과 해시가 일치한 뒤 제거했다. 합계 98개, 논리 4,944,166바이트를 제거했으며 관측된 D: 여유 변화는 +3,698,688바이트다. 차이는 파일시스템 할당·동시 활동의 영향을 받는다. 과거 도구 정책이 삭제를 거부했던 354바이트는 재시도하지 않았다. 현재 핀이 사용하는 수치 DEM 캐시는 유지한다.
실제 화면 검사 출력도 고유 증거를 보고서에 모으고 해시를 대조한 뒤 중복 17개, 5,608,232논리바이트를 제거했다. 이 단계의 D: 여유 변화는 +5,480,448바이트였다. 총 정리량은 115개, 10,552,398논리바이트이며 두 단계의 관측 여유 증가 합계는 9,179,136바이트다. 다른 작업의 저장 잠금이 잠시 있었으나 잠금을 변경하지 않고 작업 종료를 기다렸다.
