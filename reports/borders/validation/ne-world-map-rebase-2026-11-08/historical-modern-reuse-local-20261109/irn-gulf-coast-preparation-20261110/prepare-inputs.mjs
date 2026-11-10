import fs from 'node:fs';
import * as m from '../deu-c1-c2-c3-combined/source-review/review-inputs.mjs';
const rev=m.git('rev-parse','main').toString().trim(); const root='reports/borders/validation/ne-world-map-rebase-2026-11-08';
const irn=m.entity('IRN',rev); const approved=JSON.parse(m.archived(root+'/display-review-final-authorized-candidate.geojson',rev));const donor=approved.features.find(f=>f.id==='IRN'||f.id==='state:IRN');
const ne=JSON.parse(m.archived('assets/data/countries-ne-5.1.1.geojson',rev));
const files=['reports/borders/reconstruction/ussr/caspian-territory-delta-2026-10-28/recipe.json','reports/borders/reconstruction/ussr/caspian-territory-delta-2026-10-28/README.md','reports/borders/reconstruction/ussr-central-asia-approved-2026-10-26/patches/atrek/patch-spec.json','reports/borders/validation/current-border-detail-lsib-2026-11-04/ATREK-SCOPE-CORRECTION.md'];
for(const p of files){const b=m.archived(p,rev);fs.writeFileSync(new URL(p.split('/').at(-2)+'-'+p.split('/').at(-1),import.meta.url),b);console.log(p+'\n'+b.toString().slice(0,12000));}
const peers=['IRQ','TUR','ARM','AZE','AFG','PAK','TKM','soviet-union','soviet-union-russian-sfsr','waterbody-caspian'].map(id=>{try{return {id,...m.entity(id,rev)}}catch(e){return {id,error:e.message}}});
fs.writeFileSync(new URL('inputs.json',import.meta.url),JSON.stringify({revision:rev,irn,donor,ne:ne.features.filter(f=>['IRN','IRQ','TUR','ARM','AZE','AFG','PAK','TKM','ARE'].includes(f.id)),peers,archiveEntries:m.archiveEntries()},null,2));
console.log('Donor found: '+Boolean(donor));
