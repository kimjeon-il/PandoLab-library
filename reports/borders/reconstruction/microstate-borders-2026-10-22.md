# 안도라·바티칸·산마리노·레소토 — 1:1,000만 국경 적용 기록

> GEO-MICRO-20261022 · 2026-10-28 과잉 검증 정리 · 기존 구현: `work/gis only` / 현재 배포 확인 아님

## 유지할 필수 형상

- **안도라–프랑스–스페인:** LSIB 11.4에서 현행 공유국경과 양 끝 삼중 접점을 공동 교정.
- **이탈리아–바티칸 및 남아프리카–레소토:** 폐곡선 경계와 주변국 구멍을 일관되게 교정.
- **이탈리아–산마리노:** [이탈리아 IGM DBSN](https://igmi.esercito.difesa.it/servizi/database-di-sintesi-nazionale/)을 선택하고 [산마리노 SIT](https://mappeonline.pa.sm/arcgis/rest/services/Cartografia/castelli_GR/MapServer/1)로 별도 비교. IGM 자료의 ODbL 1.0 등 출처·이용조건을 그대로 준수할 것.

당시 C++ 검토에서 상기 국가들의 경계 접합 및 이탈리아·바티칸의 이중 구멍, 범위 밖 육지 보존과 합집합 변화 0을 확인했다. 국가 정체성·존속기간·과거 버전은 유지했다. [주요 대상 위상 검증](../validation/diagnostics/microstate-borders-2026-10-22/microstate-applied-staged-review.json)과 [산마리노 위상 검증](../validation/diagnostics/microstate-borders-2026-10-22/smr-igm-staged-review.json)을 남긴다.

작은 국가를 축척 때문에 제거하거나 존재 자체를 일반화하지 않는다. 정확한 조약 경계·원측량 연대는 추가 검증이 필요한 별도 문제다. 바티칸의 LSIB 기반 약 0.497km²와 공식 설명 약 0.44km²는 다르지만, 이 숫자에 맞춰 임의로 형상을 축소하지 않았다. 개별 1:25,000·표석급 정밀 검증, 여러 시점의 픽셀 오차 추적, 중복 대상 후보·진단 스크립트·빌드 로그·캡처는 현행 라이브러리에서 폐기했다.

주요 출처: [LSIB 11.4](https://geodata.state.gov/), [IGM DBSN](https://igmi.esercito.difesa.it/servizi/database-di-sintesi-nazionale/), [바티칸 공식 국가 지리정보](https://www.vaticanstate.va/en/state-and-government/general-informations/geography.html). 실제 운영 지오메트리·레시피와 일반 국가 위상 테스트는 이 정리에서 변경하지 않는다.

## 보관 원자료

소국 경계 조사 원자료와 출처 검토 자료는 [원자료 첨부](microstate-borders-2026-10-22/sources/)에 보관한다. LSIB 전체 다운로드 원문은 [한국 경계 조사와 공유하는 동일 판본](korea-boundaries-2026-10-21/sources/korea-lsib-11.4.zip.parts.json)을 참조한다.
