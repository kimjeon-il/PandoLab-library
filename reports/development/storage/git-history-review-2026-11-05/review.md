# Git 이력 추가 정리 검토 — 2026-11-05

> 상태: 조사 완료, 삭제·이력 재작성 미실행. 지도/모델 변경 없음.
> 코드 main: 7964920b2cb94d9fce4064953069901c163e7c22
> 자료 main: b5e64fb40f1e523dd94e019c84e35e5b97165c5d
> 대상: kimjeon-il/Pando 및 kimjeon-il/PandoLab-library-data

## 결론

추가 후보가 있다. 자료 저장소의 구 지형 타일·수계·prepared polygons·세계 지도 생성물이 가장 크다. 선택된 3180개 고유 blob의 기존 pack 표현 크기 합계는 1095452681bytes(약1.02GiB)다. 이는 실제 확보 공간이나 GitHub GC 결과를 보장하는 값이 아니다. 3179개가 로컬 보호 ref 또는 현재 code data pin의 조상 이력에도 연결돼 있다. 판본 원문과 현재 자료를 보존하려면 재작성 매핑, 보호 refs/owners, 모든 소비자의 고정 revision을 함께 설계해야 한다. 단순히 main에서 파일을 지우거나 원격 branch pointer만 없애면 충분하지 않다.

## 우선 검토 후보

| 범위 | 고유 blob 수 | 논리 bytes | 현재 pack 표현 bytes | MiB |
| --- | ---: | ---: | ---: | ---: |
| terrain-v0.12.0 | 275 | 329788153 | 329313194 | 314.1 |
| terrain-v0.12.6 | 335 | 367620868 | 366944220 | 349.9 |
| prepared-polygons | 740 | 120118805 | 108911483 | 103.9 |
| old-hydro | 1781 | 197809845 | 184281752 | 175.7 |
| old-world | 49 | 165426107 | 106002032 | 101.1 |

위 객체들은 검사한 현재 branch tip에서 사라졌으며 17개 현재/고정/보고서 보호 archive index의 실제 stored blob identity에서 사용되지 않는다. 같은 파일명 아래 다른 판본을 같은 사용 객체로 오판하지 않게 Git OID까지 대조했다. 목록은 generated-candidates.json이다. 주된 대상은 assets/data/terrain/v0.12.0, v0.12.6, prepared-polygons/generated, 과거 hydro, 과거 world/countries/historical-world 파생물이다. 삭제 승인 목록은 아니다. 추가로 조사하지 않은 실행 중 소비자/별도 프로젝트의 명시적 과거 판본 사용까지 부재를 증명하지 않았다.

## 코드 저장소

확실한 역사상 폐기 경로는 GDAL gdal3WebAssembly.wasm/data 두 blob(논리39814980bytes, 현재 표현11260577bytes)이다. 2026-11-04의810a2b821에서 제거됐다. 과거 index.html629판본은 논리84899161bytes/표현12098203bytes이며, 그중2026-08-19 업로드된 단일 blob이22621821bytes/표현11305143bytes로 가장 크다. 옛Core WASM51판본은 논리164546949/표현12472859bytes, 이관된 docs/place-candidate-review.md5판본은 논리20556698/표현845827bytes다. 이는 서로 겹치지 않는 고유 blob별 집계다.

GDAL·옛HTML·WASM과 보고서 원문도 보호 ref에 남아 있다. 특히 원문/테스트 fixture/고정 source revision의 보존 필요를 검토해야 하므로 대량 source history 삭제를 권하지 않는다. 현재 일반 source 변경 이력은 기능 복구에 쓰이는 정상 이력으로 분류한다. 문서가 library로 이관됐다는 사실만으로 과거 모든 원문 byte가 동일하게 보관됐다고 주장하지 않았다.

## 저장량과 Git 중복

코드 pack6개101611452bytes, 자료 pack91개4394007073bytes다. loose 객체는 별도다. GitHub API 보고값은 code87591KiB, data4168708KiB로 로컬 측정과 의미가 다르다. 현재 tip에서 쓰이는 고유 blob의 선택 표현은 코드11771249bytes, 자료3164644766bytes다. 자료 전체약4.2GiB를 전부 폐기된 이력으로 볼 수 없다.

동일 Git OID의 pack 중복 slot은 코드641/자료1384개다. index offset으로 계산한 중복 표현은 각각742907/2168940bytes 정도이며, delta 의존성을 보존한 실제 repack 절감량은 별도 측정이 필요하다. 큰 절감의 주원인은 단순 중복 pack이 아니라 구 생성물 이력이다.

참조되지 않는 local blob은 코드64개1120472bytes(선택 표현303205), 자료4개4421281bytes(선택 표현957785)다. reflog·복구 필요를 별도로 검토하지 않았으므로 이번에는 삭제하지 않았다. 현재 HEAD에서 없어도 stash/보존 refs가 참조하는 객체는 미사용으로 간주하지 않았다.

## 보존과 한계

코드 보호 ref32개, 자료 보호 ref41개를 검사했다. 자료 pin30ce140bdd55b45cbe40d75346719a4b140e1342, c1d25c3f4e2b139fd043a919e411f4a7825f2ecc, 89bff9a4c9ed42a7bca5325a3449fbe8055012e8을 포함했다. 보고서 판본 refs, private source originals/stashes/code-inputs, 데이터 runtime refs는 보호 대상으로 계산했다.

자료 저장소는 부분 clone이다. 로컬에 없는 promisor blob은 다운로드하지 않고 용량 합계에서 제외했다. 이는 로컬에 존재하는 객체와 현재 받은 ref metadata의 조사다. 원격 PR refs·서버 GC·GitHub 물리 저장량 감소는 검증하지 않았다. Git 객체/인덱스/pack index metadata만 읽었고 테스트·GIS 생성·원본/모델 파일 전수 검증은 하지 않았다.

기존 tmp_pack_uUtx8n33595391bytes는 이전 복구 검사에서 early EOF가 확인된 파일이다. 이번에는 재검사하거나 삭제하지 않았으며 정상 이력 제거 후보와 구분한다. 개인 원본·보고서 고유 증거·학습 모델도 단순 크기로 삭제 후보에 넣지 않았다.

## 조치 방향

1. 자료 저장소의 구 생성물3180개를 1차 검토 범위로 삼는다. 판본과 pin을 유지할 방법, 또는 명시적으로 종료할 과거 판본을 먼저 결정한다.
2. 코드 저장소는 폐기GDAL과옛HTML을 우선 검토한다. WASM 과거 source pairing과 보고서 원문은 별도 확인 전 보존한다.
3. 적용을 승인받으면 현재 원격 SHA를 다시 대조하고 exact lease/atomic push, 보호ref/owner/pin 매핑 및 tip tree 보존 검사를 계획한다. 실제 절감량은 재작성·repack 전후에 따로 측정한다.

이번 작업은 후보 조사만 수행했고 refs, commit history, runtime pin을 변경하지 않았다. 원격 metadata fetch와 이 보고서의 선택 범위 게시만 수행한다. 기존 main 미추적 gpu-viewer-evidence/와 다른 작업트리는 보존했다.
