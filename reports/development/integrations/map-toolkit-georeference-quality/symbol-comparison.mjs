// Diagnostic comparison using preserved OCR observations, not a resumed job.
import { readFile, writeFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
const load=path=>import(pathToFileURL(resolve(process.cwd(),path)));
const {raster}=await load('plugins/pando-map-tools/lib/raster.mjs');
const {digest}=await load('plugins/pando-map-tools/lib/jobs.mjs');
const {referenceImagePointRasterFromRgba,findReferenceImagePointSymbolNearTextBox:find}=await load('plugins/pando-map-tools/lib/analysis/symbols.mjs');
const base=new URL('./',import.meta.url),j=JSON.parse(await readFile(new URL('canada.job.json',base)));
if(digest(await readFile(j.source.path))!==j.source.sha256)throw Error('Original source changed');
const image=await raster({action:'read',path:j.source.path,page:1,maxPixels:4000000});
const pixels=referenceImagePointRasterFromRgba(image),textBoxes=j.ocr.detections.map(v=>v.box);
const observations={whitehorse:[211.795,513.570],yellowknife:[465.599,591.009],iqaluit:[1005.0,527.782],ottawa:[1074.203,1033.016]};
const rows=Object.entries(observations).map(([name,actual])=>{
 const d=j.ocr.detections.find(v=>v.text.toLowerCase().includes(name));
 const symbol=d&&find(pixels,d.box,{searchRadiusPx:32,minimumConfidence:.4,textBoxes});
 return {name,actual,before:d?.symbol?.pixel,after:symbol?.pixel??null,
   beforeError:d?.symbol?Math.hypot(d.symbol.pixel[0]-actual[0],d.symbol.pixel[1]-actual[1]):null,
   afterError:symbol?Math.hypot(symbol.pixel[0]-actual[0],symbol.pixel[1]-actual[1]):null};
});
await writeFile(new URL('symbol-comparison.json',base),JSON.stringify({sourceSha256:j.source.sha256,
 note:'Selected development cases against visually checked PDF symbol centres, not held-out accuracy.',rows},null,2));
console.log(JSON.stringify(rows));
