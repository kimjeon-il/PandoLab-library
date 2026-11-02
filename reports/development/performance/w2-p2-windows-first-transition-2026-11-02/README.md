# W2-P2 Windows 최초 연도 전환 정밀 분석 — 2026-11-02

## 1. 판정과 환경

재현된 지연의 임계경로와 공유국경 패킷의 인과관계는 확인했다. **W1 원표본의 추가 2,119ms 전체를 요청 ID별로 소급 분해한 것은 아니므로, 요청의 엄격한 완료 판정은 미완료로 남긴다.** 원본에는 내부 단계 마커와 메시지 ID가 없으며 새 측정값을 원본의 실측값처럼 대입하지 않는다. 본 보고서와 증거 묶음은 현재 조사 결과의 확정판이다.

- 측정 소스: `69a34dceccdf4b348dfaaab79fa5dc712a169e53`, 격리된 detached worktree `D:/dev/worktrees/w2-p2-diagnostic`.
- runtime pin: `5eb7be55208efaafe39bd5a65ec2f111d70b9053`, 브라우저 data identity: `data-f50b7f480c812df6f5ea0c40f5461ab0`.
- W1 자료: library `fd58c91c2bb944e338c026add222788373ba2ffd`. analysis/report/하드웨어 trace 2개의 원본 SHA-256을 해당 revision의 archive index와 대조했다. `w1-original-verification.json` 참조.
- Windows NVIDIA GTX 1650, driver `32.0.16.1088`, Chromium `151.0.7922.34`, headless, ANGLE D3D11, GPU compositing enabled. 실제 Viewer WebGL2 unmasked renderer와 SystemInfo를 각 실행에 저장했다.
- 1280×800, DPR 1, ko-KR, Asia/Seoul. 2026-11 ↔ 2025-12. B는 명시적 SwiftShader이며 compositing은 enabled다. W1의 무옵션 소프트웨어 compositing 정지와 혼동하지 않는다.
- 기존 W2 보고서와 audit을 먼저 읽었다. 당시 추적 `origin/work/ui`의 관련 Worker/renderer 5개는 W1과 동일했고 Viewer 조합부 등은 변경되어 있었다. 최신 코드로 원인을 추측하는 대신 W1 커밋을 직접 실행했다.

## 2. 표본과 계측 영향

주 분석은 38 browser/context 실행, 104회 완료 전환이다. 이 중 A-B-A의 하드웨어 콜드 시작은 10회이며, 충분히 예열한 하드웨어 전환 20회를 별도로 확보했다. A 5 cold → B 2 준비+8 측정 → A 5 cold 순서다. 통제 삼중 비교는 Worker/메인 각각 3세트, 총 18 cold 실행 36전환이다. 추가 최소 계측 3회, profile 없는 단계 계측 3회, stale 검사와 정확한 지연 ID 확인 실행도 포함한다.

처음의 plain 3회와 연결 검사 smoke는 주 분석에서 제외했다. plain 초기 recorder의 wallToReady는 해시 검사 시간까지 포함해 계측 영향 비교에 부적합했기 때문이다. 이후 minimal 실행에는 W1과 같은 요청/승인/ready 마커만 넣어 다시 측정했다. 연결 검사에서는 SVG가 별도 interaction 계층에 있어 지명 개수 단언이 실패했으며, 실제 화면은 정상이었다. 실제 `svg text` 및 부모 transform을 검사하도록 수정했다. 이 설정 실패를 제품 오류나 정상 성능 표본으로 세지 않는다.

|구간|최초 표시 ms|복귀/예열 표시 ms|해석|
|---|---:|---:|---|
|W1 원본 정상/이상|1176.5 / 3295.5|—|차이 2119.0ms는 기존 관찰값|
|A 최초 5회, profile 포함|3450.8–4057.3|약 856–1208|5회 모두 느린 경로|
|A 재시험 최초 5회|1234.5–3401.2|약 857–886|재사용 정상 4회, 느린 경로 1회|
|A 재시험 예열 20전환|839.2–881.8|동일|안정적 예열 경로|
|minimal 3회, profile/단계계측 없음|3191.0 / 3224.7 / 1179.6|776.5–789.5|지연은 profile 때문에만 생기지 않음|
|thin 3회, 단계계측·profile 없음|3291.1 / 3129.6 / 1169.5|774.1–794.9|1초 패킷 구간을 비-profile trace에서도 관찰|

CPU profile 포함 복귀가 minimal보다 느려지는 계측 영향이 있다. 따라서 profile 표본의 빈도나 수치를 실제 사용자 전체의 발생률로 일반화하지 않는다. 콜드는 새 browser process와 새 context 기준이다. OS 파일 캐시·드라이버 캐시를 제거하지 않았다.

## 3. 단계별 실행과 크기

대표 이상 `A-0`의 요청→표시 3517.9ms와 정상 `A2-0` 1303.7ms를 비교한다. 새 차이 2214.2ms를 W1 원본의 2119.0ms와 동일한 측정이라고 주장하지 않는다. 아래 상대 시각은 A-0의 전환 요청 기준이다. 요청 3/세대 1은 이전 startup, 요청 5/세대 2는 새 전환이다. 품질은 canonical이다. 각 trace mark의 CDP ts가 공통 시계이며 Worker performance.now의 원점을 직접 비교하지 않았다.

|요구 단계|실측/관찰|상대 시각·시간 또는 한계|
|---|---|---|
|1 요청 생성|request-build|+1172.314→1172.588ms, 0.274ms. allocation 전 counter 4, 직후 post의 할당 ID 5와 연결|
|2 postMessage·입력 전송|main-post|+1172.658→1416.430ms, 243.772ms, 국가 254개|
|3 Worker 수신·대기|worker-receive/dequeue|공통 ts로 post/dequeue 연결. digest 시작 +1761.056ms. 내부 clone/역직렬화와 queue 대기의 완전한 분리는 불가|
|4 Core/WASM·모듈 초기화|core-load/module-load/modules-awaited|startup 초기 span 보존. 새 요청에서는 이미 완료된 모듈을 기다림. 초기화 시간을 다시 전환 비용에 더하지 않음|
|5 전체 국가 SHA|digest-all/encode/sha|새 요청 +1761.056→1879.654ms, 118.598ms. feature별 encode bytes·SHA 호출 마커 보존|
|6 캐시|cache-fetch/decompress/parse, state cacheHit|대표 요청 cacheHit=false. 해당 캐시 fetch/decompress/parse는 실행되지 않아 0회/N/A. state의 prepared geometry 재사용과 구분|
|7 state replace/patch|state-replace|+1879.669→1880.152ms, 0.483ms. topology 상태는 재사용됨|
|8 packet 계산|packet|+1884.352→2916.424ms, 1032.072ms|
|9 결과/TypedArray·post|packet/result-post|packet mark의 bytes는 본 stroke의 3개 buffer 합계(전체 JS/outline payload의 크기가 아님). post +2921.278→2989.573ms, 68.295ms|
|10 메인 수신|main-receive|+3075.841→3084.391ms, 8.550ms|
|11 pending 생성|pending|+3075.886→3075.918ms, 0.032ms|
|12 promote|promote|첫 시도는 업로드 대기. 최종 +3441.731→3452.001ms, 10.270ms|
|13 stroke 준비·업로드|stroke-upload|첫 ensure 호출 0.165ms, 마지막 0.049ms. 이는 enqueue/호출 시간이며 GPU 실행 총시간이 아님. prepared=false→true와 대기 구간 보존|
|14 publish|boundary-published|최종 승격 뒤 현재 세대 패킷 게시|
|15 temporalFrameReady|gate/readiness-sample|canonical mesh·physical·terrain과 boundary의 개별 상태 보존. 마지막까지 pending boundary가 남는 표본 확인|
|16 onPresented|transition presented|+3517.9ms. OS 디스플레이의 광자 시점이 아닌 기존 승인 콜백 기준|

데이터 크기는 feature 수, digest 입력 UTF-8 bytes, TypedArray byteLength 등 관찰 가능한 단위를 사용한다. 브라우저 내부 structured-clone wire bytes나 단계별 추가 할당량은 얻지 못했으며 임의로 추정하지 않았다. 원시 JSON의 semanticBytes 약 13.52MB는 정확성 비교용 snapshot 크기이며 Worker 전송량으로 오인하면 안 된다.

## 4. 971ms TimerFire 대응 구간과 직접 원인

A-0의 새 요청 TimerFire는 +1884.258ms에 시작해 1032.218ms 걸렸으며, 내부 packet 계산 1032.072ms와 거의 일치한다. main-2-delay에서는 같은 대응 구간이 964.822ms다. `yieldToMessages()`의 timer callback이 Promise를 풀고 continuation이 `prepareCountrySharedBoundaryPacket()`을 실행하는 경로다. A-0의 yield 예약 대기 최대는 5.937ms다. **약 1초를 setTimeout 스케줄링 지연이라고 해석하는 가설은 반증된다.**

CPU profile은 `prepareStrokePacket ← prepareCountrySharedBoundaryPacket` 경로와 `wasm-to-js`, `toHandle`, `__emval_invoke`, `__emval_set_property` 등에 집중된다. 예를 들어 A-0의 해당 packet 구간 leaf sample은 wasm-to-js 약 144.8ms, anonymous 약 70.4ms, toHandle 약 64.8ms다. 샘플 시간은 근사치이며 이 값들을 native 계산 시간과 중복 합산하지 않는다. 소스상 이 경로는 compiled `boundaryAssembleStrokePacket()`와 JS 객체/TypedArray 준비를 포함한다.

느린 경로에서는 초기 세대 1의 긴 packet 작업 꼬리가 입력 후 +1410.5ms까지 이어졌다. 그 전체 4166.6ms를 전환 비용으로 더하지 않는다. 뒤이어 새 세대 요청 5가 들어와, state/topology는 0.5ms에 재사용했지만 packet은 약 1초 재생성했다. 이전 요청 3의 결과는 +1543.7ms 수신 뒤 pending으로 승격되지 않았다. 정상 A2-0은 새 boundary Worker replace가 없고 기존 준비 결과를 사용했다.

따라서 재현된 추가 지연은 **startup 작업과 첫 전환이 겹치는 경로 → 새 세대의 전체 snapshot 재전달/해시 → 준비 상태 재사용 후 stroke packet 재생성 → 현재 패킷의 GPU 준비/게시 대기**에서 발생한다. 서로 겹치는 구간이 있으므로 단계 duration을 단순 합산해 2214.2ms 또는 원본 2119ms에 맞추지 않는다.

## 5. 인과관계 통제와 마지막 필수 조건

Worker 결과 전송에 1000ms를 넣은 worker-0 세트의 첫 표시는 정상 3325.9 → 지연 4446.9 → 복구 3415.5ms였다. worker-1도 지연 실행 4422.4ms를 기록했다. worker-2-delay는 이미 준비된 결과를 재사용해 지연 지점을 지나지 않았고 1287.7ms였다. 이를 성공적인 지연 삽입 표본으로 세지 않는다.

세대별 여러 패킷이 존재하므로 지연은 startup 요청과 새 전환 요청에 각각 걸릴 수 있다. 1초를 두 번 넣었다는 이유로 결과가 반드시 2초 늘어난다고 계산하지 않는다. 겹치는 준비와 취소를 trace에서 구분한다.

V4의 profile 없는 `main-exact-delay`에서는 현재 요청 5/세대 2/packet key `country-shared-boundary:2:5`에 대한 메인 hold가 +2652.904→3657.077ms였다. 현재 패킷은 +4049.359ms에 publish되고, +4108.1ms에 표시됐다. +3991.8ms 및 +4038.8ms의 관찰에서 canonicalMeshReady=true, physicalReady=true, terrainReady=true이고 pendingBoundary=true였다. 따라서 해당 표본에서 canonical mesh나 지형 대신 **공유국경의 prepared stroke/publish가 마지막 필수 조건**이었다. 조건을 해제하거나 이전 연도의 경계를 새 패킷으로 위장하지 않았다.

V2 통제의 main-control 종료 마커는 당시 전역 current 요청을 읽어 원래 시작 요청과 ID가 달라질 수 있는 계측 한계가 있었다. 이를 숨기지 않는다. V4는 controlId와 시작 시 metadata를 캡처하고 profile 없는 추가 실행으로 재확인했다. V1~V4의 실제 제공 소스를 각각 보존했다.

## 6. 가설 A~F

|가설|판정 및 반증|
|---|---|
|A 초기 WASM/모듈 로딩|startup 비용은 존재. 재현된 새 세대의 1초 구간은 이미 초기화된 모듈의 packet 계산이므로 직접 원인으로 기각|
|B 국가 SHA 반복|새 replace에서 254개 전체 SHA가 다시 실행됨. 대표 약 119ms로 일부 기여. 예열/재사용에서 매번 boundary SHA를 수행하는 것은 아님|
|C 캐시 미사용으로 전체 국경 재계산|대표 초기 요청은 compressed cache 미사용이며 topology 비용이 존재. 그러나 새 세대의 state.replace는 0.483ms이므로 그 단계에서 전체 topology를 다시 계산했다는 설명은 기각. packet 재생성은 별도|
|D setTimeout/재개 지연|대표 yield wait 최대 수 ms. 971ms 대응 TimerFire는 Promise continuation의 packet 계산. 1초 스케줄러 대기설 기각|
|E 준비 패킷의 메인/GPU 대기|확인. post/수신 비용과 prepared-resource 대기 구간이 있고, current packet publish를 늦추면 마지막 승인도 지연됨|
|F canonical mesh/terrain이 마지막|위 통제 표본에서 둘 다 준비된 상태에서 boundary가 pending이므로 마지막 병목설 기각. 모든 실행에서 지형 비용이 0이라는 뜻은 아님|

## 7. 정확성·오류·메모리

38개 주 분석 실행의 104회 완료 전환에서 날짜별 semantic SHA가 일치했다. 현재 문서 영토 객체/국명/상하 관계, 전체 geometry, timeline record, 실제 SVG 지명 텍스트·부모 transform 및 위치를 비교했다. 현재 카메라의 지명 117/118개와 visible territorial count 254가 관찰됐다. 모든 시점에서 builtin month와 timeline cursor 및 ready를 함께 확인했다. 화면 PNG도 보존했다. 전 세계 모든 카메라/줌 단계나 OS의 실제 표시 timestamp를 검증한 것은 아니다.

페이지 오류와 console warning/error는 주 분석에서 0건이다. safety-exact는 현재 metadata를 기준으로 요청 ID/프로젝트 세대/geometry revision/quality 중 **하나씩만** 틀린 응답 4개를 실제 consumer에 전달했고 모두 거부됐다. 문서 상태/월/visible count는 변하지 않았다. 집중 회귀 4개는 실제 Worker의 급속 교체·삭제, 동일 입력 재사용, 상하 관계 변경, 새 세대에 의한 temporal wait 취소와 stale frame 거부를 검증해 모두 통과했다. 새 프로젝트 열기/실패 복구의 전체 UI 시나리오까지 별도로 실행한 것은 아니다.

Worker target 수는 대표 실행에서 시작/종료 모두 7개였다. 추가 native 메모리 계측 실행은 browser.close 뒤 기록한 browser-owned PID가 모두 사라졌음을 확인했다. A2-4 예열 20회에서 main JS heap 표본은 약 113.2→172.1MB였다. thin-0은 143.6→188.4MB였다. GC 강제 실행, Worker별 live heap, GPU 메모리의 장기 plateau 검증은 하지 않았다. 이 증가만으로 누수라고 하거나 누수가 없다고 확정하지 않는다. raw JSON에 Performance metrics와 가능한 Windows working/private bytes를 보존하며 서로 더하지 않는다.

## 8. W2-P3 최적화 후보

|우선순위|후보|관찰 기반 기대 이득/위험|
|---|---|---|
|P1|기존 boundary 준비 소유자에서 최종 stroke packet의 동일 입력 재사용 범위 검토|느린 경로의 packet 약 1초가 상한 후보. 품질/geometry/owner hierarchy를 정확히 인증해야 하며, transferred buffer의 detach와 메모리 보유 비용을 처리해야 함|
|P1|초기 준비와 새 세대 요청의 supersession/우선순위 검토|이전 packet 꼬리 약 1.4초 중 실제 임계경로 부분만 후보. 준비 상태를 버리거나 이전 정상 지도를 지우지 말 것. 이미 필요한 startup 작업을 무조건 취소하면 역효과|
|P2|compiled packet 경계의 JS 객체 marshalling/TypedArray 계약 정리|약 1초 구간의 bridge sample이 근거. 전체 1초 제거를 보장하지 않음. native/shared renderer 결과와 buffer 수명 회귀 위험|
|P2|정확한 immutable 입력에 대한 digest/전달 재사용|대표 SHA 약 119ms 및 main post 약 244ms가 후보 상한. 복사 객체 identity나 형상 version만으로 안전성을 추정하면 안 됨|
|P3|stroke upload 준비·프레임 스케줄 대기 프로파일 보강|대표 pending 수신→최종 게시 약 376ms 중 임계 부분. GPU 호출 시간 0.1ms를 전체 비용으로 오인하거나 준비 게이트를 우회하지 말 것|

위 이득은 서로 겹쳐 합산할 수 없다. 어떤 최적화도 본 단계에서 적용하지 않았다.

## 9. 재현과 증거 구조

`tools/w2-p2-server.mjs`, `w2-p2-instrument.mjs`, `w2-p2-run.mjs`, `w2-p2-analyze.mjs`가 진단 도구다. W1 detached checkout과 기존 ui node_modules/동일 runtime materialized cache를 재사용한다. 원본 product 파일은 변경하지 않고 buildFrontendSnapshot의 readSourceBytes로 테스트 응답에만 계측한다. server source/data identity guard와 실행별 GPU identity 검사를 유지한다.

실행 순서는 server 시작 → 준비된 4190/4191 확인 → run baseline → run control → run calibration → run safety/exact → analyze다. `PANDOLAB_W2_EVIDENCE`에는 이 보고 범위의 편집 디렉터리를 지정한다. 서버의 계측 버전은 시행 중 보강되어 실제 emitted source를 instrumented-v1~v4에 남겼다. 현재 도구로 재실행하면 최신 V4 계측이며 최초 V1과 계측량이 같다고 주장하지 않는다. baseline 결과의 첫 plain 3회는 앞서 설명한 이유로 비교에서 제외한다.

개별 실행 JSON/PNG/gzip Chromium trace, phase별 console와 results, stage-analysis.json, 정확성/시계 정렬 근거, focused-unit.log, 원본 W1 verification, 재현 스크립트를 함께 보관한다. CPU profiler는 Profile/ProfileChunk와 공통 trace clock으로 읽으며 sample delta는 근사치다. 내포 span과 callback/continuation 시간은 중복 합산하지 않는다.

## 10. 남은 제한과 보존

원본 W1의 971ms 안에 들어간 함수를 새 측정 대응 구간처럼 직접 입증할 CPU profile/ID는 원본에 없다. 새 재현은 해당 구간의 함수·재계산·마지막 gate를 입증하지만, 원본 2119ms의 유일한 세부 분해를 확정하지 못했다. 따라서 W2-P2를 무조건 완료라고 표시하지 않는다. 후속 범위는 원본과 동등한 희소 마커로 자연 이상치를 추가 확보하고, 장기 메모리 plateau 및 프로젝트 열기/실패 복구의 화면 검증을 보강하는 것이다.

기존 ui의 AGENTS.md, branch-policy.md, pnpm-lock.yaml, WASM/manifest 바이트를 그대로 보존했다. 진단 워크트리의 tracked 소스도 clean 상태다. 해당 예외 worktree는 승인 없이 제거하지 않으며 현재 증거 재현 경로로 보존한다. 공유 node_modules와 ui의 runtime 캐시는 현재 pin과 재현 도구의 소비자이므로 유지한다. 원시 trace/profile/PNG는 고유 검증 증거이며 재생성 가능한 임시 빌드 사본으로 취급하지 않는다. main 통합과 공개 배포는 수행하지 않았다.

保管補足: 진단 worktree의 tracked 소스는 3,692개, 논리 크기 81,477,838 bytes다. 현 호스트 재현 경로이므로 보존하며 자동 삭제하지 않는다. 보고 범위는 약 255MB의 고유 trace/profile/화면/버전별 진단 소스와 batch 완료 증거다. 재실행은 새 보고 편집 하위 디렉터리를 사용해야 하며 현재 runner는 기존 실행 이름의 JSON/PNG/trace 덮어쓰기를 거부한다. phase results는 배치 완료 및 개별 원시 결과와의 일치 검증에 사용한다.
