import gzip, json
from pathlib import Path
manifest = json.loads(Path('assets/data/hydro/v0.13.2/manifest.json').read_text(encoding='utf-8'))
spec = manifest['metadata']['core']
with Path('assets/data/hydro/v0.13.2/hydro.bin').open('rb') as stream:
    stream.seek(spec['offset'])
    core = json.loads(gzip.decompress(stream.read(spec['bytes'])))
delivery = {**core, 'features': [{key: value for key, value in row.items()
            if key not in {'systemId', 'mainstemNameKo', 'role'}} for row in core['features']]}
raw = json.dumps(delivery, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
Path('build-native/hydro-calibration/core-delivery-python-20261102.json').write_bytes(raw)
print(len(raw), len(gzip.compress(raw)))
