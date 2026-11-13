import {execFileSync} from 'node:child_process';
import {writeFileSync} from 'node:fs';
const python=`import importlib.util,json,sys
sys.stdout.reconfigure(encoding='utf-8')
spec=importlib.util.spec_from_file_location('source','tools/gis/verify_osm_hydro_batch02_points.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(json.dumps(dict(ids=module.IDS,crs=module.CRS,static=module.STATIC,ngaTargets=module.NGA_TARGETS,ngaUrl=module.NGA),ensure_ascii=False,indent=2))
`;
const result=execFileSync('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',['-c',python],{encoding:'utf8',maxBuffer:4*1024*1024});
const data=JSON.parse(result);
if(data.ids.length!==10||Object.keys(data.ngaTargets).length!==4)throw Error('Unexpected original station evidence');
writeFileSync('tools/gis/hydro-osm-batch02-anchors.mjs',
  '// Independent named observations retained from the second-ten Hydro audit.\n'+
  '// Facility and ecological area points are not centerline measurements or naming approval.\n'+
  'export const batch02Anchors='+JSON.stringify(data,null,2)+';\n',{flag:'wx'});
console.log(JSON.stringify({systems:data.ids.length,staticSystems:Object.keys(data.static).length}));
