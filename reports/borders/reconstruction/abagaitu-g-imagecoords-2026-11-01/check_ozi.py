from pathlib import Path
import json, csv, numpy as np
from pyproj import Proj
p=Path(__file__).parent
# Read preserved metadata only; no source map or new extraction.
record=json.loads((p/'ozi-registration-consistency.json').read_text())
pts=[{'id':v['id'],'pixel':v['pixel'],'lon':v['lon'],'lat':v['lat']} for v in record['controls']]
projection=Proj('+proj=tmerc +lat_0=0 +lon_0=117 +k=1 +x_0=500000 +y_0=0 +ellps=krass +units=m')
xy=np.array([a['pixel'] for a in pts]); world=np.array([projection(a['lon'],a['lat']) for a in pts]); fit=[0,2,3,5,6,8]; held=[1,4,7]
A=np.column_stack([xy,np.ones(len(xy))]); matrix=np.linalg.lstsq(A[fit],world[fit],rcond=None)[0]; pred=A@matrix
inv=np.linalg.inv(matrix[:2,:]); res=(pred-world)@inv
for i,a in enumerate(pts): a.update({'projected_krass_m':world[i].tolist(),'role':'metadata_holdout' if i in held else 'metadata_fit','residual_px':float(np.linalg.norm(res[i])),'residual_m':float(np.linalg.norm(pred[i]-world[i]))})
r={'purpose':'Ozi registration metadata consistency only; NOT Toolkit job/export; NOT independent survey validation','datum_transform_to_WGS84':None,'fit_ids':[pts[i]['id'] for i in fit],'holdout_ids':[pts[i]['id'] for i in held],'matrix_pixel_to_krass_projection':matrix.tolist(),'holdout_max_px':float(np.linalg.norm(res[held],axis=1).max()),'holdout_p95_px':float(np.percentile(np.linalg.norm(res[held],axis=1),95)),'controls':pts,'historical_boundary_extracted':False}
(p/'ozi-registration-consistency-recomputed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));print(json.dumps(r,ensure_ascii=False,indent=2))
