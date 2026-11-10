# Partial frontier migration proposal

Source pin: 85464e0ba06fe43a0e67c9095807d260e5c5ecef.

All five frontier pairs fail raw/current compatibility in both directions. Raw/raw and current/current positive-area overlaps are zero in each scoped region. These are directly measured precision seams, not proof of a sovereignty change. The six selected base raw rows have null Map_Disp and Show_Disp; this does not erase disputes elsewhere or authorize whole-country substitutions.

Keep the existing CHN northern replacement/Spratly allocation and VNM Spratly allocation intact. No inference is made about other disputed components, historic dates or legal sovereignty. None of the five pairs is ready for whole-country raw replacement against an unchanged neighbor.

Smallest bounded next candidate experiment: MMR + BGD shared-arc migration only. Exact shared raw/current boundary contains three coincident segments, total length 0.08483646358627725 geographic degrees. Six segment endpoints were independently located as exact stored vertices on all four source exterior rings, with no snapping. See MMR-BGD-exact-anchor-feasibility.json for coordinates, polygon/ring/vertex indices and hashes in anchor-input-proofs.json.

Useful pair of existing anchors:
A = [92.17254610000003,21.17045920000004]
B = [92.65221860000008,21.279229000000043]
Raw MMR polygon 1035 ring 0 vertices 324964..326898.
Raw BGD polygon 345 ring 0 vertices 231280..229346 (reverse direction).
Current MMR polygon 469 ring 0 vertices 10237..10317.
Current BGD polygon 186 ring 0 vertices 6240..6160 (reverse direction).

Proposed candidate-only procedure:
1. Prove that these two raw subchains are byte-identical in reverse orientation and that the current subchains likewise represent the same shared boundary. Check path ordering and no branch/third-party junction inside the selected segment.
2. Replace ONLY the current two shared subchains with the exact original raw chain, reversing orientation on the counterpart. Preserve all other ring coordinates, holes, islands, political supplements, parents, dates, historic versions and metadata. No buffer cut, simplification, union, invented connector or coordinate rounding.
3. Validate candidate rings and full source geometry; test no pair overlap/gap in the changed-area corridor; prove outside-arc coordinates and all unselected components byte-identical. Check directly touching third-party raw/current features in the changed region.
4. If those proofs pass, parent may review a two-country partial-boundary candidate. Record partial progress explicitly: neither whole country is all-raw complete. Do not increment the completed all-raw-country counter for this partial adoption.

This folder is evidence and proposal only. No candidate geometry export or canonical source write was performed. The polygon-vs-multipolygon clipping helper was corrected after an initial LAO check failed; final results include both types without modifying or repairing source geometry.
