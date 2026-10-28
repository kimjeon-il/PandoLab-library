# Pando 브랜치 통합·동기화 — 2026-10-28

> 보고서 ID: DEV-RELEASE-BRANCH-SYNC-20261028 · 상태: complete · 지도 반영: existing reviewed data deployed
> 기준 코드: 22d0b24eb5916f9597f4b0c6ae4625236a6722d9
> 자료 pin: 65fbc692f47f7936a804e7af0eed546966898828
> 원본·출처: before.json, integration.json, app-verification.json, runtime.json, remote.json, review.json, web-verification.json, final.json

## 대상과 완료 결과

Pando의 main, work/ui, work/objects, work/gis, work/places를 기존 상설 작업트리에서 fast-forward하고 원격도 한 번의 atomic push로 동일 커밋에 맞췄다. 추가 병합 커밋이나 이력 재작성은 없다. 실행 직전 원격 변경을 확인했으며 새 GIS 커밋을 보존했다.

UI 미커밋93개(수정38개·미추적55개)는 원래 상태와 SHA256이 모두 유지됐다. native 설치·아이콘79개와 지도 입력·렌더링 및 관련 검사14개이며, 커밋·공개하지 않았다. 자료 저장소의 독립 작업 브랜치와 gh-pages는 동일하게 유지됐다. 보고서 소유자 refs도 본 보고서 게시 전까지 변하지 않았으며, 게시 시에는 이 완료 범위의 main 소유자 판본만 갱신한다.

## 실제 실행한 확인

- GIS의 작은 회귀 테스트5개 통과. 전체 테스트나 GIS 재생성은 실행하지 않았다.
- 앱의 기존 프런트엔드 snapshot·오프라인 입력 계획을 메모리에서 확인했다. 684개 입력/258개국이며, 수정한4개 국가의 transport 내부 byte 범위와4개 라이브러리 입력을 새 pin의 SHA256·바이트 수와 대조했다. 설치 파일이나 WASM 재빌드는 하지 않았다.
- Web Pages 실행40705220401 성공. 실제 공개 코드·자료 pin 및 전송 bytes 확인 단계도 성공했다. 다른 자동CI 전체가 통과했다고 주장하지 않는다.
- 최종 로컬·원격5개 브랜치 SHA, 모든 pin과 mount, UI93개 파일의 상태·해시를 확인했다.
- 별도 검토에서 통합·보존 관련 Critical/Important 지적은 없었다. 새 역사 형상의 독립적 지리 정확도 검증이나 미커밋 UI 기능 검증은 이 작업의 범위가 아니다.

## 캐시와 보관

현재 pin의 runtime view5개는 각 상설 작업트리가 사용하며 공통 content pool을 공유한다. 이전 pin의 해당5개 view 삭제 여부는 final.json에 기록했다. 다른 작업의 비공개 수정과 기존 소유자 판본은 보존했다. 이번 작업의 별도 저장소 복사본·복구 pack·설치 패키지·임시 스크립트는 만들지 않았다. Git fetch가 시작한 promisor 재압축에서 생긴 중복 pack은 기존 보관 helper가 정리했다.

## 실행 판단 기록

아래는 작업 중 순서·검증 인터페이스에 관한 기록이며 제품 동작 변경이 아니다.

---

# Pando branch synchronization 2026-10-28

User approved integration of committed Pando branches only. UI WIP remains uncommitted.

Ruling: this task integrates existing source commits; no new production behavior is authored, so no new TDD changes or full test suite are introduced.

- Preflight: all local and remote code heads are ancestors of 22d0b24eb5916f9597f4b0c6ae4625236a6722d9. UI 93 paths captured with original bytes. Data work branches remain independent.

- Local integration: five branches fast-forwarded without a merge commit; UI 93 original file hashes preserved. Focused GIS tests: 5 passed, 0 failed.

- Cache preparation ruling: partial-clone metadata fetch initiated Git promisor repacking; existing library storage compaction finished. Missing selected archive objects are fetched explicitly with per-command remote.origin.promisor=false and no-filter, avoiding repeated full promisor repacking. Persistent Git configuration and data branches are unchanged.

- App verification ruling: country display chunks are selected through the current packed transport, rather than individually in the offline plan. Verified the four actual transport byte ranges and four direct library chunks against the pinned archive hashes; no product change was needed.

- Ordering ruling: after local heads, WIP preservation, focused tests, independent review and app input checks passed, publish all five code refs atomically while remaining local cache preparation continues. Remote Pages reads immutable Git revision65fbc692, so remaining local mount preparation is independent and remains a final completion gate.

