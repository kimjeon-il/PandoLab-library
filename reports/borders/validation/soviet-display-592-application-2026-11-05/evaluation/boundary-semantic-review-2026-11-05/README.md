# 역사 국경 표시 상세도 — 의미 보호를 구분한 중간안

상태: 새 로컬 중간안 검증. 전체 역사 국경의 NE 목표 달성 또는 운영 채택 완료가 아니다. 기존 strong/weak/mixed/Darja 결과와 원본을 보존했으며 production source·활성 native 등록·pin·commit/push·원격 보고서를 변경하지 않았다. 이 README는 scratch 연구 인계 자료이며 canonical report publication은 실행하지 않았다.

## 선택한 조합

서부는 Latvia250m와Poland250m에 원래 프리피야트 북 접속점988을 추가 보존한다. Poland1991→671점이다. source987→988의360.919m 접속 역할을 보수적으로 지키는 것으로, 측량 위치·독립 역사 하천교차를 인증하는 것은 아니다. J1/J2·Latvia–Poland·Dniester 접점은40개 source/candidate 사본에서 정확히 남았다.

동부는 source 근거가 확인된18·20·23·25만 중간 파생본으로 바꾸고 나머지10개는 기존 weak로 유지한다. source 전체14개 point entry는1059→764점(기존weak908,원래강한500m253). 연결 route는4355→4060점이다. feature 공유 끝점 중복이 있어 세계 고유 정점 수로 합산하지 않는다.

|feature|원래|기존weak|중간안|지역cap|보호 근거|
|---|---:|---:|---:|---:|---|
|2 Pamir-22-lower|74|67|67|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|
|4 Pamir-21-lower|66|65|65|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|
|8 Pamir-21-upper|44|40|40|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|
|12 Pamir-source-10|212|187|187|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|
|18 Pamir-source-7|61|54|38|250|upstream ZIP map/mask/master SHA and current subset verified|
|20 Pamir-source-6|64|61|38|500|upstream ZIP map/mask/master SHA and current subset verified|
|23 Pamir-source-4|89|70|58|500|upstream ZIP map/mask/master SHA, Saar named anchor verified|
|25 Pamir-source-3|129|126|33|500|local originalGIF SHA/pixels checked; upstream mask/registration/master verified|
|27 Pamir-source-2|21|19|19|유지|local sameGIF; upstream90point master; embedded mask; no new replacement selected|
|35 W03-light-2|60|56|56|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|
|37 W03-light-3|83|56|56|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|
|39 W03-light-4|20|18|18|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|
|44 KAZ-sary-light|53|35|35|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|
|48 KAZ-chagan-light|83|54|54|유지|원도/분류 mask가 확인한 로컬·두ZIP 범위에서 미확보; metadata만으로 새 의미 통과 처리하지 않음|

## 무엇을 보호했는가

18: 서도곽 raw0/current60과 P15-near 인쇄 접점 raw159/current0, 원래 source-mask 앵커를 모두 보존.20: Uz-Bel4651.2 raw0/current63과 동도곽 raw176/current0 및 원래 source-mask 앵커를 모두 보존.23: Saar/Karazak5227 raw119/current47 [73.71175827378428,38.846460358426164]을 보존. source_mask의Saar115–126,Chumbagysh158–167,4584고개/길190–198,남쪽굽이/문자204–211에 대응하는 현재 범위도 모두 보존. 새 대표 지형점을 임의로 만들지 않았다. 이 세 구간은 원래 source-mask anchor를 유지하고 이전 shortcut 끝점·40도 기준을 독립 의미점과 같은 권위로 고정하지 않았다.

25: Караарт4791.3 인쇄 접점 raw203/current2 [73.84024053106174,39.001812386240246]과 별도 도곽 기술 끝점 raw205/current0 [73.84071302874241,38.99998550990847],북쪽 가시대시 raw0/current128을 구분해 보존. possible-water/contact raw120–125,138–143,201–205의 현재17점은 전부 그대로 남긴다. 그 밖의 문자·기호 중첩 모든 점을 각각 확정 의미점으로 확대하지 않는다. 대신 기존2km macro skeleton을 표시상 큰 굴곡 보호로 사용한다. 이 skeleton은 알고리즘 안전장치이지 역사적 권위점이 아니다.

기존 강한500m는25 current2를 삭제하여 원선 기준후보 선분까지48.25247m,23 current47을 삭제하여211.90057m 떨어진다(같은 기존AEQD 입력에서 upstream계산). 이것이 곧 큰 국경 노선 오류라는 뜻은 아니나, 실제 기록된 명명 접점을 정확히 고정하지 못한 점은 확인됐다. 새 중간안은이두점을 정확히 보존한다.

25의더보수적인86점안은모든불확실구간경계/major묶음을고정한비교안으로보존했고,최종이번연구안33점과구분한다. 126개가모두하천보호점이거나모두자동곡률점이라는주장은하지않는다. 원도는검정경계대시가갈색산지와조밀한청색빙설영역을지나며일관된단일하천추종으로보이지않는다. raw master 보존과 표시 파생본 일반화는 별개다. 과거 authorization 문자열은 이력일 뿐 새 권한 근거로 사용하지 않았다.

27은기존19점안유지다. 현재물/채널구간local17과pixel-context큰굽이6점이남지만,기존weak도원래넓은uncertainty/buffer분류2점을생략한한계는이전보고와동일하다. 현대비교선3점은거의직선이라굴곡비가불안정하며,밀도만으로전체노선을현대화하지않았다. 다른9개는원자료가확인된두ZIP에없었고기존archive/local연구경로에도상세mask를찾지못했다. 다른모든보관위치에존재하지않는다는뜻은아니다.

## NE 목표 비교

현재CHN의대응14arc195pointentry를지역표시상세도참조로쓴다. opaque version ID paektu-lsib-11.4를원자료의순수NE인증으로취급하지않는다. 기존의exactnativearc대응증거를재사용한다. 서로다른정치시기노선이므로현대선과의거리나전체굴곡차이를순수단순화오차로부르지않는다.

모든변형에같은localAEQD미터좌표·1/5km고정거리·8개위상을사용했다. 0길이edge는model에서삭제하지않고sampling에서만임시제외하며rawpoint수와nonzero sampling수를분리했다. 기존Space계산과위상정의가달라absolute turn값을그대로동일계산이라고주장하지않는다. 기존형상·여러후보·현대참조를이방법으로동시에비교했다.

|feature|선택안/현재 밀도비|1km굴곡비|5km굴곡비|현재 판정|
|---|---:|---:|---:|---|
|18|2.17|1.82|1.04|큰윤곽은참조에근접;미세굴곡/밀도차이남음|
|20|4.15|4.35|1.64|역사/현대큰노선차이와보호구간영향남음;완전NE등가미확정|
|23|2.43|3.36|1.06|큰윤곽은참조에근접;미세굴곡/밀도차이남음|
|25|2.16|5.45|2.06|역사/현대큰노선차이와보호구간영향남음;완전NE등가미확정|

NE target 전체 달성으로 판정한 동부 구간은 없다.18/23은5km큰굴곡에서약1.04/1.06배로근접하지만1km와밀도차이가남는다.20/25는큰노선차이도남으므로현대율을강제하면원래역사경로를변형할위험이있다. 나머지10개를유지했다는사실만으로목표달성으로세지않았다. 각구간의원래/weak/250/500/current및선택안길이·간격·굴곡은east14-ne-detail.json/CSV와selected-east-ne-metrics.json에있다.

명목cap은18=250m,20/23/25=500m이며전세계공통허용치가아니다. 선택안의원래정점→대응shortcut실제최대는약245.8/364.4/440.1/493.3m다. 이는계산한투영polyline의알고리즘상한지표이며지상측량정확도나정확한연속측지Hausdorff라고부르지않는다. 평균LSIB편차를DP허용치로바꾸지않았다.

## 서부 수문 역할

부모의원래검토이미지독립픽셀조사에서Dvina접속은동일지류교차,프리피야트북/남접속은본류횡단과지류횡단,남부는Zbruch→기존Dniester연결임이확인됐다. 후대도엽의거시노선/기술접속과1922법적측량위치를구분한다. 프리피야트북접속987/988은원래좌표를둘다보존하도록이번중간안에서복원했다. 남쪽1079,J1/J2,Latvia/Poland,Dniester는유지한다. source95.8m연결의1713/1714대응은여전히미확정이어서확정의미점으로새등록하지않았다.

기존현대hydro를정답으로강제하지않았다. canonical loadSelectedHydroFeatures를명시적서부bbox로읽어7logical systems/26fragments만확인했으며,이현대context만으로역사교차횟수인증은하지않았다. parent의원래그림/채택선대조에서본류→지류순서와거시횡단연속성이유지된다는근거를사용한다. 독립역사하천벡터전수교차검사나새지오리퍼런싱은하지않았다.

## 원자료 실제 확인

J43-028.gif는기록된정상공개URL https://github.com/ramSeraph/russian_world_topo_maps/releases/download/100k-gs-orig-extra3/J43-028.gif 에서받아SHA823c6377cfebe6fdb7effcd60d913ef9986a1d180746053e17fce97b33cfe482와정확히일치함을확인하고로컬실제픽셀을열었다. 실패한Space전송의우회가아니라공개원도정상읽기다. 원본1973도엽이1922법적경계인증이라는뜻은아니다.

LNB1930원도 https://dom.lndb.lv/data/obj/file/24799059.jpeg 도정상경로로받아새SHA bda1c0248d77f8f8b19d320207a9c7d9f034617395d68949a9aad20bef6782c4를기록했다.15014x9907원본은보존하고900pxoverview의실제픽셀을보았다. 특정95.8m접합의독립좌표판독을한것은아니다. 첫큰overview출력은도구출력크기제한으로보지못했고작은overview로나라전체윤곽을확인했다.

18/20/23원도·mask·master및등록정보의ZIPmember해시와원도판독은부모의독립클라우드조사결과로구분한다. 직접로컬픽셀을봤다고주장하지않는다. 해당원도SHA는J43-053 b318d0fcc649be3de2aa92cd4e9bf738b39d5d071b4bb8f25af16b7dfdf90839,J43-052 85a1c5b4c88d51c7a71ac1a0f3b7981614eb0b8e04477d2b167fe03662cde5a3,J43-040 8983f796ca374a1c24d981904aeb257b2ce70e2e1baf188aef7645aca8d42fe3이다.25registration SHA ea16e448df3f1aee3ac986f6e57ba85feafdd4330dde9ff741d39194ec6763d1,mask SHA d1b75c649ea2a2986a0313c78804249e15e5544885c899a9a7fec7e2550ac2d0이며raw/pixel-master를새로재구축하지않았다.

## 실행한 검증과 아직 하지 않은 일

selected/topology-checks.json: source/native-model3개와compiled3개형상유효,면/구멍수·범위밖좌표순서보존. source/compiled변경영역불일치0,구성국변경영역합집합대비USSR차이0,구성국겹침변화0.

selected/downstream-local-audit.json:6관련국가/1922-12·1925-06만prepared생성,31개중25재사용/6신규.6신규packetdecode,12날짜경계,무관source descriptor283/compiled275보존,기존manifest421항목보존. 의미/기술점8개를2국가x2layer의32사본에서정확보존하고25의17접촉점및23의4불확실고개/문자범위를정확보존했다. 폴란드접속추가도USSR/BY같은사슬이다.

기존검토게이트는변경3건을미완성review로정상거부한다. passing receipt를만들거나활성native library등록을하지않았다. Atrek/Darja/물리68holes/Aral,Monaco,한국롤백,작은영토변경제거및다른기간을보존했다. 무관한physical전체나전세계GIS/전체suite는반복하지않았다.

실제Viewer지원개발경로에서read-onlyselectedoverlay를표시했다.1922-12 WebGL2,변경3형상정확한geometry digest존재,국가114표시,페이지오류/경고0. dataCommit=null과연구dataRevision으로운영pin과구분한다. 실제screenshot의작은읽기본및selected-comparison.png픽셀을열어확인했다. 이는전체화면의윤곽/레이어표시확인이며원도모든고개나고배율틈을시각인증한것이아니다. native Windows실행파일별도검사/배포/포터블생성은하지않았다.브라우저/로컬서버는종료했다.

남은범위는9개원자료미확보구간과27의추가표현판정,그리고20/25에서큰역사노선차이와과밀묘사를더구분하는제한된검토다. 모든정점river/land분류나정밀지형재구축을새종료관문으로삼지않는다. 현재중간안은기술생성가능·기하/downstream/표시통과이며전체역사/NE의미검토통과와는다르다. 원격·생산반영은이번지시범위밖이라미실행이고거절된작업을재시도하지않았다. 기존스크립트변경거절은그대로유지하며새scratch실행본만사용했다.
