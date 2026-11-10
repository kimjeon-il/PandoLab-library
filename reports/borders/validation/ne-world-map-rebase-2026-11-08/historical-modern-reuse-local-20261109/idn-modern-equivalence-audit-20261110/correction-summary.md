# Indonesia modern geometry correction

## Saved corrections
- `36a996c1e596055c4e371b6803b92276252950bc`: the 1975-12-07 through 1999-10-24 version is now the complete approved current IDN + TLS union. All 4,128 IDN and 4 TLS components are covered; the union contains 4,130 polygons. No components were omitted, clipped to NE, rounded, or resimplified. The symmetric difference from the complete donor union is zero. Original occupation/recognition caveats and dates remain.
- `ebae7be60b7b40a00627028ee16841701c3511a6`: the 1945-08-17 through 1963-04-30 version has all 450 explicitly omitted approved donor components restored with exact source coordinates. Every pre-existing historical coordinate remains. The existing West New Guinea exclusion remains.

## Verification
`post-correction-verification.json` rechecks the archived versions: all 450 and 539 prior explicit omissions are fully covered, both versions are valid, and the later version equals the full modern IDN + TLS union exactly. The counts are version-specific: the 450 donor components are a subset of the later version's 539, not 989 different components.

## Remaining limitation
The earlier version is not certified as a complete modern baseline minus West New Guinea. The old source only identifies 25 NE Papua polygons; complete classification of modern components without NE overlap needs additional geographic evidence. No uncertain component is silently removed or assigned.

## Superseded approach
Prior source-only partial coast updates preserved some old NE political display edges and selected donor components through overlap with NE. A display-scale subpixel rule also omitted valid approved donor components. These were not verified simplification errors. The complete later-version correction supersedes that approach, and the earlier-version explicit omissions were restored. Future global retention/omission decisions are separate from this restoration.

All changes are local source/archive changes only. No remote push, deployment or portable package was performed. The earlier audit files remain a before-correction record bound to revision 9be2367b; use the post-correction verification for current restoration status.
