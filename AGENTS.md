# PandoLab library

This repository owns library data, original GIS sources, reports/evidence and
non-Viewer authoring/administration tools. Pando owns the Viewer, product Core,
its runtime generators and application validation. Map Toolkit owns analysis,
training and the private plugin. Do not copy their implementations here.

## Working safely

Reuse this permanent checkout and the existing data worktrees, shared Git object
store, materialized caches and dependencies. Before changes inspect Git status,
worktrees, processes, library locks and the exact consumer/data pin. Preserve
unfinished work. Never automatically stash, reset, clean, prune worktrees,
force-push or rewrite history. History administration tools are opt-in; moving
or testing them does not authorize a real repository rewrite.

Code lives in tools/, scripts/, config/, tests/ and .github/. The shared root
keeps code materialized. Linked data worktrees remain metadata-only. Do not
compact source code as an unused data checkout or hydrate all archive blobs.
Runtime data pins and report-owner revisions are independent of tool-code pins.

## Tools and focused checks

config/pando-code.json pins immutable Pando computation/storage inputs. Set
PANDO_CONSUMER_ROOT to the paired Pando checkout and start migrated tools with
`node --import ./tools/register-consumer.mjs tools/<tool>.mjs`. Required code
inputs fail visibly if absent or different from the reviewed pin. The consumer
root supplies its branch's existing data configuration; do not treat the tool
source checkout as the runtime dataset or replace the consumer's data revision.

Run only affected tool checks with small synthetic fixtures. Inspect setup
before running a test. Data/report-only changes must not trigger tool tests,
whole-catalog validation, a full build matrix or GIS regeneration. Full-project
validation requires an explicit request. QGIS native compilation is CI-only:
use `node tests/run-application-checks.mjs --native=qgis-native-bridge`.
Historical recipe code and its small fixed source oracles use only
`node tests/run-application-checks.mjs --native=territorial-recipe`. This
selection does not prepare real sources or regenerate historical geometry.
Do not install local compilers, SDKs, GIS or training environments. Preserve
existing QGIS profiles, running clients and source-bound native artifacts.

## Data, reports and cleanup

Keep archive/index.json and its Git objects, branch-specific data/WASM pairings,
reports/.owners.json, independent .edits/ work, .variants/ and report protection
refs. An unhydrated file is not a deletion. Never traverse a junction or symlink
to clean its target. Resolve and check every deletion path and current consumer.
Preserve original maps, labels, active checkpoints, examination databases and
unique evaluation evidence. Full report originals live once under reports/;
publish only the completed selected scopes through their existing owner.

Delete verified unused reproducible outputs when their use ends. Keep large
outputs only for a concrete current execution, regeneration or verification
consumer. Do not create deletion inventories, cleanup reports, backups or
archive copies of approved obsolete files. Report logical bytes separately
from measured drive free-space changes in the final response.
