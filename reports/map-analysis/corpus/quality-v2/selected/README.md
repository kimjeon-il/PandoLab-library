# Quality-v2 reviewed macro corpus

Eighteen distinct macro originals are partitioned into six training, six validation and six test sheets. Each split has four modern/two historical and three colour/three monochrome sheets. Sources, rights, publication/content-date distinctions, original hashes and explicit raster derivatives are recorded in corpus.reviewed.json. Subset manifests reuse those same original paths; no duplicate input copies are needed.

All eighteen annotations have two agent source-overlay review passes. Coverage is **partial**, never human-reviewed or whole-map gold. Known masks identify reviewed pixels/classes; other pixels remain unknown. Canonical source/mask validation passed for all eighteen sheets and six selected older auxiliary training sheets. UTC formatting and reviewed positive raster-cap corrections are reversible in annotation-corrections.json; prior freezes are retained.

The initial Africa selection was replaced before predictions because colour/BW editions share an original already used by macro-v6. The previous source freeze is retained as split-freeze.01.json. The replacement South America source and canonical NRCan family are in split-freeze.json. Africa source-only grid controls/fit and partial labels remain outside this eighteen-original cohort under ../development-oracles/nrcan-africa-outline.

A fresh verified public encoder was trained for twelve epochs, with six new training sheets and six older auxiliary sheets. A checkpoint and threshold were frozen before final-test inference. The candidate **failed admission**: international/coast precision, administrative recall, confounder regression and whole-map coverage gates did not pass. The test set is now exposed; do not retune against it or relabel predictions as source truth. The private default remains macro-v6.

The candidate weights remain private outside the public data repository. ONNX/WASM execution parity passed; this is not model-accuracy or historical-accuracy approval. See preparation-status.json and the scoped development integration report for actual metrics and remaining workflow verification.
