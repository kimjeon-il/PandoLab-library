import subprocess
import numpy as np
from PIL import Image, ImageDraw

for width in (65536, 100000, 1000000, 1000000000):
    for points in [((0, 0), (19, 0)), ((0, 0), (19, 19)), ((19, 0), (0, 19))]:
        image = Image.new('L', (20, 20))
        ImageDraw.Draw(image).line(points, fill=1, width=width)
        expected = ''.join(str(v) for v in np.asarray(image).flat)
        args = ['node', 'build-native/map-review/wide-line-dev.cjs', '20', '20', *map(str, points[0]), *map(str, points[1]), str(width)]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        assert result.stdout.strip() == expected, (width, points)
print('12 wide line cases match Pillow')
