import gzip
import hashlib
import json
from pathlib import Path
import urllib.parse
import urllib.request

root = Path(__file__).resolve().parents[2]
target = root / 'tools/historical-library/sources/monaco-reviewed-2026-10-22'
target.mkdir(parents=True, exist_ok=True)
requests = {
    'ign-coast.geojson': 'https://data.geopf.fr/wfs/ows?' + urllib.parse.urlencode({
        'service': 'WFS', 'version': '2.0.0', 'request': 'GetFeature',
        'typenames': 'BDTOPO_V3:limite_terre_mer', 'outputFormat': 'application/json',
        'srsName': 'EPSG:4326', 'bbox': '43.715,7.40,43.755,7.445,urn:ogc:def:crs:EPSG::4326', 'count': 100}),
    'ign-communes.geojson': 'https://data.geopf.fr/wfs/ows?' + urllib.parse.urlencode({
        'service': 'WFS', 'version': '2.0.0', 'request': 'GetFeature',
        'typenames': 'BDTOPO_V3:commune', 'outputFormat': 'application/json',
        'srsName': 'EPSG:4326', 'bbox': '43.72,7.40,43.76,7.44,urn:ogc:def:crs:EPSG::4326', 'count': 30}),
    'cnig-monaco.html.gz': 'https://cnig.gouv.fr/monaco-a25929.html',
    'mareterra-timeline.html.gz': 'https://mareterra.com/en/',
    'bouygues-maritime.html.gz': 'https://www.bouygues-construction.com/en/activities/marine-infrastructure/sea-extension/monaco-offshore-extension',
    'ign-open-data.html.gz': 'https://www.ign.fr/institut/des-donnees-et-logiciels-ouverts-au-service-de-la-nation',
}
manifest = {}
for name, url in requests.items():
    destination = target / name
    if destination.exists():
        raw = destination.read_bytes()
        original = gzip.decompress(raw) if name.endswith('.gz') else raw
    else:
        try:
            original = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'PandoLab GIS source research'}), timeout=40).read()
        except Exception as error:
            if name.endswith('.geojson'):
                raise
            manifest[name] = {'url': url, 'retrieved': '2026-10-22', 'notArchived': str(error)}
            continue
        raw = gzip.compress(original, mtime=0) if name.endswith('.gz') else original
        destination.write_bytes(raw)
    manifest[name] = {'url': url, 'retrieved': '2026-10-22', 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
(target / 'downloads.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print(json.dumps(manifest))
