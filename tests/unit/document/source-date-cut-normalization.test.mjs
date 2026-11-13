import {pathToFileURL} from 'node:url';
import {resolve} from 'node:path';
import { describe as contractSuite } from 'node:test';
import * as __dep0 from "node:assert/strict";
import * as __dep1 from "node:test";
import * as __dep2 from "node:fs";
import * as __dep8 from "pando:tools/data/builtin-country-bytes.mjs";
import * as __dep9 from "node:crypto";

import * as __dep11 from "pando:tools/data/territorial-entity-sources.mjs";
import * as __dep12 from "pando:tools/gis/territorial-library.js";
import * as __dep13 from "../../../tools/gis/borders/common/normalize-2026-source-reference.mjs";
import * as __dep14 from "pando:src/data/builtin-world-loader.js";
import * as __dep15 from "pando:src/document/temporal.js";
contractSuite("source-date-cut-normalization", () => {
const test = __dep1.default;
const { readBuiltinCountryStoredBytes, readBuiltinCountry } = __dep8;
const assert = __dep0.default;
const fs = __dep2.default;
const { createHash } = __dep9;

const { readTerritorialSource, territorialSourceRoot } = __dep11;
const { selectGeometryVersion } = __dep12;
const { SOURCE_CUTS, SOURCE_REFERENCE_DATE, planSourceDateConsolidation } = __dep13;
const { selectBuiltinCountries, assembleBuiltinWorld } = __dep14;
const { temporalContains, temporalMonthEnd } = __dep15;

const sha=value=>createHash('sha256').update(JSON.stringify(value)).digest('hex');
const world=pathToFileURL(resolve(process.env.PANDO_CONSUMER_ROOT,'assets/data/builtin-world/generated/v1')+'/');
test('source reference 2026-10-06 never becomes a political geometry transition',()=>{
 const entries=SOURCE_CUTS.map(rule=>readTerritorialSource(rule.id)),byId=new Map(entries.map(e=>[e.entityId,e]));
 const view=JSON.parse(fs.readFileSync(territorialSourceRoot+'/views/world.json','utf8'));
 const outcome=planSourceDateConsolidation(entries,view);
 assert.equal(outcome.already,true,'Five verified sources must be normalized before publishing');
 assert.equal(outcome.proof.length,5);
 for(const rule of SOURCE_CUTS){
  const e=byId.get(rule.id),kept=e.geometryVersions.find(v=>v.versionId===rule.history);
  assert.ok(e);
  assert.equal(e.lifetime.validTo,null,rule.id);
  assert.equal(kept.validFrom,rule.first,rule.id+' event date');
  assert.equal(kept.validTo,null,rule.id+' must remain valid without a fabricated end date');
  assert.equal(kept.certainty,'low',rule.id+' historical proxy confidence');
  assert.equal(kept.historicalProvenance.sourceReferenceDate,SOURCE_REFERENCE_DATE);
  assert.equal(e.metadata.sourceOutlineReferenceDate,SOURCE_REFERENCE_DATE);
  assert.equal(e.metadata.representativeGeometryVersionId,rule.history);
  assert.equal(e.geometryVersions.some(v=>v.versionId===rule.modern),false);
  assert.equal(e.geometryVersions.some(v=>v.validFrom===SOURCE_REFERENCE_DATE||v.validTo==='2026-10-05'),false);
  assert.equal(e.sourceInfo.temporalBoundaryCorrection.kind,'source-reference-date-not-geopolitical-event');
  assert.equal(e.sourceInfo.temporalBoundaryCorrection.geometrySha256,sha(kept.geometry));
  assert.equal(selectGeometryVersion(e,'2026-10-05')?.versionId,rule.history);
  assert.equal(selectGeometryVersion(e,'2026-10-06')?.versionId,rule.history);
  assert.equal(selectGeometryVersion(e,'2026-10-31')?.versionId,rule.history);
  assert.equal(view.selections.find(row=>row.entityId===rule.id)?.geometryVersionId,rule.history);
 }
});
test('published world retains uninterrupted source geometry through October 2026',()=>{
 const index=JSON.parse(fs.readFileSync(new URL('index.json',world),'utf8'));
 const entries=new Map(index.entities.map(row=>[row.entityId,row]));
 const selected=new Set(selectBuiltinCountries(index,'2026-10').map(row=>row.entityId));
 const selectedPrevious=new Set(selectBuiltinCountries(index,'2026-09').map(row=>row.entityId));
 for(const rule of SOURCE_CUTS){
  const projectId=rule.id.slice('state:'.length);
  assert.ok(selected.has(projectId),projectId+' missing in October');
  assert.ok(selectedPrevious.has(projectId),projectId+' missing in September');
  const record=entries.get(projectId);
  assert.ok(record);
  const compressed=readBuiltinCountryStoredBytes(record,file=>fs.readFileSync(new URL(file,world)));
  assert.equal(createHash('sha256').update(compressed).digest('hex'),record.sha256);
  const compiled=readBuiltinCountry(record,index,file=>fs.readFileSync(new URL(file,world)));
  const selectedSource=month=>compiled.sourceBindings.find(row=>temporalContains(row,temporalMonthEnd(month)))?.sourceVersionId;
  assert.equal(selectedSource('2026-09'),rule.history,projectId+' prior source');
  assert.equal(selectedSource('2026-10'),rule.history,projectId+' current source');
  const active=month=>assembleBuiltinWorld({...index,entities:[record]},[compiled],month);
  const before=active('2026-09'),after=active('2026-10');
  assert.equal(before.territorialEntities[0].properties.sourceGeometryVersion,rule.history);
  assert.equal(after.territorialEntities[0].properties.sourceGeometryVersion,rule.history);
 }
});
});
