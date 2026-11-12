# 2025년 유럽 — 우크라이나 차시우야르(Chasiv Yar) 군사적 실효 지배 주장·교차검증과 역사 GIS 벡터 선별

> **GEO-TIME-029 · 조사일 2026-11-13 KST** · 대상 연도 **2025(잠정·전 세계 전수 미완료)** · 대상 지역 **유럽** · 상태 `investigating / source-indexed / provisional / not-applied` · 신규 사건 묶음 `EU-2025-003` 1건(확정 도시 전체 점령일 미확정) · 국가 성립·소멸/법적 국제국경/국제적 주권 양도 확인 0건 · 정본 데이터·코드 반영 0건.

## 0. 조사 범위와 인계 대조

- `Pando/work/gis`의 `AGENTS.md`, `docs/historical-border-reconstruction-policy.md`, `docs/historical-vector-source-workflow.md`, `docs/branch-policy.md` 및 최신 HEAD `97cf9f08a77e751f5d3af693cbd8480862592aae` 확인. 요청된 `Pando/work/gis/reports/README.md`와 `reports/geography/historical-timeline-yearly-progress.md`는 **현재 그 브랜치에서 404**. 현행 AGENTS에 의거 원본 보고서는 **별도 보관 저장소 `PandoLab-library-data/main/reports/borders/`**에서 관리하며, 그곳의 `reports/borders/README.md`, `history/timeline/historical-timeline-yearly-progress.md`와 기존 보고서를 읽음.
- 최신 인계: **GEO-TIME-028 오세아니아 → 이번 GEO-TIME-029 유럽 → 다음 아시아**, 계속 **2025년**. 유럽 기존 쿠르스크·수자 `EU-2025-001`(GEO-TIME-012; 색인은 존재하나 원문 미등록), 쿠라호베 `EU-2025-002`(GEO-TIME-023), 지브롤터 정치합의(GEO-TIME-017)와 중복하지 않음.
- 2025년 새 국제법상 국경이 아니라 **도네츠크주 주요 도시의 전쟁 중 군사 통제권 주장·부분 지배**를 조사. 도시의 전략적 중요성 때문에 거시 사건 선별의 주요 도시 예외에 해당; 도시 면적 수치와 500km² 선별 참고치를 혼동하지 않음. **해안선·간척·침식·해안 지형 연구 전부 제외**.

## 1. 사건 `EU-2025-003` 및 서로 다른 효력 기준

| 확인 시점 | 교차 확인 자료와 범위 | 판정 |
| --- | --- | --- |
| **2025-01 (일자 미확정)** | Meduza 2025-07-31 보도는 **1월 러시아군의 차시우야르 내 내화물 공장 지구 점거**를 회고. ISW/CTP 2025-07-31 분석은 **2025년 1월 말부터 북부·중심부 다수 러시아군 점유**라고 분석. | 대규모 진격의 배경으로 기록하되 **공장 완전 함락일·구별 경계/시각은 확정하지 않음**. 두 출처는 완전히 독립적인 현장관측 2개라고 보증할 수 없음. |
| **2025-07-31** | **러시아 국방부가 도시 전체 점령을 발표**. Reuters가 시내 폐허의 러시아군 국기 게양 영상 한 곳을 위치 검증했으나 **영상이 도시 전체 지배를 입증하지는 않는다**. 우크라이나 대통령·군 대변인 및 DeepState가 전면 점령 주장을 반박. 독립 취재: Reuters, DW, Meduza. | 러시아 측 **공식 주장 발표일** 확정; 전체 군사적 통제 완성일로 **확정 불가**. 서로 상충하는 발표를 같이 보존. |
| **2025-07-31 (ISW 분석 기준일)** | ISW/AEI Critical Threats Project는 약 **10km² 행정 구역 중 7.81km²** 러시아군 점유로 평가. **서쪽 시 경계까지의 전체 장악은 확인되지 않음**. GIS 좌표 및 분석의 독립 정확도는 미검증. | 실효 지배의 **상당한 부분**에 대한 분석적 평가. `7.81/10`은 원문 평가 수치이며 본 조사 GIS 면적 실측값 아님. |
| **2025-08-02** | 우크라이나군 Khortytsia 대변인은 러시아가 도시 일부를 점유했지만 **우크라이나군도 도시 일부를 유지하며 계속 교전 중**이라고 설명(RBC-Ukraine 인터뷰). 7월 31일 Interfax-Ukraine·DeepState의 반박과 같은 방향. | 적어도 **8월 2일 시점 도시 전체 함락일을 확정하지 않음**. 군 발표 자체는 독립 현장 위성/폴리곤 측정이 아님. |

**독립적인 사건 사료·원문 URL**
1. [Reuters, 2025-07-31: 러시아 점령 주장, 우크라이나 반박, 위치 검증 국기 영상](https://www.reuters.com/world/europe/russia-claims-capture-chasiv-yar-after-16-month-battle-2025-07-31/) — 언론 자체 영상 검증과 양측 공식 주장 구분.
2. [ISW/AEI CTP, 2025-07-31 분석](https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-july-31-2025) — 현장 지리 정보와 분석 모델에 따른 **7.81km² 추정**; Reuters와 다른 조사 조직.
3. [Interfax-Ukraine, 2025-07-31: 우크라이나 Khortytsia 공식 반박 및 DeepState 발표](https://en.interfax.com.ua/news/general/1092220.html) — 대변인 발언과 DeepState를 두 개의 독립 영상 사료로 과대계산하지 않음.
4. [RBC-Ukraine, 2025-08-02: 일부 러시아군·일부 우크라이나군 점유, 교전 계속](https://newsukraine.rbc.ua/news/ukraine-says-russian-claim-of-success-in-1754146024.html) — 같은 군 대변인의 후속 해명.
5. [Meduza, 2025-07-31: 공장·남서부 지역 및 양측 주장](https://meduza.io/en/news/2025/07/31/russia-claims-capture-of-chasiv-yar-in-eastern-ukraine) — 재인용 주장은 독립 관측으로 중복 계산 금지.
6. [유엔 총회 제11차 긴급특별회의 2025-02-24](https://www.un.org/en/ga/sessions/emergency11th.shtml) 및 [결의 ES-11/7 원문 경로](https://docs.un.org/A/RES/ES-11/7) — 우크라이나의 국제적 승인 국경과 영토 보전 맥락. **군사점령과 법적 주권 이전은 별개**.

**법적 판정:** 2025년 현지 군사 통제 분쟁만으로 차시우야르·도네츠크주를 국제법상 러시아 영토에 합법 편입하거나 새로운 국가가 성립했다고 기록하지 않음. UN의 영토보전 원칙과 러시아의 일방적 영유 주장, 군사적 현실을 구별. **법적 국제국경 변경·주권 양도·국가 lifetime 변동 확인 0건**. 유럽 전체 2025 변화 없음 판정은 아님.

## 2. 벡터자료 우선 탐색 — 직접 서비스, 이력과 유효기간을 별도 기록

| 제공기관/직접 URL | 판본·제작/갱신/실제 유효기간 | 형식·원본 CRS·객체 ID·유형(확인 수준) | 사용권 및 결론 |
| --- | --- | --- | --- |
| **ISW·AEI/CTP** [2025-07 러시아 진격 FeatureServer/0](https://services5.arcgis.com/SaBe5HMtmnbqSWlu/arcgis/rest/services/July_2025_Timelapse/FeatureServer/0) | 서비스 이름 `July_2025_Timelapse`. **시계열 범위 2025-07-01 15:00 UTC~07-31 15:00 UTC**; **데이터 최종 편집 2025-08-05**(보고 시점과 별개). 개별 차시우야르 객체의 현지 효력일 **미확인**. | **ArcGIS FeatureServer** 폴리곤 `esriGeometryPolygon`, **GeoJSON·JSON·PBF 조회 지원**, 서버 SR **EPSG:3857 (102100)**, `OBJECTID/Creator/EditDate/GlobalID_2/datetime` 등 **서비스 메타 조회**. 특정 개별 객체 ID·좌표/레이어 원본·현장 위상 **미열람**. ‘Advances’는 **새 진격분이지 전체 점령지도 아님**. | **저작권 ISW·AEI/CTP**. [ISW Fair Use and Attribution Policy (2026-01-08 개정)](https://understandingwar.org/fair-use-and-attribution-policy/)에 따르면 shapefile/dataset 복제·변경·다른 지도 제품 편입/재배포에 **사전 서면허가 필요**. 2025 당시 권리조건과 비교 미완료. **후보 유지, 제품 도입 금지**. |
| **ISW·AEI/CTP** [2025-07 점령 평가 FeatureServer/3](https://services5.arcgis.com/SaBe5HMtmnbqSWlu/ArcGIS/rest/services/July_2025_Timelapse/FeatureServer/3) | **시계열 2025-07-01~07-31 00:00 UTC**. 서비스 **최종 수정 2026-10-27** (과거 전선 효력일이 아님). 기준일별 동일 지도 편집이 2025 당시 모습과 동등함은 **미입증**. | **ArcGIS FeatureServer, `esriGeometryPolygon`**, GeoJSON/JSON/PBF 조회, 서버 SR **EPSG:3857**, `OBJECTID`·`datetime`·`GlobalID_2` 등 필드 이름 메타. **실제 피처 값·다각형·시간 유효범위 미열람**. | **위와 동일 제공기관·동일 2025-07 데이터 계열**. 진격 레이어와 독립 역사 사료 두 개로 세지 않음. 2026-10 소급 편집 가능성 및 권리·재배포 제한 탓에 **정본 도입 유보**. |
| **William & Mary geoBoundaries** [우크라이나 ADM2 API](https://www.geoboundaries.org/api/current/gbOpen/UKR/ADM2/), [고정판 GeoJSON](https://github.com/wmgeolab/geoBoundaries/raw/9469f09/releaseData/gbOpen/UKR/ADM2/geoBoundaries-UKR-ADM2.geojson), [원본 ZIP](https://github.com/wmgeolab/geoBoundaries/raw/9469f09/releaseData/gbOpen/UKR/ADM2/geoBoundaries-UKR-ADM2-all.zip) | **2006 경계 표상**, **2023-04-30** 원천 갱신·**2023-12-12** 빌드·고정 Git revision `9469f09`, 데이터셋 ID `UKR-ADM2-74538382`, 495 raion 객체 메타. **2025 전투·2020 행정구역 개편을 직접 설명하지 못함**. | **GeoJSON·ZIP** 직접 URL 확인, 실제 원본 다운로드/ZIP 내부 SHP 필수 구성 요소/CRS/개별 피처 ID/실제 Polygon·MultiPolygon **미확인**. 데이터셋 ID는 차시우야르 개별 ID 아님. | API 라이선스 **Public Domain** 표기(원출처 Wikimedia Commons; 세부 출처/공공저작물 적법성 별도 검토). **오래된 ADM2 행정구역 경계**이므로 **2025 점령선 직접 부적합**. |
| **ETH Zürich CShapes 2.0** [공식 판본·다운로드](https://icr.ethz.ch/data/cshapes/) | **1886~2019** 세계 국가·종속영토 경계, 2025 미수록. | **SHP·GeoJSON** 제공 명시. 2025 차시우야르 군사 통제의 피처·CRS·원본 **없음/미검증**. | **CC BY-NC-SA 4.0**, 비상업·동일조건 제한. **해당 2025 시점 직접 부적합**. |

**검색 범위 및 미발견 원인:** 국제분쟁 시계열의 ISW/CTP 2025-07 ArcGIS 레이어, 관련 우크라이나 법정 ADM2 공개 벡터, ETH 역사 국제경계를 선별. **2025-07-31~08-02 차시우야르의 모든 지역에 대해 정확한 실효 점령 시작·종료시점과 법적 귀속을 독립 검증하고 재배포할 수 있는 SHP 구성 ZIP/GPKG/GeoJSON/WFS 원본은 확보하지 못함**. ArcGIS **서비스가 존재**함과 특정 날짜의 **원본 지오메트리 정확도/재사용권 검증**은 다름. 기존 월별 진격/점령 형상을 다른 포맷으로 변환해도 독립 출처가 추가되지 않음. 공공 GPKG 또는 국가 공식 전투선 WFS의 **해당 일자·지역 직접 URL 미발견**.

## 3. 실제 실행한 검사와 미실행 검사

- **수행:** 원문/취재 기사 대조, 권리 정책·서비스/API·판본·기간/형상·서버 CRS·필드 메타의 **웹 열람**. 문헌 수준 출처상충 및 권리 보류 판정.
- **미실행:** 원본 SHP `.shp/.shx/.dbf/.prj` ZIP·GPKG·GeoJSON 파일 실제 **다운로드/열람**; ArcGIS 특정 피처 `GetFeature/query` 및 객체 값·좌표·CRS 원본 내 확인; 원본 SHA-256/라이선스 파일 확인; `ogrinfo`/`ogr2ogr` GDAL·임시 GeoJSON 파생본; 국가 ID 대조·실효 유효일별 피처 판정; 이웃 지역 접합·공유 경계·인접국·도서/월경지·위상·구멍/슬리버/교차 검사; Natural Earth 1:10M 동일 투영·범위·배율 비교; 독립 역사 형상 없는 0.5 CSS px 수치 검사.
- **구분:** 레이어의 메타 `esriGeometryPolygon/EPSG:3857/OBJECTID` 확인은 원본 파일 파싱·역사 정확도 검증 통과가 아니다. ISW `7.81km²`는 보고서 인용 수치이지 **본 조사 측정**이 아니다. **역사적 정확도 검증 완료 0개**.
- **후속 복원:** 합법적으로 쓸 수 있고 시점·인접 접합을 검증한 실제 원본이 없다면 **도시 주요 통제 경계 부분만** 독립 역사 지도 중첩·지오리퍼런싱·수작업 복원 *후보*로 유지. 이번 회차 **실행하지 않음**. 1:10M 표현 기준에서 필요 없는 개별 건물·미세 전선 변동은 제외하며 주요 도시의 양측 귀속과 연결관계가 판명될 때만 검토. **해안 변경 조사 없음**.

## 4. 미확인 사항·다음 회차 인계

1. 2025년 1월 공장 점거의 정확한 시각·법적 효력과 7월 31일/8월 2일의 **도시 완전 장악 여부·날짜** 미확정. 양측 주장과 ISW 평가를 하나의 확정 점령일로 합치지 않음.
2. ISW 월별 `datetime` 값·개별 feature ID, 2026-10 재편집 영향, 실제 2025-07-31 서부 경계선, 고지도 대조 독립 증거, 재배포 허가 미확인. 2006 geoBoundaries ADM2로 2025 통제선을 소급하지 않음.
3. 원문 미등록 `GEO-TIME-002/004/006/007/008`와 색인-원문 불일치 `GEO-TIME-010/011/012/013` 보류 **유지**; 원문 추정 재구성·삭제 금지.
4. **커서:** 마지막 완료 처리 지역 **유럽(GEO-TIME-029)** → 다음 **아시아(2025)**. 유럽·아시아·아프리카·북아메리카·남아메리카·오세아니아 모두 **2025년 전수 미완료**; **2024년 조사 착수 금지**. 별도 GEO-LIFE 상태 불변. 조사 하한 1801-01-01.
5. **보관 범위:** 위 보고서, 진행기록, 색인만. 국가 lifetime·역사 폴리곤·타임라인 정본·원시/변환 GIS·웹/앱/렌더러·Pando `work/gis`·`main`·다른 브랜치·배포 변경 **0건**. 상설 로컬 Pando 워크트리 미연결: `publish-reports`·`check-reports` 로컬 명령 **미실행**. GitHub 원격 파일 검증은 별도로 표기.
