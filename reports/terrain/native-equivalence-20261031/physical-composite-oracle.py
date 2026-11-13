import base64,json
from pathlib import Path
from PIL import Image
w,h=256,1
land=bytes((i*37+31)%256 for i in range(w*3));ocean=bytes((i*73+11)%256 for i in range(w*3));mask=bytes(range(256))
a=Image.frombytes('RGB',(w,h),land);b=Image.frombytes('RGB',(w,h),ocean);m=Image.frombytes('L',(w,h),mask)
out=Image.composite(a,b,m).tobytes()
encode=lambda x:base64.b64encode(x).decode('ascii')
p=Path('tests/fixtures/physical-composite-oracle.json')
with p.open('x',encoding='utf8') as f:json.dump({'width':w,'height':h,'land':encode(land),'ocean':encode(ocean),'mask':encode(mask),'expected':encode(out)},f,separators=(',',':'))
print('Pillow composite:',len(out),'bytes')
