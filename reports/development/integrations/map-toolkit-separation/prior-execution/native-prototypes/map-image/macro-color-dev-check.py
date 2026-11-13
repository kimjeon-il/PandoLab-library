import subprocess
import numpy as np

rng = np.random.default_rng(8365)
for iteration in range(24):
    width, height = 32, 23
    image = rng.integers(0, 256, (height, width, 3), dtype=np.uint8)
    colors = rng.random((6, 3))
    image[0, 1] = [100, 100, 100]
    base = float(np.float32(100) / np.float32(255))
    colors[2] = [base + .15, base, base]
    colors[3] = [base + 2.5 / 255, base, base]
    if iteration % 3 == 0:
        colors[0] = image[0, 0].astype(np.float64) / 255
        colors[1] = colors[0]
    for mode in ('palette', 'visible'):
        rgb = image.astype(np.float32) / 255
        if mode == 'palette':
            palette = colors.astype(np.float32)
            expected = np.zeros((height, width), dtype=np.uint8)
            nearest = np.full((height, width), np.inf)
            for index, color in enumerate(palette):
                distance = np.max(np.abs(rgb - color), axis=2)
                take = (distance < nearest) & (distance <= 2.5 / 255)
                expected[take] = index + 1
                nearest[take] = distance[take]
        else:
            expected = np.zeros((height, width), dtype=bool)
            for color in colors.tolist():
                expected |= np.max(np.abs(rgb - color), axis=2) <= .15
            expected = expected.astype(np.uint8)
        native = subprocess.run(['node', 'build-native/map-image/macro-color-dev.cjs', mode, str(width), str(height), str(len(colors))],
                                input=(' '.join(repr(float(value)) for value in colors.flat) + ' ' + ' '.join(map(str, image.flat))).encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if native.returncode:
            raise RuntimeError(native.stderr.decode('utf-8', errors='replace'))
        actual = np.fromstring(native.stdout.decode(), sep=' ', dtype=np.uint8).reshape(height, width)
        assert np.array_equal(actual, expected), (mode, iteration, np.count_nonzero(actual != expected))
print('48 palette/visible cases match NumPy')
