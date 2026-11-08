# GEO-REVIEW-20261024-2200 — 국가·시대별 보고서 자동 검토

> 회차: 2026-10-24 22:00 UTC · 실제 검토: 2026-10-24 UTC / 10-25 KST
> 상태: reviewed / data-not-applied / report-only
> 신규 데이터 수정 0건. 신규 연구 보고서 2건과 기존 5건의 판본을 대조했다.
> 원문 경로·원본 커밋·현재 blob·20객체 비교·검사 목록: [evidence.json](evidence.json)

## 기준과 중복 방지

- 코드 원격 work/gis: `6f5dc6977bfb84704dfb44ba3f75e4ac0bda20e0`.
  이전 검토 `70a110cf8a1fa849046bb732e04dad3f547558bf` 이후의 지침·핀 변경을 확인했다.
- 코드의 고정 자료: `127e51c3457df87786ecf3aa5ad98ded690928df`.
  쓰기 기준 자료 work/gis: `82eb37ccba5c38d3b294347e2995fafc65bdda4c`.
- 연구 원문·최신 주제 색인: 자료 main `78f4dfd580eb1569bfd4dc552ad1fb48b836c34f`.
  이전 원문 기준 `374b5e208477c54ab251bf4eadbbaa5a2b9c1e98` 이후를 대조했다.
- `reports/README.md`가 안내하는 실제 원문은 이제
  `reports/borders/history/{lifetimes,timeline}/`, 검토는
  `reports/borders/validation/reviews/`다. `6fcdf285`의 주제 이동을 따랐다.
  work/gis에 남은 구형 geography 원문은 과거 판본으로 보존한다.
- 기존 검토 `657dd720`, 복구·커서 `8a7075cd/3921c5fa/a0bbfca9`,
  신규 `e7468c1f/af86b978` 이력을 대조했다. 같은 연구를 새 조사로 재집계하지 않는다.
  LIFE-009/010은 경로 문자열만 바뀌었고 011/012/TIME-009는 이전과 본문 동일이다.
- 전달된 별도 환경의 `/workspace/Pando-gis`와 로컬 예정 보고서는 이 환경에
  존재하지 않았다. 그 초안이나 과거 고립 blob을 가져오거나 연결하지 않았다.
  새 채팅·에이전트·워크트리도 만들지 않았다.

## 원문별 판정

원본은 아래 링크의 자료 main 고정 판본이며, 추가·복구 커밋은 괄호다.

- [GEO-LIFE-009](https://github.com/kimjeon-il/PandoLab-library-data/blob/78f4dfd580eb1569bfd4dc552ad1fb48b836c34f/reports/borders/history/lifetimes/country-lifetime-oceania-micronesia-tonga-2026-10-21.md) (`60b6ef96c1d648a23225fb89b4126e8bf2a8cdfa`): FSM/MHL의 헌정·협정·UN 조치, PLW 1981/1994, TON 왕국 계속성·연도 정밀도 보류.
- [GEO-LIFE-010](https://github.com/kimjeon-il/PandoLab-library-data/blob/78f4dfd580eb1569bfd4dc552ad1fb48b836c34f/reports/borders/history/lifetimes/country-lifetime-europe-baltic-2026-10-22.md) (`de7d465dbc9571f1cf02a61407dbbb66a8ac40f9`): 발트 3국 계속성 보류 및 현재 pin과 원보고서·자료 main의 기간 충돌.
- [GEO-LIFE-011](https://github.com/kimjeon-il/PandoLab-library-data/blob/78f4dfd580eb1569bfd4dc552ad1fb48b836c34f/reports/borders/history/lifetimes/country-lifetime-asia-south-southeast-2026-10-23.md) (`6bb7304d6ac33cf199cfcd4b6217729dead62262`): PAK 8/14·8/15, MYS 계승, NPL 기존 국가 계속성 보류.
- [GEO-LIFE-012](https://github.com/kimjeon-il/PandoLab-library-data/blob/78f4dfd580eb1569bfd4dc552ad1fb48b836c34f/reports/borders/history/lifetimes/country-lifetime-africa-cmr-mli-tza-2026-10-24.md) (`b5e5c3f0f7b50532d4fde59cb6b0ed757d3293a3`): CMR 연방화, MLI 연방 해체·계승, TZA 연합국 동일성 보류.
- [GEO-TIME-009](https://github.com/kimjeon-il/PandoLab-library-data/blob/78f4dfd580eb1569bfd4dc552ad1fb48b836c34f/reports/borders/history/timeline/historical-timeline-2025-africa-gabon-equatorial-guinea-2026-10-24.md) (`3f278895e21604d5841c6e9b6d2562e8169ed72c`): 권원 판결과 실제 이양·국경 유효일 구별 유지.
- [GEO-LIFE-013](https://github.com/kimjeon-il/PandoLab-library-data/blob/78f4dfd580eb1569bfd4dc552ad1fb48b836c34f/reports/borders/history/lifetimes/country-lifetime-north-america-slv-usa-2026-10-25.md) (`b49d3f4c115ab5d9174629bc347f0e5d20afddbe`): SLV 성립·연합 중 계속성 불명확; USA 1801 이전 존속·내전 법적 계속성.
- [GEO-TIME-010](https://github.com/kimjeon-il/PandoLab-library-data/blob/78f4dfd580eb1569bfd4dc552ad1fb48b836c34f/reports/borders/history/timeline/historical-timeline-2025-africa-western-sahara-status-2026-10-25.md) (`820fb2d458b80bc9e3d49fa51991422728a299e2`): SADR 외교관계·승인, 자치안 지지, 유엔 임무와 주권·경계 분리.

이전 5건의 불확실성을 해소할 새 역사 근거는 없었다. 같은 근거로 재승격하지 않는다.
연구 커서는 원문대로 LIFE=북아메리카→남아메리카, TIME=2025 미완료·다음 오세아니아다.
이번 검토는 새 연구 배치가 아니며 커서를 다시 전진시키지 않는다.

## 신규 2건의 확인과 수정안

**LIFE-013:** 엘살바도르 1841 헌법 전사의 제95조, 02-18 제헌의회 날짜와
02-22 집행문을 대조했다. 미국 국무부의 1839 개요·1849 승인,
1898 외교공문에서 11-14 정변·11-29 해체·12-05 통보를 구분했다.
제정·집행·승인·국가 성립을 같은 날짜로 확정할 근거가 부족하다.
`state:SLV`의 기간은 유지한다. `Texas v. White` 원판결 전사에서
1869-04-12 결정과 연방 계속성을 확인했지만 당시 전 영토의 실효 지배를
입증하지 않는다. `state:USA`에 1801 또는 내전 종료를 가상 건국일로 넣지 않는다.

**TIME-010:** 가나 외무부의 2026-09-16 후행 문서는 2025-01-06 결정의
불변을 확인하며, 모로코의 01-07 발표는 외교관계 중단을 설명한다.
원 외교공한이 없어 승인 철회의 정확한 법적 행위·효력은 보류한다.
영국 공동성명과 의회 06-11/06-27 답변은 자치안 지지와 법적 지위 미결정을
구별한다. UN 결의 2797 원문 조항은 협상·자결 및 MINURSO 연장으로,
새 주권·국경 획정으로 처리할 수 없다.
`state:SAH`(서사하라)·`state:MAR`·`state:GHA`의 기간·형상은 유지한다.
별도 ESH/SADR 국가 객체를 추정해 만들지 않는다.
geoBoundaries MAR는 2017 표현·OSM/Wambacher·ODbL이며 CShapes는 2019까지다.
2025 효력 경계로 사용하지 않는다.

핵심 재열람:
[SLV 국무부](https://history.state.gov/countries/el-salvador),
[1898 해체 공문](https://history.state.gov/historicaldocuments/frus1898/d100),
[SLV 후속 공문](https://history.state.gov/historicaldocuments/frus1898/d105),
[1841 헌법](https://www.cervantesvirtual.com/obra-visor/constitucion-politica-de-la-republica-de-el-salvador-de-1841/html/6eed6025-cfce-44e4-b9b9-171ab7fd9e8b_2.html),
[Texas v. White](https://supreme.justia.com/cases/federal/us/74/700/),
[영국 답변](https://questions-statements.parliament.uk/written-questions/detail/2025-06-04/57392),
[법적 지위 답변](https://questions-statements.parliament.uk/written-questions/detail/2025-06-03/HL8052),
[UN 결의](https://mandates.un.org/mandate/S/RES/2797%20%282025%29).
기관이 같은 개요·공문 또는 같은 원문의 전재를 독립 사료 둘로 과장하지 않았다.

## 현행 충돌: 발트 3국은 자동 덮어쓰기 금지

**최신 pin은 이전 검토·자료 main과 다르다.** pin의 EST=1991-08-20,
LVA=1991-08-21, LTU=1990-03-11이며 각 형상도 같은 날짜부터다.
자료 main의 세 lifetime과 형상 양끝은 null이다. pin 원본 JSON과
색인은 서로 일치하므로 색인만의 오류로 단정하지 않는다.
1918 국가 계속성 주장과 별도 동시 작업이 반영된 현재 값을 구분한다.
원문 당시의 공란을 근거로 현재 값을 지우거나 새 날짜를 넣지 않았다.
어느 판본도 이번 검토로 승인·역사 형상 검증 완료 처리하지 않는다.

전체 색인은 pin=282객체, main=281객체로 다르다. 두 자료를 교체하지 않았다.
집중 20객체 ID는 양쪽 각각 1개이며 정체성·lifetime 차이는 위 3국이다.
신규 대상 5객체 및 발트 3국 원본 JSON의 기간·형상 버전은 pin 색인과 일치했다.
pin은 interval-only 형식으로 datePrecision이 없고 main에는 current가 있다.
이 차이를 역사적 형상 유효성 증거나 새 날짜 부여 사유로 해석하지 않는다.
존속기간과 형상 기간을 분리하며 현재 벡터를 과거에 자동 소급하지 않는다.

## 접근 제한과 미실행

이번 신규 근거의 명시한 HTML·UN 조항·벡터 메타는 열람했다.
가나 당일 공한과 SLV 원관보·공식 첨부 PDF는 확보하지 못했다.
공식 CSJ 안내 페이지 열람은 첨부 원본 확인과 다르다.
기존 ICJ·UN·리투아니아 403, 에스토니아 JS, 네팔 timeout, 영국 XHTML
한계는 새 근거로 해소되지 않았고 거절 원문을 우회·재전송하지 않았다.

GIS 원본 다운로드·변환·CRS·위상·독립 역사 형상·1:10M 시각 비교,
웹·앱 실행·전체 테스트는 하지 않았다. 미실행을 통과로 표시하지 않는다.
아랄해, 별도 수동 소련·몽골 및 카스피해 임시 국경은 적용 보류 유지다.
이미 원격에 있는 타 작업을 자동 승인·확장·재생성·롤백하지 않았다.

## 저장 범위와 완료의 경계

사용자가 허용한 자료 **work/gis**에 이 묶음의 README·evidence,
기존 reports/README의 색인 1행 및 archive/index의 해당 보고서 항목만 저장한다.
모든 비보고서 바이트·원문 7건·runtime pin·코드는 보존한다.
--publish-reports는 라이브러리 main을 수정하므로 이번 명시적
work/gis 한정·다른 브랜치 수정 금지 지시에 따라 실행하지 않는다.
따라서 저장소 지침의 main 게시 명령 완료를 주장하지 않는다.
허용된 work/gis의 일반 갱신 뒤 선택 파일의 원격 바이트와 변경 범위를
직접 대조하고 실제 결과·커밋 링크는 최종 실행 응답에 남긴다.
