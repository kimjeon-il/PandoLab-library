# Map Toolkit0.4.2 정합 품질 수정

> 보고서 ID: `DEV-MAP-QUALITY-20261029` · 상태: `implemented-with-limitations` · 지도 반영: `not-applied` · 색인일:2026-10-29
> 원문 최종 수정:2026-10-29
> 조사 기준: app `work/ui`, baseline22d0b24eb5916f9597f4b0c6ae4625236a6722d9; source5c6fb850d9e706ef5d4e11bc6cb512c91a72689f; 최종 WASM/설치 결과는 completion.json 참조

## 대상과 기준일

기존 비공개 Map Toolkit의 OCR 문자권 선택, 도시 기호 대응, 변환 선택과 원본 픽셀 검증을 수정했다. 모델 정확도나 역사적 정확성의 합격 보고서가 아니다. macro-v6는 `pending`, `trainingOnly:true`, `releaseApproved:false`를 유지한다. 앱 main 통합, 앱 빌드·배포, 새로운 학습은 하지 않았다.

## 근거와 방법

실제 흑백 거시지도는 NRCan Atlas of Canada의 캐나다 전국 지도다. 원본841,931bytes, SHA256 `358cfad7e8329f019c820bc0b9e83b482e721eb09ebf6106d2e1580623f0b1b4`. 지도에는 Crown copyright2024가 있으나 이 사실만으로 지도 내용의 기준일을 확정하지 않았다. [공식 원본](https://ftp.maps.canada.ca/pub/nrcan_rncan/Geographical-maps_Carte-geographique/SmallScaleReferenceMaps/english_canada/b%26w/Canadab%26w.pdf), [자료 설명](https://open.canada.ca/data/en/dataset/e9ffaaa6-c8f0-4c88-be9a-5d019a919ad8), [Open Government Licence](https://open.canada.ca/en/open-government-licence-canada). 기존 자료 저장소의 동일 원본을 재사용했다.

기존144dpi 좌표계1584×1224에서 기본4MP 분석을 실행했다. Tesseract, C++/WASM, macro-v6 실제 ONNX CPU 추론을 사용했다. 원본과 모델을 교체하거나 이전 작업의 서명을 바꾸지 않았다. 현재 코드와 WASM이 바뀐 뒤에는 이전 작업을 재개 가능한 최신 작업으로 취급하지 않는다.

PDF의 검은 도시 기호를 육안 확인하고 벡터 원의 중심을 원본 픽셀로 대조했다. symbol-comparison.json의 네 사례는 개발 사례이며 독립 검증 표본이 아니다. 이미지 전체의 문자/경계 정확도를 추정하지 않는다.

원본 `/VP/Measure`에는4개 지리좌표, LPTS와 NAD83 Canada Atlas Lambert WKT가 있다. canada-reference.py는 고정 원본 해시에 한정한 개발 검증 오라클이며 제품 GeoPDF 해석기가 아니다. 기존 Python 환경의 PyMuPDF·NumPy와 pyproj3.7.2를 사용했다. 투영 좌표에서 원본4점의 affine 잔차는 각각 약0.215m다.36개 적합점과25개 분리된 셀 검사점을 고정했다. 같은 제작기관의 좌표 정보와 비교하는 보간 검사이며 독립 측량·역사 검증이 아니다. NAD83→WGS84의 서브미터 정확성도 주장하지 않는다.

## 확인 결과와 한계

- 오래된 `assets/js`/`assets/wasm` 소스 경로를 현재 `shared/frontend` 소유자로 고쳤다. 사라진 경로의 호환 사본은 추가하지 않았다.
- 실제 OSD는 Cyrillic, script confidence3.0을 반환했지만 영문 인식 probe317.97이 러시아어37.17보다 훨씬 높았다. 약한 문자권 추정을 영문 인식으로 바로잡으며 원래 OSD 근거와 각도를 따로 보존한다. 명시한 언어는 유지하고 unknown script가29개 언어를 모두 적재하지 않는다.
- 동일 원본에서 Whitehorse 기호 오차100.83→0.48px, Iqaluit30.39→0.76px, Ottawa39.38→0.62px를 관측했다. 최종 결과는 symbol-comparison.json을 따른다. Yellowknife는 OCR 상자가 실제 도시점을 포함하므로 잘못된 다른 점 대신 미해결로 남긴다. 전반적인 검출률 향상 수치로 확대하지 않는다.
- 자동 변환은 similarity/affine/projective/TPS를 기존 코어로 비교한다. 최소6점, 면적20%, 원본 픽셀 교차검증 P95≤8px 기준을 낮추지 않았다. TPS의 학습 잔차0은 합격 근거가 아니다.
- crop 검증도 실제 적용과 동일한 full-image UV 변환을 사용한다. 검증 영역 밖 기준점 때문에 접힘 검사를 건너뛰지 않는다. 잘린 영역 밖 기준점으로 coverage를 부풀려 추천할 수 없다.
- 캐나다의 기존6개 기준점은 coverage0.1907로20% 기준에 미달한다. affine 적합 RMS약380.8km, TPS 적합 잔차약0.00002m지만 독립 검증을 뜻하지 않는다.
- 제작기관의36개 좌표에서도 전국 범위 TPS 교차검증 P95약253px로8px에 실패했다. 이 결과를 자동 추천하거나 검토 완료로 바꾸지 않았다. 광범위 고위도 투영을 단순 경위도 변환/TPS로 처리하는 한계가 남는다.
- 현재 검색 seed는 Pando 표시용 승인 도시 부분집합이다. Whitehorse·Yellowknife·Iqaluit·Vancouver·Winnipeg 검색 결과가 없고, Ottawa만 있으며 Sydney는 호주 도시다. 이 색인으로 완전한 전역 위치 탐색이 구현됐다고 주장하지 않는다. 제품 진단과 스킬에 이 한계를 명시했다.

## 경계 학습과 평가 판정

evaluation-admission.json은 선택한 CIA Asia 컬러, GSI Japan 일본어 컬러, NRCan Canada 흑백 원본의 현재 라벨과7개 거시지도 원본의 family/duplicate/split을 기록한다. 선택 라벨 모두 `reviewed:false`, `source-derived-weak`, `train`이다. 일본 지도 국제경계 양성은355px뿐이며, text/frame 등의 의미 정답은 제공하지 않는다.

이미 학습에 쓴 도엽이나 색상 변형을 validation/test로 옮겨 독립 평가를 만들지 않았다. 독립적으로 검토한 제작 계열의 양성 경계·문자/격자/도곽 음성·불명확 중첩·분리된 정합 확인점이 먼저 필요하다. 새 학습, text/frame 관측 채널 승격이나 모델 승인 변경은 하지 않았다. 전체 지명 색인과 투영을 고려한 정합, 위 조건을 충족하는 별도 평가군이 후속 작업이다.

## 실제 검사와 데이터 반영

관련 검사, 최종 immutable source/WASM SHA, 비공개 설치 버전·실행 범위, 정리 결과는 completion.json에 기록한다. 사용자별 비공개 참조 ID·인증 링크·모델 가중치는 이 보고서 범위에 넣지 않는다. 이 자료를 앱 저장·재열기 또는 휴대폰 재검증의 증거로 사용하지 않는다.

앱의 일반 GeoJSON 가져오기 계약은 바꾸지 않았다. 실제 Core 기반 가져오기·편집·Undo/Redo·직렬화/재열기 검사는 관련 회귀 범위에 포함한다. 네이티브 파일 대화상자 저장과 실제 기기 검증은 별도이며 여기서 새로 통과 처리하지 않는다.

## 보관과 재현

실행은 Pando work/ui에서 한다. 외부 보고서 폴더는 원본을 중복 보관하지 않고 해시·관측·개발 검증 근거만 가진다. canada.job.json은 수정 전 기준, canada-0.4.2.job.json은 첫 수정 뒤 근거이며 최종 런타임 작업은 별도로 명시한다. 재현 스크립트는 보관한 관측을 비교할 뿐 작업 JSON의 서명을 바꾸거나 실패한 정합을 승인하지 않는다.

완료한 이 범위만 기존 publish-reports/check-reports 명령으로 원격 검증한다. 런타임 자료 pin과 모델 범위는 변경하지 않는다.

## 클라우드와 완료 판정

설치된0.4.2·고정 커밋을 새 Work 실행환경에서 읽고 공식 원본을 직접 취득했다. PC Remote 없이 실제 자동 OCR180개·ONNX12타일·경계551개·면2개를 생성했으며, 정합 미확정과 오검출을 유지해 승인/GeoJSON을 만들지 않았다. 반환된3개 파일과 다음 턴의2개 수정 파일을 실제 다운로드하고 해시를 대조했다. 수정 후 미리보기는 동일 해시여서 중복 다운로드하지 않았다.

다음 턴에서 실제 source/segmentation/rawGraph/graph/OCR/model/producer/core 해시가 유지된 채 지정 기준점 하나와 revision/history만 추가됐다. export CLI의 검토 gate 거부, 목적지·GeoJSON·완료 파일 부재도 확인했다. 클라우드 실행 경로의 회귀 통과와 지도 자동 정합/경계 정확도 합격은 별개다.0.4.2 실제 휴대폰 및 네이티브 저장 대화상자는 이번에 재검증하지 않았다.

소스58a68e11812e015cd04debdef7deb834d6869fca를 work/ui에 푸시하고 동일 비공개 플러그인을0.4.2로 갱신했다. 관련82검사와 lint가 통과했다. 전환 후 옛 소스16파일이 사라지고 주요7파일이 업로드 원문과 일치함을 원격 재열람으로 검증했다.

전달 사본2개51,771,295bytes(49.4MiB)는 자동 승인 검토의 삭제 차단으로 남아 있다. 구체적인 차단 사유는 제공되지 않았다. 같은 삭제를 우회하지 않았고, cleanup.json에 정확한 경로·명령·여유 공간 관측을 기록했다. 원본·모델·활성 런타임은 보호한다. 비교용 분석/원본 관측은 이 보고서의 현재 검증 근거이며, 모델 정확도 승인 자료로 전용하지 않는다.
