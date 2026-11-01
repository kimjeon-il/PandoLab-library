# P5-7 — 네이티브 C++·WASM 동등성 및 실패·복구 검증

> 보고서 ID: `DEV-NATIVE-P5-7-20261101` · 상태: `verified` · 지도 자료 반영: `not-applied`  
> 날짜: 2026-11-01 (KST) · 검증 단계: P5-7만 완료  
> 시작 커밋: `00b8ac42a679e88b404756a7dbec6b080007b4ba`  
> 검증·반영 커밋: `aacf43ec4c41948e8c610e30cae56532a80d3f92` · 브랜치: `work/ui`

## 결론

동일한 고정 입력을 실제 네이티브 C++ `DocumentSession`과 검증된 WASM `DocumentSession`에 공급했다. 다섯 시나리오에서 API 결과 **328회**가 일치했고, 기존 Worker 취소·늦은 응답 계약 **6개**도 통과했다. 동등성 검사 5개와 Worker 검사 6개 모두 실패·취소·건너뜀 0개다.

생산 C++·WASM·Viewer 코드는 수정하지 않았다. 새 검증 파일 네 개를 work/ui에 추가했으며, main 병합·사이트 배포·P6 실행은 하지 않았다.

## 근거와 실행 환경

- [검증 커밋](https://github.com/kimjeon-il/Pando/commit/aacf43ec4c41948e8c610e30cae56532a80d3f92)
- [CI 실행 41259763808, attempt 1](https://github.com/kimjeon-il/Pando/actions/runs/41259763808)
- [검증 job 124710425959](https://github.com/kimjeon-il/Pando/actions/runs/41259763808/job/124710425959)
- GitHub Actions Ubuntu 24.04, GNU C++ 13.3.0, Node.js 24.22.1.
- 실행 시각: 2026-11-01 10:07:59~10:10:03 KST.
- WASM: ABI 1, Emscripten 4.0.20. 기존 커밋된 JS/WASM/manifest 쌍을 사용했으며 이번 단계에서 다시 빌드하지 않았다.
- C++ 소스 입력 156개의 정규화된 해시로 만든 식별값:
  `fb6f8c79c19b0f786632b3a494c700373c2cf5a1d41f0e68c5a23c87475ea043`.
- JS SHA-256: `008ce95293a0a291fac586e95e6ec3c9d4684a92a0d552ea60eaca421355b895`.
- WASM SHA-256: `9671907356ac4b00d1f3bbb10a4a4ed85362b57c8c7d34a530d9ce20e32a70d5`.
- 고정 입력 9,835 bytes, SHA-256:
  `e09c1abac27ceb1d0a7cb6035a8fab228bb5314c319ed97e962bac1109999e60`.

원시 기계 판정은 [summary.json](summary.json), 로컬 네이티브의 네 시점 출력은 [native-fixture-output.jsonl](native-fixture-output.jsonl)에 보존했다. 전체 CI 로그와 아티팩트는 위 실행 링크에 연결되어 있다.

## 비교 방법

동일한 현재 형식의 저장 바이트·자료 개정·manifest pin·목표 월·document ID를 두 실행 환경에 전달했다. 검증용 네이티브 어댑터는 Core를 직접 호출하고 결과를 JSON으로 운반하며, 시간 조회·기하·이력·복구 규칙을 별도로 구현하지 않는다.

비교 대상은 전체 상태, 저장 스냅샷, 형상 좌표와 버전, 객체 집합, 존속기간, 국명·색·국기, 부모·루트·조상 관계, 선택, hover, 그리기 초안, Undo/Redo 이력이다. 형상 좌표가 포함되지 않는 world hash만으로 동등성을 판정하지 않았다. 중복 객체도 별도로 거부한다.

기존 전체 baseline 적재 경로와 새 후보 채택 경로도 대조했다. 기존 WASM baseline 경로가 생성한 새 document ID를 읽어 네이티브와 후보 경로에 동일하게 전달하므로, 비교에서 문서 ID를 제거하지 않았다. 복구 시에는 의도적으로 증가하는 epoch만 별도로 확인한다.

## 고정 시점의 기대값

이 자료는 실제 역사 자료가 아닌 작은 합성 fixture이다. 전체 지도나 실제 국가 catalog는 읽지 않았다. 현재 Core가 월말 상태를 조회하는 계약을 적용했다.

| 시점 | 독립적으로 고정한 기대값 |
| --- | --- |
| 2026-08 | B 생성 전. A·C와 수계 객체가 존재하고 B·R은 없음. |
| 2026-09 | 9월 15일 생성된 B가 형상 v1·상위 객체 A를 사용. C는 종료일 9월 30일에 존재. |
| 2026-10 | B는 10월 20일 변경된 형상 v2·독립 루트·새 국명·색·국기 없음 상태. C 소멸. R은 10월 31일 하루의 존속기간으로 존재. |
| 2026-11 | B의 새 상태 유지. R과 10월 31일 종료된 수계 객체는 없음. |

형상 v1의 구멍·섬·날짜변경선 좌표를 포함한 전체 스냅샷을 두 환경 및 전체 적재 경로와 대조했다. 형상 v2의 실제 좌표 `1.2345678901234567`를 직접 검사했으며, 별도 메타데이터에 같은 숫자가 있다는 이유로 통과하지 않도록 했다. 한글·이모지·결합 문자가 포함된 국명도 비교했다.

## 실행 결과

| 검사 | 결과 |
| --- | --- |
| 같은 소스·ABI·컴파일러 및 JS/WASM 바이트 확인 | 통과 |
| 시점·객체·형상·속성·관계·전체 적재 경로 동등성 | 통과 |
| 손상된 바이트·크기·schema·pin·월·예산·epoch 거부 및 활성 상태 보존 | 통과 |
| A→B→A, 오래된 후보, 이중 폐기, 파일 열기 이후 이전 epoch 거부 | 통과 |
| 잘못된 채택 영수증·캡슐 거부, 채택 이후 rollback, 실제 Undo/Redo와 재시도 | 통과 |
| 소스 재사용·개정 구분·2개 항목 제한·퇴거·해제·입력 바이트 변경의 격리 | 통과 |
| 기존 Worker 취소·늦은 ACK·순서·공개 계약 | 6/6 통과 |

다섯 동등성 시나리오에서 328회의 쌍별 API 대조가 수행됐다. 실제 Core 거부 20회에서 동일 오류 코드와 상태 보존을 확인했다. 별도로 세션 객체를 실제 파괴한 뒤 검증 어댑터가 추가 호출을 거부하는 경계 1회를 확인했다. 따라서 summary의 오류·거부 21회를 모두 독립적인 Core 오류 종류로 해석하지 않는다.

채택 뒤의 후속 단계 실패는 실제 캡슐의 rollback을 호출해 모사했다. 복구 후 저장하지 않은 국명 수정, dirty 상태, 원래 저장 내용, 선택·hover, 그리기 좌표와 이력, Undo/Redo가 돌아왔고 epoch는 전진했다. Undo→Redo의 저장 내용도 원래 편집 상태와 같았으며, 이후 정상 후보 준비·채택이 성공했다.

소스 예산 검사는 2개 항목 및 64MiB의 선언된 decoded-byte 한도와 해제 계수를 검사한다. 실제 프로세스·WASM 힙·GPU 최대 사용량 또는 누수 부재를 증명하는 검사는 아니다. Worker 검사는 제어 가능한 test double을 사용하는 기존 계약 검사이며, 실제 WASM 실행의 동등성 검사는 별도 다섯 시나리오에서 수행했다.

## 재실행 명령

```sh
cmake -S shared -B build-native/core -G Ninja -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF
cmake --build build-native/core --target pandoeditor_core --parallel 2
c++ -std=c++17 -O2 -Ishared/core/include tests/native/temporal-parity-probe.cpp build-native/core/core/libpandoeditor_core.a -lz -o build-native/core/temporal-parity-probe
node tools/package-shared-core-assets.mjs --build-dir shared/frontend/static/wasm --check
node --test tests/native/temporal-parity-p5-7.test.mjs
node --test tests/unit/core-temporal-transport-p5-5.test.mjs
```

실행 workflow는 Core·바인딩·WASM 및 관련 입력 변경 시 같은 좁은 검사만 실행한다. 새 네이티브 probe는 `shared/` 밖에 두어 테스트 추가만으로 생산 WASM의 소스 식별값을 바꾸지 않는다.

## 변경 파일과 검토

- `tests/native/temporal-parity-probe.cpp`: 네이티브 Core의 JSON-lines 검증 어댑터.
- `tests/helpers/temporal-parity-p5-7.mjs`: 동일 바이트 fixture, 고정 기대값 및 실제 WASM 어댑터.
- `tests/native/temporal-parity-p5-7.test.mjs`: 결과 대조·실패·복구·수명 시나리오와 증거 출력.
- `.github/workflows/core-temporal-parity-p5-7.yml`: 해당 검사만 실행하는 CI.

별도 검토에서 발견한 검증 코드의 채택 인자 필드, 실제 좌표 검사, 중복 객체 검사, teardown 실패의 증거 반영, 관련 입력 변경 시 CI 트리거, 이전 형상을 관찰하는 시점 문제를 실행 전 수정했다. 이들은 생산 코드 결함으로 보고하지 않는다. 최종 CI는 첫 실행에서 모두 통과했다.

## 미실행 범위 및 재개 지점

- 브라우저 프레임·카메라·클릭 판정·GPU 복구·실제 휴대폰·반복 메모리·성능 p95는 이번 P5-7의 판정 범위가 아니다.
- 기존에 유예한 브라우저 타임아웃 2건을 재실행하거나 통과로 바꾸지 않았다.
- 이전 P5-6에서 알려진 구형 read-model fixture 8건의 미통과 기록도 이번에 재실행·해결 판정하지 않았다.
- 전체 GIS 재생성, 전체 테스트, 설치 패키징, main 통합, 사이트 배포는 하지 않았다.
- 다음 소단계는 **P6-1 — 데스크톱 기능 확인**이다. 자동 착수하지 않는다.

## 보관과 판본

이 보고서와 summary·네이티브 출력은 이 작업 범위만 원격 보관한다. 현재 환경의 native Git HTTPS proxy가 연결되지 않아 prescribed `--publish-reports`/`--check-reports` 명령을 실행한 것으로 기록하지 않는다. 연결된 GitHub API로 동일한 현재 identity archive 형식·원문 SHA-256·바이트 수·범위별 원격 읽기 검증을 적용한다. app/data 런타임 pin과 다른 보고서 항목은 변경하지 않는다. API 보관 이후 원격 commit·scope·원문 해시가 일치하는지 별도로 확인한다.
