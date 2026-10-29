# 모든 상설 브랜치의 main 통합 — 2026-10-29

## 범위와 결과

- 사용자 요청: 모든 로컬·원격 브랜치를 main에 병합하며 충돌은 먼저 확인한다.
- 시작 main/origin/main: `22d0b24eb5916f9597f4b0c6ae4625236a6722d9`.
- 통합 main: `f839d72c955d92d57b8ef2257f4f06783283425e` (시작 원격 main보다 88커밋 앞섬).
- 사용자가 원격 main 푸시·자동 웹 배포를 명시적으로 승인했다. `f839d72c955d92d57b8ef2257f4f06783283425e`를 원격 main에 푸시하고 정확한 원격 SHA를 확인했다. Pages 배포와 실제 공개 응답 검증을 완료했다.
- 기존 main 작업트리와 고정 `build-native/wasm`을 재사용했다. 새 브랜치·워크트리·저장소 복사본·네이티브 앱 패키지를 만들지 않았다.

## 포함한 브랜치 판본

| 브랜치 | 로컬·원격에서 확인한 커밋 |
| --- | --- |
| work/ui | `0b56dcf2a40a68e8e96ce95f26795c17aea70bd9` |
| work/objects | `bc69f9daedc880e269506b1352171f8817104461` |
| work/gis | `7234baac176b262f7ce2b8848a69ff9b30cf9645` |
| work/places | `22d0b24eb5916f9597f4b0c6ae4625236a6722d9` |

진행 중 추가 커밋도 확인하여 UI 투영/WASM 게시와 GIS 학습 증거·결정적 resize gradient까지 통합했다. 최종 각 ref의 main 조상 포함 여부를 Git으로 확인한다. 미커밋 수정은 병합 대상이 아니다. UI의 진행 중 화면·아이콘 수정, GIS `.git-ne-oracle-path.tmp`, objects의 미추적 검증 파일 4개는 건드리지 않았다. 다른 작업 브랜치로 main을 전파하지 않았다.

## 사용자가 승인한 충돌 해결

1. UI 지도 분석과 objects 공통 C++·시기별 국명 소스를 모두 합친 뒤 기존 경로에서 WASM을 증분 빌드했다. 나중에 추가된 UI 투영 계산과 WASM 게시 커밋에도 같은 원칙을 적용했다.
2. GIS 중국 접경 3객체와 아르차흐 명칭의 자료 판본을 합쳤다. 전체 GIS를 재생성하지 않았다.
3. `jobs.mjs`의 새 지리보정 import와 shared/frontend 경로 수정을 모두 보존했다. engine/runtime-assets/library-data의 자동 병합 결과도 양쪽 입력과 대조했다.

통합 자료: `ef77d01776dfd9d8bd7a495877ce9e2b39095823`. 부모는 objects `4f3ad7c3206e22c23e34c3aa500574a07b1d94f7`와 GIS `98f41c4c7ab2ec0f07fdcc81bf21531fc7475ad0`다. 외부 자료 저장소 `work/objects`에 푸시하고 원격 SHA를 확인했다. 앱 main의 자료 핀이 이 판본을 선택한다. 라이브러리 main 독립 채널로 공개 자료를 덮어쓰지 않았다.

선택한 `state:MNG`, `state:soviet-union`, `state:soviet-union-russian-sfsr`, `state:nagorno-karabakh` 4개만 원본 색인·네이티브 객체·컴파일 청크를 해당 부모와 비교해 보존을 확인했다. 나머지 국가 본문은 파싱하거나 개별 해시 감사하지 않고 기존 압축 청크를 재사용했다. 전송 묶음의 해시는 전송 무결성 목적으로 확인했다. 통합 전송 파일은 12,563,846바이트다.

## 실제 수행한 집중 확인

- UI/objects 합본: map-analysis-georef/symbols/ocr-catalog, territorial-library, builtin-world-catalog 합성 테스트 62개 통과.
- GIS 합본: china-frontier-delta/native-tool/map-source-acquisition/map-archive 19개 통과, Python 환경변수 전제 CLI 사례 1개는 기존 조건에 따라 실행하지 않음.
- 충돌 소비자 map-plugin의 production jobs/job revision/crop quality/manual controls 4개 통과.
- 최종 투영 합본: map-analysis-projection/georef/territorial-library/builtin-world-catalog 51개 통과. 위 map-plugin 4개도 최종 WASM에서 재통과.
- 학습 proof의 변조 tensor/weights 거부 합성 사례 1개 통과. LibTorch 전체 학습·GPU 훈련·새 네이티브 바이너리 빌드는 실행하지 않았다. 해당 C++ 변경은 소스 병합과 diff 검토만 했다.
- 충돌/자동 병합 JS 파일과 새 georef/투영 테스트의 관련 ESLint 통과.
- `package-shared-core-assets --build-dir build-native/wasm/wasm --check` 통과. 소스 `3fd61e01c71374bce5038d82f45e9cbe90147284b9770500fa4da9561a44e3ec`, JS `a793e01ea90464da0784638b0b9872094c633291bb289623d38cfe365e293fe9`, WASM `3c06ff93b0d95e8e546d58cc5f8dc112fcdd9ea847e7bc76c4dad3d85becc41a`.
- 실제 Edge에서 territorial-names 브라우저 시나리오: 웹 1개 통과, 앱 웹셸 1개 통과. 1객체 합성 프로젝트로 시점별 국명, 편집, Undo, GeoPackage 저장·재열기, 형상/수정 상태를 확인했다. 기본 세계지도 transport 요청은 차단하고 요청이 없음을 검증했다.
- 웹은 다운로드 후 재열기, 앱 웹셸은 모의 Tauri 파일 브리지다. 실제 Windows/Android 네이티브 앱 검증은 수행하지 않았다.
- 독립 검토자는 충돌 해결·자동 병합·자료 부모·최종 WASM 소스 식별에 P1/P2 통합 결함을 발견하지 않았다.
- 전체 테스트·동종 실자료 전수검사·전체 GIS 재생성·앱 재빌드·설치 패키지 생성은 하지 않았다. 지원되지 않는 `--help` 호출 1회는 인자 오류였으며 실제 packaging/check 명령은 정상 통과했다.
- PROJ 라이선스 첫 문장의 기존 행 끝 공백만 정리했다. 최종 시작 main 대비 `git diff --check`를 통과했다.

## 승인 후 원격 푸시·공개 웹 배포

- Git 원격 main: `f839d72c955d92d57b8ef2257f4f06783283425e`. 일반 push로 반영했으며 force push하지 않았다. 다른 작업 브랜치와 미커밋 수정은 그대로 유지했다.
- [Pages 실행 40852823332](https://github.com/kimjeon-il/Pando/actions/runs/40852823332)의 build·deploy·실제 응답 검증 단계가 모두 성공했다.
- 공개 주소: https://kimjeon-il.github.io/Pando/ . 실제 build-meta의 코드 SHA는 `f839d72c955d92d57b8ef2257f4f06783283425e`, 자료 SHA는 `ef77d01776dfd9d8bd7a495877ce9e2b39095823`으로 일치한다.
- CI에서 게시 직전에 생성한 `deployment/pages-evidence.json`(537,778바이트)을 내려받아 기존 `tools/verify-pages-deployment.mjs`로 공개 HTML/build-meta/자료 색인 등 10개 파일의 HTTP·크기·SHA-256을 다시 검증했다. 결과는 `deployment/live-local.json`이다.
- 추가로 실제 공개된 JS·WASM·manifest와 12,563,846바이트 세계지도 transport의 HTTP 200·크기·SHA-256을 같은 CI 목록과 대조했다. 4개 모두 일치하며 결과는 `deployment/live-core-data.json`이다. 전송 바이트 검증이며 국가 전체 의미 검사나 GIS 재생성을 수행하지 않았다.
- 검증 바이트는 메모리에서 비교했다. 200MB Pages 패키지를 로컬로 내려받거나 새 staging·빌드·임시 복사본을 만들지 않았다. 보관한 작은 CI 목록과 JSON은 이 배포의 출처·검증 증거이며 이 보고서와 같은 범위로 라이브러리에 보관한다.
- 별도 Shared C++/Application Architecture 워크플로는 이 기록 시점에 진행 중이다. Pages 성공과 이 두 CI 전체 성공을 혼동하지 않는다. 실제 페이지에서 추가적인 국가 전수 검사·전체 사용자 흐름 재검사는 수행하지 않았다.

## 저장공간과 정리

- 중간 측정 D 여유 59,982,897,152바이트 → 검증 후 59,663,851,520바이트. 드라이브 전체 약 319MB 감소는 동시 다른 작업도 있어 이 작업 단독 사용량으로 단정하지 않는다.
- 기존 증분 WASM 경로는 현재 검증된 공통 바이너리와 후속 증분 빌드의 소비 경로이므로 유지했다. 자료 runtime view는 현재 main 핀의 소비 경로이며 공유 blob/하드링크를 재사용한다.
- 임시 자료 병합 스크립트 `C:/Users/taeeu/.codex/tmp/pando-runtime-union-20261029.mjs` 8,828바이트 삭제 완료. 두 검사 서버는 정상 종료했다.
- `C:/Users/taeeu/.codex/tmp/pando-main-integration-web` 53,293바이트와 `.../pando-main-integration-app` 45바이트는 사용이 끝난 검사 출력이다. 삭제 명령이 자동 승인 검토에서 `blocked by policy`로 거절되어 남아 있다. 상세 거절 이유는 제공되지 않았고 우회하지 않았다. 논리 합계 53,338바이트를 실제 회수량으로 세지 않는다.
- 앞선 작업에서 이미 삭제 차단된 파일/폴더는 이번에 재시도하거나 우회 삭제하지 않았다.

보고서 자체는 이 선택 범위만 publish/check하여 라이브러리 원격 커밋과 바이트를 별도로 확인한다.

## 아이콘 제외 미커밋 통합 및 모든 상설 브랜치 전파

- 최종 코드: `efe24258ac79cedecdfcffbb0f486c9d06e53ea1`. main, work/ui, work/objects, work/gis, work/places의 로컬·원격 5개 참조를 일반 fast-forward와 원자적 push로 같은 커밋에 맞췄다. force push/reset/stash/clean은 사용하지 않았다.
- 사용자가 승인한 범위는 아이콘 관련 파일을 제외한 미커밋 소스의 main 통합, 그 뒤 브랜치 전파·푸시·자동 웹 배포다. UI·지도 그리기 플러그인·자료 및 깃 이력 정리·지도 데이터 채팅과 변경 중단을 조율한 뒤 실행했다.
- UI 소스 작업 `095bcae9eed9a98a02917cdb2b99bc361954a871`: 지도 프레임·입력·선택·picking 관련 41개 경로와 Windows 설치 계약. README/native-contract/native-contract.test의 혼합 변경은 설치 부분만 커밋했고 아이콘 관련 부분은 미커밋 상태로 보존했다.
- GIS 소스 작업 `13ab144cf48f6a44d2f515f33218a350597d43cc`: native point-screen의 parts 모드와 첫 10개용 조사 도구·합성 회귀 사례 7개 경로. 실제 전체 수계 감사를 실행하거나 데이터 결과를 추정하지 않았다. QGIS Node 연결과 composed inverse projection의 기존 소스 커밋도 함께 포함됐다.
- UI의 남은 77개 아이콘 관련 경로/혼합 편집본은 통합 직전 바이트 SHA-256과 전부 일치했다. objects의 .pando-domain-* 검증 복사본 4개와 GIS의 .git-ne-oracle-path.tmp도 원래 바이트로 보존했다. 이 5개 임시 파일은 제품 수정이 아니므로 앱 소스 커밋에 넣지 않았고, 이전 삭제 차단을 우회하지 않았다.

### 자료·WASM 대응과 현재 마운트

- 공개 자료 핀: `0bce2891d531579b81ac0f97e6d07cb1873b878f`. GIS가 검토한 소련 벨라루스 SSR·러시아 SFSR·우크라이나 SSR 내부 경계 변경을 보존했다. ef77→0bce에서 아르차흐 정본의 해당 객체 해시가 같은 것도 그 객체에 한해 확인했다. 국가 전체 보존 감사를 실행하지 않았다.
- 다섯 작업공간의 config 핀과 .complete, assets/data 실제 마운트가 모두 위 판본과 일치했다. 기존 prepareLibraryData를 순서대로 실행하고 공유 blob/고정 view를 재사용했다. 보고서 전체 복원·GIS 재생성은 하지 않았다.
- 초기 map-content-scene 검사는 새 partial-clone 핀의 메타데이터 blob이 로컬에 없어 실패했다. 준비와 Git lazy fetch를 겹치지 않도록 순서를 바로잡고, 필요한 색인/manifest 8개만 확보한 다음 기존 준비 명령으로 복구했다. Git 객체 집합 변동을 감지한 안전장치의 중단은 기존 재개 경로로 완료됐고 소스 패치를 추가하지 않았다.
- WASM 소스 SHA: `3a28c8e17473c177a84551b47450d557ca659ab54d41d46736b85ca3d597be5d`. 실제 현재 소스·JS·WASM·manifest로 loadNodeCore ABI 1을 확인했다. 75bf0316의 검증된 대응 산출물을 재사용했으며 오래된 main build-native/wasm 산출물로 덮어쓰지 않았다.

### 집중 검증과 한계

- UI/Windows 설치 계약 관련 검사 묶음에서 151개가 통과했다. 새 핀 준비 실패가 있던 map-content-scene은 준비 후 별도로 3개 모두 통과했다. selection-fill-handoff의 오래된 mock은 실제 baseResources/territorialResources 및 물리 육지 scene 계약에 맞춰 갱신했고, 10개 모두 통과했다. 선택 가시성·형상·Undo 관련 검사를 약화하지 않았다.
- QGIS Node 연결·MCP·시작/프로젝트 검사, Hydro 합성 조사 도구, projection 및 모델 기본값 관련 47개 통과. GIS 미커밋 도구 합성 검사 6개 통과. 관련 ESLint와 diff --check 통과.
- native point-screen Windows CLI만 GitHub Actions [40864946763](https://github.com/kimjeon-il/Pando/actions/runs/40864946763)에서 source 13ab144c로 빌드했다. 기존 OSGeo4W의 GEOS 3.15.0/PROJ 9.8.1을 이용해 실제 새 CLI의 parts 모드 포함 3개 합성 검사가 통과했다. 새 SDK/AVD/환경·네이티브 앱·EXE/APK 설치 패키지는 만들지 않았다.
- 실제 Edge: Canvas·Canvas-worker의 시점 변경 중 픽셀 유지 2개, 앱 웹셸의 picking/open/zoom/문서 상태 검사 1개, Viewer hover/body click/camera/문서 상태 검사 1개 통과. 별도 앱 웹셸의 시기별 국명 편집·Undo/Redo·GeoPackage 저장/재열기 1개도 통과했다. Tauri 파일 브리지는 모의이며 실기기 검증이라는 뜻이 아니다.
- WebGL의 첫 baseline은 국경선이 아직 없었고, 이후 실패 비교의 baseline은 역사 수역이 미완료였다. 준비 상태 계측과 캔버스 차이 영역(카스피해/아랄해)으로 확인했다. 최종 테스트 변경은 실제 국경·수역 제출을 기다리도록 한정했으며 hash 허용 오차를 늘리거나 실패 검사를 제거하지 않았다.
- WebGL 집중 사례는 한 번 전체 통과했지만 최종 반복에서 실패 후 복원 hash가 580427134→623091269로 달랐다. 최초 대기 구간 hash 245350889는 동일했다. 따라서 WebGL 실패 복원은 간헐적 차이가 남은 미완료 검증으로 기록한다. 호버 캐시 가설로 시도한 제품 변경은 실제 원인이 아님을 확인해 모두 되돌렸고, 이번 추가 제품 패치는 없다.
- [Shared C++ CI 40872016724](https://github.com/kimjeon-il/Pando/actions/runs/40872016724)는 codec:50, content-command:144, object-command:54의 기존 3개 실패가 재현됐다(9개 중 6개 통과). 이전 f839/decf/ecb CI와 같은 실패다. 전체 CI가 통과했다는 뜻으로 Pages 성공을 사용하지 않는다. Application Architecture 40872016708은 이 기록 시점에 진행 중이다.
- 전체 테스트·동종 실제 자료 전수검사·GIS 재생성·네이티브 앱 재빌드는 실행하지 않았다.

### 최종 공개 응답 확인

- [Pages 40872016678](https://github.com/kimjeon-il/Pando/actions/runs/40872016678)의 build·deploy·실제 응답 검증 성공. https://kimjeon-il.github.io/Pando/ 의 코드 efe24258 / 자료 0bce2891 식별을 확인했다.
- deployment-efe24258/pages-evidence.json의 목록과 공개 HTML/build-meta/자료 색인 10개를 기존 검증기로 다시 비교했다. 실제 JS·WASM·manifest와 12,575,086바이트 세계지도 transport 4개도 HTTP 200·크기·SHA-256이 일치했다. 결과는 같은 폴더의 live-local.json, live-core-data.json이다. 200MB 사이트 묶음은 내려받지 않았다.
- 이전 decf/ecb 게시 JSON도 해당 배포 출처로 같은 선택 보고서 범위에 보관한다. 보고서 원격 보관은 아래 완료 명령으로 별도 확인한다.

### 임시 출력과 디스크

- 검사 서버 4184/4185를 종료했고 LISTEN이 없는 것을 확인했다. 이번 계측 D 여유는 59,052,822,528→59,056,136,192바이트다. 동시 시스템 활동을 포함한 관측값이며 삭제 회수량으로 계산하지 않는다.
- 브라우저 검사 출력 C:/Users/taeeu/.codex/tmp/pando-main-wip-web 17,291,078바이트와 pando-main-wip-app 45바이트는 검증이 끝난 재생성 가능한 출력이다. 안전 경로·링크 확인을 포함한 삭제 명령이 자동 승인 검토에서 blocked by policy로 거절돼 남았다. 상세 거절 이유가 없었고 다른 도구로 우회하지 않았다. 제거 논리 바이트 0, 차단 합계 17,291,123바이트다.
- D:/dev/worktrees/gis/build-native/hydro-point-screen/artifact의 구판 203,370바이트 정리와 candidate 승격도 같은 검토에서 차단돼 기존 파일을 바꾸지 않았다. 새 candidate 204,394바이트는 source 13ab 검증을 통과한 유일한 현재 CLI이며 후속 GIS 도구의 명시적 directory 입력으로 유지한다. 기본 artifact 경로는 여전히 구판임을 소유자에게 전달한다.
- 현재 자료 view는 다섯 고정 작업공간이 사용하고, 공유 blob과 활성 증분 빌드·SDK는 계속 사용하므로 보존한다. 삭제 차단된 이전 작업 출력은 재시도하지 않았다.

