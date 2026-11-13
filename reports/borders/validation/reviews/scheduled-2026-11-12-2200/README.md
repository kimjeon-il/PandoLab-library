# 양 브랜치 GIS 검토: 남미 역사 정치체·차시우야르 보류 및 관측 기준 보완

> GEO-REVIEW-20261112-2200 · 요청 실행 2026-11-12 22:00 UTC · 복구 검토 2026-11-13 · reviewed / supplemental-clarification / important-holds · report-only / runtime-unchanged

## 범위와 중복 방지

네 브랜치 HEAD와 원문 경로·blob·변경 커밋은 [evidence.json](evidence.json)에 기록했다. 직전 검토 6259502 이후 work/gis의 borders 트리는 동일하다. 기존 11월12일 회차 검토 디렉터리와 게시 커밋은 발견하지 못했다. main의 이전 검토 기준 233b0f5와 현재 5184244를 비교했으며 borders/data·reconstruction·validation 하위 tree는 동일하다. history/lifetimes와 history/timeline의 완전한 트리 및 원문 변경 이력을 비교했다. 새 국가·시대 보고서는 아래 2건, 진행기록 2건이다. 다른 history 디렉터리는 불변이다. 비교 API 파일 상한을 전수 검토 근거로 사용하지 않았다.

Pando 양 브랜치의 완전한 트리에는 reports가 없으며 외부 자료 저장소의 reports/README.md와 reports/borders/README.md, TEMPLATE.md 및 전용 경로를 따른다. 개발·지형 실험은 이 회차 국가·시대 검토 범위 밖이다. main에만 있는 보고서도 읽었다. LIFE031/TIME028은 이전 6259502 검토와 blob이 같으므로 재적용하지 않는다.

- [LIFE032: 남미 역사 정치체](https://github.com/kimjeon-il/PandoLab-library-data/blob/50b27e32c0874f614d23899e050247b430b64384/reports/borders/history/lifetimes/country-lifetime-south-america-historic-guayaquil-cundinamarca-entre-rios-2026-11-13.md) · 2026-11-12 17:19:30 UTC 원문 커밋.
- [TIME029: 차시우야르](https://github.com/kimjeon-il/PandoLab-library-data/blob/73b6c9d18d21062a67b91c154f2841a94f542a0a/reports/borders/history/timeline/historical-timeline-2025-europe-ukraine-chasiv-yar-control-vector-2026-11-13.md) · 2026-11-12 19:47:50 UTC 원문 커밋.

## LIFE032 검토·수정안

과야킬 시정부 [2024년 연혁](https://guayaquil.gob.ec/guayaquil-celebra-independencia/) 본문에서 1820-10-09 독립과 11-08 대표회의, 1822-07-13 정부 기능 종료와 07-31 편입을 분리한 설명을 재확인했다. 기념 연혁은 원 편입법령이 아니므로 법적 종료일·지역별 실제 지배 범위 보류를 유지한다. 현대 ECU에 이 기간을 덮어쓰지 않는다.

콜롬비아 [국립기록원 헌법 안내](https://www.archivogeneral.gov.co/Constituciones-de-Colombia)에서 1811-03-30 및 1812-04-17을 재확인했다. 목록·해설 열람이지 1811 원헌법 전체 판독은 아니다. 1813 독립 선언, 1814 정부 종료, 1816까지의 박물관 발행주체 표기를 단일 lifetime으로 합치지 않는다. 연방 편입의 효력·국가 동일성은 계속 보류한다.

[Salvatto의 2023년 학술논문 초록](https://www.anuarioiha.fahce.unlp.edu.ar/article/view/aihae195)은 엔트레리오스를 1820~1821년 지방의 정치·군사 조직으로 설명한다. 공화국 명칭만으로 독립 주권국 객체를 만들지 않는 원문 판정이 적절하다. 초록을 주권국 부정의 최종 법률 증명으로 승격하지 않는다. 1821-07-10 창설자 사망과 09-28 체제 종료 후보는 별개이며 종료 법률 원문·국가성·대상 ID가 없어 입력 보류한다.

수정안: 세 정치체는 사건 후보표에만 유지하고 현재 ARG/COL/ECU 국가 존속기간과 분리한다. 확정 lifetime·새 역사 객체·형상 적용 0건.

## TIME029 검토 및 확인된 시간 정밀도 보완

[ISW/CTP 2025-07-31 분석 본문](https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-july-31-2025)을 재열람했다. 본문은 서쪽 행정경계까지 진출한 위치 검증 영상이 부족하다고 명시한다. 도시 전체 점령 확정일 보류를 유지한다.

**보충 수정안:** 해당 분석의 자료 마감은 **2025-07-31 12:00 ET**, 게시 표시는 **20:30 ET**이다. 따라서 원문 표의 ‘2025-07-31 ISW 분석 기준일’은 하루 전체나 8월2일 현황을 보장하지 않으며 이 두 시각을 구별해 해석해야 한다. 여기서 마감시각은 관측 자료 기준이지 전선 자체의 효력시각이 아니다. 월별 서버 수정시각도 점령일로 입력하지 않는다. 이 확인된 구분을 본 후속 기록에 보완하고 과거 원문은 보존한다.

2025년 1월 자료는 일자가 미확정이므로 1월1일로 채우지 않는다. 러시아 측 발표일, 실제 군사 통제, 국제법상 주권은 분리한다. 군사 통제 기록을 UKR/RUS lifetime 또는 법적 국경에 적용할 근거가 없다. 피처별 독립 시점·원좌표·사용권이 확보되지 않아 형상 적용 0건이다.

원문이 인용한 [ISW 사용정책](https://understandingwar.org/fair-use-and-attribution-policy/) 재조회는 HTTP403으로 실패했다. 원문에 기록된 권리 제한을 해소했다고 주장하지 않으며, 이번에 권리 허가·라이선스 최신성을 새로 검증한 것도 아니다. 원본 벡터·지도 이미지 재배포 없음.

## 현행 충돌·기존 보류

현행 generated/v2/index.json의 blob은 d982119a3478199a499aeb8a4058b116a7a83b04로 직전 검토와 같다. 이번 fetch는 본문이 비어 있어 새로 JSON을 파싱했다고 주장하지 않는다. 직전 확인값과 원문의 현대 ARG/COL/ECU 대조를 유지하되 역사 정치체로 치환하지 않는다. 이번 두 보고서는 기존 보류인 FSM–RMI 6월11/12일 충돌, 미등록 역사 원문, 기존 주권 동일성 문제를 해소하는 자료가 아니다. 관련 기존 보류를 재확인하고 유지했다.

1801년은 조사 하한이며 건국일로 입력하지 않았다. 국가 존속기간과 지오메트리 유효기간은 분리한다. 진행기록은 읽되 두 브랜치의 조사 커서를 통째로 복사하거나 완료 횟수를 늘리지 않는다.

## 반영과 검증

반영 범위는 본 검토·evidence.json·reports/README.md 색인의 3파일이다. 원문 병합/체리픽, 국가 데이터, 타임라인 정본, 형상, 앱 pin 변경 0건. main·타 브랜치·배포·포터블 변경 없음. work/gis 최신 tree 위 단일 부모 커밋과 expected-head, force=false만 사용한다.

실행 검사: 네 브랜치 HEAD·관련 완전한 트리와 blob 비교, 2개 원문·2개 진행기록·직전 처리 기록 읽기, 원문 이력, 위 HTML 출처 재열람, JSON 직렬화 및 수정 경로 범위 검사. 원법령 스캔 전체, GIS/위상·화면 검사·전체 앱 검사 및 로컬 보고서 CLI는 미실행이다. 원격 게시 뒤 readback은 별도 실행 확인한다.
