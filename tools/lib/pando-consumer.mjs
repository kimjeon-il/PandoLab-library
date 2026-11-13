import {createHash} from 'node:crypto';
import {lstatSync,readFileSync,realpathSync} from 'node:fs';
import {isAbsolute,relative,resolve,sep} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';

// The library owns authoring tools; Pando owns product computation and storage.
// Resolve only reviewed code inputs, independently of the consumer's data pin.
export function consumerResolver({root,pin,libraryRoot}) {
  if(!root)throw Error('Set PANDO_CONSUMER_ROOT to the paired Pando checkout.');
  root=realpathSync(root);
  if(libraryRoot)libraryRoot=realpathSync(libraryRoot);
  if(pin?.repository!=='kimjeon-il/Pando'||!/^[a-f0-9]{40}$/.test(pin.revision)||!pin.files)throw Error('A pinned Pando code dependency is required.');
  const verified=new Set();
  const verify=path=>{
    const name=relative(root,path).split(sep).join('/');
    if(!name||name.startsWith('../')||isAbsolute(name))throw Error('Pando code path escaped its owner.');
    if(verified.has(name))return;
    const expected=pin.files[name];if(!expected)throw Error('Unpinned Pando code input: '+name);
    for(let item=path;item!==root;item=resolve(item,'..'))if(lstatSync(item).isSymbolicLink())throw Error('Linked Pando code input: '+name);
    const bytes=readFileSync(path,'utf8').replaceAll('\r\n','\n');
    if(createHash('sha256').update(bytes).digest('hex')!==expected)throw Error('Pando code differs from its reviewed pin: '+name);
    verified.add(name);
  };
  return {resolve(specifier,context,nextResolve){
    if(specifier.startsWith('library:')){
      const name=specifier.slice(8);
      if(!libraryRoot||! /^(tools|tests|scripts|config)\/[\w./-]+$/.test(name)||name.split('/').includes('..'))throw Error('Invalid library code module path.');
      const path=resolve(libraryRoot,name);
      for(let item=path;item!==libraryRoot;item=resolve(item,'..'))if(lstatSync(item).isSymbolicLink())throw Error('Linked library code input: '+name);
      specifier=pathToFileURL(path).href;
    }
    if(specifier.startsWith('pando:')){
      const name=specifier.slice(6);
      if(!/^(src|tools|scripts|tests|assets)\/[\w./-]+$/.test(name)||name.split('/').includes('..'))throw Error('Invalid Pando module path.');
      const path=resolve(root,name);verify(path);specifier=pathToFileURL(path).href;
    }
    const result=nextResolve(specifier,context);
    if(result.url.startsWith('file:')){
      const path=fileURLToPath(result.url),name=relative(root,path);
      if(name&&!name.startsWith('..'+sep)&&!isAbsolute(name)&&!name.split(sep).includes('node_modules'))verify(path);
    }
    return result;
  }};
}
