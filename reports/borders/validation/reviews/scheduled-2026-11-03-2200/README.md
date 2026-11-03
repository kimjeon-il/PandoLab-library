# GIS 보고서 자동 검토 — 2026-11-03 22:00 UTC

- ID: GEO-REVIEW-20261103-2200
- 상태: reviewed / supplemental-corrections / important-holds
- 지도 반영: report-only / runtime-unchanged
- 검토 기준: Pando main `eb707ab16deb4bbd1ca2d47355560ac6d6edca9d`, work/gis `04e2c2080b37b6c142515721087b7009b3947bc1`; data main `4dfc9729cf6a206db72b2a3140b1cd66cbf7f356`, work/gis `526464c099f0136ae8be271ec8c21638847b0ff9`.
- 이번부터 양 저장소 main 및 work/gis를 모두 읽는다. main은 읽기 전용이다. 수정안과 처리 결과만 data work/gis에 보관한다.
- 이 기록은 아래 원본의 보충 정정판이다. 원본은 그대로 보존하며 통째로 복사·병합하지 않는다.

## 1. 변경 이력·중복 확인

Pando 양 브랜치 전체 tree는 truncated=false이고 reports/ 파일은 0개다. 전용 정본은 외부 자료 저장소 reports/borders/다. reports/geography/는 data work/gis에만 남은 과거 경로이며 main에서 새 자료가 없다는 판정 근거로 삼지 않았다.

직전 work/gis 검토 커밋 29493ff457bd40a470abafc233940caf55effae7 이후 3개 커밋에는 보고서 변경이 없다. Hydro 및 준비 폴리곤 생성물 변경은 이번 국가·시대별 보고서 검토 대상이 아니므로 수정하지 않는다.

이전에 검토한 main 원본 81593cc21eb644ead44dcb8115bbc73c57c474b9와 현재 main의 borders/history tree를 직접 비교했다(truncated=false). 새 본문 4개, 수정된 진행기록 2개, 삭제 0개다. 기존 LIFE021/TIME018 본문은 바뀌지 않아 11/1 검토의 기관 연속성·조약/의정서 날짜 및 부속서 보류를 유지한다. 개발·성능 보고서와 그 첨부는 국경 근거로 가져오지 않는다.

| ID | 원본 커밋 | 경로 | 원본 blob |
| --- | --- | --- | --- |
| GEO-LIFE-022 | [77fde236](https://github.com/kimjeon-il/PandoLab-library-data/commit/77fde2368829962656c97a166d32301ccd8679bb) | reports/borders/history/lifetimes/country-lifetime-europe-historic-two-sicilies-hanover-cracow-2026-11-03.md | 009f28098cc49b3ce83808b2cfa60be4080382fb |
| GEO-TIME-019 | [f5c10221](https://github.com/kimjeon-il/PandoLab-library-data/commit/f5c1022138dfd1b99045b01bcae3c35c48c5f423) | reports/borders/history/timeline/historical-timeline-2025-africa-drc-m23-goma-bukavu-2026-11-03.md | 681f66a2ed136e733ed64629b1359829c3dea917 |
| GEO-LIFE-023 | [cea99260](https://github.com/kimjeon-il/PandoLab-library-data/commit/cea99260afa36d43872c77553d5cfe20a72e1071) | reports/borders/history/lifetimes/country-lifetime-asia-historic-kokand-khiva-bukhara-2026-11-04.md | a0a1cce82835f7018dac02fc05941c9ebddc2909 |
| GEO-TIME-020 | [f36fb6cf](https://github.com/kimjeon-il/PandoLab-library-data/commit/f36fb6cf1e45a93f0c2d987c862fe3706116c86e) | reports/borders/history/timeline/historical-timeline-2025-north-america-haiti-mirebalais-saut-deau-2026-11-04.md | 0a370ff84280ec8a3c319ceaa0beaea8d368ba17 |

진행기록 두 개의 원문도 대조했다. LIFE 커서는 아시아 다음 아프리카, TIME은 2025 북아메리카 다음 남아메리카이며 어느 지역도 전수 완료로 표시하지 않는다. 파일명 11/4는 한국 시각 기록이며 이번 실행은11/3 UTC다.

## 2. LIFE022 — 하노버 날짜 충돌을 명시하는 정정

**확정 보완:** “1866-10-01 프로이센 헌법 적용”을 출처 일치 사실로 읽으면 안 된다.
- [DHM](https://www.dhm.de/lemo/kapitel/reaktionszeit/deutscher-bund-und-nationale-frage/die-preussischen-annexionen-1866)은 1866-10-01을 기술한다.
- 보고서가 인용한 [1866-09-20 병합법 §2 전사](https://www.verfassungen.de/preussen/gesetze/preussen66.htm)는 **1867-10-01**을 기술한다.
- 따라서 정정 문구는 “헌법 적용일은 DHM의1866-10-01과 법률 전사의1867-10-01이 충돌한다. 병합법 제정·공표·병합 기술일 및 헌법 시행일을 분리하며 원법 스캔과 시행문서 대조 전 단일 종료일로 입력하지 않는다.”
- [법률집 제47호 색인](https://www.reichsgesetzblatt.de/D/L%C3%A4nder/Preussen/1866/47-haupt.htm)은 법률일09-20, 발행일09-23, pp.555–556을 기록한다. [니더작센 기록원](https://nla.niedersachsen.de/startseite/landesgeschichte/aus_den_magazinen_des_landesarchivs/2016/aus-den-magazinen-des-landesarchivs-oktober-2016-139830.html)의09-22 병합 기술을 관보 공표일로 추정하지 않는다.
- [원법 스캔 소재](https://books.google.de/books?id=CSNGAAAAcAAJ&pg=PA555)는 찾았지만 페이지 영상·전문 대조는 성공하지 못했다.1867이 법적 최종 정답이라고 확정한 것이 아니라 **출처 불일치를 검증하여 기록한 것**이다.

양시칠리아의 통합법·시행일·편입령·가에타 항복은 서로 다른 사건이고, 크라쿠프는3국 보호관계·1846 편입의 날짜와 법적 지위를 구분한다. 현대 ITA/DEU/POL에 과거 정치체 생애를 덮어쓰지 않는다.

## 3. LIFE023 — 부하라1873 조약의 새 전사 근거

**확정 보완:** “원조약 직접 미확인”의 증거 단계를 “당대 원본 미확인, 후대 조약집 전사 확보”로 세분한다.

[러시아–부하라 조약 전사](https://istmat.org/node/27173)는1902 조약집 pp.421–425 및1952 재수록 pp.135–139를 출전으로 명시한다. 전사 §1은 기존 러시아–부하라 경계 유지와 구 히바의 아무다리야 우안 일부가 부하라에 편입되는 조항을 구분한다. 말미의 에미르 승인1873-09-28 구력(10-10 신력)과 카우프만 승인·서명1873-10-17 구력(10-29 신력)을 각각 보존한다. 이는 체결 절차의 두 날짜이며 어느 쪽도 자동으로 공통 효력일·부하라 소멸일·전 영토 형상 시작일이 되지 않는다.

[히바 조약 전사](https://istmat.org/node/27172)와 [대통령도서관](https://www.prlib.ru/node/619484)의1873-08-12 구력/08-24 신력은 종속·우안 양도를 뒷받침하지만 칸국 전체 소멸의 증거는 아니다. 코칸트의 Iranica 달력 모순과1920 히바·부하라 군사 점령/퇴위/후계 공화국 선포의 구분은 유지한다. 새 조약 전사는 원본 지도 좌표나 검증된 형상을 제공하지 않는다.

## 4. TIME019·020 — 국가 국경 반영 대상에서 제외

- DRC: [UNICEF Flash Update #3 p.2](https://www.unicef.org/media/167371/file/DR-Congo-Humanitarian-Flash-Report-No.-3-%28Upsurge-violence-in-North-and-South-Kivu%29%2C-01-February-2025.pdf.pdf)의01-28까지 고마 대부분 통제 및 잔여 저항 문구를 재확인했다. [UN 결의2773 등록 원문](https://mandates.un.org/mandate/S/RES/2773%282025%29?agenda_item=The+situation+concerning+the+Democratic+Republic+of+the+Congo.)의 부카부02-14와 현장02-16 관측을 한 도시 전역의 단일 완료일로 합치지 않는다. M23 통제를 RWA 영토 편입으로 입력하지 않는다.
- 아이티: [UNICEF04-29 보고 p.1](https://www.unicef.org/media/170616/file/Haiti-Flash-Update-29-April-2025.pdf.pdf)의03-31 장악,04-25 수복 시도 후에도 무장집단 통제가 지속된다는 서술을 재확인했다. 정확한 표현은 계속 활동·영향을 행사하며 “통제 아래 남아 있는 것으로 보인다”는 관측이다. 전체 코뮌 면적·연말까지 연속 통제 확정이 아니다.
- 두 보고서는 국제주권 이전이 아닌 실효통제 사건이다. 국가 국경 폴리곤 수정은 **적용 제외**로 처리한다. 별도의 날짜별 실효통제 레이어를 위한 형상은 미확보 상태다. ADM 경계를 점령선으로 대입하거나 그 확보를 국가국경 업무 완료의 필수 조건으로 요구하지 않는다.
- PDF 텍스트는 이번에 읽었으나 화면·지도 중첩 검사는 실행하지 않았다. MONUSCO PDF 직접 주소는403이었고 UN 공식 등록 본문을 확인했다. 원본 벡터/권리·CRS·위상 검증 완료로 주장하지 않는다.

## 5. 대상 객체와 현행 데이터 충돌

data work/gis library.json이 지시하는10개 대상 객체를 직접 읽었다. 아래 날짜는 관측한 현행값이며 이번에 독립 승인한 역사 판단이 아니다.

| 객체 | 현행 validFrom |
| --- | --- |
| COD / HTI / RWA / DOM | 1960-06-30 / 1804-01-01 / 1962-07-01 / 1863-09-14 |
| ITA / DEU / POL | 1861-03-17 / 1867-07-01 / 1917-10-27 |
| UZB / TJK / TKM | 1991-08-31 / 1991-09-09 / 1991-10-27 |

이 객체들은 validTo=null이다. COD/HTI/RWA/DOM의 geometry version은 Natural Earth5.1.1이고 자체 validFrom/validTo는null이다. 국가 lifetime과 형상 유효기간을 혼동하지 않는다. main과work/gis의 대상 객체 해시는 다르므로 main 객체를 가져오지 않는다. 해시는 evidence.json에 기록했다.

양시칠리아·하노버·크라쿠프·코칸트·히바·부하라에 대응하는 식별자는 두 library 색인의 ID 문자열 검색에서 발견되지 않았다. 이는 이름·동일성 전수 감사가 아니므로 현대 국가로 임의 대응시키지 않는다. 새 역사 객체의 동일성, 시작/종료 기준 및 시대별 형상 근거가 필요하다.1801년은 조사 하한이며 창립일로 추가하지 않는다.

색인에 남은 LIFE016 및 TIME010–013의 전용 본문은 main borders tree에 없다. LIFE016 직접 조회도404였다. 기존 누락 보류를 유지하며 추측 복원하지 않는다.

## 6. 처리 결과·실행 검증

- 확정된 수정은 **하노버 출처 충돌 기록 및 부하라 조약 전사·서명일 구분**을 이 보충 정정판에 반영한 것이다. main 원본과 그 진행기록은 수정하지 않는다.
- 이번 수정 파일은 이 README, evidence.json 및 reports/README.md 색인 한 행뿐이다.
- 현행 국가 생애·geometry·archive·library.json·앱 핀·코드 변경0건. 신규 runtime 적용 없음은 신규 보고서 없음이라는 뜻이 아니다.
- 커넥터를 통한 원문·Git tree·커밋 이력·대상 객체 대조 및 문헌 확인을 수행했다. 실행 도구는 “No usable execution environment is available”로 실패하여 로컬 GIS·테스트·보고서 helper는 미실행이다. 데이터 변경이 없으므로 관련없는 테스트나 공간자료 생성은 시도하지 않았다.
- 기본 helper의 main 게시 경로는 이번 사용자의 main 금지와 충돌하므로 실행하지 않는다. GitHub의 기존 tree 기반 단일 부모 커밋과 expected-head 검사, force=false로 work/gis에만 기록하고 원격 세 파일 내용을 다시 대조한다. publish-reports/check-reports 성공으로 표현하지 않는다.
- main 병합·다른 브랜치·배포·포터블·무명 강/호수 조사는 하지 않았다. 로컬 파일을 만들지 않아 정리할 임시 출력은 없다.
