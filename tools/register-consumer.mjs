import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';
import {readFileSync} from 'node:fs';
import {consumerResolver} from './lib/pando-consumer.mjs';

registerHooks(consumerResolver({root:process.env.PANDO_CONSUMER_ROOT,libraryRoot:fileURLToPath(new URL('../',import.meta.url)),
  pin:JSON.parse(readFileSync(new URL('../config/pando-code.json',import.meta.url),'utf8'))}));
