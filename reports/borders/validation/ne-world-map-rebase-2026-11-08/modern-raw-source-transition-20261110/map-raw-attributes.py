import json,sqlite3,pathlib
p=pathlib.Path(__file__).parent
raw=p.parent/'historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg'
c=sqlite3.connect(raw.as_uri()+'?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
features=[dict(r) for r in c.execute('select WP_ID,WP_Name,GENC_3,WP_PAR_ID,US_Recog,Show_Disp,Map_Disp from DoS_WP_11_4')]; c.close()
x=json.loads((p/'current-raw-feature-mapping.json').read_text());byid={r['WP_ID']:r for r in features}
for r in x['rows']:
 ids=r['rawFeatureIds'];code=r['entityId'].split(':')[1]
 match=[byid[i] for i in ids if i in byid] if ids else [v for v in features if v['GENC_3']==code]
 r['rawCandidates']=match;r['mappingMethod']='recorded-WP_ID' if ids else 'GENC_3-candidate-only';r['mappingStatus']='missing-recorded-raw-id' if ids and len(match)!=len(ids) else ('one-to-one-candidate' if len(match)==1 else 'needs-special-scope-review')
x['rawFeatureCount']=len(features); x['summary']={s:sum(r['mappingStatus']==s for r in x['rows']) for s in set(r['mappingStatus'] for r in x['rows'])}
(p/'raw-attribute-mapping.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'summary':x['summary'],'rawFeatures':len(features),'notOneToOne':[{ 'entity':r['entityId'],'rawCandidates':len(r['rawCandidates'])} for r in x['rows'] if r['mappingStatus']!='one-to-one-candidate']}))
