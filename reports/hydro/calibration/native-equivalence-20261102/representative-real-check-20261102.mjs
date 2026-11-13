import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {spawnSync} from 'node:child_process';
import {calibrationRepresentativeChecks} from '../../tools/gis/hydro-calibration-metrics.mjs';

const select=(path,tokens)=>JSON.parse(readFileSync(path,'utf8')).features.filter(feature=>{
  const names=['name_en','name_original','name'].map(key=>String(feature.properties?.[key]??'')).join(' ').toLowerCase();
  return tokens.some(token=>names.includes(token));
}).map(feature=>({properties:feature.properties}));
const input={rivers:select('assets/data/hydro/rivers_base.geojson',['nile','danube','mississippi','murray']),
  lakes:select('assets/data/hydro/lakes_base.geojson',['superior','michigan','huron','erie','ontario'])};
const script=String.raw`
import ast,json,pathlib,sys
source=pathlib.Path('tools/calibrate-hydro.py');tree=ast.parse(source.read_text(encoding='utf-8'))
func=next(node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=='representative_checks')
module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),func],type_ignores=[])
ast.fix_missing_locations(module);data=json.load(sys.stdin)
scope={'read_geojson':lambda path:data['rivers' if path.name.startswith('rivers') else 'lakes']}
exec(compile(module,str(source),'exec'),scope)
print(json.dumps(scope['representative_checks'](pathlib.Path('unused')),ensure_ascii=False))
`;
const run=spawnSync('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',['-X','utf8','-B','-c',script],
  {input:JSON.stringify(input),encoding:'utf8',windowsHide:true,timeout:30000});
assert.equal(run.status,0,run.stderr);const actual=calibrationRepresentativeChecks(input);assert.deepEqual(actual,JSON.parse(run.stdout));
console.log(JSON.stringify({selectedRivers:input.rivers.length,selectedLakes:input.lakes.length,
  present:Object.fromEntries(Object.entries(actual).map(([name,value])=>[name,value.present]))}));
