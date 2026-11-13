import fs from'node:fs';const p='tests/unit/builtin-country-publication.test.mjs';let s=fs.readFileSync(p,'utf8');s=s.replace(' publication.writeBuiltinWorldPublication(before,folder);',` assert.throws(()=>publication.writeBuiltinWorldPublication(before,folder),/Historical display review required/);
 assert.equal(fs.existsSync(path.join(folder,'index.json')),false,'review failure precedes every output write');
 // Seed an immutable already-published synthetic baseline; legacy read is allowed.
 for(const [file,bytes]of before){const target=path.join(folder,file);fs.mkdirSync(path.dirname(target),{recursive:true});fs.writeFileSync(target,bytes);}`);fs.writeFileSync(p,s);
