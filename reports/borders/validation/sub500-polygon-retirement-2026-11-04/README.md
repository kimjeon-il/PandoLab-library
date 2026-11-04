# 500km² 미만 폴리곤: 로컬 수정·검사 완료, 저장 차단

2026-11-04. **자료/app 커밋·핀 변경·push는 미완료. main·배포·일반화는 미실행.**

| 대상 | 날짜 | 규모 | 상태 |
| --- | --- | --- | --- |
| 러–카 A/B Ogneuporny–Kurskoye/Varvarinka | 2006-01-12 발효 | 각5.2km² | 로컬 source/chunk/compiled/world에서 제거 |
| 러–카 C Kommunistichesky 철도 | 동일 | 각0.70km² | 위와 같음 |
| D/F Lokot–Zhezkent, E Burkotovo | 동일 | 각0.90km² | 조건부 미적용, 정밀 적용 대기 종료 |
| 중국 G 아바가이투 | 2008-10-14 인계 | 전체 대상약62km² 안의 이전분, 실제량 미확정 | runtime 미적용, native CHN1·RUS2개 G 버전 발견. 제거 차단·원본 보존 |
| 중국 H 헤이샤쯔다오 | 동일 | 중국 귀속 육지약171km² | 적용 버전 없음, 신규 작업 없음 |

규모는 기존 [종료 목록](../../history/sub500-research-retirement-2026-11-04.md)과 [A–H 사건 원장](../../reconstruction/russia-frontier-1991-2026-2026-10-31/engineered-event-ledger.json)에 근거한다. A/B의 [협상 기록 pp199–200](https://adebiportal.kz/storage/upload/iblock/784/784be81e4768a1894437005005ef4f85.pdf), [조약 등록](https://treaties.un.org/Pages/showDetails.aspx?objid=0800000280420e3a). 국가 면적·분쟁지 전체·필지 합계·경계 교정 대칭차를 실제 이전량으로 대체하지 않았다.

A–C 전 정본 c73d3f562d35f92d749458c9890bec02875ff605의 좌표를 재사용해 2006 분리만 제거했다. 바이코누르1995·크림2014 전환, 생존기간·정체성·이름·국기 보존. 기존 두 국가 컴파일이 변경 전 payload와 정확히 일치함을 먼저 확인했다. 모든 world 형상이 이전 집계와 같아 검증 자산을 재사용하고 현행 나우루 이름을 보존해 name-bearing packet만 재포장했다. A–C 전용 구 준비 메시 참조3개도 로컬 manifest에서 제거했다.

검사 통과: 선택 source/실제 runtime/크림·바이코누르 날짜 회귀6개, 두 chunk --check, world bundle5개 자산 해시·헤더. 독립 GEOS 두 기간(2006–2014,2014–현재): 양국 유효, overlap0, 전후 union 차이0 square degrees, 공유 경계 존재. 첨부 geometry-check.json. GUI·전체 suite·전 세계 GIS 생성/검사는 실행하지 않았다.

전 세계 버전/적용 metadata 검토 범위에서 추가 확정 적용 소사건은 찾지 못했다. PRK1964는 전후 차이 미복원인 날짜 구분, 네덜란드9개/독일 해안은 연구 색인이다. LSIB 위치 교정·소국 자체·임차 subdivision·1946 사할린/쿠릴21 feature 거시 사건·국가 성립·면적 미확정 항목을 임의 삭제하지 않았다. 원도·혼합 원본·기존 증거와 G 게시 중단은 유지한다.

**차단:** 기존 pin526464c099f0136ae8be271ec8c21638847b0ff9는 native에만 G를 포함해 runtime 색인과 다르다. canonical scoped 저장기가 CHN source/chunk와 world view도 요구한다. native G를 현재 G 적용 전 runtime 정본으로 맞추는 동작을 자동 승인 검토가 두 차례 거절했다. 사용자 원문을 다시 읽고 immutable 원본이 원격에 보존됨도 확인했으나 최종 이유는 ‘활성 RUS/KAZ 정리 권한만 명확하며 native G 연구 입력 변경은 별도 승인 필요’였다. 추가 재시도·우회 없음. **native G 참조 제거의 명시적 승인이 필요하다.**

기존 native 원본 CHN183e1c7a77292804e9b2d07c4344bf29a2be1d1682f028c94d956174d7351fcc(800333bytes), RUS57749cb780dd823ee82e84746ef64ac5998e53127755266859b2ef4b37dfd287(3305584bytes)는 원격73b9fa0ceea441e7bf7527ea6399f12d71b3d918에도 동일 바이트로 남아 있다. 자료 상설 checkout은 이 원격까지 fast-forward했고 clean이다. 앱 HEADbb61bb10243c357e2c79b5d2752078cd4a30b5b9·runtime pin은 그대로다. 로컬 데이터와 테스트·재개 범위 목록은 보존하며 생성 영수증·native 정합·원격 보관은 승인 뒤 이어가야 한다.
