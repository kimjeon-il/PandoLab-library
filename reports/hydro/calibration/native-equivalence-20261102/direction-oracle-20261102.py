import ast, json, math, pathlib, types

source = pathlib.Path('tools/calibrate-hydro.py')
tree = ast.parse(source.read_text(encoding='utf-8'))
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in ('line_direction', 'direction_similarity')]
module = ast.Module(body=[ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0), *functions], type_ignores=[])
ast.fix_missing_locations(module)
scope = {'math': math}
exec(compile(module, str(source), 'exec'), scope)
lines = [[], [[0, 0]], [[0, 0], [0, 0]], [[0, 0], [1, 0]], [[0, 0], [-3, 0]],
         [[0, 0], [0, 5]], [[0, 0], [3, 4]], [[0, 0], [0, 5], [5, 5]],
         [[1e-8, 2e-8], [2e-8, 4e-8]], [[0, 0], [3, 4], [-3, -4]]]
cases=[]
for left in lines:
    for right in lines:
        a, b = types.SimpleNamespace(coords=left), types.SimpleNamespace(coords=right)
        cases.append({'left': left, 'right': right, 'expected': scope['direction_similarity'](a, b)})
print(json.dumps(cases, ensure_ascii=False, indent=2))
