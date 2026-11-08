# 앱·웹 개발

[전체 주제](../README.md)

원문 ID·작성일·검증 상태를 기준으로 읽습니다. 관련 첨부는 각 작업 묶음에 보관합니다.

[ci](ci/) · [integrations](integrations/) · [native](native/) · [performance](performance/) · [releases](releases/) · [rendering](rendering/) · [storage](storage/) · [ui](ui/)

| 문서 | ID | 기록 날짜 | 상태 |
| --- | --- | --- | --- |
| [코드 변경과 검사 자동 선택·실행 연동](ci/check-automation-2026-10-19.md) | UI-CHECK-AUTOMATION-20261019 | 2026-10-20 | `local-validation / known-product-failures / unpublished` |
| [P2 — C++ 생성물 자동화 실행·검증](ci/p2-generated-artifact-automation-2026-10-14.md) | DEV-073 | 2026-10-14 | `implemented` |
| [P4 — GIS Python 격리·원격 검증](ci/p4-python-gis-isolation-2026-10-14.md) | DEV-074 | 2026-10-14 | `implemented` |
| [P5-6 — 공통 C++ 계산 소유권·앱/웹 종료 검증](ci/p5-6-final-verification-2026-10-15.md) | DEV-075 | 2026-10-15 | `implemented` |
| [검사·검증 현재 계약 검수 — 2026-10-06](ci/validation-audit.md) | DEV-001 | 2026-10-06 | `historical-record` |
| [QGIS MCP / Pando integration](integrations/qgis-mcp-20261024/REPORT.md) | DEV-QGIS-MCP-001 |  | 원문 참조 |
| [라이브러리 외부 분리 — 2026-10-21](library-migration-2026-10-21.md) | DEV-LIBRARY-MIGRATION-20261021 |  | published / web-live-verified / native-unverified |
| [편집 라이브러리 UI·네이티브 코드 검토](native/editable-library-editor-native-review-2026-10-21.md) | UI-LIBRARY-REVIEW-20261021 | 2026-10-21 | `reviewed-important-findings-resolved / native-workflow-unverified` |
| [P1 — 원격 개발환경 표준화·검증](native/p1-remote-development-validation-2026-10-14.md) | DEV-071 | 2026-10-14 | `implemented` |
| [P0 — 원격 개발 체계·도구 의존성·성능 기준 조사](native/remote-toolchain-p0-audit-2026-10-14.md) | DEV-070 | 2026-10-14 | `investigating` |
| [P5-5 공유 국경선 렌더링 패킷 성능 검증](p5-shared-border-performance.md) |  |  | 원문 참조 |
| [공유 국경선 선분 공간 인덱스 압축: JS 힙 165MiB 절감 A/B 검증](performance/boundary-spatial-index-packed-2026-10-17.md) | OBJ-089 | 2026-10-17 | `verified-web-paired` |
| [객체 시점 resolveWorld 단일화 검증](performance/objects-timeline-cursor-reuse-2026-10-17.md) | OBJ-083 | 2026-10-17 | `verified-web-diagnostics` |
| [P6–P9 구현·검증 진행 기록](performance/p6-p9-execution-2026-10-16.md) | DEV-076 | 2026-10-16 | `investigating` |
| [기준 코드·기존 계측 자산 통합 검토](performance/performance-baseline-consolidation-2026-10-17.md) | PERF-P0-001 | 2026-10-17 | `verified-source-and-focused-ci` |
| [편집 포트 제한과 WebGL 면 준비 시간 초과 수정](performance/port-mesh-worker-fixes-2026-10-20.md) | UI-PORT-MESH-20261020 | 2026-10-20 | `local-validation / native-unverified / unpublished` |
| [main·지리 판정 실험 정확성 및 제한 성능 비교](performance/predicate-comparison-2026-10-18.md) | PERF-PREDICATE-20261018 |  | verified-bounded-comparison / keep-main · 지도 반영: not-applicable |
| [러시아 상세 형상 편집: 구현 및 검증 기록](performance/russia-edit-responsiveness.md) | DEV-002 | 2026-09-16 | `historical-record` |
| [공통 C++·WASM 코어와 앱 시작 경로 개선 — 진행 기록](performance/shared-core-startup-implementation-2026-10-12.md) | DEV-066 | 2026-10-12 | `investigating` |
| [1989년 소련 대형 경계 편집 준비 지연 선분 생성 최적화](performance/soviet-boundary-preparation-2026-10-16.md) | DEV-085 | 2026-10-16 | `verified-web-ci` |
| [C++ 접촉 변환 캐시 수명 단축 및 Worker JS 23.8MiB 절감](performance/soviet-contact-wire-lifetime-2026-10-17.md) | OBJ-094 | 2026-10-17 | `verified-web-paired-and-12cycle` |
| [소련 Core 후보 준비: 135초 WASM 동기 실행 미반환 및 C++ 함수별 계측](performance/soviet-core-candidate-bottleneck-2026-10-18.md) | OBJ-097 | 2026-10-18 | `verified-root-cause / geometryContains-47s-per-SSR` |
| [1989년 소련 초기 준비시간·메모리 원인 조사](performance/soviet-initialization-memory-2026-10-16.md) | DEV-083 | 2026-10-16 | `verified-web-diagnostics` |
| [현행 main 동일 소스 소련 12회 왕복 메모리 검증](performance/soviet-main-12cycle-memory-2026-10-17.md) | OBJ-087 | 2026-10-17 | `verified-web-diagnostics` |
| [1989년 소련 편집 메모리·반복 회귀 검증](performance/soviet-memory-lifecycle-regression-2026-10-16.md) | DEV-086 | 2026-10-16 | `verified-web-ci-with-observability-limits` |
| [소련 시점 메모리 소유권 계측](performance/soviet-memory-owner-attribution-2026-10-16.md) | OBJ-082 | 2026-10-17 | `verified-web-diagnostics` |
| [소련 편집·시점 왕복 Worker/WASM 메모리 계측](performance/soviet-memory-retention-roundtrip-2026-10-17.md) | OBJ-084 | 2026-10-17 | `verified-web-diagnostics` |
| [1989년 소련 지도 이동 WebGL2 메시·GPU 업로드 재사용 검증](performance/soviet-pan-gpu-reuse-2026-10-16.md) | DEV-081 | 2026-10-16 | `verified-web-only` |
| [국가별 준비 자료와 C++ 전달 캐시 참조 소유권 교차 조사](performance/soviet-prepared-source-owners-2026-10-17.md) | OBJ-093 | 2026-10-17 | `verified-3-isolated-gc-orders` |
| [국가별 원본 선분 링 메타데이터 공유 및 Worker 6.9MiB 절감](performance/soviet-prepared-source-row-compact-2026-10-17.md) | OBJ-095 | 2026-10-17 | `verified-web-paired-and-12cycle` |
| [소련 미리보기 build 60초 지연 원인 추적](performance/soviet-preview-build-attribution-2026-10-17.md) | OBJ-085 | 2026-10-17 | `verified-web-diagnostics` |
| [소련 실제 편집·취소·확정 게이트 및 Core 30초 병목 특정](performance/soviet-real-edit-cpu-reference-2026-10-17.md) | OBJ-096 | 2026-10-17 | `worker-move-verified / core-prepare-blocked` |
| [1989년 소련 WebGL 선택 강조선 및 빈 상호작용 패스 최적화](performance/soviet-render-hotpaths-2026-10-16.md) | DEV-082 | 2026-10-16 | `verified-web` |
| [렌더링 선분 지연 생성 및 Worker 메모리 61MiB 추가 절감](performance/soviet-renderable-on-demand-2026-10-17.md) | OBJ-090 | 2026-10-17 | `verified-web-paired-and-12cycle` |
| [공유 국경선 잔여 메모리 소유 구조 3개 GC 순서별 분해](performance/soviet-retained-owner-graph-2026-10-17.md) | OBJ-091 | 2026-10-17 | `verified-isolated-chromium` |
| [공유 국경선 Worker 메모리 실제 유지 소유자 분석](performance/soviet-shared-border-retained-owners-2026-10-17.md) | OBJ-088 | 2026-10-17 | `verified-web-diagnostics` |
| [단일 접촉 공유 경계 레코드 압축 및 Worker 6MiB 절감](performance/soviet-singleton-edge-2026-10-17.md) | OBJ-092 | 2026-10-17 | `verified-web-paired-and-12cycle` |
| [고배율 지형 전환 지연의 재현과 수정](performance/terrain-interaction-latency-2026-10-21.md) | UI-TERRAIN-LATENCY-20261021 | 2026-10-21 | `local-web-verified / app-unverified / unpublished` |
| [작업 브랜치의 미통합 변경 전체 반영](releases/all-branch-integration-2026-10-20.md) | DEV-ALL-BRANCH-20261020 | 2026-10-20 | `integrated-with-validation-exception` |
| [10월 21일 작업 브랜치의 main 통합](releases/all-branch-integration-2026-10-21.md) | DEV-ALL-BRANCH-20261021 | 2026-10-21 | `integrated / release-followup-linked` |
| [미병합 커밋 main 통합](releases/all-branches-main-integration-2026-10-21.md) | DEV-MAIN-20261021 |  | integrated / focused-verification |
| [UI·GIS 전체 변경 main 통합 검증 — 2026-10-23](releases/all-branches-main-integration-2026-10-23.md) | DEV-MAIN-20261023 |  | integrated-local / focused-verification · 원격 게시: 이 기록 작성 시 대기 |
| [Canvas 지구본 지연 수정과 배포 검증](releases/canvas-globe-release-2026-10-19.md) | UI-CANVAS-GLOBE-20261019 | 2026-10-19 | `released / windows-startup-verified / android-unverified` |
| [국경선 마스크 수정 배포 — 2026-10-22](releases/country-border-release-2026-10-22.md) |  |  | 원문 참조 |
| [독립 라이브러리 게시 코드 검토](releases/editable-library-publication-review-2026-10-21.md) | UI-LIBRARY-PUBLISH-REVIEW-20261021 | 2026-10-21 | `changes-requested / live-publication-unverified` |
| [앱 평면 편집 변경 게시와 작업 브랜치 전파](releases/editor-flat-release-2026-10-20.md) | UI-EDITOR-FLAT-RELEASE-20261020 | 2026-10-20 | `pages-live-verified / branches-propagated / windows-native-verified / android-unverified` |
| [통합 main의 원격 게시와 Windows 실행 파일 갱신](releases/integrated-release-2026-10-21.md) | DEV-INTEGRATED-RELEASE-20261021 | 2026-10-21 | `pages-live-verified / windows-native-verified / separate-ci-failure` |
| [국가 자료·편집 라이브러리 main 병합 기록](releases/library-korea-main-merge-2026-10-21.md) | UI-GIS-MERGE-20261021 |  | merged-locally / followup-deferred |
| [지도 표시·UI 검사 정리와 웹·Windows 게시 검증](releases/map-scale-release-2026-10-20.md) | UI-MAP-SCALE-RELEASE-20261020 | 2026-10-20 | `pages-live-verified / windows-native-verified / separate-ci-failures` |
| [객체 워크트리 main 동기화와 미커밋 작업 복원](releases/objects-main-sync-2026-10-21.md) | OBJ-MAIN-SYNC-20261021 |  | main-synchronized / local-wip-restored |
| [프로젝트 생성·공통 보기 변경 커밋과 Pages 배포](releases/project-creation-release-2026-10-19.md) | UI-PROJECT-RELEASE-20261019 | 2026-10-19 | `published / focused-verified / android-device-unverified` |
| [남은 작업 브랜치의 main 통합](releases/remaining-branch-integration-2026-10-20.md) | DEV-REMAINING-BRANCH-20261020 | 2026-10-20 | `integrated / remote-verified / docs-only` |
| [웹·앱 저장소 통합 — 4단계](releases/repository-unification-stage4-2026-10-12.md) | DEV-065 | 2026-10-12 | `historical-record` |
| [Web·App 저장소 통합 — 5단계 검증 (2026-10-12)](releases/repository-unification-stage5-2026-10-12.md) |  |  | 원문 참조 |
| [공통 지도 변경 배포와 작업 브랜치 통합](releases/shared-viewing-release-sync-2026-10-20.md) | UI-RELEASE-SYNC-20261020 | 2026-10-20 | `pages-content-verified / ci-failures-recorded / native-unverified` |
| [지형 전환 지연 수정의 main 반영과 웹·앱 게시 검증](releases/terrain-interaction-release-2026-10-21.md) | UI-TERRAIN-RELEASE-20261021 | 2026-10-21 | `pages-live-verified / windows-native-verified` |
| [웹·앱 분리 배포 및 공개 사이트 검증](releases/web-app-product-release-2026-10-18.md) | UI-PRODUCT-RELEASE-20261018 | 2026-10-18 | `pages-live-verified / native-device-unverified` |
| [웹 날짜 도구 배포와 상설 작업 브랜치 전파](releases/web-date-tool-release-2026-10-22.md) | UI-DATE-RELEASE-20261022 |  | pages-live-verified / task-propagated / objects-core-prerequisite-blocked · 지도 반영: not-applicable |
| [하위 객체의 해안 점선 잔존 수정](rendering/child-coast-boundary-2026-10-19.md) | UI-CHILD-COAST-20261019 | 2026-10-19 | `released-in-followup / see UI-CANVAS-GLOBE-20261019` |
| [해안 점선 재발·수정 유실 여부와 경계 규칙 분기 조사](rendering/child-coast-recurrence-audit-2026-10-19.md) | UI-COAST-RECURRENCE-20261019 | 2026-10-19 | `deployment-parity-confirmed / recurrence-not-reproduced / not-fixed` |
| [하위 객체의 지형 표시 누락·지연 조사와 수정](rendering/child-terrain-readiness-2026-10-19.md) | UI-CHILD-TERRAIN-20261019 | 2026-10-19 | `released-in-followup / see UI-CANVAS-GLOBE-20261019` |
| [북중 국경 선 굵기 차이 진단 — 2026-10-22](rendering/north-korea-border-stroke-2026-10-22.md) |  |  | 원문 참조 |
| [보고서 이관 기록](storage/MIGRATION.md) |  |  | 원문 참조 |
| [데이터 버전 관리 — 과거 단계 보고서 통합 요약](storage/archive/data-versioning/README.md) |  |  | 원문 참조 |
| [판도편집기 조사·검증 보고서](storage/branch-originals/gis/README.md) | DEV-MAIN-20261021 |  | 원문 참조 |
| [10월 21일 작업 브랜치의 main 통합](storage/branch-originals/gis/development/testing/all-branch-integration-2026-10-21.md) | DEV-ALL-BRANCH-20261021 |  | integrated / focused-verified / local-only |
| [미병합 커밋 main 통합](storage/branch-originals/gis/development/testing/all-branches-main-integration-2026-10-21.md) | DEV-MAIN-20261021 |  | integrated / focused-verification |
| [gis 브랜치의 잔여 파일 정리](storage/branch-originals/gis/development/testing/branch-residue-cleanup-2026-10-21.md) | DEV-CLEANUP-GIS-20261021 |  | local-focused-verified / uncommitted / unpublished |
| [편집 상태와 취소·적용·실행 취소 구현 검증](storage/branch-originals/gis/development/testing/editing-state-recovery-2026-10-18.md) | UI-EDIT-20261018 |  | deployed-web-ci-incomplete |
| [웹 열람 UI 공유 누락 조사와 복원 검증](storage/branch-originals/gis/development/testing/viewing-ui-reuse-repair-2026-10-18.md) | UI-VIEWING-REPAIR-20261018 |  | verified-web-release / native-unverified |
| [웹 열람·앱 편집 분리 배포 검증](storage/branch-originals/gis/development/testing/web-app-product-release-2026-10-18.md) | UI-PRODUCT-RELEASE-20261018 |  | pages-live-verified / native-device-unverified |
| [웹 열람·앱 편집 분리와 휴대폰 가로 화면 검증](storage/branch-originals/gis/development/testing/web-app-product-split-2026-10-18.md) | UI-PRODUCT-SPLIT-20261018 |  | focused-verified / native-device-unverified |
| [판도편집기 조사·검증 보고서](storage/branch-originals/objects/README.md) | DEV-MAIN-20261021 |  | 원문 참조 |
| [라이브러리 외부 분리 — 2026-10-21](storage/branch-originals/objects/development/library-migration-2026-10-21.md) |  |  | 자료 원격 보존 후 코드 참조 전환 중. 배포 완료나 네이티브 실행 검증을 주장하지 않는다. |
| [10월 21일 작업 브랜치의 main 통합](storage/branch-originals/objects/development/testing/all-branch-integration-2026-10-21.md) | DEV-ALL-BRANCH-20261021 |  | integrated / focused-verified / local-only |
| [미병합 커밋 main 통합](storage/branch-originals/objects/development/testing/all-branches-main-integration-2026-10-21.md) | DEV-MAIN-20261021 |  | integrated / focused-verification |
| [objects 브랜치의 잔여 파일 정리](storage/branch-originals/objects/development/testing/branch-residue-cleanup-2026-10-21.md) | DEV-CLEANUP-OBJECTS-20261021 |  | local-focused-verified / uncommitted / unpublished |
| [편집 상태와 취소·적용·실행 취소 구현 검증](storage/branch-originals/objects/development/testing/editing-state-recovery-2026-10-18.md) | UI-EDIT-20261018 |  | deployed-web-ci-incomplete |
| [웹 열람 UI 공유 누락 조사와 복원 검증](storage/branch-originals/objects/development/testing/viewing-ui-reuse-repair-2026-10-18.md) | UI-VIEWING-REPAIR-20261018 |  | verified-web-release / native-unverified |
| [웹 열람·앱 편집 분리 배포 검증](storage/branch-originals/objects/development/testing/web-app-product-release-2026-10-18.md) | UI-PRODUCT-RELEASE-20261018 |  | pages-live-verified / native-device-unverified |
| [웹 열람·앱 편집 분리와 휴대폰 가로 화면 검증](storage/branch-originals/objects/development/testing/web-app-product-split-2026-10-18.md) | UI-PRODUCT-SPLIT-20261018 |  | focused-verified / native-device-unverified |
| [판도편집기 조사·검증 보고서](storage/branch-originals/places/README.md) | DEV-MAIN-20261021 |  | 원문 참조 |
| [10월 21일 작업 브랜치의 main 통합](storage/branch-originals/places/development/testing/all-branch-integration-2026-10-21.md) | DEV-ALL-BRANCH-20261021 |  | integrated / focused-verified / local-only |
| [미병합 커밋 main 통합](storage/branch-originals/places/development/testing/all-branches-main-integration-2026-10-21.md) | DEV-MAIN-20261021 |  | integrated / focused-verification |
| [places 브랜치의 잔여 파일 정리](storage/branch-originals/places/development/testing/branch-residue-cleanup-2026-10-21.md) | DEV-CLEANUP-PLACES-20261021 |  | local-focused-verified / uncommitted / unpublished |
| [편집 상태와 취소·적용·실행 취소 구현 검증](storage/branch-originals/places/development/testing/editing-state-recovery-2026-10-18.md) | UI-EDIT-20261018 |  | deployed-web-ci-incomplete |
| [웹 열람 UI 공유 누락 조사와 복원 검증](storage/branch-originals/places/development/testing/viewing-ui-reuse-repair-2026-10-18.md) | UI-VIEWING-REPAIR-20261018 |  | verified-web-release / native-unverified |
| [웹 열람·앱 편집 분리 배포 검증](storage/branch-originals/places/development/testing/web-app-product-release-2026-10-18.md) | UI-PRODUCT-RELEASE-20261018 |  | pages-live-verified / native-device-unverified |
| [웹 열람·앱 편집 분리와 휴대폰 가로 화면 검증](storage/branch-originals/places/development/testing/web-app-product-split-2026-10-18.md) | UI-PRODUCT-SPLIT-20261018 |  | focused-verified / native-device-unverified |
| [main 잔여 파일·구형 테스트·생성 자산 목록 정리](storage/branch-residue-cleanup-2026-10-21.md) | DEV-CLEANUP-MAIN-20261021 | 2026-10-21 | `local-focused-verified / uncommitted / unpublished` |
| [Country lineage storage 실행 기록](storage/country-lineage-storage.md) | DEV-010 | 2026-10-06 | `historical-record` |
| [통합 저장소 현행 파일 정리 — 비활성 앱 워크플로](storage/current-file-cleanup-2026-10-13.md) | DEV-067 | 2026-10-13 | `historical-record` |
| [앱 평면 편집 집중과 경위선·지구본 장식 제거](storage/editor-flat-cleanup-2026-10-20.md) | UI-EDITOR-FLAT-20261020 | 2026-10-20 | `local-focused-verified / release-followup-linked` |
| [앱 편집 집중과 프로젝트 저장 범위 변경 검증](storage/editor-focus-project-storage-2026-10-19.md) | UI-EDITOR-FOCUS-20261019 | 2026-10-19 | `focused-verified / android-device-unverified` |
| [Git 대용량 이력 정리 — 격리 검증 및 PR 참조 제약](storage/git-history-readonly-audit-2026-10-13.md) | DEV-069 | 2026-10-13 | `historical-record` |
| [미사용 세계지도 구버전 대용량 자산 정리 — 의존성 검증](storage/legacy-world-asset-retirement-2026-10-13.md) | DEV-068 | 2026-10-13 | `historical-record` |
| [판도편집기 조사·검증 보고서](storage/organization-original-indexes/README.md) | DEV-MAIN-20261023 |  | 원문 참조 |
| [새 프로젝트 생성 통합과 보기 상태 저장 분리](storage/project-creation-storage-2026-10-19.md) | UI-PROJECT-CREATION-20261019 | 2026-10-19 | `focused-verified / baseline-test-failures / android-device-unverified` |
| [웹·앱 저장소 파일 및 Git 이력 정리 — 1~3단계](storage/repository-cleanup-2026-10-12.md) | DEV-064 | 2026-10-12 | `historical-record` |
| [공통 지도·열람 구조 정리 구현과 검증](storage/shared-viewing-cleanup-2026-10-19.md) | UI-SHARED-VIEWING-20261019 | 2026-10-19 | `local-validation / native-unverified / unpublished` |
| [국가 존속기간과 지도 자료 제공 기간 분리](ui/country-lifetime-2026-10-21.md) | OBJ-MAIN-SYNC-20261021 |  | web-app-core-verified |
| [편집 가능한 라이브러리 구현 현황](ui/editable-library-2026-10-21.md) | UI-LIBRARY-20261021 |  | implementation-partial / app-unverified |
| [편집기 앱 작업표시줄의 시점 이동 제거](ui/editor-status-timeline-removal-2026-10-19.md) | UI-EDITOR-STATUS-TIME-20261019 | 2026-10-19 | `focused-verified / android-device-unverified` |
| [객체가 없는 시점의 육지 소실 원인 조사](ui/empty-time-land-mask-2026-10-19.md) | UI-EMPTY-TIME-LAND-20261019 | 2026-10-19 | `reproduced / cause-confirmed / not-fixed / native-unverified` |
| [기본 세계 역사 타임라인 검증](ui/historical-world-timeline-validation.md) | DEV-003 | 2026-10-12 | `historical-record` |
| [웹·앱 독자 규칙 추가 조사](ui/independent-view-policy-audit-2026-10-19.md) | UI-POLICY-AUDIT-20261019 | 2026-10-19 | `historical-audit / follow-up-linked` |
| [Info tab v9 — implementation and visual verification](ui/info-tab-v9-visual-validation-2026-10-06.md) | DEV-072 | 2026-10-06 | `historical-record` |
| [초기 지도 요소의 표시 시차와 새 프로젝트의 흰 화면 조사](ui/initial-map-and-project-transition-2026-10-21.md) | UI-INITIAL-MAP-20261021 | 2026-10-21 | `historical-record / follow-up-linked` |
| [초기 지도 배경과 새 프로젝트 전환의 표시 연속성 수정](ui/initial-map-continuity-2026-10-21.md) | UI-INITIAL-MAP-FIX-20261021 | 2026-10-21 | `local-verified / release-followup-linked` |
| [지도 배율별 품질과 표시 준비 상태](ui/map-scale-readiness-2026-10-20.md) | UI-MAP-SCALE-20261020 | 2026-10-20 | `focused-verified / native-webview2-verified / unpublished` |
| [웹·앱 불필요 기능 정리와 공통 소유자 유지 검증](ui/product-pruning-2026-10-19.md) | UI-PRODUCT-PRUNING-20261019 | 2026-10-19 | `focused-verified / android-device-unverified` |
| [참고 이미지 UI — 최신 work/ui 통합 검증](ui/reference-image-ui-integration-2026-10-19.md) | DEV-REF-UI-SYNC-20261019 | 2026-10-19 | `focused-verified / existing-base-check-failure / native-unverified` |
| [참고 이미지 UI P5 — 회귀 검증과 조작 영역 수정](ui/reference-image-ui-p5-2026-10-18.md) | DEV-REF-UI-P5-20261018 | 2026-10-19 | `historical-feature-verification / follow-up-linked` |
| [웹·앱 호버 깃발과 경계 규칙 재점검](ui/shared-map-rule-parity-2026-10-19.md) | UI-MAP-PARITY-20261019 | 2026-10-19 | `focused-verified / published / native-unverified` |
| [출력 외 전부 공유 기준의 추가 조사·독립 코드 잔존](ui/shared-output-audit-2026-10-18.md) | UI-SHARING-AUDIT-20261018 | 2026-10-18 | `audit-complete / follow-up-linked` |
| [웹·앱 공통 소유자 통합 및 검증 · 확대/축소 UI 회귀 수정](ui/shared-output-refactor-2026-10-19.md) | UI-SHARING-REFACTOR-20261019 | 2026-10-19 | `focused-verified / published / native-unverified` |
| [웹·앱 공통 열람 규칙 연결 수정](ui/shared-view-policy-fix-2026-10-19.md) | UI-POLICY-FIX-20261019 | 2026-10-19 | `focused-verified / published / existing-ci-failures` |
| [보기 메뉴의 내장 자료 구분 제거](ui/source-visibility-menu-2026-10-19.md) | UI-SOURCE-VISIBILITY-20261019 | 2026-10-19 | `released-in-followup / see UI-CANVAS-GLOBE-20261019` |
| [UI 독자 규칙 통합 P0 — 구조·상태·회귀 기준 조사](ui/ui-convergence-p0-audit-2026-10-20.md) | UI-CONVERGENCE-P0-20261020 | 2026-10-20 | `source-audited / focused-runtime-baseline-not-rerun` |
| [상위·하위·지방 객체의 표시 규칙 통합](ui/unified-object-display-2026-10-19.md) | UI-OBJECT-DISPLAY-20261019 | 2026-10-19 | `focused-verified / android-device-unverified` |
| [웹 열람 UI 공유 누락 조사와 복원](ui/viewing-ui-reuse-repair-2026-10-18.md) | UI-VIEWING-REPAIR-20261018 | 2026-10-18 | `verified-web-release / native-unverified` |
| [웹 열람·앱 편집 분리와 휴대폰 가로 화면](ui/web-app-product-split-2026-10-18.md) | UI-PRODUCT-SPLIT-20261018 | 2026-10-18 | `focused-verified / native-device-unverified` |

## 보고서 보관·분류

- [주제별 재배치와 보존 검증](storage/library-organization-2026-10-25/README.md)
- [완료 보고서 보관·게시 절차](storage/report-completion-2026-10-25/README.md)
