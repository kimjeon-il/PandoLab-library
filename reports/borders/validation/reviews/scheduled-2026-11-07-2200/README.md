# 양 브랜치 GIS 보고서 검토 — 사모아 왕제 전환·태국–캄보디아 회의 날짜 보완

> ID: GEO-REVIEW-20261107-2200 · 실행 2026-11-07 22:00 UTC / 11-08 KST · reviewed / supplemental-corrections / important-holds · report-only / runtime-unchanged

## 범위와 중복 확인

Pando main `4f27dc9ac18fc2f6ca0163f8d33fea33e813d50f`, work/gis `30a8402ac82a3e8a24f943f777a7aaedec211279`; 자료 main `0967eff19804867eb0c206ad982baffd6bdf3c04`, work/gis `93e6796fa9197453a28aad6be9047418a34cf1b5` 기준이다. 직전 [11월 6일 검토](../scheduled-2026-11-06-2200/README.md)의 처리 이력과 대조했다.

자료 main의 직전 `6e41eb415d66bffff400bf3b064f4605f95fa326` 이후 2커밋·5파일은 LIFE027/TIME024 원문 2개, 순환기록 2개, borders 색인 1개다. 신규 원문은 main에서 읽었으며 work/gis에 없다는 이유로 누락하지 않았다. work/gis 자체에는 직전 검토 이후 변경이 없다. Pando main의 100커밋 차이에 보고서 변경은 없고, 완전한 현재 트리에도 reports 파일이 없다. 앱 변경을 자료 검토와 섞어 병합하지 않는다.

최신 AGENTS·브랜치 정책과 자료 README/TEMPLATE·reports 색인·borders 색인·기존 geography 목록을 읽었다. main 보고서 하위 트리는 truncated=false이며 추가 AGENTS가 없다. 신규 기록은 전용 borders/validation에 둔다. 이전에 처리한 LIFE026/TIME023 및 보류를 새 적용으로 세지 않는다. 새 근거는 아래 해당 사건에만 연결하고 기존 소규모 연구 종료 목록을 재개하지 않는다. 원본별 저장소·브랜치·경로·커밋·blob은 evidence.json에 남긴다.

## LIFE027 보충

[원본 LIFE027](https://github.com/kimjeon-il/PandoLab-library-data/blob/8936a8d739d86475a9cd4c055c6c131564d86fa7/reports/borders/history/lifetimes/country-lifetime-oceania-historic-samoa-bora-bora-raiatea-2026-11-08.md)의 사모아 1898–1899 정부 계속성 보류에 구체적 사건을 보완한다.

[미 국무부 FRUS1899/d616](https://history.state.gov/historicaldocuments/frus1899/d616)은 **1899-06-10 말리에토아 타누마필리의 사임, 위원회의 수락, 같은 날 왕제 폐지 공고 및 왕·평의회 업무를 3국 영사에게 배정한 전환**을 수록한다. 따라서 1889년 독립 보장, 1899-06-10 왕제·정부 전환, 1899-12-02 조약 서명, 1900-02-16 비준서 교환·조약 효력을 별도 사건으로 기록한다. 이 사실을 곧바로 모든 사모아 제도의 주권국 validTo나 현대 WSM/ASM의 lifetime으로 바꾸지 않는다. 섬별 현지 양도와 실효 지배, 정치체 동일성은 별도다.

[프랑스 공식 판결 11PA03468, 2012-03-02](https://www.legifrance.gouv.fr/ceta/id/CETATEXT000025623744)은 **1898-03-19 리워드 제도 편입 법률**의 명칭·날짜를 인용하고 적용한다. 이 법률 존재·날짜를 별도 사건으로 추가한다. 증거는 후대 공식 판결 원문이며 1898 법률 원 스캔은 아니다. 공포지·현지 시행일·왕국 실효 통치 종료와 동일시하지 않는다.

원문의 **1898-01-25 상원 승인 후보는 미채택**으로 낮춘다. [상원 공식 Jules Godin 활동표](https://www.senat.fr/table-nominative-archives/godin_jules1831r3/3R/1898.html)는 같은 법안 위원회 보고서 제출을 **02-24**로 적어 학위논문 검색문과 불일치 가능성이 있다. 이를 근거로 실제 최종 표결일을 새로 단정하지 않는다.

자르나크 선언의 **1847-06-16/19 차이는 기록원 자체의 제목과 본문에도 존재**한다([기록원 설명](https://www.archives.pf/contenus-blog/page/24/)). 따라서 공식 기록원 대 후대 서술만의 충돌이라는 원문 분류를 보정한다. 원 서명면·보라보라 1895-09-21 퇴위 원문은 미확보이며 종료일 채택을 유지 보류한다. Gallica 법률 원문403, 상원 대형PDF 용량 초과로 원문 검증이 완료되지 않았고 접근 제한을 우회하지 않았다.

## TIME024 보충

[원본 TIME024](https://github.com/kimjeon-il/PandoLab-library-data/blob/0967eff19804867eb0c206ad982baffd6bdf3c04/reports/borders/history/timeline/historical-timeline-2025-asia-thailand-cambodia-ground-control-vector-followup-2026-11-08.md)의 기존 TIME003 사건 재사용 판단을 유지한다. 같은 휴전을 신규 영토변경으로 중복 계수하지 않는다.

1. **JBC 회의는 2025-06-14~15, 합의 회의록 서명은 06-15로 보완한다.** [태국 정부 폐회 발표](https://thailand.prd.go.th/en/content/category/detail/id/49/iid/397780)와 [캄보디아 AKP](https://vps.akp.gov.kh/post/detail/351161)가 이틀간 회의를 확인한다. 원문 06-14 시작일만으로 모든 승인·서명 시점을 표시하지 않는다. 서명 사실과 서명 회의록 원문·좌표 미확보는 구별한다.
2. **07-24는 7월 대규모 교전 국면 시작**으로 좁혀 쓴다. [태국 외교부](https://www.mfa.go.th/en/content/fmnbteng)가 05-28 Chong Bok 충돌도 명시하므로 2025년 최초 충돌로 오해하지 않게 한다.
3. [JBC 공식 발표](https://www.mfa.go.th/en/content/the-6th-thailand-cambodia-jbc-en)의 45/74 표석 합의는 전 국경 완결이 아니다. [말레이시아 총리실 발표](https://www.pmo.gov.my/en/speeches-en/joint-press-conference-on-the-special-meeting-hosted-by-malaysia-to-address-the-current-situation-between-cambodia-and-thailand/)의 07-28 24:00은 07-29 00:00과 같아 정정하지 않는다. [12-27 공동성명](https://thailand.prd.go.th/en/content/category/detail/id/3243/iid/459719)의 10:15 서명·정오 발효·현 배치 유지·국경 및 획정에 영향을 주지 않는 제3항도 재확인했다.
4. [Thai PBS 11개 구역 기사](https://www.thaipbsworld.com/thailand-cambodia-standoff/thailand-controls-11-areas-contested-by-cambodia,-including-preah-vihear)는 군 대변인 주장 인용이다. 마지막 장소도 Preah Vihear hill 인접지이며 본사원 점령으로 확대하지 않는다. 확정 통제 폴리곤·국가 주권 이전으로 승격하지 않는다.

서명 JBC 회의록·공동 좌표·일자별 독립 실효지배 형상은 확보되지 않았다. Reuters/AP 07-24 직접 열람은 이번 실패했으며 독립 완독이라고 쓰지 않는다. 공간파일·원본 CRS·링·위상·면적·화면 검사는 미실행이다. 원문의 0.5 CSS px 미실행 기록은 추가 의무 검증 관문이 아니다. 현행 약 500km² 선별·기존 소규모 연구 종료와 Natural Earth 1:10M 규칙을 유지한다.

## 현행 객체와 적용 범위

work/gis library.json과 실제 객체를 읽어 ASM=1900-02-16, WSM=1962-01-01, PYF=1880-12-30, KHM=1841 시작·끝 null을 확인했다. 모두 NE5.1.1 형상의 validFrom/validTo는 null이다. 이는 **현행 관측값이며 이번 역사적 승인값이 아니다**. 기존 현대 객체를 역사 왕국에 소급하지 않으며, 1801 하한을 가상 건국일로 입력하지 않는다.

THA는 library.json에 해시 `84486d70baf072bda7ca8d3a4c5c96e90d035999a295cbbf5c6be63e2447cfb3`가 있으나 해당 objects JSON 조회가404이며 완전한 objects 트리에도 그 경로가 없다. 현행 THA 상세 기간·형상 확인은 차단되었다. 다른 판본으로 임의 대체하지 않았다. 런타임 index 직접 응답도 빈 본문이어서 파싱하지 못했다. 이것을 공개 웹 장애라고 단정하지 않는다. 이 누락을 추정 형상으로 복구하지 않는다.

변경은 이 README, evidence.json, reports/README.md의 색인 1행뿐이다. 국가 lifetime·geometry·archive·library.json·앱 pin·코드 변경0건. 앱 pin `887f72186fda9596502a35631d0a3376d9b4a1f1` 유지. 보고서 보충 정정과 제품 적용은 별개다.

## 검증·게시

원본 이력·blob·관련 현행 객체·공식 문헌을 범위 내 대조했다. GIS 재생성·위상·제품 화면·전체테스트는 미실행이며 저장 전용 저장소에서 테스트를 돌리지 않는다. 로컬 worktree 목록·상태를 확인했으나 등록된 work/gis 경로는 실제 부재다. 관련 없는 checkout과 stale 등록은 보존했다. 새 clone/worktree/브랜치·임시 다운로드는 만들지 않았다.

main 게시 helper는 이 회차의 명시적 main 변경금지와 충돌하여 실행하지 않는다. 기존 원격 tree에 보고서3파일만 더해 단일부모 커밋을 만들고 expected-head·force=false로 work/gis만 갱신한 뒤 원격3파일과 head를 대조한다. helper 통과나 main 게시 완료라고 하지 않는다. main 병합·배포·포터블·중단된 무명 강/호수 조사는 없다.
