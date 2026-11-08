# GIS 보고서 자동 검토 — 2026-10-29 22:00 UTC

상태: `reviewed / report-only / runtime-unchanged`.

## 기준·중복 확인
- 이전 처리 기록: `cbf25b306d9b58b2febc3c69bc8f3e4c14a80e43`, `reports/borders/validation/reviews/scheduled-2026-10-28-2200/README.md`. Caspian 게시 상태 정정을 반복하지 않았다.
- 검토 데이터 work/gis: `0bce2891d531579b81ac0f97e6d07cb1873b878f`; 앱 관측 head: `5994977ca373bba85e5001f0fcc99fe56ada5f24`.
- 앱 데이터 pin `890e2ae21b8b2c240de5dd64c5d459f4c7e59841`은 위 데이터 head의 직계 후속 publisher 커밋이다. pin을 변경하지 않았다.
- 이전 처리 tree와 현재 tree를 경로·blob SHA로 비교했다(각 8728/8765 entries, truncated=false). 보고서 변경은 색인 1개와 BY/Ukraine 보고서 묶음 20개, 삭제 0개이다. geography 및 borders/history에는 새 변경이 없다. main 전용 보고서나 비공개 작업 자료는 가져오지 않았다.

## 신규 묶음 판정과 수정안
대상: `reports/borders/reconstruction/by-ukraine-full-internal-2026-10-29/`.
원본 적용 커밋 `bc97f169a4a6e166d3a12fc743a1f18a4fd455a9` 및 명칭 동시 변경 보존 커밋 `0bce2891d531579b81ac0f97e6d07cb1873b878f`를 확인했다. 이미 반영된 형상을 다시 적용하지 않는다.

README 원본 blob `b9307dc456b4cfc6d5c6d68ed53ebfb2d559ba3f`가 존재하지 않는 `source-proof.json`, `runtime-geometry-proof.json`을 참조했다. 실제 게시 파일 `source-verification.json`(blob `42995c7fcc725a28402be95d09f42718a907e899`), `runtime-geometry-verification.json`(blob `dba4a0ad4dd25ff237f5eef0e319837469b390cc`) 내용과 보고서의 대상 객체·수치가 일치하므로 참조명만 정정한다. 독립 검토 파일도 상대 링크로 명시한다.

## 유지하는 제한·보류
- 기존 BY/Ukraine/RSFSR `1922-12-30-reviewed-v2` 대상이며 국가 존속기간은 변경하지 않는다. 1801은 조사 하한이지 건국일이 아니다.
- 기존 형상 선택기간 1922-12-30~1925-05-12는 새로 확정한 법적 효력기간이 아니다. BSSR 1924 확대, Ukraine 1922년 1월 원도와 12월 30일 사이 연속성, 1925-05-12 경계 변경일은 기존 보류를 유지한다.
- Konotop 원문 가림·시점·접합, Perekop/Syvash, BY 가림 구간을 재결정하지 않는다. 중단된 Ukraine 조사와 사적 Caucasus 작업을 재개하거나 게시하지 않았다.
- 100m 표시 일반화와 등록 오차는 역사적 정확도나 주권 증거를 대체하지 않는다. 새 국가 동일성·주권 단절 판단은 없다.

## 처리·검증
보고서 참조 정정과 이 처리 기록·색인만 변경한다. 실제 JSON 내용 및 대상 파일 존재, 변경 경로 한정, 최신 원격 parent와 비강제 fast-forward 게시를 확인한다. 데이터·형상·앱 pin은 변경하지 않으며 과거 형상 검사나 집중 테스트를 재실행한 것으로 주장하지 않는다. 전체 테스트·배포·main 병합·포터블 생성은 하지 않았다.
