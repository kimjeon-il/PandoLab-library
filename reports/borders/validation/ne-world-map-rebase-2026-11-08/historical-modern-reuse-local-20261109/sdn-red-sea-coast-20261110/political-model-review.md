# Sudan 1956–2011: complete modern-union model review

Date: 2026-11-10. Status: research candidate only; no territorial source applied or committed.

Pinned library revision: `0e49cfeeb54ee83afb7671e9d56f11d5f400f380`.

## Decision

The complete approved-modern SDN + SDS union is an appropriate candidate **for replacing the existing modern-successor-union proxy with its approved modern source equivalent**. It is **not** proof of a historically accurate exterior throughout 1956-01-01 to 2011-07-08.

The existing historical geometry is spatially identical to the Natural Earth SDN + SDS union: its symmetric difference is zero. Its original notes explicitly describe a reference reconstruction from current SDN and SDS. There is no independently established historical coastline or political-border master in this version that would justify protecting the old NE coordinates merely because they are currently stored in a historical version.

Therefore a partial coastline splice cannot be described as completion of a whole-source-model update. A full modern-union proxy must retain every approved donor component and every inherited political exception. A separately labeled protected-border partial alternative is now prepared as a lower-risk first step: it changes only the common Red Sea coast and includes all 45 approved SDN non-mainland components. If historical administration or control is reconstructed, the external-boundary exceptions below require their own evidence and, where needed, dated counterpart geometries. They must not be silently resolved by either the old NE or new modern union.

**Direct model-comparison conclusion:** The checked major inclusion choices do not switch between the old and new unions. Halaib and Bir Tawil remain excluded under the respective current-source convention; Abyei, Heglig and Kafia Kingi remain within united Sudan. Historical changes in control are therefore caveats on both proxy models, not by themselves a reason to block replacing the old modern proxy with the complete approved modern proxy. Individual contested boundary contours remain unverified as historical reconstructions.

## Direct old/new political-inclusion comparison

These checks are saved in `political-inclusion-comparison.json`. Coordinates below are diagnostic probes, not reconstructed disputed boundaries.

| Subject | Old NE successor union | Complete approved-modern union | What the comparison establishes |
| --- | --- | --- | --- |
| Halaib interior [36.5, 22.4] | Excluded | Excluded | No wholesale assignment switch. In the encompassing north-of-22° box [34,22,38,24], the only new inclusion is a 0.1281 km² ribbon reaching about 22.000008°, not inclusion of the triangle. It is retained, not threshold-filtered. |
| Bir Tawil interior [33.75,21.85] | Excluded | Excluded | Old union excludes the entire NE BRT polygon; modern union excludes the entire modern BRT polygon. Comparing cross-edition boundaries gives 66.1726 km² of the NE BRT mask within the modern union and 1.9145 km² of the modern BRT mask within the old union. This is a differing BRT outline, not annexation of the roughly 2,000 km² unit. |
| Abyei box [27.5,8.8,30,10.7] | Fully included | Fully included | The full diagnostic box has symmetric difference exactly zero. |
| Kafia Kingi interior box [24.3,9,25.2,10] | Fully included | Fully included | Symmetric difference exactly zero. The broader box [23.4,8.2,25.5,10.5] has 766.7887 km² of boundary differences, all inside the union of the old and modern CAR polygons. None is an interior north–south exclusion. |
| Heglig probe [29.4,10] | Included | Included | No point-level switch; internal north–south division disappears in the union. |
| Ilemi probe [35,4.7] | Excluded | Excluded | Central probe convention unchanged. An explicitly limited diagnostic box has 2.1137 km² of contour difference; no exact legal Ilemi polygon was reconstructed. |
| al-Fashaga probes [36,14] and [36.3,14] | Both included | Both included | No switch at these probes. The broader diagnostic extent has 641.2982 km² of contour difference, including a new-inclusion probe near [36.398434,13.627645]. Its relationship to specific historical demarcation choices was not established. |

The presence of boundary-coordinate differences must not be reported as unchanged geometry. Conversely, geometric differences alone do not prove that the source changed from one historical ownership policy to another. The file records both facts separately. No exact original NE segment has been demonstrated to be an independently verified historical line that must replace the approved modern proxy in this source-model update.

## What the stored source actually says

- Entity: `state:SDN`; lifetime begins 1956-01-01 and remains open.
- Historical version: `state:sudan:1956-2011-r1`, inclusive dates 1956-01-01 through 2011-07-08, certainty `medium`, source `natural-earth-5.1.1-historical-successor-union`.
- Original note: `현재 SDN과 SDS를 합쳐 남수단 독립 전 수단의 외곽선을 재구성한 참고 경계입니다.`
- Original recipe members: SDN and SDS. Original metadata describes an approximate geometry with reference date `2010`; that label is not an independent period survey.
- Post-secession SDN and independent SDS start 2011-07-09. Both current versions are explicitly low-certainty modern-outline proxies. Their notes do not claim to resolve Abyei or every disputed border for the start date.
- Current SDN and SDS each equal their exact archived approved-modern donor geometry. These and all ten scoped neighboring sources are unchanged from the earlier 9be2367b preparation.
- Current approved-donor provenance expressly preserves the existing SDN Kafia Kingi attribution through a localized prior-ownership intersection. It is a composite prepared source, not a claim that every boundary is an unmodified State Department line.

Independence/secession dates are independently supported by the [US Office of the Historian, Sudan](https://history.state.gov/countries/sudan) and [UN South Sudan member information](https://www.un.org/en/about-us/member-states/south-sudan). This establishes the event dates, not the accuracy of all polygon edges.

## Complete-component and topology results

- Inputs: 46 SDN polygons and 11 SDS polygons, with no area overlap between the two modern inputs.
- Complete union: 49 polygons, valid geometry, no interior holes. All 57 input components are covered with zero lost area. The reduction in polygon count is joining touching north/south components, not filtering.
- Every one of the 45 non-mainland SDN components remains an equal-shaped output polygon. All SDS components remain covered; SDS components 0, 9 and 10 remain separate, while components 1–8 join the united mainland.
- No minimum area, width, vertex count or island-omission criterion was used.
- Scoped overlap with EGY, BRT, KEN, ETH, ERI, TCD, LBY, UGA and COD is zero. CAF has approximately 0.0000243 km² of existing donor alignment residual; it is not clipped or repaired by this candidate.
- The old-to-new difference is approximately 6,154.99 km² added and 6,857.19 km² removed, spread along many outer boundary/coast segments. These are source/cartographic differences, **not measured historical territorial transfers**.
- Area calculations use LAEA after densifying the geographic segments for measurement only. Stored source and candidate coordinates are not densified, rounded or simplified. Bounding-box regional summaries are not disputed-area polygons.

The complete union geometry digest, using `sha256(JSON.stringify([type, coordinates]))`, is `40739d91159df176657541905f7a5a2b9c9c8561196e20d3b9285fa31406cacf`.

## Political and temporal exceptions

### Halaib and Bir Tawil

The contemporary [US Department of State International Boundary Study 18, 27 July 1962](https://library.law.fsu.edu/Digital-Collections/LimitsinSeas/pdf/ibs018.pdf), pp. 2–4, distinguishes the 22° international line from administrative arrangements: Sudan administered the northeastern area north of 22°, while Egypt administered the paired area to the south. Both the old NE union and new approved-modern union exclude an interior Halaib probe and an interior Bir Tawil probe. Accordingly, preserving the old geometry does not solve this historical-administration mismatch.

The [Halaib legal chronology with linked UN submissions](https://www.egypil.org/article/75) records Sudan's 20 February 1958 complaint about Egypt's 1 February 1958 note, conflicting positions in 1992–95, and reported final Sudanese troop withdrawal in January 2000. No exact day for that withdrawal was verified. Egyptian control and Sudanese claims must not be conflated with an agreed sovereignty transfer.

For a modern proxy, preserve the donor's existing interpretation and mark the historical limitation. For a historical administration/control model, Halaib requires a dated Sudanese-administered extent and corresponding Egyptian version; do not use the complete modern exclusion throughout 1956–2011 as verified history. Bir Tawil must follow the same stated boundary convention; do not invent a new allocation merely to fill a gap.

### Wadi Halfa salient

The 1962 State Department study identifies a Sudanese salient north of 22°, transferred by a 26 March 1899 decree. Modern reservoir inundation by itself is not evidence of a later sovereign cession. Both evaluated geometries retain a salient north of 22° near Wadi Halfa; the modern candidate does not simply erase it. Their local shapes differ, however. In the diagnostic extent [31, 22, 31.7, 22.3], old/new areas are about 380.61/221.25 km². This comparison does not establish which historical shoreline or territorial line is correct. Do not present it as a verified transfer, and do not infer that the old NE line is the original 1956 shoreline.

### Ethiopia, al-Fashaga and the Eritrea junction

The [UN-published Eritrea–Ethiopia Boundary Commission award, 13 April 2002](https://legal.un.org/riaa/cases/vol_XXV/83-195.pdf), paragraphs 5.9–5.12, documents Ethiopia's acceptance through notes dated 18 July 1972 of earlier demarcation near the Sudan tripoint. The tripoint opposite Khor Royan originated in the 1903 demarcation. Recognition in 1972 is not by itself evidence that a new physical line appeared that day.

An [Ethiopian official statement](https://www.ena.et/web/eng/w/en_21667) describes the 1972 notes as rectifying the line south of Mount Dagleish to hill crests rather than bases and leaving northern settlement/cultivation issues for further resolution. This is a party's account. The exact implemented pre-/post-1972 geometry was not verified here, so no boundary-change polygon or date split has been manufactured.

The [International Crisis Group border briefing, 24 June 2021](https://www.ecoi.net/en/file/local/2054434/b173-ethiopia-sudan-border.pdf) distinguishes the late-2020 military takeover from prior land-use arrangements. A 2020 control pattern cannot be projected backward to the requested period. Any model intended to show effective control must separate this question from recognized/claimed international delimitation. Eritrea's emergence changes the adjacent entity identity, not automatically Sudan's external route.

### Ilemi

Ilemi is an external issue, not a north–south internal line that disappears by union. [Robert O. Collins, “The Ilemi Triangle”](https://www.persee.fr/doc/ethio_0066-2127_2004_num_20_1_1065?pageId=T1_7) and a [University of Nairobi boundary-law study](https://erepository.uonbi.ac.ke/items/b45e9c70-5a83-4928-a245-446898de3be0) distinguish the recognized 1914 boundary from Kenyan administration. No verified post-1956 cession treaty or exact change-of-control day was established in this investigation. Follow an explicit legal/claim/control convention; neither modern donor inclusion nor legacy NE exclusion alone settles historical title.

### Abyei, Kafia Kingi and other internal north–south disputes

The [22 July 2009 Abyei arbitration](https://legal.un.org/riaa/cases/vol_XXX/145-416.pdf) concerned an internal area of united Sudan. Kafia Kingi's north–south administrative history is likewise distinct from the country's external border; see the [Small Arms Survey north–south border study](https://www.smallarmssurvey.org/sites/default/files/resources/HSBA-WP30-North-South-Border.pdf).

The modern union has no interior holes. An Abyei diagnostic box is identical between old and new unions, and illustrative Abyei/Kafia Kingi interior probes are included in both. These checks and the source provenance show that dissolution does not delete those internal areas. The broad Kafia Kingi screening box also crosses the external CAR frontier: differences in that box must not be mislabeled as a north–south loss.

### Other external sections

No verified major post-1956 sovereign transfer was identified on the Libya, Chad, CAR or Congo sections in this bounded review. That is not proof that every modern vertex is a period measurement. [State Department study 16 on the CAR–Sudan border](https://library.law.fsu.edu/Digital-Collections/LimitsinSeas/pdf/ibs016.pdf) and [research on the Uganda–South Sudan border](https://academic.oup.com/past/article/248/1/209/5870984) are contextual sources, not independently reconstructed candidate arcs.

## Required handling if work continues

1. Keep the full candidate and every donor component. Do not return to arbitrary interior coastline fragments as the final modern-equivalent model.
2. Treat adoption, if later authorized, as a modern proxy source replacement. Preserve entity identity, 1956-01-01..2011-07-08 dates, original recipe/provenance and explicit uncertainty. Do not relabel it historically verified.
3. If historical administrative/control differences are reconstructed, create evidence-based exceptions or dated versions with counterpart handling, especially Halaib/Egypt. No exact old NE span was established here as an independently verified historical boundary.
4. Both alternatives have now received a saved nominal-scale visual comparison. The protected-border partial alternative passes the scoped source gate and codec roundtrip. The full-union alternative remains explicitly unresolved and is rejected by the gate while its review status is pending. Source application remains pending. No app/runtime build, packaging, push or deployment was performed.

## Prepared patch status and gate meaning

The source gate is a pure input-bound receipt validator. It checks version identity, dates, geometry digest, required evidence, review status and counterpart references. It has no blanket ban on a full modern union, but it does not establish historical correctness or grant permission to apply a source patch. Review flags must reflect actual checks.

- **Protected-border Red Sea alternative:** `safe-coast-canonical-source-patch.json` is ready for parent pre-application review. It preserves every original political edge, the old Egypt/Halaib and Eritrea junctions, all ten NE peer shared boundaries, and all old intersections/shared contacts with the ten current neighbors. Its changed area has no intersection with those current neighbors. It reuses the exact donor interior coast and every polygon 1–45 of the approved SDN donor. Those 45 polygons have aggregate bounds [36.9153939,18.0627717,38.7953048,21.6117387], wholly in the Red Sea diagnostic envelope. There is no component-size or visibility exclusion. This is a partial improvement, **not** full-modern-union equality. The three separate SDS land-boundary fragments belong only to the complete-union alternative; they are not omitted from that alternative or transferred into this coast-only operation.
- **Complete modern-union alternative:** `full-union-canonical-source-patch.json` is held. It still equals the complete modern donor union and retains all 57 input components. Raw strict CAF shared-contact intersection results differ by about 4.94 km after union noding, even though the disputed line set lies on the resulting boundary and the native overlap is only 1.2341e-17 square degrees. An attempted diagnostic-only 1e-9-degree grid did not establish equal contact sets. The issue is recorded without modifying coordinates or claiming a pass. Historical uncertainty over exterior differences, including al-Fashaga and the CAF section, remains separate.
- **Actual gate result:** the protected-border candidate checks one changed historical version successfully; its codec roundtrip, unchanged post-2011 version, original notes/certainty/dates/lifetime and original provenance preservation pass. The complete-union candidate has a deliberately pending review and receives the expected `missing or unresolved review` rejection. Its codec roundtrip passes, which does not override that gate rejection.
- **Application sequencing:** no canonical source has been written. A fresh source and peer preimage check is required after the preceding Iran commit and before any authorized Sudan source application.

## Saved local artifacts

- `modern-union-inputs.json`: exact scoped inputs and neighboring immutable-source references.
- `full-modern-union-candidate.geojson`: complete 49-polygon research candidate.
- `full-union-investigation.json`: quantitative checks, component correspondence and model decision.
- `saved-union-artifacts.json`: byte sizes, hashes and parsed read-back receipts.
- `saved-input-replay-verification.json`: independent replay from the saved UTF-8 inputs; candidate equality, validity, 49 components, all 57 inputs covered and all 45 SDN components retained.
- `political-inclusion-comparison.json`: explicit diagnostic masks, point inclusion and regional symmetric differences.
- `modern-donor-attribution-evidence.json`: scoped immutable provenance, including the retained Kafia Kingi attribution.
- `source-preparation.json`: earlier coastline-only work, retained as superseded research evidence.

These are local research originals in the existing Sudan investigation folder. They are not archived/published report completion or source application.
