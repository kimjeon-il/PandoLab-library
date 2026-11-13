# Map Toolkit 독립 저장소 분리와 Pando 소유권 정리

> 보고서 ID: DEV-INTEGRATION-MAP-SEPARATION-007 · 상태: implemented-with-platform-blocker · 지도 반영: not-applied · 색인일: 2026-11-05
> 원문 최종 수정: 2026-11-05 · Pando work/ui: 6f1292664 · Map Toolkit: ee528ace8738d2d6795135f80bbc6b0d6598346e

## 대상과 기준

Map Toolkit 분석·학습·배포 소스를 비공개 kimjeon-il/map-toolkit으로 이전했다. 상설 경로는 사용자가 지정한 D:/dev/Map Toolkit이다. 기존 Map Toolkit의 개인 비공개 범위·이름·아이콘·동일 계정 객체를 유지하고 0.7.0 분리 릴리스와 0.7.1 안내 수정 릴리스를 업로드·읽기 검증했다. 0.7.1은 Pando 가져오기·편집 안내를 제거한다. Pando 웹뷰어는 완성된 프로젝트 열람 전용이며 플러그인은 Codex/GPT 안에서 분석·수정·파일 반환을 담당한다. Pando 직접 적용이나 폐기된 편집 UI 복원은 범위가 아니다. Pando main 통합과 앱·웹 배포는 수행하지 않았다.

## 소유권과 고정 산출물

플러그인 실행기·OCR/추론·검토·수집·학습·평가·패키징·릴리스·전용 테스트와 ONNX/Tesseract 의존성은 독립 저장소 소유다. Pando에는 공통 C++/WASM, 지명/GIS 계산, 공용 이미지·PDF·미리보기, 자료·보고서 도구를 남겼다. 지형·수계도 쓰는 세 공통 헤더/라이선스를 디렉터리 이름만으로 삭제하지 않았다. 독립 실행은 Pando 체크아웃/UI temporal.js/루트 잠금파일을 참조하지 않고, 명시적인 공용 산출물 명세를 복원한다. Pando 원본 Git 이력은 재작성하지 않았다. 이전 경로·원본 해시는 독립 config/source-origin.json에 기록했다.

공용 source504df204fb346cfec79cbda2fef75ef6607ba074, 인터페이스1, 압축 44579173 bytes, SHA256 9ee47d4ad202bcceaf7ad0de3345af8e2754b3306c0c64626728fc8cd6d40d9b, inventory a020a759d6b0b64910706888fb1334c9cb6c7f85a6696d24cb17687912d933b8. 보관 위치는 shared-runtime/이며 자료 커밋0ea41ed3b2cf5ff0b8de5665ee0c17b5aace3060으로 고정했다. 명시적 이전 핀 은퇴·활성 PID lease·변조/누락 실패를 검사했다. bootstrap SDK는 검증된046cacb4를 별도 해시로 고정한다. 기존 모델·원자료·GPU 환경·SDK는 복사/삭제하지 않았다. 자료 핀과 보고서 owner map-toolkit은 독립적이며 기존 Pando 보고서 소유권과 잠금을 보존한다.

## 실제 실행과 제한

NRCan 캐나다 흑백 거시지도의 기존 공개 파생 JPEG(2560×1979, SHA256 67825bcd24499cd6e08e2dab561e1d455ee12d6869ae290f4e4e7a4e74320e3b)를 기본4MP(2274×1758)로 새 분석했다. 실제 eng OCR과 macro-v6 WASM CPU24타일을 실행해1159선/24면을 생성했다. 자동 위치는 duplicate-control-observations로 불확실한 상태를 유지했다. 기존 검토 기준점6개와 원본에서 확인한 행정경계 획 line736만 수정·검토·내보냈다. 나머지1158선의 ID·좌표·분류·신뢰도가 전부 동일하고 원본 추론도 유지된다. Codex0.7.1 설치 캐시에서 같은 작업을 재내보냈고 geometry·source·analysis·preview·report가 일치한다. 새 Feature UUID는 실제로 달라졌으며 숨기지 않았다. current-export/는 다섯 파일과 실제 해시 명세다.

6점의 거친 affine RMS는 약380794m, coverage0.1907, 교차검증P95 미확인, recommended:false다. 이 짧은 선은 기능 검증용이며 정확한 지리 형상으로 사용하면 안 된다. 모델은 pending/trainingOnly:true/releaseApproved:false, 미관측 coast/hydro/transport/text/frame 제한을 유지한다. 독립 모델 정확도나 역사 정확성 합격이 아니다.

NRCan 공식 PDF 출처: https://ftp.maps.canada.ca/pub/nrcan_rncan/Geographical-maps_Carte-geographique/SmallScaleReferenceMaps/english_canada/b&w/Canadab&w.pdf . 원본841931bytes/SHA256 358cfad7e8329f019c820bc0b9e83b482e721eb09ebf6106d2e1580623f0b1b4. Open Government Licence Canada와 Crown copyright/NRCan 크레딧을 유지한다. PDF 저작권 표기는2024이고 발행일은 미확인이다. 컬러판과 같은 계열이라 독립 평가집으로 취급하지 않는다.

## 검사와 배포

0.7.0의 관련148계약 검사와 별도 캐시공유12검사가 통과했다. 공용 Pando59집중 검사, 최종 Viewer 범위7검사도 통과했다. 0.7.1은 영향받는 기존14파일의 릴리스 검사를 다시 통과했고, 실패/취소 뒤 실제 성공 export의 안내를 확인하는 회귀검사도 통과했다. 작은 고정 학습 입력의 손실/체크포인트/ONNX 계약은 위 CI에서 검사했으며 재학습·전체 평가를 실행하지 않았다. 전체 프로젝트 검사·로컬 컴파일러/SDK 설치·설치 패키지 생성은 하지 않았다. CI의 정확한 범위와 URL은 verification.json에 있다. 마지막 Pando 변경은 문서·등록·플러그인용 테스트 제거이며 공용 native 소스는 통과한24ba45b4와 동일하다.

개인 비공개0.7.1 소스ee528ace8738d2d6795135f80bbc6b0d6598346e, content SHA256 0cee696dbfbec547db2df8c712c07ade897184c414ed827dcfd5cf1d61f5361e; 서버에서 다시 받은277개 파일을 검증했다. 서버 정규화 manifest는 동등한 JSON 설정을, 나머지는 크기/해시를 대조했다. 계정 ID·인증 링크·모델 가중치는 이 보고서에 포함하지 않는다. Codex 로컬 설치는 map-toolkit-local/0.7.1과 독립 경로를 읽으며 이전 pando-local 등록은 제거했다. 이미 열린 채팅의 캐시 갱신까지 입증한 것은 아니다.

## GPT 실행 차단과 미검증

일반 Chat 대화 한 개에서0.7.0을 선택했으나 대화는 실행 도구와 런타임 마운트가 없다고 보고했다. 참조 메타데이터의 소스/모델 해시만 일치했고 모델 바이너리 해시·다운로드·OCR·ONNX·작업/파일 반환은 실행하지 못했다. 이는 관측된 플랫폼 접근 제한이며 런타임 코드 오류로 단정하지 않는다. 응답 표시 오류를 한 번 다시 읽었고 중복 대화·Work 자동 전환·별도 서버를 만들지 않았다. 0.7.1 GPT/Work 실제 실행, 모바일 실제 사용은 미검증이다. 이전 버전의 성공으로 대신하지 않는다. 따라서 독립 코드·로컬 실행·패키지 전환은 통과했지만 모든 GPT 클라우드 사용 흐름의 완료를 주장하지 않는다.

## 보관과 정리

공용 산출물은 live dependency로 유지한다. current-export/는 현행 출력 계약의 지정 근거, prior-execution/는 실제 실행 판본·재내보내기 UUID 근거, evidence/는 원본 획 검토·수정 명령·GPT 관측 근거다. 과거 출력 안내는 prior-execution 안의 당시 기록이며 현재 사용 지침이 아니다. 원본 지도·모델·고유 실행 증거는 보호했다. 첫 전달 사본9개568581541논리bytes(542.2MiB)는 자동 승인 검토의 삭제 차단 뒤 사용자가 직접 삭제했고 모두 부재를 확인했다. 여유 공간 변화555884544bytes에는 동시 분석 파일 생성이 포함돼 삭제량과 구분한다. 817개 지명 shard100203208논리bytes는 기존 풀 hardlink로 공유하여 중복 다운로드를 없앴다. 코드217개1497968bytes는 소유권 이전량이며 저장장치 순확보량이 아니다. 후속 정리 결과와 잔여 생성물 용도는 storage/에 기록한다.

最终清理：交付包与重复验证副本共删除 851927959 逻辑 bytes (812.5 MiB)，三组目标均已确认不存在。测得空间变化分别为 555884544、214872064、55115776 bytes；第三组间隔包含报告写入，不能当作纯删除收益。最后一次观测可用空间 48356900864 bytes。保留的大型生成物及当前用途见 storage/final.json。所有独特执行记录已按哈希保留在本报告，工作视图已删除。

보고서 전용 설정의 최종 저장소 커밋은 ecb6ee8acce3a9f82df8670fff7d951e3a399930이다. reports 범위만 허용했으며 전체 런타임 자료를 마운트하지 않았다. 0.7.1 배포 소스 ee528ace8738d2d6795135f80bbc6b0d6598346e와 패키지 지문이 정확히 같아 중복 업로드를 생략했다. checks/report-config-fingerprint.json 참조.

## 보관된 선택 검토 근거

[당시 선택 검토·독립 계산·입력 근거](prior-execution/native-prototypes/)를 보관한다. 이는 과거 작업의 원문이며 현행 실행 API나 현재 배포 패키지의 검증 완료를 뜻하지 않는다. 원문에 출처가 없는 입력은 출처 미확인 상태로 유지한다. 기존 정본 소스와 현재 자료·패키지 pin은 이 첨부로 바꾸지 않는다.
