# 소련·우크라이나1922 드네스트르 내장 수계 정렬

- ID: GEO-USSR-DNIESTER-20261025
- 상태: 최소 범위 적용 / work-gis-only / 공개 미배포
- 기준: 앱 c4672cac416bfcb481671b2912fc017cdb945c20, 자료 9d3ca74c7b81091114a3b23e7cd1394d43623ec2. 소련 성립일1922-12-30 수정은 유지.
- 대상: state:soviet-union 및 state:soviet-union-ukrainian-ssr의 :1922-12-30-reviewed-v2만. 기간1922-12-30~1925-05-12. 이후 형상·존속기간은 불변.

## 승인과 근거
사용자는 내장 강을 따라 나누되 베사라비아는 추후 루마니아 작업에서 편입하므로 건드리지 말라고 지시했다. 루마니아 객체와 베사라비아 편입/소유 관계는 수정하지 않는다. 내장 Dniester/Nistru hydro-system20478829의 hydro.bin SHA256 f0832dd2024cbfad8b1662410a4f189fa95bcecb56c3e3f1ad69d36af4a0c36f를 사용했다. 이는 기존 조사와 결합한 현대 수계 기반 지도 축척 근사이며1922년 법적 수로 중심선 측량 확정이 아니다.

## 변경
원본 source와 기존 compiled 형상에 동일 국소delta를 적용했다. 다른 지역의 기존 소련 overlap 제외는 보존했다. 북쪽은 기존 경계와 내장 강의 정확한 교점에 연결했고, 하구는 내장 수계 끝과 보존한 외해 해안점을 최소 폐합했다. 약1km 접속부는 앱 최대배율 약2.87 CSS px이며 추정 기하폐합이지 독립 사료로 확정된 역사 국경이 아니다.

## 최소 확인
- 변경2개 source/builtin 폴리곤 유효, 강 공유선 누락0, 변경mask 밖 compiled 대칭차면적0.
- ROI [26,46,31,49]에서 우크라이나의 소련 밖 면적0, 루마니아와 신규 겹침0.
- 하구 ROI [30.35,46.04,30.55,46.2]에서 기존 소련 땅 제거면적0. 기존 외해 해안 보존. 다만 고해상도1922 육지/수면 마스크를 검사한 것은 아니므로 사주·수로의 당시 법적 귀속을 새로 확정하지 않는다.
- source/chunk/index 및 해당 builtin geometryBindings/sourceBindings의 새 content hash를 일치시킴. 다른 기간 geometry와 루마니아 데이터 불변.
- 기존 pack 기능으로 transport와offset만 갱신. 전세계 겹침 계산/재생성·전체검사·렌더러 코드는 수행/변경하지 않았다.
- prepared mesh는 실제 geometry digest가 달라 기존 mesh를 새형상에 재사용하지 않는다. 새digest는 cache miss이므로 기존 정상 runtime 생성 경로를 사용한다. 기존 mesh manifest의 생성 출처 해시도 바꾸지 않았다.

## 자료
manifest.json은 후보 생성 증명, integration-proof.json은 JS 런타임 content hash/참조와 실제 적용을 기록한다. Python compact JSON과 JS JSON.stringify의 숫자 직렬화 해시를 혼용하지 않고 CandidateFileSHA256으로 동일 후보 파일을 고정했다. 원본 approved ZIP의 해시는 원자료 식별자로 유지하고 파생수정 provenance를 각 대상 버전에 추가했다.

## 게시
work/gis만 반영. main 병합·publication channel·공개 배포·포터블 생성은 제외.
