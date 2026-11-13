# HydroRIVERS 한국어명·관계정보 OSM 의존성 교체 조사
> 보고서 ID: `GEO-HYDRO-OSM-20261024` · 상태: `investigating / inventory-complete` · 지도 반영: `not-applied` · 색인일: 2026-10-24  
> 조사 기준: Pando `work/gis` / 수계 데이터 v0.13.2, 외부 자료 pin `71a67904db2beb933735727ad6c19adde082d2bd`

## 이전 검증 차수: 비OSM 이름·관계 메타데이터 40/73개 (2026-10-24)

> 이 절이 아래 과거 '33개 검증' 및 이전 단계의 진행 수치를 대체한다. 과거 절은 작성 당시 검증 이력으로 유지한다.

- 대상 원본 73개 중 **40개 수계의 OSM 관계 및 관련 이름 메타데이터를 독립 출처로 교체한 검증용 패키지** 생성 성공. **8개 대표명 정정**, **32개 기존 대표명 유지·관계/별칭 교체**, **33개 미완료**.
- GitHub Actions [GIS OSM river name dependency inventory — 성공](https://github.com/kimjeon-il/Pando/actions/runs/40050627940)에서 73개 재추출, NE 본류 재비교, USGS 관측소 검증, 정부 출처 우선 기준·문헌 확인 테스트, 생산 디코더 검증을 통과.
- 원본 Hydro **16,548개 feature/902개 pack/3개 shard**의 판독 성공. **1,884개 feature 메타데이터 변경**. 기존 공간 인덱스와 하천 형상 shard 3개의 SHA-256은 이전과 바이트 단위로 동일.
- 원본 bundle SHA-256 `91c2268c6dbfdfa7fc6103d8ad0b4eeca71f6c522df5c0118db69a3654ff532a` · 시험 bundle SHA-256 `b92f80f9c971f3dbac8511522652665ab57437b233599a51bc5b36980e8554ca`.
- 검증 결과 [staged-40-proof.json](staged-40-proof.json), 격리된 [Hydro 패키지(일시적 Actions 자료)](https://github.com/kimjeon-il/Pando/actions/runs/40050627940/artifacts/12543715131), [개별 73개 판정](inventory.json).

### 신규 조사 및 교체 검증 7개

| 시스템 ID | 기존 → 검증본 | 공식·독립 출처 및 판정 |
|---|---|---|
| `10047863` | 나일강 → 나일강 | [나일강유역기구 NBI](https://nilebasin.org/nile-basin) · 독립 NE 본류 Nile 55.6%와 White Nile 19.8%, 백나일·청나일·소밧강 관계 보존 |
| `20244836` | 네만강 → 네만강 | [리투아니아 환경부](https://am.lrv.lt/uploads/am/documents/files/Raudonoji%20knyga/index.html) · NE Neman 35.8% / Neris 67.9%, 독립 지류 네리스강 보존 |
| `40017702` | 아무르강 → 아무르강 | [러시아 연방수자원청](https://voda.gov.ru/maps/khabarovskiy-kray/) · NE Amur 59.3% / Ussuri 44.4%, 별개 우수리강 분류 보존 |
| `70814357` | 미시시피강 → 미시시피강 | [미국 EPA](https://www.epa.gov/ms-htf/mississippiatchafalaya-river-basin-marb), [USGS](https://pubs.usgs.gov/ha/ha730/ch_f/F-text1.html), NE Mississippi 48.1% / Arkansas 34.6%. 독립 리오그란데 유역 별칭 제거 |
| `20265844` | 드르벵차강 → **비스와강** | [폴란드 정부](https://www.gov.pl/web/infrastruktura/wspolpraca-miedzynarodowa-w-gospodarce-wodnej) 부크강→나레프강→비스와강과 [별도 드르벵차 지류](https://samorzad.gov.pl/web/powiat-nowomiejski/informacja-o-powiecie) 확인. NE Vistula 51.9% / Western Bug 40.7% |
| `20386022` | 센강 → 센강 | [프랑스 수자원청](https://eau-seine-normandie.fr/agence-de-leau/le-bassin-de-la-seine) 및 [정부 홍수감시청](https://www.drieat.ile-de-france.developpement-durable.gouv.fr/vigicrues-a29.html), NE Seine 46.9%, 대체 강명 후보 없음 |
| `40279876` | 두만강 → 두만강 | [한국 통일부 북한지도](https://nkinfo.unikorea.go.kr/nkp/search/search.do?query=%EB%91%90%EB%A7%8C%EA%B0%95), [중국 창바이산 관리기구](https://www.changbaishan.gov.cn/zjzbs/zrzy/201612/t20161229_208378.html), NE Tumen 50.6% |

### 미교체 33개 — 독립 문헌 확보 및 다음 검사

- [남은 33개 전수 조사·우선순위](remaining-33-priority.json): Natural Earth 독립 명칭 선형 부재 **17개**, 본류/지류/객체분류 혼입 의심 **14개**, 명칭·경로 추가 검증 필요 **2개**.
- `20773860`, `20774342` [수에즈운하청](https://www.suezcanal.gov.eg/English/About/SuezCanal/Pages/AboutSuezCanal.aspx)은 수에즈 운하가 인공 수로임을 명시. 현재 `수에즈운하강`으로 표시되는 원인에는 Hydro의 강 객체 유형 및 한국어명 접미사 규칙이 포함될 수 있으므로 단순 이름 교체를 보류.
- `41337891` [태국 왕립관개청](https://www.rid.go.th/th/rid_news/28997)은 빠삭강이 짜오프라야강에 연결되는 별도 수로임을 설명. 현재 Hydro 본류는 NE 욤강 69.1% / 짜오프라야강 34.6% 근처여서 단일 이름 승격 금지.
- `41182380` [베트남 박닌성 공식 지리자료](https://bacninh.gov.vn/news/-/details/37632/he-thong-song-ngoi-215681)는 꺼우강이 타이빈강 유역에 속한다고 명시. 해당 Hydro 본류는 NE 홍강 37%와 매칭되어 있으므로 독립 형상 재분리 필요.
- `41023100` [세계은행 1960년 인더스 유역 자료](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/855531468078531004)에서 라비강과 인더스강은 별개의 하천임이 확인되지만, Hydro 본류가 여러 하천 구간과 맞닿으므로 단일 대표명 검증을 보류.

**실제 지도 데이터 원본·웹 앱 및 작은 OSM 출처 링크는 변경하지 않았다.** 검증용 분리 패키지의 33개 잔여 OSM 관계정보가 모두 제거되고 별도 국가경계 OSM 의존성까지 확인된 뒤에만 지도 출처 표시 삭제를 검토한다.

## 확정된 원본 범위

- 수계 3,818개 중 **OSM relation이 한 개 이상 연결된 수계 73개**를 `hydro.bin`의 메타데이터 core/detail SHA-256 검증 후 확인했다. 전수 재현은 `tools/inventory-osm-hydronyms.py` 및 GitHub Actions GIS OSM river name dependency inventory.
- 과거 한글 이름 교정표의 명시적 수계 **26개**, 그중 73개와 중복 **3개**. 따로 검토할 명시적 교정표 수계 **23개**.
- 현재 명칭 혼입 또는 본류 대응 불일치 의심: **23개** (독립 GIS 자료와 아직 대조하지 않은 잠정 위험 판정).
- **중요:** 73개는 'OSM 원문만으로 명명된 강'의 수가 아니다. `OsmWaterwayIndex`는 관계의 bbox와 수계 bbox를 겹쳐 연결하므로 별개 강의 이름과 별칭을 섞을 수 있다.
- HydroRIVERS 경로·수계 ID는 변경하지 않았으며, 이 단계에서는 기존 OSM 정보가 포함된 지도 패키지를 제거하거나 출처 링크를 삭제하지 않았다.

## 검토·교체 규칙

1. 실제 본류 경로와 유역, 하구, 대표명 범위를 독립 자료로 확인한다. bbox 중첩만으로 이름을 승인하지 않는다.
2. 현행 Natural Earth 1:10m 공공영역 하천명을 1차 후보로 삼고, 미국 하천은 USGS GNIS, 외국 지명은 NGA GNS 또는 발행국 공식 지명·수문 자료로 확인한다.
3. 승인된 한국어명 교정표는 기계적으로 삭제하지 않는다. 해당 이름을 뒷받침하는 OSM 외 근거(공식 문헌·Wikidata CC0 자료·한국어 용례)를 각각 확인한다.
4. `aliases`와 `tributaryNames`도 원천 단위로 분리한다. 관계ID가 다른 수계에 재사용되거나 추정 영역이 너무 넓으면 자동 보강을 금한다.
5. 검증된 새 메타데이터에서 OSM `osmRelationIds`, OSM 유래 이름·별칭·경로를 완전히 제거하고 HydroRIVERS/NE 원본 지오메트리를 바이트 단위로 보존한 뒤 웹·앱을 함께 재검증한다.

독립 자료: [Natural Earth rivers](https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-rivers-lake-centerlines/) · [USGS GNIS](https://www.usgs.gov/us-board-on-geographic-names/download-gnis-data) · [NGA GNS](https://geonames.nga.mil/geonames/GNSHome/) · [Wikidata CC0](https://www.wikidata.org/wiki/Wikidata:Licensing).

## 이름 혼입 또는 구간 오판 후보 (독립 대조 전)

| Hydro system ID | 현재 명칭 | 검토 사유 |
|---|---|---|
| `20265844` | 드르벵차강 | 드르벵차강 수계에 부크강 관계명 유입 가능성 |
| `20282220` | 엘베강 | 엘베강에 오데르강 별칭 Oder/Odra가 유입됨 |
| `20446779` | 루아르강 | 루아르강에 센강 별칭 Seine이 유입됨 |
| `20680587` | 과디아나강 | 과디아나강과 과달키비르강 후보의 지리적 불일치 |
| `20773860` | 수에즈운하강 | 운하를 강으로 표기(수에즈운하강) |
| `20774342` | 수에즈운하강 | 운하를 강으로 표기(수에즈운하강) |
| `40423228` | 남한강 | 한강 수계 전체를 남한강으로 이름붙였을 가능성 |
| `40485117` | 아라카와강 | 도네강과 아라카와강의 위치·별칭 불일치 |
| `40613666` | 장강 | 장강과 별개인 메콩강 별칭의 혼입 |
| `41023100` | 라비강 | 인더스강 본류 후보에 라비강 이름 부여 여부 조사 필요 |
| `41067217` | 브라마푸트라강/얄룽창포강 | 갠지스강과 브라마푸트라강 본류 이름 범위 조사 필요 |
| `41109275` | 난판강 | 난판강과 별개인 홍강/Red 별칭의 혼입 |
| `41171836` | 룩남강 | 룩남강과 꺼우강 관계명의 동일성 검토 필요 |
| `41182380` | 꺼우강 | 홍강 수계 범위에 꺼우강 관계명 혼입 여부 확인 필요 |
| `41279826` | 브라마푸트라강/얄룽창포강 | 살윈강 지역에 브라마푸트라강 명칭 매칭 의심 |
| `41337891` | 빠삭강 | 빠삭강과 욤강의 관계·별칭 혼입 여부 확인 필요 |
| `50261309` | 마하캄강 | 바리토강 지역에 마하캄강 명칭 매칭 의심 |
| `70576631` | 서스쿼해나강 | 서스쿼해나강과 델라웨어강의 명칭·위치 범위 검토 필요 |
| `70580124` | 서스쿼해나강 | 서스쿼해나강과 델라웨어강의 본류 범위 검토 필요 |
| `70617856` | 새크라멘토강 | 새크라멘토강과 샌와킨강의 본류·지류 구분 검토 필요 |
| `70814357` | 미시시피강 | 미시시피강에 별개인 리오그란데강 관계명 혼입 |
| `70816878` | 리오그란데강 | 리오그란데강 후보의 위치 범위(텍사스 내 타 수계 가능성) 확인 필요 |
| `70819626` | 리오그란데강 | 리오그란데강 후보의 위치 범위(텍사스 내 타 수계 가능성) 확인 필요 |

## OSM 관계 연결 73개 전체 목록

| ID | 한국어 대표명 | OSM 관계 ID | 검토상태 |
|---|---|---|---|
| `10047863` | 나일강 | 50793, 1657491 | 독립 근거 확인 대기 |
| `10521208` | 샤리강 | 2631912 | 독립 근거 확인 대기 |
| `10526283` | 샤리강 | 2631912 | 독립 근거 확인 대기 |
| `20071308` | 오울루강 | 9445500 | 독립 근거 확인 대기 |
| `20075401` | 오울루강 | 9445500 | 독립 근거 확인 대기 |
| `20081953` | 북드비나강 | 2649819, 2824464 | 독립 근거 확인 대기 |
| `20244836` | 네만강 | 189775 | 독립 근거 확인 대기 |
| `20265844` | 드르벵차강 | 1314266, 2712795 | 명칭 혼입 의심 |
| `20282220` | 엘베강 | 387605 | 명칭 혼입 의심 |
| `20282318` | 오데르강 | 387605 | 독립 근거 확인 대기 |
| `20323928` | 라인강 | 2192950 | 독립 근거 확인 대기 |
| `20336821` | 템스강 | 2263653 | 독립 근거 확인 대기 |
| `20342955` | 스헬데강 | 324288 | 독립 근거 확인 대기 |
| `20386022` | 센강 | 962076 | 독립 근거 확인 대기 |
| `20446779` | 루아르강 | 962076 | 명칭 혼입 의심 |
| `20452421` | 돈강 | 1405518, 2241333 | 독립 근거 확인 대기 |
| `20456598` | 우랄강 | 214415 | 독립 근거 확인 대기 |
| `20457454` | 남부크강 | 3160619 | 독립 근거 확인 대기 |
| `20478829` | 드네스트르강 | 2474595 | 독립 근거 확인 대기 |
| `20498112` | 도나우강 | 157031, 1566139, 1567969, 2186067, 2249121 | 독립 근거 확인 대기 |
| `20532766` | 테레크강 | 2471690 | 독립 근거 확인 대기 |
| `20540915` | 테레크강 | 2471690 | 독립 근거 확인 대기 |
| `20561290` | 리오니강 | 3396398 | 독립 근거 확인 대기 |
| `20565620` | 리오니강 | 3396398 | 독립 근거 확인 대기 |
| `20588291` | 도루강 | 2566210 | 독립 근거 확인 대기 |
| `20597827` | 마리차강 | 12796993 | 독립 근거 확인 대기 |
| `20628098` | 아무다리야강 | 223008 | 독립 근거 확인 대기 |
| `20673409` | 과디아나강 | 289968 | 독립 근거 확인 대기 |
| `20680587` | 과디아나강 | 289968 | 명칭 혼입 의심 |
| `20773860` | 수에즈운하강 | 7719838 | 명칭 혼입 의심 |
| `20774342` | 수에즈운하강 | 7719838 | 명칭 혼입 의심 |
| `30145067` | 오비강 | 157622, 2098340, 2469254, 13864527 | 독립 근거 확인 대기 |
| `40017702` | 아무르강 | 161305, 170539, 197653, 198568 | 독립 근거 확인 대기 |
| `40145639` | 시르다리야강 | 1206456 | 독립 근거 확인 대기 |
| `40188382` | 시르다리야강 | 1206456 | 독립 근거 확인 대기 |
| `40190238` | 아무다리야강 | 223008 | 독립 근거 확인 대기 |
| `40279876` | 두만강 | 6970997 | 독립 근거 확인 대기 |
| `40351117` | 압록강 | 2899525, 17250669 | 독립 근거 확인 대기 |
| `40364680` | 청천강 | 5454222 | 독립 근거 확인 대기 |
| `40391614` | 대동강 | 3858130 | 독립 근거 확인 대기 |
| `40414035` | 례성강 | 13705291 | 독립 근거 확인 대기 |
| `40415850` | 림진강/임진강 | 5488146 | 독립 근거 확인 대기 |
| `40423228` | 남한강 | 5486141, 5488155 | 명칭 혼입 의심 |
| `40475481` | 금강 | 17966007 | 독립 근거 확인 대기 |
| `40485117` | 아라카와강 | 3922416 | 명칭 혼입 의심 |
| `40486439` | 아라카와강 | 3922416 | 독립 근거 확인 대기 |
| `40505530` | 낙동강 | 11698958 | 독립 근거 확인 대기 |
| `40613666` | 장강 | 215354, 396599, 403702, 9392345 | 명칭 혼입 의심 |
| `41023100` | 라비강 | 325142 | 명칭 혼입 의심 |
| `41067217` | 브라마푸트라강/얄룽창포강 | 1067987, 1236345 | 명칭 혼입 의심 |
| `41109275` | 난판강 | 2377017 | 명칭 혼입 의심 |
| `41171836` | 룩남강 | 3388654, 9101784 | 명칭 혼입 의심 |
| `41182380` | 꺼우강 | 2377017, 3388654 | 명칭 혼입 의심 |
| `41225082` | 람강 | 393967 | 독립 근거 확인 대기 |
| `41261061` | 시탕강 | 233960 | 독립 근거 확인 대기 |
| `41279826` | 브라마푸트라강/얄룽창포강 | 1067987 | 명칭 혼입 의심 |
| `41337891` | 빠삭강 | 229599 | 명칭 혼입 의심 |
| `41339527` | 짜오프라야강 | 227317 | 독립 근거 확인 대기 |
| `41347969` | 바강 | 8529973 | 독립 근거 확인 대기 |
| `41386179` | 미명명 수계 41386179 | 9856326 | 독립 근거 확인 대기 |
| `41386700` | 미명명 수계 41386700 | 16740801 | 독립 근거 확인 대기 |
| `41390476` | 발라이강 | 9733190 | 독립 근거 확인 대기 |
| `41392598` | 메콩강 | 215354 | 독립 근거 확인 대기 |
| `50170097` | 마하캄강 | 7910696 | 독립 근거 확인 대기 |
| `50261309` | 마하캄강 | 7910696 | 명칭 혼입 의심 |
| `50798885` | 야라강 | 2211681 | 독립 근거 확인 대기 |
| `70576631` | 서스쿼해나강 | 3339284 | 명칭 혼입 의심 |
| `70580124` | 서스쿼해나강 | 3339284 | 명칭 혼입 의심 |
| `70617856` | 새크라멘토강 | 6704812 | 명칭 혼입 의심 |
| `70814357` | 미시시피강 | 1075500, 1756854, 1756890, 2716682, 11069321 | 명칭 혼입 의심 |
| `70816878` | 리오그란데강 | 2716682 | 명칭 혼입 의심 |
| `70819626` | 리오그란데강 | 2716682 | 명칭 혼입 의심 |
| `70842751` | 리오그란데강 | 2716682 | 독립 근거 확인 대기 |

## 2026-09-16 과거 교정표

- 26개 ID 중 이 조사 73개와 겹치지 않는 23개는 **별도 교정표 유지 대상**으로 판정 보류. 과거 OSM을 본류 동일성 근거로 인용했더라도 공식 문헌/Wikidata 등 독립 증거가 존재하는지 항목별 점검한다.
- 원본: [고정된 교정표](https://github.com/kimjeon-il/Pando/blob/6b0c501dd09029ef237e90c1ef55fdb82bdf315f/assets/data/hydro/hydronym-ko-overrides.json) · [23개 승인 원문 조사](https://github.com/kimjeon-il/Pando/blob/6b0c501dd09029ef237e90c1ef55fdb82bdf315f/reports/hydro-names/europe-major-rivers.md)

## 검증 결과와 한계

- 실행함: 데이터 manifest의 `metadata-core/detail` SHA-256 검증, 중복·누락 없는 73개 논리 수계 추출, 옛 교정표 26개와 ID 비교.
- 미실행: 73개 전부의 독립 원천 문헌 대조, 실제 본류의 거리/유역 수치 검증, 재패키징·WASM·브라우저 동등성 검사.
- `inventory.json`의 `reviewState`는 독립 검증 완료 또는 잘못된 이름 최종 판정이 아니다.
- 원본 OSM 조사 자료·권리 기록은 역사 연구 증거로 보존한다.

## Natural Earth 독립 선형 비교 (추가 조사)

- [73개 수계별 본류·명칭 대조 수치](ne-crosscheck.json) — OSM과 무관한 Natural Earth `rivers_base.geojson`의 SHA-256을 검사한 후, 실제 배포 수계 **본류**의 각 길이 비례 81표본을 1:10m Natural Earth 하천과 공간 대조했다.
- 소스 SHA: `3391aa917d3707be8da0a133b5a3bde26594e8b87648cb7f533d0df4fd8bcc99`; 이름 있는 Natural Earth 선분 **4,226개**.
- 대조 허용 범위 `0.14°`는 조사용 후보 범위일 뿐 위치 정확도나 확정 오차가 아니다. 점표본의 근접 비율은 지오메트리 독립 비교이며, 최종 이름 승인과 구분한다.

| ID | 현재 대표명 | 독립 NE 본류 후보 | 81표본 근접률 | 별도 검증 자료 |
|---|---|---|---:|---|
| `20680587` | 과디아나강 | 과달키비르강 (Guadalquivir) | 97.5% | [기관 원문](https://www.boe.es/buscar/doc.php?id=BOE-A-2013-5319) |
| `20773860` | 수에즈운하강 | 수에즈운하 (Suez Canal) | 85.2% | [기관 원문](https://www.suezcanal.gov.eg/English/About/SuezCanal/Pages/AboutSuezCanal.aspx) · 운하 분류 검토 |
| `40485117` | 아라카와강 | 도네강 (Tone) | 100.0% | [기관 원문](https://www.mlit.go.jp/common/001157851.pdf) |
| `41023100` | 라비강 | 인더스강 (Indus) | 60.5% | [기관 원문](https://www.fao.org/4/y5082e/y5082e05.htm) |
| `41279826` | 브라마푸트라강/얄룽창포강 | 살윈강 (Salween) | 96.3% | [기관 원문](https://www.fao.org/aquastat/en/countries-and-basins/transboundary-river-basins/salween/) |
| `50261309` | 마하캄강 | 바리토강 (Barito) | 92.6% | [기관 원문](https://sda.pu.go.id/balai/bwskalimantan3/berita/kunker-dprd-kotabaru-ke-balai-wilayah-sungai-kalimantan-iii) |
| `70576631` | 서스쿼해나강 | 델라웨어강 (Delaware) | 91.4% | [기관 원문](https://www.usgs.gov/centers/new-jersey-water-science-center/science/delaware-river-basin-study-unit-description) |
| `70816878` | 리오그란데강 | 브래저스강 (Brazos) | 76.5% | [기관 원문](https://www.usgs.gov/publications/reconnaissance-investigation-ground-water-resources-brazos-river-basin-texas) · 한국어 표기 추가 검수 |

- 위 표의 8개는 독립적인 Natural Earth 선형 비교와 기관 문헌 대조가 확보된 **교체·재분류 후보**다. 해당 교체에 영향을 받는 수계의 하구 및 본류 연속성과 한국어 표기 최종 승인은 별도로 판단한다.
- NE 대조에서 일치 후보가 없거나 두 강이 섞여 나타나는 수계는 확인 없이 이름을 새로 부여하지 않는다. 이전 승인 교정표도 보존한다.
- 자료에 포함된 한국어 이름이 OSM 계열인지 여부는 OSM bbox 매칭 자체로 판단하지 않는다. `sourceLabels`와 외부 검증 근거를 분리한다.

## 5개 수계 비OSM 교체 준비본 — 생산 디코더 검증 성공

- [`work/gis` 재생성 정책](https://github.com/kimjeon-il/Pando/blob/work/gis/tools/build-hydro-tiles.py)과 [독립 교체 표](https://github.com/kimjeon-il/Pando/blob/work/gis/tools/gis/hydro-independent-name-replacements.json)에 5개 ID(`20680587`, `40485117`, `41279826`, `50261309`, `70576631`)를 반영했다. 이 시스템들은 재생성 시 OSM 명칭·관계 메타데이터 조회를 건너뛰며, 검증된 별칭만 사용한다.
- 편집 중 지도 파일을 덮어쓰지 않는 [격리 재패키저](https://github.com/kimjeon-il/Pando/blob/work/gis/tools/gis/prepare_hydro_name_replacement_bundle.py)로 본류 데이터 102개 fragment의 이름·별칭·OSM 관계정보만 정정한 실험본을 작성했다.
- 검증: 5개 명칭 전부 기대값과 일치. 원본 지오메트리 샤드 3개 SHA-256 각각 동일, 공간 인덱스 SHA-256 동일, 총 16,548개 feature/902개 pack/3개 shard를 기존 생산 디코더로 정상 판독. `compressedBytes`와 컨테이너 바이트 수 일치. CI 성공.
- 실험본 Hydro 패키지 SHA-256: `c31cc298b2f99aec388f440253d5a2e4d9683736c1efa716201f453f199557be`. 원본 SHA-256: `91c2268c6dbfdfa7fc6103d8ad0b4eeca71f6c522df5c0118db69a3654ff532a`.
- [검사 증거 및 생성된 격리 패키지](https://github.com/kimjeon-il/Pando/actions/runs/40046580398/artifacts/12541228932) (일시적 GitHub Actions 보관). 실제 지도 데이터 저장소 최신 런타임 파일에 미게시, Pando `config/library-data.json` 수정 없음, Web/App 게시 없음.
- 원본은 73개 OSM 매칭 수계이며 격리본은 5개를 대체해 68개 매칭이 남는다. 실제 배포 패키지는 여전히 원본의 **73개**를 포함한다.

## 기존 승인 교정표 26개 원출처 확인

- [기존 26개 수계의 최초 승인 출처·독립 자료 목록](previous-26-reviewed-names.json)으로 기존 교정표의 26개 ID와 출처 URL을 전수 보존했다.
- 26개 중 24개에는 OSM 이외의 출처 URL이 포함돼 있다. 그 자료의 실제 내용·하천 선형을 본 조사에서 24개 모두 다시 검증했다는 뜻은 아니다.
- 원래 출처 열이 비었던 2개는 독일 연방수문청(BfG)의 [엘베강](https://undine.bafg.de/elbe/elbegebiet_en.html) 및 [오데르강](https://undine.bafg.de/oder/odergebiet.html) 안내에서 강의 독립 식별 근거를 보강했다.
- 기존 승인 교정표의 이름을 일괄 삭제·교체하지 않는다. 해당 26개 중 본 조사 73개와 중복 3개를 제외하면 별도 ID 23개다.

## 재검토해야 할 남은 분류

- Natural Earth 81표본 비교에서 26개는 최다 후보의 근접 비율이 75% 이상, 20개는 40~75% 미만, 9개는 40% 미만, **18개는 이름 붙은 NE 선분과 해당 허용범위에서 불일치**했다. 이는 소스 이름을 확정하는 검사가 아니다.
- 특히 기존 73개 목록 가운데 신규 5개를 제외한 **68개**는 비OSM 대체가 아직 완료되지 않았다. 원출처·별칭·본류 동일성을 일괄 정리하지 않고 개별 진행한다.
- `41023100` 인더스/라비, `70816878` 브래저스/리오그란데, `20773860` 수에즈 운하의 분류와 `20774342` 혼입 사례는 추가 검수 전 자동 승격 금지.

## 2026-10-24 후속 조사 최신본 — 22개 비OSM 메타데이터 교체 검증

> 이 절이 위 '5개 수계 교체 준비본' 및 해당 시점의 68개 잔여 수치를 갱신한다. 앞선 절은 당시 단계의 검증 이력으로 보존한다.

- 현재 `work/gis`의 [독립 출처 검토표](https://github.com/kimjeon-il/Pando/blob/work/gis/tools/gis/hydro-independent-name-replacements.json)는 **22개 수계**를 포함한다. 그중 대표명 오류 정정 **7개**, 대표명 유지·OSM 관계/별칭 제거 **15개**.
- **기준 73개 중 22개**의 메타데이터 교체 시험이 완료됐으며, 검증용 패키지에는 OSM 매칭 **51개**가 남는다. 실제 공개 원본 패키지는 여전히 **73개**를 포함한다.
- 2026-10-24 CI [검증 작업](https://github.com/kimjeon-il/Pando/actions/runs/40048314145)은 정상 완료했고, [임시 검증 패키지](https://github.com/kimjeon-il/Pando/actions/runs/40048314145/artifacts/12542780362)를 보관했다.
- 검증 내용: **551개 Hydro 형상 조각의 core 메타데이터 정정**; 원본 공간 인덱스 및 3개 geometry shard의 SHA-256 값이 변경 전후 완전 일치; 기존 생산 디코더로 전체 **16,548 feature / 902 pack / 3 shard** 판독 성공.
- 원본 번들 SHA-256 `91c2268c6dbfdfa7fc6103d8ad0b4eeca71f6c522df5c0118db69a3654ff532a`, 별도 검증 번들 SHA-256 `845a7b8d614ea8d6874f564085ba3396d025b44844d92dcb60d4444ce52e1bb9`. 모든 ID·형상 증명은 [고정 검사 결과](staged-22-proof.json)에 보존.

### 추가 6개 수계의 독립 출처 검증

| 수계 ID | 기존 → 검증본 이름 | 검증 내용 |
|---|---|---|
| `70816878` | 리오그란데강 → **브래저스강** | 텍사스 수자원개발위원회·USGS 공식 관측소 세 곳과 HydroRIVERS 본류 거리 0.143~0.371km 대조 |
| `70819626` | 리오그란데강 → **콜로라도강(텍사스)** | 텍사스 수자원개발위원회·USGS 공식 관측소 세 곳과 거리 0.061~0.199km 대조 |
| `40145639` | 시르다리야강 → 시르다리야강 | UNECE·세계은행의 유역 자료, Natural Earth 본류 일치; 나린강 지류 정보 유지 |
| `40351117` | 압록강 → 압록강 | 한국 통일부 북한지도와 중국 지린성 지방지, NE 본류 일치; 훈강 지류 정보 유지 |
| `41392598` | 메콩강 → 메콩강 | 메콩강위원회 공식 본류·지류 목록 및 한국 KSP, NE 본류 일치 |
| `70842751` | 리오그란데강 → 리오그란데강 | 미·멕 국제국경수자원위원회·텍사스 수자원개발위원회 및 NE 본류 일치; 리오콘초 지류 유지 |

- [USGS 관측소 6개와 해당 수계의 실제 본류 거리 검사](usgs-gauges-crosscheck.json)를 영구 보관했다. 각 세 곳 모두 실제 강의 선형에서 400m 미만이며 다른 후보 강 본류 관측소로부터는 최소 40km 이상 떨어진다.
- 출처 웹문헌: [UNECE 카자흐스탄 수계](https://unece.org/environment-policy/water/areas-work-convention_protocol/country-dialogues/kazakhstan), [세계은행 시르다리야 유역](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/663361468283187700), [통일부 압록강](https://nkinfo.unikorea.go.kr/nkp/search/search.do?query=%EC%95%95%EB%A1%9D%EA%B0%95), [지린성 훈강](https://dfz.jl.gov.cn/zsjl/201809/t20180929_5216605.html), [메콩강위원회](https://www.mrcmekong.org/geography/), [국제국경수자원위원회](https://www.ibwc.gov/treaties/).

### 아직 미확정인 대표명·분류

- `41023100` 라비강 명칭: 독립 NE 강선은 인더스강 60.5%, 첸나브강 17.3%, 라비강 8.6%로 본류 경로에 혼재. 임의로 인더스강으로 승격하지 않는다.
- `20265844` 드르벵차강: 실제 본류 비교에는 비스와강 51.9%와 서부크강 40.7%가 나타나 혼재. 정부 수계 자료와 하구·본류 연속성 검증 전 교체 보류.
- `41337891` 빠삭강: 독립 지도에서 욤강과 차오프라야강 구간이 혼재한다. 강 단위 명명 경계를 재구성할 필요가 있다.
- `20773860`/`20774342`: 수에즈운하는 인공 수로이므로 단순히 이름 끝의 '강'만 바꾸지 않고 수로 객체 분류 가능 여부를 먼저 조사한다.
- `70814357`: 미시시피강의 관계 데이터에 리오그란데강 별칭이 섞인 것으로 확인됐다. 광대한 지류 명칭은 개별 확인한 뒤 제거·보존을 결정한다.

### 실제 반영

- 데이터 저장소 `assets/data/hydro/v0.13.2/`와 Pando `config/library-data.json`은 **수정하지 않았다**. 검증 번들은 임시 Actions artifact 및 검증 해시로만 존재한다. 웹·앱 재배포와 `main` 병합도 수행하지 않았다.
- 런타임 OSM 의존성 0개가 되기 전까지 지도 왼쪽 아래의 `© OpenStreetMap contributors` 링크는 보존한다.

## 최신 검증: 33개 시스템 (2026-10-24 후속)

> 기존 위쪽의 5개·22개별 절은 작성 당시의 연구 단계 기록이며, **이 절이 최신 잠정 검증 상태**다. 실제 공개 지도와 저장소의 기존 hydro 원본은 수정하지 않았다.

- `work/gis` 커밋 [`f701ff4`](https://github.com/kimjeon-il/Pando/commit/f701ff4bb2263c1cc0dcabd79317e14a69322f2c)의 [독립 이름·출처 장부](https://github.com/kimjeon-il/Pando/blob/work/gis/tools/gis/hydro-independent-name-replacements.json)에 33개 시스템을 명시했다. 원래 대표명 오류 정정 7개, 대표명 보존·OSM 관계 및 별칭 정보 교체 26개다.
- GitHub Actions [GIS OSM river name dependency inventory — 성공](https://github.com/kimjeon-il/Pando/actions/runs/40049580223)에서 최신 33개 대상 격리 패키지 생성, 독립 Natural Earth 81표본 비교와 USGS 공식 관측소 검증, 추가 합류점 관계 대조, 원본 생산용 디코더 전체 검증을 통과했다.
- 원래 HydroRIVERS **16,548개 feature**, **902개 pack**, **3개 shard** 전체 판독에 성공. 메타데이터가 바뀐 구성 feature는 **1,270개**. 공간 인덱스와 지오메트리 shard 3개의 SHA-256은 각각 변경 전후 동일하다.
- 최신 별도 격리 패키지 SHA-256: `f366eae11bb2b0be80c2419cb3b710925fac78eeec83a80ee7b4cc26b7c28e5a`. 원본 공개 데이터 SHA-256: `91c2268c6dbfdfa7fc6103d8ad0b4eeca71f6c522df5c0118db69a3654ff532a`.
- [검증 증거(영구 JSON)](staged-33-proof.json) · [생성된 패키지(GitHub Actions 임시 보관)](https://github.com/kimjeon-il/Pando/actions/runs/40049580223/artifacts/12541894380) · [73개 수계별 갱신 상태](inventory.json)
- **검증용 파생본에는 33/73개 대체 완료, 미완료 40개**. 실제 지도 런타임 원본은 OSM 매칭 73개 그대로이고 화면의 OSM 저작자 표시도 유지해야 한다.

### 이번 차수의 신규 11개 시스템

| system ID | 현재명 / 교체본 대표명 | 비OSM 근거·특기사항 |
|---|---|---|
| `20336821` | 템스강 | [영국 환경청 수계 관리계획](https://www.gov.uk/guidance/thames-river-basin-district-river-basin-management-plan-updated-2022), NE Thames 본류 근접 72.8% |
| `20452421` | 돈강 | [러시아 연방수자원청](https://voda.gov.ru/press-tsenter/news/federalnye/559696/), NE Don 본류 81.5% |
| `20588291` | 도루강 | [포르투갈 환경청](https://cnpgb.apambiente.pt/content/r%C3%A9gua)·[스페인 도루 수계관리기구](https://mirame.chduero.es/chduero/public/naturalElements/river), NE Douro 74.1% |
| `41225082` | 람강 | [베트남 수자원관리기관](https://mae.gov.vn/quan-ly-dieu-phoi-lien-vung-luu-vuc-song-ca-21850.htm), NE Cả 85.2%, Sông Lam 동일 명칭 |
| `50170097` | 마하캄강 | [인도네시아 공공사업부](https://sda.pu.go.id/balai/bwskalimantan4/page/4), NE Mahakam 79.0% |
| `40190238` | 아무다리야강 | [세계은행 Amu Darya 유역 자료](https://www.worldbank.org/en/news/press-release/2026/07/21/world-bank-support-improves-central-asia-water-management-and-conservation), 판지강을 지류로 분리, NE Amu Darya 71.6% |
| `40613666` | 장강 | [중국 수리부 자료](https://slj.cq.gov.cn/zwgk_250/zfxxgkml/jczwgk/sxgcgl/sxgcyxaqgl/202204/t20220402_10585421.html), 잘못 섞인 메콩강 관계·별칭 제거, NE Yangtze 72.8% |
| `20081953` | 북드비나강 | [러시아 정부 수로 목록](https://www.consultant.ru/document/cons_doc_LAW_40441/526e96dcf757c61b65432d68902b24c3b6a25b51/), NE Northern Dvina 49.4% / Vychegda 44.4%, 합류점 관계 보존 |
| `20446779` | 루아르강 | [프랑스 정부 루아르·비엔강 합류점 지정](https://www.prefectures-regions.gouv.fr/pays-de-la-loire/DOCUMENTS-PUBLICATIONS/Environnement-Classement-de-la-confluence-de-la-Loire-et-de-la-Vienne), 잘못 들어간 센강 별칭 제거, NE Loire 40.7% / Vienne 64.2% |
| `20498112` | 도나우강 | [ICPDR 수계·지류 명단](https://www.icpdr.org/danube-basin/danube-river-basin), NE Danube 58.0% / Sava 28.4%; 주요 지류명 독립 검증 |
| `70617856` | 새크라멘토강 | [미국 USGS 센트럴밸리](https://www.usgs.gov/centers/california-water-science-center/central-valley-regional-overview)·[캘리포니아 DWR 페더강](https://water.ca.gov/Programs/Integrated-Science-and-Engineering/Feather-River-Program), 샌와킨강은 별개 수계로 분리, NE Sacramento 58.0% / Pit 38.3% |

### 남은 40개 검토 범위

- [40개 전수 후속 작업 장부](remaining-40-priority.json). NE 단순 이름 대조에 대응 후보가 없는 **17개**, 본류·지류·별칭 충돌 우려가 큰 **17개**, 명칭 범위의 문헌 보강이 필요한 **6개**로 분류했다. 이 분류는 조사 우선순위이며 잘못된 명칭의 최종 확정 수가 아니다.
- 주요 미확정: `20265844` 드르벵차/비스와/서부크강 구분(폴란드 [Wody Polskie](https://www.gov.pl/web/wody-polskie/komunikaty-nawigacyjne) 공식 노선 확인), `41023100` 라비/인더스/첸나브강, `41182380` 꺼우/홍강, `41337891` 빠삭/욤강, `70814357` 미시시피/리오그란데강 별칭 혼입([미국 USGS 별개 유역 분류](https://pubs.usgs.gov/publication/dds49118)), 수에즈운하 2개 ID의 객체 형식 문제.
- 이 40개는 단일 출처나 OSM bbox만으로 자동 명명·승격하지 않는다. 각국 정부 벡터/기준 관측소, 본류·지류 경로, 독립 지명 자료를 결합해 판단한다.

### 게시 여부

이 차수에서도 **`assets/data/hydro/v0.13.2/`, 실제 웹·앱 런타임 및 OSM 지도 출처 링크를 수정하지 않았다**. 변경은 Pando `work/gis` 연구 코드·분리된 검증용 번들과 데이터 저장소의 조사 보고서에 한정된다.

## 최신 진행 — 42개 교체 검증 · 31개 미완료 (2026-10-24)

- `work/gis` 커밋 [`112ebcd`](https://github.com/kimjeon-il/Pando/commit/112ebcd67402945b106f3ab6d5c91630e144363e)에서 **42/73개 수계**의 OSM 이름·관계 의존성을 **격리 검증용 메타데이터**로 교체했다. 대표명 정정 **8개**, 대표명 유지·출처/별칭 정리 **34개**. 실제 웹/앱 배포 및 원본 수계 자산 변경 **0개**.
- [GitHub Actions 42개 교체 검증](https://github.com/kimjeon-il/Pando/actions/runs/40053686547) **성공**: 메타데이터 수정 구성 구간 **1,895개**, 원래 16,548개 전체 형상·902 pack·3 geometry shard 재판독 통과, 압축된 공간 인덱스 및 원본 지오메트리 3개 SHA-256 각각 동일. 격리 번들 SHA-256 `d158d4323a10dc349c060647534778b70fb244543d3a843275389a898daacf9f`. [영구 검증 증거](staged-42-proof.json) · [임시 교체 패키지](https://github.com/kimjeon-il/Pando/actions/runs/40053686547/artifacts/12544785894).
- `50798885` **야라강**: 빅토리아주 정부 [Yarra River/Birrarung 공식 수계 GIS 선형](https://spatial.planning.vic.gov.au/server/rest/services/yarra_river_land/MapServer/0)과 기존 Hydro 중심선 161개 표본 상호 비교 결과, 양방향 **1km 이내 98.76%**, Hydro 기준 거리 90백분위 **0.338km**. [공식 메타데이터 CC BY 4.0](https://discover.data.vic.gov.au/en_AU/dataset/vicmap-hydro-watercourse-line) 및 [멜버른 수자원기관 설명](https://www.melbournewater.com.au/water-and-environment/water-management/rivers-and-creeks/yarra-river). [정부 지리정보 원천 해시·검증 기록](yarra-government-vector-crosscheck.json). **정부 선형을 복사해 배포하지 않았음**.
- `20597827` **마리차강**: [불가리아 동에게해 수계관리국](https://earbd.bg/indexdetails.php?menu_id=226)·[그리스 에브로스 지방정부](https://www.pamth.gov.gr/en/anaklisi-tis-apagoreysis-alieias-ston-potamo-evro-stoys-parapotamoys-toy-sta-kanalia-kai-stoys-loipoys-ydatinoys-schimatismoys-2/) 자료로 국경을 넘는 Maritsa/Evros 수계와 Tundzha 지류 관계를 확인. NE 본류 표본 일치율 37%이므로 **두 국가 기관의 독립 지명 설명을 교차검증**하여 대표명 유지. 향후 더 정확한 선형 원출처 조사 필요.
- [남은 31개 전수 조사 대기열](remaining-31-priority.json): Natural Earth 독립 명칭 선형 없음 16개, 본류·지류·객체 유형 충돌 우려 13개, 명칭 범위 자료 미비 2개. 우선순위: [젬/엠바강과 우랄강 혼동](emba-ural-identity-review.md), 핀란드 오울루강 2개 OGC 공식 수로 선형 대조, 일본 아라카와강/도네강 원천 경로 분리, 수에즈운하의 객체 유형 검토.
- 모든 기존 HydroRIVERS 지오메트리·국가 경계·OSM 저작권 링크·지도 사용 데이터·웹/앱 빌드는 수정하지 않았다. 이 단계는 **검증용 대체 소스 준비**에 한정된다.

## 후속 재조사 — 독립 지점과 원본 중심선 직접 대조 5개 (2026-10-24)

> 최신 검증용 비OSM 교체 패키지는 여전히 **42/73개**이며, 원본 지도 반영 **0개**다. 아래는 이전에 남겨둔 31개 중 **5개**에 대한 새로운 *식별 대조*다. 5개가 추가 교체 승인을 받았다는 뜻은 아니다.

- [GitHub Actions 독립 지점 공간 대조 성공](https://github.com/kimjeon-il/Pando/actions/runs/40055173588): 배포용 HydroRIVERS v0.13.2의 16,548개 feature / 902 pack / 3 geometry shard를 기존 생산 디코더로 판독, 5개 논리 수계의 실제 mainstem과 독립 발표 지명 좌표를 로컬 UTM 투영 좌표계에서 비교했다. [계산 재현 스크립트](https://github.com/kimjeon-il/Pando/blob/work/gis/tools/gis/verify_independent_river_point_anchors.py) · [수치·기초문헌 영구 증거](independent-river-point-crosscheck.json).
- 기존 OSM 관계 연결 방식은 외접 범위 중첩 매칭이므로, 서로 다른 강이 같은 이름과 별칭을 받을 위험이 이번 검사에서 구체화됐다.

| System ID | 기존 대표명 | 유력한 독립 식별 | Hydro 중심선과 독립 지점 간 거리 (km) | 판정 |
| --- | --- | --- | --- | --- |
| `20071308` | 오울루강 | Oulujoki | 오울루강 1.964 / 시카강 37.737 | 기존명 대체로 부합하나 본류 약 416.3km로 공식 오울루강 107km보다 훨씬 길어 상류 범위 분리 필요 |
| `20075401` | 오울루강 | **Siikajoki** | 시카강 0.396 / 오울루강 38.998 | **기존명 혼입 유력**. 핀란드 국가 지명등록부의 공식 지점과 기존 Hydro 일치 |
| `20456598` | 우랄강 | **Zhem/Emba** | 젬강 0.207 / 우랄강 308.332 | **기존명 혼입 유력**. 독립 지리 문헌의 지점과 기존 Hydro 일치. 공식 정부 벡터 재검증 필요 |
| `20532766` | 테레크강 | Terek | 테레크 하구 1.366 / 술라크 조사점 35.210~38.108 | 기존명 지지. 실제 본류 확인은 별도 |
| `20540915` | 테레크강 | **Sulak** | 술라크 현장 관측점 두 곳 0.030, 0.084 / 테레크 하구 34.557 | **기존명 혼입 유력**. 러시아 공식 수로 지정과 독립 현장 2개 지점으로 교차검증 |

### 독립 출처와 검증 한계

- 핀란드: [국토조사국 지명등록부 Oulujoki](https://finto.fi/yso-paikat/fi/page/p204727) · [Siikajoki](https://finto.fi/yso-paikat/en/page/p139542). [핀란드 환경정보기관 오울루강(107km)](https://www.vesi.fi/tra_arviointi/tulvariskien-alustava-arviointi-oulujoen-vesistoalueella/)과 [시카강(약 194km)](https://www.vesi.fi/tra_arviointi/tulvariskien-alustava-arviointi-siikajoen-vesistoalueella/)은 별개의 강이다. 실제 이름 있는 공식 수로 선형을 [국토조사국 OGC API](https://avoin-paikkatieto.maanmittauslaitos.fi/inspire-hydrography/features/v1/)에서 확보해 전 구간 재검토할 것.
- 카자흐스탄: [무갈자르 지방정부](https://www.gov.kz/org/aktobe-mugalzhar/press/article/details/25185?directionId=8907&lang=ru)는 젬/엠바강의 발원지를 독립적으로 명시한다. 비교에 쓴 **좌표**는 [카자흐스탄 지리 문헌 2차 전사](https://silkadv.com/ru/node/4653)와 [우랄강 전문서적 2차 전사](https://silkadv.com/en/content/ural-river-kazakhstan) 자료이며, 공식 정부 GIS가 아니다. 따라서 명칭을 즉시 변경하지 않는다.
- 러시아: [연방수자원청](https://voda.gov.ru/favr/structure/bvu/department/subject/6885)은 테레크/술라크를 별도 하천으로 관리한다. [독립 2024년 현장 관측 연구](https://www.mdpi.com/2073-4441/17/23/3390)는 술라크 2개 지점의 위치를 측정했고, [정부 제1543-р호 명령](https://base.garant.ru/407033236/)은 술라크강 합류점(42.7923N, 46.7951E)과 치르케이 댐·미아틀리 댐·바브투가이 등 지점의 공식 좌표를 별도로 명시한다. 이것들은 표본 지점이지 전체 벡터는 아니다.
- 공통 한계: 개별 지점의 하천 선형 근접성만으로 하천 **전체** 동일성, 상류의 다른 이름, 지류 포함 여부, 라이선스 및 한국어 표기까지 확정할 수 없다. 지도 이름·형상·원본 OSM relation 정보·OSM 저작권 링크는 계속 유지한다. 남은 31개 중 5개에만 구체적인 강 식별 단서를 추가했으며, 미완료 31개라는 검증상 숫자는 바뀌지 않았다.

## 데이터 반영 — 코드·자료 저장 완료 (2026-10-24)

> 이 절이 위의 과거 검증용 패키지·미반영 기록을 대체하는 **최신 데이터·웹 게시 상태**다.

- **실제 HydroRIVERS v0.13.2 메타데이터 42개 수계 반영 완료**, 대표명 정정 8개, 기존 대표명 유지·별칭·지류·출처 정리 34개. 1,895개 feature 조각에 각각의 비OSM 증거 URL 등록.
- 자료 저장소의 불변 원본 커밋 [`36210d5`](https://github.com/kimjeon-il/PandoLab-library-data/commit/36210d5fde7d4d2301d0ff1335cf728e23b24195), 원본 `hydro.bin`과 동위 `manifest.json`의 SHA 검증 통과. 새 bundle SHA-256 `aee3368aa05543050fb4455265d2192c2322d2a0506c88f9f9a61f1f1158daf4`.
- 코드 저장소 `main` 새 자료 pin [`15046c8`](https://github.com/kimjeon-il/Pando/commit/15046c820c393e9822b9e148d972291d101822f1). [42개 메타데이터 전수 검증 성공](https://github.com/kimjeon-il/Pando/actions/runs/40055943255), [Hydro 현재 런타임 계약 검사](https://github.com/kimjeon-il/Pando/actions/runs/40056841310) 성공.
- 국경선·하천 실제 좌표·압축 인덱스·세 기하 shard 원본 해시를 유지했다. 미교체 OSM 31개는 해당 원본 이름·관계정보 및 ODbL 표시를 보존한다. 오른쪽 개별 객체 비고에는 검증된 42개에 대해 공식 출처 URL이 나온다.
- 독립 발표 지점과의 거리 검사에 따라 Siikajoki `20075401`, Zhem/Emba `20456598`, Sulak `20540915` 등은 오명명 유력 **후속 확인 대상**이며 **이번 8개 확정 정정에 포함되지 않는다**. 검증 전에는 기존 이름을 변경하지 않는다.
- 웹 Pages 재게시: [게시 작업](https://github.com/kimjeon-il/Pando/actions/runs/40057033282)에서 **빌드·배포 모두 성공**. GitHub Actions 기준 확인. 외부 HTTP 개별 파일 응답은 별도 검증하지 못했음. [최종 게시 증빙](published-42-proof.json).

[원본 별도 조사표](remaining-31-priority.json) · [현재 73개 원천 판정](inventory.json) · [5개 중심선 거리 검증](independent-river-point-crosscheck.json)

## 2026-10-24 잔여 31개 재조사 · 1차 10개 완료

- [1~10번 상세 조사보고서](batch01-ten-research-2026-10-24.md) · [10개 수계 / 99개 독립 지점 거리 대조 원자료](batch01-ten-named-point-screen.json) · [GitHub Actions 성공](https://github.com/kimjeon-il/Pando/actions/runs/40058061900)
- 독립된 정부 수문·현장 관측 좌표를 HydroRIVERS v0.13.2 공개 원본의 중심선과 대조했다. **10개 조사 완료**이나 OSM 완전 대체용 공식 중심선·구간별 검증이 남아 있어 **추가 승인 0개**, 실제 지도 수정 **0개**.
- **대표명 변경 유력**: `20561290` 리오니→엔구리(2022 조지아 NEA 엔구리강 조사 지점 0.001·0.126·0.213·0.623km), `20540915` 테레크→술라크, `20075401` 오울루→시카, `20456598` 우랄→젬·엠바. 나머지는 기존 이름 유지 또는 혼입/정체 미확정. 구체적 판정은 위 상세 보고서에 기록.
- **반대 검증**: `20565620`은 2017년 NVE·조지아 NEA의 Rioni 하류 관측지점까지 0.276~0.861km이며 Kvirila 지류 지점과도 근접한다. 기존 **리오니강**을 유지하되 지류 구간 구분이 필요하다.
- 핀란드 NLS 공인 수로 벡터 서비스는 온라인 조회가 `URLError`로 실패해 전 구간 형상 검증을 하지 못했다. 출처 부재로 오해하면 안 된다.
- 현재 상태는 여전히 **42/73개 실제 반영, 31개 미교체**. 지형·수계 형상·기존 OSM 저작권 링크는 변경하지 않았다. 다음 묶음은 [잔여 조사표](remaining-31-priority.json)의 11~20번이다.

## 2026-10-24 잔여 31개 재조사 · 2차 10개 완료

- [11~20번 상세 조사·판정표](batch02-ten-research-2026-10-24.md) · [10개 수계/90회 공간 대조 원자료](batch02-ten-named-point-screen.json) · [NGA 공식 한반도 하천 4개 UFI 기록](batch02-nga-government-names.json) · [성공한 원본 Hydro 디코딩·공간 검증](https://github.com/kimjeon-il/Pando/actions/runs/40060444582).
- **오명명 의심 최우선**: `20628098` 아무다리야→**무르가브강** (관측소 7m·89m, 진짜 아무다리야 Kerki 약 257km), `40188382` 시르다리야→**추강(Chu)** (추강 11m, 촌케민강 191m). 실측 검증 원본: 체크섬 확인한 [CA-discharge 2023](https://zenodo.org/records/7743778).
- **강/운하 객체 분류 오류**: `20773860`은 수에즈 항행운하 지점까지 0.407km이며 원본 NE Suez Canal 선형과 85.2% 부분 매칭이나 **인공 항행운하**이므로 하천명만 수정하면 안 된다. `20774342`는 같은 항행 운하라는 근거가 부족해 정체를 계속 조사한다.
- **같은 논리 수계에 다른 이름의 구간이 혼합**: `30145067` 오비강/이르티시강, `40423228` 남한강/한강. 북한 `40364680`, `40391614`, `40414035`, `40415850`은 NGA 독립 공식 지명을 확인했지만 명칭 위치 좌표만으로 수계 전체가 검증된 것은 아니다.
- 2차 **10개 전부 개별 조사 완료**, 앞선 1차 10개 포함 **20개 조사 완료**. 정식 신규 OSM-free 교체 승인 **0개**, 실제 배포 **42개**, OSM 미교체 **31개** 및 기존 저작권 표기는 유지. 다음은 [잔여 조사표](remaining-31-priority.json) **21~30번 10개**.

## 최종 31/31개 독립 조사 완료 — 3차 마지막 11개 (2026-10-24)

- [21~31번 마지막 11개 상세 조사](batch03-last11-research-2026-10-24.md) · [431회 독립 정부 지명점/원본 중심선 거리 원자료](batch03-last11-named-point-screen.json) · [GitHub Actions 공간검증 성공](https://github.com/kimjeon-il/Pando/actions/runs/40061608741).
- 미국 NGA 지정하천(`STM`) 지명정보 13회 조회, 11개 Hydro 논리 수계 중심선 대조 완료. 미명명 2개 지역에서는 동나이강 계통과 밤꼬강 동·서 두 지류가 뚜렷한 후보. 광역 목록 요청은 각각 300개 상한이어서 **지역 내 개별 하천 지명 전수 완료가 아님**.
- 대표명 오배정 **강력 의심**: `41023100` 라비강이 인더스/판즈나드/첸나브 경로와 혼합, `41109275` 난판강에 좌강/우강/욱강/심강/서강 경로 혼합, `41182380` 꺼우강 경로가 독립 홍강 계통에 가까움, `41337891` 빠삭강에 욤·핑·난강 경로 포함, `41390476` 발라이강의 2017 베트남 정부 공식 시작·종점은 실제 Hydro 중심선에서 각각 15.200km/27.159km 떨어짐.
- 기존명 **유지 지지**: `40475481` 금강 (NGA Kum-gang 0km), `40486439` 아라카와강 (NGA Arakawa 0.444km, 도네강 최근접 약 20.995km), `41171836` 룩남강 (일부 구간 0.347km; 트엉·꺼우와 합류 구간 주의), `41067217` 브라마푸트라 계통 (하류 자무나·파드마 구간 분리 필요).
- **전체 31개 수계는 1차 10개 + 2차 10개 + 3차 11개로 개별 자료조사 완료**. 그러나 독립 하천 전체 명칭 선형·지류·이용조건을 충족하지 않아 **정식 신규 OSM 출처 교체 승인 0개**, 이미 배포한 42개 외 **31개는 계속 OSM 명칭/관계자료에 의존**함. OSM 저작권 표시 삭제 금지.
- 더 이상의 단순 출처 웹조사보다 **독립 정부 명명 벡터 확보, 국가별 관측점 최소 복수 교차검증, 실제 mainstem 구간 분할, 격리 1:1 소스 대체 검사**가 다음 단계. 여기서 데이터를 적용하지 않았으며 원래 지도 형상·핀·웹·앱·출처 UI는 그대로다.

### 31개 전체 연구 산출물

[1차 10개](batch01-ten-research-2026-10-24.md) · [2차 10개](batch02-ten-research-2026-10-24.md) · [3차 11개](batch03-last11-research-2026-10-24.md) · [전수 판정 현황](remaining-31-priority.json). **조사 완료와 OSM 교체 완료는 별도 상태**로 관리한다.

## 보관된 native 전환 평가 근거 — point

[원자료·선택 평가 결과·독립 oracle 생성 근거](native-point-screen-20261102/)를 보관한다. 이는 당시 구현의 비교 근거이며 현행 전체 자료의 재검증을 뜻하지 않는다. 유지되는 정본 fixture와 검사에 없는 옛 실행 API나 Python 환경을 복원하지 않는다. 큰 원문은 부품 순서·각 부품과 전체의 SHA-256이 적힌 parts.json을 기준으로 원래 바이트로 복원한다.
