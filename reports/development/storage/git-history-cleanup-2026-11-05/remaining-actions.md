# 잔여 조치 검토 — 2026-11-05

## 현재 확인

- Pando 저장소 ID: 1436926716. 일반 원격 heads 6개는 정리된 이력이다. main 6a1db6c2e87894016f98309135896ce0199537b6, work/gis a30d5b9ee28a9a932cb54dd2bb435e7ce7cba1ad, work/remote-only bab7c99f748fbad8e9f77ae3a36e2cad0363c40f. UI/objects/places는 main과 같다.
- 서버 PR heads 21개 중 정리 전 이력의 17개에서 승인 코드 blob 633개가 참조된다. 17개 대응 SHA는 로컬 정확한 기록과 기존 보고서 근거를 보존했다.
- 추적 범위의 코드 633개와 자료 3,180개는 로컬 및 일반 원격 branch 탐색에 없다. 5개 작업트리의 WIP 36개 해시·상태와 자료 마운트를 이번 재개에서도 재확인했다.
- 자료 저장소에는 PR refs가 없다. 자료 저장소 삭제·교체는 필요 범위로 제안하지 않는다.

## GitHub 제약

GitHub 공식 문서는 refs/pull/*가 읽기 전용이라고 명시하고, 지원팀이 비민감 자료 삭제는 처리하지 않는다고 명시한다. 승인한 대상은 과거 생성물·GDAL/HTML이며 민감정보 유출 신고로 분류하지 않는다. PR을 닫거나 force-push/로컬 GC를 반복해도 이 서버 ref 소유권은 바뀌지 않는다.

출처: [Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository), [Deleting a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository). 확인일 2026-11-05. 저장소를 삭제해도 제3자 fork나 clone 및 GitHub의 모든 물리 백업 삭제를 보장하지는 않는다.

## 운영 저장소에서 PR 잔존을 없애는 추가 승인안

아직 실행하지 않은 제안이다. 현재 Pando를 잠시 옛 이름으로 옮겨 보존하고, 같은 주소의 새 Pando 저장소에 검증된 6개 원격 head만 전송한다. private report refs나 GIS 로컬 전용 3커밋·미커밋 파일을 공개하지 않는다. 기존 로컬 checkout과 permanent worktrees를 그대로 사용하며 새 clone이나 전체 backup을 만들지 않는다. 새 저장소는 GitHub fork 기능으로 생성하지 않는다.

Pages와 Actions 설정을 복원하고 새 저장소 ID를 사용하는 토큰의 접근 범위를 갱신한 뒤, 필요한 배포와 공개 주소를 검증한다. Actions secrets 4개(PANDOLAB_LIBRARY_WRITE_TOKEN, PANDO_ANDROID_DEBUG_KEYSTORE_B64, PANDO_ANDROID_DEBUG_KEY_PASSWORD, PANDO_ANDROID_DEBUG_STORE_PASSWORD)는 API로 값을 읽어 옮길 수 없으므로 검증 가능한 기존 로컬 원본 또는 사용자 재등록이 필요하다. 값이 없어 기능을 복원하지 못하면 옛 저장소를 삭제하지 않는다.

동일한 브랜치·자료 pin·immutable 자료 주소와 공개 사이트의 정상 동작을 확인하고 나서만, 기존 ID 1436926716을 대조해 옛 Pando 저장소를 삭제한다. 이에 따라 옛 PR/Issues/Actions/설정 등 저장소 메타데이터는 유지되지 않는다. 로컬 보존 원본·모델·자료 저장소·사용자 WIP는 삭제하지 않는다. 작업 중 서비스 전환과 재인증이 필요할 수 있다. 이 저장소 자체 교체·삭제는 단순 생성물 Git 이력 제거와 별도 범위이므로 명시적 승인이 필요하다.

## 로컬 임시 파일 거절 재확인

기존 358,184,404바이트 삭제는 미실행이다. 같은 exec_command에서 59,567,335바이트 ZIP 하나만 고정 경로로 지정하고 SHA256·부모 reparse·현재 소비자를 검사하는 좁은 명령도 제출했으나, 프로세스 생성 전에 blocked by policy로 거절됐다. 상세 사유는 제공되지 않았다. 파일 점유나 PowerShell 실행 결과가 아니라 실행 도구의 사전 차단이다. 다른 도구를 통한 삭제 우회는 하지 않았다. 작업 소유 대상의 정확한 경로·해시와 필요한 보존 메타데이터는 로컬 private-evidence에 있다.
