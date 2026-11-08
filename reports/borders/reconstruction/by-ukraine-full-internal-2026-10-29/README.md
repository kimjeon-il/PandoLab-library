# 벨라루스·우크라이나 내부 경계 전체 재검토 — 실제 반영 준비

상태: source/compiled/native 반영본과 독립 최종 검토 통과. 실제 원격 커밋은 Git 이력과 작업 결과 통지로 확인한다. 데이터 기준 `cbf25b306d9b58b2febc3c69bc8f3e4c14a80e43`; 사용 코드 기준 `1860e3db66a80d5d76e7279a414536439e49b5bb`. 이는 work/gis 반영 범위이며 main 통합·공개 배포 보고가 아니다.

## 범위와 판독 결과
네 공유선의 기존 498개 변을 모두 검토했다. 판독 가능한 노선만 수정하고 불확실한 구간은 그대로 보존한다.
- BY–RSFSR: 104변 중 92변 재추적, 12변 문자·철도·교차점 불명확으로 보존. 표시 105→164점.
- BY–Ukraine: 23변 검토·재추적. 표시 24→47점.
- Ukraine–RSFSR 본토: 273변 중 235변 전체 재추적, 4변 일부 재추적, 34변 전체 보존. 원형380점 / 표시369점(기존274점).
- Crimea/Perekop/Syvash: 98변 전체 검토. 정치적 수상 경계가 없는 95변과 등록·접합 불확실성이 남은 Perekop 육상3변을 모두 보존. 기존99점 변경 없음.
전체 검토가 전체 좌표 변경이나 역사적 전구간 확정을 뜻하지 않는다. 삼국점·외부 접속점·기존 외곽선은 잠근다. 기존 Mozyr 목부 부분안은 이번 전체안에 포함되므로 따로 중복 적용하지 않는다.

## 근거와 정밀도
벨라루스: BSSR CEC 1924 지도에 명시된 1920–1924 옛 경계 파선. 이후 확대지역 음영은 추적하지 않았다.
https://commons.wikimedia.org/wiki/File:Bie%C5%82aru%C5%9B._%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D1%8C_(1924).jpg
15개 인쇄 격자점 quadratic 등록, LOO RMS2.189px/max4.040px. 추가 보류 격자점 검증 기록을 보존한다.

우크라이나: 1922년1월 NKVD 지도 원도. HURI 목록과 RGASPI 제공 스캔.
https://www.gis.huri.harvard.edu/resource/january-1922
https://donbass.ostkraft.ru/razdel-3/administrativnaya-karta-ukrainskoj-sovetskoj-soczialisticheskoj-respubliki-yanvar-1922-g/
수동 관측392점 원형과 도시 기호 중심 교정 이력을 보존. 연속 LCC 계산 좌표계+affine 등록, fit RMS3.63km/LOO RMS4.29km/max7.53km, 독립 Zhytomyr1.58km. 계산 투영을 원도 투영이나 Pulkovo 경선 확정으로 오인하지 않는다. 실제 교차점에서만 접합하고 Konotop 가림 구간을 임의 직선으로 만들지 않는다. 1923년 지도는 별도 비교 근거이며 1922년으로 소급하지 않는다.

100m는 별도 표시 파생본의 보수적 일반화 허용값이지 천만분의1의 보편 허용오차나 역사적 측량 정확도가 아니다. 원도 자체 위치 오차와 연대 불확실성이 남아 `provisional`이다. 수작업 경로이며 managed Map Toolkit 엔진을 실행했다고 주장하지 않는다. 원도와 원형은 개인 복구 자료로 유지하며 공개 저장소에는 자동 업로드하지 않는다.

## 객체·기간·중요 보류
대상은 BY/Ukraine/RSFSR 세 기존 객체의 `1922-12-30-reviewed-v2` 형상이다. 국가 lifetime은 변경하지 않는다. 조사 하한1801을 건국일로 만들지 않는다. 기존 형상 선택기간1922-12-30~1925-05-12를 유지할 뿐, 새 역사 사건이나 법적 유효기간을 확정하지 않는다.
- BSSR1924 확대를 기존 기간이 가로지르는 문제는 미해결: 별도 사건·객체·효력일 검증 필요.
- Ukraine1922년1월 원도만으로12월30일까지 불변임을 증명하지 못한다.
- 1925-05-12는 이번에 확정한 경계 변경일이 아니다.

## 실제 적용 방식·검증
세 source를 먼저 일관되게 수정한 뒤 기존 compiled에 국소 source delta만 적용한다. 전체 재생성을 하지 않으며 중국·카스피해 및 이전 compiled-only 외곽 보정을 보존한다. native/index와 전송 묶음은 변경3객체를 반영하여 한 번 다시 작성했다.
- 세 source 유효; 겹침0, 합집합차0.
- 실제 compiled 유효; 겹침0, 합집합차1.58e-17deg²(부동소수 잔차).
- 다른 시점의 binding/geometry 동일; 변경영역 밖 잔차 최대6.86e-16deg².
- 관련 없는 compiled273청크 바이트 동일. native 변경객체는 정확히3개. source/native 직렬화 일치.
- 전송 SHA256 `1d4a539a4e4c7bc6eabd672fdd699df829b46af12d6bd1282f6a1a6f1171f49d`.
- delta focused tests4통과. 전체 테스트·브라우저 표시·배포 검증은 실행하지 않았다.
- 상세 실측/독립검토는 [source-verification.json](source-verification.json), [runtime-geometry-verification.json](runtime-geometry-verification.json) 및 [independent-runtime-review.json](independent-runtime-review.json) 참고.

원격 게시 시 최신 브랜치와 충돌 재확인 필요. main 병합·배포·포터블 생성 없음. 실제 코드 함수가 현재1860e3db와 동일함을 검증했다. 원본 복구 파일은 별도 Library 보존.

## 주황색 보존 구간 한정 재확인
사용자 추가 지시에 따라 새 전면 조사 없이 기존 원도로 보존 구간을 조금 더 확인했다. BY 12변/6묶음은 모두 유지한다. 교통선·문자 아래 중심선은 확정할 수 없고 edge57/Mozyr에 몇 원픽셀 차이는 보이지만 새 큰 돌출·함몰 근거는 없다. 유지가 완전 동일성이나 역사적 정확성의 증명은 아니다. 상세 추가 검토는 별도 addendum을 따른다.

Ukraine 주황색 구간도 유지하되 이유를 구분한다. 삼국점·해안 접속·Perekop에는 수정할 만큼 명확한 큰 차이 근거가 없고 Syvash 수상 정치경계는 원도에 없다. **Konotop는 단순히 ‘차이가 작다’는 판정이 아니다.** 동일 등록틀의 비교에서 최대13.74km 이격이 보이나 원도 문자 가림,1923지도 접힘·시점 차이와 안전한 접합 미확정 때문에 현행을 보존한다. 표시상 미해결 구간이며 같은 위치라는 보증이 아니다. 이번 추가 검토로 후보 좌표와 실제 staging은 변경하지 않았다.


## 동시 작업 보존
앱 최신 work/gis의 자료 핀이 다른 작업의 Artsakh 명칭 변경과 중국 경계를 합친 ef77d017로 이동했다. 이번 BY/Ukraine 적용 bc97f169 위에 그 명칭 변경만 충돌 해소하여 보존했다. 이미 검증한 세 공화국을 포함한275청크는 이 명칭 통합 전후 바이트 동일하며 국가 형상은 다시 만들지 않았다. 최종 transport는 8b0e53e4463609d463344ab2cb646bdad63927298f0a75b4bbb589cd42aa1c33이다. 기존보고와 카스피해 상태정정도 유지한다.
앱 연결 커밋은 [skip ci] 사용: 기존 P2의 범위 밖 전체 재생성 위험이 수정되지 않았음을 확인했다. 집중 회귀4개와 실제 독립 형상 검증을 시행했으며 자동 CI/전체검사 통과를 주장하지 않는다.
