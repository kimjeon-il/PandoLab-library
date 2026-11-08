# GEO-REVIEW-20261028-2200 — 보고서 게시 상태 정정

- 회차: 2026-10-28 22:00 UTC; 완료 검토일: 2026-10-29 UTC.
- 상태: reviewed / report-only / runtime-not-changed.
- 자료 기준: work/gis `98f41c4c7ab2ec0f07fdcc81bf21531fc7475ad0`.
- 앱 기준: work/gis `2f616b1a4518305831d45ae9623fbadeb59abfa5`; 이번 보고서 전용 수정은 앱 pin을 바꾸지 않는다.
- 전용 위치: 외부 자료 저장소의 reports/borders/validation/reviews/. 사용자 지정 work/gis만 대상으로 하며 main 전용 보고서를 가져오지 않는다.

## 확인된 수정안과 처리

대상 원문: [카스피 영토 차분 보고서](../../../reconstruction/ussr/caspian-territory-delta-2026-10-28/README.md).
검토 원본 blob: `bc0c6a323c56597afcc7e86ec3544d288e1be209` (위 자료 기준 커밋).
“업로드 승인 대기”라는 게시 상태가 실제 커밋과 충돌하므로 원래 계산 기준은 유지하고 실제 게시 이력을 별도로 명시했다.

- [자료 65fbc692](https://github.com/kimjeon-il/PandoLab-library-data/commit/65fbc692f47f7936a804e7af0eed546966898828): 커밋 기록 시각 2026-10-28 13:33:13 UTC; 부모 `d4c65479847d12f810f96b2162698dbc96d25ed7`.
- [앱 22d0b24](https://github.com/kimjeon-il/Pando/commit/22d0b24eb5916f9597f4b0c6ae4625236a6722d9): 커밋 기록 시각 2026-10-28 13:33:55 UTC; 부모 `69ee27763b75c7aca6ede227a21d1ccb090c0be7`.
- 해당 앱 커밋의 [config/library-data.json](https://github.com/kimjeon-il/Pando/blob/22d0b24eb5916f9597f4b0c6ae4625236a6722d9/config/library-data.json)은 자료 65fbc692를 참조한다.
- 원문의 c55fc510/c22c85ce는 계산 기준이며 실제 게시 직전 부모로 오인하지 않도록 표시했다.

## 중복 방지와 보류

reports/README.md, reports/geography/ 및 기존 scheduled-2026-10-25-2200 검토 기록을 확인했다. 현행 work/gis에는 새 정본 reports/borders/history/가 없으며, main 전용 LIFE-017/TIME-014를 이번 브랜치에 새 반영한 것으로 기록하지 않는다. 삭제된 과거 보고서·증거를 복원하지 않는다. 이 기록은 전체 과거 문헌의 재검증이나 모든 기존 보류의 해소를 뜻하지 않는다.

카스피 형상은 이미 게시되어 다시 적용하지 않는다. 원문의 동부 7개 조각 소유권 가정, 기존 섬 본체 미복원, 기존 기간 공백 및 동부 연구 보류는 그대로다. 국가 동일성·주권 연속성·경계 효력일을 새로 확정하지 않았고, 국가 존속기간과 형상 유효기간을 변경하지 않았다. 1801 조사 하한을 건국일로 입력하지 않았다.

기준 커밋에 포함된 [중국 접경 별도 적용](../../../reconstruction/ussr/china-frontier-application-2026-10-29/README.md)은 보존하며 이번 보고서 수정으로 재실행하지 않는다.

## 검증 범위

GitHub의 두 게시 커밋 객체에서 전체 SHA·부모·커밋 기록 시각을 확인하고 앱 pin 원문을 대조했다. 수정 범위는 카스피 README, 본 검토 기록, 보고서 색인 3개 텍스트 파일뿐이다. 런타임·형상·생성물·코드에 변경이 없으므로 GIS 재생성이나 런타임 테스트는 수행하지 않는다. 원문에 남아 있는 테스트 결과는 당시 기록이며 이번 실행의 재검증 결과가 아니다. main 병합·배포·포터블 생성은 포함하지 않는다.
