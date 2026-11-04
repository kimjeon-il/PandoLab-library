# 미사용 도구·옛 앱 산출물 정리 — 2026-11-04

## 완료한 삭제

|대상|실제 논리 삭제 바이트|근거|
|---|---:|---|
|옛 native 앱 16버전 뷰|3,110,035,244|현재 브랜치 참조·프로세스·lease 밖의 검증된 버전|
|미사용 frontend 뷰|859,500,490|공유 저장소 원문 및 현재 뷰와 분리, 완료 journal|
|Emscripten 6.0.3 / LLVM-MinGW 20261020 / micromamba 다운로드·추출 캐시 / LibTorch SDK 입력|4,039,069,998|50,626개 파일, 정확한 scope·해시·SDK archive member 증명|
|실패 artifact ZIP·종료 Cargo 임시파일|171,067,058|394개 파일, truncated ZIP 및 종료 bootstrap|
|온라인 C 캐시·종료 fixture|166,369|사용 중·readonly 공유 파일 제외|
|휴지통 orphan 위치 메타데이터|16,886|115개, 대응 데이터 없음|

C 휴지통 데이터는 Windows Clear-RecycleBin으로 제거했다. 선택 조사 파일 58,966개, 선택 NTFS 주 스트림 할당량 5,223,229,256바이트. 사전 할당 조사와 공식 삭제의 시간이 겹쳤으므로 이를 정확한 물리 확보량으로 단정하지 않는다. 현재 휴지통에는 Windows desktop.ini 129바이트만 남았다. 휴지통의 정확한 논리 삭제 합계는 확보하지 못했다.

하드링크인 뷰와 blob을 중복 합산하지 않는다. native 선택 NTFS 단독 회수 가능 할당량 3,107,819,744바이트, SDK 선택 3,446,665,400바이트. SDK 마지막 링크 해제 payload는 3,374,076,767바이트이며 미선택 환경과 공유한 686,014,008바이트 할당은 그대로 유지된다. frontend 후속 blob 삭제는 213,967,062바이트이며 뷰 논리량과 별도로 참고한다.

## 실제 단계별 드라이브 변화

- 옛 앱: D 41,362,952,192 → 44,469,460,992 (+3,106,508,800).
- SDK: D 45,026,369,536 → 48,481,689,600 (+3,455,320,064).
- frontend blob: D 48,481,964,032 → 48,695,947,264 (+213,983,232).
- 휴지통: C 42,372,317,184 → 47,470,829,568 (+5,098,512,384).
- 실패 전송: C 47,368,224,768 → 47,508,971,520 (+140,746,752).

전체 작업 시작 기준은 C 42,573,242,368 / D 41,390,043,136바이트. 마지막 전체 여유 공간은 후속 measurement.json을 참고한다. 다른 채팅의 작업·캐시 생성도 동시에 발생하므로 전체 차이를 전부 이 작업의 삭제 효과로 환산하지 않는다.

## 재발 방지와 검증

work/objects에 322e3f4634513d30fbbc4c61754f9c84d4fe71ab 및 a50166162e69ad5af293ebb8d73d2860bce23dca를 commit/push했다. native 준비는 로컬 자동 설치·컴파일 대신 선택된 CI 계약을 요청한다. 새 앱 참조 전환 후 미참조 native/frontend 뷰와 마지막 blob을 기존 저장소 소유자가 회수한다. 쓰기 전 journal 배치로 중단 재개하며 참조·lease·프로세스·해시 검사를 유지한다. 이 변경은 work/objects 범위이며 main과 다른 작업 브랜치 통합·배포는 하지 않았다.

최종 집중 검사 47/47, 실제 viewer 제공 및 artifact 계약 검사 4/4 통과. 최초 CI 구현 commit의 선택 검사와 native-map-image 준비는 https://github.com/kimjeon-il/Pando/actions/runs/41831543957 에서 성공했다. 후속 배치·scope 변경은 위 로컬 집중 검사로 검증했다. CHECK-BUDGET이 파일 목록 ESLint와 E7 planner 실행 명령을 거부하여 해당 검사는 실행하지 않았고 우회하지 않았다. 전체 검사·WASM/GIS/학습 재생성은 실행하지 않았다.

보호한 런타임 40개 해시 재확인, objects 기존 미추적 WIP 4개 해시 일치. GPU Python torch 2.14.1+cu126 CUDA tensor 연산 결과 1.0, ADB 1.0.41 실행 확인. 기존 Windows 앱 build-info 실행 성공(development, MSVC x64, Rust 1.99.1); 상세 JSON 첨부.

## 보존·미완료

- 현재 앱/브랜치 참조 frontend·native, GPU Python/CUDA, GDAL/GEOS/PROJ 환경과 LibTorch runtime DLL은 실제 소비 경로로 유지한다. 원자료·서명키·WIP·학습 체크포인트·고유 평가 증거는 삭제 대상에 넣지 않았다.
- 실행 중인 Codex·Edge의 캐시는 온라인 삭제하지 않았다. 정상 종료 후 D:/build/cache/pandolab/cache-lifecycle-cleanup-20261104/run-offline.cmd 를 실행하는 단계가 남았다. 이는 캐시 전용이며 DB·로그인·쿠키·프로젝트를 건드리지 않는다. 따라서 이 잔여 범위를 전체 완료로 표시하지 않는다.
- 이전에 정책 차단된 readonly 공유 fixture 링크 약 4,598바이트 및 손상 Git 임시 pack 약 33.6MB는 우회 삭제하지 않았다. Git 이력 재작성은 범위 밖이다.
- Windows.old, OneDrive DB, 현재 Playwright/Qt/Java/ADB와 다른 프로젝트 자료는 제외했다.
- 사용이 끝난 작업 manifest/journal/검사 로그는 이 폴더의 gzip 증거로 보관 후 임시 위치에서 제거한다. 최종 남긴 offline 명령의 크기와 마지막 드라이브 수치는 measurement.json에 기록한다.
