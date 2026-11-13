import {execFileSync} from 'node:child_process';
import {writeFileSync} from 'node:fs';
const python=`import importlib.util,json
spec=importlib.util.spec_from_file_location('source','tools/gis/verify_osm_hydro_batch01_anchors.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(json.dumps(dict(batch=module.BATCH,points=module.POINTS,groups=module.GROUPS,crs=module.CRS),ensure_ascii=False,indent=2))
`;
const result=execFileSync('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',['-c',python],{encoding:'utf8',maxBuffer:4*1024*1024});
const data=JSON.parse(result);
if(data.batch.length!==10||Object.keys(data.points).length<30)throw Error('Unexpected original station evidence');
writeFileSync('tools/gis/hydro-osm-batch01-anchors.mjs',
  '// Transcribed independent named-station references retained from the first-ten Hydro audit.\n'+
  '// The Manda point remains explicitly disputed; proximity is not river-name approval.\n'+
  'export const batch01Anchors='+JSON.stringify(data,null,2)+';\n',{flag:'wx'});
console.log(JSON.stringify({systems:data.batch.length,points:Object.keys(data.points).length}));
