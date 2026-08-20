import json,glob,re,os,statistics as st
import numpy as np
base='/home/user/nischen-methodik/quiet_physics_analysis/tmp'
sd={x['video_id']:x for x in json.load(open(f'{base}/sample_meta.json'))}
out={}
for p in sorted(glob.glob(f'{base}/transcripts/*.json')):
    d=json.load(open(p)); vid=d['videoId']; tr=d['transcript']
    if vid not in sd: continue
    dur=sd[vid]['duration_s']
    segs=[]
    for s in tr:
        a=int(s['startMs'])/1000.0; b=int(s['endMs'])/1000.0
        segs.append((a,b,s['text'].strip()))
    segs.sort(key=lambda x:x[0])
    # YouTube auto-captions overlap; dedupe text by reconstructing the rolling stream
    words=[]
    for a,b,t in segs:
        for w in t.split():
            words.append((a,w))
    # de-overlap: auto captions repeat lines; rebuild unique word stream using start-time monotonic + text dedupe
    txt_parts=[]; last_end=-1
    for a,b,t in segs:
        if a>=last_end-0.01:
            txt_parts.append((a,b,t)); last_end=b
    full=' '.join(t for _,_,t in segs)
    # Better: auto-caption rolling windows duplicate ~50%. Use the "new tail" heuristic.
    stream=[]
    prev=''
    for a,b,t in segs:
        tw=t.split()
        if not stream: stream.extend((a,w) for w in tw); prev=t; continue
        # find overlap between end of accumulated and start of tw
        acc=[w for _,w in stream]
        mx=0
        for k in range(min(len(tw),12),0,-1):
            if acc[-k:]==tw[:k]: mx=k; break
        stream.extend((a,w) for w in tw[mx:])
    n_words=len(stream)
    text=' '.join(w for _,w in stream)
    # timing
    t_first=segs[0][0]; t_last=segs[-1][1]
    speak_span=t_last-t_first
    wpm_span=n_words/(speak_span/60)
    wpm_video=n_words/(dur/60)
    # gaps between caption segments = pause proxy
    gaps=[]
    for i in range(len(txt_parts)-1):
        g=txt_parts[i+1][0]-txt_parts[i][1]
        if g>0: gaps.append(g)
    # sentence stats
    sents=[s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    slen=[len(s.split()) for s in sents if len(s.split())>1]
    q=[s for s in sents if s.strip().endswith('?')]
    # vocab
    wl=[len(w) for w in re.findall(r"[A-Za-z']+", text)]
    uniq=len(set(w.lower() for w in re.findall(r"[A-Za-z']+", text)))
    # readability (Flesch)
    def syl(w):
        w=w.lower(); v='aeiouy'; c=0; prev=False
        for ch in w:
            isv=ch in v
            if isv and not prev: c+=1
            prev=isv
        if w.endswith('e') and c>1: c-=1
        return max(1,c)
    ws=re.findall(r"[A-Za-z']+", text)
    syls=sum(syl(w) for w in ws)
    nsent=max(1,len(sents))
    flesch=206.835-1.015*(len(ws)/nsent)-84.6*(syls/max(1,len(ws)))
    fk=0.39*(len(ws)/nsent)+11.8*(syls/max(1,len(ws)))-15.59
    # per-10-min WPM curve
    curve=[]
    for k in range(0,int(dur),600):
        c=sum(1 for a,w in stream if k<=a<k+600)
        curve.append(round(c/10.0,1))
    # rhetorical markers
    low=text.lower()
    markers={k:low.count(k) for k in ['imagine','but here','the answer','what if','notice','in other words','picture','think of','consider','that is why','which means','and yet','the strange','the surprising','no one knows','we do not know',"we don't know"]}
    subscribe = sum(low.count(k) for k in ['subscribe','like this video','hit the bell','comment below','let me know'])
    sleepmention = sum(low.count(k) for k in ['fall asleep','drift off','sleep well','good night','goodnight','close your eyes','as you sleep','tonight','while you sleep'])
    out[vid]=dict(channel=sd[vid]['channel'],classification=sd[vid]['classification'],title=sd[vid]['title'],
        duration_s=dur,n_words=n_words,n_caption_segments=len(segs),
        wpm_over_video=round(wpm_video,1),wpm_over_speaking_span=round(wpm_span,1),
        narration_start_s=round(t_first,2),narration_end_s=round(t_last,2),
        tail_silence_s=round(dur-t_last,1),
        n_sentences=len(sents),mean_sentence_words=round(st.mean(slen),2) if slen else None,
        median_sentence_words=round(st.median(slen),1) if slen else None,
        p90_sentence_words=round(float(np.percentile(slen,90)),1) if slen else None,
        n_questions=len(q),questions_per_1000w=round(1000*len(q)/max(1,n_words),2),
        questions_per_hour=round(len(q)/(dur/3600),1),
        mean_word_len=round(st.mean(wl),2),unique_words=uniq,type_token_ratio=round(uniq/max(1,n_words),4),
        flesch_reading_ease=round(flesch,1),flesch_kincaid_grade=round(fk,1),
        gap_median_s=round(st.median(gaps),2) if gaps else None,
        gap_p90_s=round(float(np.percentile(gaps,90)),2) if gaps else None,
        gaps_gt_1s=sum(1 for g in gaps if g>1.0),
        wpm_curve_per10min=curve,
        markers=markers,subscribe_mentions=subscribe,sleep_mentions=sleepmention,
        first_300_chars=text[:300])
    print(f"{sd[vid]['channel'][:20]:20} {vid:12} words={n_words:6} wpm={wpm_video:5.1f} sent={len(sents):5} mslen={st.mean(slen):4.1f} q={len(q):4} flesch={flesch:5.1f} FK={fk:4.1f} start={t_first:.1f}s",flush=True)
json.dump(out,open(f'{base}/transcript_metrics.json','w'),indent=1)
