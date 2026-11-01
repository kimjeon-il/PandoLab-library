# DEM 고도 판독과 타일 경계 보정 전환 기록

범위: Python 완전 전환의 부분 작업. `work/gis`에서 DEM 판독과 경계 보정만 전환했으며, 전체 전환 완료나 운영 데이터 승인을 뜻하지 않는다.

- 고도 판독: `b2eebdfebec7b2099078695780cbfcfc25d021af`, 생성기 연결 `832c49b9`. 고정 Rasterio 결과를 C++/GDAL 스트리밍 판독기와 비교했다. 영역 평균, 경도 래핑, 극지 행, NoData, 허용 범위와 오류 전달을 확인했다. 실제 ETOPO 크기 및 EPSG:9518 등록 조건은 합성 희소 TIFF로 확인했다. [Windows/Linux CI](https://github.com/kimjeon-il/Pando/actions/runs/41170497377)가 통과했고, Windows에서 소스 고정 바이너리와 생성기 연결을 검증했다.
- 타일 경계: `cf70f805`, 생성기 연결 `1d35ff5c`. Python 고정 결과와 C++ 픽셀 계산을 날짜변경선, 극지, 다른 부분 타일 크기에서 비교했다. [Windows/Linux CI](https://github.com/kimjeon-il/Pando/actions/runs/41171207229)가 통과했다. Windows에서 WebP 픽셀 왕복, 두 번째 실행 안정성, 손상 입력 시 앞선 타일 보존을 확인했다. 압축 바이트가 기존과 같다는 주장은 하지 않는다.
- 원본 보호: `ccba91e1`에서 tint ZIP을 별도 임시 위치에 풀고, 주변 같은 이름 파일과 기존 출력의 덮어쓰기를 막았다. 경로 이탈과 ZIP CRC 오류를 거부하는 합성 사례를 검사했다. 작업 공간이 큰 경우 추출과 마스크 처리 전에 여유 공간을 확인한다.
- 실행기: `d9d17e13`에서 색상만 재생성할 때 관련 없는 DEM 판독 및 경계 도구를 요구하지 않도록 했다.

## 2026-11-01: DEM 생성기 종료

- tint의 육지·빙하 분류, 면적 평균과 배경 채우기는 GDAL C++와 Node 관리 경로로 이전했다. 동결된 소형 자료, 128행 경계·날짜변경선, 육지·빙하 판정, 한글 경로, ZIP CRC·경로 이탈과 원본 보존을 확인했다. [Windows/Linux tint CI](https://github.com/kimjeon-il/Pando/actions/runs/41286886878)가 통과했다.
- ETOPO 원본의 좌표계·격자·NoData 검사를 GDAL C++로 옮기고 Rasterio 의존성을 제거했다. 고정 Python 결과의 작은 8×4 격자를 6개 타일로 나눈 모든 RGBA 픽셀이 일치했다. 극지 음영 보정과 gutter 재실행도 합성 데이터에서 확인했다. [Windows/Linux 통합 CI](https://github.com/kimjeon-il/Pando/actions/runs/41288514066)와 [극지·gutter CI](https://github.com/kimjeon-il/Pando/actions/runs/41287762768)가 통과했다.
- 원본 해시, 출력 덮어쓰기 거부, 라이브러리 출력 lease, 1GiB 이상 작업의 공간 여유 검사와 명시적 재사용·보정 기능을 유지하며 Node 실행기로 전환했다. 재사용 후보는 원본·복사 타일의 해시를 확인하고, 원본 내부를 가리키는 연결 경로를 출력으로 받지 않는다. 기존 Python 생성기와 대응 테스트는 코드 커밋 `589e8758`에서 제거했다. 최종 소형 관련 Node 검사 34개와 실행기의 실제 도움말 호출을 확인했다.

실제 보존 ETOPO 및 HYP_HR 원본은 확인하지 못했으며 전체 LOD 0–5의 실자료·처리 시간 비교는 미완료다. 인코딩 파일 전체의 기존 바이트 일치를 주장하지 않는다. 다른 Python 도구와 테스트는 여전히 남아 있다. 운영 자료와 자료 pin은 변경하지 않았다.
