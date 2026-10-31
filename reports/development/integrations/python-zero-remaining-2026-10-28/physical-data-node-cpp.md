# 물리 자료 생성기 Node/C++ 전환

- 코드 커밋: `58fb3bad506776a96b8d6777417c9b10c0fad9cb`, 브랜치 `work/gis`. 자료 pin: `c73d3f562d35f92d749458c9890bec02875ff605`.
- 물리 수계 입력은 Node와 GDAL, 래스터 TIFF 판독은 GDAL C++, 리샘플링·마스크·합성은 공통 C++, 파일·manifest 관리는 Node가 맡는다. 기존 Python 실행기와 그 전용 릴레이는 제거했다. 기존 원본 및 출력 덮어쓰기와 원본 폴더 내부 출력은 거부한다.
- 물리 수계의 8종 합성 SHP와 입출력 계약은 [Windows/Linux CI 41169053303](https://github.com/kimjeon-il/Pando/actions/runs/41169053303)에서 검증했다. TIFF 판독, 회색·RGB 합성 원본의 2단계 타일 픽셀, 원본·기존 출력 보호는 [Windows/Linux CI 41169053050](https://github.com/kimjeon-il/Pando/actions/runs/41169053050)에서 확인했다. 마스크·gutter와 WebP 픽셀은 [Windows/Linux CI 41169052986](https://github.com/kimjeon-il/Pando/actions/runs/41169052986)에서 확인했다.
- 선택한 보존 국가 3개와 호수 2개의 720×360 육지 마스크 259,200픽셀은 이전 Python 결과와 일치했다. SHA-256: `cc6046314e28b654e07e53e38acf5116ea7b9578e59ab5e5116b34fc078f5d31`.
- 실제 21,600×10,800 TIFF 원본의 이미지 모드·전체 타일과 대형 입력 성능, 실제 Natural Earth 수계 SHP 전체는 확인하지 않았다. WebP 및 GeoJSON 인코딩 바이트가 과거 파일과 같다는 뜻은 아니다. 운영 데이터, 모델, 웹 배포는 변경하지 않았다. 나머지 Python 전환은 별도 작업으로 남는다.
