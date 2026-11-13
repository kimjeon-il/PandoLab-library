import {readFileSync} from 'node:fs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {modernCaspianWater} from '../../../tools/gis/prepare-water-object-history.mjs';
import {geometryAreaKm2} from 'pando:tools/gis/geometry-metrics.js';
test('derived modern water retains islands and uses the small spherical interior',()=>{
 const square=(w,s,e,n)=>[[w,s],[w,n],[e,n],[e,s],[w,s]];
 const outer=square(40,30,60,55),water=square(45,36,55,47).reverse(),island=square(48,40,49,41);
 const land={type:'MultiPolygon',coordinates:[[outer,water],[island]]},before=structuredClone(land);
 const result=modernCaspianWater(land);
 assert.equal(result.coordinates.length,2);
 assert.ok(geometryAreaKm2(result)>0&&geometryAreaKm2(result)<10000000,'water cannot fill the complementary world');
 assert.deepEqual(land,before,'source land and islands stay immutable');
 const points=rings=>[...new Set(rings.flat().map(point=>point.join(',')))].sort();
 assert.deepEqual(points(result.coordinates),points([water,island]));
});

test('water preparation cannot migrate or regenerate all builtin countries as a side effect',()=>{
 const text=readFileSync(new URL('../../../tools/gis/prepare-water-object-history.mjs',import.meta.url),'utf8');
 assert.doesNotMatch(text,/prepareCommonCountryTargets|build-builtin-world\.mjs|finalizeBuiltinWorldFiles|writeBuiltinWorldPublication/,
  'The completed country wire migration is not a dependency of water preparation');
});
