# GIS 보고서 자동 검토 — 2026-11-04 22:00 UTC

- ID: GEO-REVIEW-20261104-2200
- 상태: reviewed / supplemental-corrections / important-holds
- 지도 반영: report-only / runtime-unchanged
- 검토 기준: Pando main `d667ed067354d086edfa362da3dea88b7b2b16bc`, work/gis `26ecb9ca0237d0d8026c190d50f52c664e53a723`; data main `68c9a1fa23dd3272c5822697cfbeffc3e537265a`, work/gis `c1d25c3f4e2b139fd043a919e411f4a7825f2ecc`.
- 아래 main 원본의 보충 정정판이다. 원문·진행기록을 복사하거나 변경하지 않는다. 이번 기록은 data work/gis에만 보관한다.

## 1. 변경 이력과 중복 방지

직전 검토 [6e3e3f9](https://github.com/kimjeon-il/PandoLab-library-data/commit/6e3e3f9dfae3cbf7a1c73016bad5e81a65c9128f)의 main 기준 `4dfc9729cf6a206db72b2a3140b1cd66cbf7f356` 및 work/gis 검토 커밋과 전체 reports tree를 비교했다. 모든 비교 tree는 truncated=false다.

- Pando 양 브랜치 전체 tree에 reports 파일은 0개다. 외부 자료 정본의 reports/README.md, 전용 reports/borders/와 남아 있는 reports/geography/를 확인했다.
- data main: 국가·시대별 새 본문 2개, 진행기록 2개와 borders 색인 수정, 새 검증 묶음 6개(첨부 포함 123개 파일). borders 전체 추가·수정 128개, 삭제 0개. 별도 development 변경 117개는 국가 경계 근거로 가져오지 않는다.
- data work/gis: 보고서 19개 추가·수정과 비교 PNG 1개 삭제. 500km² 미만 연구 종료·요약·상태표 갱신이며 기존 세부 연구를 재개하지 않는다. 직전 검토 이후 12개 커밋의 출처와 변경 경로를 대조했다.
- 아래 원본과 처리 기준, 변경 파일/blob 목록은 [evidence.json](evidence.json)에 기록했다. LIFE022/023, TIME019/020 등 이전 본문은 동일 blob이므로 다시 반영하지 않는다.

| 보고서 | 원본 커밋 | 원본 경로 |
| --- | --- | --- |
| GEO-LIFE-024 | [b6d7c787](https://github.com/kimjeon-il/PandoLab-library-data/commit/b6d7c787145060203b19ba206fc26ea36eb15f33) | [잔지바르·마다가스카르·다호메이](https://github.com/kimjeon-il/PandoLab-library-data/blob/b6d7c787145060203b19ba206fc26ea36eb15f33/reports/borders/history/lifetimes/country-lifetime-africa-historic-zanzibar-madagascar-dahomey-2026-11-05.md) |
| GEO-TIME-021 | [71d77218](https://github.com/kimjeon-il/PandoLab-library-data/commit/71d77218dff8620214da35025b620ab7073b99d3) | [페루·콜롬비아 산타로사](https://github.com/kimjeon-il/PandoLab-library-data/blob/71d77218dff8620214da35025b620ab7073b99d3/reports/borders/history/timeline/historical-timeline-2025-south-america-peru-colombia-santa-rosa-2026-11-05.md) |

파일명 11/5는 한국 시각 기록이다. LIFE 커서는 아프리카 다음 북아메리카, TIME은 2025 남아메리카 다음 오세아니아이며 어느 지역도 전수 완료가 아니다. 원문 누락 LIFE016 및 TIME010–013의 기존 보류는 새 본문으로 추측 복구하지 않는다.

## 2. LIFE024 — 직접 확인한 날짜와 증거 단계 보완

### 잔지바르

[UN RIAA의 중재판정 원문 재록, pp.109–113](https://legal.un.org/riaa/cases/vol_XXVIII/107-114.pdf)은 **1861-04-02 Canning 중재판정**을 수록한다. 잔지바르와 무스카트의 분리, 잔지바르 통치자로 Majid를 인정하는 결정 및 이후 무스카트 05-15·잔지바르 06-25/29 수락 서신을 구분한다. 원본의 막연한 1861년 설명을 “1861-04-02 분리 중재판정과 후속 수락 서신 확인”으로 보완한다. 이 판정일을 앞선 사실상 분리 또는 단일 entity 창립일로 자동 입력하지 않는다.

[Zanzibar Act 1963 §1](https://www.legislation.gov.uk/ukpga/1963/55/pdfs/ukpga_19630055_en.pdf)의 1963-12-10 보호관계 종료·독립과 12-03 법률 제정은 구별한다. [Tanzania Act 1969 §§1(2), 2(6)](https://www.legislation.gov.uk/ukpga/1969/29/pdfs/ukpga_19690029_en.pdf)의 1964-04-26 기준일도 기존 보고와 부합한다. 1963년을 19세기 술탄국의 최초 건국일로 삼지 않으며 1890 보호협정 효력, 1964 혁명 전후 국가 동일성은 보류한다.

### 마다가스카르

[FRUS 1896 문서90의 당대 외교보고·조약 번역](https://history.state.gov/historicaldocuments/frus1896/d90)은 **1895-10-01 서명**을 직접 기록한다. §1 보호관계, §3 대외관계, §§2·4 여왕과 궁정의 존속을 분리한다. “원조약 미확인”은 “당대 외교문서에 수록된 영문 번역과 서명일 확인, 비준·발효·후속 변경 별도 검증”으로 보완한다. 같은 문서의 1885-12-17 선행 조약도 구별하며 보호관계의 역사를 1895년부터라고 단정하지 않는다.

[FRUS 문서107](https://history.state.gov/historicaldocuments/frus1896/d107)은 **1896-08-06 공포, 08-08 프랑스 관보 게재**와 식민지 선언을 수록한다. 현지 시행 및 관세 조치도 별도다. 식민지 선언과 왕정 폐지를 합치지 않는다. 1897-02-27/28 폐위·왕정 폐지의 정확한 원명령과 국가 법적 연속성은 계속 보류한다.

### 다호메이

[ICJ에 제출된 니제르의 2003년 준비서면, 인쇄 p.38 §1.2.9](https://icj-web.leman.un-icc.cloud/sites/default/files/case-related/125/8285.pdf)은 **1892-12-03 보호 선언, 1894-01-15 Agoli-Agbo 임명, 1894-01-29 Dodds와 조약**을 별개 사건으로 기술하고 Hertslet pp.651–652를 인용한다. 이는 **당사국 제출문서이지 ICJ 판결 또는 조약 원본이 아니다**.

[SHD의 전쟁사 설명](https://www.servicehistorique.sga.defense.gouv.fr/en/thematic-topics/conquest-dahomey-1890-1894)의 검색 본문에는 실제로 1895-01-29가 있어 단순 인용 착오로 지우지 않는다. 1894년을 지지하는 근거가 강화됐지만 원법 대조 전 SHD 날짜를 확정 정정하지 않는다. 중요한 보완은 01-15 왕 인정·임명과 01-29 조약, 앞선 보호 선언을 분리하는 것이다. 모든 불일치를 하나의 “보호국 효력일 충돌”로 묶지 않는다. SHD 상세 페이지 시간 초과, 페르피냥 전사 502, 원조약·1900년 폐위 원법령 미확인이라는 한계를 유지한다.

## 3. TIME021 — 의회 회기와 문서 날짜를 분리

**확정 정정:** [의회 회의기록 PDF p.14](https://www3.congreso.gob.pe/Docs/legislativo/TemasTratados/files/22_ctt_11.jun.2025.pdf)과 [PCM 설명](https://www.gob.pe/institucion/pcm/noticias/1195200-pcm-demarcacion-territorial-en-lo-que-va-del-ano-beneficia-a-mas-de-2-5-millones-de-peruanos-y-fortalece-la-presencia-del-estado)은 법안11278의 **6월11일 회기 승인**을 기록한다. 회의는 6월12일 00:14에 끝나므로 정확한 표결 시각 없이 달력 날짜를 확정하지 않는다. 원본의 “6월12일 통과”는 “6월11일 회기에서 승인; 6월12일 의회 문서일”로 보완한다. 외교부가 6월12일이라고 쓴 것은 그 출처의 표현으로 남긴다. [법률32403](https://busquedas.elperuano.pe/dispositivo/NL/2415565-1)의 7월2일 대통령 서명과 7월3일 관보 게재는 유지한다.

[콜롬비아 8월5일 성명](https://cancilleria.gov.co/node/30985)과 [페루 공식 입장 재록](https://www.elperuano.pe/noticia/276140-peru-expresa-protesta-por-declaraciones-de-colombia-sobre-integridad-territorial)은 상반된 권원 주장을 입증한다. 국내 지구 신설이나 주권 주장은 양자 국경 변경이 아니다. [9월11–12일 COMPERIF 공동성명](https://www.cancilleria.gov.co/en/node/31174)에 새 국경 좌표·양도·최종 귀속 결정이 **공표되지 않았음**을 확인했다. 어디에도 결정이 존재하지 않는다는 전수 부재 주장으로 확대하지 않는다.

SERFOR 지구 서비스의 2024년 참고 센서스 경계·Polygon·EPSG:4326, SENACE 서비스명의 2025와 설명문의 INEI 2020-06 차이는 메타데이터에서 재확인했다. 원시 피처의 역사적 유효기간·사용권·형상 검증은 아니다. 국가 국경 반영은 보류하며 법적 지구와 국제국경을 같은 레이어로 처리하지 않는다. 중요 정착지·도서 예외는 이 짧은 검토를 뒷받침할 뿐 세밀한 섬·하천 복원을 승인하지 않는다. 미확인 변경 면적은 500km² 통과나 자동 제외로 판정하지 않는다.

## 4. 검증 묶음 6개 — 이미 처리한 변경과 미적용 후보

- [소규모 폴리곤 정리](https://github.com/kimjeon-il/PandoLab-library-data/blob/68c9a1fa23dd3272c5822697cfbeffc3e537265a/reports/borders/validation/sub500-polygon-retirement-2026-11-04/README.md), [한반도 LSIB 복원](https://github.com/kimjeon-il/PandoLab-library-data/blob/68c9a1fa23dd3272c5822697cfbeffc3e537265a/reports/borders/validation/korean-lsib-baseline-rollback-2026-11-04/README.md), [표시 검토 게이트](https://github.com/kimjeon-il/PandoLab-library-data/blob/68c9a1fa23dd3272c5822697cfbeffc3e537265a/reports/borders/validation/historical-display-review-gate-2026-11-04/README.md)는 현재 work/gis의 선행 커밋이다. 자료 `89bff9a4`·`30ce140b`, 앱 `9f9058f7`·`3b3339df`의 반영을 다시 실행하지 않는다. 과거 보고서의 채택 상태보다 최신 원격과 후속 복원을 우선한다.
- [LSIB 좌표 감사](https://github.com/kimjeon-il/PandoLab-library-data/blob/68c9a1fa23dd3272c5822697cfbeffc3e537265a/reports/borders/validation/current-lsib-coordinate-audit-2026-11-04/README.md)는 이미 복원 전 표본임을 명시한다. [Atrek 범위 정정](https://github.com/kimjeon-il/PandoLab-library-data/blob/68c9a1fa23dd3272c5822697cfbeffc3e537265a/reports/borders/validation/current-border-detail-lsib-2026-11-04/ATREK-SCOPE-CORRECTION.md)도 17점/36.292km 부분 표본과 140점/100.056km 승인선 전체를 구별한다. 299km 외삽을 다시 사용하지 않는다.
- [역사 상세 검토](https://github.com/kimjeon-il/PandoLab-library-data/blob/68c9a1fa23dd3272c5822697cfbeffc3e537265a/reports/borders/validation/historical-border-detail-review-2026-11-04/README.md)의 동부·라트비아·폴란드·Atrek 관련 5개 국가 후보는 productionActivated=false이며 운영 반영되지 않았다. 자료 `a548d5fa`→`c1d25c3f` Git 차이는 archive index와 새 blob뿐이다. 준비·검토 영수증을 runtime 활성화로 오인하지 않는다.
- Darja는 겹침 총면적이 같더라도 독립 겹침 형상 차이가 남은 기존 보류, 프로이센은 별도 보류를 유지한다. 이 검토에서 새로운 기술적 결함을 재현했다고 주장하지 않는다. 보고서 안의 구현·반영 제안을 실행 권한으로 해석하지 않는다.
- work/gis의 500km² 종료 원장 S01–S24와 갱신된 106행 커버리지·요약을 대조했다. 11개 CSV 행은 역사 사건·날짜를 바꾸지 않고 연구 상태만 종료로 변경했다. 이미 종료된 G/H·미세 교환 연구는 새 자료가 있다는 이유로 재개하지 않는다. 큰 사건·국가 존재·미확정 면적은 임의로 소규모 종료에 포함하지 않는다.

## 5. 현행 객체와 반영 판단

work/gis library.json의 286개 ID와 아래 6개 객체 원문을 읽었다. TZA=1964-04-26, MDG=1960-06-26, BEN=1960-08-01, PER=1838-08-25, COL=1831-11-21, BRA=1822-09-07이며 모두 validTo=null이다. 이는 관측한 현행값이지 이번에 승인한 새 역사 판단이 아니다. 각각 Natural Earth 5.1.1 geometry version의 validFrom/validTo는 null이다.

잔지바르·다호메이·메리나·산타로사·치네리아에 해당하는 ID 문자열은 이 색인에서 찾지 못했다. 이름·법적 동일성 전체 감사를 완료한 뜻은 아니다. 현대 TZA/MDG/BEN에 과거 왕국 생애를 덮어쓰거나 새 날짜로 PER/COL/BRA 국경을 바꾸지 않는다. 조사 하한 1801년을 건국일로 입력하지 않는다. 확정된 문헌 사건 날짜와 국가 lifetime·geometry 유효기간은 독립적으로 유지한다.

## 6. 실제 검사와 범위

- 이번 변경은 이 보충 정정 README, evidence.json 및 reports/README.md의 색인 한 행뿐이다. 현재 데이터·원자료·runtime·library.json·앱 pin·코드 변경은 0건이다.
- 실행: 양 저장소·양 브랜치 Git tree와 원문/blob·변경 이력 비교, 공식 문헌·당대 외교문서·의회 기록과 서비스 메타데이터 검토, 6개 현행 객체 JSON 확인, 보고서 JSON·링크·쓰기 경로·변경 범위 검사.
- 미실행: 새 GIS 형상·측량·위상·중첩·화면 검증, 원본 벡터 다운로드, 제품/전체 테스트와 재생성. 이전 검증 수치는 당시 기록으로만 인용한다.
- 로컬의 등록된 work/gis 워크트리 경로는 현재 존재하지 않았다. 원격 커넥터에서 기존 tree 기반 단일 부모 커밋과 expected-head 검사, force=false로 이 보고서 범위만 기록한다. 다른 로컬 작업·브랜치는 건드리지 않는다.
- main을 게시 대상으로 삼는 publish-reports/check-reports helper는 이번 사용자의 main 변경 금지에 따라 실행하지 않는다. helper 성공으로 표현하지 않고 원격 커밋과 세 파일의 바이트 일치를 별도 확인한다.
- main 수정·병합·배포·포터블·무명 강/호수 조사는 하지 않는다. 로컬 임시 산출물은 생성하지 않았다.
