import json,pathlib,sqlite3,hashlib
p=pathlib.Path(__file__).parent;c=sqlite3.connect('file:D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109/c-raw-versus-prepared-audit/official-original-preserved/WorldPolygons11_4.gpkg?mode=ro&immutable=1',uri=True);c.row_factory=sqlite3.Row
out=[]
for code in ['MMR','CHN','IND','BGD','LAO','VNM']:
 rows=c.execute('select * from DoS_WP_11_4 where GENC_3=?',(code,)).fetchall();out.append({'code':code,'rows':[{k:r[k] for k in r.keys() if k!='geom'} for r in rows]})
(p/'raw-feature-attribution.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
