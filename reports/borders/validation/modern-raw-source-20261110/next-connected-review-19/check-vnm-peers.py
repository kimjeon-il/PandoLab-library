exec((__import__('pathlib').Path(__file__).parent/'map-vnm-spratly.py').read_text().replace('print(json.dumps(report))',''))
selected={m['rawComponent'] for m in matches};peer=[]
for i in selected:
 a=raw.GetGeometryRef(i)
 for j in range(raw.GetGeometryCount()):
  if j in selected:continue
  z=raw.GetGeometryRef(j)
  if a.Intersects(z):peer.append({'selected':i,'otherSpratly':j,'area':a.Intersection(z).GetArea()})
 donorPath='D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/display-review-final-authorized-candidate.geojson';ds=ogr.Open(donorPath);ly=ds.GetLayer();ly.SetSpatialFilter(a);ly.ResetReading()
 for f in ly:
  z=f.GetGeometryRef();area=overlaps(a,z)
  if area>0:
   props=json.loads(f.ExportToJson())['properties'];peer.append({'selected':i,'approvedDonorProperties':{k:v for k,v in props.items() if k.lower() in ['id','adm0_a3','name','entityid','code','iso_a3']},'area':area})
 ds=None
rbase=c.execute("select * from DoS_WP_11_4 where GENC_3='VNM'").fetchone();bb=rbase['geom'];base=ogr.CreateGeometryFromWkb(bb[8+{0:0,1:32,2:48,3:48,4:64}[(bb[3]>>1)&7]:]);baseOverlap=[]
for i in selected:
 a=raw.GetGeometryRef(i);baseOverlap.append({'rawSpratly':i,'intersectionBaseArea':overlaps(a,base),'baseContainsInterior':bool(base.Contains(a.PointOnSurface()))})
meta=json.loads((p/'source-metadata.json').read_text());mr=next(x for x in meta['rows'] if x['code']=='VNM');v=next(v for v in mr['descriptor']['geometryVersions'] if v['validTo'] is None);sup=v['modernBoundarySupplement'];receipt=[]
for t in sup['spratlyAllocationEvidence'].values():
 if isinstance(t,dict) and 'reference' in t: receipt.append({'reference':t['reference'],'recordedSha':t['sha256'],'actualSha':hashlib.sha256(pathlib.Path(t['reference']).read_bytes()).hexdigest()})
report.update({'status':'complete-approved-current-set-correspondence-individual-prepared-index-order-unavailable','sourceRevision':meta['pinRevision'],'descriptorSha':mr['descriptorSha256'],'currentGeometryResourceSha':v['geometryResource']['sha256'],'rawBaseBlobSha':hashlib.sha256(bb).hexdigest(),'rawBaseValid':bool(base.IsValid()),'selectedRawComponents':sorted(selected),'rawBaseOverlap':baseOverlap,'peerObservations':peer,'approvedAllocationReceipts':receipt,'proofScope':'Exact raw-to-current component mapping and approved allocation set [0,1,2,4]. Individual prepared-index-to-raw-index bijection is not asserted: original prepared component geometry hashes were unavailable in restored handoff.','noNewOwnershipDecision':True,'candidateComposition':'All original VNM base components plus original Spratly components [2,3,6,10], only after main-country frontier checks pass. Preserve existing allocation keys unchanged; attach separate mapping proof.','raw6Caveat':'Current component 626 shares exact min/max longitudes and intersects original raw6, but thin simplification covers only 7.5644% of raw area and does not contain raw interior point. Do not describe interior-point inclusion as passed.'})
(p/'VNM-supplemental-set-proof.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'selected':sorted(selected),'peers':peer,'base':baseOverlap,'receipts':receipt}))
