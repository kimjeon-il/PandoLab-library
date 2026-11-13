import fs from'node:fs';import path from'node:path';import{createHash}from'node:crypto';const b='build-native/territorial-recipe/',r=b+'east-followup-final-2026-11-05/',read=p=>JSON.parse(fs.readFileSync(p)),sha=x=>createHash('sha256').update(x).digest('hex'),m=read(r+'final-metrics.json').rows,d=read(r+'downstream-audit.json'),v=read(r+'viewer-identity-check.json'),topo=read(r+'selected/topology-checks.json');
const table=m.map(x=>`|${x.feature}|${x.original_points}→${x.baseline764_points}→${x.final_points}|${x.selected_cap_m||'유지'}|${x.projected_764_vertex_to_corresponding_final_chord_max_m.toFixed(2)}|${x.projected_registered_vertex_to_corresponding_final_chord_max_m.toFixed(2)}|${x.detail_ratios.turn1km.toFixed(2)} / ${x.detail_ratios.turn5km.toFixed(2)}|`).join('\n');
let text=`# 동부 후속 표시 연구: 764→592점

로컬 provisional 연구 결과. 운영 source·활성 native 등록·pin·commit/push·원격 보고서 변경 없음. 이전764 및 Darja/강한후보/혼합본/READY는 보존했다. Space 최초 연구와 후속14파일은764 이전판이며 이번592 결과를 포함하지 않는다.

## 선택과 비교

보수 의미보호안은 East14 합계651 point entries, 간결한 국소 표시안은592다. 원래1059→이전908→764→592이며 공유 끝점이 포함된 합계이지 독립 정점 수가 아니다. 이번에는9구간을 변경하고 Sary44는35점을 유지했다. 이미 개선한18/20/23/25는38/38/58/33점 그대로다. 라트비아250m163점,폴란드250m+원래 프리피야트987–988 연결점671점도 그대로다. Atrek/Darja·Aral·68수역hole·먼해안·국가기간·한국롤백·Monaco·500km² 미만 사건 제거는 이번 동부 편집의 바깥에서 보존된다.

|feature|등록route→764→선택|국소 cap m|764→최종 정점/대응 chord 최대 m|등록route→최종 누적 정점/chord 최대 m|현대 대비1km/5km 굴곡비|
|---|---:|---:|---:|---:|---:|
${table}

cap은 두 번째 단계의 연구 파라미터다. 누적 편차가 cap보다 커질 수 있으며 f8은250m cap에 등록기준 누적256.43m다. f44의300.28m는 이번 변경0인 기존 보수안의 누적 차이다. 원래 route 정점부터 대응하는 최종 유한 chord까지의 정확한 local-AEQD 최대와 전체 polyline 양방향25/12.5m 표본 최대를 final-metrics.json에 각각 기록했다.12.5m 표본의 추가 상한 여유는6.25m이며 지표면 측량 정확도나 geodesic 인증이 아니다. 투영 정의와 이미 실행된 변환 근거는 trials.json에 있다.

각 구간에서125/250/375/500m 및 기존 같은 지역 현대 point-omission sagitta q25 후보를 비교했다. 검색 상한은 min(500m,2×해당 구간q25)라는 명시적 연구 휴리스틱이며 국가 공통 tolerance나 정책상 허용오차가 아니다. 원형 대비가 아니라764 입력 대비 길이97.5% 이상·5km 위상평균 굴곡 변화12% 이내의 보수 shape guard로 간결한 후보를 골랐다. guard 통과 자체는 의미 검토나 NE 동등성 승인이 아니다. 보수안은 넓은 불확실 범위/기술분류 경계/기존 계산macro까지 유지하고, 간결안은 실제 의미·수문/접촉·끝점을 같이 지키되 수문과 겹치지 않는 문자/빙설 범위의 양끝과 계산macro만 고정한다. 이전 shortcut·40도 lock을 새 의미점으로 승격하지 않았다.

## 보호 근거와 한계

- f2:route1–9,53–58,61–73 수문가능,40–43/48–52 고개·빙설 접촉의 현존764 점 보호. 넓은14–25/27–37 문자범위는 별도 처리.
- f4:직접 큰굽이11/25/26,수문/접촉13–23/43–49/53–59 및끝점 유지.
- f8:직접 큰굽이34/35,가능접촉5–14/15–22/28–32,headwater 우려24/37 및끝점 유지.
- f12:복구 hook12/cusp42와 upstream 실제원픽셀 거시 검토창109–124/89–94/52–76/33–43/14–26/5–13의 현존점을 보존. 이 창은 이번 provisional 연구용이며 기존 원mask를 대체하거나 창밖을 육상 안전으로 인증하지 않는다.
- f27:직접 기록된 큰굽이0/1/3/8/10/12,possible-water17 및끝점 유지. 현대3점 비교선은 거시 정치노선이 다르며 큰 굽이를 지워 수치만 맞추지 않는다.
- f35:문자·빙설 구간과 육상분류 경계를 분리. 수문 없음으로 새 인증하지 않는다. 직접 독립 단일명명점은 이번 감사에서 미확정.
- f37:실제 Chon-Uzengi 횡단/접근route39–42 중 현존39/42 유지.40/41은 과거 생략이며 이번에 되살리지 않았다.
- f39:직접 큰굽이2/10/16,인쇄P7-near19와 남쪽도곽0 유지. 인쇄접촉과 계산P7의21.09m 차이를 스냅으로 없애지 않는다.
- f44:두 양성 능선범위 외 넓은 source 보호의 point-specific 수문 대응을 추가 확정하지 못해35점 유지. 원도2장의 개요는 이 데스크톱에서 실제 봤으나 구간별 배수교차를 인증하지 않는다. 평균seam/분류경계는 측량의미점과 다르다.
- f48:07남향U 수문불확실route13–42 및08현존 불확실47–81을 유지. Baanur 문자구간은 별도 처리. 실제L45-08 서남부 crop에서 인쇄경계와 청색 수계/고개 표기가 근접하므로 정확한 교차 정점 대응 없이08 전체를 자유로운 능선으로 선언하지 않았다. 먼 원본165–175의 river interpolation은 사용clip밖이므로 적용하지 않는다. 기존 평균seam 이력과 원본은 보존한다.

새 좌표/스냅/커넥터/정점 재삽입은0이다. 새로 전달된 넓은 보호창에 속하지만764에 이미 없었던 점은 final-metrics.json categories.prior_omitted 및 hard_constraints_previously_absent에 기록했다. 이는 이번 신규 삭제와 분리한다. 단일 직접 의미앵커는 모두 남는다. 특히f2[41,49,51],f8[12],f12[20,26,56,64,90,92],f37[40,41] 등의 과거 생략은 보호범위 원점이 바뀌었다는 이유로 복원하지 않았다. f48 목록은 수문범위와 별도 미분류08범위를 분리하여 읽어야 한다.

모든14구간의 NE 목표 달성을 주장하지 않는다. f2/8은5km 거시 굴곡이 현대문맥에 근접하지만 보호범위 때문에1km에서는 더 복잡하다. f27은 현대3점 arc와 역사적 큰 굽이가 달라 굴곡비의 분모도 작다. f4/12/35/37/48의 보호구간·원도 불확실성과 역사노선 차이는 남는다. f44는 새 단순화 판단 보류다. 현대 참조195 point entry는 현재 CHN native와 arc 단위 exact 대조된 기존 model/compiled 문맥이며 순수 NE 독립 원본으로 단정하지 않는다.

## 실제 실행한 검증

- 새 공유사슬18치환(9구간×USSR/RSFSR),양 소유자에 같은 좌표subset 사용.
- source/compiled4whole geometry 모두유효,component/hole 유지,대상밖 좌표 순서 exact cyclic;source–compiled 변경영역 불일치0,두소유자 변경영역 불일치0. 구성국겹침 변화0,기존 외국상대 비교6건의 overlap/contact 변화0. topology-checks.json과 splice-proof.json 참조.
- 새 scratch raw/chunk/native6객체 exact,국가기간·모든 비편집 geometryversion 유지. 기존7버전의 passed receipt는 과거 증거로 보존하고 활성승인필드에서 빼 연구용 provisional record로만 구성했다. 누락4/오래된peer6을 허위승인으로 메우지 않았으며 새 연구용counterpart digest는 현재형상과 일치한다.
- 날짜 경계1922-12-29/30,1925-05-12/13를5국가에서20건 확인. 실제prepared 입력6국가(활성가족closure 포함)·조회1922-12/1925-06만 사용했다.
- prepared31개 중26재사용·신규5packet decode 통과. 기존 실험manifest427개entry를 보존하여 전체append manifest432개다. 물리land/water/manifest는 기존Darja 바이트와동일;추가 물리재생성 안 함. 실제33개필요mesh 중 과거실험잉여를 제외한Viewer용manifest는 생산402entry+현재신규12=414entry이다. 이는 별도 명시적preview입력이며 원래append manifest는 보존했다.
- raw–chunk 불일치4객체는 이 독립 scratch에서 해결됐다. pure canonical storage gate는 지금 'missing or unresolved review'로 거절하며7source버전은 미승인이다. 정상적인provisional차단이고 생산store 시도가 아니다.
- manifest의 이전Caspian source해시1항목은 append가보존한 과거기록이다. 이번 국가owner는5국가source만읽고 물리owner는별도land/water asset을읽는다. 이 과거항목을 현재실행 입력이라고 표기하지 않았다. 실제물리입력은 해시동일하고 sourceCaspian은raw/chunk/native로별도검증됐다. 전체manifest의모든과거inputHashes가새source와일치한다고주장하지않는다.
- 최신local06e4466f9(원격c85bce17a 포함)에서 실제Viewer1922-12,WebGL2,114국가,USSR/RSFSR 최종digest2/2존재,오류${v.errors.length}·경고${v.warnings.length}. 실제화면과동일AEQD범위 그림2장을직접열어봤다. 거시윤곽/레이어연계 확인이며 고배율 모든 접점·원도 의미의 인증이 아니다.

## 실패·해결·미실행

최초preview는 실험append manifest가가리키는 불필요한이전packet이없어시작하지못했다. 생산기준+현재33개로범위를명시한preview manifest를만들었으나,첫실행은build identity가작은manifest를해시하고서버는원래큰파일을보내size검사에실패했다. instrumented실패와최종화면은보존했다. 새scratch script에서정확히같은바이트를metadata와응답에연결한뒤 실제1922전환을통과했다. 앱코드는수정하지않았다.

보수651안은trial/수치비교까지 실행했으며 source/compiled/prepared/Viewer 전체검증은선택592안에만 실행했다. Sary의 미분류범위 안전해제,모든구간의역사·법적정확도,전세계GIS/전체테스트,운영반영은미실행이다. 과거원도·master를새로재구축하지않았다.

이전거절prepared 코드2파일(tools/build-prepared-polygon-mesh.mjs,tests/unit/prepared-polygon-country-scope.test.mjs)의remote commit/push는재시도하지않았다. splice2파일(tools/build-korean-boundaries.mjs,tests/unit/shared-boundary-splice.test.mjs)의git push origin HEAD:work/gis도재시도하지않았다. 원격보고서편집/게시는계속금지다. 이번에는새권한거절을발생시키는원격동작을요청하지않았다. 기존runner 수정거절을우회하지않고새scratch스크립트만만들었다.

## 재현 경로와 실제 실행 순서

cwd D:/dev/worktrees/gis. b=build-native/territorial-recipe. 이전764/Darja/불변입력은그대로참조한다. 새runner는이기록과해시로고정됐다. 출력루트가이미있으면생성기는보존을위해실패하므로동일경로를지우거나덮어써재실행하지말고새scratch경로로복사하여O/r/o출력상수만바꾼다. 원본등록route와입력좌표/해시를바꾸지않는다.

1. 기존OSGeo4W Python312 환경으로 historical-detail-east-followup-final-trials.py 실행.
2. node historical-detail-east-followup-final-compose.mjs; node historical-detail-east-followup-final-plot.mjs.
3. 기존OSGeoPython으로 historical-detail-east-followup-check.py.
4. node east-followup-final-2026-11-05/prepare-consistent-research.mjs 250.
5. node historical-detail-east-followup-audit-scoped-inputs.mjs.
6. 기존OSGeoPython으로 historical-detail-east-followup-metrics.py; node historical-detail-east-followup-finalize.mjs.
7. node historical-detail-east-followup-identity-viewer.mjs.
8. node historical-detail-east-followup-report.mjs.

모든상대파일은b아래다. 250은prepared case key이며동부공통 tolerance가아니다. 기존OSGeo의PYTHONHOME=D:/dev/tools/osgeo4w/apps/Python312,process-localPATH=D:/dev/tools/osgeo4w/bin+기존PATH를썼다. 설치·C++재빌드·새SDK·portable패키지는없다. 실제사용한code/input/outputSHA는checksums.json에있다. stage별topology/downstream/Viewer JSON은구분하여유지한다.

## 공개원도와 출처 범위

다음공개원도3개는정상HTTP읽기로한번수신했고기록SHA와일치했다. Library Windows오류재시도/비공식전송이아니다. 보존위치 ../east-followup-classified-2026-11-05/maps/.
- [L44-28](https://maps.vlasenko.net/smtm200/l-44-28.jpg):a0cd8fbb1e0deaaa2f4e61d487ea3cb76f9a9c79c72355d1e5e62c47eff714d0
- [L44-29](https://maps.vlasenko.net/smtm200/l-44-29.jpg):3f65c2d7f7f491a411065980b260d02dd0c7783ee95600ce37bb80a889676abd
- [L45-08](https://maps.vlasenko.net/smtm200/l-45-08.jpg):ef8ab8757bffd02b1d164c2da78ed2ed98a38dc32443aca3dbe08bc1f50055d3

그외새Pamir/W03 mask/member/좌표대응은부모의공식Library 원자료감사에서전달된증거다. 그원도를이desktop에서새로전부봤다고하지않는다. preserved-trials 초기/분류갱신/f12갱신본은같은새근거가어떻게선택에반영됐는지비교하는현재소비자가있어보존하며운영자료가아니다.

남은허용행동은이로컬근거의검토와제한된미해결의미판단이다. 채택승인없이review를passed로만들거나생산등록·pin·push·원격보고서게시를하지않는다. canonical report 원격보관완료가아닌로컬결과다.
`;
fs.writeFileSync(r+'README.md',text);
const code=['historical-detail-east-followup-final-trials.py','historical-detail-east-followup-final-compose.mjs','historical-detail-east-followup-final-plot.mjs','historical-detail-east-followup-check.py','historical-detail-east-followup-audit-scoped-inputs.mjs','historical-detail-east-followup-metrics.py','historical-detail-east-followup-finalize.mjs','historical-detail-east-followup-identity-viewer.mjs','historical-detail-east-followup-report.mjs'].map(f=>b+f),inputs=['historical-detail-line-2.geojson','historical-detail-east-candidate.json','historical-detail-final-metric-input.json','historical-detail-west-whole-view.json','historical-detail-eastern-comparator-chains.json'].map(f=>b+f),owner=['tools/build-korean-boundaries.mjs','tools/build-prepared-polygon-mesh.mjs','tools/gis/historical-display-review.mjs','tools/gis/historical-display-storage.mjs'];let outputs=[];function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){assertSafe(e);const f=path.join(dir,e.name);if(e.isDirectory())walk(f);else if(e.name!=='checksums.json')outputs.push(f);}}function assertSafe(e){if(e.isSymbolicLink())throw Error('Do not traverse linked scratch output');}walk(r);const describe=p=>({path:p.replaceAll('\\','/'),bytes:fs.statSync(p).size,sha256:sha(fs.readFileSync(p))});const checks={status:'local research only',createdAt:new Date().toISOString(),code:[...code,r+'prepare-consistent-research.mjs'].map(describe),canonicalOwners:owner.map(describe),immutableInputs:inputs.map(describe),outputs:outputs.map(describe)};fs.writeFileSync(r+'checksums.json',JSON.stringify(checks,null,2)+'\n');console.log(JSON.stringify({reportSha256:sha(fs.readFileSync(r+'README.md')),checksumsSha256:sha(fs.readFileSync(r+'checksums.json')),outputFiles:outputs.length,logicalBytes:outputs.reduce((n,p)=>n+fs.statSync(p).size,0),viewer:v.status,finalEast:592,conservativeEast:651}));