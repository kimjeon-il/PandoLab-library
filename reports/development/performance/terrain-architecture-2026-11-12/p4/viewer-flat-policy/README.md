# 실제 뷰어의 평면 투영 제약

Actions 43188738896, 앱 `6142bd9131bb99724beccf0677b36c07085c05cb`. 실험 하네스에서 Viewer 화면을 평면으로 전환하려 했으나 `PL-PRODUCT-PROJECTION`, `The viewer supports only the globe projection.`으로 거부됐다. 실제 `src/app/product-mode-policy.js`는 제품 모드에 허용된 투영만 받아들이며, 현재 Viewer는 globe, editor는 flat이다. 첨부 명세의 평면·지구본 모두 실제 Viewer에서 비교하라는 전제와 최신 코드가 다르다.

제품 정책을 실험 목적으로 우회하거나 바꾸지 않았다. 따라서 이 실행은 평면 Viewer 화면이나 성능 증거가 아니다. 별도 시제품의 평면 역투영 및 합성 WebGL 픽셀 검사는 통과했지만 실제 편집기 화면·성능을 검증한 것은 아니다. 실제 편집기 기반 평면 비교는 별도의 실행 경로와 결과가 필요하다.
