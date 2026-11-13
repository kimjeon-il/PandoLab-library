import importlib.util,json,pathlib,sys
root=pathlib.Path('build-native/terrain-preview/physical-hydro-oracle-20261031');root.mkdir(exist_ok=False)
source=root/'source';source.mkdir();expected=root/'python-output'
spec=importlib.util.spec_from_file_location('physical',pathlib.Path('tools/build-physical-data.py'))
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
import shapefile
for layer,category,stem in module.HYDRO_SOURCES:
    w=shapefile.Writer(str(source/stem),shapeType=shapefile.POLYLINE if category=='river' else shapefile.POLYGON)
    w.field('ne_id','N',9,0);w.field('name','C',30);w.field('scalerank','N',3,0);w.field('min_zoom','N',5,1);w.field('strokeweig','N',5,1)
    if category=='river':w.line([[[0,0],[1.125,2.25],[3,4]]])
    else:w.poly([[[0,0],[0,2],[3,2],[3,0],[0,0]]])
    w.record(101,'Fixture',2,3.5,1.2)
    w.null();w.record(102,'Null',3,4,1.1)
    if category=='river':w.line([[[5,6],[7,8]]])
    else:w.poly([[[5,6],[5,8],[7,8],[7,6],[5,6]]])
    w.record(0,'No id',4,4,1)
    w.close()
manifest=module.build_hydro(source,expected)
print(json.dumps({'layers':len(manifest['layers']),'first':manifest['layers'][0]}))
