# RSFSR 1946 사건영역 폴리곤 — 실제 GeoJSON 보관

> ID: GEO-RSFSR-DATED-POLYGONS-20261031 · 상태: geometry-produced / generalized-administrative-candidate · runtime: not-applied
> 기준 원격 data work/gis: `a3e8122206181707cc15843d5a67d9eead24b4cc`.

## 산출물과 정확한 수량
[dated-polygons.geojson](dated-batch/dated-polygons.geojson)은 **21 feature**를 포함한다: 남사할린 사건영역1 + 입력에 존재하는 쿠릴섬18 = 사건영역19, 사할린 전·후 로컬범위2. 하나의 1946-02-02 행정편입 사건을 표현하는 부분 형상들이며, 19개 독립 역사 사건이나 전체 역사국가21개가 아니다. 보고서만이 아니라 실제 닫힌 폴리곤 좌표를 보관한다. 원본 좌표 파일 SHA-256: `f940f5a6edd3a7d6059b0ed1bb5faf72ef9179b5f2f71652b92f385ee4770019`.

- [생성자 범위·제약](dated-batch/README-ko.md)
- [생성자 위상 검증](dated-batch/validation.json), [쿠릴 포함·생략 목록](dated-batch/kuril-coverage.json)
- [사할린 경계 권고 근거](sakhalin-demarcation/RECOMMENDATION-ko.md), [표시 크기 계산](sakhalin-demarcation/display-scale.json), [출처목록](sakhalin-demarcation/source-manifest.json)
- [쿠릴 섬 식별 검토](kuril-membership/README-ko.md), [식별지도 출처·해시](kuril-membership/sources.json)
- [게시 검사와 원문 해시](publication-checks.json)

## 날짜·권리·기하 해석
1946-02-02는 RSFSR 행정편입 기준이며 군사통제나 국제적 주권 인정일을 의미하지 않는다. 1945 통제는 연도 정밀도만 유지하고 주권일은 미결정이다. [from,to)와 null의 미확정 시작/종료 의미를 유지하며 국가 존속기간은 변경하지 않는다. 사건영역과 전후 비교범위를 동시에 국가층으로 겹쳐 넣지 않는다.

사할린50N은 1907측도/1911제작 도엽과1908·1935 측량 기록 검토를 바탕으로 권고한 **1:10M 표시 일반화선**이다. 당시 표석 연결선을 측지학적으로 완전 복원했다고 주장하지 않는다. 80.81m는 당시 경계점 사이 상대 측지차이며 WGS84 절대오차 상한이 아니다. 1920px 창 약0.24CSSpx는 지정된 로컬 코드·최대배율 계산 조건에서의 표시 크기다. 최신 work/gis 전체 렌더러 검증 결과가 아니다. 임의200m 남향 보정을 하지 않는다.

쿠릴18개는 입력의 해당 범위 안에 존재하는 완전한 컴포넌트를 좌표 이동 없이 재사용했다. 생략된 섬·암초는 임의 생성하지 않으며 군도 전체의 상세 완전성을 주장하지 않는다. 남부 분쟁지역의 일본 주장을 해소한 것으로 표시하지 않는다. 현대 일반화 해안 재사용과1946 실측 해안의 정점 일치는 다른 주장이다.

## 입력·검증·보관 상태
입력은 복구된 `recovery/final-selected/countries/state-soviet-union-russian-sfsr.json`의 `state:soviet-union-russian-sfsr:1991-r1`. 파일 SHA-256 `a40f9b418677d23be3a20b83c6627b414b2047a2bfdff242bdac3a6fb3f85da4`. 이 복구 파일을 최신 원격 전체국가와 동일하다고 가정하지 않으며, 실제 런타임 적용 전 최신 데이터와 충돌·기간·객체 대응 검사가 필요하다.

생성자 검증은 모두 유효, 사건영역간 겹침0, 사할린 전북부+남부영역=후본섬, 쿠릴 입력 재합성 대칭차0을 기록한다. 게시자는 JSON/feature수/링 폐합, 쿠릴18개 입력 좌표 완전 동일, 파일 해시·선택경로·원격 읽기 검증을 수행한다. 생성자 검사를 게시자가 재실행한 것으로 혼동하지 않는다. 생성 당시 PRIVATE/CANDIDATE 속성은 내용 보존을 위해 유지하며 이 커밋은 공개 범위 확대나 런타임 적용 명령이 아니라 사용자 요청의 저장소 후보 보관이다.

원지도/PDF/영상·스크린샷·ZIP은 재배포 권리 미확인으로 제외한다. 문서 속 원자료 파일 경로는 비공개 조사 패키지 경로다. Private Library의 GeoJSON `libfile_690d868f751081918a3732c26c46c927` v2와 묶음 `libfile_27ab300912dc81918b93ad7c51f0efda`는 별도 보존 경로다. 이 커밋은 source/native/compiled/transport·앱 pin·main을 수정하지 않고 배포·포터블을 생성하지 않는다.
