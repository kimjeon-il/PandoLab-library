# 저장소 교체 진행 결과 — 2026-11-05

사용자는 저장소 교체와 검증 후 옛 저장소 삭제를 승인했다. 현재 공개 코드 저장소는 새 ID 1446519692의 kimjeon-il/Pando다. 옛 ID 1436926716은 kimjeon-il/Pando-retired-20261105로 이름을 옮겨 읽기 전용 보관 중이며, 아직 삭제하지 않았다.

## 완료한 조치

1. 옛 저장소를 유지한 채 새 staging 저장소를 생성하고 Actions를 먼저 비활성화해 불필요한 전체 검사 없이 정리된 6개 heads를 정확히 전송했다. settings·Pages·Actions 권한을 대조해 복원했다. 새 clone이나 로컬 worktree는 만들지 않았다.
2. 기존 secrets 4개는 옛 저장소의 수동 Actions run 41966844856에서 원래 값의 존재, 자료 저장소 API 접근, Android keystore의 store/key password와 인증서를 확인했다. 새 저장소 공개키로 libsodium sealed box 암호화를 수행하고, 이 암호문만 받아 새 secrets API에 등록한 뒤 이름 4개를 재확인했다. plaintext를 PC나 보고서로 추출하지 않았다. YAML에서 숫자로 읽힌 key_id 메타데이터는 동일 공개키에 대응하는 API의 정확한 문자열로 사용했다. 기존 Android 인증서 SHA256은 2F:AB:34:B4:D4:E0:70:91:5C:51:57:41:68:9F:B5:34:9C:86:06:CC:03:C8:29:5B:27:3D:35:9B:D4:E6:7B:DD로 유지됐다.
3. 일회성 이전 workflow는 옛 work/remote-only의 web-pages.yml에만 적용했다. 실행 중 별도 작업의 새 커밋 dd6712842ffa08d1c41880e17ce5bc365528ebc7이 들어와 exact lease가 덮어쓰기를 거절했다. 옛 저장소를 읽기 전용으로 고정하고, 해당 원본의 4개 파일 patch·작성자·날짜를 보존한 4310a5e4cb6408409de348f5332bb60277f47971을 새 work/remote-only로 옮겼다. diff 바이트를 직접 대조했으며, 이전용 workflow는 새 이력에서 제외했다. 자동 전체 검사를 막는 [skip ci] 메시지만 추가됐다.
4. staging Pages run 41967224151 성공 뒤 이름을 전환했다. canonical Pages run 41967722086도 성공했다. 실제 https://kimjeon-il.github.io/Pando/ 의 source 6a1db6c2e87894016f98309135896ce0199537b6, data 2b8825e4570b0c1e0558f76317f4ce3d021b4f11, 전송 파일 9개와 실제 Viewer 시작·날짜 전환을 workflow에서 확인했다. Map Toolkit의 기존 immutable bootstrap URL도 동일 SHA256으로 전송됨을 확인했다. source·모델·WASM을 새로 빌드/학습하거나 전체 GIS를 재생성하지 않았다.
5. 새 운영 저장소의 refs/pull/*는 0개다. 로컬 origin 이름과 영구 worktrees는 그대로다. main과 5개 상설 작업 브랜치의 공개 커밋 범위는 replacement.json에 있다. work/gis의 로컬 전용 3커밋은 공개하지 않았다.

## 삭제 전 남은 실제 조건

브라우저에 기존 Codespace urban-lamp가 열려 있었다. 최초 캐시 화면의 변경 1개 표시는 재연결 후 없어졌고, 실제 git status는 깨끗했다. Git은 shallow이며 work/remote-only와 그 origin ref 두 개만 관찰됐다. HEAD cdfe47a309d3427dc405aee92716e12739804257의 대응 정리 커밋은 a2f73d0f30fd8a49cb9dc6639cae445c8e76cc73이고 새 원격 head의 조상이다. Codespace 자체와 현재 환경을 삭제하지 않는다. Git 소스 연결을 새 이력에 맞추고 기존 환경이 안전하게 유지됨을 확인하기 전 옛 저장소 삭제를 보류한다.

현재 GitHub CLI 인증에는 codespace 및 delete_repo 권한이 없어 해당 API를 사용할 수 없었다. GitHub가 제공한 device authorization 화면을 준비해 사용자에게 승인을 요청했다. 작업 범위 승인을 다시 요청하는 것이 아니라 GitHub 계정이 요구하는 별도 API 권한 승인이다. 실제 사용은 위 Codespace 보존과 옛 ID 1436926716 삭제로 제한한다. 삭제 완료/모든 서버 사본 제거로 표시하지 않는다.

## 완료 증거

상세 공개 상태는 replacement.json, 실제 canonical 전송 검증은 replacement-live.json에 있다. 일회성 workflow·암호문·계정 설정 원문은 로컬 제외 경로에만 보관했다. 이전에 도구 정책이 거절한 임시 출력 삭제는 여전히 미완료이며 다른 도구로 우회하지 않았다.

[GitHub secrets 암호화 방법](https://docs.github.com/en/rest/guides/encrypting-secrets-for-the-rest-api), [Codespace lifecycle](https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle). 사용자 권한 화면과 개인 계정 정보는 공개 보고서에 포함하지 않았다.
