import json,os,glob,math,sys
import numpy as np
from PIL import Image
import cv2
base='/home/user/nischen-methodik/quiet_physics_analysis/tmp'
sd=json.load(open(f'{base}/sample_meta.json'))
os.makedirs(f'{base}/keyframes',exist_ok=True)
TARGETS=[0,10,30,60,120,300,600,900,1800,2700,3600,4500,5400,6300,7200]
results={}
for s in sd:
    vid=s['video_id']; dur=s['duration_s']
    d=json.load(open(f'{base}/meta/{vid}.json'))
    f=[x for x in d['formats'] if x.get('format_id')=='sb0'][0]
    tw,th=f['width'],f['height']; frags=f['fragments']
    sheets=sorted(glob.glob(f'{base}/sheets/{vid}/*.jpg'))
    frames=[]; times=[]; t=0.0
    for i,p in enumerate(sheets):
        im=Image.open(p).convert('RGB'); W,H=im.size
        cols=max(1,round(W/tw)); rows=max(1,round(H/th))
        a=np.asarray(im)
        fd=frags[i]['duration'] if i<len(frags) else frags[-1]['duration']
        per=fd/(rows*cols)
        for r in range(rows):
            for c in range(cols):
                tile=a[r*th:(r+1)*th, c*tw:(c+1)*tw]
                if tile.shape[0]<th//2 or tile.shape[1]<tw//2: continue
                frames.append(tile); times.append(t); t+=per
    N=len(frames)
    F=np.stack([cv2.resize(x,(160,90),interpolation=cv2.INTER_AREA) for x in frames]).astype(np.float32)
    G=F.mean(axis=3)
    # ---- per-frame appearance metrics
    lum = 0.2126*F[...,0]+0.7152*F[...,1]+0.0722*F[...,2]
    bright = lum.reshape(N,-1).mean(1)
    contrast = lum.reshape(N,-1).std(1)
    dark_frac = (lum.reshape(N,-1)<32).mean(1)
    verydark_frac = (lum.reshape(N,-1)<16).mean(1)
    mx=F.max(3); mn=F.min(3)
    sat = np.where(mx>0,(mx-mn)/np.maximum(mx,1e-6),0).reshape(N,-1).mean(1)
    Rm=F[...,0].reshape(N,-1).mean(1); Gm=F[...,1].reshape(N,-1).mean(1); Bm=F[...,2].reshape(N,-1).mean(1)
    warm = Rm-Bm
    # colorfulness (Hasler-Susstrunk)
    rg=np.abs(F[...,0]-F[...,1]).reshape(N,-1); yb=np.abs(0.5*(F[...,0]+F[...,1])-F[...,2]).reshape(N,-1)
    colorfulness = np.sqrt(rg.std(1)**2+yb.std(1)**2)+0.3*np.sqrt(rg.mean(1)**2+yb.mean(1)**2)
    # edge density (proxy for detail / text / diagrams)
    edges=np.array([cv2.Canny(cv2.resize(frames[i],(320,180)),60,160).mean()/255 for i in range(N)])
    # ---- pairwise difference metrics
    hists=[]
    for i in range(N):
        h=cv2.calcHist([cv2.cvtColor(frames[i],cv2.COLOR_RGB2HSV)],[0,1,2],None,[16,8,8],[0,180,0,256,0,256])
        cv2.normalize(h,h); hists.append(h.flatten())
    hists=np.stack(hists)
    hcorr=np.array([float(cv2.compareHist(hists[i].reshape(16,8,8),hists[i+1].reshape(16,8,8),cv2.HISTCMP_CORREL)) for i in range(N-1)])
    hbhat=np.array([float(cv2.compareHist(hists[i].reshape(16,8,8),hists[i+1].reshape(16,8,8),cv2.HISTCMP_BHATTACHARYYA)) for i in range(N-1)])
    pixdiff=np.abs(G[1:]-G[:-1]).reshape(N-1,-1).mean(1)
    # zoom-robust: compare center-cropped-and-rescaled next frame to current (approximates a zoom)
    def crop_scale(x,f=0.90):
        h,w=x.shape[:2]; ch,cw=int(h*f),int(w*f); y0=(h-ch)//2; x0=(w-cw)//2
        return cv2.resize(x[y0:y0+ch,x0:x0+cw],(w,h),interpolation=cv2.INTER_AREA)
    zoomdiff=[]
    for i in range(N-1):
        a0=G[i]; b0=G[i+1]
        cands=[np.abs(a0-b0).mean(),
               np.abs(crop_scale(a0)-b0).mean(),
               np.abs(a0-crop_scale(b0)).mean()]
        zoomdiff.append(min(cands))
    zoomdiff=np.array(zoomdiff)
    results[vid]=dict(
        channel=s['channel'],classification=s['classification'],title=s['title'],duration_s=dur,
        n_frames=N, interval_s=round(dur/N,3), times=[round(x,2) for x in times],
        bright=bright.round(3).tolist(), contrast=contrast.round(3).tolist(),
        dark_frac=dark_frac.round(4).tolist(), verydark_frac=verydark_frac.round(4).tolist(),
        sat=sat.round(4).tolist(), R=Rm.round(2).tolist(), G=Gm.round(2).tolist(), B=Bm.round(2).tolist(),
        warm=warm.round(3).tolist(), colorfulness=colorfulness.round(3).tolist(), edges=edges.round(5).tolist(),
        hcorr=hcorr.round(5).tolist(), hbhat=hbhat.round(5).tolist(),
        pixdiff=pixdiff.round(4).tolist(), zoomdiff=zoomdiff.round(4).tolist())
    # save keyframes at target timestamps
    kd=f'{base}/keyframes/{vid}'; os.makedirs(kd,exist_ok=True)
    tarr=np.array(times)
    for T in TARGETS:
        if T>dur-5: continue
        i=int(np.argmin(np.abs(tarr-T)))
        Image.fromarray(frames[i]).resize((tw*2,th*2),Image.LANCZOS).save(f'{kd}/t{T:05d}.jpg',quality=92)
    print(f"{vid} N={N} int={dur/N:.2f}s bright={bright.mean():.1f} sat={sat.mean():.3f} hcorr_med={np.median(hcorr):.3f}",flush=True)
json.dump(results,open(f'{base}/frame_metrics.json','w'))
print("saved frame_metrics.json", os.path.getsize(f'{base}/frame_metrics.json'))
