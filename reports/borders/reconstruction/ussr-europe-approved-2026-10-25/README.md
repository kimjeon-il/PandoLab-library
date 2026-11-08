# 유럽1922 외곽 적용용 로컬 패치 — 최신 원격 기준

원격앱 c7549c04 / 데이터 e6b41735에서추출한 `research/europe-approved-baseline/` 4 source+builtin을 기준으로준비했다. **이 디렉터리는 로컬후보뿐이며 원본/저장소를쓰기하지않았다.** publication담당이최신원격guard를다시검사후반영한다.

## 대상과 기간
USSR/RSFSR/ByelorussianSSR/UkrainianSSR의 각 `1922-12-30-reviewed-v2` geometry만대상. validFrom1922-12-30 / validTo1925-05-12불변. 다른시기/타국/Bessarabia/물리해안/수계리소스불변. Armenia/Transcaucasia등다른공화국은대상아님.

## publication 입력
`application-manifest.json`에4객체별 source/builtin파일 SHA,원래geometry SHA,버전/ref,after geometry 경로와SHA,추가/제거delta를기록했다.
- `*-source-master-geometry.json`: 보존할원픽셀후보조합 원형.
- `*-source-display-geometry.json`: 실제선택 표시형상. 현행source도reviewed-display이므로적용권장대상이다.
- `*-compiled-display-geometry.json`: **기존compiled에국소 add/remove delta만적용**. source전체를compiled에덮어쓰지않았고비유럽기존clipping을보존했다.
- `*-add.geojson`/`*-remove.geojson`: source 변경의정확국소delta. compiled 변경이이delta바깥으로번지지않음을확인했다.
- `shared-and-locked-guards.json`: 공화국분할공유선/해안정확subsequence/현대137점보존.

## 승인 후보 선택
- 핀란드 EOX2016 해안 보정은 제외. 기존남해안1397..1406과북해안2152→2153→2154를정확보존. 기존남해안끝C→역사A **2.524km/8.28CSSpx**는국경을기존해안모델에연결하기위한표시접합한계이며작은오차라고표현하지않는다. 철회B해상연장안을부활시키지않았다.
- 에스토니아10점호수선으로lake-only교체. 기존육상/해안/강은보존.
- 라트비아북접속+승인v8+t끝교정파생선 사용. 별도Ludza보강은양끝지물접합미확정으로**미편입**,기존승인v8유지. 보완원도자료는보존한다.
- 폴란드연속1991점+공화국내부선과의실제교점J1/J2두점삽입. 외곽은RSFSR/BLR/UKR과같은좌표/선분을공유한다. 기존내부선의바깥꼬리만교점까지절단하며내부방향/나머지공유선은보존.
- 드네스트르승인교점이후기존선과베사라비아는불변.

## 1:1천만 가벼운 단순화/강보존
라트비아 Pleiki–Dubniki의원도상명확한육상7점을4점으로만단순화,전체1737→1734. tolerance0.0005°,실제최대43.75665m/0.102025CSSpx(종이상0.004376mm). 모든하천/판독모호구간은원본유지. 폴란드1991점전체,에스토니아10점,핀란드380점(현대재사용137점포함)은추가단순화하지않았다. 이름이land라는이유만으로혼합하천구간을줄이지않았다. 명확히판독된범위만줄였으므로추가단순화가없거나매우적은구간이있다는제한을보고한다.

## 근거·시기 한계
이것은승인된1922재구성후보의기하반영이며모든후대세부를1922법적측량선으로확정하는것이아니다. Lipienie/Morocz개별의결·인계일,드비나주항로미세위치 등은별도보류기록을유지한다. 새사건일/가상건국일을만들지않는다. 원래ZIP/hash는baseline근거식별자로보존하고새국소보정기록을추가해야한다.

검증은대상4객체국소형상/공유선/잠금원좌표와compiled delta밖보존만수행했다. 전세계테스트/전체재생성/main병합/배포/포터블작업없음.

## 원자료와 기존 근거 기록 — 추적용 목록
아래 경로는 작업 산출물 루트 `research/europe1922/` 기준이다. 이 README와 함께 모든 원본 스캔이 저장소에 배포된다는 뜻은 아니다. 공개 URL은 원자료 재확인용이며, 후대 지도 발행일을 1922 경계 확정일로 해석하지 않는다. 초기 조사 README보다 아래 최종 선택 manifest/후속 보고서를 우선한다.

### 핀란드
- 최종 해안 보존 선택: `finland/coast-preserved-application/manifest.json`; 육상 후보와 지역별 정합: `finland/final-review/manifest.json`, `finland/historical-joins/{karelia,salla,petsamo}/README.md`; 현대 공유선: `finland/modern-reuse/manifest.json`.
- 남쪽 원도: Finnish Land Survey, Terijoki–Valkeasaari 1:50,000, 1921–1922 발행(기초 측량은 더 오래됨). [원본 JPEG](https://timomeriluoto.kapsi.fi/KARTAT/Topografiset%20kartat/Topografinen%20kartta%201:50.000%20Terijoki-Valkeasaari%201921-1922%20%282+0%29.jpg). 해시·해상도: `finland/historical-joins/karelia/terijoki-source.json`; 지역 분할 정합: 같은 폴더 `50k-registration.json`.
- 북쪽 Vaitolahti 원도: [기관 카탈로그](https://expo.oscapps.jyu.fi/s/vanhakartta/item/58805), [원본 JPEG](https://expo.oscapps.jyu.fi/files/original/711be4b1077a2e5143010ca7be10849ff704ee48.jpg). 판독·보존 범위는 `finland/historical-joins/petsamo/README.md`.
- 현대와 존치 구간/할양 구간 구분 문헌: [International Boundary Study No.74](https://library.law.fsu.edu/Digital-Collections/LimitsinSeas/pdf/ibs074.pdf), [Finlex HE22/2018](https://www.finlex.fi/fi/hallituksen-esitykset/2018/22). 이 문헌만으로 모든 원도 끝점의 정밀 위치를 인증하지 않는다.
- 제외 자료: `finland/south-coast-patch-v2/` EOX 해안 보정은 이번 적용에 사용하지 않았다.

### 에스토니아 호수 경계
- 최종 선택: `estonia/retrace/patch-v2/README.md`, `joined-shared-boundary.geojson`; 출처 해시·취득 정보: `estonia/retrace/source.json`; 정본 해석: `estonia/retrace/TREATY-CROSSCHECK.md`.
- [공식 역사 지도 WMS](https://kaart.maaamet.ee/wms/ajalooline?request=GetCapabilities&service=WMS&version=1.3.0): 1933/1935 1:200,000 지역 래스터를 실제 확보하여 호안과 수면 국제경계 기호를 구분했다. WMS EPSG:3301은 제공 좌표계이지 원도 투영이라는 뜻이 아니다.
- [1920 타르투 조약 부속 원도](https://commons.wikimedia.org/wiki/File:Tartu_rahu_kaart_1920.jpg), [국제연맹 조약집 제11권, No.289](https://treaties.un.org/doc/Publication/UNTS/LON/Volume%2011/v11.pdf). 정본의 Poddubje 서쪽 표현과 번역본 불일치를 교차 확인했다. 부속 원도를 직접 정밀 좌표화했다고 주장하지 않는다.

### 라트비아
- 원본 1921 지도: [LNB 원본](https://dom.lndb.lv/data/obj/file/33382381.jpeg), [카탈로그](https://dom.lndb.lv/data/obj/1039220.html), 1:800,000 제2판. 1930 상세 재추적 기준: [LNB 원본](https://dom.lndb.lv/data/obj/file/24799059.jpeg), 1:400,000. 교차 원도: [1923 제작/1924 달력 지도](https://dom.lndb.lv/data/obj/file/24846025.jpeg). 원자료 판독/경도 원점 차이: `latvia/README.md`.
- 최종 북쪽 접속: `latvia/north-join-v1/manifest.json`; 승인 v8 남쪽 중첩 연결: `latvia/southern-junction-review/full-overlap/README.md`; 실제 적용 원형·표시형 및 비하천 단순화 증거: `latvia/final-landonly-simplification/{README.md,analysis.json,106-land-proof.png}`.
- `latvia/supplement-ludza-1922survey/`는 미채택 보완 자료다. 1923 측계 전후의 모든 미세 차이가 해소되었다는 뜻은 아니다.

### 폴란드와 드네스트르 접점
- 최종 연속 후보·접속 이력: `poland/whole-continuous-v1/{README.md,artifact-manifest.json,original-preservation.json}`; 상세 연결 자료는 `poland/overlap-continuous-v1/`, `poland/north/dvina-to-wilejka-continuous/`, `poland/middle-continuous-candidate/`, `poland/south-continuous-v1/`. 공화국 공유 교점: `poland/application-readonly-plan/application-junctions.json`.
- WIG 원도 다운로드 URL/해시/해상도: `poland/north/manifest.json`, `poland/whole/download-manifest.json`, `poland/whole/download-extra-manifest.json`, `poland/whole/download-extra2-manifest.json`, `poland/seam52-followup/new-source-downloads.json`. 대표 원본: [Dyneburg1924](http://maps.mapywig.org/m/WIG_maps/series/300K/28_Dyneburg_1924.jpg), [Wilejka1924](http://maps.mapywig.org/m/WIG_maps/series/300K/38_WILEJKA_1924.jpg), [Minsk1922](http://maps.mapywig.org/m/WIG_maps/series/300K/48_Minsk_1922.jpg), [Sarny1928](http://maps.mapywig.org/m/WIG_maps/series/300K/68_SARNY_1928.jpg), [Kamieniec Podolski1929](http://maps.mapywig.org/m/WIG_maps/series/300K/98_KAMIENIEC_PODOLSKI_1929.jpg). 상세도와 중첩 구간을 사용했으며 이 대표 목록만으로 전체 선을 만들었다는 뜻은 아니다.
- 법적 시기 구분: [리가조약1921 공식 PDF](https://eli.gov.pl/api/acts/DU/1921/300/text.pdf), [1924 의정서의1933 공포문](https://eli.gov.pl/api/acts/DU/1933/541/text.pdf), [Kochanowski1994 원문 pp.59–74](https://bazhum.muzhp.pl/media/texts/przeglad-historyczny/1994-tom-85-numer-1-2/przeglad_historyczny-r1994-t85-n1_2-s59-74.pdf). 실제 확보 본문·페이지 이미지와 개별 보류는 `poland/legal/epoch-review/{README.md,DECISION-TABLE.md}`. 1922 거시 경계 설정·인계와 후대 도엽의 모든 세부 굴곡 확정은 별개다.
- 드네스트르 기존 승인 근거는 작업 루트의 `research/gap-audit-1922/approved-patch/manifest.json`. 이번 새 폴란드 선의 남단을 그 승인 교점에 일치시키고 그 이후 강 좌표 및 베사라비아는 보존했다.

## 처리 결과

GEO-USSR-EUROPE-20261025. work/gis 전용 반영. 위 로컬 후보 상태 문구는 후보 작성 당시 기록이며, 이번 저장에서는 source/runtime의 대상 네 객체에 표시용 형상을 적용했다. 존속기간 및 다른 시기 형상은 보존했다. 기존 드네스트르 보정과 베사라비아 귀속, 이웃 국가 및 수계/해안 자원은 변경하지 않았다. source index 네 항목과 builtin sourceRevisions·content references 및 packed transport만 갱신했다. 준비 메시 입력 해시는 조작하지 않았으며 새 geometry content key는 정상 캐시 미스로 생성된다.

새 좌표 파일 해시·원본 대상 해시·기간·다른 시기 보존과 네 객체 pack 해시는 통합 단계에서 확인했다. 공유선/기하 검사는 후보 담당의 함께 보관된 결과를 재사용했으며 전세계 검사/생성기는 실행하지 않았다. 앱 main 병합과 공개 배포는 하지 않았다.
