# 브랜치 변경 메인 통합 및 검증

> 보고서 ID: `DEV-RELEASE-20261102-BRANCH-INTEGRATION` · 상태: `complete` · 지도 자료 변경: `not-applied` · 색인일: 2026-11-02  
> 웹·앱 코드: `7c1c55e2a47b03177104bd4a54452692a80674b1`  
> 자료 pin: `5eb7be55208efaafe39bd5a65ec2f111d70b9053`

## 대상과 방법

기존 main과 로컬·원격 코드 브랜치의 미반영 커밋을 대조해 work/ui 로컬·원격, gpu-recovery-fix, p6-5-resource-check, p6-6-desktop-performance, p6-7-narrow-performance를 병합했다. 미커밋 작업과 독립 자료 브랜치는 보존했다. Windows 앱은 승인된 읽기 전용 검수기 전환을 포함한다.

통합 중 검수 요청 취소 후 버튼 잠김, 파일 지도와 기본 지도 전환 시 출처 표시, Windows Tauri의 절대 경로 URL 오인과 빌드 식별자의 NOTICE/LICENSE 줄바꿈 차이를 수정했다. 수동 Pages 실행은 중복 전체 자동 검사를 피하려고 사용했다.

## 확인 결과와 한계

- E2/E3/E4/E5 및 공통 지도 관련 Node 집중 검사 79개, GPU 복구 관련 검사 75개 통과. 추가 회귀 및 네이티브 계약 검사도 통과했다.
- Windows에서 변경 전후 지도 전환, 검수 패널과 실제 파일 지도 전환을 포함한 브라우저 검사 통과.
- 최종 커밋의 [E5 Windows·브라우저 CI](https://github.com/kimjeon-il/Pando/actions/runs/41390067551)는 Windows WebView2 지도·검수 패널·쓰기 차단과 웹 검수 경로를 검증했다. 원본 결과는 e5-windows/와 native-artifacts/에 포함한다. 별도 로컬 실행은 85a30edf와 1cc0eebe 후보에서 통과했으며 각 원본 JSON을 별도 보존했다.
- [Pages 배포 및 공개 검증](https://github.com/kimjeon-il/Pando/actions/runs/41390770498)이 성공했다. pages-live/live.json은 코드·자료 식별과 10개 공개 파일 바이트 검증을 기록한다. pages-browser는 공개 Viewer 시작과 연도 변경 증거다.
- 전체 테스트, 전체 GIS 재생성, 설치 패키지는 실행하지 않았다. 검수 결과는 역사 형상 정확도 승인이나 모델 정확도 승인이 아니다.

## 데이터 반영

코드 및 웹 배포만 반영했다. 런타임 지도 자료는 기존 pin을 유지했다.
