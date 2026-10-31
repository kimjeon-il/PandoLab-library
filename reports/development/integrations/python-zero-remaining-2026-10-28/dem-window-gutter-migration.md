# DEM 고도 판독과 타일 경계 보정 전환 기록

범위: Python 완전 전환의 부분 작업. `work/gis`에서 DEM 판독과 경계 보정만 전환했으며, 전체 전환 완료나 운영 데이터 승인을 뜻하지 않는다.

- 고도 판독: `b2eebdfebec7b2099078695780cbfcfc25d021af`, 생성기 연결 `832c49b9`. 고정 Rasterio 결과를 C++/GDAL 스트리밍 판독기와 비교했다. 영역 평균, 경도 래핑, 극지 행, NoData, 허용 범위와 오류 전달을 확인했다. 실제 ETOPO 크기 및 EPSG:9518 등록 조건은 합성 희소 TIFF로 확인했다. [Windows/Linux CI](https://github.com/kimjeon-il/Pando/actions/runs/41170497377)가 통과했고, Windows에서 소스 고정 바이너리와 생성기 연결을 검증했다.
- 타일 경계: `cf70f805`, 생성기 연결 `1d35ff5c`. Python 고정 결과와 C++ 픽셀 계산을 날짜변경선, 극지, 다른 부분 타일 크기에서 비교했다. [Windows/Linux CI](https://github.com/kimjeon-il/Pando/actions/runs/41171207229)가 통과했다. Windows에서 WebP 픽셀 왕복, 두 번째 실행 안정성, 손상 입력 시 앞선 타일 보존을 확인했다. 압축 바이트가 기존과 같다는 주장은 하지 않는다.
- 원본 보호: `ccba91e1`에서 tint ZIP을 별도 임시 위치에 풀고, 주변 같은 이름 파일과 기존 출력의 덮어쓰기를 막았다. 경로 이탈과 ZIP CRC 오류를 거부하는 합성 사례를 검사했다. 작업 공간이 큰 경우 추출과 마스크 처리 전에 여유 공간을 확인한다.
- 실행기: `d9d17e13`에서 색상만 재생성할 때 관련 없는 DEM 판독 및 경계 도구를 요구하지 않도록 했다.

실제 보존 ETOPO 원본은 확인하지 못했으며 전체 LOD 0–5의 실자료·처리 시간 비교는 미완료다. Python DEM 생성기와 다른 Python 작업이 남아 있다. 운영 자료와 자료 pin은 변경하지 않았다.
