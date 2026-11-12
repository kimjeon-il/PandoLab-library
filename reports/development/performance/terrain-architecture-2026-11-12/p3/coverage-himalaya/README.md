# 히말라야 COG 복원 검증

동일 ETOPO 원본에서 히말라야 5×3 타일 영역과 마진을 세 해상도로 별도 표본화해 COG overview를 구성했다. `manifest.json`의 파일 및 64KiB 청크 해시, `pyramid-input.json`의 각 해상도 입력 해시를 보존한다. GDAL 전체 COG 구조 검사 오류·경고는 없었으나 실행 시 `GDAL_DATA` 미설정으로 `tms_NZTM2000.json` 환경 경고가 별도 출력됐다.

`report.json`은 브라우저 모의 206 서버에서 1024 타일 15개와 512 타일 60개를 복원하여 모든 RGBA·gutter 해시가 타일 표본과 일치한 결과다. 실제 외부 호스트 접근성 또는 뷰어 성능 결과는 아니다.
