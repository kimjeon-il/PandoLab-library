# GIS 보고서 자동 검토 — 2026-11-05 22:00 UTC

> ID: GEO-REVIEW-20261105-2200 · 상태: reviewed / supplemental-corrections / important-holds · 지도 반영: report-only / runtime-unchanged

## 검토 범위와 중복 방지
Pando main `7cd224bd198c014d2215e35a93452702227d8314`, work/gis `a4f2f7f8a72e25b36b3ba5388c18cd8c2e2f8b04`; 자료 main `0ed277208a52fcda77d5777f1622e5272c08dadf`, work/gis `887f72186fda9596502a35631d0a3376d9b4a1f1` 기준이다. 직전 검토 `8beb97cca9992ae2099ab0ce19dca4d62f10961a`의 main 기준 `68c9a1fa23dd3272c5822697cfbeffc3e537265a` 이후 보고서 blob을 비교했다. Pando 양 브랜치 reports 파일은 0개다. 외부 자료 reports/README.md와 최신 borders 위치를 따르며 legacy geography도 tree 비교에 포함했다.

자료 main 보고서 하위 파일 100개 추가·수정(국경 82, 무관한 개발 18), work/gis 36개 추가·수정, 삭제는 각각 0개다. 파일별 원본 blob은 [evidence.json](evidence.json)에 보존한다. 새 역사 본문은 LIFE025, TIME022 두 개이며 각 진행기록·색인 변경을 대조했다. 기존 LIFE024/TIME021과 앞선 보류 본문은 동일 blob이므로 재반영하지 않는다. main에만 있는 두 새 본문도 실제 검토했다.

원본:
- [LIFE025 / cb78b674](https://github.com/kimjeon-il/PandoLab-library-data/blob/cb78b674aae8504fd6237a10603bd830feadc9b6/reports/borders/history/lifetimes/country-lifetime-north-america-historic-west-florida-confederacy-federation-1921-2026-11-06.md)
- [TIME022 / 0ed27720](https://github.com/kimjeon-il/PandoLab-library-data/blob/0ed277208a52fcda77d5777f1622e5272c08dadf/reports/borders/history/timeline/historical-timeline-2025-oceania-vanuatu-maritime-shelf-2026-11-06.md)

11/6 파일명은 한국 시각 기록이다. 아래 보충판만 work/gis에 기록하며 main 원문은 바꾸지 않는다.

## LIFE025 보충 정정안
**1921 중미 연방:** [FRUS 1921 I 문서124](https://history.state.gov/historicaldocuments/frus1921v01/d124)는 온두라스 외무장관의 1921-06-16 서한이다. 제3 비준서 기탁이 **1921-05-12** 이루어져 협약 제18조에 따라 발효했다고 보고하며, 임시 연방평의회 설치는 **06-13**으로 구별한다. 원본의 국내 비준·평의회·헌법 날짜 사이에 이 별도 법적 사건을 추가한다. 06-16은 서한일, 07-18은 미국 수신일이며 발효일이 아니다. 협약 원문·기탁증서 자체를 열람한 것은 아니므로 당대 공식 외교서한에 의한 확인으로 표시한다. 헌법 10-01 발효와 연방의 단일 국가 lifetime 시작을 자동으로 같게 하지 않는다.

**미국 남부연합:** [NPS 연표](https://home.nps.gov/apco/learn/historyculture/surrender-events-after-appomattox.htm)는 **1865-05-05 내각 해산**을 명시한다. 원본의 05-10 데이비스 체포와 분리하여 정부 소멸 판단에 필요한 사건으로 보완한다. 04-09 군 항복, 05-05 정부 해산, 05-10 체포, 후속 군 항복은 동일 사건이 아니다. NPS의 역사 해설은 법적 국가 동일성의 최종 판결이나 해산 원법령이 아니며 하나의 validTo를 임의 입력하지 않는다.

**서플로리다 날짜 정정 후보:** [Claiborne 서한집 권5 pp.46–50, 53–56의 OCR](https://archive.org/stream/officialletterbo05claiiala/officialletterbo05claiiala_djvu.txt)은 12월7일 서한에서 Holmes의 전날 방문과 Claiborne·미군의 당일 도착 및 국기 게양을 구분한다. 따라서 원본의 “1810-12-06 미군 세인트프랜시스빌 진주”를 단일 확정일로 재사용하지 않고 **12-06 Holmes 방문 / 12-07 권한 인수**로 대조한다. 12-10 배턴루지 점유는 12-12 서한으로 확인된다. 원스캔 이미지 판독은 남아 있으므로 보충 근거·정정 후보로 기록한다.

[남부연합 헌법 제7조](https://avalon.law.yale.edu/19th_century/csa_csa.asp)의 비준·선거·새 의회 소집 및 그때까지 임시의회 존속을 구별한다. 1861-03-11 상설헌법 채택이 즉시 상설정부 전환 완료를 뜻하지 않는다. [FRUS d133](https://history.state.gov/historicaldocuments/frus1921v01/d133) 1921-10-06 승인 요청과 [d142](https://history.state.gov/historicaldocuments/frus1921v01/d142) 12-23 미국의 승인 논의 유보는 미국 관계에 한정한 근거다. 1922-01-29 중앙기구 종료와 02-07 온두라스 탈퇴의 관계는 원회의록·관보·효력조항 미대조로 보류한다. HathiTrust 관보 접근 실패를 원문 확인으로 대체하지 않는다.

서플로리다의 선언·미국 점유명령·실제 점유와 권원, 남부연합의 국가 동일성·종료 기준, 중미 연방의 국가성·1922 종료일 및 구성국 연속성은 구체적 보류다. 현대 USA/GTM/HND/SLV lifetime을 과거 정치체 날짜로 덮어쓰지 않는다. 1801 조사 하한을 건국일로 입력하지 않는다.

## TIME022 — 협상·제출을 영토변경으로 변환하지 않음
[프랑스 대통령실 2025-07-23 공동성명](https://www.elysee.fr/en/emmanuel-macron/2025/07/23/joint-communique-from-vanuatu-and-france-on-their-commitment-to-maritime-delimitation)은 매슈·헌터 섬 주권과 해양경계의 미해결 쟁점을 협상하도록 지시한다. 확정 양도나 경계좌표를 발표한 문서가 아니다. [피지 외교부 09-09 발표](https://www.foreignaffairs.gov.fj/fiji-vanuatu-progress-maritime-boundary-delimitation-work/)는 09-04~05 협상과 결과문서 서명을 기록하지만 최종 획정조약·좌표·효력일을 제공하지 않는다. 이 두 문서를 다시 직접 읽었으며 기존 보류 판단을 유지한다.

[피지 외교부 07-10 발표](https://www.foreignaffairs.gov.fj/fiji-deposits-extended-continental-shelf-claim-submissions-to-the-united-nations-un/)의 세 건 제출과 향후 CLCS 검토·권고를 확인했다. 해저·하층토에 대한 권리와 육지 영토주권을 분리한다. 이번 UN No.96 직접 열람은 403으로 실패했으므로 개별 07-08/09 날짜를 새로 원문 검증했다고 주장하지 않는다. 원본의 날짜는 출처 표기가 있는 기존 관측으로 유지한다. 453,400km² 주장 규모를 실제 영토 이전 면적으로 사용하지 않는다. 제출·협상만으로 VUT/FJI/NCL/FRA 경계나 lifetime을 변경하지 않는다. 원본 벡터·권리·효력기간·객체 매핑은 계속 미확인이다.

## 기존 적용과 최신 상태
work/gis의 Soviet592 적용 기록은 선행 앱 `3be531e2`와 자료 `bd62cc8e`로 처리된 결과다. East592, Latvia163, Poland671와 기존 Pripyat 연결, protected Atrek, Darja387을 다시 생성·등록하지 않는다. 기존 정량·화면 검증은 해당 당시 증거이지 이번에 재실행한 검증이 아니다.

main의 1914-country-activation 묶음은 앞선 단일 날짜 등록과 후속 문제 조사를 함께 보존한다. 최신 work/gis의 1914-representative-periods 보고서와 앱 `a4f2f7f8`의 자료 pin `887f7218`을 우선한다. DEU 대표형상은 1871-01-01~1918-11-08, 오스트리아-헝가리는 1867-02-17~1918-10-30, 세르비아 왕국은 1882-03-06~1918-11-30의 양끝 포함 구간이다. DEU lifetime 1867-07-01~null과 형상 기간은 별개다. **1914 기준 대표형상을 잠정 확장한 것으로 전 기간 국경 불변이 검증된 뜻이 아니다.** 이 작업은 이미 반영됐으므로 단일 날짜로 되돌리거나 재등록하지 않는다. 인접국 clipping·원본 형상 변경·날짜별 새 복원은 수행하지 않는다.

후속 reference-path-investigation의 기준일 UI·소련 검토형상 그대로 재사용 제안과 로컬 중단 파일은 공개 구현이 아니다. 검토 형상의 정점 순서 차이에 관한 진단이 검토 영수증 재사용 또는 게이트 완화 승인은 아니다. ci-follow-up은 1914-07-31 프로이센 부모관계 수정으로 앞선 “compiled 불변” 설명을 보완한다. 해당 날짜 관계 수정과 후기 전체 기간 형상 재사용을 혼동하지 않는다.

## 현행 객체와 실제 검사
work/gis의 USA, GTM, HND, SLV, VUT, FJI, NCL 객체 7개를 직접 읽었다. 관측 lifetime 시작은 각각 1776-07-04, 1839-04-17, 1838-10-26, 1841-02-02, 1980-07-30, 1970-10-10, 1853-09-24이며 끝은 null이다. NCL parent는 FRA다. 이 값은 관측값이지 이번 승인한 역사 판단이 아니다. 해당 NE 지오메트리 기간은 null이다. 색인에 west-florida/confederacy/central 문자열의 대상 ID는 없었지만 이것을 완전한 동일성 감사로 표현하지 않는다.

실행: 양 저장소·브랜치 원격 이력/보고서 blob 비교, 신규 본문과 상태·출처 검토, 공식 웹 문헌 대조, 해당 7개 객체 읽기, 보고서 JSON·변경 경로 검토. 미실행: GIS 재생성, 형상·위상·화면·전역 검증, 제품 전체 테스트. runtime·library.json·앱 pin 변경 0건.

등록된 work/gis 로컬 worktree가 존재하지 않아 원격 커넥터의 기존 tree 기반 단일 부모 커밋으로 이 보고서와 색인만 저장한다. expected-head 및 force=false로 동시 변경을 보존한다. main 게시 helper는 사용자의 main 변경 금지 때문에 실행하지 않는다. 원격 파일 재조회로 별도 검증하며 helper 통과라고 표시하지 않는다. main 수정·병합·배포·포터블·중단된 무명 강/호수 조사는 하지 않는다.
