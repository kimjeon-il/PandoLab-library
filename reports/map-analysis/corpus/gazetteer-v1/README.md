# Analysis gazetteer v1

Modern GeoNames cities500 settlements and source-reviewed Pando historical aliases. Search-only data; it does not approve historical city existence, sovereignty or display labels.

Official snapshot: https://download.geonames.org/export/dump/cities500.zip
License: CC BY4.0, https://creativecommons.org/licenses/by/4.0/ . Retain GeoNames attribution.
Original ZIP SHA256: d1e13678275b108d6dd0a5a35dcaee59ca2f0e3f3a6fa56a23c796f497ecebed
Records: 236849; normalized names: 1139860.
Runtime revision: a44261bca491ea878acd95d33d94272d72ade84f9054e1461e53e2d7de977cfe.

Existing approved historical catalog SHA256: d35bd85615fbaf4929da660ba5fc94830e1d7c1520b85d094f8f11c8089d5906. Name normalization affects search keys only; originals and historical timelines remain. Raw data is not independently verified ground truth.

The 4352 runtime shards are hash verified and fetched on demand with a24MiB decoded-byte cache. Compilation and all checks run from the Pando code checkout. No full allCountries audit or app data pin replacement was performed.
