# PandoLab library

Data and non-Viewer authoring tools share this repository. The Web Viewer,
product Core and runtime build support remain in [Pando](https://github.com/kimjeon-il/Pando).
Map analysis, training and the private plugin remain in Map Toolkit.

The permanent local root is `D:/dev/PandoLab-library`. Read [AGENTS.md](AGENTS.md)
before changing sources, materialized data, reports or caches.

## Tool code and paired data

`tools/` owns QGIS integration, historical-source authoring and repository
administration. `tests/` contains focused tool tests and fixtures, `config/`
contains execution configuration and `.github/` contains selected tool CI.
`config/pando-code.json` independently pins shared computation/storage inputs;
it does not change any application's runtime data revision.

Use the existing Node 24/pnpm runtime and shared package store. In PowerShell:

```powershell
$env:PANDO_CONSUMER_ROOT='D:/dev/PandoLab'
node --import ./tools/register-consumer.mjs tools/qgis/native-bridge.mjs status
node --test tests/tools/pando-consumer.test.mjs
```

For tool tests that spawn Node children, pass the same import hook through a
task-local `NODE_OPTIONS` using its absolute file URL. Do not set it globally.
Native code builds only through the selected registered CI command documented
in AGENTS.md. Data-only work does not run tests or generators automatically.

## Data and evidence

- [Reports and research index](reports/README.md)
- [Compressed original evidence](archive/README.md)
- Editable library: library.json and objects/.
- Runtime baseline: assets/data/. Branches preserve paired app datasets.
- Current terrain: terrain/v0.13.3/, LOD0-5 of one dataset. Only currently selected terrain editions remain. Required source and explicit reproduction history is retained; unused generated editions are retired.

Only terrain is published from gh-pages. Main holds the full storage corpus and is not a Pages source.
