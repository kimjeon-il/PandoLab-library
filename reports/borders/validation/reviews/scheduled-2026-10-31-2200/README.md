# GIS 보고서 자동 검토 — 2026-10-31 22:00 UTC

> ID: GEO-REVIEW-20261031-2200 · 상태: reviewed / important-holds · 지도 반영: report-only / runtime-unchanged

## 기준과 중복 방지
- 이전 완료: `0fb896410458d6671d93e491761c9cea32a0d749`, [10월 29일 처리 기록](../scheduled-2026-10-29-2200/README.md). 기존 Caspian·BY/Ukraine 정정을 반복하지 않는다.
- 관측 데이터 work/gis: `a3872b373584d06f20da1975f82739c9b6210f1a`; 앱 work/gis: `fc4599400cd6d847fa445adc2efec211ff849fda`. 앱 pin은 같은 `a3872b3`이다.
- latest AGENTS의 외부 데이터 보고서 소유권과 borders/reconstruction·validation 위치를 따른다. 이번 사용자 지시의 work/gis 한정 범위를 지키며 main 게시·병합은 하지 않는다.
- 이전 완료 tree 8767개와 현재 tree 9254개를 경로·blob으로 대조했다(모두 truncated=false). 변경 보고서 23개, 삭제 0개. legacy geography 및 borders/history 신규 변경 없음. 과거 기록은 원본으로 보존한다.

## 보고서별 판정·수정안
### 북캅카스 현대선 근사
원본 보고서 추가 커밋: `5ff5bd8f941f53a2f55787aa17665277226224b2`(앱 생산자 `56c72cd4e8c0bf82f6809d35c3cd7fe593423282`). 해당 커밋의 RSFSR·TSFSR source/compiled/index/transport 변경과 보고서 게시를 확인했다. 이미 게시된 작업으로 분류하여 재적용하지 않는다. 이번 검토는 과거 위상 검사를 재실행하거나 1922년과 현대선의 역사적 동일성을 인증한 것이 아니다. 서단 산악 연결부와 사무르 하류 보류, 사용자 승인 표시 근사라는 구분을 유지한다.

### 러시아–카자흐스탄 A–H
보관 원본 커밋: `de3f724f0b89d2232ed0d9411bb55a23164d3b41`, 기준 `c73d3f562d35f92d749458c9890bec02875ff605`. 보고서의 runtime-not-applied와 사건경계 비교 컨테이너 설명을 유지한다.
- A–C 기본 복원은 기존 조사·독립 검사 기록이 있는 적용 후보다. D–F는 SK-42 가정의 별도 조건부안, G/H는 보류다. 보관 보고서 안의 명령이나 승인 주장을 새 권한으로 사용하지 않는다.
- 현 원격 RUS/KAZ source 생성 청크 blob은 기준 c73d3f5와 완전히 동일하다: RUS `07f8d5ecb8270f1dbe9df31aea3562e19c6fe25d`, KAZ `4fd975d7ff62a410bf72de5fa3c7a4a2d169c8a8`. KAZ JSON도 직접 읽어 두 versionId·기간·geometry hash가 같음을 확인했다. source의 2006 사건경계 적용은 확인되지 않으며, 보고서 보관을 생산 반영 완료로 표시하지 않는다. 모든 런타임 transport를 해제·검사한 것은 아니다.
- de3f724 뒤 b9dc780→185857c→a3872b3가 추가되었고, 앱 `7868239264c6ecfc8449095b99db0a2ebe9f7759` 뒤에도 국명·국기 작업이 누적됐다. 옛 수동 패키지의 expected-base 검사를 우회하거나 그대로 재실행하면 동시 변경을 훼손할 수 있다.
- 적용안: 최신 원격 위에서 A–C의 두 대상·관련 기간만 재검토한 뒤 source/native/compiled/transport를 일관되게 게시해야 한다. 현 자동화에서는 기존 대형 blob 16MiB 전송 및 HTTPS 인증·네트워크 제한이 해결됐다고 가정하지 않으며 재시도·패키지 재제작·사용자 PC 실행을 하지 않는다. 최신 기반 충돌 검토와 최종 transport 게시·검증 미완료로 데이터 반영을 보류한다.
- 조약 2005-01-18 서명, 2006-01-12 발효, 2006-01-24 발표 구분은 원본 보고서의 근거 기록을 유지하며 이번에 외부 원문을 새로 검증했다고 주장하지 않는다. 발효 전 시작일·필지별 실물 인계일은 미확정이다. 1991년으로 임의 소급하지 않는다.
- 국가 존속기간과 기하 선택기간은 독립적이다. 1801 조사 하한을 건국일로 쓰지 않는다. 다른 시기의 경계가 남아 있는 비교 컨테이너를 전체 역사 국가 스냅샷으로 승격하지 않는다.

## 원본 보관 파일 대응·한계
원문 ENGINEERED-REPORT는 조사 당시 서술로 보존한다. 거기에 적힌 .geojson 네 파일의 게시본은 동일 상대 위치의 `.geojson.gz`이며, 비교 그림 게시 위치는 보고서 루트 `six-panel-period-comparison.png`이다. 원문이 언급한 `02-reverse-*.geojson` 중간 단계와 재현 코드는 이 보관 범위에 게시되어 있지 않다. 현재 저장소에서 이 파일들을 내려받거나 전체 재현할 수 있다고 주장하지 않는다. 이러한 포장 차이를 좌표나 검증 결과의 변경으로 해석하지 않는다.

## 경로·원본 변경 이력
아래 23개는 0fb8964→a3872b3의 보고서 delta다. 러시아 접경 묶음 및 색인 추가는 de3f724, 북캅카스 README는 5ff5bd8이다.
- `reports/README.md` — blob `8427d5415d3e3bc5d9db775c5c7497d257f072ef`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/ENGINEERED-REPORT-ko.md` — blob `dc9f7e5384f09b3d6aab01e60b3b031d533fbbe1`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/README.md` — blob `7407d437424a73244714543e98e3f22973bdc8a4`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/conditional-ABCDEF-periods/01-post-2006-RUS-KAZ.geojson.gz` — blob `14ca3c11aa0166021dc108c9c92a8dab34598070`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/conditional-ABCDEF-periods/03-pre-2006-RUS-KAZ.geojson.gz` — blob `bcfbd06c34f93b3439d9db72c16890e4f8d1b425`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/conditional-ABCDEF-periods/D-source-and-engineered-lines.geojson` — blob `20ed392ee6352fe3156e2379d5a805db3cd17f1e`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/conditional-ABCDEF-periods/E-source-and-engineered-lines.geojson` — blob `8974ec6ac2ca0b420285ff830f538d45979d9721`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/conditional-ABCDEF-periods/F-source-and-engineered-lines.geojson` — blob `d54900e27071166a023a86ffb0791ac8a65eb29d`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/conditional-ABCDEF-periods/independent-qa.json` — blob `14acaf4b8c18f6a8c359ec26ec781970438f6f6e`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/conditional-ABCDEF-periods/validation.json` — blob `8d904f5c196b1ce9a6bea84264ba573a7382da18`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-event-ledger.json` — blob `088d73e57d66f1746f79a297997d8ce65aeccbba`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-periods/01-post-2006-RUS-KAZ.geojson.gz` — blob `30b5943f06e3ff4e25dc7b8f3eabcbd1c0941429`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-periods/03-pre-2006-RUS-KAZ.geojson.gz` — blob `3168d0ac7f0961e253883e52439e8220f2698668`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-periods/A-source-and-engineered-lines.geojson` — blob `da94b533c357ae868349ff185bcdb3472ac58d47`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-periods/B-source-and-engineered-lines.geojson` — blob `5ee259cb5ef9c43f35e227d514a56c81204fc429`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-periods/C-source-and-engineered-lines.geojson` — blob `0698ab920f51961b1fc8fb4ff33a7680ee2b2181`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-periods/independent-qa.json` — blob `d590bc6a58d7d14fd0c64a2c8df6df9eb5a04d98`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-periods/validation.json` — blob `4835359143f57bd6e77bd28397307f742b1586c8`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineering-anchor-review.json` — blob `1b84a5f132708ec4dc6c6e7bf5adbb4d12f5ddfc`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/engineering-review-D-H-east.json` — blob `1caa4678b8242bbc5bca66f0ae1120996cd5309d`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/remote-snapshot.json` — blob `aeba8186b76330fa895f8bc7640f905da803e544`
- `reports/borders/reconstruction/russia-frontier-1991-2026-2026-10-31/six-panel-period-comparison.png` — blob `3266c2dfa5313d11ed238bdf9da2b93dd1adcfdc`
- `reports/borders/reconstruction/ussr/north-caucasus-modern-2026-10-30/README.md` — blob `415ec293e341532625a317a22c72e49f1abeb46f`

## 처리 결과와 실제 검사
이 처리 기록과 reports/README.md의 색인 행만 게시한다. 기존 원본 보고서·후보·데이터·앱 pin은 수정하지 않는다. source 경로·커밋 이력·두 청크 blob 및 KAZ의 실제 JSON 비교, 보고서 경로 존재·delta 범위를 검사했다. 역사 좌표의 새 시각 검토, 이전 독립 위상 검사, 전체 테스트·브라우저·배포는 실행하지 않았다. 최신 원격을 다시 확인하고 expected SHA 및 force=false로 두 문서만 fast-forward 게시한다. 대형 blob 재전송, main/다른 브랜치 변경, 무명 수계 조사, 포터블 생성은 하지 않는다.
