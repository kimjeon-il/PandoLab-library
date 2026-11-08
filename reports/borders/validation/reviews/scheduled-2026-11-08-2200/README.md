# 양 브랜치 GIS 검토 — 틸지트 비준 교환·아니프 선언·수단 단위 구분

> GEO-REVIEW-20261108-2200 · 2026-11-08 22:00 UTC / 11-09 KST · reviewed / supplemental-corrections / important-holds · report-only / runtime-unchanged

## 범위·중복 방지

Pando main `c2ce04816be70ec87fac194a5f34e214dea1bc8a`, work/gis `528fdf0665b3250c34a8a06bbed3892cdf6dd6b2`; 자료 main `65a4c70c253eae81b039d0ccce7e49ad789e3c5e`, work/gis `dc5e6635d412ddc16e77192cf430ccabd1913acc`에서 검토했다. 직전 [11월7일 처리](../scheduled-2026-11-07-2200/README.md)를 기준으로 원본 저장소·브랜치·경로·blob을 대조했다.

이번 main에는 기존 자료의 통합 이력이 많아 compare의 파일 목록은300개에서 잘린다. 이를 전부로 오인하지 않고 자료 reports 하위의 완전한 두 트리(truncated=false)를 비교했다. 직전 main `0967eff19804867eb0c206ad982baffd6bdf3c04` 대비 전체 보고서 신규/수정347개 중 borders286개, 그중 **277개는 work/gis의 기존 blob과 동일**하다. 이들 복원·통합을 새 조사나 새 적용으로 세지 않았다. borders 삭제0개. 경로·blob별 판정은 evidence.json에 보존한다.

남은9개는 LIFE028/TIME025 원문2개, 진행기록2개, 주제색인1개, 한국 보고서 링크 정리1개, 세계지도 원본보존JSON3개다. Pando 양 브랜치의 루트에는 reports가 없으며 정본은 외부 자료 저장소다. 최신 AGENTS·branch-policy·불변 역사경계 정책과 reports 색인·기존 geography 트리를 확인했다. geography tree는 `cc011048be374646ba373504c9df87fd214c05d5`로 이전과 같다.

## LIFE028 보충 정정

[원본](https://github.com/kimjeon-il/PandoLab-library-data/blob/ea7ce127025962860b4fd2ce843b3476b214ff01/reports/borders/history/lifetimes/country-lifetime-europe-historic-bavaria-wurttemberg-warsaw-2026-11-09.md)은 바이에른·뷔르템베르크 왕국, 바르샤바 공국을 현대 DEU/POL과 구분했다. 왕호·정부형태·연방 구성국 지위와 법적 국가 동일성을 분리한 판단을 유지한다. 순환기록은 후속정정 `978efb3adf73ca4a65339076cce02fe7180b2fab`까지 반영된 판본을 읽었다.

1. [틸지트 조약 전사](https://www.napoleon.org/en/history-of-the-two-empires/articles/treaty-between-prussia-and-france-tilsit-9-july-1807/) 마지막 문장에 **1807-07-12 Königsberg 비준서 교환**이 명시되어 있다. 원문의 교환일 미확인을 **전사본에서 확인, 비준 원본·독립 교차검증 미실행**으로 보완한다. 제30조의6일내 교환 규정과 실제 교환일을 구별한다.
2. 같은 조약 **제1조는 프랑스·프로이센 간 평화와 우호**의 시작을 교환일로 정한다. 이를 조약 전체 또는 공국 성립 효력의 직접 규정으로 확대하지 않는다. 제15조의 공국·작센 국왕 규정은 별개다. 공국 lifetime을7월12일로 자동 확정하지 않는다.
3. [HLB 아니프 선언](https://www.historisches-lexikon-bayerns.de/Lexikon/Anifer_Erkl%C3%A4rung,_12./13._November_1918)은 **원본 분실**, MA980의 **Eisner 해석이 덧붙은 타자 사본**을 설명한다. 단순 원이미지 미열람 대신 원본 전승상태를 보완한다.11-12 서약해제/11-13 공표와 정식퇴위 구별은 유지하며 사본·신문 이미지 검독은 미실행이다.
4. 뷔르템베르크1918-11-30 퇴위 선언은 [Landesarchiv 공식 Archivnachrichten56/2018](https://www.landesarchiv-bw.de/sixcms/media.php/120/Archivnachrichten_56_pdf.pdf#page=9) **인쇄p9 그림5**의 사진 재현을 화면 확인했다. 캡션 HStAS M743/1 Bü1 Nr10을 확인하여 목록만 파악한 상태에서 공식기관 간행물의 문서이미지 확인으로 진전했다. 원관보S263 자체 검독이나 국가 소멸일 확정은 아니다.

## TIME025 보충 정정

[원본 TIME025](https://github.com/kimjeon-il/PandoLab-library-data/blob/bfb14cde40c39bd7977c3c4bcd41ebd545c26c3a/reports/borders/history/timeline/historical-timeline-2025-africa-sudan-khartoum-parallel-government-el-fasher-2026-11-09.md)은 수단 내 군사통제와 국가 주권을 구별했다. 새 국제국경·주권국 성립0건이라는 조사 범위 내 판정을 유지한다.

- **“19개 주”를 “ADM1 메타상19개 단위”로 정정한다.** [geoBoundaries API](https://www.geoboundaries.org/api/current/gbOpen/SDN/ADM1/)의 admUnitCount19는 법적 주 개수가 아니다. [CIA 공식 행정도](https://www.cia.gov/static/ce5e08ba0b181e403e5b0ad8e681bab0/Sudan_Administrative.pdf)의 텍스트는18개 주와 별도 Abyei Area·최종 주권 미확정을 구분한다. 고정GeoJSON은 LFS포인터만 읽혔으므로 실제19피처가18주+아비에이라고도 단정하지 않는다.
- [OHCHR10-27 원문](https://sudan.un.org/en/304113-appalling-reports-summary-executions-and-other-serious-violations-rsf-makes-major)의 **large parts**는 **“상당 부분, 과반·전역 여부와 정확한 윤곽 미확정”**으로 쓴다. 기존 “대부분이 아닌”은 원문이 배제하지 않은 과반을 부정하므로 제거한다.10-25 바라/10-26 군본부 장악발표/10-27 UN관측은 구분 유지한다.
- [EUAA 지도](https://www.euaa.europa.eu/country-guidance-sudan/21-map-areas-control-and-influence)는6월 발행·3월 기준으로 첫 표의 링크명도 명확히 한다. [AU성명](https://peaceau.org/en/article/press-statement-of-the-1264th-meeting-of-the-peace-and-security-council-held-on-11-march-2025-on-the-situation-in-sudan)은3월11일 회의·페이지갱신3월12일을 구분한다.
- Tasis7월26일 구성발표·8월30일 선서 보도는 인용 Sudan Tribune과 일치하나 당사자 원선언의 독립 검증은 아니다. 군사통제·병행정부를 국가 소멸·국경 양도로 바꾸지 않는다.

LEO-BW403, Ludwigsburg500, AP10-28·HDX접근실패, UN SC/16144 공식링크404로 일부 원문은 검증하지 못했다. UN공식목록의 문서번호·날짜 확인을 본문 완독으로 과장하지 않았다. 접근제한 우회 없이 확인된 문헌 보완만 반영한다.

## 기타 수정 보고서와 보류

한국 보고서 변경은 `671e9234abe78f042cb6201e6828d75909969934`에서 일반 통합기록 링크를 정리한 한 줄뿐이며 날짜·형상 판단은 바뀌지 않았다. 과거 검사 결과를 이번 재검증으로 승격하지 않고 제품에 중복 적용하지 않았다.

원본보존3JSON은 `0509df26bac1173a119b35770ee5ad771c6ba87a`의 기록이다. KAS/SPI의 기존 NE 형상 보존, 현재252개 출력·254개 원본의 바이트 보존, 고정판887f721의 과거 카탈로그280개 보존을 보고한다. 이는 **이미 생성된 보존 검사 기록을 읽은 것**이며 이번에 그 검사를 재실행한 것은 아니다. 미완성 런타임 활성화·pin변경의 근거로 삼지 않는다.

현행 work/gis 객체를 직접 읽었다. DEU lifetime1867-07-01~null과 1871/1918 형상기간, POL1917-10-27~null 및 형상기간null, SDN1956-01-01~null 및 2011-07-09 분리 전후 형상기간을 확인했다. 관측값이지 이번 역사적 승인값이 아니다. 바르샤바 공국으로 POL 시작일을 소급하거나 RSF 통제로 SDN lifetime/국제경계를 덮어쓰지 않는다.1801 조사 하한은 건국일로 입력하지 않는다.

기존 THA 객체 누락과 다른 법적 동일성·원형상 보류를 해소하는 새 증거는 이번 신규 보고서에 없다. 자료 work/gis 자체도 직전 검토 이후 그대로라 재해결로 보고하지 않는다. 종료된500km²미만 연구를 main에 복원된 과거 자료 때문에 재개하지 않는다. 신규 독립 역사 폴리곤·권리·기간 근거가 없으므로 런타임 반영0건.

## 반영·검사

이 README·evidence.json·reports/README.md 색인1행만 work/gis에 반영한다. 원문 main을 수정·통째 병합·체리픽하지 않는다. 앱 pin은 이미 다른 작업으로 `a1bc7a5229b252c5b8d9612026cd0ae3e82d7327`로 바뀌어 있었으며 이번에는 변경하지 않았다. main 통합·배포·포터블·중단된 무명 강/호수 조사는 없다.

수행한 검사는 원격 이력·완전한 보고서 트리·blob 중복대조, 관련 객체 JSON읽기, 문헌 대조, 변경3파일 범위 및 원격 재조회다. 독립 GIS 형상·화면·위상·전체테스트는 미실행이며0.5CSSpx는 추가 완료조건이 아니다. 저장 전용 자료 저장소에서 검사 실행·재생성은 하지 않았다.

로컬 worktree 목록과 상태를 읽었고 등록된 work/gis 경로는 실제 부재, 관련 없는 checkout은 ahead1인 채 보존했다. 새 clone/worktree·임시 다운로드를 만들지 않았다. main에 쓰는 publish-reports helper는 이번 명시적main변경금지로 미실행이며 통과했다고 하지 않는다. 기존 원격tree에 단일부모 커밋을 만들고 expected-head와force=false로 work/gis에만 게시한 뒤3파일·head를 대조한다.
