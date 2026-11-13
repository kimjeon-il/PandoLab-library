import zipfile,json,hashlib
p='tools/historical-library/sources/ussr-1922-approved/caspian-shoreline-completed-candidate-20261024.zip'
print('zipsha',hashlib.sha256(open(p,'rb').read()).hexdigest())
with zipfile.ZipFile(p) as z:
 for n in z.namelist():
  if any(k in n.lower() for k in ['protect','mask','readme','generaliz']):print('member',n)
 n='caspian-completion/assembled-completion-candidate/waterbody-boundary-network.geojson';d=json.loads(z.read(n));f=d['features'][72];print('feature72keys',list(f));print('properties',json.dumps(f['properties'],ensure_ascii=True));print('coords',len(f['geometry']['coordinates']))
