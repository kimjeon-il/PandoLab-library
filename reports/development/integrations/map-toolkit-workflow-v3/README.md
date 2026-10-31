# Map Toolkit 0.6 실제 사용 흐름 검증

> 보고서 ID: DEV-MAP-TOOLKIT-WORKFLOW-V3-20261030 · 상태: partial-validation · 지도 반영: not-applied
> 기준일: 2026-10-30 · 비공개 Work 설치: 0.6.3 · 실행 소스: 749c15490c778b28403d18ef1d2ad883955ffa4f
> 완료 범위: 구현·집중 회귀·설치 대조·캐나다/유럽 실제 내보내기·Pando 브라우저 검증. 최신 그리스 Work 완료와 휴대폰 다운로드는 요청 제한으로 미확인.

## 결과와 남은 차단 조건

기존 분석·작업·수정 소유자를 확장해 원본 픽셀 벡터 편집, 단조 증가 ID와 changeSet, 선택을 공유하는 GeoJSON/PNG, schema3와 실패 시 작업/PNG 보존을 구현했다. 별도 분석 엔진·서버·Pando 전용 화면을 추가하지 않았다. 기존 macro-v6의 pending, trainingOnly:true, releaseApproved:false와 미관측 채널 제한을 유지했다.

공식 비공개 설치를 0.6.3으로 갱신하고 설치 아카이브의 211개 파일을 대조했다. 두 호스트 manifest는 설정의 의미를, 그 외 파일은 실제 바이트·크기·SHA256을 검사했다. 공개 코드·모델을 바꾸거나 서명을 우회하지 않았다. 설치 대조는 실제 Work 처리 완료와 구분한다. [installed-063-receipt.json](installed-063-receipt.json) 참조.

0.6.3의 새 실제 Work 요청은 만들었지만 이후 PC의 새/기존 대화가 “대화를 불러올 수 없음”으로 표시됐다. 제한된 UI 복구 시도로 해결되지 않았고, 사용자가 휴대폰에서도 노란색 “요청이 너무 많음” 알림을 확인했다. 추가 요청·중복 분석·API/서버/다른 계정 전환을 하지 않았다. 이미 만든 대화를 먼저 확인한 뒤 그리스 내보내기와 다음 턴/휴대폰 파일 반환을 재개해야 한다. 이 상황에서 0.6.3의 실제 OCR·추론·내보내기를 통과로 기록하지 않는다. [work-063-service-limit.json](work-063-service-limit.json) 참조.

## 구현과 집중 검사

- C++ 정본 경계망 편집기가 원본 픽셀 벡터를 직접 수정한다. 무관한 선의 좌표·분류·confidence·ID를 유지하며 추가·분할·병합에 새 ID를 할당한다. 면은 현재 공유 경계망에서 구성하고 변경 ID를 기록한다.
- 정본 선택 해석을 먼저 검증한 뒤 선택 부분만 투영한다. 검토 뒤 PNG와 GeoJSON이 같은 선·면·구멍 범위를 사용한다. 검토 전에는 진단 후보를 표시한다.
- schema3 서명과 자료/모델/producer 검증을 유지한다. 기존 .part 예약 및 작업/PNG 쌍 저장으로 정상 오류·취소 시 이전 성공 파일을 보존한다. 강제 종료·전원 손실·환경 만료 복구까지 보장하지 않는다.
- 최초 기능 검사 41 Node, 그래프11, 코어/정합/투영/패키지56, 실제 PNG 픽셀2가 통과했다. 검사군은 중복되므로 합산하지 않는다. 독립 검토에서 발견한 선택 외 투영·파일 충돌 문제도 재현 후 수정했다.
- 최신 고정 소스의 workflow/graph/region-atomic/package 35개와 변경 JS ESLint가 통과했다. 새 사례는 실제 analyze의 두 호 보존, 소수점 끝점의 방향4조합·반복 rebuild, 끝점 가까운 별개 교차점의 정상 분할을 포함한다. [focused-checks.json](focused-checks.json) 참조.
- 필요한 WASM만 원격 CI에서 재생성했다. [CI41068002945](https://github.com/kimjeon-il/Pando/actions/runs/41068002945)는 성공했고 생성커밋은 ffd119d5857daa2d1fe9f3fd2a86d6858718e4bf다. 실제 로딩 source SHA는 1c2fc8330475703b3cc1ede8edf768c7e0771234e4ddf1d43688422cc2c9eca0, WASM SHA는 105cac16c2af6b868471ecf521a29ff1bcdca8d556841f64f74c3eab651f287a다.
- 해당 push의 기존 P1은 공통 native-core 검사만 수행하고 native-artifact/wasm-compile/web-smoke/GIS 도구는 건너뛰었다. P3의 브라우저/스냅샷/계산 성능 작업도 건너뛰었다. 이를 실제 Windows·Android 앱 통과로 해석하지 않는다. 로컬 전체 suite·전체 GIS·앱 설치 패키지는 실행/생성하지 않았다.

## 실제 지도 결과

원본·판본·권리·내용연대의 불확실성은 [source-inputs.json](source-inputs.json)에 기록했다. 공개 회귀 지도이며 새로운 독립 모델 평가군이 아니다.

| 입력 | 실제 확인 범위 | 근거 |
| --- | --- | --- |
| 페르시아어 캐나다 지도 URL | 0.6.0에서 실제 fas OCR·9/9 WASM CPU 타일·51.813초. 다음 턴 revision0→7 수정 후 선1개와 공유 경계의 인접 면2개를 선택하고 실제 정본5파일 다운로드·해시 확인 | canada-initial-receipt.json, canada-export-receipt.json |
| NRCan 흑백 유럽 PDF 첨부 | 0.6.0에서 eng OCR·12/12 타일·42.4초. 공선 기준점 실패의 review/export 거부를 확인한 뒤, 제한을 명시한 수동 정합으로 기준점 범위 안의 line:791만 검토·내보냄. 실제 정본5파일 해시 확인 | europe-initial-receipt.json, europe-export-receipt.json |
| Mitchell 그리스 역사 지도 자연어 검색 | 실제 검색·원본 SHA·권리 확인. 0.6.0/0.6.1은 겹침 보호 오류로 실패. 0.6.2 새 기본4MP 작업은 실제 eng OCR256개·25/25 타일·9,644개 호/854개 면·후보PNG 생성 성공(145.843초). 다음 턴의 ID 보존 위반으로 export 중단. 0.6.3 수정본의 실제 Work 완료는 요청 제한으로 미확인 | greece-062-initial-receipt.json, greece-062-edit-failure-receipt.json |

캐나다는 원본 별 기호14개와 고정 GeoNames 좌표를 사용한 수동 LCC 가설이다. affine CV P95 9.265px가 자동 기준8px를 초과했고 TPS도 채택하지 않았다. 원래673개 선 중655개는 모든 속성이 같고18개 대상/교차 구간만 대체됐다. OCR·원래 rawGraph·resources는 불변이다. 두 면은 chain675/677을 공유한다. 수동 호수선을 모델의 미관측 coast/hydro 인식으로 표시하지 않았다. 남쪽 외삽과 독립 경계 정확도는 미확인이다.

유럽은 원본의 Arctic Circle 표기와 실제 경선 교점을 사용했다. 위도 숫자가 원본에 인쇄돼 있다고 주장하지 않고 [NSIDC](https://nsidc.org/learn/cryosphere-glossary/arctic-circle)와 [NOAA](https://pmel.noaa.gov/arctic-zone/faq.html)의 근사 정의를 보조로 기록했다. fit6점·같은 출처 확인2점 잔차4.37/0.62px, 분포0.0796, 내장CV 미산출 및 추가 LOO P95 57.39px인 수동 geographic+TPS다. Winkel II 구현이나 독립 정확도 합격이 아니다. 원래790개 선·OCR·rawGraph·resources는 불변이며 선택한 북유럽 한 선 외에는 승인하지 않았다.

정본 출력 이름은 features.geojson, preview.png, analysis.json, report.md, complete.json이다. 초기 검증 요청에서 잘못 부른 completion.json은 제품 계약/호환 별칭으로 추가하지 않았다. 국가·이름·귀속·유효기간은 자동 확정하지 않았다.

## 그리스에서 실제 발견한 두 오류

첫 오류는 서로 다른 경계 호를 독립적으로 단순화하면서 같은 현으로 겹치게 만드는 문제였다. 같은 원본·모델·기본3998075픽셀의 기존 엔진 진단에서 실제 충돌 두 호를 확보했다. 초기 픽셀 마스터의 단순화만 끄고 원래 겹침 거부는 유지했다. 로컬 진단 시간은 Windows 값이며 Work 성능으로 보고하지 않는다. [greece-overlap-two-arcs.json](greece-overlap-two-arcs.json), [greece-061-failure-receipt.json](greece-061-failure-receipt.json) 참조.

이후 0.6.2 실제 Work 분석은 성공했지만 후보4615 제외 시 멀리 있는 동일 형상의9644가9645로 바뀌었다. 기존 끝점의 교차 매개변수가0.9999999999999999인데 좌표는 정확한 끝점이라, 가짜 분할 뒤 새 ID를 만드는 수치 문제였다. C++ 정본에서 정확히 같은 끝점 좌표에만 정확한 끝점 매개변수를 사용하도록 수정했다. 근처의 별개 교차점을 epsilon으로 합치지 않았다.

새 WASM으로 실제 이전 baseline 경계망을 순수 코어 회귀 입력으로 읽어,4615만 제거되고 나머지9,643개 선이 모든 속성과 ID까지 같음을 검증했다. 다시 rebuild해도 changeSet은 비었고 nextChainId도 유지됐다. 과거 job을 새 버전 작업으로 재서명하거나 내보낸 것이 아니다.

실제 Work의 실패 결과는 승인/export하지 않고 보존했으며, 서명된 원본 복원과 기존 revise로 정합만 적용된 revision1을 유지했다. fit6/withheld5, geographic+경험적 projective 가설의 내부CV P95 30.69px, 같은 출처 withheld P95 14.54px는 자동 합격이 아니다. 후보 해안은 원본 검토안일 뿐 적용된 결과가 아니다. [미적용 원본 검토 이미지](coast-unapplied-source-review.png)와 [실패 근거](greece-062-edit-failure-receipt.json)를 구분한다.

0.6.2 최대RSS는 Linux 자식 프로세스 최대값1,438,440KiB이며 동시 process-tree 합계나 휴대폰 메모리가 아니다. 전체 채팅의 검색·시각 검토 시간과 엔진 analyze145.843초도 구분한다.

## Pando·휴대폰·네이티브

실제 캐나다 GeoJSON d22565a1e302a6fb1470503e39c6282ea209fe7431e9c0065cefba289c728ff5로 기존 브라우저 흐름1개가 통과했다(57.3초). 일반 객체3개 가져오기, 일괄 Undo/Redo, 격리된 테스트 문서의 기존 수계 편집기를 통한 선 꼭짓점 수정·Undo/Redo, SQLite GeoPackage 저장·재열기와 출처 보존을 확인했다. 실제 경계를 강으로 분류한 것이 아니다. 저장 파일143,360바이트/SHA8263577d17a33590d07308cc5990a6761b6a7e53b9c0ab676b73eac0b6876e1b 및 명세/화면은 canada-browser/에 있다.

휴대폰0.6.2 후속 요청은 승인 없는 revision1·review:null gate에서 거부됐다. 사용자 보고로 새 폴더/정본/UUID가 없고 기존 job/PNG가 바이트까지 유지됐음을 기록했다. 이는 성공적인 export/download 검증이 아니다. 0.6.3의 휴대폰 확인은 요청 제한 알림에서 멈췄다.

Windows 정본 바인딩의 공유 캐시에 이전 개발 실행기는 있지만 입력2596d458…가 현재 보호 중인 네이티브 입력0c638b81…와 다르다. 불일치 실행기를 강제로 사용하거나 다른 작업의 변경을 빌드/덮어쓰지 않았다. 현재 adb에는 연결 기기가 없고 설정 SDK에 emulator 실행 파일도 없다. Windows 및 가로 Android 네이티브 검증은 pending이다. [platform-availability.json](platform-availability.json) 참조.

## 정리와 보관

배포용 폴더·ZIP·계정 아카이브·진단 텐서·해시 중복 파일 등 합계425,419,493 논리 바이트(405.71MiB)를 제거했다. 이 합계에는33,674,457바이트의 고유 초기 작업 근거를2,616,296바이트 gzip으로 압축하고 원본 바이트를 대조한 단계가 포함된다. 원본 지도·모델·미완성 변경·상설 작업공간은 보호했다.

논리 삭제량과 삭제 구간의 드라이브 여유 변화는 다르며 동시 활동/할당 차이를 포함한다. 전체 작업 전후 변화나 확보 공간을 논리량으로 대신하지 않는다. 세부 대상·관측 가능한 전후 수치·측정 누락은 [cleanup.json](cleanup.json)에 있다.

비공개 검증 경로의 실제 출력·서명 baseline 압축본·설치 화면 등22개 파일 약7.55MiB는 실제 작업 불변/실패 재현/사용자 결과 근거다. 별도 캐나다 다운로드 ZIP은 전체 수정 감사·원본 명세 근거이며 모델 가중치나 설치물 사본이 아니다. 계정 식별자·대화 URL·인증 링크·모델 가중치를 공개 보고서에 넣지 않았다.

이번 소스는 work/ui에만 반영했다. 앱 main 통합·앱 배포·공개 플러그인 제출·재학습을 하지 않았다. 요청 제한 해제 후의 기존 Work 결과 조회, 그리스 정본5파일과 최신 휴대폰 재내보내기/다운로드, 접근 불가능한 두 네이티브 검증이 남아 있다.


## 2026-10-31 일반 Chat 추가 검증 — 일부 통과, 전체 미완료

Work 전환 없이 일반 Chat에서 기존 Map Toolkit 0.6.3을 선택했다. 실제 Ubuntu24.04.3/Node24.22.1/Python3.12.14 실행, 설치된 release448바이트의 해시, 실제 ONNX16,697,571바이트/SHA04ee59b0… 대조와 기존 WASM 로더 초기화(source1c2fc833…, exit0)가 통과했다. contentSha256는 기록된 릴리스 필드와 대조했으며 이번에 전체 설치물 콘텐츠 해시를 재계산했다고 주장하지 않는다. [환경 근거](chat-063-environment.json).

새 그리스 job 하나의 실제 eng OCR 저장256개, 기본2215×1805=3,998,075픽셀, ONNX WASM CPU25/25타일,9,644chains/854faces 분석이 통과했다. CLI 전체124.356초에는 런타임 준비·OCR·추론·저장·미리보기가 포함된다. 자동 정합은 duplicate-control-observations 실패로 유지됐다. 최초 revise는 정상 종료한 analyze의48바이트 잠금이 남아 EEXIST로 거부됐고, 원본 job33,674,206바이트/SHAfb798d1e… 및 전체 경계·OCR·rawGraph·resources·서명은 그대로였다. 실제 내려받은 진단71,498바이트/SHA4edc2184…를 대조했다. [초기 분석·실패 근거](chat-063-first-revise-failure.json).

작업 소유 프로세스·열린 파일·절대경로·일반파일·해시를 다시 확인한 고아 잠금 하나를 정상 unlink로 정리해 같은 job에서 이어갔다. 새 분석·코드/모델 변경·재서명은 하지 않았다. 후속 Chat 진행 기록에는 수동 projective 가설(CV P95 30.6933px, 같은 원본 withheld P95 14.5414px, 자동 recommended:false),4615번 선 제외와 나머지9,643개 선 보존이 나타났다. 그러나 이 후속 단계의 최종 진단·정본 파일은 아직 받지 못했으므로 최종 회귀 합격으로 확정하지 않는다.

기존 후속 요청은 응답 중 표시만 남아 있으며 추가 대화·중복 분석을 만들지 않았다. 수동 해안 add·최종 검토·정본5파일 다운로드 및 다음 턴 수정/재내보내기는 미확인이다. 일반 Chat 사용 가능과 실제 분석 통과를 전체 무개입 작업 흐름 통과로 확대하지 않는다. 남은 잠금/중복 part 및 응답 대기의 원인이 제품 코드인지 클라우드 실행환경인지도 미확정이다. 별도 이전 증거 압축본은 후속 검사에서 손상/해시 불일치가 보고되어 내려받거나 합격 근거로 채택하지 않았다. [후속 상태와 정리 기록](chat-063-continuation-status.json).

이번에는 소스·버전·배포본·학습·앱 빌드를 변경하지 않았다. 로컬 삭제0바이트, 확인된 클라우드 자기 잠금 정리48바이트이며 추가 클라우드 정리는 최종 결과 미수신으로 확정하지 않는다. 현재 job·snapshot·임시 저장물은 활성 검증의 소비자가 있어 보호한다. 실제 드라이브 여유 변화는 동시 활동을 포함하며 확보 용량으로 보고하지 않는다. 휴대폰 일반 Chat과 Windows/Android 네이티브 미검증은 그대로 남는다.


## 2026-10-31 후속 응답 수신·실제 파일 검증 — 첫 export 통과, 최종 저장 실패

앞 절의 응답 대기 상태를 후속 결과로 갱신했다. 일반 Chat의 첫 수동 해안 export 정본5파일과 최종 진단을 실제 다운로드했고,6개 파일의 크기·SHA-256 및 complete.json의4파일 해시를 대조했다. analysis.json33,671,534바이트/SHAdee516eb…의 schema3/revision5/reviewed 상태와 기존 계약의 서명을 읽기 전용으로 재계산해 확인했다. 선택은 line:9644 하나이며, GeoJSON15,293바이트/SHAd0aacdf5…는 열린 LineString1개·투영 좌표13개다. 원본 픽셀 마스터10점, 수동 origin/semanticBits4, 자동 추천false와 모델 미검증 상태가 유지됐다. 실제 PNG10,741,020바이트/SHA0388fd62…도 육안 확인했다. [파일별 해시와 판정](chat-063-export-receipt.json).

후속 affine→projective의 실제 revision6·7에서 review 무효화와 graph/OCR/rawGraph/resources 불변이 진단에 확인됐다. 그러나 마지막 review가 exit0/revision8/reviewed를 출력한 뒤 실제 current.job.json과 .part는 모두0바이트였고 JSON 파싱이 불가능했다. 두 번째 export는 실행하지 않았으며 손상 상태를 복원·재서명·재실행하지 않았다. 원래 저장 문제의 근본 원인은 미확정이며, CLI 성공 출력만으로 저장 성공을 판단할 수 없다는 실패 근거다. 첫 성공 export는 이 손상 상태와 별도로 보존돼 있다.

클라우드 정리는 실제 성공4회/삭제7건(잠금3개·정본과 같은 .part2개·빈 디렉터리2개), 논리 파일67,338,318바이트이며 삭제 정책 거부0회다. 수동 유지보수 없이 전체 흐름이 통과한 것은 아니다. 실제 드라이브 확보량과도 구분한다. 로컬은 다운로드 사본을 검증용 고정 폴더로 이동해 중복을 남기지 않았고, 유일한 첫 성공 출력·서명·진단6파일44,521,250바이트는 작업 손상 조사 및 결과 재검증의 근거로 유지한다. 공개 보고서에는 개인 Library 링크·계정 ID·클라우드 작업 경로·원본 작업 전체 JSON을 넣지 않았다. 소스·버전·배포본은 변경하지 않았다.

남은 우선 작업은 같은 클라우드 파일시스템의 기본 write/close/rename/unlink 동작과 정본 저장 트랜잭션의 경계를 최소 입력으로 재현해 원인을 분리하는 것이다. 근거 없이 제품 코드나 클라우드 환경 중 한쪽을 원인으로 단정하지 않는다. 최종 저장·같은 대화 재내보내기와 기존 휴대폰/네이티브 미검증은 계속 미완료다.

최종 응답을 받아 사용이 끝난 임시 UI 화면1개·텍스트2개를 해시/경로/비링크 여부 확인 후 정리했다(197,830 논리 바이트). 이 삭제 구간의 D: 여유는200,704바이트 증가, C: 여유는4,931,584바이트 감소했으며 동시 활동을 정리 효과로 간주하지 않는다. 유효 첫 export·최종 진단6개44,521,250바이트는 서명된 작업과 저장 손상 조사에 필요한 현재 근거로 한 사본만 유지한다.
