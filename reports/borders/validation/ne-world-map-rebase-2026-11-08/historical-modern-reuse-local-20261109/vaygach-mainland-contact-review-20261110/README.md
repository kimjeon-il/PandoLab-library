# Vaygach plus linked Yugorsky mainland coast

Status: geometry candidate prepared, not applied. Reads pinned to 2af6c0834ac2987a7ffdfe3cde0db1827b04d4e1, with Kolguyev already included. Source writes, commits, runtime changes and remote Git were not performed.

## Finding

Approved donor 1554 is offshore at 60.63547–60.67357 E, 69.69992–69.71039 N. It is about 559 m from approved modern mainland polygon 3289, but overlaps the old historical mainland polygon 6 in all three versions. Donor 1552 touches 1554 at exactly one point; both must remain. These are display-topology observations, not proof of a surveyed physical land bridge. Their individual names were not established.

The old 42-vertex mainland arc is found exactly in reverse orientation in all four original 1922 master/display features. All 42 vertices also match Natural Earth coordinates rounded to six decimals. This is coordinate lineage, not political evidence.

## Complete paired operation

Retain the entire 51-component initial window and additionally donor 1562, which appears along the linked mainland shore. Total: **52 whole modern components**, with no omissions. Replace the matching mainland arc between actual old/modern line intersections (61.69390816458813, 69.76822725873602) and (60.193136184349186, 69.56182045126044). Keep every intervening approved donor vertex, all original coast vertices outside the arc, and all other rings/polygons. The two endpoint segments are split at their actual intersections; no clipping, area subtraction repair, invented bridge, coordinate rounding or simplification is used to generate the candidate.

Three full candidates are valid. Donor/mainland and donor/retained geometry intersections are empty. Independent JavaScript replay agrees with Python geometry assembly. Parent/constituent uses the same scoped coordinates; original vertex offsets differ and are recorded separately. The new local mainland symmetric difference, about 147.732 square km, is a display-source difference, not historical land loss.

- RSFSR reviewed 1922-12-30 through 1925-05-12: old Vaygach index 98; 231→282 components.
- USSR reviewed same dates: old index 102; 235→286.
- USSR Caspian 1925-05-13 through 1929-12-31: old index 138; 299→350.

## Evidence and limits

See historical-and-physical-evidence.json for canonical donor, administration chronology and the explicit 1920/1922 provincial-draft distinction. No title, date, certainty or Arctic exception is changed. The original caveat about individual tiny-islet title remains. Canonical approved donor equality is verified; its underlying raw GPKG was not revalidated.

paired-coast-operation.json is a compact replay instruction, not a source write. candidate-hash-ledger.json records exact full candidate hashes and all 52 donor hashes. candidate-topology-proof.json and original-source-lineage.json contain checks. Visuals have been opened and reviewed. Combined Novaya Zemlya/Vaygach/source-provenance preparation is separate so one standalone patch cannot revert the other.
