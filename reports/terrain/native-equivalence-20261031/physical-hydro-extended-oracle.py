import json,pathlib,subprocess
root=pathlib.Path('build-native/terrain-preview/physical-hydro-oracle-extended-20261031');root.mkdir(exist_ok=False)
source=root/'source';source.mkdir();expected=root/'python-output'
src=subprocess.check_output(['git','show','HEAD:tools/build-physical-data.py']).decode('utf8')
namespace={'__name__':'physical_oracle','__file__':'tools/build-physical-data.py'};exec(compile(src,'physical_oracle','exec'),namespace)
import shapefile
for layer,category,stem in namespace['HYDRO_SOURCES']:
    w=shapefile.Writer(str(source/stem),shapeType=shapefile.POLYLINE if category=='river' else shapefile.POLYGON,encoding='utf8')
    w.field('ne_id','N',9,0);w.field('name','C',60);w.field('scalerank','N',3,0);w.field('min_zoom','N',5,1);w.field('strokeweig','N',5,1)
    if category=='river':w.line([[[0,0],[1.125,2.25],[3,4]],[[5,6],[7,8]]])
    else:w.poly([[[0,0],[0,4],[5,4],[5,0],[0,0]],[[1,1],[2,1],[2,2],[1,2],[1,1]],[[7,0],[7,2],[9,2],[9,0],[7,0]]])
    w.record(101,'한강 Fixture',2,3.5,1.2)
    w.null();w.record(0,'Null',0,0,0)
    if category=='river':w.line([[[4,4],[5,5]]])
    else:w.poly([[[10,0],[10,2],[12,2],[12,0],[10,0]]])
    w.record(0,'fallback',None,None,None);w.close()
manifest=namespace['build_hydro'](source,expected);print(json.dumps({'layers':len(manifest['layers'])}))
