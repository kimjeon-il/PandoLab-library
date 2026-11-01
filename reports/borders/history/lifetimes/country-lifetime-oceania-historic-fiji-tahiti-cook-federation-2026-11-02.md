# GEO-LIFE-021 — 오세아니아 역사 정치체 국가 존속기간 1차 조사 (2026-11-02)

> 상태: `investigating / phase-1 / source-crosschecked / provisional / not-applied`  
> 운영: Pando `work/gis` 국가 존속기간 순환 조사. 보고서 정본은 `PandoLab-library-data/reports/borders/history/lifetimes/`.  
> 연구 범위: **1801-01-01~2026-11-02**. 1801년 이전 역사·기원 조사, 해안선·간척·침식 제외. 제품 데이터·코드 변경 없음.

## 순환·중복 검토 및 자료 기준

- 직전 GEO-LIFE-020 **남아메리카** → 이번 **오세아니아**, **미조사 역사 정치체 1차 3건**, 다음 **유럽**. 오세아니아 지역 전체 1·2차 완료가 아니다.
- 기조사 GEO-LIFE-001(AUS·COK), GEO-LIFE-009(FSM·MHL·PLW·TON), GEO-LIFE-015(NZL·하와이 왕국/공화국), GEO-023(FJI 등 현존국 기간 근거)를 재검토하여 하와이·현재 피지 독립일·현대 쿡 제도 국가성의 중복 신규 조사로 세지 않았다.
- Pando `work/gis`의 `AGENTS.md`, `docs/branch-policy.md`, `docs/historical-border-reconstruction-policy.md`, 자료 고정 설정 `config/library-data.json` 검토. 고정 라이브러리 revision `5eb7be55208efaafe39bd5a65ec2f111d70b9053`. `assets/data/territorial-entities/generated/v2/index.json` blob `f8c0c94a26c492115d41504f3ffc099c19d31d62`는 일반 파일 조회 시 빈 본문이었으나 **blob 직접 읽기로 JSON 파싱·286개 entity 확인 완료**.
- 색인에서 `state:FJI` lifetime=`1970-10-10~null`, `state:COK`=`1965-08-04~null`, `state:NIU`=`1974-10-19~null`, `state:PYF`(프랑스령 폴리네시아, parent=FRA)=`1880-12-30~null` 확인. 이번의 19세기 왕국·연방정부 3건에 이름으로 대응하는 *독립 역사 entity*는 해당 286개 색인에서 찾지 못함(별도 원자료/압축 파일까지 전수 검증했다는 의미 아님). 현존 `FJI/COK/PYF`의 기간을 역사 정치체에 역적용하지 않는다.

## 1. 피지 왕국 / Kingdom of Fiji (Matanitu o Viti): 1871~1874 정치체

| 날짜 | 원자료로 확인한 사건 | 국가 존속기간 관점 |
| --- | --- | --- |
| **1871년** | 세루 에페니사 카코바우의 피지 전체 국왕 주장과 통치기구 구성. 피지 의회 공식 역사교육 자료가 1871년 왕권 주장을 기록 | 왕국/전국 통합정부 출범 후보. 전체 도서의 실효 주권 및 국가적 통합 범위 **미확정** |
| **1871-06-05 (2차 확인 필요)** | 몇몇 2차·3차 자료가 즉위·왕국 출범 날짜로 제시 | 공식 원선언/1871년 관보로 미확인; **확정 `validFrom`으로 사용 금지** |
| **1874-10-10** | 카코바우·마아푸 등 13명의 추장이 영국 왕실에 양도한 **Deed of Cession** 서명 | 영국의 식민 지배와 기존 왕국 정부 종료에 관한 강한 사건 근거. 국내·대외 주권 및 섬별 편입 범위를 상세 확인할 필요 |

- **기관 자료**: 피지 의회, *Our S.a.Y Modules for Primary Schools* (2017), p.23: https://www.parliament.gov.fj/newitems/A4Primarymodules.pdf (텍스트 추출에서 1871 왕권 주장·1874-10-10 양도 확인; 웹 PDF 화면 캡처는 404 오류로 미확인). 
- **독립 학술 검토**: *The Journal of Pacific History*, `History, Hermeneutics and Fijian Ethnic ‘Paramountcy’: Reflections on the Deed of Cession of 1874` (2011), https://www.tandfonline.com/doi/abs/10.1080/00223344.2011.573631 (당시 `Fiji Government Gazette` 1874-10-10 인용; 직접 관보 대조는 미완료). 독립 지역신문의 의식 기록: https://www.fijitimes.com.fj/a-special-day-for-fiji/
- **판정**: 1871~1874 왕국 정부의 존재를 **1차 문헌 검토**, 그러나 1871-06-05 원선언·군도 전체 실효통치·국제법상 단일 주권국 범위와 1874 양도법률의 구체적 효력 모두 2차 유보. 1970-10-10 현대 `state:FJI` 독립과 동일 정치체의 연속 기간으로 작성하지 않음.

## 2. 타히티 왕국 / Pomare 왕조 국가: 보호국·할양·법률 비준 구별

| 날짜 | 확인 사건 | 층위 |
| --- | --- | --- |
| **1842년** | 프랑스의 타히티 보호국 협약 강요; 프랑스령 폴리네시아 기록원은 협약이 **1847년 확인**되었다고 설명 | 보호국화: 대외권 축소와 내부왕정 존속을 구분. **1842년 정확한 체결일 미확정** |
| **1880-06-29** | 포마레 5세가 왕국의 해당 영토를 프랑스에 양도한 협정 | 현지 군주권·통치권 이양 사건. 곧바로 비준·국내법 효력일과 동일시 금지 |
| **1880-12-30** | 프랑스에서 주권 전면 양도를 비준하는 법률 제정 | 프랑스 법률상 비준·식민 지위. 기존 `state:PYF` 1880-12-30과 일치하더라도 과거 타히티 왕국의 확정 종료 필드로 자동 복사하지 않음 |

- **현지 정부 기록원**: `Te Piha Faufa'a Tupuna / Archives de la Polynésie française`, https://www.archives.pf/136-ans-dhistoire-29-juin-1880-tahiti-devient-francais/ (보호국과 1880-06-29 양도, 소속 군도 범위). 같은 기록원의 1883년 왕궁 문서는 1880년 협정과 같은 해 12월 법률 비준을 별도로 언급: https://www.archives.pf/remise-du-palais-21-juin-1883/
- **독립 법률 전사**: 페르피냥대학교 `Digithèque MJP`, *Loi du 30 décembre 1880* 원법률 전사 및 관보 인용: https://mjp.univ-perp.fr/constit/pf1880.htm (원문 관보: `Journal officiel de la République française` 1881-01-01, p.1, 현장 스캔 직접 검증은 미실행).
- **판정**: 1842 보호국화·1880 양도·1880 비준 **서로 다른 단계**. 1801년 이전 왕조 기원·왕국 건국일은 **조사하지 않음**. 보호국 아래 왕국 국가성, 1880-06-29/12-30 중 실제 법적 소멸 기준, 양도된 군도와 소시에테 제도/리워드 제도/감비에 등 범위 **2차 유보**.

## 3. 쿡 제도 연방정부 / Cook Islands Federation: 비주권 보호국 내부 연방 정치체

| 날짜 | 확인 사건 | 판정 |
| --- | --- | --- |
| **1888-09-27** | 영국 보호국 선포 (쿡 제도 역사기록) | 이후 지방 정부의 자체 법률과 영국 대외 보호 병존; 완전 독립국으로 분류하지 않음 |
| **1891-06-05** | 쿡 제도 `Constitution Act 1891` 채택, 총평의회를 `Parliament`로 설정 | **연방 입법기구/내부 정치체 시작의 강한 1차 근거**. 독립 주권국 성립일이 아님 |
| **1900-10-08~09** | 추장·섬별 양도 문서와 영국 병합 선포의 시점은 자료마다 서술 차이 | 정확한 섬별 효력·문서 서명/선포를 다시 확인할 것 |
| **1901-06-11** | 1901-05-13 국왕 추밀원령, 1901-06-10 뉴질랜드 총독 공포에 따라 **뉴질랜드 식민지 영역에 편입 효력** | 확인된 법적 영토 귀속 전환일. 연방의 실효기관 종료일과 동일시 금지 |

- **1891년 당대 공식 문서**: 뉴질랜드 의회 *Appendix to Journals of House of Representatives*, 1891 Session II A-3a (영국 주재관의 보고 및 현지 연방 헌정법): https://paperspast.natlib.govt.nz/parliamentary/AJHR1891-II.2.1.2.4 ; `Constitution Act` 제정일 및 내용은 1898년 재수록: https://paperspast.natlib.govt.nz/parliamentary/AJHR1898-I.2.1.2.4
- **독립 기관 소장 목록**: 뉴질랜드 국립도서관 원기록 목록 https://natlib.govt.nz/records/22619871 (1891~1901 연방 의회 자료, 1891-06-05 법 제정). **현대 정부 역사 서술**: https://nzhistory.govt.nz/cook-islands-achieves-self-government (1901년 의회 해산 기록).
- **당대 법률 정본**: 뉴질랜드 입법 자료 `Cook, etc, Islands Boundaries and Inclusion in New Zealand Proclamation 1901`: https://www.legislation.govt.nz/regulation/imperial/1901/0531/latest/whole.html ; `Cook and other Islands Government Act 1901`: https://www.legislation.govt.nz/act/public/1901/44/en/latest/
- **판정**: 식민/보호국 내부의 지방 연방 정치체를 **주권국 1건으로 세지 않는다**. 국립도서관 목록의 1900년 연방의회 폐지 설명과 NZHistory의 1901년 폐지 서술이 다르므로 **정확한 기관 소멸일 보류**. 1891/1900/1901 날짜를 현대 `COK`의 `1965-08-04` 자유연합 국가성 판단에 직접 대입하지 않음. `NIU`도 별도 법적 분류 보류.

## 검사·불확실성·인계

- 자료 **읽음**: 공식/원법령·기록기관 및 독립 학술·역사 편찬; 과거 데이터 index 286개 **blob 파싱 완료**. `fetch_file`의 대형 index 빈 본문은 `fetch_blob` 우회로 해소했다.
- **수행하지 않음**: 피지 의회 PDF 시각 화면 확인(화면 호출 실패), 타히티 관보 원 스캔 검사, 1891~1901 연방의회 원본 일자 대조, 기존 GIS 원본/형상·배율·위상 검사, 코드·웹/앱 테스트, 로컬 `publish-reports`/`check-reports`. 이번 작업은 공간자료/형상 변경 대상이 아닌 국가 존속기간 문헌 조사다.
- 확정된 **신규 주권국 lifetime 입력 승인 0건**; 국가 `lifetime`, 신규 엔티티 ID, 역사/현대 GIS, 웹/앱 코드, 렌더러, `Pando/work/gis` 및 `Pando/main`, 배포 변경 **0건**.
- **lastProcessedRegion=오세아니아**, **nextRegion=유럽**, **nextPhase=유럽 미조사 역사 정치체 1차(미조사 소진 시 2차)**.
- 오세아니아 후속 2차: 피지 1871 왕국 공식 원선언·실효 지배·1874 양도 관보; 타히티 보호국 체결 효력일·군도 범위·1880 왕국 종료일; 쿡 연방의회 1900/1901 폐지일·영국 양도 효력과 1965 이후 COK, 1974 이후 NIU 주권국 집계기준. 여섯 지역 모두 1·2차 전수 **미완료**. 1801 이전은 계속 제외.
