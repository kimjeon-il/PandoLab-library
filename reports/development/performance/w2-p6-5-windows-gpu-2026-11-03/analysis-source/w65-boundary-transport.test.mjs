import test from 'node:test';
import assert from 'node:assert/strict';
import { createGeometryVersionStore } from '../../shared/frontend/js/modules/geometry-version-store.js';
import { createCountryBoundaryGeometryTransport } from "data:text/javascript;base64,aW1wb3J0IHsgZ2VvbWV0cnlSZWZlcmVuY2VGb3IgfSBmcm9tICJmaWxlOi8vL0Q6L2Rldi93b3JrdHJlZXMvdWkvc2hhcmVkL2Zyb250ZW5kL2pzL21vZHVsZXMvZ2VvbWV0cnktdmVyc2lvbi1zdG9yZS5qcyI7CmltcG9ydCB7IGdlb21ldHJ5UmV2aXNpb25LZXkgfSBmcm9tICJmaWxlOi8vL0Q6L2Rldi93b3JrdHJlZXMvdWkvc2hhcmVkL2Zyb250ZW5kL2pzL21vZHVsZXMvZ2VvbWV0cnktdmVyc2lvbnMuanMiOwoKLy8gQSB2ZXJpZmllZCBXb3JrZXIgYWNrbm93bGVkZ2VtZW50IGlzIHRoZSBvbmx5IHVzYWJsZSBiYXNlLiBBIEpTIGdlb21ldHJ5Ci8vIGlkZW50aXR5L3JldmlzaW9uIGlzIE5PVCBwcm9vZiBvZiBlcXVpdmFsZW50IGNvb3JkaW5hdGVzIGFjcm9zcyBkb2N1bWVudHMuCi8vIE9ubHkgdGhlIGV4YWN0IHNhbWUgZGVlcGx5IGZyb3plbiBHZW9tZXRyeVZlcnNpb25TdG9yZSBvYmplY3QgbWF5IG9taXQgYnl0ZXMuCmV4cG9ydCBmdW5jdGlvbiBjcmVhdGVDb3VudHJ5Qm91bmRhcnlHZW9tZXRyeVRyYW5zcG9ydCgpIHsKICBsZXQgYWNjZXB0ZWQgPSBudWxsOwogIGxldCBwZW5kaW5nID0gbnVsbDsKCiAgZnVuY3Rpb24gcmVzZXQoKSB7CiAgICBhY2NlcHRlZCA9IG51bGw7CiAgICBwZW5kaW5nID0gbnVsbDsKICB9CgogIGZ1bmN0aW9uIHBsYW5SZXBsYWNlKGZlYXR1cmVzKSB7CiAgICBjb25zdCBvcmRlciA9IGZlYXR1cmVzLm1hcChmZWF0dXJlID0+IFN0cmluZyhmZWF0dXJlLmlkKSk7CiAgICBjb25zdCB2YWxpZE9yZGVyID0gb3JkZXIuZXZlcnkoQm9vbGVhbikgJiYgbmV3IFNldChvcmRlcikuc2l6ZSA9PT0gb3JkZXIubGVuZ3RoOwogICAgY29uc3Qgc25hcHNob3RzID0gZmVhdHVyZXMubWFwKGZlYXR1cmUgPT4gKHsKICAgICAgaWQ6IFN0cmluZyhmZWF0dXJlLmlkKSwKICAgICAgZ2VvbWV0cnk6IGZlYXR1cmUuZ2VvbWV0cnksCiAgICAgIHJlZmVyZW5jZTogZ2VvbWV0cnlSZWZlcmVuY2VGb3IoZmVhdHVyZS5nZW9tZXRyeSksCiAgICAgIHJldmlzaW9uOiBnZW9tZXRyeVJldmlzaW9uS2V5KGZlYXR1cmUuZ2VvbWV0cnkpLAogICAgfSkpOwogICAgY29uc3QgZnVsbCA9ICgpID0+ICh7CiAgICAgIHR5cGU6ICdyZXBsYWNlJywgdHJhbnNwb3J0VmVyc2lvbjogMSwKICAgICAgZmVhdHVyZXM6IGZlYXR1cmVzLm1hcCgoZmVhdHVyZSwgaW5kZXgpID0+ICh7CiAgICAgICAgLi4uZmVhdHVyZSwgYm91bmRhcnlHZW9tZXRyeVJldmlzaW9uOiBzbmFwc2hvdHNbaW5kZXhdLnJldmlzaW9uLAogICAgICB9KSksCiAgICAgIHJlbW92ZWRJZHM6IFtdLAogICAgfSk7CgogICAgbGV0IG1lc3NhZ2UgPSBmdWxsKCk7CiAgICBsZXQgcmV1c2VkR2VvbWV0cnlDb3VudCA9IDA7CiAgICBpZiAodmFsaWRPcmRlciAmJiBhY2NlcHRlZCAmJiAhcGVuZGluZykgewogICAgICBjb25zdCBuZXh0SWRzID0gbmV3IFNldChvcmRlcik7CiAgICAgIC8vIEV4aXN0aW5nIHByZXBhcmVkLXN0b3JlIE1hcCBvcmRlciBpcyBzdGFibGUgZm9yIGRlbGV0aW9uIGFuZCBhcHBlbmQuCiAgICAgIC8vIEluc2VydGlvbiBvciByZW9yZGVyaW5nIGluIHRoZSBtaWRkbGUgdXNlcyBhbiBhdXRob3JpdGF0aXZlIGZ1bGwgZnJhbWUuCiAgICAgIGNvbnN0IGV4cGVjdGVkT3JkZXIgPSBbCiAgICAgICAgLi4uYWNjZXB0ZWQub3JkZXIuZmlsdGVyKGlkID0+IG5leHRJZHMuaGFzKGlkKSksCiAgICAgICAgLi4ub3JkZXIuZmlsdGVyKGlkID0+ICFhY2NlcHRlZC5ieUlkLmhhcyhpZCkpLAogICAgICBdOwogICAgICBpZiAoZXhwZWN0ZWRPcmRlci5sZW5ndGggPT09IG9yZGVyLmxlbmd0aAogICAgICAgICYmIGV4cGVjdGVkT3JkZXIuZXZlcnkoKGlkLCBpbmRleCkgPT4gaWQgPT09IG9yZGVyW2luZGV4XSkpIHsKICAgICAgICBjb25zdCBkZWx0YUZlYXR1cmVzID0gZmVhdHVyZXMubWFwKChmZWF0dXJlLCBpbmRleCkgPT4gewogICAgICAgICAgY29uc3QgY3VycmVudCA9IHNuYXBzaG90c1tpbmRleF0sIHByZXZpb3VzID0gYWNjZXB0ZWQuYnlJZC5nZXQoY3VycmVudC5pZCk7CiAgICAgICAgICBjb25zdCBzYW1lID0gY3VycmVudC5yZWZlcmVuY2UgJiYgcHJldmlvdXM/LnJlZmVyZW5jZQogICAgICAgICAgICAmJiBjdXJyZW50Lmdlb21ldHJ5ID09PSBwcmV2aW91cy5nZW9tZXRyeQogICAgICAgICAgICAmJiBjdXJyZW50LnJldmlzaW9uID09PSBwcmV2aW91cy5yZXZpc2lvbgogICAgICAgICAgICAmJiBjdXJyZW50LnJlZmVyZW5jZS5pZCA9PT0gcHJldmlvdXMucmVmZXJlbmNlLmlkCiAgICAgICAgICAgICYmIGN1cnJlbnQucmVmZXJlbmNlLnZlcnNpb24gPT09IHByZXZpb3VzLnJlZmVyZW5jZS52ZXJzaW9uOwogICAgICAgICAgaWYgKCFzYW1lKSByZXR1cm4geyAuLi5mZWF0dXJlLCBib3VuZGFyeUdlb21ldHJ5UmV2aXNpb246IGN1cnJlbnQucmV2aXNpb24gfTsKICAgICAgICAgIHJldXNlZEdlb21ldHJ5Q291bnQgKz0gMTsKICAgICAgICAgIGNvbnN0IHsgZ2VvbWV0cnksIC4uLm1ldGFkYXRhIH0gPSBmZWF0dXJlOwogICAgICAgICAgcmV0dXJuIHsgLi4ubWV0YWRhdGEsIGJvdW5kYXJ5R2VvbWV0cnlSZXZpc2lvbjogY3VycmVudC5yZXZpc2lvbiB9OwogICAgICAgIH0pOwogICAgICAgIGlmIChyZXVzZWRHZW9tZXRyeUNvdW50KSB7CiAgICAgICAgICBtZXNzYWdlID0gewogICAgICAgICAgICB0eXBlOiAnZGVsdGEnLCB0cmFuc3BvcnRWZXJzaW9uOiAxLCBiYXNlVG9rZW46IGFjY2VwdGVkLnRva2VuLAogICAgICAgICAgICBmZWF0dXJlczogZGVsdGFGZWF0dXJlcywKICAgICAgICAgICAgcmVtb3ZlZElkczogYWNjZXB0ZWQub3JkZXIuZmlsdGVyKGlkID0+ICFuZXh0SWRzLmhhcyhpZCkpLAogICAgICAgICAgfTsKICAgICAgICB9CiAgICAgIH0KICAgIH0KCiAgICAvLyBUaGUgbmV4dCBtZXNzYWdlIG11c3QgYmUgZnVsbCB1bnRpbCB0aGlzIHJlcXVlc3QgaGFzIGFjdHVhbGx5IGJlZW4KICAgIC8vIGFja25vd2xlZGdlZDsgV29ya2VyIGNvYWxlc2NpbmcgbWF5IHNraXAgYW55IGluLWZsaWdodCBwcmVwYXJhdGlvbi4KICAgIHBlbmRpbmcgPSB7IG9yZGVyLCBzbmFwc2hvdHMsIG1vZGU6IG1lc3NhZ2UudHlwZSwgcmV1c2VkR2VvbWV0cnlDb3VudCB9OwogICAgcmV0dXJuIG1lc3NhZ2U7CiAgfQoKICBmdW5jdGlvbiBhY2tub3dsZWRnZShiYXNlVG9rZW4pIHsKICAgIGlmICghcGVuZGluZyB8fCB0eXBlb2YgYmFzZVRva2VuICE9PSAnc3RyaW5nJyB8fCAhYmFzZVRva2VuKSB7CiAgICAgIHJlc2V0KCk7CiAgICAgIHJldHVybiBmYWxzZTsKICAgIH0KICAgIGFjY2VwdGVkID0gewogICAgICB0b2tlbjogYmFzZVRva2VuLAogICAgICBvcmRlcjogcGVuZGluZy5vcmRlciwKICAgICAgYnlJZDogbmV3IE1hcChwZW5kaW5nLnNuYXBzaG90cy5tYXAoc25hcHNob3QgPT4gW3NuYXBzaG90LmlkLCBzbmFwc2hvdF0pKSwKICAgIH07CiAgICBwZW5kaW5nID0gbnVsbDsKICAgIHJldHVybiB0cnVlOwogIH0KCiAgcmV0dXJuIE9iamVjdC5mcmVlemUoewogICAgcGxhblJlcGxhY2UsCiAgICBhY2tub3dsZWRnZSwKICAgIHJlc2V0LAogICAgcGVuZGluZ01vZGU6ICgpID0+IHBlbmRpbmc/Lm1vZGUgfHwgbnVsbCwKICAgIHBlbmRpbmdSZXVzZWRHZW9tZXRyeUNvdW50OiAoKSA9PiBwZW5kaW5nPy5yZXVzZWRHZW9tZXRyeUNvdW50IHx8IDAsCiAgfSk7Cn0K";
import { touchGeometry } from '../../shared/frontend/js/modules/geometry-versions.js';

const polygon = (west, east) => ({ type: 'Polygon',
  coordinates: [[[west, 0], [east, 0], [east, 1], [west, 1], [west, 0]]] });
const feature = (id, geometry, parentId = '', name = id) => ({
  type: 'Feature', id, geometry,
  properties: { parentId, entityKind: 'general', name },
  boundaryRootId: parentId || id,
});

test('P6-3 sends only certified immutable geometry omissions and preserves all current metadata', () => {
  const immutable = createGeometryVersionStore([
    { id: 'root-geometry', version: 1, geojson: polygon(0, 1) },
    { id: 'child-geometry', version: 1, geojson: polygon(1, 2) },
  ]);
  const root = immutable.get({ id: 'root-geometry', version: 1 });
  const child = immutable.get({ id: 'child-geometry', version: 1 });
  const mutable = polygon(3, 4);
  const transport = createCountryBoundaryGeometryTransport();
  const original = [feature('ROOT', root), feature('CHILD', child, 'ROOT'), feature('OTHER', mutable)];
  const first = transport.planReplace(original);
  assert.equal(first.type, 'replace');
  assert.ok(first.features.every(row => Object.hasOwn(row, 'geometry')));
  assert.equal(transport.acknowledge('worker-ack:1'), true);

  const renamed = [feature('ROOT', root, '', 'Renamed'), feature('CHILD', child, '', 'Reassigned'),
    feature('OTHER', mutable)];
  const next = transport.planReplace(renamed);
  assert.equal(next.type, 'delta');
  assert.equal(next.baseToken, 'worker-ack:1');
  assert.deepEqual(next.removedIds, []);
  assert.ok(!Object.hasOwn(next.features[0], 'geometry'), 'unchanged frozen root sends no coordinates');
  assert.ok(!Object.hasOwn(next.features[1], 'geometry'), 'owner reassignment preserves current hierarchy metadata');
  assert.equal(next.features[1].properties.parentId, '');
  assert.equal(next.features[0].properties.name, 'Renamed');
  assert.strictEqual(next.features[2].geometry, mutable, 'unregistered mutable geometry is never omitted');
  assert.equal(transport.pendingReusedGeometryCount(), 2);

  // An in-flight job may be superseded. Its unacknowledged geometry cannot
  // serve as the base of a subsequent request.
  assert.equal(transport.planReplace(renamed).type, 'replace');
  assert.equal(transport.acknowledge('worker-ack:2'), true);
  const moved = structuredClone(renamed);
  moved[0].geometry.coordinates[0][1][0] += 1e-8;
  const changed = transport.planReplace(moved);
  assert.equal(changed.type, 'replace', 'cloned geometry cannot claim the old immutable provenance');
  assert.equal(transport.acknowledge('worker-ack:3'), true);

  transport.reset();
  assert.equal(transport.planReplace(renamed).type, 'replace', 'Worker restart/rollback must retransmit a full base');
});

test('P6-3 supports removed IDs and trailing insertion but falls back for reorder', () => {
  const store = createGeometryVersionStore([{ id: 'a', version: 1, geojson: polygon(0, 1) }]);
  const a = feature('A', store.get({ id: 'a', version: 1 }));
  const b = feature('B', polygon(2, 3));
  const transport = createCountryBoundaryGeometryTransport();
  transport.planReplace([a, b]);
  transport.acknowledge('ack-1');
  const deletion = transport.planReplace([a]);
  assert.equal(deletion.type, 'delta');
  assert.deepEqual(deletion.removedIds, ['B']);
  assert.equal(deletion.features.length, 1);
  assert.ok(!Object.hasOwn(deletion.features[0], 'geometry'));
  transport.acknowledge('ack-2');
  const addition = transport.planReplace([a, feature('C', polygon(4, 5))]);
  assert.equal(addition.type, 'delta');
  assert.ok(Object.hasOwn(addition.features[1], 'geometry'));
  transport.acknowledge('ack-3');
  assert.equal(transport.planReplace([feature('C', polygon(4, 5)), a]).type, 'replace');
});

test('P6-3 touch revisions and missing acknowledgement force safe full geometry', () => {
  const store = createGeometryVersionStore([{ id: 'a', version: 1, geojson: polygon(0, 1) }]);
  const row = feature('A', store.get({ id: 'a', version: 1 }));
  const transport = createCountryBoundaryGeometryTransport();
  transport.planReplace([row]);
  assert.equal(transport.acknowledge(''), false);
  transport.planReplace([row]);
  transport.acknowledge('ack-2');
  touchGeometry(row.geometry);
  const fresh = transport.planReplace([row]);
  assert.equal(fresh.type, 'replace', 'a new revision may not be declared identical even at the same object address');
});
