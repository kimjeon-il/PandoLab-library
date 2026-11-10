import fs from 'node:fs';import {createHash} from 'node:crypto';import {decodeArchiveEntry} from 'file:///D:/dev/worktrees/gis-raw-modern/tools/data/library-context.mjs';
const root='D:/dev/PandoLab-library-data',pin=JSON.parse(fs.readFileSync('D:/dev/worktrees/gis-raw-modern/config/library-data.json')),index=JSON.parse(fs.readFileSync(root+'/.pando-worktrees/gis-raw-modern/archive/index.json')),out=[];const hash=b=>createHash('sha256').update(b).digest('hex');
for(const code of ['MMR','CHN','IND','BGD','LAO','VNM']){const path='assets/data/territorial-entities/source/countries/state-'+code+'.json',bytes=decodeArchiveEntry(root,index.files[path],'85464e0ba06fe43a0e67c9095807d260e5c5ecef',{fetch:false}),d=JSON.parse(bytes);out.push({code,path,descriptorSha256:hash(bytes),descriptor:d});}
fs.writeFileSync(new URL('./source-metadata.json',import.meta.url),JSON.stringify({pinRevision:'85464e0ba06fe43a0e67c9095807d260e5c5ecef',rows:out},null,2)+'\n');console.log(JSON.stringify({pinRevision:'85464e0ba06fe43a0e67c9095807d260e5c5ecef',rows:out.map(r=>({code:r.code,descriptorSha256:r.descriptorSha256,descriptor:r.descriptor}))},null,2));



