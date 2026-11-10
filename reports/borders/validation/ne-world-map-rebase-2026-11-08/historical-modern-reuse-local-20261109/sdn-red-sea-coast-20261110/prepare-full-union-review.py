"""Read saved scoped inputs; write research evidence only, never territorial source."""
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pyproj import Transformer
from shapely.geometry import shape, LineString
from shapely.ops import transform, unary_union
from shapely.validation import explain_validity

ROOT = Path(__file__).resolve().parent
read = lambda name: json.loads((ROOT / name).read_text(encoding="utf-8"))
def write(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

inputs = read("modern-union-inputs.json")
peer_inputs = read("scoped-peer-geometries.json")
safe = "--safe" in sys.argv
prefix = "safe-coast" if safe else "full-union"
candidate_file = read("safe-coast-all-sdn-components-candidate.geojson" if safe else "full-modern-union-candidate.geojson")
old_version = inputs["records"]["SDN"]["entity"]["geometryVersions"][0]
sdn_version = inputs["records"]["SDN"]["entity"]["geometryVersions"][-1]
sds_version = inputs["records"]["SDS"]["entity"]["geometryVersions"][-1]
old, sdn, sds, candidate = map(shape, [old_version["geometry"], sdn_version["geometry"], sds_version["geometry"], candidate_file["geometry"]])
union = unary_union([sdn, sds])
expected_candidate = union
if safe:
    a = old_version["geometry"]["coordinates"][0][0]
    b = sdn_version["geometry"]["coordinates"][0][0]
    north = list(LineString(a[222:224]).intersection(LineString(b[939:941])).coords[0])
    south = list(LineString(a[420:422]).intersection(LineString(b[1646:1648])).coords[0])
    replay = {"type": "MultiPolygon", "coordinates": [[a[:223] + [north] + b[940:1647] + [south] + a[421:]], *sdn_version["geometry"]["coordinates"][1:]]}
    expected_candidate = shape(replay)
ne_union = unary_union([shape(f["geometry"]) for f in inputs["naturalEarth"]["features"]])
definition = "+proj=laea +lat_0=12 +lon_0=30 +datum=WGS84 +units=m +no_defs"
project = Transformer.from_crs("EPSG:4326", definition, always_xy=True).transform
projected = lambda g: transform(project, g.segmentize(0.01))
area = lambda g: projected(g).area / 1e6
length = lambda g: projected(g).length / 1000

shared = []
for peer in peer_inputs["peers"]:
    for version in peer["versions"]:
        geometry = shape(version["geometry"])
        donor_contact = unary_union([sdn.boundary.intersection(geometry.boundary), sds.boundary.intersection(geometry.boundary)])
        if safe:
            donor_contact = old.boundary.intersection(geometry.boundary)
        candidate_contact = candidate.boundary.intersection(geometry.boundary)
        mismatch = donor_contact.symmetric_difference(candidate_contact)
        candidate_overlap = candidate.intersection(geometry)
        expected_overlap = (old if safe else union).intersection(geometry)
        shared.append({
            "entityId": peer["entityId"], "versionId": version["versionId"],
            "geometrySha256": version["geometrySha256"],
            "candidateSharedLengthKm": length(candidate_contact),
            "expectedDonorSharedLengthKm": length(donor_contact),
            "sharedBoundaryDifferenceEmpty": mismatch.is_empty,
            "sharedBoundaryDifferenceKm": length(mismatch),
            "candidateOverlapKm2": area(candidate_overlap),
            "candidateOverlapDegrees2": candidate_overlap.area,
            "exactExpectedOverlapPreserved": candidate_overlap.equals(expected_overlap),
            "changedRegionIntersectsPeer": not old.symmetric_difference(candidate).intersection(geometry).is_empty,
            "interpretation": "Current modern reference only; not a reconstructed contemporaneous historical counterpart."
        })

all_inputs = [(name, index, polygon) for name, geometry in [("SDN", sdn), ("SDS", sds)] for index, polygon in enumerate(geometry.geoms)]
if safe:
    all_inputs = [("SDN", index, polygon) for index, polygon in enumerate(sdn.geoms) if index > 0]
component_checks = [{"entity": name, "polygon": index, "covered": candidate.covers(p), "lostAreaKm2": area(p.difference(candidate))} for name, index, p in all_inputs]
assert candidate.is_valid and candidate.equals(expected_candidate)
assert candidate.symmetric_difference(expected_candidate).is_empty
assert old.equals(ne_union)
assert all(row["covered"] for row in component_checks)
assert all(row["exactExpectedOverlapPreserved"] for row in shared)
if safe:
    assert all(row["sharedBoundaryDifferenceEmpty"] for row in shared)
    assert all(not row["changedRegionIntersectsPeer"] for row in shared)
    key = lambda a, b: tuple(sorted([tuple(a), tuple(b)]))
    new_ring = candidate_file["geometry"]["coordinates"][0][0]
    new_edges = {key(a, b) for a, b in zip(new_ring, new_ring[1:])}
    old_ring = old_version["geometry"]["coordinates"][0][0]
    political_preserved = all(key(a, old_ring[i + 1]) in new_edges for i, a in enumerate(old_ring[:-1]) if not 219 <= i <= 429)
    assert political_preserved

projected_boundary = projected(candidate.boundary).wkb
(ROOT / (prefix + "-projected-candidate-boundary.wkb")).write_bytes(projected_boundary)
extent = projected(candidate.union(old)).bounds
padding = 75000
extent = [extent[0] - padding, extent[1] - padding, extent[2] + padding, extent[3] + padding]
scale, dpi = 10000000, 96
metres_per_pixel = scale * 0.0254 / dpi
width_px = (extent[2] - extent[0]) / metres_per_pixel
height_px = (extent[3] - extent[1]) / metres_per_pixel
gap_px, side_px, top_px, bottom_px = 30, 30, 90, 55
fig_width_px = 2 * width_px + gap_px + 2 * side_px
fig_height_px = height_px + top_px + bottom_px
def font(size):
    return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)

figure = Image.new("RGB", (round(fig_width_px), round(fig_height_px)), "white")
fd = ImageDraw.Draw(figure)
fd.text((30, 14), "Sudan: " + ("protected-border Red Sea alternative" if safe else "complete modern-union comparison") + "; not historical-boundary certification", fill="#222222", font=font(19))

def draw(panel, geometry, fill, outline, width=1):
    d = ImageDraw.Draw(panel)
    geometry = projected(geometry)
    parts = list(geometry.geoms) if hasattr(geometry, "geoms") else [geometry]
    xy = lambda ring: [((x - extent[0]) / metres_per_pixel, (extent[3] - y) / metres_per_pixel) for x, y in ring.coords]
    for p in parts:
        if p.geom_type != "Polygon":
            continue
        points = xy(p.exterior)
        if fill is not None:
            d.polygon(points, fill=fill)
        d.line(points, fill=outline, width=width)
        for interior in p.interiors:
            points = xy(interior)
            if fill is not None:
                d.polygon(points, fill="white")
            d.line(points, fill=outline, width=width)

for index in range(2):
    panel = Image.new("RGB", (round(width_px), round(height_px)), "white")
    for peer in peer_inputs["peers"]:
        draw(panel, shape(peer["versions"][-1]["geometry"]), "#f1f3f4", "#b5bbc2")
    if index == 0:
        draw(panel, old, "#e9d6bc", "#8c6135")
    else:
        draw(panel, candidate, "#c5ddec", "#13628a")
        draw(panel, old, None, "#b96343")
    left = round(side_px + index * (width_px + gap_px))
    figure.paste(panel, (left, top_px))
    fd.rectangle((left, top_px, left + round(width_px), top_px + round(height_px)), outline="#999999")
    title = "Existing NE SDN + SDS proxy" if index == 0 else ("Safe coast + all 45 SDN components; old outline in orange" if safe else "Full modern union; original outline in orange")
    fd.text((left, top_px - 30), title, fill="#222222", font=font(16))
fd.text((30, round(fig_height_px) - 44), "Nominal 1:10,000,000 at 96 DPI | LAEA | " + ("All 45 modern SDN non-mainland components retained | Political lines unchanged" if safe else "All 57 inputs retained | 49 union polygons | No omission threshold"), fill="#222222", font=font(14))
fd.text((30, round(fig_height_px) - 23), "Current neighboring references only. Historical disputes and individual microscopic fragments are not visually certified.", fill="#444444", font=font(13))
figure.save(ROOT / (prefix + "-source-scale.png"), dpi=(dpi, dpi))

proof = {
    "schemaVersion": 1, "status": "passed-for-safe-coast-source-change" if safe else "pending-raw-CAF-shared-boundary-diagnostic",
    "sourceRevision": inputs["sourceRevision"], "peerRevision": peer_inputs["sourceRevision"],
    "candidateValid": candidate.is_valid, "validity": explain_validity(candidate),
    "oldEqualsExactNEUnion": old.equals(ne_union),
    "operationReplaySymmetricDifferenceEmpty": candidate.symmetric_difference(expected_candidate).is_empty,
    "donorUnionSymmetricDifferenceEmpty": candidate.symmetric_difference(union).is_empty,
    "fullUnionRequiredForThisAlternative": not safe,
    "allOriginalPoliticalEdgesExact": political_preserved if safe else None,
    "inputComponents": len(all_inputs), "outputComponents": len(candidate.geoms),
    "holes": sum(len(p.interiors) for p in candidate.geoms),
    "all45SdnDetachedComponentsExact": all(any(p.equals(q) for q in candidate.geoms) for p in list(sdn.geoms)[1:]),
    "components": component_checks, "sharedBoundaryAndOverlap": shared,
    "dates": {"validFrom": old_version["validFrom"], "validTo": old_version["validTo"], "nextVersionValidFrom": sdn_version["validFrom"], "sourceHistoricalDatesUnchanged": True, "historicalAccuracyRevalidated": False},
    "projection": {"definition": definition, "units": "metre", "sourceCRS": "EPSG:4326", "measurementDensificationDegrees": 0.01, "densificationChangesSourceOrCandidate": False, "projectedExtent": extent, "projectedBoundarySha256": hashlib.sha256(projected_boundary).hexdigest()},
    "render": {"image": prefix + "-source-scale.png", "nominalScaleDenominator": scale, "dpi": dpi, "mapPanelWidthPixels": width_px, "mapPanelHeightPixels": height_px, "metresPerPixel": metres_per_pixel, "physicalDisplayScaleCalibrated": False},
    "limits": (["Partial improvement only: verified interior Red Sea donor subarc plus every one of the 45 modern SDN non-mainland components; not the full modern SDN+SDS union.", "Original NE political edges, both coastline junctions and all ten old peer intersections/shared boundaries remain unchanged, including pre-existing mismatches with modern neighboring references.", "Historical political attribution and dates are not re-established by coast reuse. Al-Fashaga, CAF and other land-border changes from the full-union alternative are not applied.", "All 45 detached components come from the approved SDN donor and are retained without an omission threshold; donor attribution is not a new period-specific island sovereignty finding.", "No final source application or runtime approval is implied."] if safe else ["This verifies a modern successor-union proxy, not every historical border in 1956–2011.", "Al-Fashaga and other external coordinate changes are not proved to be historically identical lines by matching inclusion conventions.", "The CAF raw strict shared-contact check is unresolved, though exact full-union geometry and donor area preservation pass.", "No final source application or runtime approval is implied."])
}
if safe:
    detached = list(sdn.geoms)[1:]
    proof["all45SdnComponentLocation"] = {
        "aggregateBounds": unary_union(detached).bounds,
        "allStrictlyWithinRedSeaDiagnosticEnvelope": all(p.bounds[0] > 36.5 and p.bounds[2] < 39 and p.bounds[1] > 18 and p.bounds[3] < 22 for p in detached),
        "envelope": [36.5, 18, 39, 22], "donorFeatureId": "SDN", "donorVersionId": sdn_version["versionId"],
        "attribution": "Exact approved SDN donor polygons 1..45, retaining approved source attribution. Envelope confirms location only, not historical sovereignty or a filtering criterion.",
        "noneExcluded": True, "all45ExactEquality": proof["all45SdnDetachedComponentsExact"]
    }
    legacy = []
    for f in read("natural-earth-peer-geometries.json")["features"]:
        peer = shape(f["geometry"])
        before = old.boundary.intersection(peer.boundary)
        after = candidate.boundary.intersection(peer.boundary)
        legacy.append({"id": f["id"], "sharedBoundaryIdentical": before.equals(after), "sharedDifferenceEmpty": before.symmetric_difference(after).is_empty, "originalSharedLengthDegrees": before.length, "overlapIdentical": old.intersection(peer).equals(candidate.intersection(peer))})
    assert all(row["sharedDifferenceEmpty"] and row["overlapIdentical"] for row in legacy)
    proof["legacyNEPeerSharedBoundaryChecks"] = legacy
write(prefix + "-topology-and-projection.json", proof)
print(json.dumps({"mode": prefix, "valid": candidate.is_valid, "expectedOperationEqual": candidate.equals(expected_candidate), "shared": shared, "image": str(ROOT / (prefix + "-source-scale.png"))}))
