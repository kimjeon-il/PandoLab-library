import ast,base64,json,math,struct,subprocess,tempfile
from pathlib import Path
from PIL import Image
source=subprocess.check_output(['git','show','bffbabb6:tools/build-physical-data.py']).decode('utf8');tree=ast.parse(source)
fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='crop_with_gutter')
mod=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),fn],type_ignores=[])
scope={'Image':Image};exec(compile(ast.fix_missing_locations(mod),'gutter-oracle','exec'),scope);crop=scope['crop_with_gutter']
w,h=4,3
land=Image.frombytes('RGB',(w,h),bytes((i*31+7)%256 for i in range(w*h*3)))
ocean=Image.frombytes('RGB',(w,h),bytes((i*17+211)%256 for i in range(w*h*3)))
mask=Image.frombytes('L',(w,h),bytes((i*23)%256 for i in range(w*h)))
relief=Image.frombytes('L',(w,h),bytes((i*19+5)%256 for i in range(w*h)))
images=[land,ocean,mask,relief];cases=[]
for name,box in [('northwest',[0,0,2,2]),('southeast',[2,1,4,3]),('interior',[1,1,3,2]),('world',[0,0,4,3])]:
 left,top,right,bottom=box;y0=max(0,top-1);y1=min(h,bottom+1);bands=[]
 for img,mode in zip(images,['RGB','RGB','L','L']):
  for b in [(left,y0,right,y1),((left-1)%w,y0,(left-1)%w+1,y1),(right%w,y0,right%w+1,y1)]:
   bands.append(img.crop(b).convert(mode).tobytes())
 frame=struct.pack('<8sIIII',b'PDPCMP03',right-left,bottom-top,int(top>0),int(bottom<h))+b''.join(bands)
 a,b,m,shade=[crop(img,tuple(box)) for img in images];r,g,bl=Image.composite(a.convert('RGB'),b.convert('RGB'),m).split();expected=Image.merge('RGBA',(r,g,bl,shade.convert('L'))).tobytes()
 cases.append({'name':name,'box':box,'frame':base64.b64encode(frame).decode(),'expected':base64.b64encode(expected).decode()})
enc=lambda im:base64.b64encode(im.tobytes()).decode('ascii')
Path('tests/fixtures/physical-gutter-composite-oracle.json').write_text(json.dumps({'width':w,'height':h,'land':enc(land),'ocean':enc(ocean),'mask':enc(mask),'relief':enc(relief),'cases':cases},separators=(',',':')),encoding='utf8')
print('cases',len(cases))

