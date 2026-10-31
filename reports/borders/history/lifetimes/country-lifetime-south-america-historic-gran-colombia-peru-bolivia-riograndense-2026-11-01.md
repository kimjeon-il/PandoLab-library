# GEO-LIFE-020 — 남아메리카 역사상 소멸·분리 정치체 국가 존속기간 1차 조사 (2026-11-01)

> 상태: `investigating / phase-1 / source-crosschecked / provisional / not-applied`  
> 운영: `Pando/work/gis`의 국가 존속기간 지역 순환 조사. 보고서 정본은 별도 자료 저장소 `reports/borders/history/lifetimes/`에 보관.  
> 범위: **1801-01-01 ~ 2026-11-01**. 1801년 이전 건국·왕조·국경 변천 제외. 해안선·간척·침식 조사 제외.

## 조사 대상 선정·중복 점검

- 직전 완료 회차 `GEO-LIFE-019`: **북아메리카** → 이번 **남아메리카**, **1차 국가·역사 정치체 문헌 조사**. 다음 **오세아니아**.
- 기존 `GEO-LIFE-001`(ARG·BOL·COL 등), `GEO-LIFE-008`(COL·PER·URY·VEN), `GEO-LIFE-014`(ARG·BOL 2차), `GEO-023`(현존 주권국 후보 기간) 및 순환 진행기록을 참조했다. 이번은 해당 현대 국가의 건국일 재조사가 아니라 **그란콜롬비아·페루-볼리비아 연합·리우그란덴시 공화국**이라는 과거 정치체의 독립적 존속성과 법적 성격을 구분하는 1차 조사다. 서로 다른 시기의 세 정치체를 현대 COL/PER/BOL/BRA의 `lifetime`에 자동 연결하지 않는다.
- `Pando/work/gis`의 `AGENTS.md`, 역사 GIS 공통 지침, `config/library-data.json` 및 별도 자료 보고서 색인/순환 기록 확인. 고정 데이터 revision `a3872b373584d06f20da1975f82739c9b6210f1a`. 이 revision의 `assets/data/territorial-entities/generated/v2/index.json` 직접 조회는 **본문이 빈 상태로 반환되어** 오늘 실시간 인덱스의 객체별 ID 및 기간 필드를 검증하지 못했다. 따라서 역사 객체 ID 유무·`validFrom/validTo`를 확정 주장하거나 객체를 생성하지 않는다. 전 회차 `GEO-LIFE-019` 기준 색인 286개는 **과거 조사기록**으로만 참고했다.
- 원격 `Pando` 최근 커밋 검색의 첫 결과는 `2b460e40dbc51de2d13b0fe40e11bd4af9e49b75`이지만 `work/gis`와의 HEAD 동등성은 직접 ref 대조하지 않았으므로 확정하지 않는다.

## 조사 결과 (세 정치체 1차)

### 1. 그란콜롬비아 — 당대 공식 국명 *República de Colombia*

| 확인 날짜 | 성격 | 판단 |
|---|---|---|
| **1819-12-17** | 앙고스투라 의회가 베네수엘라·누에바그라나다를 단일 `República de Colombia`로 결합하는 기본법 채택·공포 | **국가 형성의 법령상 시작 후보**. 당대 각 지방에 대한 완전한 실효 지배를 뜻하지 않음 |
| **1821-07-18 / 1821-10-06** | 통합 기본법 재확인 / 쿠쿠타 헌법 공포 | 국가 통합·헌정 구조의 후속 확립 단계; 최초 법령 일자와 혼동 금지 |
| **1830년** | 베네수엘라·에콰도르의 연방 이탈, 통합 통치 약화 | **점진적 실효 해체**. 정확한 연방 소멸 일자로 단정 불가 |
| **1831-11-17 / 1831-11-21** | 누에바그라나다 기본법 채택 / 시행 | 잔여 통합 공화국의 **법적 종료일 후보는 11-21**. 17일은 의결일이며 시행과 구별 |

독립 대조: 콜롬비아 국립기록원(AGN)은 1819-12-17 `Ley Fundamental`을 기록한다(https://www.archivogeneral.gov.co/del-orinoco-el-cauce-congreso-de-angostura-1819-2019-origen-de-tres-republicas-testimonios-de). 콜롬비아 중앙은행 문화백과는 1819년 법 및 1821년 헌정 단계를 원문 조항과 구분한다(https://enciclopedia.banrepcultural.org/El_proyecto_grancolombiano). 콜롬비아 공영방송 기록원은 1831-11-17 채택과 **11-21 발효**를 별도로 기록한다(https://www.senalmemoria.co/piezas/asi-termino-la-gran-colombia). Archontology는 당시 관보 `Gaceta de Colombia`를 근거로 1819-12-17~1831-11-21 정치체 기간을 제시한다(https://www.archontology.org/nations/gran_colombia/01_polity.php).

**유보:** 법적 국가의 승계가 1831년 누에바그라나다/현 콜롬비아로 어느 범위까지 연속되는지; 1830년에 이탈한 베네수엘라·에콰도르의 각각의 법적 효력 시점과 실효 범위; 1831년 기본법 원본과 당시 관보 직접 대조. 국가 최초 형성일·종료 후보를 현대 국가 `lifetime`으로 승격하지 않는다.

### 2. 페루–볼리비아 연합 (*Confederación Perú-Boliviana*)

| 확인 날짜 | 성격 | 판단 |
|---|---|---|
| **1836-03-17 / 1836-08-06** | 남페루국 성립 선언 / 북페루국 의회의 성립 결의 | **연합 이전 구성국 사건**. 북페루 법령 공포는 08-11이라는 별도 날짜로 기록됨 |
| **1836-10-28** | 안드레스 데 산타크루스의 **연합 설치 칙령** | 삼자 연합 정치체 성립의 문서상 시작 후보 |
| **1837-05-01** | 타크나 `Ley Fundamental`의 연합 규약 | 연합의 후속 법률 체계. 최초 성립일과 동일시 금지 |
| **1839-02-20** | 최고보호관 사임과 연합 정부 종료(사료 색인) | **실효 정부 종료의 후보** |
| **1839-11-10** | 페루 의회 디지털 법령실이 1837년 연합 기본법의 효력 종료일로 기재 | **법령 색인의 효력 종료**. 실제 연합 정부의 존속을 11월까지 입증하지 않음 |

독립 대조: 페루 공화국 의회 법령실의 1836-10-28 설치 칙령 원문(https://www3.congreso.gob.pe/Docs/sites/webs/quipu/constitu/1836con.htm), 1837-05-01 연합 기본법 원문(https://www3.congreso.gob.pe/Docs/sites/webs/quipu/constitu/1837co.htm), 법령 색인의 유효기간(https://www.leyes.congreso.gob.pe/constituciones.aspx). 별도 연구 편찬인 Archontology는 1839-02-20 산타크루스 사임과 연합 정부의 종결을 기록한다(https://www.archontology.org/nations/peru_bol/01_1836_1839_polity.php). 페루 지방정부도 1836년 설치와 1839년 붕괴를 독립적으로 개괄한다(https://www.gob.pe/institucion/muniislaymollendo/noticias/1275596-28-de-octubre-proclamacion-de-la-confederacion-peru-boliviana-1836).

**유보:** 1839-02-20 정부 종료와 1839-11-10 법령 색인 종료의 법적 의미; 볼리비아가 연합 참여 중에도 독립 국가성을 유지했는지(1837년 기본법 1~4조는 각 구성 공화국의 상호 독립과 연합을 명시); 북·남페루 구성국의 개별 효력일 및 승계. **단일 주권국으로 셋을 완전히 합병했다는 판정 금지.**

### 3. 리우그란덴시 공화국 (*República Rio-Grandense*) — 주권국 국가성 **유보 후보**

| 확인 날짜 | 성격 | 판단 |
|---|---|---|
| **1836-09-11** | 브라질 제국에서 분리된 공화국 선포 | 혁명정부의 **정치체 성립 주장 및 일부 실효 통치** |
| **1845-02-25** | 폰시베르지(Ponche Verde) 평화문서의 반군 측 검토·열람 | 협상 단계 |
| **1845-02-28** | 반군 측의 평화 합의·서명에 관한 지방정부 기록 | 군사·정치적 종결 과정 |
| **1845-03-01** | 카시아스 장군의 평화 선언 | 공개적인 종전 선언. **공화국의 단일 법적 소멸일 확정 아님** |

독립 대조: 브라질 국립도서관 디지털 기록(https://bndigital.bn.gov.br/artigos/historia-proclamada-a-republica-riograndense/)은 1836년 선포 사건을 소개하지만 이번 재열람은 HTTP 403으로 실패했다. 상파울루대학교 학술지 `Almanack Braziliense`의 연구(https://revistas.usp.br/alb/pt_BR/article/view/11604)는 1836~1845년 반란정부의 자체 공화국·공보·정치적 정당화 활동을 분석한다. 브라질 바제(Bagé) 시청 역사 기록(https://www.bage.rs.gov.br/municipio/historia)과 파수푼두 시청 1845년 종전 연표(https://www.pmpf.rs.gov.br/cultura/eventos/13a-missa-da-paz-180-anos-da-assinatura-do-tratado-de-paz-de-ponche-verde/)를 비교했다. 비아망(Viamão) 시청은 1836-09-11 선포를 명시한다(https://www.viamao.rs.gov.br/portal/servicos/1005/simbolos-do-municipio).

**유보:** 국제적 승인, 주권독립국 인정 여부, 당대 통제구역, 1845-02-28 서명자·협약 원본 진위와 효력, 마지막 관청/군 지휘권 이양일. 연구 대상은 **실효 분리정치체**이지 검증된 주권국 1건이 아니다. 단독 국가 ID 및 `lifetime` 생성 불허.

## 분류·검증 수준

- 세 정치체의 **1차 문헌 사건 검토**를 수행했다. 독립된 기관·학술자료를 가능한 범위에서 교차 대조했으나, 모든 원관보·관보 스캔·국제법상 국가성을 전부 검증하지는 못했다. 3개 주권국 확정이 아니라 **2개 연합 정치체 + 1개 실효 분리정치체 후보**를 검토한 것이다.
- 연합 해체·정부 종료·법령 효력·실효 지배·외교적 승인을 분리했다. 독립 사료의 동일 문헌 재현을 복수 독립 검증으로 계수하지 않는다.
- 1801년 이전 사건 조사·1801년을 건국일로 대입·해안선/간척/침식 조사 **0건**.
- 국가 색인 직접 본문 대조 **미완료(빈 응답)**; 역사 지형·GIS 위상·정량 화면 검사, 앱/웹 테스트 **미실행**; 새 정본 `lifetime`·형상·타임라인 및 앱/웹 변경 **0건**.

## 다음 순환 및 후속 조사

- **lastProcessedRegion: 남아메리카**
- **nextRegion: 오세아니아**
- **nextPhase: 오세아니아 미조사 역사 정치체·COK/NIU 법적 지위 1차(소진되면 2차 교차검증).** 기존 GEO-LIFE-001/009/015와 GEO-023 중복 제외.
- 남아메리카 2차 인계: 그란콜롬비아 1831 기본법 원관보·현 콜롬비아 승계, 페루–볼리비아 1839 종료의 이중 층위와 각 구성국 국가성, 리우그란덴시 공화국의 국제적 승인·1845 평화 원문. 페루-볼리비아와 남미 연합 정치체의 시대별 서로 다른 엔티티 ID 여부는 자료 인덱스가 정상 열릴 때 다시 확인.
- **남아메리카 전체 1차·2차 미완료**; 다른 다섯 지역도 미완료. 전체 조사 종료나 새 주제 전환 없음.

## 변경 범위

본 보고서·국가 존속기간 지역 순환 진행기록·보고서 색인 3개 파일만 `PandoLab-library-data/main`에 저장. `Pando/work/gis`, `Pando/main`, 다른 작업 브랜치·국가 `lifetime`·형상·정본 GIS·웹/앱·배포 **수정 0건**. 로컬 `publish-reports`/`check-reports` 및 GIS 검사는 **미실행**; 원격 변경 파일·내용 재조회로 저장 여부를 확인한다.
