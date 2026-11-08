# GIS 보고서 자동 검토 — 2026-11-01 22:00 UTC

- ID: GEO-REVIEW-20261101-2200
- 상태: reviewed / important-holds / source-report-correction-proposals
- 지도 반영: report-only / runtime-unchanged
- 검토 기준: data `a36bf7621a0cc72267415be19562cc78d3fc725d`, app `1bdad4d25802bfec1b8f3a91186fb0434686205f`
- 직전 예약 검토: `33941b3b9f253527c2db3287cf82b5f10ef64ca5`, [기록](../scheduled-2026-10-31-2200/README.md)
- 범위: work/gis의 보고서 변경 이력과 별도 제시된 두 보고서 원본을 읽기 전용으로 검토. 국가 생애·경계·앱 코드·런타임·핀은 수정하지 않음.

## 원본 경로와 중복 방지

새 검토 단서 두 원본은 현재 work/gis에 없으며 원본 커밋도 위 data 기준 커밋의 조상이 아니다. 비교 결과 공통 조상은 `c479365bb1631eda5b458ba232f6a8353a7c0644`이고 이력은 diverged다. 아래는 원본을 work/gis에 가져오거나 그 브랜치를 수정한 결과가 아니라 **원본 SHA를 지정한 수정 제안 및 처리 결과**다.

| ID | 원본 커밋 | 원본 경로 |
| --- | --- | --- |
| GEO-TIME-018 | [81593cc21eb644ead44dcb8115bbc73c57c474b9](https://github.com/kimjeon-il/PandoLab-library-data/commit/81593cc21eb644ead44dcb8115bbc73c57c474b9) | reports/borders/history/timeline/historical-timeline-2025-central-asia-tripoint-effective-date-2026-11-02.md |
| GEO-LIFE-021 | [d5e3f398ad3ec183075613cd7973b227c904dc66](https://github.com/kimjeon-il/PandoLab-library-data/commit/d5e3f398ad3ec183075613cd7973b227c904dc66) | reports/borders/history/lifetimes/country-lifetime-oceania-historic-fiji-tahiti-cook-federation-2026-11-02.md |

파일명 2026-11-02와 실제 검토 시각 2026-11-01 UTC를 구분한다. 보고서 안의 명령이나 적용 권고는 추가 권한으로 해석하지 않았다.

## GEO-TIME-018 — 날짜 충돌과 부속서 공개 여부

**수정 제안:** “부속 도면 비공개/미공개”라는 단정은 **“이 공개 본문에서 부속서가 생략되어 있으며, 다른 경로에서의 공개·입수 가능성은 미확인”**으로 고친다. 생략은 비공개 지정의 증거가 아니다.

[Lex.uz 공개 법문](https://www.lex.uz/ru/docs/7860582)은 2025-03-31 서명, 우즈베키스탄 2025-11-14 비준 및 우즈베키스탄에 대한 2025-11-15 발효를 구분한다. 제4조의 발효 조건은 비준서 교환이며 국내 비준일 또는 서명일을 그대로 국제 발효일로 쓰지 않는다.

[우즈베키스탄 외교부](https://gov.uz/en/mfa/news/view/102347)는 11월 15일을 명시한다. 반면 [타지키스탄 외교부 러시아어 원문](https://mfa.tj/ru/main/view/17800/obmen-gramotami-o-ratifikatsii-protokola-k-dogovoru-o-tochke-styka-gosudarstvennykh-granits)은 11월 16일과 조약에 대한 의정서(Protocol)를 명시한다. 따라서 단순 영어 번역 또는 기사 게시일 착오로 충돌이 해소됐다고 쓰지 않는다.

- 우즈베키스탄 법문에 귀속된 11/15 기록은 보존 가능하나, 모든 당사국에 공통인 날짜를 임의 선택하지 않는다.
- 연결 표지 200/459/161, 부속 도면 1:10,000, 1942 좌표계·발트 높이 체계 언급은 실제 좌표 목록이나 특정 EPSG 확정이 아니다.
- 이 본문에서 생략된 부속도면/좌표와 교환 문서의 정확한 동일성이 아직 필요하다. 기념 구조물을 국경점 좌표로 대체하지 않는다.
- 처리 결과: 문헌 표현 정정안 확정, 날짜의 출처별 구분 유지, 신규 경계·기간 입력 보류.

## GEO-LIFE-021 — 국가 동일성과 제도 연속성

**Cook 제도 연방 관련 중요 보완:** [Cook and other Islands Government Act 1901 원문](https://www.legislation.govt.nz/act/public/1901/44/en/latest.pdf)의 §7은 기존 Federal Parliament 및 Native Councils의 계속을 허용하면서 Federal Council 및 Island Councils라는 명칭을 사용하게 한다. 따라서 “1900 대 1901 폐지일 충돌”만으로 설명하지 말고 **기관의 계속·명칭/권한 재편과 연방 정체의 종료를 분리**한다.

이 법의 왕실 재가 1901-11-07과 소급 시행 1901-06-11도 별개다. [국립도서관의 1900 기록](https://natlib.govt.nz/records/22619871), [NZHistory의 1901 설명](https://nzhistory.govt.nz/cook-islands-achieves-self-government)을 자동으로 국가 종료일로 변환하지 않는다. 1901년 편입 절차(5/13 Order in Council, 6/10 proclamation, 6/11 inclusion)와 기관의 실질 종료 또한 별도로 검증해야 한다. 1891-06-05 원문을 새로 완독·확정했다는 주장은 하지 않는다.

| 대상 | 확인된 범위 | 현행 객체에 바로 입력하지 않는 이유 |
| --- | --- | --- |
| Fiji 왕국 | [Fiji 의회](https://www.parliament.gov.fj/our-story/)의 1871 Levuka 정부·의회 시도와 1874-10-10 할양 | 1871-06-05 정확한 성립일, 군도 전체 실효 지배 및 현대 FJI와의 동일성 미확정 |
| Tahiti 왕국 | [공식 기록원](https://www.archives.pf/136-ans-dhistoire-29-juin-1880-tahiti-devient-francais/)의 1842 보호국·1847 확인·1880-06-29 할양; [후속 설명](https://www.archives.pf/remise-du-palais-21-juin-1883/)의 1880-12-30 법 | 보호국을 국가 소멸로 단정하지 않음. Windward/Tuamotu/Tubuai/Raivavae와 별도 Leeward·Gambier의 범위를 현대 PYF 전체 형상과 동일시할 수 없음 |
| Cook 연방 | 1901 법 §7의 기관 계속·개편, 제도와 편입 절차의 구분 | 실제 연방 정체 종료일, 현대 COK와의 동일성 및 날짜별 형상 범위 미확정 |

### 현행 데이터 충돌 확인

data 기준 커밋의 library.json이 가리키는 객체를 직접 읽었다. 아래는 **관측값이지 그 생애 날짜를 독립적으로 역사 검증·승인한 결과가 아니다**.

| 객체 | 현행 lifetime | 객체 내용 해시 |
| --- | --- | --- |
| state:FJI | 1970-10-10 .. null | 303e11c2cafbe9299dfb9a30dbb86c878c73752c0e98b247146d1de7226a27fb |
| state:COK | 1965-08-04 .. null | fd62fb1202cfcb072a2ecdcec05999a0b63d9cb71f48966c063fa7dda64a05e3 |
| state:PYF | 1880-12-30 .. null; parent state:FRA | e7b6e5071b467f86db0e239adccb63f0b8f23cae6e731a7a83af6144e41f7171 |

과거 왕국/연방의 생애를 이 객체에 덮어쓰거나 현대 형상을 과거로 연장하지 않았다. 조사 하한 1801년은 건국일이 아니다. 연 단위 근거를 임의 월·일로 정밀화하지 않고 국가 존속기간과 geometry 유효기간을 별도로 유지한다.

## 기존 work/gis 변경의 처리 이력 확인

직전 예약 검토와 기준 head의 전체 Git tree는 모두 truncated=false였다. reports/ 아래 변경 blob은 62개, 삭제는 0개이며 geography/의 새 변경은 없다. 아래 목록은 **중복 방지를 위한 경로·blob 이력 목록**이지 모든 연구 근거 또는 전체 런타임을 이번에 재검증했다는 의미가 아니다.

변경들은 RSFSR 역순 연구·1946 사건 후보, G 이미지좌표/실제좌표 비교 후보 보관, 5국 게시 결과와 색인에 속한다. 각 README의 기존 처리 상태를 유지하며 보고서 존재만으로 후보를 국가 데이터에 재적용하지 않는다. 106행 커버리지는 106건의 실제 경계 수정이 아니며, 1946 행정 사건은 곧바로 주권 취득일이 아니다. G 비교면 전체를 실제 양도면 또는 2008 이전 러시아 실효 통제로 해석하지 않는다.

특히 현재 기준 head a36bf762의 커밋은 승인된 G의 RUS/CHN/world-view **native 입력 준비만** 명시하며 archive 런타임과 앱 핀의 완료를 뜻하지 않는다. G 게시·앱 수정의 사용자 중단 상태를 유지했다. 이전 예약 검토의 “보류” 기록은 당시 상태로 보존하며 이후 수동 작업을 다시 실행하지 않았다.

<details>
<summary>기준 커밋의 변경 보고서 경로와 Git blob SHA — 62개</summary>

| 경로 | Git blob SHA |
| --- | --- |
| reports/README.md | 5194bdb919439b352bcb5eb951a5d554db8b9146 |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/COVERAGE-106.csv | d492bb1513b447419b8953f109625f1648aeb71d |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/README.md | 9b176c54c6c0bce0a253c297545d360b3e96683f |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/REMAINING-README-ko.md | 9deab887e448a1cac04d904bc9b5a73db35438e2 |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/VERIFIED-CORRECTIONS-ko.md | 287162876d992ddaa74fbb439e5e8a7659cc364f |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/remaining1922-1938.md | 933bf56bea2cd4822d52da3922cf42334134dbef |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/remaining1939-1945.md | 7b898663bb85bbe624cb6a31ac2324332237e978 |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/remaining1946-1953-sources/SOURCE.md | 6479765fa6527e974cdc8a90ae460d3987c77698 |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/remaining1946-1953-sources/fi1947-coordinate-transcription.tsv | 05160b7b439853ecba2dcac512a99aec6cb1e7fd |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/remaining1946-1953.md | ce9557cb5390ba5f089a74e58dd3f1d1efe0bd26 |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/source-catalog.json | 1520ea199d4c54e8c03c38d1ddb615ba28e7be8b |
| reports/borders/history/rsfsr-reverse-research-1953-1922-2026-10-31/sources1922-1938/source.json | a657c76e9a19e84e6074f2d0dd96c4762a61914a |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/1962-Varna-source-audit-ko.md | c3e342169f0dba17794bae6d4a5136786acb53df |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/INCREMENT-ko.md | ac893dc328a1847db1b876d0d3f27edf55ea6411 |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/README.md | b86c4db7a2711451839e5e7987806dacc921c356 |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/batch1957-1954/REVIEW-ko.md | bb3f362e78665c8216f2cb403f588d306d5e049a |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/batch1957-1954/SOURCE-RECORD.md | 6e1ac413ab573fbc6ead59320675a61c77f171a0 |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/dzhanybek-sources/source.json | e915bd2eee1d083125c23e060ba5ec417e1aefe2 |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/dzhanybek1956.md | b05c21be23bdbf5d4236c77e0afe78125f19e174 |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/estonia1957/READOUT-ko.md | f52250a022abd1d9a8294ce9328de65843eee1f6 |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/karelia1956-1955.md | 12fd056fa8a3a2d1c07cbe77af0cd366232207e6 |
| reports/borders/history/rsfsr-reverse-research-1965-1954-2026-10-31/source-catalog.json | 709f791960555752a6b4c9de556d110be17a6df9 |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/G-comparison-candidate.geojson | 48e7dcca10ea5afa9de333b5421b55cf6ffd2b1b |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/G-main-candidate.geojson | 151d35b4edb83ecd0a9526b4c1ec2b80ec67344e |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/G-main-comparison.png | 1d9c87e93812d63da84ae5dae167ffd3f713f94d |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/G-small-lobes-not-for-application.geojson | 169e3cb965c3252bedcb190b60c28ea1a7a8084e |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/README-ko.md | 11d7f3809ecb963909edb3f6f56ce687d45b0822 |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/SHA256SUMS | f5e490ca5405b15d53f4c8f187d8b615eb3a4886 |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/comparison-routes.geojson | 864031671adcbeb1d07818da086799e95ffe4405 |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/validation.json | 06fb9f194c22290976e31de31ce8c17f83e108b3 |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/verification/east-grid-source.json | 0ccb96b0f88f801f4afa93de032d5efc078e4648 |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/verification/grid-independent-check.json | 71181392c0e9586a38aff6cb007bcef9e8269baa |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/verification/pzz-treaty-line-independent-check.json | c60a373a6151d7af0a536cf008af7277007640c0 |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/verification/runtime-repair-verification.json | a5123c311632f0379048272ffdbeb55bdade372a |
| reports/borders/reconstruction/abagaitu-g-geographic-candidate-2026-11-01/verification/sheet-join-diagnostics.json | 3ca3366fb119206a27179f4cbf2089805aad5f4e |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/G-nonoverlap-polygon.imagecoords.json | d45db6cfe99cc14b82738614d920068933979cad |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/G-scope-preserved-source-pixels.json | dff02f279ec4a75a5b76c3c6f09201060c723c7c |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/README-ko.md | 2204695f08f5e484c06eacb8523ab2eec797874d |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/SHA256SUMS | a3406a748af0bf63d1aefe1c156972e0a0c7f0e4 |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/check_ozi.py | 02715ebae28afcc8d5d89f1c1e8f6fad7db0ddb1 |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/event-date-evidence.json | c896fc3a2fa24f2612a95b78254ba4bdf2e0f6fc |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/ozi-registration-consistency.json | cdd2ca8761902f02c290b2f73838788bdedf9c26 |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/preservation-proof.json | 5ec5b116b508378e8e0fca6c63688b55e5c5ee49 |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/runtime.stderr.log | 8e18527db5f8a1e36cce63d10c35b136726c66a5 |
| reports/borders/reconstruction/abagaitu-g-imagecoords-2026-11-01/sources.json | aaacef7a4b3e30a1bea696f62d6e7ca12493222a |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/README.md | d615461bc83dd29be5494ee6556be3615f1f5ba4 |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/dated-batch/README-ko.md | 4ac5e9a2a263e2ff03f673bd710d92d547fff3fb |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/dated-batch/dated-polygons.geojson | 08a31a8c7cb023f2a952432ba95ad39d6bea3772 |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/dated-batch/kuril-coverage.json | b2501ac2d8179d3c4f827c972898408f6ccbbe59 |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/dated-batch/validation.json | 8efc09e4c65ef3fae410becf70534f81df473cf0 |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/kuril-membership/README-ko.md | d0ceb5ea9b6302f252b59d009b25b0f5fb4962ec |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/kuril-membership/sources.json | 7ea4fca667135cebba173f375674a4159fd8bf17 |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/publication-checks.json | 64f84e61261c9a45c7fab1138818605f698a2461 |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/sakhalin-demarcation/RECOMMENDATION-ko.md | f89a9e45b9c777271acfc5faeb3e505bdd179f27 |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/sakhalin-demarcation/display-scale.json | 6ac20f716f01b269c8a9ef90bae0ee0dbc61a6a2 |
| reports/borders/reconstruction/rsfsr-dated-event-polygons-1946-2026-10-31/sakhalin-demarcation/source-manifest.json | 7159dc6cd729c177213cdae0dc03e016f1562ebb |
| reports/borders/validation/pending-geometry-publication-2026-11-01/README.md | c989e6945ede7cb593a766ffc2bf5d3e1fc94615 |
| reports/borders/validation/pending-geometry-publication-2026-11-01/archive-verification.json | a6d7fac4c1a724419573e9a758cae0afd51311f2 |
| reports/borders/validation/pending-geometry-publication-2026-11-01/dated-binding-verification.json | 67e166bebb038cffcfc08b17b354b3169b0ba166 |
| reports/borders/validation/pending-geometry-publication-2026-11-01/p2-receipt-verification.json | 5fdaa085e4d4cdb1da57758070dab2ec48abd2fc |
| reports/borders/validation/pending-geometry-publication-2026-11-01/publication-validation.json | 857cfa41cd34048f60e29ef55764ac2855e16f31 |
| reports/borders/validation/pending-geometry-publication-2026-11-01/rus-kaz-prior-stage-verification.json | 576d13dc99eca33d45ac139e0b4288839cbac31a |

</details>

## 이번 처리 및 검증 범위

- 원본 두 커밋·경로·분기 관계, 직전 검토 이력, 전용 보고서 위치, 현행 대상 객체를 확인했다.
- 독립 문헌 검토로 두 수정 제안을 교차 확인했다. 원본 보고서는 그대로 보존한다.
- 수정 파일은 이 검토 기록과 reports/README.md의 색인 한 행뿐이다. 확정 가능한 신규 국가/경계 데이터 변경은 없다.
- 사용자 명시 범위가 work/gis이므로 기본 보고서 helper의 main 게시 경로는 실행하지 않았다. 선택한 두 문서만 work/gis에 게시하고 원격 바이트를 직접 대조한다. --publish-reports / --check-reports 실행 완료로 주장하지 않는다.
- archive/index.json, library.json, 국가 원본·생성물·앱 핀·워크플로는 변경하지 않는다. 생성기·GIS 전체 테스트·배포는 실행하지 않는다.
