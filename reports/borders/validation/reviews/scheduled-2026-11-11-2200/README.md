# 양 브랜치 GIS 검토 — 시킴 소급효력·예멘 조약 계속성·2025 사건 범위

> GEO-REVIEW-20261111-2200 · 2026-11-11 22:00 UTC 실행 · reviewed / supplemental-corrections / important-holds · report-only / runtime-unchanged

## 범위와 중복 방지

Pando main/work/gis `87763ec1c231484c2d3787f49056f3f9f918a97d`, 외부 자료 main `233b0f5ecdc92400862f24dfaf1f86477d34c065`, work/gis `229a7f0afc9ddb9da2c56d9ab531ea07cc391b34`를 읽었다. 직전 [11월8일 검토](../scheduled-2026-11-08-2200/README.md)의 main `65a4c70c`와 검토 커밋 `5d56ba42`의 보고서 blob을 대조했다. 양쪽의 완전한 reports 트리(truncated=false)를 이용했으며 compare API의 파일 수 제한을 전수 목록으로 취급하지 않았다.

신규/변경 main 보고서·첨부 1,435개를 경로/blob로 분류했다. 역사 원문 6개, 역사 진행기록 2개, 색인 2개, 현대/역사 형상 검증 첨부 1,284개, 개발·렌더링 첨부 141개다. 첨부 전부를 재실행·시각 검증했다는 뜻은 아니다. 역사 원문 6개와 진행기록, 관련 형상 검토 서술 23개를 읽었고 원문 이력과 판정은 evidence.json에 기록했다. 코드 저장소 루트에 reports는 없으며 현행 AGENTS와 branch-policy가 지정한 외부 reports/borders를 따른다. 폐기된 reports/geography를 다시 만들지 않는다.

LIFE031과 TIME028은 main에만 있으며 실제로 읽고 검토했다. 나머지 역사 원문 4개는 두 자료 브랜치의 blob이 같다. main 보고서의 부재를 work/gis의 '새 자료 없음'으로 오인하지 않았다. main과 work/gis 사이 진행 커서를 통째로 복사하거나 이전 조사의 완료 수를 늘리지 않는다.

### 검토한 국가·시대 원문

- [country-lifetime-africa-gha-nam-uga-2026-11-11.md](https://github.com/kimjeon-il/PandoLab-library-data/blob/56ace92d61b4caad58d90d0e208b4a01d37d8a51/reports/borders/history/lifetimes/country-lifetime-africa-gha-nam-uga-2026-11-11.md) · 원문 56ace92d · blob 848a670c
- [country-lifetime-asia-historic-sikkim-north-south-yemen-2026-11-10.md](https://github.com/kimjeon-il/PandoLab-library-data/blob/a1a4e2136fbb231811c6c3cdcf85287a783bbfed/reports/borders/history/lifetimes/country-lifetime-asia-historic-sikkim-north-south-yemen-2026-11-10.md) · 원문 a1a4e213 · blob 459a0230
- [country-lifetime-north-america-blz-jam-pan-2026-11-12.md](https://github.com/kimjeon-il/PandoLab-library-data/blob/5440aff540c18334e18c49b8e49e867e1ad8feb7/reports/borders/history/lifetimes/country-lifetime-north-america-blz-jam-pan-2026-11-12.md) · 원문 5440aff5 · blob 9f980da9 · main에만 존재
- [historical-timeline-2025-north-america-haiti-kenscoff-2026-11-10.md](https://github.com/kimjeon-il/PandoLab-library-data/blob/77ddcbaeedf711f9038ef325966812102bf9338a/reports/borders/history/timeline/historical-timeline-2025-north-america-haiti-kenscoff-2026-11-10.md) · 원문 77ddcbae · blob fb95d970
- [historical-timeline-2025-oceania-fsm-palau-marshall-maritime-treaty-amendments-2026-11-12.md](https://github.com/kimjeon-il/PandoLab-library-data/blob/5ed850ba9e482c9279f3a8d81743e5e8dd14071f/reports/borders/history/timeline/historical-timeline-2025-oceania-fsm-palau-marshall-maritime-treaty-amendments-2026-11-12.md) · 원문 5ed850ba · blob 6966fdb2 · main에만 존재
- [historical-timeline-2025-south-america-paraguay-bolivia-rio-negro-demarcation-2026-11-11.md](https://github.com/kimjeon-il/PandoLab-library-data/blob/5541047dca60bcb1a7cfac6f2b208ff91e8a5b19/reports/borders/history/timeline/historical-timeline-2025-south-america-paraguay-bolivia-rio-negro-demarcation-2026-11-11.md) · 원문 5541047d · blob 72e4185c

## 확정된 보충 정정

### LIFE029: 시킴의 재가일과 소급효력

[인도 법무부 제36차 개정법](https://www.legislative.gov.in/static/uploads/2025/07/2a875dab390ddae1419f7f050ccd6ed0.pdf) 제1조 제2항은 연방상원 통과일로 소급 시행하도록 한다. 원법 PDF 해당 페이지 화면을 확인했다. [2025 공식 헌법 통합본](https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2025/08/202508081113544342.pdf)의 제2A조 및 371F 각주는 효력일을 **1975-04-26**으로 명시한다. 통합본은 텍스트 확인이며 화면 조회는 실패했다. [인도 감사원 시킴 연혁](https://www.cag.gov.in/ag/sikkim/en/page-ag-sikkim-history)도 4월26일을 기록한다.

따라서 원문의 '4월26일 효력 자료와 소급효력의 불일치 미확인' 보류는 **공식 통합본상 4월26일 소급효력 확인, 5월16일 재가와 구별; 당일 상원 원회의록 미확인**으로 좁힌다. 이는 시킴 별도 객체의 국제법상 국가성·종료 기준을 확정하지 않으며, IND lifetime이나 지오메트리의 유효기간을 덮어쓰지 않는다.

### LIFE029: 예멘의 조약 계속성

[UN Treaty Collection Historical Information](https://treaties.un.org/pages/historicalinfo.aspx)의 Yemen 본문은 1990-05-19 양국 외무장관 통지, 5월22일 단일 주권국 형성 및 기존 유효 조약·국제관계의 계속을 설명한다. UN 기탁표의 참가일은 두 전신 중 앞선 참가일을 따른다. 이 **UN 기탁 조약 처리의 계속성**은 확인된 부분이므로 전체 승계가 미확인이라는 보류를 그 범위만 보완한다. 국내 통일법 원문, 국가 동일성 모델과 별도 역사 객체 ID는 계속 보류한다. 유엔 회원국 가입일·조약 참가일을 국가 건국일로 혼동하거나 YEM의 1990-05-22를 1947/1962년으로 소급하지 않는다.

과거 원문과 근거는 그대로 두고 본 보충 검토를 후속 판정으로 연결한다. 기존 검사 결과나 날짜를 새 검증값처럼 다시 쓰지 않는다.

## 다른 역사 보고서 판정과 구체적 보류

- **LIFE030/031:** GHA 1957-03-06, NAM 1990-03-21, UGA 1962-10-09, BLZ 1981-09-21, JAM 1962-08-06, PAN 1903-11-03은 읽은 현행 generated 색인 값과 원문 독립일이 일치한다. 새 입력 0건. 가나 Hansard, 남아공 법률 §4, 미국 역사국의 벨리즈·자메이카·파나마 및 1903-11-04 당대 전보를 재확인했다. 우간다 법률은 검색 본문 확인이나 직접 페이지가 JavaScript 검증으로 막혔고, 벨리즈 PDF 용량·자메이카 XHTML 형식 제한이 남았다. 기존 각국 전체 법적 계속성·헌법 부칙·영토 귀속 검증은 완료로 승격하지 않는다.
- **TIME026:** [UN Haiti 2025-04-07](https://haiti.un.org/en/292260-least-262-people-killed-over-two-months-brutal-attacks-kenscoff-heights-port-au-prince)의 본문은 1월27일 공격 시작과 3월24~27일 후속 공격을 확인한다. [VBI 8월25일 기사](https://vantbefinfo.com/securite-la-pnh-et-la-mmss-reprennent-le-controle-du-site-teleco-a-kenscoff/)는 Téléco 시설 재장악을 서술하되 경찰·지원군 발표에 의존한다. 국지적 통제와 코뮌 전체, 국제국경을 구별한 원문 판정 유지. 시설별 최초 점거일·독립 공간 경계가 없으므로 HTI 형상·lifetime 변경 없음.
- **TIME027:** [파라과이 2025-10-15](https://www.mre.gov.py/paraguay-y-bolivia-a-punto-de-finalizar-la-demarcacion-total-de-los-limites/)의 잔여3.5km, [볼리비아 2026-09-16](https://cancilleria.gob.bo/mre/2026/09/16/26279/)의 2025년46.5km/2026년 잔여3.5km 처리 및 755.67km, [파라과이 최종 승인 발표](https://www.mre.gov.py/paraguay-y-bolivia-aprueban-la-demarcacion-final-de-su-frontera-comun/)의 742km를 직접 확인했다. 측량·표지와 법적 영토 양도를 구별한 판정 유지. 승인 원도·좌표·효력 조항·거리 차이의 기준이 없으므로 PRY/BOL/BRA 공유경계를 새로 만들지 않는다. 원문에 있는 추가 상세 도면 연구 권고는 현행 거시적 선별정책을 통과하기 전 자동 실행하지 않는다.
- **TIME028:** [FSM 대통령실](https://gov.fm/president-simina-champions-ocean-governance-stewardship-at-unoc-secures-historic-treaty-signing-to-safeguard-maritime-zones-amid-climate-threats/)의 RMI 6월12일과 [CR24-41 발의안](https://www.cfsm.gov.fm/wp-content/uploads/2025/08/CR-24-41.pdf)의 6월11일 충돌이 재현된다. [의회 색인](https://www.cfsm.gov.fm/24th-resolutions/)에서 두 결의의 9월22일 채택을 확인했다. 다만 색인의 채택본 PDF 링크 C.R-NO.-24-40/41은 이번 조회에서 404다. **발의안 본문 열람과 채택된 최종문 열람을 구별**한다. 날짜 충돌은 임의 선택하지 않고 양자 개정 서명본·상대국 비준·발효와 좌표 변경 여부를 계속 보류한다. 2006년 EEZ 선형을 2025 새 육상/도서 국가 폴리곤으로 복제하지 않는다.

LIFE028의 틸지트·아니프와 기존 THA/미등록 역사 원문 등 보류를 해소하는 새 증거는 이번 검토에서 확인하지 못했다. 1801년을 가상 건국일로 입력하지 않았고 국가 존속·지오메트리 유효기간은 분리했다.

## 형상 검토 기록: 중복 재적용 금지

신규 현대원본·역사재사용 검토 23개 서술을 읽었다. 준비 시점의 not-applied와 후속 APPLICATION/local-application 기록을 구별했다. ARG/CHL의 35개 잔여는 SPI 인터페이스로 분류되어 있으며 단일 LSIB선 적용은 귀속 변경이 된다. IDN의 450개 복원·후속26개 교체 기록은 서로 다른 시점의 누적이며 전체 Papua 분류 완료가 아니다. Arctic의 Kolguyev 및 Novaya/Vaygach 결합 적용 기록은 준비본을 재실행할 이유가 아니다. IRN의 187개 후보는 폐기된 준비 상태이고 실제 source-only 기록은188개 및 Abu Musa 보존이다. SDN의 Red Sea 부분 적용은 완전 SDN+SDS 합집합 승인과 다르다.

현재 별도 담당자가 현대 형상 정본 교체를 실행 중임을 확인했다. 이 자동화는 원격 보고서와 현재 공개된 이력을 검토하며 해당 로컬 archive·pin·잠금·형상에 쓰지 않는다. 과거 원문에 적힌 로컬 적용 커밋을 이번의 신규 적용이나 현재 runtime 완성으로 계산하지 않는다. 단일 국가 전체 교체·부분 경계 갱신·source-only·runtime 반영을 구분하고, 새 해안선·역사적 국경의 독립 정확성은 이번 문헌 검토로 인증하지 않는다. 개별 고유 첨부의 전체 GIS/시각 재검증은 미실행이다.

## 현행 데이터·반영·검증

data work/gis의 generated index blob `d982119a3478199a499aeb8a4058b116a7a83b04`를 실제 파싱해 관련13개 객체만 추출했다. 직접 source/countries 경로는404이므로 원격 source 원문을 읽었다고 주장하지 않는다. generated의 기존 lifetime 확인은 별도 로컬 source 작업의 최신 검증을 대체하지 않는다.

이번 반영은 **본 보충검토, evidence.json, reports/README.md 색인1행의 3파일만**이다. 국가 데이터·타임라인·형상·앱 pin 변경은0건. main의 원문을 병합·체리픽하거나 main·다른 브랜치·배포·포터블을 변경하지 않는다. 저장소 지침의 publish-reports는 main을 쓰므로 이번 명시적 work/gis 한정 지시에 따라 사용하지 않았다. 기존 원격 tree 위 단일 부모 커밋을 생성하고 expected-head, force=false로 게시한다.

실제 검사: 네 브랜치 HEAD, 완전한 reports 트리/blob·원문별 변경 이력, 선택된 현행 기록, 위 문헌, 수정3파일 범위·원격 readback. GIS 재생성/위상·전체테스트·화면 검사는 미실행이다. 로컬 다운로드·캐시·임시복제·worktree 생성 없음.
