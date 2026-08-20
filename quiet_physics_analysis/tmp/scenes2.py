import json,numpy as np
base='/home/user/nischen-methodik/quiet_physics_analysis/tmp'
f2=json.load(open(f'{base}/frame_metrics2.json'))
f1=json.load(open(f'{base}/frame_metrics.json'))
sd={x['video_id']:x for x in json.load(open(f'{base}/sample_meta.json'))}
THRS=[0.30,0.40,0.50,0.60]
PRIMARY=0.40
BANDS=[(0,600,'00-10min'),(600,1800,'10-30min'),(1800,3600,'30-60min'),(3600,5400,'60-90min'),(5400,7200,'90-120min'),(7200,99999,'120min+')]
out={}
for vid,d in f2.items():
    t=np.array(d['times']); hb=np.nan_to_num(np.array(d['hb_masked']),nan=0.0)
    dur=d['duration_s']; N=d['n_frames']; T=dur/N
    a1=f1[vid]
    r={'video_id':vid,'channel':d['channel'],'classification':d['classification'],'title':sd[vid]['title'],
       'duration_s':dur,'views':sd[vid]['views'],'upload_date':sd[vid]['upload_date'],
       'n_storyboard_frames':N,'sample_interval_s':round(T,3),
       'letterbox_pct_of_height':round(d['letterbox_frac']*100,1),
       'aspect_after_letterbox':round(16/9/(1-d['letterbox_frac']),2),
       'threshold_sensitivity':{}}
    for th in THRS:
        c=hb>th; n=int(c.sum())
        r['threshold_sensitivity'][f'{th:.2f}']={'changes':n,'changes_per_min':round(n/(dur/60),2),'s_per_asset':round(dur/max(1,n),1)}
    c=hb>PRIMARY; idx=np.where(c)[0]; n=int(c.sum())
    r['primary_threshold']=PRIMARY
    r['total_visual_changes']=n
    r['changes_per_min']=round(n/(dur/60),2)
    r['mean_s_per_asset']=round(dur/max(1,n),1)
    r['assets_per_10min']=round(n/(dur/600),1)
    r['est_unique_assets_120min']=int(round(n/(dur/7200)))
    if len(idx)>2:
        g=np.diff(t[idx+1])
        r['asset_duration_dist']={'median_s':round(float(np.median(g)),1),'mean_s':round(float(g.mean()),1),
          'p10_s':round(float(np.percentile(g,10)),1),'p25_s':round(float(np.percentile(g,25)),1),
          'p75_s':round(float(np.percentile(g,75)),1),'p90_s':round(float(np.percentile(g,90)),1),
          'max_s':round(float(g.max()),1),'pct_shots_over_30s':round(float((g>30).mean()*100),1),
          'pct_shots_over_60s':round(float((g>60).mean()*100),1)}
    bands=[]
    for a,b,nm in BANDS:
        m=(t[:-1]>=a)&(t[:-1]<b)
        if m.sum()<3: continue
        span=min(b,dur)-a; nc=int(c[m].sum())
        sl=slice(None)
        bands.append({'band':nm,'changes':nc,'changes_per_min':round(nc/(span/60),2),
          's_per_asset':round(span/max(1,nc),1),
          'brightness_0_255':round(float(np.array(a1['bright'])[:-1][m].mean()),1),
          'saturation':round(float(np.array(a1['sat'])[:-1][m].mean()),3),
          'contrast':round(float(np.array(a1['contrast'])[:-1][m].mean()),1),
          'dark_pixels_pct':round(float(np.array(a1['dark_frac'])[:-1][m].mean()*100),1),
          'near_black_pct':round(float(np.array(a1['verydark_frac'])[:-1][m].mean()*100),1),
          'colorfulness':round(float(np.array(a1['colorfulness'])[:-1][m].mean()),1),
          'edge_density':round(float(np.array(a1['edges'])[:-1][m].mean()),4),
          'warm_R_minus_B':round(float(np.array(a1['warm'])[:-1][m].mean()),1)})
    r['time_bands']=bands
    # motion proxy on same-asset pairs
    same=~c
    pd=np.array(d['pd_masked']); zn=np.array(d['zoomdiff_norm'])
    if same.sum()>5:
        r['motion_on_held_images']={'held_pairs':int(same.sum()),
          'median_masked_pixel_change':round(float(np.median(pd[same])),2),
          'pct_held_pairs_essentially_static':round(float((pd[same]<1.5).mean()*100),1),
          'median_zoom_normalized_residual':round(float(np.median(zn[same])),4)}
    ap=a1
    r['appearance']={'brightness_mean_0_255':round(float(np.mean(ap['bright'])),1),
      'brightness_median':round(float(np.median(ap['bright'])),1),
      'saturation_mean':round(float(np.mean(ap['sat'])),3),
      'contrast_mean':round(float(np.mean(ap['contrast'])),1),
      'dark_pixels_pct_mean':round(float(np.mean(ap['dark_frac'])*100),1),
      'near_black_pct_mean':round(float(np.mean(ap['verydark_frac'])*100),1),
      'colorfulness_mean':round(float(np.mean(ap['colorfulness'])),1),
      'edge_density_mean':round(float(np.mean(ap['edges'])),4),
      'R':round(float(np.mean(ap['R'])),1),'G':round(float(np.mean(ap['G'])),1),'B':round(float(np.mean(ap['B'])),1),
      'warm_R_minus_B':round(float(np.mean(ap['warm'])),1),
      'blue_dominance_B_minus_R':round(float(np.mean(ap['B'])-np.mean(ap['R'])),1)}
    out[vid]=r
json.dump(out,open(f'{base}/scene_analysis.json','w'),indent=1)
order=['Sleep On Physics','Calm Science','Calm Space','Sleepy Science Channel','Cosmo Explains']
print(f"{'channel':22} {'vid':13} {'cls':19} {'chg':>4} {'s/ast':>6} {'/10min':>7} {'120m':>5} {'med':>5} {'p90':>5} {'lb%':>5} {'bright':>6} {'sat':>5} {'dark%':>6}")
for vid,r in sorted(out.items(),key=lambda kv:(order.index(kv[1]['channel']),kv[1]['classification'])):
    ad=r.get('asset_duration_dist',{})
    print(f"{r['channel'][:22]:22} {vid:13} {r['classification'][:19]:19} {r['total_visual_changes']:4} {r['mean_s_per_asset']:6.1f} {r['assets_per_10min']:7.1f} {r['est_unique_assets_120min']:5} {ad.get('median_s',0):5.1f} {ad.get('p90_s',0):5.1f} {r['letterbox_pct_of_height']:5.1f} {r['appearance']['brightness_mean_0_255']:6.1f} {r['appearance']['saturation_mean']:5.3f} {r['appearance']['dark_pixels_pct_mean']:6.1f}")
