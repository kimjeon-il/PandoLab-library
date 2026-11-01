# G 아바가이투: 이미지좌표 차이면 보관

**이 묶음은 runtime 국가데이터가 아니다.** 폴리곤 1개는 원도 상대정렬 픽셀좌표이며 RFC7946 GeoJSON/WGS84가 아니다. 새 지리좌표 폴리곤은 0개다. 1991 실제통제선 또는 2008 실제이양영토로 사용하지 않는다.

## 포함 파일
- `G-nonoverlap-polygon.imagecoords.json`: 도5 러시아 주장선과 도6 2004 합의선의 차이. 기술적 폐합선2개를 별도 표기했다. 원도 법적 경계가 아니다.
- `G-scope-preserved-source-pixels.json`: 남쪽 공통구간과 나머지 작업구간. old 정점0–27/new0–55 보존.
- `preservation-proof.json`: 원래 입력 불변 및 A–C 미변경 기록.
- `event-date-evidence.json`: 2004-10-14 서명, 2005-06-02 효력, 2008-10-14 현장 인계. 사건 날짜와 미확정 지오메트리 유효기간(null)을 분리한다.
- `sources.json`: 출처와 비공개 보존/공개 제외 범위.
- `ozi-registration-consistency.json`: 1979년판 M-50-092의 제3자 등록표 9점 내부 일관성 계산.
- `check_ozi.py`: 보존된 좌표표만으로 계산 재현. NumPy/pyproj 필요. 실행 시 `ozi-registration-consistency-recomputed.json`을 새로 만들며 입력은 유지한다.
- `runtime.stderr.log`: 공식 MapToolkit0.6.5 실행 실패 기록.
- `SHA256SUMS`: 이 묶음 파일 무결성.

## 검증과 한계
픽셀 Polygon1개 유효, 면적128939.234698px². 물리면적 및 역사적 지리 유효기간은 미확정이다. 공통 남쪽 굽이는 변경하지 않았다.
1979 원도에는 Большой 섬 남·동 구하도를 따른 국경기호가 보이며 Pulkovo1942(2) Ozi 등록표가 확보됐다. 서·동열6점 fit/중간열3점 holdout 잔차15.26/33.68/36.67m는 **동일 등록표 내부 일관성**이지 독립 위치정확도나 Toolkit 통과가 아니다. 원도1979 표현을1991 통제선으로 간주하지 않는다. WGS84 datum 변환도 수행하지 않았다.
공식 분석은 필수 macro-mask.h 누락으로 실패했으며 우회하지 않았다. 정합·추출 성공 산출물은 없다. 원본지도/overlay 이미지/개인정보 XML/현대국가 참조 GeoJSON은 이 공개묶음에서 제외했다. 따라서 코드도 원도 접근 없이 보존 메타데이터만 재계산한다.
