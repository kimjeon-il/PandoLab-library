import base64,json
from pathlib import Path
from PIL import Image
w,h=256,1
land=bytes((i*37+31)%256 for i in range(w*3));ocean=bytes((i*73+11)%256 for i in range(w*3));mask=bytes(range(256));relief=bytes(reversed(range(256)))
a=Image.frombytes('RGB',(w,h),land);b=Image.frombytes('RGB',(w,h),ocean);m=Image.frombytes('L',(w,h),mask);shade=Image.frombytes('L',(w,h),relief)
r,g,bl=Image.composite(a,b,m).split();out=Image.merge('RGBA',(r,g,bl,shade)).tobytes()
encode=lambda x:base64.b64encode(x).decode('ascii')
Path('tests/fixtures/physical-composite-oracle.json').write_text(json.dumps({'width':w,'height':h,'land':encode(land),'ocean':encode(ocean),'mask':encode(mask),'relief':encode(relief),'expected':encode(out)},separators=(',',':')),encoding='utf8')
print('Pillow composite RGBA:',len(out),'bytes')
