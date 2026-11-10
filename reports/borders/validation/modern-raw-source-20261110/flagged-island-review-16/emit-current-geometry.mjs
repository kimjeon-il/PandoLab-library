process.env.PATH='C:/Program Files/Git/cmd;'+process.env.PATH;
import fs from 'node:fs';import {decodeArchiveEntry} from 'file:///D:/dev/worktrees/gis-raw-modern/tools/data/library-context.mjs';
const root='D:/dev/PandoLab-library-data',meta=JSON.parse(fs.readFileSync(new URL('./source-metadata.json',import.meta.url))),index=JSON.parse(fs.readFileSync(root+'/.pando-worktrees/gis-raw-modern/archive/index.json')),r=meta.rows.find(r=>r.code===process.argv[2]),v=r.descriptor.geometryVersions.find(v=>v.validTo===null),path='assets/data/territorial-entities/source/'+v.geometryResource.file;
process.stdout.write(decodeArchiveEntry(root,index.files[path],meta.pinRevision,{fetch:false}));


