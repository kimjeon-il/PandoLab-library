# 동부14 보호 근거 검토와 혼합 연구안

상태: 로컬 연구 완료, 운영 채택 검토는 미완료. 생산 source·활성 native 등록·pin·commit/push·원격 보고서를 변경하지 않았다. 기존 강한 후보 결과와 Darja 묶음도 보존했다.

추천 연구 조합은 Latvia250 + Poland250 + East기존보수적후보다. Latvia500은 비교용 대안으로 남긴다. 동부14개를500m로 일괄 바꾸는 것은 추천하지 않는다. 이는 기존 lock 전부가 조약상 의미점이라는 판정이 아니라, 알려진 의미/불확실 구간과 연산 보호를 분리할 근거가 불완전하기 때문이다. 서부 하천/육지 의미도 완전 인증되지 않았으므로 이 추천은 연구 비교안이지 운영 승인 기록이 아니다.

|feature|기존|기존 보수안|East500|현재 기록 lock|East500이 제거하는 lock|
|---|---:|---:|---:|---:|---:|
|2 Pamir-22-lower|74|67|13|66|54|
|4 Pamir-21-lower|66|65|16|58|43|
|8 Pamir-21-upper|44|40|13|33|23|
|12 Pamir-source-10|212|187|41|164|136|
|18 Pamir-source-7|61|54|13|47|35|
|20 Pamir-source-6|64|61|11|60|50|
|23 Pamir-source-4|89|70|21|59|43|
|25 Pamir-source-3|129|126|20|126|106|
|27 Pamir-source-2|21|19|7|18|12|
|35 W03-light-2|60|56|23|53|32|
|37 W03-light-3|83|56|31|35|20|
|39 W03-light-4|20|18|4|18|15|
|44 KAZ-sary-light|53|35|16|25|14|
|48 KAZ-chagan-light|83|54|24|46|27|

동부14 point entry 합계는1059→908이며,253점 강한 안보다655점을 더 보존한다. 연결된 전체 동부 route는4355→4204점이다. 각 feature의 공유 끝점 중복이 있으므로 이 합계를 세계 고유 정점 수라고 부르지 않는다. 서부는 Latvia1734→163/92, Poland1991→670이며, 이전 강한 서부와 정확히 같다. 두 혼합본의 BY/UA 전체 geometry는 해당 강한 조합과 정확히 같고 USSR/RSFSR의 동부 사슬만 기존 보수안으로 돌아간다. 지문은 mixed-comparison.json에 기록했다.

## 보호 근거와 한계

14개 모두 실제 route metadata와 새500m retained indices를 대조했다.25·27은 해시/경로와 함께 내장된 mask 전체 분류가 있으며, 그 외는 원본 mask anchor 인덱스·이전 shortcut 끝점·40도 회전 기준 및 일부 land-only 참조가 남아 있다. 구간별 겹치는 분류와 정확한 current indices는 feature-review.json/CSV, 내장 provenance는 embedded-provenance.json에 있다. 원본 master 재복구를 수행하지 않았다.

검사한 범위는256e833f... archive/index.json의 preservation-mask/land-mask 및 관련 china-frontier/remaining-display 경로, 기존 local research 참조 경로, tracked tools의 생성 필드 이름이다. 독립 mask 파일·원래 생성 코드는 이 범위에서 찾지 못했다. archive에는 적용 selected-route와 application README/recipe/verification만 남아 있었다. 미발견을 전체 디스크/모든 과거 Git 이력에 존재하지 않는다는 뜻으로 확대하지 않는다. 더 찾는 것을 종료 조건으로 삼지 않았다.

Pamir-source-3의126 보호 집합은 원래206점 mask 및 역순 retained mapping과 대응한다. 물/얼음 미확정 구간17점, 문자·기호 중첩/끝점 구간117점, 큰 굴곡/명명 앵커 묶음42점이며 중복된다. 새500m는 그 분류별15/100/25점을 제거한다. 실제 하천 추종으로 확정된 segment는0이다. 넓은 interval과 정확한 교차점 자체를 혼동하지 않았고, 명명 앵커와 큰 굴곡이 분리되지 않은 한계도 유지했다.

일부 raw-anchor 대응은 supplemental의 removedAssemblyIndices/removedRawSourceIndices 쌍과 retained 인덱스로 계산했다. 이것은 기록된 인덱스 관계의 재현이지 회수하지 못한 master 좌표·역사 지형을 독립 검증한 것이 아니다. source-mask anchor의 점별 이유가 없는 경우 unclassified로 표시했다.40degree_or_unexplained residual도 전부 순수 자동점이라고 부르지 않았다.

중요 예외: feature27 기존 보수안도 원래 넓은 uncertainty/bend-buffer 분류의2점을 제거한다. 현재 파생본의18개 lock, 식별된 물/채널 구간1점, pixel-context 큰 굴곡6점은 모두 보존한다. 이 혼합안의 보존 주장은 현재 display 계약에 한정하며, 원래 raw blanket/buffer 전체를 보존한다고 주장하지 않는다. 이2점의 의미는 미확정으로 남긴다. feature12는 source_mask_anchors가 비어 있고 raw-master allLocked 표기가 있지만, 그것만으로 의미 보호가 없다고 판정하지 않았다.

분류 결과: 현재 보수안 유지14개, source-semantic 확인을 마친 East500 채택0개, 강한 동부 후보14개 모두 provisional. 기존 표시 후보의 과거 의미 검증을 이번에 새로 인증한 것도 아니다.

## 혼합본 검증

두 혼합본 각각7개 공유 사슬을 canonical bounded-splice로 치환했다. source/native-model4개와 compiled4개 형상, 유효성·면/구멍 수·편집 범위 밖 순서 있는 좌표 보존을 검사했다. Polygon-only 구성국 겹침 변화, 구성국 변경 영역 합집합 대비 USSR 차이, source/compiled 변경 영역 불일치는 모두0이다. Atrek/Darja/IRN/USSR1925 및 물리 수역은 이전 묶음을 그대로 재사용했다. 이전에 통과한 무관한 foreign-peer·유지 사슬 GIS 계산은 반복하지 않았다.

기존 prepared owner로6개 관련 국가와1922-12/1925-06만 순차 처리했다. 각 조합31개 중24개 재사용/7개 새 생성, 총14개 새 packet decode 통과. 날짜 경계1922-12-29/30 및1925-05-12/13 총32건, 무관한 source descriptor282개·compiled descriptor274개, 기존 prepared manifest414개 항목 보존을 확인했다. 입력/출력 byte와 hash 연결은 mixed/downstream-local-audit.json과각prepared root의research-prepared-result.json에 있다.

변경된 연구 source에서 과거 passed review를 제거하고 unreviewed experiment를 기록했다. 기존 검토 게이트가8건 모두 거부함을 확인했다. 통과 receipt를 만들거나 활성 native library에 등록하지 않았다. Monaco·한국 롤백·500미만 제거는 편집 대상 밖이며 이전 묶음/descriptor를 보존했다.

## 실제 앱 표시

지원되는 buildFrontendSnapshot(readPinnedData/dataPaths)와 createP3PreviewServer 경로로 읽기 전용 연구 overlay를 구성했다. 파일 우선순위는 새 혼합본→기존 Darja 후보→현재 materialized cache다. production pin이나 마운트를 바꾸거나 서버의prepareLibraryData를 실행하지 않았다. app code는현재52725b98..., 연구 dataCommit은null이고 dataRevision은실제overlay metadata에서 계산된다.

1922-12 WebGL2 프레임이 실제 표시됐고 후보 compiled4형상이 document geometry에 정확한 hash로 존재했다. 국가114개, 페이지 오류0, 경고0. 브라우저와 로컬 서버는 종료했다. viewer-mixed-1922.png의 실제 픽셀을 열어 주요 윤곽·해안/수역·레이어 표시를 확인했다. renderer의limited 상태는자료 최고해상도 안내이며 성공/실패를 숨기지 않았다. 전세계 화면 검사이므로 고배율 접점/틈의 완전한 시각 인증은 아니다. Latvia500 대안은 앱에서 별도 표시하지 않았으며 scoped resolver/mesh 검사만 통과했다.

14-panel east14-comparison.png도 실제로 열어 확인했다. 이는 같은 local AEQD extent의 좌표 그림이며 앱 screenshot과 구분한다.

## 남은 단계와 제한

동부500m의 source-semantic 채택 검토, feature27의 원래 광범위 buffer2점 해석, 서부의 완전한 hydro 의미 검토는 미완료다. 이번 로컬 연구 결과만으로 운영 채택 게이트를 해제하지 않는다. 현재 추천은 동부 기존 표시 유지이며, 새 사료 추적이나 세밀한 지형 복원은 수행하지 않았다. 원격 반영은 이전 거절 상태이며 재시도하지 않았다.

자동 승인 검토가 기존 강한 후보 실행 스크립트 직접 수정안을 거부했다. 해당 명령은 미실행이며, 검토가 제시한 안전한 대안인 새 scratch 실행본5개를 사용했다. runner-copy-manifest.json의 원본 해시를 다시 검증하여 기존 스크립트 불변을 확인했다. 기존 prepared/splice 원격 거절과는 별개다.

현재 retained generated 파일의 소비자는 이 혼합안의 실제 앱 재현·검토 표·source/compiled/prepared 재개 경로다. 이전 강한 후보와의 비교에 필요하므로 삭제하지 않았다. 설치·SDK·네이티브 빌드·포터블/배포 패키지를 만들지 않았다.
