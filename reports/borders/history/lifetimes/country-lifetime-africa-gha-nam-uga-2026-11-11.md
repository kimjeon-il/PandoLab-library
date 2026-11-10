# GEO-LIFE-030 — 아프리카 국가 존속기간 1차: 가나·나미비아·우간다 (2026-11-11)

> 상태: investigating / phase-1 / source-crosschecked / provisional / not-applied  
> 범위: 1801-01-01~2026-11-11 · 지역: 아프리카 · 미조사 현존 국가 3개 · 다음 지역: 북아메리카  
> 법적 독립·원법령 효력일·국제기구 가입일·정부 형태 변화·국가 법적 동일성·실효 통치를 분리한다. 데이터 반영은 없다.

## 1. 조사 순서·중복 점검·현재 국가 색인

- 직전 완료 국가 존속기간 조사는 GEO-LIFE-029(2026-11-10, 아시아: 시킴·북예멘·남예멘). 이번 차례는 **아프리카 국가별 1차 조사**, 다음 차례는 **북아메리카**.
- GEO-LIFE-001(A–D 일부), 006(에리트레아·기니비사우·세네갈), 012(카메룬·말리·탄자니아), 018(에티오피아·수단·남아공), 024(잔지바르·마다가스카르·다호메이) 및 보고서 색인을 대조했다. **가나·나미비아·우간다에 대한 별도 1차 보고서를 찾지 못해** 이 3국을 선택했다. 현존 국가 중심 1차 조사일 뿐, 아프리카 전수 완료가 아니다.
- Pando `work/gis` HEAD `762a730a6654361911a9c700afcc29396f4fa2cf` (최근 커밋: docs/raw-modern-workspace-handoff.md). 해당 브랜치의 AGENTS.md와 docs/branch-policy.md를 확인했고, 보고서는 현행 정책에 따라 외부 `PandoLab-library-data/reports/borders/history/lifetimes`에 보존한다. Pando `work/gis`의 `config/library-data.json` pin `33d3066e36e16609ae81b77e10913277d56bcd25`.
- 고정판 `assets/data/territorial-entities/generated/v2/index.json` Git blob `d982119a3478199a499aeb8a4058b116a7a83b04`를 **직접 읽고 JSON 파싱하여 288 entities 확인**. 기존 `state:GHA`=1957-03-06, `state:NAM`=1990-03-21, `state:UGA`=1962-10-09, 세 객체의 `validTo=null`. 세 시작일 모두 1차 근거와 일치하므로 **수정 권고 없음**. 이는 288개 객체 전수 역사 판정이 아니다.
- 러시아·튀르키예·조지아의 국가 분류는 기존 진행기록에 따라 유럽으로 고정. 남극/기타 비국가 지리 객체 제외. 1801년 이전 건국·왕조·국경사는 조사하지 않는다.

## 2. 가나 — Ghana (state:GHA)

| 날짜 | 근거 사건 | 국가 존속 판정 |
| --- | --- | --- |
| **1957-02-07** | 영국 `Ghana Independence Act 1957` 국왕 재가. 영국 하원 1957-02-21 회의록의 총리 발표에서 확인. | 재가일이지 독립 효력일 아님 |
| **1957-03-06** | 법률에 따른 Gold Coast의 **Ghana** 명칭 아래 주권국 독립 효력. 영국 총리는 영연방 안의 완전한 독립 주권국이 된다고 발표. | 국가 `validFrom=1957-03-06`을 지지. 영연방 가입과 영국 군주를 국가원수로 인정하는 헌정방식은 식민지 지위의 존속이 아님 |
| **1957-03-08** | 유엔 회원국 가입. | 국제기구 가입일이며 독립일과 다름 |
| **1960-07-01** | 공화국 헌법 발효·공화정 전환. Archontology는 1960-06-29 제헌회의 승인 및 Ghana Gazette 원문 서지사항을 제시. | **국가 법적 계속성 유지 후보**. 1960년을 신생 주권국 건국일이나 1957년 국가 소멸일로 입력하지 않음 |

**독립 출처 및 직접 열람 상태**
1. 영국 국립 법령 데이터베이스, [Ghana Independence Act 1957](https://www.legislation.gov.uk/ukpga/Eliz2/5-6/6/contents) (원법령 웹 목차·효력 항목 검색, 원문 PDF 전체 화면 확인 미실행); 영국 의회 [Hansard 1957-02-21](https://api.parliament.uk/historic-hansard/commons/1957/feb/21/ghana-membership-of-commonwealth) (원시 의회기록 본문 직접 열람; 02-07 재가/03-06 독립).
2. 유엔 [공식 회원국 입회일 목록](https://www.un.org/en/about-us/member-states) (`Ghana` 1957-03-08; 사이트 검색 색인으로 확인, 원본 회원국 목록 전체 열람은 접근 제한).
3. Archontology, [Ghana 1957–1960 Polity Style](https://www.archontology.org/nations/ghana/01_polity_1957.php) (직접 열람, 1957 원 법률·1957 Constitution Order·1960 Ghana Gazette의 문헌 위치 제시). Archontology의 영국 법률 인용은 법률 원문과 **독립 사료 2개로 중복 계수하지 않음**.

**2차 보류:** `Ghana (Constitution) Order in Council 1957` 원문 및 1960 헌법 당대 관보 대조, 영국령 토골란드 신탁통치 종결·가나 귀속의 정확한 별도 법적 절차, 공화정 이행 시 대외 법인격의 문서상 승계. 현행 기간 변경 불필요.

## 3. 나미비아 — Namibia (state:NAM)

| 날짜 | 근거 사건 | 국가 존속 판정 |
| --- | --- | --- |
| **1966-10-27** | 유엔 총회 결의 2145 (XXI)에서 남서아프리카에 대한 남아공 위임통치 종료를 선언. | 남아공의 국제법상 통치 권원에 관한 사건. **1966년을 나미비아 독립 건국일로 소급 금지**; 당시 영토 실효 통치와도 구분 |
| **1990-02-09** | 헌법 제헌회의 채택(유엔 UNTAG 기록). 헌법 제130조 발효는 독립일. | 헌법 채택일 ≠ 독립국 성립일 |
| **1990-03-20** | 남아프리카 공화국 `Recognition of the Independence of Namibia Act 34 of 1990` 재가. | 재가일 ≠ 효력일 |
| **1990-03-21** | 위 남아공 법 제4조 **시행**, 남아공의 관련 행정권 행사 종료와 독립 주권국 승인. 나미비아 헌법 발효·독립식. | 국가 `validFrom=1990-03-21` 강한 교차 근거 |
| **1990-04-23** | 유엔 회원국 가입. | 국제기구 가입일이며 03-21 독립일과 다름 |

**독립 출처 및 직접 열람 상태**
1. 남아프리카 정부 [Recognition of the Independence of Namibia Act 34 of 1990](https://www.gov.za/documents/acts/recognition-independence-namibia-act-34-1990-20-mar-1990) (공식 법률 전사 웹 직접 열람, §1–4와 1990-03-20 재가·03-21 시행 확인; 첨부 원 PDF 미열람).
2. 유엔 [UNTAG 활동·독립 진행 연혁](https://peacekeeping.un.org/sites/default/files/past/untagS.htm) / [United Nations in Namibia](https://namibia.un.org/en/175155-uns-role-namibian-independence) (검색 색인으로 1989 선거·1990-02-09 헌법·03-21 독립·04-23 가입 확인; 첫 URL 상세 본문 직접 열람은 403).
3. 나미비아 사법부 [독립국·헌정 질서 안내](https://www.ejustice.jud.na/ABOUT%20US/Pages/IndependentState.aspx) (1990-03-21 독립과 독립사법제도 기록); [NamibLII Constitution](https://namiblii.org/en/akn/na/act/1990/constitution/eng%402014-10-13) (헌법 제130조·1990-03-21 발효 검색 색인, 직접 열람 403). 남아공 정부·나미비아 사법부·유엔은 기관상 독립.

**2차 보류:** 원시 1990년 나미비아 헌법 관보(2014년 통합본과 구별), 1966 유엔 총회 원결의/1971 ICJ 의견 구체 효과, 1990년 독립 당시 월비스베이 등 별도 영토의 귀속과 향후 변동(국가 탄생일과 역사 형상은 별도). 기존 기간 변경 불필요.

## 4. 우간다 — Uganda (state:UGA)

| 날짜 | 근거 사건 | 국가 존속 판정 |
| --- | --- | --- |
| **1962-03-01** | 우간다 의회 연혁에 따른 국내 자치정부 출범. | 독립 주권국 성립이 아님 |
| **1962-08-01** | 영국 `Uganda Independence Act 1962` 국왕 재가. | 재가일이지 1962-10-09 효력일 아님 |
| **1962-10-09** | 동 법 제1조에 명시된 독립일. 영국 정부의 통치 책임 종료, 우간다 주권국 출범. 우간다 의회도 독립 문서 인수일로 확인. | 국가 `validFrom=1962-10-09`을 지지 |
| **1962-10-25** | 유엔 회원국 가입. | 국제기구 가입일과 독립일 구별 |
| **1963-10-09** | 우간다 1963년 헌법 제1차 개정법에 따른 군주제 종료 및 공화정 체제 전환 후보. Archontology는 1963-09-26 의회 통과·09-30 재가·10-09 효력과 1963 Uganda Gazette 서지를 제시. | **주권국 재건국 아님**. 정확한 개정조문·관보 원본 직접 검증 전 세부 법적 명칭과 국가원수 직위 변화 2차 유보 |

**독립 출처 및 직접 열람 상태**
1. 영국 법령 DB [Uganda Independence Act 1962](https://www.legislation.gov.uk/ukpga/Eliz2/10-11/57?view=plain) (검색 색인에 제1조 전문 및 1962-10-09 확인; 본문 직접 접속 시 JavaScript 봇 차단, 원본 PDF 화면 미열람).
2. 우간다 의회 [History of Parliament](https://parliament.go.ug/page/history-parliament) (1962-03-01 자치정부와 10-09 독립 인수 관련 공식 연혁; 검색 본문 확인, 상세 페이지 타임아웃).
3. 유엔 [공식 회원국 입회일 목록](https://www.un.org/en/about-us/member-states) (`Uganda` 1962-10-25; 검색 색인 확인).
4. Archontology [Uganda 1962–1963 Polity Style](https://www.archontology.org/nations/uganda/01_polity_1962.php) (직접 열람, 1963-10-09 헌법 변동과 1963 Uganda Gazette 법률 서지 정보; 원관보 전수 열람은 미실행). 영국 법률 인용을 영국 법령과 독립된 사료로 다시 집계하지 않음.

**2차 보류:** 1962 독립헌법 Order in Council 1962/2175 원문과 1963 Constitution (First Amendment) Act, 1963 (No. 61/1963) 원관보·1963-10-09 효력 대조, 전통 왕국들의 헌정적 내부 지위/국제 주권국과의 구별. 공화정 전환 후 동일 주권국 연속성에 관한 법제적 서술 완성. 기존 기간 변경 불필요.

## 5. 판정·검사·순환 인계

- **국가별 1차 근거 대조 3개국 완료(이번 배치)**. 확인된 주권국 성립 기준일 후보: 가나 1957-03-06, 나미비아 1990-03-21, 우간다 1962-10-09. **세 날짜 모두 현행 고정판 lifetime 시작일과 일치**하므로 정본 수정 **0건**. 추가 입력 확정/새 역사 정치체 확정 **0건**. 단일 1차 문헌 연구만으로 각국 1801~현재의 모든 법적 연속성·종료 여부를 최종 검증했다고 선언하지 않는다.
- **불확실성:** 가나 1960 원헌법, 나미비아 1966–1990 권원·월비스베이 등 영토, 우간다 1963 공화정 원관보 원문. 각각 2차 검증으로 인계. 기존 아프리카 GEO-LIFE-024의 잔지바르·마다가스카르·다호메이도 2차 유보 유지.
- **미실행:** 현장 문서 스캔/PDF 전체 페이지 검사(이번 회차는 웹 본문 및 검색 색인 대조), GIS 형상·위상/공유경계·배율/화면, 웹·앱 검사, 로컬 `publish-reports` / `check-reports` CLI. 원본 GIS 자료 복사·변환·국가 형상 재생성 없음.
- **변경 허용 범위:** 보고서 정본 저장소의 **본 문서·순환 진행기록·색인**만 갱신. 국가 lifetime/형상/정본 타임라인/코드/Pando `work/gis` 및 `main`/배포 **수정 0건**.
- **순환 커서:** `lastProcessedRegion=아프리카`, `nextRegion=북아메리카`, `nextPhase=미조사 국가별 1차 조사 2~4개(지역 1차 소진 시 2차)`. 전 세계 여섯 지역 모두 1·2차 전수 미완료이므로 순환 지속. 외부 라이브러리 저장은 `work/gis`의 보고서 소유 정책에 따른 것이며 애플리케이션 브랜치 수정을 뜻하지 않는다.
