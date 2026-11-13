import {execFileSync} from 'node:child_process';
import {randomUUID} from 'node:crypto';
import {fileURLToPath} from 'node:url';

const root=fileURLToPath(new URL('../',import.meta.url));
const choices={'--native=qgis-native-bridge':['qgis-native-bridge','qgis-native.yml'],'--native=territorial-recipe':['territorial-recipe','territorial-recipe-native.yml']};
const selection=choices[process.argv.slice(2).join(' ')];if(!selection)throw Error('Select exactly one registered library native check.');
const run=args=>execFileSync(args[0],args.slice(1),{cwd:root,encoding:'utf8',stdio:['ignore','pipe','pipe']}).trim();
if(run(['git','status','--porcelain','--untracked-files=no']))throw Error('Commit the reviewed tool inputs before dispatch.');
const head=run(['git','rev-parse','HEAD']),branch=run(['git','symbolic-ref','--short','HEAD']);
if(run(['git','ls-remote','--heads','origin','refs/heads/'+branch]).split(/\s+/)[0]!==head)throw Error('Push the exact tool revision before dispatch.');
const requestId=randomUUID();
run(['gh','workflow','run',selection[1],'--repo','kimjeon-il/PandoLab-library','--ref',branch,'-f','request_id='+requestId]);
console.log(JSON.stringify({check:selection[0],revision:head,branch,requestId}));
