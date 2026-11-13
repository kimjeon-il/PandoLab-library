import {execFileSync} from 'node:child_process';
import {writeFileSync} from 'node:fs';
const python=`import importlib.util,json,sys
sys.stdout.reconfigure(encoding='utf-8')
spec=importlib.util.spec_from_file_location('source','tools/gis/verify_osm_hydro_batch03_points.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(json.dumps(dict(ids=module.IDS,bbox=module.BBOX,crs=module.CRS,queryTerms=module.QUERY_TERMS,external=module.EXTERNAL,placeZones=module.PLACE_ZONES,gns=module.GNS,gnsAbout=module.GNS_ABOUT),ensure_ascii=False,indent=2))
`;
const result=execFileSync('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',['-c',python],{encoding:'utf8',maxBuffer:4*1024*1024});
const data=JSON.parse(result);
if(data.ids.length!==11||Object.keys(data.placeZones).length!==2)throw Error('Unexpected original station evidence');
writeFileSync('tools/gis/hydro-osm-batch03-anchors.mjs',
  '// Independent government endpoint and named-stream references for the last eleven Hydro systems.\n'+
  '// Named points and a roof-mounted rain gauge do not establish river identity.\n'+
  'export const batch03Anchors='+JSON.stringify(data,null,2)+';\n',{flag:'wx'});
console.log(JSON.stringify({systems:data.ids.length,referenceGroups:Object.keys(data.external).length}));
