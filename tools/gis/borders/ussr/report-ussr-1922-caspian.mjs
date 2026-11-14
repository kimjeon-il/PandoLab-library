#!/usr/bin/env node
/** Condense verified 1922 Soviet/Caspian receipts without rewriting source
 * archives, historic maps, sovereign polygons or pinned application data.
 * Archived report claims are evidence of an older publication, NOT a new
 * approval of the differences measured by current native GEOS audits.
 */
import {createHash} from 'node:crypto';
import {readFileSync,mkdirSync,writeFileSync,existsSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {fileURLToPath} from 'node:url';
import {FOUNDER_IDS,USSR_ZIP_SHA} from './replay-ussr-1922-countries.mjs';
import {ARCHIVE_SHA} from '../../hydro/verify-approved-caspian-network.mjs';
import {validatePhysicalMetrics} from './replay-ussr-1922-physical.mjs';
import {APPROVED_DATA_PIN,approvedReportReceiptsMatch} from './audit-ussr-1922-approved-followups.mjs';

export const ROOT=process.env.PANDO_CONSUMER_ROOT;
export const ARCHIVE_BASE='reports/borders/reconstruction/ussr-1922-caspian-application-2026-10-24/';
export const ARCHIVED=Object.freeze({
  'application-proof.json':{sha256:'6948649a0ba4be6201552b75f2cbec1f88b7f696bf5c7f88eff34d10d744b8b4',bytes:2655},
  'caspian-comparison-10m.png':{sha256:'a4b30417e8cd2f809e26800470184fa81b16dba2a55ab296c43eda2fc1178626',bytes:33142},
  'app1922.png':{sha256:'c561d7e37bde8d6a57d123da4e8e56c578888934871d9212db86bf434e6961ed',bytes:138526},
  'web1922.png':{sha256:'98c0d863db8c8c60fa538db1706e0b598ac7bb7245aa0dd19a5c5b0e8bbc93e0',bytes:629391},
});
const requireValue=(condition,message)=>{if(!condition)throw Error(message);};
const sha256=bytes=>createHash('sha256').update(bytes).digest('hex');
const MAGIC=Buffer.from([137,80,78,71,13,10,26,10]);

export function parseReceipt(source,prefix){
  const found=source.split(/\r?\n/).filter(line=>line.startsWith(prefix+'='));
  requireValue(found.length===1,'Expected exactly one receipt: '+prefix);
  return JSON.parse(found[0].slice(prefix.length+1));
}
export function validateReceipts({countries,network,display,physical,corrections=null}){
  requireValue(countries?.schema==='pando-ussr-1922-sources-verified-audit-v1'
    &&countries.zipSha256===USSR_ZIP_SHA &&countries.evidenceComputed===true
    &&countries.libraryDataMutated===false
    &&countries.automaticSourceReplacementApproved===false
    &&countries.founders===5 &&countries.entities?.length===5,
    'Country receipt is missing a frozen five-founder native audit');
  const ids=countries.entities.map(row=>row.entityId);
  requireValue(ids.length===new Set(ids).size
    &&FOUNDER_IDS.every(id=>ids.includes(id)),'Reviewed Soviet founder identities changed');
  const differences=countries.entities.filter(row=>
    row.geosTopologicalEquals!==true ||row.suitableForAutomaticReapplication!==true);
  requireValue(differences.length===countries.nonEquivalentFounders
    &&countries.status===(differences.length?
      'source-geometry-difference-blocked':'same-geometry-proven')
    &&countries.entities.every(row=>Number.isFinite(row.areaDifferenceSquareDegrees)
      &&row.areaDifferenceSquareDegrees>=0 &&Number.isFinite(row.boundaryHausdorffDegrees)),
    'Country source audit contains inconsistent discrepancy evidence');
  requireValue(network?.schema==='pando-c1-approved-1922-caspian-network-v1'
    &&network.archiveSha256===ARCHIVE_SHA &&network.featureCount===266
    &&network.nonEndpointCrossings===0 &&network.topologyVerified===true
    &&network.sourceBytesUnchanged===true
    &&network.historicalAreaOrSovereigntyApproved===false,
    '266-reach source network evidence differs from its immutable receipt');
  requireValue(display?.schema==='pando-approved-caspian-display-native-candidate-v1'
    &&display.original?.archiveSha256===ARCHIVE_SHA
    &&display.original?.networkFeatures===266
    &&display.original?.waterHoles===68
    &&display.metrics?.holesBefore===68 &&display.metrics?.holesAfter===68
    &&display.metrics?.nonEndpointIntersections===0
    &&display.status==='review-only-not-approved-for-runtime'
    &&display.sourceZipUnchanged===true,
    'Historical water display was not approved as a review-only candidate');
  requireValue(physical?.schema==='pando-1922-caspian-physical-replay-v1'
    &&physical.referenceDate==='1922-12-30'
    &&physical.validFrom==='1922-12-30'&&physical.validTo==='1925-05-12'
    &&physical.modernPhysicalLandUnchanged===true
    &&physical.publishedHistoricalAssetsUnchanged===true
    &&physical.runtimePromoted===false,
    'Historical physical asset publication semantics have changed');
  validatePhysicalMetrics(physical.metrics);
  requireValue(physical.publishedGeometryDifferenceSquareDegrees<=1e-12,
    'Physical source comparison did not establish equality');
  if(corrections!==null){
    const approved=new Map(corrections?.entities?.map(row=>[row.entityId,row]));
    requireValue(corrections.schema==='pando-ussr-1922-approved-descendant-audit-v1'
      &&corrections.status==='approved-followups-verified'
      &&corrections.pinnedDataRevision===APPROVED_DATA_PIN
      &&corrections.canonicalPublishedVersionVerified===true
      &&corrections.originalZipWasNotOverwritten===true
      &&corrections.sourceObjectsMutated===false
      &&corrections.runtimePromotionPerformed===false
      &&corrections.correctedFounders===5 &&corrections.unchangedFounders===0
      &&approved.size===5
      &&corrections.parentRepublicPartition?.passed===true
      &&corrections.parentRepublicPartition.founderCount===5
      &&approvedReportReceiptsMatch(corrections.verifiedReportReceipts)
      &&differences.length===5
      &&countries.entities.every(row=>{
        const proof=approved.get(row.entityId);
        return proof?.sourceGeometryVerified===true
          &&proof.approvedCorrection===(row.geosTopologicalEquals!==true)
          &&proof.validFrom==='1922-12-30'
          &&proof.validTo==='1925-05-12';
      }),
      'Post-ZIP Soviet corrections must have five fully verified canonical geometries');
  }
  return differences;
}
export async function verifyArchivedReports(index,revision,readOriginal,expected=ARCHIVED){
  requireValue(/^[0-9a-f]{40}$/.test(revision),
    'Pinned library revision must be immutable');
  requireValue(index?.files &&typeof index.files==='object',
    'Historical evidence archive index unavailable');
  const records=[];
  for(const [file,receipt] of Object.entries(expected)){
    const logical=ARCHIVE_BASE+file,entry=index.files[logical];
    requireValue(entry?.sha256===receipt.sha256 &&entry.bytes===receipt.bytes
      &&entry.encoding==='identity'
      &&entry.stored===logical,'Original report/map archive receipt differs: '+logical);
    const bytes=Buffer.from(await readOriginal(entry.stored));
    requireValue(bytes.length===receipt.bytes &&sha256(bytes)===receipt.sha256,
      'Archived 1922 report/map failed SHA-256: '+logical);
    if(file.endsWith('.png'))
      requireValue(bytes.subarray(0,8).equals(MAGIC),
        'Archived 1922 map no longer contains a PNG signature: '+logical);
    records.push({path:logical,sha256:receipt.sha256,bytes:receipt.bytes,
      url:'https://github.com/kimjeon-il/PandoLab-library-data/blob/'+revision+'/'+logical});
  }
  return records;
}
export function buildCompactReport(receipts,archive){
  const discrepancies=validateReceipts(receipts);
  requireValue(Array.isArray(archive)&&archive.length===Object.keys(ARCHIVED).length
    &&ARCHIVED['app1922.png'].sha256===archive.find(x=>x.path.endsWith('/app1922.png'))?.sha256,
    'Required archived 1922 reference maps are missing');
  const {countries,network,display,physical,corrections=null}=receipts;
  const result={
    schema:'pando-ussr-1922-caspian-compact-evidence-v1',
    referenceDate:'1922-12-30',geometryDisplayValidUntil:'1925-05-12',
    interpretation:'provisional 1922 boundary and physical-water presentation only',
    nativeEvidenceVerified:true,allHistoricalBorderReplacementsApproved:false,
    automaticSourceReplacementApproved:false,runtimePromoted:false,
    publishedLibraryMutated:false,
    countries:{founders:countries.founders,
      topologicalDiscrepancies:discrepancies.map(row=>({
        id:row.entityId,areaDifferenceSquareDegrees:row.areaDifferenceSquareDegrees,
        boundaryHausdorffDegrees:row.boundaryHausdorffDegrees})),
      status:corrections?'approved-followups-verified':countries.status,
      unresolvedCanonicalGeometryIssues:corrections?0:discrepancies.length,
      approvedFollowupCorrectionCount:corrections?.correctedFounders??0,
      latestPartition:corrections?.parentRepublicPartition??null,
      correctionSequence:corrections?.correctionSequence??[],
      sourceZipSha256:countries.zipSha256},
    caspian:{approvedNetworkReaches:network.featureCount,
      approvedNetworkZipSha256:network.archiveSha256,
      historicalWaterHoles:display.metrics.holesAfter,
      displayVerticesBefore:display.metrics.verticesBefore,
      displayVerticesAfter:display.metrics.verticesAfter,
      physicalPublishedSymmetricDifferenceSquareDegrees:
        physical.metrics.publishedSymmetricDifferenceSquareDegrees,
      physicalOutsideWindowDifferenceSquareDegrees:
        physical.metrics.outsideRegionDifferenceSquareDegrees,
      preexistingGlobalInvalidityPreserved:
        physical.metrics.preexistingGlobalInvalidityPreserved===true,
      unchangedFarPolygonCount:physical.metrics.unchangedFarPolygonCount},
    archivedOriginals:archive,
  };
  return {json:result};
}
const fetchPinned=async(url)=>{
  const response=await fetch(url,{signal:AbortSignal.timeout(120000)});
  requireValue(response.ok,'Pinned historical evidence download failed HTTP '+response.status);
  return Buffer.from(await response.arrayBuffer());
};
export async function main(args=process.argv.slice(2),{
  fetchArchive=fetchPinned,
}={}){
  const names=new Map();
  for(let i=0;i<args.length;i+=2){
    requireValue(args[i]?.startsWith('--')&&args[i+1]&&!names.has(args[i]),
      'Usage: --countries JSONL --network JSONL --display JSONL --physical JSONL --report-directory NEW_DIR');
    names.set(args[i],args[i+1]);
  }
  for(const key of ['--countries','--network','--display','--physical','--corrections','--report-directory'])
    requireValue(names.has(key),'Missing historical report argument '+key);
  requireValue(names.size===6,'Unexpected historical report argument');
  const config=JSON.parse(readFileSync(join(ROOT,'config/library-data.json'),'utf8'));
  requireValue(config.repository==='kimjeon-il/PandoLab-library-data'
    &&/^[a-f0-9]{40}$/.test(config.revision),
    'Unpinned library data or unexpected report evidence owner');
  const base='https://raw.githubusercontent.com/'+config.repository+'/'+config.revision+'/';
  const evidence=JSON.parse((await fetchArchive(base+'archive/index.json')).toString('utf8'));
  const originals=await verifyArchivedReports(evidence,config.revision,
    path=>fetchArchive(base+path));
  const read=(flag,prefix)=>parseReceipt(readFileSync(resolve(names.get(flag)),'utf8'),prefix);
  const report=buildCompactReport({
    countries:read('--countries','USSR_1922_SOURCE_GEOMETRY_AUDIT'),
    network:read('--network','CASPIAN_1922_NATIVE_NETWORK_PARITY'),
    display:read('--display','CASPIAN_1922_NATIVE_DISPLAY'),
    physical:read('--physical','USSR_1922_PHYSICAL_REPLAY'),
    corrections:read('--corrections','USSR_1922_APPROVED_FOLLOWUPS'),
  },originals);
  const directory=resolve(names.get('--report-directory'));
  requireValue(!existsSync(directory),'A historical audit must not overwrite an earlier report');
  mkdirSync(directory,{recursive:true});
  writeFileSync(join(directory,'summary.json'),JSON.stringify(report.json,null,2)+'\n',{flag:'wx'});
  console.log('USSR_1922_COMPACT_REPORT='+JSON.stringify({
    reportDirectory:directory,archivedFiles:originals.length,
    originalZipDifferences:report.json.countries.topologicalDiscrepancies.length,
    unresolvedCanonicalGeometryIssues:report.json.countries.unresolvedCanonicalGeometryIssues,
    libraryUpdated:false,runtimePromoted:false}));
  return report.json;
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url))
  main().catch(error=>{console.error('ussr-1922-report: '+error.message);process.exitCode=1;});
