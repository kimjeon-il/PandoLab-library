# 저장 및 보존

선택 증거 범위 325992759 bytes / 250 files (발행 전 집계). Chromium trace·원시 JSON·화면·실패 시도·계측 판본과 재현 스크립트가 현재 보고서의 근거다.

정확한 gzip roundtrip 검증 후 중복 비압축 JSON 614352691 bytes를 정리했고, 동일 원문을 보존한 gzip 24262129 bytes를 남겼다. 논리 감소 590090562 bytes. compression 로그에 원문과 압축본 SHA/길이가 있다. D free 측정 차이는 511901696 bytes이며 다른 writer와 파일시스템 비용도 포함하므로 이 차이를 전부 회수량으로 귀속하지 않는다.

- D:/dev/worktrees/w2-p3-before: 82115303 bytes / 3772 files; 고정 A/B/최신 snapshot 재현용. node_modules junction은 합산/복제하지 않았다.
- D:/dev/worktrees/w2-p3-after: 82117944 bytes / 3772 files; 고정 A/B/최신 snapshot 재현용. node_modules junction은 합산/복제하지 않았다.
- D:/dev/worktrees/w2-p3-latest: 81702232 bytes / 3681 files; 고정 A/B/최신 snapshot 재현용. node_modules junction은 합산/복제하지 않았다.

보고서·원시 증거는 보고서 검증 소비자가 있고 세 detached worktree는 재현용으로 유지한다. 기존 W2-P2·W1 recovery와 현재 work/ui WIP는 보호되어 삭제하지 않았다. ui의 기존 WASM·manifest·branch-policy는 preflight와 SHA가 같다(preservation.json). 새 A/B/최신 tracked source는 clean이다. 측정용 서버는 종료했고 4201/4202/4203 listener가 없다. 브라우저 종료 후 소유 PID는 각 원시 memory/performance JSON에 0으로 검증됐다.
