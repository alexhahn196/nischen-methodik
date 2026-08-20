import json,glob,statistics as st
import numpy as np
base='/home/user/nischen-methodik/quiet_physics_analysis/tmp'
sm=json.load(open(f'{base}/sample_meta.json'))
sa=json.load(open(f'{base}/scene_analysis.json'))
tm=json.load(open(f'{base}/transcript_metrics.json'))
ss=json.load(open(f'{base}/script_structure.json'))
f2=json.load(open(f'{base}/frame_metrics2.json'))
CH=['Sleep On Physics','Calm Science','Calm Space','Sleepy Science Channel','Cosmo Explains']
CHMETA={'Sleep On Physics':dict(id='UCuKoEFuLJL1Q8HUqXC70RjQ',subs=28100,longform=123,total_views=2922700,uploads_per_week=6.10,handle='@SleepOnPhysics'),
 'Calm Science':dict(id='UCUGv6JOgXVKbGYF57VYTagQ',subs=5720,longform=29,total_views=646594,uploads_per_week=2.89,handle='@CalmScienceToSleep'),
 'Calm Space':dict(id='UCXyJmt3PKv0fbsU9DtcreEw',subs=93900,longform=185,total_views=12919830,uploads_per_week=5.79,handle='@CalmSpaceToSleep'),
 'Sleepy Science Channel':dict(id='UCNZegH5HQPx_chNsPqJw1Rw',subs=328000,longform=290,total_views=33390500,uploads_per_week=4.96,handle='@SleepyScienceChannel'),
 'Cosmo Explains':dict(id='UCIhxIGwGDetnoPGiHfXTsTg',subs=22800,longform=134,total_views=1585678,uploads_per_week=6.77,handle='@CosmoExplainsYT')}
MUSIC={'_nLpB_Ao7zw':61.5,'tvB659d_oik':71.0,'YBNfHLlrJkg':60.3,'BLPBP5BaU-0':77.9,'Nq-wJpo8Hk4':18.0,'LxDfEBostXk':14.8,'-n6HdllViRU':0.0,'lqZntA10Q5g':15.7,'Ty6ZMyFagsU':9.1,'Lgu_Oq8_J5I':15.9,'o2eIwICmo7w':14.8,'xg8ieJQIB70':24.8,'A0vVW7PWnm4':100.0,'BA59TWIMNG4':99.4,'gmq4gqCytlY':0.0,'WHh8Q-gNZAk':0.0,'xXuMfbr0V9o':0.0}
RPM={'BLPBP5BaU-0':(18.21,11.53,24.89),'lqZntA10Q5g':(19.04,11.32,26.76),'o2eIwICmo7w':(14.26,7.50,21.02),'BA59TWIMNG4':(20.10,12.50,27.70)}
def m(xs): return round(float(np.mean(xs)),2)
def md(xs): return round(float(np.median(xs)),2)
per_video={}
for s in sm:
    v=s['video_id']; A=sa[v]; T=tm[v]; S=ss[v]
    per_video[v]=dict(channel=s['channel'],classification=s['classification'],title=s['title'],
      url=s['url'],upload_date=s['upload_date'],duration_s=s['duration_s'],duration_min=s['duration_min'],
      views=s['views'],likes=s['likes'],comments=s['comments'],views_per_day=s['views_per_day'],like_rate_pct=s['like_rate_pct'],
      visual=dict(total_visual_changes=A['total_visual_changes'],changes_per_min=A['changes_per_min'],
        mean_s_per_asset=A['mean_s_per_asset'],assets_per_10min=A['assets_per_10min'],
        est_unique_assets_120min=A['est_unique_assets_120min'],
        asset_duration=A.get('asset_duration_dist'),
        letterbox_pct=A['letterbox_pct_of_height'],aspect=A['aspect_after_letterbox'],
        threshold_sensitivity=A['threshold_sensitivity'],
        time_bands=A['time_bands'],appearance=A['appearance'],motion=A.get('motion_on_held_images')),
      script=dict(n_words=T['n_words'],wpm=T['wpm_over_video'],wpm_curve_per10min=T['wpm_curve_per10min'],
        narration_start_s=T['narration_start_s'],narration_end_s=T['narration_end_s'],
        mean_sentence_words=T['mean_sentence_words'],median_sentence_words=T['median_sentence_words'],
        p90_sentence_words=T['p90_sentence_words'],n_sentences=T['n_sentences'],
        flesch_reading_ease=T['flesch_reading_ease'],flesch_kincaid_grade=T['flesch_kincaid_grade'],
        type_token_ratio=T['type_token_ratio'],unique_words=T['unique_words'],
        n_questions=S['n_questions'],questions_per_hour=S['questions_per_hour'],
        cta_count=S['cta_count'],first_cta_s=S['first_cta_s'],last_cta_s=S['last_cta_s'],
        sleep_mentions=S['sleep_mention_count'],you_per_1000w=S['you_per_1000w'],
        analogy_per_hour=S['analogy_per_hour'],jargon_per_1000w=S['jargon_per_1000w'],
        attention_reset_pct=S['reset_pct'],first_sentence=S['first_5_sentences'][0] if S['first_5_sentences'] else None,
        cta_text=S['cta_hits'][0][1] if S['cta_hits'] else None,
        top_repeated_6grams=S['repeated_6grams'][:4]),
      audio_proxy=dict(music_tag_minute_coverage_pct=MUSIC.get(v),chapters=0),
      rpm=dict(zip(['estimate','min','max'],RPM[v])) if v in RPM else None)
per_channel={}
for ch in CH:
    vs=[v for v,r in per_video.items() if r['channel']==ch]
    R=[per_video[v] for v in vs]
    def g(path):
        out=[]
        for r in R:
            x=r
            for k in path.split('.'):
                x=x.get(k) if isinstance(x,dict) else None
                if x is None: break
            if x is not None: out.append(x)
        return out
    bands={}
    for nm in ['00-10min','10-30min','30-60min','60-90min','90-120min']:
        cs=[b['changes_per_min'] for r in R for b in r['visual']['time_bands'] if b['band']==nm]
        br=[b['brightness_0_255'] for r in R for b in r['visual']['time_bands'] if b['band']==nm]
        ed=[b['edge_density'] for r in R for b in r['visual']['time_bands'] if b['band']==nm]
        if cs: bands[nm]=dict(changes_per_min=m(cs),brightness=m(br),edge_density=round(float(np.mean(ed)),4))
    first=bands.get('00-10min',{}).get('changes_per_min')
    rest=[bands[k]['changes_per_min'] for k in ['30-60min','60-90min','90-120min'] if k in bands]
    per_channel[ch]=dict(**CHMETA[ch],n_sampled=len(R),
      views_per_longform_video=round(CHMETA[ch]['total_views']/CHMETA[ch]['longform']),
      s_per_asset=dict(mean=m(g('visual.mean_s_per_asset')),median=md(g('visual.mean_s_per_asset')),
        min=min(g('visual.mean_s_per_asset')),max=max(g('visual.mean_s_per_asset'))),
      assets_per_120min=dict(mean=round(m(g('visual.est_unique_assets_120min'))),
        min=min(g('visual.est_unique_assets_120min')),max=max(g('visual.est_unique_assets_120min'))),
      changes_per_min=m(g('visual.changes_per_min')),
      letterbox_pct=md(g('visual.letterbox_pct')),
      brightness=m([r['visual']['appearance']['brightness_mean_0_255'] for r in R]),
      saturation=m([r['visual']['appearance']['saturation_mean'] for r in R]),
      contrast=m([r['visual']['appearance']['contrast_mean'] for r in R]),
      dark_pixels_pct=m([r['visual']['appearance']['dark_pixels_pct_mean'] for r in R]),
      near_black_pct=m([r['visual']['appearance']['near_black_pct_mean'] for r in R]),
      colorfulness=m([r['visual']['appearance']['colorfulness_mean'] for r in R]),
      edge_density=round(float(np.mean([r['visual']['appearance']['edge_density_mean'] for r in R])),4),
      rgb=dict(R=m([r['visual']['appearance']['R'] for r in R]),G=m([r['visual']['appearance']['G'] for r in R]),B=m([r['visual']['appearance']['B'] for r in R])),
      blue_minus_red=m([r['visual']['appearance']['blue_dominance_B_minus_R'] for r in R]),
      time_bands=bands,
      front_loading_pct=round(100*(np.mean(rest)/first-1),1) if first and rest else None,
      wpm=dict(mean=m(g('script.wpm')),min=min(g('script.wpm')),max=max(g('script.wpm'))),
      words=dict(mean=round(m(g('script.n_words'))),min=min(g('script.n_words')),max=max(g('script.n_words'))),
      sentence_words=dict(mean=m(g('script.mean_sentence_words')),median=md(g('script.median_sentence_words'))),
      flesch=m(g('script.flesch_reading_ease')),fk_grade=m(g('script.flesch_kincaid_grade')),
      questions_per_hour=m(g('script.questions_per_hour')),
      jargon_per_1000w=m(g('script.jargon_per_1000w')),
      analogy_per_hour=m(g('script.analogy_per_hour')),
      you_per_1000w=m(g('script.you_per_1000w')),
      cta=dict(first_cta_s=[r['script']['first_cta_s'] for r in R],count=[r['script']['cta_count'] for r in R]),
      narration_start_s=m(g('script.narration_start_s')),
      music_tag_coverage_pct=m([r['audio_proxy']['music_tag_minute_coverage_pct'] for r in R]))
out=dict(
  meta=dict(generated='2026-08-20',n_channels=5,n_videos=len(per_video),
    method=dict(
      visual='YouTube storyboard strip (format sb0, 320x180 tiles) fetched with yt-dlp; ~10.0s temporal sampling across the full runtime of every video; 1,502 sheets / ~13,600 frames analysed with OpenCV.',
      scene_detection='Per-video temporal-variance mask isolates the changing image region (handles fixed-frame formats); HSV 12x6x6 histogram Bhattacharyya distance between consecutive samples; "new asset" at distance > 0.40.',
      calibration='Threshold validated against 3 independent ground truths: multimodal shot list (13/13 exact), manual frame inspection of Sleep On Physics median (5/5), manual inspection of Cosmo Explains (10 vs ~11).',
      script='YouTube auto-caption tracks via NexLev, de-overlapped into a timestamped word stream; 17 transcripts, 11,950-22,511 words each.',
      audio='NO direct audio access (media streams auth-gated; not circumvented). Audio evidence is INDIRECT ONLY: caption [Music] annotation coverage, caption-derived WPM, viewer comments. Pitch/LUFS/TTS-vs-human NOT measured.',
      limits=['10s sampling cannot resolve shots shorter than ~10s; the first 60s of the top 3 channels saturates the detector (>=6-7 changes/min) so opening cut rate is a LOWER BOUND.',
              'Multimodal video tool (Gemini) capped at 15 calls/24h; full shot-lists obtained for 2 Sleep On Physics videos only.',
              'No audience-retention data exists for competitor channels; none is inferred.']),
    ),
  per_channel=per_channel, per_video=per_video)
json.dump(out,open('/home/user/nischen-methodik/quiet_physics_analysis/analysis_data.json','w'),indent=1)
print(json.dumps(per_channel,indent=1)[:60])
for ch in CH:
    c=per_channel[ch]
    print(f"{ch:24} subs={c['subs']:7} v/vid={c['views_per_longform_video']:7} up/wk={c['uploads_per_week']:4.1f} s/ast={c['s_per_asset']['mean']:5.1f} assets120={c['assets_per_120min']['mean']:4} lb={c['letterbox_pct']:4.1f}% bright={c['brightness']:5.1f} sat={c['saturation']:.3f} dark={c['dark_pixels_pct']:5.1f}% wpm={c['wpm']['mean']:5.1f} FK={c['fk_grade']:4.1f} jarg={c['jargon_per_1000w']:5.1f} Q/h={c['questions_per_hour']:5.1f} music={c['music_tag_coverage_pct']:5.1f}% front={c['front_loading_pct']}")
