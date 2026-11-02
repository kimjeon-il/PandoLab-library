# W1 Windows 실제 GPU 성능 검증 — 2026-11-02

완료 범위: Windows Chromium 실제 NVIDIA GPU 확인 및 동일 호스트 A-B-A. A-B-A 30회(준비 6, 본 측정 24), 보조 무옵션 진단 4회(준비 2, 본 측정 2). 본 검사는 8.3분, 보조 진단은 1.8분 걸렸다. 앞서 저장한 blocked-preflight는 이 측정 이전 상태이며 현재 중단 상태를 나타내지 않는다.

## 환경 및 고정 조건

- work/ui source: 69a34dceccdf4b348dfaaab79fa5dc712a169e53; runtime library pin: 5eb7be55208efaafe39bd5a65ec2f111d70b9053; browser data identity: data-f50b7f480c812df6f5ea0c40f5461ab0.
- Windows, Chromium 151.0.7922.34, 1280x800, DPR 1, 실제 canvas 1280x752, Asia/Seoul, ko-KR, headless.
- NVIDIA GeForce GTX 1650, driver 32.0.16.1088, ANGLE D3D11. SystemInfo GPU device ID 0x2188, vendor 0x10de; WebGL 실제 canvas의 unmasked renderer 및 GPU compositing enabled를 함께 확인했다. AMD와 Intel 장치는 이 호스트에서 확인되지 않아 해당 하드웨어는 검증 대상이 아니다. Microsoft Basic Render Driver도 열거되지만 A의 실제 renderer는 NVIDIA다.
- A: --use-angle=d3d11, B: --use-angle=swiftshader, A 재시험: --use-angle=d3d11. 각 실행은 별도 browser/context. B는 WebGL은 SwiftShader이고 GPU compositing은 enabled다. 무옵션 진단은 WebGL SwiftShader 및 GPU compositing disabled_software다. 같은 SwiftShader 문자열이라도 합성기 경로는 다르다.
- 연도 버튼으로 2025-12 ↔ 2026-11을 교대로 전환. 기존 viewer-gpu-backend-cross.spec.mjs의 시나리오와 마커를 재사용했다. 날짜 및 지도 데이터, 제품 코드, 스타일, 표시 항목을 성능 목적으로 바꾸지 않았다.

## 본 측정 결과

단위 ms. 표시/준비/RPC/Worker는 중앙값, Long Task와 DoUpdateLayers는 전환 구간의 최댓값. n=8의 p95는 탐색적 수치이며 원시 JSON에 남겼다.

|실행|n|지도 표시|준비 완료|Core release RPC|Worker release|Long Task 최대|DoUpdateLayers 최대|
|---|---:|---:|---:|---:|---:|---:|---:|
|default|8|800.1|926.1|8.4|3.3|173|0.544|
|swiftshader|8|819.6|1018.3|14.2|3.5|176|3.372|
|default-retest|8|831.8|961.1|8.6|3.4|198|0.567|
|unforced|2|809.9|3618|2656.3|3.8|2726|2659.241|

표시는 기존 onPresented 승인 콜백, 준비 완료는 viewerStatus ready 마커다. OS 모니터의 실제 광자 표시 시점을 측정한 것은 아니다. 특히 무옵션 경로는 표시 콜백 뒤 합성기 대기가 이어지므로 표시 콜백만으로 사용자가 즉시 화면을 보았다고 해석하면 안 된다. Core RPC 수치는 core.document-replacement-release의 왕복이며 모든 Core 연산의 합계가 아니다. Long Task는 요청~준비 구간과 겹치는 메인 스레드 표본이다. trace span은 중첩되므로 서로 더하지 않는다.

## 2초 정지 판정과 원인

- 하드웨어 본 측정 16회에서 준비 완료 최댓값 997.6ms, 메인 Long Task 최댓값 198ms로 반복되는 2초 메인 스레드 정지는 재현되지 않았다.
- 단, 하드웨어 재시험 첫 준비 전환에서는 표시 3295.5ms/준비 3431.8ms가 관찰됐다. 이를 숨기거나 통계에서 없었던 것으로 취급하지 않는다. 이때 Long Task 최대 410ms, DoUpdateLayers 최대 0.568ms, release 왕복 5.9ms였다. trace에는 DedicatedWorker의 TimerFire 3992ms(전환 구간과 일부 겹침), 971ms 및 country-shared-boundary-worker 처리 256ms가 보인다. 첫 사용 시 Worker 작업/경합과 연관된 후보이지만 단일 예외 표본으로 정확한 인과관계는 확정하지 못했다.
- 무옵션 진단은 준비/본 측정 모두 2.65~2.77초 Long Task를 재현했다. 본 측정 DoUpdateLayers 2636.769~2659.241ms, 그 내부 GLES2::ReadPixels 약 2.66초 및 GPU command buffer 대기가 확인됐다. 반면 Worker release는 3.3~4.3ms였다. 따라서 긴 release RPC 왕복을 Core release 계산 비용으로 해석하는 것은 틀리며, 이 환경에서는 소프트웨어 합성기의 동기 readback이 응답 처리를 막은 것으로 trace가 뒷받침한다.
- D3D11 A와 재시험 A의 드라이버가 같고 중앙값이 유사해 첫 실행 순서만으로 결과를 설명할 수 없다. 명시적 SwiftShader B도 합성기가 enabled이므로 무옵션 소프트웨어 합성 경로와 구분해야 한다.

## 데이터/오류 및 시각 확인

모든 완료 실행에서 source/data identity와 Chromium 버전이 일치한다. 날짜별 영토 ID/이름/부모/geometry reference, 전체 현재 문서 geometry, timeline record 개수, 표시된 SVG 경계 path 및 지명 text/좌표를 SHA-256으로 비교했다. 2025-12와 2026-11 각각 반복 및 백엔드 간 해시가 일치하며 visible territorial count는 254다. 실제 화면에서 국경과 국가/도시 지명이 표시됨을 스크린샷으로 확인했다. 이는 이 뷰포트와 현재 문서/표시 지명 범위의 검증이며 전체 지명 카탈로그 또는 모든 줌 단계 검증은 아니다. PNG는 드라이버별 안티앨리어싱이 다를 수 있어 바이트 동일성 기준으로 사용하지 않았다. 페이지 오류는 0건이다.

## 후속 최적화 대상

1. 성능 실행 환경에서 GPU compositing/rasterization 및 실제 renderer를 필수 증거로 유지하고, 소프트웨어 합성기 readback 비용과 WebGL 소프트웨어 렌더러 비용을 구분한다. 무옵션 지연만을 근거로 Core release를 최적화하지 않는다.
2. 실제 GPU의 남은 약 0.8초 전환에서 Worker 메시지 처리와 메인 HandlePostMessage 160~198ms, map-render-coordinator의 프레임 처리(관찰 표본 약 56~62ms)를 다음 프로파일 대상으로 삼는다. 이 trace만으로 특정 함수 내부 원인을 확정하지 않는다.
3. 최초 연도 전환 예외는 country-shared-boundary-worker의 기존 배경 작업과 첫 사용 준비의 스케줄링/재사용을 분리 측정한다. 본 W1에서 최적화 코드를 수정하지 않았다.

## 재현 및 증거

기준 커밋에서 instrumentation.patch를 기존 테스트에 적용하면 측정 전용 변경을 재현할 수 있다. instrumented-benchmark.spec.mjs는 정확한 보조 진단 포함 소스이며 원래 tests/browser 위치 기준 import다. analyze.mjs는 tools/w1-windows-gpu-analyze.mjs 위치 기준 import다.

실행: PANDOLAB_TEST_PORT=4187로 tests/browser/server.mjs를 먼저 시작하고 준비 완료를 기다린다. 같은 환경에서 pnpm exec playwright test tests/browser/viewer-gpu-backend-cross.spec.mjs -g 'same-host GPU/backend' --workers=1 --retries=0 --trace=off --reporter=list. 보조 진단은 PANDOLAB_W1_ROUNDS=2와 -g 'W1 unforced backend diagnostic'. node tools/w1-windows-gpu-analyze.mjs로 분석한다. 수집 trace categories는 devtools.timeline, blink.user_timing, cc, gpu. 해시/화면 검사는 준비 완료 후 수행해 측정 구간에서 제외했으며, 모든 모드는 동일한 trace 계측을 사용한다.

report-win32.json, analysis.json, console.log, 4개 gzip Chromium trace, 8개 스크린샷, unforced.json과 보조 로그가 원시 근거다. initial-unforced-aborted.log는 설정 오류 발견 후 2개 준비 표본에서 중단한 진단이며 A-B-A 본 표본에 합치지 않았다.

## 기존 작업 보존

work/ui의 기존 수정 5개를 ../recovery에 복사하고 manifest의 SHA-256으로 재확인했다. 충돌한 기존 WASM과 manifest는 그 복구본에 보존하고 원격 브랜치의 짝을 측정했다. AGENTS.md, docs/branch-policy.md, pnpm-lock.yaml의 기존 바이트는 그대로 유지했다. 복구본은 다른 작업의 미완성 자료라 본 완료 범위에 발행하지 않는다. 라이브러리 runtime pin은 동기화한 브랜치의 핀이며 보고서 발행으로 변경하지 않는다. main 통합/배포는 수행하지 않았다.
