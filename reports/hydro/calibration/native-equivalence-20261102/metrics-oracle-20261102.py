import ast, json, pathlib, subprocess, types

path = pathlib.Path('tools/calibrate-hydro.py')
tree = ast.parse(path.read_text(encoding='utf-8'))
names = {'report_ratio', 'selected_at', 'stage_metrics', 'residual_overlap', 'acceptance', 'estimate_world', 'chain_rivers', 'run_calibration_native', 'representative_checks'}
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
module = ast.Module(body=[ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0), *functions], type_ignores=[])
ast.fix_missing_locations(module)
stages = [6.0, 6.7, 7.0, 7.5]
scope = {'STAGES': stages, '__file__': str(path.resolve()), 'Path': pathlib.Path, 'json': json, 'subprocess': subprocess}
exec(compile(module, str(path), 'exec'), scope)

source = {
    'rivers': [{'assignedStage': 6.0, 'lengthKm': 10.12345, 'screenLength': 3.5, 'duplicateFraction': 0.1},
               {'assignedStage': 7.0, 'lengthKm': 2.4, 'screenLength': 1.25, 'duplicateFraction': 0.5},
               {'assignedStage': None, 'lengthKm': 5.0, 'screenLength': 7.0, 'duplicateFraction': 0.9}],
    'lakes': [{'assignedStage': 6.7, 'screenArea': 2.5, 'duplicateFraction': 0.2},
              {'assignedStage': 7.5, 'screenArea': 7.5, 'duplicateFraction': 0.4}],
    'riverTargets': {}, 'riverBaselines': {}, 'lakeTargets': {}, 'lakeBaselines': {},
}
for index, stage in enumerate(stages):
    key = str(stage)
    source['riverTargets'][key] = {'count': 10 + index, 'lengthKm': 20.0, 'screenLength': 10.0}
    source['riverBaselines'][key] = {'count': index, 'lengthKm': 5.0, 'screenLength': 2.0}
    source['lakeTargets'][key] = {'count': 4 + index, 'screenArea': 12.0}
    source['lakeBaselines'][key] = {'count': index, 'screenArea': 1.0}

def fields(value):
    return types.SimpleNamespace(**{''.join('_' + c.lower() if c.isupper() else c for c in key): val for key, val in value.items()})
data = types.SimpleNamespace(
    rivers=[fields(row) for row in source['rivers']], lakes=[fields(row) for row in source['lakes']],
    river_targets={float(key): fields(value) for key, value in source['riverTargets'].items()},
    river_baselines={float(key): fields(value) for key, value in source['riverBaselines'].items()},
    lake_targets={float(key): fields(value) for key, value in source['lakeTargets'].items()},
    lake_baselines={float(key): fields(value) for key, value in source['lakeBaselines'].items()},
)
metrics = {'river': scope['stage_metrics'](data, 'river'), 'lake': scope['stage_metrics'](data, 'lake'),
           'riverOverlap': scope['residual_overlap'](data.rivers, 'river'), 'lakeOverlap': scope['residual_overlap'](data.lakes, 'lake')}
acceptance_input = {'regions': {'europe': {'rivers': metrics['river'], 'lakes': metrics['lake'],
                                            'riverBaseOverlapRatio': metrics['riverOverlap'], 'lakeBaseOverlapRatio': metrics['lakeOverlap']}},
                    'representativeChecks': {'present': {'present': True}, 'unreviewed': {'present': None}}}
world_input = [
    {'region': {'id': 'europe', 'calibrate': True},
     'rivers': [{'sourceId': 1, 'nextDown': 2, 'assignedStage': 6.0, 'sourceCoordinateCount': 10},
                {'sourceId': 2, 'nextDown': 0, 'assignedStage': 6.0, 'sourceCoordinateCount': 12},
                {'sourceId': 3, 'nextDown': 2, 'assignedStage': None, 'sourceCoordinateCount': 5}],
     'lakes': [{'assignedStage': 6.7, 'sourceCoordinateCount': 20},
               {'assignedStage': None, 'sourceCoordinateCount': 30}]},
    {'region': {'id': 'korea', 'calibrate': False},
     'rivers': [{'sourceId': 4, 'nextDown': 0, 'assignedStage': 6.0, 'sourceCoordinateCount': 50}], 'lakes': []},
]
world_data = [types.SimpleNamespace(region=fields(row['region']), rivers=[fields(item) for item in row['rivers']],
                                    lakes=[fields(item) for item in row['lakes']]) for row in world_input]
representative_input = {'rivers': [{'properties': {'name_en': 'Nile River'}}, {'properties': {'name_original': 'DANUBE'}},
                                   {'properties': {'name': 'Murray'}}],
                        'lakes': [{'properties': {'name_en': name}} for name in ('Superior', 'Michigan', 'Huron', 'Erie', 'Ontario')]}
scope['read_geojson'] = lambda value: representative_input['rivers' if value.name.startswith('rivers') else 'lakes']
print(json.dumps({'input': source, 'metrics': metrics, 'acceptanceInput': acceptance_input,
                  'acceptance': scope['acceptance'](acceptance_input), 'worldInput': world_input,
                  'worldExpected': scope['estimate_world'](world_data), 'representativeInput': representative_input,
                  'representativeExpected': scope['representative_checks'](pathlib.Path('unused'))}, ensure_ascii=False, indent=2))
