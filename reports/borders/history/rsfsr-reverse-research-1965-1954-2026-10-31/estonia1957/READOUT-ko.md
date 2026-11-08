# 1957 에스토니아 — 개별 도엽·현장 커버리지 검토
2026-10-31 21:38–21:41 UTC. 지도 엔진 정합/선 추출은 하지 않음.

## 확보된 실제 자료
공식 Maa-ja-Ruumiamet WMS GetCapabilities와 GetFeatureInfo 성공. 단순 목록 검색에서 실제 위치별 도엽 메타데이터 조회로 진행했다.

| 대상 | 조회점 WGS84 (검색용 마을점) | 1:50k 도엽 ID | old 연도 | middle 연도 | newer 연도 |
|---|---|---|---|---|---|
| Podmotsa/Подмоча |58.00833N,27.66222E|o3568v (O-35-68-В)|1937|1964|1989|
| Perdaku/Пердаку |57.89583N,27.79056E|o3580b (O-35-80-Б)|1938|1964|1989|

연도는 서비스의 `aasta` 메타데이터 값이다. 난외 원문이 없는 WMS이므로 측량·수정·발행일 세 항목을 모두 검증했다고 주장하지 않는다. 각도엽의 날짜 정밀도는 연도 단위.
1:25k old 메타데이터는 두 조회점에서 결과 없음. Perdaku 인근1:100k old는o3580/1938. 이점들에서1944–1957 사이 판본이 제공된다는 증거를 얻지 못했다. 서비스 전체에 그런 자료가 없다는 뜻은 아님.

## 실제 영상 커버리지 육안검수
- `podmotsa-1964-wms.png` (1200×1067): Подмоча, Дубки, Кулье, Вельна와 Кулейская 수로 및 경계 기호가 실제로 보인다.1957 법령 북부 설명을 대조할 수 있는 후기 참조 영상이다.
- `perdaku-1964-wms.png` (1400×1145): Пердаку, Сестники, Лутепя, Тсюдски, Литвина, Питсина 등 법령 지명이 영상에 포함됨. Perdaku 북쪽·동쪽으로 돌아가는 경계 기호를 확인할 수 있다.
- 영상은 서버가 이미 등록한 WMS 발췌이지 원도 전체가 아니다. 자체 정합 잔차검증·GeoJSON·실제변경폭 계산은 미실행.
- 두 발췌는 법령 전체(Pedедзе까지)를 포괄하지 않는다. 북부 두 주요 구간만 검수했다.

## 중요한 전후 비교 판단
1937/1938 old와1964 middle을 빼서1957 변경면이라고 하면1944 공화국 이관까지 섞일 수 있다. 따라서 이들은 '1957 직전/직후 확정쌍'이 아니다. 후기 영상은 확보됐지만 정확 이전선의 직접 지도는 여전히 추가 필요.

## 정확한 이전/승인 지도 후보 — 국립기록원
공식 카탈로그 https://www.ra.ee/kaardid/index.php/et/map/view?id=100108
청구기호 **ERA.T-6.5.13 leht1**.
제목은ГУГК O-35-68(Самолва) 및 O-35-79 Võru를 포함한 합성도.1:100,000,117×65cm. 카탈로그 편집1952, 인쇄 IV1956 및 XI1952. '소련 최고회의 간부회에서 승인된 문서'라는 주석.
주의: 승인필기 시점을 읽지 못했으므로1952/56 바탕지도라는 이유만으로1957 이전경계라 확정할 수 없다. 원도상 승인선의 날짜·범례 확인 필요.
카탈로그에는 '사용제한 없음'이나 실제 제공된3000px 다운로드 링크를 열면 **VAU 로그인페이지(Sisene)**가 반환됐다. `archive-image-response.html`에 보존. 이미지 미확보이며 로그인우회·유료주문·사용자PC 접근 없음.

## 다음 필요한 것
1. 위 기록원 승인도에 정상 접근할 수 있을 때 원도 날짜·주석·승인선을 판독.
2.1957 이전 공화국경계가 확인되는 경우에만 확보1964 영상과 비교.
3. 현재 등록된 WMS는 출처등록된 참고영상으로 보존하되 Toolkit 검증export라고 부르지 않음.

## 출처 / 요청 재현
공식 서비스설명: https://geoportaal.maaruum.ee/est/teenused/wms-wfs-wcs-teenused-p65.html
GetCapabilities: https://kaart.maaamet.ee/wms/ajalooline?SERVICE=WMS&REQUEST=GetCapabilities
좌표검색용 Perdaku: https://www.geonames.org/794220/perdaku.html
Podmotsa 위치는 Wikipedia 좌표를 조회점으로만 사용했고 영상의 Подмоча 명칭으로 커버리지를 확인함: https://en.wikipedia.org/wiki/Podmotsa

모든 WMS 요청 VERSION=1.1.1, SRS=EPSG:3301.
GetMap 공통 LAYERS=nltopo_keskmine_50T_alt,STYLES=,FORMAT=image/png.
Podmotsa BBOX=712000,6432000,721000,6440000;WIDTH=1200;HEIGHT=1067.
Perdaku BBOX=719000,6419000,730000,6428000;WIDTH=1400;HEIGHT=1145.
GetFeatureInfo 공통 INFO_FORMAT=text/plain,FEATURE_COUNT=20,WIDTH=101,HEIGHT=101,X=50,Y=50.
LAYERS와QUERY_LAYERS=nltopo_vanem_50T_info,nltopo_keskmine_50T_info,nltopo_uuem_50T_info.
Podmotsa BBOX=715899,6435071,716899,6436071.
Perdaku BBOX=724183,6422983,725183,6423983.
조회응답 txt를 수정없이 보존. SHA256SUMS에 파일해시 기록.
