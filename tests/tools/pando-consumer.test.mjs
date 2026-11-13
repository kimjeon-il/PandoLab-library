import test from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {mkdirSync,mkdtempSync,rmSync,writeFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {pathToFileURL} from 'node:url';
import {consumerResolver} from '../../tools/lib/pando-consumer.mjs';

test('consumer code is pinned independently of data and unknown or modified code is refused',t=>{
  const root=mkdtempSync(join(tmpdir(),'pando-code-input-'));
  t.after(()=>rmSync(root,{recursive:true,force:true}));mkdirSync(join(root,'src'));
  const path=join(root,'src/current.mjs'),bytes='export const current=true;\n';writeFileSync(path,bytes);
  const pin={repository:'kimjeon-il/Pando',revision:'a'.repeat(40),files:{'src/current.mjs':createHash('sha256').update(bytes).digest('hex')}};
  const next=url=>({url}),hook=consumerResolver({root,pin});
  assert.equal(hook.resolve('pando:src/current.mjs',{},next).url,pathToFileURL(path).href);
  assert.throws(()=>hook.resolve('pando:src/../secret.mjs',{},next),/Invalid/);
  assert.throws(()=>hook.resolve('pando:src/unknown.mjs',{},next),/Unpinned/);
  writeFileSync(path,'export const current=false;');
  assert.throws(()=>consumerResolver({root,pin}).resolve('pando:src/current.mjs',{},next),/differs/);
  assert.throws(()=>consumerResolver({pin}),/PANDO_CONSUMER_ROOT/);
});
