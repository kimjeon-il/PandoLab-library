# 기존 500km² 미만 역사 경계 연구 폐기 — 2026-11-04

> 상태: `retired-research-under-500km2` · 적용: data `work/gis`의 연구 우선순위·후속조사 · 지도 형상 변경 없음

사용자가 기존에 조사한 사항 중 **500제곱킬로미터 미만은 모두 폐기**하도록 지시했다. 아래 면적 근거가 있는 연구 항목은 활성 상세 조사·추가 지오리퍼런싱·선 추출·미완료 정밀 검증의 대기열에서 제외한다. 과거 소규모 예외로 선택한 A–C나 중요한 소규모 할양도 이번 기존 연구 종료 대상에서 임의로 빼지 않는다. 국가 존속 자체나 더 큰 사건의 분리 불가능한 일부를 작은 수치 하나만 보고 폐기하지 않는다.

폐기는 연구 작업의 종료다. 역사적 사건이 없었다는 판정, 종전 검증의 취소, 이미 채택한 GIS 폴리곤의 삭제를 뜻하지 않는다. 원보고서의 사실·출처·당시 상태는 감사 이력으로 남기며, 아래 항목의 옛 `다음 조사/보류 해소/정밀 복원` 지시는 더 이상 활성 작업이 아니다. 혼합 ZIP·원지도·조약 원문·채택 형상과 그 근거, Git 과거 이력은 삭제하지 않는다.

## 1. 연구 종료: 면적이 명시된 18개 사건 묶음

면적은 **기존 조사문서가 보고한 값**이다. 이번 정리는 원조약을 모두 새로 측량·대조한 전수 역사 검증이 아니다. 각 방향의 교환을 별개 사건으로 중복 집계하지 않고, 순증감 0을 변경 면적 0으로 취급하지 않는다.

| ID | 사건 | 기존 보고 면적 | 근거·범위 구분 |
| --- | --- | --- | --- |
| S01 | 러시아–카자흐스탄 A/B: Ogneuporny ↔ Kurskoye–Varvarinka, 2005 서명·2006 발효 | 각 방향 520ha = 5.2km² | 협상 당사자 문헌 pp199–200. A/B는 같은 교환의 양쪽 필지다. [기존 A–F 보고](../reconstruction/russia-frontier-1991-2026-2026-10-31/README.md). |
| S02 | 같은 조약 C: Kommunistichesky 철도 | 각 방향 70ha = 0.70km² | 같은 문헌 pp192–193. 도면 후보 91.50/51.40ha를 법적 양도 면적으로 대체하지 않는다. 기존 채택 형상은 보존한다. |
| S03 | 같은 조약 D/F: Lokot 캠프·도로 ↔ Zhezkent 보상 | 각 방향 90ha = 0.90km² | 같은 문헌 pp202–204. D/F는 한 교환이며, 거절된 2,050ha 제안은 최종 면적이 아니다. |
| S04 | 같은 조약 E: Burkotovo 묘지·접근로 ↔ 미동정 보상 필지 | 각 방향 90ha = 0.90km² | 같은 문헌 pp204–205. S03과 별개이며 보상 필지 위치는 여전히 미확정이다. 미확정을 해소하는 상세 연구는 종료한다. |
| S05 | 1939-11-11 Alimbetovsky 농장 일부, 카자흐 SSR → RSFSR | 14,635ha = 146.35km² | [기존 1939 보고](rsfsr-reverse-research-1953-1922-2026-10-31/remaining1939-1945.md), `east-1939-alimbetovsky`. 문헌상 잘 뒷받침되지만 원명령은 미확보다. 농장 전체 79,954.64ha 및 반대 방향 5개 셀소비에트와 별개다. |
| S06 | 1956-04-20 Dzhanybek/Janybek 남부 → RSFSR | 7,049ha = 70.49km² | [기존 보고](rsfsr-reverse-research-1965-1954-2026-10-31/dzhanybek1956.md), `east-1956-dzhanybek`; [카자흐 법령집](https://old.adilet.zan.kz/upload/zan_lib/sz0_1_c.pdf) 인쇄 p41의 기존 확인값. |
| S07 | 1962-11-24 Varna–Karabalyk 교환 | 각 방향 381ha = 3.81km² | [기존 감사](rsfsr-reverse-research-1965-1954-2026-10-31/1962-Varna-source-audit-ko.md), `east-1962-varna`. 합계 7.62km², 순변동 0. 상세 경계기술 미확보는 그대로 기록하되 추가 수집을 종료한다. |
| S08 | 1965-12-06 Bobrovsky/Sandzhursky → RSFSR | 1,833ha = 18.33km² | [기존 문헌 검토](rsfsr-reverse-research-1965-1954-2026-10-31/INCREMENT-ko.md), `east-1965-bobrovsky`. Enbeksky 전체 행정구역 면적으로 확대 해석하지 않는다. |
| S09 | 1964-11-17 Smolensk 7개 마을·Mazykin 일부 → BSSR | 2,256ha = 22.56km² | `west-1964-belarus`; 기존 `RSFSR-1964-georeference-and-1976-evidence.zip`의 `by1964/legal/legal-review.md`. 후기 지도상의 선 교정은 별도 양도 사건이 아니다. |
| S10 | 1947 Jäniskoski–Niskakoski, 핀란드 → 소련 | 176km² | [기존 보고](rsfsr-reverse-research-1953-1922-2026-10-31/remaining1946-1953.md), `FI-1947`; [UNTS 216](https://treaties.un.org/doc/Publication/UNTS/Volume%20216/v216.pdf). 1947-02-03 서명·04-18 발효. 후보 도형 173.7106/171.7253km²는 법정 면적 대체값이 아니다. |
| S11 | 1947 서명·1949 발효 노르웨이 3개 섬 → 소련 | 총 18.45ha = 0.1845km² | [기존 보고](rsfsr-reverse-research-1953-1922-2026-10-31/remaining1946-1953.md), `NO-1947`; St.prp119(1948) p4. Kisteholmen 14.45ha, 나머지 두 섬 합계 4ha. |
| S12 | Hestefoss 교환, 1967 기본 협정·1969/1970 최종 문서 | 각 방향 약 0.704km² | `NO-1968-DEM`; 기존 `norway-originals-1968-1984.zip/REVIEW-ko.md`. 현장 작업·확정문서를 추가 교환으로 중복 계산하지 않는다. |
| S13 | 1983 노르웨이–소련 Melkefoss·Skogfoss·Jakobselv | 각 방향 0.0052·0.0124·0.0258km²; 합계 0.0434km² | `NO-1983-C/B/A`; 같은 노르웨이 보고와 St.meld18(1985–86) p4. 1984/1985 이행 문서는 별도 새 교환이 아니다. |
| S14 | 2018 서명·2019 발효 Patsojoki·Vorjema | 각 방향 38.47ha + 6.40ha = 0.4487km² | 기존 `norway-focused-diagnostics-repro-20261103.zip`의 법문 전사 pp267–268; [UN I-58231](https://treaties.un.org/doc/Publication/UNTS/No%20Volume/58231/Part/I-58231-080000028062789f.pdf). 진단 도형 면적으로 대체하지 않는다. |
| S15 | Sarakhs/Hari Rud, 1954 협정·1955 발효 | 약 10sq mi = 25.9km² | 기존 `east-limited-followup-2338.zip/research/east-iran-afghan-1922/iran-east/README.md`의 IBS1978 p7 각주 확인값. 같은 문서의 Atrek 전체 면적과 별개이며 이미 채택한 1922 선은 유지한다. |
| S16 | 이란–소련 1956–57 재측계 편차·1958 승인 | 이란→소련 1.23km², 소련→이란 5.62km²; 합계 6.85km² | 기존 `southern-literature-2202.zip/research/south-rebuild-20261025/literature-quantities/1955-1958-findings.md`. 법령 전사 근거이며 원관보·13개 부속도는 미확보다. 1955 최초 변경 전체나 1971 저수지 교환을 포함하지 않는다. |
| S17 | 소련–튀르키예 1969–73 재측계·보상 | 최종 각 방향 7.877km²; 합계 15.754km² | 같은 묶음의 `turkey/territorial-change-evidence/CHANGE-QUANTITIES.md`, [기존 연구자 해설 출처](https://mediamax.am/am/news/special-file/47201/). 조약 정본 면적표가 아닌 기존 문헌 보고값이다. 1982 아후리안 사건과 분리한다. |
| S18 | 같은 2005/2006 조약의 Prigornoe 및 별도 명시된 Orenburg 필지 연구 | Prigornoe 약 12km²; Novovvedenka 4.5km²; Pervomayskoye 8.5km²; Soyuznaya 주변 16km² | 기존 `russia-maxzoom-border-review-backup.zip`의 `kazakhstan/prigornoe/events.json` 및 `book-supplement-ko.md`. Prigornoe·Soyuznaya 이관은 문헌상 확인되며 나머지 보상 필지는 보고값·위치 보류다. 각 필지 상세 연구를 종료하되 마을·역 전체 면적으로 확대하거나 29.90km² 지역 총계와 중복 합산하지 않는다. |

S01–S04 문헌: [러시아–카자흐스탄 경계 협상 기록](https://adebiportal.kz/storage/upload/iblock/784/784be81e4768a1894437005005ef4f85.pdf). 원보고서와 혼합 패키지는 사실·출처 감사 및 기존 형상 근거로만 보존하며, 이 목록의 연구 재개 지시로 읽지 않는다.

## 2. 이번에 폐기 판정을 확정하지 않은 범위

- **면적의 대상이 다름:** 중국 G/H의 62/335km², Markansu 235(다른 문헌 226)km², Karazak 200(186)km², 키르기스 한텡그리 약 450km²는 전체 분쟁지·청구지역의 수치다. 실제 변경량·범위와의 대응이 미확정이므로 확정 양도 면적으로 바꾸지 않았다. 카자흐 한텡그리의 다른 국소 연구와 혼동하지 않는다.
- **더 큰 복합 사건:** Sarychieldy+Chagan-Obo 전체 944km²의 537/407 배분에서 407만 떼어 전체 연구를 폐기하지 않는다. 2011 타지키스탄–중국 파미르 인도 1,158km²는 이 목록 밖이다.
- **수치·효력 미확정:** 1940 Adamovsky의 200ha/200,000ha 상충, 1927 Sulyukta 14,000ha의 독립 근거 미확정, Atrek·Mugan/Deman/Eddy-Evlar·1970/71 저수지 교환·1982 아후리안·2025 키르기스–타지크 교환은 미판정이다. 경계 길이, 저수지 면적, 순변동 0을 변경 면적으로 대체하지 않는다.
- **확정 사건이 아닌 기존 제외 자료:** Polesye 815.8ha의 거절안, Kostanay 농장 20,000ha의 취소안은 이미 확정 이관이 아니므로 새 확정 양도로 세지 않는다.
- **추가 소규모 협상·분쟁 주장:** Orsk 1.6km², Belyaev 0.3km²는 협상 합의 보도와 토지·법적 이전의 대응이 미확정이다. Imashev·Ilek 등은 분쟁지 배분·중복 집계가 섞여 있어 실제 변경량으로 대체하지 않는다. 확인되는 별도 필지에는 같은 폐기 원칙을 적용하되, 합계를 새 사건으로 만들지 않는다. Prigornoe와 명시된 보상·역 주변 필지는 S18로 연구를 종료한다.
- **변경량이 아님:** 모나코·바티칸의 국가 전체 면적, 동독 경계 교정 대칭차, 바이코누르 표시 일반화 면적은 이 폐기 기준의 변경 면적이 아니다. 국가 존속 연구·이미 구현된 국가·도서·통로를 삭제하지 않는다.
- 가봉–적도기니·사포딜라 및 네덜란드의 일부 기존 보고에는 해당 변경의 면적이 명시되지 않았다. 국가·호수·군도 전체 면적을 임의 대입하지 않았다.

미판정은 추가 정밀조사를 새로 시작하라는 뜻이 아니다. 기존 근거가 부족함을 남기며, 작은 사건의 면적을 알아내기 위한 새 측량·벡터화·원도 수집을 종료 조건으로 요구하지 않는다.

## 3. 적용·보존·도달 범위

- 현행 `work/gis`의 관련 보고서에 이 연구 종료가 우선함을 표시하고, [106행 커버리지](rsfsr-reverse-research-1953-1922-2026-10-31/COVERAGE-106.csv)의 대응 11행은 `review_bucket`만 `retired_research_under_500km2`로 바꾼다. 날짜·역사적 상태·당시 형상 준비도·출처 및 나머지 95행은 그대로 보존한다.
- 원보고서의 옛 권고·hold/conditional 상태는 당시의 역사 기록이다. 이 목록에 해당하면 그 표현을 근거로 상세 작업을 재개하지 않는다. 필요하면 이 정리 커밋을 되돌려 복구할 수 있다.
- 자료 저장소 `main`, 앱 `main`, `archive/index.json`, `library.json`, `objects/`, 런타임 자료와 앱 자료 핀은 변경하지 않는다. 압축 원본 ZIP·원지도·실제 채택 지오메트리도 변경하지 않는다.
- 읽기 범위는 관련 `work/gis` 보고서·원장, `main`의 국경 보고서 색인 및 텍스트, 기존 연구 ZIP 238개의 중복 내용 제외 텍스트 보고서 713개다. 모든 PDF·이미지를 새로 OCR하거나 모든 비공개 자료를 전수 재분석하지 않았다.
- `main`의 별도 보고서 트리와 기존 비공개 보관 패키지는 읽기만 했으며 그 원본에 폐기 표시를 쓴 것은 아니다. 따라서 이 변경은 **work/gis에서 확인된 연구의 종료**이며 모든 저장소·보관 파일의 물리 삭제 완료가 아니다. 같은 근거가 있는 다른 기존 소규모 항목을 발견하면 본 원칙으로 종료하되, 미확정 면적을 추정으로 채우지 않는다.
