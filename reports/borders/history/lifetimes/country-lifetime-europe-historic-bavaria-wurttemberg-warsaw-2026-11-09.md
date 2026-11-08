# GEO-LIFE-028 — 유럽 역사 정치체 3건 국가 존속기간 1차 조사 (2026-11-09)

> 관리 ID: `GEO-LIFE-028` · 상태: `investigating / phase-1 / provisional / not-applied`  
> 조사 지역: **유럽** · 직전 지역: **오세아니아(GEO-LIFE-027)** · 다음 지역: **아시아**  
> 조사 범위: **1801-01-01 ~ 2026-11-09**. 1801년 이전 건국·왕조·국경 변천은 미조사. 남극 등 비국가 지리객체는 주권국가 존속기간에서 제외.  
> 정본 저장: `kimjeon-il/PandoLab-library-data/reports/borders/history/lifetimes/` (Pando `work/gis/AGENTS.md`에 따른 보고서 외부 보관)

## 조사 대상·중복 확인·데이터 범위

- Pando `work/gis` HEAD `528fdf0665b3250c34a8a06bbed3892cdf6dd6b2`에서 `AGENTS.md`, `docs/branch-policy.md`, `config/library-data.json` 확인. `reports/`는 Pando 코드 브랜치에 존재하지 않으며 보고서는 외부 라이브러리가 정본이다.
- `config/library-data.json`의 고정 라이브러리 revision `a1bc7a5229b252c5b8d9612026cd0ae3e82d7327`에 해당하는 `assets/data/territorial-entities/generated/v2/index.json` blob `d982119a3478199a499aeb8a4058b116a7a83b04`를 `fetch_blob`으로 읽고 **288개 객체를 JSON 파싱**. `state:DEU`는 `1867-07-01`, `state:POL`은 `1917-10-27`부터로 기입되어 있음. 본 회차 세 옛 정치체인 바이에른 왕국, 뷔르템베르크 왕국, 바르샤바 공국과 일치하는 별도 객체 ID는 현 고정 색인에서 확인되지 않음. 독일·폴란드 객체를 과거 정치체와 동일시하지 않음.
- 이전 GEO-LIFE-001/004(유럽 현존국), 010(발트 국가), 016(체코슬로바키아·동독·유고), 022(양시칠리아·하노버·크라쿠프) 및 지역 순환 기록과 비교: 이 세 역사 정치체의 **별도 국가별 1차 보고서가 없어** 새로운 배치 3건으로 선정. GEO-LIFE-016의 기존 색인 참조 파일 404는 이번 조사에서 수정/복구하지 않음.
- **대륙 배정:** 바이에른·뷔르템베르크·바르샤바 모두 유럽. 러시아·튀르키예·조지아 등 횡단국 유럽 고정 규칙 유지. 1801년 이전 정치체의 탄생일을 조사하거나 `1801-01-01`로 대체하지 않음.

## 1. 바이에른 왕국 (Königreich Bayern)

| 날짜 | 문헌으로 확인된 사건 | 국가 lifetime 해석 |
| --- | --- | --- |
| **1806-01-01** | 선제후 막시밀리안 4세 요제프가 국왕 막시밀리안 1세 요제프로 왕호를 채택하고 왕국 선포. 바이에른 정부·바이에른 역사사전의 1806년 기록·선포 의사록 소재로 대조. | **왕국·왕호 시작일**로 근거 충분. 바이에른 지역 국가 자체의 최초 건국일은 아님. |
| **1871-01-01** (소급 효력) | 바이에른의 독일제국 편입: 의회의 1871-01-21 승인, 01-30 형식상 가입이 01-01로 소급된 경위가 별도로 기록됨. | 왕국은 독일제국 **구성국**으로 존속, 완전 독립 주권의 상태는 달라짐. 1871년을 왕국 종료일로 단정 금지. |
| **1918-11-07/08** | 11-07 혁명, 11-08 임시정부·자유국(Freistaat) 출범. 바이에른 역사박물관과 방송·정부 자료 일치. | **왕정 실효 종료·공화정 전환**. 바이에른이라는 영토/국가 단위의 소멸과 다름. |
| **1918-11-12/13** | 루트비히 3세의 충성 서약 해제 성명 작성 11-12, 11-13 발표. 바이에른 역사사전은 이것을 **정식 퇴위 서명과 구별**한다. | 법적 왕권 종료 절차 및 시작/종료일 배타성은 2차 유보. |

**독립 출처·열람 수준**
1. 바이에른주 정부, *Bayerische Geschichte*, 1806 왕국 성립 및 1818 헌법의 1918 종료: https://www.bayern.de/der-freistaat/bayerische-geschichte/ — 공식 기관 설명 직접 열람.
2. *Historisches Lexikon Bayerns*, *Königswürde (1806)*, 바이에른 주립기록원 `Landtag 10189`의 1806-01-01 원 의사록 소개: https://www.historisches-lexikon-bayerns.de/Lexikon/K%C3%B6nigsw%C3%BCrde_%281806%29 — 학술 역사사전 직접 열람. 원문 기록 이미지 별도 검독 **미실행**.
3. Haus der Bayerischen Geschichte, 왕국 기간 1806-01-01 ~ 1918-11-08: https://archiv.hdbg.de/geschichte-bayerns/de-02-die-geschichte-05.php — 역사기관 별도 설명 직접 열람.
4. *Historisches Lexikon Bayerns*, *Reservatrechte*, 제국 가입 1871년 소급 효력 구분: https://www.historisches-lexikon-bayerns.de/Lexikon/Reservatrechte — 직접 열람.
5. *Historisches Lexikon Bayerns*, *Anifer Erklärung, 12./13. November 1918*: https://www.historisches-lexikon-bayerns.de/Lexikon/Anifer_Erkl%C3%A4rung%2C_12./13._November_1918 — 원 성명 기록 및 정부의 퇴위 해석 구별, 성명 원 이미지 **미실행**.

**2차 검증 보류:** 1806 왕국 선포 원관보·의사록 원본 전체, 1870/71 조약 법적 효력·왕국의 연방 구성국 지위, 1918 왕정 종료의 법적 최종 기준(11-08 / 11-12 / 11-13) 및 후계 자유국과의 법적 동일성. 왕국이라는 **정부 형태** 기간과 바이에른 국가·영토체의 **법적 계속성**을 다른 필드로 분리해야 하므로, 새 lifetime 값은 입력하지 않음.

## 2. 뷔르템베르크 왕국 (Königreich Württemberg)

| 날짜 | 문헌으로 확인된 사건 | 국가 lifetime 해석 |
| --- | --- | --- |
| **1806-01-01** | 선제후 프리드리히가 슈투트가르트 행사에서 국왕 지위를 취함. 바덴뷔르템베르크 주립 궁전관리기관 원행사 해설 및 Landesarchiv의 1806–1918 자료 범위 일치. | **왕국 시작일**, 기존 뷔르템베르크 국가 최초 건국일 아님. |
| **1870-11-25 / 1871** | 독일연방 구성 조약 가입과 이후 독일제국의 구성국화. 주립기록원 전시·원조약 소장 정보로 확인. | 왕국 계속, 완전한 대외 주권과 제국 내 구성국 지위를 구별. |
| **1918-11-09** | 혁명 중 임시 주정부 수립·공화정 선언. 기록원 LEO-BW는 11-10 구왕실 내각 해산의 별도 과정도 설명. | 실효 정부 전환. 왕의 정식 퇴위와 **다른 날짜**. |
| **1918-11-30** | 국왕 빌헬름 2세 퇴위 선언, 임시정부 접수. 원문은 `Regierungsblatt für Württemberg 1918 S. 263`, 기록물 `HStAS M 743/1 Bü 1 Nr. 10`으로 목록 확인. | 법적 왕권 종료를 확인하는 핵심 날짜이지만, 왕국 실효 통치 종료일(11-09)과 불일치. |

**독립 출처·열람 수준**
1. Staatliche Schlösser und Gärten Baden-Württemberg, *1. Januar 1806: Der württembergische Kurfürst Friedrich wird König*: https://www.schloss-ludwigsburg.de/en/press-media/press-releases/press-releases-detail/4629 — 공공 문화유산기관 직접 열람.
2. Landesarchiv Baden-Württemberg, *Das Königreich Württemberg in Zahlen*: https://www.landesarchiv-bw.de/de/landesarchiv/projekte/projektarchiv/43991 — 1806–1918 왕국 역사자료 프로젝트 직접 열람.
3. LEO-BW/Landesarchiv, *Die provisorische Regierung des Volksstaates Württemberg*: https://www.leo-bw.de/en/themenmodul/von-der-monarchie-zur-republik/zeitstrahl/die-provisorische-regierung-des-volksstaates-wurttemberg — 11-09 임시정부, 11-10 왕실 내각 해산 기록 직접 열람.
4. LEO-BW, *Abdankung König Wilhelms II*: https://www.leo-bw.de/de/web/guest/themenmodul/von-der-monarchie-zur-republik/zeitstrahl/abdankung-konig-wilhelms-ii-von-wurttemberg — 1918-11-30 당대 퇴위 문서 소장정보 직접 열람.
5. `Regierungsblatt für Württemberg 1918 S.263` 전사: https://www.verfassungen.de/bw/wuerttemberg/thronverzicht18.htm — 원관보가 아닌 **민간 전사** 열람. 원관보 스캔 교차확인 **미실행**. 3·4는 같은 지역 기록체계의 중복 설명으로 완전히 독립된 원사료 2건으로 세지 않음.
6. Landesarchiv의 1870/71 제국 형성 전시: https://www.landesarchiv-bw.de/de/aktuelles/nachrichten/69212 — 1871 법적 지위 변화의 역사 연구 출처.

**2차 검증 보류:** 1806 왕호 채택 원선언과 실제 공포일, 1870 가입 조약 효력·1871 제국내 법적 지위, 1918-11-09 공화정 선포 원문, 왕국 종료의 법적 기준(11-09 / 11-30), 뷔르템베르크 구성국/자유국의 법적 계속성. **현재 국가 색인 신규 lifetime 및 객체 생성 금지.**

## 3. 바르샤바 공국 (Księstwo Warszawskie)

| 날짜 | 문헌으로 확인된 사건 | 국가 lifetime 해석 |
| --- | --- | --- |
| **1807-07-09** | 프랑스–프로이센 틸지트 조약 서명. **제15조**는 프로이센 양도지를 작센 국왕이 바르샤바 공국 명의로 주권 행사하도록 규정함. | 공국 성립의 **조약 날짜**. 제1조가 비준서 교환 후 효력을 규정하므로 바로 유효 시작일로 확정하지 않음. |
| **1807-07-22** | 드레스덴에서 나폴레옹이 공국 헌법을 재가. 폴란드 하원(Sejm) 도서관의 헌법 전사 최종 조항과 AGAD의 1807-07-22 헌법 기록물 목록 대조. | 공국 헌정 기반 확립. 조약 효력·행정 집행 시작과는 구분. |
| **1813년** | 나폴레옹 패전 후 공국의 실효통치가 무너지는 과정. 국립 옛 기록원의 각료회의 자료 존속 기록은 1813년까지. | **정확한 점령일·실효 국가 소멸일 미확정**, 기록물 최종연도만으로 단정 금지. |
| **1815-05-03 / 06-09** | 러시아–프로이센·러시아–오스트리아 관련 조약(05-03), 빈 회의 최종의정서(06-09) 제1조는 공국 영토 분배와 러시아 황제하 폴란드 왕국 재편 규정. | 공국 해체의 조약상 근거. **체결일과 실제 영토 이관·시행일 다름**; 단일 법적 종료일 보류. |

**독립 출처·열람 수준**
1. Fondation Napoléon, *Treaty between Prussia and France, Tilsit, 9 July 1807*, 원조약 제15조 전사: https://www.napoleon.org/en/history-of-the-two-empires/articles/treaty-between-prussia-and-france-tilsit-9-july-1807/ — 직접 열람. 다른 웹사이트에 실린 동일 조약 전사는 독립 원사료로 중복 계산하지 않음.
2. 폴란드 의회 도서관, *Ustawa Konstytucyjna Księstwa Warszawskiego*, 1807-07-22: https://biblioteka.sejm.gov.pl/tek01/txt/kpol/1807-r12.html — 1807년 헌법 원문 전사 직접 열람.
3. 폴란드 중앙고문서기록원 AGAD, *Rada Ministrów Księstwa Warszawskiego* 인벤토리: https://www.agad.gov.pl/inwentarze/RMKW176.xml — 1807-07-22 헌법 사본 및 1807–1813 각료회의 문서 소장 정보 직접 열람. 2와 3은 서로 다른 기관의 보관 기술이나 **동일 헌법 내용은 독립된 법령 2개가 아님**.
4. 폴란드 국가 교육 플랫폼, *Decyzje kongresu wiedeńskiego w sprawie polskiej*, 1815-05-03 조약과 06-09 최종의정서 제1조 전사: https://zpe.gov.pl/a/decyzje-kongresu-wiedenskiego-w-sprawie-polskiej/DEPDFKZJT — 교육기관의 재수록 법률 문서·설명 직접 열람. 빈 회의 조약 원 비준문·원문 스캔 **미검증**.
5. 폴란드 국가 교육 플랫폼, *Podział Księstwa Warszawskiego*: https://zpe.gov.pl/a/podzial-ksiestwa-warszawskiego/DmmRMOpWY — 1815 공국 해체 및 후계 폴란드 왕국 성립을 설명하는 2차 자료.

**2차 검증 보류:** 틸지트 조약 비준서 교환일 및 효력, 1807 공국 최초 실효 행정·전 외교권 한계(프랑스 위성정치체/작센 국왕과 군주 결합), 1813 점령과 망명정부 법적 계속성, 1815 개별 조약 비준·영토 이관·의정서 실제 시행일 및 공국/폴란드 왕국 법적 동일성. 현대 `state:POL` 시작일을 1807년으로 되돌리지 않음.

## 검증 결과와 다음 인계

- **이번 회차 유럽 1차 배치 3건**(바이에른 왕국, 뷔르템베르크 왕국, 바르샤바 공국) 문헌 조사 완료. 새로 최종 확정·승인한 국가 lifetime **0건**. 1801년 이전 기원 조사 없음.
- **직접 수행:** `work/gis`의 운영규칙·자료 핀 확인, 이전 보고서·순환기록·색인 대조, 고정판 색인 288개 JSON 파싱, 독일 주정부·기록원·역사사전 및 폴란드 의회 도서관·기록원·조약 전사 웹 문서 열람. 서로 같은 법령의 재수록본을 독립 법률 증거로 중복 계산하지 않음.
- **미실행/미확보:** 1806·1918 독일 원관보와 1807·1815 조약 비준·시행 원스캔 전수, 헌법 원문 스캔 시각검증, 상세 GIS 형상·위상·배율·화면·웹/앱 검사, 로컬 `publish-reports` / `check-reports` CLI. 위 문헌 열람만으로 역사적 폴리곤의 정확성을 보증하지 않음.
- **분류:** 독일 제국 구성국의 왕호·정부형태 존속과 대외 주권, 바르샤바 공국의 프랑스 종속 및 작센 국왕 군주권을 구분. 바이에른·뷔르템베르크의 1918 왕정 종료와 국가 동일성 단절을 혼동하지 않는다.
- **제품 데이터 변경:** 국가 lifetime·정본 타임라인·역사 GIS 형상·국가 객체·웹/앱 코드·렌더러·Pando `work/gis`·`main`·배포 모두 **0건**. 보고서·지역 순환 진행기록·보고서 색인만 자료 저장소에서 변경한다.
- **커서:** `lastProcessedRegion=유럽`; `nextRegion=아시아`; `nextPhase=미조사 역사 정치체 국가별 1차 2~4개(1차 소진 시 사건별 2차)`. 유럽 기존 GEO-LIFE-010/016/022 및 이번 세 건의 미확정 법적 종료·동일성은 유럽 2차 인계. **6지역의 1·2차 전수 모두 미완료**.
