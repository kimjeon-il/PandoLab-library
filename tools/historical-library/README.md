# Historical source recipes

This library owns source acquisition, reviewed authoring operations and the
East Germany / German Empire recipes. Pando owns the common geometry engine
and the Viewer runtime generators. Follow the [canonical historical boundary
policy](https://github.com/kimjeon-il/Pando/blob/4972742b1c7a23abadc006b89dbdab7047163b9d/docs/historical-border-reconstruction-policy.md).

Set PANDO_CONSUMER_ROOT to the paired Pando workspace. Its existing
config/library-data.json selects the data revision and mounted source scope;
the library tool-code revision does not replace that pin. Run a selected tool
with node --import ./tools/register-consumer.mjs tools/gis/<tool>.mjs.

Recipe compilation requires an existing source-bound CI artifact selected by
PANDO_TERRITORIAL_RECIPE_BINARY. Do not install a local compiler or recreate a
GIS environment. Native reproduction is a manually selected CI operation.
Keep original bytes, source attribution and unique evaluation evidence in their
existing library owner; prepare and write only the selected input/output scope.

No recipe or source audit runs automatically on a data/report commit.
