import fs from'node:fs';const p='tools/gis/lsib-coordinate-audit.mjs';let s=fs.readFileSync(p,'utf8');s=s.replace('for(const ring of polygonRings(geometry)){','for(const originalRing of polygonRings(geometry)){\n  const ring=originalRing;');s=s.replace('for(const[id,positions]of groups){const ref=',`for(const[id,originalPositions]of groups){
   const open=originalRing.coordinates.slice(0,-1),outside=open.map((_,i)=>i).filter(i=>!originalPositions.has(i));
   const candidates=outside.length?outside:open.map((_,i)=>i);
   const cut=candidates.reduce((a,b)=>open[a][0]<open[b][0]||open[a][0]===open[b][0]&&open[a][1]<=open[b][1]?a:b);
   const ordered=[...open.slice(cut),...open.slice(0,cut)];ordered.push(ordered[0]);
   const ring={...originalRing,coordinates:ordered},positions=new Map();
   ordered.forEach((p,targetIndex)=>{const found=(index.vertices.get(key(p,index.digits))||[]).filter(m=>m.id===id).map(m=>m.index);if(found.length)positions.set(targetIndex,found);});
   const originalTarget=i=>(i+cut)%open.length;
   const ref=`);s=s.replace('targetStart:run[0].targetIndex,targetEnd:run.at(-1).targetIndex','targetStart:originalTarget(run[0].targetIndex),targetEnd:originalTarget(run.at(-1).targetIndex),ringRotation:cut');s=s.replace('targetMatchedIndices:run.map(m=>m.targetIndex)','targetMatchedIndices:run.map(m=>originalTarget(m.targetIndex))');fs.writeFileSync(p,s);
