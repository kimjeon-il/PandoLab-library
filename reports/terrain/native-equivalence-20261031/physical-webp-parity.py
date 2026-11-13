import base64,hashlib,io,json,subprocess,sys
from PIL import Image
r=json.load(open('tests/fixtures/physical-gutter-composite-oracle.json',encoding='utf8'))['cases'][0]
w=r['box'][2]-r['box'][0]+2;h=r['box'][3]-r['box'][1]+2
rgba=base64.b64decode(r['expected']);image=Image.frombytes('RGBA',(w,h),rgba)
b=io.BytesIO();image.save(b,'WEBP',lossless=True,method=4,exact=True);old=b.getvalue()
header=b'PWEBP001'+w.to_bytes(4,'little')+h.to_bytes(4,'little')
p=subprocess.run(['node','tools/gis/physical-webp-encoder.mjs'],input=header+rgba,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
size=int.from_bytes(p.stdout[:4],'little');new=p.stdout[4:]
assert len(new)==size
assert Image.open(io.BytesIO(new)).convert('RGBA').tobytes()==rgba
assert Image.open(io.BytesIO(old)).convert('RGBA').tobytes()==rgba
print(json.dumps({'pillowBytes':len(old),'nativeBytes':len(new),'pillowSha256':hashlib.sha256(old).hexdigest(),'nativeSha256':hashlib.sha256(new).hexdigest(),'bytesEqual':old==new,'rgbaPixelsEqual':True}))
