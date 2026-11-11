# GEO-LIFE-031 — 북아메리카 국가 존속기간 1차: 벨리즈·자메이카·파나마 (2026-11-12)

> 관리 ID: `GEO-LIFE-031` · 상태: `investigating / phase-1 / source-crosschecked / not-applied`  
> 조사 범위: **1801-01-01~2026-11-12** · 지역: **북아메리카(중앙아메리카 및 카리브 포함)** · 직전 지역: 아프리카(GEO-LIFE-030) · 다음 지역: **남아메리카**  
> 정본 국가 lifetime·역사 폴리곤·타임라인·코드·배포 **변경 0건**. 날짜는 '이미 있는 기간 값에 대한 1차 문헌 검토'이며 새로운 기간값 적용 승인이 아니다.

## 1. 기준·중복 점검·기존 국가 객체

- `kimjeon-il/Pando` `work/gis` HEAD **`e191ed6a6fce97a6f683540491d3e2c81618a0ab`** (최근 커밋 'Align frontend fixture with current terrain catalog [skip ci]', 2026-11-11 14:27:38 UTC). `AGENTS.md` 및 `docs/branch-policy.md`를 읽어 보고서 정본이 코드 저장소에서 `kimjeon-il/PandoLab-library-data/main/reports/borders/history/lifetimes/`로 이전되었음을 확인. 현재 코드 저장소의 레거시 `reports/README.md`·`reports/geography/` 경로는 없음. 이 회차에서 `Pando/work/gis`를 수정하지 않는다.
- `work/gis/config/library-data.json`의 라이브러리 고정 리비전은 **`921d86aa3c03ffa0b3d5879ad30c9914c4d1b31a`**. 동일 리비전의 `assets/data/territorial-entities/generated/v2/index.json`을 GitHub 원격에서 읽어 **288개 entities를 JSON 파싱**했다.
- 기존 국가 원장: `state:BLZ` `validFrom=1981-09-21`; `state:JAM` `validFrom=1962-08-06`; `state:PAN` `validFrom=1903-11-03`. 모두 `validTo=null`, `entityKind=general`, `parentEntityId=""`, `instantiation.mode=independent`로 나타남. 모두 Natural Earth 5.1.1 현행 형상 1종을 참조하므로 **그 형상은 독립 당시 역사 국경 검증 증거가 아니다**. 국가 3개의 현재 시작일은 이번 독립 근거와 일치한다.
- 선행 근거 `GEO-023` (`verified-entity-lifetimes.md`)에서 BLZ/JAM/PAN 시작일 3건이 이미 기록·적용됐음을 확인. 해당 독립일을 **새 발견 또는 새 입력 3건으로 중복 집계하지 않음**. `GEO-LIFE-001`(A–D), 007(MEX/GTM/HND/NIC), 013(SLV/USA), 019(중앙아메리카 연방/텍사스/유카탄), 025(서플로리다/남부연합/1921 중미연방)의 1차 대상과 겹치지 않는 **국가별 문헌 1차 상세 검토 3개**를 실시함.
- 횡단국 러시아·튀르키예·조지아는 유럽 고정, 남극 등 비주권 지리 객체는 조사 집계에서 제외. 이 회차의 1801년 이전 건국·왕조·국경 변천은 조사하지 않음.

## 2. 벨리즈 — Belize (`state:BLZ`)

| 날짜 | 확인된 사건 | 법적 성립·동일성 판정 |
| --- | --- | --- |
| **1973년 6월** | 식민지 `British Honduras`가 `Belize`로 개칭(미 국무부 역사국). | **독립 전 명칭 변경**이며 1973년을 독립국 설립일로 기록 금지. 이 자료에서는 정확한 일 단위의 법령 효력일 확인 유보. |
| **1981-07-31** | 영국 `Belize Independence Order 1981` (SI 1981/1107) 제정. | 법령 제정일. 독립 효력일과 별도. |
| **1981-09-21** | 해당 명령 제1조 제2항에 명시된 일반 시행일과 Independence Day; 벨리즈 고등판무관실도 완전 독립일로 설명. | **영국으로부터 주권국 독립**의 직접 효력일. `state:BLZ` 현재 시작일과 일치. |
| **1981-09-25** | 유엔 총회 결의 A/RES/36/3에 따라 회원국 가입. | 국제기구 가입일이지 독립 효력일 아님. |
| **1981-10-29** | 미국의 공식 승인 및 수교·대사관 설치(미 국무부). | 타국 승인일이지 건국일 아님. |

**독립 출처와 확인 한계**

1. **영국 원법령:** [Belize Independence Order 1981, SI 1981/1107](https://www.legislation.gov.uk/uksi/1981/1107/pdfs/uksi_19811107_en.pdf), 제1조 시행일 1981-09-21(원본 PDF 검색 텍스트·색인 확인; PDF 전 페이지 시각 판독 **미실행**). [Belize Act 1981](https://www.legislation.gov.uk/ukpga/1981/52/contents) 법률 목차 및 관련 조문 검색. 제정일·효력일 구별.
2. **벨리즈 외교당국:** [Belize High Commission, About Belize](https://belizehighcommission.co.uk/about-belize/) — 1964 자치, 1973 개칭, 1981-09-21 독립을 별도로 기술. 영국 법령 작성 기관과 독립된 벨리즈 공식 설명.
3. **유엔:** [36차 총회 결의 색인, A/RES/36/3](https://research.un.org/en/docs/ga/quick/regular/36) — 1981-09-25 가입. **미국 국무부 역사국:** [Belize](https://history.state.gov/countries/belize) — 1981-10-29 승인과 독립일 구별. 이 자료들이 동일 영국 법령을 설명한 대목은 '독립된 원법령' 수로 중복 계산하지 않음.

**2차 보류:** 명령·헌법 원본의 상세 부칙과 발효 경과, 과테말라 영토 주장·국제법적 경계와 벨리즈 국가성의 관계. 영토 다툼을 이유로 1981 독립 효력을 부정하거나 현행 지도 국경을 1981 국경으로 소급 금지.

## 3. 자메이카 — Jamaica (`state:JAM`)

| 날짜 | 확인된 사건 | 법적 성립·동일성 판정 |
| --- | --- | --- |
| **1962-07-19** | 영국 `Jamaica Independence Act 1962` (1962 c.40) 국왕 재가. | 법률 제정일이지 국가 주권 독립 효력일 아님. |
| **1962-08-06** | 동 법 **제1조**의 독립 효력 개시; 자메이카 국가도 1962년 헌법 효력을 독립일로 설명. | **주권국 출범**, `state:JAM` 시작일과 일치. 영연방 내 군주국 지위 자체는 식민지 지위가 아님. |
| **1962-08-16** | 미국의 공식 승인·대사관 설치. | 국제 승인 시점으로, 8월 6일 독립 효력을 대체하지 않음. |

**독립 출처와 확인 한계**

1. **영국 원법령:** [Jamaica Independence Act 1962 — as enacted](https://www.legislation.gov.uk/ukpga/Eliz2/10-11/40/enacted) 제1조 (1962-08-06 법적 효력), 제4조(독립 당시 `Jamaica` 범위: Morant Cays·Pedro Cays는 포함, Cayman Islands·Turks and Caicos Islands 제외). 법령 검색 색인에서 조문 확인; 사이트 원문 직접 열람은 XHTML 콘텐츠 오류로 **미완료**.
2. **자메이카 국립도서관:** [Jamaica Independence, 1962](https://nlj.gov.jm/jamaicaindependence1962/) — 1962-08-06 독립·헌법 효력·의식 기록(본문 열람). 영국 법령과 다른 자국 기관의 독립 서술.
3. **미 국무부 역사국:** [Jamaica](https://history.state.gov/countries/jamaica) — 독립일 1962-08-06, 승인일 08-16. [1962-07-19 러스크 장관 문서](https://history.state.gov/historicaldocuments/frus1961-63v10-12mSupp/d175)는 예정 독립일을 보여주는 **당시 문서**(미래 예정과 법률 효력 사실은 구별).

**2차 보류:** 당시 영국 의회 법률·Jamaica (Constitution) Order 원문 전체 대조, 1958~1962 서인도제도연방 관계의 법적 효과, 독립 당시 부속 도서 및 종속 영토의 국가 객체 처리. 1962 후 정부 변화는 신규 건국으로 취급하지 않음.

## 4. 파나마 — Panamá (`state:PAN`)

| 날짜 | 확인된 사건 | 법적 성립·동일성 판정 |
| --- | --- | --- |
| **1903-11-03** | 콜롬비아로부터 분리·독립 공화국 선포, 임시정부 구성. 11월 4일 파나마 임시정부의 당대 대외전보가 전날 독립 선언을 명시. 파나마 국회도 같은 날짜를 확인. | **국가 분리 성립일**의 강한 근거; `state:PAN` 시작일과 일치. 분리 선언·실효 지배·외국 승인 구별. |
| **1903-11-06** | 미국의 독립 공화국 승인 및 임시정부와 관계 개시(미 국무부 역사국). | 타국 승인일은 최초 국가 성립일과 구별. |
| **1903-11-13** | 미국이 파나마 특사 신임장을 수리하여 정식 외교관계 수립. | 외교관계 수립일 ≠ 성립일. |
| **1977-09-07 / 1979-10-01 / 1999-12-31** | 파나마운하 조약 서명 / 운하지대 별도 관할 종료 / 운하 운영권 완전 이관. | 영토·관할·운영권 변화와 **파나마 국가 자체의 존속**은 구별. 1979·1999를 재독립 건국일로 덮어쓰지 않음. |

**독립 출처와 확인 한계**

1. **파나마 국회 공식 역사 설명:** [Asamblea Nacional, 1903-11-03 독립](https://www.asamblea.gob.pa/Noticias/Actualidad/PANAMA-PROCLAMA-SU-INDEPENDENCIA-EL-3-DE-NOVIEMBRE-DE-1903), 2024-11-03 게시. 검색 색인 본문 확인; 직접 열람은 HTTP 502로 **실패**.
2. **당대 외교 원문:** [미국 `Foreign Relations of the United States` 1903, 1903-11-04 파나마 임시정부 전보](https://history.state.gov/historicaldocuments/frus1903/d259) — "yesterday afternoon" 11월 3일 선포와 임시 집행위원 구성(원문 전사 본문 **직접 열람**). 파나마 국회와 다른 기관·당대 기록.
3. **미국 역사국 연혁:** [Panama](https://history.state.gov/countries/panama) — 1903-11-06 승인, 11-13 수교; [Panama Canal Treaties](https://history.state.gov/milestones/1977-1980/panama-canal) — 1979 운하지대·1999 운하 운영 이양. 역사국 연혁과 FRUS는 **같은 미국 외교기록 계통**으로, 두 개의 완전히 독립된 국가별 사료라고 과대 집계하지 않음.

**2차 보류:** 1903년 독립선언 원문 및 임시정부의 행정 실효 범위, 파나마 운하지대 조약의 권원(주권·관할권·운영권)과 1979/1999 이양의 구분, 콜롬비아의 후속 승인과 영토 귀속. 현행 파나마 형상을 1903년으로 소급 사용 금지.

## 5. 판정·검사·인계

- **이번 회차:** 북아메리카, **국가별 상세 문헌 1차 3개(BLZ/JAM/PAN)**. 세 국가의 **이미 저장된** `validFrom`과 출처상 독립 효력일이 일치하여 수정 권고 **0건**. 원래 `GEO-023`에서 확인된 날짜를 신규 발견으로 재계수하지 않음. 확정된 국가 신규 데이터 **0건**.
- **1801년 이전은 조사하지 않음.** 1801년 당시 이미 존재한 정치체의 건국일에 관한 추정 없음. 국가성·국명·정부제·국제 승인·영토 실효 통치와 법적 정체성의 구분을 유지.
- **미실행:** 원문 법령 PDF 전수 이미지 판독(벨리즈), 영국 자메이카 법률 XHTML 본문 직접 접속, 파나마 국회 원페이지 직접 열람, 지리정보 파일 다운로드·CRS 확인·해시·GDAL 변환·GIS 위상·화면 대조·배율별 정밀도·0.5 CSS px 검사, 제품 테스트. 독립 역사 형상 자체를 확정하지 않음.
- **변경 0건:** `Pando/work/gis`, `Pando/main`, 기타 작업 브랜치, 국가 lifetime·정본 역사 타임라인·GIS 형상, 원본 SHP/GPKG/GeoJSON·제품 파일·웹/앱·렌더러·배포는 **어떤 것도 수정하지 않음**. 자료 저장소의 본 보고서·순환 기록·색인만 별도 범위로 보관.
- **남은 북아메리카 미완료:** 기존 GEO-LIFE-007의 온두라스/니카라과 정확 법적 날짜; GEO-LIFE-019의 중앙아메리카 연방 최종 존속, 텍사스 편입, 유카탄 분리 국체; GEO-LIFE-025의 미승인 분리정치체 국가성; BLZ/JAM/PAN의 위 2차 검토. 지역 내 다른 국가·소멸국의 1차 전수 역시 아직 미완료.
- **순환 기록:** 직전 `lastProcessedRegion=아프리카` → 이번 `북아메리카(phase-1)` → 이후 `nextRegion=남아메리카`, `nextPhase=남아메리카 미조사 국가·역사 정치체 1차 우선, 소진 시 2차`. 모든 지역 1·2차 완료 전까지 순환 유지.
