import json,glob,os,sys
import numpy as np
from PIL import Image, ImageDraw
base='/home/user/nischen-methodik/quiet_physics_analysis/tmp'
sd={x['video_id']:x for x in json.load(open(f'{base}/sample_meta.json'))}
os.makedirs(f'{base}/contact',exist_ok=True)
def frames_for(vid):
    d=json.load(open(f'{base}/meta/{vid}.json'))
    f=[x for x in d['formats'] if x.get('format_id')=='sb0'][0]
    tw,th=f['width'],f['height']; frags=f['fragments']
    out=[];t=0.0
    for i,p in enumerate(sorted(glob.glob(f'{base}/sheets/{vid}/*.jpg'))):
        im=Image.open(p).convert('RGB'); W,H=im.size
        cols=max(1,round(W/tw)); rows=max(1,round(H/th)); a=np.asarray(im)
        fd=frags[i]['duration'] if i<len(frags) else frags[-1]['duration']
        per=fd/(rows*cols)
        for r in range(rows):
            for c in range(cols):
                tile=a[r*th:(r+1)*th,c*tw:(c+1)*tw]
                if tile.shape[0]<th//2: continue
                out.append((t,tile)); t+=per
    return out
def sheet(vid,t0,t1,cols=6,scale=1.6,tag=''):
    fr=frames_for(vid)
    sel=[(t,x) for t,x in fr if t0<=t<=t1]
    if not sel: return None
    h,w=sel[0][1].shape[:2]; W=int(w*scale); H=int(h*scale)
    rows=(len(sel)+cols-1)//cols
    canvas=Image.new('RGB',(cols*W, rows*(H+16)),(20,20,20)); dr=ImageDraw.Draw(canvas)
    for i,(t,x) in enumerate(sel):
        r,c=divmod(i,cols)
        canvas.paste(Image.fromarray(x).resize((W,H),Image.LANCZOS),(c*W,r*(H+16)))
        dr.text((c*W+4,r*(H+16)+H+2),f"{int(t//60)}:{int(t%60):02d}",fill=(255,220,120))
    p=f'{base}/contact/{vid}_{tag or int(t0)}.jpg'; canvas.save(p,quality=90); return p
if __name__=='__main__':
    for vid,t0,t1 in [('xXuMfbr0V9o',1800,1980),('gmq4gqCytlY',1800,1980),('YBNfHLlrJkg',1800,1980),
                      ('BA59TWIMNG4',1800,1980),('tvB659d_oik',1800,1980),('lqZntA10Q5g',1800,1980)]:
        print(sheet(vid,t0,t1))

def timeline(vid,n=24,cols=6,scale=1.55):
    import numpy as np
    fr=frames_for(vid)
    if not fr: return None
    T=fr[-1][0]
    picks=[fr[min(len(fr)-1,int(i*(len(fr)-1)/(n-1)))] for i in range(n)]
    h,w=picks[0][1].shape[:2]; W=int(w*scale); H=int(h*scale)
    rows=(n+cols-1)//cols
    canvas=Image.new('RGB',(cols*W,rows*(H+16)),(20,20,20)); dr=ImageDraw.Draw(canvas)
    for i,(t,x) in enumerate(picks):
        r,c=divmod(i,cols)
        canvas.paste(Image.fromarray(x).resize((W,H),Image.LANCZOS),(c*W,r*(H+16)))
        dr.text((c*W+4,r*(H+16)+H+2),f"{int(t//60)}:{int(t%60):02d}",fill=(255,220,120))
    p=f'{base}/contact/TL_{vid}.jpg'; canvas.save(p,quality=90); return p
