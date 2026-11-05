# 1914 독일·오헝·세르비아 정본 등록과 work/gis 적용

> 보고서 ID: `GEO-HIST-1914-ACTIVATION-20261105` · 상태: `provisional` · 지도 반영: `work/gis-applied` · 색인일: 2026-11-05  
> 원문 최종 수정: 2026-11-05  
> 웹·앱 커밋: `d3a241588424afb7fc0dcf5f94c71f3bdd995238` · 런타임 자료: `bd62cc8ec6d8221202ed19de0a66f98d3e07ace9`

검토 기준: Pando work/gis `3be531e2fb8217adc9803357176e356c0030968b`, 자료 핀 `d2c023082b3e10ed0dc6928f629f190e0756933c`. 사용자 우선순위 독일 → 오헝 → 세르비아. main 통합·배포·포터블 생성은 하지 않는다.

## 적용 범위와 한계

독일은 사용자가 선택한 독일 국가의 연속성을 소유하는 기존 `state:DEU`에 1914-07-31 형상을 추가한다. 오헝 `state:austro-hungarian-empire`와 세르비아 왕국 `state:kingdom-of-serbia`는 1914-07-28 단일 날짜 형상으로 등록한다. 국가 존속기간과 형상 유효기간은 다르며, 오헝·세르비아의 존속기간 연도 정보로 이 형상의 기간을 늘리지 않는다. 독일의 기존 현대 형상은 새 참조일 양쪽에 기존 baseline으로 보존하며, 앞쪽 복제 버전을 명시적인 provisional modern proxy로 기록한다. 이는 과거 독일 형상을 새로 검증하거나 적용 범위를 넓힌 것이 아니다.

모든 새 역사 형상은 **provisional**이다. 기술적 유효성·표시 일반화 검토 통과를 historically-verified로 표시하지 않는다. 독일의 현대 해안/Helgoland·Düne proxy, 오헝의 현대 Adriatic/Bodensee 정책, 세르비아–몬테네그로 조약·거시 경로 확인과 상세 도엽 중첩 미완료를 그대로 남긴다. HistoGIS의 넓은 원천 연대는 형상 validity로 복사하지 않았다. restricted Harvard 26-state HGIS 레시피는 사용하지 않았다. HistoGIS CC BY 4.0, OSM ODbL 1.0 및 OpenStreetMap 기여자 표시, Natural Earth public domain 계보를 유지한다.

**현재 UI 제한:** builtin 뷰어는 월말을 조회한다. 1914-07에는 독일 7월 31일 형상이 선택되지만, 오헝·세르비아의 7월 28일 스냅샷은 그 월말 조회에서 선택되지 않는다. 정확한 날짜 및 대표 형상 가져오기는 기존 공통 모델에서 실제 검사했다. 이를 해결한다는 이유로 근거 없는 날짜 확장이나 UI 변경을 하지 않았다. 이번 작업은 완전한 1914년 세계 지도나 모든 국가의 역사 재구성을 완성한 것이 아니다.

## 원본 보존과 수정

세 원본 SHA·아카이브 레코드는 evidence-manifest.json에 있다. 등록 후 원본 바이트도 재확인했다. 독일 원본의 polygon 1은 polygon 0 안에 완전히 포함된 Usedom 부근 중복이다. 면적 374.683 km²의 중복 성분만 제거했으며, 그 땅은 component 0에 계속 포함된다. 원본 비주성분 내부점 보존 검사도 모두 통과했다. 이 작업은 Usedom이나 다른 섬을 지운 것이 아니다.

독일–오헝 경계는 오헝의 채택된 역사 육상 경로와 현대 Bodensee 구분선으로 한 번 맞췄다. 독일의 lake-to-Konstanz 연결도 채택된 NE 구분선으로 연결했다. 오헝–세르비아는 오헝의 381점 경로를 세르비아에도 똑같이 사용했다. Stelvio 삼합점 [10.452726,46.530948]과 두 Serbia 접합점은 유지했다.

공유 TopoJSON arc를 EPSG:3035에 실제 투영해 250 m DP 후보를 검토했다. 이 값은 이 후보의 매개변수이며 보편적인 거리 오차나 1:10M의 정의가 아니다. 이미 NE 참조와 동일한 arc 및 짧은 닫힌 도서 arc는 그대로 두었다. 원좌표 쌍을 재사용하며 전역 반올림을 하지 않았다. 1:10M 실제 비교와 별도 1:2M 기술 확대를 구분했다. 초기 후보의 해안 재단순화 때문에 덴마크에 잔여 조각이 생겨 해당 후보를 버리고 NE arc를 보존한 최종 후보를 사용했다.

|형상|원본 점 수|최종 점 수|최종 성분|
|---|---:|---:|---:|
|독일|7198|5261|22|
|오헝|7898|4640|24|
|세르비아|12114|973|1|

점 수는 복잡도 기록이며 역사적 위치 정확도가 아니다.

## 중첩 연산 잔여 10곳

최초 교차 결과에서 하나였던 기존 현대 육지 성분이 자르기 때문에 여러 조각으로 갈라지는 경우를 추출했다. 기존의 독립 도서 성분을 대상으로 한 삭제가 아니다. 각 원래 성분과 분리된 결과, 원본 내부점 및 면적은 probe·ledger·전후 display 파일로 추적 가능하다. 아래 잔여는 Boolean 공통 처리로 역사 표시 파생본에 닫아 넣었으며 땅을 양쪽에서 삭제하지 않았다. 주요 원본 성분·도서 내부점, 공통 경로의 연속성·합집합, 고정 기준점을 재검사했다. 이 작은 표시 조정은 별도의 역사적 영토 이양 주장이나 종료된 세부 연구의 재개가 아니다. 기록된 15 km² guard는 이 열 개 관측 결과를 넘어선 자동 처리를 막는 검사이며 세계 공통 단순화 기준이 아니다.

|기존 국가|날짜|표시 파생본 소유자|잔여 면적 km²|
|---|---|---|---:|
|DEU|1914-07-28|AH|0.089363|
|ITA|1914-07-28|AH|11.459742|
|ITA|1914-07-28|AH|14.509881|
|CHE|1914-07-31|DEU|0.426877|
|FRA|1914-07-31|DEU|0.211308|
|FRA|1914-07-31|DEU|0.938362|
|FRA|1914-07-31|DEU|1.184471|
|FRA|1914-07-31|DEU|1.802694|
|FRA|1914-07-31|DEU|2.228687|
|LUX|1914-07-31|DEU|0.091990|

총 32.943377 km². 원본 master는 변경하지 않았다. 작은 필지·표석·모든 상세 도엽 조사를 새 종료 조건으로 요구하지 않았다.

## 기존 13개 국가에 필요한 참조일 변화

아래 면적은 이전 현대 proxy와 최종 컴파일 형상의 차이이며 실제 역사적 영토 변동 면적의 측정값이 아니다. 주변국의 나머지 윤곽은 현대 proxy로 남는다. `HUN`은 해당 하루 현대 독립국 proxy의 중복 표시만 숨기며 원본과 다른 날짜는 유지한다.

|ID / 국가|날짜|컴파일 차이 km²|이유|
|---|---|---:|---|
|ALB / 알바니아|1914-07-28|6.329|오헝·세르비아 표시 형상과 중복되는 현대 proxy 부분만 자름|
|BEL / 벨기에|1914-07-31|933.480|독일제국 표시 형상과 중복되는 현대 proxy 부분만 자름|
|BGR / 불가리아|1914-07-28|254.223|오헝·세르비아 표시 형상과 중복되는 현대 proxy 부분만 자름|
|CHE / 스위스|1914-07-28|52.565|오헝·세르비아 표시 형상과 중복되는 현대 proxy 부분만 자름|
|CHE / 스위스|1914-07-31|137.962|독일제국 표시 형상과 중복되는 현대 proxy 부분만 자름|
|DEU / 독일|1914-07-28|466.407|오헝·세르비아 표시 형상과 중복되는 현대 proxy 부분만 자름|
|DEU / 독일|1914-07-31|188593.000|독일제국 참조일 형상 교체|
|DNK / 덴마크|1914-07-31|3921.495|독일제국 표시 형상과 중복되는 현대 proxy 부분만 자름|
|FRA / 프랑스|1914-07-31|14275.850|독일제국 표시 형상과 중복되는 현대 proxy 부분만 자름|
|GRC / 그리스|1914-07-28|77.274|오헝·세르비아 표시 형상과 중복되는 현대 proxy 부분만 자름|
|HUN / 헝가리|1914-07-28|93200.959|오헝에 전부 포함된 현대 proxy 중복 제거|
|ITA / 이탈리아|1914-07-28|15093.001|오헝·세르비아 표시 형상과 중복되는 현대 proxy 부분만 자름|
|LUX / 룩셈부르크|1914-07-31|46.782|독일제국 표시 형상과 중복되는 현대 proxy 부분만 자름|
|NLD / 네덜란드|1914-07-31|83.267|독일제국 표시 형상과 중복되는 현대 proxy 부분만 자름|
|ROU / 루마니아|1914-07-28|107859.187|오헝·세르비아 표시 형상과 중복되는 현대 proxy 부분만 자름|

## 정확한 gate 대상

기존 historical display review 검증기는 변경하지 않았다. source 4건과 compiled 18건을 실제 적용 파일에서 다시 검사했다. source 4건 중 하나는 기존 현대 baseline을 유지하기 위한 독일의 복제 버전이며, 새 역사 형상은 세 건뿐이다.

|source entity|versionId|validFrom|validTo|
|---|---|---|---|
|state:DEU|state:DEU:natural-earth-5.1.1-before-1914-snapshot|null|1914-07-30|
|state:DEU|state:DEU:1914-07-31-display-r1|1914-07-31|1914-07-31|
|state:austro-hungarian-empire|state:austro-hungarian-empire:1914-07-28-display-r1|1914-07-28|1914-07-28|
|state:kingdom-of-serbia|state:kingdom-of-serbia:1914-07-28-display-r1|1914-07-28|1914-07-28|

|compiled entity|sourceVersionId|validFrom|validTo|
|---|---|---|---|
|ALB|state:ALB:natural-earth-5.1.1|1914-07-28|1914-07-28|
|BEL|state:BEL:natural-earth-5.1.1|1914-07-31|1914-07-31|
|BGR|state:BGR:natural-earth-5.1.1|1914-07-28|1914-07-28|
|CHE|state:CHE:natural-earth-5.1.1|1914-07-28|1914-07-28|
|CHE|state:CHE:natural-earth-5.1.1|1914-07-31|1914-07-31|
|DEU|state:DEU:natural-earth-5.1.1-before-1914-snapshot|1867-07-01|1914-07-27|
|DEU|state:DEU:natural-earth-5.1.1-before-1914-snapshot|1914-07-28|1914-07-28|
|DEU|state:DEU:natural-earth-5.1.1-before-1914-snapshot|1914-07-29|1914-07-30|
|DEU|state:DEU:1914-07-31-display-r1|1914-07-31|1914-07-31|
|DNK|state:DNK:natural-earth-5.1.1|1914-07-31|1914-07-31|
|FRA|state:FRA:natural-earth-5.1.1|1914-07-31|1914-07-31|
|GRC|state:GRC:natural-earth-5.1.1|1914-07-28|1914-07-28|
|ITA|state:ITA:natural-earth-5.1.1|1914-07-28|1914-07-28|
|LUX|state:LUX:natural-earth-5.1.1|1914-07-31|1914-07-31|
|NLD|state:NLD:natural-earth-5.1.1|1914-07-31|1914-07-31|
|ROU|state:ROU:natural-earth-5.1.1|1914-07-28|1914-07-28|
|state:austro-hungarian-empire|state:austro-hungarian-empire:1914-07-28-display-r1|1914-07-28|1914-07-28|
|state:kingdom-of-serbia|state:kingdom-of-serbia:1914-07-28-display-r1|1914-07-28|1914-07-28|

## 실행한 검사

- 최종 source/compiled GEOS 유효성, 두 공유 경로의 연속·정확한 양 끝점·겹침 0, 합집합 유효성, 원본 성분/도서 내부점과 주요 기준점 보존.
- 세 역사 형상의 source/compiled 대칭차 0. 두 참조일 실제 참가국 169쌍의 최대 겹침 6.889020603972895e-16 degree²로 부동소수점 연산 수준 이내. 이 수치를 역사적 위치 오차로 해석하지 않는다.
- 기존 13개국의 현대 기준일 2026-10-06 및 범위 밖 사건 경계 표본에서 원좌표 digest 동일. 바뀌지 않은 source descriptor 274개·builtin descriptor 265개를 이전 pin과 대조. USSR·프로이센은 열거나 재생성하지 않고 그 불변 descriptor로 보존 확인.
- 정식 등록한 49파일의 SHA-256·길이, source/chunk/index 메타데이터, 실제 source 4 / compiled 18 gate 및 세 정확한 날짜의 static snapshot provenance 검사.
- 기존 생성기로 14개 변경 entity의 chunk만 --check 통과.
- 집중 Node 테스트 17/17 및 추가 부분 저장 통합 fixture 3/3 통과. 변경 파일 ESLint와 git diff --check 통과.
- 전체 세계 GIS 재생성, 전체 프로젝트 검증, native 앱 실행·재빌드, main 통합, 배포, 포터블/설치 패키지 생성은 실행하지 않았다.

관련 코드 변화는 신규 entity의 source·chunk·index·정확한 lineage source 짝을 검사하면서 부분 저장을 허용하는 기존 저장 소유자 보완이다. 제거·중복·고아 membership 및 누락된 짝은 계속 거부한다. 새 테스트를 먼저 실행해 기존 membership 거부 실패를 확인한 뒤 수정했다.

## 증거

- [최종 1:10M 및 공통선 확대](display-review.png)
- [실제 컴파일 파생본 비교](compiled-review.png)
- [정확한 source/compiled ID·기간·digest 및 UI 제한](post-registration-proof.json)
- [컴파일 차이와 검사](compiled-proof.json)
- [범위 밖 보존](preservation-proof.json)
- [도서/성분 보존](important-islands-proof.json)
- [입력·증거 해시](evidence-manifest.json)

## 원격 반영 기록

- 앱 work/gis: [d3a241588424afb7fc0dcf5f94c71f3bdd995238](https://github.com/kimjeon-il/Pando/commit/d3a241588424afb7fc0dcf5f94c71f3bdd995238) — push 후 원격 SHA 재확인.
- 런타임 자료 work/gis: [bd62cc8ec6d8221202ed19de0a66f98d3e07ace9](https://github.com/kimjeon-il/PandoLab-library-data/commit/bd62cc8ec6d8221202ed19de0a66f98d3e07ace9) — 원격 SHA 및 보관된 49개 파일 SHA·길이 재확인. 무관 native 객체 참조 274개도 이전 pin과 동일.
- 앱 pin은 위 자료 커밋과 일치하며 새 pin 재마운트 후 정본/chunk/compiled 검사를 다시 수행했다. 두 work/gis 작업 트리는 깨끗하다.
- 변경한 고유 compiled 형상 17개의 공통 GPU 메시 생성 및 패킷 codec 검사를 추가로 통과했다. 전체 세계 메시를 생성하지 않았다.
- 원격 combined-status API는 빈 statuses 배열을 반환했다. 원격 CI 통과로 간주하지 않는다. 로컬 집중 검사는 위와 같이 20건 통과·0건 실패다.
- 앱 main 통합·배포·native 실행·포터블/설치 패키지는 실행하지 않았다.
- 런타임/앱 push 및 제한의 구조화된 기록: [publication-result.json](publication-result.json). 보고서 원문은 기존 --publish-reports / --check-reports 절차로 이 범위만 보관·원격 검증한다.


[CI follow-up](ci-follow-up.md): reference-day provincial parent correction, exact commits, reproduction and separate baseline failures.


[Reference-date usability investigation](reference-path-investigation.md): active UI contract, minimum existing-file path and exact USSR coordinate-order diagnosis; implementation and screen checks remain pending.
