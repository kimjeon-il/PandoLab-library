import fs from'node:fs';let p='tools/gis/historical-display-review.mjs',s=fs.readFileSync(p,'utf8');s="import fs from 'node:fs';\nimport {pathToFileURL} from 'node:url';\n"+s;s+=`if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 if(process.argv.length!==6||process.argv[2]!=='--before'||process.argv[4]!=='--candidate')throw Error('Usage: node tools/gis/historical-display-review.mjs --before BEFORE.json --candidate CANDIDATE.json');
 const previous=JSON.parse(fs.readFileSync(process.argv[3])),candidate=JSON.parse(fs.readFileSync(process.argv[5]));if(previous.entityId!==candidate.entityId)throw Error('Review identity mismatch');
 console.log(JSON.stringify({entityId:candidate.entityId,changedHistoricalVersionsReviewed:assertHistoricalDisplayChanges(candidate,previous),result:'passed-for-this-change-only'}));
}\n`;fs.writeFileSync(p,s);
