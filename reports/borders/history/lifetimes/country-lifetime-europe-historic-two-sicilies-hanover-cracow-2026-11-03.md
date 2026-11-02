# GEO-LIFE-022 — 유럽 역사 정치체 국가 존속기간 1차 조사: 양시칠리아·하노버·크라쿠프 (2026-11-03)

> 상태: `investigating / phase-1 / source-crosschecked-partially / provisional / not-applied`  
> 조사 범위: 1801-01-01~2026-11-03. 1801년 이전 건국·왕조·국경 변천은 조사하지 않음.  
> 운용: Pando `work/gis`의 국가 존속기간 지역 순환. 보고서 정본: `PandoLab-library-data/reports/borders/history/lifetimes/`. 보고서·진행기록·색인 이외 제품 자료 및 코드 변경 금지.

## 1. 순환 위치·기존 조사 및 색인 대조

- **직전:** GEO-LIFE-021 오세아니아 → **이번 유럽** / 미조사 역사 정치체 1차 3건 → **다음 아시아** / 미조사 1차(소진 시 2차). 이번 유럽 **배치** 완료이지 유럽 1차·2차 **전수 완료가 아님**.
- 기조사 GEO-LIFE-001(A–D 현존국), GEO-LIFE-004(유럽 현대국·횡단국 27건), GEO-LIFE-010(발트 3국 2차), 진행기록상의 GEO-LIFE-016(체코슬로바키아·동독·유고슬라비아)을 중복 조사로 집계하지 않음. GEO-LIFE-016 원문은 현행 외부 저장소 `main` 직접 조회에서 404이며 색인에는 남아 있어 정합성 보류; 임의 재생성·삭제하지 않음.
- 이번에는 19세기 기존 현존 현대 국가의 설립일이 아닌, **양시칠리아 왕국**, **하노버 왕국**, **크라쿠프 자유시**를 조사. 크라쿠프는 보호국적 지위 때문에 주권국 집계 **유보**.
- Pando `work/gis` HEAD 확인: `a60eae2815c67f7c25c1bd3e432543265dd14c75` (2026-11-02T15:42:13Z). `AGENTS.md`와 `docs/branch-policy.md`의 외부 보고서 정본 분리 정책 확인. `reports/README.md`와 `reports/geography/`는 Pando `work/gis`에 존재하지 않아, 정본 `PandoLab-library-data/reports/borders/README.md` 및 `reports/borders/history/lifetimes/country-lifetime-rotation-progress.md`를 사용. 다른 앱 브랜치에는 쓰지 않음.
- 자료 핀: Pando `config/library-data.json` revision `5eb7be55208efaafe39bd5a65ec2f111d70b9053`, `assets/data/territorial-entities/generated/v2/index.json` blob `f8c0c94a26c492115d41504f3ffc099c19d31d62`. GitHub `fetch_blob` 결과 JSON **286개 entity 실제 파싱**. `state:ITA`=`1861-03-17~null`, `state:DEU`=`1867-07-01~null`, `state:POL`=`1917-10-27~null`. 3개 역사 정치체의 별도 ID는 이 색인 내 ID·한글/대체 이름 검색에서 미발견; 압축 원자료 전체의 비존재를 증명한 것은 아님. 기존 기간값은 **검증 대상 기록일 뿐 확정 수정 근거가 아니며 모두 유지**.

## 2. 양시칠리아 왕국 — Regno delle Due Sicilie

| 역사 날짜 | 검토 사건 | 법적 동일성·실효 주권 관점 |
| --- | --- | --- |
| **1816-12-08** | 페르디난도 1세가 나폴리·시칠리아 영토를 하나의 양시칠리아 왕국으로 합치는 기본법 제정 | 두 전신 왕국의 **통합·국호 및 제도 변경**. 이전 국가와의 법적 계속성은 별도 문제 |
| **1816-12-09** | Archontology는 앞서 제정한 법의 공포·발효를 **12월 9일**로 기록 | **법률일 8일 / 시행·공표일 9일** 구분; 원관보 직접 열람 미완료 |
| **1860-09-06~07** | 프란체스코 2세의 나폴리 철수 및 사르데냐 측 행정권 장악 | 나폴리 실효 통치 상실이지 왕권의 즉각 법적 소멸과 동일하지 않음 |
| **1860-12-17** | 사르데냐 국왕의 남부 주·시칠리아 편입 칙령(Archontology에 당대 관보 번호·페이지 제시) | 병합 법령 사건. 당시 모든 지역의 실효 지배 완료 여부와 구분 |
| **1861-02-13** | 가에타 요새 항복; 프란체스코 2세의 마지막 주요 실효 통치권 소멸 | 국가의 실효정부 종료일 후보. 12월 칙령과 **같은 날짜가 아님** |
| **1861-03-17** | 통일 이탈리아 왕국 선포 법률 제4671호 | 후계 이탈리아 왕국 성립 관련, 양시칠리아의 단독 종료일로 단순 복사하지 않음 |

**독립 출처:** 이탈리아 문화부 국립기록원 SIAS `Regno delle Due Sicilie, 1816–1860`는 1816-12-08 기본법 제1조와 1860-10-21 투표, 1861년 편입을 명시한다. https://sias-archivi.cultura.gov.it/cgi-bin/pagina.pl?Chiave=29&TipoPag=contesto ; 역사 연대기 Archontology는 1816년 법의 8일 제정/9일 발효, 1860년 왕실·통치 중심 이탈, 1860-12-17 칙령 및 1861-02-13 가에타 항복을 당대 법령집 참조와 함께 정리한다. https://www.archontology.org/nations/italy/kingdom_of_two_sicilies/01_polity.php ; 이탈리아 문화부 가에타 최후 항전 설명 https://cultura.gov.it/luogo/ponte-real-ferdinando ; 이탈리아 국방부의 1861-03-17 통일 법률 원문 인용 https://www.difesa.it/area-storica-html/pilloledistoria/17-marzo-1861-litalia-unita/34902.html

**1차 판정:** 왕국 통합과 후일 병합·실효통치 종료의 핵심 기간 근거 확보. **단일 `validFrom`: 1816-12-08 vs 09 최종 유보**, **단일 `validTo`: 1860년 편입 법률 vs 1861-02-13 마지막 통치권 소멸 및 법적 소멸의 동일성 유보**. 원본 1816/1860 법령 원스캔 및 국제승인·법적 승계 연구 추가 필요.

## 3. 하노버 왕국 — Königreich Hannover

| 역사 날짜 | 검토 사건 | 판정 |
| --- | --- | --- |
| **1814-10-12 (원선언 추가 검증)** | 빈 회의 중 하노버 선제후국이 왕국으로 승격·선포되었다고 복수 역사편찬 자료가 제시 | 1814년 왕국 성립 강한 후보. **당대 왕실 선언문·공포일 직접 대조 미완료** |
| **1814~1837** | 영국 국왕과 하노버 국왕 동군연합 | 같은 군주 ≠ 영국에 병합. 별도 정치체·외교 지위 검토 |
| **1866-06-29** | 랑겐잘차 전투 후 하노버군 항복 | 실효 군사권 상실. 법적 병합일은 아님 |
| **1866-09-20** | 프로이센 `Gesetz, betreffend die Vereinigung des Königreichs Hannover ...` 제정 | **법률 제정일**. 원래 하노버·헤센·나사우·프랑크푸르트 병합 법률 |
| **1866-09-22** | 니더작센 주립기록원 설명에서 '병합'일로 기재 | 법률 공포·현지 인식과 20일 제정일의 정확한 관계는 **보류** |
| **1866-10-01 / 10-03** | 독일역사박물관은 10월 1일 프로이센 헌법 적용 및 주 편입 서술; 10월 3일 영토 점유 특허 문서별 차이 | 20일 법 제정·22일 기록원 날짜·10월 시행/포고 중 **단일 종료일 미선정** |

**독립 출처:** 니더작센 주립기록원 NLA의 1866-10-05 게오르크 5세 항의선언 보존자료(1866-09-22 병합으로 기술) https://nla.niedersachsen.de/startseite/landesgeschichte/aus_den_magazinen_des_landesarchivs/2016/aus-den-magazinen-des-landesarchivs-oktober-2016-139830.html ; 프로이센 1866-09-20 병합 원법의 당대 인쇄본은 바이마르 Herzogin Anna Amalia Bibliothek 목록에서 1866년 `Sammlung der Gesetze ... für das Königreich Hannover` 제43호, 269~270쪽으로 확인 https://portal.haab.klassik-stiftung.de/Record/779156013 ; 법조문 전사(원본 시각 검증 미완료) https://www.verfassungen.de/preussen/gesetze/preussen66.htm ; 독일역사박물관 LeMO(1866-10-01 프로이센 헌법 적용 및 주 편입) https://www.dhm.de/lemo/kapitel/reaktionszeit/deutscher-bund-und-nationale-frage/die-preussischen-annexionen-1866 ; 1814-10-12 제시 자료 https://feltas.de/ereignis/proklamation-koenigreich-hannover.html

**1차 판정:** 하노버 별도 왕국 존재(1814~1866)·프로이센 병합은 확인. **왕국의 성립일은 원선언 검증 전 1814-10-12 잠정**, 법적 종료일은 1866-09-20/22/10-01/10-03의 법률·공표·집행 구분 추가 검증. 동군연합 1837년 해체는 하노버 신국가 건국으로 간주하지 않음. 기존 하노버 선제후국의 1801년 이전 성립사는 미조사.

## 4. 크라쿠프 자유시 — Wolne Miasto Kraków / Rzeczpospolita Krakowska

| 역사 날짜 | 검토 사건 | 판정 |
| --- | --- | --- |
| **1815-05-03** | 오스트리아·프로이센·러시아 조약으로 자유·독립·엄격중립 도시 및 구역 설치 | 공식 명칭은 '독립', 실제 외교는 **3국 보호관계** 아래. 완전 주권국 여부 별도 |
| **1815-06-09** | 빈 회의 최종의정서에서 크라쿠프의 지위 규정 확인 | 5월 조약과 6월 확정을 서로 다른 효력 층위로 보존 |
| **1836~1841** | 외국 군대의 점령·간섭 | 독립 법적 국가 자동 소멸로 보지 않음 |
| **1846-02~03** | 크라쿠프 봉기와 외세 군사介入 | 실효 통치 변화. 법적 종료일과 구분 |
| **1846-11-06 / 11-11 / 11-16** | 3국 지위 폐기 합의(6일), 황제 점유 특허(11일), 합병일로 기술되는 16일 | 3개 시점 구별; 직접 조약·특허 원문 및 지역 발효일까지 검증 필요 |

**독립 출처:** 크라쿠프 국립기록원은 1815-05-03 국가 구성과 당시 헌정기록·1833년 헌법 사본 `WMK I 19`를 제시 https://ank.gov.pl/wystawy/wolne-miasto-krakow-1815-1846-materialy-z-zasobu-krakowskiego-archiwum/ ; 폴란드 교육부 교육포털에 1815-06-09 빈 회의 최종의정서 제6조 사료와 보호·중립 규정 제시 https://zpe.gov.pl/watek/LPAMVE4GV7/36/a/decyzje-kongresu-wiedenskiego-w-sprawie-polskiej/D4HXB2EG8 ; 크라쿠프 항소법원은 1815년 조약 이중일자(구력/신력 4월 21일/5월 3일) 및 사법 헌정 기록 확인 https://www.krakow.sa.gov.pl/wolne-miasto-krakow%2Cnew%2Cmg%2C213.html%2C18 ; 폴란드 교육포털 지도 설명은 1846-11-16 오스트리아 편입일 제시 https://zpe.gov.pl/a/emisariusze-i-kraj/DnTZrXca ; 크라쿠프 국립기록원 역사 https://ank.gov.pl/o-archiwum/dzieje-archiwum/ . 추가 학술 논문 검색 결과는 1846-11-06 합의·11-11 점유 특허를 제시하나 **논문 PDF 원문 시각 열람 미실행**: https://ruj.uj.edu.pl/bitstreams/ae861baa-672a-4c31-bac5-90e63e78d483/download

**1차 판정:** 1815~1846 크라쿠프의 독립적인 헌정기관·지역 통치와 3국 보호관계 병존 확인. **국제법상 완전한 독립 주권국으로 최종 확정하지 않음**; 보호국·명목독립 도시국가 별도 분류 후보. 1846년 병합의 조약일·점유선언·효력일을 최종 lifetime 필드로 선택하지 않음. 1801 이전 역사는 다루지 않음.

## 5. 제한·후속 검증·인계

- **증거 구분:** 공식 기록원·조약문 전사·독립 역사 편찬 자료가 서로 독립적인 경우만 교차근거로 사용. 법률 목록 조회는 원문 전문의 내용·일자·발효를 검증한 것과 구별. 불확실한 법적 동일성은 보류하고 '주권국 3건 확정'이라 표현하지 않음.
- **실행 검사:** 외부 문헌 페이지 및 GitHub 현재 색인 blob **읽음**. 역사 법률 원문 일부는 전사·검색/색인만 확인, PDF 스캔 화면 재검증 **미실행**. GIS 원본·시대별 형상/위상·국가·영토 경계 지도 비교, 웹/앱 회귀·렌더러 검사 **미실행**. 이 보고서는 국가 존속기간에 대한 문헌 조사이며 형상 도입 승인 아님.
- **객체 데이터 변경 0건:** `lifetime`·국가/하위 정치체 객체 ID·역사/현대 형상·정본 타임라인·웹/앱 코드·Pando `work/gis`·`main`·다른 작업 브랜치·배포 전부 수정하지 않음. **보고서/진행기록/색인만** 외부 정본 보고서 저장소에 기록.
- **지역 커서:** `lastProcessedRegion=유럽`, `lastBatchCompletedRegion=유럽`, `nextRegion=아시아`, `nextPhase=미조사 역사 정치체 1차(소진 시 시기·사건별 2차)`. **유럽 전체 phase-1/phase-2는 미완료**; 아시아 포함 전 세계 6개 지역 모두 두 단계 전수 미완료.
- **2차 인계:** 양시칠리아 1816법 시행일·1860 병합/1861 가에타·국가 법적 소멸; 하노버 1814 원선언 및 1866 법·공포·시행·점유문서; 크라쿠프 국제법상 주권 범주 및 1846 조약/특허/병합 최종 효력. 다른 지역 기존 미해결 사건은 순환 진행기록의 종전 내용을 그대로 유지.
