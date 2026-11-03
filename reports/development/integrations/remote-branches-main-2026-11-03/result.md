# 원격 브랜치 미반영 커밋의 main 통합

> 보고서 ID: DEV-INTEGRATION-20261103 · 상태: complete
> 최종 수정: 2026-11-03 · 코드: `b917ddb7485f4bab3446aa31050270f5b2aa7a45`
> 자료 pin: `0388abf78dff4ea4835e36b01de67d10703ac596`

## 범위와 보존

원격 코드 refs 18개의 미반영 커밋을 통합했다. 독립 통합 머리는 UI `0eec519a8`, R4-E3 `78568cac3`, P6-3 `0af8b63d2`, GIS `ba6b2fe67`이다. GIS는 최초 검토 후 추가된 Node-only Landsat 도구 10커밋도 포함한다. 전체 SHA와 조상 판정은 `final-ref-coverage.json`에 있다. main 외 브랜치 동기화·삭제, 보고서 보호 refs와 자료 저장소 브랜치 병합은 하지 않았다.

기존 UI 정책 문서 1개, objects 미완성 파일 4개, GIS `.git-ne-oracle-path.tmp` 1개의 SHA256은 시작과 같다(`wip-preservation.json`). 다른 작업트리의 새 작업도 건드리지 않았다. main은 최종 커밋 후 깨끗하다. stash/reset/clean/강제 푸시를 쓰지 않았다.

## 충돌 해결

현재 사용하는 map-diagnostics 테스트·helper와 source oracle 3개를 보존했다. R4 삭제 ledger를 실제 범위로 합쳤다. UI application catalog를 유지해 오래된 브랜치가 폐기된 browser spec 34개를 재등록하지 않게 했다. 두 workflow의 대상과 관련 검사를 합쳤다. 틀린 전역 테스트 수 877 상수만 제거하고 170개 폐기 목록·고유 등록·정확한 제거/보존 검사는 유지했다.

Windows CRLF에서 실패하는 세 진단 입력을 메모리에서 LF로 정규화했다. Windows BSD tar와 GNU 옵션의 차이는 Git for Windows GNU tar와 bundled gzip PATH로 해결했다. `--force-local`, 링크/중복/크기/전체 inventory 거절을 유지했다. USTAR 링크 type flag 합성으로 Windows 링크 권한 없이 실제 거절 동작을 검사한다. P6 문서도 Worker의 ID/집합/토큰 거절과 sender의 순서 비호환 full replace 전환을 구분했다.

## 자료와 검증 범위

자료 pin은 기존 main의 hydro v0.13.4 `91c127dd...` 후속이며 prepared-polygons manifest·105480-byte gzip object와 인덱스만 다르다. 기존 준비 명령으로 1768 runtime 파일, private 0개를 준비했다. runtime identity는 `data-49126647213439404ae76ebefca51e3f`다. 전체 GIS 생성·보고서 전체 복원·모델 갱신은 하지 않았다.

실행한 영향 검사:

- R4-B/C 11, E3 현재 inventory 4, 폐기/catalog closure 20, diagnostics/hover 49 통과.
- P6 Worker/transport 및 label/click/tooltip 소비자 62, GIS provenance/hydro 합성/P6 protocol 24, hydro layout/packfile/service와 native data plan 24 통과.
- 최종 GIS spectral/connectivity 6, release 18, R4-E0/E1/E2 13, Pages staging 8을 묶어 45/45 통과. Node spectral self-test도 통과.
- 앱 snapshot/native Worker 계약 4/4 통과. 기존 Windows reviewer browser 2, Worker rollback 1, packet reuse 1 통과. distinct supersession으로 강화한 packet reuse 단독 재검사도 통과.
- 변경 파일 scoped ESLint와 diff whitespace 통과. 진단 도구의 browser 평가 전역을 명시했고 lint rule을 끄지 않았다.

전체 테스트·전체 C++/WASM matrix·전체 GIS 검사는 실행하지 않았다. production C++/WASM은 같아 rebuild/설치 패키지를 만들지 않았다. 위성 자료·법적 경계·모델 정확도 승인과 별개다.

## Windows 실GPU A-B-A

GTX1650, driver32.0.16.1088, Chromium151.0.7922.34, D3D11과 GPU compositing을 CDP와 WebGL 양쪽에서 확인했다. 1280×800 DPR1, 동일 최종 자료로 A=`488c845ad5eda8c392f186744da0b96e2938802c`, B=`f53efa37153f4b65ceaf3ba25d122b8962144842`, A2=A를 비교했다. Viewer/shared frontend의 차이는 P6 제품 파일 3개다. 이후 GIS/진단/release 수정은 측정한 Viewer 제품 경로를 바꾸지 않는다.

새 browser 10개씩 총30개에서 두 방향을 측정했다. 각 방향 n=10, p90은 nearest-rank다. 원시 JSON·trace·화면과 `performance/summary-compact.json`을 보관한다.

| 전환 | A p50/p90 ms | B p50/p90 ms | A2 p50/p90 ms |
| --- | ---: | ---: | ---: |
| 1991-12→1992-12 | 5869.8/6305.2 | 5893.3/6122.6 | 5872.0/5938.7 |
| 1992-12→1991-12 | 5402.3/5450.2 | 5051.5/5168.9 | 5385.8/5451.2 |

정방향은 full 전송한다. 역방향 B는 242개 중 형상1개 전송·241개 재사용·4개 제거다. 역방향 postMessage p50은 A190.6/B1.5/A2187.9ms, 전체 표시 p50은 약6.2–6.5% 개선됐다. 전체 메시지0바이트나 모든 날짜의 개선을 뜻하지 않는다. 각 목표 document/geometry/timeline/label 의미 hash는 모든 표본에서 일치한다.

2025/2026 warm 왕복 A20/B60/A220회 통과. 표시 p50은 777.8/785.2/781.2ms로 약1% 이내 차이며 개선 주장 대상이 아니다. B60회까지 packet1개16556996bytes로96MiB 상한 안이고 detached buffer가 없다. Worker post-GC JS 초기136059588→최종136060048bytes, main 초기124567468→최종126692024bytes다. 초기 cache 확장 뒤20→60회 main 증가는370688bytes, WASM은10회 이후386465792bytes다. 일반적인 무누수 증명은 아니다.

stale 응답 거절, wrong-token resync→full 복구, distinct burst[9,10,11] 중11만 채택, 오류 후 Core rollback, WebGL context loss 복구를 확인했다. 상태·픽셀은 유지됐다. context 초기 캡처 실패는 성공 toast가 canvas 위에 겹친 원인이었고, 알림이 사라진 뒤 같은 PNG byte 비교가 통과했다. 실패 원본도 원인 증거로 보관하며 비교 기준을 완화하지 않았다.

## 비공개 Map Toolkit

기존 PRIVATE 개인 플러그인0.6.10의 exact-release archive와267-file inventory/manifest/receipt를 인증된 Plugin Creator에서 읽고 원격 바이트를 확인했다. content SHA256 `14b34d96dc29e8b15299af812cfc53b40922c9acdb9a913fe9d77a16bda633ff` 일치. 기준 source `15dcb790c007625bb2a15d0b56081af339c88e0a`는 통합 main의 조상이다. packaged closure239개 중 바뀐 것은 package.json의 비배포 scripts뿐이며 실제 package dependency 투영은 같다. 내용이 같아 upload/version bump를 생략했다. 비공개 model·account 설정은 이 보고서에 넣지 않았다. 설치 cache/열린 chat 갱신은 주장하지 않는다.

## 배포와 정리

main push와 [Pages41578529081](https://github.com/kimjeon-il/Pando/actions/runs/41578529081) 모두 성공했다. 공개 코드·자료 identity와10개 전송 파일의 크기/SHA256을 로컬과 CI에서 각각 확인했다. 실제 공개 Viewer 시작·연도 전환1개가36.2초에 통과했고 오류·실패 요청은0개다. 완료·cleanup 증거는 completion.json과 deployment/에 있다.

시험용 A/B 서버2개는 PID·command line 재확인 후 중지했다. SDK·training 환경·현재 pin cache·타 작업 서버를 보존한다. raw trace/화면은 이 통합 판단의 고유 증거다. 사용 종료된 다운로드·중간 checkpoint 등은 소비자 확인 뒤 정리한다.

정리한10개 파일의 논리 크기는 62099509bytes다. 첫6개 정리의 관측 여유 공간 증가는61259776bytes이며 동시 호스트 활동이 포함될 수 있다. 나머지 raw performance trace/화면·JSON은 재현과 통합 결정의 고유 증거로 선택된 보고서 범위에 보관한다.
