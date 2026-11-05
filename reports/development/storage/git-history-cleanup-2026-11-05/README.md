# 승인 후보 Git 이력 정리 결과

> 보고서 ID: DEV-STORAGE-GIT-20261105 · 상태: 일반 refs·로컬 완료 / GitHub PR refs 미완료 · 지도 반영: not-applied · 기준일: 2026-11-05
> 코드 기준: 6a1db6c2e87894016f98309135896ce0199537b6 / runtime pin: 2b8825e4570b0c1e0558f76317f4ce3d021b4f11
> 근거: 앞선 git-history-review-2026-11-05 승인 목록, 실제 객체·refs·작업트리·전송 바이트 확인

## 범위와 방법

승인한 과거 생성물만 제거했다. 자료 저장소는 terrain-v0.12.0 275개, terrain-v0.12.6 335개, prepared-polygons 740개, old-hydro 1,781개, old-world 49개로 총 3,180개다. 코드 저장소는 현행 tip에서 사용하지 않는 과거 index.html·GDAL WASM/data 객체 633개다. 재탐색에서 기존 631개 집계의 HTML 경로 별칭 2개가 추가됐으며 동일한 승인 생성물 범위다. 정확한 Git blob 목록은 approved-blobs.json에 있다.

커밋·트리·태그·refs를 승인 blob 단위로 다시 작성했다. archive/index.json은 해당 stored blob의 항목만 제거했고, 유효하지 않은 과거 JSON은 고유 증거로 보존했다. 자료 tip 트리는 동일하고 코드 tip 차이는 새 자료 커밋을 가리키는 config/library-data.json뿐이다. 서명된 커밋/태그는 재작성으로 원래 서명 효력이 유지되지 않는다. 공개 코드 tip에는 넓은 자동 CI 실행을 막는 [skip ci]가 추가됐다.

두 저장소 각각 실행 직전 원격 SHA를 exact lease로 제한한 atomic push를 사용했다. 작업 중 work/remote-only에 새 커밋 bab7c99f748fbad8e9f77ae3a36e2cad0363c40f가 추가됐으나 정리한 0c2fae913087697846f79481ae6eb85c3966e2d9의 후손임을 확인하고 보존했다. 이후 자료 보고서 게시 커밋은 정리한 library main에서 이어진다.

## 실제 확인과 보존

- 일반 원격 heads의 탐색 결과 승인 blob이 0개이며 로컬 object store에서도 코드 633개와 자료 3,180개가 모두 없다.
- 영구 작업트리 5곳의 미커밋·미추적 36개 파일은 상태와 SHA256이 시작 전과 동일하다. GIS의 로컬 전용 3커밋도 보존했다.
- 원본 지도, 모델, 비승인 원본 blob, 독립 보고서 판본, 보고서 보호 refs, 기존 stash·작업트리를 보존했다. 자료 pin과 owner revision, reflog, detached HEAD를 새 대응 커밋으로 연결했다.
- 종료된 과거 시험 작업트리 4개의 깨끗한 인덱스와 자료 UI 준비 인덱스에 남은 승인 객체·옛 cache-tree 포인터를 같은 변환으로 수정했다. 다른 staged 작업을 제거하지 않았으며 작업트리 자체는 삭제하지 않았다.
- 양쪽 git fsck --connectivity-only --no-reflogs --no-dangling 통과. 부분 clone의 미수신 비대상 archive blob은 그대로이며 전체 원본을 다운로드하지 않았다.
- 기존 준비 명령으로 5곳의 자료 마운트를 갱신하고 config pin, .cache-owner.json, .complete, 실제 assets/data 마운트 대상을 확인했다. GIS pin은 3673ce501c5c2479356414816b5c5daa0ca3e6c6으로 독립 유지했다. 전체 GIS 재생성, 전체 앱 검사, 네이티브 재빌드는 실행하지 않았다.

## 저장 공간

정상 .pack 파일 합계는 코드 101,611,452 → 87,690,843바이트, 자료 4,394,007,073 → 3,152,209,232바이트로 줄었다. 합계 감소는 1,255,718,450바이트(약 1.17GiB)다. 이는 raw pack 기준이며 삭제한 구 pack의 총 바이트, 압축 전 논리 용량, D: 여유 공간 증감과 구분한다. 최종 보고서 저장과 새 원격 커밋으로 작은 객체가 추가될 수 있다. 작업 소유 임시 파일 삭제 및 D: 실측은 cleanup.json에 별도 기록한다.

비공개 판본의 옛→새 출처 대응과 정확한 삭제 증거는 로컬 제외 경로 private-evidence/git-history-cleanup-20261105/provenance.zip에 metadata만 보관했다. 42개 항목을 원본 크기·SHA256으로 재확인했으며 18498426바이트다. 제거 대상 payload, 지도·모델·전체 저장소 백업을 포함하지 않는다. 기존 손상 복구 파일 tmp_pack_uUtx8n 33,595,391바이트는 고유 복구 가능성을 판정하지 못했고 승인 목록 밖이므로 보존했다.

## Map Toolkit 의존 주소 갱신

Git 이력 변경으로 달라진 immutable 자료·bootstrap 주소를 비공개 Map Toolkit 소스 9b0b52ec8470526a9c89a54e365d1bcdf3fbf543에 반영·푸시했다. 동일한 모델과 shared artifact 바이트를 유지했다. 관련 단위 사례 27개 및 패키지 생산기의 runtime 사례 10개를 통과했고, 기존 비공개 개인 플러그인 0.7.2를 갱신한 후 실제 배포 archive 277개 파일을 계획과 정확히 비교했다. 설치된 캐시나 기존 대화의 갱신을 입증한 것은 아니다. 모델 정확도·추론·학습을 새로 승인한 작업도 아니다.

## GitHub 서버에 남은 이력과 한계

GitHub가 소유하는 과거 PR refs 17개에서 코드 승인 blob 633개가 여전히 도달 가능하다. PR1은 이미 closed/merged지만 refs/pull/1/head 삭제 API는 HTTP 422, refs/pull/* is read-only.로 거절됐다. 이 ref는 일반 branch force-push나 로컬 GC로 제거할 수 없다. 자료 저장소에는 해당 PR ref가 없다.

따라서 일반 브랜치 이력·로컬 객체 정리는 완료됐지만 GitHub 서버의 모든 사본 삭제나 물리 GC 완료는 확인하지 못했다. 서버 관리 PR refs의 별도 처리가 남았으며, 저장소 자체 삭제·재생성은 이 승인 범위를 넘어 실행하지 않았다. 웹 배포도 이번 이력 정리의 완료 기준에 포함하지 않았다. 상세 공개 결과와 새 head 목록은 result.json에 있다.

## 종료 임시 산출물 정리의 실제 상태

이번 작업의 scratch 202,785,218바이트, 검증 완료된 private plugin 패키지 디렉터리 95,768,754바이트, ZIP 59,567,335바이트, release receipt 63,097바이트(총 358,184,404바이트)를 대상으로 경로·reparse·SHA256·소비자 검사를 포함한 PowerShell 삭제 명령을 제출했으나 실행 도구의 자동 승인 검토가 blocked by policy로 거절했다. 파일 삭제는 실행되지 않았으며 다른 도구로 우회하지 않았다. 보존 원인은 사용자 전체 검증 제한이나 파일 사용 필요가 아닌 실제 도구 정책 거절이다. 파일별 해시·삭제 대상 manifest는 로컬 비공개 증거에 남겼다. 따라서 Git 정상 pack 정리와 별도로 작업 종료 임시 산출물 삭제는 미완료다.

## 재개 확인

좁힌 단일 ZIP 삭제도 도구의 사전 정책 검토에서 거절돼 임시 산출물은 남아 있다. GitHub 공식 문서의 PR refs 제한과 비민감 자료 지원 제외를 확인했고, 운영 저장소 교체의 대상·보존 범위·삭제 영향·secrets 복원 조건을 remaining-actions.md에 구체화했다. 저장소 교체와 옛 저장소 삭제는 승인 대기이며 실행하지 않았다.
