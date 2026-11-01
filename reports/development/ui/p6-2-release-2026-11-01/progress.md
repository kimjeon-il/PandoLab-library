# P6-2 · main 통합 · 배포 최종 상태

2026-11-01 UTC. 요청 범위의 기능 검사, main 통합, Pages 배포 및 선택한 공개 응답의 동일성 검증을 완료했다. 전체 저장소 CI가 모두 통과했다는 의미는 아니다.

## 완료

- 최종 코드: `35bce38a3444c57bcaf60a9a12d30421e6602740`; main과 work/ui 원격 ref 동일.
- main은 `2b460e40dbc51de2d13b0fe40e11bd4af9e49b75`에서 force=false fast-forward 통합했다.
- P6-2 390×844 Chromium touch emulation: 1 test / 4 steps 통과, page/console error 0. 입력 계약 18/18 및 변경 대상 lint 통과.
- Read model 14/14, registry/runner 26/26, 실제 자료 shared boundary 8/8, P2 source/selection/graph 49/49 통과.
- Web closure와 App test-fixture/map-data staging·verify 통과. Native installer는 빌드·기동하지 않았다.
- Pages run 41266675990의 build/deploy 성공. 실제 공개 응답 10개의 bytes/hash와 code/data identity 확인.
- 런타임 자료 pin `139941d8056418547c796068304ba8db3696fe69` 유지. 무관한 P2 생성 실행은 기존 concurrency로 취소되고 자료 publication이 없었다.

## 실패·미확인·보류

- 최종 P3 run 41266380046: 85개 중 84 pass, 1 fail. 예전 assets/css 경로를 사용하는 current-browser 계약 fixture 실패가 남아 있다.
- 앞선 cancelled P3 run 41265483904의 완료된 unit batch: 399개 중 333 pass, 66 fail. 해결·통과로 처리하지 않았다. 서로 다른 실행 수를 합산하지 않는다.
- 현재 main SharedCore run 41266676029: native CTest 9개 중 6 pass, 3 fail. 후속 WASM parity/lifecycle 단계 skipped.
- Architecture run 41266676100: 02:57:32 UTC snapshot에서 checks 진행 중. 실패 수는 미관찰이며 0으로 취급하지 않는다.
- 독립 공개 브라우저에서 dynamic module 요청이 ERR_BLOCKED_BY_CLIENT로 차단됐다. 공개 지도 UI 기동 미확인. 이것을 HTTP 404 또는 제품 회귀로 확정하지 않는다.
- 1953년 7월 전환 대기 및 injected-failure 뒤 이전 연도 timeout 두 사례는 미해결 상태로 보존했고 재실행하지 않았다.
- 실기기·Safari·WebView·소프트웨어 키보드·IME 및 새 성능 benchmark는 인증 범위 밖이다.

전체 결과와 원문 근거 연결은 [p6-2-release-report.md](p6-2-release-report.md), 기계 판독 결과는 [release-verification.json](release-verification.json)을 참조한다.
