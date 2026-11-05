# Three historical representative geometry periods

Status: scoped date update verified locally for work/gis; publication outcome is recorded separately by immutable commit verification.

| Target | Inclusive validFrom | Inclusive validTo | End event (exclusive) | Geometry reference |
| --- | --- | --- | --- | --- |
| state:DEU | 1871-01-01 | 1918-11-08 | 1918-11-09 | 1914-07-31 |
| state:austro-hungarian-empire | 1867-02-17 | 1918-10-30 | 1918-10-31 | 1914-07-28 |
| state:kingdom-of-serbia | 1882-03-06 | 1918-11-30 | 1918-12-01 | 1914-07-28 |

**DEU lifetime remains 1867-07-01 through null.** AH and Serbia lifetimes match their intervals above. AH February 17 selects the dual-government formation stage of the multistage 1867 settlement. Serbia uses Gregorian March 6 (Julian February 22). Ending events start a new identity/regime on that day; the old interval ends the previous day under the inclusive contract.

The 1914 coordinates and original review receipts are preserved verbatim. 국경 변동별 세부 형상은 후속 작업이며, 기준일 대표 형상을 존속기간에 잠정 적용합니다. These are provisional representative displays, not verified unchanged borders throughout the period. Modern coastal proxies and Serbia-Montenegro uncertainty remain.

Validation: 12 targeted tests passed on the candidate and applied files. The same tests detect the baseline one-day limitation (10 expected failures, 2 preservation passes). Checks use the existing C++ exact-date resolver and ordinary monthly loader, and verify 81 protected files plus unchanged unrelated catalog descriptors. No new clipping, source-master edit, neighbor restoration, or neighbor geometry update occurs. The older 12-country/13-day-slice neighbor edits remain unchanged.

Germany’s independent name history is intentionally unchanged because the user requested geometry only. Consequently its empire geometry and name editions do not acquire identical intervals in this change.

No full world generation, full-period exclusivity/topology review, browser UI pass, or complete CI pass is claimed. Full generation would apply existing ownership rules; that behavior is outside this no-clipping change. UI/USSR WIP remains separate. No main integration, deployment, package, or cleanup is performed.

See [validation.json](validation.json) for before/after digests, protected-file hashes, endpoint semantics and exact file scope; [local-plan.json](local-plan.json) records the 12 runtime logical files. Existing immutable base: app `ebc525a87e32808c3bf5f3cb008618a95fb58fba`, data `b6c3c85bba690244829bdec93c58682d9342bda8`.

## Historical date sources

- **state:DEU**: German imperial constitution effective; January 18 was the subsequent symbolic proclamation. Republic proclaimed; the imperial regime ends at the start of this model date. [source 1](https://www.bundestag.de/dokumente/textarchiv/2021/kw11-kalenderblatt-150jahre-reichstag-828278), [source 2](https://www.bundestag.de/en/parliament/history/parliamentarism/empire/empire-200352)
- **state:austro-hungarian-empire**: Formation of the dual government selected as the registration event. The 1867 settlement had several constitutional and legislative stages; this date is a documented modeling choice, not the date of every stage. Dissolution of the dual union; treated as the first date outside the old identity. [source 1](https://universitaetsverlage.eu/bucher-e-books/titel/die-protokolle-des-cisleithanischen-ministerrates-1867-1918-band-i-1867/), [source 2](https://encyclopedia.1914-1918-online.net/article/post-war-turmoil-and-violence-hungary-1-1/)
- **state:kingdom-of-serbia**: Kingdom proclaimed on March 6 Gregorian (February 22 Julian). New South Slav kingdom established; treated as the first date outside the Kingdom of Serbia identity. [source 1](https://nmkv.rs/140-years-since-the-establishment-of-the-kingdom-of-serbia/?lang=en), [source 2](https://www.parlament.gov.rs/national-assembly/history/history-1804---1918.1918.533.html)
