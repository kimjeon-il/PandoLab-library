# Remote branches to main — 2026-11-03

Status: historical execution notes. Final integration findings are in result.md; deployment and cleanup evidence are in completion.json.

Baseline remote main: ddf40152876e0f4ac334e3e1e2e35ff9c72f857c.
Selected independent heads: work/ui 0eec519a8, retired-test-fixture-pruning 78568cac3, geometry-delta 0af8b63d2, work/gis 67b9f6c1b. Other remote code refs are covered by ancestry; refresh before push.

Ruling: preserve current map diagnostics, its test helper and three read-only source oracles. The older independent removal branch incorrectly treated these active consumers as retired. Keep its DOM fixture relocation, hover regressions, retirement closure and audit coverage. Keep the UI canonical application catalog because the other branch still reintroduces 34 already-deleted browser entries. Combine workflow coverage and deletion-ledger facts.

Ruling: remove the brittle global test total 877 assertion; newly integrated main already adds four legitimate tests. Preserve the exact 170 retired-suite list, three additional retired comparisons, unique registration, live fixture and workflow assertions. Do not replace the total with a new magic number.

Windows source instrumentation needed LF normalization for three in-memory diagnostic fixture inputs. Reproduced exact-anchor failures; all 49 diagnostic/hover cases pass after normalization. Shipping sources are unchanged by this correction.

Checks so far: R4-B/C 11 cases passed; R4-E3 current inventory 4 passed; combined retirement/catalog closure 20 passed; diagnostics and hover 49 passed. These are affected checks, not a full-suite claim.

Performance A source (pre-delta combined runtime): 488c845ad5eda8c392f186744da0b96e2938802c. Compare with final B using identical final pinned data and hardware conditions. No performance or deployment completion claimed yet.
