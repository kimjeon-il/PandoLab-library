# GIS 보고서 자동 검토 — 2026-11-06 22:00 UTC

> ID: GEO-REVIEW-20261106-2200 · 상태: reviewed / supplemental-corrections / important-holds · 지도 반영: report-only / runtime-unchanged

## 범위·원본 이력
Pando main과 work/gis는 모두 `30a8402ac82a3e8a24f943f777a7aaedec211279`, 자료 main은 `6e41eb415d66bffff400bf3b064f4605f95fa326`, work/gis는 `c85273422a1e89d16892c73f8f729d5bc1d56855` 기준이다. 직전 [11/5 검토](../scheduled-2026-11-05-2200/README.md)의 main 기준 `0ed277208a52fcda77d5777f1622e5272c08dadf` 이후 커밋5개·변경파일5개를 대조했다. 신규 역사 본문2개, 진행기록2개, 색인1개이며 work/gis는 직전 검토 이후 변경이 없다. 기존 보류·적용 보고서는 재반영하지 않는다.

Pando 양 브랜치의 동일 tree는 truncated=false이며 reports 파일0개다. 외부 reports/README와 최신 reports/borders 위치를 확인했다. work/gis의 과거 reports/geography tree는 `cc011048be374646ba373504c9df87fd214c05d5`로 그대로다. main에만 있는 다음 본문도 실제 읽었다.
- [LIFE026](https://github.com/kimjeon-il/PandoLab-library-data/blob/82bacc4524b62f2a1252f2f5046b7b5b3693a5f5/reports/borders/history/lifetimes/country-lifetime-south-america-historic-buenos-aires-acre-juliana-2026-11-07.md): 원본커밋82bacc45, blob49a306c2658809247217a4d884c3b10b6e1f18b0.
- [TIME023](https://github.com/kimjeon-il/PandoLab-library-data/blob/6e41eb415d66bffff400bf3b064f4605f95fa326/reports/borders/history/timeline/historical-timeline-2025-europe-kurakhove-effective-control-2026-11-07.md): 원본7469b9b5, UN 링크 후속정정6e41eb41, 최종blob790eb7cfa631b5f0a7f1b83e27a0a728314beaeb. 이미 수정된 UN 링크를 중복 정정하지 않는다.

파일명11/7은 한국시간 기록이며 본 실행은11/6 UTC다. LIFE 커서는 남아메리카 다음 오세아니아, TIME은2025 유럽 다음 아시아로 확인했다. 보고서의 후속 권고를 새 권한으로 해석하지 않는다.

## LIFE026 — 확인한 보충 정정
### 부에노스아이레스
[아르헨티나 의회도서관 조약집](https://digitales.bcn.gob.ar/files/textos/pacto-de-san-jose-de-flores-1859.pdf)은 **1859-11-10 서명**(인쇄p340), **11-11 양측 비준**(pp342–343), **11-11 비준서 교환**(pp343–344)을 구분한다. p340·344의 화면도 검수했다. 목록/머리말의11/11과 조약 서명문10일을 구분하면 원본의 포괄적인 “서명일10/11일 충돌” 보류를 줄일 수 있다. 이 보충판에서는 위 사건별 날짜로 정정한다. 다만 어느 날짜도 자동으로 국가 소멸일이나 전 영토 geometry 시작/종료일은 아니다.

헌법은 [ECAE 논문](https://www.argentina.gob.ar/sites/default/files/2024/08/revista_de_la_ecae6.pdf) 인쇄p157의1854-04-08과 [AGN 문헌](https://www.argentina.gob.ar/sites/default/files/estado_de_buenos_aires.pdf) p369의04-11 사이 추가 충돌을 기록한다. 원본이 화면 확인한 AGN pp365–366만으로 이 충돌은 드러나지 않는다.04/08을 출처 귀속 날짜로 유지하며 원관보의 제정·공포·시행 구분 전 단일 효력일로 입력하지 않는다. ECAE 조약 논의의 해당 쪽도p157이 아닌 **p158**로 보완한다.

### 줄리아나
원본 인용 [산타카타리나 주의회 인물기록](https://memoriapolitica.alesc.sc.gov.br/biografia/1346-Vicente_Ferreira_dos_Santos_Cordeiro)은 **1839-07-24 라구나 함락**, **07-29 Garibaldi·Canabarro의 선포**,08-07 선거,11-15 종료를 각각 기술한다. 따라서07/24를 가설적 “군사 선포”로 부르지 않고 군사적 함락으로 고친다. 이 페이지는 원본의 “라구나 시의회 독립선언” 귀속을 뒷받침하지 않으므로 그 기관 귀속은 확정 표현에서 제외한다. 원선언문·의회결의문과 정치체 동일성 검증은 여전히 남는다.

### 아크레
[브라질 외교부 Concórdia](https://concordia.itamaraty.gov.br/acordo/243)의1903-11-17 서명,1904-03-10 국제법상 발효,03-15 국내 시행과 [법령1179](https://legis.senado.leg.br/norma/603638/publicacao/15628099)의02-18 승인을 재확인했다. [조약 제10조](https://concordia.itamaraty.gov.br/ApiConcordia/Acordo/integra-acordo-html/243)는 비준서 교환을 정한다. 이 구분은 유지하며 혁명정부의 종료일로 바꾸지 않는다.1899–1903 무중단 국가기간·국제승인·1903 재선포일은 새로 확정하지 않았다.

## TIME023 — 시간 메타와 국가 경계 분리
[ISW/CTP ArcGIS 레이어](https://services5.arcgis.com/SaBe5HMtmnbqSWlu/ArcGIS/rest/services/JAN2025Timelapse_Ukraine_Russia_War/FeatureServer/1)의 서비스 메타를 직접 읽었다. Polygon,SR102100(3857),시간범위2025-01-01~31 UTC,최종편집04-16을 확인했다.

**보충:** startTimeField=datetime, endTimeField=null, Time Data Cumulative=false다. 따라서 날짜 속성을 국가 경계의 시작/끝 유효기간이나 이후 자동 누적 적용 계약으로 취급하지 않는다. 이는 서비스 메타 확인이며 쿠라호베 개별 피처·실제 최종 점령시각의 검증은 아니다.

원본이 구분한01/06 발표,01/07 관측,01/11 지도갱신을 단일 점령 완료일로 합치지 않는다. 군사적 실효통제와 법적 RUS/UKR 국경도 분리한다. 원본UN 링크 후속정정은 이미 반영되어 중복하지 않았다. [공식 UN 결의 PDF](https://digitallibrary.un.org/record/4076916/files/A_RES_ES-11_7-EN.pdf)는 이번 직접 열람403으로 실패했고 공식 검색 색인에서 영토보전 문구를 확인했다. 완독·화면검증이라고 하지 않는다.

[ISW 이용정책](https://understandingwar.org/fair-use-and-attribution-policy/)도 직접403, 공식 검색 발췌에서 데이터셋/지도 플랫폼 편입 등에 사전서면허가가 필요함을 확인했다. CTP01/11 본문 직접조회도403이었다. 원본의 그날 평가를 이번에 독립 재검증했다고 주장하지 않는다. 형상을 수집·제품 편입하지 않았으며 허가요청 외부통신도 보내지 않았다. 공개 서비스 존재만으로 재배포권을 가정하지 않는다.

## 대상 객체·범위·처리 결과
현행 work/gis library.json의 ARG/BOL/BRA 객체를 직접 읽었다. lifetime 시작은 각각1831-01-04,1825-08-06,1822-09-07,끝은null이다. Natural Earth5.1.1 geometry의 기간은null이다. 이들은 관측값이며 이번 독립적으로 승인한 역사 결론이 아니다. 부에노스아이레스·아크레·줄리아나 생애를 현대 국가에 덮어쓰지 않는다. 색인의 해당 영문 식별자 검색에는 전용ID가 없었지만 완전한 동일성 감사로 표현하지 않는다. RUS 객체 직접조회는 빈 본문이어서 JSON 파싱 실패했으며 상세 필드 재검증 완료로 주장하지 않는다. 국가 lifetime과 형상 유효기간을 분리하고1801 조사 하한을 창립일로 추가하지 않는다.

최신500km² 선별·종료 정책을 읽었다. 기존에 종료된 소규모 연구를 재개하지 않는다. 이번3개 정치체의 존재·국가성 검토는 영토변경량을 새로 정밀 측량하는 작업이 아니다. 쿠라호베의 중요도시 선정 사유는 기록하되 면적 기준을 충족했다고 주장하지 않는다.

**확정 반영:** 조약 서명/비준/교환 날짜 분리, 줄리아나 함락/선포·기관 귀속 정정, 헌법 날짜 출처 충돌 및 쪽수 보완, 서비스 시간필드 해석을 이 보충 정정판에 반영한다. main 원문은 보존한다. 국가 동일성·소멸기준·역사형상 근거가 없는 곳은 구체적 보류로 유지한다.

변경은 이 README,evidence.json,reports/README.md 색인1행뿐이다. 국가 lifetime·geometry·archive·library.json·앱pin·코드 변경0건. 검증은 원문·이력·대상 객체·문헌·조약 화면·JSON/변경경로 및 원격 바이트 대조이며 GIS 재생성·위상·제품화면·전체테스트는 미실행이다.

로컬 등록 work/gis 경로가 실제로 없어 원격 커넥터 기존 tree 기반 단일부모 커밋을 사용한다. 관련없는 로컬 checkout과 stale worktree 등록은 보존했다. main 게시helper는 명시적main 변경금지와 충돌해 미실행이며 helper 통과라고 하지 않는다. expected-head와force=false로 work/gis에만 게시하고3파일을 다시 읽어 대조한다. main병합·배포·포터블·중단된 무명강/호수 조사는 없다.
