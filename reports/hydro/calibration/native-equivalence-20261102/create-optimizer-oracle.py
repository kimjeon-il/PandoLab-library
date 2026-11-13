import ast, bisect, json, math, pathlib, random, statistics, subprocess, types

source = pathlib.Path('tools/calibrate-hydro.py')
tree = ast.parse(subprocess.check_output(['git','show','3cc20b32:tools/calibrate-hydro.py'],encoding='utf-8'))
names = {'ratio', 'log_error', 'candidate_thresholds', 'optimize_thresholds', 'assign_stages'}
body = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
for classname in ('LinearFeature','AreaFeature'):
    cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==classname)
    fn=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='score')
    fn.name=classname+'_score';body.append(fn)
module = ast.Module(body=[ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0), *body], type_ignores=[])
ast.fix_missing_locations(module)
stages = [6.0, 6.7, 7.0, 7.5]
scope = {'math': math, 'bisect': bisect, 'statistics': statistics, 'STAGES': stages}
exec(compile(module, str(source), 'exec'), scope)
rng = random.Random(20261102)

def region(count, kind, zero=False, tied=False):
    features=[]
    for i in range(count):
        features.append(dict(order=(i%7)+1, first=10 if tied else rng.choice([0, .000001, .3, 1, 10, 77.3, 1200]),
                             second=10 if tied else rng.choice([0, .000001, .2, 1, 10, 135.7, 1400]),
                             metricFirst=round(rng.uniform(.5, 40),4), metricSecond=round(rng.uniform(.5,20),4)))
    targets=[dict(first=(0 if zero else 5 + i*31), second=(0 if zero else 3 + i*13)) for i in range(4)]
    baselines=[dict(first=0 if zero else i*.2, second=0 if zero else i*.1) for i in range(4)]
    return dict(features=features, targets=targets, baselines=baselines)

requests=[]
for kind in ('river','lake'):
    weights=[[1,0],[1.3,.7],[2.5,-.5],[4,-2]]
    for label,regions in [('ordinary',[region(19,kind),region(12,kind)]),('ties',[region(12,kind,tied=True)]),
                          ('zero-target',[region(7,kind,zero=True)]),('empty',[region(0,kind)]),('no-regions',[]),
                          ('quantile-ties',[region(111,kind),region(0,kind)])]:
        request=dict(kind=kind,stages=stages,regions=regions,weights=weights)
        best=None
        for pair in weights:
            scored={};targets={};baselines={}
            for i,r in enumerate(regions):
                scored[str(i)]=[]
                for f in r['features']:
                    score=(f['order'] if kind=='river' else 0)+pair[0]*math.log10(max(f['first'],1e-6))+pair[1]*math.log10(max(f['second'],1e-6))
                    scored[str(i)].append((score,types.SimpleNamespace(length_km=f['metricFirst'],screen_length=f['metricSecond'],screen_area=f['metricFirst'])))
                def metrics(values):
                    return {s:types.SimpleNamespace(length_km=v['first'],screen_length=v['second'],screen_area=v['first'],count=v['second']) for s,v in zip(stages,values)}
                targets[str(i)]=metrics(r['targets']);baselines[str(i)]=metrics(r['baselines'])
            thresholds,objective=scope['optimize_thresholds'](scored,targets,baselines,kind)
            if best is None or objective<best[0]:best=(objective,pair,thresholds)
        objective,pair,thresholds=best
        stage_values=[thresholds[s] for s in stages] if thresholds else []
        assignment=None
        if thresholds:
            rows=[];objects=[]
            for f in [f for r in regions for f in r['features']]:
                item=types.SimpleNamespace(order=f['order'],flow=f['first'],upstream_area=f['second'],area_km2=f['first'],shoreline_km=f['second'],duplicate=False,assigned_stage=99)
                item.score=types.MethodType(scope['LinearFeature_score' if kind=='river' else 'AreaFeature_score'],item)
                objects.append(item);rows.append(dict(duplicate=False,order=f['order'],first=f['first'],second=f['second']))
            if objects:
                duplicate=types.SimpleNamespace(duplicate=True,assigned_stage=99);objects.append(duplicate);rows.append(dict(duplicate=True))
            scope['assign_stages'](objects,tuple(pair),thresholds)
            assignment=dict(request=dict(kind=kind,stages=stages,weights=pair,thresholds=stage_values,features=rows),expected=[o.assigned_stage for o in objects])
        requests.append(dict(name=kind+'-'+label,request=request,expected=dict(weights=pair,thresholds=stage_values,objective=objective if math.isfinite(objective) else None),assignment=assignment))
path=pathlib.Path('tests/fixtures/hydro-calibration-optimizer-oracle.json')
path.write_text('[\n'+',\n'.join(json.dumps(row,ensure_ascii=False,separators=(',',':')) for row in requests)+'\n]\n',encoding='utf-8')
print('Frozen original optimizer cases:',len(requests))
