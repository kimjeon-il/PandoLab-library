import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {pathToFileURL} from 'node:url';
import {resolve} from 'node:path';
const {probeNgaBatch03}=await import(pathToFileURL(resolve('tools/gis/probe-nga-streams.mjs')));
const payload={exceededTransferLimit:true,features:[
  {attributes:{desig_cd:'STM',ufi:123,long_dd:107,lat_dd:11,full_name:'Đồng Nai',cc_ft:'VM'}},
  {attributes:{desig_cd:'STM',ufi:123,long_dd:107,lat_dd:11,full_name:'Dong Nai',cc_ft:'VM'}}]};
const raw=JSON.stringify(payload),source=`import importlib.util,sys,json,io
sys.stdout.reconfigure(encoding='utf-8')
s=importlib.util.spec_from_file_location('original','tools/gis/verify_osm_hydro_batch03_points.py')
m=importlib.util.module_from_spec(s)
s.loader.exec_module(m)
data=sys.stdin.buffer.read()
m.urllib.request.urlopen=lambda request,timeout:io.BytesIO(data)
q=[(sid,False) for sid in m.IDS]+[(sid,True) for sid in ('41386179','41386700')]
print(json.dumps([m.search_geonames(*pair) for pair in q],ensure_ascii=False))
`;
const previous=JSON.parse(execFileSync('D:/dev/worktrees/ui/build-native/python/Scripts/python.exe',['-c',source],{input:raw,encoding:'utf8',maxBuffer:4*1024*1024}));
const current=await probeNgaBatch03({fetcher:async()=>new Response(raw,{status:200})});
assert.deepEqual(current,previous);console.log(JSON.stringify({queries:current.length,featureCount:current.reduce((sum,row)=>sum+row.features.length,0)}));
