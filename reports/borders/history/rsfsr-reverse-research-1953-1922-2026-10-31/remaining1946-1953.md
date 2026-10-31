# RSFSR 1946–1953 원장 범위 검토
검토 2026-10-31 UTC. 기존 master-events.json v1(106기록), Library libfile_b6a4b18714588191aebf3db6f60c84e4 읽기 및 복원본 재사용. 원격변경·새 폴리곤 없음.

## 핵심 진전
**핀란드1947 얘니스코스키·니스카코스키**의 UN 원조약 부속지도(1:100,000)를 실제 확보·육안검토했다. 법률상 새선의 다섯 좌표와 마지막 삼합점 연결을 전사했다. 정합·datum 검증 전이므로 GeoJSON 확정선은 아니다. **쾨니히스베르크 원장 주석의 개칭일 7July1946은 4July1946으로 정정할 근거를 찾았다.** 개칭은 영토이동이 아니다.

## 전체 커버리지 행렬
분류는 confirmed=사건확인,conditional=형상조건부,held=추가이동/세부미확정,notneeded=새RSFSR외곽이동아님. 한 사건의 법적확인과 형상준비는 따로 적는다.

|원장ID|날짜|법적상태|형상준비/분류|남은 작업|
|---|---|---|---|---|
|east-1946-south-sakhalin-kurils|1946-02-02행정편입|confirmed|conditional|기존 섬별 형상·1945점령속성 분리,남사할린50도 옛경계와섬목록 검증|
|DE-1946|1946-04-07 RSFSR주설치|confirmed|conditional|1945점령/포츠담과 분리,당시남쪽폴란드선은PL-1945-56보류클러스터 의존|
|west-1946-estonia-delimitation|1946-08-27경계설정|confirmed 문서전사|held / 추가양도미증명|1944이관후 경계설명으로중복면적제외;발령기관전사불일치원본확인|
|west-1946-kfssr-delimitation|1946-08-27경계설정|confirmed 문서전사|held / 추가양도미증명|1944-11-24지구이관후정의로중복방지;이제직접원문경로확보|
|west-1946-latvia-boundary-definition|1946-10-19소련승인;라트비아10-05,RSFSR10-12동의(원장)|문서존재confirmed|held|1944아브레네전체를1946에또이관하지않음;원부속도필요|
|FI-1947|1947-02-03서명 / **1947-04-18발효**|confirmed|conditional,원부속지도+좌표확보|지구datum·이후1:25k표석지도확인;실무인도일미확인|
|NO-1947|1947-12-18서명 / **1949-05-23발효**|confirmed|conditional|18장1:25k위원회지도중해당섬도엽찾기;면적에서폭추정금지|
|PL-1945-56|null일자,1945–1956구간|held 후보클러스터|held|Ostre Bardo·Szczurkowo등각지역원프로토콜없음;1946-04-07이전은아직RSFSR외곽아님|
|west-1953-alakurtti-candidate|null일자,1953주장|held, probable date error|notneeded as separate confirmed event|1954동의/1955-02-24전체셀소비에트이관보다약한증거.별도1953변경중복금지|

1948,1950–1953에 새로 확정된 직접RSFSR이관이 이 원장범위에서 발견되지 않았다. 이는 이 기간의 모든 세계자료를 완전조사했다는 선언은 아니다.1951Ialbuz의조지아내지구재배속은1955클루호리면적준비에필요한내부의존성이지그자체RSFSR외곽사건이아니다.

## 핀란드1947 새 원자료
[UN공식조약2939](https://treaties.un.org/Pages/showDetails.aspx?objid=0800000280149b8d), [원문UNTS216](https://treaties.un.org/doc/Publication/UNTS/Volume%20216/v216.pdf).176km²양도,서명1947-02-03,발효04-18.1955는UN등록/인쇄연도이며이관일이아니다.1:10만부속지도러시아어판PDFpage257와핀란드어판page255를육안확인.새국경굵은선과양도영역해칭이보인다.

원문순서 좌표:68°52.2′N28°48.4′E →68°53.2′N28°40′E →68°53.1′N28°28.4′E →68°54.9′N28°25.2′E →68°55.8′N28°30′E →북동직선으로소련/노르웨이/핀란드삼합점.경계위원회가후속1:25,000지도를작성·양국승인하도록규정.그후속지도와기준계는이번미확보이므로WGS84로자동해석하지않는다.

보존파일 `remaining1946-1953-sources/`:
- `unts216.pdf` 전체공식원문6.3MB.
- `fi1947-treaty2939-extract.pdf` 원문PDF247–265쪽,조약·부속도 포함2.2MB.
- `fi1947-russian-annex-map.png` 원문257쪽읽기용렌더.정합지도아님.
- `fi1947-coordinate-transcription.tsv`, `SOURCE.md`, `SHA256SUMS`.

## 1946 쾨니히스베르크
[대통령도서관](https://www.prlib.ru/node/619151)과[1956법령집scan80](https://ru.wikisource.org/wiki/Страница:Sbornik_zakonov_1938-1956.djvu/80)은04-07주설치/RSFSR편입과**07-04개칭**을구별한다.원장notes의07-07은주석수정대상.주설치일을러시아국가건국일로쓰지않고,당시관리자/편입속성의전환으로기록.기존현대칼리닌그라드외곽은1945–56지역조정미확정때문에당시와동일하다고단정하지않음.
PL클러스터기존자료보존: https://czasopisma.uni.lodz.pl/historica/article/download/25777/25607/63876 ; https://www.klgd.ru/city/history/almanac/a3_16.php . 이번원프로토콜추가확보없음.신문의'16회변경'을16개의날짜있는사건으로확장하지않음.

## 사할린·쿠릴1946
[소련명령전사](https://ru.wikisource.org/wiki/Указ_Президиума_ВС_СССР_от_2.02.1946_об_образовании_Южно-Сахалинской_области_в_составе_Хабаровского_края_РСФСР) 재열람:1946№5.1945군사점령과1946RSFSR행정편입은다른속성.남부4개섬분쟁상태를삭제하지않음.1947사할린주통합은RSFSR내부변경이며새국경이동아님.새해안선생성없음,기존섬별객체확인필요.

## 1946 경계정의 세 건
에스토니아 [전사](https://ru.wikisource.org/wiki/Указ_Президиума_ВС_СССР_от_27.08.1946_об_установлении_границы_между_РСФСР_и_Эстонской_ССР):본문RSFSR/표제와서명USSR불일치여전.1944법령근거·Narva수로·Kreenholm공장섬귀속이있지만,그자체신규양도면적은미증명.1957전후작업의기초설명으로활용,원본스캔확인전발령기관임의정정하지않음.
카렐리야 [직접전사](https://ru.wikisource.org/wiki/Указ_Президиума_ВС_СССР_от_27.08.1946_об_установлении_границы_между_РСФСР_и_Карело-Финской_ССР_на_Карельском_перешейке):기존카테고리목록대신실제문언확인.1944-11-24이관근거. Pitkäjärvi/Aitjärvi→Ilmeenjoki→Harjula(레닌그라드)→Pukinniemi·Salokiuru(카렐리야)→Kurosenjärvi북안→Kotkanniemi→Ladoga→Gumboritsy 경로.현대지명대응과지오레퍼런스는미완료.
라트비아 [1992공식법률](https://likumi.lv/ta/id/72436) 재열람.1946문서존재근거지만1946원도/양도델타아님.1992불인정결의를역사적물리국경변경으로넣지않음.

## 노르웨이1947 / 발효1949
기존원장세섬Kisteholmen약144,500m²,Brennholmen+무명섬약40,000m²전사판정유지.새명칭이나폭을추정하지않음.[미국공식IBS24](https://library.law.fsu.edu/Digital-Collections/LimitsinSeas/pdf/ibs024.pdf) 재열람으로기본위원회지도**1:25,000,18장**존재확인.표석총415개기술과세부수로경계자료가있지만작은섬의정확좌표를아직추출하지않음.소규모이므로무조건생략한다고결론내리지않고최대확대비교보류.
기존원장원자료: https://treaties.un.org/doc/Publication/UNTS/Volume%2052/v52.pdf ; https://www.stortinget.no/no/Saker-og-publikasjoner/Stortingsforhandlinger/Lesevisning/?p=1948&paid=2&wid=a&psid=DIVL1262&pgid=a_1000 . 1947-09-04현장표석작업완료/12-18서명/1949-05-23발효를같은날로합치지않음.

## 한계와 다음 작업
이행렬은범위커버리지완료이지모든형상준비완료가아니다.가장준비가앞선새대상은FI1947(법문+원좌표+원지도).원문datum·정합과기존객체중복확인후에만적용.1946경계정의3건은1944자료와연결해중복이관차단.원격커밋없음.
