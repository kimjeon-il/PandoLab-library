# GEO-REVIEW-20261025-2200 — 국가·시대별 보고서 자동 검토

> 회차: 2026-10-25 22:00 UTC · 검토: 2026-10-25 UTC / 10-26 KST
> 상태: reviewed / report-corrections-proposed / runtime-not-changed
> 신규 연구 2건, 이전 검토 7건의 원본 blob과 오늘 적용 이력을 대조했다.
> 원본 커밋·판본·현행 대상 기간: [evidence.json](evidence.json).

## 기준·중복 방지

앱 work/gis `9a53595508e3798e37326803d7545f2e44eca8ad`, pin과 자료 work/gis `63aebba20cf60cad314022c8aeb24c87922ceb6d`.
이전 자동 검토는 자료 `c0d5fc6751d1fc9801b16b3fbc62d653ae290147`.
최신 연구 원문은 자료 main `2529e6f99ff696a24b6148743bf21436068bc6b3`의
`reports/borders/history/{lifetimes,timeline}/`이다.
work/gis의 geography는 구판 보존본이다. 최신 주제 색인을 읽되 원문 main은 수정하지 않았다.

이전 LIFE-009/010/011/012/013, TIME-009/010은 이전 검토의 blob과 모두 동일했다.
새 근거 없는 보류를 재승격하거나 연구 커서를 이동하지 않았다.
오늘 USSR 성립일(9d3ca74c), 드네스트르(1879138b), 유럽 외곽(1d0c9169),
66개 기간(e6b41735/앱45f1a532), 34개 기간(앱50533bb8→자료b0d73723)은
이미 반영된 별도 작업이다. 재적용하지 않았다.
Atrek·몽골 보관(c7f66909)은 후보 보존이며 날짜·데이텀·최신 형상 정합 미해결 상태를 유지한다.
현행 수동 남부 국경 재작성은 이번 자동화로 가져오거나 적용하지 않았다.

## LIFE-014 — 현행 자료와 보고서 전제 충돌

원문: [아르헨티나·볼리비아 2차](https://github.com/kimjeon-il/PandoLab-library-data/blob/2529e6f99ff696a24b6148743bf21436068bc6b3/reports/borders/history/lifetimes/country-lifetime-south-america-arg-bol-phase2-2026-10-26.md), 추가 커밋 `f832c248`.

원문이 읽은 main은 ARG/BOL 기간 공란이지만, 실제 이번 pin에는
**ARG=1831-01-04, BOL=1825-08-06**이 이미 있다. 두 객체의 현대 Natural Earth
형상 기간은 양끝 null이다. 이 차이를 공란 오류나 새 역사 형상 검증으로 해석하지 않는다.
새 보고서만 보고 현행 값을 삭제·교체하지 않는다.

확인된 문헌 정밀화:
- [Infoleg 1853 원문](https://www.infoleg.gob.ar/?page_id=3873)의 제35조는 하원 인구조사 조항이다. 현행 국명 병기 조항을 1853 원문 제35조라고 부르면 안 된다.
- [상원 PDF](https://www.senado.gob.ar/bundles/senadoparlamentario/pdf/institucional/constitucionNac1853.pdf)는 1992 인쇄 및 1860 등 개정을 반영한 합본이다. 파일명1853을 순수 원판본으로 해석하지 않는다.
- [공식 국명 설명](https://www.argentina.gob.ar/pais/territorio/denominacion)은 1860-10-08 행정상 국명 통일을 설명하지만 그것만으로 국가 재창설을 뜻하지 않는다. 공식 개요도 1853/후대 조문을 혼용하므로 법문 판본을 우선 구분한다.
- [볼리비아 박물관 공개 전사](https://casadelalibertad.org.bo/wp-content/uploads/2017/08/ACTA-DE-LA-INDEPENDENCIA.pdf)는 1825-08-06 독립 주권 선언을 뒷받침한다. 08-08 의결, 08-11 법령, 10-03 명칭 사용은 별도 사건이다.

수정안: 선행 LIFE-001의 국명 제35조 출처를 “1853 제정 후 개정을 반영한 헌법”으로 명시.
LIFE-014의 “현재 공란”은 읽은 main 판본의 관찰로 한정하고 위 work/gis 기간 충돌을 함께 표시한다.
ARG의 1816 연합주–1831 연방–1853/1860 통합 간 동일성, BOL의 연합기 계속성과 법령 효력은
이번 문헌만으로 단일 필드 변경을 확정하지 않는다. **현행 lifetime·형상 보존**.
1801년 조사 하한을 건국일 또는 형상 유효 시작일로 입력하지 않는다.

## TIME-011 — 협정 날짜·안보 표현 수정안

원문: [오세아니아 2025](https://github.com/kimjeon-il/PandoLab-library-data/blob/2529e6f99ff696a24b6148743bf21436068bc6b3/reports/borders/history/timeline/historical-timeline-2025-oceania-bougainville-cook-islands-2026-10-26.md).
추가 `d5a70f52`, 정정 `834b0752/2529e6f9`를 구분하여 최신판만 검토했다.

1. **부건빌:** [PA-X 공개 PDF](https://www.peaceagreements.org/media/documents/PG_250626_Melanesian_Agreement.pdf)의 1.1·1.5·2.2·2.3조는 PNG 의회 결정과 후속 절차를 남긴다.
공개본문 승인 표기는 **2025-06-26**이나 [PNG 총리실 6/27 발표](https://www.pmnec.gov.pg/pm-marape-and-president-toroama-sign-melanesian-agreement-affirming-commitment-to-bougainville-peace-process/)는 당일 서명으로 서술한다.
PDF는 ABG 공식 웹페이지의 2025-07-30 인쇄본이지 자필서명 원본 스캔이 아니다.
따라서 “서명문 원본 확인”이 아니라 **공개본문 승인일과 발표 서술 사이 차이가 있으며 자필서명본 미확보**로 기록한다.
어느 날짜도 독립·국제경계 효력일로 입력하지 않는다.

2. **쿡 제도:** [행동계획 공식 PDF](https://mfai.gov.ck/wp-content/uploads/mfai-migration/documents/6b8cd3e63b8b_2025-2030_-_Action_Plan_for_Strategic_Partnership_0.pdf) 6쪽에는 일반 다자 안보·비확산·사이버범죄 협력이 있다.
따라서 “안보·국방 조항 없음”은 과도하다.
**수정 문구:** “6/18 외무부는 별도 안보·국방 arrangements가 없다고 설명했다.
계획에는 일반 다자 안보협력 문구가 있으나 자유연합 종료 조항은 확인되지 않았다.”
[6/18 외무부](https://mfai.gov.ck/2025/06/statement-ministry-foreign-affairs-and-immigration-cook-islands-position-regarding-new/)의 비구속적 성격·자유연합 계속 설명과 실제 문구를 구분한다.
PDF 텍스트 서명란에 날짜가 없어 공표일로 실제 서명일을 대체하지 않는다.

원문의 “두 PDF 본문 미열람” 제한은 이번 검토에서 **공개 PDF 텍스트 열람**까지 해소했다.
자필서명본·파일 해시·페이지 화면 검증은 하지 않았다.
PNG·COK의 현행 기간은 각각1975-09-16/1965-08-04이며 새2025국가나 부건빌 주권 객체를 만들지 않는다.
2019 ADM1이나 현대 참조선을 2025 신규 국제경계로 승격하지 않는다.

## 처리·검증·저장 범위

- 변경안은 위 문헌 표현 및 판본/현행 충돌 주석이다. **확인된 국가·형상 데이터 수정 0건**.
- 공식 커넥터로 원격 커밋·blob·색인 및 대상 7객체(ARG/BOL/PNG/COK/발트3국)만 읽었다.
발트3국의 기존 충돌은 새 근거가 없고 날짜도 기존1990/1991 그대로여서 보류 유지.
- 이전 검토 이후 work/gis의 geography 본문 변경0, 새 경계보고서4묶음은 앞서 적용/후보보존된 작업임을 확인했다.
새2연구 외 기존7문서는 동일 blob이라 재조사 완료로 세지 않는다.
- GIS 생성·형상/위상·렌더러·웹앱·전세계 검사 미실행. 이번은 문헌/보고서 검토이며 미실행을 통과라고 하지 않는다.
- 기존 상설 GIS worktree는 이 환경에서 경로가 없고 prunable 표기다. 다른 브랜치 checkout을 사용하거나 새 작업공간/채팅을 만들지 않고 공식 원격 API로 처리했다.
- 저장은 이 README·evidence.json, work/gis reports/README 색인1행, archive/index 해당 항목뿐.
모든 비보고서 자료·원문·앱 pin·연구 커서·타브랜치를 보존한다.
- main을 쓰는 --publish-reports는 명시적 work/gis 한정 지시로 실행하지 않는다.
원격 work/gis의 부모·선택 파일 바이트·변경 범위를 확인한 뒤 커밋을 보고한다.

