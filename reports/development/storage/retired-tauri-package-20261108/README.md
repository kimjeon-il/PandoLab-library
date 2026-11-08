# 폐기 앱 Tauri 저장소 정리 — 2026-11-08

D:/build/cache/pandolab/pnpm/store/v11/projects에서 package.json이 없는 폐기 apps/editor 경로를 가리키는 junction 5개를 링크 자체만 제거했다. 5개 상설 작업트리 링크는 유지했다. 동일 저장소 links/@tauri-apps의 cli 및 cli-win32-x64-msvc 2.12.3 패키지 view 15파일·16,517,532 논리 바이트와 그 내부 package junction 1개를 제거했다. 검사한 Pando·Map Toolkit node_modules와 글로벌 store 내부에는 제거 대상 외 해당 패키지를 가리키는 링크가 없었다.

pnpm index.db의 Tauri 두 package_index 레코드를 msgpackr로 읽고 전체 122개 패키지 색인을 대조한 결과 다른 색인과 동일한 파일 digest가 없었다. view 제거 후 대상 content-addressed 파일 15개는 각각 SHA-512·단일 하드링크·크기를 검증했다. SQLite BEGIN IMMEDIATE 내에서 두 대상 레코드만 제거하고, write-ahead journal을 기록해 해당 15파일 16,517,532바이트를 제거했다. view와 content는 같은 파일 ID였으므로 논리 바이트를 합산하지 않는다. 변경 후 index 120개, quick_check ok, journal·lock 제거를 확인했다.

시작 C 53,352,415,232 / D 47,881,773,056바이트, 정리 후 C 53,306,044,416 / D 47,898,300,416바이트. D 실제 여유 공간은 16,527,360바이트 증가했고 C는 동시 작업 영향으로 감소했다. ONNX Runtime 1.30.0과 Tesseract.js 7.0.0은 별도 D:/dev/Map Toolkit의 현재 package.json 및 설치 의존성이며 objects·GIS 작업트리에도 링크가 남아 있어 보존했다. 실제 Map Toolkit에서 두 모듈 resolve 성공, Pando에서 esbuild resolve 성공, 두 repository git 상태는 깨끗하다. 전체 검사·지도 재생성·제품 배포는 수행하지 않았다.
