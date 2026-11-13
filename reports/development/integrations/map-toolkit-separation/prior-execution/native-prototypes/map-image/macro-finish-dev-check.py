import subprocess
import numpy as np
from PIL import Image, ImageDraw

rng = np.random.default_rng(8891)
for iteration in range(24):
    width, height = int(rng.integers(1, 15)), int(rng.integers(1, 15))
    image = rng.integers(0, 256, (height, width, 3), dtype=np.uint8)
    target = rng.integers(0, 128, (height, width), dtype=np.uint8)
    known = rng.integers(0, 128, (height, width), dtype=np.uint8)
    x = sorted(rng.integers(-5, width + 5, 2).tolist())
    y = sorted(rng.integers(-5, height + 5, 2).tolist())
    glyphs = [[x[0], y[0], x[1], y[1]]]
    for rotation in (0, 90, 180, 270):
        text = Image.new('L', (width, height))
        ImageDraw.Draw(text).rectangle(glyphs[0], fill=1)
        obscured = np.asarray(text).astype(bool)
        a, b = target.copy(), known.copy()
        a[obscured] = b[obscured] = 0
        rgb, a, b = [np.rot90(value, -rotation // 90).copy() for value in (image, a, b)]
        out_h, out_w = a.shape
        exclusions = [[0, 0, max(1, out_w // 2), max(1, out_h // 2)]]
        left, top, right, bottom = exclusions[0]
        a[top:bottom, left:right] = b[top:bottom, left:right] = 0
        expected = np.concatenate([rgb.ravel(), a.ravel(), b.ravel()])
        values = [*glyphs[0], *exclusions[0], *image.flat, *target.flat, *known.flat]
        result = subprocess.run(['node', 'build-native/map-image/macro-finish-dev.cjs', str(width), str(height), str(rotation), '1', '1'],
            input=' '.join(map(str, values)).encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        actual = np.fromstring(result.stdout.decode(), sep=' ', dtype=np.uint8)
        assert np.array_equal(actual, expected), (iteration, rotation, np.count_nonzero(actual != expected))
print('96 glyph, rotation and exclusion cases match Pillow/NumPy')
