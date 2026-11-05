# CI follow-up: 1914 reference-day hierarchy

This follow-up supersedes the earlier statement that all Prussia compiled descriptors are unchanged. Their source records, original shapes, compiled geometry archives, source bindings and dates remain unchanged. Only two compiled parent relations are now dated 1914-07-31 through 1914-07-31.

## Cause and correction

The registered pin bd62cc8ec6d8221202ed19de0a66f98d3e07ace9 introduced the German Empire outline on 1914-07-31. Existing East and West Prussia library objects have blank source parents. The compiler therefore treated them as peers of Germany, intersected their outlines, unioned the overlaps and subtracted them from Germany. That wrong peer classification reached polygon-clipping's recursive isExteriorRing path and raised RangeError: Maximum call stack size exceeded. Merely applying priority subtraction to provinces instead also produced an invalid degenerate shell. Neither error is swallowed.

Lineage records support successor relations, not administrative inclusion. Source parentEntityId is static. The existing compiled timeline already supports dated parentRelations. The canonical compiler now accepts bounded policy parentRelations, maps source IDs to builtin IDs, and resolves them before parent availability and peer clipping. The scoped publication graph includes the two endpoints and passes only its component's rules. Unknown endpoints, self-links, unbounded or overlapping rules and cycles are rejected.

The two policy entries link state:east-prussia and state:west-prussia to state:DEU only on 1914-07-31. They compile to parentId DEU. This records their inclusion in the selected empire baseline; it does not certify the provincial outlines or rewrite library source parents, source validity, lifetimes, lineage or any coordinate. Geometry validation and numerical error handling are unchanged.

## Exact changes and checks

- Application commit: ebc525a87e32808c3bf5f3cb008618a95fb58fba on work/gis. Changed files: tools/builtin-world-compiler.mjs, tools/build-builtin-world.mjs, tests/unit/historical-world-parent-relations.test.mjs, docs/territorial-source-contract.md, config/library-data.json.
- Paired data commit: b6c3c85bba690244829bdec93c58682d9342bda8 on work/gis, remotely verified. Four logical outputs: two province country payloads, builtin index and historical-world/policy.json. See p2-parent-runtime-plan.json for exact paths, hashes and bytes.
- No source or geometry change. Both province payloads are deep-equal to their prior payload after substituting the original parentRelations array. All other 278 builtin country descriptors are identical. The three registered historical outlines match the pinned geometry objects exactly, so their reviewed shared seams, required islands, fixed anchors and provisional status remain intact.
- The first synthetic regression failed with an empire missing its provincial land before implementation. The affected compiler/territory/timeline tests now pass: 23 tests, zero failures. Lint for both modified tools and the new test passes. The new test also checks rule rejection and scoped dependency/filter behavior.
- The reproducible real-input check reads only the same explicit source identities: old d2c02308 has 15 and passes; registered bd62cc8e has 17 and reproduces the stack overflow; fixed b6c3c85b has 17 and passes. Run: node reproduce-1914-p2.mjs <Pando-root> <library-Git-checkout>. See p2-three-pin-regression.json.
- The actual source and compiled coordinates for Germany, Austria-Hungary, Serbia and both provinces match the registered pin at their reference dates. Province parents and geometry match outside the changed day, including July 30, August 1 and the modern date. C++ timeline adapter checks passed for 1914-06, 1914-07, 1914-08 and 2026-11; July selects the existing DEU parent for both provinces. See p2-parent-preservation-proof.json.
- Remote archive comparison confirms exactly the four planned logical changes. The five source descriptors, including both Prussias, are unchanged. See p2-parent-remote-proof.json.

## Separate pre-existing CI failures

1. Residual dependency contracts: the unchanged runtime-materialization fixture lacks territorial generated/v2/index.json. The same single test fails with ENOENT on both the old application 3be531e2 and registered d3a24158 module. The unchanged historical storage preflight unconditionally reads that source index during builtin storage. See residual-baseline-reproduction.json and both logs. This follow-up does not alter that fixture or storage path.
2. Hydro live-cutover: the unchanged workflow hardcodes pin 91c127ddbae902405de6e35b38940a59a8c0d021. The before, registered and fixed pins all fail that guard. Hydro v0.13.4 manifest and hydro.bin hashes are equal before and after registration. No Hydro code or data is changed.
3. 2000–2026 display: the unchanged test expects landRevision a627e16f..., while the actual shared physical timeline selection is 66fa6cbb.... The physical manifest bytes are identical in the before, registered and fixed pins. The real selector at 1922-12-31 resolves that same 66fa6cbb... revision in all three. The earlier CI had passed physical.frame.matches before failing the stale literal. No browser oracle or physical data is changed, and this follow-up does not claim a local browser rerun.

4. Builtin country publication contracts (exact commit run 42012652728): 40/41 pass. The deterministic/stale-output test fails at the existing historical display gate for state:changing/before. The same single test was run against extracted prior d3a24158 builder/compiler/gate modules and current ebc525a87 modules; both fail identically. The test, synthetic fixture, helper and gate have identical normalized source hashes. Only import paths and fresh fixture retention were adapted in the copies; no assertions or gate were weakened. See publication-baseline-reproduction.json and both logs. No application fix is made for this separate fixture/gate mismatch.

## Remaining limits

German Empire remains a 1914-07-31 single-day provisional reconstruction; Austria-Hungary and Serbia remain 1914-07-28 single-day reconstructions. Modern coastal proxies, the Helgoland/Dune proxy and Serbia–Montenegro detailed-map uncertainty remain documented. The month-end viewer limitation for the July 28 snapshots is unchanged. Province geometry accuracy is not promoted by the new parent relation.

## Final P2 result and protected scope

The exact application commit's [P2 run](https://github.com/kimjeon-il/Pando/actions/runs/42012652702) completed with failure. It passed plan and reached writeBuiltinWorldPublication after catalog compilation; the original German/Prussia stack overflow is absent. The remaining failure is: Historical display review required: state:soviet-union/state:soviet-union:1922-12-30-reviewed-v2: missing or unresolved review. See p2-fixed-commit-failure.log. This is not a P2 pass claim.

The named USSR raw source SHA is 7d28467b07fc933b9421e57216cb002e8a4df16fa5d61973b254789923f15b8a and existing compiled payload SHA is b243f8b7fd9e6014725865fd6e017f907b5558e59e0f04fd65f85d3b7f89c258 at all three pins (before, registered and fixed). The source contains an existing passed source review, but the newly generated compiled binding has no matching resolved derivative review at the writer gate. Merely having a source review is not proof that every regenerated derivative is approved. Exact baseline full generation was not run, so this report does not claim such a run reproduced the USSR failure. The new parent policy is bounded to 1914-07-31; the USSR version starts in 1922. No USSR source, compiled payload, review, policy or gate is changed to bypass this out-of-scope failure. See p2-ussr-input-comparison.json.

Final remote app remains ebc525a87e32808c3bf5f3cb008618a95fb58fba and data remains b6c3c85bba690244829bdec93c58682d9342bda8. P2 did not publish a replacement result. Exact-commit P1, P3, P4 and German source-readiness workflows succeeded; P2, publication contracts, Hydro and the 2000–2026 display workflow failed. The older residual failure is separately baseline-reproduced and was not rerun in this exact commit's workflow set. Full observed statuses are in p2-follow-up-result.json.

No application main merge, deployment, portable package, local whole-world regeneration or task temporary-file deletion was performed. GitHub's existing P2 workflow attempted its normal full generation and stopped at the unchanged review gate before publication.
