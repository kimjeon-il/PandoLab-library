import ast, json, pathlib

source = pathlib.Path('tools/calibrate-hydro.py')
tree = ast.parse(source.read_text(encoding='utf-8'))
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in ('format_percent', 'write_report')]
module = ast.Module(body=[ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0), *functions], type_ignores=[])
ast.fix_missing_locations(module)
scope = {'STAGES': (6.0, 6.7, 7.0, 7.5)}
exec(compile(module, str(source), 'exec'), scope)

class Sink:
    def write_text(self, text, encoding):
        assert encoding == 'utf-8'
        self.value = text

stages = ['6.0', '6.7', '7.0', '7.5']
river = {stage: {'selectedCount': 1234 + index, 'lengthRatio': None if index == 0 else 1.2345,
                 'pixelRatio': 0.125} for index, stage in enumerate(stages)}
lake = {stage: {'selectedCount': 56 + index, 'countRatio': 0.875, 'pixelAreaRatio': None if index == 1 else 1.125}
        for index, stage in enumerate(stages)}
results = {
    'acceptance': {'density': True, 'network': True},
    'regions': {'korea': {'label': '한반도', 'rivers': river, 'lakes': lake,
                          'riverBaseOverlapRatio': 0.0125, 'lakeBaseOverlapRatio': 0.005}},
    'formula': {'rivers': {'flowWeight': 1.3, 'upstreamAreaWeight': -0.7,
                           'thresholds': dict(zip(stages, [14.4744, 12.4307, 11.2137, 10.55]))},
                'lakes': {'areaWeight': 1.25, 'shorelineWeight': 0.5,
                          'thresholds': dict(zip(stages, [3.0, 2.5, 2.0, 1.5]))}},
    'worldEstimate': {'riverChaining': {'selectedReachCount': 10000, 'chainCount': 5000,
                                       'objectReductionPercent': 50.0, 'sourceCoordinateCount': 100000,
                                       'coordinatesAfterChaining': 100000},
                      'riverReachCount': 12345, 'riverChainCount': 6789, 'riverCoordinateCount': 98765,
                      'lakeFeatureCount': 1355, 'gzipMiB': 12.25,
                      'riverRenderLoadRatio': 1.25, 'lakeRenderLoadRatio': 0.75},
    'representativeChecks': {'압록강': {'present': True}, '미확인': {'present': None}, '누락': {'present': False}},
}
cases = []
for accepted in (True, False):
    results['acceptance']['network'] = accepted
    sink = Sink()
    scope['write_report'](results, sink)
    cases.append({'input': json.loads(json.dumps(results, ensure_ascii=False)),
                  'expectedPrefix': sink.value.split('## 재현 방법', 1)[0]})
print(json.dumps(cases, ensure_ascii=False, indent=2))
