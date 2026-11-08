# 폐기된 앱 잔여물 정리 — 2026-11-08

옛 Windows 개발 앱 2개·검증 앱 1개와 Android 개발 APK 2개를 참조하던 다섯 작업트리의 오래된 native-artifacts.json을 내용·해시·공유 저장소 잠금·실행 프로세스와 lease를 확인하고 제거했다. 각 작업트리는 검사 시 a8d24278843550b176b9d28711ca63dadf5b7220에 있었다. 기존 소유자의 retire-native 적용으로 5개 앱 뷰 논리 359,977,574바이트를 제거하고 prune-blobs로 마지막 링크 6개를 회수했다. 두 논리량은 하드링크로 중복되므로 더하지 않는다. blob 회수 단계의 D 여유 공간 증가는 359,669,760바이트였다.

각 작업트리의 삭제된 앱 전용 node_modules 링크 및 메타데이터 50항목 62,947바이트와 앱 참조 파일 2,497바이트를 제거했다. 링크 대상은 추적하지 않았다. 사용자 UI 미추적 gpu-viewer-evidence는 유지했다. C/D 전체 시작 여유는 50,251,853,824 / 47,620,976,640바이트이고 중간 확인은 50,243,874,816 / 47,980,322,816바이트였다. 다른 프로세스가 동시에 디스크를 사용하므로 전체 차이는 이 작업 단독의 확보량과 다를 수 있다.

중복되어 도달 불가능한 --retire-native 분기와 삭제된 apps/editor를 가리키는 toolchain scope 문자열을 삭제했다. storage/frontend 집중 단위검사 13개, 실제 viewer 제공 검사 2개 통과. 현재 Viewer 4개 프런트엔드 참조는 보존됨을 확인했다. 코드는 work/objects 미커밋 변경이며 main이나 배포에는 반영하지 않았다.

미완료: C Pandoeditor 자동저장 프로젝트 16.8MB와 physical-data 29.1MB는 사용자 자료로 유지. 옛 앱 staging 42.3MB, linker probe 5.1MB, D editor staging 15.6MB, 앱 검증 증거 약 2.1MB는 원본 또는 증거의 독립 보존 여부·내용이 아직 입증되지 않아 유지했다. 기존 sccache 차단 대상과 공통 GIS/C++ 도구도 유지했다. 고유 원본 증거를 삭제하지 않도록 전체 폐기 잔여물의 정리는 미완료다.

## 후속 정리 — 2026-11-08

이 섹션이 앞서 기재한 미완료 상태를 갱신한다. C 제품 staging의 291개 파일 32,551,493바이트는 현재 라이브러리 자료와 개별 SHA-256이 같음을 확인하고 삭제했다. 나머지 13개·9,725,420바이트는 현재 다섯 작업트리 또는 두 content store에서 같은 원문을 찾지 못해 유지한다.

D UI 작업트리의 옛 앱 staging은 848개 파일과 marker/evidence까지 해시·소유권을 확인했다. 독립 복구가 불확실한 3개 파일과 stage-evidence를 retired-stage-originals/에 보관하고, 고유 검증 스크린샷 및 result는 editor-canvas-worker/에 보관했다. 원격 라이브러리 d5aeb12f024a755704439e5a616ee0d00f99747a에서 바이트 검증한 뒤 기존 저장소 소유자 removeStagedDirectory로 850파일·15,578,970 논리 바이트를 삭제했다. UI WIP와 웹 Viewer 참조는 보존했다.

원격 검증된 원본과 SHA-256이 같은 옛 검증 파일 10개·2,087,398바이트를 원위치에서 제거했다. 마지막 공유 blob 66개·4,988,809바이트를 기존 pruneApplicationBlobs로 회수했고 그 단계의 D 여유 증가는 5,095,424바이트였다. staging 뷰와 blob에는 하드링크가 있으므로 논리량을 물리 확보량으로 합산하지 않는다.

검증 도구의 중복 분기와 폐기 앱 경로 설정 변경은 work/objects d4c976c70에 커밋·푸시했다. 이전 작업에서 관련 storage/frontend 테스트 13개 및 실제 viewer 테스트 2개가 통과했으며 이번 후속 작업에서 코드가 추가로 바뀌지는 않았다. main 통합·제품 배포는 하지 않았다.

linker-probe.exe 5,085,236바이트는 제작·복구 근거가 불명확해 보존한다. 사용자 Pandoeditor 자동저장과 physical-data도 유지한다. 검사 완료 상태 .last-run.json 45바이트와 빈 폴더 제거 요청은 실행 정책이 blocked by policy로 거부하여 우회하지 않았다.
