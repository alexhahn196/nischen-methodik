import json,glob,os
import numpy as np, cv2
from PIL import Image
base='/home/user/nischen-methodik/quiet_physics_analysis/tmp'
sd={x['video_id']:x for x in json.load(open(f'{base}/sample_meta.json'))}
def load(vid):
    d=json.load(open(f'{base}/meta/{vid}.json'))
    f=[x for x in d['formats'] if x.get('format_id')=='sb0'][0]
    tw,th=f['width'],f['height']; frags=f['fragments']
    fr=[];tt=[];t=0.0
    for i,p in enumerate(sorted(glob.glob(f'{base}/sheets/{vid}/*.jpg'))):
        im=Image.open(p).convert('RGB'); W,H=im.size
        cols=max(1,round(W/tw)); rows=max(1,round(H/th)); a=np.asarray(im)
        fd=frags[i]['duration'] if i<len(frags) else frags[-1]['duration']
        per=fd/(rows*cols)
        for r in range(rows):
            for c in range(cols):
                tl=a[r*th:(r+1)*th,c*tw:(c+1)*tw]
                if tl.shape[0]<th//2 or tl.shape[1]<tw//2: continue
                fr.append(tl); tt.append(t); t+=per
    return fr,np.array(tt),d['duration']
out={}
for vid in sd:
    fr,tt,dur=load(vid); N=len(fr)
    A=np.stack([cv2.resize(x,(160,90),interpolation=cv2.INTER_AREA) for x in fr]).astype(np.float32)
    L=(0.2126*A[...,0]+0.7152*A[...,1]+0.0722*A[...,2])
    # ---- letterbox: rows that are near-black in >95% of frames, from the top/bottom inward
    rowmean=L.mean(axis=2)                       # N x 90
    rowdark=(rowmean<8).mean(axis=0)             # fraction of frames where row is black
    top=0
    while top<45 and rowdark[top]>0.95: top+=1
    bot=0
    while bot<45 and rowdark[89-bot]>0.95: bot+=1
    lb_frac=(top+bot)/90.0
    # ---- temporal variance map -> dynamic region mask
    std=L.std(axis=0)                            # 90 x 160
    thr=max(3.0, float(np.percentile(std,55)))
    mask=std>thr
    if mask.mean()<0.05: mask=std>float(np.percentile(std,70))
    dyn_frac=float(mask.mean())
    # ---- lower-third text band: high edge density + high temporal variance, low in the rest
    edge=np.stack([cv2.Canny(cv2.resize(fr[i],(320,180)),80,200) for i in range(N)]).astype(np.float32)/255.
    band=edge[:,int(180*0.72):int(180*0.95),:]   # lower band
    rest=edge[:,int(180*0.08):int(180*0.60),:]
    text_score=float(band.mean()/max(1e-6,rest.mean()))
    band_var=float(band.mean(axis=(1,2)).std())
    band_active=float((band.mean(axis=(1,2))>rest.mean(axis=(1,2))*1.6).mean())
    # ---- masked-region scene detection
    idx=np.where(mask)
    Am=A[:,idx[0],idx[1],:]                      # N x P x 3
    P=Am.shape[1]
    hs=[]
    for i in range(N):
        px=Am[i].reshape(-1,1,3).astype(np.uint8)
        hsv=cv2.cvtColor(px,cv2.COLOR_RGB2HSV)
        h=cv2.calcHist([hsv],[0,1,2],None,[12,6,6],[0,180,0,256,0,256]); cv2.normalize(h,h); hs.append(h)
    hb=np.array([float(cv2.compareHist(hs[i],hs[i+1],cv2.HISTCMP_BHATTACHARYYA)) for i in range(N-1)])
    Gm=Am.mean(axis=2)
    pdm=np.abs(Gm[1:]-Gm[:-1]).mean(axis=1)
    nrm=pdm/max(1e-6,float(np.percentile(np.abs(Gm[1:]-Gm[:-1]),99)))
    # normalized structural diff on full frame with zoom hypotheses (motion-robust)
    G=L
    def cs(x,f):
        h,w=x.shape; ch,cw=int(h*f),int(w*f); y0=(h-ch)//2; x0=(w-cw)//2
        return cv2.resize(x[y0:y0+ch,x0:x0+cw],(w,h),interpolation=cv2.INTER_AREA)
    zd=np.array([min(np.abs(G[i]-G[i+1]).mean(),
                     np.abs(cs(G[i],0.92)-G[i+1]).mean(),
                     np.abs(G[i]-cs(G[i+1],0.92)).mean(),
                     np.abs(cs(G[i],0.85)-G[i+1]).mean(),
                     np.abs(G[i]-cs(G[i+1],0.85)).mean()) for i in range(N-1)])
    zd_n=zd/max(1e-6,float(np.median(L.mean(axis=(1,2)))))   # normalize by scene brightness
    out[vid]=dict(channel=sd[vid]['channel'],classification=sd[vid]['classification'],
        n_frames=N,duration_s=dur,interval_s=round(dur/N,3),
        letterbox_top_rows_of_90=top,letterbox_bottom_rows_of_90=bot,letterbox_frac=round(lb_frac,4),
        dynamic_region_frac=round(dyn_frac,4),
        text_band_edge_ratio=round(text_score,3),text_band_active_frac=round(band_active,3),text_band_var=round(band_var,5),
        hb_masked=hb.round(4).tolist(), pd_masked=pdm.round(3).tolist(),
        zoomdiff_norm=zd_n.round(4).tolist(), times=tt.round(2).tolist())
    print(f"{sd[vid]['channel'][:20]:20} {vid:13} lb={lb_frac*100:4.1f}% dyn={dyn_frac*100:4.1f}% textband={text_score:5.2f} act={band_active:4.2f} hb_med={np.median(hb):.3f}",flush=True)
json.dump(out,open(f'{base}/frame_metrics2.json','w'))
