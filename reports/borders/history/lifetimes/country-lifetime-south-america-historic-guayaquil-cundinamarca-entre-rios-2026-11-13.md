# GEO-LIFE-032 — 남아메리카 역사 정치체 국가 존속기간 1차 조사 (2026-11-13)

> 상태: `investigating / phase-1 / source-crosschecked / provisional / not-applied`
> 선택 지역: **남아메리카** · 직전 지역: **북아메리카** (GEO-LIFE-031, 2026-11-12) · 다음 지역: **오세아니아**
> 범위: **1801-01-01 ~ 2026-11-13**. 1801년 이전 사건·해안선/간척/침식 조사 제외.
> 저장 정본: `kimjeon-il/PandoLab-library-data/reports/borders/history/lifetimes/` (현행 Pando `work/gis/AGENTS.md`에 따른 보고서 보관).
> 주권국 최종 lifetime 입력 승인: **0건**. GIS/국가 엔티티/제품 코드 반영: **0건**.

## 선행 기록과 중복 방지

- `Pando/work/gis`의 `AGENTS.md`, `docs/branch-policy.md`, `config/library-data.json`을 읽음. Pando 코드 저장소의 구 `reports/README.md` 및 `reports/geography/country-lifetime-rotation-progress.md`는 **404**. 현행 규칙상 보고서는 외부 `PandoLab-library-data`에 보관. 외부 `reports/borders/README.md`, `history/lifetimes/country-lifetime-rotation-progress.md`, GEO-LIFE-008/020/026/031, GEO-023 선행 기록 검토.
- 데이터 핀 `921d86aa3c03ffa0b3d5879ad30c9914c4d1b31a`의 `assets/data/territorial-entities/generated/v2/index.json` blob `d982119a3478199a499aeb8a4058b116a7a83b04`을 **실제 읽고 JSON 파싱**: `entities` 288개. `state:ARG` 시작 1831-01-04, `state:COL` 1831-11-21, `state:ECU` 1830-05-13, 세 객체 모두 `validTo=null`; 조사 대상 3개 역사 정치체의 이름/ID는 이 고정판 엔티티 색인에서 확인되지 않음(색인에 없다는 사실만 확인; 어느 시기의 실체가 존재하지 않았다는 뜻 아님).
- 기존 남미 현대 12개국 기초 기록(GEO-LIFE-001/008, GEO-023), ARG/BOL 2차(GEO-LIFE-014), 그란콜롬비아·페루–볼리비아 연합·리우그란덴시(GEO-LIFE-020), 부에노스아이레스국·아크레·줄리아나(GEO-LIFE-026)와 **중복하지 않는** 역사 정치체 3건을 신규 1차 검토. 세 정치체의 역사상 국가성은 각각 별도로 판단.

## 1. 과야킬 자유주(Provincia Libre de Guayaquil, 1820~1822)

| 날짜 | 확인 사항 | 존속기간 판정 |
| --- | --- | --- |
| **1820-10-09** | 과야킬의 스페인 왕권에 대한 독립 선언 및 임시 정부 형성. | 정치적 독립 출발 후보. 도시의 독립과 주 전체에 대한 실효 통치를 동일시하지 않음. |
| **1820-11-08 / 11-11** | 과야킬 시정부의 2024년 자료는 지방대표 57명 회의(11-08), 2025년 자료는 임시통치규정 promulgación(11-11)을 기록. | 대의기구 구성·규정 채택·공포/시행은 구별. 원본 규정의 서명·관보·효력일 확인 전 헌정상의 성립일 확정 보류. |
| **1822-07-13** | 시정부의 2024년 설명에 따르면 볼리바르가 집행위원회(Junta de Gobierno)의 기능을 종료. 독립 연구자 기고(El Universo, 2022)도 7월 13일의 군사·정치권력 장악을 서술. | **사실상 독립정부 종료** 후보. 국제법상 영토귀속 변경의 효력일로 자동 확정하지 않음. |
| **1822-07-31** | 과야킬 시정부는 그란콜롬비아에 대한 영토 편입일을 7월 31일로 구분. | 행정·법적 편입 후보. 원 편입결의·법령/조약 원문 및 효력일 검증 전 법적 종료 확정 보류. |

**서로 독립된 근거**:
1. 과야킬 시청, `Guayaquil celebra 204 años de independencia` (2024): https://guayaquil.gob.ec/guayaquil-celebra-independencia/ — 9 October, 8 November, 13 July, 31 July 구별.
2. 에콰도르 국회, `Loor a Guayaquil al cumplir 193 años de su Independencia` (2013): https://www.asambleanacional.gob.ec/es/contenido/loor_guayaquil_al_cumplir_193_anos_de_su_independencia — 1820-10-09 독립 선언 및 임시정부, 1822-07-26~27 회담 기록. 국회 기념기사는 선언문 원문 아님.
3. 역사학자 Gabriel Fandiño, `El Universo` (2022-07-12): https://www.eluniverso.com/noticias/ecuador/hace-200-anos-simon-bolivar-ponia-fin-al-deseo-de-independencia-guayaquilena-nota/ — 1822-07-13 실효 통제 변경에 관한 제3자 해석.
4. 과야킬 시청 2025년 후속 설명: https://guayaquil.gob.ec/guayaquil-celebra-independencia-nacimiento-libertad-ecuador/ — 1820-11-11 규정 언급. 2024년 시청 설명과 **동일 기관**이므로 독립 출처 둘로 세지 않음.

**유보**: 1820-10-09부터 도시 외 지역의 실제 편입 일자·범위, 1820-11-08과 11-11 규정 절차의 원문, 1822-07-13(실효 정부 종료) 대 07-31(공식 편입)의 원법령·효력일, 국제적 승인 및 법적 국가성. 1822-07-26 회담일을 편입 법적 효력일로 혼동하지 않음. 현재 에콰도르 `state:ECU`의 시작일 1830-05-13을 과야킬에 덮어쓰지 않음.

## 2. 쿤디나마르카국(Estado de Cundinamarca, 1811~1814/1816 검토)

| 날짜 | 확인 사항 | 존속기간 판정 |
| --- | --- | --- |
| **1811-03-30** | 쿤디나마르카 헌법 재가·제정. 왕 페르난도 7세의 명의 아래 국가기관을 구성하는 헌정 문구가 남음. | **1801년 이후 헌정 실체 형성**의 확실한 사건. 완전 대외독립 선언과 다름. |
| **1812-04-17** | 개정 헌법 편찬 종료. | 제도 변화. 독립된 새 국가 탄생으로 자동 처리하지 않음. |
| **1813-07-16** | 완전한 대(對)스페인 독립 선언(국가선거인단). | 왕권과의 법적 단절 주장; 1811 헌정 창설과 다른 층위. |
| **1814-12-12** | 은행 역사백과의 대통령 명단에서 Manuel Bernardo Álvarez의 집행정부 임기 종료; 연방군 포위·장악 맥락. | **독자 중앙정부 실효 종료 후보**이지 곧바로 모든 쿤디나마르카 법적 지위 소멸로 단정 불가. |
| **1815~1816** | 중앙은행 박물관은 발행주체 `Estado de Cundinamarca (1811-1816)`로 1814년 주화의 제작 정보를 수록. | 박물관의 발행주체 연대 범위는 1816년 독립정부 존속의 확증 아님. 연방 편입·스페인 재정복 시기 독자적 정치체 지속성 보류. |

**서로 독립된 근거**:
1. 콜롬비아 국립기록원(AGN) 헌법 목록: https://www.archivogeneral.gov.co/Constituciones-de-Colombia — 1811-03-30 제정 및 1812-04-17 개정.
2. 콜롬비아 공화국은행(Banco de la República) 역사 헌법 원문 색인·일부 전사: https://enciclopedia.banrepcultural.org/Constituciones_de_Colombia — 1811 헌법은 왕명으로 시작, 1812년 개정문.
3. 공화국은행 역사백과 Manuel Bernardo Álvarez 전기: https://enciclopedia.banrepcultural.org/index.php?title=Manuel_Bernardo_%C3%81lvarez_del_Casal — 1813-07-16 완전 독립 결정.
4. 공화국은행 역대 대통령 기록: https://enciclopedia.banrepcultural.org/index.php/Presidentes_colombianos_%281810_-_actualidad%29 — 1814-12-12 임기 종료.
5. 공화국은행 주화 수장품: https://colecciones.banrepcultural.org/es/documento/moneda-de-un-real/63a069155d96b8790f342067 — 1814년 주화, 수장품의 `1811-1816` 표시.
6. 공화국은행 기록지 아카이브: https://babel.banrepcultural.org/digital/collection/p17054coll26/id/4225 — 1811년부터 관보 발간 사실. 은행의 복수 페이지는 **한 기관 계열 근거**로 취급.

**유보**: 국가 전체의 정확한 성립일을 헌법 제정일로 둘지, 1813 독립 선언일로 둘지; 1814 연방 편입의 군사·법률 효력일; 1816 스페인 재정복 시기 법적 동일성·실효 통치·해외 승인. 현 `state:COL`의 1831-11-21 시작일과 동일 정치체로 취급하지 않음.

## 3. 엔트레리오스 공화국(República de Entre Ríos, 1820~1821) — 주권국 분류 유보/부적합 유력

| 날짜 | 확인 사항 | 존속기간 판정 |
| --- | --- | --- |
| **1820-09-29** | 프란시스코 라미레스가 코리엔테스에서 포고(Bando) 및 군사·정치·경제·인지세 규칙을 제정해 지역적 공화국 조직 선언. | **정치·행정체 출범**. `República`라는 명칭만으로 국제법상 분리 주권국이라 볼 수 없음. |
| **1821-07-10** | 라미레스 전사, 체제 위기 및 후계 권력 투쟁. | 창설자의 사망이지 자동적인 법률상 국가 소멸일 아님. |
| **1821-09-28** | 역사 정치연표는 만시야의 지방정부 복귀·공화국 체제 종료로 서술. | **날짜 2차 검증 유보**. 원 당시 임명장·선거록·규정 폐지 원문 미확인, 독립적 사료 두 건 확보 전 확정 금지. |

**서로 독립된 근거**:
1. 엔트레리오스 주정부 2020년 편찬 연구집 `Francisco Ramírez: 200 años de identidad entrerriana` (2020-03 제1판), 인쇄 p.80–81, p.192–193: https://cge.entrerios.gov.ar/recursosaprender/ramirez/assets/francisco-ramirez---interior-a5-(1).pdf — 웹 PDF **p40, p96 화면 직접 확인**. 포고일 1820-09-29, 분리 독립국의 창설을 의도하지 않았다는 저자 분석, 1821년 라미레스 사망 및 행정 재편.
2. Fabricio Gabriel Salvatto(UNLP–CONICET), `Las condiciones político-jurídicas... República de Entre Ríos`, *Anuario del Instituto de Historia Argentina* 23(2), 2023, DOI:10.24215/2314257Xe195: https://www.anuarioiha.fahce.unlp.edu.ar/article/view/aihae195 — 1820~1821년의 지역적 정치·군사 조직 및 명령체계에 대한 **독립된 학술 연구**.
3. 엔트레리오스 주정부 공보: https://portal.entrerios.gov.ar/prensa/noticias/9027 — 1820년 창설과 1821-07-10 사망에 관한 별도 설명. 연구집과 같은 지역 정부 계열로 세지 않음.
4. 독립 원전은 아닌 편집 역사연표(1821-09-28 **후속 검색 단서**, 단독 채택 금지): https://www.rulers.org/argprov1.html

**유보**: 1820 포고·규정의 당시 원본(주립기록원 보관분), 1821-09-28 정부 전환 법률 원문, 1820~1821 코리엔테스·미시오네스에 대한 실제 권한, 외교적 승인·분리 의사. 특히 2020년 주정부 학술 편찬은 **독립국을 만들려는 뜻이 아니었다**고 구분하므로 원칙적으로 지방 분리·특수 행정정체로 추적하며, 국가 `lifetime` 대상 최종 승인 **유보**.

## 판단·자료 정확도·미실행

- **1차 문헌 검토 3건** (과야킬·쿤디나마르카·엔트레리오스). 주권국 확정·최종 `validFrom/validTo` 확정 **0건**. 사건 날짜의 문헌 확인과 법적 국적/동일성/실효 주권은 별개.
- 주요 PDF 중 엔트레리오스 주정부 편찬물 p.40/p.96은 웹 **실제 화면 확인**. 국립기록원 헌법 원본 이미지, 원 방고·조약·관보 전체, 기타 링크된 문헌 전체 전수 판독은 **미실행**. 웹 HTML/학술 초록 검토와 원본 PDF 전체 판독을 구별함.
- 직접 원본 역사 GIS 폴리곤 다운로드, CRS, 인접국 경계, 위상, 배율별 화면 검사, 네이티브/앱 검사 **미실행**(본 자동화는 국가 존속기간 문헌 조사이며 역사 형상은 수정 대상 아님).
- 1801년 이전 건국·왕조·영토 변천, 해안선/간척/침식은 조사하지 않았음. 기존 288개 색인·국가 lifetime·정본 타임라인·역사 형상·앱/웹 코드·렌더러·`Pando/work/gis`·`main`·배포 **변경 0건**. 보고서·순환기록·보고서 색인만 외부 저장소에서 보관.

## 순환 인계

- `lastProcessedRegion=남아메리카`, `nextRegion=오세아니아`, `nextPhase=미조사 주권국/역사 정치체 2~4건 1차(소진 시 2차)`.
- 남미 기존 GEO-LIFE-014/020/026 미해결은 보존. 이번 3건은 **1차 문헌 검토 완료, 법적 동일성·종료 효력·국가성 2차 검증 미완료**로 표시해 차기 남미 1차 조사에서 다시 신규 조사로 집계하지 않음.
- 전 세계 6개 지역 1·2차 전수 조사 **모두 아직 완료 아님**. 단계 소진 전에는 2차만으로 넘어가지 않음. 남극 등 비국가 지리객체는 주권국 대상 외, 횡단 국가 러시아·튀르키예·조지아는 기존 유럽 담당 고정.
