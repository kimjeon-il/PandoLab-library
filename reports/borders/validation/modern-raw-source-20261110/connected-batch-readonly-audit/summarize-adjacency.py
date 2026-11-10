import json,pathlib,collections
p=pathlib.Path(__file__).parent
rows=json.loads((p/'raw-adjacency.json').read_text())
inv=json.loads((p.parent/'modern-source-progress.json').read_text())
byentity={r['entityId']:r for r in inv['rows']}
selected={r['entityId'] for r in rows}; graph={e:set() for e in selected}
for r in rows:
 for n in r['neighbors']:
  if n['entityId'] in selected and (n['area']>0 or n['length']>0):graph[r['entityId']].add(n['entityId']);graph[n['entityId']].add(r['entityId'])
components=[]; todo=set(selected)
while todo:
 first=min(todo);seen={first};queue=[first]
 for e in queue:
  for n in graph[e]-seen:seen.add(n);queue.append(n)
 todo-=seen
 external=[];overlaps=[];point=[]
 for r in rows:
  if r['entityId'] not in seen:continue
  for n in r['neighbors']:
   rec={'entity':r['entityId'],**n}
   if n['area']>0:overlaps.append(rec)
   if n['area']==0 and n['length']==0:point.append(rec);continue
   if n['entityId'] not in seen and n['class']!='raw-original-applied':external.append(rec)
 components.append({'members':sorted(seen),'memberCount':len(seen),'blockingExternalContacts':external,'overlapObservations':overlaps,'pointContacts':point,'safeForClosedRawBatch':not external and not overlaps})
components.sort(key=lambda r:(r['memberCount'],r['members']))
unique={};gate=[];unmapped=[]
for r in rows:
 source=byentity[r['entityId']]['rawCandidates'][0]['WP_ID']
 for n in r['neighbors']:
  rec={'entity':r['entityId'],**n}
  if n['area']>0:unique.setdefault(tuple(sorted([source,n['id']])),rec)
  if n['class']=='unmapped':unmapped.append(rec)
  elif n['class'] not in ('unreviewed-one-to-one-modern','raw-original-applied'):gate.append(rec)
summary={'status':'complete','scope':'111 raw originals from initial 114 unreviewed inventory; CUB/JPN/PHL excluded as parallel work. This is a targeted adjacency audit, not complete catalog validation.','currentInventorySummary':inv['summary'],'method':'Original GPKG opened SQLite mode=ro&immutable=1; R-tree bbox candidate lookup; original OGR Intersects/Intersection. No simplification, repair, source modification, network or runtime work.','limitations':['Exact contacts only; this does not detect near gaps or prove mixed old/new source seam safety.','Areas are square degrees, not metric area. Tiny positive overlaps are recorded without asserting material geographic error.','unmapped means no matching WP_ID in inventory rawCandidates, not necessarily absent app entity. XKS is Kosovo; null-code Spain is Spain mainland.','Geometry validity and geopolitical correctness were not exhaustively revalidated. No source application approved by this audit.'],'reviewedCount':len(rows),'componentCount':len(components),'safeClosedComponents':[c['members'] for c in components if c['safeForClosedRawBatch']],'positiveAreaPairCount':len(unique),'positiveAreaPairs':list(unique.values()),'gateContacts':gate,'unmappedInventoryContacts':unmapped,'components':components}
(p/'connected-batch-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
checkpoint=json.loads((p/'checkpoint.json').read_text(encoding='utf-8-sig'));checkpoint.update(status='complete',lastObservedCompletedCount=len(rows),completedCodes=[r['entityId'][6:] for r in rows],lastObservedEntity=rows[-1]['entityId']);(p/'checkpoint.json').write_text(json.dumps(checkpoint,indent=2)+'\n')
print(json.dumps({k:summary[k] for k in ['reviewedCount','componentCount','safeClosedComponents','positiveAreaPairCount']}))
for c in components:print(c['memberCount'],','.join(x[6:] for x in c['members']),'external',len(c['blockingExternalContacts']),'overlaps',len(c['overlapObservations']))
for o in unique.values():print('OVERLAP',o['entity'],o['name'],o['area'])
