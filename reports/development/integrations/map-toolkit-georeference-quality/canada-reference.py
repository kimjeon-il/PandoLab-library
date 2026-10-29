"""Source-specific evaluation oracle, not a product GeoPDF reader.

Run from the Pando work/ui checkout. The fixed hash and exact viewport values
bind this diagnostic to the reviewed NRCan sheet; no PDF text is executed.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np
import pymupdf
import pyproj

sys.path.insert(0, str(Path.cwd() / 'tools'))
from report_paths import report_path

source = report_path('reports/map-analysis/corpus/macro-political/sources/nrcan-canada-monochrome.pdf', access='read')
sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
assert sha256 == '358cfad7e8329f019c820bc0b9e83b482e721eb09ebf6106d2e1580623f0b1b4'
with pymupdf.open(source) as document:
    viewport = document.xref_get_key(document[0].xref, 'VP')[1]
    assert '/BBox[0 0 792 612]' in viewport
    geographic = np.array([float(v) for v in re.search(r'/GPTS\[([^]]+)\]', viewport)[1].split()]).reshape(-1, 2)
    local = np.array([float(v) for v in re.search(r'/LPTS\[([^]]+)\]', viewport)[1].split()]).reshape(-1, 2)
    wkt = re.search(r'/WKT\((.*)\)>>>>', viewport)[1]

crs = pyproj.CRS.from_wkt(wkt)
forward = pyproj.Transformer.from_crs(crs.geodetic_crs, crs, always_xy=True)
inverse = pyproj.Transformer.from_crs(crs, crs.geodetic_crs, always_xy=True)
projected = np.array(forward.transform(geographic[:, 1], geographic[:, 0])).T
design = np.column_stack([local, np.ones(len(local))])
matrix = np.linalg.lstsq(design, projected, rcond=None)[0]
residuals = np.linalg.norm(design @ matrix - projected, axis=1)
assert max(residuals) < 2, residuals

def coordinate(u, v):
    east, north = np.array([u, 1-v, 1]) @ matrix
    return list(inverse.transform(east, north))

# Frozen before fitting/selection. Offset cells are excluded from training.
train_axis = np.linspace(.05, .95, 6)
check_axis = [.14, .32, .50, .68, .86]
controls = [dict(id=f'publisher-{x}-{y}', image=[float(u), float(v)], coordinate=coordinate(u, v))
            for x, u in enumerate(train_axis) for y, v in enumerate(train_axis)]
checks = [dict(id=f'check-{x}-{y}', image=[u, v], coordinate=coordinate(u, v))
          for x, u in enumerate(check_axis) for y, v in enumerate(check_axis)]
output = dict(sourceSha256=sha256, originalSize=[1584, 1224], oracle='Embedded NRCan GEO viewport, projected CRS affine grid',
              datum='NAD83 as specified in the source; no sub-metre WGS84 accuracy claim',
              wkt=wkt, projectedControlResidualMeters=residuals.tolist(),
              versions=dict(pyproj=pyproj.__version__, proj=pyproj.proj_version_str, pymupdf=pymupdf.VersionBind, numpy=np.__version__),
              controlPoints=controls, checkPoints=checks,
              independentOfModelTraining=True, independentOfPublisher=False,
              note='Checks measure interpolation against the publisher georeferencing, not independent cartographic/historical accuracy.')
root = Path(__file__).parent
(root / 'canada-reference.json').write_text(json.dumps(output, indent=2), encoding='utf-8')
(root / 'publisher-controls.json').write_text(json.dumps(dict(type='control-points', mode='auto', points=controls), indent=2), encoding='utf-8')
print(json.dumps(dict(controls=len(controls), checks=len(checks), projectedResidualMeters=residuals.tolist(), output=str(root/'canada-reference.json'))))
