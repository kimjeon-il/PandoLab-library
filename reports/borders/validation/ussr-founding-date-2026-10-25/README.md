# 소련 성립일 이전 표시 수정

- ID: GEO-USSR-FOUNDING-20261025
- 상태: 소련 범위 검증 완료 / work-gis-only / 공개 미배포
- 대상: state:soviet-union. 다른 국가, 좌표, 종료일은 변경하지 않음.
- 원본: Pando 65ab491ee6cf9dd2b25a4c04ede9416ee4cf896e; runtime pin 127e51c3457df87786ecf3aa5ad98ded690928df; 자료 작업 기준 c7f66909147e57976eeccb8bd897fa5fe5620e22.
- 기존 적용 기록: reports/geography/ussr-1922-caspian-application-2026-10-24/README.md. 기존 reviewed1922 좌표를 재작성하지 않음.

## 원인과 승인 범위
기존 lifetime.validFrom=1922와 before-reviewed-day 형상(1922~1922-12-29)이 모두 존재하여 연도 정밀도의 시작일 1월 1일부터 표시되었다. 날짜 해석기 오류가 아니다. 사용자가 정확한 성립일 1922-12-30으로 시작일 수정 및 성립 전 근사 형상 제거를 승인했다. 국가 존속기간을 geometry 유효기간과 분리한다.

## 수정
1. 국가 validFrom만 1922-12-30으로 정밀화. validTo=1991 유지.
2. before-reviewed-day 버전 제거. reviewed-v2 (1922-12-30~1925-05-12), after-reviewed-day (1925-05-13~1991)의 전체 내용/좌표 보존. 1925-05-13은 기존 사용자 지정 형상 선택 경계이며 새 역사적 영토변경 판단이 아니다.
3. 최초 적용 스크립트 재실행에도 성립 전 소련을 만들지 않도록 회귀 방지.
4. 원본, territorial v2 chunk/index, native library object/index, builtin runtime, packed transport를 일관 갱신. 일반 날짜 코드, 다른 국가, 해안선/호수/경계 좌표는 변경하지 않음.

## 검증
- 수정 전 실제 source 검사에서 1922-01-01에 소련이 존재하는 실패를 재현했다.
- 수정 후 소련 정확한 시작일, 성립 전 버전 부재, 1~11월 및 12월29일 부재, 12월30~31일 존재, 월별 색인 선택을 확인했다(소련 한정 1건 통과).
- 최초 적용 코드 회귀검사 1건 통과. 기존 형상/종료일 보존을 독립 읽기 리뷰로 확인.
- territorial source/chunk/index 외 다른 territorial 파일은 원본 해시와 동일. builtin 소련 geometries 배열 SHA256은 수정 전후 동일하며 다른 국가 gzip 바이트는 그대로 재포장했다.
- 최초 전세계 생성 시도는 사용자의 범위 축소 지시에 따라 종료했고 완료 산출물은 사용하지 않았다. 일반 compiler에 증분 선택 기능은 없으므로 소련 compiled lifetime, binding, sourceVersion 메타데이터 및 색인 coverage만 수정하고 packBuiltinWorldFiles로 해시/offset/transport를 재포장했다. 다른 국가 경계, 전세계 overlap/역사구간 계산, 렌더러 수정은 하지 않았다.
- prepared mesh manifest 및 payload는 원본 바이트 그대로. 런타임은 prepared-polygon-mesh.js의 SHA256([type,coordinates]) 키로 조회하며 날짜는 키가 아니다. 없으면 정상 fallback 생성한다. 원본 inputHashes는 기존 mesh 생성 출처이므로 새 생성으로 위장하여 바꾸지 않았다.
- 공개 웹/네이티브 UI E2E, 전세계 재컴파일, 전체 회귀 검증은 이번 변경 범위 밖.

## 게시 범위
work/gis만 저장. main 병합, publication release/channel 갱신, 공개 배포는 승인 범위 밖이므로 수행하지 않는다. 기존 공개 URL은 이 수정으로 자동 갱신되지 않는다.

## 동시 작업 보존
앱 work/gis의 동시 변경 61aa02a9fd098237f7ced6601db76ab4f94eeb65를 fast-forward로 보존했다. 자료 work/gis c7f66909 이후에만 저장하며 main이나 publication channel은 변경하지 않는다.
