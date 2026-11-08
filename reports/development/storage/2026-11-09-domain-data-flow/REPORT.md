# Pando 책임 구조·단일 정본·지오메트리 지연 로딩

> 보고서 ID: DEV-STORAGE-20261109-DOMAIN-DATA · 상태: focused-verified · 지도 반영: not-applied  
> 색인일·원문 최종 수정: 2026-11-09  
> 웹 코드: 2a24ac97d024481db4fbd31163c0182b3cee3ae8 / 독립 앱: 해당 없음  
> 자료 pin: c370d4f95e27c6b777239de58d3170171d7379db / 전체 프로젝트 검증·main 통합·배포: 미실행

## 대상과 기준

사용자가 승인한 0~7단계를 기존 UI 상설 작업트리의 work/optimization에서 구현했다. main과 독립 Windows/Android 앱은 수정·배포하지 않았다. 독립 앱은 착수 전 폐기되어 현행 진입점은 Web Viewer다. 기존 work/ui 브랜치, 다른 상설 작업트리와 미추적 gpu-viewer-evidence는 보존했다. 병행 작업의 폐기 검사 삭제도 유지했다. 퇴역 검사 복구, 전체 테스트/네이티브 행렬/전체 GIS 재생성은 하지 않았다.

기준 자료는 a1bc7a5229b252c5b8d9612026cd0ae3e82d7327이다. 로딩 전 측정 코드는 2bb6a621c518af6a4e4d88b10dd6315dc5085b22, 후 측정은 위 최종 코드다. 같은 Windows·GTX 1650 ANGLE D3D11, 1280×800 headless Chromium, 같은 Viewer 준비 완료 조건을 사용했다. 전후 변경은 경로 이동과 데이터 표현·실행 흐름 변경을 포함하므로 개별 최적화의 독립 효과로 해석하지 않는다.

## 단계별 결과

| 단계 | 결과 | 구현·근거 |
| --- | --- | --- |
| 0 계약·기준선 | 완료 | 책임별 이동표, source/native 대조, 배포·로딩 기준선 확보. source 288개 일치, 충돌 0. |
| 1 소스·도구·검사 | 완료 | frontend 783, 도구 78, 등록 검사 402개를 책임별 위치로 이동. 248개 공개 JS 산출물은 이동 체크포인트에서 바이트 일치. CLI 정본을 준비·보관·보고서·발행 책임으로 분리하고 구 전달 파일 제거. |
| 2 native/WASM | 완료 | native 입력 175개 이동. 이동 시 알고리즘/헤더 152개 정규화 바이트 일치. 이후 stage7의 실제 native 로직 변경은 소스 일치 CI 산출물로 검증. |
| 3 목적별 준비 | 완료 | Viewer는 매니페스트 전이 폐쇄만, GIS는 선택 입력, 보고서는 런타임 준비 없이 처리. revision+목적+범위 identity, CAS hardlink 재사용. 미준비 부재를 삭제로 취급하지 않음. |
| 4 편집 정본 | 완료 | source/countries가 유일한 writer 정본. library.json/objects는 명시적 이전 경계에서만 읽고 역동기화 제거. 288개 동일, 0충돌; 합성 충돌·중단·재실행 검증. |
| 5 descriptor/geometry | 완료 | 작성 source 288개, runtime 280개 전체 순서 포함 문서 정확 일치. 해시 검증 불변 payload와 descriptor 분리. 이름 등 메타데이터 변경의 geometry 쓰기 0·해시/URL 재사용은 합성 회귀로 검증. |
| 6 육지·메시 공유 | 완료 | 승인된 결과에서 정확한 Polygon/ring 대체와 이진 메시 델타 생성. 새 역사 형상 추정·좌표 단순화·재삼각분할 없음. 과거→현재→과거 실제 브라우저 확인. |
| 7 전체 문서·지연 로딩 | 완료 | 전체 시대 identity/386개 binding 유지. 현재 월 필요 payload만 준비, 명시적 missing refs·준비 상태·generation/request guard. 전체 시대·편집 형상 포함 저장/오프라인 재열기 native 합성 검증. |

## 정본 저장 흐름

작성 source descriptor → 콘텐츠 해시 불변 좌표 → 정본 생성기 → runtime descriptor+독립 payload → manifest 폐쇄 기반 준비/CAS 읽기 전용 뷰 → canonical C++ document의 전체 시대 메타데이터 → 해당 월 required geometry 조회 → 데이터 계층 무결성 검증 → Core admission → 장면 발행 순서다. source/native 역동기화와 전체 시대 좌표 선로딩은 제거했다. 보관 원본·과거 pin은 그대로 보존했다.

Core admission은 문서 편집·epoch·dirty·Undo 이력을 만들지 않는다. preview 도중 들어온 준비 자원도 confirm/Undo/Redo에서 유지한다. 프로젝트 교체·연속 날짜 변경의 오래된 응답은 현재 문서에 적용하지 않는다. 오류는 누락 참조·무결성·준비 작업 경계에서 명시적으로 전달한다. 일반 프로젝트 저장 형식 v14와 GPKG 입구는 유지하며 builtin 전용 resource catalog를 공개 프로젝트 reader의 호환성 분기로 추가하지 않았다.

## 전후 측정과 동일성

| 항목 | 기존 구조 | 개선 구조 | 성능·크기 변화 | 결과 동일성 |
| --- | --- | --- | --- | --- |
| source 작성 자료 | 좌표 중복 포함 83,451,669 B | descriptor 1,985,235 B + 고유 좌표 19,694,167 B | 논리 표현 21,679,402 B | 288개 순서 포함 문서 정확 일치 |
| 국가 runtime gzip | 293파일·12,821,168 B | 604파일·12,364,781 B | 좌표 324개 독립 자원 | 280개 순서 포함 문서 정확 일치 |
| 역사 육지 | gzip 4,360,786 B 전체 사본 | 기존 공통 기반 + patch 104,309 B | 역사분 추가 전송 97.6% 감소 | ordered geometry SHA 37d223c5…; 11 Polygon 대체 |
| 역사 준비 메시 | gzip 19,352,611 B 전체 사본 | 기존 공통 메시 + delta 6,213,292 B | 역사분 추가 전송 67.9% 감소 | raw 43,350,288 B, SHA 741f5ec2… 정확 일치 |
| 초기 좌표 준비 | 324개 전체 시대 payload | 254개 현재 필요 payload | 70개 초기 다운로드 제외 | 전체 280개 객체·386개 binding 유지 |
| 최초 준비 | 23,444.4149 ms | 17,866.4075 ms | 23.8% 감소 | page error 0 |
| 재방문 준비 | 21,977.433 ms | 16,572.8986 ms | 24.6% 감소 | page error 0 |
| 메인 페이지 JS heap | 최초 214,748,580 / 반복 216,454,788 B | 최초 107,425,456 / 반복 83,305,824 B | 각각 약 50.0% / 61.5% 감소 | 같은 준비 완료 지점 |
| CDP encoded network | 최초 46,042,314 / 반복 4,764,556 B | 최초 39,912,277 / 반복 4,729,012 B | 최초 13.3%, 반복 0.7% 감소 | Worker 네트워크 제외 |
| 메인 페이지 요청 수 | 최초 585 / 반복 287 | 최초 823 / 반복 284 | 최초는 독립 payload 때문에 증가 | 파일 수 감소를 목표로 하지 않음 |
| Viewer 배포 폐쇄 | 1,580파일·240,871,446 B | 1,900파일·223,346,549 B | 논리 바이트 17,524,897 B 감소 | 동적 Worker/WASM 자산 포함 준비·실행 검증 |
| GPU quiet upload 합성 | 9×256KiB 작업에 9프레임 | 기존 2MiB/2ms 예산 안에서 2프레임 | 불필요한 대기 프레임 제거 | 취소·우선순위·다른 소비자 보존 |

위 시간·힙은 전후 단일 실행 비교로 통계적 성능 보장은 아니다. CDP는 메인 페이지 세션만 수집하여 Worker의 네트워크/CPU/힙과 전체 브라우저 메모리를 측정하지 않는다. GPU 실제 프레임 시간의 전후 분포나 전체 시스템 CPU/할당 횟수는 측정하지 않았다. 반복 실행에서 기존 Core WASM의 불필요한 재전송을 확인해 기존 저장 자산 캐시를 재사용했으며 새 캐시 관리자는 만들지 않았다.

고유 콘텐츠 Viewer 바이트는 222,373,245 B다. 현재 준비된 runtime 자료는 1,048파일·207,327,815 논리 B이며 모두 hardlink다. 중복 inode를 한 번만 센 현재 공유 NTFS 할당량은 209,818,392 B다. 전 상태 물리 할당량을 측정하지 않았고 archive/과거 pin도 보존하므로 이를 디스크 절약량으로 주장하지 않는다. 압축 전송량·논리 바이트·고유 콘텐츠·물리 할당은 서로 다른 값이다.

## 집중 검증

- 구조 이동: frontend/domain/native Worker/asset/HTML/소스 카탈로그 및 변경된 검사 자동화 테스트, desktop 1280/mobile 640 실제 시작. 이동 시 공개 JS 248/248 byte 동일.
- 저장: 목적별 폐쇄, 선택 쓰기·명시 삭제·미준비 보존, 정본 충돌·재실행, descriptor/좌표 인코딩·해시, metadata-only 쓰기 0, 선택 실제 KOR 검증. 전체 GIS 재생성 없음.
- 실제 Viewer: 선택·피킹·드래그·확대 후 Core revision/checkpoint/dirty 불변; 2026-11→1922-12→2026-11→1922-12 준비 완료, 오류 0. 10개 과거 좌표 추가 후 재방문은 공유.
- native: [CI 42491573144](https://github.com/kimjeon-il/Pando/actions/runs/42491573144) SUCCESS. Core geometry-resource 합성 1개(전체 시대/잘못된 payload/무편집 admission/preview와 history/오프라인 save-reopen). 최종 native 입력 158개 source SHA efd08f639c261375e45e932c268b915161e15cc8d05a6e4bcf2778224098e35b, ABI 1, Emscripten 6.0.3 일치. 로컬 compiler 설치·검증 우회 없음.
- 최종 업로드 회귀: node --test의 이름 선택으로 4개 PASS, 실패·skip 0. 실제 사용 중 입력에 필요한 physical upload, quiet-frame 예산 활용, self-cancel, priority 확인. 수정한 7개 JS/검사 파일 eslint PASS, git diff --check PASS.
- 최종 실제 브라우저: viewer-calendar의 'last complete webgl frame' 시나리오 1개 PASS. SwiftShader 환경에서도 준비 지연 중 compositor 픽셀 hash 621355592와 라벨 위치 정확 유지, 승인된 역사 육지/수면 표시, 실패 rollback, 연속 요청 coalescing, 같은 월의 geometry/GPU 업로드 불변을 확인했다. 검증 조건·시간 제한을 완화하지 않았다. 구형 rebuild 강제 기대는 항상 필요한 source preparation으로 옮겼다.

초기 실패 CI 42490441555는 WASM-only planner의 불필요한 GIS 준비, 42490676366은 불필요한 자동 발행 그래프 진입이었다. 선택 경로를 고친 최종 CI가 위 결과다. 초기 software 브라우저 실패는 필수 upload가 입력 중 정지하고, quiet budget이 낭비되며, 목표 country source 확인 전 예전 mesh로 발행되는 문제를 직접 수정했다. 결과를 숨기기 위한 test skip은 추가하지 않았다.

## 미실행·한계

- 전체 프로젝트 테스트·전체 C++ 행렬·전체 카탈로그/GIS 검증: 사용자 지정 범위에 따라 미실행; 통과 주장 없음.
- 독립 Windows 검사기 실제 실행: 해당 없음. 착수 전 폐기된 제품을 복원하지 않았다.
- 모든 실제 GPKG/대규모 프로젝트 조합, Canvas 전체 행렬, GPU별 성능 분포: 미실행. 이번 변경과 관련된 선택 경로·합성 저장 및 WebGL 실제 흐름만 검증했다.
- historical source 원본 좌표·날짜·의미를 변경하지 않았으며 저장 표현만 바꾸었다. 원본과 과거 archive는 삭제하지 않았다.
- App main 통합과 실제 배포는 수행하지 않았다. 자료 work/optimization의 pin은 완료된 runtime 범위로 고정하고 보고서 발행은 독립된 라이브러리 main 보고서 범위만 사용한다.

## 보관·판본

이 판본과 evidence/의 원본 JSON·이동표·측정 스크립트·최종 검사 로그를 함께 보관한다. 자료 revision 순서: runtime descriptor 9941f5783ab71e4779816b28de9fcfc584515693 → source descriptor fb33c2dd27448cbbe6fee510d39368869f24920c → land patch ec90157f4a834c5bcbbdc66ecbe036d536d971d8 → mesh delta 0e06e120ddf7ad0c8cd6b72a8dd599efef2c9098 → type catalog c370d4f95e27c6b777239de58d3170171d7379db. 기존 보고서를 대체하거나 예전 결과를 새 검증으로 바꾸지 않는다.

## 종료 정리: BLOCKED

선택 증거를 원격 보관한 뒤 task scratch 삭제를 시도했으나, 도구 자동 승인 심사가 해당 명령을 `blocked by policy`로 거부했다. 삭제는 실행되지 않았고 다른 도구로 우회하지 않았다. 이는 사용자의 전체 검사 제한과 별개다.

현재 남은 task scratch는 147개 파일, 논리 57,655,197 B다. 그중 이미 Git 바이트와 해시가 일치하는 CI 복사본은 각각 3,463,463 B와 3,521,253 B, 재현 가능한 실패 진단 trace는 48,842,512 B다. 원본 측정·이동표·최종 통과 증거는 이 보고서에 별도 보관되어 있다. 남은 scratch의 현재 런타임 소비자는 없으며, 보존 사유는 도구 정책으로 삭제가 차단됐기 때문이다. 실제 삭제량은 0 B이고 드라이브 여유 공간 변화는 측정하지 않았다. 상세는 `evidence/cleanup.json`에 기록했다. 다른 작업의 `gpu-viewer-evidence`, 상설 작업트리 및 참조 중인 runtime 캐시는 보존했다.
