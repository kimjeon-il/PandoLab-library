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
