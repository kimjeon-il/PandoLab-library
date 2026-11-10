import json,pathlib,ast
p=pathlib.Path(__file__).parent
first={'MYS':'BRN IDN THA','CHL':'ARG BOL PER','BOL':'CHL ARG BRA PRY PER','PER':'CHL BRA BOL ECU COL','ARG':'CHL BRA XQP PRY BOL URY','CYP':'XQZ XXD','IND':'PAK XSQ CHN XQO NPL XXO BGD BTN MMR','LBN':'ISR SYR','ETH':'SDN ERI DJI KEN SOM SSD','SOM':'DJI ETH KEN','MWI':'MOZ TZA ZMB','TZA':'KEN MWI COD BDI MOZ RWA UGA ZMB','SUR':'BRA GUY GUF','GUY':'BRA SUR VEN','MAR':'MRT DZA ESP','CRI':'NIC PAN','NIC':'HND CRI','COG':'AGO COD CAF XQR GAB CMR','COD':'COG AGO CAF XQR BDI RWA SSD TZA UGA ZMB','BTN':'IND CHN XQY','NAM':'ZAF AGO BWA ZMB','ZAF':'SWZ NAM BWA LSO MOZ ZWE','OMN':'ARE YEM SAU','BRA':'ARG XQP PRY BOL PER URY COL GUY SUR GUF VEN','URY':'ARG BRA XQP','CZE':'AUT DEU POL SVK','NOR':'FIN SWE RUS','SWE':'FIN NOR'}
edges={k:set(v.split()) for k,v in first.items()}
for line in (p/'progress-output.txt').read_text(encoding='utf-8-sig').splitlines():
 if not line.startswith('state:'):continue
 code,vals=line.split(' ',1);edges[code[6:]]=set(n[0] or 'Spain-mainland-null-code' for n in ast.literal_eval(vals) if n[2]>0 or n[3]>0)
for r in json.loads((p/'tail-adjacency-checkpoint.json').read_text()):edges[r['entityId'][6:]]=set(n['code'] or n['name'] for n in r['neighbors'] if n['area']>0 or n['length']>0)
todo=set(edges);components=[]
while todo:
 first=min(todo);seen={first};queue=[first]
 for e in queue:
  for n in edges[e]&set(edges)-seen:seen.add(n);queue.append(n)
 todo-=seen
 external=sorted(set().union(*(edges[e] for e in seen))-seen)
 components.append({'members':sorted(seen),'boundaryDependencies':external,'closed':not external})
components.sort(key=lambda x:(len(x['members']),x['members']))
out={'status':'provisional; USA/CAN/MEX exact checks pending','reviewedUniqueCount':len(edges),'scope':'Connectivity collapsed by GENC code for early checkpoint; not a substitute for final per-WP_ID adjacency. Only measured positive-length contacts or positive-area overlaps included.','components':components,'closedComponents':[c for c in components if c['closed']]}
(p/'provisional-connectivity-summary.json').write_text(json.dumps(out,indent=2)+'\n')
for c in components:print(','.join(c['members']),' -> ',','.join(c['boundaryDependencies']))
