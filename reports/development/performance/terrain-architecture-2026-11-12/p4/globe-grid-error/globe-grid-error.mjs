// Numerical comparison only: one 512 tile's exact orthographic projection
// versus the Viewer's linearly interpolated grid triangles at 32x.
const rad=Math.PI/180, lon0=102*rad,lat0=28*rad,scale=10570.56;
const X=[-Math.sin(lon0),Math.cos(lon0),0],Y=[Math.sin(lat0)*Math.cos(lon0),Math.sin(lat0)*Math.sin(lon0),-Math.cos(lat0)];
function screen(lon,lat){lon*=rad;lat*=rad;const p=[Math.cos(lat)*Math.cos(lon),Math.cos(lat)*Math.sin(lon),Math.sin(lat)];return [X.reduce((s,x,i)=>s+x*p[i],0)*scale,Y.reduce((s,x,i)=>s+x*p[i],0)*scale];}
const west=66*512/120-180,north=90-14*512/120,span=512/120,step=Math.max(.75,Math.min(8,Math.sqrt(4/scale)*180/Math.PI)),n=Math.ceil(span/step),d=[];
for(let j=0;j<n;j++)for(let i=0;i<n;i++){
  const p=[[0,0],[1,0],[0,1],[1,1]].map(([x,y])=>screen(west+(i+x)*span/n,north-(j+y)*span/n));
  for(let a=0;a<=16;a++)for(let b=0;b<=16;b++){
    const u=a/16,v=b/16,exact=screen(west+(i+u)*span/n,north-(j+v)*span/n);
    const z=u+v<=1?[0,1].map(k=>p[0][k]*(1-u-v)+p[1][k]*u+p[2][k]*v):[0,1].map(k=>p[1][k]*(1-v)+p[2][k]*(1-u)+p[3][k]*(u+v-1));
    d.push(Math.hypot(exact[0]-z[0],exact[1]-z[1]));
  }
}
d.sort((a,b)=>a-b);
console.log(JSON.stringify({schema:'pando-globe-grid-error-v1',tile:[66,14],center:[102,28],scale,step,subdivisions:n,samples:d.length,
  p50Pixels:d[Math.floor((d.length-1)*.5)],p95Pixels:d[Math.floor((d.length-1)*.95)],maxPixels:d.at(-1)},null,2));
