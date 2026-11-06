# 2025년 유럽 — 우크라이나 쿠라호베 실효 지배 변화·역사 GIS 벡터 후보 (GEO-TIME-023)

> 조사일: 2026-11-07 KST · 연도: **2025, 잠정·전 세계 미완료** · 지역: **유럽** · 상태: `investigating / source-indexed / provisional / not-applied`  
> 사건: `EU-2025-002` (우크라이나 도네츠크주 쿠라호베·주변 지역 군사적 실효 지배 전환) · 신규 사건 묶음 1건 · 국제법상 주권·국경 확정 변경 0건 · GIS 정본/코드 반영 0건

## 0. 기존 조사 인계와 조사 선택

- 최신 진행기록은 GEO-TIME-022(2025 오세아니아) 다음 **2025 유럽**이다. Pando `work/gis`의 `AGENTS.md`, `docs/historical-border-reconstruction-policy.md`, `docs/historical-vector-source-workflow.md`를 확인했다. 해당 `work/gis`에는 `reports/README.md`와 `reports/geography/historical-timeline-yearly-progress.md`가 없고, 현행 `AGENTS.md`는 보고서 정본을 `PandoLab-library-data/reports/`에 보관하도록 지시한다. 외부 자료 저장소 `reports/borders/README.md`, `history/timeline/historical-timeline-yearly-progress.md`, 존재하는 연도·지역 원문과 보고서 목록을 확인했다.
- 이전 유럽 조사 `GEO-TIME-012`(쿠르스크–수자; **보고서 원문은 색인에만 남아 있음**) 및 `GEO-TIME-017`(지브롤터–스페인, 원문 확인)과 사건·공간을 분리했다. 이번 도네츠크 **쿠라호베(Kurakhove / Курахове)**는 러시아 영내 쿠르스크와 다른 사건이며 중복 신규 집계가 아니다. 2024년의 선행 전투와 2025년 결과를 혼동하지 않는다.
- 거시적 전선 변화의 대표적인 도시·주요 도로 결절점으로서 선별했다. 도시 자체가 약 500km² 기준을 충족한다고 주장하지 않으며, 상위 정책 §0의 **중요 도시 귀속 예외**로 조사한다. 2025 도네츠크 전역 점유면적·연결 구역 면적은 측정하지 않았다. 하천 수위·해안선·간척·침식은 연구 대상에서 제외한다.
- Pando `work/gis` 최근 확인 HEAD `30a8402ac82a3e8a24f943f777a7aaedec211279`(2026-11-06 UTC, Viewer Worker 관련 병합). 동시 작업 영역을 수정하지 않는다.

## 1. 사건 및 실제 날짜 — 법적 영토와 실효 지배 구분

| 실제 일자 | 사건·출처 | 판정 |
| --- | --- | --- |
| **2025-01-06** | 러시아 국방부가 쿠라호베 전체 장악을 **발표**. 우크라이나군 호르티차 부대 대변인은 같은 날 시내 교전 지속을 설명. [Reuters, 2025-01-06 보도, 01-07 최종 갱신](https://www.reuters.com/world/europe/russia-says-it-captures-kurakhove-eastern-ukraine-2025-01-06/), [AP 2025-01-06](https://apnews.com/article/1a43d984adf4543b582c61d487fa1cff). | **러시아 점령 완료 주장과 우크라이나 반박이 병존**. 01-06을 '검증된 전 지역 점령 확정일'로 저장 금지. |
| **2025-01-07** | 우크라이나 민간 OSINT **DeepState**는 01-06 말 기준 도시 **거의 전체**가 러시아군 통제라고 평가, 발전소 주변 관측초소 등 잔여 지역 언급. [Ukrainska Pravda, 2025-01-07](https://www.pravda.com.ua/eng/news/2025/01/07/7492469/). | 2025년 **도시 대부분 실효 지배 전환**의 독립 관측. 구역별 정확한 전환시각/전면 장악 미확정. |
| **2025-01-11** | DeepState가 밤사이 지도를 갱신하며 쿠라호베 러시아군 점령으로 표시. [Ukrainska Pravda, 2025-01-11](https://www.pravda.com.ua/news/2025/01/11/7493004/). 같은 날 우크라이나군 대변인은 부대의 잔존 위치를 주장. [RBC-Ukraine, 2025-01-11](https://newsukraine.rbc.ua/news/deep-state-claims-full-occupation-of-kurakhove-1736589495.html). | **지도 표기 갱신일은 실제 최종 점령일과 다를 수 있음**. 러시아군의 상당한 실효 통제는 확인되지만 **완전 점령의 정확한 효력일은 유보**. |
| **2025-01-11** | ISW/CTP는 쿠라호베 방면 11일 새 러시아군 진격 주장 중 **확인된 신규 전진 없음**으로 평가. [ISW/CTP 2025-01-11](https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-january-11-2025). | '당일 확인된 신규 전진 없음' ≠ 도시 전체가 우크라이나 통제라는 의미. DeepState와 동일 조사조직이 아닌 별도 분석임. |
| **2025-02-24** | 유엔총회 결의 **A/RES/ES-11/7**에서 우크라이나 영토 보전·국제법적 평화 원칙 재확인. [유엔 공식 결의 A/RES/ES-11/7](https://docs.un.org/A/RES/ES-11/7), [당일 보도](https://www.theguardian.com/world/2025/feb/24/un-general-assembly-russia-ukraine-war). | 군사적 점유선·러시아의 병합 주장과 별도로 **2025년 새 국제법상 국경·주권 이양 인정 근거 0건**. |

**독립성:** Reuters와 AP의 동시대 취재는 서로 다른 보도기관이며 양측 국방당국의 *동일 발표 인용*은 독립적인 두 개의 점령 확인이 아니다. DeepState의 원지도 관측은 제3의 분석 자료지만 이를 전재한 언론 기사들을 별개의 독립 OSINT로 세지 않는다. ISW/CTP는 또 다른 관측체계이며 특정 날짜/피처의 상세 비교는 미실행. 공식 양국의 충돌하는 발표는 각자의 주장으로 보존한다.

**대상 일자/주권 분리:** 러시아의 2022년 도네츠크 병합 주장 및 그 전후 교전은 2025 신규 국가 수립이나 국제법상 합법적 영토 이전이 아니다. 2025-01-06·07·11은 **공표·관측·갱신일**로 기록하며 단일한 '법적 유효일'로 합치지 않는다. 도시가 장기간 저항한 사실과 대규모 지역 전선을 역사 국경으로 동일시하지 않는다. 공식 법적 러시아–우크라이나 국제경계 변경 확인 0건; 전쟁 중 실효 지배 변화 1개 묶음.

## 2. 역사적 GIS 벡터 우선 탐색

검토 대상은 **실효 지배의 2025년 1월 시점**이다. 먼저 시기별 점유선 폴리곤을 탐색했으며, 그 다음 법적 행정경계와 국경의 참고용 대조자료를 구분했다. 현재 조사에서 원본 ZIP/SHP·GPKG 파일 자체는 입수하지 않았고, 서비스 **메타데이터 조회**와 공개 설명만 확인했다.

| 제공기관·직접 URL | 판본·시점·범위 | 형식·좌표계·객체 ID·유형 | 권리·적합성 |
| --- | --- | --- | --- |
| **ISW/AEI-CTP** [JAN2025Timelapse FeatureServer/1](https://services5.arcgis.com/SaBe5HMtmnbqSWlu/ArcGIS/rest/services/JAN2025Timelapse_Ukraine_Russia_War/FeatureServer/1), [서비스 전체](https://services5.arcgis.com/SaBe5HMtmnbqSWlu/ArcGIS/rest/services/JAN2025Timelapse_Ukraine_Russia_War/FeatureServer) | **2025-01-01~01-31** 분석 시간범위. 서비스의 **데이터 최종 편집 2025-04-16**은 조사대상 시점과 별도. 2025년 1월 러시아군의 'assessed control of terrain' 우크라이나 내 지도. **쿠라호베의 01-06/07/11 개별 피처 유효기간은 미확인**. | ArcGIS **Feature Layer**, GeoJSON·JSON 쿼리 지원(개별 결과 미요청), `esriGeometryPolygon`; **서비스 표기 SR 102100 (EPSG:3857)**; `OBJECTID`(시스템 관리), `datetime`, `Creator`, `EditDate`, `MERGE_SRC` 등의 **스키마 메타** 확인. 개별 피처 ID·원본 SHP/CRS **미확인**. | 당시 실효 지배선의 **가장 관련성 높은 후보**, 그러나 역사적 범위/변경 유효일·레이어별 정확도 미검증. [ISW 저작권·이용 정책](https://understandingwar.org/fair-use-and-attribution-policy/)에 따라 **복제·변형·상업적 사용·데이터셋 편입은 사전 서면허가 필요**. 제품 정본 도입 유보. |
| **우크라이나 국가 지리공간정보 기반시설 (NSDI)** [공식 포털 문서](https://nsdi.gov.ua/docs/portal/) | 국가 지도·행정구역 및 메타데이터 플랫폼. 2025년 전쟁 중 **군사적 점유선의 유효기간 레이어는 미발견**. | 국가 공식 지오포털/서비스 목록 안내 확인. 쿠라호베 2025 **직접 SHP·GPKG·GeoJSON·WFS 레이어 URL, 피처 종류/ID·CRS 미확인**. | **법적 행정기반선 탐색 후보**, 군사 실효 지배선의 대체자료 아님. 데이터별 사용·재배포권 미확인. |
| **William & Mary geoBoundaries** [UKR ADM1 API](https://www.geoboundaries.org/api/current/gbOpen/UKR/ADM1/), [고정판 GeoJSON](https://github.com/wmgeolab/geoBoundaries/raw/9469f09/releaseData/gbOpen/UKR/ADM1/geoBoundaries-UKR-ADM1.geojson), [원본 ZIP](https://github.com/wmgeolab/geoBoundaries/raw/9469f09/releaseData/gbOpen/UKR/ADM1/geoBoundaries-UKR-ADM1-all.zip) | **2017년 경계 표상**, OSM/Wambacher 원천 **2023-01-19 갱신**, **2023-12-12 빌드**. 우크라이나 ADM1 27개, 메타 `UKR-ADM1-14850775`, 릴리스 커밋 `9469f09`. | **GeoJSON·ZIP(SHP 포함 여부 원본 미확인)** 후보, 행정구역 **폴리곤**으로 기술; **실제 .prj/원본 CRS·개별 피처 ID·Polygon/MultiPolygon 미확인**. `UKR-ADM1-14850775`는 **데이터셋 ID**이지 쿠라호베 피처 ID가 아님. | **ODbL 1.0**(OSM 저작자표기·Share-Alike 등 준수 필요). 2017 법정 행정경계로부터 **2025 전투 통제선/군사점령 폴리곤 소급 불가**. |
| **ETH Zürich CShapes 2.0** [공식 설명·다운로드](https://icr.ethz.ch/data/cshapes/) | 세계 **1886~2019** 역사 국가경계. CShapes-Europe 1816 이후, 본 글로벌판은 **2025년 미수록**. 제작/최신 소스 판본은 공식 2.0, 2025 쿠라호베 상세 시계열 피처 **없음**. | **Shapefile·GeoJSON** 형식 게시. 대상 지역·시점의 레이어/CRS/객체 ID/폴리곤 유형 **미검증**. | **CC BY-NC-SA 4.0**, 비상업·동일조건 제한. 2025 전쟁 통제선 및 법적 국경 변화 근거로 **직접 부적합**. |

**검색 범위/미발견 이유:** ISW–CTP 2025-01 시간 레이어, 국가 NSDI 공개 지리포털, geoBoundaries ADM1 API, ETH CShapes 공식판을 조사했다. ISW의 서비스가 존재하나 **쿠라호베 개별 역사시점 피처·정확도·재사용권 검증 미완료**. 다른 공공·학술 후보는 2025년 실효점유선이 아닌 법적 행정단위이거나 2019년에 끝난 역사 경계다. 따라서 **독립 검증되고 제품 재배포 가능한 2025-01-06/07/11 통제선 SHP/GPKG/GeoJSON 원본은 미확보**다. 같은 GIS의 SHP와 GeoJSON이 존재해도 독립 사료 2건으로 세지 않는다.

## 3. 데이터 확인·검증 상태의 정확한 구분

| 항목 | 이번 회차 |
| --- | --- |
| 원법령/전시 양측 공식 주장 및 독립 보도 일자 | **문헌 열람·출처 구분 완료**, 최종 전체 점령일 불확정 |
| ISW 2025-01 FeatureServer 서비스의 Polygon·SR·필드·시간 범위 | **서비스 HTML 메타 확인**, 실제 개별 피처 미열람 |
| 국가 NSDI·geoBoundaries·CShapes | **포털/메타 조회**, 대상 사건의 유효 기하 확인 불가 |
| 원본 SHP(.shp/.shx/.dbf/.prj) ZIP·GPKG·GeoJSON 파일 다운로드/열람 | **미실행** |
| 원본 내 CRS·피처 ID/유형/시간 속성 직접 검증·SHA256 해시 | **미실행** (서비스 메타와 원본 검증은 별개) |
| GDAL `ogrinfo`/`ogr2ogr`·임시 GeoJSON 파생본·원본 보존 비교 | **미실행** |
| 러시아–우크라이나 법적 국경·인접 지역 접합·공유 경계/도서·월경지·구멍·슬리버·위상 | **미실행** |
| Natural Earth 1:10M 동일 투영/배율 화면 비교·0.5 CSS px 정량 검사 | **미실행/통과 아님**, 독립 역사 기준선 미확보 |
| 날짜별 군사 통제 지도 ↔ 실제 법적 국경 역사 정확도 | **검증 완료 아님** |
| 제품 정본 형상·국가 lifetime·타임라인·앱/웹/렌더러 변경 | **0건** |

**보고 상태:** `source-indexed / provisional / not-applied`. 독립 분석 결과의 '거의 전체 점령' 관측은 역사적 군사 변화의 근거이지만 단독으로 `historically-verified` 또는 지도 적용 승인을 부여하지 않는다. ISW 사용권이 명시적으로 제한적이므로 **제품 편입/배포 불허 상태**를 유지한다. 보유하지 않은 원본과 CRS를 가정해 GeoJSON을 생성하지 않는다.

## 4. 미완료·후속 인계

1. **유럽 2025 전수 미완료:** 이번 조사 범위 외 사건 조사 계속. 같은 쿠라호베 사건을 새 발견으로 다시 집계하지 않는다. 도시 완전 점령의 정확한 날짜, 잔여 발전소·서측 방어, 전선 이동 연결구역/면적(§0.1) 등은 미확정이다.
2. 2025-01 ISW/CTP **개별 시간 피처** 및 DeepState가 사용한 지도 증거의 날짜별 독립 비교, 원본·CRS·레이어·피처 ID·권리·정량/위상 검사는 별도 승인·합법적 이용 전 검증 후속으로 보류. **배포권 없는 외부 원본 수집을 제품 작업으로 전환하지 않는다**. 재배포 가능한 역사적 실효 지배 벡터가 없으면 중요 구역만 역사 지도의 후속 중첩/지오리퍼런싱/수작업 복원 *후보*로 남기되 본 회차에는 실행하지 않는다.
3. 기존 진행기록에 남은 `GEO-TIME-002/004/006/007/008` 원문 미등록 및 `GEO-TIME-010/011/012/013` 색인-원문 불일치를 **그대로 보존**한다. 원문을 유추 재생성·무단 복구·색인에서 삭제하지 않는다.
4. **지역 순환:** 마지막=**유럽(2025)**, 다음=**아시아(2025)**. 유럽·아시아·아프리카·북아메리카·남아메리카·오세아니아 모두 **2025년 전수 미완료**, 전수 완료/변화 없음 기록 전 **2024년으로 이동 금지**. 별도 GEO-LIFE 국가 존속기간 순환 기록과 독립. **1801-01-01 이전 조사 제외**.
5. 이번 회차의 유럽 소범위에서 **국가 성립/소멸·합법적 국제국경 획정·주권 양도 확인 0건**이라는 판정은 유럽 전체의 `변화 없음` 판정과 다르다.

**보관 범위:** 자료 저장소 `reports/borders/history/timeline/`에 이 보고서 및 인계 기록, `reports/borders/README.md` 색인 텍스트만. 실효 지배·국가 정본 GIS, 제품 소스, Pando `work/gis`/`main`/다른 브랜치, 배포 **전부 변경 0건**. 원본·파생 GIS 바이너리 추가 0건. 현장 로컬 `node tools/library-data.mjs --publish-reports`/`--check-reports` 명령은 사용 가능한 Pando 상설 워크트리가 없어 **미실행**; GitHub 원격 텍스트 파일 바이트·SHA 검증과 구분한다.
