import fs from'node:fs';import{pathToFileURL}from'node:url';const root='D:/dev/PandoLab-library-data/reports/.edits/gis/borders/validation/ne-world-map-rebase-2026-11-08/historical-modern-reuse-local-20261109',m=await import(pathToFileURL(root+'/deu-c1-c2-c3-combined/source-review/review-inputs.mjs')),rev=m.git('rev-parse','main').toString().trim();fs.writeFileSync(root+'/idn-modern-equivalence-audit-20261110/source-inputs.json',JSON.stringify({sourceRevision:rev,rec:m.entity('IDN',rev),neighbors:[m.entity('TLS',rev)],ne:JSON.parse(m.archived('assets/data/countries-ne-5.1.1.geojson',rev))}));



