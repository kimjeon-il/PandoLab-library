# W2-P4-2 Windows GTX 1650 실GPU 인과관계 검증

> 날짜: 2026-11-02 · 소스: fe8282ba32761ab9586348d1712e11cc1f4e7882 · 데이터 핀: 5eb7be55208efaafe39bd5a65ec2f111d70b9053 · 데이터 식별: data-f50b7f480c812df6f5ea0c40f5461ab0

Windows Chromium 151.0.7922.34, NVIDIA GeForce GTX 1650 driver 32.0.16.1088, WebGL2 ANGLE D3D11, gpu_compositing enabled, 1280×800 canvas 1280×752 DPR 1, ko-KR / Asia-Seoul. 모든 주 표본은 브라우저의 SystemInfo.getInfo와 실제 WebGL renderer 및 데이터/소스 식별을 검사했다. 각 실행 JSON에 원본이 있다.

제품 소스나 GIS는 변경하지 않았으며 고정 소스의 메모리 snapshot에만 계측과 실험용 step 제한을 적용했다. A/B/A2의 step 상한은 256KiB/1MiB/256KiB, 전체 frame의 2ms/2MiB 제한과 입력 보호, temporalFrameReady gate는 유지했다. p90은 선형 보간이며 n10으로 p95/p99를 확정하지 않는다. 새 브라우저 process가 콜드의 정의이며 OS 파일 캐시는 제거하지 않았다.

## 최초 전환과 국경 업로드

| 조건 | 표시 p50 ms | p90 | 최대 | >2.5초 | 최초 cache hit 수 | hit 수신→게시 p50 ms | scheduler 단계 p50 | 실제 stroke upload bytes p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 2198.8 | 2468.4 | 2805.4 | 1/10 | 6 | 375.7 | 23.0 | 5426656.0 |
| B | 2813.4 | 3284.6 | 3776.9 | 8/10 | 8 | 112.0 | 7.0 | 5426656.0 |
| A2 | 2230.3 | 2447.6 | 2451.4 | 0/10 | 9 | 378.1 | 23.0 | 5426656.0 |

표시 통계는 느린 표본과 메인 렌더러 재사용 표본을 포함한 각 10개 전체다. 수신→게시와 업로드 수치는 실제 Worker cache hit 표본에만 적용한다. glBytes는 country-shared-boundary 요청의 gl.bufferSubData 인자 바이트 합계이며 Worker 응답의 6.63MB와 같다고 가정하지 않는다. CPU 호출과 GPU 실행 시간은 다르다. 프레임 step 끝 마커는 publish 직후 기록될 수 있어, 같은 scheduler의 즉시 완료 마커를 포함한다. 단계별 원시 값은 p4-analysis.json 및 각 trace에 있다.

최초 전환 중 main Long Task 최대는 A 427.0ms, B 492.0ms, A2 402.0ms다.

| 조건 | 예열 전환 수 | 표시 p50 ms | 표시 p90 ms | 최대 main Long Task ms |
| --- | ---: | ---: | ---: | ---: |
| A | 20 | 945.4 | 1197.0 | 224.0 |
| B | 20 | 793.5 | 849.4 | 176.0 |
| A2 | 20 | 812.2 | 840.3 | 179.0 |

cache hit 표본의 국경 리소스 계측 p50. callback 간격은 선택된 업로드 프레임 사이 시간이며 별도의 전체 display FPS 측정은 아니다. GL API 시각은 CPU 호출 구간이며 GPU device 실행시간 측정값이 아니다. GPU timer query는 수집하지 않아 실제 GPU 실행시간은 미확정이다.

| GPU 단계 | A | B | A2 |
| --- | ---: | ---: | ---: |
| CDP FireAnimationFrame 매칭 수 | 23.0 | 7.0 | 23.0 |
| 최대 업로드 callback 간격 ms | 17.5 | 17.6 | 17.6 |
| 25ms 초과 callback 간격 수 | 0.0 | 0.0 | 0.0 |
| instances bytes | 3008160.0 | 3008160.0 | 3008160.0 |
| nodes bytes | 2418496.0 | 2418496.0 | 2418496.0 |
| bufferSubData 호출 수 | 22.0 | 11.0 | 22.0 |
| bufferData 호출 수 | 2.0 | 2.0 | 2.0 |
| GL API 호출 CPU 합계 ms | 0.9 | 0.6 | 0.7 |
| 최장 scheduler step ms | 7.6 | 7.6 | 8.0 |
| resource ready→publish ms | 7.1 | 7.1 | 7.6 |

## 메시지 수신 및 첫 준비 단계

| 구간 (cache hit) | A p50 ms | B p50 ms | A2 p50 ms |
| --- | ---: | ---: | ---: |
| 요청→Worker post | 1101.8 | 1149.2 | 1143.6 |
| main post 호출 | 219.5 | 223.5 | 208.0 |
| post 반환→Worker listener 시작 | 0.0 | 817.0 | 0.0 |
| 해당 대기 중 이전 packet 준비 겹침 (관측된 경우) | 미측정 | 816.7 | 미측정 |
| Worker event.data 최초 접근 | 243.3 | 249.1 | 235.8 |
| Worker 결과 post 호출 | 59.8 | 59.1 | 54.2 |
| 결과 post 반환→main listener 시작 | 0.0 | 0.0 | 0.0 |
| main event.data 최초 접근 | 60.2 | 57.5 | 57.9 |
| main 수신→국경 게시 | 375.7 | 112.0 | 378.1 |

각 첫 마커는 event.data에 접근하기 전에 찍고 같은 수신 순번·스레드의 뒤 마커와 연결했다. event.data 접근 구간에는 마커·필드 읽기 비용이 포함된다. listener 시작 이전 시간은 엔진 복원과 스케줄링을 추가 분리하지 못한다. 양방향 post 반환→listener 값이 음수면 양쪽 실행이 겹친 것이며 음의 큐 시간이 아니다. 공통 CDP 단조 시각을 사용하며 중첩 span을 합산하지 않는다.

이전 packet 준비가 같은 Worker 스레드에서 관측된 표본 수는 A/B/A2 각각 0/8/0개다. 관측되지 않은 표본을 0ms로 대체하지 않았다.

B의 cache hit 8개 모두에서 post 반환 이후 같은 Worker 스레드의 이전 packet 준비가 겹쳤다. 그 겹침의 중앙값 816.7ms는 listener 시작 전 대기 중앙값 817.0ms의 대부분이다. 해당 packet 구간은 동기 처리이므로 진행 중 같은 Worker의 다음 메시지 핸들러가 실행될 수 없다. B가 왜 이전 준비와 더 자주 겹쳤는지의 상위 경로는 별도 조사 대상이다.

측정 중 A와 B 일부 표본에 중간 trace 분석 프로세스가 겹쳤다(interim-analysis-overlap.json). 모든 표본을 보존하고 제외하지 않았으며 부하 교란 가능성을 고려해 A/B 전체 표시 차이를 일반적인 개선율로 단정하지 않는다.

별도 v3 계측 process 3회에서 첫 전환 전 prepare 경로를 관찰했다. 병렬 및 중첩 함수 p50을 합산하지 않는다. source cache 정보와 개별 span은 early-analysis.json에 있다.

관측된 foreground source cache hit/miss는 0/3회다.

| 계측 단계 | 관측 수 | wall p50 ms |
| --- | ---: | ---: |
| candidate-prepare | 3 | 911.9 |
| physical-prepare | 3 | 0.4 |
| core-source | 3 | 415.8 |
| core-candidate | 3 | 132.6 |
| core-adopt | 3 | 23.6 |
| generation | 3 | 1.1 |
| presentation-catalog | 0 | 미측정 |
| replace-accepted | 3 | 1280.3 |
| country-io | 3 | 87.1 |

## 별도 전송·입력 실험

254개 국가 snapshot을 별도 진단 Worker에서 객체→UTF-8 transferable→객체 순서로 각 10회 왕복했다. 모든 응답 JSON SHA가 같았다. buffer 수치는 양방향 인코딩/디코딩을 포함하고 제품 지도 전환 개선율이 아니다. JSON 크기는 13308801 bytes.

| 방식 | n | 왕복 p50 ms | main 인코딩 p50 | main 디코딩 p50 |
| --- | ---: | ---: | ---: | ---: |
| object | 20 | 930.2 | 0.0 | 75.4 |
| buffer | 10 | 532.4 | 183.1 | 149.6 |

업로드 중 별도 trusted pointer 입력 표본이며 자연 업로드가 없는 경우 진단용 강제 재준비 여부를 JSON에 남겼다. 입력 실험은 성능 분포와 혼합하지 않았다.

| 조건 | 통과 실행 | 이벤트 | 입력 지연 p50 ms | 최대 ms |
| --- | ---: | ---: | ---: | ---: |
| A | 3/3 | 36 | 0.3 | 357.0 |
| B | 3/3 | 36 | 0.3 | 1.0 |
| A2 | 3/3 | 36 | 0.3 | 348.3 |

## Trace 대조와 메모리

| 조건 | trace 없는 최초 전환 3회 ms |
| --- | --- |
| A | 1727.1 / 2422.5 / 3745.5 |
| B | 2814.5 / 2875.2 / 2608.1 |
| A2 | 2636.6 / 1246.6 / 2300.5 |

별도 process의 예열 연속 20회에 대해 GC 전/후 및 Worker/WASM, private bytes를 수집했다. 아래는 GC 후 MiB이며 각 지표는 중복될 수 있다. 원본 JSON의 전/후와 10/20회 checkpoint 및 종료 PID를 확인한다.

| 조건 | main JS 0→20 | boundary JS 0→20 | boundary WASM @20 | private 0→20 |
| --- | --- | --- | ---: | --- |
| A | 118.9 → 120.5 | 129.8 → 129.8 | 69.2 | 1854.4 → 1870.8 |
| B | 118.9 → 120.5 | 129.8 → 129.8 | 69.2 | 1832.9 → 1854.0 |
| A2 | 118.8 → 120.5 | 129.8 → 129.8 | 69.2 | 1850.8 → 1873.9 |

## 정확성 및 안전성

주 표본에서 모든 완료 전환은 국가 객체·속성·형상·timeline·표시 지명과 위치의 SHA 및 월/cursor를 기록했다. W2-P3의 날짜별 SHA와 비교한다. stale 요청/세대/형상/quality 거부, 기존 집중 회귀, Worker error 및 WebGL 복구 결과는 별도 JSON과 검사 로그에 보존한다. 예상치 못한 주 표본 pageerror 및 console error: 0. 대표 PNG 비교의 차이 픽셀 수는 0 / 0다. 원본과 비교 범위는 pixel-comparison.json에 있다.

## 판단 범위와 후속 분석

같은 stroke upload bytes에서 B의 수신→게시 wall과 scheduler 단계가 줄고 A2에서 돌아오는지 위 표와 표본별 원시 값으로 판단한다. 전체 표시 p50은 빠른 렌더러 재사용 표본 비율에도 영향을 받으므로 cache hit 조건부 수치와 전체 표본을 함께 봐야 한다. 별도의 입력 지연과 Long Task 결과를 고려해야 하며 이 통제 실험 자체를 제품 최적화로 적용하지 않는다.

스케줄링 인과 판정: **동일 업로드 바이트의 B 단계 수 및 수신→게시 지연 감소와 A2 복귀를 관측하여 지지**. Worker 최초 event.data 접근은 위 표의 직접 측정 구간으로 한정한다. 초기 준비의 중첩 span과 listener 실행 이전의 대기·복원은 상세 인과가 미확정일 수 있다.

조건부 국경 수신→게시 중앙값은 A 대비 B 70.2% 감소했다. 전체 첫 표시 p50은 B가 A보다 27.9% 늘었다. 두 집계의 표본 구성과 부하 조건이 다르므로 이 수치를 더하거나 일반 사용의 보장 개선율로 해석하지 않는다.

CPU packet cache hit가 있었던 요청에서도 국경 GPU resource key는 현재 세대와 요청 ID를 포함하고 실제 bufferSubData가 다시 발생했다(p4-analysis.json의 resourceKey). 장치 자원 재사용 후보를 보여 주지만, source/형상/소유·quality·outline의 정확한 동일성과 새 세대 승인, 취소·rollback·context loss를 보장하지 않은 재사용은 허용할 수 없다. B의 상한 변경도 최종 제품 방안이 아니며 첫 전환 전체가 실제로 개선됐다고 판정하지 않는다.

기존 W2-P3 최종 기록은 라이브러리 84d68e4e462457fd0e3d7c86a2088aa081b9b562, W2-P4-1 분석은 Pando cc092f19이며 본 작업은 원문을 수정하지 않았다. 주 A/B/A는 v2 snapshot, 초기 세부 단계만을 위한 추가 표본은 v3 snapshot이다. 각 emitted source, 원시 JSON, gzip Chrome trace, PNG 및 재현 스크립트는 이 scope에 저장한다. 최종 작업과 최적화 대상 결정은 W2-P4-3에서 다룬다.
